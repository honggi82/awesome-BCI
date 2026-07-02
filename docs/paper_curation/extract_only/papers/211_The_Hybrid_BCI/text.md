#### PERSPECTIVE ARTICLE

published: 21 April 2010 doi: 10.3389/fnpro.2010.00003

# The hybrid BCI

## Gert Pfurtscheller1*, Brendan Z. Allison1, Clemens Brunner1, Gunther Bauernfeind1, Teodoro Solis-Escalante1, Reinhold Scherer2, Thorsten O. Zander3, Gernot Mueller-Putz1, Christa Neuper1 and Niels Birbaumer4,5

- 1 Laboratory of Brain-Computer Interfaces, Institute for Knowledge Discovery, Graz University of Technology, Graz, Austria
- 2 Computer Science and Engineering, University of Washington, Seattle, WA, USA
- 3 Team PhyPA, Department of Human-Machine Systems, Berlin University of Technology, Berlin, Germany
- 4 Institute of Medical Psychology and Behavioral Neurobiology, Eberhard-Karls-University, Tübingen, Germany
- 5 Istituto di Ricovero e Cura a Carattere Scientiﬁco, Ospedale San Camillo, Venezia, Italy

Edited by: José del R. Millán, Ecole Polytechnique Fédérale de Lausanne, Switzerland Reviewed by: Dario Farina, Aalborg University, Denmark Shangkai Gao, Tsinghua University, China

*Correspondence: Gert Pfurtscheller, Laboratory of Brain-Computer Interfaces, Institute for Knowledge Discovery, Graz University of Technology, Krenngasse 37, Graz 8010, Austria. e-mail: pfurtscheller@tugraz.at

Nowadays, everybody knows what a hybrid car is. A hybrid car normally has two engines to enhance energy efﬁciency and reduce CO2 output. Similarly, a hybrid brain-computer interface (BCI) is composed of two BCIs, or at least one BCI and another system. A hybrid BCI, like any BCI, must fulﬁll the following four criteria: (i) the device must rely on signals recorded directly from the brain; (ii) there must be at least one recordable brain signal that the user can intentionally modulate to effect goal-directed behaviour; (iii) real time processing; and (iv) the user must obtain feedback. This paper introduces hybrid BCIs that have already been published or are in development. We also introduce concepts for future work. We describe BCIs that classify two EEG patterns: one is the event-related (de)synchronisation (ERD, ERS) of sensorimotor rhythms, and the other is the steady-state visual evoked potential (SSVEP). Hybrid BCIs can either process their inputs simultaneously, or operate two systems sequentially, where the ﬁrst system can act as a “brain switch”. For example, we describe a hybrid BCI that simultaneously combines ERD and SSVEP BCIs. We also describe a sequential hybrid BCI, in which subjects could use a brain switch to control an SSVEP-based hand orthosis. Subjects who used this hybrid BCI exhibited about half the false positives encountered while using the SSVEP BCI alone. A brain switch can also rely on hemodynamic changes measured through near-infrared spectroscopy (NIRS). Hybrid BCIs can also use one brain signal and a different type of input. This additional input can be an electrophysiological signal such as the heart rate, or a signal from an external device such as an eye tracking system.

Keywords: brain–computer interface, hybrid BCI, motor imagery, event-related desynchronization, SSVEP

## INTRODUCTION

Brain–computer interface (BCI) research is advancing very rapidly. Most BCI research still focuses on restoring communication and control in severely paralysed patients (Birbaumer et al., 1999; Wolpaw et al., 2002; Pfurtscheller et al., 2008a), but BCIs are quickly becoming useful to healthy people too (Allison et al., 2007; Nijholt et al., 2008). Modern BCIs may use invasive and non-invasive recording techniques, and non-invasive BCIs may rely on electrical potentials, magnetic ﬁelds, and hemodynamic changes (Wolpaw et al., 2006; Vaadia and Birbaumer, 2009). Non-invasive BCIs utilize changes in the dynamics of brain oscillations such as event-related (de)synchronization (ERD, ERS), steady-state evoked potentials (SSEPs), P300 evoked potentials and related components, real-time fMRI BOLD signals or near-infrared spectroscopy (NIRS)-measured oxyhemoglobin signals (Pfurtscheller et al., 2005a; Birbaumer and Cohen, 2007; Sitaram et al., 2007). Each of these BCIs has advantages and disadvantages.

Conventional “simple” BCIs rely on only one of these signals. Here, we describe ways to combine different approaches to create a “hybrid” BCI that exploits the advantages of different approaches. We also describe “hybrid” BCIs that combine a BCI with another interface.

A hybrid car usually has two engines, which rely on electricity and gasoline. The major goals of such a hybrid car are to enhance their energy efﬁciency and to reduce their CO2 output. Similarly, a typical hybrid BCI is also composed of one BCI and another system (which might be another BCI), and must also achieve speciﬁc goals better than a conventional system. For example, a hybrid BCI might infer user intent more accurately during imagery-based and/or visual attention-based experimental paradigms, improve the overall performance of the system, or reduce the rate of false positives during resting periods of i.e. steady-state visual evoked potential (SSVEP)-based BCI applications. The hybrid BCI can either have more than one input whereby the inputs are typically processed simultaneously (Figures 1B,C) or operate two systems sequentially, whereby the ﬁrst system can act as a “brain switch” (Figures 1A,D,E) or as “selector” (Figures 1F,G). There are other types of sequential BCIs possible, which could go beyond these switch/selector concepts and/or incorporate P300-based or other types or BCIs. We use the terms “simultaneous” and “sequential” to refer to these two types of hybrid BCIs. In both cases, as in any BCI, at least one of the input signals must be a signal recorded directly from the brain.

[Figure 1]

FIGURE 1 | Examples of hybrid BCIs with sequential (A,D–G) and simultaneous processing (B,C).

A brain switch is a BCI system designed to detect only one brain state (brain pattern) in the ongoing brain activity. A brain switch, like any communication system, should not produce any output when the user does not intend to communicate. In other words, the false positive rate should be as low as possible. Mason and Birch (2000) were the ﬁrst to develop a brain switch based on EEG. They proposed a low-frequency asynchronous switch design able to automatically recognize single-trial, voluntary motor related potentials from ongoing EEG activity in bipolar channels. Recent work demonstrated that a single channel brain switch can also be realized when the post-imagery beta ERS is detected in the EEG during motor imagery (Pfurtscheller et al., 2005b; Pfurtscheller and Solis-Escalante, 2009; Solis-Escalante et al., 2010). A brain switch can also rely on SSVEPs with a high amplitude threshold (Cheng et al., 2002) or hemodynamic changes measured through NIRS (Coyle et al., 2007).

A simultaneous hybrid BCI can either use two different brain signals (e.g. electrical and hemodynamic signals), one brain signal (e.g. EEG) associated with two mental strategies (motor imagery and spatial visual attention;Figure 1C), or one brain signal and another input. Such an additional input can be a physiological signal like the electrocardiogram (ECG, Figure 1B) or a signal from an external device such as an eye gaze control system (Zander et al., in press).

Hybrid BCIs, like any BCI, must fulﬁl four criteria to function as BCI:

- 1. Direct: The system must rely on activity recorded directly from the brain.
- 2. Intentional control: At least one recordable brain signal, which can be intentionally modulated, must provide input to the BCI (electrical potentials, magnetic ﬁelds or hemodynamic changes).
- 3. Real time processing: The signal processing must occur online and yield a communication or control signal.

4. Feedback: The user must obtain feedback about the success or failure of his/her efforts to communicate or control.

## HYBRID BCI SYSTEMS

### SIMULTANEOUS ERD/SSVEP BCI TO IMPROVE ACCURACY

In a recent study, we evaluated the feasibility of combining two mental tasks that simulated a simultaneous hybrid BCI (Figure 1C). Fourteen subjects participated in three conditions that simulated a binary BCI (a BCI that allows two choices). In all conditions, each trial began with an arrow pointing to the left or right, which indicated that the subject should perform a left or right motor imagery task. In the ﬁrst condition (the ERD condition), the left task was imagined left hand movement, and the right task was imagined right hand movement. In the second condition (the SSVEP condition), a left arrow cued the subject to focus attention on a left LED that ﬂickered at 8 Hz, and the right arrow cued the subject to focus on a right LED that ﬂickered at 13 Hz. In the third condition (the hybrid condition), a left arrow cued the subject to both imagine left hand movement and attend to the left LED, while the right arrow cued the subject to both imagine right hand movement and attend to the right LED. Performance was measured by classiﬁcation accuracy (that is, whether a classiﬁer could correctly distinguish left versus right tasks from the EEG) and subjective report (based on questionnaires). Table 1 summarizes the resulting classiﬁcation accuracies as well as the number of illiterates (subjects whose classiﬁcation accuracy was below 70%). More details can be found elsewhere (Allison et al., 2010; Brunner et al., 2010).

There were four noteworthy results. First, classiﬁcation accuracy was highest in the hybrid condition, although this effect did not reach statistical signiﬁcance. Second, in both the ERD and SSVEP conditions, some subjects could not attain proﬁciency, meaning that their classiﬁcation accuracy was too low for effective communication.

Table 1 | Mean and standard deviation of the classiﬁcation accuracy of 14 subjects in each condition.

ERD SSVEP Hybrid

Mean accuracy (%) 69.4 82.8 84.5 Standard deviation (%) 8.6 12.2 10.2 Number of illiterates 11 3 1

The bottom row shows the number of illiterates, corresponding to subjects with a classiﬁcation accuracy below 70%.

This phenomenon has been called “BCI illiteracy” by some authors (Kübler and Müller, 2007; Nijholt et al., 2008). However, when a subject was not proﬁcient with either the ERD or SSVEP approach, s/he was usually proﬁcient with the other approach. This result implies that people who could not use an ERD BCI might attain proﬁciency with an SSVEP BCI, and vice versa. Third, the number of illiterates in the hybrid condition was signiﬁcantly lower than in the ERD condition, while there was no signiﬁcant difference in illiteracy in the SSVEP-hybrid comparison or the ERD-SSVEP comparison. This implies that subjects who could not use an ERD or SSVEP BCI could use a hybrid BCI. Fourth, the questionnaire responses revealed that subjects generally did not consider the hybrid condition more difﬁcult than the other two conditions. Hence, a hybrid BCI might yield improved performance without taxing the user any more than a conventional simple BCI.

### SEQUENTIAL ERS-BASED BRAIN SWITCH TO TURN ON/OFF AN SSVEP BCI

The sequential hybrid BCI approach was inspired by earlier work that showed that SSVEP BCIs often send signals when the user did not intend to convey anything (called false positives), which can be especially problematic during breaks or resting periods. We recorded SSVEPs bipolarly from electrodes placed over the occipital area (electrode position O1, 2.5 cm inter-electrode distance). Subjects could focus on one of two LEDs mounted on an orthosis to open or close the orthosis whenever they wanted (Otto Bock Healthcare Products GmbH, Vienna, Austria). That is, we implemented a self-paced or asynchronous BCI, rather than a cue-paced or synchronous BCI. Subjects received real-time feedback by watching the orthosis open or close, and could hence correct errors. Our paradigm included some resting periods (breaks), during which the subjects were asked to avoid sending any commands. The LEDs continued to ﬂicker during breaks, and the SSVEP detection algorithm remained active.

Figure 2 summarizes the results in 10 able-bodied subjects (Linortner et al., 2009). The main ﬁndings were that most subjects could perform the task without training, but produced many false positives. Interestingly, good and bad performers displayed about the same rate of false positives during all resting periods, which collectively lasted several minutes. The rate of false nonintended commands in resting periods (FPr) was between 4 and 5/min, while the rate of false commands during orthosis control (FPa) was between 0.1 and 0.4/min. Hence, we wanted to ﬁnd a way to improve this system by reducing the false positive rate.

The ERS-based brain switch detects brisk imagined foot movements in one Laplacian EEG channel recorded at the vertex (Cz) (Solis-Escalante et al., 2008, 2010; Pfurtscheller and Solis-Escalante,

[Figure 2]

FIGURE 2 | Performance measures of hand orthosis control in 10 subjects. This ﬁgure displays the errors during orthosis control (FPa; right y-axis: scale 0–1.0) and during rest (FPr; left y-axis: 0–6). The x-axis presents subjects organized from low to high FPa. Subjects’ FPas did not affect their FPrs.

2009), and can be seen as a special type of ERD BCI. Foot motor imagery induces a relatively stable pattern, known as post-imagery ERS or beta rebound, which can be easily recorded with electrodes overlaying the foot representation area close to the vertex (Pfurtscheller et al., 2005b; Pfurtscheller and Lopes da Silva, 1999). A post-imagery beta ERS-based brain switch has three appealing features: minimal training time for both the user and the classiﬁer; effective communication with only one EEG channel; and few false positives.

We hypothesized that FPs during SSVEP conditions might be reduced by allowing subjects to deactivate the LEDs and SSVEP detection via the brain switch when they do not want to send commands.Figure 1A illustrates this concept of using a hybrid BCI that uses a brain switch to turn on/off an SSVEP BCI. We developed an ERS-based switch to activate or deactivate a four-step SSVEP-based orthosis. Users operate the SSVEP part of the BCI by gazing at an 8-Hz LED to open it, and gazing at a 13-Hz LED to close it. The brain switch ensures that the LEDs and SSVEP detection algorithms (Müller-Putz et al., 2008) only operate when needed for control; the user can deactivate the LEDs and SSVEP detection algorithm during resting periods.

Figure 3 shows additional examples of self-paced switch control and orthosis operation in a healthy subject. Data from two runs (each lasting about 400 s) are displayed separately for the brain switch and the SSVEP orthosis control. In the ﬁrst run four errors (FP) occurred with the switch during the total experiment. The orthosis control was erroneous in the ﬁrst orthosis activity period, but nearly perfect thereafter. The situation improved in the second run, since no error occurred during switch control (FP = 0). This example shows a beneﬁt of learning the dual task paradigm in this hybrid BCI, as documented by the improvements in run#2, and also shows that such a hybrid BCI is feasible (Pfurtscheller et al., 2010b).

This hybrid approach requires shifting between motor and visual tasks. Imagined movement induced the post-imagery ERS (beta rebound, used in switch), whereas visual attention modulates SSVEPs. Throughout the self-paced task, the user always obtained feedback

[Figure 3]

FIGURE 3 | Examples of two runs (runs #1 and #2) in one able-bodied subject (s3) over several minutes each.The lower traces of runs #1 and #2 display the four-step sequence of opening/closing the SSVEP-based orthosis with two 60-s breaks (grey shaded). The upper traces of runs #1 and #2 show the ERS-based switch operation (black bars indicate switch opened). The four-steps of orthosis opening (from left to right) are displayed in the bottom panel.

about success or failure of BCI operation, and could therefore adapt his or her mental strategy if necessary.Table 2 shows the positive prediction value PPV [PPV = TP/(TP + FP)] for the brain switch (called PPVb) and for the SSVEP BCI (called PPVa) over six runs. The PPVb was 0.77 ± 0.19 (mean ± SD), and the PPVa was 0.73 ± 20.

### NIRS-BASED BCI AS A BRAIN SWITCH

In preliminary work, we explored an asynchronous hybrid BCI that combines a NIRS BCI with SSVEP orthosis control (Figure 1E). The optical BCI is based on NIRS and measures mentally modulated oxyhemoglobin (HbO2) changes at closely spaced optodes placed over a predeﬁned cortical area (for examples see Coyle et al., 2007; Bauernfeind et al., 2008).

One healthy subject performed four runs with the hybrid BCI system. In each run, the subject had to open and close (one activation block) the orthosis three times (for details see Sequential ERSbased Brain Switch to Turn On/Off an SSVEP BCI andPfurtscheller et al., 2010b), each at self paced intervals, with 60 s breaks between the blocks (resting periods). Prior to the ﬁrst block, the subject had to initiate the SSVEP orthosis control using the optical BCI. The brain switch was activated if the relative oxyhemoglobin concentration change (measured with two closely spaced optodes over position Fp1, see Figure 4), normalized to a 4-s baseline interval, exceeded a subject-speciﬁc value. During the resting period and after the last activation block, the subject was instructed to switch off the SSVEP orthosis control system to avoid FPs.

During the ﬁrst two runs, FPs were detected in the activation as well as in the resting period. Figure 4 shows that the subject displayed perfect performance in the third run using the NIRS

Table 2 | Results from our study involving a brain switch to turn on/off an SSVEP based orthosis.

Subject/run Brain switch SSVEP

TP FP PPVb PPVa FPr (min–1)

- S11 5 0 1.00 0.47 0.00
- S12 5 2 0.71 0.52 0.50

- S21 11 9 0.55 0.82 2.50
- S22 8 3 0.73 1.00 1.00

- S31 7 4 0.64 0.79 3.00
- S32 5 0 1.00 0.76 0.00 Mean 6.83 3.00 0.77 0.73 1.17 SD 2.40 3.35 0.19 0.2 1.29

The six runs reﬂect two runs each from three subjects. We show the rates of TPs, FPs and PPVb of the ERD BCI (switch) and PPVa and rate of errors/minute during resting periods (FPr) of the SSVEP BCI.

[Figure 4]

FIGURE4 | From top to bottom: Position trace of the switch (grey areas mark closed switch position) and four-step SSVEP-based orthosis control trace (grey areas indicate 60-s resting periods) of run#2; position trace of brain switch and orthosis control of run#3; level of oxyhemoglobin

(HbO2) concentration of run#3; views of prefrontal optodes and bipolar occipital EEG electrode placements. FPs of switch (FP) and SSVEP-based

orthosis control (FPa, FPr) are indicated. Note the HbO2 peaks associated with the intended mental tasks.

switch, and only one FP occurred during the SSVEP orthosis control. In the last run, the subject displayed perfect performance with 100% accuracy, meaning no FPs occurred in the NIRS and SSVEP control, respectively.

Like the EEG, NIRS is well suited to BCI applications outside the lab. NIRS requires a simple optode montage, is relatively resistant to artefacts, and can be combined with EEG recording to

allow simultaneous measurement of electrical and hemodynamic changes. Both imaging approaches can detect speciﬁc brain states with a minimum of sensors (one bipolar EEG channel and two optodes). However, EEG can detect brain changes instantly, whereas NIRS entails a delay of a few seconds (Coyle et al., 2007). Further research is necessary to identify better training strategies, new experimental paradigms, and optimal optode positions to reliably classify data from a one or two NIRS channel BCI systems.

Spatio-temporal differences in brain oxygenation during movement execution and imagery were reported by Wriessnegger et al. (2008). They used a 24-channel NIRS system and explored the topographical distribution of the NIRS responses in a movement task. Their work showed that optode location selection and/or optimization is very important when developing a one-channel optical BCI suitable within a hybrid BCI.

### ENHANCEMENT OF BCI ACCURACY WITH BOTH EEG AND HEART RATE EVALUATION

Neocortical structures and the cardiovascular nuclei in the brain stem communicate intensively (Verberne and Owens, 1998). Central commands can activate cardiovascular nuclei in the brainstem and modify the heart rate (HR). Hence, motor imagery produces changes not only in characteristic EEG patterns (Pfurtscheller and Neuper, 2001), but also in the HR (Pfurtscheller et al., 2006, 2008b).

The HR can display either an event-related HR deceleration or acceleration. Two responses can be distinguished with HR deceleration: an early response related to stimulus anticipation and registration;

and a second response related to motor preparation (Lacey and Lacey, 1980; Damen and Brunia, 1987; Papakostopoulos et al., 1990). One characteristic and stable HR response is its deceleration prior to internally (self)-paced ﬁnger movements (Florian et al., 1998; Pfurtscheller et al., 2010a). HR acceleration is also a common response to many situations; HR acceleration was reported during mental simulation of movement (Decety et al., 1991; Oishi et al., 2000) and during motor imagery (Papadelis et al., 2007; Pfurtscheller et al., 2008b).

Preparation of a speciﬁc movement and imagination of the same movement involve similar cortical networks (Porro et al., 1996; Lotze et al., 1999). Execution of movement is generally accompanied by a biphasic HR response starting with a preparatory decrease, followed by a fast increase and a decrease to the baseline (Brunia and Damen, 1985; Papakostopoulos et al., 1990; Florian et al., 1998). In training sessions with an EEG-based BCI (hand versus foot motor imagery), the HR usually decelerates (see Fig. 2 in Pfurtscheller et al., 2006). However, during EEG-based control of “walking” in a virtual street, the same mental strategy can induce HR acceleration (see Fig. 3 in Pfurtscheller et al., 2006). This suggests that the increased somatomotor effort and emotional processing (“walking” in virtual reality) are driving forces behind the HR acceleration. During a similar walking experiment in a virtual street, a tetraplegic patient revealed a signiﬁcant HR increases in parallel with the mentally induced beta bursts (Figure 5).

The HR changes in the order of 10–20 bpm during effortful mental activity suggest that the BCI performance could be improved when a hybrid BCI uses both the EEG and the HR

[Figure 5]

synchronous averaged HR response (mean ± SD, lower panel, right). Remarkably, the HR increase starts some seconds before the band power enhancement. Modiﬁed from Pfurtscheller et al. (2008b).

FIGURE 5 | Raw EEG, heart rate and time course of the logarithmic band power (15–19 Hz), enlarged from a 10-s time window (lower panel, left), and averaged logarithmic beta power (mean ± SD) together with

response simultaneously for control purposes (Figure 1B).Figure 6 presents ofﬂine analyses of the HR changes in the tetraplegic patient, which revealed that changes in the differentiated HR (dHR) can be detected in parallel with the motor imagery-induced EEG bursts used for online control.

### INDUCED HR CHANGES FOR ON/OFF SWITCHES IN A SSVEP BCI

The previous section explored hybridizing a BCI with HR activity to increase accuracy. However, transient HR changes could also be used in a switch that is hybridized with a BCI, like a brain switch based on the ERD (see Sequential ERS-based Brain Switch to Turn On/Off an SSVEP BCI) or the hemodynamic response (see NIRS-based BCI as a Brain Switch). Respiration and blood pressure waves usually modulate the constant intrinsic rhythm of the heart. However, HR changes can also be modulated by central commands. Therefore, individuals may modulate their own HR by mental activity correlated with somatomotor processes (see Brunia and Damen, 1985; Papakostopoulos et al., 1990). Behaviourally triggered HR changes can be used in a switch (Figure 1D).

In an initial feasibility study to explore this prospect, we used brisk inspiration to modulate the HR. The HR-triggered switch could turn the SSVEP-operated prosthetic hand on and off. We recorded the ECG and computed the HR. Changes of the HR

measured in beat-to-beat intervals (RRI) were computed and used to initiate the SSVEP BCI control. An on/off event was generated

each time the relative change (dRRI), induced by brisk inspiration, exceeded the subject-speciﬁc threshold (see Figure 7B). The relative RRI change with the highest true positive rates during the cue-guided inspiration, and the lowest false positive detections during the remaining tasks, were selected through receiver operating analysis and used as basis for the online experiments.

Four light emitting diodes were afﬁxed on the hand prosthesis (see Figure 7A), each ﬂickering at a different frequency between 6.3 and 17.3 Hz (stimulation frequency). The EEG was recorded bipolarly from EEG electrodes placed 2.5 cm anterior and posterior to electrode position O2. The harmonic sum decision algorithm (Müller-Putz et al., 2005) was used for the SSVEP classiﬁcation. The ﬂickering light source with the highest harmonic sum within a given time period triggered the prosthetic hand movement. A typical selection time period of about 1.5 s was estimated empirically for each subject (see Scherer et al., 2007).

The online experiment used to evaluate the performance of the HR-switch lasted about 30 min. Subjects were verbally instructed to turn on the SSVEP BCI, perform a pre-deﬁned motion sequence with the prosthetic hand, then turn the BCI off. The motion sequence to be performed was:

- (i) O: open the hand;
- (ii) L: rotate the hand 90° to the left;
- (iii) R: rotate the hand 90° to the right;

[Figure 6]

FIGURE 6 | Beta power and HR changes during self-paced motor imagery. This Figure shows logarithmic beta power with online detected output signals (vertical lines) during mental practice in virtual environment (for details see

Pfurtscheller et al., 2008b), HR and ﬁrst derivative of HR (dHR). The dHR time course shows that the detection of foot motor imagery with the HR correlates well with EEG detection and revealed six TPs, one FP and two FNs.

[Figure 7]

FIGURE 7 | Prosthetic hand with four mounted LEDs (A), examples of respiratory signals (Resp), heart beat-to-beat intervals (RRI) measured in seconds and ﬁrst derivative of RRI (dRRI) during intentional (B) and non-intentional control (C). Two motion sequences (O, R, L, C) and the threshold are indicated. Modiﬁed from Scherer et al. (2007).

- (iv) C: close the hand;
- (v) R: rotate the hand 90° to the right;
- (vi) O: open the hand;
- (vii) C: close the hand; and
- (viii) L: rotate 90° left, back to the original position.

The whole sequence had to be performed four times within 30 min. The start time of each sequence was randomly chosen by the experimenter, who talked to the subjects between the motor sequences. Subjects succeeded in switching on and off the BCI by

brisk inspiration and operating the SSVEP-actuated hand prosthesis. Eight true positive HR switches were required to turn the BCI on and off for the four movement trials. The average number of false positive RRI detections was 2.9. The average number of erroneous (true negative) RRI detections was 4.9. The average selection speed for one out of the four SSVEP classes was about 9.5 s (6.3 commands per minute). On average, one SSVEP detection per minute was erroneous. These results, based on ten able-bodied subjects, suggest that transient HR changes, induced by brisk inspiration, are feasible signals in a hybrid BCI.

measures is feasible, similar to the example inFigure 1D. To ensure that the dwell times match stimulus complexity, different variants were evaluated in pilot experiments (1000 ms “easy”/1300 ms “difﬁcult”). Details can be found in Vilimek and Zander (2009).

Figure 7 shows examples of two sequences with respiratory and RRI signals, during intentional prosthesis control (Figure 7B) and non-intentional control (Figure 7C). The motion sequence was performed during the time between “ON” and “OFF”.

The comparison of dwell time based approaches (eye gaze input) versus the ERD-based approach shows that the ERD BCI is statistically signiﬁcantly more accurate when selecting items of different complexity (seeFigure 8). For both search conditions, task completion was fastest with short dwell times (easy: 4.0 s; difﬁcult: 5.4 s), next was dwell time long, with BCI solution as the slowest activation method (5.9 s; 8.8 s), over both conditions.

### COMBINING EYE GAZE AND ERD BCI

This study, conducted in cooperation among Team PhyPA, TU Berlin, and Siemens Corporate Technology in Munich, Germany1, explored an ERD-based BCI (ERD BCI) and eye gaze cursor control. If patients can control parts of their peripheral nervous system (PNS), then physiological signals from the PNS could provide control in a hybrid BCI. For example, if users can control eye movements, then they could select an item on the screen by ﬁxating on it (Bolt, 1982; Jacob et al., 1993). The difﬁculty is the deﬁnition of an appropriate time window for the response (dwell time). It should be longer than the time needed to read the information encoded in the stimulus. Otherwise, items might be accidentally selected when a user simply looks at them, before s/he decided whether to select it. The dwell time should be as short as possible to avoid frustration and unnecessarily slow communication. It is difﬁcult, and maybe impossible, to establish the optimal dwell time without an additional communication channel. Until now there is no adequate solution that deals appropriately with different stimulus complexities. One reason for this is the utilization of human gaze for two tasks – searching and selecting. While searching is a natural action within gaze behaviour, human beings are not used to triggering commands with their eyes.

A strong user preference (90%) and signiﬁcantly lower frustration ratings (NASA TLX, frustration scale) resulted from subjective measures. Since subjects selected items more slowly and were less frustrated with an ERD approach, we infer that the subjects appreciated selecting items at their own pace. Taken together, these ﬁndings show that an ERD BCI could be an effective tool for supplementing eye gaze. Our results also suggest that a hybrid BCI based on eye gaze and ERD might be particularly useful in environments with rapid stimulus complexity changes.

## DISCUSSION

The described work shows that a hybrid BCI could successfully combine two different mental strategies, namely imagined hand movement and spatial visual attention. The mean accuracy of the reported cue-paced ERD study (see Simultaneous ERD/SSVEP BCI to Improve Accuracy; Allison et al., 2010; Brunner et al., 2010) was relatively poor (69.1 ± 8.6%, mean ± SD; 14 subjects). The low accuracy probably had two causes: the group consisted of naïve subjects without any BCI experience or training; and only two bipolar EEG channels over C3 and C4 were used. In a similar ERD study (Pfurtscheller et al., 2008c) with experienced subjects, 30 EEG recordings and processing with the common spatial pattern method the corresponding mean accuracy was 80 ± 10% (10 subjects) for the discrimination between left and right hand imagery.

One approach for solving this problem could be the addition of a second communication channel. This extra channel should be independent of eye movements, but still under voluntary control of the user. Both requirements might be fulﬁlled by an ERD BCI. Hence, an eye gaze system might be hybridized with an ERD BCI, as proposed in Figure 1G. Ten participants took part in this study, ranging from 19 to 36 years old. All participants reported normal or corrected-to-normal vision. The participants had to perform a search-and-select task. A reference string presented in the centre of the screen had to be found in a set of 12 strings, consisting of 11 distractors and one target. These strings were presented in a circular arrangement around the reference string to ensure a constant spatial distance. To emulate changes in the complexity of information encoded in items, two types of conditions have been deﬁned. The “easy” condition used strings with four letters, and the “difﬁcult” condition used strings with seven letters. All strings used only consonants to avoid similarities to known words. The distractors shared characters in some positions with the target string, and differed in other positions. The stimuli were chosen to avoid taxing working memory in the “easy” condition, and to push the limits of working memory in the “difﬁcult” condition. Indeed, classic work in cognitive psychology has shown that most people’s working memory is limited to about seven items (Miller, 1994).

[Figure 8]

In one condition, subjects had to select the target stimulus by ﬁxating it for two different given dwell times. In the other condition, subjects instead used ERD to select targets. This approach shows that deﬁning hybrid BCIs with two inputs from different physiological

FIGURE 8 | For condition “easy”, accuracy of the BCI based solution was only slightly lower (88%) compared to the long dwell times (DTL, 93%). Short dwell times (DTS) resulted in the lowest mean accuracy (83.3%). Remarkably, the BCI achieves the best results in accuracy for the condition “difﬁcult” (78.7%), but only the difference to the short dwell time (51.1%)

##### 1We thank Christian Kothe and Matti Gaertner (Team PhyPA) and Roman Vilimek was signiﬁcant. (Siemens AG) for their support and help with this study.

However, in both of these studies, the maximum of the discrimination peak was present relatively early, namely ∼1 s after visual cue onset. Examples for two subjects out of Pfurtscheller’s study (Figures 9A,B) and ﬁve subjects out of Allison and Brunner’s study (Figure 9C) document this early discrimination peak. This suggests that the discrimination between left and right motor imagery was strongest in a small time window after cue presentation. Other studies support this interpretation.Müller-Gerking et al. (2000) already reported such an initial recognition peak after visual cue presentation when subjects had to execute a real movement 1.5 s after cue-offset. They inferred that this result reﬂected a very short-lived brain state lasting about 300 ms after visual cue presentation. These ﬁndings with two different tasks, a memorized delayed movement execution task (Müller-Gerking et al., 2000) and a motor imagery task (Pfurtscheller et al., 2008c; Allison et al., 2010; Brunner et al., 2010), suggest that the visual cue acts as a trigger and activates visual speciﬁc cortical motor areas. Naito et al. (2002) suggested that “motor memories” are stored in cortical motor areas and cerebellar motor systems, and are important when memories related to previous actions are retrieved. However, this cue-triggered motor cortex activation starting about 300 ms after cue-onset is not necessarily a conscious process. This supports our view that a hybrid BCI that

[Figure 9]

FIGURE 9 | Example of discrimination time courses (off-line classiﬁcation accuracy) from two different studies with visual cue-based right and left hand motor imagery. In one study (Pfurtscheller et al., 2008c) subjects with BCI experience took part, whereas the other study used naïve subjects (for details see “Simultaneous ERD/SSVEP BCI to Improve Accuracy”; Allison et al., 2010). (A,B) Display the discrimination accuracy of two subjects from the group of BCI experienced subjects, and (C) displays superimposed accuracy time courses of ﬁve subjects of the naïve group. In all examples an early discrimination peak ∼1 s after visual cue onset is visible. Cue duration is indicated by the grey area.

combines simultaneous ERD- and SSVEP-processing could yield better performance than an ERD- or SSVEP BCI alone because only the visual attention task requires fully conscious effort.

The switch concept we introduced, which uses only two EEG channels (one over motor cortex and one over occipital cortex) to combine ERD and SSVEP BCIs to realize orthosis control, demonstrates the usefulness of the hybrid BCI concept. In the six runs reported (Table 2), the false positive rate in resting periods was 1.2 ± 1.3/min (mean ± SD). This rate is clearly lower than the false positive rate reported during SSVEP-based orthosis control without brain switch (Linortner et al., 2009; Pfurtscheller et al., 2010b), which shows that the brain switch concept could substantially reduce false positives.

The ECG could also be used as second input for a hybrid BCI to enhance classiﬁcation accuracy. This is only feasible with a paradigm that produces a large HR change. Cardiac and respiratory activity during imagined movement is proportional to mental effort (Decety et al., 1991). Subjects who vividly imagined a speed skating sprint displayed a signiﬁcant HR increase (Oishi et al., 2000). Large HR responses may also occur when the user performs BCI experiments in an immersive virtual environment (VE). Pfurtscheller et al. (2008b) reported HR changes in the order of 10 bpm associated with foot motor imagery-based wheelchair movement in a multi-projection based stereo VE system commonly known as CAVE (Cave Automatic Virtual Environment). In such a hybrid BCI, it is fairly easy to classify such changes in the HR, and combine the results with the EEG classiﬁcations. Also, the imagery induced HR response is not always the same, and can differ between labs and CAVE applications (Pfurtscheller et al., 2006). The HR decreased during cue-paced motor imagery in the order of 3–5%, while the HR increased during immersive CAVE conditions by about the same amount.

When the HR is used as additional input signal for a hybrid BCI, the great variability of this signal must be considered. The HR is not only modiﬁed by the respiration and blood pressure waves of higher order (see e.g. Pfurtscheller et al., 2010a), but is also affected by fear, feelings, stress, mood or other psychological states. The major source for HR changes, namely the impact of respiration on the HR can be reduced, e.g. by an adaptive autoregressive ﬁlter algorithm (Florian et al., 1998). For the reduction of slow blood pressure waves on the HR the same algorithm can be used. Rapid changes in the HR are mediated by only the parasympathetic system, whereas slower variations are mediated beside others by the sympathetic system (Levy, 1977). Furthermore, it is vital that a BCI function when the user is under stress. These could be times when the user needs to communicate most. In stressful situations, the baroreﬂex vagal component is suppressed and the HR increases (Nosaka et al., 1991). Hybrid BCIs that use HR activity must account for stressrelated changes in the HR.

Some of the studies reported used a limited number of subjects. More subjects should be run to assess effects across different people. However, the studies do validate different hybrid BCI concepts, and demonstrate the great variety of possible hybrid BCIs. In some cases (see Enhancement of BCI Accuracy With Both EEG and Heart Rate Evaluation), we started with ofﬂine simulations using data from “old” experiments. In other cases (see NIRS-based BCI as a Brain Switch) online studies are planned with feedback. Section

“Simultaneous ERD/SSVEP BCI to Improve Accuracy” describes ofﬂine simulations of a hybrid BCI, and we have just developed an online version of this study to explore this simultaneous hybrid approach. Promising results from one pilot subject are reported in Allison et al. (2010).

The large scale integrated project TOBI (Tools for Brain– Computer Interaction, EU Project FP 7 224631) aims to develop hybrid BCIs using a different deﬁnition. The TOBI project uses the same deﬁnition of a hybrid BCI as in the introduction, with the exception that a BCI should be available only if the user needs it. That is, a TOBI hybrid BCI might effectively use only one type of signal. Such a hybrid system might decide which input channel(s) offer the most reliable signal(s), and/or switch between input channels to improve information transfer rate, usability, or other factors.

### CONCLUSION AND OUTLOOK

Summarizing, different hybrid BCIs could expand a conventional “simple” BCI in different ways. Hybrid BCIs could involve a second type of input operating sequentially and/or simultaneously. The second input might be another BCI, which might require the user to perform additional mental tasks. The second input might use on other physiological signals (Wolpaw et al., 2002), or could be a conventional input such as a keyboard or mouse (Nijholt et al., 2008). Examples of sequentially operating hybrid BCIs include systems where the ﬁrst BCI acts as simple switch to turn on/off the second BCI. This approach has been validated with two BCIs that use electrical brain signals, modiﬁed by different mental strategies (see Sequential ERS-based Brain Switch to Turn On/Off an SSVEP BCI), and two BCIs based on hemodynamic and electrical signals (see NIRS-based BCI as a Brain Switch), and a system that combines a BCI with HR changes

(see Enhancement of BCI Accuracy With Both EEG and Heart Rate Evaluation and Induced HR Changes for On/Off Switches in a SSVEP BCI). Instead of serving as a switch, the second input might instead improve accuracy. This concept was validated in a study that combined ERD and SSVEP tasks (see Simultaneous ERD/SSVEP BCI to Improve Accuracy), and a different study that could lead to an ERD BCI combined with an eye tracker (see Combining Eye Gaze and ERD BCI).

Future work should assess different combinations of input signals, possibly involving three or more signals. One of the great challenges in hybrid BCI research is identifying the best combinations of signals to accomplish desired goals. The optimal combination probably differs considerably across users, and in some situations, a BCI might not be the best input mechanism. For a more comprehensive evaluation of hybrid BCIs, factors including system complexity, cost, user workload have to be evaluated. In the TOBI deﬁnition of a hybrid BCI, a BCI has to be available, and not necessarily used.

## ACKNOWLEDGMENTS

This work was partially supported by the EU project PRESENCCIA (IST-2006-27731), the European Community’s Seventh Framework Programme FP7/2007-2013, BrainAble project, under grant agreement n° 247447, the Wings for Life – Spinal Cord Research Foundation, the Austrian Allgemeine Unfallversicherung (AUVA), the LorenzBöhler Gesellschaft the Deutsche Forschungsgemeinschaft (DFS), the Land Steiermark (project A3-22.N-13/2009-8), the Neuro Center Styria (NCS), the BMBF-Computational Neuroscience BernsteinProject and a grant from the European Research Council (ERC). We would like to thank Rupert Ortner and Patricia Linortner for assistance during the data collection of different experiments and the support of Otto Bock Healthcare Products GmbH, Vienna, Austria for providing the orthosis.

## REFERENCES

Allison, B. Z., Brunner, C., Kaiser, V., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2010). Toward a hybrid brain–computer interface based on imagined movement and visual attention.J. Neural Eng. (in press). Allison, B. Z., Wolpaw, E. W., and Wolpaw, J. R. (2007). Brain–computer interface systems: progress and prospects.Expert Rev. Med. Devices 4, 463–474.

Bauernfeind, G., Leeb, R., Wriessnegger, S. C., and Pfurtscheller, G. (2008). Development, set-up and ﬁrst results for a one-channel near-infrared spectroscopy system.Biomed. Tech. (Berl.) 53, 36–43.

Birbaumer, N., and Cohen, L. G. (2007). Brain–computer interfaces: communication and restoration of movement in paralysis. J. Physiol. 579(Pt. 3), 621–636.

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kübler, A., Perelmouter, J., Taub, E., and Flor, H. (1999). A spelling device for the paralysed. Nature 398, 297–298.

Bolt, R. A. (1982). “Eyes at the interface,” in Proceedings of the 1982 Conference on Human Factors in Computing Systems (New York: ACM Press), 360—362.

Brunia, C. H. M., and Damen, E. J. P. (1985). “Evoked cardiac responses during a ﬁxed 4 sec foreperiod preceding four different responses,” in Psychophysiology of Cardiovascular Control, eds J. F. Orlebeke, G. Mulder and L. J. P. van Doornen (New York: Plenum Publishing Corporation), 613–619.

Brunner, C., Allison, B. Z., Krusienski, D. J., Kaiser, V., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2010). Improved signal processing approaches in an ofﬂine simulation of a hybrid brain–computer interface. J. Neurosci. Methods (in press).

Cheng, M., Gao, X., Gao, S., and Xu, D. (2002). Design and implementation of a brain–computer interface with high transfer rates. IEEE Trans. Biomed. Eng. 49, 1181–1186.

Coyle, S. M., Ward, T. E., and Markham, C. M. (2007). Brain–computer interface using a simplified functional

near-infrared spectroscopy system. J. Neural Eng. 4, 219–226.

Damen, E. J. P., and Brunia, C. H. M. (1987). Changes in heart rate and slow brain potentials related to motor preparation and stimulus anticipation in a time estimation task.Psychophysiology 24, 700–713.

Decety, J., Jeannerod, M., Germain M., and Pastene, J. (1991). Vegetative response during imagined movement is proportional to mental effort.Behav. Brain Res. 42, 1–5.

Florian, G., Stancak, A., and Pfurtscheller, G. (1998). Cardiac response induced by voluntary self-paced ﬁnger movement. Int. J. Psychophysiol. 28, 273–283. Jacob, R. J. K., Legett, J. J., Myers, B. A., and Pausch, R. (1993). Interaction styles and input/output devices. Behav. Inf. Technol. 12, 69–79.

Kübler, A., and Müller K. R. (2007). “An introduction to brain computer interfacing,” in Toward Brain–Computer Interfacing, eds G. Dornhege, J. R. Millán, T. Hinterberger, D. McFarland and K. R. Müller (Cambridge, MA: MIT press), 1–25.

Lacey, B. C., and Lacey, J. I. (1980). Cognitive modulation of timedependent primary bradycardia. Psychophysiology 17, 209–222.

Levy, M. N. (1977). “Parasympathetic control of the heart,” inNeural Regulation of the Heart, eds W. C. Randall (New York: Oxford University Press), 95–129.

Linortner, P., Ortner, R., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2009). “Self -paced control of a hand orthosis using SSVEP-based BCI,” in Proceedings of the13th International Conference on Human–Computer Interaction 2009 (Heidelberg: Springer), 716–720.

Lotze, M., Montoya, P., Erb, M., Hulsmann, E., Flor, H., Klose, U., Birbaumer, N., and Grodd, W. (1999). Activation of cortical and cerebellar motor areas during executed and imagined hand movements: an fMRI study. J. Cogn. Neurosci. 11, 491–501.

Mason, S. G., and Birch, G. E. (2000). A brain-controlled switch for asynchronous control applications.IEEE Trans. Biomed. Eng. 47, 1297–1307.

Miller, G. A. (1994). The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychol. Rev. 101, 343–352.

Müller-Gerking, J., Pfurtscheller, G., and Flyvbjerg, H. (2000). Classiﬁcation of movement-related EEG in a memorized delay task experiment. Clin. Neurophysiol. 111, 1353–1365.

Müller-Putz, G. R., Eder, E., Wriessnegger, S. C., and Pfurtscheller, G. (2008). Comparison of DFT and lock-in ampliﬁer features and search for optimal electrode positions in SSVEP-based BCI.J. Neurosci. Methods 168, 174–181.

Müller-Putz, G. R., Scherer, R., Brauneis, C., and Pfurtscheller, G. (2005). Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components. J. Neural Eng. 2, 1–8.

Naito, E., Kochiyama, T., Kitada, R., Nakamura, S., Matsumura, M., Yonekura, Y., and Sadato, N. (2002). Internally simulated movement sensations during motor imagery activate cortical motor areas and the cerebellum. J. Neurosci. 22, 3683–3691.

Nijholt, A., Tan, D., Pfurtscheller, G., Brunner, C., Millan, J. R., Allison, B., Graimann, B., Popescu, F., Blankertz, B., and Müller K. R. (2008). Brain– computer interfacing for intelligent systems. IEEE Intell. Syst. 23, 72–79.

Nosaka, S., Murase, S., and Murata, K. (1991). Arterial baroreﬂex inhibition by gastric distension in rats: mediation by splanchnic afferents.Am. J. Physiol. 260, R985–R994.

Oishi, K., Kasai T., and Maeshima, T. (2000). Autonomic response specificity during motor imagery. J. Physiol. Anthropol. Appl. Hum. Sci. 19, 255–261.

Papadelis, C., Kourtidou-Papadeli, C., Bamidis, P., and Albani, M. (2007). Effects of imagery training on cognitive performance and use of physiological measures as an assessment tool of mental effort.Brain Cogn. 64, 74–85.

Papakostopoulos, D., Banerji, N. K., and Pocock, P. V. (1990). Performance, EMG, brain electrical potentials and heart rate change during a self-paced skilled motor task in Parkinson’s disease. J. Psychophysiol. 4, 163.

Pfurtscheller, G., Leeb, R., and Slater, M. (2006). Cardiac responses induced

during thought-based control of a virtual environment.Int. J. Psychophysiol. 62, 134–140.

Pfurtscheller G., and Lopes da Silva F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857.

Pfurtscheller, G., Müller-Putz, G., Scherer, R., and Neuper, C. (2008a). Rehabilitation with brain–computer interface systems. IEEE Comp. Mag. 41, 58–65.

Pfurtscheller, G., Leeb, R., Friedman, D., and Slater, M. (2008b). Centrally controlled heart rate changes during mental practice in immersive virtual environment: a case study with a tetraplegic. Int. J. Psychophysiol. 68, 1–5.

Pfurtscheller, G., Scherer, R., MüllerPutz, G. R., and Lopes da Silva, F. H. (2008c). Short-lived brain state after cued motor imagery in naive subjects. Eur. J. Neurosci. 28, 1419–1426.

Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct brain–

computer communication.Proc. IEEE 89, 1123–1134.

Pfurtscheller, G., Neuper, C., and Birbaumer, N. (2005a). “Human brain–computer interface,” in Motor Cortex in Voluntary Movements: A Distributed System for Distributed Functions. Series: Methods and New Frontiers in Neuroscience, eds E. Vaadia and A. Riehle (Boca Raton: CRC Press), 367–401.

Pfurtscheller, G., Neuper, C., Brunner, C., and Lopes da Silva, F. H. (2005b). Beta rebound after different types of motor imagery in man.Neurosci. Lett. 378, 156–159.

Pfurtscheller G., Ortner R., Bauernfeind G., Linortner P., and Neuper C. (2010a). Does conscious intention to perform a motor act depend on slow cardiovascular rhythms? Neurosci. Lett. 468, 46–50.

Pfurtscheller, G., Solis-Escalante, T., Ortner, R., Linortner, P., and MüllerPutz, G. R. (2010b). Self-paced operation of an SSVEP-based orthosis with and without an imagery-based “brain switch”: a feasibility study towards a hybrid BCI. IEEE Trans. Neural Syst. Rehabil. Eng. (in press).

Pfurtscheller, G., and Solis-Escalante, T. (2009). Could the beta rebound

in the EEG be suitable to realize a “brain switch”? Clin. Neurophysiol. 120, 24–29.

Porro, C. A., Francescato, M. P., Cettolo, V., Diamond, M. E., Baraldi, P., Zuiani, C., Bazzocchi, M,., and di Prampero, P. E. (1996). Primary motor and sensory cortex activation during motor performance and motor imagery: a functional magnetic resonance imaging study. J. Neurosci. 16, 7688–7698.

Scherer, R., Müller-Putz, G. R., and Pfurtscheller, G. (2007). Self-

initiation of EEG-based brain–computer communication using the heart rate response. J. Neural Eng. 4, L23–L29.

Sitaram R., Zhang H., Guan C, Thulasidas M., Hoshi Y., Ishikawa A., Shimizu K., and Birbaumer N. (2007). Temporal classiﬁcation of multichannel nearinfrared spectroscopy signals of motor imagery for developing a brain–

computer interface. Neuroimage 34, 1416–1427.

Solis-Escalante, T., Müller-Putz, G. R., Brunner, C., Kaiser V., and Pfurtscheller, G. (2010). Analysis of sensorimotor rhythms for the implementation of a brain switch for healthy subjects. Biomed. Signal Process. Control 5, 15–20.

Solis-Escalante, T., Müller-Putz, G. R., and Pfurtscheller, G. (2008). Overt foot movement detection in one single Laplacian EEG derivation.J. Neurosci. Methods 175, 148–153.

Vaadia, E., and Birbaumer, N. (2009). Grand challenges of brain computer interfaces in the years to come. Front. Neurosci. 3, 151–154.

Verberne, A. J., and Owens, N. C. (1998). Cortical modulation of the cardiovascular system. Prog. Neurobiol. 54, 149–168.

Vilimek, R., and Zander, T.O. (2009). “BC(eye): combining eye-gaze input with brain–computer interaction,” in Lecture Notes In Computer Science, Vol. 5615: Proceedings of the 5th International on Conference on Universal Access in Human–Computer Interaction. Part II: Intelligent and Ubiquitous Interaction Environments, HCI International San Diego (Berlin/ Heidelberg: Springer-Verlag).

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T.

M. (2002). Brain–computer interfaces for communication and control.Clin. Neurophysiol. 113, 767–791.

Wolpaw, J. R., Loeb, G. E., Allison, B. Z., Donchin, E., do Nascimento, O. F., Heetderks, W. J., Nijboer, F., Shain,W. G., and Turner, J. N. (2006). BCI meeting 2005 – workshop on signals and recording methods. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 138–141.

Wriessnegger, S. C., Kurzmann, J., and Neuper, C. (2008). Spatio- temporal differences in brain oxygenation between movement execution and imagery: a multichannel nearinfrared spectroscopy study. Int. J. Psychophysiol. 67, 54–63.

Zander, T. O., Kothe, C., Jatzev S., and Gaertner M. (in press). “Enhancing human–computer interaction with input from active and passive brain–computer interfaces,” in The Human in Brain–Computer Interfaces and the Brain in Human–Computer Interaction, eds D. S. Tan and A. Nijholt (Berlin: Springer).

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conﬂict of interest.

Received: 18 December 2009; paper pending published: 22 February 2010; accepted: 15 March 2010; published online: 21 April 2010. Citation: Pfurtscheller G, Allison BZ, Brunner C, Bauernfeind G, Solis-Escalante T, Scherer R, Zander TO, Mueller-Putz G, Neuper C and Birbaumer N (2010) The hybrid BCI. Front. Neurosci. 4:30. doi: 10.3389/fnpro.2010.00003 This article was submitted to Frontiers in Neuroprosthetics, a specialty of Frontiers in Neuroscience. Copyright © 2010 Pfurtscheller, Allison, Brunner, Bauernfeind, Solis-Escalante, Scherer, Zander, Mueller-Putz, Neuper and Birbaumer. This is an open-access article subject to an exclusive license agreement between the authors and the Frontiers Research Foundation, which permits unrestricted use, distribution, and reproduction in any medium, provided the original authors and source are credited.

