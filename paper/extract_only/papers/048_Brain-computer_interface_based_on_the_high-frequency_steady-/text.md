[Figure 1]

2005 First International Conference on Neural Interface and Control Proceedings; 26-28 May 2005; Wuhan, China

## Brain-computer Interface based on the High-frequency Steady-state Visual Evoked Potential

### WANG Yijun, WANG Ruiping*, GAO Xiaorong, Member, IEEE, GAO Shangkai,SeniorMember, IEEE

Departmentof Biomedical Engineering, School ofMedicine, Tsinghua University, Beijing, China

Abstract-Low-frequency steady-state visual evoked potentials (SSVEPs)are used as the input signal in the present SSVEP-based brain-computer interface (BCI). This prototype system has a high information transfer rate. On the other hand, it has some limitations including visual fatigue, false positive, and some possibility of causing a seizure. These drawbacks can be largely eliminated when using high-frequency stimulations. In this paper, we study the amplitude versus stimulation frequency response of SSVEPs. The signal-to-noise ratio versus frequency curve suggests that the high-frequency SSWP (>20Hz)could help to construct a practical BCT system.

the above disadvantages, we attempt to employ it as the communication medium in BCI research, though the system performance may be decreased due to a lower amplitude response and a restricted topographical distribution.

##### 11.METHODOLOGY

###### A. Data acquisition

13 volunteers with normal vision (5 female and 8 male) participated in the experiments. The subjects sat in a comfortable chair facing the visual stimuIus device. White light-emitting diodes (LEDs) were used as' the blinking buttons. The flashing frequency of each LED was controlled by a programmable logic device [6].44-channel EEGs were recorded with a BioSemi ActiveTwo system at positions of the extended international 10/20 system. The repetition rates of stimulation covered the bandwidth from 21to 43Hz (2Hz each step). For one subject, the stimulation frequency band was from 5 to 45Hz,including both IOWand high frequency bands for comparison. 60-second-long data in each session corresponding to different frequencies were acquired for offline analysis. Signals were sampled at 256Hz. During periods between sessions, subjects couid relax in order to eliminate the reaction of visual fatigue.

Keywords-Brain-computer interface (BCI), steady-state visual evoked potential (SSVEP)

I. INTRODUCTION

Brain-computer interfaces (BCIs) translate brain signals into a control signal without using muscles or peripheral nerves. Most BCIs use noninvasive scalp electroencephalogram (EEG) signals as inputs. Eventrelated potentials, mu and beta rhythms, event-related synchronization and desynchronization + slow cortical potentials , and visual evoked potentials are common signals used in EEG-basedBCIs [1][2][3].

Visual evoked potentials (VEPs) recorded from scalp over visual cortex reflect the visual information processing mechanism in the brain. The steady-state visual evoked potential (SSVEP), which is characterized as an increase in amplitude at the stimulus frequency, occurs when stimulation frequency is higher than 6Hz. Current SSVEPbased BCIs harness low-frequency SSVEPs to determine gaze directions [4][5]. Several frequency-coded buttons flash on the monitor. The user looks at a button and the system determines the frequency of the photic driving response. The button, which matches the detected frequency,

###### B. Ofline analysis

The feasibility of using the high-frequency SSVEP in BCI application is considered through offline data analysis. We compare the signal-to-noise ratio of SSVEPs in different frequency bands. The detailed procedures are described in three stepsas follows:

1) Determine optimal electrode positions according to the spatial signal-to-noise ratio mapping of multichannel

EEGs.

is the target the user wants to select. This BCI has the following advantages: high information transfer rates, wide subject applicability, and little training required for users.

In order to detect the frequency components in SSVEPs accurately and conveniently during online applications, an optimal bipolar lead with high signal-to-noise ratio should be selected. In practice, channel with the most significant amplitude of SSVEP is considered as the signal channel which commonly locates over visual cortex. The difficulty is to select a reference channel for the bipolar lead. A correct choice of reference channel can greatly enhance the signal-to-noise ratio. A comprehensive consideration must be taken for optimal lead selection [71.

The low-frequency SSVEP has a good signal-to-noise ratio (SNR), a wide distribution over the scalp, and it can be induced easily, but it also has some unavoidable limitations. First, visual fatigue evoked by durative stimuli will reduce the amplitude ofresponse and make the user uncomfortable. Second, alpha rhythm (8-13Hz) of spontaneous EEG may cause false positive. Additionally, flickering stimuli have some possibility of causing a seizure in subjects. Considering that the high-frequency SSVEP can eliminate

Signal-to-noise ratio is used as the criterion to evaluate the efficiency of lead selection. The amplitude spectrum is

###### 0-7803-8902-6/05/$20.00Q2005 XEEE 37

[Figure 2]

3) Compare the signal-to-noise ratios of different frequency regions and select the usable high-frequency bands for online application.

calculated by y=(FFT(x)l, where x is the temporal EEG data. FFT(x) is the 1024-point fast Fourier transform (FFT) of x, and the fi-equency resolution is 256/1024=0.25Hz. Here, when the stimulation frequency isf ; signal-to-noise ratio is defined as the ratio of yv> to mean value of the n adjacent points:

The lower amplitude response may decrease the signalto-noise ratio if the amplitude of background noise is unchanged. Fortunately, the noise, i.e. spontaneous EEG, also decreases in higher frequency bands. So the signal-tonoise ratios of the three subsystems are almost on the same level (as shown in Fig.3). Offline frequency detection in higher frequency region has been done on this subject. The frequency corresponding to the maximum of amplitude spectra should be the stimulation frequency when the detection is accurate. The length of data section for FFT is 1024 points, and the frequency resolution is 0.25Hz. The detection accuracy is about 97% when the stimulation frequencies are in the medium-ftequency region (31-35Hz).

SNR = a , 2 n x v ( f )

# 1[y(fi-0.25xk)+y(f -0.25xk ) ]

k -1

It can approximately reflect the signal-to-noise ratio of the SSVEP. Fig.1 illustrates the SNR mappings with different reference channels of one subject when the stimulation frequency is 21Hz. An optimal bipolar lead including a signal channel and a reference channel can be determined with the aid of these mappings. First, we use Fig.f(a), i.e. the SNR mapping with Cz as reference, to select the signal channel. According to Fig.l(a), Oz, the channel with the highest SNR, is selected as the signal channel with prominent SSVEP.Next, as shown in Fig.l(b), the SNR mapping with reference to the selected signal channel Oz is displayed to find the reference channel. The channel with the highest SNR is considered as the reference channel. The arrow indicates the selected optimal lead.

In the high-frequency region (39-45Hz), the average accuracy remains as 95%. The total usable bandwidth is about 1OHz, leading to about 40 targets at most.

For the other subjects, we analyze the SSVEPs with the stimulation frequencies from 21 to 43Hz. With the proper selection of electrode position and stimulation frequency bands, the average accuracy of all the 13 subjects is about 96%.The results of the individual are listed in Table I.

2) Plot the amplitude versus frequency response curve through amplitude spectra analysis.

4.5 .................... e...*............ :.~........j............. j.. -:*mi: FW9

5

i * ~ngim~vnlue

According to human brain electrophysiological research, the amplitude of the SSVEP varies in a complex manner with the frequency of stimulation. The amplitude response has several peaks with three regions, often referred to as subsystems [81: low-frequency region, medium-frequency region, and high-frequency region, The amplitudes of subsystems depend on many factors including electrode position, luminance, and flicker modulation depth. The amplitude versus frequency response curves for the three SSVEP subsystems of one subject are shown in Fig.2. EEG data of the optimal lead are used to calculate the amplitude response through amplitude spectra analysis. Filled dots indicate the original results and solid lines denote the polynomial fitting results. The three subsystems are centered on 15Hz-low frequency, 31Hz-medium frequency, and 41Bz-high frequency, respectively. The lower frequency region has the larger amplitude response.

Stimulatlon Frequency (Hr)

Fig2 The three SSVEPsubsystemsof one subject.

Fig.1. SNR mappingswith reference IO (a) Cz and (b)Oz respectively.

###### 38

[Figure 3]

N is the number of targets and P is the accuracy of target selections. B multiplied by selecting speed is the transfer rate (bits per minute) [ I ] . Assume that there are 8 visual targets, selection is performed every 4s, the expected information transfer rate of the online system could exceed 30bitdm ifthe detection accuracy is 90%.

: -PolyncunialFilling

5

: 4 onginalvaiue

4.6-........... i......... ..........;............. i............. i............<........... ..i.............

‘r

Other effective signal processing methods for enhancing signal-to-noise ratio, e.g.adaptive filtering, could be used in future systems. The system parameters such as electrode position, number of targets, stimulation frequencies, and operating speed, should be optimized for each user individually. To implement a practical BCI, a higher information transfer rate should be expected, and moreover, the research on a portable system realized with digital signal processor is ongoing.

i i 1

1.51 5-.................. ;......... .i~........ jj...................... jj ....... ii............. ii.....................

mmulation Frequency(Hz)

###### ACKNOWLEDGMENT

Fig.3. SNR curves corresponding to the three SSVEP subsystems.

The project is supported by National Natural Science Foundation of China (#60318001) and the Key Project of ChineseMinistry of Education (NO. 1041185).

TABLEI

OFFLIh’EANALYSIS RESULTS OF ALL SUBJECTS

Subjects FrequencyBands(Hz) Accuracy (%)

REFERENCES

CSQ 31 -37 97 css 27 * 35 99 LH 21 * 27 90 LL 21-31 100 LY 23-37 100 NTS 27 - 43 100 S Z I 31 -37,41-43 95

J.R. Wolpaw, N. 3irbaumer, D.J. McFarland, G Pfurtscheller, T.M. Vaughan, “Braincomputer interfaces for communication and control,” Clin.Neurophysiol.,vo1.113,pp.767-791,2002.

T.M. Vaughan, W.J. Heetderks, L.J. Trejo, “Brain-computer interface technology: a review of the second international meeting,”1EE.E Trans. N e ~ Systd Eng. vol.] I , pp.94-109,2003 B. Blankertz, K. R. Muller, G Curio, T.M. Vaughan, G Schalk, J. R. Wotpaw, A. Schloegl, C. Neuper, G Pfurtscheller, T.

WH 21 -43 . 100

WMH 31 - 43 100

ww 31-35,39*45 96

Hinterberger, M. Schroeder, and N. Birbaumer, “The BCI Competition 2003”, IEEE Trum Biomed. Eng., vo1.51, pp.10441051,2004

YH 21 - 21 76 YJ 31- 35,39-43 100 YY 21 -23,33-43 95

M. Cheng, X. Gao, and S . Gao, “Design and implementation of a brain-computer interface With high transfer rates,” IEEE 7f.ans. Biomed. Eng.,vo1.49,pp.118t-1186,2002.

Mean 96

M. Middendorf, G McMillan, G Calhoun, and K. S. Jones, “Brain-computer interfaces based on the steady-state visualevoked response,” IEEE Trans. Rehab. Eng., vo1.8, pp.211-214, 2000

111. CONCLUSION AND DtSCUSSION~

- X. Gao, D. Xu, M. Cheng, and S. Gao, “A BCI-based environmental controller for the motiondisabled,” IEEE Trans. Rehab. Eng., vol.II, pp.137-140,2003
- Y . Wang, 2. Zhmg, X. Gao, and S. Gao, “Lead selection for

Our results suggest that the high-frequency SSVEPhas a lower background noise as well as a lower amplitude response, so it has a signal-to-noise ratio almost the same as the low-frequency SSVEP. The offline analysis demonstrates that the high-frequency SSVEP could be employed as a good medium in SSVEP-based BCIs. With great decrease of visual fatigue, possibility of causing a seizure, and interference of alpha rhythm, it makes the SSVEP-based BCI a more comfortable and stabIe system.

SSVEP-based brain-computer interface,” fmc. 26th h r , lEEE D. Regan. “Evoked potentials and evoked magnetic fields in science and medicine,” Elsevier, 1987

EMES C O ~pp. 4507I -4510,2004

###### Correspondingauthor:

*WANG Ruiping is with the Department of Biomedical Engineering, Tsinghua University, Beijing 100084,China. (E-mail: wrp@mail.tsinghua.edu. cn)

The standard method for measuring BCI performance is information transfer rate. It is the amount of information communicated per unit time. The bit rate (B) of each selection can be expressedas

B=log, fv+Plog, P+(I-P) log,[(l-P)/(N-I)]

#### 39

