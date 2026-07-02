# Prediction of Three-Dimensional Arm Trajectories Based on ECoG Signals Recorded from Human Sensorimotor Cortex

Yasuhiko Nakanishi1., Takufumi Yanagisawa2,3,4., Duk Shin1*, Ryohei Fukuma3, Chao Chen1, Hiroyuki Kambara1, Natsue Yoshimura1, Masayuki Hirata2, Toshiki Yoshimine2, Yasuharu Koike1

1 Precision and Intelligence Laboratory, Tokyo Institute of Technology, Yokohama, Japan, 2 Department of Neurosurgery, Osaka University Medical School, Osaka, Japan, 3 ATR Computational Neuroscience Laboratories, Kyoto, Japan, 4 Division of Functional Diagnostic Science, Osaka University Graduate School of Medicine, Osaka, Japan

|Abstract<br><br>Brain-machine interface techniques have been applied in a number of studies to control neuromotor prostheses and for neurorehabilitation in the hopes of providing a means to restore lost motor function. Electrocorticography (ECoG) has seen recent use in this regard because it offers a higher spatiotemporal resolution than non-invasive EEG and is less invasive than intracortical microelectrodes. Although several studies have already succeeded in the inference of computer cursor trajectories and finger flexions using human ECoG signals, precise three-dimensional (3D) trajectory reconstruction for a human limb from ECoG has not yet been achieved. In this study, we predicted 3D arm trajectories in time series from ECoG signals in humans using a novel preprocessing method and a sparse linear regression. Average Pearson’s correlation coefficients and normalized root-mean-square errors between predicted and actual trajectories were 0.44,0.73 and 0.18,0.42, respectively, confirming the feasibility of predicting 3D arm trajectories from ECoG. We foresee this method contributing to future advancements in neuroprosthesis and neurorehabilitation technology.<br><br>Citation: Nakanishi Y, Yanagisawa T, Shin D, Fukuma R, Chen C, et al. (2013) Prediction of Three-Dimensional Arm Trajectories Based on ECoG Signals Recorded from Human Sensorimotor Cortex. PLoS ONE 8(8): e72085. doi:10.1371/journal.pone.0072085<br><br>Editor: Maurice Ptito, University of Montreal, Canada Received April 18, 2013; Accepted July 4, 2013; Published August 21, 2013 Copyright: 2013 Nakanishi et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.<br><br>Funding: This work was supported in part by KAKENHI grants (22390275, 23390347, and 24700419) from the Japan Society for the Promotion of Science (JSPS). A part of this study was the result of ‘‘Brain Machine Interface Development’’ carried out under the Strategic Research Program for Brain Sciences by the Ministry of Education, Culture, Sports, Science and Technology of Japan. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.<br><br>Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: shinduk@cns.pi.titech.ac.jp<br><br>. These authors contributed equally to this work.|
|---|

Introduction

A number of prominent brain-machine interface studies have arisen, in which electroencephalography (EEG), magnetoencephalography (MEG), electrocorticography (ECoG), and intracortical microelectrode have been applied to neuroprosthesis control, neurorehabilitation and novel communication tools for paralyzed or ‘‘locked–in’’ patients suffering from neuromuscular disorders. Since EEG and MEG are non-invasive and have high temporal resolution, they have been used in various paradigms, such as online control of a computer cursor [1–2], direction inference of hand movements [3–5], operation of a spelling device [6], and neurofeedback for rehabilitation [7–13]. Although a large proportion of these non-invasive methods succeeded in classification of movement direction or intention, prediction of timevarying trajectories is likely difficult due to insufficient spatial resolution and low signal-to-noise ratio in such methods.

Signal recording with intracortical microelectrodes is a powerful tool to realize precise trajectory prediction or accurate device control. Using motor cortical signals in animals, studies have shown successful prediction of hand trajectories [14–16] and grasp types and velocity [17], control of a computer cursor [18] or a robot arm [19–22], and controlled stimulation to a paralyzed arm

[23]. These techniques have also been applied in humans to control a cursor [24] and a virtual keyboard and virtual hand [25]. However, though intracortical electrodes can provide rich information for BMI control, they face limitations such as signal degradation due to glial scarring [26]and potential displacement from the recording site [27].

Conversely, ECoG is less invasive than microelectrodes and can offer higher spatial resolutions than EEG and MEG. Researchers have been applying ECoG in humans for several years now and in numerous applications. The classification of hand movement directions or grasp types [28–33], one-, two-, or three-dimensional cursor control [27,34–40], and prediction of finger flexion [41] are just some examples of ECoG applications in human patients. Studies concerning the prediction of three-dimensional (3D) trajectory or muscle activities from primate ECoG have shown outstanding results [42–45]. Investigations on the prediction of 3D arm trajectory using ECoG in humans, however, are lacking, despite the potential to provide significant improvement in neuroprosthesis and neurorehabilitation technology. The inadequate quality of ECoG signals recorded from patients is one potential obstacle in predicting 3D trajectories. Specifically, (1) paralyzed or elderly patients may find it difficult to perform a long series of repeating trials and stably replicate the same motion for

Table 1. Clinical profiles in patients who participated in this study.

No. Age Sex Diagnosis (Left/Right) Duration of disease Paresis (MMT) Sensation

- 1 64 yr. Male Thalamic hemorrhage (R) 7 yr. Spastic (4) Hypoesthesia
- 2 65 yr. Male Ruptured spinal dural arteriovenous fistula 8 yr. Spastic (4) Hypoesthesia
- 3 14 yr. Male Intractable epilepsy (R) 7 yr. None Normal

doi:10.1371/journal.pone.0072085.t001

each trial, (2) ECoG signals in patients can include pathological activity, depending on the condition, and (3) the electrode sites on the cortex and the recording lengths can differ, depending on the treatment.

The aim of this study was to predict 3D arm trajectories from ECoG time series in human patients as a basis for a neuroprosthesis. Patients diagnosed with thalamic hemorrhage, ruptured spinal dural arteriovenous fistula (dAVF) and intractable epilepsy executed rotating tasks with three objects on a table. We simultaneously recorded arm trajectories and ECoG signals from 15,60 electrodes on the sensorimotor cortex. Using a novel method, we predicted four joint angles for the shoulder and elbow joints and six coordinates for the elbow and wrist joints in patients with different pathology.

Materials and Methods Ethics Statement

The study was approved by the ethics committee of Osaka University Hospital (Approval No.08061) and conducted in accordance with the Declaration of Helsinki. ECoG electrodes were embedded not for our experiments but for patients’ medical treatments. Written informed consent was obtained before initiating any research procedures. All patients or their guardians gave written informed consent for the use of their data in the academic study.

Participants

Three patients (males; 14–64 years) participated in our study (Table 1). Patients 1 and 2 had spastic paresis and weakness in the left arm due to stroke. Their sensorimotor cortices were undamaged, though moderate motor dysfunction was observed. The youngest participant, patient 3, was diagnosed with intractable epilepsy but did not show motor dysfunction. As part of their treatments, all participants were implanted with subdural electrode arrays (Unique Medical Co., Tokyo, Japan) covering the sensorimotor cortex, including the central sulcus. The arrays remained implanted in the intracranium for two weeks to determine the optimum site for effective pain reduction (patients

- 1 and 2) or epileptic foci localization (patient 3).

Behavioral Tasks

Patients executed the tasks in an electromagnetically shield room approximately one week after electrode implantation. All patients were seated upright on a chair at a table and were asked to perform the tasks using their left hands. Patient 1 repositioned three blocks around a 25 cm 625 cm square one by one and in a clockwise fashion (green arrows in Figure 1). He moved his hand to the first block (a rectangular parallelepiped in Figure 1), grasped it, carried it to the vacant corner of the square, and released it. Next,

he moved the second block (a cube) to the corner vacated by the rectangular parallelepiped. Finally, he moved the third block (a cylinder) to the corner vacated by the cube. When all objects had been moved to the next corner once, a cycle of hand motion was completed. Patient 1 regularly repeated nine cycles in session 1 and eleven cycles in session 2. Patient 2 also carried the three blocks to vacant corners of the square, but he randomly chose one block among the three to move. Patient 2 performed similar arm movements 19 and 20 times for sessions 1 and 2, respectively. Patient 3 chose one of three blocks and placed it at an arbitrary position on the table. He performed 18, 31, and 24 movements in sessions 1, 2 and 3, respectively. We instructed patients to perform the tasks at their own pace. Each session started just after an audio cue, delivered through a speaker controlled with a MATLAB R2007b (Mathworks, Inc., Natick, MA, USA) script, and

Figure 1. Behavioral tasks. Patient 1 repositioned three blocks one by one and clockwise (green arrows ) at the corners of a 25 cm 6 25 cm square. ECoG signals were obtained with planarsurface platinum grid electrodes placed on the right sensorimotor cortex. Half-closed circles on the left shoulder, elbow, and wrist joints represent three-dimensional markers for the motion capture system. The angles q1, q2, q3, and q4 are defined as an abduction/adduction angle, a flexion/extension angle, an external/internal rotation at the left shoulder joint, and a flexion/extension angle at the left elbow joint, respectively. When he lowered his arm toward the -z direction and turned his palm to the y direction with the elbow extended, q1, q2, and q3 were all zero, and q4 was p radians. doi:10.1371/journal.pone.0072085.g001

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

## Figure 2. Electrodes placed on the sensorimotor cortex of patient 1. (A) Positions of the electrodes (circles). (B) Two 5 66 electrode arrays were placed on the right hemisphere, covering the sensorimotor cortex. Yellow lines depict the right central sulcus.

- doi:10.1371/journal.pone.0072085.g002

Figure 3. ECoG signal processing and decoding method. (A) Raw ECoG signals from channels 1, 2, and 27 are shown as typical examples. (B) The ECoG signal of channel 27 was divided into seven frequency components (d,h, …, c 2) with bandpass filters (black lines). These seven filtered signals were digitally rectified, smoothed with a low-pass filter, and down-sampled to 100 Hz. The band-passed ECoG signals were then z-score normalized (red lines). The linear relationship betweenthepast1 sofnormalizedECoG(light-bluearea;t,t-jDt,j=1,2,…,100,Dt=0.01 s,i.e.,100samplingpoints)andacoordinatex,y,orzatthepresentt(tiny yellow boxes) was determined using sparse linear regression. Once weight coefficients were obtained through training, construction of the decoder was complete.

- doi:10.1371/journal.pone.0072085.g003

| | | |[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>[Figure 17]<br><br>[Figure 18]| | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

[Figure 19]

- Figure 4. Color-map of the normalized ECoG signals and coordinates at the left wrist joint. Signals were obtained from channels 1,30 in session 2 of patient 1(channels 31,60 are not shown). This session includes 11 cycles. We treated each cycle as an independent trial.Start and end points were respectively defined as the instances where tangential velocity of the arm exceeded or fell below 5% of maximum velocity. Unused sampling points are colored yellow (yellow vertical lines). Precise wave forms of z-score on channel 27 inside of a red rectangle were already displayed in detail in Figure 3.

- doi:10.1371/journal.pone.0072085.g004

continued for 180 seconds. We excluded 20 trials in which patient

- 2 moved more than 20 cm sagittally because his torso swung forward and backward during the tasks. The abovementioned tasks included several actions, i.e., reaching, grasping, carrying and releasing, which are basic and indispensable actions for daily life.

ECoG Signals and Motion Recordings

Patients 1 and 2 were implanted with two 566 electrode arrays, and patient 3 was implanted with a 365 array. The planar-surface platinum grid electrodes had a diameter of 3 mm and an interelectrode distance of 7 mm, as shown in Figure 2. The number of electrodes was 60 for patients 1 and 2, and 15 for patient 3. ECoG signals were recorded inside an electromagnetically shielded room with a 128-channel digital EEG system (EEG 2000; Nihon Koden Corporation, Tokyo, Japan) set at a sampling rate of 1000 Hz. All electrodes were referenced to a scalp electrode on the nasion of each patient. Figure 2A shows electrodes placed on the cortex of patient 1.

3D arm motions were recorded at a sampling rate of 100 Hz with an optical motion capture system (Eagle Digital System; Motion Analysis Corporation, Santa Rosa, CA) using reflecting

- 3D markers shaped in 6 mm-diameter spheroids to identify the left shoulder, left elbow, and left wrist joint positions (Figure 1). The frame lengths of images available for leave-one-out crossvalidation (LOO-CV) were as follows: 180 seconds for each session by patient 1, 120 seconds for each session by patient 2, and 90, 180 and 120 seconds for sessions 1, 2, and 3 by patient 3, respectively. Frame lengths differed between patients and sessions since the 3D markers occasionally went out of the field of view or were occluded by the patient’s body. The start of ECoG and motion capture recordings was time-locked to the cue signal.

ECoG Signal Processing

ECoG signals were pre-processed with our previously proposed method [44]. Firstly, the signal data sampled at 1000 Hz were rereferenced with a common average reference (CAR) and divided into seven frequency bands (d : ,4 Hz, h : 4,8 Hz, a: 8,14 Hz, b 1:14,20 Hz, b 2:20,30 Hz, c 1:30,50 Hz, and c 2:50,90 Hz) using fourth-order bandpass Butterworth filters (Figure 3). Secondly, these band-passed signals were digitally rectified and smoothed with a second-order low-pass filter (cut-off frequency: 2.2 Hz), which changed high oscillations into low frequency features. Thirdly, the signals were down sampled to 100 Hz, i.e., the sampling rate of the motion capture recordings. Finally, the obtained signals xi(t) (i=1, 2, …, n 7) at time t were normalized to the standard z-score zi(t) as follows (red lines in Figure 3B).

xi(t){mi si

zi(t)~

(i~1,2, ..., n|7) ð1Þ

where mi, si and n denote the mean value of xi(t), the standard deviation of xi(t), and the number of ECoG channels, respectively. These z-scores calculated from ECoG signals were utilized as training data to construct a decoder.

Decoding Method

The value of an angle or a coordinate Yp(t) at a present time t was predicted with the following linear equation:

Yp(t)~Xn|7 i~1

j~1

Xm

wijzi(t{jDt)zw0 ð2Þ

where Dt and m denote time-step and the number of consecutive sampling points before the present time t used to predict Yp at t, respectively. In this study, we assigned 100 points and 0.01 seconds to m and Dt, respectively. w0 and wij are, respectively, a bias term and a weight coefficient to the i-th filtered ECoG signal zi at time tjDt (Figure 3B). We applied a Bayesian algorithm called sparse linear regression [44,46–49] to determine values of the weights wij.

Each session was segmented into 9,31 trials. Figure 4 shows zscores and coordinates x, y and z at the wrist joint in session 2 of patient 1. In this example, the session was divided into 11 trials. We defined the starting point of each trial as the instance when tangential velocity at the elbow joint exceeded 5% of the maximum velocity in the trial. The end point of each trial was decided in a similar manner, i.e., the instance when tangential velocity decreased to less than 5% of maximum. In Figure 4, unused data between the k-th ending point and the k+1-th starting point are colored over with yellow (yellow vertical lines).

We verified the validity of our method using LOO-CV. Firstly, a decoder was constructed using filtered ECoG signals and actual arm position or actual joint angle in all trials except the k-th trial, which was used as test data. The weight coefficients wij were obtained from this training. Iterations of the sparse linear regression were terminated just before over-training. Secondly, an arm trajectory Yp in the k-th trial was predicted with the decoder. Pearson’s correlation coefficient (CC) and the normalized root-mean-square error (nRMSE) were obtained by comparing Yp and Yact of the k-th test trial. Thirdly, the abovementioned training and testing phases were repeatedly executed using different trials for k (Figure 4, k=1, 2, …, 11). Finally the CC and nRMSE values were averaged across all trials.

[Figure 20]

- Figure 5. Examples of the predicted (red lines) and actual 3D trajectories (blue lines). A part of the 10th trial (6 s) in session 2 of patient 1 is shown (see Video S1). Markers (circles, triangles, squares, and diamonds) represent 2 s time intervals. Circles and diamonds indicate the earliest and the latest positions, respectively. The red trajectories were computed using predicted data q1,q4 and patient 19s actual arm length. The timings (positions of the markers) and trajectory curves of the predicted data were similar to those of the actual data.

- doi:10.1371/journal.pone.0072085.g005

Results Reconstruction of Angles and Positions

Movement duration average and standard deviations across 20 trials for patient 1 was 17.1762.76 s, indicating that his motion in each trial was non-uniform (see Fig. S1). Figure 5 is an example of the comparison between predicted (red lines) and actual 3D trajectories (blue lines) for six seconds in the 10th trial of session 2 by patient 1. The red lines were drawn using inferred joint angles q1, q4 and the patient’s arm length. Figure 6 shows predicted joint angles (red lines in the left column) and joint positions (red lines in the center and right columns) in comparison with actual measurements (blue lines) in the 10th trial of session 2 as typical plots by patient 1 (Figure 4). In this trial, it took 15.1 s to move all three blocks to the next open corners of the square. Most blue lines have curvatures with three peaks representing the three block moving tasks. The timings of the peaks differed between q2 and q3

indicated by green arrows. The predicted red lines fit the peaks at various timings, even though the ECoG signals utilized for the prediction were common between q2 and q3. The traces for q1, z at the elbow, and z at the wrist have narrow variation ranges and many peaks, in contrast to those of the other joint angles/ coordinates. The ranges of CC and nRMSE for joint angles (left column in Figure 6) were 0.57,0.88 and 0.13,0.40, respectively. The flexion/extension angle q2 at the left shoulder showed the best result. CC and nRMSE for joint coordinates (middle and right columns) were 0.48,0.82 and 0.16,0.30, respectively. The y coordinate values at the elbow were relatively greater than those of the other coordinates. Both q2 and y at elbow showed wider ranges of variation than the others.

Average CC and average nRMSE of the three patients are summarized in Figure 7. The best average CC and nRMSE among joint angles were 0.7160.026 and 0.2360.010 (mean 6 SEM), respectively, corresponding to angle q2 for patient 1. The

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

- Figure 6. Examples of predicted joint angles and positions in time series. Blue lines are actual recoded joint angles (left column), and actual positions at the left elbow (center column) and left wrist joint (right column) in the 10th trial shown in Figure 3 and Figure 4. The joint angles and coordinates predicted with sparse linear regression are plotted in red. The Pearson’s correlation coefficient (CC) and the normalized root-mean-square error (nRMSE) are shown at the top of each graph.

- doi:10.1371/journal.pone.0072085.g006

best average CC and nRMSE among joint coordinates were 0.7360.022 and 0.1860.0071, respectively, corresponding to the z coordinate of the left wrist for patient 1.

To judge whether performance of the proposed method differed significantly between patients, a two-way ANOVA with Tukey’s multiple-comparison test was conducted to analyze the effects of two factors (patients and joint angles; patients and joint coordination). The 2-way interaction did not show any significance. Significant differences were observed among the patients (joint angle: F2, 436 =82.46, p,0.001; coordination: F2, 654 =117.56, p,0.001), whereas significant differences were not observed among joint angles and joint coordination. The CC values of both patients 1 and 2 were significantly higher than those of patient 3. The nRMSE values for patient 3 were also significantly higher than those of the other patients (joint angle: F2, 436 =10.42, p,0.05; coordination: F2, 654 =41.14, p,0.01). This may be interpreted such that the proposed method is more suitable for patients 1 and 2 than for patient 3.

Frequency Components Contributing to Reconstruction of Arm Trajectory

3D hand trajectories were predicted using each sensorimotor rhythm, one by one. The results averaged across 20 trials for patient 1 are shown in Figure 8. A two-way ANOVA was employed to judge two effects (seven sensorimotor frequency bands and four joint angles or six coordinations). Among the 2way interactions, only elbow coordination showed significance (joint angle: F18, 532 =1.07, p=0.38; elbow coordination: F12, 399 =1.86, p=0.04; wrist coordination: F12, 399=1.4, p=0.16). Significant differences were observed among the sensorimotor frequency bands (joint angle: F6, 532=27.26, p,0.001; elbow coordination: F6, 399=33.67, p,0.001; wrist coordination: F6, 399=43.58, p,0.001), as shown in figure 8. The CC values of the d and c2 bands were significantly higher than those of the other bands.

- Figure 7. Prediction results for all patients. Averaged correlation coefficients (CC) for joint angle (A) and x, y, z coordination (B), and the normalized root-mean-square error (nRMSE) for joint angles (C) and x, y, z coordination (D) were obtained using LOO-CV on 20, 19 and 73 trials for patients 1, 2, and 3 (blue, red, and green bars), respectively.

- doi:10.1371/journal.pone.0072085.g007

Discussion

We predicted 3D arm trajectory in humans based on ECoG signals divided into seven frequency bands using a sparse linear regression method. Although two-dimensional (2D) cursor trajectories on a display have been precisely predicted using ECoG signals obtained from patients in several studies [35,37–38], to the best of our knowledge, inference of 3D trajectory for the human arm using ECoG has not been previously presented.

We inferred both joint angles (q1, q4) and joint positions (x, y and z) to reconstruct 3D trajectory and obtained acceptable prediction accuracies in both cases. Our average CC and nRMSE were 0.44,0.73 and 0.18,0.42, respectively, excluding patient 3. In the previous studies on 2D cursor trajectories with humans,

average CC were approximately 0.22,0.71 for Schalk et al. (2007) (with the average across positions and velocities for the best participant being 0.62) [35], 0.3,0.6 for Pistohl et al. (2008) [37], and 0.52,0.87 for Gunduz et al. (2009) [38]. Kubanek et al. (2009), who predicted individual finger flexions, showed an average CC of 0.23 (little finger) , 0.75 (thumb) (CC averaged across all fingers and participants was 0.52) [41]. Our results were not inferior to the aforementioned studies, especially considering the higher dimensionality of trajectory data.

The prediction accuracy for patient 3 was significantly worse than that of the other patients. His average CC and nRMSE were 0.13,0.38 and 0.28,0.52, respectively. We suggest the following as possible causes for this result: (1) ECoG signal quality; There were obvious disturbances or noise in his ECoG signals which

- Figure 8. Contribution of each frequency band for trajectory prediction. Each panel (A: joint angles; B: xyz coordinates of the elbow; C: xyz coordinates of the wrist) shows the results of prediction using each sensorimotor rhythm, one by one. Noteworthy significant differences between CC values of frequency bands are marked with * (p,0.05) and ** (p,0.001). Other significance comparisons are omitted for visualization purposes.

- doi:10.1371/journal.pone.0072085.g008

could be discerned through visual inspection. The baselines of his ECoG signals also randomly and widely fluctuated. (2) Electrode number; Patient 3 had only 15 electrodes placed around his central sulcus, whereas the other patients had 60 electrodes. (3) Pathology; Patient 3 had epilepsy while the others did not. (4) Task properties; He was allowed to place the blocks at arbitrary places on the table. He decided their positions impromptu, in contrast to the other participants who placed their blocks at fixed positions. We suggest that much more training data are necessary for the prediction of motions involving various postures such as those in the data of patient 3.

Joint angle q1 could not be predicted precisely, in contrast to q2,q4 (Figure 7A and 6C). The range of abduction/adduction for q1 was the narrowest among all angles, as shown in the left column of Figure 6. We presume that it was difficult to extract the faint component correlating with this small fluctuation from ECoG as a summation of various signals.

The high frequency band c2 (50,90 Hz) had relatively high CC values (Figure 8). Several papers also reported that high frequency bands of ECoG were important for prediction, such as 40,80 Hz for cursor trajectory prediction in humans [37], 80,150 Hz for the classification of human hand movements [31], 40,90 Hz for 3D hand trajectory prediction in monkeys [43], and 50,90 Hz for EMG prediction in monkeys [44]. The low frequency band d (,4 Hz) had the highest values among the seven bands in this study. This was also supported by previous works [32,37] which reported that the low frequency band ECoG (2,6 Hz; with band-pass filter) and low frequency component (LFC) (,5 Hz; with Savitzky-Golay smoothing filter) were important for classifying different grasp types [32].

We verified that 3D arm trajectories in patients of different pathology could be predicted with our proposed method using a sparse linear regression. We foresee this method contributing to further studies and further improvements in neuroprostheses and neurorehabilitation.

Supporting Information

Figure S1 Actual position at the wrist joint for patient 1. Coordinates x, y, and z of all 20 trials are shown. Motion of patient 1 was non-uniform, with duration and timing differing between trials. (EPS)

Video S1 Examples of the predicted arm positions of patient 1. Blue and red lines are actual and predicted arm positions in the 10th trial of session 2, respectively. (MOV)

Acknowledgments

We thank the participants for their commitment and effort for this study. We thank the contribution and support from clinicians and researchers at the Osaka University Hospital. We thank also C. S. DaSalla for proofreading the manuscript.

Author Contributions

Conceived and designed the experiments: T. Yanagisawa MH T. Yoshimine. Performed the experiments: T. Yanagisawa MH RF T. Yoshimine. Analyzed the data: YN DS. Contributed reagents/materials/analysis tools: YN DS CC HK NY YK. Wrote the paper: YN T. Yanagisawa DS.

References

- 1. Wolpaw JR, McFarland DJ, Neat GW, Forneris CA (1991) An EEG-based brain-computer interface for cursor control. Electroencephalogr Clin Neurophysiol 78: 252–259.
- 2. Wolpaw JR, McFarland DJ (2004) Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. Proc Natl Acad Sci U S A 101: 17849–17854.
- 3. Blankertz B, Dornhege G, Schafer C, Krepki R, Kohlmorgen J, et al. (2003) Boosting bit rates and error detection for the classification of fast-paced motor commands based on single-trial EEG analysis. IEEE Trans Neural Syst Rehabil Eng 11: 127–131.
- 4. Blankertz B, Dornhege G, Krauledat M, Muller KR, Kunzmann V, et al. (2006) The Berlin Brain-Computer Interface: EEG-based communication without subject training. IEEE Trans Neural Syst Rehabil Eng 14: 147–152.
- 5. Waldert S, Preissl H, Demandt E, Braun C, Birbaumer N, et al. (2008) Hand movement direction decoded from MEG and EEG. J Neurosci 28: 1000–1008.
- 6. Birbaumer N, Ghanayim N, Hinterberger T, Iversen I, Kotchoubey B, et al.

(1999) A spelling device for the paralysed. Nature 398: 297–298.

- 7. Pfurtscheller G, Neuper C (1994) Event-related synchronization of mu rhythm in the EEG over the cortical hand area in man. Neurosci Lett 174: 93–96.
- 8. Birbaumer N, Cohen LG (2007) Brain-computer interfaces: communication and restoration of movement in paralysis. J Physiol 579: 621–636.
- 9. Daly JJ, Wolpaw JR (2008) Brain-computer interfaces in neurological rehabilitation. Lancet Neurol 7: 1032–1043.
- 10. Buch E, Weber C, Cohen LG, Braun C, Dimyan MA, et al. (2008) Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39: 910–917.
- 11. Broetz D, Braun C, Weber C, Soekadar SR, Caria A, et al. (2010) Combination of brain-computer interface training and goal-directed physical therapy in chronic stroke: a case report. Neurorehabil Neural Repair 24: 674–679.
- 12. Soekadar SR, Witkowski M, Mellinger J, Ramos A, Birbaumer N, et al. (2011) ERD-based online brain-machine interfaces (BMI) in the context of neurorehabilitation: optimizing BMI learning and performance. IEEE Trans Neural Syst Rehabil Eng 19: 542–549.
- 13. Shindo K, Kawashima K, Ushiba J, Ota N, Ito M, et al. (2011) Effects of neurofeedback training with an electroencephalogram-based brain-computer interface for hand paralysis in patients with chronic stroke: a preliminary case series study. J Rehabil Med 43: 951–957.
- 14. Mehring C, Rickert J, Vaadia E, Cardosa de Oliveira S, Aertsen A, et al. (2003) Inference of hand movements from local field potentials in monkey motor cortex. Nat Neurosci 6: 1253–1254.
- 15. Koike Y, Hirose H, Sakurai Y, Iijima T (2006) Prediction of arm trajectory from a small number of neuron activities in the primary motor cortex. Neurosci Res 55: 146–153.
- 16. Wu W, Gao Y, Bienenstock E, Donoghue JP, Black MJ (2006) Bayesian population decoding of motor cortical activity using a Kalman filter. Neural Comput 18: 80–118.
- 17. Stark E, Abeles M (2007) Predicting movement from multiunit activity. J Neurosci 27: 8387–8394.
- 18. Serruya MD, Hatsopoulos NG, Paninski L, Fellows MR, Donoghue JP (2002) Instant neural control of a movement signal. Nature 416: 141–142.
- 19. Chapin JK, Moxon KA, Markowitz RS, Nicolelis MA (1999) Real-time control of a robot arm using simultaneously recorded neurons in the motor cortex. Nat Neurosci 2: 664–670.
- 20. Taylor DM, Tillery SI, Schwartz AB (2002) Direct cortical control of 3D neuroprosthetic devices. Science 296: 1829–1832.
- 21. Carmena JM, Lebedev MA, Crist RE, O’Doherty JE, Santucci DM, et al. (2003) Learning to control a brain-machine interface for reaching and grasping by primates. PLoS Biol 1: E42.
- 22. Velliste M, Perel S, Spalding MC, Whitford AS, Schwartz AB (2008) Cortical control of a prosthetic arm for self-feeding. Nature 453: 1098–1101.
- 23. Moritz CT, Perlmutter SI, Fetz EE (2008) Direct control of paralysed muscles by cortical neurons. Nature 456: 639–642.
- 24. Hochberg LR, Serruya MD, Friehs GM, Mukand JA, Saleh M, et al. (2006) Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442: 164–171.
- 25. Kennedy PR, Kirby MT, Moore MM, King B, Mallory A (2004) Computer control using human intracortical local field potentials. IEEE Trans Neural Syst Rehabil Eng 12: 339–344.

- 26. Polikov VS, Tresco PA, Reichert WM (2005) Response of brain tissue to chronically implanted neural electrodes. J Neurosci Methods 148: 1–18.
- 27. Leuthardt EC, Schalk G, Wolpaw JR, Ojemann JG, Moran DW (2004) A braincomputer interface using electrocorticographic signals in humans. J Neural Eng 1: 63–71.
- 28. Chin CM, Popovic MR, Thrasher A, Cameron T, Lozano A, et al. (2007) Identification of arm movements using correlation of electrocorticographic spectral components and kinematic recordings. J Neural Eng 4: 146–158.
- 29. Ball T, Schulze-Bonhage A, Aertsen A, Mehring C (2009) Differential representation of arm movement direction in relation to cortical anatomy and function. J Neural Eng 6: 016006.
- 30. Yanagisawa T, Hirata M, Saitoh Y, Kato A, Shibuya D, et al. (2009) Neural decoding using gyral and intrasulcal electrocorticograms. Neuroimage 45: 1099– 1106.
- 31. Yanagisawa T, Hirata M, Saitoh Y, Kishima H, Matsushita K, et al. (2012) Electrocorticographic control of a prosthetic arm in paralyzed patients. Ann Neurol 71: 353–361.
- 32. Pistohl T, Schulze-Bonhage A, Aertsen A, Mehring C, Ball T (2012) Decoding natural grasp types from human ECoG. Neuroimage 59: 248–260.
- 33. Chestek CA, Gilja V, Blabe CH, Foster BL, Shenoy KV, et al. (2013) Hand posture classification using electrocorticography signals in the gamma band over human sensorimotor brain areas. J Neural Eng 10: 026002.
- 34. Leuthardt EC, Miller KJ, Schalk G, Rao RP, Ojemann JG (2006) Electrocorticography-based brain computer interface–the Seattle experience. IEEE Trans Neural Syst Rehabil Eng 14: 194–198.
- 35. Schalk G, Kubanek J, Miller KJ, Anderson NR, Leuthardt EC, et al. (2007) Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. J Neural Eng 4: 264–275.
- 36. Schalk G, Miller KJ, Anderson NR, Wilson JA, Smyth MD, et al. (2008) Twodimensional movement control using electrocorticographic signals in humans. J Neural Eng 5: 75–84.
- 37. Pistohl T, Ball T, Schulze-Bonhage A, Aertsen A, Mehring C (2008) Prediction of arm movement trajectories from ECoG-recordings in humans. J Neurosci Methods 167: 105–114.
- 38. Gunduz A, Sanchez JC, Carney PR, Principe JC (2009) Mapping broadband electrocorticographic recordings to two-dimensional hand trajectories in humans Motor control features. Neural Netw 22: 1257–1270.
- 39. Leuthardt EC, Gaona C, Sharma M, Szrama N, Roland J, et al. (2011) Using the electrocorticographic speech network to control a brain-computer interface in humans. J Neural Eng 8: 036004.
- 40. Wang W, Collinger JL, Degenhart AD, Tyler-Kabara EC, Schwartz AB, et al.

(2013) An Electrocorticographic Brain Interface in an Individual with Tetraplegia. PLoS ONE 8: e55344.

- 41. Kubanek J, Miller KJ, Ojemann JG, Wolpaw JR, Schalk G (2009) Decoding flexion of individual fingers using electrocorticographic signals in humans. J Neural Eng 6: 066001.
- 42. Chao ZC, Nagasaka Y, Fujii N (2010) Long-term asynchronous decoding of arm motion using electrocorticographic signals in monkeys. Front Neuroeng 3: 3.
- 43. Shimoda K, Nagasaka Y, Chao ZC, Fujii N (2012) Decoding continuous threedimensional hand trajectories from epidural electrocorticographic signals in Japanese macaques. J Neural Eng 9: 036015.
- 44. Shin D, Watanabe H, Kambara H, Nambu A, Isa T, et al. (2012) Prediction of muscle activities from electrocorticograms in primary motor cortex of primates. PLoS One 7: e47992.
- 45. Watanabe H, Sato MA, Suzuki T, Nambu A, Nishimura Y, et al. (2012) Reconstruction of movement-related intracortical activity from micro-electrocorticogram array signals in monkey primary motor cortex. J Neural Eng 9: 036006.
- 46. Sato M (2001) Online model selection based on the variational bayes. Neural Computation 13: 1649–1681.
- 47. Ting JA, D’Souza A, Yamamoto K, Yoshioka T, Hoffman D, et al. (2008) Variational Bayesian least squares: an application to brain-machine interface data. Neural Netw 21: 1112–1131.
- 48. Nambu I, Osu R, Sato MA, Ando S, Kawato M, et al. (2009) Single-trial reconstruction of finger-pinch forces from human motor-cortical activation measured by near-infrared spectroscopy (NIRS). Neuroimage 47: 628–637.
- 49. Yoshimura N, DaSalla CS, Hanakawa T, Sato MA, Koike Y (2012) Reconstruction of flexor and extensor muscle activities from electroencephalography cortical currents. Neuroimage 59: 1324–1337.

