# Prediction of Muscle Activities from Electrocorticograms in Primary Motor Cortex of Primates

Duk Shin1*., Hidenori Watanabe2., Hiroyuki Kambara1, Atsushi Nambu3,4, Tadashi Isa2,4, Yukio Nishimura2,4,5, Yasuharu Koike1,6

1 Precision and Intelligence Laboratory, Tokyo Institute of Technology, Yokohama, Japan, 2Department of Developmental Physiology, National Institute for Physiological Sciences, National Institutes of Natural Sciences, Okazaki, Japan, 3 Department of System Integrative Physiology, National Institute for Physiological Sciences, National Institutes of Natural Sciences, Okazaki, Japan, 4Graduate University for Advanced Studies (SOKENDAI), Hayama, Japan, 5 Precursory Research for Embryonic Science and Technology, Japan Science and Technology Agency, Tokyo, Japan, 6 CREST, Japan Science and Technology Agency, Kawaguchi, Japan

|Abstract<br><br>Electrocorticography (ECoG) has drawn attention as an effective recording approach for brain-machine interfaces (BMI). Previous studies have succeeded in classifying movement intention and predicting hand trajectories from ECoG. Despite such successes, however, there still remains considerable work for the realization of ECoG-based BMIs as neuroprosthetics. We developed a method to predict multiple muscle activities from ECoG measurements. We also verified that ECoG signals are effective for predicting muscle activities in time varying series when performing sequential movements. ECoG signals were band-pass filtered into separate sensorimotor rhythm bands, z-score normalized, and smoothed with a Gaussian filter. We used sparse linear regression to find the best fit between frequency bands of ECoG and electromyographic activity. The best average correlation coefficient and the normalized root-mean-square error were 0.9260.06 and 0.0660.10, respectively, in the flexor digitorum profundus finger muscle. The d (1.5,4Hz) and c2 (50,90Hz) bands contributed significantly more strongly than other frequency bands (P,0.001). These results demonstrate the feasibility of predicting muscle activity from ECoG signals in an online fashion.<br><br>Citation: Shin D, Watanabe H, Kambara H, Nambu A, Isa T, et al. (2012) Prediction of Muscle Activities from Electrocorticograms in Primary Motor Cortex of Primates. PLoS ONE 7(10): e47992. doi:10.1371/journal.pone.0047992<br><br>Editor: Maurice Ptito, University of Montreal, Canada Received June 21, 2012; Accepted September 19, 2012; Published October 24, 2012 Copyright: 2012 Shin et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Funding: This study is supported by the Strategic Research Program for Brain Sciences from the MEXT of Japan. The funder had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: shinduk@cns.pi.titech.ac.jp<br><br>. These authors contributed equally to this work.|
|---|

Introduction

Brain-machine interfaces (BMI) are versatile technologies with potential to provide assistance to disabled individuals, allowing

- them greater interaction with the external environment. Several studies have applied electroencephalography (EEG) in the field of non-invasive BMIs: amplitudes of different frequency bands [1,2]; imagining movement of different parts of the body [3]; slow cortical potentials [4] and gamma band rhythms [5]. Although EEG-based BMIs are generally portable and easy to use in practical application, few studies have tried to reconstruct kinematic information in time series.

Several invasive BMI studies have demonstrated that sequential movements can be reproduced from multichannel spike signals recorded with intracortical multiple electrode arrays [6–13]. They have reported that multichannel spike signals are effective in predicting kinematic information such as direction and velocity of the arm. However, although intracortical electrodes can provide rich information for the control of BMIs, they face limitations such as signal degradation due to glial scarring [14] and potential displacement from the recording site [15].

Electrocorticography (ECoG) is an alternative approach to less invasive BMIs [15–23]. Since ECoG records directly from neuronal activities on the cortical surface, ECoG has higher

spatio-temporal resolution with better signal-to-noise ratio than scalp EEG [24,25]. ECoG has also shown potential as a stable long-term recording method [21]. Several studies using ECoG have already succeeded in the classification of movement direction [16,17], grasp type [22], and prediction of hand trajectory [18,20,21].

Despite these successes, however, there still remains considerable work for the realization of ECoG-based prosthetics. The human neuromuscular system naturally modulates mechanical stiffness and viscosity to achieve proper interaction with the environment. Current rehabilitation robots can perform sophisticated operations including stiffness control [26,27]. Our previous works suggested that the angle, torque, and stiffness of joints can be predicted from muscle activity [28,29,30]. Therefore, decoding muscle activity is an important component for realizing BMI systems capable of controlling interaction force or stiffness.

The aim of this study is to predict time-varying muscle activities from ECoG signals as a basis for a neuromuscular BMI system. Two well-trained Japanese monkeys performed a series of reaching, grasping, pulling, and releasing movements. We simultaneously recorded 15 or 16 ECoG signals of the primary motor cortex (Ml) and 12 electromyography (EMG) signals in the right arm. We predicted EMG from ECoG signals using sparse linear regression (SLiR). We also examined the weights of the

prediction model in order to infer which sensorimotor rhythms contribute more to the prediction. Our results indicate that multiple muscle activities can be accurately predicted from a small number of ECoG signals.

Methods Ethics statement

All experimental procedures were performed in accordance with the Guidelines for Proper Conduct of Animal Experiments of the Science Council of Japan and approved by the Committee for Animal Experiment at the National Institutes of Natural Sciences (Approval No.: 11A157). Monkeys were monitored closely and animal welfare was assessed on a daily basis and, if necessary, several times a day. This included veterinary examinations to ensure animals were not suffering as well as the use of analgesics, antiemetics, or antibiotic therapy if necessary. No monkeys were sacrificed in this study. Animals were housed individually on a 12hour light/dark cycle and provided a rubber toy. They were not food deprived. Water was provided in their home cage and recording booth. The animal welfare and steps taken to ameliorate suffering were in accordance with the recommendations of the Weatherall report [31], ‘‘The use of non-human primates in research.’’

Behavioral task

Two Japanese macaques (Monkey A: male, at 8.9 kg; Monkey B: female, at 4.7 kg) were trained to perform reaching and grasping tasks with the right hand as shown in Figure 1A. The grasping object was a small plastic knob instrumented with a thinfilm force sensor (FlexiForce; Tekscan, Inc., South Boston, MA) to measure grip force. The knob was attached to the end of a joystick switch lever equipped with several elastic bands. The joystick switch detected the pulling duration (positive phase of the target signal in Figure 2). The monkey launched a trial by placing its hand on a home button located in front of the chair for a predetermined length of time. If the monkey held the home button for 2 s, a ‘‘go’’ cue was given in the form of a beep sound instructing the monkey to reach for the knob. The monkey then had to pull the knob and hold for a preprogrammed length of time. The monkey would then release the knob and return its hand to the home button. When the monkey successfully pushed the home button to elicit a go cue and pulled the knob to the required displacement of 6 cm, it received a juice reward. The monkeys performed this task repeatedly, with monkey A performing a total of 134 trials and monkey B performing a total of 248 trials. Monkey B performed one additional session that was used to test the proposed method on continuous rather than trial-based data.

Surgery for ECoG and EMG electrode implantation

Both monkeys underwent surgery on different days to implant an ECoG electrode array and EMG wire electrodes under anesthesia after they completed behavioral training. The monkeys were anesthetized with ketamine (1.0 mg/kg) and xylazine (0.5 mg/kg). The inhalation of 1–2% isoflurane maintained anesthesia during the surgeries. We also continuously monitored electrocardiogram, pCO2, and arterial O2 levels.

We chronically implanted a platinum ECoG array (Unique Medical Corporation, Tokyo, Japan) over the left primary motor cortex (M1), which had 15 (monkey A: 563 grid) and 16 (monkey B: 464 grid) channel electrodes, as shown in Fig 1B. The electrodes had a diameter of 1 mm and an inter-electrode distance of 3 mm center-to-center. Four silver wires (300 mm in diameter; over 5 cm in length) were used as reference and ground electrodes

A

ECoGs

Force sensor

[Figure 1]

Home button

Elastic band

Touch sensor

EMGs

B

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

#3 #2 #1

#4 #3#2 #1

CS

CS

3mm

1mm

Dorsal

AS

AS

3mm

Rostral

subject A subject B

Figure 1. Behavioral task and ECoG electrode locations. A) Monkeys performed sequential right arm and hand movements, which consisted of reaching to a knob, grasping the knob with a lateral grip, pulling the knob closer, releasing the knob, and returning the hand to the home position, in a 3-D workspace. During the task, ECoG and EMG signals were recorded simultaneously. B) Schematic diagrams of ECoG electrode locations in left hemisphere. The planar-surface platinum electrode arrays were placed on the gyrus between the central sulcus (CS) and the arcuate sulcus (AS) in the primary motor area. The # indicates the location according to the column of ECoG electrodes. doi:10.1371/journal.pone.0047992.g001

and shunted (single-end mode) through connectors (#A8828-001; Omnetics Connector Corporation, Minneapolis, MN, US). A craniotomy was performed above M1, and the dura was incised and reflected. We placed the ECoG array on the rostral bank of the central sulcus, the hand/arm area of M1. The dura was closed using 6.0 synthetic absorbable suture threads within surgical glue composed of gelatin after the two silver wire reference electrodes were inserted into the subdural space. A piece of artificial dura mater was applied over the dura and two reference ground electrodes were inserted into supradural space between the dura and the skull. The craniotomy was closed with a piece of dental acrylic, and head holders were attached to the skull. Finally, the skull was coated with dental acrylic.

EMG activities of the right forelimb muscles were recorded from chronically implanted pairs of multi-stranded stainless steel wires (Cooner Wire, Chatsworth, CA, USA). They were subcutaneously tunneled to the following target muscles: adductor pollicis (AP), abductor pollicis longus (APL), flexor digitorum superficialis (FDS; monkey A only), flexor digitorum profundus (FDP), and extensor digitorum communis (EDC) for hand muscles; flexor carpi radialis (FCR; monkey A only), flexor carpi ulnaris

- 0

- 1

- 2

- γ1
- γ2

| |
|---|
| |
| |
| |
|[Figure 8]|
| |
| |
| |

[Figure 9]

[Figure 10]

- β1
- β2

α

θ

15ch 1ch

δ

[Figure 11]

TB

BB

ECU

FCR

FCU

PT

PL

FDP

EDC

FDS

APL

AP

force

home

target

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

Time [s]

- Figure 2. Example of measured signals from monkey A during the tasks. All signals are aligned to trial onset. At the top are frequency feature values of the ECoG signals. Frequency features were resorted in time and sensorimotor rhythm bands. Frequency features of each band are ordered by channel. Below the frequency features are the 12 EMG signals recorded from wire electrodes implanted into muscles of the right forelimb. The blue traces represent original muscle activities. The red traces represent muscle activities obtained by low pass filtering (cut-off frequency: 4 Hz). Below the EMG are grip force on the knob and logical signals, indicating presence of the monkey’s hand on the home button or grasping the knob.

- doi:10.1371/journal.pone.0047992.g002

(FCU), palmaris longus (PL; monkey A only), extensor carpi radialis (ECR; monkey B only), and extensor carpi ulnaris (ECU; monkey A only) for wrist muscles; and pronator teres (PT; monkey

- A only), biceps brachii (BB), and triceps brachii (TB) for elbow muscles. Isolation of the muscles was confirmed with electronic current stimulation through a silver ball electrode (intensity of a

single monophasic current pulse: ,100 mA, pulse duration: 1ms, 1 stimulation: 5 pulses with 3ms pulse intervals, inter-stimulus interval: 1s), which evoked joint movement and muscle twitch in the fingers and arm during electrode implantation surgery. In each muscle, two electrodes were implanted and one electrode was used as reference (differential mode). Circular connectors (MCP-12, Omnetics, Minneapolis, MN, USA) were anchored to the skull.

Data recording

Recording sessions were initiated two months after the surgery. ECoG and EMG signals were sampled at 4 kHz using an acquisition processor system (Plexon MAP system; Plexon, Inc., Dallas, US). ECoG signals were filtered with band-pass filters through multi-channel bio-signal amplifiers (monkey A: 1.5 Hz high-pass and 1 kHz low-pass analog filters, MEG-6116, Nihon Kohden Corporation, Tokyo, Japan; monkey B: 0.7 Hz high-pass and 8 kHz low-pass analog filters, Plexon, Inc., Dallas, USA). Due to logistical reasons, two different amplifiers were used for ECoG filtering in the two subjects. However, post-hoc data processing (Results section) showed no substantial differences between the band-pass filters of the two amplifiers. EMG signals were also filtered online with 1.5 Hz high-pass and 3 kHz low-pass analog filters through a signal amplifier (MEG-6116: Nihon Kohden Corporation, Tokyo, Japan). Separate amplifiers were used for signal filtering because the analog-to-digital converter boards of the acquisition processor system did not support user-defined filters.

Preprocessing of ECoG and EMG data

ECoG signals were down-sampled to 500 samples per second to match movement data and re-referenced using a common average reference (CAR) montage. Bidirectional fourth-order Butterworth band-pass filters were applied to each ECoG signal, dividing them into specific rhythmic bands. These bands were d (1.5,4 Hz), h (4,8 Hz), a (8,14 Hz), b1 (14,20 Hz), b2 (20,30 Hz), c1 (30,50 Hz), and c2 (50,90 Hz). We selected these particular frequency bands, because their use is common in current EEG and ECoG based BMIs. The seven band-pass filters split each of the 15- or 16-channel ECoG signals into seven band-passed signals to produce M channels of band-pass filtered signals. Each bandpass filtered signal x^i(t) was then normalized by the standard z-score, resulting in signal sources xi(t), where

x^i(t){m^i s^i

(i~1,2,3, ,M ) ð1Þ

xi(t)~

and m^i and s^i are the mean and the standard deviation of x^i, respectively, over a 1 s interval before the time t. Finally, the resulting amplitude modulations were smoothed with a Gaussian filter (width: 0.1 s, s: 0.04 s).

EMG signals were rectified and passed through a 4th-order lowpass filter with a cut-off frequency of 4 Hz and further downsampled to 500 Hz, resulting in muscle activities.

Prediction of muscle activities from ECoG signals

Previous studies have reconstructed finger-movements, finger force, and arm EMG patterns from neural firings [32], blood oxygen level-dependent signals [33], near-infrared spectroscopy signals [34], cortical current dipoles [35], EEG signals [36], and local field potential (LFP) signals [37]. Since the SLiR algorithm can automatically select significant input variables and reduce the number of input dimensions, we used the Variational Bayesian Sparse Regression toolbox [38] to determine which band is

effective in predicting EMG signals. The SLiR algorithm estimates the linear weight and automatic relevance determination (ARD) parameters [39], which represent how the weight contributes to the reconstruction. Based on these ARD parameters, SLiR identified only the channels that provided the best generalization properties by pruning the channels ineffective for reconstruction (setting the linear weight value to zero) [40].

The predicted muscle activity at time t, is described as

iP~M1NjP~{01

yk(t)~

vkijxi(t{jDt)zvk0 , ð2Þ

where vkij is the weight coefficient of the k-th muscle for the i-th signal source at a delay time jDt, vk0 is the bias term, xi(t) is the ith ECoG source at time t, and Dt is a discrete-time step-size of 20 ms. The muscle activity at time t was predicted using 10 time points (N=10) starting 200 ms before the target time t.

Analysis

Accuracy of the muscle activity prediction was evaluated using 10-fold cross validation. We extracted trials in reference to the trial onset, where onset was defined as the movement initiation from the home button. The extracted trials were randomly partitioned into 10 subsets. Each subset for monkeys A and B had 12 trials and 24 trials, respectively. A single subset was retained as a test subset to evaluate the model, and the remaining 4 subsets were used as training data. The cross-validation process was then repeated 10 times, with each of the 10 subsets used exactly once as a test subset. To verify its applicability to continuous data, we also tested the model on 50 s of task data randomly extracted from an additional session performed by monkey B.

We calculated the coefficient of correlation (CC) to evaluate the similarity between actual and predicted muscle activities. Accuracy was also evaluated using normalized root-mean-square error (nRMSE) between actual and predicted muscle activities, defined as

v u t

ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ iP~n1

(ypredictedi {yactuali )2 n

,(yactualmax {yactualmin ) ð3Þ

nRMSE~

where for each time i (i=1, 2, … ,n), yipredicted is the predicted muscle activity and yiactual is the actual muscle activity, and yactualmax and yactualmin are the maximum and minimum of actual muscle activities, respectively.

Weight values for contributing to prediction

We examined the weight values for frequency bands, locations, muscles, and subsets in the prediction model. Weight coefficients vkij were averaged across time points (j=0, 1, 2, ..., 9). They were normalized by the maximum weight within each muscle and applied in a 3-way ANOVA. We used locations rather than electrodes because the 3-way ANOVA could not be calculated with so many degrees of freedom. Since Rathelot and Strick [41] reported that corticomotoneuronal (CM) cells that make monosynaptic connections to spinal motoneurons are located predominantly in the anterior bank of the central sulcus, we hypothesized that the weight values of locations near the central sulcus would be larger than those of the other locations. Median differences were

- then analyzed using Tukey multiple comparison tests. Statistical significance was assessed at a 5% or 1% confidence level using an F test. Fw, r values (Results section) represent the ratio of variances

within subjects with degrees of freedom w and between subjects with degrees of freedom r. Large F values indicated more variance between subjects than within subjects. All data processing and analyses were performed using MATLAB R2011b (The Mathworks, Inc., Natick, MA, USA).

Results Multiple task-related muscle activities

Movement duration averages and standard deviations (STD) for monkeys A and B were 3.2260.24 s and 1.1660.29 s, respectively. Therefore, we set the duration of each trial to 4.0 s (monkey A) and 2.0 s (monkey B), including a before-onset period of 0.5 s and after-onset periods of 3.5 s (monkey A) and 1.5 s (monkey B). Figure 2 shows an example trial including frequency band features of the ECoG signals, rectified raw EMG signals, grip force, and logical signals. Sequential movements were divided into four movements according to the logical signals. Four patterns of actual muscle activity were observed when subjects performed the sequential movements. First, activity for the elbow flexor muscle BB and finger extensor EDC increased before trial onset to raise the hand. Second, all muscles except the wrist flexor muscle FCR and the wrist pronation muscle PT peaked upon opening the hand to grasping the knob. Third, the palm muscle PL, finger flexor muscles FDP and FDS, and thumb adductor muscle AP were activated while the monkey grasped the knob (from 1 s to 2.45 s). The wrist muscle ECU and FCU also co-contracted to fix the wrist during the knob pulling movement. Fourth, all muscles, with the exception of FCU, FDS and FDP, peaked when the monkey released the knob and returned its hand to the start button. Muscle activations almost always occurred in this pattern, though timings slightly differed from trial to trial.

Reconstruction using sparse linear regression

Figure 3 shows typical plots of predicted muscle activity (solid line) from a test subset in comparison with actual muscle activity (dotted line) during a trial conducted with monkey A. The proposed method was able to predict sequential muscle activations during the reaching and grasping task, as well as concurrent bursts such as the EDC and APL. In particular, the proposed method generated the co-contraction features occurring for grasping, as seen in the ECU and FCU.

CC and nRMSE between the actual and predicted EMGs were used to quantify the information extracted directly from ECoGs related to muscle activity. The highest CC values were 0.7360.10 for EDC in the 10th test subset for monkey A and 0.9260.06 for FDP in the 3rd test subset for monkey B. The highest nRMSE values were 0.1660.02 for FDS in the 3rd test subset and 0.0660.10 for FDP in the 8th test subset for monkeys A and B, respectively. Table 1 summarizes the results of the validation in predicting each muscle for 10 test subsets of monkey B (see also Table S1 for monkey A). Grand averages and standard error of the mean (SEM) for each muscle ranged between 0.5560.013 and 0.8860.009 for CC and 0.1760.003 and 0.4260.007 for nRMSE. These results clearly show that ECoG data contained information about muscle activations.

A one-way ANOVA was conducted to judge whether performance of the proposed method differed significantly among the test subsets. Significant differences of the nRMSE values were not observed among test subsets in both monkeys (monkey A: F9, 110 =0.65, p=0.75; monkey B: F9, 110 =0.03, p =1).

The histogram in Figure 4 shows the distribution of CC and nRMSE for each muscle of monkey A. Average and STD of the median of CC were 0.5960.04 and 0.8560.07 for monkeys A and

CC=0.75, nRMSE=0.12

CC=0.70, nRMSE=0.15

CC=0.50, nRMSE=0.21

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

1.5

### ECU

### BB

### TB

- -0.5

0

- 0.5
- 1

- -0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5

-0.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

CC=0.72, nRMSE=0.20

CC=0.75, nRMSE=0.15

CC=0.63, nRMSE=0.15

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

### FCR

### FCU

### PT

-0.5

-0.5

-0.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

CC=0.75, nRMSE=0.16

CC=0.60, nRMSE=0.19

CC=0.82, nRMSE=0.17

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

EDC

FDP

PL

-0.5

-0.5

-0.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

CC=0.76, nRMSE=0.17

CC=0.69, nRMSE=0.15

CC=0.80, nRMSE=0.14

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

- 0

- 0.5
- 1

- 1.5

actual predicted

FDS

### APL

AP

-0.5

-0.5

-0.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

-0.5 0 0.5 1 1.5 2 2.5 3 3.5

Time [s]

- Figure 3. Representative example of predicted and recorded muscle activities. Dotted lines are actual muscle activities from EMG signals measured with wire electrodes, and solid lines represent predicted muscle activities from ECoG signals of monkey A. The normalized root mean square error (nRMSE) and correlation coefficient (CC) are also shown above each panel.

- doi:10.1371/journal.pone.0047992.g003

Table 1. Summary of prediction accuracies for 10-fold cross validation of monkey B.

Statistics Test set TB BB ECR FCU EDC FDP APL AP CC 1 0.5160.40 0.8660.12 0.59±0.32 0.8160.21 0.81±0.12 0.8960.17 0.8660.12 0.8460.17

- 2 0.62±0.36 0.87±0.11 0.5760.34 0.8360.14 0.8060.14 0.8660.20 0.8560.17 0.8560.11
- 3 0.5660.33 0.8360.25 0.5860.30 0.8360.14 0.8360.15 0.92±0.06 0.8660.17 0.8760.13
- 4 0.5160.38 0.8560.25 0.5460.32 0.7760.25 0.8360.12 0.8560.24 0.8560.15 0.8560.22
- 5 0.5460.35 0.8460.29 0.5660.33 0.8060.21 0.8060.14 0.8660.23 0.83±0.19 0.8060.23
- 6 0.51±0.39 0.87±0.11 0.60±0.32 0.8260.20 0.83±0.10 0.8960.17 0.87±0.11 0.85±0.17
- 7 0.6160.36 0.8660.12 0.5560.34 0.8360.15 0.7960.15 0.86±0.19 0.8360.18 0.8560.12
- 8 0.5760.33 0.8360.25 0.5960.30 0.84±0.14 0.8260.15 0.9260.06 0.8660.18 0.88±0.12
- 9 0.5460.38 0.8560.25 0.5660.32 0.7860.24 0.8360.12 0.8660.23 0.8660.15 0.8660.21
- 10 0.5760.38 0.8760.11 0.5660.26 0.7960.21 0.8060.12 0.8560.25 0.8460.18 0.8660.13 Avg. 0.5560.013 0.8560.006 0.5760.007 0.8160.008 0.8260.006 0.88±0.009 0.8560.004 0.8560.007

nRMSE 1 0.4060.31 0.1260.13 0.3260.11 0.2160.20 0.1260.05 0.1760.06 0.1260.08 0.1760.09

- 2 0.3660.27 0.11±0.07 0.3460.11 0.14±0.41 0.1460.06 0.2060.25 0.1760.08 0.11±0.12
- 3 0.3360.30 0.2560.21 0.3060.12 0.1460.13 0.1560.05 0.0660.10 0.1760.10 0.1360.06
- 4 0.3860.23 0.2560.43 0.3260.11 0.2560.16 0.1260.08 0.2460.23 0.1560.09 0.2260.16
- 5 0.3560.18 0.2960.44 0.33±0.09 0.2160.21 0.1460.06 0.2360.19 0.1960.11 0.2360.17
- 6 0.3960.30 0.1160.13 0.3260.11 0.2060.20 0.10±0.05 0.1760.065 0.11±0.08 0.1760.09
- 7 0.3660.29 0.1260.07 0.3460.11 0.1560.39 0.1560.07 0.1960.24 0.1860.09 0.12±0.12
- 8 0.33±0.30 0.2560.22 0.3060.12 0.1460.13 0.1560.05 0.06±0.10 0.1860.10 0.1260.06
- 9 0.38±0.23 0.25±0.42 0.3260.11 0.24±0.17 0.12±0.08 0.2360.23 0.1560.09 0.2160.16
- 10 0.3860.38 0.1160.08 0.26±0.11 0.2160.10 0.1260.07 0.25±0.07 0.1860.12 0.1360.10 Avg. 0.4260.007 0.2160.010 0.3160.004 0.2860.010 0.1960.004 0.1760.008 0.17±0.003 0.2060.008

Each cell except Avg. shows the CC or the nRMSE(mean 6 STD) of 24 trials. Bold numbers indicate the best value in each test subset. The Avg. cells show the grand averages of mean and SEM. Bold numbers here indicate the best grand averages. doi:10.1371/journal.pone.0047992.t001

## TB

50

0.17 0.57

40

Frequency

Frequency

30

20

10

0

0 0.2 0.4 0.6 0.8 1

## FCR

50

0.17 0.63

40

FrequencyFrequencyFrequency

Frequency

30

20

10

0

0 0.2 0.4 0.6 0.8 1

PL

50

0.18 0.54

40

FrequencyFrequency

30

20

10

0

0 0.2 0.4 0.6 0.8 1

FDS

50

|0.18|0.57|
|---|---|

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

## BB

50

0.18 0.64

40

FrequencyFrequency

30

20

10

0

0 0.2 0.4 0.6 0.8 1

FCU

50

0.19 0.55

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

FDP

50

0.21 0.58

40

FrequencyFrequency

30

20

10

0

0 0.2 0.4 0.6 0.8 1

APL

50

0.19 0.63

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

## ECU

50

0.19 0.5

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

PT

50

0.25 0.51

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

EDC

50

| |0.19|0.66|
|---|---|---|

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

AP

50

| |0.18|nRMSE CC| |
|---|---|---|---|
| | |0.54| |

40

30

20

10

0

0 0.2 0.4 0.6 0.8 1

- Figure 4. CC and nRMSEdistributions for each muscle of monkey A. The height of each blue bar is equal to the CC density of the interval (0.05). The height of each red bar is equal to the nRMSE density of the interval (0.02). The total area of the histogram is equal to the number of trials used as validation data. Each dotted line with a number shows the median of nRMSE or CC for each muscle. For visualization, we substituted zeros for all negative CC values in validation.

- doi:10.1371/journal.pone.0047992.g004

- B, respectively. Average and STD of the median of nRMSE were 0.1960.01 and 0.1860.03 for monkeys A and B, respectively. Negative CC values were not removed from the analysis but were substituted with zeros strictly for visualization in Figure 4.

We also applied the prediction model to continuous data from an additional session by monkey B. One example of continuous prediction is shown in Figure 5, where the prediction was stable even for repetitive trials over 50 s. Mean and STD of CC and nRMSE for each muscle ranged from 0.3860.08 to 0.8760.02 (CC) and 0.1160.01 to 0.1760.05 (nRMSE). These results clearly show that the model can predict muscle activity from ECoG in an online fashion.

Frequency bands contributing to prediction

We analyzed the weight values for the 7 frequency bands, 3 or 4 locations, 12 or 8 muscles, and 10 subsets in the prediction model. A 3-way ANOVA was conducted to test the effects of three factors (frequency bands, locations, and muscles). Results of ANOVA showed significant main effects of frequency bands (F6, 1008= 43.46, p=2.42610247; F6, 672=33.78, p =1.07610235) and locations (F2, 1008=6.23, p=0.002; F3, 672 =18.47, p=1.59610211). The 3-way interaction did not show any significance. The interaction between frequency bands and locations only showed the significance (F12, 1008=12.89, p=6.89610225; F18, 672 =4.01, p =5.9461028) among the two-way interaction. We, therefore, investigated simple main effects of frequency bands by running

separate two-way ANOVA for each level of the locations to infer which frequency band most greatly contributed to the prediction. Simple main effects of frequency bands for all levels of locations, except the fourth location, were significant (first location: F6, 1239=38.37, p=1.34610242; F6, 868=12.81, p=1.79610213; second location: F6, 1239=28.57, p =1.03610231; F6, 868 =20.82, p=1.81610222; third location: F6, 1239=13.51, p=1.84610214; F6, 868=11.56, p=4.64610212). Multiple comparisons were conducted as shown in Figure 6. Multiple comparisons showed that the d and c2 bands significantly contributed to the prediction more than any other frequency band in both monkeys. However, all frequency bands were needed for effective prediction because input dimensions were not reduced by the SLiR algorithm. No significant differences between b1 and b2 were observed for all levels of locations, showing that feature bands could be reduced by unifying b1 and b2. The weight values of column #1 that were located in the most caudal part of the pre-central gyrus were slightly larger than those of the other columns located more rostral.

We also conducted a two-way ANOVA to calculate simple main effects of the locations for each frequency band level. All simple main effects except h level showed significance for monkey A (d: F2, 1239=5.91, p=0.003; a: F2, 1239=7.99,

- p=3.561024; b1: F2, 1239=9.11, p =1.2061024; b2: F2, 1239=11.02, p =1.7861025; c1: F2, 1239=21.91,
- p=4.30610210; c2: F2, 1239=39.94, p=1.46610217). The simple

- 0
- 1.5

CC=0.48 nRMSE=0.13

1.0 0.5

EDCFDPAPLECRTBBBFCU

1.5 1.0 0.5

CC=0.84 nRMSE=0.12

0

- 0
- 1.5

| | | | |CC=0.38|nRMSE=0.|11| | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |

1.0 0.5

- 0
- 1.5

- CC=0.68 nRMSE=0.14

- CC=0.69 nRMSE=0.13

1.0 0.5

- 0
- 1.5

1.0 0.5

- 0
- 1.5

CC=0.87 nRMSE=0.11

1.0 0.5

- 0
- 1.5

CC=0.76 nRMSE=0.11

1.0 0.5

- 0
- 1.5 1.0

CC=0.81 nRMSE=0.12 actual

predicted 0.5

AP

410 415 420 425 430 435 440 445 450 455 460

Time [s]

- Figure 5. Example of muscle activity prediction in a continuous time series from monkey B. Dotted lines are actual muscle activities from EMG signals and solid lines are predicted muscle activities from ECoG signals over a 50 s time interval. Both lines were normalized to the ranges of actual muscle activities. The normalized root mean square error (nRMSE) and correlation coefficient (CC) are also shown.

- doi:10.1371/journal.pone.0047992.g005

main effects of d, b1 and c2 showed significance for monkey B (d: F3, 868=11.45, p=3.1861027; b1: F3, 868 =6.33, p =3.9961024; c2: F3, 868=20.08, p=1.88610212). Results of multiple comparisons are summarized in Figure 7.

Discussion

This study describes a novel attempt to predict multiple muscle activities from a small number of ECoG signals. This approach offers important insight regarding the presence of ample information in ECoG signals to predict time-varying muscle activities, whereas previous ECoG-based studies have tried to classify direction or intention of movement. The results clearly demonstrate that muscle activity time series and trial-to-trial variations of finger, hand, and arm muscles can be predicted from ECoG signals.

Previous studies using invasive methods have succeeded in the prediction of muscle activities through linear summation of the Ml

firing rate [7,28,29,42–45] or LFP [46]. Only one study, to our knowledge, has demonstrated that temporal activities of wrist muscles can be reconstructed from EEG cortical source currents, estimated from EEG sensor signals using a hierarchical Bayesian EEG inverse method [36]. Although their method could lead to drastic improvement in the non-invasive BMI area, it is still unknown whether it can be applied to sequential movements. In addition, their method has to solve an inverse problem, i.e., a projection from EEG sensors to current sources. A large number of current sources also increases the computational burden. In contrast, the present approach may be useful as a real-time force controller for BMI devices because it is fundamentally based on a simple filtering technique that addresses the z-score of frequency features of ECoG signals. This is the first report of a method for predicting multiple muscle activities from ECoG signals during natural forelimb movements.

- A
- B

sum = 79.73

sum = 78.28 sum = 94.87

0.5

0.5

0.5

**

**

*

0.4

0.4

0.4

*

**

**

0.3

0.3

0.3

*

**

0.2

0.2

0.2

0.1

0.1

0.1

0

0

0

δ θ α β1 β2 γ1 γ2 δ θ α β1 β2 γ1 γ2 δ θ α β1 β2 γ1 γ2

# 3

# 2 # 1

sum = 23.88 sum = 29.04 sum = 36.32 sum = 42.47

0.5

0.5

0.5

0.5

**

0.4

0.4

0.4

0.4

** **

*

0.3

0.3

0.3

0.3

*

0.2

0.2

0.2

0.2

0.1

0.1

0.1

0.1

0

0

0

0

δ θ α β1β2γ1 γ2 δ θ α β1β2γ1 γ2 δ θ α β1β2γ1 γ2 δ θ α β1β2γ1 γ2

# 4

# 3

# 2

# 1

- Figure 6. Contribution of each frequency band for EMG prediction. Each panel shows results of multiple comparisons among the frequency bands for each location level (A: monkey A, B: monkey B). Each bar represents the mean of the median weights of each frequency band. At the top of each graph are the sum of the total weights. The # indicates the location of the ECoG electrodes. Noteworthy significant differences between weight values of frequency bands are marked with * (p,0.05) and ** (p,0.001). Other significance comparisons are omitted for visualization purposes.

- doi:10.1371/journal.pone.0047992.g006

#3 #2 #1 #4 #3 #2 #1

0

0.1

0.2

0.3

0.4

0.5

0

0.1

0.2

0.3

0.4

0.5

A B

δ α θ

- β1
- β2

- γ1
- γ2

δ α θ

- β1
- β2

- γ1
- γ2

Figure 7. Simple main effect of electrode location contributing to EMG prediction. Each panel shows results of multiple comparisons among the locations for each frequency band level (A: monkey A, B: monkey B). Each marker displays the mean of the median weights. Faded lines show non-significant frequency bands. Solid lines represent a significant difference between weight values (p,0.001) and the dotted lines represent no significance. The # indicates the location of the ECoG electrodes.

- doi:10.1371/journal.pone.0047992.g007

Most EEG-based BMI studies have used one or two sensorimotor rhythms such as m (8,12 Hz) or b (14,30 Hz) oscillations because the c (.30 Hz) rhythm is often inconspicuous and neglected with a low pass filter, though Khan and Sepulveda [5] did use c band EEG to discriminate four types of wrist motion. In ECoG-based BMIs, however, the c rhythm has been widely used. In our studies, we identified the useful ECoG frequency bands associated with muscle activity. Analysis of the weight values for the frequency bands showed that contributions by the d, c, and b bands were significantly larger than those of the h and a bands (e.g. Figure 6). This result corresponds to previous studies as well [21,46–49].

Kinematic artifacts might have influenced the d band to become the most contributing feature because the power spectrum of the movements had a peak in low frequency components (,2 Hz). These d band features, however, are mainly derived from low frequency local field potentials (lf-LFPs) or movement eventrelated potentials (MRPs) in the frontal motor areas [4,15,50,51]. The weights of the d and c bands were higher than those of the h and a bands. This result coincides well with previous studies classifying of finger movement [52] and grasp type [22]. They reported that the accuracy of movement classification using power spectrums in high (75,170 Hz) and low (,4 or 5 Hz) frequency bands was greater than that using intermediate frequency bands (6,15 Hz and 17,40 Hz).

It should be noted that no frequency band weights disappeared after applying the SLiR algorithm. This might indicate that all sensorimotor rhythms of ECoG encode muscle activity and are needed, at least at some degree, to predict them. Toro et al. (1994) reported that multi-joint arm movements were accompanied by a decrease in the spectral power of the 8,12 Hz band in ECoG signals [53]. Previous works also reported a significant coherence between the M1 and EMG at the b band frequency [54,55,56]. Additionally, recent studies reported that higher frequency bands (.100 Hz [48]; 100,200 Hz and 200,400 Hz [51]) yielded better performance than the typically used c band (30,100 Hz). Therefore, we expect that the usage of all sensorimotor rhythms including the high frequency bands would contribute to the improved performance of an ECoG-based BMI.

References

- 1. Wolpaw JR, Mcfarland DJ, Neat GW, Forneris CA (1991) An Eeg-Based BrainComputer Interface for Cursor Control. Electroen Clin Neuro 78: 252–259.
- 2. Pfurtscheller G, Neuper C (1994) Event-related synchronization of mu rhythm in the EEG over the cortical hand area in man. Neurosci Lett 174: 93–96.
- 3. Birbaumer N, Ghanayim N, Hinterberger T, Iversen I, Kotchoubey B, et al.

(1999) A spelling device for the paralysed. Nature 398: 297–298.

- 4. Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM (2002) Brain-computer interfaces for communication and control. Clin Neurophysiol 113: 767–791.
- 5. Khan YU, Sepulveda F (2010) Brain-computer interface for single-trial EEG classification for wrist movement imagery using spatial filtering in the gamma band. Iet Signal Processing 4: 510–517.
- 6. Wessberg J, Stambaugh CR, Kralik JD, Beck PD, Laubach M, et al. (2000) Real-time prediction of hand trajectory by ensembles of cortical neurons in primates. Nature 408: 361–365.
- 7. Carmena JM, Lebedev MA, Crist RE, O’Doherty JE, Santucci DM, et al. (2003) Learning to control a brain-machine interface for reaching and grasping by primates. PLoS Biol 1: 193–208.
- 8. Lebedev MA, Carmena JM, O’Doherty JE, Zacksenhouse M, Henriquez CS, et al. (2005) Cortical ensemble adaptation to represent velocity of an artificial actuator controlled by a brain-machine interface. J Neurosci 25: 4681–4693.
- 9. Hochberg LR, Serruya MD, Friehs GM, Mukand JA, Saleh M, et al. (2006) Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442: 164–171.
- 10. Velliste M, Perel S, Spalding MC, Whitford AS, Schwartz AB (2008) Cortical control of a prosthetic arm for self-feeding. Nature 453: 1098–1101.
- 11. Nicolelis MAL, Lebedev MA (2009) OPINION Principles of neural ensemble physiology underlying the operation of brain-machine interfaces. Nat Rev Neurosci 10: 530–540.

In addition, the weight values of the electrodes located near the central sulcus were higher than those of the electrodes located more rostral. This result matches well with previous anatomical and physiological findings. CM cells that make monosynaptic connections to spinal motoneurons are located predominantly in anterior bank of the central sulcus [41]. The output from CM cells encodes muscle-activation patterns reflected in EMG activity [57]. Thus the frequency band features near the central sulcus may be the key to decoding muscle activities.

The primary advantage of the proposed method is that it can predict agonist and antagonist muscle activities during sequential movement tasks. If we can predict agonist and antagonist muscle activities, joint angle, torque, and stiffness can also be predicted using previously proposed methods [28,29,30]. This creates remarkable benefits, which would contribute to the realization of ECoG-based prosthetics.

Supporting Information

Table S1 Summary of prediction accuracies for 10-fold cross validation of monkey A. Each cell except Avg. shows the CC or the nRMSE (mean 6 STD) of 12 trials. Bold numbers indicate the best value in each test subset. The Avg. cells show the grand averages of mean and SEM. Bold numbers here indicate the best grand averages. (DOCX)

Acknowledgments

We thank M. Togawa (NIPS) and Y. Yamanishi (NIPS) for their assistance with our experiments, N. Yoshimura (Tokyo Tech.) and M. Sato (ATR) for their helpful advice regarding the Variational Bayesian Sparse Regression toolbox, and C. S. DaSalla (NCNP) for proofreading the manuscript.

Author Contributions

Conceived and designed the experiments: DS HW AN TI YN YK. Performed the experiments: HW AN TI YN. Analyzed the data: DS HW HK YK. Contributed reagents/materials/analysis tools: DS HW. Wrote the paper: DS.

- 12. Chase SM, Schwartz AB, Kass RE (2010) Latent Inputs Improve Estimates of Neural Encoding in Motor Cortex. J Neurosci 30: 13873–13882.
- 13. Andersen RA, Hwang EJ, Mulliken GH (2010) Cognitive Neural Prosthetics. Annu Rev Psychol 61: 169–190.
- 14. Polikov VS, Tresco PA, Reichert WM (2005) Response of brain tissue to chronically implanted neural electrodes. J Neurosci Methods 148: 1–18.
- 15. Leuthardt EC, Schalk G, Wolpaw JR, Ojemann JG, Moran DW (2004) A braincomputer interface using electrocorticographic signals in humans. J Neural Eng 1: 63–71.
- 16. Pistohl T, Ball T, Schulze-Bonhage A, Aertsen A, Mehring C (2008) Prediction of arm movement trajectories from ECoG-recordings in humans. J Neurosci Methods 167: 105–114.
- 17. Levine SP, Huggins JE, BeMent SL, Kushwaha RK, Schuh LA, et al. (2000) A direct brain interface based on event-related potentials. IEEE Trans Rehabil Eng 8: 180–185.
- 18. Mehring C, Nawrot MP, de Oliveira SC, Vaadia E, Schulze-Bonhage A, et al.

(2004) Comparing information about arm movement direction in single channels of local and epicortical field potentials from monkey and human motor cortex. Journal of Physiology-Paris 98: 498–506.

- 19. Schalk G, Kubanek J, Miller KJ, Anderson NR, Leuthardt EC, et al. (2007) Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. J Neural Eng 4: 264–275.
- 20. Sanchez JC, Gunduz A, Carney PR, Principe JC (2008) Extraction and localization of mesoscopic motor control signals for human ECoG neuroprosthetics. J Neurosci Methods 167: 63–81.
- 21. Chao ZC, Nagasaka Y, Fujii N (2010) Long-term asynchronous decoding of arm motion using electrocorticographic signals in monkeys. Front Neuroeng 3:3.
- 22. Pistohl T, Schulze-Bonhage A, Aertsen A, Mehring C, Ball T (2012) Decoding natural grasp types from human ECoG. Neuroimage 59: 248–260.

- 23. Parameshwaran D, Crone NE, Thiagarajan TC (2012) Coherence potentials encode simple human sensorimotor behavior. PLoS ONE 7: e30514.
- 24. Ball T, Kern M, Mutschler I, Aertsen A, Schulze-Bonhage A (2009) Signal quality of simultaneously recorded invasive and non-invasive EEG. Neuroimage 46: 708–716.
- 25. Slutzky MW, Jordan LR, Krieg T, Chen M, Mogul DJ, et al. (2010) Optimal spacing of surface electrode arrays for brain-machine interface applications. J Neural Eng 7: 26004.
- 26. Heliot R, Orsborn AL, Ganguly K, Carmena JM (2010) System Architecture for Stiffness Control in Brain-Machine Interfaces. IEEE Trans. Syst. Man Cybern. Part A-Syst. Hum. 40: 732–742.
- 27. Kawase T, Kambara H, Koike Y (2011) A Power Assist Device Based on Joint Equilibrium Point Estimation from EMG Signals. Journal of Robotics and Mechatronics 24:205–218.
- 28. Koike Y, Hirose H, Sakurai Y, Iijima T (2006) Prediction of arm trajectory from a small number of neuron activities in the primary motor cortex. Neurosci Res 55: 146–153.
- 29. Choi K, Hirose H, Sakurai Y, Iijima T, Koike Y (2009) Prediction of arm trajectory from the neural activities of the primary motor cortex with modular connectionist architecture. Neural Netw 22: 1214–1223.
- 30. Shin D, Kim J, Koike Y (2009) A myokinetic arm model for estimating joint torque and stiffness from EMG signals during maintained posture. J Neurophysiol 101: 387–401.
- 31. Weatherall D (2006) The use of non-human primates in research-The Weatherall Report. Available: http://royalsociety.org/The-Weatherall-reporton-the-use-of-non-human-primates-in-research/. Accessed 2012 Sep 30.
- 32. Ting JA, D’Souza A, Yamamoto K, Yoshioka T, Hoffman D, et al. (2008) Variational Bayesian least squares: an application to brain-machine interface data. Neural Netw 21: 1112–1131.
- 33. Ganesh G, Burdet E, Haruno M, Kawato M (2008) Sparse linear regression for reconstructing muscle activity from human cortical fMRI. Neuroimage 42: 1463–1472.
- 34. Nambu I, Osu R, Sato MA, Ando S, Kawato M, et al. (2009) Single-trial reconstruction of finger-pinch forces from human motor-cortical activation measured by near-infrared spectroscopy (NIRS). Neuroimage 47: 628–637.
- 35. Toda A, Imamizu H, Kawato M, Sato MA (2011) Reconstruction of twodimensional movement trajectories from selected magnetoencephalography cortical currents by combined sparse Bayesian methods. Neuroimage 54: 892– 905.
- 36. Yoshimura N, DaSalla CS, Hanakawa T, Sato MA, Koike Y (2012) Reconstruction of flexor and extensor muscle activities from electroencephalography cortical currents. Neuroimage 59: 1324–1337.
- 37. Watanabe H, Sato MA, Suzuki T, Nambu A, Nishimura Y, et al. (2012) Reconstruction of movement-related intracortical activity from micro-electrocorticogram array signals in monkey primary motor cortex. J Neural Eng 9: 036006.
- 38. Sato M (2009) Variational Bayesian Sparse Regression toolbox. ATR Computational Neuroscience Laboratories. Available: http://www.cns.atr.jp/ cbi/sparse_estimation/sato/VBSR.html. Accessed 2012 Sep 30.
- 39. Neal RM (1996) Bayesian learning for neural networks. Lect. Notes Stat. No.

118. New York: Springer-Verlag.

- 40. Sato M (2001) Online model selection based on the variational bayes. Neural Computation 13: 1649–1681.
- 41. Rathelot JA, Strick PL (2009) Subdivisions of primary motor cortex based on cortico-motoneuronal cells. Proc Natl Acad Sci U S A. 106: 918–23.
- 42. Morrow MM, Miller LE (2003) Prediction of muscle activity by populations of sequentially recorded primary motor cortex neurons. J Neurophysiol 89: 2279– 2288.
- 43. Santucci DM, Kralik JD, Lebedev MA, Nicolelis MAL (2005) Frontal and parietal cortical ensembles predict single-trial muscle activity during reaching movements in primates. Eur J Neurosci 22: 1529–1540.
- 44. Pohlmeyer EA, Solla SA, Perreault EJ, Miller LE (2007) Prediction of upper limb muscle activity from motor cortical discharge during reaching. J Neural Eng 4: 369–379.
- 45. Schieber MH, Rivlis G (2007) Partial reconstruction of muscle activity from a pruned network of diverse motor cortex neurons. J Neurophysiol 97: 70–82.
- 46. Flint RD, Ethier C, Oby ER, Miller LE, Slutzky MW (2012) Local field potentials allow accurate decoding of muscle activity. J Neurophysiol 108: 18– 24.
- 47. Stark E, Abeles M (2007) Predicting movement from multiunit activity. J Neurosci 27: 8387–8394.
- 48. Flint RD, Lindberg EW, Jordan LR, Miller LE, Slutzky MW (2012) Accurate decoding of reaching movements from field potentials in the absence of spikes. J Neural Eng 9: 046006.
- 49. Zhuang J, Truccolo W, Vargas-Irwin C, Donoghue JP (2010) Decoding 3-D Reach and Grasp Kinematics From High-Frequency Local Field Potentials in Primate Primary Motor Cortex. IEEE Trans Biomed Eng. 57: 1774–1784.
- 50. Rickert J, de Oliveira SC, Vaadia E, Aertsen A, Rotter S, et al. (2005) Encoding of movement direction in different frequency ranges of motor cortical local field potentials. Journal of Neuroscience 25: 8815–8824.
- 51. Bansal AK, Truccolo W, Vargas-Irwin CE, Donoghue JP (2012) Decoding 3D reach and grasp from hybrid signals in motor and premotor cortices: spikes, multiunit activity, and local field potentials. J Neurophysiol 107: 1337–1355.
- 52. Mollazadeh M, Aggarwal V, Singhal G, Law A, Davidson A, et al. (2008) Spectral modulation of LFP activity in M1 during dexterous finger movements. Conf Proc IEEE Eng Med Biol Soc 2008: 5314–5317.
- 53. Toro C, Cox C, Friehs G, Ojakangas C, Maxwell R, et al. (1994) 8-12 Hz rhythmic oscillations in human motor cortex during two-dimensional arm movements: evidence for representation of kinematic parameters. Electroencephalogr Clin Neurophysiol. 93: 390–403.
- 54. Baker SN, Olivier E, Lemon RN (1997) Coherent oscillations in monkey motor cortex and hand muscle EMG show task-dependent modulation. Journal of Physiology-London 501: 225–241.
- 55. Ohara S, Nagamine T, Ikeda A, Kunieda T, Matsumoto R, et al. (2000) Electrocorticogram-electromyogram coherence during isometric contraction of hand muscle in human. Clin Neurophysiol 111: 2014–2024.
- 56. Nishimura Y, Morichika Y, Isa T (2009) A subcortical oscillatory network contributes to recovery of hand dexterity after spinal cord injury. Brain 132: 709–721.
- 57. Griffin DM, Hudson HM, Belhaj-Saı¨f A, McKiernan BJ, Cheney PD (2008) Do corticomotoneuronal cells predict target muscle EMG activity? J Neurophysiol. 99:1169–986.

