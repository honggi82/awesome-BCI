ORIGINAL RESEARCH published: 28 February 2017 doi: 10.3389/fnhum.2017.00078

# Evaluation of a Dry EEG System for Application of Passive Brain-Computer Interfaces in Autonomous Driving

Thorsten O. Zander1,2*, Lena M. Andreessen1,2, Angela Berg1, Maurice Bleuel1, Juliane Pawlitzki1, Lars Zawallich1, Laurens R. Krol1,2 and Klaus Gramann1,3

1 Biological Psychology and Neuroergonomics, Technical University of Berlin, Berlin, Germany, 2 Team PhyPA, Biological Psychology and Neuroergonomics, Technical University Berlin, Berlin, Germany, 3 Center for Advanced Neurological Engineering, University of California San Diego, San Diego, CA, USA

We tested the applicability and signal quality of a 16 channel dry electroencephalography (EEG) system in a laboratory environment and in a car under controlled, realistic conditions. The aim of our investigation was an estimation how well a passive Brain-Computer Interface (pBCI) can work in an autonomous driving scenario. The evaluation considered speed and accuracy of self-applicability by an untrained person, quality of recorded EEG data, shifts of electrode positions on the head after driving-related movements, usability, and complexity of the system as such and wearing comfort over time. An experiment was conducted inside and outside of a stationary vehicle with running engine, air-conditioning, and muted radio. Signal quality was sufﬁcient for standard EEG analysis in the time and frequency domain as well as for the use in pBCIs. While the inﬂuence of vehicle-induced interferences to data quality was insigniﬁcant, driving-related movements led to strong shifts in electrode positions. In general, the EEG system used allowed for a fast self-applicability of cap and electrodes. The assessed usability of the system was still acceptable while the wearing comfort decreased strongly over time due to friction and pressure to the head. From these results we conclude that the evaluated system should provide the essential requirements for an application in an autonomous driving context. Nevertheless, further reﬁnement is suggested to reduce shifts of the system due to body movements and increase the headset’s usability and wearing comfort.

Edited by:

Mikhail Lebedev, Duke University, USA

Reviewed by: Nima Bigdely-Shamlo,

Qusp, USA Tjeerd W. Boonstra,

University of New South Wales, Australia

Tomas Emmanuel Ward, Maynooth University, Ireland

*Correspondence: Thorsten O. Zander tzander@gmail.com

Received: 08 January 2016 Accepted: 08 February 2017 Published: 28 February 2017

Keywords: autonomous driving, passive BCI, EEG, usability, ERP

## INTRODUCTION

Citation: Zander TO, Andreessen LM, Berg A,

Driving has become a part of everyday life, which makes the drive to work or for recreational activities a simple routine task. However, the eﬀects of the mental workload and eﬀort required by driving often go unnoticed. A study by Borghini et al. (2014) found that mental workload, fatigue, and drowsiness are signiﬁcantly increased while driving. Especially long periods of constant driving, as often performed by professional truck drivers, result in an accumulation of these eﬀects over time, decreasing the driver’s cognitive capabilities and driving performance, thus increasing the chances of traﬃc accidents.

Bleuel M, Pawlitzki J, Zawallich L,

Krol LR and Gramann K (2017) Evaluation of a Dry EEG System for

Application of Passive Brain-Computer Interfaces in

Autonomous Driving. Front. Hum. Neurosci. 11:78. doi: 10.3389/fnhum.2017.00078

The ﬁeld of automotive human factors and ergonomics is concerned with minimizing safety risks depending on human performance in driving tasks. Today, many automations and small devices have found their way into cars in order to help reduce the mental workload required to operate the vehicle (Young and Stanton, 1997; Tadaka and Shimoyama, 2004; Ma and Kaber, 2005). A diﬀerent approach aims to fully or at least partly automate the task of driving, so the human driver can be eliminated as a risk factor in most instances. The scientiﬁc ﬁeld working toward this goal is called Autonomous Driving (Franke et al., 1998) and has grown more important over the past years.

One particular problem with autonomous driving is the question of responsibility: Who is accountable in case of an accident? Most countries still deﬁne the human driver of a car as the entity responsible for anything that happens while driving (Beiker, 2012). Therefore, experts believe it would be best to only automate some of the tasks that arise while driving, but to leave the most complex tasks to a human driver for the time being. According to Sukthankar et al. (1997), the task of driving consists of diﬀerent levels, which are the strategic level (route planning), the tactical level (maneuver selection), and the operational level (maneuver operation). Automation of the lowest, operational level is thus legally the least complex, and also technically possible (Dickmanns and Zapp, 1987; Pomerleau, 1992). Driving along a highway could relatively easily be automated, but once the traﬃc situation changes, the human may be required to take over control. This approach thus requires an important exchange of information between the human driver and the automated system: The human must be timely and appropriately informed of the pending takeover. As stated by Llaneras et al. (2013), people tend to focus their attention on secondary tasks once the primary objective of driving has been taken over by automation. As a consequence, in a situation where the car drives autonomously, a signal given by the system to indicate the necessity for takeover might be missed, or might catch the human by surprise. This may result in loss of control over the vehicle.

As a solution to the above problem, the car could monitor the driver’s mental state, and adapt the notiﬁcation process to the current context. A completely attentive driver might quickly perceive and understand even simple signals, whereas for example a sleeping driver may need to be woken carefully by the car in advance of leaving the highway. Passive braincomputer interfaces (passive BCIs, Zander and Kothe, 2011) are promising approaches for such monitoring and automated adaptation (Zander et al., 2011). This technology enables realtime detection of mental conditions like fatigue, workload, and degree of relaxation (Blankertz et al., 2010; Gerjets et al., 2014), which oﬀer a good estimate of whether or not the driver is ready to take over control of the car. But the passive BCI approach during autonomous driving is not limited to this. More general information—like mood or situational awareness—and also very speciﬁc information about the subjective interpretation of the current context—that might be reﬂected in the driver’s brain as error responses—could be assessed by the passive BCI (Zander and Jatzev, 2012). This information could then be integrated in the autonomous decisions of the car. The car learns how the driver interprets the context and gains a

degree of context-awareness by utilizing the driver’s brain as a sensor.

Passive BCIs are commonly based on electroencephalography (EEG). Traditional EEG systems are relatively cumbersome to apply and use, requiring preparation of the skin, application of conductive gel, and cleaning of the cap afterwards. To make EEG applicable for non-scientiﬁc uses, e.g., to be used by drivers, its application and handling needs to be as easy as possible. This is why alternative electrode systems (e.g., described in Zander et al., 2011; Liao et al., 2012) are an important focus of autonomous driving related BCI research. Primarily, the use of gel is eliminated, and the caps containing the electrodes are made for quick application, resulting in less preparation time and, ideally, more comfortable for the wearer. Recent laboratory studies provided evidence of good signal quality, comparable to that of standard gel-based electrodes. It is still unclear however that the signal quality can be maintained in real-world contexts.

This study focused on evaluating the use and application of a dry electrode EEG system in the context of a running vehicle. It was assessed how easy it is for untrained person to apply the system on their own head, how well the electrodes can be positioned and remain in place, and whether the signal quality is suﬃcient for BCI usage when the system is self-applied. Two common features in the EEG, an N200-P300 ERP and the parietal alpha rhythm, were analyzed as examples of signals that potentially can be used in a passive BCI application. Furthermore, interference in the EEG signal resulting from usage inside a running car—a noisy environment—was investigated. Finally, wearing comfort over a prolonged period of time as well as general user acceptance were evaluated.

MATERIALS AND METHODS Participants

Ten participants, ﬁve male, participated in the experiment. The mean age was 28 years (SD = 3.4). Two participants reported to have sensitive skin. All participants gave their written informed consent to participate in the study and were paid 20 euros as expense allowance. The overall duration of the experiment was on average 165min (SD = 39min.), including breaks.

Apparatus

Vehicle

The vehicle we used to evaluate the inﬂuence of vehicleinduced noise on the recorded EEG was a Volkswagen Touran (year of manufacture 2003). The car was stationary during the experiments, but had the engine running, the radio switched on (though muted), and the air conditioning enabled. A 7.6′′ TFTdisplay was mounted to the right of the steering wheel near the center console.

Experimental Room

The experimental room used for baseline recordings was a nonfrequented room at the TU Berlin with constant light, right next to the parked car. Diversions and disturbances were kept to a minimum.

|[Figure 1]<br><br>FIGURE 1 | Overview of the used EEG system, the Brain Products actiCAP Xpress. Image courtesy of Brain Products GmbH.|
|---|

Computer System

The EEG system was connected to a laptop (Sony Vaio Z, 2012) and EEG data was recorded using the BrainVision Recorder, BrainVision RDA (Brain Products GmbH, Munich, Germany), and LabRecorder (as part of the BCILAB framework, Delorme et al., 2010). The experimental paradigms were run using SNAP1 (Iversen and Makeig, 2013). To analyze the data, we used the EEGLAB toolbox (Delorme and Makeig, 2004), an open source toolbox embedded in MATLAB. For classiﬁcation we used the open source toolbox BCILAB (Kothe and Makeig, 2013), also embedded in MATLAB.

EEG System

The system examined in this study was the Brain Products actiCAP Xpress dry-electrode EEG system (see Figure 1) provided by Brain Products GmbH for the duration of the experiment. The system included 16 active data electrodes plus one reference and one ground electrode. Electrodes were applied to one of two diﬀerently-sized ﬂexible caps, depending on the head circumference of the participant (52–58, or 58–64cm). To ensure ﬁxation on the participant’s head, a chin belt was attached to the cap. Each cap provided 78 possible electrode positions most of the extended international 10% system, with additional options to set up regions of interest. We used electrode positions

- Fp1, Fp2, Fz, FC5, FC6, C3, C4, Cz, CPz, Pz, CP5, CP6, PO3, PO4, POz, and Oz.

To adjust the system to an individual participant, the electrodes can be extended to diﬀerent shapes and sizes by attaching so-called QuickBits (see Figure 2). The kit used in the study came with six T-shaped ﬂat tips (with a diameter of 7mm) to be attached to the forehead and earlobes, as well as 32 mushroom-head tips for application on the scalp. These latter come in diﬀerent lengths of 8, 10, 12, and 14mm, which can be attached to the electrodes according to head shape and required pressure. This enabled a personalization of the system: Optimal

1Simulation and Neuroscience Application Platform (SNAP). Available: https://github.com/sccn/SNAP.

|[Figure 2]<br><br>FIGURE 2 | The different QuickBit types provided with the actiCAP Xpress. Image courtesy of Brain Products GmbH.|
|---|

sensor lengths for electrode positions can be noted, stored and re-applied in follow-up experiments.

Prior to applying the actiCAP Xpress, the electrodes were cleaned using a disinfectant spray. This was done even in case the electrodes and sensors had not been used before to remove dust and particles to improve connectivity.

The electrode array was connected to a V-Amp EEG signal ampliﬁer (Brain Products GmbH, Munich, Germany), which in turn was connected to a laptop computer through a universal serial bus (USB) 2.0.

Experimental Procedure

Experimental Rationale

This study was designed to assess diﬀerent requirements to an EEG system for application in real-world driving scenarios. We deﬁned the following requirements: (1) self-applicability of the system, (2) impact of interfering noise signals inside a running vehicle on EEG signal quality, (3) stability of cap and electrode positions after context-related movements, and (4) usability and wearing comfort of the system.

The experiment was divided into four blocks covering these four issues, answering the following questions.

- 1. How easy and accurate is self-application of the system in comparison to application by another person? (Block I)
- 2. How strong is the eﬀect of interfering signals in a running car on EEG recording? (Block II)
- 3. How do electrode positions change during typical body movements inside a car? (Block III)
- 4. How do participants rate the system’s usability? (Block IV)

Figure 3 summarizes the experimental session. After arrival of the participant, the experiment was explained and a demographic survey was conducted. While the cap was personalized by the investigator by exchanging electrode tips where necessary, the participant was asked to read the instruction manual of the system, in preparation for Block I.

Block I: Self-application

Self-application of the cap, as opposed to having the cap ﬁtted to you by a trained operator, may take a diﬀerent amount of time and may aﬀect the positioning of the electrodes and the signal quality. To estimate these eﬀects, we compared cap application

|[Figure 3]<br><br>FIGURE 3 | Experiment timeline.|
|---|

in two conditions: Application by the experimenter, and selfapplication by the participant. Customization of the cap was not included here, as it is assumed to be a one-time eﬀort.

Participants were seated in the experimental room, in front of a laptop. A stopwatch was used to ﬁrst measure the time required by the experimenter to apply the EEG cap to the participant’s head.

Once the cap and ground/reference electrodes were in place, electrode positions were measured using the Polaris Vicra system (Northern Digital Inc., Waterloo, ON, Canada), allowing for measuring 3-dimensional electrode locations. We chose to record the 16 electrode positions, as well as the inion, the nasion and the left and right preauricular points. The latter three were used as coordinate references to allow the transformation of coordinates taken from diﬀerent measuring sessions into one coordinate system to allow comparison (described below in the section “Analysis Procedures”). To achieve comparable, stable

positions for the reference points in each measurement during the experiment, we marked them by a small dot on the respective positions on the participant’s skin using a removable eudermic marker.

Following this, signal quality was optimized by relatively ﬁne-grained adjustments to the electrodes. As the system did not provide an objective measure of signal quality or electrode contact (e.g., impedance), signal quality was assessed visually. The signal was monitored using the BrainVision Recorder software, with all 16 channels displayed at once, set to a resolution of 50 µV. A display ﬁlter was enabled, bandpass-ﬁltering the visible signal from 0.1 to 40Hz, not aﬀecting the recording. The duration of this optimization was again timed using a stopwatch. The resulting signal quality was also recorded, as rated by the experimenter. The indication for signal quality was the visual form of the signal on the display, artifacts had to be recognized visually. The rating followed predeﬁned guidelines and was done

on a 5-point scale with 5 meaning “perfect signal” and 1 meaning “no signal at all” (see Figure 4). This rating was done twice: Once for the signals with the display ﬁlter switched on, and once based on the unﬁltered raw signal.

Following this, the cap was removed and participants, who read the instructions manual, were asked to put on the cap by themselves, after all of their questions about the procedure had been answered by the experimenter. Application time was again measured, as were the electrode positions and the resulting signal quality.

- Block II: EEG Recording For investigating signal quality in standard EEG analyses we chose the well-known N200 and P300 components of the visual event-related potential and the parietal alpha rhythm. Both time- and frequency domain parameters are well-examined phenomena in EEG research. Hence, clear expectations about morphology, topography and signal strength can be drawn, that build the baseline of comparison for our results.

In order to assess the EEG signal and the possible inﬂuence on it of the electromagnetically noisy environment that is the car, participants performed in two established experimental paradigms of BCI research (Zander et al., 2011), once in the experimental room, and once inside the car. The order of these two conditions was randomized between participants.

The ﬁrst paradigm focused on the elicitation of visual eventrelated potentials (ERPs) using a standard oddball approach: An

infrequent deviant stimulus sometimes appeared instead of the frequent standard stimuli (Duncan-Johnson and Donchin, 1977; see Figure 5). This is a common approach when researching ERPs referred to as the N200-P300 complex (Polich and Kok, 1995; Linden, 2005). ERP detection during autonomous driving can be useful, as they may allow a car to detect how drivers react cognitively to perceived stimuli/information.

On the screen, participants saw a circle divided by lines into 30◦ angles. First, a bar appeared, like a clock’s arm pointing 12 o’clock. This bar then rotated clockwise in discrete steps, once every second. A standard stimulus had it rotate by 90◦; a deviant consisted of an initial 60◦ rotation, followed by a 100ms pause and a 15◦ counterclockwise rotation. After each deviant, the bar disappeared and reappeared at the 12 o’clock position.

10% of all stimuli were deviants. In total 400 trials were displayed (360 standard, 40 deviant).

The second paradigm focused on features in the spectral domain, speciﬁcally the parietal alpha rhythm. This feature is of special interest to autonomous driving, as parietal alpha can be used as an indicator of whether the participant is currently in a relaxed state or performing some mentally demanding task (Berka et al., 2007). It also is a standard example for features in the spectral domain.

The paradigm (see Figure 6) presented to the participant was designed to induce changes in parietal alpha activity by alternating between two states of mind: Engaged and relaxed. To engage the participant, a six-letter word was presented letter

|[Figure 4]<br><br>FIGURE 4 | Examples for signal quality ratings on a scale from one to ﬁve. Green colored parts indicate adequate signal quality, yellow parts moderate signal quality, and red parts unacceptable signal quality.|
|---|

|[Figure 5]<br><br>FIGURE 5 | Oddball Paradigm.|
|---|

|[Figure 6]<br><br>FIGURE 6 | Induced Alpha Paradigm.|
|---|

by letter, with letters appearing on random locations on the screen amidst visual noise. Each letter was only visible for 1s. Participants were instructed to read the word. After each engagement trial, the participant was instructed simply to relax for 6s with their eyes open. This relaxation phase was introduced using an auditory signal and ended by a similar one with lower pitch.

There were 32 trials of each condition. The order of words in the engaged condition was randomized across participants.

These two paradigms were presented in ﬁxed order to the participants in the two conditions (room vs. car).

- Block III: Driving-Related Movements The third block investigated the inﬂuence of movements on the position of the electrodes.

Electrode positions were recorded, using again the Polaris system mentioned earlier, at the start of this block. Participants then performed a series of three diﬀerent types of drivingrelated movements inside the car, and the electrode positions were measured again after each group of movements. Because measurements were not done inside the car but in a nearby room, some walking was required. Electrode cables were bundled together and ﬁxed to the participant’s clothing in a relaxed way to minimize their strain on the cap while walking.

To make movements comparable between participants, we placed markers (sticky notes) at certain places in the car: One on the left rear window, one above the driver’s seat, one in the legroom of the front passenger seat and one in the center of the rear bench seat. Before seating the participant in the driver’s seat, the markers were shown to them. The EEG system was not connected to the ampliﬁer during the movements.

All instructions for diﬀerent movements were given through pre-recorded audio ﬁles played back using a laptop and speakers inside the car.

Block IV: Usability

To assess the usability of the system, the participants were asked to ﬁll out a questionnaire right after Block I. This questionnaire was the System Usability Scale (SUS; Brooke, 1986) was employed, also used in other BCI related studies prior to this one (Pasqualotto et al., 2011; Duvinage et al., 2012). SUS is a standardized questionnaire consisting of ten questions based on Likert scales with ﬁve options ranging from “strongly disagree” to “strongly agree.” In total, SUS contains ﬁve positively and ﬁve negatively formulated questions about the system being assessed, for example “I think that I would like to use this system frequently” or “I found the system unnecessarily complex.” From the answers given, a SUS score is calculated, ranging between 0 (worst possible system) and 100 (best possible system). This score has to be interpreted taking the individual context of system usage into account. In contrast to qualitative assessments, the SUS does not yield any insight into which usability problems exactly are present within the system. It provides however a quick and reliable way to determine whether or not major changes are necessary in order to make the system safe and comfortable to use.

Additionally, the participants were asked to rate the level of comfort wearing the system after each of the previously described experimental blocks (I–III) on a scale from 1 to 10, one meaning “extremely bad” and ten “very comfortable.” We acquired these three subjective impressions to gather insight into how the system’s perceived comfort changed over the course of the experiment.

To get an even deeper insight into the comfort of wearing the system, participants were asked to ﬁll out another questionnaire after the third experimental block, after roughly 140min of wearing the system almost constantly. We adapted a questionnaire for the evaluation of the wearing comfort for ﬁremen helmets (Fabrizio and Cimolino, 2014), by only keeping questions deemed ﬁtting to our context. All questions were rated on a ﬁve point Likert scale. In addition to these questions, we asked two yes-no questions: Whether or not the participant believed the cap had moved, and whether or not it induced the feeling of dents on their head. Finally, we asked the participants to mention any discomfort associated with wearing the system, like the feeling of pressure on the head, headaches, or nausea.

Analysis Procedures

Block I: Self-application

Comparison of time needed by the experimenter and the participant to apply the system and to adjust the electrodes was done by two-sample t-tests.

The signal quality ratings were subjected to a three-way mixed measures ANOVA with the two within-subject factors visual ﬁlters (no ﬁlters vs. 0.1–40Hz bandpass) and electrode (Fp1 vs.

- Fp2 vs. vs. Fz vs. FC5 vs. FC6 vs. C3 vs. C4 vs. Cz vs. CPz vs. Pz vs. CP5 vs. CP6 vs. PO3 vs. PO4 vs. POz vs. Oz) and the between-subject factor applicant (investigator vs. participant).

Because a total of six diﬀerent measurements of electrode positions were taken during the course of this experiment, these measurements were ﬁrst transformed into one coordinate system to allow a uniﬁed comparison. To this end, all measurements were re-referenced to a mean head middle and radius, within participants, as follows.

1. All coordinates of recording j, j = 1,...,6 were referenced to the head midpoint hmj, which is calculated with the recorded reference points (nasion nj and left and right preauricular points, lpj and rpj) by

- a. Drawing a line through both preauricular points lpj and rpj:

Calculate the slope by computing new coordinates (uj)i : = (lpj)i − (rpj)i,for i = 1,2,3 denoting the

scalars of the three-dimensional vector uj. Deﬁne the line by

gj := lpj + rjuj with rj to be determined.

- b. Construction of a plane Hj through nj, which is perpendicular to the line gj:

Find the variables x,y,z to determine the plane equation for Hj

Hj : (uj)1 x + (uj)2y + (uj)3z := e. To ﬁnd e, insert the coordinates of the nasion reference point nj into the equation

Hj(nj) : (uj)1 (nj)1 + (uj)2 (nj)2 + (uj)3 (nj)3 = e.

c. For the purpose of ﬁnding the intersection of the line gj with the plane Hj, insert the coordinates of gj into the plane equation above and solve for rj:

Hj gj : rj =

e − (uj)1(lpj)1 − (uj)2(lpj)2 − (uj)3(lpj)3 (uj)21 + (uj)22 +(uj)23

.

Inserting rj into the plane equation yields the head midpoint:

hmj = lpj + rjuj.

- 2. After calculating the head midpoints hm1 to hm6, we compute the arithmetic average hm over all recordings as the ﬁnal reference point in order to minimize the error of measurement in the system.

- 3. The deviation of the recorded head midpoint hmj to hm is calculated for each recording:

dj := hmj − hm , j = 1,...,6.

- 4. Then, all recorded electrode positions (epk)j, k = 1,...,16 are re-referenced to hm by addition with dj and the euclidean distance edj1j2 between diﬀerent recordings j1,j2 is calculated:

(dj1j2)i := ((epk)j1 + dj1)i − ((epk)j2 + dj2)i, edj1j2 : = (dj1j2)21 + (dj1j2)22 + (dj1j2)23

The value used for comparison of diﬀerent recordings j1, j2 was this euclidean distance edj1, j2.

For Block I, recorded positions from the investigator-applied cap were compared to the positions from the self-applied cap. Mean diﬀerences of electrode positions were then compared to the expected value of no diﬀerence in positions using a onesample t-test against zero.

### Block II: EEG Recordings Oddball paradigm: ERP analysis

EEG data was ﬁrst preprocessed by applying a bandpass-ﬁlter from 1 to 30Hz, retaining all frequencies relevant for later analyses. Then, epochs of 1100ms were extracted, starting 100ms before stimulus onset of the standard and deviant events. Baseline correction was performed with a 100ms pre-stimulus interval.

To compare event-related activity between car and indoor recordings, amplitudes and latencies of the N200’s and P300’s were extracted.

First, the indoor condition was used as a baseline as it conforms to laboratory conditions. Inspection of the grand average revealed a global negative minimum at 300ms over the centro-parietal lead (Pz) and a global positive maximum at 400ms over the centro-central lead (Cz). Based on these peaks, a search window was deﬁned around 300 ± 70 and 400 ± 70ms to search for maxima in the individual averages. Once for each individual the global peaks were identiﬁed, the peaks on individual channels were identiﬁed using a ± 25ms

window around the individual global peak. Mean amplitudes and latencies were extracted for all channels. This procedure resulted in a 4 x 16 vector for each participant, consisting of the mean amplitudes and the latencies of the two components at each channel.

For comparison of mean peak amplitudes two repeated measures ANOVAs were performed. Mean amplitudes from electrode Pz were used for the negativity and from Cz for the positivity. Each 2x2 ANOVA had the two within-participant factors recording condition (indoor vs. car) and stimulus (standard vs. deviant).

In order to examine disparities of mean peak latencies between conditions (indoor vs. car), mean diﬀerence peak latencies were calculated by subtracting the negative from the positive peak latency. The mean diﬀerence was taken per participant for the two conditions and subjected to a paired sample t-test.

To test for equivalence of EEG measures between recording conditions the two one-sided tests (TOST, Schuirmann, 1981, 1987; Westlake, 1981) procedure was applied to mean peak amplitudes and mean diﬀerence peak latencies with an epsilon of the standard deviation of the indoor condition, which was regarded as the control group (R-package “equivalence” May 14, 2016; V0.7.2). A p-value of 0.05 was taken as the signiﬁcant threshold for all TOST.

### Induced alpha paradigm: frequency analysis

To compare oscillatory features between car and indoor recordings, three diﬀerent measures were taken: The power spectral density function covering 0.1–40Hz, single measurements of the band power in the alpha band, and the time course of the alpha band power during the 6-s trials of the paradigm (engaged vs. relaxed).

Fluctuations in alpha power occur with a broader distribution over posterior areas of the scalp (Sauseng et al., 2005). Since we were interested in parietal alpha as potential indicator of mental load, analyses were restricted to ﬁve posterior electrodes, namely Pz, PO3, PO4, POz, and Oz. The data was bandpass ﬁltered from 0.1 to 40Hz and time epochs of 6s were selected, covering each full trial.

Power spectral densities (PSD) were calculated for each entire epoch and averaged per participant, resulting in 2 x 2 x 5 PSD distributions for each participant (2 experimental conditions x 2 mental states x 5 channels). We used these participant-individual PSDs as well as the averaged PSDs over all participants (grand average), resulting in a total of 11 (2 x 5+1) PSD-distributions for each experimental condition.

Individual and grand average Pearson Correlation of the PSD in the frequency band of 0.1 Hz to 40Hz were calculated for each electrode between indoor and car conditions and tested for signiﬁcance using one sample t-tests against zero.

The alpha band (7–13Hz) being of prime interest here, we also calculated a single bandpower value in this frequency range for each participant, electrode, and trial. We used epochs of 4s length, starting 2s after stimulus onset. Logarithmic variances of each trial per electrode of each participant were calculated and normalized with the maximum value of each electrode. These measures were then averaged over all trials, resulting in

a normalized mean alpha band power for each participant under each experimental condition on the ﬁve investigated electrodes. Eﬀects between recording conditions, stimuli and electrodes were investigated in a 2 x 2 x 5 ANOVA with the three withinparticipant factors recording condition (indoor vs. car), stimulus (standard vs. deviant) and electrode (Pz vs. PO3 vs. PO4 vs. POz vs. Oz). The factor electrode is a repeated measure here as EEG measures at one electrode depend on values measured by other electrodes. Again, the TOST procedure with an epsilon of the standard deviation of the indoor condition was applied to normalized mean alpha band power values to test for equivalence between recording conditions.

As a third measure, the time course of the band power in the alpha band was used. It was calculated by shifting a 500ms window over each single trial and calculating the band power for each window position. To avoid leakage eﬀects, the window was multiplied with a Gaussian bell curve of the same size. Afterwards the single-trial measurements were normalized with the mean of all band powers. The normalized measurements were averaged, resulting in 2 x 5 time courses for each participant (2 experimental conditions x 5 channels). As above, we also took the grand average into account, resulting in 11 time courses in total per experimental condition.

To examine the diﬀerence in the time course of the band power in the alpha range between conditions, Pearson Correlations were calculated for each participant, channel and condition.

### BCI Analysis of both paradigms

BCILAB’s built-in classiﬁcation approaches were used to evaluate the oﬄine single-trial accuracies as an estimate of potential online performance.

For the oddball paradigm, data was bandpass ﬁltered from 0.1 to 15Hz and downsampled to 100Hz. Epochs of 800ms were extracted starting at each stimulus marker. A windowed-means approach (Blankertz et al., 2011) was used to extract features, using 8 consecutive windows of 50ms starting at 300ms poststimulus. As a classiﬁer we used linear discriminant analysis, LDA (Webb, 2002). Mean ERP classiﬁcation error rates of all eight participants were subjected to a paired samples t-test.

Logarithmic band power was used for feature extraction (SolisEscalante et al., 2010; Zander et al., 2011) of the data of the second paradigm. This was applied to epochs of 6s, as above. We performed a (10 x 10)-fold cross-validation, and classiﬁed using LDA. Mean classiﬁcation error rates were subjected to a paired samples t-test.

Classiﬁcation error rate results from both paradigms were subjected to a TOST procedure with an epsilon of the standard deviation of the indoor condition to test for equivalence between recording conditions.

Block III: Driving-Related Movements

Each of the three movement groups had one electrode position measurement before, and one after it. Mean diﬀerences of electrode positions prior to and after each movement group were compared to the expected value of no diﬀerence in positions using a one-sample t-test against zero.

- Block IV: Usability The System Usability Scale was interpreted following the guidelines set by Brooke (1986). To determine the resulting SUS score of the system, all given answers were weighted accordingly and added up. This resulted in a total score per participant, which then was multiplied by the factor 2.5.

After experimental blocks I to III, participants were asked to give a subjective estimate of how comfortable the system felt. The median of the comfort ratings of all participants was used as the overall comfort rating here. To test for diﬀerences between the three time points, a Wilcoxon Signed-rank test was applied. The wearing comfort questionnaire was evaluated descriptively.

RESULTS Block I: Self-application

Application Time

A two-samples t-test indicated that the mean time needed for application of the cap did not diﬀer signiﬁcantly between experimenter (M = 123.2s, SD = 43.8) and participants (M = 104.9s, SD = 49.0), t(9) = 0.880, p = 0.391, though showing a tendency that participants perform faster. Mean times needed for adjustment of electrodes also did not diﬀer signiﬁcantly between investigator (M = 256.3s, SD = 221.3) and participants (M = 310.2s, SD = 285.1), t(9) = 0.472, p = 0.642, showing a tendency that experimenters are faster.

Electrode Signal

The three-way mixed measures ANOVA on signal quality ratings revealed no signiﬁcant main eﬀect of applicant, F(1, 18) = 0.341, p = 0.341, η2 = 0.019. The main eﬀect of ﬁlter was signiﬁcant, F(1, 18) = 66.861, p = 0.000, η2 = 0.788. Since the main eﬀect of electrode violated the assumption of sphericity GreenhouseGeisser corrected values were used. The main eﬀect electrode was signiﬁcant, F(5.167, 93.012) = 2.876, p = 0.017 η2 = 0.138. None of the interaction eﬀects were signiﬁcant, all ps > 0.281.

Electrode Positions

The t-test against zero performed on mean diﬀerences of electrode positions (M = 13.76mm, SD = 5.12mm) between investigator- and self-applied cap yielded signiﬁcance, t(9) = 8.498, p = 0.00001. The electrode positions varied most on the midline of the head, with 15.5mm variation (averaged over all 10 participants) at Oz to 16.1mm averaged variation at Fz. This could be due to the structure of the cap: It has two holes for the ears, so electrodes in this area are ﬁxated more clearly than electrodes elsewhere. Electrodes on the forehead can be positioned up to 1cm higher or lower without any obvious eﬀects on the cap like inconvenience or ill-ﬁttingness, so it was hard for both participants and investigators to position the cap correctly around the midline of the head (see Figure 7).

For Block I, recorded positions from the investigator-applied cap were compared to the positions from the self-applied cap. Mean diﬀerences of electrode positions were then compared to the expected value of no diﬀerence in positions using a onesample t-test against zero.

|[Figure 7]<br><br>FIGURE 7 | Shifts in electrode positions after self application in mm compared to application by investigator.|
|---|

Block II: EEG Recordings

Due to software problems on a laptop EEG data of two participants had to be excluded. Analyses of the EEG data were based on the remaining eight participants.

Oddball Paradigm: ERP Results

Grand average ERPs from the oddball paradigm are depicted in Figure 8. The repeated measures ANOVA performed on mean amplitudes of the negativity measure yielded signiﬁcance for the main factor stimulus, F(1, 7) = 21.745, p = 0.002, η2 = 0.756. Amplitudes of the deviant stimuli (M = −5.44 µV, SD = 6.21 µV) were more negative than in standard stimuli (M = −0.01 µV, SD = 2.66 µV). The main factor environment was not signiﬁcant, F(1, 7) = 0.101, p = 0.760, η2 = 0.014. There was also no signiﬁcant interaction, F(1, 7) = 0.261, p = 0.625, η2 = 0.036. Results of a TOST procedure with an epsilon of the standard deviation of the indoor condition were not signiﬁcant (mean diﬀerence = 0.145; epsilon = 3.95; conﬁdence-interval: −6.79 to 7.08; df = 7; p = 0.166).

For the positivity measure there was no signiﬁcant main eﬀect of stimulus, F(1, 7) = 5.001, p = 0.060, η2 = 0.417. The main eﬀect environment also was not signiﬁcant, F(1, 7) = 2.767, p = 0.140, η2 = 0.283. The interaction between stimulus and environment was signiﬁcant, F(1, 7) = 31.800, p = 0.001, η2 = 0.820. Amplitudes of the deviant trials were higher indoors (M = 9.54 µV, SD = 9.05 µV) than in the car (M = 5.18 µV, SD = 10.57 µV), while amplitudes in standard trials indoors (M = 0.02 µV, SD = 1.25 µV) were only slightly smaller than in the car (M = 0.92 µV, SD = 2.27 µV). Due to this signiﬁcant interaction eﬀect no TOST was performed.

Results from the t-test performed on mean peak latency diﬀerences of the indoor (M = 85ms, SD = 46.3ms) and the car condition (M = 101.5ms, SD = 75.1ms) were not signiﬁcant (p = 0.569). The TOST procedure with an epsilon of the standard deviation of the indoor condition showed no signiﬁcance for

|[Figure 8]<br><br>FIGURE 8 | Grand average ERPs of the indoor condition (top left) and the running car condition (top right) on channel Cz. Deviant (bottom left) and standard (bottom right) ERPs in comparison between indoor and car condition.|
|---|

mean peak latency diﬀerences (mean diﬀerence = −16.5; epsilon

= 46.3; conﬁdence-interval: −68.8 to 35.8; df = 7; p = 0.158).

Induced Alpha Paradigm: Frequency Results

All individual correlation values for power spectral densities between conditions were higher than 0.79 on all ﬁve electrodes, with a mean correlation value of 0.97 (SD = 0.046). All t-tests of these correlations against zero were signiﬁcant with ps < 0.0001. For the grand average, correlation values between indoor and car condition were both higher than 0.989, with a mean of 0.997 (SD = 0.004). T-tests against zero yielded signiﬁcance (ps < 0.0001) for both conditions (engaged/relaxed).

The three-way repeated measures ANOVA with withinsubject factors recording condition (p = 0.061), stimulus (p = 0.177), and electrode (p = 0.24) performed on mean alpha band powers was not signiﬁcant on main or interaction eﬀects, with non-signiﬁcant interactions (all ps > 0.272). The TOST procedure with an epsilon of the standard deviation of the indoor condition assigned to mean alpha band powers showed signiﬁcance on electrodes PO4 (mean diﬀerence = 0.049; epsilon = 0.129; conﬁdence-interval: −0.031 to 0.128; df = 7; p = 0.049) and Oz (mean diﬀerence = 0.001; epsilon = 0.127; conﬁdenceinterval: −0.079 to 0.076; df = 7; p = 0.009). The TOST was not signiﬁcant for electrodes PO3, POz, and Pz, all ps > 0.340.

Alpha band time course (see Figure 9) correlations between indoor and car condition yielded a mean correlation of r = 0.27 for the relaxed condition (Pz: r = 0.43, PO3: r = 0.26, PO4: r =

0.29, POz: r = 0.30, Oz: r = 0.09). Correlations in this condition were signiﬁcant on all ﬁve electrodes for ﬁve participants (ps < 0.00001), on four electrodes for one participant (ps < 0.005), and for the other three participants on three electrodes (ps < 0.021). In the engaged condition the mean correlation of all participants was r = 0.23 (Pz: r = 0.34, PO3: r = 0.19, PO4: r = 0.18, POz: r = 0.31, Oz: r = 0.14). Tests yielded signiﬁcance of correlations on all ﬁve channels for three participants (ps < 0.043). For three participants correlation was signiﬁcant on four channels (ps < 0.00001) and for two participants on three electrodes (ps < 0.00001).

BCI Results of Both Paradigms

A paired samples t-test indicated that the error rates for ERP classiﬁcation in the indoor condition (M = 0.126, SD = 0.086) did not diﬀer signiﬁcantly from the error rates in the car condition (M = 0.145, SD = 0.116), t(7) = −0.68149, p = 0.518. Furthermore, the TOST procedure with an epsilon of the standard deviation over participants in the indoor condition conﬁrmed signiﬁcant equivalence classiﬁcation results in the two recording conditions (mean diﬀerence = 0.018; epsilon = 0.086; conﬁdence-interval: −0.032 to 0.069; df = 7; p = 0.020).

A paired samples t-test indicated that the error rates of band power classiﬁcation for the indoor condition was lower (M = 0.283, SD = 0.160), but did not diﬀer signiﬁcantly from the error rates in the car condition (M = 0.351, SD = 0.137), t(7) = −1.608, p = 0.152. The TOST procedure with an epsilon of the

|[Figure 9]<br><br>FIGURE 9 | Grand Averages of the alpha band time courses for relaxed and engaged conditions indoors and in the car. For the red and the green curve, displaying the relaxed conditions, a similar pattern starting 1s after onset of stimulus presentation is observed. Similarities over time are also apparent for the engaged conditions, represented in the black and blue curve. Clear co-variation of indoor and in car alpha time courses for both relaxed and engaged conditions is proven by high correlation between the signals.|
|---|

|[Figure 10]<br><br>FIGURE 10 | Shifts in electrode positions after movements of the head (A), the arms (B), and the whole body (C) in mm.|
|---|

standard deviation over the participants in the indoor condition conﬁrmed signiﬁcant equivalence for classiﬁcation results in the two recording conditions (mean diﬀerence = 0.066; epsilon = 0.162; conﬁdence-interval: −0.012 to 0.144; df = 7; p = 0.026).

- Block III: Driving-Related Movements Figure 10 shows the shifts in electrode positions after each of the three groups of movements.

After head-related movements the diﬀerence between electrode positions (M = 9.6, SD = 9.1) diﬀered signiﬁcantly from zero, t(9) = 3.3237, p = 0.009. The apparent lateralization of this eﬀect (25.3mm mean variation at CP5 vs. 19.6mm at CP6) may be due to the direction of the shoulder check.

After performance of arm movements the mean diﬀerence between electrode positions (M = 7.6, SD = 4.8) diﬀered signiﬁcantly from zero, t(9) = 5.0241, p = 0.001. Variations were located mainly to the right side of the head with a maximum of 10.5mm mean variation at PO4. The cause for this may be the direction of the rotation and/or handedness of participants.

Mean electrode position diﬀerences after whole-body movements (M = 8.4, SD = 6.4) diﬀered signiﬁcantly from zero, t(9) = 4.1691, p = 0.002. The greatest shift was on the forehead with 10.1mm average variation on Fp2 and on the midline of the head (8.2 and 9.3mm mean variation at POz and Fz). This could be caused by the cables, which were tied together, but interfered with the seatbelt nevertheless.

Block VI: Usability

The total SUS score of the system added up to 65. Following the oﬃcial SUS score interpretation, this is slightly above the threshold for an acceptable system.

Due to minor delays during the experiments, the time points of the additional questionnaires varied slightly for each participant. On average, questions were answered after 60 (Block I), 122 (Block II), and 137.5 (Block III) min.

After the ﬁrst 60min, the system got a comfort rating of 7.5, which then decreased signiﬁcantly over the next hour resulting in a rating of 3 after 122min. In the following quarter of an hour needed for block III, the comfort rating stayed stable at 3.

A Wilcoxon signed-rank test showed that there was a signiﬁcant diﬀerence between the ﬁrst time point of the rating after 60min (Mdn = 7.5) and the second rating after 122min (Mdn = 3), (W = 0, Z = −2.69, p = 0.008). No valid Wilcoxon signed-rank test could be performed to compare the second and third ratings, because the number of eﬀective samples was less than 6 after subtraction of ratings equaled zero for six participants (W = 4, Z = −0.82, p = 0.625). Rating scores of the ﬁrst and the third rating again showed signiﬁcant diﬀerences, (W = 0, Z = −2.67, p = 0.008).

The six examined items of wearing comfort of the system are summarized in Figure 11. A feeling of pressure on the head was rated as the most irritating with a mean score of 2.2. The overall impression of wearing comfort got a mean score of 2.7, and was therefore also perceived as bad. The overall weight of the system on the head was on average rated as the most pleasant aspect of it with a score of 4.2.

Furthermore, the wearing comfort questionnaire yielded the following insights. Seven participants complained about dents and chafe marks on their heads, four about headaches, and one each about neck pains, nausea, and dizziness. Moreover, one participant had the subjective impression that the system had moved over the course of the experiments. None of the participants reported skin irritations due to wearing the cap.

DISCUSSION Block I: Self-application

We found that the participants were equally fast as the experimenter in applying the cap, and equally capable in optimizing signal quality. We thus conclude that this type of dry electrode EEG system can indeed be used by individual endusers. We should note, however, that there was no objective measure of when the application was ﬁnished; it was based on individual judgements of the experimenter.

We did not investigate the personalization of the cap by adjusting the length of each electrode pin, because this task needs to be done only once. Therefore, we did not investigate how easy it is to personalize the cap while wearing it. Personalization did, however, take up quite some time. We assume that the QuickBit approach would beneﬁt from improvement: Continuously adjustable bits would probably simplify personalization and optimize the result.

While it is not surprising that the signal quality was rated better with active display ﬁlters, we had assumed that the signal quality would be better after adjustments by an expert operator than compared to that adjusted by the participant. This, however, was not the case: Participants reached a similar, sometimes even better signal quality. We assume the reason for this to be that participants had a better feeling for how hard, and where exactly the electrodes pressed against their heads, allowing them to ﬁt them even better to the scalp than the experimenter could without the risk of harming the participant.

For the electrode positions, some variation in the measurements must be taken into account. The used system has known variations in measured data points, and for some electrodes (primarily at the back of the head), the measuring stylus may have moved slightly due to head shifts that were sometimes necessary for the measurement. This problem was addressed mathematically, as described above. It was also not possible to point the stylus exactly at the electrode’s point of contact with the skin, but only at the electrode’s body. It remains unclear, whether or to what extent the diﬀerences in electrode positions we measured, imply that the points of contact changed as well.

Block II: EEG Recordings

For the oddball paradigm ERP analysis revealed highly similar morphology of ERPs elicited by deviant stimuli in both recording conditions. We found highly signiﬁcant eﬀects for the negative

|[Figure 11]<br><br>FIGURE 11 | Mean score of questions about wearing comfort.|
|---|

peak in the ERP condition. The deviant trials were signiﬁcantly diﬀerent from the standard trials in both the indoor and the car condition, showing no diﬀerence between conditions. This is not the case for the positivity. The main eﬀect is not signiﬁcant. It should be mentioned though that we have a clear tendency into the right direction with a p value slightly missing the threshold criteria of 5%. Peaks of the P300 are reduced in the car environment as a result of other signals interfering with the recorded signal in the car. No signiﬁcant diﬀerences were found between peak latencies between indoor and car recordings. We conclude that the main information carried in the signal is comparable for indoor and in car recordings, but its signal strength is attenuated slightly in the car condition.

For the alpha recordings, we have a slightly more complex case. We clearly see a correlation between conditions—alpha values show a similar development over time outside of and in the car. However, there is no signiﬁcant diﬀerence between relaxed and engaged trials on average over all participants, which was expected from the experimental design. When we take a closer look at the individual values (see Figure 12), we see that some participants managed to get relaxed in the corresponding task, while others did not. This explains why we do not get signiﬁcant main eﬀects—several participants were not able to relax in the appropriate condition. This eﬀect can be seen consistently on both conditions, inside and outside the car. However, we do perhaps see a tendency on the main eﬀect of condition that, even though it’s not signiﬁcant, indicates a small change in alpha power between recordings inside and outside of the car.

For all comparisons that showed no signiﬁcant diﬀerence between conditions an equivalence test was performed. Features of the ERP were not equivalent between conditions while spectral features were equivalent on some of the tested electrodes.

These results show that even though we do not have signiﬁcant diﬀerences, the recoded data cannot be taken equivalent. For strict neurophysiological measurements it hence might be worth a consideration whether the tested headset should be used or not.

For ERP and spectral data classiﬁcations were not signiﬁcantly diﬀerent, and were furthermore clearly equivalent. We, hence,

assume that the evaluated system measured the diﬀerences in cognitive states, well, in both conditions. Despite small morphological and power diﬀerences, classiﬁcation results were comparable in both domains. Therefore, a BCI can be applied with equal reliability to data from both conditions.

The results we found on the EEG components examined here are as expected from the literature and replicate results from a previous comparison study (Zander et al., 2011). Therefore, we conclude that the dry electrode system investigated here provides comparable data to a conventional gel-based system when used in an autonomous driving context.

It still remains unclear whether the results can be fully transferred to a real-world autonomous driving context where the car would most likely be moving. A driving car would bring additional factors like increased vibration from the engine, jerks due to uneven roads, or inertial eﬀects induced by direction changes. Moreover, the driving task itself could lead to additional artifacts, such as stress related sweating on the scalp and the user scratching their own skin. Also head movements against the headrest might lead to changes of electrode positions in a way that was not examined here. Another factor would be the radio not being muted in a real-world-driving scenario: Environmental noises between 70 and 120 decibels have been found to increase the amplitude of measured P300 events (Nam et al., 2008). Drivers will also be moving e.g. their heads and hands, which they minimized during data recording. This study however presents a ﬁrst step in investigating the applicability of dry systems in a car environment, revealing initial insights in a scenario with controlled artifact activity. These results can form the basis for future studies in active driving study scenarios, where that control is further relaxed.

Block III: Driving-Related Movements

The results showed that the electrodes shifted in position when executing diﬀerent driving-related movements.

The most signiﬁcant shifts occurred during movements involving the head directly, primarily at the rear left of the head.

|[Figure 12]<br><br>FIGURE 12 | Mean alpha power in relaxed and engaged trials for individual subjects.|
|---|

We assume this was due to the shoulder check, which required a sudden, fast turn of the whole head to the left and back. We can, however, not be sure as to whether the shoulder check or the look at the ceiling had more eﬀect on the electrodes positions since they were measured together as one movement group. Either way, the resulting diﬀerences may well-inﬂuence the quality of the data recorded by the system.

The performed arm movements had less impact on the electrode positions, though the shifts were still signiﬁcant.

The third group of movements resulted in the least position changes for all electrodes although the participants had to move their whole upper body—including the head. The most pronounced shifts were observed at the right frontal area. The instruction to touch the marker in the legroom of the passenger seat might oﬀer an explanation for this, as the head had to be moved rather far to the right and down. Also in the area around the left ear increased shifts in position were observed. Most likely, this was a result of fastening and unfastening the seatbelt which may have induced some strain in that area, maybe by pulling on the cables.

Finally, since the movements were always performed in the same order (head, arm, and body), order eﬀects cannot be excluded.

For future use, the cap could be applied e.g., only after the seat belt has been fastened, which often requires some eﬀort. Since the cables may also have caused some of the position shifts, a wireless system is preferable.

- Block IV: Usability The System Usability Scale is a general questionnaire to evaluate the usability of technical systems, and is not speciﬁcally designed for BCI systems. As SUS provided signiﬁcant insights in other BCI-related studies, we decided to use it here as well (Duvinage et al., 2012; Käthner et al., 2013). Some questions however, especially about the interaction with the system, did not ﬁt the current purpose and even confused some of the participants. The resulting SUS score might therefore not be entirely accurate, but, we believe, still provides a good indication about the overall usability of the system in an autonomous driving context.

The evaluation of the wearing comfort was better tuned to the current context and raised no questions from participants. The results showed that the ﬁrst hour of using the system did not bother the participants much, which qualiﬁes it for shortterm usage at least. After the second hour of using the system, however, the subjective comfort ratings dropped signiﬁcantly and participants began to complain about dents, slight headaches, neck pain, even nausea and dizziness, which clearly shows that the EEG system with the current cap design is not suitable for long-term use. We did not investigate recovery time: How long a break is needed, before the cap can be comfortably worn again? This remains an open question.

The most annoying features of the system, according to the participants, were its rather tight ﬁt onto the head resulting in the feeling of pressure. The overall weight of the system was, in contrast, rated to be quite pleasant which might be caused by the ﬂexible, thin material of the cap. Also, participants rated the adaptability of the cap as quite high. The cap was rated as being

ﬁxated well, thanks to the chin belt and the holes for the ears providing a lot of stability–only one participant had the feeling the cap had moved at all.

## CONCLUSION

Concluding in brief, the EEG system allowed for technically sound recordings, even with car-induced interferences present. It thus appears to be suitable for passive BCIs in autonomous driving scenarios, allowing mental states to be detected in real time.

In only a few minutes, individuals were able to apply and adjust a pre-customized cap, with the help of a little mirror, like the rear view mirror of a car. A system to better support the evaluation of signal quality would be beneﬁcial, however.

According to the system usability scale, the system is at the edge of acceptability in terms of usability. This may suﬃce for professional drivers, who likely stand to gain the most from autonomous driving and supportive systems, but room for improvement remains. In particular the reported discomfort after longer use is unacceptable. Here, major improvement is necessary to decrease pressure on the scalp so the system is no longer obstructive and uncomfortable, hindering the users from focusing on themselves and their tasks.

Seeing now that EEG technology has made clear progress toward ease of use and mobile scenarios, we can envision the application of passive BCIs in the context of autonomous driving. Passive BCIs can provide essential information about the driver’s cognitive or aﬀective state, which can be combined with other sensor data of the car. In that way, the car can adapt to, and make decisions informed by, individual aspects of the driver. As passive BCIs do not rely on directed or even conscious actions of the driver (Zander and Kothe, 2011), the car will still drive autonomously but gains an additional stream of information, pertaining to the subjective situational interpretation of the driver.

For example, we can clearly imagine applications improving safety and comfort. In cases where the driver is required to take over control, the communication of this requirement can be adapted to the current, actual state of the driver. Another scenario would be the detection of whether or not communicated alarm signals were perceived and processed by the driver. These are only a few, simple examples of a broad range of applications to be thought of.

Moreover the investigated system could be used in a broader ﬁeld of scenarios and might be of special interest for the ﬁeld of Mobile brain/body imaging (MoBI). The ﬁeld’s objective is to acquire neurophysiological recordings of human cognition in real world environments where subjects perform real-world tasks. A portable, wireless, high-quality data recording and fast to prepare dry contact system would prove useful for brain activity recordings on actively behaving participants (Gramann et al., 2011, 2014; De Sanctis et al., 2012).

The application of passive BCI during autonomous driving however provides an exemplary use case for technology that adapts to the (neuronal) state of its operator during automation

in general. Such Neuroadaptive Technology is a clear additional step toward closing the cybernetic loop (Pope et al., 1995).

## ETHICS STATEMENT

The study involved standard EEG procedures covered in an ethic statement approved by the ethics committee of the Institute of Psychology and Ergonomics of the Berlin Institute of Technology. All participants gave written consent to their participation in the conducted study. They were provided with information on the purpose of the study, given the opportunity to ask questions and were informed that their participation was voluntary and they could end the experiment whenever they liked without a need to provide reasons. Participants also gave their consent for data recording, anonymous storage of that data, as well as its usage for publication.

## AUTHOR CONTRIBUTIONS

All authors contributed substentially to the work presented here. Everybody was contributing to the drafting and revising

of the documents and approved the ﬁnal version. Everybody agreed to be accountable for the integrity and accuracy of the work. Speciﬁcally: TZ designed and supervised the experimental procedures, conducted and supervised the analyzes, interpreted the results for the context of autonomous driving. LK and KG were responsible for quality of writing and validation of results. Everybody below was involved in conducting the experiments and ensured data quality. LA was responsible for the statistical analyzes and integrity of the manuscript. JP and MB were responsible for the electrode localization and the related mathematical procedures. LZ: Was responsible for the programming and EEG and BCI analyzes. AB: Was responsible for evaluation of the questionnaires.

## ACKNOWLEDGMENTS

We thank Brain Products GmbH (Munich, Germany) for providing us with the tested EEG System which made this research possible. We are also indebted to Prof. Dr.-Ing. Matthias Roetting and Mario Lasch, Chair for Human-Machinse Systems, TU Berlin for providing the research car and supporting us in all technical questions regarding the car.

## REFERENCES

Beiker, S. A. (2012). Symposium, Legal Aspects of Autonomous Driving, 52. Santa Clara, CA, 1145.

Berka, C., Levendowski, D. J., Lumicao, M. N., Yau, A., Davis, G., Zivkovic, V. T., et al. (2007). EEG correlates of task engagement and mental workload in vigilance, learning, and memory tasks. Aviat. Space Environ. Med. 78(Suppl. 1), B231–B244.

Blankertz, B., Lemm, S., Treder, M., Haufe, S., and Müller, K. R. (2011). Singletrial analysis and classiﬁcation of ERP components—a tutorial. Neuroimage 56, 814–825. doi: 10.1016/j.neuroimage.2010.06.048

Blankertz, B., Tangermann, M., Vidaurre, C., Fazli, S., Sannelli, C., Haufe, S., et al. (2010). The berlin brain–computer interface: non-medical uses of BCI technology. Front. Neurosci. 4:198. doi: 10.3389/fnins.2010. 00198

Borghini, G., Astolﬁ, L., Vecchiato, G., Mattia, D., and Babiloni, F. (2014). Measuring neurophysiological signals in aircraft pilots and car drivers for the assessment of mental workload, fatigue and drowsiness. Neurosci. Biobehav. Rev. 44, 58–75. doi: 10.1016/j.neubiorev.2012.10.00

Brooke, J. (1986). SUS: A “Quick and Dirty” Usability Scale. Usability Evaluation in Industry. London: Taylor and Francis

Delorme, A., Kothe, C., Vankov, A., Bigdely-Shamlo, N., Oostenveld, R., Zander, T. O., et al. (2010). “MATLAB-based tools for BCI research,” in Brain-Computer Interfaces (London: Springer), 241–259.

Delorme, A., and Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. J. Neurosci. Methods 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

De Sanctis, P., Butler, J. S., Green, J. M., Snyder, A. C., and Foxe, J. J. (2012). “Mobile brain/body imaging (MoBI): high-density electrical mapping of inhibitory processes during walking,” in 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (San Diego, CA: IEEE), 1542–1545.

Dickmanns, E. D., and Zapp, A. (1987). “A curvature-based scheme for improving road vehicle guidance by computer vision,” in Cambridge Symposium_Intelligent Robotics Systems (International Society for Optics and Photonics), 161–168.

Duncan-Johnson, C. C., and Donchin, E. (1977). On quantifying surprise: the variation of event-related potentials with subjective probability. Psychophysiology 14, 456–467. doi: 10.1111/j.1469-8986.1977.tb01312.x

Duvinage, M., Castermans, T., Petieau, M., Seetharaman, K., Hoellinger, T., Cheron, G., et al. (2012). “A subjective assessment of a P300 BCI system for lower-limb rehabilitation purposes,” in Engineering in Medicine and Biology Society (EMBC), Proceedings of the 2012 Annual International Conference of the IEEE, (San Diego, CA: IEEE), 3845–3849.

Fabrizio, M., and Cimolino, U. (2014). Persönliche Schutzausrüstung. Düsseldorf: Hüthig Jehle Rehm. Franke, U., Gavrila, D., Gorzig, S., Lindner, F.,Paetzold, F., and Wohler, C. (1998). Autonomous driving approaches downtown. IEEE Intell. Syst. 13, 40–48.

Gerjets, P., Walter, C., Rosenstiel, W., Bogdan, M., and Zander, T. O. (2014). Cognitive state monitoring and the design of adaptive instruction in digital environments: lessons learned from cognitive workload assessment using a passive brain-computer interface approach. Front. Neurosci. 8:385. doi: 10.3389/fnins.2014.00385

Gramann, K., Ferris, D. P., Gwin, J., and Makeig, S. (2014). Imaging natural cognition in action. Int. J. Psychophysiol. 91, 22–29. doi: 10.1016/j.ijpsycho.2013.09.003

Gramann, K., Gwin, J. T., Ferris, D. P., Oie, K., Jung, T. P., Lin, C. T., et al. (2011). Cognition in action: imaging brain/body dynamics in mobile humans. Rev. Neurosci. 22, 593–608. doi: 10.1515/RNS.2011.047

Iversen, J. R., and Makeig, S. (2013). “MEG/EEG Data Analysis Using EEGLAB,” in Magnetoencephalography: From Signals to Dynamic Cortical Networks. eds Selma S. and Cheryl, J. A (Berlin; Heidelberg: Springer Verlag), 199–212.

Käthner, I., Ruf, C. A., Pasqualotto, E., Braun, C., Birbaumer, N., and Halder, S.

(2013). A portable auditory P300 brain–computer interface with directional cues.Clin. Neurophysiol. 124, 327–338. doi: 10.1016/j.clinph.2012.08.006

Kothe, C. A., and Makeig, S. (2013). BCILAB: a platform for brain–computer interface development. J. Neural Eng. 10:056014. doi: 10.1088/1741-2560/10/5/056014

Liao, L. D., Lin, C. T., McDowell, K., Wickenden, A. E., Gramann, K., Jung, T. P., et al. (2012). “Biosensor technologies for augmented brain–computer interfaces in the next decades,” in Proceedings of the IEEE, 100(Special Centennial Issue), 1553–1566.

Linden, D. E. (2005). The P300: where in the brain is it produced and what does it tell us?. Neuroscientist 11, 563–576. doi: 10.1177/1073858405280524

Llaneras, R. E., Salinger, J., and Green, C. A. (2013). “Human factors issues associated with limited ability autonomous driving systems: drivers’ allocation of visual attention to the forward roadway,” in Proceedings of the 7th

International Driving Symposium on Human Factors in Driver Assessment, Training and Vehicle Design (Bolton Landing: NY), 92–98.

Ma, R., and Kaber, D. B. (2005). Situation awareness and workload in driving while using adaptive cruise control and a cell phone. Int. J. Ind. Ergon. 35, 939–953. doi: 10.1016/j.ergon.2005.04.002

Nam, C. S., Johnson, S., and Li, Y. (2008). “Environmental Noise and P300Based Brain-Computer Interface (BCI),” in Proceedings of the Human Factors and Ergonomics Society Annual Meeting (Sage, CA; Los Angeles, CA: SAGE Publications), 803–807.

Pasqualotto, E., Federici, S., Simonetta, A., and Olivetti Belardinelli, M. (2011). “Usability of brain computer interfaces,” in 11th European Conference for the Advancement of Assistive Technology: AAATE (Maastricht).

Polich, J., and Kok, A. (1995). Cognitive and biological determinants of P300: an integrative review. Biol. Psychol. 41, 103–146. doi: 10.1016/0301-0511(95)05130-9

Pomerleau, D. (1992). Neural Network Perception for Mobile Robot Guidance. PhD thesis, Carnegie Mellon University.

Pope, A. T., Bogart, E. H., and Bartolome, D. S. (1995). Biocybernetic system evaluates indices of operator engagement in automated task. Biol. Psychol. 40, 187–195. doi: 10.1016/0301-0511(95)05116-3

Sauseng, P., Klimesch, W., Stadler, W., Schabus, M., Doppelmayr, M., Hanslmayr, S., et al. (2005). A shift of visual spatial attention is selectively associated with human EEG alpha activity. Eur. J. Neurosci. 22, 2917–2926. doi: 10.1111/j.1460-9568.2005.04482.x

Schuirmann, D. J. (1981). On hypothesis testing to determine if the mean of a normal distribution is contained in a known interval. Biometrics 37:617.

Schuirmann, D. J. (1987). A comparison of the two one-sided tests procedure and the power approach for assessing the equivalent of average bioavailability. J. Pharmacokinet. Biopharm. 15, 657–680. doi: 10.1007/BF01 068419

Solis-Escalante, T., Müller-Putz, G., Brunner, C., Kaiser, V., and Pfurtscheller, G. (2010). Analysis of sensorimotor rhythms for the implementation of a brain switch for healthy subjects. Biomed. Signal Process. Control 5, 15–20 doi: 10.1016/j.bspc.2009.09.002

Sukthankar, R., Baluja, S., and Hancock, J. (1997). “Evolving an Intelligent Vehicle for Tactical Reasoning in Traﬃc,” in Proc. IEEE Int. Conf. on Robotics and Automation. (New York, NY: IEEE ), 519–524.

Tadaka, Y., and Shimoyama, O. (2004). “Evaluation of driving-assistance systems based on drivers’ workload,” in Proceeding of the International Driving Symposium on Humand Factors in Driver Assessment, Training and Vehicle Design.

Webb, A. R. (2002). Statistical Pattern Recognition. Chichester: John Wiley and Sons Ltd. Westlake, W. J. (1981). Response to T.B.L. Kirkwood: bioequivalence testing – a need to rethink. Biometrics 37, 589–594. Young, M. S., and Stanton, N. A. (1997). Automotive automation: Investigating the impact on drivers mental workload. Int. J. Cogn. Ergon. 1, 325–336.

Zander, T. O., and Jatzev, S. (2012). Context-aware brain–computer interfaces: exploring the information space of user, technical system and environment. J. Neural Eng. 9:016003. doi: 10.1088/1741-2560/9/1/016003

Zander, T. O., and Kothe, C. (2011). Towards passive brain–computer interfaces: applying brain computer interface technology to human–machine systems in general. J. Neural Eng. 8:025005. doi: 10.1088/1741-2560/8/2/025005

Zander, T. O., Lehne, M., Ihme, K., Jatzev, S., Correia, J., Kothe, C., et al. (2011). A dry EEG-system for scientiﬁc research and brain–computer interfaces. Front. Neurosci. 5:53. doi: 10.3389/fnins.2011.00053

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2017 Zander, Andreessen, Berg, Bleuel, Pawlitzki, Zawallich, Krol and Gramann. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

