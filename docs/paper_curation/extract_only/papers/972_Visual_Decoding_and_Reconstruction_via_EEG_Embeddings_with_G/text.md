# arXiv:2403.07721v7[cs.HC]4Oct2024

## Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion

###### Dongyang Li1∗ Chen Wei1∗ Shiying Li1 Jiachen Zou1 Haoyang Qin1 Quanying Liu1†

1Department of Biomedical Engineering, Southern University of Science and Technology, Shenzhen, China {lidy2023, weic3}@mail.sustech.edu.cn liuqy@sustech.edu.cn

Visual Perception Sequence Brain Encoding Seen Images

...

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

|Relax|＋|
|---|---|

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

...

Rest ＋ Visual Visual t1 t2 t3 t3

Our Reconstructed Images Decode

| | |[Figure 13]| | |
|---|---|---|---|---|
|[Figure 14]|[Figure 15]|[Figure 16]<br><br>[Figure 17]|[Figure 18]|[Figure 19]|
| | |[Figure 20]| | |

Classification Retrieval Generation

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

...

|[Figure 27]|[Figure 28]|[Figure 29]<br><br>[Figure 30]|[Figure 31]|[Figure 32]|
|---|---|---|---|---|
|[Figure 33]|[Figure 34]|[Figure 35]| |[Figure 36]|

Brain Embedding

Figure 1: EEG/MEG-based zero-shot brain decoding and reconstruction. Left: Overview of three visual decoding tasks using EEG/MEG data under natural image stimulus. Right: Our reconstruction examples.

###### Abstract

How to decode human vision through neural signals has attracted a long-standing interest in neuroscience and machine learning. Modern contrastive learning and generative models improved the performance of visual decoding and reconstruction based on functional Magnetic Resonance Imaging (fMRI). However, the high cost and low temporal resolution of fMRI limit their applications in brain-computer interfaces (BCIs), prompting a high need for visual decoding based on electroencephalography (EEG). In this study, we present an end-to-end EEG-based visual reconstruction zero-shot framework, consisting of a tailored brain encoder, called the Adaptive Thinking Mapper (ATM), which projects neural signals from different sources into the shared subspace as the clip embedding, and a two-stage multi-pipe EEG-to-image generation strategy. In stage one, EEG is embedded to align the highlevel clip embedding, and then the prior diffusion model refines EEG embedding into image priors. A blurry image also decoded from EEG for maintaining the lowlevel feature. In stage two, we input both the high-level clip embedding, the blurry image and caption from EEG latent to a pre-trained diffusion model. Furthermore, we analyzed the impacts of different time windows and brain regions on decoding and reconstruction. The versatility of our framework is demonstrated in the magnetoencephalogram (MEG) data modality. The experimental results indicate that our EEG-based visual zero-shot framework achieves SOTA performance in classification, retrieval and reconstruction, highlighting the portability, low cost, and high temporal resolution of EEG, enabling a wide range of BCI applications. Our code is available at https://github.com/ncclab-sustech/EEG_Image_decode.

∗D. Li and C. Wei contributed equally. †Corresponding author.

Preprint. Under review.

###### 1 Introduction

A key technical challenge in BCIs is to decode/reconstruct the visual world seen by humans through non-invasive brain recordings, such as fMRI, MEG or EEG. These highly dynamic brain activities reflect human perception of the visual world, which is influenced by properties of the external visual stimulus, our internal states, emotions and even personal experiences. Thus, visual decoding and reconstruction based on neural signals can uncover how the human brain processes and interprets natural visual stimulus, as well as promote non-invasive BCI applications.

Contrastive learning and generative models have greatly advanced fMRI-based visual decoding in both decoding tasks (e.g., image classification and retrieval) and generative tasks (e.g., image reconstruction). By combining pre-trained visual models, existing fMRI decoding models can learn highly-refined feature embeddings in limited data [29, 42]. Using these embedded fMRI features, generative models such as diffusion models can reconstruct the image one is seeing [42, 12]. However, despite many advances in fMRI-based visual decoding, fMRI equipment is unportable, expensive, and difficult to operate, largely limiting its application in BCIs. Alternatively, EEG is portable, cheap, and universal, facilitating a wide range of BCI applications. EEG has higher temporal resolution and can effectively capture rapid changes in brain activity when processing complex, dynamic visual stimulus.

EEG has long been considered incomparable to fMRI in natural image decoding/reconstruction tasks,

- as EEG suffers from low signal-to-noise ratio, low spatial resolution, and large inter-subject variability. Recent advances in multimodal alignment have made MEG/EEG visual decoding possible, although the performance is still inferior to fMRI [8, 46, 17]. Yohann Benchetrit et al. used the CLIP model to extract the latent representation of the image and trained the MEG encoder to align it with the image representation extracted by CLIP. It achieved excellent retrieval and reconstruction performance on MEG and fMRI datasets, demonstrating the potential for real-time visual decoding and reconstruction using EEG/MEG signals. Recently, Song et al. [46] used an EEG encoder based on ShallowNet [39] and performed representation alignment through contrastive learning, achieving excellent decoding performance on the THING-EEG dataset [15]. These two studies provide preliminary evidence of the potential of EEG/MEG-based visual decoding. However, there is a significant gap in their performance compared to the fMRI-level performance. This gap is largely caused by the fact that the framework of EEG visual decoding and reconstruction have not yet been thoroughly explored.

To fill this gap, we have developed a visual decoding framework based on EEG/MEG, including a novel EEG encoder and a two-stage image generation strategy. Our work has three main contributions:

- 1. We present brain decoding framework, which is the first work allows zero-shot image classification, retrieval, and reconstruction via EEG data. Experimental results demonstrate that our framework is applicable to various common EEG encoder architectures.
- 2. By extensively studying the existing EEG encoder modules, we construct a tailored EEG encoder ATM, which achieves state-of-the-art performance in three downstream visual decoding tasks.
- 3. We report a two-stage EEG-to-image generation strategy, which separately extracts highlevel and low-level visual features from EEG and refining these features with an additional lightweight prior diffusion model, enabling reliable reconstruction of images using less than 500ms EEG.

###### 2 Method

To learn high-quality latent representations of EEG data, it is crucial to consider the spatial position of EEG channels and the Temporal-Spatial properties of EEG signals. Let T represent the length of the time window of the data, C the number of EEG channels, and N the total number of data samples. Our objective is to derive EEG embeddings ZE = f(E) ∈ RN×F from the brain activity data E ∈ RN×C×T, where f is the EEG encoder and F is the projection dimension of the embeddings. Concurrently, we use the CLIP model to extract image embeddings ZI ∈ RN×F from images I. Our goal is to effectively align the EEG representation with the image representation, as illustrated in Fig. 2. In the training phase, the EEG encoder is trained with EEG and image pairs using a contrastive learning framework. In the inference phase, the EEG embeddings from the trained EEG projector

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

Image Embedding

###### X Contrastive Learning Trainable Frozen

Visual stimulus Training

Image Dataset

[Figure 41]

|[Figure 42]<br><br>[Figure 43]<br><br>…<br><br>antelope pear<br><br>|antelope|
|---|
<br><br>kettle sausage …<br><br>|
|---|

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

CLIP Image

[Figure 50]

Classification

[Figure 51]

zero-shot

[Figure 52]

###### X

EEG Embedding

[Figure 53]

[Figure 54]

[Figure 55]

Retrieval

[Figure 56]

EEG Encoder

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

Generatilon

[Figure 62]

[Figure 63]

Reconstruction

[Figure 64]

MSE Loss

EEG Embedding EEG Encoder

[Figure 65]

[Figure 66]

[Figure 67]

IPAdapter

[Figure 68]

[Figure 69]

EEG series

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

low level

VAE image encoder

VAE image decoder

[Figure 75]

+ SDXLturbo

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

high level

VAE Latent

EEG Embedding

Image Embedding

×T

###### Inference EEG

[Figure 81]

[Figure 82]

Noise

Embedding

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

|“A bunch of colorful, dense fudge.”|
|---|

|[Figure 87]|
|---|

[Figure 88]

| |
|---|

EEG Encoder

GIT model img2text

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

Diffusion U-Net

[Figure 94]

[Figure 95]

Semantic level

- Figure 2: EEG/MEG-based visual decoding and generation framework. The EEG encoder is designed as a flexible replacement component. After aligning with image features, the EEG features are used for zero-shot retrieval and classification tasks, and the reconstructed images are obtained through a two-stage generator.

can be used for a variety of zero-shot tasks, including EEG-based image classification, retrieval, and image reconstruction.

###### 2.1 ATM for EEG Embedding

Inspired by advanced time series models [28, 13], we develop an EEG encoder called ATM, for aligning the original EEG signals to its feature representation space (Fig. 3). ATM is based on the channel-wise Transformer encoder, Temporal-Spatial convolution and multilayer perceptron (MLP) architecture. In contrast to other conventional practices, the original EEG does not need to be segmented, and each sequence acts as a patch. After sinusoidal position embedding, these patches are processed through a channel-attention module to integrate the information of different series. Subsequently, through the Temporal-Spatial aggregation, we project the output with a MLP to get rational shape representations. The Temporal-Spatial convolution module is an effective way to represent EEG data with a small number of parameters [46], prevent overfitting in training. The difference is our components is plug-and-play and can be flexibly replaced with different types of Temporal-Spatial convolution components as needed to adapt to various EEG/MEG datasets. Finally, MLP projectior consists of M simple residual components and fully connected layers, with LayerNorm applied in the output to ensure the stability of training. In addition to entering the original series, we provide an identification input for a known subject and can specifically use this token for downstream tasks. For unknown subjects, we use shared tokens or average all tokens equally directly into the MLP projector.

###### 2.2 Image Embedding

Many previous studies have explored various training strategies to train deep neural networks for image embedding, such as VGG-19 and ResNet trained with supervised learning, CLIP, DINO trained with contrastive learning, and VAEs with self-supervised learning [50, 4, 46, 17]. They have reported that DINO and CLIP models pre-trained using the Vision Transformer (ViT) architecture perform better in a range of downstream tasks, including image decoding and reconstruction, compared to models trained using supervised learning methods (such as VGG, ResNet) and self-supervised VAE frameworks. Thus, in this study, we use CLIP for image embedding, denoted as ZI ∈ RN×1024,

푞￿

Add & LayNorm

Flatten

Embedding MLP Projectior

푧￿

Temporal Spatial Aggregation

Linear Projection

Temporal Spatial Conv Module

ELU

푝￿

GELU

###### L ×

Channel-wise Attention Layer

CNN & Norm

푁 ∗

Linear Projection

mbedding

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

Input Embedding

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

...

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

E

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

Variate

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

Sequence Tokens

[Figure 2041]

[Figure 2042]

[Figure 2043]

[Figure 2044]

푠￿=?

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

|Embedding Layer<br><br>[Figure 2098]<br><br>[Figure 2099]| | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

[Figure 2100]

[Figure 2101]

[Figure 2102]

[Figure 2103]

Subject Tokens

|[Figure 2104]|
|---|

[Figure 2105]

[Figure 2106]

[Figure 2107]

[Figure 2108]

Shared Token

푥￿

|[Figure 2109]|
|---|

[Figure 2110]

[Figure 2111]

|[Figure 2112]|
|---|

|[Figure 2113]|
|---|

FPz FP1 ... O2 Oz P7

푠￿=1,2..

- Figure 3: The structure of ATM. The original EEG sequences of different variates are independently embedded into tokens. Channel-wise attention is applied to embedded variate tokens with enhanced interpretability revealing electrode correlations. And representations of each token are extracted by the shared feedforward network (FFN). Then Temporal-Spatial convolution can prevent overfitting and enhance the ability of Temporal-Spatial modeling.

instead of ZI ∈ RN×257×768, with the EEG embeddings. Before formal training, all images undergo the standard preprocessing procedure [36].

###### 2.3 EEG Guidance Image Generation

In this study, we present a two-stage pipeline for generating images that serve as visual stimulus for EEG recordings, as shown in the bottom right of Fig. 2. In the left of Fig. 3 we have obtained the EEG embeddings zE for each image by the EEG encoder ATM. Now our goal is to use these EEG embeddings to generate the corresponding images. The joint distribution of images, EEG embeddings, and image embeddings can be expressed as p(I,zE,zI) = p(zI|zE)p(I|zI), corresponding to the prior diffusion and CLIP-guided generation, respectively. In Stage I, we first focus on the prior diffusion stage. Inspired by DALL-E 2 [37] and Mind’s Eyes [42], we train a diffusion model conditioned on the EEG embeddings ZˆE to learn the distribution of CLIP embeddings p(zI|zE). In this stage, we construct a lightweight U-Net: ϵprior(zIt,t,zE), where zIt represents the noisy CLIP embedding at diffusion time step t. We train the prior diffusion model using EEG and CLIP embeddings. Through this diffusion model, we can generate corresponding CLIP embeddings zI from EEG embeddings as a prior for stage II. In Stage II, we employ the pre-trained SDXL [35] and IP-Adapter [62] models to model the generator p(I|zI), thereby sampling image I according to zI. In addition, we introduce the low-level features here using img2img[31]. Further details are provided in Appendix C.

###### 2.4 Loss Function

Following the methodology outlined by Benchetrit et al. [4], we adopt a dual approach to loss functions, serving distinct objectives. For the classification and retrieval tasks, we only utilize the CLIP loss, which is inspired by the contrastive learning approach described in Radford et al. [36]. This loss function aids in aligning the EEG data E with corresponding image data I, thereby facilitating the identification of EEG-image pairs and maximizing the boundaries of EEG representations. For the generation tasks, besides the CLIP loss, we add a Mean Squared Error (MSE) loss to facilitate consistency learning in regression. Thus the overall loss function for our model is a combination of these two distinct loss types, expressed as:

Loss = λ · LCLIP + (1 − λ) · LMSE

Here, λ is a hyperparameter that balances the contribution of each loss type.

Classification

Classification

Classification

Classification

(Across Subject top-5)

(Across Subject top-1)

(Across Subject top-5)

(Across Subject top-1)

[Figure 2114]

[Figure 2115]

Retrieval

Classification

Retrieval

Classification

(In Subject top-1)

(In Subject top-5)

(In Subject top-1)

(In Subject top-5)

[Figure 2116]

Retrieval

Classification

Retrieval

Classification

[Figure 2117]

(In Subject top-5)

(In Subject top-1)

(In Subject top-5)

(In Subject top-1)

[Figure 2118]

Retrieval

Generation

Retrieval

Generation

(Across Subject top-1)

(top-5)

(Across Subject top-1)

(top-5)

[Figure 2119]

Generation

Generation

Retrieval

Retrieval

(top-1)

(top-1)

(Across Subject top-5)

(Across Subject top-5)

|[Figure 2120]<br><br>ATM-S (Ours) Conformer EEGNetV4<br><br>B.D. NICE<br><br>MLP ShallowFBCPNet|
|---|

|[Figure 2121]<br><br>[Figure 2122]<br><br>ATCNet<br><br>ATM-S (Ours)<br><br>Conformer<br><br>EEGITNet EEGNetV4<br><br>B.D. NICE<br><br>MLP ShallowFBCPNet|
|---|

- Figure 4: EEG/MEG-based decoding and reconstruction performance. Left: Comparisons of nine encoders on the THINGS-EEG dataset, including within-subject and cross-subject performance. Right: Comparisons on the THINGS-MEG dataset, similar to left. Our method achieves the highest performance compared to other competing encoders in EEG/MEG-based visual decoding tasks.

###### 3 Experiments

###### 3.1 Training and Computational Considerations

We conducted our experiments on the THINGS-EEG dataset’s training set [15, 17]. To verify the versatility of ATM for embedding electrophysiological data, we tested it on MEG data modality using the THINGS-MEG dataset [19]. All experiments can be completed in a single NVIDIA RTX 4090 GPU. We used the Adam optimizer [25] to train the across-subject model on a set of approximately 496,200 samples, and the within-subject model on a set of about 66,160 samples, with an initial learning rate of 3 × 10−4 and batch sizes of 16 and 1024. Our initial temperature parameter was set to 0.07. We tested on the zero-shot test dataset at the end of each training epoch during the training process. For fairness, all models’ hyperparameters were kept consistent. In our study, we compared the performance of different encoders on the within-subject test set and cross-subject (leave-one-subject-out) test set (see Appendix H).

###### 3.2 EEG Decoding Performance

Our method obtains the EEG embedding for the classification task. We output the category of EEG with the highest cosine similarity with text embeddings(Fig. 5a). Fig. 5c presents the average accuracy across different methods in the subjects, and shows that our method outperforms others. More details of the EEG-based image classification are in Appendix B.

In Fig. 5, we test the effectiveness of EEG embeddings in the image retrieval task. We calculate the cosine similarity between the EEG embeddings and the CLIP embeddings instead of text embeddings in the image dataset (with 200 images). Fig. 5d shows the average results for all subjects. We take the highest test accuracy in the training process as the statistical result. Fig. 5b shows the Top-5 retrieved images corresponding to the real visual stimulus seen by subjects. Compared with the previous models, the Top-1 accuracy of our model is significantly improved, and the Top-5 images all maintain a high degree of similarity with the original images. See the Tab. 8 in Appendix for more detailed averages of test accuracy in subjects.

Ablation Study on ATM We systematically deconstructed and analyzed each layer of our EEG projector. We conducted an ablation study for each component in ATM (i.e., the MLP projector, the Temporal-Spatial convolution module and the channel-wise attention block). We specified two different convolution architectures, ShallowNet (ATM-S) and EEGNetV4 (ATM-E), as our convolution backbone. Appendix B.3 showed the results obtained under different experimental configurations.

a

b

[Figure 2123]

[Figure 2124]

[Figure 2125]

[Figure 2126]

EEG Embedding

|[Figure 2127]<br><br>[Figure 2128]<br><br>[Figure 2129]<br><br>[Figure 2130]|
|---|

[Figure 2131]

[Figure 2132]

Retrieval

Image Dataset

Classification

|,,,<br><br>…<br><br>antelope pear kettle sausage …<br><br>|antelope|
|---|
<br><br>[Figure 2133]<br><br>| |
|---|
|
|---|

Text / Image Embedding

c

d

[Figure 2134]

[Figure 2135]

- Figure 5: EEG-based image retrieval and classification. (a) The paradigm of EEG-based image retrieval and classification. (b) Samples of the top-5 accuracy in EEG-image retrieval tasks. See Appendix G for additional images results. (c) Average in-subject classification accuracy across different methods. (d) Average in-subject retrieval accuracy across different methods.

###### 3.3 Image Generation Performance

- Fig. 6a shows the process of generating images under the guidance of EEG embedding and evaluating the quality of the generated images. To evaluate the generation performance, we conducted an image retrieval task. Specifically, we extract the CLIP embedding of the generated images and compare the similarity between the CLIP embeddings of all images to retrieve the generated image.
- Fig. 6b shows the similarity of distribution. Fig. 6c shows the generated samples. The generated images have high semantic similarity with the seen images and have good diversity in low-level visual features, which can be manipulated by the guidance scale hyperparameter (Fig. 6d). We also report the decoding and reconstruction performance for EEG, MEG, and fMRI across various metrics from different datasets in the Tab. 1.

Table 1: Quantitative assessments of the reconstruction quality for EEG, MEG, and fMRI in Subject

8. For detailed explanations of the metrics.

Low-level High-level Dataset ↑ PixCorr ↑ SSIM ↑ AlexNet(2) ↑ AlexNet(5) ↑ Inception ↑ CLIP ↑ SwAV ↓

NSD-fMRI [4] 0.305 0.366 0.962 0.977 0.910 0.917 0.410 NSD-fMRI [33] 0.254 0.356 0.942 0.962 0.872 0.915 0.423 NSD-fMRI [41] 0.130 0.308 0.917 0.974 0.936 0.942 0.369

THINGS-MEG [4] 0.058 0.327 0.695 0.753 0.593 0.700 0.630 THINGS-MEG (averaged) [4] 0.076 0.336 0.736 0.826 0.671 0.767 0.584 THINGS-MEG (Ours) 0.104 0.340 0.613 0.672 0.619 0.603 0.651 THINGS-EEG (Ours) 0.160 0.345 0.776 0.866 0.734 0.786 0.582

###### 3.4 Temporal Analysis

To investigate the effects of different EEG time window on visual decoding, we calculated the average top-1 classification accuracy for sliding and growing time windows: [0, t], including the entire period

EEG Embedding

Distribution of Similarity

###### a b

[Figure 2136]

[Figure 2137]

[Figure 2138]

[Figure 2139]

| |
|---|

2-Stage Generation

[Figure 2140]

| | |
|---|---|
|…<br><br>[Figure 2141]| |

Image Embedding

Image Embedding

[Figure 2142]

Cosine Similarity

| |
|---|

###### c d

Similarity and diversity for different guidance scale

[Figure 2143]

Seen Our Reconstructed Images

|[Figure 2144]<br><br>[Figure 2145]<br><br>[Figure 2146]<br><br>[Figure 2147]<br><br>[Figure 2148]<br><br>[Figure 2149]<br><br>[Figure 2150]<br><br>[Figure 2151]<br><br>[Figure 2152]<br><br>[Figure 2153]<br><br>[Figure 2154]<br><br>[Figure 2155]<br><br>[Figure 2156]<br><br>[Figure 2157]<br><br>[Figure 2158]<br><br>[Figure 2159]<br><br>[Figure 2160]<br><br>[Figure 2161]<br><br>|
|---|

[Figure 2162]

[Figure 2163]

[Figure 2164]

[Figure 2165]

- Figure 6: EEG guidance image generation. (a) The paradigm of image generation. (b) The similarity between random visual objects and the EEG embeddings, and the similarity between generated visual objects and the target EEG embeddings. (c) Comparison between the original image and the image generated using the corresponding EEG data. (see Appendix C for details). (d) The similarity between visual objects and target EEG embeddings as the guidance scale changes, and the diversity of visual objects as the guidance scale changes. See Appendix G for additional results.

from the onset of visual stimulus to time point t, and [t-100, t], only including the data 100ms before time point t. We compared the accuracy with a randomly selected baseline (0.5% chance level) to test predictive performance (Fig. 7). Our results show that within 500ms after visual stimulus, the accuracy reaches an upper limit of about 30%, after which the accuracy no longer improves (Fig. 7a). The MEG decoding shows a similar profile as the time window expands (Fig. 7b). We exhibit the generated images under different EEG time windows, [0, t] in Fig. 7c. The similarity is low when the time window is less than 150ms, and this similarity gradually increase as the time window expands. After 500 milliseconds, EEG-guided image generation can reliably reveal the semantics of the images seen. Interestingly, we find differences in the optimal reconstruction time windows for different categories of images, for example, jelly beans (200ms) are faster than aircraft carrier (500ms), implying that the human brain may process different visual objects at different speeds. This finding highlights the advantage of EEG’s high temporal resolution in studying fast visual processing compared with the lower temporal resolution of fMRI.

###### 3.5 Spatial Analysis

To investigate the contribution of different brain regions to visual decoding, we divided the EEG electrodes from the THING-EEG data into five distinct brain regions (i.e., Frontal, Temporal, Center, Parietal, Occipital regions in Fig. 8a), and then conducted ablation experiments on retrieval task (Fig. 8b) and the reconstruction task (Fig. 8c). The results showed that using information from all brain regions is optimal, for both retrieval and generation tasks. The occipital had the highest retrieval accuracy and reconstruction performance compared to other regions. Parietal and temporal regions contain some semantic information, whereas frontal and central regions contribute the least useful information to the visual decoding.

###### 4 Related Works

Visual decoding using neural signals: Decoding visual information from our brain has been a long-standing pursuit in neuroscience and computer science [32, 21]. Some progress has been

Average top-1 accuracy across subjects (EEG) c Seen

- a 50ms 150ms
- b

100ms 200ms 250ms 300ms 500ms 800ms

1000ms

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

1000ms

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

[Figure 2203]

[Figure 2204]

[Figure 2205]

[Figure 2206]

[Figure 2207]

[Figure 2208]

[Figure 2209]

Average top-1 accuracy across subjects (MEG)

[Figure 2210]

[Figure 2211]

[Figure 2212]

[Figure 2213]

[Figure 2214]

[Figure 2215]

[Figure 2216]

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

###### Figure 7: Performance of different EEG/MEG time windows on EEG-guided visual retrieval and reconstruction. (a) The retrieval accuracy of the expanding EEG windows at intervals [0, t] and

at intervals [t-100, t] respectively. (b) The retrieval accuracy of the expanding MEG windows. (c) Samples reconstructed as the EEG window expands. When the EEG time window is greater than 200ms, the reconstructed image is stable. See Appendix H for more detailed explanations.

- a c
- b

Division of electrode Seen Frontal Central Temporal Parietal Occipital All

[Figure 2242]

[Figure 2243]

[Figure 2244]

[Figure 2245]

[Figure 2246]

[Figure 2247]

[Figure 2248]

regions

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

###### Figure 8: EEG-guided retrieval and reconstruction using EEG from different brain regions. (a) The EEG electrodes assigned to five brain regions. (b) Top-1 and top-5 retrieval accuracy, using only the EEG channels in each leaved region and all channels. (c) Reconstructed images obtained using only the electrode channels in each individual region and all channels.

made in decoding steady-state visual stimulus. However, accurately and rapidly decoding semantic information in natural images remains a challenge [44]. fMRI has been widely used to estimate semantic and shape information in visual processing within the brain [49, 20]. However, the demand for high-speed and practical applications in brain-computer interfaces calls for alternative approaches. EEG, due to its high temporal resolution and portability, emerges as a promising option [56]. Yet, the overall performance across different subjects and biological plausibility remains unresolved [1]. Furthermore, previous approaches often relied on supervised learning methods with limited image categories, overlooking the intrinsic relationship between image stimulus and brain responses [29, 43, 27].

Neural decoding using EEG/MEG data: Previous studies have shown the efficacy of TemporalSpatial modules in representing neural data [39, 26]. For example, lightweight convolutional neural

networks such as EEGNet and ShallowNet [39] have achieved considerable performance in small EEG and MEG datasets. Using contrastive learning, it has been shown that merely using convolutional neural networks and projection layers can yield satisfactory results on neural datasets [6]. More recently, Benchetrit et al proposed a method towards real-time MEG-based reconstruction of visual perception [4]. Song et al. presented an EEG encoder using ShallowNet Temporal-Spatial convolution module with a large convolution kernel with a few parameters for EEG embedding, resulting in favorable performance on EEG-based visual decoding [46].

Limitations of previous studies: Previous EEG studies are primarily oriented toward understanding visual perception in the human brain rather than maximizing EEG decoding performance. Thus the visual decoding performance is far from optimal. Specifically, previous studies have trained linear models to (1) classify a small set of images from brain activity [16, 24], (2) to predict brain activity from the latent representations of images [8], or (3) to quantify the similarity analysis between these two patterns with representational similarity [8, 16, 15, 3]. While these studies also utilize image embeddings, their linear decoders are limited to classifying a small group of object categories or distinguishing image pairs. Moreover, several deep neural networks have been applied to maximize classification of speech [10], cognitive load [22], and images [34, 30, 2] in EEG recordings. [34] proposed a deep convolutional neural network for classifying natural images using EEG signals. Unfortunately, the experiment presented all images of the same category in a single block, probably misleading the decoder to rely on autocorrelated noise rather than the hidden informative patterns of brain activity [27]. Also, these EEG studies only classify a relatively small number of image categories.

###### 5 Discussion and Conclusion

In this study, we proposed a novel and feasible EEG-based zero-shot image reconstruction framework. Although it utilizes existing machine learning techniques , we demonstrate for the first time that EEG-based zero-shot visual decoding and reconstruction can be competitive with MEG and fMRI.

Technical Impact: Our technical contributions are mainly on the EEG encoder and the two-stage zero-shot visual reconstruction framework (Fig. 2). First, we developed the ATM, an EEG encoder which can efficiently represent EEG/MEG features for three tasks. Our comprehensive experiments of the EEG encoder (Fig. 3), compared to various architectures and training methods, achieves SOTA performance across various metrics and tasks (Figs. 4b, 5). Second, our two-stage EEG guidance image reconstruction framework achieves performance close to fMRI using only EEG data (Figs. 6, 14, Tab. 1, 6), and this method is compatible with MEG data (Figs. 4c, 7b).

Neuroscience Insights: Our results offer insights into the relationship between brain activity and visual perception. We analyzed EEG-based visual decoding within different time windows to examine when visual information is perceived in the brain (Fig. 7). Our results revealed that visual information in EEG data is predominantly contained within the 200-400ms range (Fig. 7a), consistent with previous EEG studies [50, 17, 46]. Interestingly, the visual information in MEG data last up to 800ms, much longer than EEG (Fig. 7b), in line with the results reported by a previous MEG study [4, 46]. We also found that EEG performs better than MEG in visual tasks (See Appendix D for Tab. 6), which is different from other fields, such as speech decoding [10]. In addition, through ablation experiments of spatial information, we found that visual information is mainly encoded in the occipital and parietal areas (Fig. 8).

Interesting Phenomena and Future Directions: First, there are non-negligible performance differences between cross-subject and within-subject settings. This performance gap arises from inter-subject differences in EEG signals [14, 61], likely attribute to heterogeneity in individual brain, differences in visual perception between individuals, and even shifts in noise distribution during EEG recording. So it calls for more efforts on EEG encoder, such as more flexible neural network architectures or better weight initialization of pre-trained models [9, 7]. Transfer learning and meta-learning are also future directions worth exploring [58, 57, 60]. Moreover, how to unify various electrode montages of different EEG datasets when pre-training large EEG models is a challenge. EEG source localization, which converts senor-level EEG signals into the standard brain source space [54, 52], might be a potential solution.

###### References

- [1] Ahmed, H., Wilbur, R. B., Bharadwaj, H. M., and Siskind, J. M. (2021). Object classification from randomized eeg trials. pages 3845–3854.
- [2] Bagchi, S. and Bathula, D. R. (2022). Eeg-convtransformer for single-trial eeg-based visual stimulus classification. Pattern Recognition, 129:108757.
- [3] Bankson, B. B., Hebart, M. N., Groen, I. I., and Baker, C. I. (2018). The temporal evolution of conceptual object representations revealed through models of behavior, semantics and deep neural networks. NeuroImage, 178:172–182.
- [4] Benchetrit Y, Banville H, K. J. R. (2023). Brain decoding: toward real-time reconstruction of visual perception. arXiv, 2310:19812.
- [5] Caron, M., Misra, I., Mairal, J., et al. (2020). Unsupervised learning of visual features by contrasting cluster assignments. Advances in neural information processing systems, 33:9912–9924.
- [6] Chen, T., Kornblith, S., Norouzi, M., et al. (2020). A simple framework for contrastive learning of visual representations. In International conference on machine learning, pages 1597–1607. PMLR.
- [7] Chen, X., Teng, X., Chen, H., Pan, Y., and Geyer, P. (2024). Toward reliable signals decoding for electroencephalogram: A benchmark study to eegnex. Biomedical Signal Processing and Control, 87:105475.
- [8] Cichy, R. M. and Pantazis, D. (2017). Multivariate pattern analysis of meg and eeg: A comparison of representational structure in time and space. NeuroImage, 158:441–454.
- [9] Cui, W., Jeong, W., Thölke, P., Medani, T., Jerbi, K., Joshi, A. A., and Leahy, R. M. (2023). Neuro-gpt: Developing a foundation model for eeg. arXiv preprint arXiv:2311.03764.
- [10] Défossez, A., Caucheteux, C., Rapin, J., Kabeli, O., and King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. Nature Machine Intelligence, 5(10):1097–1107.
- [11] Du, C., Fu, K., Li, J., and He, H. (2023). Decoding visual neural representations by multimodal learning of brain-visual-linguistic features. IEEE Transactions on Pattern Analysis and Machine Intelligence.
- [12] Fang, T., Zheng, Q., and Pan, G. (2023). Alleviating the semantic gap for generalized fmri-to-image reconstruction. In Thirty-seventh Conference on Neural Information Processing Systems.
- [13] Gao, S., Koker, T., Queen, O., Hartvigsen, T., Tsiligkaridis, T., and Zitnik, M. (2024). Units: Building a unified time series model. arXiv preprint arXiv:2403.00131.
- [14] Gibson, E., Lobaugh, N. J., Joordens, S., and McIntosh, A. R. (2022). Eeg variability: Task-driven or subject-driven signal of interest? NeuroImage, 252:119034.
- [15] Gifford, A. T., Dwivedi, K., Roig, G., and Cichy, R. M. (2022). A large and rich eeg dataset for modeling human visual object recognition. NeuroImage, 264:119754.
- [16] Grootswagers, T., Robinson, A. K., and Carlson, T. A. (2019). The representational dynamics of visual objects in rapid serial visual processing streams. NeuroImage, 188:668–679.
- [17] Grootswagers, T., Zhou, I., Robinson, A. K., Hebart, M. N., and Carlson, T. A. (2022). Human eeg recordings for 1,854 concepts presented in rapid serial visual presentation streams. Scientific Data, 9(1):3.
- [18] Guggenmos, M., Sterzer, P., and Cichy, R. M. (2018). Multivariate pattern analysis for meg: A comparison of dissimilarity measures. Neuroimage, 173:434–447.
- [19] Hebart, M. N., Contier, O., Teichmann, L., Rockter, A. H., Zheng, C. Y., Kidder, A., Corriveau, A., Vaziri-Pashkam, M., and Baker, C. I. (2023). Things-data, a multimodal collection of large-scale datasets for investigating object representations in human brain and behavior. Elife, 12:e82580.
- [20] Ho, J. K., Horikawa, T., Majima, K., Cheng, F., and Kamitani, Y. (2023). Inter-individual deep image reconstruction via hierarchical neural code conversion. NeuroImage, 271:120007.
- [21] Jia, C., Yang, Y., Xia, Y., Chen, Y.-T., Parekh, Z., Pham, H., Le, Q., Sung, Y.-H., Li, Z., and Duerig, T. (2021). Scaling up visual and vision-language representation learning with noisy text supervision. In International conference on machine learning, pages 4904–4916. PMLR.
- [22] Jiao, Z., Gao, X., Wang, Y., Li, J., and Xu, H. (2018). Deep convolutional neural networks for mental load classification based on eeg data. Pattern Recognition, 76:582–595.

- [23] Karras, T., Aittala, M., Aila, T., and Laine, S. (2022). Elucidating the design space of diffusion-based generative models. Advances in Neural Information Processing Systems, 35:26565–26577.
- [24] King, J.-R. and Wyart, V. (2021). The human brain encodes a chronicle of visual events at each instant of time through the multiplexing of traveling waves. Journal of Neuroscience, 41(34):7224–7233.
- [25] Kingma, D. P. and Ba, J. (2014). Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980.
- [26] Lawhern, V. J., Solon, A. J., Waytowich, N. R., et al. (2018). Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces. Journal of Neural Engineering, 15(5):056013.
- [27] Li, R., Johansen, J. S., Ahmed, H., Ilyevsky, T. V., Wilbur, R. B., Bharadwaj, H. M., and Siskind, J. M.

(2020). The perils and pitfalls of block design for eeg classification experiments. IEEE Transactions on Pattern Analysis and Machine Intelligence, 43(1):316–333.

- [28] Liu, Y., Hu, T., Zhang, H., Wu, H., Wang, S., Ma, L., and Long, M. (2023a). itransformer: Inverted transformers are effective for time series forecasting. arXiv preprint arXiv:2310.06625.
- [29] Liu, Y., Ma, Y., Zhou, W., Zhu, G., and Zheng, N. (2023b). Brainclip: Bridging brain and visuallinguistic representation via clip for generic natural visual stimulus decoding from fmri. arXiv preprint arXiv:2302.12971.
- [30] McCartney, B., Devereux, B., and Martinez-del Rincon, J. (2022). A zero-shot deep metric learning approach to brain–computer interfaces for image retrieval. Knowledge-Based Systems, 246:108556.
- [31] Meng, C., He, Y., Song, Y., Song, J., Wu, J., Zhu, J.-Y., and Ermon, S. (2021). Sdedit: Guided image synthesis and editing with stochastic differential equations. arXiv preprint arXiv:2108.01073.
- [32] Miyawaki, Y., Uchida, H., Yamashita, O., Sato, M.-a., Morito, Y., Tanabe, H. C., Sadato, N., and Kamitani, Y. (2008). Visual image reconstruction from human brain activity using a combination of multiscale local image decoders. Neuron, 60(5):915–929.
- [33] Ozcelik, F. and VanRullen, R. (2023). Natural scene reconstruction from fmri signals using generative latent diffusion. Scientific Reports, 13(1):15666.
- [34] Palazzo, S., Spampinato, C., Kavasidis, I., Giordano, D., Schmidt, J., and Shah, M. (2020). Decoding brain representations by multimodal learning of neural activity and visual features. IEEE Transactions on Pattern Analysis and Machine Intelligence, 43(11):3833–3849.
- [35] Podell, D., English, Z., Lacey, K., Blattmann, A., Dockhorn, T., Müller, J., Penna, J., and Rombach, R. (2023). Sdxl: Improving latent diffusion models for high-resolution image synthesis. arXiv preprint arXiv:2307.01952.
- [36] Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al. (2021). Learning transferable visual models from natural language supervision. In International conference on machine learning, pages 8748–8763. PMLR.
- [37] Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., and Chen, M. (2022). Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125, 1(2):3.
- [38] Sauer, A., Lorenz, D., Blattmann, A., and Rombach, R. (2023). Adversarial diffusion distillation. arXiv preprint arXiv:2311.17042.
- [39] Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M., Eggensperger, K., Tangermann, M., Hutter, F., Burgard, W., and Ball, T. (2017). Deep learning with convolutional neural networks for eeg decoding and visualization. Human Brain Mapping, 38(11):5391–5420.
- [40] Schonfeld, E., Ebrahimi, S., Sinha, S., et al. (2019). Generalized zero-and few-shot learning via aligned variational autoencoders. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 8247–8255.
- [41] Scotti, P., Banerjee, A., Goode, J., et al. (2024). Reconstructing the mind’s eye: fmri-to-image with contrastive learning and diffusion priors. Advances in Neural Information Processing Systems, 36.
- [42] Scotti, P. S., Banerjee, A., Goode, J., Shabalin, S., Nguyen, A., Cohen, E., Dempster, A. J., Verlinde, N., Yundler, E., Weisberg, D., et al. (2023). Reconstructing the mind’s eye: fmri-to-image with contrastive learning and diffusion priors. arXiv preprint arXiv:2305.18274.

- [43] Shen, G., Dwivedi, K., Majima, K., Horikawa, T., and Kamitani, Y. (2019). End-to-end deep image reconstruction from human brain activity. Frontiers in computational neuroscience, 13:21.
- [44] Shi, N., Li, X., Liu, B., Yang, C., Wang, Y., and Gao, X. (2023). Representative-based cold start for adaptive ssvep-bci. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:1521–1531.
- [45] Shi, Y., Paige, B., and Torr, P. (2019). Variational mixture-of-experts autoencoders for multi-modal deep generative models. Advances in neural information processing systems, 32.
- [46] Song, Y., Liu, B., Li, X., Shi, N., Wang, Y., and Gao, X. (2023). Decoding natural images from eeg for object recognition. arXiv preprint arXiv:2308.13234.
- [47] Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., and Poole, B. (2020). Score-based generative modeling through stochastic differential equations. In International Conference on Learning Representations.
- [48] Sutter, T. M., Daunhawer, I., and Vogt, J. E. (2020). Generalized multimodal elbo. In International Conference on Learning Representations.
- [49] Takagi, Y. and Nishimoto, S. (2023). High-resolution image reconstruction with latent diffusion models from human brain activity. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14453–14463.
- [50] Teichmann, L., Hebart, M. N., and Baker, C. I. (2023). Multidimensional object properties are dynamically represented in the human brain. bioRxiv.
- [51] Wang, J., Yang, Z., Hu, X., Li, L., Lin, K., Gan, Z., Liu, Z., Liu, C., and Wang, L. (2022). Git: A generative image-to-text transformer for vision and language. arXiv preprint arXiv:2205.14100.
- [52] Wang, S., Wei, C., Lou, K., Gu, D., and Liu, Q. (2024). Advancing eeg/meg source imaging with geometric-informed basis functions. arXiv preprint arXiv:2401.17939.
- [53] Wang, Z., Bovik, A. C., Sheikh, H. R., et al. (2004). Image quality assessment: from error visibility to structural similarity. IEEE transactions on image processing, 13(4):600–612.
- [54] Wei, C., Lou, K., Wang, Z., et al. (2021). Edge sparse basis network: A deep learning framework for eeg source localization. In 2021 International Joint Conference on Neural Networks (IJCNN), pages 1–8. IEEE.
- [55] Wei, C., Zou, J., Heinke, D., and Liu, Q. (2024). Cocog: Controllable visual stimuli generation based on human concept representations. arXiv preprint arXiv:2404.16482.
- [56] Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., and Shenoy, K. V. (2021). Highperformance brain-to-text communication via handwriting. Nature, 593(7858):249–254.
- [57] Wu, D., Jiang, X., and Peng, R. (2022). Transfer learning for motor imagery based brain–computer interfaces: A tutorial. Neural Networks, 153:235–253.
- [58] Wu, D., Xu, Y., and Lu, B.-L. (2020). Transfer learning for eeg-based brain–computer interfaces: A review of progress made since 2016. IEEE Transactions on Cognitive and Developmental Systems, 14(1):4–19.
- [59] Wu, M. and Goodman, N. (2018). Multimodal generative models for scalable weakly-supervised learning. Advances in neural information processing systems, 31.
- [60] Xie, Y., Wang, K., Meng, J., Yue, J., Meng, L., Yi, W., Jung, T.-P., Xu, M., and Ming, D. (2023). Crossdataset transfer learning for motor imagery signal classification via multi-task learning and pre-training. Journal of Neural Engineering, 20(5):056037.
- [61] Xu, L., Xu, M., Ke, Y., An, X., Liu, S., and Ming, D. (2020). Cross-dataset variability problem in eeg decoding with deep learning. Frontiers in human neuroscience, 14:103.
- [62] Ye, H., Zhang, J., Liu, S., Han, X., and Yang, W. (2023). Ip-adapter: Text compatible image prompt adapter for text-to-image diffusion models. arXiv preprint arXiv:2308.06721.

### Supplementary Material: Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion

###### A Datasets for experiments

- A.1 EEG dataset

We conducted our experiments on the THINGS-EEG dataset’s training set [15, 17]. This dataset includes a large EEG corpus from 10 human subjects during the visual task. The experiment employed the Rapid Serial Visual Presentation (RSVP) paradigm for orthogonal target detection tasks to ensure that participants attended to the visual stimulus. All 10 participants completed 4 equivalent experiments, resulting in 10 datasets with 16,540 training image conditions repeated 4 times, and 200 testing image conditions repeated 80 times, totaling (16,540 training image conditions × 4 repetitions) + (200 testing image conditions × 80 repetitions) = 82,160 image trials. Original data were collected using a 64-channel system at a sampling rate of 1000 Hz. After signal denoising, epoch data were downsampled to 100 Hz, selecting 17 channels covering the occipital and parietal cortex. Instead of using the raw dataset, we chose to filter it to [0.1, 100] Hz, retaining 63 channels of the original EEG data at a sampling rate of 1000 Hz. For preprocessing, we segmented the EEG data from 0 to 1000 ms after the stimulus onset into trials. Baseline correction was performed using the mean of the 200 ms pre-stimulus data. All electrodes were retained and downsampled to 250 Hz for analysis, and multivariate noise normalization was applied to the training data [18]. To improve signal-to-noise ratio, we averaged across the 4 EEG trials from the same image in the test set, while keeping each EEG trial in the training setting. We compared the effects of averaging across EEG trials and found it indeed improved the performance.

- A.2 MEG dataset

To verify the versatility of ATM for embedding electrophysiological data, we tested it on MEG data modality using the THINGS-MEG dataset [19]. It includes 271-channel MEG data from 4 subjects with 12 MEG sessions. The training dataset has 1854 Concepts × 12 images × 1 repetition, and the test dataset has concepts × 1 image × 12 repetitions for 200 times. Here, we discarded 200 testing concepts from the training set to construct the same zero-shot task as with the THINGS-EEG. Each image in the THINGS-MEG was displayed for 500 ms. There was a fixed time for each image of 1000 ± 200 ms. Continuous MEG data from -100 ms to 1300 ms was segmented into trials after the stimulus onset from 0 to 1000 ms. Preprocessing was performed using a bandpass filter of [0.1, 40] Hz and baseline correction after downsampling to 200 Hz. Note that due to the small number of participants, no statistical analysis was performed on the MEG dataset. We compared our approach with advanced methods i.e. NICE [46] and B.D. [4] for classification and retrieval tasks on the MEG dataset. We directly used the stimulus images to match the template, rather than other images belonging to the concept.

###### B More Implementation Details

###### B.1 Evaluation metric implementation

Classification accuracy As CLIP has been designed to align text and image modalities, we also leverage its text encoder for EEG classification using the text embeddings of categories. This approach utilizes CLIP’s text encoding capabilities to facilitate EEG classification. We conducted zero-shot classification tests on the THINGS-EEG dataset. We employed Top-K accuracy as a metric for performance evaluation. Specifically, we assessed performance based on the Top-k (where k=1, 5) predictions. We conducted tests for both within-subject and leave-one-subject-out classification accuracy, enabling a comprehensive evaluation of the model’s performance across different scenarios. Additionally, for each test instance, we extracted embeddings of N-1 unrelated samples from the test set as inputs. This means, apart from the entire test set, the model evaluated by N-Way accuracy (where N=2, 4, 10 in our experiments) on the test set. We report these results in Appendix H.

Retrieval accuracy Similar to the classification task, in the retrieval task, the objective is to retrieve the Top-K images most related to a given stimulus image via its corresponding EEG signal. This implies that by changing the text embeddings of image labels to image embeddings, we can transition the task from classification to image retrieval. Given that contrastive learning is known to be sensitive to batch size, we also compared the performance improvement of different methods under varying batch sizes (batch size=16, 1024) (Appendix H).

Generation accuracy The generation task presents more challenges than the other tasks. For each image condition in the test set, we generate 10 different images from 10 subjects based on the corresponding EEG. Subsequently, image retrieval is performed for each generated image. The Top-1 and Top-5 accuracies are calculated. It helps in evaluating the semantic alignment between the generated images and their original counterparts.

###### B.2 Computing methods implementation

In the upstream EEG encoder part, we compared various methods. For the B.D. method [4], we replicated the network structure as described in the original work, with the difference being in the shape of the input data due to the original study’s focus on MEG. It is worth mentioning that we used the leave one for subject method in the testing process so we modify its subject-wise layer as an linear layer for modeling the time dimension. To ensure fairness, we did not use the same hyperparameters as in the original paper. Instead, we chose settings yielded excellent results upon reproduction. Across all methods, we used identical hyperparameters, apart from the network structures. These included batch size, optimizer, initial learning rate, and temperature parameters.

###### B.3 Architecture details

Table 2: Brain module configuration Layer Input shape Output shape # parameters Channel-wise attention layer (N, C, T) (N, C, D) 553,078 Temporal-Spatial Conv module (N, C, D) (N, H1, H2) 103,680 Temporal-Spatial aggregation (N, H1, H2) (N, H1*H2) 0 MLP projector (N, H1*H2) (N, 1024) 2,527,232 Total 3,183,990

Table 3: Ablation study on the ATM model’s different components for THINGS-EEG retrieval.

Module MLP TSConv CAL TOP-1 TOP-5

✓ ✗ ✗ 8.11±1.74 26.83±4.78 ✓ ✓ ✗ 21.65±6.22 51.34±9.83

ATM-S ✓ ✗ ✓ 23.73±7.62 52.71 ±9.71 ✓ ✓ ✓ 28.64±6.39 58.47±8.97 ✓ ✗ ✗ 8.11±1.74 26.83±4.78 ✓ ✓ ✗ 17.95±5.95 43.10±8.63

ATM-E ✓ ✗ ✓ 23.73±7.62 52.71 ±9.71 ✓ ✓ ✓ 24.92±6.00 54.78±8.49

###### B.4 Model configuration

To validate the efficacy of our EEG encoder, we experimented with a variety of empirical setups aimed at optimizing the model’s efficiency. we leverage joint subject training to adapt to new subjects. Once a model is trained, it can be used for both reasoning about known subjects (subject-specific tokens) and reasoning about unknown subjects (shared tokens). In the context of channel-wise attention layer, we explored four distinct approaches for enhancing downstream retrieval capabilities: leveraging subject-specific tokens for retrieval, averaging all tokens for a more generalized retrieval,

flattening the entire token set for direct retrieval, and preserving token dimensions to feed into the Temporal-Spatial convolution module for feature integration. Notably, the strategy of preserving dimensions and using the Temporal-Spatial convolution module emerged as the most effective.

In our quest to optimize token embeddings, we experimented with a variety of approaches, including using 1 × 1 convolution and linear layers. Under our framework, using linear layers performs better than convolutions. Moving beyond, we delved into the efficacy of diverse Feed Forward Networks (FFNs) within the Transformer encoder layer. Our findings indicated that an FFN tailored to the temporal dimension emerged as the superior option. We also conducted a comparative analysis of various positional encoding techniques. Interestingly, for Temporal-Spatial convolution utilized in retrieval tasks, the significance of positional encoding diminished.

In a further exploration, we examined the impact of deploying convolutions at various stages and even contemplated the complete removal of the convolution module. It was discovered that situating convolutions post the Transformer encoder layer yielded the most favorable outcomes. Conversely, a shift to a MLP or the removal of the convolution module led to a notable degradation in performance. Our assumption is though the convolution’s inherent translational invariance is compromised when the context of the time dimension is disrupted, the efficiency of parameters it possesses may confer a resistance to overfitting, thereby maintaining its effectiveness.

Table 4: Impact of each module on the result in different configurations.

###### Module Config Top-1 (std) Top-5 (std)

w/ mean token 7.29 (3.01) 23.11 (6.62) w/ flatten token 14.85 (5.46) 37.56 (8.92)

Channel-wise attention layer

w/ keep dim 28.64 (6.39) 58.47 (8.97) Token embedding

w/ conv1d 24.81 (7.29) 55.68 (9.08) w/ linear 28.64 (6.39) 58.47 (8.97)

w/ temporal dim 28.64 (6.39) 58.47 (8.97) w/ spatial dim 19.92 (7.74) 47.59 (11.5) w/o 26.45 (7.73) 57.00 (9.95)

Feed Forward Network

w/ sinusoidal 27.96 (6.54) 58.16 (8.44) w/ learnable absolute 26.66 (6.56) 56.95 (7.95)

Position encoding

###### w/o 28.64 (6.39) 58.47 (8.97)

w/ pre 14.23 (4.20) 37.44 (6.06) w/ post 28.64 (6.39) 58.47 (8.97) w/ both 25.37 (5.16) 57.07 (6.13)

Temporal spatial convolution

w/o 23.73 (7.62) 52.71 (9.71)

###### B.5 Training details

In our EEG projector module, we integrated two distinct strategies for steering model predictions: text embedding and image embedding. Given the variance in feature granularity, we observed that alignments that prioritize image embedding excel in tasks of image retrieval and classification. Throughout the training phase, our experiments revealed that a batch size of 16 is a judicious selection for all models. Conversely, a batch size of 1024, which implies a substantial number of samples are processed in each training iteration, necessitates the model to exhibit a heightened capacity for noise resistance. In order to enhance the signal-to-noise ratio within EEG data, we implemented an averaging technique on 80 repeated instances within the test set. This approach mirrors the methodology employed in identifying Event-Related Potentials (ERP). To maximize the utilization of the available training data, we refrained from averaging the 4 repetitions in the training set. Instead, we opted to input the complete set of EEG data into the model, thereby facilitating comprehensive learning.

###### a b

[Figure 2280]

[Figure 2281]

[Figure 2282]

[Figure 2283]

[Figure 2284]

[Figure 2285]

- Figure 9: Test accuracy during each training epoch. (a) Training of different within-subject models. (b) Training of different across-subject models. We compared 7 different EEG encoding models, including EEGconformer, MLP, EEGNetv4, B.D., NICE, ATM-S (Ours) and ATM-E (Ours).

###### C Details of EEG guidance image generation

Here, we provide a concise overview of the conditional diffusion model framework used in EEGguided image generation, following the presentation of continuous-time diffusion models in [47, 23].

Diffusion models Diffusion Models (DMs) engage in a generative process by transforming highvariance Gaussian noise into structured data representations. This transformation is achieved by gradually reducing noise levels across a sequence of steps. Specifically, we begin with a high-variance Gaussian noise xM ∼ N(0,σmax2 ) and systematically denoise it through a series of steps to obtain xt ∼ p(xt;t), where σt < σt+1 and σM = σmax. For a well-calibrated DM, and with σ0 = 0, the final x0 aligns with the original data distribution.

Sampling process The sampling in DMs is implemented by numerically simulating a Probability Flow ordinary differential equation (ODE) or a stochastic differential equation (SDE). The ODE is represented as:

dx = −σ˙(t)σ(t)∇x log p(x;t)dt, (1)

where ∇x log p(x;t) is the score function, and σ(t) is a pre-defined schedule with its time derivative σ˙(t). The SDE variant includes a Langevin diffusion component and is expressed as:

dx = − σ˙(t)σ(t)∇x log p(x;t)dt − β(t)σ2(t)∇x log p(x;t)dt

+ 2β(t)σ(t)dωt,

where dωt is the standard Wiener process.

(2)

Training of DMs The core of DM training is to learn a model for the score function. This is typically achieved through denoising score matching (DSM), where ϵθ is a learnable denoiser. The training process can be formulated as:

0,c)∼pdata(x0,c),(nt,t)∼p(nt,t) ∥ϵθ(x0 + σtϵ;t,c) − ϵ∥22 , (3) where ϵ is Gaussian noise with variance σt2, and c represents a condition.

E(x

###### C.1 Stage I - EEG-Conditioned Diffusion

The initiation of the EEG-conditioned diffusion phase is paramount in our EEG-based image generation framework, leveraging the classifier-free guidance strategy alongside data pairs of CLIP embeddings and EEG embeddings (zI,zE). Adapting from state-of-the-art generative techniques, our diffusion process is specifically conditioned on the EEG embedding zE to adeptly capture the distribution of CLIP embeddings p(zI|zE). The CLIP embedding zI, procured during this phase, establishes the groundwork for the ensuing image generation stage. Our architecture incorporates a streamlined U-Net, labeled as ϵprior(zIt,t,zE), where zIt signifies the perturbed CLIP embedding at a

given diffusion timestep t. The training utilizes pairs from the ImageNet database, consisting of over a million images, to fine-tune the EEG-Conditioned Diffusion model. This model is meticulously trained using the classifier-free guidance approach, effectively balancing the conditioning signal’s fidelity with the generative output’s diversity.

Classifier-free guidance method The Classifier-Free Guidance technique is crucial in guiding the iterative refinement of a Diffusion Model (DM) under a specific EEG condition zE. It achieves this by synchronizing the outputs of both a conditional and an unconditional model. The model’s formulation, ϵwprior(zIt;t,zE), is as follows:

ϵwprior(zIt;t,zE) = (1 + w)ϵprior(zIt;t,zE) − wϵprior(zIt;t), (4) where w ≥ 0 represents the guidance scale. This mechanism facilitates concurrent training of the conditional and unconditional models within a singular network framework, periodically substituting the EEG embedding zE with a null vector to promote training variability, i.e. 10% of the time. The primary objective of this method is to enhance the sample quality produced by DMs while maintaining output diversity.

###### C.2 Stage II - CLIP-Embedded Image Synthesis

In Fig. 10, we compare the effects of one-stage and two-stage EEG-guided image generation. We show images generated using EEG embeddings directly (One-stage) and images generated using image embeddings obtained via prior diffusion (Two-stage). It can be seen that the two-stage EEGguided image generation can more accurately reconstruct the semantic and low-level visual features of the original image, and the style is more realistic.

###### a b

[Figure 2286]

[Figure 2287]

Seen

Stage I

Stage 2

- Figure 10: Comparison between one-stage and two-stage EEG guidance image reconstruction. (a) We present the images that subjects seen (Seen), our reconstructed images directly using EEG embeddings (One-stage), and the reconstructed images from low level and high level image embeddings obtained by the prior diffusion (Two-stage). These results indicate that the strategy of our two-stage generation can better reconstruct the seen visual stimulus. (b) We employed ATM-S to compare the generated images with the original images in a retrieval task. Our result indicates that the images generated in two stages significantly enhance the performance of the original model on the retrieval task.

Table 5: Latent VAE retrieval performance Condition Top-1 (%) Top-5 (%) ideal chance 0.5 2.5 ATM-S (Ours) 10.14 29.55

In the second stage of our EEG-based image generation approach, the CLIP embedding zI derived from the EEG-conditioned diffusion acts as the precursor for synthesizing visual objects I based on

zI. This is achieved by harnessing the synergies of advanced pre-trained models, namely SDXL and IP-Adapter [35, 62], facilitating the creation of high-caliber images.

The cornerstone of our synthesis process is the SDXL framework, acclaimed for its proficiency in textto-image conversion. The integration of the IP-Adapter introduces dual cross-attention mechanisms,

allowing the CLIP embedding zI to serve as a directive input and guide the denoising trajectory within the U-Net structure. The synthesis model is denoted as ϵSD(zt,t,zI), where zt denotes the SDXL Variational Autoencoder’s (VAE) disturbed latents.

SDXL-turbo for accelerated processing To augment the efficiency of our framework, we additionally explore the SDXL-Turbo [38], a refined iteration of SDXL optimized for swift image synthesis. This variant proves especially beneficial in scenarios demanding quick generation of high-fidelity visuals.

IP-Adapter’s efficacy The IP-Adapter, with its compact design, has proven to be effective in enhancing image prompt adaptability within pre-trained text-to-image models. Its compatibility with text prompts for multimodal image generation extends the versatility of our EEG-based image synthesis approach.

###### C.3 Low-level pipeline

Compared with pure vision pre-training models such as (ViT, ResNet, DINO, etc.), the CLIP model lacks low-level visual features. Therefore, in order to make up for this shortcoming, our framework introduces a low-level visual reconstruction pipeline. We hope to restore basic such as contour, posture, orientation and other pixel-level information from EEG by aligning with the latent of VAE.

Past work [49] has found that in the denoising stage of the early diffusion model, z signals (corresponding to the VAE latent in our framework) dominated prediction of fMRI signals. And during the middle step of the denoising process, zc predicted activity within higher visual cortex much better than z. However, note that this is only an analysis based on decoding accuracy. These analyses do not have a strong neuroscience causal relationship. We still cannot conclude that the low-level features of neural data are modeled by VAE.

We trained the low-level pipe for 200 epochs, trying a latent mean squared error (MSE) loss, along with a contrastive learning loss, and a variational autoencoder (VAE) image reconstruction loss to align the 4 × 64 × 64 EEG latents obtained from a projection layer and an upsampled CNN with the VAE latents. Nevertheless, reconstruction loss or contrastive learning loss performs worse than only applying the loss in latent space and also requires significantly more GPU memory. In addition, we found that using a low-level visual model for distillation learning in the low-level pipeline is not only unhelpful for VAE latent training, but also leads to overfitting. Similar conclusions were reached in MindEye[42]. Our results suggested that the low-level zeroshot reconstruction in EEG is not stable enough and may mislead the model results. When using the low level pipeline, we usually set the inference steps of SDXL to 10 (or SDXL-turbo to 4) and the image-to-image denoising strength to 0.5. We give several reconstruction examples in Fig. 11 to compare the impact before and after using low level pipeline. Moreover, low level alignment was validated through retrieval performance tests, as depicted in Tab. 5. Our findings indicate that retrieval using EEG latents can also achieve excellent performance. This further substantiates the feasibility of aligning the low-level consistency through VAE latents.

###### C.4 Semantic-level pipeline

In addition to using EEG latent and low-level pipelines during reconstruction, we also add a corresponding semantic level pipeline guided by text captions during the image reconstruction. We input the 1 × 1024 EEG features output by prior Diffusion into the trained image projector to obtain 256 × 1024 image features. Using the GIT model[51], we can directly generate a caption from the latent features of the image. IP-Adapter accepts such a caption as a text prompt to guide the semantic level reconstruction of the image. It should be noted that due to the difficulty of the zeroshot task itself and the low dimensionality of the EEG features, the caption generated from the latent may be unstable, thereby interfering with the original correct EEG semantics. Considering that the image features extracted by the CLIP model itself are already high-level visual features and do not require the introduction of more semantic information, this framework retains the entry of the text prompt, and the reconstructed image presented does not force the use of the semantic level pipeline.

CLIP + Semantic Only low level

CLIP + low level

CLIP + Semantic + low level

Seen image Only CLIP

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

- Figure 11: Example of our reconstructions for Subject 8 output from different pipelines. From left to right: reconstruction using only CLIP (i.e., Only CLIP), using only CLIP and the semantic pipeline (i.e., CLIP + Semantic), using only the low level pipeline (i.e., Only low level), using only CLIP and the low level pipeline (i.e., CLIP + low level), using joint CLIP, low level, and semantic pipelines.

###### D Performance comparison

Comparison metrics Our study uses various metrics to evaluate how well we can recreate visual stimulus from brain data (EEG, MEG, fMRI) (Tab. 1 and Tab. 7). These metrics include PixCorr (pixelwise correlation, between ground truth and reconstructions), SSIM (structural similarity index metric)[53], SwAV (SwAV-ResNet50, refer to average correlation distance)[5], and two-way identification using neural networks (AlexNet(2/5), Inception, CLIP. Here AlexNet(2/5) the 2nd and 5th feature layers of AlexNet) for both low-level and high-level image features. Here two-way identification can be seem as a two-way retrieval task described in [33]. In Tab. 1, our results showed that on the THINGS dataset, we could achieve performance over MEG on EEG reconstruction using ATM. Tab. 6 shows the decoding performance of different data sets (fMRI, MEG, EEG) on visual

stimulus tasks, and we even achieved the same or better performance than fMRI and MEG. Our results suggest that a suitable neural representation plays a decisive role in the downstream task.

- Table 6: The classification performance of various methods are discussed. Due to differences in datasets and data modalities, we have specified unified metrics to objectively assess the performance of each method.

50-way 100-way 200-way Dataset Model top-1 top-5 top-1 top-5 top-1 top-5

GOD-Wiki (fMRI)

CADA-VAE (V&T)[40] 10.02 40.37 - - - MVAE (V&T) [59] 10.04 39.60 - - - MMVAE (V&T) [45] 11.68 43.29 - - - MoPoE-VAE (V&T) [48] 12.90 51.78 - - - BraVL (V&T) [11] 13.99 53.13 - - - -

THINGS (MEG) ATM (Ours) 15.63 41.38 11.75 29.25 5.88 19.25 THINGS (EEG) BraVL [11] 14.33 40.28 - - 5.82 17.45

ATM (Ours) 17.40 39.40 11.50 28.50 7.40 20.60

- Table 7: Quantitative comparison results of image reconstruction in Subject 8 via our framework using different encoders.

Low-level High-level Dataset ↑ PixCorr ↑ SSIM ↑ AlexNet(2) ↑ AlexNet(5) ↑ Inception ↑ CLIP ↑ SwAV ↓

NSD-fMRI [4] 0.305 0.366 0.962 0.977 0.910 0.917 0.410 THINGS-MEG [4] 0.058 0.327 0.695 0.753 0.593 0.700 0.630 THINGS-MEG (averaged) [4] 0.090 0.336 0.736 0.826 0.671 0.767 0.584 THINGS-MEG (Ours) 0.104 0.340 0.613 0.672 0.619 0.603 0.651

THINGS-EEG (NICE) [46] 0.142 0.276 0.739 0.832 0.659 0.722 0.612 THINGS-EEG (EEGNetV4)[26] 0.140 0.302 0.767 0.840 0.713 0.773 0.581 THINGS-EEG (Ours) 0.160 0.345 0.776 0.866 0.734 0.786 0.582

###### E Representational analysis

As depicted in Fig. 12, we showcase the representational similarity matrix and visualization in the latent space. To investigate the relationship between the representations obtained from EEG and those of images, we conducted a representational similarity matrix. We focused on Subject 8, who exhibited the highest retrieval accuracy. By applying a clustering algorithm to the image embeddings corresponding to 200 images in the test set, we observed distinct within-category clustering. We generated similarity matrices based on both image and text embeddings, which were then compared with EEG representations. As shown in Fig. 12, clear within-category clustering is observable in the representational similarity matrix with image, whereas this phenomenon is not present in the representational similarity matrix with text.

###### F Concept analysis

We have adopted the concept embedding encoder proposed by Wei et al. [55], which encodes the clip embedding of the original image into a 42-dimensional vector, with each dimension representing a distinct concept. Utilizing the ATM for direct projection on the EEG data of 200 categories from the test set, we obtained EEG embeddings that were then fed into the concept encoder with frozen weights, yielding 200 concept embeddings, as depicted in Fig. 13. An analysis of representational similarity at the concept level indicates that the EEG embeddings derived from our EEG projector effectively align with the conceptual space. This ensures semantic consistency at a high level of alignment, providing compelling evidence for the reconstruction of images from EEG data.

###### a b

[Figure 2354]

[Figure 2355]

[Figure 2356]

[Figure 2357]

[Figure 2358]

- Figure 12: Visualization of the representation of EEG, image and text modality. (a) Representational similarity matrix between EEG features and image/text features. (b) Visualization in the latent space of EEG/image/text by t-SNE.

##### a

[Figure 2359]

[Figure 2360]

[Figure 2361]

EEG embedding

[Figure 2362]

Reconstruction

[Figure 2363]

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
|…| | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

[Figure 2364]

[Figure 2365]

[Figure 2366]

Seen

[Figure 2367]

[Figure 2368]

[Figure 2369]

[Figure 2370]

[Figure 2371]

[Figure 2372]

###### b Similarity Matrix

c Clustered Similarity Matrix

[Figure 2373]

[Figure 2374]

[Figure 2375]

[Figure 2376]

Encodedconceptionembedding

Encodedconceptionembedding

[Figure 2377]

[Figure 2378]

[Figure 2379]

Conception embedding

Conception embedding

[Figure 2380]

- Figure 13: Visualization of the conceptual representation analysis. (a) Conceptual representations were obtained from eeg embeddings using concept encoder. (b) The similar matrix between EEG embeddings and real concept embeddings. (c) Concept embedding similarity matrix after cluster rearrangement (k=5).

###### G Additional images results

We visualize the best, medium and worst generated images in Fig. 14. We randomly selected the EEG data of a subject viewing 100 images, and extracted EEG embeddings to guide image generation. By calculating the cosine similarity of the CLIP embedding between the generated image and the original image, we found 12 images each with the best, medium and worst generation effects. It can be seen that in the best group, the generated image is not only highly consistent with the semantics of the original image, but also well retains the low-level visual features. in the medium group, the generated image maintains the semantic features of the original image, and the low-level visual features are well preserved. Visual features were altered. in the worst group, both semantic features and low-level visual features were altered.

[Figure 2381]

SeenGeneratedSeenGeneratedSeenGenerated

WorstBestMedian

[Figure 2382]

[Figure 2383]

- Figure 14: Examples of EEG-guided visual reconstruction. From top to bottom, we exhibit the best, median, and worst 12 generated images, respectively. We show the images subjects seen and the generated images by our two-stage image generator.

###### G.1 Additional retrieval results

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

###### Figure 15: Additional retrieval results

- G.2 Additional generated images

[Figure 2396]

SeenGeneration

[Figure 2397]

#### Best

- Figure 16: Additional generated results with the best alignment to original images

[Figure 2398]

SeenGeneration

[Figure 2399]

#### Median

- Figure 17: Additional generated results with the median alignment to original images

[Figure 2400]

Seen

[Figure 2401]

#### Worst

Generation

Figure 18: Additional generated results with the worst alignment to original images

###### G.3 Additional generated images for each subject

[Figure 2402]

GeneratedSeenGeneratedSeenGeneratedSeen

BestWorstMedian

[Figure 2403]

[Figure 2404]

- Figure 19: Part of subject 1 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2405]

[Figure 2406]

[Figure 2407]

BestWorstMedian

GeneratedSeenGeneratedSeenGeneratedSeen

- Figure 20: Part of subject 2 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

###### H Additional evaluation results

[Figure 2408]

GeneratedSeenGeneratedSeenGeneratedSeen

BestWorstMedian

[Figure 2409]

[Figure 2410]

- Figure 21: Part of subject 3 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2411]

[Figure 2412]

[Figure 2413]

BestWorstMedian

GeneratedSeenGeneratedSeenGeneratedSeen

- Figure 22: Part of subject 4 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2414]

GeneratedSeenGeneratedSeenGeneratedSeen

BestWorstMedian

[Figure 2415]

[Figure 2416]

- Figure 23: Part of subject 5 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2417]

[Figure 2418]

[Figure 2419]

BestWorstMedian

GeneratedSeenGeneratedSeenGeneratedSeen

- Figure 24: Part of subject 6 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2420]

GeneratedSeenGeneratedSeenGeneratedSeen

BestWorstMedian

[Figure 2421]

[Figure 2422]

- Figure 25: Part of subject 7 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2423]

[Figure 2424]

[Figure 2425]

[Figure 2426]

[Figure 2427]

[Figure 2428]

BestWorstMedian

GeneratedSeenGeneratedSeenGeneratedSeen

- Figure 26: Part of Subject 8 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2429]

GeneratedSeenGeneratedSeenGeneratedSeen

BestWorstMedian

[Figure 2430]

[Figure 2431]

- Figure 27: Part of subject 9 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

[Figure 2432]

[Figure 2433]

[Figure 2434]

[Figure 2435]

[Figure 2436]

[Figure 2437]

BestWorstMedian

GeneratedSeenGeneratedSeenGeneratedSeen

[Figure 2438]

[Figure 2439]

- Figure 28: Part of subject 10 generates images. We do a batch generation of the subjects and then calculate the best, medium, and worst performers compared to the original stimulus pictures.

###### H.1 Accuracy for time windows

According to our results in 30 for time windows, which shows that for all embeddings, a clear peak can be observed for windows ending around 200-250 ms after image onset. Comparing 29 and 30, we can see that, unlike [4], our time window results on THINGS-EEG dataset do not have a second peak, which may be mainly affected by the experimental paradigm. In 7, we can see that in the first 50ms-200ms, the image reconstructed at 50 ms is completely messy and has no semantics; the semantics of the reconstructed image after 250 ms is basically correct and gradually stabilizes, and after 500ms, due to the lack of additional visual response, the content of the image reconstruction is more stable. Similar results are also shown in Figure 4 A of [4]: their method can also reconstruct high-quality images at 100ms. This just shows that our reconstruction results are in line with the neuroscience prior. However, this does not mean that the EEG data after the absence of visual response (200ms) loses its contribution to decoding, because the processing of high-level visual features (corresponding to the visual features of CLIP) may be involved over time.

[Figure 2440]

[Figure 2441]

[Figure 2442]

[Figure 2443]

[Figure 2444]

[Figure 2445]

[Figure 2446]

[Figure 2447]

- Figure 29: Accuracy for growing windows. We use an EEG time window of 100ms, sliding 100ms each time. (a) Top-1 accuracy. (b) Top-5 accuracy.

[Figure 2448]

[Figure 2449]

[Figure 2450]

[Figure 2451]

[Figure 2452]

[Figure 2453]

[Figure 2454]

[Figure 2455]

###### Figure 30: Accuracy for sliding windows. We use an EEG time window of 100ms, sliding 100ms each time. (a) Top-1 accuracy. (b) Top-5 accuracy.

[Figure 2456]

[Figure 2457]

[Figure 2458]

[Figure 2459]

[Figure 2460]

[Figure 2461]

###### Figure 31: Accuracy for growing windows. The MEG time window grows from 50ms to 1000ms. (a) Top-1 accuracy. (b) Top-5 accuracy.

[Figure 2462]

[Figure 2463]

[Figure 2464]

[Figure 2465]

[Figure 2466]

[Figure 2467]

[Figure 2468]

[Figure 2469]

[Figure 2470]

- Figure 32: Accuracy for sliding windows. We use an MEG time window of 100ms, sliding 100ms each time. (a) Top-1 accuracy. (b) Top-5 accuracy.

- Table 8: Overall accuracy of zero-shot Retrieval on THINGS-EEG dataset. We showed in-subject and cross-subject retrieval task performance (Ave ± Std.%) under the condition of batch size=1024. We compared the 2-way, 4-way, 10-way, the Top-1 and Top-5 accuracy of 200-way from different EEG embedding methods. Our ATM outperformed all the others.

Subject dependent - train and test on one subject (batch size=1024)

###### Methods 2-Way 4-Way 10-Way Top-1 Top-5

EEGITNet 76.69 ± 12.97 56.98 ± 16.31 36.35 ± 15.11 5.75 ± 3.62 18.14 ± 9.40 EEGConformer 76.17 ± 13.13 56.29 ± 16.70 34.72 ± 14.79 3.98 ± 2.80 17.10 ± 9.21

- ShallowFBCSPNet 74.32 ± 12.14 53.97 ± 15.81 33.48 ± 14.35 6.10 ± 4.61 16.53 ± 9.94 EEGNetV4 92.81 ± 2.22 83.15 ± 4.20 67.81 ± 6.11 19.51 ± 5.19 48.99 ± 6.75 B.D. 78.42 ± 8.81 58.24 ± 12.13 37.97 ± 11.38 5.88 ± 3.49 18.61 ± 7.81 NICE 92.73 ± 2.75 83.26 ± 5.47 67.96 ± 8.31 19.32 ± 5.33 49.26 ± 9.69 MLP 83.09 ± 2.54 66.70 ± 4.16 45.43 ± 4.58 7.23 ± 1.66 25.14 ± 3.66 ATM-S (Ours) 94.92 ± 1.45 87.91 ± 3.14 75.37 ± 5.77 28.64 ± 6.39 58.47 ± 8.97 ATM-E (Ours) 92.99 ± 2.20 83.81 ± 4.46 68.87 ± 7.27 22.40 ± 6.62 50.59 ± 9.59

Subject independent - leave one subject for test (batch size=1024)

Methods 2-Way 4-Way 10-Way Top-1 Top-5

EEGNetV4 82.85 ± 3.62 64.65 ± 6.29 42.35 ± 7.10 6.25 ± 2.56 20.95 ± 5.73 EEGConformer 56.54 ± 4.00 31.80 ± 3.20 13.89 ± 2.01 0.87 ± 0.33 4.42 ± 1.20

- ShallowFBCSPNet 75.76 ± 2.49 53.63 ± 3.58 31.43 ± 4.30 2.51 ± 1.31 12.03 ± 2.78 EEGNetV4 82.60 ± 3.17 64.28 ± 5.44 42.24 ± 6.10 6.13 ± 2.40 21.23 ± 5.19 B.D. 72.84 ± 12.41 51.41 ± 15.10 31.67 ± 12.96 4.10 ± 2.72 14.46 ± 7.97 NICE 83.88 ± 2.57 66.14 ± 5.30 45.13 ± 5.85 8.24 ± 3.01 23.76 ± 5.09 MLP 75.80 ± 2.45 55.08 ± 3.07 34.05 ± 2.83 4.46 ± 0.81 15.26 ± 2.34 ATM-S (Ours) 87.36 ± 3.97 72.80 ± 7.02 53.80 ± 8.41 11.84 ± 4.80 33.73 ± 8.73 ATM-E (Ours) 80.65 ± 3.11 61.65 ± 5.31 39.66 ± 6.44 7.00 ± 2.20 21.12 ± 5.25

