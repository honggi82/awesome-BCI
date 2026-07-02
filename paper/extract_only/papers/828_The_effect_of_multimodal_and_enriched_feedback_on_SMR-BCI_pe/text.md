# The effect of multimodal and enriched feedback on SMR BCI performance

T. Sollfranka, A. Ramsayb, S. Perdikisc, J. Williamsonb, R. Murray-Smithb, R. Leebc, J.d.R. Millánc & A. Küblera,d

- a Department of Psychology I, University of Würzburg, 97070 Würzburg, Germany
- b Department of Computing Science, Glasgow University, Glasgow G12 8QQm, Scotland
- c École Polytechnique Fédérale de Lausanne, 1015 Lausanne, Switzerland
- d Institute of Medical Psychology and Behavioural Neurobiology, University of Tübingen, 72074 Tübingen, Germany

## Corresponding Author:

Dipl. Biol.Teresa Sollfrank: Department of Psychology I, University of Würzburg Workgroup Prof. Dr. Andrea Kübler Marcusstraße 9-11 97070 Würzburg Phone: +49 931 31-89115 Fax: +49 931 31-82424 Email: teresa.sollfrank@uni-wuerzburg.de

Andrew Ramsay: Andrew.Ramsay@glasgow.ac.uk , Room SAW320, Computing Science, 17 Lilybank Gardens, Glasgow G12 8QQ, Scotland

John Williamson: John.Williamson@glasgow.ac.uk, Room 209 Level 2, Eng -Micro & Nanotechnology, 74 Oakfield Avenue, Glasgow G12 8LP, Scotland Serafeim Perdiki: serafeim.perdikis@epfl.ch , EPFL STI IBI-STI CNBI, ELB 118 (Bâtiment ELB), Station 11 CH-1015 Lausanne, Switzerland Roderick Murray Smith: rod@dcs.gla.ac.uk, School of Computing Science, Glasgow University, Glasgow G12 8QQ, Scotland Robert Leeb: robert.leeb@epfl.ch, CRR E1 B1 (Clinique Romande de Réadaptation), Av. Grand-Champsec 90, CP 352, CH-1951 Sion,

Switzerland Jose Millan: jose.millan@epfl.ch, EPFL STI IBI-STI CNBI, ELB 138 (Bâtiment ELB), Station 11, CH-1015 Lausanne, Switzerland

Andrea Kübler: andrea.kuebler@uni-wuerzburg.de, Raum 302,Psychology I, Marcusstrasse 9-11 97070 Würzburg, Germany

Conflicts of Interest Statement Manuscript title: Effect of multimodal and enriched feedback on SMR BCI performance

The authors whose names are listed immediately below certify that they have NO affiliations with or involvement in any organization or entity with any financial interest (such as honoraria; educational grants; participation in speakers’ bureaus; membership, employment, consultancies, stock ownership, or other equity interest; and expert testimony or patent-licensing arrangements), or non-financial interest (such as personal or professional relationships, affiliations, knowledge or beliefs) in the subject matter or materials discussed in this manuscript.

Author names: T. Sollfrank, A. Ramsay, S. Perdikis, J. Williamson, R. Murray-Smith, R. Leeb, J.d.R. Millán & A. Kübler Keywords:

Brain-computer interfaces EEG Sensorimotor rhythms Feedback Multimodality

Highlights:

- - Uncertainty is not static and can vary substantially over time, possibly rendering BCI frustrating for the enduser.
- - The multimodal feedback gives direct continuous feedback about the quality of motor imagery classification.
- - Participants were able to control the BCI with the funnel feedback with better performance during the initial session and less frustration compared to the conventional cursorbar feedback.

ABSTRACT

Objective: This study investigated the effect of multimodal (visual and auditory) continuous feedback with information about the uncertainty of the input signal on motor imagery based BCI performance. A liquid floating through a visualisation of a funnel (funnel feedback) provided enriched visual or enriched multimodal feedback.

Methods: In a between subject design 30 healthy SMR-BCI naive participants were provided with either conventional bar feedback (CB), or visual funnel feedback (UF), or multimodal (visual and auditory) funnel feedback (MF). Subjects were required to imagine left and right hand movement and were trained to control the SMR based BCI for five sessions on separate days.

Results: Feedback accuracy varied largely between participants. The MF feedback lead to a significantly better performance in session 1 as compared to the CB feedback and could significantly enhance motivation and minimize frustration in BCI use across the five training sessions.

Conclusion: The present study demonstrates that the BCI funnel feedback allows participants to modulate sensorimotor EEG rhythms. Participants were able to control the BCI with the funnel feedback with better performance during the initial session and less frustration compared to the CB feedback.

Significance: The multimodal funnel feedback provides an alternative to the conventional cursorbar feedback for training subjects to modulate their sensorimotor rhythms.

## 1. Introduction

Brain Computer Interfaces (BCIs) based on the modulation of sensorimotor rhythms (SMR) classify differences in the electroencephalogram (EEG) elicited by different motor imagery (MI), actual movement or movement preparation (Pfurtscheller et al., 1997) and translate these into control commands, e.g., for a spelling application (Kübler et al., 2001; Perdikis et al., 2014; Wolpaw et al., 2002) or cursor control on a computer screen (Wolpaw et al., 1991). This provides an alternative communication channel for people diagnosed with neurodegenerative diseases such as amyotrophic lateral sclerosis (ALS), who have only residual control of few muscles, which may be unreliable (Kübler et al., 2005). A limiting factor for the use of a traditional SMR based BCI is that vision must not be compromised in the end-user. For instance, several studies showed that in the last stage of ALS (i.e., completely locked-in) the visual sensory channel cannot be used as a reliable BCI input (De Massari et al., 2013; Murguialday et al., 2011). Sensorimotor rhythms (SMR) refer to localized sinusoidal frequencies in the upper alpha band (10–12 Hz) usually accompanied by changes in synchronization in the beta band (13–25 Hz) (Pfurtscheller and Neuper, 2001), which can be recorded over primary somatosensory and motor cortical areas. SMR decreases or desynchronizes (event related desynchronisation, ERD) with movement or movement imagery in the contralateral sensorimotor areas (Halder et al., 2011; Lotze et al., 1999; Neuper et al., 2005; Pfurtscheller and Aranibar, 1979; Schnitzler et al., 1997). Motor imagery is defined as the mental simulation of a kinesthetic movement (Decety and Inqvar, 1990; Neuper et al., 2005). Signal processing algorithms, individual users' characteristics, such as psychosocial and physiological parameters (e.g., fine motor skills) or brain structures, can predict performances for SMR-based BCIs (Blankertz et al., 2010; Halder et al., 2011, 2013; Hammer et al., 2011; Randolph, 2012). Besides these factors, feedback is a necessary feature for initial learning of the BCI skill (Brown, 1970; Kuhlman, 1978; McFarland et al., 1998; Wolpaw et al., 1991, 2002). The end-user have to be properly trained to be able to successfully control their EEG signals, especially for the use of a BCI based on the recognition of mental imagery tasks (e.g., motor imagery, Neuper and Pfurtscheller, 2010).

To learn modulating SMR power, usually unimodal visual feedback is provided: The end-user receives feedback by an extending bar or a moving cursor (Fig. 1) in one or two dimensions according to the classiﬁcation results (Schreuder et al., 2010; Pfurtscheller, 2004, Neuper and Pfurtscheller, 2010). It provides no information about the quality of the mental imagery as it only gives feedback about which MI is classified at any one point in time. This presentation can be inaccurate, because often the input signal contains a degree of uncertainty that can make a precise classification difficult (Hattie and Timperley, 2007; Shute, 2008, van Beers et al., 2002). The crucial step is to extract robustly the relevant information from EEG signals in the presence of various noise sources, signal non-stationarity and with limited amount of data available (McFarland and Wolpaw, 2011; van Erp et al., 2012) and to give meaningful and precise feedback (Hattie and Timperley, 2007; Shute, 2008). Uncertainty is not static and can vary substantially over time. Therefore, we created the visually enriched “funnel feedback” to provide more information about the quality of the EEG signal: we implemented a liquid cursor model in a funnel shape that can provide the end-user with additional information about their input signal. The stability of the EEG was mirrored by the speed of the liquid cursor through the funnel (Fig. 2). Being not in control of a BCI can make its use frustrating (Holz et al., 2015). Frustration has been experienced as problematic in BCI use (Curran and Stokes, 2003) and further Kleih et al. (2010, 2013) showed that learning an SMR-BCI task is facilitated by increased motivation. If the enriched funnel feedback allowed for better learning, frustration may be lowered and motivation increased.

Although the most common feedback is visual, there is evidence that training can be enhanced by providing multimodal feedback with the same granularity and specificity for each modality (Ainsworth, 2006, Lotte et al., 2013). Kaufman et al. (2011) provided their BCI users with a cursor indicating the integrated classifier output, and the instantaneous sign and absolute value, coded as the colour and intensity of the cursor. Results suggested that end-user can deal with a multi-dimensional feedback although no significant increase in performance was

found. Auditory feedback provides an alternative to a visually-based BCI system (McCreadie et al., 2012; Simon et al., 2014), specifically for those potential end-user with impaired vision. Nijboer et al. (2008) found that although the initial BCI performance in the visual feedback group was superior to the auditory feedback group, there was no significant difference in performance at the end of training. A study by Schreuder et al. (2010) showed that the combination of audio and visual feedback did not lead to an enhancement in BCI performance, whereas Gargiulo et al. (2012) concluded, that multimodal feedback could increase performance in some naïve subjects and could relieve the sense of frustration due to the feeling of not being in control of the visual cue. Thus, studies provided mixed results and further investigation is warranted to elucidate the effect of multimodal feedback on SMR-BCI performance.

The goal of this study was to investigate the effects of a multimodal and visually enriched feedback during SMR based BCI control in a between subject design. For this purpose three end-user groups tested three different forms of feedback: conventional unimodal (visual) cursorbar feedback (CB), unimodal (visual) funnel feedback (UF) and multimodal (visual-auditory) funnel feedback (MF) during five training sessions. All enduser had to perform the same left and right hand motor imagery tasks to control the different type of cursor to the left or right side on the screen. The focus of this study was to investigate how feedback can support endusers in learning to control the BCI therefore we abstained from using communicative characteristics, such as “yes/no” to keep the task as simple as possible. We hypothesized that the enriched visual feedback in combination with auditory feedback would facilitate the learning process, lead to better performance and diminish the level of frustration. The presentation of uncertainty information may render end-users confident toward the functionality of the SMR-BCI, especially during the training phase, where the subject tends to explore different mental strategies to determine the optimal one for achieving control. We further predicted, that the multimodal approach would motivate the end-user.

## 2. Methods

- 2.1 Participants

Thirty healthy SMR-BCI novices took part in the study which was approved by the Ethical Review Board of the Medical Faculty, University of Tübingen. Each participant was informed about the purpose of the study and signed informed consent prior to participation. None of the participants was excluded from analysis. Of the 30 participants 20 were women, and mean age of the sample was 27.73 years (SD 6.57, range 19–51); six were left-handed.

- Fig. 1. Experimental design and electrode position: Timing of the paradigm used in the screening session and in the online session with the three different feedback types: cursor bar feedback, visual unimodal funnel feedback and multimodal funnel feedback.

- 2.2 Experimental set-up

[Figure 1]

The participants were seated in a comfortable chair approximately 1 m away from the computer screen. Participants were asked to sit relaxed with eyes open and to avoid any eye and body movements. After the specific task instruction, all participants underwent a screening session (0.5 h). During this period end-users were instructed to perform kinestethic imagery (Neuper et al., 2005) of a movement with their right or left hand, with their arms relaxed. They had to perform three runs with individual breaks in between. Every run consisted of 30 trials with 15 trials per class (left vs right) presented in randomized order. The trial started with the presentation of a fixation cross (2 s). Afterwards one of the two visual cues (arrows pointing left and right) indicated to the participant which type of motor imagery task to perform (2 s, Fig. 1). The period of movement imagery lasted for four seconds and the end-users could control a cursorbar to the left and to the right side, until the screen turned blank. After a two-second pause the next trial started. After the screening session, following a between-subject design, participants were randomly assigned to three feedback groups with ten subjects each. Multimodal funnel feedback: 6 female, aged between 23-51, mean age 30.2 ±7.8 SD; unimodal funnel feedback: 6 female, aged between 19-46, mean age 27.1 ±7.5 SD; conventional cursorbar feedback: 8 female, aged between 23-38, mean age 25.9 ±4.4 SD. They then performed the first training session, consisting of six runs with 20 trials each. The timing was the same in all feedback groups (Fig. 1): Each started with the presentation of a fixation cross at the centre of the monitor. For two seconds a visual cue indicated to the participants which type of motor imagery task to perform (left or right hand). The duration of online feedback depended on the end-user’s ability to control the BCI. It terminated when the decision threshold (classification values: left/right, cursor hit one of the corners of the lower part of the funnel visualization) was reached or by timeout after 15 seconds. During the last two seconds of the trial, the screen

was blank. There were breaks of 5-10 min between the runs, depending on the participants’ individual needs. The subsequent four training sessions were performed on different days over a period of 2-3 weeks. No classifier adaptation or retraining occurred at any time.

[Figure 2]

- Fig. 2. Top left: conventional cursor bar feedback, top right and bottom: visualization of the funnel feedback and the feedback sequence of the unimodal and multimodal funnel display. Multimodality: Each of the three different modes of control corresponded to specific sounds. Auditory feedback was provided simultaneously to changes in the visual display.

Cursorbar (CB) feedback: Visual feedback was provided by a cursorbar that moved to the left and right according to the classification values along a horizontal line between two arrows (Fig. 2 upper left). It provided feedback about which MI was classified at any one point in time (further details on classification in section 2.4).

Visual unimodal funnel (UF) feedback: Visualisation of a liquid cursor moving in a funnel shape connected to a “test tube” at the bottom (Fig. 2 right). The BCI provided two types of information: an estimate of how stable the end-user’s control was and a left/right MI classiﬁcation value. The respective quality of the EEG was visualised as the dispersion of the cursor. The liquid cursor began in an amorphous, diffuse state (Fig. 2, mode of control: incoherent) and remained like this until the stability estimate of the end-user’s EEG signal increased. With larger steadiness in the input signal, the liquid condensed and altered into a transitional mode while it moved to the lower region (mode of control: transitional). The cursor could shift between the two modes of control according to the classification values. When the liquid cursor reached the “test tube”, it remained in a stabilized mode and could not return to one of the previous states, independent of the signal quality, to avoid any negative feedback (mode of control: stabilized). As the input signals became more accurate to discriminate between the two (left and right hand motor imagery) classification values, the end-user could control the liquid cursor to the left and to the right (mode of control: controlled).

Multimodal funnel (MF) feedback: In addition to the described visual feedback participants were provided simultaneously with auditory feedback: The “incoherent” to “transitional” visual state was acoustically discernible by bubble sounds (Fig. 2). Metal sounds were presented while the liquid cursor was in a “stabilized” mode and the movement of the liquid cursor to the left and to the right was supported by the sound of clinking glasses. No sounds were played when moving from “transitional” to “incoherent” or from “controlled” to “stabilized”.

- 2.3 Data acquisition

The EEG was recorded from 16 channels located over the sensorimotor cortex. The locations of the Ag/AgCl electrodes were based on the modified 10-20 system of the American Electroencephalographic Society (Sharbrough, 1991). Each channel was referenced to the left and grounded at the right mastoid (Fig. 1). Impedances were kept below 5kΩ. The EEG was recorded using a g.USBamp amplifier (manufactured by g.tec Medical Engineering GmbH, Austria), notch filtered at 50 Hz and sampled at 512 Hz. Data processing, storage and online display were performed on a conventional laptop with an additional external monitor.

- 2.4 Feature extraction, selection and classification

After the screening session, power spectral density (PSD) features were computed in 1-second sliding windows (Leeb et al., 2013; Polat and Güneß, 2007). EEG signals were first spatially filtered with a local Laplacian derivation and the PSD was estimated within 4–48 Hz with 2 Hz resolution, accounting for 23 frequency bands per channel. The PSD was computed every 62.5 ms using the Welch method (five 25 %–overlapping internal Hanning windows of 500 ms) and was log-transformed to better comply with the normality assumption of the classification method subsequently employed. The overall candidate feature vectors were thus 368 (16x23) band power estimated on combinations of channels and frequency bands. For the classification of left versus right hand motor imagery trials Fisher’s linear discriminant analysis (LDA) was applied. Three to six features were identified as optimal using the Canonical Discriminant Spatial Patterns (CDSP) method, which best discriminated between the two classification values (left versus right hand) within the motor imagery period (Leeb et al., 2013). A classifier was then built for each pair of MI tasks, with the selected MI pair (highest controllability), and the corresponding EEG channels and PSD features identified by the feature selection process, which were used online to control the BCI. In the online feedback sessions, the BCI used the individual classifier of each participant to translate the end-users’ EEG over the sensorimotor area during motor imagery into a continuous output on the computer screen. For the cursorbar feedback the LDA classified a single sample (decision = +-1) and then the bar moved from its current position x, as x = x + decision*dx. dx was adjusted per subject to obtain a movement to the threshold in 0.5 to 2 seconds, depending on individual performance. In the visual unimodal and multimodal funnel feedback, uncertainty in the input signal was displayed by the combination of two visualisations: the liquid cursor that could be moved and deformed by pseudo-physical forces, that was basically a Monte Carlo visualisation, where 60 particles represented the state of the classifiers input: Each particle had a Gaussian density field around it. The physics were defined by attractive and repulsive fields around each particle, which had an inverse-square-exponential falloff such that there was an equilibrium point at a set inter-particle spacing. As the strength of the forces increased, the points coalesced into a single blob and eventually into a fairly solid object. The implementation used an Euler integrator to provide the physics functionality. The second visualisation of uncertainty in the end-users input signal was the movement speed of the liquid cursor along the vertical axis in the funnel shape to the “test tube”. The uncertainty index was computed by calculating the Euclidian distance of the sample from the global mean. The dispersion was a complex nonlinear and time-varying function of the distance; but the cohesive force in the liquid varied monotonically with d_c(x): The classiﬁer assumed a Gaussian distribution N(µc, Mc ) for each prototype of the class c and then, a feature vector x was assigned to the class that corresponded to the nearest prototype, according to the so-called Mahalanobis distance dc(x) (Lotte et al., 2007).

𝑑𝑐(𝑥) =  (𝑥 − 𝜇𝑐)𝑀𝑐−1(𝑥 − 𝜇𝑐)𝑇 (1)

The user interface and the interface to the incoming BCI signal were written as a Python module, using TOBI interfaces C and D, which was established during the TOBI project (EU grant FP7-224631, Tools for Brain-

Computer Interaction, http://www.tobi-project.org/).

- 2.5 BCI performance

Accuracy was calculated as the ratio between the number of correct selections and the total number of selections. The maximum duration of each motor imagery period was up to 15 seconds. If the target side was not reached within this time window, the trial was terminated and separately counted as a ‘time out’ (miss). To decide whether performance was above chance level, indicating that the cursor control and classification rates exceeded chance level and reached statistical significance, the number of trials has to be taken into account. Kübler and Birbaumer (2008) stated that for the two-choice SMR BCI the observed frequencies (of hits (cursor into the correct target) and misses) have to be compared to the expected frequencies given chance performance and can be tested for significance as follows: With

𝑥2 = ∑ (𝑓0−𝑓𝑓𝑒)2

𝑒

(2)

, more than 75 trials (𝑓0, observed frequency; 63% correct trials in one session) have to be hits to get performance above chance level with 𝑓𝑒 as the expected frequency of 60 hits in 120 trials and a 𝑥2 value with a probability of 0.05 (df=1). The percentage of sessions, where performance was above chance level (63%) is indicated in Table 1.

- 2.6 ERD/ERS analyses

EEG signals were visually inspected and trials contaminated with muscle or eye movement activity were removed. The ERD/ERS) was quantified in the artifact-free EEG in the following steps: The ERD/ERS values of the imagery period were calculated by the squared value of the raw EEG over a 250 ms non-overlapping interval across 8 s of each tasks. The ERD/ERS was expressed as percentage power decrease (ERD) or power increase (ERS) and were quantified relative to the baseline (in relation to a 1 s reference interval before the imagery period) for the upper alpha frequency band (10-12 Hz) and beta (13–25 Hz). The natural log ratio of the EEG power value and the baseline power was estimated for all sample points and the ERD was represented as the mean of these. For statistical comparison we computed a 3x5 repeated measures ANOVA, with the ERD values of the imagery period as dependent variable and sessions (5) as within and feedback type (3) as between subjects factors.

- 2.7 Questionnaires

After the last training session, subjects were asked to rate five questions by assigning a score between one and ten (1 = not at all, not very likely and 10 = a lot, very much likely). Questions were related to the feeling of the subject during and after the experiment (see Table 2). There was no time constraint for answering the questions, and the questionnaire was completed immediately following the experiment while the subject was still in the lab. A one-way analysis of variance was conducted to evaluate significant differences in the ratings of the different feedback groups. Tuckey HSD was used for post hoc pairwise comparisons.

## 3. Results

- 3.1 Performance

Feedback accuracy varied largely between participants (mean 62.29% ±16.1%), covering the full range from chance-level performance (63%) to perfect control (100%). For most participants, performance also varied strongly between sessions. More specifically, the intra-participant performance variability between the five training sessions ranged from 3.5% to 21.3% (mean 6.2% ±4.4%, Fig. 3). Above chance level performance (>63% hits) was reached by the end-users in 21 training sessions (42%) in the MF group, in 17 sessions (34%) of the UF group and in 15 sessions (30%) of the CB group (Table 1). One-way ANOVA for the classification results of the screening session did not reveal any significant main effect, indicating that the performance was similar in all three groups. Mean SMR-BCI performance as a function of feedback in the online training sessions is summarized in Table 1. For the online classification in the feedback sessions, a classifier, built on a distinctive data set was applied. The 3x5 repeated measures ANOVA with feedback and number of sessions as independent variables yielded a significant main effect of Session (F4,236=3,00; p=.019) and a significant session x feedback interaction (F8,472=2,11; p=.034). Post hoc comparisons revealed weakest performance for all feedback groups in session 2 (Tuckey HSD test, p=.005) as compared to the initial training session. The cursorbar (CB) feedback group revealed the lowest level of performance during the first session (58.40 ±16.05 SD) but could afterwards continuously increase the level with significantly best results during session 4 compared to the initial session (64.64, SD ±15.03; p=.037). In Session 1 the funnel feedback groups, both unimodal (66.25 ±18.47 SD) and multimodal (66.40 ±20.02 SD) could achieve a significantly better performance as compared to the cursor bar feedback group (MF*CB, t(118)=2,96; p=.004; UF*CB, t(118)=2,53; p=.013). This effect vanished during the following training sessions (Fig. 4). A significant higher occurrence of ‘time outs’ was present in the funnel feedback group across all training sessions (Table 1, F3,255= 1,89; p=.012).

[Figure 3]

- Fig. 3. Feedback performance: The black crosses show the feedback performance averaged across all recorded sessions for each enduser for all feedback groups. Vertical lines indicate performance range for every end-user and the horizontal line indicates above chance level performance (>63% correct responses). End-user were re-ordered by increasing performance. Feedback types are indicated by different grey shades.

[Figure 4]

- Fig. 4. Mean performance values and SE obtained for the three feedback groups during five training sessions. Significant differences between sessions are indicated: p –values 5% (*) and 1% (**) level.
- Fig. 5. Grand average time-frequency representation of significant ERD values (marked in blue, p<0.01) at electrode position Cz pooled for the left and right hand motor imagery periods, for all five training sessions, separately for the three feedback groups. The maps are plotted for the mean duration of a whole trial (0-8 s; x-axis) and for the frequency range of 0-30 Hz (y-axis). A vertical line indicates the cue onset.

[Figure 5]

Fig. 5 shows the grand average time-frequency representations (0-30 Hz) of significant ERD/ERS values at electrode position Cz for all five training sessions for the two tasks (right and left hand motor imagery together). The differentiation of the frequencies between ERD and ERS revealed a mean frequency of the desynchronized components of 10.1 Hz ±1.0 (CB), 10.2 Hz ±1.0 (UF) and 10.2 Hz ±1.1 (MF) and a corresponding frequency of the synchronized components of 12.5 Hz ±1.4 (CB), 12.4 Hz ±1.4 (UF) and 12.5 Hz ±1.2 (MF). This difference was significant for all feedback groups for the alpha band (t(149)=-16,23, p=0), but not for the beta band (13–25 Hz; t(149)=-1,69, p=.108), that is why we excluded the beta band from further analysis. In order to analyse the potential influence of the feedback on the ERD/ERS patterns during task performance in the different sessions, we performed a 3 (Feedback) x 5 (Session) repeated measures ANOVA. The feedback x session interaction and the main effect of feedback were not significant. The main effect of session was significant (F4,36=3,35, p=.023) with higher ERD values in session 1 compared to session 2 (t(29)=2,75; p=.010) and Session 4 (t(29)=3,96; p=0) for all feedback groups.

- 3.3 Questionnaire and user satisfaction

### Quantitative analyses of the questionnaire are shown in Table 2. Post hoc comparisons to evaluate pairwise differences among group means were conducted with the use of Tuckey HSD test since equal variances were tenable. The visualisation of the funnel feedback was rated as more helpful than the CB feedback (MF*CB feedback group, p=.002 and UF*CB p=.006). The MF group reported less frustration (MF*CB feedback group, p=.009) and was afterwards more motivated (MF*CB feedback group, p=.033) as compared to the CB group.

- Table 1 Mean values of accuracies (%) of participants of the three different feedback groups for the offline screening session and across the five training sessions.

- a percentage of correct responses,
- b percentage of ‘time out’ trials,
- c percentage of sessions, where performance was above chance level.

- Table 2 Average ratings per question: Every question could be rated between one and ten (1= not at all, not very likely and 10= a lot, very much likely). Standard deviations are noted in brackets. Quantitative analysis shows that the one-way ANOVA was significant for Question 2 (F(2,17.9)=8,756, p=.001**), Question 4 (F(2,17.1)=5,33, p=.011**) and Question 5 (F(2,15.9) =3,649, p=.040*).

Type of feedback CB UF MF N 10 10 10 Mean screening performancea ±SD 55.05 ±13.43 55.33 ±17.23 57.55 ±15.22 Mean online performancea ±SD 61.04 ±16.53 61.36 ±15.85 64.84 ±17.02 Range online performance 40.00 – 97.00 41.67 – 99.17 44.17 – 98.33 Time out trialsb 16% 27% 25% Above chance level performancec 30% 34% 42%

Question CB UF MF

- 1. Did you find the task difficult? 7.71 (±1,29) 7.11 (±1,21) 6.23 (±1,42)

- 2. Did you find the visualization helpful? 5.33 (±1,41) 7.56 (±1,37 7.87 (±1,64) **

- 3. Did you find the sound helpful? 6.34 (±1,14)

- 4. Did you feel frustration during the experiment? 8.34 (±1,50) 6.45 (±1,92) 5.23 (±2,81) **

- 5. How motivated are you to be test end-user for this kind of experiment again?

5.34 (±1,56) 6.55 (±2,05) 7.21 (±1,71) * p-values 5% (*) and 1% (**) level.

## 4. Discussion

We investigated the SMR-BCI performance as a function of feedback type. Performance was measured as the percentage of correct responses during motor imagery tasks. Averaged for all feedback groups 56% of the enduser performed at least one session above chance level with more than 63% correct responses and could, thus, achieve significant control over the required brain response.

During the initial training session significant better performance was measurable in the MF and UF groups as compared to the conventional CB group. It seems that the enriched unimodal and multimodal online feedback, with information about the quality of the input signal supports an easier approach for BCI control, specifically for untrained end-users. The two modalities of auditory and visual feedback seemed to be not as important as the enriched information of the feedback, as there was no significant difference in performance of the two funnel feedback groups. This is in accordance with Schreuder et al. (2010) who also found no effect of multimodal (auditory and visual) feedback on performance with a BCI using slow cortical potentials as input signal. An efﬁcient feedback should not be too complex, and should be provided in manageable pieces (Lotte et al., 2013). It may be that the visual feedback was too dominant such that the simultaneous auditory feedback did not provide any beneficial information. However, in line with results of Gargiulo et al. (2012) we could also show that multimodal feedback can reduce frustration and enhance motivation, making the use of a BCI more enjoyable. Learning to control a BCI is a complex task and psychological factors like motivation and frustration may play an important role (Kleih et al., 2010; Kleih and Kübler, 2013; Nijboer et al., 2008). Such psychological factors could be influenced by the choice of feedback presentation. An engaging, stimulus-rich feedback (Pfurtscheller et al., 2006, 2007; Pineda et al., 2003) might, in turn, increase the success in controlling a BCI application. A study by Gruzelier et al. 2010 showed that a SMR neurofeedback training in virtual reality (VR) enhanced the artistic performance of actors more successful than a training with a 2D feedback rendition. The efficacy of this training was attributed to the psychological engagement through the ecologically relevant learning context of the immersive VR technology.The liquid cursor in combination with sounds was judged more helpful and descriptive than the conventional CB feedback and the motivation for participating again in another BCI experiment was higher for the MF group than for the CB group. However, on the physiological level the ERD analyses revealed no significant difference between the ERD in the alpha band of sensorimotor areas between the three feedback groups. Significantly highest values of performance and ERD were present only in the first session in all feedback groups and along with training, performance and ERD values of the feedback groups converged. Thus, we may cautiously conclude that the funnel feedback may support the initial training phase and represents an alternative feedback for an SMR BCI. Another explanation for the significantly better performance during the initial training session could be due to the fact that we did not include any online adaptation (Blankertz et al., 2007). Classification accuracy is certainly affected by inter-session non-stationarity of brain patterns and the uncertainty metric used for the funnel might be even more affected by this issue. This may explain the drop of performance in subsequent sessions of the funnel feedback group, which did not occur in the conventional cursorbar group. In each group were also end-users who did not achieve any significant cursor control. This phenomenon is known as BCI illiteracy (Hammer et al., 2011; Kübler and Müller, 2007; Vidaurre and Blankertz, 2010), and it seems to be present in 10-30% of potential BCI end-users (Blankertz et al., 2010; Guger et al., 2003). Approaches to alleviate this phenomenon have been explored, such as improved signal processing (Blankertz and Vidaurre, 2010). Blankertz et al. (2007) demonstrated that participants, who had no peak of the sensory motor idle rhythm at the beginning of the experiment, could develop such peak during the course of the session with an end-user-optimized state-of-the-art classifier. They developed the BBCI – a machine learning BCI approach – which provides BCI control during the first session after 20 min screening period. A statistical analysis of the screening measurement is used to adapt the system to the specificities of the end-user`s current brain signals. Kindermans at al. (2010) could show that a combination of Reservoir Computing and a feature selection algorithm based on Common Spatial Patterns can be used to improve performance in an uncued motor

imagery based BCI. They enhanced the discrimination of the motor imagery classes which made the system more robust against potential changes in the environment. Besides online, or even offline adaptation in the classifier, other factors like training, new task instructions and feedback (Allison and Neuper, 2010; Lotte et al., 2013; Pfurtscheller et al., 2006, 2007) can also play an important role in learning to control a BCI. We decided to train end-user with a non-adaptive classifier to focus on the potential effect of an enriched feedback and to be able to exclude any other factors besides the type of feedback.

A rather unexpected result was that there was no improvement of classification accuracy with training and overall performance in all groups was surprisingly low. Contrarily, all four patients with amyotrophic lateral sclerosis of the Kübler et al. (2005) study were able to achieve SMR-regulation of more than 75% accuracy within less than 20 training sessions. Performance was around chance level during the first 10 sessions, but increased significantly during the last 10 sessions. A study by Nijboer et al. (2008) also showed that healthy participants were able to control an SMR based BCI with solely auditory feedback. Although BCI performance in the visual feedback group was superior to the auditory feedback group there was no difference in performance at the end of the third training session. Participants in the auditory feedback group learned slower, but four of eight end-user reached an accuracy of more than 70% correct responses in the last session which was comparable to the visual feedback group. Both studies have in common that the participants had to perform a high number of trials: In the study of Nijboer and colleagues (2008) around 2070 trials were conducted in 3 sessions, and Kübler et al. (2005) included a minimum of 3200 to even 10500 trials in 20 sessions, depending on the physical and psychological condition of the patient. For end-user with low control the duration of a trial was maybe too long. In some trials the liquid cursor remained in the centre of the test tube and it was not possible or too exhausting for the end-user to maintain motor imagery over the 15 seconds before the ‘time out’ occurred. A significant higher number of ‘time outs’ were found in the funnel feedback groups compared to the CB group and every ‘time out’ was rated as a miss, even though the tendency of the cursor was toward the correct target. On average, the experiment for the funnel feedback took 2.2h, whereas the same number of trials in the CB feedback training was often faster. This may have had a negative impact on the accuracy results of the funnel feedback groups.

## 5. Conclusions

Taken together, healthy participants were able to control a BCI when presented with multimodal funnel feedback of SMR including information about uncertainty. The enriched visual feedback in combination with auditory feedback lead to a significantly better performance in the initial training session. Such feedback may boost initial performance, but beneficial effects were not maintained. Studies possibly with more training sessions are required to replicate this finding and to elucidate the long-term effect. Independent of performance, multimodal funnel feedback was rated more helpful, more motivating, and less frustrating than the unimodal and cursorbar feedback. Especially in the operant conditioning approach feedback plays an important role in learning to control a BCI. The herein presented results can partly support our hypothesis and contribute to the idea that an enriched feedback can support end-users in learning to control an SMR-BCI. Thus, the multimodal funnel feedback represents an alternative approach for training end-users to modulate their SMR and may be advantageous for training adherence. It can facilitate the initial training phase and render end-users confident toward the functionality of the SMR-BCI. Combined with adaptive classification and feature selection approaches, more distinct differences might arise between feedback types.

## Acknowledgement

This work is partly supported by the GK Emotion (Research Training Group RTG 1253/2) and the Graduate School of Life Sciences of the University of Würzburg and the EU grant FP7-224631 “TOBI” (Tools for BrainComputer Interaction) project. This paper only reflects the authors’ views and funding agencies are not liable for any use that may be made of the information contained herein.

## References

Allison B, Neuper C. Could anyone use a BCI? ,in Brain–Computer Interfaces: D.S. Tan, A. Nijholt (Eds.), Human–Computer Interaction Series, Springer, London (2010), pp 35-54.

Blankertz B, Dornhege G, Krauledat M, Müller KR, Curio G. The non-invasive Berlin Brain-Computer Interface: fast acquisition of effective performance in untrained subjects. NeuroImage 2007; 37, 539-550.

Blankertz B, Sannelli C, Halder S, Hammer E, Kübler A, Müller KR, Curio G, Dickhaus T. Neurophysiological predictor of SMR-based BCI performance. NeuroImage 2010; 51, 1303–1309.

Blankertz B, Vidaurre C. Towards a Cure for BCI Illiteracy. Brain Topogr 2010; 23:194-198. Brown B. Recognition of aspects of consciousness through association with EEG alpha activity represented by light signal. Psychophysiology 1970; 6(4):442-452. Curran E, Stokes M. Learning to control brain activity: A review of the production and control of EEG components for driving brain–computer interface (BCI) systems. Brain Cognition 2003; 51:326–336. De Massari D, Ruf CA, Furdea A, Matuz T, van der Heiden L, Halder S, Silvoni S, Birbaumer N. Brain communication in the locked-in state. Brain 2013; 136(6): 1989-2000. Decety J, Inqvar D. Brain structures participating in mental simulation of motor behavior: a neuropsychological interpretation. Acta Psychol 1990; 73(1): 13–34.

Gargiulo GD, Mohamed A, McEwan A, Bifculo P, Cesarelli M, Jin C, Tapson J, van Schaik A. Investigating the role of combined acoustic-visual feedback in one-dimensional synchronous brain computer interfaces, a preliminary study. Med Devices 2012; 5: 81-88.

Gruzelier J, Inoue A, Smart R, Steed A, Steffert T. Acting performance and flow state enhanced with sensorymotor rhythm neurofeedback comparing ecologically valid immersive VR and training screen scenarios. Neurosci Lett, 2010; 480(2): 112-116.

Guger C, Edlinger G, Harkam W, Niedermayer I, Pfurtscheller G How many people are able to operate an EEGbased brain–computer interface (BCI)? IEEE T Neu Sys Reh 2003; 11(2): 145–147.

Halder S, Agorastos D, Veit R, Hammer EM, Lee S, Varkuti B, Bogdan M, Rosenstiel W, Birbaumer N, Kübler A. Neural mechanisms of brain–computer interface control. NeuroImage 2011; 55(4): 1779-1790.

Hammer EM, Halder S, Blankertz B, Sannelli C, Dickhaus T, Kleih S, Müller KR, Kübler A. Psychological predictors of SMR-BCI performance. Biol Psychol 2011; 89(1): 80-86.

Hattie J, Timperley H. The power of feedback. Rev Educ Res 2007; 77: 81–112.

Holz E, Botrel L, Kaufmann T, Kübler A. Long-Term Independent Brain-Computer Interface Home Use Improves Quality of Life of a Patient in the Locked-In State: A Case Study. Arch Phys Med Rehab 2015; 96(3):16-26.

Kindermans PJ, Buteneers P, Verstraeten D, Schrauwen B. An Uncued Brain-Computer Interface Using Reservoir Computing. Workshop: machine learning for assistive technologies, Proceedings 2010; 1447714.

Kleih S, Nijboer F, Halder S, Kübler A. Motivation modulates the P300 amplitude during brain–computer interface use. Clin Neurophysiol 2010; 121(7): 1023-1031.

Kleih SC, Kübler A. Empathy, motivation, and P300-BCI performance. Front Hum Neurosci 2013; 7:642. Kübler A, Birbaumer N. Brain-computer interfaces and communication in palysis: Extinction of goal directed thinking in completely paralysed patients? Clin Neurophysiol 2008; 119 (11): 2658-2666.

Kübler A, Müller KR. Introduction to brain–computer interfacing. In: Dornhege, G., Millan, J.d.R., Hinterberger, T., McFarland, D., Müller, K.-R.(Eds.), Towards Brain–Computer Interfacing. MIT Press, Cambridge, MA, 2007.

Kübler A, Neumann N, Kaiser J, Kotchoubey B, Hinterberger T, Birbaumer N. Brain–computer communication: self-regulation of slow cortical potentials for verbal communication. Arch Phys Med Rehab 2001; 82: 1533– 1539.

Kübler A, Nijboer F, Mellinger J, Vaughan TM, Pawelzik H, Schalk G, McFarland DJ, Birbaumer N, Wolpaw JR. Patients with ALS can use sensorimotor rhythms to operate a brain–computer interface. Neurology 2005; 64: 1775-1777.

Kuhlmann WN. EEG feedback training: enhancement of somatosensory cortical activity. Electroen Clin Neuro 1978, 45: 290-294.

Leeb R, Perdikis S, Tonin L, Biasiucci A, Tavella M, Molina A, Al-Khodairy A, Carlson T, Millán JdR. Transferring brain-computer interfaces beyond the laboratory: Successful application control for motor-disabled users. Artif Intell Med 2013; 59(2):121–132.

Lotte F, Congedo M, Lécuyer A, Lamarche F, Arnaldi B. A Review of Classiﬁcation Algorithms for EEG-based Brain-Computer Interfaces. J Neural Eng 2007; 4: 1-13.

Lotte F, Larrue F, Mühl C. Flaws in current human training protocols for spontaneous Brain-Computer Interfaces: lessons learned from instructional design. Front Hum Neurosci 2013; 7: 568.

Lotze M, Montoya P, Erb M, Hülsmann E, Flor H, Klose U, Birbaumer N, Grodd W. Activation of Cortical and Cerebellar Motor Areas during Executed and Imagined Hand Movements: An fMRI Study. J Cognitive Neurosci 1999, 1(5): 491-501.

McCreadie KA, Coyle DH, Prasad G. Learning to modulate sensorimotor rhythms with stereo auditory feedback for a brain-computer interface. (EMBC), Annual International Conference of the IEEE 2012: 67116714.

McFarland D, McCane L, Wolpaw J. EEG-based communication and control: short-term role of feedback. IEEE Trans Rehab Eng 1998; 6: 7–11.

McFarland D, Wolpaw J. Brain-computer interfaces for communication and control. Commun ACM 2011; 54: 60–66.

Murguialday AR, Hill J, Bensch M, Martens S, Halder S, Nijboer F, Schoelkopf B, Birbaumer N, Gharabaghi A. Transition from the locked in to the completely locked-in state: a physiological analysis. Clin Neurophysiol

- 2011; 122(5): 925-33.

Neuper C, Pfurtscheller G. Neurofeedback trainingfor BCI control. Brain-Computer Interfaces, eds B. Graimann,G. Pfurtscheller and B. Allison (London: Springer), 2010; 65–78.

Neuper C, Scherer R, Reiner M, Pfurtscheller G. Imagery of motor actions: Differential effects of kinesthetic and visual-motor mode of imagery in single-trial EEG. Cognitive Brain Res 2005; 25: 668-677.

Nijboer F, Furdea A, Gunst I, Mellinger J, McFarland DJ, Birbaumer N, Kübler A. An auditory brain-computer interface (BCI). J Neurosci Meth 2008a; 167(1): 43-50.

Nijober F, Sellers EW, Mellinger J, Jordan MA, Matuz T, Furdea A, Halder S, Mochty U, Krusienski DJ, Vaughan TM, Wolpaw JR, Birbaumer N, Kübler A. A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clin Neurophysiol 2008b; 119(8):1909-16.

Perdikis S, Leeb R, Ramsay A, Tavella M, Desideri L, Hoogerwerf EJ, Al-Khodairy A, Murray-Smith R, Millán JdR. Clinical evaluation of Brain Tree, a motor imagery hybrid BCI speller. J Neural Eng 2014; 11:036003.

Pfurtscheller G, Aranibar A. Evaluation of event-related desynchronization preceding and following voluntary self-paced movement. Electroen Clin Neuro 1979; 46(2): 138–146.

Pfurtscheller G, Brunner C, Schlogl A, Lopes da Silva FH. Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of different motor imagery tasks. NeuroImage 2006; 31: 153–159.

Pfurtscheller G, Neuper C, Flotzinger D, Pregenzer M. EEG-based discrimination between imagination of right and left hand movement. Electroen Clin Neuro 1997; 103: 642–651.

Pfurtscheller G, Neuper C. Motor imagery and direct brain-computer communication. Proceedings of the IEEE 2001; 89(7): 1123-1134.

Pfurtscheller G, Scherer R, Leeb R, Keinrath C. Viewing Moving Objects in Virtual Reality Can Change the Dynamics of Sensorimotor EEG Rhythms. Presence 2007; 16(1): 111–118.

Pineda J A, Silverman DS, Vankov A, Hestenes J. Learning to control brain rhythms: making a brain-computer interface possible. IEEE Trans Neural Syst Rehabil Eng 2003; 11: 181-4.

Polat K, Güneß K. Classification of epileptiform EEG using a hybrid system based on decision tree classifier and fast Fourier transform. Appl Maths Comput 2007; 187: 1017–1026.

Randolph AB. Not all created equal: individual-technology fit of brain-computer interfaces. System Science (HICSS), 2012 45th Hawaii International Conference on 2012; 572-578.

Schnitzler A, Salenius S, Salmelin R, Jousmäki V, Hari R. Involvement of primary motor cortex in motor imagery: a neuromagnetic study. NeuroImage 1997; 6(3): 201–208.

Schreuder M, Blankertz B, Tangermann M. A new auditory multi-class brain-computer interface paradigm: spatial hearing as an informative cue. PloS One 2010; 5: e9813.

Simon N, Käthner I, Ruf C, Pasqualotto E, Kübler A, Halder S. An auditory multiclass brain-computer interface with natural stimuli: Usability evaluation with healthy participants and a motor impaired end user. Front Hum Neurosci 2014; 8: 1039.

Van Beers RJ, Baraduc P, Wolpert DM. Role of uncertainty in sensorimotor control. Roy Soc 2002; 357: 11371145.

van Erp J, Lotte F, Tangermann M. Brain-computer interfaces: beyond medical applications. IEEE Comput 45,

- 2012; 26–34. Vidaurre C, Blankertz B. Towards a Cure for BCI Illiteracy. Brain Topogr 2010; 23:194-198.

Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan T. Brain-computer interfaces for communication and control. Clin Neurophysiol 2002; 113(6): 767-791.

Wolpaw JR, McFarland DJ, Neat GW, Forneris CA. An EEG-based brain-computer interface for cursor control. Electroen Clin Neuro 1991; 78(3): 252–259.

