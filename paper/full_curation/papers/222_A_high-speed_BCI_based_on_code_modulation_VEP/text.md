IOP PUBLISHING JOURNAL OF NEURAL ENGINEERING J. Neural Eng. 8 (2011) 025015 (5pp) doi:10.1088/1741-2560/8/2/025015

# A high-speed BCI based on code modulation VEP

## Guangyu Bin, Xiaorong Gao1, Yijun Wang, Yun Li, Bo Hong and Shangkai Gao

Biomedical Engineering Department, Tsinghua University, 100084, Beijing, People’s Republic of China E-mail: gxr-dea@tsinghua.edu.cn

Received 29 November 2010 Accepted for publication 21 December 2010 Published 24 March 2011 Online at stacks.iop.org/JNE/8/025015

Abstract Recently, electroencephalogram-based brain–computer interfaces (BCIs) have attracted much attention in the ﬁelds of neural engineering and rehabilitation due to their noninvasiveness. However, the low communication speed of current BCI systems greatly limits their practical application. In this paper, we present a high-speed BCI based on code modulation of visual evoked potentials (c-VEP). Thirty-two target stimuli were modulated by a time-shifted binary pseudorandom sequence. A multichannel identiﬁcation method based on canonical correlation analysis (CCA) was used for target identiﬁcation. The online system achieved an average information transfer rate (ITR) of 108 ± 12 bits min−1 on ﬁve subjects with a maximum ITR of 123 bits min−1 for a single subject.

(Some ﬁgures in this article are in colour only in the electronic version)

### 1. Introduction

Brain–computer interface (BCI) systems establish a direct communication channel between the human brain and the external environment by translating human intentions into control signals [1], thereby providing a new communication channel to people with severe motor disabilities. Recently, electroencephalogram (EEG)-based brain–computer interfaces have attracted much attention in the study of neural engineering and rehabilitation due to their noninvasiveness. However, the communication speed limits the practical applications of the current EEG-based BCI systems. The information transfer rate (ITR), given in bits per minute, was commonly used to evaluate the communication speed of a BCI [2]. Current BCIs have ITRs of 5–60 bits min−1, which cannot fully meet the requirements of many applications [3].

Recently, BCIs based on visual evoked potentials (VEP) have received increasing attention due to their advantages of little user training, ease of use and high ITR [4]. In our recent study, we proposed a new prototype system based on code modulation VEPs (c-VEP), where binary pseudorandom codes were used to modulate different visual stimuli [5].

1 Author to whom any correspondence should be addressed.

Compared to other types of VEP-based BCIs, the c-VEP BCI has many advantages including increased number of targets (16 targets) and higher ITR (92.8 ± 14.1 bits min−1) [5]. Despite the success of this ﬁrst implementation, the system has many areas for improvement. In this paper, we provide a detailed description of how to build a c-VEP BCI system and propose a multichannel detection approach for improving the identiﬁcation accuracy. Test results for a 32-target online system demonstrate the feasibility and practicality of the proposed system.

### 2. Method

#### 2.1. System conﬁguration

The system consists of an EEG ampliﬁer and a personal computer (PC) with a CRT monitor. The online analysis program and the stimulus presentation program are operated on the PC. Figure 1 depicts the basic structure of the system. The c-VEP BCI system requires a trigger channel in the EEG ampliﬁer, which synchronizes the EEG data and the stimulus. A Synamps2 EEG system (NeuroScan Inc.), which has a parallel port for trigger synchronization, was used in our system.

1741-2560/11/025015+05$33.00 1 © 2011 IOP Publishing Ltd Printed in the UK

Synchronous

||EEG Amplifier|EEG channel<br><br>signal|
|---|---|
| | |
| |Trigger channel|
|Stimulus Presentation|CRT|
|---|---|---|
| | | |

|EEG Amplifier|EEG channel<br><br>signal|
|---|---|
| | |
| |Trigger channel|

Monitor

EEG Signal

|TCP| |
|---|---|
|Online Analysis| |

TCP

PC

Figure 1. The block diagram of the c-VEP BCI.

Visual stimuli were presented on a CRT monitor with a 60 Hz refresh rate. For precise timing control of stimulus presentation, DirectXtechnology(MicrosoftInc.) wasutilized in the stimulus program. A stimulus alternated between two states: ‘light’ and ‘dark’, so a binary sequence can be used as a modulation sequence. ‘Light’ and ‘dark’ were represented as ‘1’ and ‘0’ in the binary sequence respectively. For instance, the stimulus modulated by a periodic sequence ‘100010001000... ’ represents a 15 Hz ﬂickering, when the refresh rate of the monitor is 60 Hz.

As shown in ﬁgure 2(a), 32 targets were arranged as a 4 × 8 matrix surrounded by 28 complementary non-target stimuli. Each target was periodically modulated by a 63bit binary m-sequence. Figure 2(b) presents the modulation sequences of all targets in one stimulus period. Except for a two-frame time lag between two consecutive targets, the used modulationsequencesinoneperiodwerethesamem-sequence for all targets. The arrangement of targets and complementary non-targets, as well as the design of modulation sequence conformed to the principle of equivalent neighbors, will be discussed in section 4.1.

#### 2.2. Target identiﬁcation

The circular-shift relationship between responses of different targets is the basis for target identiﬁcation. Figure 3 illustrates the circular-shift process of target T0 and target T1. At the beginning of each stimulus period of target T0, a synchronous signal was sent to the EEG ampliﬁer. A VEP template for

[Figure 1]

trigger

- Resp. (T0)

- T0
- T1

Ts

- Resp. (T1)

Resp. (T0).

- M0(t)
- M1(t)

(f)

Ts

- (a)
- (b)
- (c)
- (d)
- (e)

Figure 3. An illustration of the circular-shift process. (a) Trigger signal indicates the beginning of each stimulus period of T0. (b) The modulation sequence of target T0. (c) The evoked response of target T0. (d) The modulation sequence of target T1, which has a τs lag of (b). (e) The evoked response of target T1 which can be

thought as τs lag of (c). (f) The template of target T1 can be obtained by shifting the template of target T0 circularly.

target T0 can be obtained by averaging the EEG data from multiple stimulus cycles. The length of the template was Ts = 63/60 = 1.05s, which equals the length of a stimulus cycle. Once the template for T0 was obtained, templates for other targets can be easily obtained by shifting the template for T0 circularly. In our system, the time lag between two consecutive targets was τs = 2/60 = 0.033s. Hereafter, the target for the calculation of the ﬁrst template is referred to as the reference target, and its template as the reference template. In practice, any target can be selected as the reference target.

[Figure 2]

(a) (b)

Figure 2. (a) The target arrangement of the c-VEP-based BCI. The 32 targets distributed as a 4 × 8 array (the gray area in the center of the screen) surrounded by 28 complementary ﬂickers (white background). The digit on a target indicated the index of the target. A complementary non-target was synchronized with the target that had the same digit. (b) The modulation sequences of 32 targets in one stimulation cycle. All targets were activated simultaneously, and the stimulation cycle was repeated constantly. There was a two-frame time lag between two consecutive targets.

#### 2.3. Multichannel processing

[Figure 3]

In our previous study [5], an exhaustive method was used for selecting the optimal bipolar channel [5]. The Oz channel, which had the highest VEP amplitude, was ﬁxed as signal channel, and the bipolar reference channel, which maximized training accuracy, was selected from the remaining channels.

A multichannel method can improve the identiﬁcation accuracy of VEP BCIs [6, 7]. Canonical correlation analysis (CCA) is a multichannel data processing approach that has been successfully used in the SSVEP BCI [6]. Here, we proposed a similar method for the c-VEP BCI.

In the training stage, the user is required to ﬁxate on the reference target, and multichannel EEG data within k stimulus cycles are collected as X. Averaging the segments of data from the k stimulus cycles, the multichannel evoked response R can be obtained.

- Figure 4. An example of target identiﬁcation. The data to be identiﬁed was recorded during gazing at target T21 and the red star indicated the identiﬁcation result.

The signal component S of the original EEG data can be obtained by replicating the evoked response R k times:

After obtaining templates for all targets, a template matchingmethodcanbeusedfortargetidentiﬁcation. Figure4 shows the framework of the template matching process. The steps of the target identiﬁcation process are as follows.

- (1) In the training stage, the user is required to ﬁxate on the reference target. In our experiment, the reference target is target T20. EEG data within N stimulus cycles are collected as xn(t),n = 1,2,...,N.
- (2) A reference template Mr(t) is obtained by averaging over k cycles. In our experiment, the reference template is the template for T20, i.e. M20(t):

M20(t) =

1 N

N

n=1

xn(t). (1)

- (3) The templates of all targets are obtained by shifting the reference template: Mk(t) = M20(t − (τk − τ20)) k = 0,1,2... ,31 (2)

where τk −τ20 indicates the time lag between target k and the reference target T20.

- (4) For a segment of EEG data x(t), the correlation coefﬁcient ρk between x(t) and the template Mk(t) is calculated as

ρk =

Mk(t),x(t) √ Mk(t),Mk(t) x(t),x(t)

(3) where x, y indicates the product of x and y.

- (5) The ﬁxation target is identiﬁed by selecting the target that maximizes the correlation coefﬁcient.

Target identiﬁcation was performed using an online analysis program developed using Microsoft VC++. A synchronous trigger signal indicating stimulus onset initiates accumulation of EEG data in a buffer. Data are accumulated throughout the stimulus period, followed by target identiﬁcation. The identiﬁcation result is then sent to the stimulus presentation program through TCP/IP and visual feedback is provided by highlighting the identiﬁed target. Feedback presentation and shifting of gaze to the next target occurs throughout the subsequent stimulus period. Data collected in this period is discarded.

S = [R R ··· R]. (4)

In this case, the CCA method can be employed to optimize the system. This involves ﬁnding linear transformations Wx and Ws which maximize the correlation between projected X and S [6]:

WxT XST Ws WxT XXT Wx · WsT SST Ws

. (5)

Max

Wx,Ws

In practice, we use Wx as spatial ﬁlter coefﬁcients for online data processing. In our system, nine electrodes over the occipital region (O1, Oz, O2, P3, Pz, P4, PO7, POz, and PO8) were selected.

#### 2.4. Experiment and data

Two systems with 16 targets and 32 targets were tested separately. Five healthy adults with normal or corrected-tonormal vision participated in the experiment after giving their informed consent. They were randomly selected from subjects with experiences in BCI experiments. For each system, the experiment was divided into a training stage and a testing stage. In the training stage, subjects were required to ﬁxate on the reference target for about 200 stimulus periods. Data from the training stage was used for ofﬂine analysis to calculate the spatial ﬁlter weights and the reference template for online use. In the testing stage, each subject was asked to input a sequence of 64 characters. The online accuracy and corresponding ITR were used for evaluating the system performance. In the calculation of ITR, the time cost of each selection is 2.1s (including two stimulus periods, one for data acquisition and one for target identiﬁcation, feedback presentation and gaze shifting).

A dataset involving 12 subjects from our previous study was used for testing the performance of the multichannel method [5]. The EEGsignals weremeasured from47 channels located over parietal-occipital cortex in the training stage of the 16-target c-VEP BCI.

[Figure 4]

[Figure 5]

|+7τs|+8τs|+9τs|
|---|---|---|
|+τs|T|−τs|
|−7τs|−8τs|−9τs|

(a) (b)

- Figure 5. Illustrations of the principle of equivalent neighbors. (a) The blue boxes marked the two targets (T9 and T30) and the boxes of the red dash line indicated the eight neighbors of the two targets. (b) The time lags between the neighbors and the target (the symbol ‘+’ indicates ‘ahead’, the symbol ‘−’ indicates ‘behind’). For example the left neighbor of T9 was T8 which has a time lag of τs ahead of T9. So the time lag of the left neighbor is +τs.

Table 1. Comparison between two identiﬁcation methods.

Accuracy of Accuracy of Subject bipolar method multichannel method

- S1 0.91 0.99
- S2 0.98 0.99
- S3 0.98 0.98
- S4 0.98 0.97
- S5 0.92 0.95
- S6 0.98 0.97
- S7 0.99 0.98
- S8 0.79 1.00
- S9 0.95 0.96
- S10 0.96 0.99
- S11 0.93 0.98
- S12 0.98 1.00 Mean 0.95 ± 0.05 0.98 ± 0.02

### 3. Results

Table 1 compares the training accuracy of the optimal bipolar method and the multichannel method for each subject. The average training accuracy of the multichannel method is signiﬁcantly higher than the optimal bipolar method at the 10% signiﬁcance level (mean: 95% versus 98%, p = 0.06).

Table 2 lists the test results of the two c-VEP BCI systems. Although the online accuracy of the 32-target system is lower than the 16-target system (85 ± 5%, versus 92 ± 3% p = 0.04), the ITR of the 32-target system outperforms the 16-target system (108 ± 12.0 bits min−1 versus 96 ± 6.3 bits min−1,

p = 0.08). For a single subject, a maximum ITR of 123 bits min−1 was achieved in the 32-target system.

### 4. Discussion

#### 4.1. Principle of equivalent neighbors

In a c-VEP BCI, the arrangement of targets satisﬁes a principle of equivalent neighbors. Figure 5 illustrates the principle. As shown in ﬁgure 5 (a), a central target has eight neighboring targets (e.g., T9). With the inclusion of complementary nontargets, a peripheral target also has eight neighbors consisting of some targets and some complementary non-targets (e.g., T30). For each target, all neighbors keep ﬁxed time lag relationships (ﬁgure 5 (b)). For example, the stimulus sequence of the left neighbor always has a time lag of τs ahead of the target sequence; the stimulus sequence of the bottom neighbor always has a time lag of 8τs behind of the target sequence, and so on.

A previous study indicated that stimuli outside the foveal visual ﬁeld can also contribute to VEP [9]. Therefore, the c-VEP combines evoked responses to the target as well as its neighbors. According to the principle of equivalent neighbors, c-VEPs corresponding to different targets are equivalent except for the time shift. Thus, unlike SSVEP BCIs, no gap is required between stimuli, allowing us to place a larger number of targets within a given area.

Table 2. Performance of the c-VEP BCIs.

System of 16 targets System of 32 targets Subject Training accuracy Online accuracy ITR (bits min−1) Training accuracy Online accuracy ITR (bits min−1)

- S13 0.99 0.88 87 0.95 0.86 109
- S14 0.95 0.92 97 0.97 0.92 123
- S15 0.95 0.91 93 0.90 0.80 96
- S16 0.99 0.95 104 0.88 0.80 96
- S17 0.97 0.94 98 0.95 0.89 116 Mean 0.97 ± 0.02 0.92 ± 0.03 96 ± 6.3 0.93 ± 0.04 0.85 ± 0.05 108 ± 12.0

the visual system is not a linear system. Thus, by further elucidating the encoding/decoding mechanisms of the visual pathway, it may be possible to ﬁnd an optimal sequence that would further improve performance of the c-VEP BCI system.

#### 4.2. Information transform rate

In 1984, Sutter ﬁrst reported the design of a c-VEP BCI with 64 targets [8]. A later publication applied this system to a singlepatientwithimplantedelectrodesandreportedaspelling speed of 10 to 12 words/min. [9]. However, performance was not evaluated for non-invasive EEG. Moreover, because the system needed a specially designed hardware platform, which included a display generator, a processor and an ampliﬁer module, the application of the system was limited. In our previous study, the c-VEP BCI system with 16 targets achieved a mean ITR of 92.8 ± 14.1 bits min−1 [5]. In this study, the ITR of the c-VEP BCI was further improved to 108.0 ± 12.0 bits min−1 due to the employment of more targets and the multichannel identiﬁcation method. To our knowledge, the proposed system represents the fastest EEG-based BCI reported to date.

### 5. Conclusion

In this paper, the basic principle and implementation of a high-speed c-VEP BCI system are described in detail. The proposed c-VEP BCI shows a high ITR of 108 ± 12.0 bits min−1, exceeding the previous record of EEGbased BCIs [3]. We believe that our progress will accelerate the development of BCI products that meaningfully contribute to helping the severely disabled.

### Acknowledgment

As shown in table 2, the average ITR of the 32-target system is signiﬁcantly higher than the 16-target system (108 bits min−1 versus 96 bits min−1). For subjects s13, s14 and s17, the increment is around 20 bits min−1. However, there is no obvious difference for the other two subjects between the two systems (93 bits min−1 versus 96 bits min−1 and 104 bits min−1 versus 96 bits min−1 for s15 and s16 respectively). The online accuracy of the two subjects dropped signiﬁcantly when using more targets (91% and 95% in the 16-target system versus 80% in the 32-target system). The decrease of the accuracy may be caused by a non-sharp autocorrelation function of the template. The time lag between two consecutive targets for the 32-target system and the 16target system is 2 frames (33.3 ms) and 4 frames (66.7 ms) respectively. Thus, when the autocorrelation function of the template is not sharp enough, the target may be more easily misidentiﬁed for shorter time lags.

This work was supported by the National Basic Research Program of China (Grant No 2011CB933204) and National Natural Science Foundation of China (Grant No 90820304). The authors would like to thank Tin Mullen for his careful proofreading of the manuscript.

### References

- [1] Wolpaw J R, Birbaumer N, McFarland D J, Pfurtscheller G and Vaughan T M 2002 Brain–computer interfaces for communication and control Clin. Neurophysiol. 113 767–91
- [2] Wolpaw J R, Ramoser H, McFarland D J and Pfurtscheller G 1998 EEG-based communication: improved accuracy by response veriﬁcation IEEE Trans. Rehabil. Eng. 6 326–33
- [3] Tonet O, Marinelli M, Citi L, Rossini P M, Rossini L, Megali G and Dario P 2008 Deﬁning brain-machine interface applications by matching interface performance with device requirements J. Neurosci. Methods 167 91–104
- [4] Wang Y, Wang Y, Gao X, Hong B, Jia C and Gao S 2008 Brain-computer interfaces based on visual evoked potentials: feasibility of practical system designs IEEE EMB Mag. 27 64–71
- [5] Bin G, Gao X, Wang Y, Hong B and Gao S 2009 Research frontier: VEP-based brain–computer interfaces: time, frequency, and code modulations IEEE Comput. Intell. Mag. 4 22–6
- [6] Bin G Y, Gao X R, Yan Z, Hong B and Gao S K 2009 An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method J. Neural Eng. 6 046002
- [7] Friman O O, Volosyak I and Graser A 2007 Multiple channel detection of steady-state visual evoked potentials for brain–computer interfaces IEEE Trans. Biomed. Eng. 54 742–50
- [8] Sutter E 1984 The visual evoked response as a communication channel IEEE Trans. Biomed. Eng. 31 583
- [9] Sutter E 1992 The brain response interface-communication through visually induced electrical brain responses J. Microcomput. Appl. 15 31–45
- [10] Wolfmann J 1992 Almost perfect autocorrelation sequences IEEE Trans. Inf. Theory 38 1412–8

#### 4.3. Further improvement

The screen refresh rate inﬂuences the system performance. On one hand, a decrease of the refresh rate will increase the length of a stimulus cycle, leading to a reduction of ITR. On the other hand, an increase of the refresh rate can intensify the nonlinearity between the stimulus sequence and the evoked potential [8]. Therefore, optimizing the screen refresh rate may improve system performance.

The selection of the stimulus sequence isanother direction for future work. In the c-VEP BCI system, a visual evoked response with a sharp autocorrelation function is expected. In previous studies [5, 8, 9], m-sequences were generally utilized for their good auto-correlation properties. The system performance might be improved when using other sequences with good autocorrelation properties (e.g. almost perfect sequences [10]). In fact, a sequence with a sharp autocorrelation function cannot ensure the same sharpness of the autocorrelation function of the evoked potential since

