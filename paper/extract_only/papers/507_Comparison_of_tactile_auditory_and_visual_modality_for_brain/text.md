#### ORIGINAL RESEARCH ARTICLE

published: 24 July 2013 doi: 10.3389/fnins.2013.00129

# Comparison of tactile, auditory, and visual modality for brain-computer interface use: a case study with a patient in the locked-in state

## Tobias Kaufmann*, Elisa M. Holz and Andrea Kübler

Department for Psychology I, Institute for Psychology, University of Würzburg, Würzburg, Germany

Edited by: Emanuel Donchin, University of South Florida, USA

Reviewed by: Eric W. Sellers, East Tennessee State University, USA Yael Arbel, University of South Florida, USA Dean Krusienski, Old Dominion University, USA

*Correspondence: Tobias Kaufmann, Department for Psychology I, Institute for Psychology, University of Würzburg, Marcusstr. 9-11, 97070 Würzburg, Germany e-mail: tobias.kaufmann@ uni-wuerzburg.de

This paper describes a case study with a patient in the classic locked-in state, who currently has no means of independent communication. Following a user-centered approach, we investigated event-related potentials (ERP) elicited in different modalities for use in brain-computer interface (BCI) systems. Such systems could provide her with an alternative communication channel. To investigate the most viable modality for achieving BCI based communication, classic oddball paradigms (1 rare and 1 frequent stimulus, ratio 1:5) in the visual, auditory and tactile modality were conducted (2 runs per modality). Classiﬁers were built on one run and tested ofﬂine on another run (and vice versa). In these paradigms, the tactile modality was clearly superior to other modalities, displaying high ofﬂine accuracy even when classiﬁcation was performed on single trials only. Consequently, we tested the tactile paradigm online and the patient successfully selected targets without any error. Furthermore, we investigated use of the visual or tactile modality for different BCI systems with more than two selection options. In the visual modality, several BCI paradigms were tested ofﬂine. Neither matrix-based nor so-called gaze-independent paradigms constituted a means of control. These results may thus question the gaze-independence of current gaze-independent approaches to BCI. A tactile four-choice BCI resulted in high ofﬂine classiﬁcation accuracies. Yet, online use raised various issues. Although performance was clearly above chance, practical daily life use appeared unlikely when compared to other communication approaches (e.g., partner scanning). Our results emphasize the need for user-centered design in BCI development including identiﬁcation of the best stimulus modality for a particular user. Finally, the paper discusses feasibility of EEG-based BCI systems for patients in classic locked-in state and compares BCI to other AT solutions that we also tested during the study.

Keywords: brain-computer interface, tactile auditory and visual modality, locked-in syndrome, user-centered design, end-user testing, assistive technology

## INTRODUCTION

Damages to neuromuscular pathways, e.g., due to a stroke in the brainstem, or neurodegenerative diseases such as amyotrophic lateral sclerosis (ALS) or spinal muscular atrophy (SMA) can entail a severe loss of voluntary muscular control. These patients are summarized under the term locked-in syndrome (LIS; Plum and Posner, 1966) as they are locked into their own body despite often intact cognitive functioning. Patients in classic LIS are in total paralysis except for retaining control of vertical eye movements (Bauer et al., 1979). Consequently, communication is severely restricted for patients in this state. They usually rely on communication partners and utilize remaining eye muscle control (blinking or moving eye-brows) to answer questions in the closed format (yes/no) or to select suggested options.

Brain-computer interfaces (BCIs) were proposed as an alternative communication channel bypassing the requirement for

retaining muscular control (for review, e.g., Kübler et al., 2001; Birbaumer and Cohen, 2007; Birbaumer et al., 2008; Allison et al., 2012; Wolpaw and Wolpaw, 2012). BCIs based on classiﬁcation of event-related potentials (ERP) in the electroencephalogram (EEG) of a patient are most frequently used for communication purpose (Farwell and Donchin, 1988; for review, e.g., Kleih et al., 2011; Mak et al., 2011; Sellers et al., 2012). Several options (e.g., characters for typing words) are iteratively presented and users focus their attention on presentation of the one option they intend to select. Such target stimuli will elicit more pronounced ERPs than all other, irrelevant non-target stimuli. The procedure is thus referred to as oddball paradigm, as the target stimulus is rare compared to the frequent occurrence of irrelevant, non-target stimuli. ERP–BCIs usually rely highly on the P300 component (Sutton et al., 1965), a positive potential deﬂection occurring in the period of 200–500 ms post-stimulus (for review, Polich, 2007). Importantly, the P300 can be elicited in

different modalities, i.e., visually, auditory or tactually. Thus, ERP–BCIs relying on any of the three modalities have been introduced (visual, Farwell and Donchin, 1988; auditory, Hill et al., 2005; Sellers and Donchin, 2006; tactile, Aloise et al., 2007; Brouwer and Van Erp, 2010; for review, Riccio et al., 2012).

Visual ERP–BCIs present characters for typing (or other selection options) on a screen. Usually, they are arranged in a matrix so that groups of characters can be stimulated at once, e.g., row/column wise (Farwell and Donchin, 1988; for review, e.g., Sellers et al., 2012). Stimulation can be performed by highlighting characters (i.e., light-ﬂashing; Farwell and Donchin, 1988) or, as recently proposed, by overlaying them with faces (e.g., Kaufmann et al., 2011, 2013a; Zhang et al., 2012; Jin et al., 2012). However, matrix based ERP–BCIs may require accurate gaze control, therefore limiting its feasibility for people with LIS (Brunner et al., 2010; Treder andBlankertz, 2010). Thus, so-called gaze-independent paradigms have been suggested that present characters in the center of the screen (e.g., Acqualagnaet al., 2010; Treder and Blankertz, 2010; Liu et al., 2011; Aloise et al., 2012; Acqualagna and Blankertz, 2013).

Auditory ERP–BCIs present sound stimuli that may differ in terms of volume, pitch, direction or combinations of those (e.g., Hill et al., 2005; Halder et al., 2010; Höhne et al., 2010, 2011; Schreuder et al., 2010, 2011a, 2013; Käthner et al., 2013) or differ with regard to informational content (e.g., Sellers and Donchin, 2006; Furdea et al., 2009; Klobassa et al., 2009; Kübler et al., 2009). Furthermore, stimuli may be presented sequentially or as a continuous stream (e.g., Hill and Schölkopf, 2012).

Tactile ERP–BCIs utilize stimulation units (further referred to as tactors; e.g., vibration motors or piezo elements) placed at different body locations, e.g., on hands, around the waist or on the back of participants (e.g., Aloise et al., 2007; Brouwer and Van Erp, 2010; Brouwer et al., 2010; Thurlings et al., 2012; van der Waal et al., 2012; Kaufmann et al., 2013b). Users focus their attention on tactile stimulation of one location they intend to select (target stimulus) and ignore stimuli on all other locations.

Aloise et al. (2007) compared the modalities in terms of achieved classiﬁcation accuracies of eight participants. Results yielded strong superiority of the visual modality in terms of higher ERP amplitudes and lower latencies, thus enhancing classiﬁcation accuracy. Consequently, all participants achieved best accuracy with visual stimulation, except for one participant who achieved equal performance in tactile and visual modality. However, this study faces the limitation that all participants were healthy. As described above, patients in classic LIS have impaired vision and thus results may differ.

Herein we report a case study with a locked-in patient for who we aimed at developing a BCI for communication. To our knowledge, this is the ﬁrst report on tactile ERP classiﬁcation in a patient with classic LIS. We compared ERPs evoked in all three modalities, investigated reliability of classiﬁcation and further explored issues involved in the use of visual paradigms. Finally, we emphasize the requirement for user-centered design in BCI development and discuss limitations of current EEG-based BCI systems compared to other assistive technology (AT).

## MATERIALS AND METHODS

### THE CASE

We visited a 46-year-old Italian woman twice for intensive testing on 7 days in total (ﬁrst visit: 4 days; second visit: 3 days; with morning and afternoon testing sessions on most days). She had a brainstem stroke in the pons 7 years ago and since then has been in the classic locked-in state (for deﬁnition: Bauer et al., 1979). As conﬁrmed by computed tomography (CT), the lesion barely affected her cortical abilities and she was fully attentive during all testing sessions. During the last year, she has been regaining some (still unreliable) control of her right thumb. Still reliable communication is only possible with vertical eye movements (partner scanning). As she cannot well accommodate, her left eye was partially sutured to avoid double vision. With her right eye ﬁxation was possible, but never for more than few seconds and thus, she had to re-focus constantly.

She currently has no means of independent communication, i.e., communication is only possible in a partner scanning approach. Her dialog partner suggests letters or statements in the closed format that she can either select/agree with (eyelift) or not select/disagree (looking down). To enhance communication speed the patient utilizes an interval approach, i.e., characters were sorted according to their importance in Italian daily language and grouped into four categories (Figure 1A). First, the dialog partner reads out the categories (“ﬁrst, second, third, fourth”) and she selects one category. Next, the letters of the selected category are read out and again she makes a choice (“A, E, I, O, U” for the ﬁrst category; “B, C, D, F, G” for the second; “H, L, M, N, P” for the third and “Q, R, S, T, V, Z” for the fourth category).

The patient rated her quality of life as indexed by the ACSA [Anamnestic Comparative Self-Assessment Scale for Measuring the Subjective Quality of Life; scale from -5 (worst time in life) to 5 (best time in life); Bernheim and Buyse, 1993] as the worst time in her life (ACSA = −5). Asked for the reason, she

|[Figure 1]<br><br>FIGURE 1 | (A) Spelling system used by the patient in a partner scanning approach. Characters are grouped into four categories to increase spelling speed. (B) We developed a BCI system based on the partner scanning approach described in (A). Four tactile stimulation units were placed on the patient’s left arm. We individually adjusted the BCI paradigm to the partner scanning approach the patient is used to. Each tactor either represented one of the groups of characters, or represented a character of one prior selected group. Please note that we restricted the number of tactors to four, thus limiting the possible selections. Practical use of the system would require seven tactors (up to six tactors for selection of characters plus one tactor to undo a wrong selection).|
|---|

answered “Desperate because I depend on others and I do not see a solution.” For 1 week prior to our ﬁrst visit, caregivers daily assessed her mood and health as well as satisfaction with communication and nursing using questionnaires (linear scales from 0 [extremely bad] to 10 [excellent]). She rated mood low to medium (M = 5.0, range 3–6) and health as slightly above medium (M = 5.6, range 5–7). She had a cold prior to our ﬁrst visit with ﬁts of coughing leading to spasms. She was satisﬁed with nursing (M = 7.2, range 7–8) but displayed greater variance with regard to satisfaction with communication (M = 5.8, range 2–7). During our ﬁrst stay, she reported one incidence where she had physical pain but was not able to call attention due to the absence of a communication partner. Establishing an independent communication ability is thus of utmost importance for her.

Prior to all testing sessions, we verbally informed the patient in detail about the procedure and obtained her consent to participate in the study through partner scanning. As no means of independent communication was possible, we asked her prior to every run if she agreed to proceed. The experiment was conducted in accordance with standard ethical guidelines as deﬁned by the Declaration of Helsinki (World Medical Association) and the European Council’s Convention for the Protection of Human Rights and Dignity of the Human Being with regard to the Application of Biology and Medicine (Convention on Human Rights and Biomedicine).

We approached the intended development of a BCI-based communication channel from a user-centered perspective targeting an individually tailored BCI solution for the patient. (1) We presented her with several classic oddball paradigms in three different modalities to identify the most promising modality for BCI use. (2) We tested different settings of BCI paradigms to explore emerging issues related to, e.g., system timing, gaze requirement, modality. Apart from BCI paradigms, we also tested other AT.

### EXPERIMENTAL DESIGN

Figure 2 illustrates the various different paradigms that were tested during the visits.

Classic oddball paradigms

All tested oddball paradigms shared the same parameters except for the modality and stimulus duration (SD) (Figure 3). Two

stimuli were presented with an inter-SD of 1000ms and a rare to frequent ratio of 1:5. One run comprised 90 rare and 450 frequent stimuli. We conducted two runs per modality.

Ofﬂine classiﬁcation. To investigate reliability of each modality, we build weights of a stepwise linear discriminant analysis (SWLDA; e.g., Donchin, 1969; Farwell and Donchin, 1988; Krusienski et al., 2006) based on one of two runs and tested the classiﬁer on the other run (and vice versa). We used 1000ms of data post-stimulus for classiﬁcation. In ERP–BCIs, higher reliability is usually achieved by considering several trials for classiﬁcation. To align with this setting we grouped trials into several blocks for ofﬂine classiﬁcation. This led to classiﬁcation based on 15 trials, based on 5 trials, 3 trials, 2 trials and ﬁnally to classiﬁcation of single trials respectively.

Online classiﬁcation. Apart from the above described ofﬂine classiﬁcation we conducted one run with online classiﬁcation in the tactile modality. A classiﬁer was built from the two classic tactile oddball runs. The task was to select the target stimulus four times and online classiﬁcation was performed each time after 20 rare and 100 frequent stimuli. Feedback was immediately presented to the patient in that we verbally communicated classiﬁcation outcome.

Visual oddball. A red square of size 100 × 100 pixels was displayed frequently in the center of a screen with black background.

|[Figure 2]<br><br>FIGURE 3 | Classic oddball paradigms in three modalities. Stimuli where Einstein face vs. red square displayed in the center of a black screen (visual; the ﬁgure exemplarily displays another face due to printing license), high vs. low pitched tone (auditory) and tactile stimulation at one position vs. stimulation on a second position (tactile). Rare stimuli to frequent stimuli ratio was 1:5.|
|---|

|[Figure 3]<br><br>FIGURE 2 | Illustration of paradigms and systems tested during the visits.|
|---|

The odd stimuli were of same size and displayed the famous picture of Albert Einstein presenting his tongue. We modiﬁed the picture in that it only displayed the face on a black background. SD was 64.25ms.

Auditory oddball. Stimuli were presented with headphones to both ears with same volume for all stimuli. SD was 400ms. Odd stimuli comprised a high-pitched tone whereas irrelevant stimuli comprised a low-pitched tone.

Tactile oddball. Target and non-target stimuli did not vary in terms of SD (220ms), vibration frequency or vibration gain, but only with respect to the location. The task was to focus attention on one location while ignoring stimuli on the other. To account for sensitivity differences on two forearm locations, we switched target and non-target location between the two runs. As such, we made sure that elicited ERPs following rare stimuli are not due to decreased sensory perception capabilities on the location of frequent stimuli.

Visual BCI

The patient reported to see the entire screen placed approximately 80–90cm distant to her. We pointed to different locations in a visually displayed character matrix, in particular to the corners, and asked if she could see these locations (closed question by means of partner scanning; “Can you see the character displayed at this location?”). The tested visual matrices were of different size (large matrix grid on full screen; smaller matrix grid in the center of the screen), contents (6 × 6 matrix; 4 × 4 matrix) and timing [short, medium and long inter-stimulus interval (ISI)]. We adjusted the latter settings based on the patient’s report after each testing run. Stimuli in all matrix paradigms comprised the famous face of Albert Einstein as introduced earlier (Kaufmann et al., 2011, 2013a), i.e., the famous face overlaid characters (face ﬂash) and the patient counted the number of face ﬂashes on top of the intended character. We explicitly told the patient to focus attention continuously on face ﬂashes on top of the target character even if she was not able to keep her gaze focused on the target.

Apart from matrix paradigms, we tested a so-called gazeindependent paradigm in which characters were presented consecutively in the center of the screen. We used only six characters (A–F) to align with the properties of the visual oddball paradigm. The target character was the “D.” Furthermore, we tested one setting, to bridge between the oddball paradigm and the gazeindependent speller. Instead of the “D,” it displayed the Einstein face as for the visual oddball paradigm. Yet, in contrast to the visual oddball, frequent stimuli comprised characters instead of the red square (thus referred to as “leading to” gaze-independent speller).

Tactile BCI

We checked sensory sensitivity of the patient’s left forearm and upper arm by stimulating different locations and inquiring her perception capabilities (two closed questions by means of partner scanning; “Do you feel the stimulus?”; “Do you feel the stimuli approximately equally well?”). Four tactors (see section

Equipment, Data Acquisition and Analysis)were then placed with around 10–15cm distance on her left forearm and upper arm (see Figure 1B).

We investigated different timing parameters in several sessions to deﬁne the setting in which discrimination of four tactors would work best for the patient. Each setting comprised ﬁve runs, each run with every tactor being the target once. (1) SD was long (520 ms) and ISI was short (200ms). Each tactor was stimulated 15 times per selection, resulting in 60 target and 180 non-target stimuli per run. (2) SD was long (520ms) and ISI was medium (520 ms) with again every tactor being stimulated 15 times per target. (3) SD was short (220ms) and ISI was long (800ms). We increased the number of stimulations by factor 2 to gather more data, resulting in 120 target and 360 nontarget stimuli. For direct comparison of the ﬁrst and the second setting, we reduced the number of stimulations in the ofﬂine analysis.

For comparison of these settings, we trained SWLDA classiﬁers on every combination of four of ﬁve runs and tested classiﬁcation outcome on the remaining run (see ﬁrst three columns of Table 1 for illustration of all combinations). Furthermore, we assessed classiﬁcation outcome for classiﬁer weights trained on 800ms of data, 1000ms, 1200ms, and1400 ms respectively.

Finally, we conducted one run, in which the patient used the tactile BCI for communication. We implemented a BCI spelling system analog to her partner scanning approach (see Figure 1). First, one of four groups of characters was selected, followed by selection of an individual character. As our setup and calibration was restricted to a four-choice paradigm, we only enabled selection of the ﬁrst four characters in each group for this online test (colored characters in Figure 1). The patient tested this system in one run aiming at copy spelling a four-letter word (8 selections, i.e., four times selection of group plus four times selection of character). SD was the same as ISI duration, both 520ms long.

Other assistive technology

In this study, we investigated feasibility of a BCI system as a communication channel alternative to the partner scanning that she currently uses. Yet, during the visits, we also attempted to provide her with other AT as no reliable communication method other than partner scanning has ever been established within the past 7 years. During our ﬁrst visit we tried two commercial AT devices, (1) an infrared blink detection sensor (SCATIR, Prentke Romich GmbH) and (2) a button (Lib Switch, Prentke Romich GmbH) on her thumb. We connected it to a communication device that allows for selecting characters or commands (XLTalker, Prentke Romich GmbH). During our second visit, we investigated use of an electrooculogram (EOG) for detection of eyelifts. We connected one EOG electrode placed below her right eye to our BCI software and classiﬁed eyelifts using SWLDA. The software read out characters in the same manner as the above-described partner scanning approach the patient is used to (see also section Tactile BCI and Figure 1A). When the software read out the intended group or the intended character respectively, the patient lifted her eyebrow

Table 1 | Classiﬁcation accuracy based on different runs of tactile BCI use.

Data set Classiﬁer trained Classiﬁer tested 800ms 1000 ms 1200 ms 1400 ms on runs # on run # post-stimulus post-stimulus post-stimulus post-stimulus

Long stimulus, short ISI [1 2 3 4] [5] 50 75 75 75

- [1 2 3 5] [4] 25 25 75 100
- [1 2 4 5] [3] 50 75 100 75

- [1 3 4 5] [2] 100 100 100 100
- [2 3 4 5] [1] 50 100 100 100 Mean ± STD 55.5 ± 27.4 75.0 ± 30.6 90.0 ± 13.7 90.0 ± 13.7

Long stimulus, medium ISI [1 2 3 4] [5] 75 100 100 100

- [1 2 3 5] [4] 75 50 100 100
- [1 2 4 5] [3] 50 50 75 50

- [1 3 4 5] [2] 0 0 50 25
- [2 3 4 5] [1] 50 50 75 50 Mean ± STD 50 ± 30.6 50 ± 35.4 80 ± 20.9 65 ± 33.5

- [1 2 3 4] [5] 75 75 50 75
- [1 2 3 5] [4] 75 50 75 100

Short stimulus, long ISI. Number of stimulations reduced ofﬂine for direct comparison

- [1 2 4 5] [3] 75 75 75 75
- [1 3 4 5] [2] 25 75 50 0 [2 3 4 5] [1] 75 75 75 75 Mean ± STD 65 ± 22.4 70 ± 11.2 65 ± 13.4 65 ± 37.9

- [1 2 3 4] [5] 100 75 100 100
- [1 2 3 5] [4] 75 75 75 100

Short stimulus, long ISI. Full data set with twice as much stimuli.

- [1 2 4 5] [3] 75 75 75 75
- [1 3 4 5] [2] 75 75 75 100 [2 3 4 5] [1] 75 75 50 50 Mean ± STD 80.0 ± 11.2 75.0 ± 0.0 75.0 ± 17.7 85.0 ± 22.4

We trained SWLDA classiﬁers on every combination of four of ﬁve runs and tested them on the remaining run. The table furthermore presents classiﬁcation outcome for classiﬁer weights trained on 800ms of data, 1000ms, 1200ms, and 1400ms respectively.

thereby triggering a reliable deﬂection in the recorded muscle activity.

performed utilizing SWLDA (e.g., Donchin, 1969; Farwell and Donchin, 1988; Krusienski et al., 2006).

### EQUIPMENT, DATA ACQUISITION, AND ANALYSIS

Visual stimulation was performed on a 22 screen (LG Flatron; 1680 × 1050 pixels), auditory stimulation through headphones fully covering both ears (Sennheiser, HD280 pro) and tactile stimulation with small vibrate transducers (C2 tactors; Engineering Acoustics Inc., USA). We implemented the stimulation paradigms for all modalities in Python 2.7 (www.python.org) and connected them to the BCI2000 software (Schalk et al., 2004; www.bci2000. org) via user datagram protocol.

EEG during oddball-paradigms was obtained from 11 passive Ag/AgCl electrodes with mastoid ground and reference placed at positions Fz, FC1, FC2, C3, Cz, C4, PO7, P3, Pz, P4 and PO8. For testing BCI paradigms, we extended the electrode setup by four electrodes (TP7, CP3, CP4 and TP8) to a 15 electrodes setting. EEG was ampliﬁed with a g.USBamp ampliﬁer (g.Tec Medical GmbH, Austria) and recorded at 512 Hz using BCI2000. Data was analyzed in Matlab 2012 (The Mathworks Inc., USA) and classiﬁcation of oddball paradigms as well as all BCI paradigms

## RESULTS

### CLASSIC ODDBALL PARADIGMS

Figure 4 displays ERPs elicited in the oddball paradigms for two exemplary electrodes. Difference between rare and frequent stimuli was most pronounced for visual and tactile modalities displaying a distinct P300 around 500ms post-stimulus. Peak amplitudes were of same size for the visual (5.96 µV, 530ms, Pz) and the tactile modality (5.92 µV, 471ms, FC2) and higher than for the auditory modality (3.95µV, 493 ms, Fz).

To investigate the reliability of elicited ERPs ofﬂine, we trained classiﬁers for each modality based on one run and tested them on the other run (and vice versa). Figure 5 depicts average ofﬂine classiﬁcation accuracies. The tactile modality was clearly superior to the visual andauditory modality. Although classiﬁcationof visual and auditory ERPs was possible when including many trials into classiﬁcation (visual: M = 83.33%, auditory: M = 66.67% with 15 trials), performance severely decreased with reduced number of trials. This effect was more pronounced in the auditory

|[Figure 4]<br><br>FIGURE 4 | Comparison of ERPs elicited in different modalities in the classic oddball paradigms. ERPs are exemplarily displayed for electrode Cz (upper row) and Pz (lower row). Visual and tactile stimulation elicited<br><br>the most pronounced differences between target and non-target stimulations. Reliability across trials was highest for the tactile modality (see Figure 5).|
|---|

modality. Classiﬁcation accuracy based on few trials was insufﬁciently low (below M = 60% with 3 trials or less). In contrast, in the tactile modality ﬁve or more trials led to 100% classiﬁcation accuracy. Importantly, accuracy was still high if based on two trials (M = 92.85%) and even if based on single trial (M = 78.33%).

We conducted an online test session with the tactile oddball paradigm. The patient correctly selected the target in all cases, i.e., online classiﬁcation accuracy based on 10-trials of two tactile stimuli was 100%.

### TRANSFER TO BCI

As visual and tactile oddballs displayed pronounced ERPs poststimulus, we tested these modalities with BCI paradigms.

Visual BCI

Although the patient reported to perceive the entire screen (see section Experimental Design), matrix-based BCI paradigms were not viable. After initial testing with a 6 × 6 matrix, we reduced the number of matrix items to 4 × 4 and ﬁnally we reduced the size from full-screen to a small matrix in the center of the screen. Yet, none of these paradigms evoked pronounced and thus, reliably classiﬁable ERPs (Figures 6A–C). No N170 was visible as would have been expected if recognizing the face presented on the target character (Bentin et al., 1996; Eimer, 2000). The patient reported

difﬁculties in continuously focusing on a target, although possible for a short time.

As she had trouble with focusing her gaze on targets, we tested a so-called gaze-independent BCI paradigm, randomlypresenting six characters in the center of the screen. However, also this paradigm failed such that no reliable ERPs were elicited (Figure 6D). As the visual oddball elicited pronounced ERPs, we further investigated possible reasons for failure of the gazeindependent paradigm. In the visual oddball, the black and white Einstein face was easily distinguishable from the red squares. Thus, we combined the oddball with the gaze-independent speller such that ﬁve white characters were used as non-targets and the (black and white) Einstein face as target. As depicted in Figure 6E, the paradigm elicited pronounced ERPs including a strong N170. The P300 was even of higher amplitude compared to the visual oddball (7.78 µV, Fz), however, its latency was strongly increased (723ms), indicating increased difﬁculty to discriminate between target and non-target stimuli (Figure 4).

Tactile BCI

As the visual modality appeared unreliable, we further focused on the tactile modality. We extended the setup to a four-choice BCI paradigm and conducted 15 runs in total where each of four tactors was the target once per run. Figure 7 compares

|[Figure 5]<br><br>FIGURE 5 | Ofﬂine classiﬁcation accuracy achieved in different modalities in the classic oddball paradigms. Classiﬁcation accuracies are presented based on classiﬁcation of single trials, two, three, ﬁve, or ﬁfteen trials. Tactile modality outperformed other modalities in that high classiﬁcation accuracy could be achieved even based on single trials.|
|---|

the ERPs elicited in different settings (long SD + short ISI; long SD + medium ISI; short SD + long ISI). The condition with long SD and short ISI elicited most pronounced ERPs, followed by the condition with short SD and long ISI. Importantly, ERPs of all conditions could be classiﬁed ofﬂine with high accuracies (see Table 1). In general classiﬁcation on 1200 ms and 1400 ms post-stimulus achieved highest accuracy yet variance was lowest for classiﬁcation based on 1200 ms. All obtained classiﬁcation results were clearly above the chance level of 25%.

Finally, we tested a communication application online, utilizing the tactile four choice BCI described in section Tactile BCI. The patient completed one run with 50% online accuracy (four of eight selections correct).

### OTHER ASSISTIVE TECHNOLOGY

Communication by means of an infrared blink detection sensor failed due to the presence of involuntary muscle movements of her eyelids. Use of a simple button on her thumb appeared more promising. Although still unreliable, selections were clearly above chance.

The EOG based eye lift detection tested during our second visit appeared far most promising. After a short calibration of 8min only, the patient could use the EOG for reliable communication and spelled several words without error. Classiﬁcation was performed after every three trials of eye lifts. This system for the ﬁrst time provided a reliable and fast means of independent communication.

## DISCUSSION

This case study with a LIS patient revealed the potential of tactile stimulation for BCI use such that tactually evoked ERPs were clearly more reliable than those elicited in the visual or

auditory modality. Although an average across 180 target trials per modality led to similar ERP amplitudes for the tactile and the visual domain, visual ERPs were much less reliable. With single-trial ofﬂine classiﬁcation of tactile ERPs in the oddball paradigm, almost the same level of classiﬁcation accuracy was obtained (M = 78.33) as with 15 trials of classiﬁcation in the visual modality (M = 83.33). These promising ofﬂine results were replicated in an online run in which the patient correctly selected the target stimuli without any error (four times, each based on 20 rare and 100 frequent tactile ERP stimuli).

When extending the setting to four tactile stimulation units, ERPs of same amplitude were elicited. Classiﬁcation accuracies as depicted in Table 1 were up to 100% and for all settings clearly above chance level. Performance achieved in runs based on long SD and short ISI was higher than in other settings (M = 90%). ERPs depicted in Figure 7 render a short SD feasible for tactile ERP elicitation in our patient, yet classiﬁcation accuracy was not as high. The larger SD may have increased the patient’s stimulus perception ability. Brouwer and Van Erp (2010) reported signiﬁcantly decreased classiﬁcation accuracy for a condition with long SD (367 ms) and no ISI (0ms). Our results complement these ﬁndings in that the decreased performance may not be due to the increased SD but due to the missing ISI. The authors further reported, that for a condition with sufﬁciently long SD (188 cms), performance could be further increased by decreasing the ISI (SD: 188 ms, ISI: 188ms). This ﬁnding is in line with our results, where a shorter ISI entailed better accuracy than a longer ISI.

In the test of the tactile spelling system, the patient achieved an accuracy of 50% only. Although this result was above chance, it is insufﬁcient for communication (Kübler et al., 2001). Choice of 520ms SD and 520ms ISI might have been suboptimal when considering the results from the comprehensive ofﬂine analysis conducted afterwards (depicted in Table 1). Consequently, we expect higher accuracies for future tests, when applying a shorter ISI. Also, the patient had a strong cough during the last character selection process, explaining the last miss-selection. As noted by a family member, these coughs particularly appear when she is excited and endeavored (see also section General Implications with EEG-Based BCIs and Comparison to Other Assistive Technology). To use the proposed spelling system in full functionality, an extension from four to seven tactors would be required. Brouwer and Van Erp (2010) reported similar classiﬁcation accuracies when using two, four, or six tactors. Our results yielded decreased performance when extending the setup from two to four tactors. Although accuracies were still high, they were lower in the four-choice tactile BCI than expected from the classic oddball paradigm results. If an extension to seven tactors may be feasible for the patient remains to be investigated.

Notwithstanding these caveats, our results were a proof of concept for the feasibility of tactile stimulation for BCI control in a patient for who the visual modality did not work in any setting.

Apart from these promising results on tactually evoked ERPs, we reported on two other modalities. The auditory modality

|[Figure 6]<br><br>FIGURE 6 | Comparison of ERPs elicited in different visual BCI paradigms, exemplarily illustrated for electrode Cz (upper row) and Pz (lower row). (A) 6 × 6 matrix presented in fullscreen, (B) 4 × 4 matrix presented in fullscreen, (C) 4 × 4 matrix presented at smaller size in the center of the screen, (D) “Gaze independent” speller, characters were presented in the center of the screen (E) “Leading to” gaze independent speller, similar to the gaze independent speller except for the target stimulus that was replaced by a face stimulus. Neither matrix based paradigms (A-C),<br><br>nor a gaze-independent paradigm (D) led to reliable differences between target and non-target stimulations. To investigate potential sources why the gaze-independent paradigm did not work, we conducted one run in which the target character was replaced with a face (E). This paradigm is similar to the visual oddball and differed only with regard to the non-target stimuli. As this paradigm elicited pronounced ERPs that compared to the visual oddball, we assume that identiﬁcation of a character in a plethora of presented characters may be aggravated and sufﬁcient gaze control may be required.|
|---|

appears least promising in this patient. ERP amplitudes were lower as compared to other modalities and ofﬂine classiﬁcation accuracy rapidly decreased when reducing the number of trials. Here we used stimuli that varied in pitch as a study by Halder et al. (2010) reported such stimuli superior to those that varied in volume or direction. Yet other differentiations between rare and frequent stimuli may yield better results, e.g., combinations of pitch and spatial information (Schreuder et al., 2010; Höhne et al., 2011; Käthner et al., 2013). Recently, Halder et al. (2013) illustrated that training may positively affect auditory BCI performance. Furthermore, as for tactile BCIs, SD may strongly affect classiﬁcation outcome. No deﬁnite conclusion can thus be drawn for the auditory modality.

For the visual modality, we conducted many runs in different settings and were thus able to draw a more detailed picture than for the auditory modality. Matrix-based visual ERP–BCIs failed in all of the tested conﬁgurations. Although able to see

the entire screen, the patient had difﬁculties in focusing for a longer time on a peripheral location. However, it is notable that a so-called gaze-independent speller did not work either. Focusing attention on the target character seemed not sufﬁcient for correct selection. A possible explanation is that these paradigms in fact do require gaze control for discrimination between characters. To investigate this hypotheses we compared ERPs elicited in the visual oddball (Einstein face vs. red squares) to ERPs elicited in a paradigm with the black and white Einstein face as target and white characters as non-targets. This paradigm elicited a strong P300, yet the peak was delayed as compared to the visual oddball. This delay may be due to an increased difﬁculty in discriminating targets from non-targets. Consequently, we assume that enhancing discriminability between characters may entail better results in her case. Acqualagna et al. (2010) compared a condition in which characters were presented in different colors to a condition with black characters only. Participants

|[Figure 7]<br><br>FIGURE 7 | Comparison of ERPs elicited in a four-choice tactile BCI with different stimulus parameters. Stimulus duration (SD) was either long (520ms) or short (220ms). Inter-stimulus interval (ISI) was short (200ms), medium (520ms) or long (800ms). Three combinations of SD and ISI were<br><br>tested exploratory, i.e., (1) SDlong + ISIshort, (2) SDlong + ISImedium, and (3) SDshort + ISIlong. Please note that for the third combination, more data was available. For comparison, we thus reduced the amount of data to similar size for all conditions. Yet, the full data set is depicted in the plot on the right.|
|---|

achieved better counting accuracy when characters were of different color, yet ofﬂine classiﬁcation was lower compared to the black-character condition. In the follow-up online study classiﬁcation accuracy was the same for both conditions (Acqualagna and Blankertz, 2013). Thus, we would not expect a boost in performance from such modiﬁcation. Other “gaze-independent” spellers could be tested, e.g., a speller that groups characters into categories (Treder and Blankertz, 2010). However, from the classiﬁcation accuracy achieved in the visual oddball we would not expect reliable communication based on the visual modality.

Our results manifest the importance of user-centered design in BCI development (Maguire, 1998; Zickler et al., 2011; Holz

- et al., 2012). Based on data obtained from healthy participants, we expected the visual modality (gaze-independent) to be superior to the others (e.g., the direct comparison of modalities by Aloise et al., 2007; accuracies reported from studies conducted in different modalities, for review, Riccio et al., 2012). Clearly, this was not the case in our patient, which convincingly demonstrates that results achieved with healthy subjects do not necessarily transfer to locked-in patients. BCIs that yield lower results in healthy users may be the only possible setting for a particular end-user with

motor impairment or in the locked-in state. Thus, when aiming at bringing BCIs to end-users, those have to be included in the developmental process for which the user-centered design provides a framework (Maguire, 1998; Holz et al., 2012). Only when speciﬁcally investigating the requirements of a targeted end-user a well-suited BCI can be implemented as their needs and requirements may well differ from that of healthy users (Zickler et al., 2011). In addition, development of a BCI system that copies the communication approach a patient is used to may increase learnability of system control. The approach we implemented in this study (Figure 1) was similar to the patient’s approach, which she highly appreciated.

In our case study, the patient rated her perceived quality of life as “the worst time in life” (see section The Case) and explained her low rating as being due to the strong dependence on others. In a survey among 65 LIS patients, Bruno et al. (2011) reported that only 28% of patients perceived unhappiness (ACSA scores below 0) and only 1/3 of them rated quality of life with an ACSA score of -5. Yet unhappiness was associated with nonrecovery of speech production. These and our results manifest the importance of providing these patients with a means of independent communication.

GENERAL IMPLICATIONS WITH EEG-BASED BCIs AND COMPARISON TO OTHER ASSISTIVE TECHNOLOGY

Recent research demonstrated that independent BCI home-use by a locked-in patient is possible (Sellers et al., 2010; Holz

- et al., 2013) and that the software can be automatized such that naïve users can handle it (Kaufmann et al., 2012a). However, several issues remain, e.g., related to artifact contamination of EEG data or attention allocation capacity. Some of these issues may be:

- 1. Spasm artifacts: During our ﬁrst visit, the patient had several spasm attacks (due to cough, see section The Case) so that we had to cancel runs and start again. On the last day, the attacks were so intense, that the BCI session had to be terminated. Apart from health related attacks, the patient also had coughs due to an increased excitement and endeavor (as noted by a family member). Future research should thus investigate algorithms for identiﬁcation of artifacts from the ongoing EEG. A practical BCI should automatically pause in the case of too noisy EEG and proceed once artifact induced electrode drifts diminished. In addition, the EEG could be cleaned prior to computing classiﬁer weights to avoid building classiﬁers based on artifacts. Furthermore, classiﬁcation based on a dynamically adjusting number of trials may compensate small artifact contamination such that more trials can be presented if artifacts lower classiﬁcation certainty (e.g., Lenhardt et al., 2008; Höhne et al., 2010; Liu et al., 2010; Jin et al., 2011; Schreuder et al., 2011a; for review, Schreuder et al., 2011b, 2013).
- 2. Single electrode drifts and cap displacement: Apart from spasm artifacts, that usually contaminate all electrodes, single electrode drifts or shift of cap placement should automatically be identiﬁed. During our stay, the patient had a strong spasm attack after which the whole electrode cap had shifted. Furthermore, single electrodes sometimes lost contact or even dropped out after such attacks. Dauce andProix(2013) suggested a method for identiﬁcation of performance drops during free spelling. The backspace key is used as an indicator of low performance. If used too frequently, the BCI is recalibrated.
- 3. Attention allocation and workload: In a home environment, background noise is present in daily life situations, e.g., phone rings, voice of others, etc. ERP–BCIs (especially non-visual ERP–BCIs) require high attention to stimuli (e.g., Kaufmann et al., 2012b) and such noise may badly affect performance. This clearly is a limitation compared to other assistive technologies. For example, the EOG based device that we provided to the patient (see section The Case) requires far less attention allocation and may thus prove more useful for her in daily life even if both systems would display equivalent bit rates.
- 4. Flexibility: In the partner scanning approach that the patient currently uses, the communication partner can easily repeat a scan if selection of a character was unclear or can even suggest another more likely character instead. Not only may these selections be based on the spelled characters but also be based on contextual knowledge of the patient’s life. Furthermore, the partner will easily recognize if the patient was distracted.

Consequently, the partner scanning approach is particularly ﬂexible. First approaches to increase ﬂexibility of BCI systems are available (e.g., the above described dynamic stopping, for review Schreuder et al., 2013; text prediction, e.g., Ryan et al., 2011; Kaufmann et al., 2012a; or error correction procedures, e.g., Dauce and Proix, 2013), yet compared to the partner scanning these systems still lack ﬂexibility.

5. Evaluation: It is important to validate after each run if the patient could concentrate and if anything was disturbing or unclear. Although this is rather time consuming when considering that the patient can only communicate on a character-by-character basis in a partner scanning approach, it is a necessity. Otherwise, it is impossible to investigate if for example decreased performance results from a modiﬁcation of the system or from decreased attention or distraction (Zickler et al., 2011, in press; Holz et al., 2013, in press).

Although we consider BCIs of particular interest for the patient described in this paper, the patient will not use a current BCI system for communication. As described in section The Case we tested an EOG based system that was far more reliable. However, the system requires muscular control which can be too fatiguing in frequent use. A tactile ERP–BCI would be a muscleindependent alternative. Importantly, the patient reported tactile BCI use as not being tiring. Thus, although we identiﬁed multiple issues that prevent transfer of current BCI technology to her daily life, the method should still be further explored as an alternative communication channel. If future research identiﬁes solutions to the issues described above, BCIs may well be a feasible communication tool for patients in (classic) LIS - at least as a valuable alternative among other systems.

## CONCLUSION

This case study demonstrated successful classiﬁcation of tactually evoked ERPs in a patient with classic LIS. The tactile modality was clearly superior to the visual and auditory modality. The patient achieved high accuracy even with a small number of trials in a two-class oddball and medium to high accuracy in a fourchoice tactile BCI paradigm. Results from visual BCI paradigms may question gaze-independence of current gaze-independent spellers, as gaze-control may not only be required to focus peripheral targets but also for discrimination of characters presented in the center of the screen. Further, our results emphasize the need for user-centered design in BCI development and underline remaining issues when considering practical daily life use that are not as relevant with other assistive technologies.

## ACKNOWLEDGMENTS

This work is supported by the European ICT Programme Project FP7-224631. This paper only reﬂects the authors’ views and funding agencies are not liable for any use that may be made of the information contained herein. Open access publication was funded by the German Research Foundation (DFG) and the University of Würzburg in the funding programme Open Access Publishing.

## REFERENCES

Acqualagna, L., and Blankertz, B. (2013). Gaze-independent BCI-spelling using rapid serial visual presentation (RSVP). Clin. Neurophysiol. 124, 901–908. doi: 10.1016/j.clinph.2012.12.050

Acqualagna, L., Treder, M. S., Schreuder, M., and Blankertz, B. (2010). A novel brain-computer interface based on the rapid serial visual presentation paradigm. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2010, 2686–2689. doi: 10.1109/IEMBS.2010.5626548

Allison, B. Z., Dunne, S., Leeb, R., Millán, J. D. R., and Nijholt, A. (2012). “Towards practical braincomputer interfaces: bridging the gap from research to realworld applications,” in Springer, Biological and Medical Physics, Biomedical Engineering. doi: 10.1007/978-3-642-29746-5

Aloise, F., Aricò, P., Schettini, F., Riccio, A., Salinari, S., Mattia, D., et al. (2012). A covert attention P300based brain-computer interface: geospell. Ergonomics 55, 538–551. doi: 10.1080/00140139.2012.661084

Aloise, F., Lasorsa, I., Brouwer, A. M., Mattia, D., Babiloni, F., Salinari, S., et al. (2007). Multimodal stimulation for a P300-based BCI. Int. J. Bioelectromagn. 9, 128–130.

Bauer, G., Gerstenbrand, F., and Rumpl, E. (1979). Varieties of the locked-in syndrome. J. Neurol. 221, 77–91. doi: 10.1007/BF00313105 Bentin, S., Allison, T., Puce, A., Perez, E., and McCarthy, G. (1996). Electrophysiological studies of face perception in humans. J. Cogn. Neurosci. 8, 551–565. doi: 10.1162/jocn.1996.8.6.551

Bernheim, J. L., and Buyse, M. (1993). The anamnestic comparative selfassessment for measuring the subjective quality of life of cancer patients. J. Psychosoc. Oncol. 1, 25–38. doi: 10.1300/J077v01n04_03

Birbaumer, N., and Cohen, L. G. (2007). Brain-computer interfaces: communication and restoration of movement in paralysis. J. Physiol. 579(Pt 3), 621–636. doi: 10.1113/jphysiol.2006.125633

Birbaumer, N., Murguialday, A. R., and Cohen, L. (2008). Brain-computer interface in paralysis. Curr. Opin. Neurol. 21, 634–638. doi: 10.1097/WCO.0b013e328315ee2d

Brouwer, A.-M., and Van Erp, J. B. F. (2010). A tactile P300 braincomputer interface. Front. Neurosci. 4:19. doi: 10.3389/fnins.2010.00019

Brouwer, A.-M., Van Erp, J. B. F., Aloise, F., and Cincotti, F. (2010).

Tactile, visual, and bimodal p300s: could bimodal p300s boost bci performance? SRX. Neuroscience 2010, 1–9. doi: 10.3814/2010/967027

Brunner, P., Joshi, S., Briskin, S., Wolpaw, J. R., Bischof, H., and Schalk, G. (2010). Does the “P300” speller depend on eye gaze? J. Neural Eng. 7, 056013. doi: 10.1088/17412560/7/5/056013

Bruno, M.-A., Bernheim, J. L., Ledoux, D., Pellas, F., Demertzi, A., and Laureys, S. (2011). A survey on self-assessed well-being in a cohort of chronic locked-in syndrome patients: happy majority, miserable minority. BMJ Open 1:e000039 doi: 10.1136/bmjopen-2010-000039

Dauce, E., and Proix, T. (2013). “P300speller adaptivity to change with a backspace key,” in Proceedings of the Fourth Workshop on Tools for Brain Computer Interaction (TOBI) (Sion).

Donchin, E. (1969). Discriminant analysis in average evoked response studies: the study of single trial data. Electroencephalogr. Clin. Neurophysiol. 27, 311–314. doi: 10.1016/0013-4694(69)90061-3

Eimer, M. (2000). Event-related brain potentials distinguish processing stages involved in face perception and recognition. Clin. Neurophysiol. 111, 694–705.

Farwell, L. A., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523.

Furdea, A., Halder, S., Krusienski, D. J., Bross, D., Nijboer, F., Birbaumer, N., et al. (2009). An auditory oddball (P300) spelling system for brain-computer interfaces. Psychophysiology 46, 617–625. doi: 10.1111/j. 1469-8986.2008.00783.x

Halder, S., Baykara, E., Fioravanti, C., Simon, N., Käthner, I., Pasqualotto, E., et al. (2013). “Training effects of multiple auditory BCI sessions”, in Fifth International BrainComputer Interface Meeting 2013, (Monterey). doi: 10.3217/978-385125-260-6-80

Halder, S., Rea, M., Andreoni, R., Nijboer, F., Hammer, E. M., Kleih, S. C., et al. (2010). An auditory oddball brain-computer interface for binary choices. Clin. Neurophysiol. 121, 516–523. doi: 10.1016/j.clinph.2009.11.087

Hill, N. J., and Schölkopf, B. (2012). An online brain–computer interface based on shifting attention to concurrent streams of auditory stimuli. J. Neural Eng. 9, 026011. doi: 10.1088/1741-2560/9/2/026011

Hill, N. J., Lal, T. N., Bierig, K., Birbaumer, N., and Schölkopf, B. (2005). “An Auditory Paradigm for Brain–Computer Interfaces,” in Advance in Neural Information Processing Systems, Vol. 17, eds L. K. Saul, Y. Weiss, and L. Bottou (Cambridge, MA: MIT Press), 569–576.

Höhne, J., Schreuder, M., Blankertz, B., and Tangermann, M. (2010). Two-dimensional auditory p300 speller with predictive text system. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2010, 4185–4188. doi: 10.1109/IEMBS.2010.5627379

Höhne, J., Schreuder, M., Blankertz, B., and Tangermann, M. (2011). A Novel 9-class auditory erp paradigm driving a predictive text entry system. Front. Neurosci. 5:99. doi: 10.3389/fnins.2011.00099

Holz, E., Höhne, J., Staiger-Sälzer, P., Tangermann, M., and Kübler, A. (in press). BCI-Controlled gaming: evaluation of usability by severely motor restricted end-users. Artif. Intell. Med.

Holz, E. M., Botrel, L., Kaufmann, T., and Kübler, A. (2013). “Longterm independent bci home-use by a locked-in end-user: an evaluation study,” in Procedings of the Fifth International Brain Computer Interface Meeting 2013 (Monterey, USA). doi: 10.3217/978-3-85125260-181

Holz, E. M., Kaufmann, T., Desideri, L., Malavasi, M., Hoogerwerf, E.-J., and Kübler, A. (2012). “User Centred Design in BCI Development,” in Towards Practical Brain-Computer Interfaces, eds B. Z. Allison, S. Dunne, R. Leeb, J. D. R. Millán, and A. Nijholt (Berlin, Heidelberg: Springer),155–172. Available online at http://link.springer.com/chapter/ 10.1007/978-3-642-29746-5_8

Jin, J., Allison, B. Z., Kaufmann, T., Kübler, A., Zhang, Y., Wang, X., et al. (2012). The changing face of P300 BCIs: a comparison of stimulus changes in a P300 BCI involving faces, emotion, and movement. PLoS ONE 7:e49688. doi: 10.1371/journal.pone.0049688

Jin, J., Allison, B. Z., Sellers, E. W., Brunner, C., Horki, P., Wang, X., et al. (2011). An adaptive P300based control system. J. Neural Eng. 8, 036006. doi: 10.1088/17412560/8/3/036006

Käthner, I., Ruf, C. A., Pasqualotto, E., Braun, C., Birbaumer, N., and Halder, S. (2013). A portable auditory P300 brain-computer interface with directional cues. Clin. Neurophysiol. 124, 327–338. doi: 10.1016/j.clinph.2012.08.006

Kaufmann, T., Schulz, S. M., Grünzinger, C., and Kübler, A. (2011). Flashing characters with famous faces improves ERP-based brain-computer interface performance. J. Neural Eng. 8, 056016. doi: 10.1088/1741-2560/8/5/056016

Kaufmann, T., Schulz, S. M., Köblitz, A., Renner, G., Wessig, C., and Kübler, A. (2013a). Face stimuli effectively prevent brain–computer interface inefﬁciency in patients with neurodegenerative disease. Clin. Neurophysiol. 124, 893–900. doi: 10.1016/j.clinph.2012.11.006 Kaufmann, T., Herweg, A., Kübler, A. (2013b). “Tactually-evoked event-related potentials for bci-based wheelchair control in a virtual environment,” in Proceedings of the Fifth International Brain Computer Interface Meeting (Monterey, USA). doi: 10.3217/978-4-83452-381-5/051 Kaufmann, T., Völker, S., Gunesch, L., and Kübler, A. (2012a). Spelling is just a click away - a user-centered brain-computer interface including auto-calibration and predictive text entry. Front. Neurosci. 6:72. doi: 10.3389/fnins.2012.00072

Kaufmann, T., Vögele, C., Sütterlin, S., Lukito, S., and Kübler, A. (2012b) Effects of resting heart rate variability on performance in the P300 brain-computer interface. Int. J. Psychophysiol. 83, 336–341. doi: 10.1016/j.ijpsycho.2011.11.018

Kleih, S. C., Kaufmann, T., Zickler, C., Halder, S., Leotta, F., Cincotti, F., et al. (2011). Out of the frying pan into the ﬁre—the P300-based BCI faces real-world challenges. Prog. Brain Res. 194, 27–46.

Klobassa, D. S., Vaughan, T. M., Brunner, P., Schwartz, N. E., Wolpaw, J. R., Neuper, C., et al. (2009). Toward a highthroughput auditory P300-based brain-computer interface. Clin. Neurophysiol. 120, 1252–1261. doi: 10.1016/j.clinph.2009.04.019

Krusienski, D. J., Sellers, E. W., Cabestaing, F., Bayoudh, S., McFarland, D. J., Vaughan, T. M., et al. (2006). A comparison of classiﬁcation techniques for the P300 Speller. J. Neural Eng. 3, 299–305. doi: 10.1088/1741-2560/3/4/007 Kübler, A., Furdea, A., Halder, S., Hammer, E. M., Nijboer, F., and Kotchoubey, B. (2009). A brain– computer interface controlled auditory event-related potential (p300) spelling system for locked-in patients. Ann. N.Y. Acad. Sci. 1157, 90–100. doi: 10.1111/j. 1749-6632.2008.04122.x

Kübler, A., Kotchoubey, B., Kaiser, J., Wolpaw, J. R., and Birbaumer, N. (2001). Brain-computer communication: unlocking the locked in. Psychol. Bull. 127, 358–375.

Lenhardt, A., Kaper, M., and Ritter, H. J. (2008). An adaptive P300based online brain-computer interface. IEEE transactions on neural systems and rehabilitation engineering: a publication of the IEEE Eng. Med. Biol. Soc. 16, 121–130. doi: 10.1109/TNSRE.2007.912816

Liu, T., Goldberg, L., Gao, S., and Hong, B. (2010). An online brain–computer interface using non-ﬂashing visual evoked potentials. J. Neural Eng. 7, 036003. doi: 10.1088/1741-2560/7/3/036003

Liu, Y., Zhou, Z., and Hu, D. (2011). Gaze independent brain-computer speller with covert visual search tasks. Clin. Neurophysiol. 122, 1127–1136. doi: 10.1016/j.clinph.2010.10.049

Maguire, M. C. (1998). User-Centred Requirements Handbook wp5 d5.3 of the Telematics Applications Project TE – RESPECT: Requirements Engineering and Speciﬁcation in Telematics, The RESPECT Project Consortium 1998.

Mak, J. N., Arbel, Y., Minett, J. W., McCane, L. M., Yuksel, B., Ryan, D., et al. (2011). Optimizing the P300-based brain-computer interface: current status, limitations and future directions. J. Neural Eng. 8, 025003. doi: 10.1088/1741-2560/8/2/025003

Plum, F., and Posner, J. B. (1966). The Diagnosis of Stupor and Coma. Philadelphia, PA: FA Davis.

Polich, J. (2007). Updating P300: an integrative theory of P3a and P3b. Clin. Neurophysiol. 118, 2128–2148. doi: 10.1016/j.clinph.2007.04.019 Riccio, A., Mattia, D., Simione, L., Olivetti, M., and Cincotti, F. (2012). Eye-gaze independent EEG-based brain–computer

interfaces for communication. J. Neural Eng. 9, 045001. doi: 10.1088/1741-2560/9/4/045001

Ryan, D. B., Frye, G. E., Townsend, G., Berry, D. R., Mesa,-G. S., Gates, N. A., et al. (2011). Predictive spelling with a P300-based braincomputer interface: increasing the rate of communication. Int. J. Hum. Comput. Interact. 27, 69–84. doi: 10.1080/10447318.2011. 535754

Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw, J. R. (2004). BCI2000: a general-purpose brain-computer interface (BCI) system. IEEE Trans. Biomed. Eng. 51, 1034–1043. doi: 10.1109/TBME.2004.827072

Schreuder, M., Blankertz, B., and Tangermann, M. (2010). A new auditory multi-class braincomputer interface paradigm: spatial hearing as an informative cue. PLoS ONE 5:e9813. doi: 10.1371/journal.pone.0009813

Schreuder, M., Höhne, J., Blankertz, B., Haufe, S., Dickhaus, T., and Tangermann, M. (2013). Optimizing event-related potential based brain–computer interfaces: a systematic evaluation of dynamic stopping methods. J. Neural Eng. 10, 036025. doi: 10.1088/1741-2560/10/3/036025 Schreuder, M., Rost, T., and Tangermann, M. (2011a). Listen, You are Writing! Speeding up online spelling with a dynamic auditory BCI. Front. Neurosci. 5:112. doi: 10.3389/fnins.2011.00112

Schreuder, M., Höhne, J., Treder, M., Blankertz, B., and Tangermann, M. (2011b). Performance optimization of ERP-based BCIs using dynamic stopping. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2011, 4580–4583. doi: 10.1109/ IEMBS.2011.6091134

Sellers, E. W., Arbel, Y., and Donchin, E. (2012). “BCIs that use P300

event-related potentials,” in BrainComputer Interfaces: Principles and Practice, eds J. R. Wolpaw and E. W. Wolpaw (New York, NY; Oxford: Oxford University Press), 215–226.

Sellers, E. W., and Donchin, E. (2006). A P300-based braincomputer interface: initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548. doi: 10.1016/j.clinph.2005.06.027

Sellers, E. W., Vaughan, T. M., and Wolpaw, J. R. (2010). A braincomputer interface for long-term independent home use. Amyotroph. Lateral Scler. 11, 449–455. doi: 10.3109/174829610037774706/ j.clinph.2005.06.027

Sutton, S., Braren, M., Zubin, J., and John, E. R. (1965). Evoked-potential correlates of stimulus uncertainty. Science 150, 1187–1188. doi: 10.1126/science.150.3700.1187

Thurlings, M. E., Van Erp, J. B. F., Brouwer, A.-M., Blankertz, B., and Werkhoven, P. (2012). Control-display mapping in brain– computer interfaces. Ergonomics 55, 564–580. doi: 10.1080/00140139. 2012.661085

Treder, M. S., and Blankertz, B. (2010). (C)overt attention and visual speller design in an ERP-based braincomputer interface. Behav. Brain Funct. 6, 28. doi: 10.1186/17449081-6-28

van der Waal, M., Severens, M., Geuze, J., and Desain, P. (2012). Introducing the tactile speller: an ERP-based brain–computer interface for communication. J. Neural Eng. 9, 045002. doi: 10.1088/1741-2560/9/4/045002

Wolpaw, J. R., and Wolpaw, E. W. (2012). Brain-Computer Interfaces: Principles and Practice. New York, NY; Oxford: Oxford University Press.

Zhang, Y., Zhao, Q., Jin, J., Wang, X., and Cichocki, A. (2012). A

novel BCI based on ERP components sensitive to conﬁgural processing of human faces. J. Neural Eng. 9, 026018. doi: 10.1088/17412560/9/2/026018

Zickler, C., Halder, S., Kleih, S. C., Herbert, C., and Kübler, A. (in press). Brain painting: usability testing according to the usercentered design in end users with severe disabilities. Artif. Intell. Med.

Zickler, C., Riccio, A., Leotta, F., Hillian-Tress, S., Halder, S., Holz, E., et al. (2011). A brain-computer interface as input channel for a standard assistive technology software. Clin. EEG Neurosci. 42, 236–244. doi: 10.1177/1550059411 0420040

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 26 March 2013; accepted: 05 July 2013; published online: 24 July 2013. Citation: Kaufmann T, Holz EM and Kübler A (2013) Comparison of tactile, auditory, and visual modality for braincomputer interface use: a case study with a patient in the locked-in state. Front. Neurosci. 7:129. doi: 10.3389/ fnins.2013.00129 This article was submitted to Frontiers in Neuroprosthetics, a specialty of Frontiers in Neuroscience. Copyright © 2013 Kaufmann, Holz and Kübler. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in other forums, provided the original authors and source are credited and subject to any copyright notices concerning any third-party graphics etc.

