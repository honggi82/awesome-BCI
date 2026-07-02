#### Methods Article

published: 07 February 2011 doi: 10.3389/fnins.2011.00005

# Rapid communication with a “P300” matrix speller using electrocorticographic signals (ECoG)

### Peter Brunner1,2,3, Anthony L. Ritaccio3, Joseph F. Emrich4, Horst Bischof2 and Gerwin Schalk1,3,5,6,7*

- 1 New York State Department of Health, Brain–Computer Interface Research and Development Program, Wadsworth Center, Albany, NY, USA
- 2 Institute for Computer Graphics and Vision, Graz University of Technology, Graz, Austria
- 3 Department of Neurology, Albany Medical College, Albany, NY, USA
- 4 Department of Neurosurgery, Albany Medical College, Albany, NY, USA
- 5 Department of Neurosurgery, Washington University School of Medicine, St. Louis, MO, USA
- 6 Department of Biomedical Sciences, State University of New York at Albany, Albany, NY, USA
- 7 Department of Biomedical Engineering, Rensselaer Polytechnic Institute, Troy, NY, USA

Edited by: Carsten Mehring, Imperial College London, UK Reviewed by: Andrea Kubler, University of Wuerzburg, Germany Ferran Galan, Newcastle University, UK Nick F. Ramsey, University Medical Center Utrecht, Netherlands

*Correspondence: Gerwin Schalk, Brain-Computer Interface R&D Program, Wadsworth Center, New York State Department of Health, C650 Empire State Plaza, Albany, NY 12201, USA. e-mail: schalk@wadsworth.org

A brain–computer interface (BCI) can provide a non-muscular communication channel to severely disabled people. One particular realization of a BCI is the P300 matrix speller that was originally described by Farwell and Donchin (1988). This speller uses event-related potentials (ERPs) that include the P300 ERP. All previous online studies of the P300 matrix speller used scalprecorded electroencephalography (EEG) and were limited in their communication performance to only a few characters per minute. In our study, we investigated the feasibility of using electrocorticographic (ECoG) signals for online operation of the matrix speller, and determined associated spelling rates. We used the matrix speller that is implemented in the BCI2000 system. This speller used ECoG signals that were recorded from frontal, parietal, and occipital areas in one subject. This subject spelled a total of 444 characters in online experiments. The results showed that the subject sustained a rate of 17 characters/min (i.e., 69 bits/min), and achieved a peak rate of 22 characters/min (i.e., 113 bits/min). Detailed analysis of the results suggests that ERPs over visual areas (i.e., visual evoked potentials) contribute significantly to the performance of the matrix speller BCI system. Our results also point to potential reasons for the apparent advantages in spelling performance of ECoG compared to EEG. Thus, with additional verification in more subjects, these results may further extend the communication options for people with serious neuromuscular disabilities.

Keywords: brain–computer interface, electrocorticography, event-related potential, P300, speller

- 1 IntroductIon Many people affected by neurological or neuromuscular disorders such as amyotrophic lateral sclerosis (ALS), brainstem stroke, or spinal cord injury, are impaired in their ability to or even unable to communicate. A brain–computer interface (BCI) uses brain signals to restore some of the lost function. A BCI approach that several groups have begun to test in clinical applications in humans (e.g., Sellers et al., 2006, 2010; Vaughan et al., 2006; Nijboer et al., 2008; see Donchin and Arbel, 2009 for a comprehensive review) is the matrix-based speller originally described by Farwell and Donchin

(1988). This speller uses different event-related potentials (ERPs) including the P300 evoked response. In this system, the user attends to a character in a matrix while each row or column flashes rapidly and pseudo-randomly. The brain produces a response to the row or column that contains the intended character (i.e., the oddball); this response is different for the other rows or columns. The BCI can detect the desired character by determining the row and column that produces the largest evoked response. Using this approach, recent electroencephalography (EEG)-based studies (Serby et al., 2005; Sellers et al., 2006, 2010; Lenhardt et al., 2008; Nijboer et al., 2008; Guger et al., 2009) reported real-time accuracies from 79 to 91% (6 × 6 matrix of 36 characters; 2.8% chance) at 13–42 s per selection.

A growing number of recent studies (e.g.,Leuthardt et al., 2004, 2006; Wilson et al., 2006; Felton et al., 2007; Schalk et al., 2008; Miller et al., 2010; Ritaccio et al., 2010; Vansteensel et al., 2010) suggested that signals recorded from the surface of the brain [electrocorticography (ECoG)] are a promising platform for real-time BCI communication. This advantage is due in part to the high spatial, spectral, and temporal fidelity that characterize ECoG signals (Leuthardt et al., 2004; Miller et al., 2007, 2008; Ball et al., 2009; Brunner et al., 2009). It is possible that these favorable signal characteristics may provide distinct advantages in the context of the matrix speller, but this has not been explored.

In this study, we investigated this possibility by evaluating the feasibility and online performance of the matrix speller using ECoG signals recorded from frontal, parietal, and occipital areas in one human subject. We hypothesized that these experiments will provide evidence that the ECoG-based speller may support communication rates that are higher than those typically expected by EEG-based spellers. The results demonstrate that ECoG allows for accurate single-trial detection of evoked responses, and thereby supports very high communication rates. Thus, with additional verification in more subjects, these results may further extend the communication options for people with serious neuromuscular disabilities.

- 2 methoDs 2.1 human subjeCt The subject in this study was a 29-year-old right-handed woman with intractable epilepsy who underwent temporary placement of subdural electrode arrays (see Figure 1A) to localize seizure foci prior to surgical resection. The subject had corrected-to-normal vision and gave informed consent through a protocol reviewed and approved by the review board of Albany Medical College.

A neuropsychological evaluation revealed a full-scale IQ score of 122 (93rd percentile;Wechsler, 1997), superior visuomotor scanning performance (92nd percentile, Trail Marking Test; Reitan, 1958), and average visual search capacity (75th percentile, WAISIII: Symbol Search Subtest; Wechsler, 1997).

The subject had a total of 96 subdural electrode contacts (i.e., one

- 8× 8 64-contact grid, one 23-contact grid, and two strips in 1× 6 and 1× 3 configuration, respectively). These grids/strips were placed over the left hemisphere in frontal, parietal, temporal, and occipital regions (see Figure 1B for details). The implants consisted of flat electrodes with an exposed diameter of 2.3 mm and an inter-electrode distance of 1 cm, and were implanted for 1 week. Grid placement and duration

|[Figure 1]<br><br>[Figure 2]<br><br>[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>[Figure 8]<br><br>[Figure 9]<br><br>A B<br><br>Figure 1 | implant. The subject had 96 subdural electrodes (two grids and two strips in different configurations) implanted over left frontal, parietal, temporal, and occipital regions. (A) Photograph of the craniotomy and the implanted grids in this subject. (B) Lateral X-ray of the subject, showing an 8 × 8 grid over frontal/parietal cortex, a 23-contact grid over temporal cortex, and several strips.|
|---|

of ECoG monitoring were based solely on the requirements of the clinical evaluation without any consideration of this study. Following placement of the subdural grid, postoperative CT imaging verified grid location (Talairach and Tournoux, 1988).

- 2.2 Data ColleCtion We recorded ECoG from the implanted electrodes using six g.USBamp amplifier/digitizer systems (g.tec, Graz, Austria) and the BCI software platform BCI2000 (Schalk et al., 2004; Mellinger and Schalk, 2007; Schalk and Mellinger, 2010). Simultaneous clinical monitoring was implemented using a connector that split the cables coming from the patient into one set that was connected to the clinical monitoring system and another set that was connected to the g.USBamp devices. Thus, at no time was clinical care or clinical data collection compromised. Two electrocorticographically silent electrodes (i.e., locations that were not identified as eloquent cortex by electrocortical stimulation mapping) over inferior and superior posterior parietal cortex served as ground and reference, respectively. We used a grounding connection between the g.USBamp systems and the patient’s skin to dissipate any electric currents generated by external electromagnetic fields and to block electromagnetic interference. The amplifiers sampled the signal at 512 Hz and used a high-pass filter at 0.1 Hz and a notch filter at 60 Hz.
- 2.3 experimental paraDigm The subject sat 60 cm in front of a flat-screen monitor. She was presented with a matrix of alphanumeric characters that was centered on the screen and arranged in a 6 × 6 configuration (see Figure 2). At this distance, the matrix subtended ±7.1° of the horizontal and vertical visual field.

The subject participated in a recording session that consisted of offline and online experiments. In the offline (i.e., calibration) experiments, the BCI2000 matrix speller flashed each of the 12 rows or columns in a pseudo-random sequence. Flashes occurred at a rate of 16 Hz. Each flash lasted 1/64 s (16 ms) to 3/64 s (47 ms), followed by a 1/64 to 3/64-s inter-stimulus period. The intensity contrast between a flash and a non-flash was 3:1. Fifteen flash sequences comprised one trial. The subject’s task in each trial was to pay

|[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>[Figure 17]<br><br>Figure 2 | experimental setup. The subject sat 60 cm in front of a flat-screen monitor that presented a centered 6 × 6 matrix containing alphanumeric characters as well as space (Sp) and backspace (Bs). The rows and columns in the matrix flashed rapidly and pseudo-randomly. The subject’s task was to pay attention to the intended character. The computer determined the intended character from the subject’s ECoG responses.|
|---|

attention to the highlighted character in the words “THE QUICK BROWN,” and to make a mental note (i.e., to count) each time the correct row/column flashed. A 3-s pause (i.e., “flight time”) between characters gave the subject time to shift her attention onto the next character. We used the ECoG data collected in this calibration experiment to establish a classifier using the stepwise regression method reported in Krusienski et al. (2006). We then configured the BCI to use this classifier in online experiments.

During each of the seven online experiments, the subject copyspelled the sentence “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” The BCI system provided feedback of the characters predicted from the ECoG signals. The subject selected “backspace” to correct incorrect selections. In the seven online experiments, the subject spelled a total of 301 characters (i.e., 444 characters including “backspace” and subsequent corrections) using different stimulation parameters that are described in more detail in the Section “Results.”

- 2.4 offlIne analyses In offline analyses of data from each of the calibration experiments, we first filtered the signal between 0.1 and 20 Hz and downsampled it to 40 Hz. We then extracted the stimulus response, i.e., the ECoG signals from all 96 channels for 500 ms after stimulus onset (see Figure 3). This yielded 20 features (i.e., 40 × 0.5 = 20) per channel or a total of 1920 features for all 96 channels. We define a sequence to be 12 flashes, i.e., flashes of six rows and six columns of the presented matrix. Of these 12 flashes, two (i.e., the row and column that contained the desired character) are expected to elicit a target evoked response (i.e., oddball ERP) and 10 are not. With 15 flash sequences in each trial, this yielded 30 target ERPs and 150 nontarget ERPs. As we recorded 13 trials (i.e., each character in “THE QUICK BROWN”) during a calibration experiment, this resulted in a total of 390 target and 1950 non-target ERPs for calibration.
- 2.5 stepwIse regressIon model In the matrix speller paradigm, the subject’s selection is predicted by the intersection of the row and column that elicits the largest target-related response. Farwell and Donchin (1988) proposed

|[Figure 18]<br><br>[Figure 19]<br><br>[Figure 20]<br><br>[Figure 21]<br><br>[Figure 22]<br><br>[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]<br><br>[Figure 26]<br><br>[Figure 27]<br><br>[Figure 28]<br><br>[Figure 29]<br><br>[Figure 30]<br><br>[Figure 31]<br><br>[Figure 32]<br><br>[Figure 33]<br><br>[Figure 34]<br><br>[Figure 35]<br><br>[Figure 36]<br><br>[Figure 37]<br><br>[Figure 38]<br><br>[Figure 39]<br><br>[Figure 40]<br><br>[Figure 41]<br><br>[Figure 42]<br><br>[Figure 43]<br><br>[Figure 44]<br><br>[Figure 45]<br><br>[Figure 46]<br><br>[Figure 47]<br><br>[Figure 48]<br><br>[Figure 49]<br><br>[Figure 50]<br><br>[Figure 51]<br><br>[Figure 52]<br><br>[Figure 53]<br><br>[Figure 54]<br><br>[Figure 55]<br><br>[Figure 56]<br><br>[Figure 57]<br><br>[Figure 58]<br><br>[Figure 59]<br><br>Figure 3 | event-related potentials (erPs). The figure above shows averaged event-related responses to target (red) and non-target (blue) flashes at each of the 96 recorded locations.|
|---|

multiple approaches to determine the target-related response from data for which the intended selection is known (i.e., calibration data). These approaches included stepwise regression, peak picking, area under the curve measurements, and the covariance. In our study, we used a stepwise regression procedure that has been described in detail in Krusienski et al. (2006). In brief, we first filtered the brain signal from each channel between 0.1 and 20 Hz and downsampled it to 40 Hz. The downsampled ECoG signal of all 96 channels for 500 ms after stimulus onset comprised a total of 1920 potential signal features. A stepwise procedure then produced a linear model that predicted, given a subset of all features, whether or not the stimulus associated with these features was a target or non-target. In this iterative procedure, each step added the most significant and/or removed the least significant feature based on the p-value of an F-statistic (padd = 0.1, premove = 0.15; Jennrich, 1977). To prevent overfitting, the stepwise procedure limited the number of features to 60 and terminated when a step did not further improve the regression model or when the maximum number of iterations (5000) was reached. In summary, this procedure reduced the 1920 potential ECoG features to a maximum of 60 features, and resulted in a linear model that was predictive of target or non-target. This linear model was applied to the ECoG response to each stimulus (i.e., row or column flash). The row and column with the highest model output defined the predicted character. Because there were 36 characters, chance accuracy was 2.8%.

- 2.6 onlIne experIments For each online experiment, we used one of three different flash durations (i.e., 1/64, 2/64, 3/64 s). For each flash duration, we collected calibration data (“THE QUICK BROWN”) and performed the offline analyses described above to establish a regression model. We then used this model to evaluate online system performance. In these online experiments, we asked the subject to use the matrix speller BCI system to spell “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” The BCI system provided feedback on the predicted characters as shown in Figure 2. The subject performed a “backspace” selection to correct for incorrect selections. 3 results
- 3.1 optImIzatIon of system performance Over the course of online experimentation, we continually optimized system parameters (i.e., the flash duration and number of flash sequences) so as to optimize the subject’s information transfer rate. The results are shown in Figure 4 and Table 1. For one flash sequence, spelling accuracy reached a maximum of 81% (see Figure 4) at a flash duration of 3/64 s. We then used a flash duration of 3/64 s (i.e., 47 ms) and increased the number of flash sequences. The accuracy reached 98% at three flash sequences, while the actual information transfer rate (i.e., bit rate), which was calculated including stimulation- and flight-time, peaked at 60.5 bits/min and two flash sequences (i.e., a selection every 4.5 s).

In a subsequent seventh 3.5 min run, we reduced the time between selections to 2 s. The subject achieved a selection every 3.5 s at 86.4% accuracy. This represents an information transfer rate of 69 bits/min or 17 characters/min.

|Figure 4 | Optimizing accuracy and information transfer rate. The figure on the left shows the relationship between the flash duration and letter classification accuracy with a single-flash sequence. The figure on the right shows the relationship between the number of flash sequences and classification accuracy using a flash duration of 3/64 s (i.e., 47 ms). The subject reached a maximum of 98% classification accuracy at three flash sequences, and a maximum of 60.5 bits/min at 92.2% accuracy (i.e., a selection every 4.5 s) at two flash sequences.|
|---|

- Table 1 | Optimizing accuracy and information transfer rate.

Flash duration Flash sequences Accuracy Bit rate (s) (%) (bits/min)

- 1/64 1 42
- 2/64 1 61
- 3/64 1 81

- 3/64 1 78 53
- 3/64 2 92 60
- 3/64 3 98 56

The first three rows of the table show the relationship between flash duration and classification accuracy with a single-flash sequence. The lower three rows show the relationship between the number of flash sequences and classification accuracy using a flash duration of 3/64 s (i.e., 47 ms). The data in these tables corresponds to the traces in Figure 4.

In a final run, we further decreased the number of flash sequences to one. In this run, which is shown in Video 1 in Supplementary Material, the subject spelled the word “FLOWER” at a rate of

- 2.75 s/character (i.e., 22 characters/min or 113 bits/min).
- 3.2 cortIcal locatIons wIth sIgnIfIcant evoked responses The results presented in the previous section demonstrated that the BCI system successfully predicted the intended character online with an accuracy of 81% using only one flash of each row/column. We were interested in the physiological basis for this successful demonstration, i.e., in the cortical locations and ERP components that held significant information. To do this, we trained the classifier separately on each location using the calibration data with a flash duration of 3/64 s, and evaluated performance on the online

data with the same flash duration and 1–3 flash sequences.Figure 5 shows the locations of all 96 subdural electrodes (blue dots) and the corresponding color-coded classification accuracies. Accuracy ranged from chance level (1/(6 × 6) = 2.8%) to 50% for the best electrode location.

Statistical comparisons (two-samplet-test, Bonferroni corrected for the number of features, i.e., 1920) of each extracted feature (ECoG amplitudes at a given time and location) between target and non-target conditions revealed statistically significant (p << 0.001) differences over wide-spread areas in secondary visual cortex (see locations marked with A, B, C, D in the brain plot in Figure 5), associative visual cortex (E), angular gyrus (F), and somatosensory association cortex (G). The traces below show the correlation of the ECoG signals following the flash with the type of the ERP (i.e., target vs. non-target). This correlation analysis for locations A–G showed dominant peaks between 125 and 175 ms after the flash. The polarities of these peaks were reversed between the neighboring electrodes C, D, and E. Furthermore, signals recorded from angular gyrus (F), but not other locations, were sensitive to the orientation (i.e., row or column) of the attended flash (p = 0.00003).

3.3 optImIzIng number of electrodes

The results presented in the previous section show that, in this particular subject, ERPs recorded from electrodes over visual cortex contribute significantly to the performance of the matrix speller BCI system. This suggests that a similar level of performance may be achieved using recordings from only a few electrodes over a relatively small area, which is important for potential clinical application of this approach. Thus, we were interested in the relationship between the number of utilized electrodes over visual cortex and spelling performance.

To do this, in offline post hoc analyses, we evaluated spelling performance using 1–6 electrodes over visual cortex (i.e., locations A–F in Figure 5) and 1–3 flash sequences. In these analyses, we used the same calibration data as in the online experiment (i.e., “THE QUICK BROWN,” 15 flash sequences, 3/64 s flash duration). We then established one classifier for each possible combination of the 1–6 electrodes over visual cortex. For each combination, we then applied the corresponding classifier to the data from the online experiments. The results in Figure 6 and Table 2 show the relationship between the best combinations of 1–6 electrodes and spelling performance, i.e., accuracy and bit rate, for 1–3 flash sequences. The results suggest that this particular subject could achieve a maximum of 100% classification accuracy at three flash sequences and four electrodes, and a maximum of 64 bits/min at two flash sequences and five electrodes. Furthermore, one bipolar derivation ( between locations C and A) may already allow for 57 bits/min or 90% of the peak spelling performance supported by five electrodes (see Table 2).

### 4 dIscussIon

The results of this study show that ECoG can support matrix BCI spelling at a sustained rate of 17 characters/min (i.e., 69 bits/min) and a peak rate of 22 characters/min (i.e., 113 bits/min). In line with recently completed studies (Brunner et al., 2010a,b; Treder and Blankertz, 2010), our offline analyses show that visual areas provided important contributions to the subject’s performance. The results also indicate that only one bipolar derivation over visual

|[Figure 60]<br><br>[Figure 61]<br><br>[Figure 62]<br><br>G<br><br>F E<br><br>D<br><br>C<br><br>B<br><br>A<br><br>|[Figure 63]|
|---|
<br><br>0%<br><br>10%<br><br>20%<br><br>30%<br><br>40%<br><br>50%<br><br>chance<br><br>TIME (ms)<br><br>CORRELATION (r)<br><br>0 100 200 300 400 500<br><br>0 100 200 300 400 500<br><br>-0.2<br><br>0<br><br>0.2<br><br>A<br>B<br>C<br>D<br>E<br>F<br>G<br><br><br>Figure 5 | Qualitative results. The figure at the top shows the locations of the 96 subdural electrodes (blue dots), as well as the color-coded single-flash classification accuracy at each individual electrode.The traces at the bottom show the correlation between ECoG amplitude and the type of the stimulus (target/non-target) for cortical locations A–g.|
|---|

|Figure 6 | Optimizing number of electrodes. The two figures show the relationship between the number of electrodes over visual cortex and accuracy (left) or bit rate (right) that this subject may achieve with these electrodes at one (blue circle), two (green triangle), and three (orange square) flash sequences. The subject may achieve a maximum of 100% classification accuracy at three flash sequences and four electrodes, and a maximum of 64 bits/min at two flash sequences and five electrodes.|
|---|

The spelling rate reported for the one subject in this ECoGbased study (i.e., 17 sustained characters/min or 69 bits/min) is 3–4 times higher than what had previously been reported in EEGbased P300 BCI studies (i.e., 1.4–4.5 characters/min; Serby et al., 2005; Sellers et al., 2006, 2010; Lenhardt et al., 2008; Nijboer et al., 2008; Guger et al., 2009)1 or in EEG-based sensory motor rhythm (SMR) BCI studies (1.7–4.9 characters/min; Wolpaw et al., 1991; McFarland et al., 2003; Pfurtscheller et al., 2003; Müller et al., 2008). Furthermore, the sustained performance demonstrated in this study is within the same range of previously reported EEG-based steadystate visual evoked potential (SSVEP) studies (15.8–18.7 characters/ min; Gao et al., 2003; Bin et al., 2009). Finally, to the best of our knowledge, the peak performance shown here is the highest BCI performance demonstrated in humans to date.

## CORRELATION (r)

The spelling rate of the ECoG-based matrix speller BCI shown here is beginning to match or even exceed that of conventional assistive devices. These devices are often either intrusive (e.g., cheek or tongue-switch), cumbersome (e.g., letter board), or susceptible to fatigue (e.g., video-based eye-trackers using the corneal reflection). Thus, while invasive, the BCI method presented here may provide distinct advantages over those conventional assistive devices.

While the spelling rate shown here is very high, it is still at least one order of magnitude slower than conventional communication (e.g., 200–400 characters using keyboard or voice; Majaranta and Räihä, 2002; Schalk, 2008). Although the spelling rate of the matrix speller could be further improved, there are fundamental limitations to these potential improvements. These limitations are due to the required dwell time (i.e., the time during which the rows/columns are intensified) and the flight time (i.e., the time between two characters). In our study, we used single-flash sequence

cortex could support almost the same level of performance. In conclusion, with verification of our results in more subjects, these findings may increase the BCI-based communication options for people with serious motor disabilities.

1Some of these EEG-based studies used software and analysis methods that were identical to those used here.

- Table 2 | Optimizing number of electrodes.

Accuracy (%) Bit rate (bits/min)

Number of Location(s) Flash sequences Flash sequences locations

1 2 3 1 2 3

1 C 53 75 78 28 41 38

- 1* C–A 75 91 93 50 57 51
- 2 C, A 81 94 96 56 60 54
- 3 C, B, A 86 96 98 62 63 56
- 4 E, C, B, A 86 96 100 62 63 59
- 5 E, D, C, B, A 87 97 100 63 64 59
- 6 F, E, D, C, B, A 86 96 100 62 63 59

This table shows the relationship between the number of electrodes over visual cortex and accuracy (left) or bit rate (right) that this subject can achieve with these electrodes at 1–3 flash sequences. The data in these tables corresponds to the traces in Figure 6; locations A–F correspond to the electrode locations and evoked responses in Figure 5.

*Bipolar derivation.

presentation/classification (i.e., the smallest possible number) and a dwell time (i.e., the time the subject sustained eye-gaze/attention) of as little as 0.75 s. While this dwell time compares favorably to what is used in other assistive devices (e.g., 0.6–1.0 s for a modern eye-tracker; Majaranta and Räihä, 2002), these other devices tend to provide higher communication performance. This is because the matrix spelling paradigm used here also requires a flight time during which the subject produces brain responses, the computer evaluates the responses, and the subject shifts gaze/attention to the next character. It appears impractical to further substantially decrease either the 2-s flight-time, or the 0.75-s dwell time. Thus, the paradigm presented here should be limited to a spelling rate that is only modestly higher than what we report here. This limitation appears to have two reasons. First, the current paradigm is synchronous, i.e., the subject has to synchronize his/her behavior with the timing of the BCI. This requires the subject to shift eye-gaze/ attention onto the intended character within the 2-s flight-time and to sustain eye-gaze/attention for the 0.75-s dwell time. One potential solution to overcome this limitation is an asynchronous paradigm, i.e., a paradigm in which the subject does not have to synchronize behavior with the system. SSVEP-based BCIs often use such asynchronous paradigms. In such a paradigm, the subject performs a selection by focusing eye-gaze on the target character (i.e., one of multiple light sources flickering at different frequencies) while the BCI detects those frequencies in the EEG recorded over occipital cortex (Middendorf et al., 2000). These paradigms not only overcome the synchronization requirement, they also permit stimulating each potential target independently for the whole dwell time (i.e., by using individual frequencies for each potential target). Using such a paradigm, Bin et al. (2009) reported 18.7 characters/ min for EEG. The use of this paradigm with ECoG may further increase performance.

The results suggest that ERPs over visual areas (VEPs) contribute significantly to the performance of the matrix speller BCI system. Recent studies (Bin et al., 2009; Martens et al., 2009) suggest that a time-, frequency-, and code-based stimulation may elicit a wide range of VEPs while minimizing the flight time and obtrusive flickering that currently limits the utility of P300- and SSVEP-based

BCIs. However, generation of a VEP depends on foveation of the target character. This is of critical relevance to clinical application of this BCI method, because eye movements are often impaired or lost in the target population. For example, although some people with ALS maintain residual eye movement for years (Cohen and Caroscio, 1983; Palmowski et al., 1995; Birbaumer and Cohen, 2007), others progress to near-complete or complete paralysis. The distance to foveation influences visual acuity and also VEP amplitude (Sherman, 1979; De Keyser et al., 1990) and thus would reduce the performance of any BCI that depends at least in part on VEPs.

An interesting finding was the polarity reversal of VEPs recorded from neighboring electrodes. While recording at the cortical surface (ECoG) can record these polarity-reversed VEPs, EEG recordings may only record the canceled superposition (Di Russo et al., 2002; Makeig et al., 2002). This cancellation effect may be one reason why the performance of EEG-based matrix speller systems, despite wider cortical coverage (e.g., 64 scalp locations of an extended 10–20 montage; Sharbrough et al., 1991), appears to be lower than that shown here.

While quite encouraging, the results shown here are based on only one subject who had coverage of large cortical areas including visual areas. Thus, it is currently unclear whether the results presented here will generalize to other subjects. Furthermore, while we were able to make general performance comparisons of this ECoGbased study with previously published EEG-based studies, we did not compare performance of ECoG and EEG within this subject.

The linear relationship between the flash duration and the accuracy, as well as the fact that only one electrode was sensitive to the orientation (i.e., row or column) of the attended flash, suggests that, in this particular subject, the magnitude of the ERP in response to visual stimulation was determined mostly by luminance. However, many previous studies have shown that the cortex performs neuronal processing of other features of visual stimuli, such as spatial frequency, orientation, motion, direction, speed, and many other spatiotemporal features (Hubel and Wiesel, 1959, 1962; Zeki et al., 1991). A recent study (Martens et al., 2009) showed that these properties of the visual system can be exploited to increase

the amplitude of the EEG response, and thereby increase overall classification accuracy. This suggests that more extensive electrode coverage may yield higher performance.

While in this study we only recorded signals from electrodes over the left hemisphere, it is known that visual cortex has bilaterally symmetric retinotopic maps (Engel et al., 1994, 1997; Yoshor et al., 2007). Thus, some of the ERPs may only reflect right visual field stimulation (Daniel and Whitteridge, 1961) and therefore bilateral coverage might further increase performance. As a related point, the electrode placement in this study was based solely on the requirements of the clinical evaluation, without any consideration of this study. Pre-surgical mapping of visual cortex using functional magnetic resonance imaging (fMRI;Engel et al., 1994, 1997; Vansteensel et al., 2010) could be used to optimize electrode location.

In this study we used subdural electrodes (i.e., electrodes placed underneath the dura mater). This placement requires penetration of the skull and the outer meningeal covering, i.e., the dura. This is important for clinical application of this BCI method, because the penetration of the dura increases the risk of bacterial infection (Davson, 1976; Hamer et al., 2002; Fountas and Smith, 2007; Van Gompel et al., 2008; Wong et al., 2009). Epidural electrodes (i.e., electrodes placed on top of the dura mater) provide signals of approximately comparable fidelity (Torres Valderrama et al., 2010) and do not penetrate the dura. Thus, epidural placement may increase safety and thus clinical practicality of an ECoG-based matrix speller BCI.

Success of wide-spread clinical application of ECoG-based matrix speller BCI systems depends mainly on costs and risks (Higson, 2002; Raab and Parr, 2006). The results presented in this paper are of critical relevance to these issues, because they suggest that effective ECoG-based matrix speller BCI systems may be realized by using only one bipolar and possibly epidural electrode.

Our results provide encouraging evidence that ECoG can provide high spelling rates, and recent results (Chao et al., 2010; Schalk, 2010) suggest that ECoG has good long-term stability. Moreover, an ECoG-based system reduces the patient’s dependence on a caregiver to set up EEG electrodes or other external conventional assistive devices. At the same time, the clinical value of an ECoG-based

matrix speller BCI remains unclear. Compared to non-invasive approaches, an ECoG-based approach entails additional costs and risks. More generally, despite some encouraging successes of noninvasive matrix spellers (Sellers et al., 2006; Nijboer et al., 2008), it is still unclear to what extent matrix spellers can serve the needs of people with disabilities, in particular those in whom eye-gaze is compromised: two recent studies (Brunner et al., 2010b; Treder and Blankertz, 2010) demonstrated that the performance of the matrix speller depends substantially on the subject’s ability to fixate the target character. It is also unclear whether similar fast stimulation rates (i.e., 16 Hz) can be used in people with disabilities. Even if the high speed suggested by this study could be translated to clinical applications, it is unclear to what extent end users will find this increased spelling rate desirable. Furthermore, it is currently unknown whether the added benefit of increased robustness and/ or increased spelling rate will outweigh the additional cost of surgical implantation. More generally, it is still debated whether people with complete paralysis can even achieve and maintain brain-based control, irrespective of whether EEG or ECoG is used (Hill et al., 2006; Kübler and Birbaumer, 2008).

In summary, the results shown in this study demonstrate that ECoG supports spelling performance exceeding 20 characters/min. In consequence, with additional verification in more subjects, our results may further extend the communication options for people with severe motor disabilities.

### acknowledgments

We are grateful to Drs. N. Jeremy Hill, Dennis J. McFarland, and Jonathan R. Wolpaw for their helpful comments. This work was supported by the NIH [EB006356 (Gerwin Schalk), EB00856 (Jonathan R. Wolpaw and Gerwin Schalk)], and the US Army Research Office [W911NF-07-1-0415 (Gerwin Schalk) and W911NF-08-1-0216 (Gerwin Schalk)].

### supplementary materIal

The Video 1 for this article can be found online at http://www. frontiersin.org/Neuroprosthetics/10.3389/fnins.2011.00005/ abstract

### references

Ball, T., Kern, M., Mutschler, I., Aertsen, A., and Schulze-Bonhage, A. (2009). Signal quality of simultaneously recorded invasive and non-invasive EEG. Neuroimage 46, 708–716.

Bin, G., Gao, X., Wang, Y., Hong, B., and Gao, S. (2009). VEP-based brain–computer interfaces: time, frequency, and code modulations [Research Frontier]. Comput. Intell. Mag. IEEE 4, 22–26. Birbaumer, N., and Cohen, L. G. (2007). Brain–computer interfaces: communication and restoration of movement in paralysis. J. Physiol. 579(Pt 3), 621–636.

Brunner, P., Joshi, S., Briskin, S., Wolpaw, J. R., Bischof, H., and Schalk, G. (2010a). “Does the P300 speller depend on eye gaze?” in Presentation at the TOBI Workshop, Graz.

Brunner, P., Joshi, S., Briskin, S., Wolpaw, J. R., Bischof, H., and Schalk, G. (2010b). Does the “P300” speller depend on eye gaze? J. Neural Eng. 7, 056013.

Brunner, P., Ritaccio, A. L., Lynch, T. M., Emrich, J. F., Wilson, J. A., Williams, J. C., Aarnoutse, E. J., Ramsey, N. F., Leuthardt, E. C., Bischof, H., and Schalk, G. (2009). A practical procedure for real-time functional mapping of eloquent cortex using electrocorticographic signals in humans.Epilepsy Behav. 15, 278–286.

Chao, Z. C., Nagasaka, Y., and Fujii, N. (2010). Long-term asynchronous decoding of arm motion using electrocorticographic signals in monkeys. Front. Neuroeng. 3:3. doi: 10.3389/ fneng.2010.00003

Cohen, B., and Caroscio, J. (1983). Eye movements in amyotrophic lateral

sclerosis. J. Neural. Transm. (Suppl. 19), 305–315.

Daniel, P. M., and Whitteridge, D. (1961). The representation of the visual field on the cerebral cortex in monkeys. J. Physiol. 159, 203–221.

Davson, H. (1976). Review lecture. The blood–brain barrier. J. Physiol. 255, 1–28.

De Keyser, M., Vissenberg, I., and Neetens, A. (1990). Are visually evoked potentials (VEP) useful for determination of visual acuity? A clinical trial. Neuroophthalmology, 10, 153–163. Di Russo, F., Martìnez, A., Sereno, M. I., Pitzalis, S., and Hillyard, S. A. (2002). Cortical sources of the early components of the visual evoked potential. Hum. Brain Mapp. 15, 95–111.

Donchin, E., and Arbel, Y. (2009). “P300 based brain computer interfaces: a

progress report,” inFAC ’09: Proceedings of the 5th International Conference on Foundations of Augmented Cognition. Neuroergonomics and Operational Neuroscience (Heidelberg: SpringerVerlag), 724–731.

Engel, S. A., Glover, G. H., and Wandell, B. A. (1997). Retinotopic organization in human visual cortex and the spatial precision of functional MRI.Cereb. Cortex 7, 181–192.

Engel, S. A., Rumelhart, D. E., Wandell, B. A., Lee, A. T., Glover, G. H., Chichilnisky, E. J., and Shadlen, M. N. (1994). fMRI of human visual cortex. Nature 369, 525.

Farwell, L. A., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523.

Felton, E. A., Wilson, J. A., Williams, J. C., and Garell, P. C. (2007). Electrocorticographically controlled brain–computer interfaces using motor and sensory imagery in patients with temporary subdural electrode implants. report of four cases. J. Neurosurg. 106, 495–500.

Fountas, K. N., and Smith, J. R. (2007). Subdural electrode-associated complications: a 20-year experience. Stereotact. Funct. Neurosurg. 85, 264–272.

Gao, X., Xu, D., Cheng, M., and Gao S. (2003). A BCI-based environmental controller for the motion-disabled. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 137–140.

Guger, C., Daban, S., Sellers, E., Holzner, C., Krausz, G., Carabalona, R., Gramatica, F., and Edlinger, G. (2009). How many people are able to control a P300-based brain–computer interface (BCI)? Neurosci. Lett. 462, 94–98. Hamer, H. M., Morris, H. H., Mascha, E. J., Karafa, M. T., Bingaman, W. E., Bej, M. D., Burgess, R. C., Dinner, D. S., Foldvary, N. R., Hahn, J. F., Kotagal, P., Najm, I., Wyllie, E., and Lüders, H. O. (2002). Complications of invasive video-EEG monitoring with subdural grid electrodes. Neurology 58, 97–103.

Higson, G. R. (2002). Medical Device Safety: The Regulation of Medical Devices for Public Health and Safety, 1st Edn. London: Taylor & Francis.

Hill, N. J., Lal, T. N., Schröder, M., Hinterberger, T., Wilhelm, B., Nijboer, F., Mochty, U., Widman, G., Elger, C., Schölkopf, B., Kübler, A., and Birbaumer, N. (2006). Classifying EEG and ECoG signals without subject training for fast BCI implementation: comparison of nonparalyzed and completely paralyzed subjects. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 183–186.

Hubel, D. H., and Wiesel, T. N. (1959). Receptive fields of single neurones in the cat’s striate cortex. J. Physiol. 148, 574–591.

Hubel, D. H., and Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat’s visual cortex. J. Physiol. 160, 106–154.

Jennrich, R. I. (1977).Stepwise Regression. New York: John Wiley and Sons, 58–75.

Krusienski, D. J., Sellers, E. W., Cabestaing, F., Bayoudh, S., McFarland, D. J., Vaughan, T. M., and Wolpaw, J. R. (2006). A comparison of classification techniques for the P300 Speller.J. Neural Eng. 3, 299–305.

Kübler, A., and Birbaumer, N. (2008). Brain–computer interfaces and

communication in paralysis: extinction of goal directed thinking in completely paralysed patients? Clin. Neurophysiol. 119, 2658–2666.

Lenhardt, A., Kaper, M., and Ritter, H. J. (2008). An adaptive P300-based online brain–computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 16, 121–130.

Leuthardt, E. C., Miller, K. J., Schalk, G., Rao, R. P., and Ojemann, J. G. (2006). Electrocorticography-based brain computer interface–the Seattle experience.IEEE Trans. Neural Syst. Rehabil. Eng. 14, 194–198.

Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., and Moran, D. W. (2004). A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1, 63–71.

Majaranta, P., and Räihä, K. J. (2002). “Twenty years of eye typing: systems and design issues,” in ETRA ’02: Proceedings of the (2002). Symposium on Eye Tracking Research and Applications (New York, NY: ACM), 15–22.

Makeig, S., Westerfield, M., Jung, T. P., Enghoff, S., Townsend, J., Courchesne, E., and Sejnowski, T. J. (2002). Dynamic brain sources of visual evoked responses. Science 295, 690–694.

Martens, S. M., Hill, N. J., Farquhar, J., and Schölkopf, B. (2009). Overlap and refractory effects in a brain–computer interface speller based on the visual P300 event-related potential.J. Neural Eng. 6, 026003–026003.

McFarland, D. J., Sarnacki, W. A., and Wolpaw, J. R. (2003). Brain–computer interface (BCI) operation: optimizing information transfer rates. Biol. Psychol. 63, 237–251.

Mellinger, J., and Schalk, G. (2007). “BCI2000: A general-purpose software platform for BCI,” in Toward Brain–Computer Interfacing, eds G. Dornhege, J. del R. Millan, T. Hinterberger, D. McFarland, and K. Müller (Cambridge: MIT Press), 359–367.

Middendorf, M., McMillan, G., Calhoun, G., and Jones, K. S. (2000). Brain–computer interfaces based on the steady-state visual-evoked response. IEEE Trans. Rehabil. Eng. 8, 211–214.

Miller, K. J., Leuthardt, E. C., Schalk, G., Rao, R. P., Anderson, N. R., Moran, D. W., Miller, J. W., and Ojemann, J. G. (2007). Spectral changes in cortical surface potentials during motor movement. J. Neurosci. 27, 2424–2432. Miller, K. J., Schalk, G., Fetz, E. E., den Nijs, M., Ojemann, J. G., and Rao, R. P. (2010). Cortical activity during motor execution, motor imagery, and image-

ry-based online feedback. Proc. Natl. Acad. Sci. U.S.A. 107, 4430–4435. Miller, K. J., Shenoy, P., den Nijs, M., Sorensen, L. B., Rao, R. N., and Ojemann, J. G. (2008). Beyond the gamma band: the role of highfrequency features in movement classification.IEEE Trans. Biomed. Eng. 55, 1634–1637.

Müller, K. R., Tangermann, M., Dornhege, G., Krauledat, M., Curio, G., and Blankertz, B. (2008). Machine learning for real-time single-trial EEG-analysis: from brain–computer interfacing to mental state monitoring. J. Neurosci. Methods 167, 82–90.

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., Halder, S., Mochty, U., Krusienski, D. J., Vaughan, T. M., Wolpaw, J. R., Birbaumer, N., and Kübler, A. (2008). A P300-based brain–computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916.

Palmowski, A., Jost, W. H., Prudlo, J., Osterhage, J., Käsmann, B., Schimrigk, K., and Ruprecht, K. W. (1995). Eye movement in amyotrophic lateral sclerosis: a longitudinal study. Ger. J. Ophthalmol. 4, 355–362.

Pfurtscheller, G., Neuper, C., Müller, G. R., Obermaier, B., Krausz, G., Schlögl, A., Scherer, R., Graimann, B., Keinrath, C., Skliris, D., Wörtz, M., Supp, G., and Schrank, C. (2003). Graz-BCI: state of the art and clinical applications.IEEE Trans. Neural Syst. Rehabil. Eng. 11, 177–180.

Raab, G. G., and Parr, D. H. (2006). From medical invention to clinical practice: the reimbursement challenge facing new device procedures and technology–part 2: coverage. J. Am. Coll. Radiol. 3, 772–777.

Reitan, R. M. (1958). Validity of the trail making test as an indicator of organic brain damage. Percept. Mot. Skills 8, 271–276.

Ritaccio, A. L., Brunner, P., Cervenka, M. C., Crone, N., Guger, C., Leuthardt, E. C., Oostenveld, R., Stacey, G., and Schalk, G. (2010). Proceedings of the first international workshop on advances in electrocorticography. Epilepsy Behav. 19, 204–215.

Schalk, G. (2008). Brain–computer symbiosis. J. Neural Eng. 5, 1–15.

Schalk, G. (2010). Can Electrocorticography (ECoG) support robust and powerful brain–computer interfaces? Front. Neuroeng. 3:9. doi: 10.3389/ fneng.2010.00009

Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw, J. R. (2004). BCI2000: a general-purpose brain–computer interface (BCI) sys-

tem. IEEE Trans. Biomed. Eng. 51, 1034–1043.

Schalk, G., and Mellinger, J. (2010). A Practical Guide to Brain–Computer Interfacing with BCI2000, 1st Edn. London: Springer.

Schalk, G., Miller, K. J., Anderson, N. R., Wilson, J. A., Smyth, M. D., Ojemann, J. G., Moran, D. W., Wolpaw, J. R., and Leuthardt, E. C. (2008). Twodimensional movement control using electrocorticographic signals in humans. J. Neural Eng. 5, 75–84.

Sellers, E. W., Krusienski, D. J., McFarland, D. J., Vaughan, T. M., and Wolpaw, J. R. (2006). A P300 event-related potential brain–computer interface (BCI): the effects of matrix size and inter stimulus interval on performance. Biol. Psychol. 73, 242–252.

Sellers, E. W., Kübler, A., and Donchin, E. (2006). Brain–computer interface research at the University of South Florida Cognitive Psychophysiology Laboratory: the P300 Speller. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 221–224.

Sellers, E. W., Vaughan, T. M., and Wolpaw, J. R. (2010). A brain–computer interface for long-term independent home use. Amyotroph Lateral Scler. 11, 449–455.

Serby, H., Yom-Tov, E., and Inbar, G. F. (2005). An improved P300-based brain–computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 13, 89–98.

Sharbrough, F., Chatrian, G. E., Lesser, R. P., Luders, H., Nuwer, M., and Picton, T. W. (1991). American Electroencephalographic Society guidelines for standard electrode position nomenclature.Electroencephalogr. Clin. Neurophysiol. 8, 200–202.

Sherman, J. (1979). Visual evoked potential (VEP): basic concepts and clinical applications. J. Am. Optom. Assoc. 50, 19–30.

Talairach, J., and Tournoux, P. (1988). Co-Planar Sterotaxic Atlas of the Human Brain. New York: Thieme Medical Publishers, Inc.

Torres Valderrama, A., Oostenveld, R., Vansteensel, M. J., Huiskamp, G. M., and Ramsey, N. F. (2010). Gain of the human dura in vivo and its effects on invasive brain signal feature detection. J. Neurosci. Methods 187, 270–279. Treder, M. S., and Blankertz, B. (2010). (C)overt attention and visual speller design in an ERP-based brain– computer interface. Behav. Brain Funct. 6, 28.

Van Gompel, J. J., Worrell, G. A., Bell, M. L., Patrick, T. A., Cascino, G. D., Raffel, C., Marsh, W. R., and Meyer, F. B. (2008). Intracranial electroencephalography with subdural grid

electrodes: techniques, complications, and outcomes. Neurosurgery 63, 498–505.

Vansteensel, M. J., Hermes, D., Aarnoutse, E. J., Bleichner, M. G., Schalk, G., van Rijen, P. C., Leijten, F. S., and Ramsey, N. F. (2010). Brain–computer interfacing based on cognitive control. Ann. Neurol. 67, 809–816.

Vaughan, T. M., McFarland, D. J., Schalk, G., Sarnacki, W. A., Krusienski, D. J., Sellers, E. W., and Wolpaw, J. R. (2006). The Wadsworth BCI Research and Development Program: at home with BCI.IEEE Trans. Neural Syst. Rehabil. Eng. 14, 229–233.

Wechsler, D. (1997). Weschsler Adult Intelligence Scale-III. Antonio, TX: The Psychological Corporation.

Wilson, J. A., Felton, E. A., Garell, P. C., Schalk, G., and Williams, J. C. (2006). ECoG factors underlying multimodal control of a brain–computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 246–250.

Wolpaw, J. R., McFarland, D. J., Neat, G. W., and Forneris, C. A. (1991). An EEG-based brain-computer interface for cursor control.Electroencephalogr. Clin. Neurophysiol. 78, 252–259.

Wong, C. H., Birkett, J., Byth, K., Dexter, M., Somerville, E., Gill, D., Chaseling, R., Fearnside, M., and Bleasel, A. (2009). Risk factors for complications during intracranial electrode recording in presurgical evaluation of drug resistant partial epilepsy.Acta Neurochir. (Wien) 151, 37–50.

Yoshor, D., Bosking, W. H., Ghose, G. M., and Maunsell, J. H. (2007). Receptive fields in human visual cortex mapped with surface electrodes. Cereb. Cortex 17, 2293–2302.

Zeki, S., Watson, J. D., Lueck, C. J., Friston, K. J., Kennard, C., and Frackowiak, R. S. (1991). A direct demonstration of functional specialization in human visual cortex.J. Neurosci. 11, 641–649.

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Received: 25 June 2010; paper pending published: 07 September 2010; accepted:

06 January 2011; published online: 07 February 2011. Citation: Brunner P, Ritaccio AL, Emrich JF, Bischof H and Schalk G (2011) Rapid communication with a “P300” matrix speller using electrocorticographic signals (ECoG). Front. Neurosci.5:5. doi: 10.3389/ fnins.2011.00005 This article was submitted to Frontiers in Neuroprosthetics, a specialty of Frontiers in Neuroscience. Copyright © 2011 Brunner, Ritaccio, Emrich, Bischof and Schalk. This is an open-access article subject to an exclusive license agreement between the authors and Frontiers Media SA, which permits unrestricted use, distribution, and reproduction in any medium, provided the original authors and source are credited.

