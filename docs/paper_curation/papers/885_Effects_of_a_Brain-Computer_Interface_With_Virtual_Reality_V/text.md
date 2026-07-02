ORIGINAL RESEARCH published: 19 June 2019

doi: 10.3389/fnhum.2019.00210

# Effects of a Brain-Computer Interface With Virtual Reality (VR) Neurofeedback: A Pilot Study in Chronic Stroke Patients

Athanasios Vourvopoulos1*, Octavio Marin Pardo1, Stéphanie Lefebvre1, Meghan Neureither1, David Saldana1, Esther Jahng1 and Sook-Lei Liew1,2*

1 Neural Plasticity and Neurorehabilitation Laboratory, Occupational Science and Occupational Therapy, University of Southern California, Los Angeles, CA, United States, 2 Department of Neurology, Stevens Neuroimaging and Informatics Institute, University of Southern California, Los Angeles, CA, United States

Rehabilitation for stroke patients with severe motor impairments (e.g., inability to perform wrist or ﬁnger extension on the affected side) is burdensome and difﬁcult because most current rehabilitation options require some volitional movement to retrain the affected side. However, although these patients participate in therapy requiring volitional movement, previous research has shown that they may receive modest beneﬁts from action observation, virtual reality (VR), and brain-computer interfaces (BCIs). These approaches have shown some success in strengthening key motor pathways thought to support motor recovery after stroke, in the absence of volitional movement. The purpose of this study was to combine the principles of VR and BCI in a platform called REINVENT and assess its effects on four chronic stroke patients across different levels of motor impairment. REINVENT acquires post-stroke EEG signals that indicate an attempt to move and drives the movement of a virtual avatar arm, allowing patient-driven action observation neurofeedback in VR. In addition, synchronous electromyography (EMG) data were also captured to monitor overt muscle activity. Here we tested four chronic stroke survivors and show that this EEG-based BCI can be safely used over repeated sessions by stroke survivors across a wide range of motor disabilities. Finally, individual results suggest that patients with more severe motor impairments may beneﬁt the most from EEG-based neurofeedback, while patients with more mild impairments may beneﬁt more from EMG-based feedback, harnessing existing sensorimotor pathways. We note that although this work is promising, due to the small sample size, these results are preliminary. Future research is needed to conﬁrm these ﬁndings in a larger and more diverse population.

Edited by: Praveen Pilly,

HRL Laboratories, United States

Reviewed by: Joon-Ho Shin,

National Rehabilitation Center, South Korea

Arnaud Saj, Université de Genève, Switzerland

*Correspondence: Athanasios Vourvopoulos

vourvopo@usc.edu Sook-Lei Liew sliew@usc.edu

Received: 15 March 2019 Accepted: 03 June 2019 Published: 19 June 2019

Citation: Vourvopoulos A, Pardo OM,

Keywords: brain-computer interfaces, virtual reality, action observation, stroke, neurorehabilitation

Lefebvre S, Neureither M, Saldana D,

## INTRODUCTION

Jahng E and Liew S-L (2019) Effects of a Brain-Computer Interface With Virtual Reality (VR) Neurofeedback:

Stroke is a leading cause of adult long-term disability worldwide (Mozaﬀarian et al., 2015), and an increasing number of stroke survivors suﬀer from severe cognitive and motor impairments each year. This results in a loss of independence in their daily life, such as decreased ability to perform self-care tasks and decreased participation in social activities (Miller et al., 2010). Rehabilitation

A Pilot Study in Chronic Stroke

Patients. Front. Hum. Neurosci. 13:210.

doi: 10.3389/fnhum.2019.00210

Vourvopoulos et al. Stroke BCI With VR

The most common brain signal acquisition technology used with BCIs in stroke patients is non-invasive electroencephalography (EEG) (Wolpaw, 2012), which provide a cost-eﬀective BCI platform (Vourvopoulos and Bermúdez i Badia, 2016b). In BCI paradigms for motor rehabilitation, EEG signals related to motor planning and execution are utilized. During a motor attempt, the temporal pattern of the Alpha rhythm (8–12 Hz) desynchronizes. The Alpha rhythm is also termed Rolandic mu or the sensorimotor rhythm (SMR) when it is localized over the sensorimotor cortices of the brain. Mu rhythms (8–12 Hz) are considered indirect indications of the action observation network (Kropotov, 2016) and reﬂect general sensorimotor activity. Mu rhythms are often detected with changes in the Beta rhythm (12–30 Hz) in the form of event-related desynchronization (ERD), in which a motor action is executed (Pfurtscheller and Lopes da Silva, 1999). These EEG rhythms, or motor-related EEG signatures, are primarily detected during task-based EEG (i.e., when the patient is actively moving or imagining movement) and used for neurofeedback.

following stroke focuses on maximizing restoration of lost motor and cognitive functions and on relearning skills to better perform activities of daily living (ADLs). There is increasing evidence that the brain remains plastic at later stages after stroke, suggesting additional recovery remains possible (Page et al., 2004; Butler and Page, 2006). To maximize brain plasticity, several rehabilitation strategies have been exploited, including the use of intensive rehabilitation (Wittenberg et al., 2016), repetitive motor training (Thomas et al., 2017), mirror therapy (Pérez-Cruzado et al., 2017), motor-imagery (Kho et al., 2014), and action observation (Celnik et al., 2008), amongst others.

Recently, growing evidence of the positive impact of virtual reality (VR) techniques on recovery following stroke has accumulated (Bermúdez i Badia et al., 2016). When combined with conventional therapy, VR is able to eﬀectively incorporate rehabilitation strategies such as intensity, frequency, and duration of therapy in a novel and low-cost approach in the stroke population (Laver et al., 2017). However, patients with low levels of motor control cannot beneﬁt from current VR tools due to their low volitional motor control, range of motion, pain, and fatigue. Rehabilitation for these individuals is challenging because most current training options require some volitional movement to train the aﬀected side, however, research has shown that individuals with severe stroke may receive modest beneﬁts from action observation and brain-computer interfaces (BCIs) (Silvoni et al., 2011).

Further, neurofeedback-induced changes in brain activity have also been linked to changes in brain activity at rest. That is, after training one’s brain activity using neurofeedback, the intrinsic, resting brain activity (i.e., EEG activity in the absence of a task) may also show changes. This resting brain activity can be used to assess more generalized brain changes, and baseline resting-state signatures may be used to predict recovery (Wu et al., 2015) or response to treatments (Zhou et al., 2018). When combined with neural injury information, resting EEG parameters can also help predict the eﬃcacy of stroke therapy.

Merging BCIs with VR allows for a wide range of experiences in which patients can feel immersed in various aspects of their environment. This allows patients to control their experiences in VR using only brain activity, either directly (e.g., movement in VR through explicit control) or indirectly (e.g., modulating task diﬃculty level based on workload as implicit control) (Vourvopoulos et al., 2016; Friedman, 2017). This direct brain-to-VR communication can induce a sensorimotor contingency between the patient’s internal intentions and the environment’s responsive actions, increasing the patient’s sense of embodiment of their virtual avatar (Slater, 2009; Ramos-Murguialday et al., 2013).

In this study, our goal was to combine the principles of virtual reality and BCIs to elicit optimal rehabilitation gains for stroke survivors. We hypothesized that merging BCIs with VR should induce illusions of movement and a strong feeling of embodiment within a virtual body via the action observation network, activating brain areas that overlap with those controlling actual movement, which is important for mobilizing neuroplastic changes (Dobkin, 2007). Using a VR-based BCI, those with severe stroke impairments can trigger voluntary movements of the virtual arm in a closed neurofeedback loop. This helps to increase the illusion of one’s own movements through the coordination between one’s intention and the observed ﬁrst-person virtual action. Therefore, we developed a training platform called REINVENT, which uses post-stroke brain signals that indicate an attempt to move and then drives the movement of a virtual avatar arm, providing patient-driven action observation in headmounted VR (Spicer et al., 2017). Our previous work using REINVENT with healthy individuals indeed showed that the combination of VR integrated into a BCI encouraged greater embodiment, and greater embodiment was related to greater neurofeedback performance (Anglin et al., 2019).

After a stroke resulting in severe motor impairments (e.g., inability to perform wrist or ﬁnger extension on the aﬀected side), research shows that action observation combined with physical training enhances the eﬀects of motor training (Celnik et al., 2008), eliciting motor-related brain activity in the lesioned hemisphere, leading to modest motor improvements (Ertelt et al., 2007; Garrison et al., 2013). Moreover, action observation in a head-mounted VR increases motor activity in both healthy and the post-stroke brains (Ballester et al., 2015; Vourvopoulos and Bermúdez i Badia, 2016a).

In addition, neurofeedback through BCIs has been proposed for individuals with severe stroke because BCIs do not require active motor control. Research on BCIs for rehabilitation has shown that motor-related brain signals are reinforced by rewarding feedback so they can be used to strengthen key motor pathways that are thought to support motor recovery after stroke (Wolpaw, 2012). Such feedback has previously shown modest success in motor rehabilitation for severe stroke patients (Soekadar et al., 2015).

For this study, we recruited four chronic stroke survivors to undergo a longitudinal BCI-VR intervention using REINVENT to provide EEG-based neurofeedback with simultaneous EMG acquisition. We assessed intervention results using clinical measures, Transcranial Magnetic Stimulation (TMS) and Magnetic Resonance Imaging (MRI) and compared these measures before and after the intervention. The purpose of

Vourvopoulos et al. Stroke BCI With VR

a distributed architecture, making it hardware independent, in an open and modular design. This updated version makes it possible to integrate as many new interfaces as needed to keep up with the rapid pace of technology development. In this version, the data acquisition and processing modules are also independent of the VR task, communicating bidirectionally over a network layer. We acquired the electrophysiological signals from the hardware using a set of “satellite” clients (EEG, EMG) and sending them to the processing module(s) and a logger via the Lab Streaming Layer (LSL) protocol. After signal processing, the extracted features (i.e., EEG bands, EMG ﬂexion detection) were sent through the same protocol to VR. The VR training environment streamed back to the network the following items: task score, task events (e.g., trial start, pause, complete), and rotational information of the VR hand controllers in three-dimensions.

this study was twofold. First, we sought to determine whether REINVENT is feasible for stroke patients to use across repeated sessions and second, whether REINVENT might be able to strengthen motor-related brain signals in individuals with diﬀering levels of motor impairment after stroke.

## MATERIALS AND METHODS Population

In this pilot study, we recruited four chronic stroke survivors (1 female, 3 male) with subcortical stroke (mean age: 60 ± 5.8 years old). The inclusion criteria included: (1) chronic (>6 months) stroke, between 18 and 80 years of age, (2) motor impairment in the upper limb, and (3) brain lesion as demonstrated by brain imaging. The exclusion criteria included: the presence of (1) intracranial metal, (2) epilepsy, (3) pregnancy, (4) cognitive impairments or psychiatric disorders, and (5) being unable to understand the instructions. All individuals were right-handed prior to the stroke, had a normal or corrected-to-normal vision, and were safe for MRI. Medications for spasticity were not permitted during the study intervention. The experimental protocol was approved by the University of Southern California Health Sciences Campus Institutional Review Board (IRB), and written informed consent was obtained from all patients upon recruitment in accordance with the 1964 Declaration of Helsinki. Patient demographics and stroke characteristics are described in Table 1.

All VR elements were implemented in the Unity game engine (Unity Technologies, San Francisco, CA, United States) and rendered through an Oculus Rift HMD using the Oculus SDK (Oculus VR, Menlo Park, CA, United States). Overall, the entire architecture layout was encapsulated in three inter-dependent layers: (1) interfacing, (2) processing, and (3) interaction. Each layer can incorporate a subset of independent subcomponents (e.g., device interfacing clients, custom processing code or outof-the-box processing software, and desktop VR or mobile VR) (Figure 1).

Training Procedures and Tasks

We divided the experimental protocol is into three blocks: (a) pre-intervention, (b) intervention, (c) post-intervention.

## REINVENT System

In the pre- and post-intervention blocks, we assessed motor impairment in all the patients using a set of clinical tests. In addition, we acquired functional and structural scans during an MRI session and neurophysiological measurements during a TMS session (Figures 2A,C; see also sections Behavioral and Clinical Assessments and MRI and TMS Assessments).

System Architecture

We implemented a software architecture that could be tailored for stroke patients with diﬀerent motor capabilities and rehabilitation needs. This system incorporated interfaces with diﬀerent degrees-of-freedom (DoF) for training patients with: (1) no active movement, using EEG in a direct brain-toVR interfacing, (2) weak muscle activation, using EMG in a muscle-to-VR interfacing, and (3) substantial active movement, using hand tracking. The VR paradigm included avatar personalization with diﬀerent gender hand models and diﬀerent skin tones to increase embodiment and expand demographic inclusivity. Building upon our previous VR BCI training paradigm (Spicer et al., 2017), we created this new version with

In the intervention block, patients were trained over 8 sessions. Due to self-reported improvements in daily life activities, patient S01 requested a second intervention block of an additional 8 training sessions, leading in a total of 16 training sessions, lasting 6 weeks. However, for consistency across patients, only the ﬁrst 8 sessions are reported in this study. A case report for this patient, including the results following the full 16 sessions, are presented separately (Vourvopoulos et al., 2019).

TABLE 1 | Patients demographics.

Patient number FMA-UEa SISb Time since stroke (months)

Stroke lesion location

Lesion size (volume mm3)

Lesion overlap with the CST in the damaged hemisphere (%)

Affected side

- 1 13 45 112 SC 5237 22 Left
- 2 28 35 186 SC 2686 15 Right
- 3 37 10 77 SC 4389 33 Right
- 4 49 40 59 SC 172 0 Right Mean 31.8 32.5 108.5 – SD 13.1 13.5 48.6 –

FMA, Fugl-Meyer Assessment; FMA-UE, Upper Extremity; and SIS, Stroke Impact Scale physical domain. aFMA-UE was scored on a scale up to 66 points. bSIS was scored on a scale of 0–100. SC, subcortical stroke.

Vourvopoulos et al. Stroke BCI With VR

|[Figure 1] Neurofeedback A Pilot Stud_images/imageFile1.png>)<br><br>FIGURE 1 | System architecture of a closed neurofeedback loop. From left, (1) the evoked physiological responses are captured at the interfacing layer through the data acquisition clients, (2) sent to the processing layer where the signals are ﬁltered and logged, and then, (3) the extracted features (e.g., EEG bands) are sent to the interaction layer where VR training occurs. Written permission to use this photo was obtained from the individual.|
|---|

|[Figure 2] Neurofeedback A Pilot Stud_images/imageFile2.png>)<br><br>FIGURE 2 | Experimental protocol in three levels. (A) Pre-intervention, including assessment through clinical scales, TMS, and MRI. (B) During each intervention session, questionnaires were completed to assess pre- and post-simulation sickness, followed by a resting-state session in which raw the EEG was recorded with the patients’ eye open and closed. Next, four training blocks consisting of 20 trials each were performed in VR. Resting-state and follow up questionnaires were then completed. (C) Post-intervention assessment with MRI and TMS.|
|---|

regarding simulator sickness. We also acquired a resting-state EEG acquisition (4 min).

Each training session lasted for 1.5 h (Figure 2B). Before each session, patients were seated in a comfortable chair with a pillow under the aﬀected arm for support. We instructed all patients to remain relaxed and avoid any unnecessary movement during the experiment. At the beginning and end of every training session, patients completed a set of questionnaires

The training task included a virtual environment in which a set of virtual hands represented the patient’s physical hands from a ﬁrst-person perspective. During training, patients had to perform a wrist and elbow extension attempt of the virtual

Vourvopoulos et al. Stroke BCI With VR

- to track patient changes over time (Vellone et al., 2015). The results are reported on a scale of 0–100, with higher scores indicating the best self-reported quality of life.
- • The Simulator Sickness questionnaire (revised by the UQO Cyberpsychology Lab, 2013) includes 16 questions on a 0–3 Likert scale resulting in two sub-scales: Nausea (9 questions for a maximum of 27 points) and Oculo-Motor (7 questions for a maximum of 21 points) (Kennedy et al., 1993).
- • Finally, we qualitatively acquired the patient’s feedback regarding enjoyment and ease of use in a freeform comments section that patients completed after each session.

hand toward a pre-deﬁned target, followed by rest. The patient’s virtual arm moved toward the target if their sensorimotor brain activity during the motor attempt increased relative to baseline. The intervention consisted of four blocks of training in VR (each block consisted of 20 trials), and each trial lasted 30 s. The ﬁrst 10 s period was a resting baseline, during which the patient was asked to relax. We chose this duration because eventrelated changes need time to develop and then recover, and thus the inter-event interval between two consecutive motor events should last at least 10 s (Pfurtscheller and Lopes da Silva, 1999). The next 20 s consisted of a motor intervention, during which we asked the patient to try to move. This 20 s active movement period was divided into epochs of 4 s each, during which the average ERD was calculated and compared to the ERD of the preceding 10 s baseline. Again, a trial was successful and triggered positive neurofeedback of a virtual arm moving toward a target if the ERD during the active trial was greater than at baseline. In the current study, we collected both EEG and EMG signals, but only EEG was used to control the VR neurofeedback to assess the eﬃcacy of the BCI paradigm across all patients.

## Physiological Measurements

EEG Acquisition and Online Processing

We used the Starstim 8 (Neuroelectrics, Barcelona, Spain) system to capture EEG data. Starstim is a wireless hybrid EEG/tCDS 8channel neurostimulator system with a triaxial accelerometer for the recording and visualization of 24-bit EEG data at 500 Hz. The spatial distribution of the electrodes followed the 10– 20 system conﬁguration (Klem et al., 1999), with electrodes placed over the frontal, somatosensory and motor areas: frontalcentral (FC3, FC4), central (C3, C4, C5, C6), and central-parietal (CP3, CP4). The electrodes were referenced and grounded to the right ear lobe, and the electrode impedance was kept at less than 10 k . Finally, the EEG system was connected via Bluetooth to the dedicated desktop computer for raw signal acquisition and processing.

The experimental setup consisted of a desktop computer (OS: Windows 10, CPU: Intel

CoreTM i7-6700 at 4.00 GHz, RAM: 16GB DDR3 1600 MHz, Graphics: NVIDIA GeForce GTX 1080) running all the acquisition, processing, and VR software. An Oculus Rift HMD was used to deliver the VR feedback to the user. The HMD had two OLED displays, 1080 × 1200 resolution per eye, at 90 Hz refresh rate, and 110◦ ﬁeld of view (the extent of the observable environment at any given time). The HMD also featured 6-DoF tracking (3-axis rotational tracking and 3axis positional tracking) and integrated headphones with 3D spatial audio. Moreover, the Oculus Rift HMD also included two Oculus touch controllers with 6-DoF, delivering vibrotactile feedback to the users.

R

The EEG signals were ﬁrst acquired through the Neuroelectrics NIC-2 client before sending them to OpenVibe platform for online processing. We used a surface Laplacian for spatial ﬁltering over the target location (C3 or C4) and the adjacent electrodes because the desynchronization of SMRs are enhanced and better localized with Laplacian (Pfurtscheller, 1988; McFarland et al., 1997). The online signal processing included a bandpass ﬁlter (8–24 Hz), which was then squared, averaged over 500 samples, and logarithmized. Finally, the output was sent via LSL to the VR client.

## Behavioral and Clinical Assessments

During pre- and post-intervention sessions, a battery of assessments targeting the patient’s upper extremity motor function, spasticity, stroke-related impacts on life and simulator sickness for VR were completed. All clinical assessments were performed by a trained occupational therapist. The clinical and behavioral assessments included the following:

EEG-Based Neurofeedback Training Performance

We measured training performance based on the number of successful motor actions initiated by the virtual hand toward a target. As described previously, each virtual action was triggered when the ERD power exceeded the baseline measurement over C3 or C4 locations and was calculated with the following formula:

- • Fugl-Meyer Upper Extremity scale (FMA-UA). The FMAUA is a scale (0–66) that evaluates motor impairment in post-stroke individuals. A higher score is reﬂective of less motor impairment (Fugl-Meyer et al., 1975).
- • Modiﬁed Ashworth Spasticity (MAS) scale. The MAS is a scale (0–4) that measures spasticity, or velocity-dependent movement, in patients with central nervous system lesions. A lower score indicates less spasticity in the assessed muscle group (Gregson et al., 1999). We measured the MAS in the wrist and elbow.
- • Stroke Impact Scale (SIS). The SIS is a 59-item instrument measuring the self-reported quality of life of stroke survivors across eight categories. In the current study, we only utilized the SIS-Physical domain. Each item is rated on a 5-point Likert scale, designed for repeated administration

n

1 n

Score =

xi ∗ 100 (1)

i=1

where n the total number of trials and xi the successful motor actions.

EEG Post hoc Analysis

For the post hoc EEG analyses, we processed EEG signals in Matlab (The MathWorks, MA, United States) with the EEGLAB toolbox (Delorme and Makeig, 2004). After importing the data and channel information, we used a high-pass ﬁlter at

Vourvopoulos et al. Stroke BCI With VR

1 Hz to remove the “baseline drift,” followed by line-noise and harmonics removal at 60 Hz. To reject bad channels and correct continuous data, we used an artifact subspace reconstruction (ASR) method (Kothe and Jung, 2016). The missing channels were interpolated before re-referencing to average. Next, we performed an independent component analysis (ICA) to remove EOG, EMG, and ECG artifacts (Makeig et al., 1996).

brachii (BB), and triceps brachii (TB) muscles of the paretic arm. Electrode positioning was selected by palpation while individually performing elbow and wrist ﬂexion and extension and was conﬁrmed by visual inspection of the EMG signals. Skin preparation involved shaving the selected area, cleaning with alcohol, and applying abrasive and conducting paste. Both processing pipelines were implemented with a custom-made script in Matlab (The MathWorks, MA, United States). All raw and processed data were streamed and recorded via LSL.

To acquire the diﬀerent EEG bands, we extracted the power spectral density (PSD) for the following frequency bands: alpha (8–12 Hz), beta (12–30 Hz), theta (4–7 Hz), and gamma (25–90 Hz).

EMG Post hoc Analysis

Online processing was performed by reading 0.5 s of the EMG signal from EDC and BB, applying a DC-oﬀset correction, performing full-wave rectiﬁcation and comparing the mean of each epoch with a predeﬁned threshold of muscle activation.

In addition, we extracted the event-related synchronization/desynchronization (ERS/ERD) following the standard ERS/ERD method (Pfurtscheller and Aranibar, 1979) in the mu band between 8 and 12 Hz and the beta band between 12 and 30 Hz. Both mu and beta power were extracted over C3 and C4 electrode locations. ERD was calculated using the following formula:

Oﬄine processing of the EDC signal applied epoch extraction within the boundaries of the trial markers of “baseline” and “active contraction,” DC-oﬀset correction, band-pass ﬁltering within 10-500 Hz, and full-wave rectiﬁcation. Finally, the mean absolute value (MAV) of the epoched EMG signal was extracted as the main feature (Veer and Sharma, 2016):

ERD = (PowerMotor Activity − PowerBaseline)/PowerBaseline × 100 (2)

With positive numbers for ERS and negative numbers indicating ERD.

N

1 N

|xn| (5)

EMGmean = MAV =

Moreover, we extracted the event-related EEG data maps as a time/frequency representation of ERD/ERS between 8 and 24 Hz (Graimann et al., 2002). These maps are also known as ERSP (event-related spectral perturbation) and act as a generalization of the ERS/ERD (Makeig, 1993).

n=1

Where xn is the voltage read by the sensor at that point in time, for N samples.

Furthermore, we assessed the hemispheric lateralization through a hemispheric asymmetry index (HA). HA was computed using both the relative EEG band power during rest and the ERD during motor task over C3 and C4 electrode locations. The power values were measured contralateral to the lesioned side and were subtracted from ipsilateral values of the non-aﬀected side. For those with left hemiparesis, this index was calculated using the following formula:

## MRI and TMS Assessments

We also acquired additional neural assessments (MRI, TMS) during pre- and post-intervention sessions for each patient to assess any potential brain changes.

MRI Acquisition

Using MRI, we acquired an anatomical image (T1w MPRAGE), a T2-weighted anatomical MRI, a diﬀusion-weighted MRI, and a 7 min resting-state fMRI (rs-fMRI). MRI data were acquired on

HAleft = PowerC4Left movement − PowerC3Left movement (3)

- a 3T Prisma MRI scanner (Siemens, Germany) with a 32-channel head coil, using protocols from the Human Connectome Project (HCP)1. The MRI sequences acquired included the following: T1-weighted MPRAGE scan (208 sagittal slices, 0.8 mm thick, TR = 2400 ms, TE = 2.22 ms, ﬂip angle = 8◦, voxel size 0.8 × 0.8 × 0.8 mm); T2-weighted turbo spin-echo scan (208 sagittal slices, 0.8 mm thick, TR = 3200 ms, TE = 523 ms, ﬂip angle = 8◦, voxel size 0.8 × 0.8 × 0.8 mm); diﬀusion MRI scan (92 slices, 1.5 mm thick, TR = 3230 ms, TE = 89.20 ms, multiband factor = 4, ﬂip angle = 78◦, voxel size 1.5 × 1.5 × 1.5 mm, with a gradient protocol with seven scans at b = 0 s/mm2, 47 at
- b = 1500 s/mm2, 46 at b = 3000 s/mm2, and a complete repetition with reversed phase encoding in the A-P direction); and a rsfMRI scan (7 min and 6 s covering 520 volumes of 72 slices per scan; TR = 800 ms, TE = 37 ms, ﬂip angle = 52◦, voxel size 2 × 2 × 2 mm). For patients with a brain lesion in the left hemisphere, we ﬂipped both structural and functional scans to the right hemisphere for the group analyses.

For those with right hemiparesis, the index was calculated using the following formula:

HAright = PowerC3Right movement − PowerC4Right movement (4)

Finally, we extracted HA for alpha during the resting-state because alpha oscillation at rest is associated with motor and cognitive performance in stroke patients (Dubovik et al., 2012, 2013; Mottaz et al., 2015).

EMG Acquisition and Online Processing

We acquired surface EMG at 2000 Hz using a Delsys Trigno Wireless System (Delsys, MA, United States) with their proprietary software. Each sensor incorporated diﬀerential Ag electrodes with ampliﬁcation and ﬁltering stages and a 16-bit A/D converter. Three-axes of acceleration data were also acquired with the same sensors at 150 Hz and 8-bit ADC resolution. Delsys Trigno EMG sensors were placed on the extensor digitorum comunis (EDC), ﬂexor carpi ulnaris (FCU), biceps

1http://protocols.humanconnectome.org/CCF/

Vourvopoulos et al. Stroke BCI With VR

Lesion Map, Lesion Size, and Lesion Overlap

we also classiﬁed these ROI-to-ROI interactions as follows: (1) damaged intra-hemispheric motor network connectivity: damaged M1-damaged PMd; (2) undamaged intra-hemispheric motor network connectivity: undamaged M1-undamaged PMd; and (3) inter-hemispheric motor network connectivity: average of (undamaged M1-damaged PMd connectivity, damaged M1undamaged PMd connectivity, undamaged M1-damaged M1 connectivity, undamaged PMd-damaged PMd connectivity).

Using MRIcro software, we manually drew a lesion mask on each patient’s brain (see Figure 3). Then, using FSL we calculated the lesion size in mm3 (Table 1). Finally, we used the PALS toolbox (Ito et al., 2018) to calculate the overlap of each patient’s lesion with the corticospinal tract (CST), the primary descending motor pathway (Table 1). The lesion overlap with the CST has been shown to correspond to motor impairment after stroke (Riley et al., 2011).

Transcranial Magnetic Stimulation (TMS)

We used single- and paired-pulse TMS (Magstim 2002 device with BiStim module; Magstim Inc., United Kingdom) with a ﬁgure-of-eight coil combined with the Brainsight neuronavigation system (Rogue Resolutions Ltd., United Kingdom) and surface electrodes to record muscle activity (EMG; Delsys Trigno wireless sensors, Delsys Inc., MA, United States). To localize the motor hotspot, we recorded EMG at the right ﬁrst dorsal interosseous (FDI). We then recorded the patient’s resting motor threshold (RMT) and recruitment curve in each hemisphere by acquiring 5 MEPs at each of the following threshold 100, 110, 120, 130, 140, and 150% of the RMT.

Resting-State fMRI Processing

We analyzed all rs-fMRI data in Matlab using SPM12 and the CONN toolbox2. The preprocessing steps included slice-timing correction, motion realignment, noise correction using white matter, CSF and motion parameters as regressors, and bandpass ﬁltering (0.01–0.1 Hz). We also performed co-registration between the functional scans and the 3D-T1w MPRAGE scans of each patient. Finally, we normalized the functional scans to MNI space and smoothed them using a Gaussian ﬁlter of 6 mm. To measure functional changes in the motor network, we compared the FC between regions of interest (ROI-to-ROI analyses).

ROI-to-ROI Analyses

## Diffusion MRI

We used four regions of interest (ROIs): left M1, right M1, left PMd, and right PMd. We used a meta-analysis from Hardwick and collaborators to deﬁne the location of the ROIs in the left hemisphere and then ﬂipped them to the right hemisphere. The exact coordinates of the center of each ROI, which was deﬁned as a sphere with a radius of 10 mm, were: left M1 (x = −38, y = −24, z = 56), right M1 (x = 38, y = −24, z = 56), left PMd (x = −26, y = 2, z = 60), right PMd (x = 26, y = 2, z = 60). In addition, to explore changes in the intra and inter-hemispheric connectivity in the motor network pre- and post-intervention sessions,

In addition, we acquired diﬀusion MRI in order to correlate the baseline fractional anisotropy (FA) of the corticospinal tract in the damaged hemisphere with the initial motor performance as assessed by the FMA-UA and the changes in EEG-based neurofeedback training performance in VR (i.e., last training session versus ﬁrst training session).

For the diﬀusion MRI preprocessing, we followed the HCP processing pipeline3. We then, modeled each voxel using a multicompartment ﬁber orientation distribution (FOD) approach.

3https://github.com/Washington-University/HCPpipelines/tree/master/ DiﬀusionPreprocessing

2http://www.nitrc.org/projects/conn

|[Figure 3] Neurofeedback A Pilot Stud_images/imageFile3.png>)<br><br>FIGURE 3 | Lesion map does not overlap with cortical motor areas. Display of the lesion map (blue to green scale, with green indicating greater overlap across participants) with regions of interest for M1 (red) and PMd (Yellow). The M1 and PMd ROIs are used in ROI-to-ROI analysis (section fMRI ROI-to-ROI Analysis).|
|---|

Vourvopoulos et al. Stroke BCI With VR

virtual reality) (Kennedy et al., 1993). We measured simulator sickness before and after the ﬁrst and last session of the BCI-VR training. Across all patients, a paired-samples t-test revealed no signiﬁcant diﬀerences before and after REINVENT use in either the ﬁrst or last session for either the nausea or oculomotor subscales [ﬁrst session: Nausea, t (3) = 0.2928, p = 0.79, Oculomotor, t(3) = 1.0954, p = 0.35; last session: Nausea, t(3) = −0.7746, p = 0.50, Oculomotor, t(3) = −0.7746, p = 0.50]. The average change in simulator sickness following REINVENT use was small for both nausea (M = 0.13, SD = 1.46) and oculomotor (M = −0.25, SD = 1.67) subscales (Figure 4). This suggests that repeated VR intervention could be feasible and does not induce increases in simulator sickness.

Finally, we obtained the diﬀusion tensor FA values using FSL and completed the deterministic FOD ﬁber tracking using the Quantitative Imaging Toolkit (QIT). For each patient, we created two tracts: a damaged corticospinal tract (CST) and an undamaged CST from an ROI covering the posterior limb of the internal capsule in each hemisphere.

Statistical Analyses

We note that this is a pilot study with a small sample size (n = 4). However, we performed statistical analyses at the group and individual subject levels to provide a general indication of the signiﬁcance of any observed changes. We encourage the reader to interpret these statistical analyses with caution.

We assessed the normality of the distribution of all data using the Shapiro-Wilk (S-W) normality test. We used one-sample t-tests to determine whether there was a signiﬁcant diﬀerence between the patient’s ERD values and the mean ERD values of a healthy population from prior literature (Pfurtscheller and Aranibar, 1979; Pfurtscheller et al., 2006). We performed paired t-tests to compare pre- and post-intervention means for mu and beta bands on the same continuous, dependent variable (ERD %), and for pre- and post-intervention clinical scales. We used repeated measures (RM) ANCOVAs (one RM-ANCOVA for each ROI as a seed region using “sessions” (pre and postintervention sessions) as a factor and lesion size and lesion overlap on the CST as covariates) in the CONN toolbox in Matlab to compare combinations of pairs between the four ROIs (the following six FC pairs: left M1-right M1, left PMdright PMd, left M1-left PMd, left M1-right PMd, right M1-left PMd, right M1-right PMd) and to compare the intra/interhemispheric connectivity across sessions. We used one RMANOVA to compare the recruitment curve across session using “thresholds” (RMT, 110, 120, 130, 140, 150%) and “sessions” (pre and post-intervention sessions).

Neurofeedback Performance

We extracted the neurofeedback performance in terms of training score in VR and ERD power between the ﬁrst and the last session of the intervention block.

Training Score

In terms of training performance (measured as successful when the virtual hand reached the target), only S01 had an increased score of 7.3% between the ﬁrst (M = 73.3, SD = 17.2) and the last session (M = 80.6, SD = 9.6) while the rest of the patients showed a decrease over time. Speciﬁcally, S02 had a decreased score of 37.1% between the ﬁrst (M = 80.9, SD = 7) and the last session (M = 43.8, SD = 8.9); S03 had a decreased score of 5.4% between the ﬁrst (M = 65.4, SD = 8.7), and the last sessions (M = 60, SD = 4) and S04 had a decreased score of 32.5% between the ﬁrst (M = 80.5, SD = 5) and the last sessions (M = 48, SD = 21.2). A paired-samples t-test revealed a signiﬁcant diﬀerence between the ﬁrst and the last sessions, only for S02, t(3) = 6.671, p = 0.007 (Figure 5). However, by examining the session scores, it is clear that there was wide variability in training score individuals and across sessions. This suggests that the patient’s ability to control the neurofeedback was highly variable, and may depend on variables such as mood, motivation, attention, and fatigue.

We used non-parametric group comparisons using the Kruskal-Wallis H-test for the EMG data. Finally, we performed Pearson’s correlations between the strength of the CST in the damaged hemisphere (as measured by the FA value) and the lesion size/location with the initial motor performance (as measured by the FMA-UA score) and also with the changes in EEG-based neurofeedback training performance (last training session versus ﬁrst training session).

ERD Power

Because both movement and imagery are associated with mu and beta rhythm desynchronization (McFarland et al., 2000), we anticipated a stronger ERD (in terms of higher negative percentage compared to baseline) at the end of the intervention. However, a paired-samples t-test revealed no signiﬁcant diﬀerences between the ﬁrst and last session across patients (Figure 6).

For all statistical comparisons, the signiﬁcance level was set to

- 5% (p < 0.05). All statistical analyses were done using IBM SPSS 20 (SPSS Inc., Chicago, IL, United States), R (The R Foundation for Statistical Computing Platform, version 3.5.2), and Matlab

- R2017a (The MathWorks, MA, United States).

Post hoc EEG Analyses

We extracted the ERSP maps for qualitative purposes as a time/frequency representation of ERD/ERS for all pre- and post-intervention trials. Maps illustrate a clear desynchronization between 8 and 24 Hz compared to baseline for all patients (Figure 7).

RESULTS Simulator Sickness in VR Training

A key concern of using a VR-based BCI over multiple sessions is the possibility of discomfort resulting from VR-induced simulator sickness. Simulator sickness refers to symptoms similar to motion-induced sicknesses, such as dizziness and nausea, following visually-induced simulations (e.g., from head-mounted

ERD Comparisons With Healthy Population Data

We then compared the mean ERD for our patients with the mean for a representative healthy population, reported previously

Vourvopoulos et al. Stroke BCI With VR

|[Figure 4] Neurofeedback A Pilot Stud_images/imageFile4.png>)<br><br>FIGURE 4 | Change in simulator sickness following REINVENT use in the domains of Nausea and Oculomotor disorientation for the ﬁrst and the last sessions of the BCI-VR intervention. A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

asymmetry or motor impairment score (FMA). Speciﬁcally, a strong signiﬁcant negative correlation was observed between the VR task score and the FMA score (r = −0.96, p = 0.04) but not for resting-state alpha (r = −0.83, p = 0.17), nor the hemispheric asymmetry of alpha (r = −0.82, p = 0.18). This suggests that baseline motor impairment impacts a person’s ability to control the BCI, similar to previous ﬁndings (Liew et al., 2016). In addition, the results for the EEG correlations showed a strong relationship, but this is not signiﬁcant, likely due to the small sample size and high variability.

(Pfurtscheller and Aranibar, 1979; Pfurtscheller et al., 2006). Because the healthy population data only reported the frequency range of the mu band, we compared these data with the mu ERD from the patients in our study. In this way, we were able to quantify the diﬀerence between the evoked ERD of stroke patients compared to healthy individuals.

We performed an independent one-sample t-test for each patient, and it revealed signiﬁcant diﬀerences between all patient ERDs compared to the mean ERD of the healthy population (Figure 8). Speciﬁcally, for S01, ERD (M = −10.8, SD = 21.3) was lower than the mean healthy ERD value of −74.5, with a statistically signiﬁcant mean diﬀerence of 63.6, 95% CI [51.95– 75.3], t(15) = 11.591, p < 0.05. For S02, ERD (M = −25.3, SD = 8) was lower than the mean healthy ERD value of −74.5, a statistically signiﬁcant mean diﬀerence of 49.2, 95% CI [42.1– 56.3], t(7) = 16.367, p < 0.05. For S03, ERD (M = −27.3, SD = 19.3) was lower than the mean healthy ERD value of −74.5, a statistically signiﬁcant mean diﬀerence of 47.2, 95% CI [30– 64.5], t(7) = 6.479, p < 0.05. Finally, for S04, ERD (M = −34.8, SD = 5.8) was lower than the mean healthy ERD value of −74.5, a statistically signiﬁcant mean diﬀerence of 39.7, 95% CI [33.9– 45.5], t(6) = 16.789, p < 0.05 (Figure 8).

Post hoc EMG Analyses

Because we designed the REINVENT system to match patients’ motor ability with the best available interfacing technology, we also performed an oﬄine analysis of muscle responses in all patients to validate REIVENT’s ability to measure training beneﬁts across modalities and to examine the potential of using EMG data as an interfacing modality for those with a degree of active movement.

After analyzing the EMG data from all baseline sessions (N = 640) and trials during BCI training, we extracted the mean EMG (in mV) from all subjects. This allowed us to quantify muscle activation diﬀerences between rest and during motor intention. To compare the mean EMG activation between patients, we used a Kruskal-Wallis H-test, which revealed signiﬁcant diﬀerences in signal amplitude χ2(3) = 2044.43, p < 0.001 as well as in resting-state amplitude χ2(3) = 1711.63, p < 0.001. Current data found EMG diﬀerences between patients for both resting-state and muscle activation and also diﬀerences within each patient for EMG signal during activation versus rest periods (Figure 9). This suggests that active EMG signals can be distinguished from baseline rest in all of our patients, across diﬀerent motor impairment levels.

Correlation Analyses

Resting-state EEG alpha oscillation synchrony was previously determined to be related to cognitive and motor performance in patients (Dubovik et al., 2012, 2013). Analysis of the interhemispheric asymmetries might provide a valuable neurophysiological parameter to determine prognosis and follow-up of patients (Cicinelli et al., 2003). In addition, baseline motor impairment level may impact the ability to control the BCI feedback. We, therefore, assessed the relationship between VR task (score) and the resting-state alpha, alpha hemispheric

Vourvopoulos et al. Stroke BCI With VR

|[Figure 5] Neurofeedback A Pilot Stud_images/imageFile5.png>)<br><br>FIGURE 5 | In-game training score for each patient across the 8 sessions (each session score is an average of the 4 training blocks). A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

using EMG neurofeedback. Only patient S01 (EEG Mdn = 79, EMG Mdn = 55), who had a lower motor ability and muscle ﬂaccidity, showed better performance using EEG neurofeedback. This suggests that motor impairment level should be used to determine the modality of neurofeedback given to patients.

We, then, examined whether EMG neurofeedback might have been more successful for patients than using EEG neurofeedback. In particular, we found that patients with less motor impairment showed reduced performance in VR training when using EEG neurofeedback. Therefore, we re-calculated the training score for all patients using the EMG data and compared it with the performance levels calculated using EEG (Figure 10).

## MRI, TMS, Behavior

Patients with higher motor ability showed a higher success rate when using EMG neurofeedback than when using EEG neurofeedback. Speciﬁcally, S02 (EEG Mdn = 72.5, EMG Mdn = 100), S03 (EEG Mdn = 62, EMG Mdn = 100), and

TMS Sessions

Patients participated in two TMS sessions – one pre-intervention and one post-intervention – to assess the functional integrity of the corticospinal tract, or brain-to-muscle pathway, in patients

- S04 (EEG Mdn = 67, EMG Mdn = 100) had better results

Vourvopoulos et al. Stroke BCI With VR

|[Figure 6] Neurofeedback A Pilot Stud_images/imageFile6.png>)<br><br>FIGURE 6 | ERD values for mu and beta bands pre- and post-intervention for C3 and C4 electrodes. A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

integrated ANOVA in the CONN toolbox. Finally, we averaged the functional connectivity measurements for the intra- and inter-hemispheric motor network connectivity and observed also no signiﬁcant changes between pre- and post-intervention in the intra-hemispheric connectivity in the damaged hemisphere. We also did not observe any statistically signitﬁcant impacts of the lesion size or the lesion overlap with the CST on: (1) connectivity [mean connectivity session pre: 0.27 ± 0.36; mean connectivity session post: 0.19 ± 0.18; ANCOVA: time: F(3) = 0.92, p = 0.44, lesion size: F(1) = 0.82, p = 0.53, lesion overlap with the CST: F(1) = 8.49, p = 0.22], (2) the intra-hemispheric connectivity in the undamaged hemisphere [mean connectivity session pre: −0.10 ± 0.19; mean connectivity session post: 0.05 ± 0.19; ANCOVA: time: F(3) = 5.19, p = 0.11, lesion size: F(1) = 0.22, p = 0.72, lesion overlap with the CST: F(1) = 10.65, p = 0.19], or (3) the inter-hemispheric connectivity in the damaged hemisphere [mean connectivity session pre: 0.21 ± 0.19; mean connectivity session post: 0.29 ± 0.22; ANCOVA: time: F(3) = 0.74, p = 0.45, lesion size: F(1) = 0.13, p = 0.77, lesion overlap with the CST: F(1) = 3.12, p = 0.33].

(Stinear and Byblow, 2017). This measure has been related to post-stroke motor recovery and ability to beneﬁt from therapy.

In the four patients (Table 2), we localized the motor hotspot in the undamaged hemisphere around the M1 area (i.e., the hand knob). This localization was reliable between pre- and post-intervention assessments (Figure 11). At this location, we acquired the RMT at the same intensity between the two sessions (Pre: 51.3 ± 6.4, Post: 52.3 ± 5.1). It was diﬃcult to localize the motor hotspot in the damaged hemisphere; therefore, we had to use a higher stimulator intensity to evoke an MEP. At this location, only one patient (S04) had a reachable RMT during the ﬁrst session (71%). For the other patients, as RMT was not reachable at each session, we determined the active motor threshold (AMT) in both pre and post-intervention sessions. Interestingly, however, while patient S01 did not have a reachable RMT pre-intervention, he had a reachable RMT postintervention (which was maintained after his extended 16-session protocol, Vourvopoulos et al., 2019). In this patient, the motor hotspot localization from the AMT moved posteriorly to the parietal cortex for the RMT (in the post-intervention session).

We were able to reliably acquire the recruitment curves only in the undamaged hemisphere for all patients. Using a RM-ANOVA, we compared the recruitment curves across the two sessions and observed only an eﬀect of the “thresholds” (meaning an increase of the MEP amplitude with increased threshold) but there was no eﬀect of “sessions” nor an interaction eﬀect (RM ANOVA: interaction “thresholds”x”sessions”: F(5) = 0.084, p = 0.99; thresholds: F(5) = 3.96, p = 0.006; sessions: F(1) = 0.275, p = 0.60).

Diffusion MRI

We obtained the CST tract in the damaged and undamaged hemisphere of each of the four patients. As shown in Figure 12, patients S03 and S04 overall had intact CST tracts in both hemispheres, whereas patients S01 and S02 had impaired CST tracts in the damaged hemisphere. We explored if the strength of the CST in the damaged hemisphere could predict the changes in EEG-based neurofeedback training performance. This analysis revealed no correlation (Pearson: r = −0.03, p = 0.96) between these measurements. We also performed a Pearson correlation analysis between the FA of the CST in the damaged hemisphere and the initial motor ability of the patients and observed a positive non-statistically signiﬁcant trend with the initial FMA-UA score (r = 0.92, p = 0.07), suggesting a loose

fMRI ROI-to-ROI Analysis

We next examined changes in connectivity for each motor ROI-to-ROI pair using an ANOVA with time as a factor. We did not observe any signiﬁcant diﬀerences in the ROIto-ROI functional connectivity measurement between pre- and post-intervention at the group level as assessed using an

Vourvopoulos et al. Stroke BCI With VR

|[Figure 7] Neurofeedback A Pilot Stud_images/imageFile7.png>)<br><br>FIGURE 7 | ERSP activation maps, pre and post stimulus between mu and beta bands over the lesioned side during motor attempt. Signiﬁcant ERD is illustrated with blue.|
|---|

were not signiﬁcant, these show a potential trend that patients with larger lesions and greater lesion overlap with the CST may have greater improvements on the EEG-based neurofeedback training performance.

relationship between patients with a stronger CST in the damaged hemisphere and better initial motor ability.

Lesion Size and Lesion Location

We used the size of the lesion and the lesion overlap with the CST to explore the impact of the lesion location and size on the initial motor impairment (initial FMA-UE). There was no relationship between either the size of the lesion and the initial FMA-UE (Pearson: r = −0.81, p = 0.19), or the lesion overlap on the CST and the initial FMA-UE (Pearson: r = −0.47, p = 0.53).

Clinical Outcomes

Last but not least, in terms of clinical scales, we compared whether there was a diﬀerence in FMA-UE, MAS, or SIS before and after the 8 week intervention block, expecting an improvement in clinical scales. A paired-samples t-test yielded no signiﬁcant group diﬀerences between pre- and postintervention for all scales.

We also explored if the lesion size and location had any impact on the EEG-based neurofeedback training performance. We found a strong positive, but non-signiﬁcant, correlation between the changes in EEG-based neurofeedback performance and both the lesion size (Pearson: r = 0.84, p = 0.16) and the lesion overlap with the CST (r = 0.91, p = 0.09). Although these

Nonetheless, patients S01, S03, S04 had increased FMAUE scores, with S03 demonstrating a six-point increase in the FMA-UE. According to Page et al. (2012) this degree of increase in the FMA-UE meets the minimal clinically important diﬀerence

Vourvopoulos et al. Stroke BCI With VR

|[Figure 8] Neurofeedback A Pilot Stud_images/imageFile8.png>)<br><br>FIGURE 8 | ERD power of the Mu band over the lesioned side of the four stroke patients compared with healthy population data (Pfurtscheller and Aranibar, 1979; Pfurtscheller et al., 2006). ∗ indicates signiﬁcance of p < 0.05. A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

|[Figure 9] Neurofeedback A Pilot Stud_images/imageFile9.png>)<br><br>FIGURE 9 | Average EMG activation during baseline (resting) and motor action (muscle activation). ∗ indicates the signiﬁcance of p < 0.05. A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

|[Figure 10] Neurofeedback A Pilot Stud_images/imageFile10.png>)<br><br>FIGURE 10 | Re-calculated average score from EMG data (shown as a blue and red circle) compared to the average EEG-based score (shown as a box and whisker plot) during training. A box and whisker plot showing medians and standard deviations are illustrated.|
|---|

threshold of 4.25–7.25 points. Finally, the self-reported SIS scores increased in all patients except one (S04), while the MAS remained stable (Table 3).

## DISCUSSION

In this pilot study, we described the use of an EEG-based BCI for motor rehabilitation that provides biologicallyrelevant neurofeedback in head-mounted virtual reality (REINVENT) with four chronic stroke patients across diﬀerent motor impairment levels. We demonstrated that VR-based neurofeedback may be feasible for stroke patients with motor impairments for prolonged, multi-session use. We also suggest that the source of neurofeedback should be tailored to the individual’s impairment level and that for individuals with more motor ability, EMG-based feedback may be more useful. Overall, the current results contribute toward our understanding of how BCI-VR training can be used for chronic stroke patients with diﬀerent levels of motor impairment.

First, we found that repeated use of a BCI with head-mounted VR-based neurofeedback (8 sessions of 1.5 h each) was feasible and tolerable for stroke patients across a variety of motor impairment levels. The overall set-up process took about 20 min per individual, including setting up the 8-channel EEG and 4channel EMG systems and putting on the HMD-VR over the EEG cap. However, there were no issues with simulator sickness following any of the sessions and no other complaints about pain, discomfort or fatigue. Overall, patients were enthusiastic about using REINVENT and appreciated the new form of therapy. Despite variable motor results after using REINVENT, patients self-reported positive changes in overall quality of life on a

comments form and asked to continue using REINVENT after the study was completed. This suggests that the use of multiple sessions of a VR-based BCI paradigm not only could be feasible but potentially enjoyable for individuals after stroke.

Second, we found that the EEG-BCI seemed to have the greatest positive eﬀects for the patient with the worst motor impairments (patient S01), and little-to-no eﬀects for individuals with more motor ability (e.g., more volitional movement of the aﬀected limb). Patient S01 was the only one to have signiﬁcant changes in cortical physiology, as measured by TMS as the appearance of a motor-evoked potential during rest, and he also had large improvements in SIS following

Vourvopoulos et al. Stroke BCI With VR

- TABLE 2 | TMS motor hotspot.

Undamaged hemisphere Damaged hemisphere

RMT pre-int RMT post-int RMT pre-int AMT pre-int RMT post-int AMT post-int

- S01 48% 48% n/a 68% 73% 68%
- S02 58% 58% n/a 75% n/a 75%
- S03 55% 55% n/a 75% n/a 75%
- S04 44% 48% 71% Not acquired 75% Not acquired Mean 51.25% 52.25% Cannot be calculated due to missing data 72.7% 74% 72.7% SD 6.40% 5.06% 4.04% 1.41% 4.04% RMT, Resting Motor Threshold; AMT, Active Motor Threshold; Pre-Int, Post-Int, Pre- and Post-Intervention. Results displayed are a percentage of stimulator output.

|[Figure 11] Neurofeedback A Pilot Stud_images/imageFile11.png>)<br><br>FIGURE 11 | Individual motor hotspot locations in each session. On each individual brain, a blue acquisition grid is displayed around the sensorimotor cortex. Using<br><br>this grid, we localized the motor hotspot during the initial and ﬁnal session. The site where the hotspot was localized for each session is displayed with a colored arrow in both the damaged and undamaged hemispheres. In patients S01 and S04, the motor hotspot in the damaged hemisphere was found at a different grid node between the two sessions.|
|---|

REINVENT use. He was also the most successful at controlling the EEG-BCI feedback and showed improved performance following REINVENT training. In contrast, the other three patients all had volitional movement of the aﬀected hand and wrist and did not show improved performance with REINVENT training. They also showed many fewer and more variable changes in behavior and neural assessments. This ﬁnding mirrors previous work showing that individuals with greater motor impairments after stroke show the greatest beneﬁts from real-time fMRI neurofeedback (Liew et al., 2016). One potential hypothesis to explain this ﬁnding is that in individuals with worse motor impairment, there are fewer inputs to and outputs from the damaged motor cortex, hence poorer motor ability. Given this, these brain areas may be more ﬂexible to neuromodulation and may be more easily trained because these regions are not being actively engaged for other tasks. On the other hand, in individuals with volitional movement, these brain regions may already be actively recruited through more naturalistic processes (e.g., trying to move one’s arm on a regular basis) and may be less ﬂexible to learn new patterns imposed by the neurofeedback training.

On the other hand, individuals with volitional movement may show greater beneﬁts from a form of neurofeedback that strengthens their existing brain-to-muscle pathways. Our post hoc EMG analysis showed that if individuals with volitional movement had been given EMG-based feedback, instead of EEG-based feedback, they would have shown much better BCI control and performance. This was the opposite for Patient S01, who would have performed worse with EMG-based feedback. Although more research is needed in a larger and more diverse sample, these data provide some insight into how BCIs could be personalized to each patient’s needs. For those without volitional motor control, learning to control the damaged hemisphere at all, using broad motor frequency bands was successful. However, for those with some motor control or at least muscle activity, harnessing the individual’s own already established pathways may be more eﬀective. This could potentially be done with EEG, by matching the neurofeedback to the speciﬁc ipsilesional brain activity evoked when the individual moves, or with EMG, which by nature utilizes an established pathway from the brain to the muscle. A ﬂexible BCI that collects multimodal data (e.g., EEG and EMG), and can provide a tailored neurofeedback signal, may have the best potential for improving recovery.

Vourvopoulos et al. Stroke BCI With VR

|[Figure 12] Neurofeedback A Pilot Stud_images/imageFile12.png>)<br><br>FIGURE 12 | Individual corticospinal tracts in both hemispheres. The damaged hemisphere is represented on the right hemisphere in all images.|
|---|

Overall, these results show that the training paradigm was feasible and safe. However, there were no signiﬁcant group changes in clinical scales or in brain imaging metrics following REINVENT. This is perhaps not surprising, given that three of the individuals with greater motor ability did not show improved performance on the BCI, and thus would be unlikely to show improvements in motor function or brain activity. The one consistent improvement was in the SIS, which improved in three of the four patients, and could be more related to the social interactions of engaging in a novel therapy and therapy team. In terms of actual motor changes, the most notable change was the detection of a resting motor threshold in patient S01 after neurofeedback training, and he was also the only person to improve on the neurofeedback training. We hypothesize that for the other three patients, using EMG-based neurofeedback will have more positive eﬀects. It is possible that 8 sessions might be too few sessions to show marked changes in either behavior or intrinsic brain activity; future studies should explore this with longer study duration. It is also worth noting that there is high variability in BCI performance across sessions, suggesting that individual state factors, such as fatigue, motivation, and attention may have a strong inﬂuence on patients’ ability to control the BCI. Patients also reported experimenting with trying out diﬀerent

strategies to control the BCI across days, which could also have introduced variability in overall BCI performance and resulting behavioral and neural changes.

## LIMITATIONS

Although this study collected and explored 160 EEG datasets (128 motor related and 32 resting-state data) along with pre- and post-intervention MRI, TMS, and clinical behavior datasets from stroke patients, it was limited by its sample size (N = 4). Our ﬁndings, therefore, are preliminary, have limited statistical power, and should be interpreted with caution. In addition, the statistical outcomes relating to our measurement (eﬃcacy of the proposed technique) and the comparisons presented here are exploratory and not conﬁrmative. Furthermore, increasing the number of sessions per patient could also have resulted in more positive results. Finally, as noted above, given the wide range of motor impairment levels across our four patients, there was signiﬁcant variability in results. Future studies should focus on testing EEGbased BCIs with VR in a wider population of individuals with severe motor impairments.

## CONCLUSION

Overall, in this study, we illustrated a novel architecture with multimodal interfaces for widening the inclusion criteria into VR rehabilitation and training. We showed the eﬀect of an EEG-based VR BCI in stroke survivors with a wide range of motor disabilities and identify a potential clinical proﬁle of those who can beneﬁt from an EEG-based interface. This pilot data suggests that patients with more severe motor impairments achieve the maximum beneﬁts of a BCI paradigm, while those with active movement may beneﬁt more from EMG feedback in a multimodal platform. Finally, this VR-based platform is feasible for use by individuals with stroke across repeated

- TABLE 3 | Clinical scales pre- and post-intervention.

FMA-UA MAS SIS

Patient Pre Post Pre Post Pre Post

- S01 13 14 2 2 45 75
- S02 28 25 0 0 35 50
- S03 37 43 1 1 10 60
- S04 49 50 0 0 40 30

FMA-UA, Fugl-Meyer Assessment – Upper Extremity; MAS, Modiﬁed Ashworth Scale; SIS, Stroke Impact Scale.

Vourvopoulos et al. Stroke BCI With VR

sessions, opening the potential for new VR-BCI paradigms for stroke rehabilitation.

designed the technical speciﬁcations underlying the experiment. OP collected and analyzed the EMG data. SL collected and analyzed the TMS and MRI data. MN collected all the behavioral data and performed the clinical assessments pre- and post-intervention. DS and EJ recruited the patients. AV, OP, SL, S-LL, and MN interpreted the data. S-LL designed and supervised the study. All authors revised and approved the current version of the manuscript and deﬁned and designed the research study.

## DATA AVAILABILITY

The datasets generated for this study are available on request to the corresponding author.

## ETHICS STATEMENT

## FUNDING

The experimental protocol was approved by the University of Southern California Health Sciences Campus Institutional Review Board (IRB), and written informed consent was obtained from all participants upon recruitment in accordance with the 1964 Declaration of Helsinki.

This research was supported by the American Heart Association (16IRG26960017), the US Army Research Oﬃce (W911NNF-14D-0005), and the National Institutes of Health (K01HD091283).

## ACKNOWLEDGMENTS

## AUTHOR CONTRIBUTIONS

We would like to thank the Ph.D. students Julia Juliano and Kaori Ito for providing assistance during the MRI and TMS sessions, as well as the M.Sc. student Harmeet Singh for providing assistance in VR development.

AV participated in the development of the VR and neurofeedback software and collected and analyzed the EEG data. AV and OP

## REFERENCES

motor deﬁcits after stroke. Neuroimage 36(Suppl. 2), T164–T173. doi: 10.1016/ j.neuroimage.2007.03.043

Anglin, J. M., Spicer, R., Lefebvre, S., Jann, K., Ard, T., Santarnecchi, E., et al. (2019). Embodiment improves performance on an immersive brain computer interface in head-mounted virtual reality. bioarxiv

Friedman, D. (2017). “Brain-computer interfacing and virtual reality,” in Handbook of Digital Games and Entertainment Technologies, eds R. Nakatsu, M. Rauterberg, and P. Ciancarini (Singapore: Springer), 151–171. doi: 10.1007/ 978-981-4560-50-4_2

Ballester, B. R., Nirme, J., Duarte, E., Cuxart, A., Rodriguez, S., Verschure, P., et al. (2015). The visual ampliﬁcation of goal-oriented movements counteracts acquired non-use in hemiparetic stroke patients. J. Neuroeng. Rehabil. 12:50. doi: 10.1186/s12984-015-0039-z

Fugl-Meyer, A. R., Jääskö, L., Leyman, I., Olsson, S., and Steglind, S. (1975). The post-stroke hemiplegic patient. 1. a method for evaluation of physical performance. Scand. J. Rehabil. Med. 7, 13–31.

Bermúdez i Badia, S., Fluet, G. G., Llorens, R., and Deutsch, J. E. (2016). “Virtual reality for sensorimotor rehabilitation post stroke: design principles and evidence,” in Neurorehabilitation Technology, eds D. J. Reinkensmeyer and V. Dietz (Cham: Springer International Publishing), 573–603. doi: 10.1007/9783-319-28603-7_28

Garrison, K. A., Aziz-Zadeh, L., Wong, S. W., Liew, S.-L., and Winstein, C. J.

(2013). Modulating the motor system by action observation after stroke. Stroke 44, 2247–2253. doi: 10.1161/STROKEAHA.113.001105

Graimann, B., Huggins, J. E., Levine, S. P., and Pfurtscheller, G. (2002). Visualization of signiﬁcant ERD/ERS patterns in multichannel EEG and ECoG data. Clin. Neurophysiol. 113, 43–47. doi: 10.1016/S1388-2457(01)00 697-6

Butler, A. J., and Page, S. J. (2006). Mental practice with motor imagery: evidence for motor recovery and cortical reorganization after stroke. Arch. Phys. Med. Rehabil. 87, S2–S11. doi: 10.1016/j.apmr.2006.08.326

Gregson, J. M., Leathley, M., Moore, A. P., Sharma, A. K., Smith, T. L., and Watkins, C. L. (1999). Reliability of the tone assessment scale and the modiﬁed ashworth scale as clinical tools for assessing poststroke spasticity. Arch. Phys. Med. Rehabil. 80, 1013–1016. doi: 10.1016/s0003-9993(99)90053-9

Celnik, P., Webster, B., Glasser, D., and Cohen, L. (2008). Eﬀects of action observation on physical training after stroke. Stroke J. Cereb. Circ. 39, 1814–

1820. doi: 10.1161/STROKEAHA.107.508184

Cicinelli, P., Pasqualetti, P., Zaccagnini, M., Traversa, R., Oliveri, M., and Rossini, P. M. (2003). Interhemispheric asymmetries of motor cortex excitability in the postacute stroke stage. Stroke 34, 2653–2658. doi: 10.1161/01.STR.0000092122. 96722.72

Ito, K. L., Kumar, A., Zavaliangos-Petropulu, A., Cramer, S. C., and Liew, S.-L. (2018). Pipeline for Analyzing Lesions After Stroke (PALS). Front. Neuroinformatics 12:63. doi: 10.3389/fninf.2018.00063

Kennedy, R. S., Lane, N. E., Berbaum, K. S., and Lilienthal, M. G. (1993). Simulator sickness questionnaire: an enhanced method for quantifying simulator sickness. Int. J. Aviat. Psychol. 3, 203–220. doi: 10.1207/s15327108ijap0303_3

Delorme, A., and Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. J. Neurosci. Methods 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

Kho, A. Y., Liu, K. P. Y., and Chung, R. C. K. (2014). Meta-analysis on the eﬀect of mental imagery on motor recovery of the hemiplegic upper extremity function. Aust. Occup. Ther. J. 61, 38–48. doi: 10.1111/1440-1630.12084

Dobkin, B. H. (2007). Brain-computer interface technology as a tool to augment plasticity and outcomes for neurological rehabilitation. J. Physiol. 579, 637–642. doi: 10.1113/jphysiol.2006.123067

Klem, G. H., Lüders, H. O., Jasper, H. H., and Elger, C. (1999). The ten-twenty electrode system of the International Federation. The International Federation of Clinical Neurophysiology. Electroencephalogr. Clin. Neurophysiol. Suppl. 52, 3–6.

Dubovik, S., Pignat, J.-M., Ptak, R., Aboulaﬁa, T., Allet, L., Gillabert, N., et al.

(2012). The behavioral signiﬁcance of coherent resting-state oscillations after stroke. Neuroimage 61, 249–257. doi: 10.1016/j.neuroimage.2012.03.024

Dubovik, S., Ptak, R., Aboulaﬁa, T., Magnin, C., Gillabert, N., Allet, L., et al. (2013). EEG alpha band synchrony predicts cognitive and motor performance in patients with ischemic stroke. Behav. Neurol. 26, 187–189. doi: 10.3233/BEN2012-129007

Kothe, C. A. E., and Jung, T.-P. (2016). Artifact Removal Techniques with Signal Reconstruction. Available at: https://patents.google.com/patent/ US20160113587A1/en (accessed February 4, 2019).

Kropotov, J. D. (2016). “Chapter 2.2 - Alpha Rhythms,” in Functional Neuromarkers for Psychiatry, ed. J. D. Kropotov (San Diego, CA: Academic Press), 89–105. doi: 10.1016/B978-0-12-410513-3.00008-5

Ertelt, D., Small, S., Solodkin, A., Dettmers, C., McNamara, A., Binkofski, F., et al. (2007). Action observation has a positive impact on rehabilitation of

Vourvopoulos et al. Stroke BCI With VR

Laver, K. E., Lange, B., George, S., Deutsch, J. E., Saposnik, G., and Crotty, M.

Slater, M. (2009). Place illusion and plausibility can lead to realistic behaviour in immersive virtual environments. Philos. Trans. R. Soc. B Biol. Sci. 364, 3549–3557. doi: 10.1098/rstb.2009.0138

(2017). Virtual reality for stroke rehabilitation. Cochrane Database Syst. Rev. 11:CD008349. doi: 10.1002/14651858.CD008349.pub4

Liew, S.-L., Rana, M., Cornelsen, S., Fortunato de Barros Filho, M., Birbaumer, N., Sitaram, R., et al. (2016). Improving motor corticothalamic communication after stroke using real-time fMRI connectivity-based neurofeedback. Neurorehabil. Neural Repair 30, 671–675. doi: 10.1177/154596831561 9699

Soekadar, S. R., Birbaumer, N., Slutzky, M. W., and Cohen, L. G. (2015). Brain– machine interfaces in neurorehabilitation of stroke. Neurobiol. Dis. 83, 172–179. doi: 10.1016/j.nbd.2014.11.025

Spicer, R., Anglin, J., Krum, D. M., and Liew, S. L. (2017). “REINVENT: a lowcost, virtual reality brain-computer interface for severe stroke upper limb motor recovery,” in Proceedings of the 2017 IEEE Virtual Reality (VR), (Los Angeles, CA), 385–386. doi: 10.1109/VR.2017.7892338

Makeig, S. (1993). Auditory event-related dynamics of the EEG spectrum and eﬀects of exposure to tones. Electroencephalogr. Clin. Neurophysiol. 86, 283–293. doi: 10.1016/0013-4694(93)90110-H

Stinear, C. M., and Byblow, W. D. (2017). “The role of TMS for predicting motor recovery and outcomes after stroke,” in Translational Research in Stroke Translational Medicine Research, eds P. A. Lapchak and G.-Y. Yang (Singapore: Springer), 537–553. doi: 10.1007/978-981-10-5804-2_25

Makeig, S., Bell, A. J., Jung, T.-P., and Sejnowski, T. J. (1996). “Independent component analysis of electroencephalographic data,” in Proceedings of the 8th International Conference on Neural Information Processing Systems, (San Diego CA), 145–151.

Thomas, L. H., French, B., Coupe, J., McMahon, N., Connell, L., Harrison, J., et al. (2017). Repetitive task training for improving functional ability after stroke: a major update of a cochrane review. Stroke 48, e102–e103. doi: 10.1161/ STROKEAHA.117.016503

McFarland, D. J., McCane, L. M., David, S. V., and Wolpaw, J. R. (1997). Spatial ﬁlter selection for EEG-based communication. Electroencephalogr. Clin. Neurophysiol. 103, 386–394. doi: 10.1016/S0013-4694(97)00022-2

Veer, K., and Sharma, T. (2016). A novel feature extraction for robust EMG pattern recognition. J. Med. Eng. Technol. 40, 149–154. doi: 10.3109/03091902.2016. 1153739

McFarland, D. J., Miner, L. A., Vaughan, T. M., and Wolpaw, J. R. (2000). Mu and beta rhythm topographies during motor imagery and actual movements. Brain Topogr. 12, 177–186. doi: 10.1023/A:1023437823106

Miller, E. L., Murray, L., Richards, L., Zorowitz, R. D., Bakas, T., Clark, P., et al. (2010). Comprehensive overview of nursing and interdisciplinary rehabilitation care of the stroke patient: a scientiﬁc statement from the American Heart Association. Stroke 41, 2402–2448. doi: 10.1161/STR.0b013e3181e7512b

Vellone, E., Savini, S., Fida, R., Dickson, V. V., Melkus, G. D., Carod-Artal, F. J., et al. (2015). Psychometric evaluation of the Stroke Impact Scale 3.0. J. Cardiovasc. Nurs. 30, 229–241. doi: 10.1097/JCN.0000000000000145

- Vourvopoulos, A., and Bermúdez i Badia, S. (2016a). Motor priming in virtual reality can augment motor-imagery training eﬃcacy in restorative braincomputer interaction: a within-subject analysis. J. Neuroeng. Rehabil. 13:69. doi: 10.1186/s12984-016-0173-2
- Vourvopoulos, A., and Bermúdez i Badia, S. (2016b). “Usability and costeﬀectiveness in brain-computer interaction: is it user throughput or technology related?” in Proceedings of the 7th Augmented Human International Conference AH ’16, (Geneva: ACM), doi: 10.1145/2875194.2875244

Mottaz, A., Solcà, M., Magnin, C., Corbet, T., Schnider, A., and Guggisberg, A. G. (2015). Neurofeedback training of alpha-band coherence enhances motor performance. Clin. Neurophysiol. 126, 1754–1760. doi: 10.1016/j.clinph.2014. 11.023

Mozaﬀarian, D., Benjamin, E. J., Go, A. S., Arnett, D. K., Blaha, M. J., Cushman, M., et al. (2015). Heart disease and stroke statistics–2015 update: a report from the American Heart Association. Circulation 131, e29–e322. doi: 10.1161/CIR. 0000000000000152

Vourvopoulos, A., Ferreira, A., and Bermúdez i Badia, S. (2016). “NeuRow: an immersive VR environment for motor-imagery training with the use of brain-computer interfaces and vibrotactile Feedback,” in Proceedings of the 3rd International Conference on Physiological Computing Systems, Lisbon, 43–53. doi: 10.5220/0005939400430053

Page, S. J., Fulk, G. D., and Boyne, P. (2012). Clinically important diﬀerences for the upper-extremity Fugl-Meyer Scale in people with minimal to moderate impairment due to chronic stroke. Phys. Ther. 92, 791–798. doi: 10.2522/ptj. 20110009

Page, S. J., Gater, D. R., and Bach-Y-Rita, P. (2004). Reconsidering the motor recovery plateau in stroke rehabilitation. Arch. Phys. Med. Rehabil. 85, 1377–

Vourvopoulos, A., Marin Pardo, O., Neureither, M., Saldana, D., Jahng, E., and Liew, S.-L. (2019). “Multimodal head-mounted virtual-reality training and brain-computer interaction for stroke rehabilitation: a clinical case study with REINVENT,” in Proceedings of the 21st International Conference on HumanComputer Interaction (HCII 2019), Orlando, FL.

1381. doi: 10.1016/j.apmr.2003.12.031

Pérez-Cruzado, D., Merchán-Baeza, J. A., González-Sánchez, M., and CuestaVargas, A. I. (2017). Systematic review of mirror therapy compared with conventional rehabilitation in upper extremity function in stroke survivors. Aust. Occup. Ther. J. 64, 91–112. doi: 10.1111/1440-1630.12342

Wittenberg, G. F., Richards, L. G., Jones-Lush, L. M., Roys, S. R., Gullapalli, R. P., Yang, S., et al. (2016). Predictors and brain connectivity changes associated with arm motor function improvement from intensive practice in chronic stroke. F1000Res. 5:2119. doi: 10.12688/f1000research.8603.2

Pfurtscheller, G. (1988). Mapping of event-related desynchronization and type of derivation. Electroencephalogr. Clin. Neurophysiol. 70, 190–193. doi: 10.1016/ 0013-4694(88)90119-8

Wolpaw, J. R. (2012). Brain-Computer Interfaces: Principles and Practice. Oxford: Oxford University Press. Wu, J., Quinlan, E. B., Dodakian, L., McKenzie, A., Kathuria, N., Zhou, R. J., et al.

Pfurtscheller, G., and Aranibar, A. (1979). Evaluation of event-related desynchronization (ERD) preceding and following voluntary selfpaced movement. Electroencephalogr. Clin. Neurophysiol. 46, 138–146. doi: 10.1016/0013-4694(79)90063-4

(2015). Connectivity measures are robust biomarkers of cortical function and plasticity after stroke. Brain 138, 2359–2369. doi: 10.1093/brain/awv156

Pfurtscheller, G., Brunner, C., Schlögl, A., and Lopes da Silva, F. H. (2006). Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of diﬀerent motor imagery tasks. Neuroimage 31, 153–159. doi: 10.1016/j.neuroimage.2005. 12.003

Zhou, R. J., Hondori, H. M., Khademi, M., Cassidy, J. M., Wu, K. M., Yang, D. Z., et al. (2018). Predicting gains with visuospatial training after stroke using an EEG measure of frontoparietal circuit function. Front. Neurol. 9:597. doi: 10.3389/fneur.2018.00597

Pfurtscheller, G., and Lopes da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857. doi: 10.1016/s1388-2457(99)00141-8

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Ramos-Murguialday, A., Broetz, D., Rea, M., Läer, L., Yilmaz, Ö, Brasil, F. L., et al.

(2013). Brain–machine interface in chronic stroke rehabilitation: a controlled study. Ann. Neurol. 74, 100–108. doi: 10.1002/ana.23879

Copyright © 2019 Vourvopoulos, Pardo, Lefebvre, Neureither, Saldana, Jahng and Liew. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

Riley, J. D., Le, V., Der-Yeghiaian, L., See, J., Newton, J. M., Ward, N. S., et al.

(2011). Anatomy of stroke injury predicts gains from therapy. Stroke 42, 421–426. doi: 10.1161/STROKEAHA.110.599340

Silvoni, S., Ramos-Murguialday, A., Cavinato, M., Volpato, C., Cisotto, G., Turolla, A., et al. (2011). Brain-computer interface in stroke: a review of progress. Clin. EEG Neurosci. 42, 245–252.

