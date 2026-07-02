# arXiv:2604.09649v1[cs.HC]29Mar2026

## Short Paper: WearBCI Dataset: Understanding and Benchmarking Real-World Wearable Brain-Computer Interfaces Signals

Haoxian Liu, Hengle Jiang, Lanxuan Hong, Xiaomin Ouyang∗

Hong Kong University of Science and Technology Hong Kong SAR, China hliueu@connect.ust.hk,hjiangbg@connect.ust.hk,lhongae@connect.ust.hk,xmouyang@cse.ust.hk

### Abstract

Brain-computer interfaces (BCIs) have opened new platforms for human-computer interaction, medical diagnostics, and neurorehabilitation. Wearable BCI systems, which typically employ noninvasive electrodes for portable monitoring, hold great promise for real-world applications, but also face significant challenges of signal quality degradation caused by motion artifacts and environmental interferences. Most existing wearable BCI datasets are collected under stationary or controlled lab settings, limiting their utility for evaluating performance under body movement. To bridge this gap, we introduce WearBCI, the first dataset that comprehensively evaluates wearable BCI signals under different motion dynamics with synchronized multimodal recordings (EEG, IMU,and egocentric video), and systematic benchmark evaluations for studying impacts of motion artifact. Specifically, we collect data from 36 participants across different motion dynamics, including body movements, walking, and navigation. This dataset includes synchronized electroencephalography (EEG), inertial measurement unit (IMU) data, and egocentric video recordings. We analyze the collected wearable EEG signals to understand the impact of motion artifacts across different conditions, and benchmark representative EEG signal enhancement techniques on our dataset. Furthermore, we explore two new case studies: cross-modal EEG signal enhancement and multi-dimension human behavior understanding. These findings offer valuable insights into real-world wearable BCI deployment and new applications1.

• Computing methodologies → Machine learning; • Humancentered computing → Ubiquitous and mobile computing; • Computer systems organization → Embedded and cyber-physical systems.

CCS Concepts

### Keywords

Wearable BCI System, EEG Signal Enhancement, Multimodal Sensing, Motion Artifacts

∗Corresponding author 1The dataset and code are available at: https://github.com/HKUST-MINSysLab/WearBCI-Dataset.

ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. SenSys ’26, Saint Malo, France

© 2026 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-2309-4/2026/05 https://doi.org/10.1145/3774906.3802782

###### ACM Reference Format:

Haoxian Liu, Hengle Jiang, Lanxuan Hong, Xiaomin Ouyang. 2026. Short Paper: WearBCI Dataset: Understanding and Benchmarking Real-World Wearable Brain-Computer Interfaces Signals. In ACM/IEEE International Conference on Embedded Artificial Intelligence and Sensing Systems (SenSys ’26), May 11–14, 2026, Saint Malo, France. ACM, New York, NY, USA, 8 pages. https://doi.org/10.1145/3774906.3802782

### 1 Introduction

EEG-based brain-computer interfaces (BCIs) have enabled applications in human-computer interaction [4, 18], neurorehabilitation [12, 22, 29], and medical diagnostics [42, 43]. However, conventional BCI systems are expensive and require complex electrode setup, making them impractical for long-term use in natural daily environments. To overcome these limitations, wearable BCIs have emerged as a promising technology by providing non-invasive and portable solutions for applications like attention regulation [8, 15], sleep monitoring [2, 13, 20], and stroke rehabilitation [33].

Despite their promise, wearable BCIs still face major challenges for real-world deployment. Wearable BCI systems are highly vulnerable to motion-induced artifacts: facial and scalp muscles generate strong EMG signals that overlap with neural activity, and body movements cause subtle electrode shifts, disrupting skin contact and increasing impedance, introducing voltage jumps that degrade signal quality [11, 24]. However, existing wearable BCI datasets are largely collected under stationary, controlled conditions (e.g., sitting or resting), overlooking movement and environmental variability. This gap limits the development and evaluation of wearable BCI systems for everyday scenarios.

In this paper, we present WearBCI, the first dataset that comprehensively evaluates wearable BCI signals under different motion dynamics with synchronized multimodal recordings (EEG, IMU, and egocentric video), and systematic benchmark evaluations for studying impacts of motion artifact. To systematically assess the impact of motion on EEG signal quality, we designed experiments at three levels of motion intensity: body movements, walking, and navigation. The dataset includes recordings from 36 participants, consisting of approximately 17 hours of EEG, 10 hours of IMU, and 1 hour of egocentric video data. The video recordings are collected only during the navigation session, while EEG and IMU are available across all motion sessions.

We then analyze the impact of motion conditions on EEG signal quality using time-domain features, power spectral density (PSD), and topographic maps across brain regions. Results show that EEG signals remain stable under mild movement, but stronger acceleration introduces larger time-domain fluctuations and broadband

spectral elevation. Different actions also affect distinct scalp regions, highlighting the need for motion- and region-aware processing. To benchmark existing EEG enhancement methods under motion conditions, we apply six representative approaches on our dataset: three traditional methods, including Independent Component Analysis (ICA), Empirical Mode Decomposition (EMD), and Artifact Subspace Reconstruction (ASR), and three deep learning models (GAN, Transformer, and Diffusion-based). Results show that classical methods degrade as motion intensity increases, while deep models better restore spectra but risk suppressing neural signals. Moreover, analysis across different navigation scenes shows that abrupt behaviors, such as obstacle avoidance, introduce more severe distortions than smoother actions.

###### # of Channels

###### Signal Quality Interference

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

More Channels

Higher SNR

Controlled Setting

Traditional BCIs

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

Wearable BCIs

Sparse Channels Lower SNR

Motion/Noise

##### Figure 1: Comparison of traditional and wearable BCIs.

However, both datasets focus on task-specific settings without systematic variation of body motion. Overall, most existing datasets are collected under stationary or controlled conditions, and none systematically study how different motion dynamics degrade wearable EEG with synchronized IMU and egocentric video. WearBCI addresses this gap by providing the first multimodal dataset designed specifically for benchmarking motion artifact analysis and EEG enhancement under different motion dynamics.

To further showcase new applications enabled by our dataset, we present two case studies. The first case study explores how additional sensor modalities, such as IMU signals, can assist in enhancing EEG quality under motion conditions. The second case study motivates the practical value of the WearBCI dataset by demonstrating application scenarios like comprehensive human behavior understanding enabled by multimodal signals. These findings highlight the potential of our dataset for addressing challenges in real-world deployment with various motion artifacts and enable new applications of wearable BCI systems.

### 3 Background and challenges

- • We introduce the first multimodal wearable BCI dataset with synchronized recordings (EEG, IMU, and egocentric video) from 36 subjects across different motion dynamics, covering body movements, walking, and navigation.
- • We benchmark the collected wearable EEG data by evaluating the impact of various artifacts across sessions and assessing representative EEG enhancement methods, providing insights for motion-aware wearable BCI applications.
- • We conduct two case studies including cross-modal EEG signal enhancement using complementary sensor modalities such as IMU, and multi-dimensional behavior analysis using multimodal data and large language models.

In summary, we make the following key contributions:

In this section, we compare traditional and wearable BCI systems, highlighting key challenges of using wearable EEG in real-world environments (Figure 1).

Sparse Electrode Channels. Wearable BCIs typically use 1-8 dry electrodes on frontal or occipital areas [48], allowing quick setup but limiting spatial resolution and brain coverage. In contrast, traditional systems deploy 21-256 wet electrodes [34] for full-head monitoring, but require 20-60 minutes for setup and adjustment [46], making them less suitable for real-world deployment.

Lower SNR. Signal quality is another major challenge. Traditional BCIs use wet electrodes with low impedance (<20 kΩ), yielding high-fidelity signals [14], whereas wearable systems use dry electrodes at the cost of increased impedance and reduced SNR due to greater susceptibility to noise and contact instability [35].

Susceptibility to Interference. Wearable BCIs are highly vulnerable to motion-induced artifacts. Facial and scalp muscles generate strong EMG signals that overlap with neural activity, while body movements cause subtle electrode shifts that disrupt skin contact, increase impedance, and introduce voltage jumps that degrade signal quality. In contrast, traditional BCIs operate in controlled environments with stable wet-electrode contact, making them far less susceptible to such interference.

### 2 Related Work

EEG-Based BCI Systems. EEG-based BCIs provide signals with high temporal resolution, valuable for identifying biomarkers of neurodegenerative diseases like Alzheimer’s [7, 10, 30] and Parkinson’s [25, 44], and for neurofeedback in rehabilitation [22, 29]. However,traditionalsystemsoftenrequirecomplex,invasivesetup, limiting their practicality in daily environments. Wearable BCIs overcome these barriers with portable solutions for attention tracking [8, 15, 39], sleep monitoring [2, 13, 20], and motor rehabilitation [5, 37], despite remaining prone to motion artifacts and bioelectrical interferences [19, 21].

### 4 WearBCI Dataset Collection 4.1 Experiment Setup

Wearable BCI Datasets. A growing number of wearable BCI datasets have been collected for diverse applications. BCIC IV 2b [23] and MILimbEEG [6] target motor control and rehabilitation, while AMIGOS [26] and Emognition [36] combine EEG with GSR for emotion recognition. For multimodal datasets, MOCAS [17] captures EEG, PPG, GSR, and video data during anomaly detection tasks, and MPDB [41] collects EEG, ECG, EMG, GSR, and eye movement data in a driving simulator for behavior classification.

Devices and collected data. EEG data were collected using the OpenBCI Cyton board [1] with eight dry electrodes positioned at Fp1, Fp2, P7, P8, T3, T4, O1, and O2 (reference and ground at A1 and A2), following the 10-20 system [28]. The overall setup is illustrated in Fig.2a. Electrode impedance was maintained below 50 kΩ.Asdryelectrodesundermotionconditionsarepronetocontact changes that increase impedance, we check the impedance before each session type and reposition the electrodes when it exceeded

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

Subjects 36 healthy adults (18 - 26 yrs), balanced gender ratio Total Duration EEG: 16.4 h, IMU: 9.2 h, Video: 0.9 h Modalities 8-ch EEG (250 Hz), 5 IMUs (100 Hz), egocentric video (30 FPS) Sessions Static, Body Movements (5 types), Walking (3 speeds), Navigation

[Figure 15]

Eight Dry Electrodes

Eight Dry Electrodes

Cognitive Task Guidance System

Cognitive Task Guidance System

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

EEG Data

[Figure 20]

EEG Data

Gyro Data (3 axis)

##### Table 1: Summary of the WearBCI Dataset.

[Figure 21]

Reference Electrodes

Gyro Data (3 axis)

[Figure 22]

Reference Electrodes

[Figure 23]

[Figure 24]

Acc Data (3 axis)

[Figure 25]

Camera

Five IMUs

[Figure 26]

Camera

collected during navigation. To reduce cognitive variability, participants were instructed to remain relaxed during the first three sessions; in the navigation task, cognitive load was kept minimal despite simple spatial decisions (e.g., turning or stopping).

Acc Data (3 axis)

Cyton Board and Five IMUs Dongle Receiver

Cyton Board and Dongle Receiver

Egocentric Video Data

(a) Experimental setup.

(b) Data.

Static baseline. EEG was recorded while participants sat still to establish a physiological reference. Participants performed eyesopen and eyes-closed tasks lasting two minutes, each repeated three times.

Egocentric Video Data

###### Static Movements Walking Navigation

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

Body movements. This session examined the influence of smallscale body and facial movements on EEG. Prior wearable EEG literature [3, 38] has identified a broad set of motion types that introduce artifacts, covering head motions, eye actions, and upper-body movements. From this set, we selected five representative actions: head shaking, head nodding, eye movement, arm stretching, and typing, allowing isolated examination of how different body parts affect distinct scalp regions. Each action followed 10-second cycles of baseline, motion, and post-motion, repeated three times.

(c) Illustration of different experiment sessions.

- Figure 2: Overview of the WearBCI experimental setting and recorded multimodal data.

50 kΩ. IMUs were placed on the head, wrists, and ankles for motion artifact analysis, and egocentric video was recorded during navigation. All data streams were synchronized using the Network Time Protocol (NTP) to establish a common time reference, with EEG recorded at 250 Hz, IMU at 100 Hz, and egocentric video at 30 FPS, each accompanied by Unix timestamps. Post-processing aligns all streams through timestamp-based interpolation. Preprocessing included a 1 Hz high-pass filter for slow drift removal, a 45 Hz low-pass filter for high-frequency noise, and ICA-based artifact removal. Due to the limited 8 channels, ICA was restricted to 8 components, so only the most prominent 1-2 artifact components were removed to preserve signal fidelity. Due to technical issues, data from 3 participants in the walking session and 4 participants in the navigation session were excluded from analysis. Occasional packet loss resulted in missing IMU samples across several recordings. Table 1 summarizes the dataset statistics.

Walking. This session evaluated the effect of continuous walking on EEG. Participants walked at speeds of 2, 3, and 4 km/h, representing slow, moderate, and brisk pedestrian movement to examine how gait intensity affects signal degradation, with two minutes per trial and two-minute rest periods between trials. Baseline recordings were collected under standing conditions as reference. Natural navigation. This session recorded neural activity during navigation tasks in an indoor setting. Participants followed a predefined route consisting of six sequential tasks: opening a door, greeting an experimenter, avoiding an obstacle, walking along a corridor, reading a wall poster, and knocking on a door. This design ensures that all participants encounter the same set of action types and environmental contexts, enabling systematic comparison of EEG responses across scenes. Walking speed and pause duration were unconstrained to preserve natural movement, with 10second standing baselines at the start and end. The entire sequence took approximately 1.5 minutes.

Subject recruitment. 36 healthy adults (ages 18–26, balanced gender ratio, right-handed) were recruited2. Individuals with neurological, psychological, or cardiovascular disorders, or taking medicationsaffectingbrainactivity,wereexcluded.Participantsavoided alcohol, excessive caffeine, and sleep deprivation within 24 hours prior, and all provided informed consent.

### 5 Evaluation 5.1 Understanding the WearBCI Dataset

5.1.1 Association between IMU and EEG signal. Figure 3a shows raw EEG and IMU signals across motion conditions. As motion intensity increases, both signals exhibit larger amplitudes and variability: EEG displays stronger fluctuations due to electrode shifts and scalp muscle activation, walking introduces rhythmic gait oscillations, and navigation induces irregular bursts. Figure 3b quantifies this by computing STD of IMU and EEG signals across all 36 participants, revealing a clear association between IMU and EEG variability. Physically, increased acceleration leads to transient electrode-contact changes and scalp muscle activity, supporting the use of IMU-derived features as proxies for motion-induced EEG degradation and motivating IMU-aware denoising strategies.

### 4.2 Experiment Protocol

This study evaluates wearable BCIs under different motion dynamics. The three motion sessions were designed to cover discrete body actions, continuous locomotion, and a naturalistic navigation scenario combining movement with environmental interaction, providing a structured setting for examining how motion complexity affects EEG signal quality. Paired EEG and IMU were recorded across all non-static sessions, with egocentric video additionally

2All the data collection was approved by the Institutional Review Board (IRB) of the authors’ institution

[Figure 31]

Nodding Stretching Arm Walking Knock Door

|| | |
|---|---|
| | |
<br><br>| | |
|---|---|
| | |
<br><br>| | |
|---|---|
| | |
<br><br>Movement<br><br>Walking<br><br>Navigation<br><br>Movement (Mean)<br><br>Walking (Mean)<br><br>Navigation (Mean)|
|---|

|[Figure 32]|
|---|

- 0
- 1
- 2
- 3

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

40

EEGSTD

PSD(dB/Hz)

30

20

- -2
- -1

10

-2 -1 0 1 2

##### Figure 5: Topographic maps of different brain regions. Colors indicate PSD values, blue is higher.

IMU STD

(a) EEG and IMU waveforms.

(b) IMU-EEG correlation.

##### Figure 3: Time-domain waveforms and motion-EEG correlation across different motion levels.

GCTNet (GAN-based) [45]: A hybrid network combining convolutional and transformer branches within a GAN framework. The generator restores EEG signals, while the discriminator ensures global signal realism through adversarial training.

50

80

|Sit<br><br>Door<br><br>Greet<br><br>Avoid<br><br>Walk View Knock<br><br>|
|---|

|Sit<br><br>Type<br><br>Nod<br><br>Shake Head Stretch Arm Eye Move<br><br>|
|---|

|Sit<br><br>Stand<br><br>Slow<br><br>Medium<br><br>Fast|
|---|

50

70

40

40

PSD(dB/Hz)

PSD(dB/Hz)

PSD(dB/Hz)

60

30

50

30

40

20

20

30

10

20

EEGDNet (Transformer-based) [32]: An attention-based network that models both local and global dependencies via transformer layers, enabling fine-grained removal of motion noise.

10

10

0

0

0

-10

0 5 10 15 20 25 30 35 40 45

0 5 10 15 20 25 30 35 40 45

0 5 10 15 20 25 30 35 40 45

Frequency (Hz)

Frequency (Hz)

Frequency (Hz)

(a) Body movements.

(b) Walking speeds.

(c) Navigation.

EEGDfus (Diffusion-based) [16]: A conditional diffusion model that iteratively refines noisy EEG segments toward clean targets, leveraging multi-scale attention across adjacent windows for finegrained temporal recovery.

##### Figure 4: PSD of EEG signals in different settings.

- 5.1.2 Impact on spectral characteristics. We compute PSD across motion dynamics to assess spectral distortions. Resting-state EEG shows a clear alpha peak (8-13 Hz) during eyes-closed, consistent with the BCIC IV 2a dataset [9], supporting the physiological reliability of WearBCI under static conditions. As shown in Figure 4, distortion increases with motion: light activities introduce mild broadband elevation, while larger head movements lead to stronger increases. During walking, PSD elevation grows progressively with speed. Under navigation, distortion varies by scenetasks like walking or knocking cause greater broadband elevation, while standing or brief avoidance actions show milder changes.

- 5.2.2 Evaluation Metrics. We evaluate denoising performance using four metrics covering spectral fidelity, physiological consistency, artifact suppression, and signal interpretability. Weighted PSD Distance (𝐷PSD): Following [47], this metric mea-

sures 𝐿2 spectral deviation of the denoised signal against static eyes-closed reference over 1-45 Hz. We use double weighting on alpha (8-13 Hz) and beta (13-30 Hz) bands to emphasize key neural rhythms. Lower is better.

Alpha Peak Consistency (𝐷𝛼): This metric measures the deviation of the alpha peak amplitude of the denoised signal against the static eyes-closed baseline [40], assessing whether key physiological oscillations are preserved after denoising. Lower values indicate better retention of spectral structure.

EMG Index: Ratio of high-frequency (30-45 Hz) to low-frequency (8-30 Hz) power in the denoised signal, reflecting residual muscle artifact contamination [27]. Lower values imply cleaner signals.

Brain IC Ratio: Proportion of components after ICA decomposition labeled as “Brain” by ICLabel [31], indicating how well neural sources are preserved after denoising. Higher is better. When denoising effectively suppresses artifacts while retaining neural signals, ICA can identify a higher proportion of brain-origin components. This metric thus captures neural preservation.

- 5.2.3 Performance of different approaches. We benchmarked representative methods against a static baseline derived from intra-

- 5.1.3 Impact on different brain regions. We analyze how motion artifacts influence the spatial distribution of alpha-band power by computing topographic maps(Figure 5). The results show distinct regional effects depending on the type of movement. Arm stretching increases power in parietal and temporal regions, knocking affects frontal and occipital areas, and walking causes widespread elevation across all regions. These findings suggest that contamination patterns depend on both motion intensity and action type.

- 5.2 Benchmarking EEG Enhancement Approaches

We then evaluate the performance of several EEG denoising algorithms on our dataset.

- 5.2.1 Methodology. We evaluate the following EEG enhancement algorithms. ICA: A blind source separation technique that decomposes EEG into statistically independent components. Artifacts are removed by discarding components identified via manual inspection. EMD: A signal decomposition method that extracts intrinsic mode functions (IMFs). Components dominated by noise or high entropy are selectively suppressed to recover cleaner waveforms. ASR: A statistical technique that identifies and suppresses artifacts by reconstructing the signal within a low-variance subspace, based on deviations from clean calibration segments.

subject eyes-closed (EC) comparisons: 𝐷PSD = 4.5 ± 1.3, Brain = 0.68 ± 0.23, EMG Index = 0.28 ± 0.06, and Alpha Consistency = 0.56 ± 0.45. Traditional methods (ICA, EMD, ASR) suffer pronouncedperformancedropsasmotionbecomesmoredynamic.For example, ICA’s spectral distortion (𝐷PSD) escalates from 16.1 (body movements) to 50.6 (navigation). ASR also deteriorates under nonstationary walking and navigation, showing large 𝐷PSD values and unstable EMG suppression. Deep learning models, including GCTNet, EEGDNet, and EEGDfus, consistently achieve low spectral distortion (𝐷PSD ≈ 9.0). However, all three exhibit low Brain IC Ratios (e.g., < 0.35 across conditions), suggesting over-cleaning where

𝐷PSD Body𝐷𝛼 MovementsEMG Index Brain 𝐷PSD 𝐷𝛼 WalkingEMG Index Brain 𝐷PSD 𝐷Navigation𝛼 EMG Index Brain

ICA 16.1 ± 15.5 2.1 ± 0.4 1.3 ± 1.8 0.47 ± 0.19 31.5 ± 16.2 1.6 ± 0.4 1.1 ± 9.3 0.30 ± 0.17 50.6 ± 34.9 1.7 ± 0.6 1.7 ± 0.4 0.50 ± 0.35 EMD 25.0 ± 19.4 1.7 ± 0.3 0.2 ± 0.1 0.38 ± 0.15 96.4 ± 40.3 3.4 ± 0.4 0.3 ± 0.2 0.38 ± 0.18 213.9 ± 167.9 1.9 ± 0.4 0.5 ± 0.1 0.41 ± 0.12 ASR 12.8 ± 12.6 2.1 ± 0.5 1.2 ± 0.7 0.28 ± 0.21 23.6 ± 7.5 2.2 ± 0.7 2.3 ± 2.9 0.45 ± 0.23 145.0 ± 155.1 1.8 ± 0.3 1.6 ± 0.2 0.66 ± 0.16 GCTNet 13.7 ± 11.2 2.3 ± 0.3 2.0 ± 0.4 0.20 ± 0.10 16.4 ± 62.8 2.1 ± 0.4 2.0 ± 0.4 0.33 ± 0.20 9.0 ± 3.5 2.4 ± 0.2 1.9 ± 0.1 0.19 ± 0.22 EEGDnet 9.5 ± 3.2 2.4 ± 0.1 1.3 ± 0.3 0.17 ± 0.07 10.2 ± 1.9 2.3 ± 0.3 1.3 ± 0.1 0.25 ± 0.05 9.6 ± 3.4 2.4 ± 0.2 1.2 ± 0.2 0.28 ± 0.16 EEGDfus 8.5 ± 3.1 2.2 ± 0.1 0.9 ± 0.1 0.23 ± 0.31 9.1 ± 3.2 2.2 ± 0.1 1.4 ± 0.1 0.35 ± 0.23 8.6 ± 4.2 2.2 ± 0.1 1.5 ± 0.1 0.16 ± 0.22

Method

Table 2: Benchmarking EEG denoising methods across three motion conditions relative to a static intra-subject eyes-closed setting. The results reveal performance degradation under increasing motion and highlight trade-offs between artifact suppression and neural preservation. Bold denotes best, underline denotes second best in each column and motion condition.

[Figure 37]

Temporal Loss

#### Feature ExtractionModel

#### Input

Input

NoiseEstimation andRemoval

Baseline EEG Data

[Figure 38]

Noisy EEG Data

[Figure 39]

[Figure 40]

Frequency Loss

IMU Data

##### Figure 7: IMU-assisted EEG signal enhancement.

Figure 6: Analysis of noise reduction effects in different scenes of navigation.

meaningful neural components may also be suppressed. These results highlight that linear statistical methods are ill-suited for complex real-world motion, and that multi-metric evaluation is necessary to avoid over-cleaning and ensure neural fidelity.

120

|R-Slow<br><br>R-Medium<br><br>R-Fast<br><br>C-Slow<br><br>C-Medium<br><br>C-Fast<br><br>Static|
|---|

100

PSD(dB/Hz)

80

60

40

20

0

- 5.2.4 Performance under different scenes in navigation tasks. We evaluate denoising robustness across navigation scenes (Figure 6)

by comparing 𝐷PSD against the static baseline. The six scenes are opening a door, greeting an experimenter, avoiding an obstacle, walking along a corridor, reading a wall poster, and knocking on a door. Distortion levels vary systematically with motion type: abrupt or multi-joint actions (e.g., Greeting, Avoid Obstacle) induce the most severe artifacts, while structured scenes (e.g., Open Door, View Poster) show milder deviations. Walking produces moderate errors but still challenges ASR due to gait-induced periodic noise. ICA remains stable yet underperforms; EMD fails consistently under complex motion. EEGDfus shows greater robustness but still degrades as motion becomes less predictable.

6 CASE STUDY

We present two case studies enabled by WearBCI. Section 6.1 investigates whether incorporating auxiliary IMU signals can improve EEG quality under motion, while Section 6.2 demonstrates that behavioral understanding becomes feasible when multimodal signals are combined.

- 6.1 Cross-Modal EEG Signal Enhancement To address the limitations of existing denoising methods (Section

-20

0 5 10 15 20 25 30 35 40 45

Frequency (Hz)

(a) PSD (Frequency domain). (b) Waveform (Time domain).

##### Figure 8: Comparison of PSD and waveform before (R: Raw EEG) and after (C: Clean EEG) IMU-assisted signal enhancement during walking.

maps multi-site IMU features to motion-induced EEG artifacts in a transparent, model-agnostic manner, as illustrated in Figure 7. The input consists of acceleration and gyroscope signals from five IMUs placed on the head, wrists, and ankles, and the output is the estimated artifact component for each EEG channel. Training minimizes a combined time-domain MSE and frequency-domain PSD loss, encouraging both waveform fidelity and spectral alignment with static baselines. During inference, predicted artifacts are subtracted from the raw EEG to obtain cleaned signals.

Figures 8a and 8b show that the cleaned signal better matches the eyes-closed PSD reference with suppression of low-frequency motion bursts, and recovers more stable oscillatory patterns. Quantitatively, our approach reduces spectral distortion (𝐷PSD = 10.8± 4.6) and retains a relatively high proportion of neural components (Brain IC Ratio = 0.52 ± 0.21), outperforming traditional methods in navigation scenes. These results show that even a simple IMUinformed model can enhance EEG quality and motivate future multimodal denoising frameworks for wearable BCIs.

- 5.2.3), we investigate whether incorporating motion information can improve robustness. As shown in Figure 3b, IMU variability correlates with EEG fluctuations, motivating an IMU-assisted enhancement approach. We adopt a linear regression model that

Multi-dimensional Human Behavior Understanding

|"Person is standing and waving their right hand."<br><br>"Person is actively engaged and<br><br>observing surroundings, in a state of relaxed focus."<br><br>"A wide corridor with orange flooring, tables with objects, person is moving forward."<br><br>Cognition<br><br>Action<br><br>Scene<br><br>|
|---|

[Figure 41]

[Figure 42]

Modality Cognition Scene Action Overall

[Figure 43]

EEG

[Figure 44]

EEG-only 0.451 0.271 0.573 0.386 IMU-only 0.168 0.143 0.649 0.330 Video-only 0.276 0.864 0.652 0.622 Concatenate Fusion 0.477 0.885 0.229 0.727 Optimized Fusion 0.413 0.907 0.729 0.859

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

Video

Multimodal LLMs

[Figure 49]

[Figure 50]

Table 3: Quantitative evaluation of semantic alignment (BERTScore F1) across modalities and fusion strategies.

IMU

Figure 9: Illustration of multi-dimension behavior understanding through different modalities.

### 7 Discussion

Key insights and lessons learned. First, motion severely degrades EEG signal quality of wearable BCI systems, with spectral distortion increasing over 10-fold from static to navigation conditions. Second, existing denoising methods struggle under realistic motion conditions: traditional methods such as ASR and EMD experience catastrophic failure as motion complexity increases, as stationarity assumptions break down; deep learning models reduce spectral distortion more effectively but suppress neural components excessively. Third, the synchronized multimodal recordings in WearBCI enable signal enhancement and behavioral understanding beyond single-modality EEG, as shown in our case studies.

### 6.2 Multi-dimension Behavior Understanding

The synchronized multimodal recordings in WearBCI enable richer behavior understanding than any single modality. As illustrated in Figure 9, EEG, IMU, and egocentric video each capture distinct dimensions of behavior during naturalistic navigation, where video grounds environmental context, IMU tracks motor dynamics, and EEG reflects cognitive engagement. We annotate the navigation recordings across three semantic categories (Scene, Action, and Cognition) to assess each modality’s representational capacity and examine how fusion improves behavioral understanding.

- 6.2.1 Data Annotation. Each navigation recording is segmented based on behavior-driven events (e.g., turning, reading), with annotators marking boundaries based on natural cognitive transitions. Due to individual variability, segmentation differs across participants. We define three semantic categories: Scene (the physical environment and context, e.g., “corridor,” “doorway”), Action (the motor behavior, e.g., “opening door,” “obstacle avoidance”), and Cognition (the inferred mental engagement, e.g., “visual focus,” “spatial planning”), refined into a detailed label set covering edge cases and compound events.

Future directions and enabled applications. First, our case study shows that multimodal sensing can infer internal states like attention during natural behavior, enabling more personalized interventions for populations such as those with Alzheimer’s disease. Moreover, as discussed in Section 5.1.3, different actions contaminate distinct brain regions—for example, knocking affects frontal areas while walking introduces global interference—suggesting the value of region-aware models. While the current dataset provides systematic coverage of representative motion scenarios under controlled indoor conditions, future work should extend to unconstrained outdoor settings and more diverse participant populations to further improve ecological validity.

- 6.2.2 Evaluation. We use Gemini 2.5 Pro to generate textual descriptions for each modality, and compare them to human anno-

tations using BERTScore F1 [49]. BERTScore is adopted because it provides a context-aware semantic similarity measure in a shared Transformerembeddingspace,capturingalignmentbeyondsurfacelevel string matching across heterogeneous sensor inputs. Scores above 0.7 indicate strong alignment, 0.4–0.7 suggest partial over-

### 8 Conclusion

In this work, we introduce WearBCI, a multimodal dataset containing synchronized EEG, IMU, and egocentric video from 36 participants across movement scenarios of increasing complexity. Through benchmark experiments and case studies, we examine how motion impacts EEG quality, evaluate current EEG enhancement methods, and show that multimodal signals enable both cognitive decoding and signal enhancement. WearBCI is designed as a benchmarking resource for the community to develop and evaluate approaches for enhancing EEG signals collected by wearable BCI systems, and supports the development of more robust wearable BCI systems for everyday use.d

lap, and below 0.4 reflect poor correspondence. We compute F1 separately for Scene, Action, Cognition, and overall alignment. For EEG and IMU, we use waveform inputs, with EEG additionally including PSD features to enhance decoding. For modality fusion, we compare two strategies: Concatenate Fusion merges outputs assumingequalimportance,whileOptimizedFusionappliesprecisionweighted aggregation followed by cross-modal calibration that reconciles omissions and conflicts.

6.2.3 Results. As shown in Table 3, modalities differ in representational strength: Video achieves the highest overall BERTScore (0.62), EEG better captures cognitive states (0.45 in Cognition), and IMU best reflects motor actions (0.65 in Action). Fusion further improves—Concatenate Fusion reaches 0.73, and Optimized Fusion reaches 0.86 by reconciling cross-modal conflicts. These results demonstrate that EEG, IMU, and video capture distinct but synergistic aspects of behavior, and that multimodal integration compensates for the limited spatial coverage of wearable EEG.

### ACKNOWLEDGMENTS

This work is supported by the Research Grants Council (RGC) of Hong Kong, China, under grant ECS 26200825, the HKUSTHKUST(GZ) Cross-campus Research Collaboration “1+1+1” Joint Funding Program under G_2025_052, and is partly funded by the HKUST Institute for Emerging Market Studies with support from EY, under grant IEMS25EG01.

### References

- [1] [n. d.]. Cyton Biosensing Board (8-channels) — shop.openbci.com. https://shop. openbci.com/products/cyton-biosensing-board-8-channel. ([n. d.]). [Accessed 23-06-2025].
- [2] Khald Ali I Aboalayon, Miad Faezipour, Wafaa S Almuhammadi, and Saeid Moslehpour. 2016. Sleep stage classification using EEG signal analysis: a comprehensive survey and new investigation. Entropy 18, 9 (2016), 272.
- [3] Sheikh Farhana Binte Ahmed, Md Ruhul Amin, and Md Kafiul Islam. 2024. Motion artifact contaminated multichannel EEG dataset. Data in brief 57 (2024), 110994.
- [4] Maryam Alimardani and Kazuo Hiraki. 2020. Passive brain-computer interfaces for enhanced human-robot interaction. Frontiers in Robotics and AI 7 (2020), 125.
- [5] Pasquale Arpaia, Luigi Duraccio, Nicola Moccaldi, and Silvia Rossi. 2020. Wearable brain–computer interface instrumentation for robot-based rehabilitation by augmented reality. IEEE Transactions on instrumentation and measurement 69, 9

(2020), 6362–6371.

- [6] Víctor Asanza, Leandro L Lorente-Leyva, Diego H Peluffo-Ordóñez, Daniel Montoya, and Kleber Gonzalez. 2023. MILimbEEG: A dataset of EEG signals related to upper and lower limb execution of motor and motor imagery tasks. Data in Brief 50 (2023), 109540.
- [7] C Babiloni, X Arakaki, H Azami, K Bennys, K Blinowska, L Bonanni, A Bujan, MC Carrillo, A Cichocki, J de Frutos-Lucas, et al. 2021. Measures of resting state EEG rhythms for clinical trials in Alzheimer’s disease: recommendations of an expert panel. Alzheimers Dement. 17 (9), 1528–1553. (2021).
- [8] Joan Belo, Maureen Clerc, and Daniele Schön. 2021. EEG-based auditory attention detection and its possible future applications for passive BCI. Frontiers in computer science 3 (2021), 661178.
- [9] Clemens Brunner, Robert Leeb, Gernot Müller-Putz, Alois Schlögl, and Gert Pfurtscheller. 2008. BCI Competition 2008–Graz data set A. Institute for knowledge discovery (laboratory of brain-computer interfaces), Graz University of Technology 16, 1-6 (2008), 1.
- [10] Raymundo Cassani, Mar Estarellas, Rodrigo San-Martin, Francisco J Fraga, and Tiago H Falk. 2018. Systematic review on resting-state EEG for Alzheimer’s disease diagnosis and progression assessment. Disease markers 2018, 1 (2018), 5174815.
- [11] Yu Mike Chi, Tzyy-Ping Jung, and Gert Cauwenberghs. 2010. Dry-contact and noncontact biopotential electrodes: Methodological review. IEEE reviews in biomedical engineering 3 (2010), 106–119.
- [12] Stefanie Enriquez-Geppert, René J Huster, and Christoph S Herrmann. 2017. EEG-neurofeedback as a tool to modulate cognition and behavior: a review tutorial. Frontiers in human neuroscience 11 (2017), 51.
- [13] Maria Laura Ferster, Giulia Da Poian, Kiran Menachery, Simon J Schreiner, Caroline Lustenberger, Angelina Maric, Reto Huber, Christian R Baumann, and Walter Karlen. 2022. Benchmarking real-time algorithms for in-phase auditory stimulation of low amplitude slow waves with wearable EEG devices during sleep. IEEE Transactions on Biomedical Engineering 69, 9 (2022), 2916–2925.
- [14] Patrique Fiedler, Paulo Pedrosa, Stefan Griebel, Carlos Fonseca, Filipe Vaz, Eko Supriyanto, F Zanow, and J Haueisen. 2015. Novel multipin electrode cap system for dry electroencephalography. Brain topography 28 (2015), 647–656.
- [15] Haiyun Huang, Jie Chen, Jun Xiao, Di Chen, Jun Zhang, Jiahui Pan, and Yuanqing Li. 2024. Real-Time Attention Regulation and Cognitive Monitoring Using a Wearable EEG-based BCI. IEEE Transactions on Biomedical Engineering (2024).
- [16] Xiaoyang Huang, Chang Li, Aiping Liu, Ruobing Qian, and Xun Chen. 2024. EEGDfus: a conditional diffusion model for fine-grained EEG denoising. IEEE Journal of Biomedical and Health Informatics (2024).
- [17] Wonse Jo, Ruiqi Wang, Go-Eum Cha, Su Sun, Revanth Krishna Senthilkumaran, Daniel Foti, and Byung-Cheol Min. 2024. MOCAS: A multimodal dataset for objective cognitive workload assessment on simultaneous tasks. IEEE Transactions on Affective Computing (2024).
- [18] Evelyn Karikari and Konstantin A Koshechkin. 2023. Review on brain-computer interface technologies in healthcare. Biophysical reviews 15, 5 (2023), 1351–1358.
- [19] Byung Hyung Kim and Sungho Jo. 2015. Real-time motion artifact detection and removal for ambulatory BCI. In The 3rd International Winter Conference on Brain-Computer Interface. ieee, 1–4.
- [20] Abhay Koushik, Judith Amores, and Pattie Maes. 2019. Real-time Smartphonebased Sleep Staging using 1-Channel EEG. In 2019 IEEE 16th International Conference on Wearable and Implantable Body Sensor Networks (BSN). IEEE, 1–4.
- [21] Velu Prabhakar Kumaravel, Victor Kartsch, Simone Benatti, Giorgio Vallortigara, Elisabetta Farella, and Marco Buiatti. 2021. Efficient artifact removal from lowdensity wearable EEG using artifacts subspace reconstruction. In 2021 43rd annual international conference of the IEEE engineering in medicine & biology society (EMBC). IEEE, 333–336.
- [22] Ioulietta Lazarou, Spiros Nikolopoulos, Panagiotis C Petrantonakis, Ioannis Kompatsiaris, and Magda Tsolaki. 2018. EEG-based brain–computer interfaces for communication and rehabilitation of people with motor impairment: a novel

approach of the 21 st Century. Frontiers in human neuroscience 12 (2018), 14.

- [23] Robert Leeb, Clemens Brunner, G Müller-Putz, A Schlögl, and GJGUOT Pfurtscheller. 2008. BCI Competition 2008–Graz data set B. Graz University of Technology, Austria 16 (2008), 1–6.
- [24] Kyle E Mathewson, Tyler JL Harrison, and Sayeed AD Kizuk. 2017. High and dry? Comparing active dry EEG electrodes to active and passive wet electrodes. Psychophysiology 54, 1 (2017), 74–82.
- [25] Aleksandar Miladinović, Miloš Ajčević, Pierpaolo Busan, Joanna Jarmolowska, Giulia Silveri, Manuela Deodato, Susanna Mezzarobba, Piero Paolo Battaglini, and Agostino Accardo. 2020. Evaluation of Motor Imagery-Based BCI methods in neurorehabilitation of Parkinson’s Disease patients. In 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 3058–3061.
- [26] Juan Abdon Miranda-Correa, Mojtaba Khomami Abadi, Nicu Sebe, and Ioannis Patras. 2018. Amigos: A dataset for affect, personality and mood research on individuals and groups. IEEE transactions on affective computing 12, 2 (2018), 479–493.
- [27] Mo H. Modarres, Jonathan E. Elliott, Kristianna B. Weymann, Dennis Pleshakov, Donald L. Bliwise, and Miranda M. Lim. 2022. Validation of Visually Identified Muscle Potentials during Human Sleep Using High Frequency/Low Frequency Spectral Power Ratios. Sensors 22, 1 (2022), 55. https://doi.org/10.3390/s22010055
- [28] Ernst Niedermeyer and FH Lopes da Silva. 2005. Electroencephalography: basic principles, clinical applications, and related fields. Lippincott Williams & Wilkins.
- [29] Mostafa Orban, Mahmoud Elsamanty, Kai Guo, Senhao Zhang, and Hongbo Yang. 2022. A review of brain activity and EEG-based brain–computer interfaces for rehabilitation application. Bioengineering 9, 12 (2022), 768.
- [30] Xiaomin Ouyang, Xian Shuai, Yang Li, Li Pan, Xifan Zhang, Heming Fu, Sitong Cheng, Xinyan Wang, Shihua Cao, Jiang Xin, et al. 2024. ADMarker: A Multi-Modal Federated Learning System for Monitoring Digital Biomarkers of Alzheimer’s Disease. In Proceedings of the 30th Annual International Conference on Mobile Computing and Networking. 404–419.
- [31] Luca Pion-Tonachini, Ken Kreutz-Delgado, and Scott Makeig. 2019. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. NeuroImage 198 (2019), 181–197.
- [32] Xiaorong Pu, Peng Yi, Kecheng Chen, Zhaoqi Ma, Di Zhao, and Yazhou Ren. 2022. EEGDnet: Fusing non-local and local self-similarity for EEG signal denoising with transformer. Computers in Biology and Medicine 151 (2022), 106248.
- [33] Zhun Qin, Yao Xu, Xiaokang Shu, Lei Hua, Xinjun Sheng, and Xiangyang Zhu.

2019. econhand: A wearable brain-computer interface system for stroke rehabilitation. In 2019 9th International IEEE/EMBS Conference on Neural Engineering (NER). IEEE, 734–737.

- [34] Rajesh PN Rao. 2013. Brain-computer interfacing: an introduction. Cambridge University Press.
- [35] Elena Ratti, Shani Waninger, Chris Berka, Giulio Ruffini, and Ajay Verma. 2017. Comparison of medical and consumer wireless EEG systems for use in clinical trials. Frontiers in human neuroscience 11 (2017), 398.
- [36] Stanisław Saganowski, Joanna Komoszyńska, Maciej Behnke, Bartosz Perz, Dominika Kunc, Bartłomiej Klich, Łukasz D Kaczmarek, and Przemysław Kazienko.

2022. Emognition dataset: emotion recognition with self-reports, facial expressions, and physiology using wearables. Scientific data 9, 1 (2022), 158.

- [37] F Sayegh, F Fadhli, F Karam, M BoAbbas, F Mahmeed, JA Korbane, S Alkork, and T Beyrouthy. 2017. A wearable rehabilitation device for paralysis. In 2017 2nd International Conference on Bio-engineering for Smart Technologies (BioSMART). IEEE, 1–4.
- [38] Daehyun Seok, Seokhwan Lee, Minju Kim, Joonhyuk Cho, and Chulwoo Kim.

2021. Motion artifact removal techniques for wearable EEG and PPG sensor systems. Frontiers in Electronics 2 (2021), 685513.

- [39] Anke Snoek, Anne-Marie Brouwer, Ivo V Stuldreher, Pim Haselager, and Dorothee Horstkötter. 2025. Wearables for tracking mental state in the classroom: ethical considerations from the literature and high school students. Frontiers in Neuroergonomics 6 (2025), 1536781.
- [40] David Steyrl, Gunther Krausz, Karl Koschutnig, Günter Edlinger, and Gernot R. Müller-Putz. 2018. Online Reduction of Artifacts in EEG of Simultaneous EEGfMRI Using Reference Layer Adaptive Filtering (RLAF). Brain Topography 31

(2018), 129–149. https://doi.org/10.1007/s10548-017-0606-7

- [41] Xiaoming Tao, Dingcheng Gao, Wenqi Zhang, Tianqi Liu, Bing Du, Shanghang Zhang, and Yanjun Qin. 2024. A multimodal physiological dataset for driving behaviour analysis. Scientific data 11, 1 (2024), 378.
- [42] Pieter Van Mierlo, Margarita Papadopoulou, Evelien Carrette, Paul Boon, Stefaan Vandenberghe, Kristl Vonck, and Daniele Marinazzo. 2014. Functional brain connectivity from EEG in epilepsy: Seizure prediction and epileptogenic focus localization. Progress in neurobiology 121 (2014), 19–35.
- [43] Lasitha S Vidyaratne and Khan M Iftekharuddin. 2017. Real-time epileptic seizure detection using EEG. IEEE Transactions on Neural Systems and Rehabilitation Engineering 25, 11 (2017), 2146–2156.
- [44] Su Yang, Jose Miguel Sanchez Bornot, Kongfatt Wong-Lin, and Girijesh Prasad.

2019. M/EEG-based bio-markers to predict the MCI and Alzheimer’s disease: a review from the ML perspective. IEEE Transactions on Biomedical Engineering 66, 10 (2019), 2924–2935.

- [45] Jin Yin, Aiping Liu, Chang Li, Ruobing Qian, and Xun Chen. 2023. A GAN guided parallel CNN and transformer network for EEG denoising. IEEE Journal of Biomedical and Health Informatics (2023).
- [46] Thorsten Oliver Zander, Moritz Lehne, Klas Ihme, Sabine Jatzev, Joao Correia, Christian Kothe, Bernd Picht, and Femke Nijboer. 2011. A dry EEG-system for scientific research and brain–computer interfaces. Frontiers in neuroscience 5

(2011), 53.

- [47] Haoming Zhang, Mingqi Zhao, Chen Wei, Dante Mantini, Zherui Li, and Quanying Liu. 2021. EEGdenoiseNet: a benchmark dataset for deep learning solutions of EEG denoising. Journal of Neural Engineering 18, 5 (2021). https:

- //doi.org/10.1088/1741-2552/ac2bf8
- [48] Jiayan Zhang, Junshi Li, Zhe Huang, Dong Huang, Huaiqiang Yu, and Zhihong Li. 2023. Recent progress in wearable brain–computer interface (BCI) devices based on electroencephalogram (EEG) for medical applications: a review. Health data science 3 (2023), 0096.
- [49] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger, and Yoav Artzi. 2019. Bertscore: Evaluating text generation with bert. arXiv preprint arXiv:1904.09675 (2019).

