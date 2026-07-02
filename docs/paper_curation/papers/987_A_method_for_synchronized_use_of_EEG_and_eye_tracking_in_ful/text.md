TYPE Brief Research Report PUBLISHED February DOI   .    /fnhum.    .       

OPEN ACCESS

EDITED BY

Jiahui Pan, South China Normal University, China

REVIEWED BY

Jozsef Katona, University of Dunaújváros, Hungary Penghai Li, Tianjin University of Technology, China

*CORRESPONDENCE

Olav F. P. Larsen

olav.f.p.larsen@ntnu.no Emanuel A. Lorenz

emanuel.a.lorenz@ntnu.no

†These authors have contributed equally to this work and share ﬁrst authorship

RECEIVED December ACCEPTED February PUBLISHED February

CITATION

Larsen OFP, Tresselt WG, Lorenz EA, Holt T, Sandstrak G, Hansen TI, Su X and Holt A (    ) A method for synchronized use of EEG and eye tracking in fully immersive VR.

Front. Hum. Neurosci.   :       . doi:   .    /fnhum.    .       

COPYRIGHT

© Larsen, Tresselt, Lorenz, Holt,

Sandstrak, Hansen, Su and Holt. This is an open-access article distributed under the terms of the Creative Commons Attribution

License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# A method for synchronized use of EEG and eye tracking in fully immersive VR

Olav F. P. Larsen *†, William G. Tresselt †, Emanuel A. Lorenz *, Tomas Holt , Grethe Sandstrak , Tor I. Hansen , , Xiaomeng Su and Alexander Holt

Motion Capture and Visualization Laboratory, Department of Computer Science, Faculty of Information Technology and Electrical Engineering, Norwegian University of Science and Technology, Trondheim, Norway, Department of Neuromedicine and Movement Science, Faculty of Medicine and Health Sciences, Norwegian University of Science and Technology, Trondheim, Norway, Department of Acquired Brain Injury, St. Olav’s University Hospital, Trondheim, Norway

This study explores the synchronization of multimodal physiological data streams, in particular, the integration of electroencephalography (EEG) with a virtual reality (VR) headset featuring eye-tracking capabilities. A potential use case for the synchronized data streams is demonstrated by implementing a hybrid steady-state visually evoked potential (SSVEP) based brain-computer interface (BCI) speller within a fully immersive VR environment. The hardware latency analysis reveals an average o set of ms between EEG and eye-tracking data streams and a mean jitter of  .   ms. The study further presents a proof of concept brain-computer interface (BCI) speller in VR, showcasing its potential for real-world applications. The ﬁndings highlight the feasibility of combining commercial EEG and VR technologies for neuroscientiﬁc research and open new avenues for studying brain activity in ecologically valid VR environments. Future research could focus on reﬁning the synchronization methods and exploring applications in various contexts, such as learning and social interactions.

KEYWORDS

electroencephalography, eye-tracking, virtual reality, brain-computer interface, speller, synchronization, SSVEP

## Introduction

In cognitive neuroscience research, the acquisition of multimodal physiological signals has gained prominence in exploring the relationships between behavior and associated cortical activity. This development is promoted by advances in computer science, increasing the accessibility and precision of associated technologies. Fields such as vision research, mobile brain imaging (MoBi), neurorehabilitation, and neuromarketing use multimodal physiological data, achieving ecologically valid insight into the underlying cortical processes (McMullen et al., 2014; King and Parada, 2021; Pereira et al., 2021; Zhu and Lv, 2023).

One frequently employed modality used within cognitive and neuroscience research is optical eye-tracking. This technique allows for the non-invasive tracking of eye movements and gaze ﬁxations, as well as pupillometry using optical sensors like video cameras (Punde et al., 2017). Thus, eye-tracking is a valuable instrument for analyzing behavioral metrics and cognitive processes such as attention, cognitive workload, emotional processing, and memory (Lim et al., 2020; Ryan and Shen, 2020; Vehlen et al., 2021; Pradhan and Kumar, 2022). Beyond its research applications, optical eye-tracking ﬁnds utility

in clinical contexts, such as systematically evaluating strokerelated neurologic deﬁcits, aiding in designing treatment strategies and predicting therapy results (Kaiser et al., 2022). Besides eyetracking specialized for medical and research applications, which achieve high temporal and spatial accuracy, the market has seen a proliferation of cost-eﬀective commercial products (Kapp et al., 2021). In particular, current XR headsets often provide integrated eye-tracking, initially to enhance immersion in gaming experiences (Adhanom et al., 2023). However, open-source solutions exist to access the integrated eye-tracking system for other purposes directly (Tobii, 2023; ValveSoftware, 2023).

In addition to their eye-tracking capabilities, commercial Extended-Reality (XR) headsets are considered valuable tools to provide realistic and, thus, ecologically valid environments within the conﬁnes of a laboratory. The headset can generate the illusion of a three-dimensional world by providing distinct two-dimensional images for each eye. Additionally, the system actively tracks the user’s head position and orientation in space, thus enhancing the immersive experience (Parsons, 2015). Hand-held controllers or hand-tracking technologies ultimately allow for interaction with the virtual environment (Buckingham, 2021). Such immersive displaying techniques increase the user’s engagement toward the visual paradigm and allow for investigating cortical processes within ecologically valid environments (Parsons, 2015; Gall et al.,

- 2021). Thus, it sees increased use for medical applications, such as motor rehabilitation and mental disorders (Srivastava et al., 2014; Feitosa et al., 2022).

Another commonly used modality for evaluating cognitive processes is electroencephalography (EEG). Recently, it has been used more frequently in combination with XR headset application, chosen for its mobility, real-time capabilities, and low-cost point (Ocklenburg and Peterburs, 2023). By amplifying the fast changes in electrical cortical activity recorded over electrodes attached noninvasively to the scalp, it becomes possible to derive corresponding cortical processes at high temporal resolution (Jackson and Bolger, 2014). Cognitive neuroscience research using EEG often utilizes speciﬁc stimuli or behavioral events to evoke an event-speciﬁc cortical activity known as event-related potential (ERP) (Luck, 2012). Given that these events occur within milliseconds, the setup demands exceptionally high temporal resolution. Furthermore, the ERPs mentioned were also used in medical applications, such as brain-computer interfaces (BCI). BCIs are often used as an assistive communication tool e.g., for patients with locked-in syndrome, such as in P300 spellers or steady-state visual evoked potential (SSVEP) spellers that allow patients to communicate based on their cortical response to a presented stimulus (Kundu and Ari,

- 2022). Eye tracking has been combined with EEG in several studies in neuroscience (Langer et al., 2017; Zhu and Lv, 2023), which often employed research-grade eye-tracking devices that enabled seamless integration into the EEG recording with high temporal and spatial accuracy. However, the question remains whether this can be done with easily accessible commercial eyetracking devices, such as those integrated into XR headsets. The use of XR additionally allows for the generation of ecologically valid experimental tasks, which increases the applicability and generalizability of the results (Parsons, 2015).

To fully harness the capabilities of these combined technologies, a deep and comprehensive understanding of

the technical challenges in synchronizing and integrating measurements is crucial. Although hybrid XR headsets with integrated eye-tracking and EEG are being developed, as Neurospec’s DSI-VR300 and OpenBCI’s Galea (AG, 2023; OpenBCI, 2023), their cost and lack of ﬂexibility, such as lack of support to not manufacturer-endorsed applications or highdensity EEG, render them at times ill-suited for a variety of research applications. Thus, various open-source methods were developed recently to allow for synchronized multimodal recordings of research-grade and commercial products, which sometimes lack the capability of hardware synchronization via, e.g., transistortransistor logic (TTL) (Iwama et al., 2022). LabStreamingLayer (LSL) is an often-used middleware ecosystem that enables the streaming and synchronizing of multiple data streams via the network (LabStreamingLayer, 2023). However, LSL can not take the hardware’s intrinsic and the data transfer’s delay and jitter into account. Thus, in cases where high temporal accuracy is required, those delays must be evaluated before the experiment (Artoni et al., 2018; Iwama et al., 2022). This study provides a method for measuring and understanding hardware oﬀset and eventual limitations tailored toward an increasingly relevant combination of EEG, VR, and Eye tracking. We particularly emphasize general accessibility and ﬂexibility through open-source solutions and the use of oﬀ-the-shelf VR-integrated eye tracking.

The objective of this study is, therefore, threefold:

- 1. Present a method for setting up a synchronized measurement of EEG and VR-headset-integrated eye movement and the subsequent real-time processing of the data streams.
- 2. Present a method for evaluating the temporal accuracy of the proposed setup.
- 3. Demonstrate a potential use case of the method using a hybrid SSVEP speller in a fully immersive VR environment.

## Method

The following section provides an overview of the two setups used in this study. The ﬁrst setup was utilized to calculate the latency and jitter of the VR-integrated eye-tracker, while the second setup was employed for the proof of concept SSVEP-Speller. For calculating the hardware latency and jitter of the VR-integrated eye-tracker, the temporal diﬀerence between the measured time points of complete eye closure detected by the eye-tracker and the EMG channel of the EEG ampliﬁer was calculated. The calculated hardware oﬀset is then used for the implementation of a proof of concept SSVEP speller, which uses the eye-tracker to make a preselection of a relevant subsection of a virtual 3D keyboard and the SSVEP response to select a speciﬁc letter.

 .  Hardware latency evaluation

 . .  Experimental setup

The experimental setup for the hardware latency analysis based on eye blinks comprised two computing devices, both running Windows: one desktop computer (PC1; AMD Ryzen 9 5950X, an RTX 3090, and 32GB of DDR4 RAM) running Unity and

Neuropype, and one laptop (PC2) running EEG Recorder (Brain Vision Recorder) software.

 . . .  Set up for collecting electrophysiological data

Electrophysiological data was collected using a Brain Products LiveAmp and Brain Products Trigger Extention Box with a single-channel EMG. The EEG channels were irrelevant for evaluating the hardware latency, as they were recorded using the same hardware. The EEG system operated at a sampling rate of 500 Hz. The participant wore three EMG electrodes at the following positions: one positioned beneath the left eye, one on the temple, and a ground electrode placed under the right ear (Figure 1). The EEG/EMG data stream was consistently transmitted using BrainProduct’s LSLBrainAmpSeries (https:// github.com/brain-products/LSL-BrainAmpSeries) at a sampling rate of 500 Hz from the EEG recorder. Wearing only the EMG and VR headset during synchronization was deemed necessary as the EEG data would not be utilized at this stage, resulting in the ﬁnal setup seen in Figure 1.

 . . .  Setup for collecting behavioral data

Behavioral data was measured using a commercially available HTC VIVE Pro Eye VR headset with an integrated Tobii eyetracker recording at a sample rate of 120 Hz. The eye-tracker’s data stream was transmitted at a sampling rate of 250 Hz from the Unity software environment utilizing LSL4Unity integration (https://github.com/labstreaminglayer/LSL4Unity/, cloned April

- 2023). The eye-tracking data stream contained ﬁve channels of interest, with three of them representing binary values denoting the state of each eye (left, right, or both) in terms of closure, where a value of 1 signiﬁed complete closure. The remaining two channels provided decimal values indicating the degree of eye openness of each eye, with a value of 1 indicating complete eye aperture. This data was retrieved through the TobiiXR (v3.0.1) and SRanipal (1.3.6.8) APIs, respectively.

 . . .  Data handling

The LSL streams, transmitted from Unity (PC1) and the EEG recorder (PC2), were received and processed by PC1. Following this, a dejittering process was applied to these streams to remove irregularities in the timestamps of the data points (Intheon, 2022), facilitated by the dejittering function provided by NeuroPype (Academic Edition v2022.0.1). Subsequently, the processed data streams were saved into ﬁles formatted as Extensible Data Format (XDF), also using the NeuroPype software. As part of the data preprocessing, the EEG stream was downsampled from its original sampling rate of 500 Hz to 250 Hz before storing it. This downsampling operation was performed using the downsampling function within the NeuroPype software.

 . .  Data acquisition

The dataset utilized in this study consists of 661 blinks and was obtained from 4 diﬀerent participants, who received speciﬁc instructions to engage in natural blinking with both eyes. The participants were instructed to synchronize the eye blinks with a metronome at a tempo of 60 beats per minute (BPM). This was

introduced to enhance the interpretability and ease of analysis of the recorded data.

Blink data was collected in sets of 10–20 consecutive blinks. Multiple sets of blinks were captured within a single recording session, and the eye-tracking system underwent recalibration between each successive recording session to maintain data accuracy and consistency. Each recording session captured around ten sets. A few blinks were excluded from the analysis due to instances where the EMG curve was distorted, or the blinks were considered outliers, with a value of more than three times the STD. An example of a distorted EMG curve (Figure S1) can be seen in the Supplementary data.

 . .  Data analysis

Preprocessing of the EMG stream included ﬁltering the EMG signal by applying a zero-phase Butterworth ﬁlter (0.75–5 Hz, 3rd order) (Sharma et al., 2020). The entire analysis was performed using Python (3.11). The signal stream ﬁltering achieves a signal curve that excludes frequencies outside the predeﬁned frequency range. These frequencies would introduce noise and interfere with the accuracy of the signal analysis (Leske and Dalal, 2019). The zero-phase version was applied to correct any signal distortion created by the normal Butterworth ﬁlter (Leske and Dalal, 2019).

The synchronization algorithm operates by aligning two distinct data streams utilizing a standard biological marker, speciﬁcally the occurrence of an eye blink. This synchronization event coincides with the peak observed in the EMG signal and the initiation of a numeric value of “1” within the eye-tracker data stream, signifying the full closure of the eyes. The peak of the EMG curve was deﬁned as the 90% amplitude maximum of the curve, allowing more reliable peak detection corresponding to a full closure of the eye. The TobiiXR API deﬁnes an eye as closed when the numeric value of openness is less than 0.1. It is crucial to emphasize that the analysis was conducted by comparing two data streams, both sampled at a rate of 250 Hz. However, it should be noted that due to the limitations inherent in the eyetracker equipment, achieving a higher temporal accuracy than an index granularity of 8.33 ms (equivalent to 1/120th of a second) was unattainable. The blink recording ﬁles often contained varying quantities of samples. NeuroPype handled the recording of ﬁles, and diﬀerent trimming strategies were employed to address this, where the strategy yielding the minimal STD was selected as the approach for ﬁle recordings of diﬀerent lengths.

 . . .  Algorithm for ﬁnding the o set of a single blink

This algorithm was applied to every blink within each recording. The average oﬀset from each recording session was compared to determine the ﬁnal estimated oﬀset value.

- 1. Input: Data of a single blink in two streams—EEG/EMG and eye-tracker.
- 2. Find the start index of the blink in the eye-tracker stream by locating the ﬁrst numeric value of 1 in the both_blinking channel.
- 3. Filter the EMG channel in the EEG stream using the previously speciﬁed Butterworth ﬁlter.

|[Figure 1]<br><br>FIGURE<br><br>Experimental setup of the synchronization pipeline, showing EEG data being recorded by BrianProducts to PC  and transferred from PC  to PC  using LSL. Simultaneously, eye-tracking data is collected from the VR headset and transmitted directly to PC  via Unity. PC  is responsible for visual and auditory output to the VR headset. The positions of the EMG electrodes are also shown, with the ground electrode placed under the right ear, while the recording electrodes are positioned beneath the left eye, one on the temple. The electrode placement was taken from a study by López ( ).|
|---|

- 4. Locate the index corresponding to the peak of the ﬁltered EMG signal. To account for diﬀerent slope lengths of the diﬀerent blinks, the peak was set to 90% of the peak of the curve.
- 5. Calculate the diﬀerence between the indexes obtained in steps 2 and 4.
- 6. Multiply the index diﬀerence by the sampling rate to compute the oﬀset in milliseconds.

 . . .  Algorithm to ﬁnd mean o set of a series of multiple blinks

This algorithm was applied to all the valid blinks in every recording to ﬁnd an average oﬀset and variance between the EEG and eye-tracker.

- 1. Input: Eye tracking and EEG/EMG data as Python DataFrames.
- 2. Store index of every blink start by ﬁnding each sequence of 1’s in the eye-tracking stream.
- 3. Split the DataFrames into pairs of both streams based on each individual blink and add some data points as padding.
- 4. Use the algorithm for ﬁnding the oﬀset in a single blink, for every blink.
- 5. Use the diﬀerent oﬀsets to compute mean, STD, and average oﬀset for the entire blink recording.
- 6. Do this for multiple recordings that contain multiple blinks and compute the oﬀset.

 .  Proof of concept—BCI speller

Based on the oﬀset found for the synchronization, an SSVEPbased hybrid BCI speller was created in an immersive VR environment in Unity as a proof of concept. This demonstrates a potential use case for the synchronized equipment while being simple to implement. BCI spellers are widely employed BCI applications, encompassing diverse setups. This particular speller leverages SSVEP in conjunction with CCA, avoiding the need for the synchronization of the eye-tracker and EEG to have a millisecond-level precision (Bin et al., 2009; Zerafa et al., 2018). Furthermore, BCI spellers oﬀer the advantage of available comparative results, making it easy to evaluate their performance. Notably, these applications are also relatively straightforward to implement, necessitating no more than a keyboard layout with ﬂickering letters, in contrast to the requirements of more intricate gaming or application systems.

To accommodate the simultaneous use of the VR headset and the EEG recording equipment, the Fp1, F3, F7, F4, F8, and Fp2 electrodes were removed. Additionally, the ground electrode was repositioned to a higher location on the electrode cap. These adjustments were made to increase the comfort of the participant while wearing the VR headset and the EEG cap simultaneously. A participant might use the speller as shown in Figure 2B. The setup of the speller interface was inspired by Du et al. (2019) and Mannan et al. (2020), with clusters of letters that ﬂew out toward the user of the speller when looked at. Mannan et al.

|[Figure 2]<br><br>FIGURE<br><br>(A) Shows the speller setup in the immersive  D VR environment where one of the clusters has been selected and has started to ﬂicker. (B) Shows a person using the speller by holding it up to their face, making sure not to a ect the most critical electrodes over the occipital region.|
|---|

(2020) states that the addition of an eye tracker makes the speller less tiring, and improves performance as compared to EEG only. The eye tracker and clusters enable the reuse of the ﬂickering frequencies, only needing six frequencies for a six-letter cluster, contrary to 30 frequencies for 30 letters and symbols in the speller. Some diﬀerences were introduced, though. By taking a heuristical approach, the frequencies 4 Hz, 5 Hz, 5.5 Hz, 6 Hz, 7 Hz, and 7.4 Hz were chosen for the ﬂickering of the letters, (1) due to lower frequencies eliciting stronger responses (Mannan et al., 2020) and (2) to avoid conﬂicting harmonization. Though the Information Transfer Rate (ITR) gets lower with lower frequencies, it was deemed ok considering the performance of the speller was not the main focus of this project. ITR is a common way to evaluate BCIs and says something about how eﬀective the system is (Liu et al., 2012). Further, the layout of the keyboard was chosen to have a traditional QWERTY layout with some minor diﬀerences to the special characters (Figure 2A).

Some ﬁltering techniques were implemented in a Python script and applied to remove noise and artifacts from the EEG. These include a notch ﬁlter (50 Hz) to remove the line nose, a bandpass ﬁlter (1–15 Hz) to give a reasonable threshold for the chosen ﬂickering frequencies, and a zero-phase Butterworth ﬁlter of 3rd order with some initial padding that was eventually removed to return the signal to its original length. It should also be mentioned that the only electrodes used for the EEG signal were O1, Oz, O2, P3, P7, Pz, P8, and P4, as these are placed over the occipital region of the brain. These electrodes recorded data of the visual stimuli, which was later used to ﬁgure out which letter the participant was looking at.

The ﬁltered EEG data, along with the reference signal that was calculated based on a data stream from Unity signaling when a cluster was ﬂickering, was put in a Canonical Correlation Analysis (CCA) to calculate the similarities between the signals registered in the brain and the plausible ﬂickering values. The calculation was

based on the publication by Mannan et al. (2020) and is a robust way to calculate the correlation between some input signal and a given reference signal. This can be done without training data and without phase sensitivity (Zerafa et al., 2018).

It’s essential to consider an ocular delay in the speller pipeline, which requires adjusting the EEG data accordingly. This delay will be added on top of the computed oﬀset from the synchronization of the pipelines. This additional delay was set to 100 ms, which was retrieved from a study with a similar setup (Mannan et al., 2020), and is necessary due to the time it takes a visual signal entering the eye to be registered in the visual cortex (Li et al., 2015). When applying CCA to assess signal correlations, it’s important to align the signals based on their arrival at the visual cortex rather than at the point when Unity displays the ﬂickering. The speller was tested in two rounds with the same participants, though with a slightly modiﬁed setup in the latter round. Noteworthy improvement was evident during the initial testing phase, leading to the decision to keep the original speller conﬁguration as the proof of concept.

## Results

The following section presents the results from the analysis of the blinking data, showing the diﬀerence in the time it takes to sample a data point in the data streams, including the variance in the mentioned time. Then, the accuracy and Information Transfer Rate (ITR) found during testing of the BCI speller is presented. A graphical explanation of the data stream shifting can be seen in Figures 3A, B as before and after the shift, respectively.

The oﬀset was computed on a dataset with 4 participants, with a cumulative total of 661 individual blinks considered for the analysis. A table containing the results for each participant (Table S2) and the results plotted in a histogram (Histogram S3) can be found in the Supplementary data.

|[Figure 3]<br><br>FIGURE<br><br>An eye blink recorded in both data streams before (A) and after (B), adjusting for o set.|
|---|

TABLE The average ITR and accuracies for the test round for all tested ﬂickering periods.

|Flicker period<br><br>|Accuracy|ITR (bpm)<br><br>|
|---|---|---|
|6s<br><br>|79.83%<br><br>|25.26|
|5s|72.27%<br><br>|24.79|
|4s|57.98%<br><br>|20.43|
|3s<br><br>|51.26%|20.71|
|2s|47.06%<br><br>|23.85|

 .  Eye-tracker–latency and jitter

The data analysis method determined that the average oﬀset between the EEG and eye-tracker is 8–10 indices, equating to 36 milliseconds with the given sampling rate. To be more precise, the eye-tracker was found to be 36 milliseconds faster than the EEG, and thus should be adjusted for this delay accordingly. The STD of the data at its lowest, measured 5.76 ms. This is lower than greater than a single sample (8.33 ms) when considering the limited sampling rate of the eye-tracker, which operates at 120 Hz.

 .  BCI speller–accuracy and ITR

The speller was tested on 7 participants. Even with varying results in accuracy and Information Transfer Rate (ITR), some of the participants were able to use the speller with high accuracy for every ﬂickering length, which supports the proof of concept that it is possible to utilize this combination in an immersive VR environment. The results of the speller’s performance are presented in Table 1. The speller results showed higher accuracy for the longer ﬂickering durations.

## Discussion

The primary strength of this study is the utilization and synchronization of two distinct and powerful oﬀ-the-shelf equipment setups with diﬀerent data processing pipelines, which are all open source. The study demonstrates possible applications for the synchronized equipment by implementing a BCI application in an immersive VR environment, unlike some other variants such as EYE-EEG toolbox which is a bundle for synchronizing some standalone eye trackers with EEGs (EYE-EEG, 2021). Such combined usage has the potential to improve performances in a range of applications. For example, in software engineering, this technology can assess a programmer’s comprehension, as demonstrated in eye-tracking studies (Lin et al., 2016). In engineering science, it measures cognitive load across tasks and participant knowledge levels (Keskin et al., 2020), identiﬁes optimal learning approaches and eﬃciency (Baceviciute et al., 2022). Beyond engineering, applications include neuromarketing (Mashrur et al., 2023; Zhu and Lv, 2023), and safety training utilizing VR, eye tracking, and EEG to evaluate attitudes and learning abilities (Katona, 2014; Comu et al., 2021; Huang et al., 2022).

For the comparison of diﬀerent synchronization methods, to our knowledge no study has yet presented a method for the synchronization of EEG and VR-integrated eye trackers, thus rendering a direct comparison of methods not applicable. There are nonetheless related studies that evaluate the general hardware delay of VR-integrated eye trackers. In a related study, researchers used the Vive Pro Eye with TobiiSDK and electrooculography (EOG) to quantify eye saccades, demonstrating a notable delay in the eye-tracking system (Stein et al., 2021). Their study revealed a mean oﬀset of 50 ms latency in the eye-tracker, alongside an end-to-end delay of 80 ms within their experimental setup (Stein et al., 2021). Similar outcomes were identiﬁed in the present study, where the presented setup displayed an end-to-end oﬀset of 36 ms. The apparent 44 ms variability could potentially be caused by transmission delays inherent in the diﬀerences in the experimental setup. Another aspect of the proposed experimental setup worth mentioning is the accessibility of the pipeline. This particular setup utilized an EMG for recording blinks in the EEG pipeline, but if no EMG is at hand, one could, for example, instead use the frontal electrodes of the EEG to record the same motions. This makes the experimental setup more accessible to a wider audience who might not have all the dedicated equipment to warrant synchronized usage. Given the increasingly widespread usage of BCI-VR systems with eye-tracking (Wen et al., 2021), there will be more cases where such synchronized usage is called upon. Our proposed method presents a ﬂexible and aﬀordable way of synchronizing the needed equipment.

The demand for precise synchronization varies from case to case. A study on the synchronization of EEG-EMG movements combined with motion capture found that even a 10 ms temporal misalignment between the devices can aﬀect causal relationship investigations between EEG-EMG connectivity (Artoni et al., 2018). However, for less strict analyses, such as time-frequency transformations within 0.2 to 0.5-second time windows, synchronization demands can be more relaxed (Artoni et al., 2018). In Iwama et al. (2022), the authors attempted to integrate an EEG and an eye-tracker within an experimental setup similar to our study, and they underscored the importance of synchronized equipment in online applications such as the proof of concept speller, compared to oﬄine analysis where one can adjust the signals accordingly. Large latency between diﬀerent data streams fails to capture state-dependent diﬀerences in the streams, while signiﬁcant jitter in the variable latency can be fatal if the application relies on external triggers, such as a P300 speller (Iwama et al., 2022; Kundu and Ari, 2022). In our study, after measuring the jitter of the setup, we chose a BCI speller based on SSVEP, which is less susceptible to the eﬀects of jitter. It can be argued that an attempt to measure the latency and jitter between equipment should be advocated almost irrespectively because it can unearth and examine the underlining assumptions of hardware performances that subsequently conﬁne and frame the architecture choices of the downstream applications.

Despite limitations in the sampling rate of the equipment, the proof of concept of the BCI Speller demonstrates the potential of the integration of an eye-tracker and an EEG. The speller drew inspiration from conventional SSVEP-based spellers with a keyboard layout. The speller also introduced an eye-tracker improvement by having fewer diﬀerent ﬂickering frequencies and

placing the letters into clusters, resulting in reducing ocular and cognitive strain (Kundu and Ari, 2022). While a previous study has incorporated the combination of eye-tracking and EEG techniques in a BCI speller (Mannan et al., 2020), it is noteworthy that this has predominantly been conﬁned to 2D computer screens. Furthermore, the development of BCI spellers within a VR environment has been documented, although without the inclusion of eye-tracking (Du et al., 2019). This study distinguishes itself because it combines a commercial EEG and a commercial VR headset with eye-tracking capabilities within a hybrid BCI Speller, set in a fully immersive VR environment. Both the accuracy and ITR of the presented BCI speller are lower to comparable stateof-the-art BCI spellers (Wen et al., 2021; Maslova et al., 2023). However, the primary intention of the study is to display the feasibility of the synchronized ecosystem, and this was also the main concern when implementing the speller. Our results indicate that longer ﬂicker periods result in higher classiﬁcation accuracy. This is to be expected as a higher sample count increases the certainty of the CCA’s prediction (da Cruz et al., 2015). However,

- as longer ﬂicker periods negatively impact the ITR, the length of the ﬂicker period must be carefully balanced. Besides a speller, there are other applications that will beneﬁt from the synchronized acquisition of EEG, and eye-tracking in a VR environment, such as observing human eye movement and brain activity during learning, social interactions, or other behavior studies that require an ecologically valid environment but are hard to study “in the wild”.

 .  Limitations

The presented SSVEP-Speller is merely a proof of concept to show case possible application of synchronized EEG and VRintegrated eye tracking. It was chosen due to its robustness and simplicity compared to e.g., P300-Spellers. Retrospectively, our SSVEP-Speller is not highly dependent on perfect hardware oﬀset compensation between the eye tracker and EEG. We, thus, strongly encourage future research to investigate applications that are more sensitive to correct hardware oﬀset correction, such as ﬁxationrelated potentials (Kamienkowski et al., 2012). Further, the impact of correct hardware oﬀset correction, should be quantiﬁed before and after oﬀset adjustment. The presented method for hardware oﬀset and jitter measurements, however, is suitable for diﬀerent applications and experimental setups, due to its ﬂexibility.

It is also worth noting that this is a method paper, to show how ET and EEG can be synchronized in VR, the exact number of oﬀsets we arrive at is of less importance, as it will likely diﬀer when other people use diﬀerent hardware and setups. Future applications should repeat the process, not just use the oﬀset we arrive at, due to hardware and inter-subject diﬀerences.

## Conclusion and future scope

This study successfully demonstrates the possibility of synchronizing the data streams of commercially available equipment, in an accessible and easy-to-use manner with synchronization results on par with similar setups, with a computed jitter of less than 9 ms. To demonstrate the usability of such synchronized equipment an online hybrid SSVEP-based

BCI Speller was implemented as a proof of concept. It is important to note, however, that the method presented is developed for accessibility, and may not be well-suited for more sophisticated EEG and eye-tracking applications. Furthermore, the calculated STD for both data streams exceeds a single sample by 0.44 ms. To ﬁnd the limitations of this method a more exhaustive investigation using equipment characterized by a higher sampling rate is encouraged.

## Data availability statement

Publicly available datasets were analyzed in this study. The repository for the Unity implementation of the BCI Speller and the Unity Blinking environment: https://gitlab.stud.idi.ntnu.no/ group-92/eye-tracking-unity-lsl. The repository for the NeuroPype pipelines the analysis of the blinking data, and the CCA analysis for the speller: https://gitlab.stud.idi.ntnu.no/group-92/neuropypepipeline. YouTube link that showcases the speller in use, spelling “HEI”: https://www.youtube.com/watch?v=s6PwwigH5AA.

## Ethics statement

The studies involving humans were approved by SIKT– Norwegian Agency for Shared Services in Education and Research (975161). The studies were conducted in accordance with the local legislation and institutional requirements. The participants provided their written informed consent to participate in this study. Written informed consent was obtained from the individual(s) for the publication of any potentially identiﬁable images or data included in this article.

## Author contributions

OL: Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing—original draft, Writing—review & editing. WT: Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing—original draft, Writing—review & editing. EL: Conceptualization, Methodology, Project administration, Resources, Supervision, Writing—review & editing. TH: Project administration, Resources, Writing—review & editing. GS: Project administration, Resources, Writingreview & editing. TIH: Writing—review & editing. XS: Project administration, Resources, Writing—review & editing. AH: Project administration, Resources, Writing—review & editing, Conceptualization, Methodology, Supervision.

## Funding

The author(s) declare that no ﬁnancial support was received for the research, authorship, and/or publication of this article.

## Acknowledgments

The authors would like to thank the participants who took part in the testing of the speller.

## Conﬂict of interest

The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their aﬃliated

organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fnhum. 2024.1347974/full#supplementary-material

## References

Adhanom, I. B., MacNeilage, P., and Folmer, E. (2023). Eye tracking in virtual reality: a broad review of applications and challenges. Virt. Real. 27, 1481–1505. doi: 10.1007/s10055-022-00738-z

AG, N. (2023). DSI-VR300. Available online at: https://www.neurospec.com/ Products/Details/1077/dsi-vr300 (accessed October 30, 2023).

Artoni, F., Barsotti, A., Guanziroli, E., Micera, S., Landi, A., and Molteni, F. (2018). Eﬀective synchronization of EEG and EMG for mobile brain/body imaging in clinical settings. Front. Hum. Neurosci. 11:652. doi: 10.3389/fnhum.2017.00652

Baceviciute, S., Lucas, G., Terkildsen, T., and Makransky, G. (2022). Investigating the redundancy principle in immersive virtual reality environments: an eyetracking and EEG study. J. Comput. Assist. Learn. 38, 120–136. doi: 10.1111/jcal. 12595

Bin, G., Gao, X., Yan, Z., Hong, B., and Gao, S. (2009). An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method. J. Neural Eng. 6:046002. doi: 10.1088/1741-2560/6/4/046002

Buckingham, G. (2021). Hand tracking for immersive virtual reality: opportunities and challenges. Front. Virtual Real. 2:728461. doi: 10.3389/frvir.2021.728461

Comu, S., Kazar, G., and Marwa, Z. (2021). Evaluating the attitudes of diﬀerent trainee groups towards eye tracking enhanced safety training methods. Adv. Eng. Inform. 49:101353. doi: 10.1016/j.aei.2021.101353

da Cruz, J. N., Wan, F., Wong, C. M., and Cao, T. (2015). Adaptive timewindow length based on online performance measurement in SSVEP-based BCIs. Neurocomputing, 149, 93–99. doi: 10.1016/j.neucom.2014.01.062

Du, J., Ke, Y., Kong, L., Wang, T., He, F., and Ming, D. (2019). “3D stimulus presentation of ERP-speller in virtual reality,” in 2019 9th International IEEE/EMBS Conference on Neural Engineering (NER), 167–170. ISSN: 1948–3554. doi: 10.1109/NER.2019.8717164

EYE-EEG (2021). EYE-EEG: Combining Eye Tracking EEG. Feitosa, J. A., Fernandes, C. A., Casseb, R. F., and Castellano, G. (2022). Eﬀects of

virtual reality-based motor rehabilitation: a systematic review of fMRI studies. J. Neur. Eng. 19:011002. doi: 10.1088/1741-2552/ac456e

Gall, D., Roth, D., Stauﬀert, J.-P., Zarges, J., and Latoschik, M. E. (2021). Embodiment in virtual reality intensiﬁes emotional responses to virtual stimuli. Front. Psychol. 12:674179. doi: 10.3389/fpsyg.2021.674179

Huang, D., Wang, X., Liu, J., Li, J., and Tang, W. (2022). Virtual reality safety training using deep EEG-net and physiology data. Visual Comput. 38, 1195–1207. doi: 10.1007/s00371-021-02140-3

Intheon, N. (2022). Neuropype by Intheon: DejitterTimeStamps. Available online

- at: https://www.neuropype.io/docs/nodes/utilities.html#dejittertimestamps (accessed October 30, 2023).

Iwama, S., Takemi, M., Eguchi, R., Hirose, R., Morishige, M., and Ushiba, J. (2022). Two common issues in synchronized multimodal recordings with EEG: Jitter and Latency. Neurosci. Res. 2022:518625. doi: 10.1101/2022.11.30.518625

Jackson, A. F. and Bolger, D. J. (2014). The neurophysiological bases of EEG and EEG measurement: a review for the rest of us. Psychophysiology 51, 1061–1071. doi: 10.1111/psyp.12283

Kaiser, A. P., Villadsen, K. W., Samani, A., Knoche, H., and Evald, L. (2022). Virtual reality and eye-tracking assessment, and treatment of unilateral spatial neglect: systematic review and future prospects. Front. Psychol. 13:787382. doi: 10.3389/fpsyg.2022.787382

Kamienkowski, J. E., Ison, M. J., Quiroga, R. Q., and Sigman, M. (2012). Fixationrelated potentials in visual search: a combined EEG and eye tracking study. J. Vision 12:4. doi: 10.1167/12.7.4

Kapp, S., Barz, M., Mukhametov, S., Sonntag, D., and Kuhn, J. (2021). ARETT: augmented reality eye tracking toolkit for head mounted displays. Sensors 21:2234. doi: 10.3390/s21062234

Katona, J. (2014). “The comparison of the non-invasive mobile EEG registration and the signal processing devices,” in Informatika terek (DUF Press), 97–110.

Keskin, M., Ooms, K., Dogru, A. O., and De Maeyer, P. (2020). Exploring the cognitive load of expert and novice map users using EEG and eye tracking. ISPRS Int. J. Geo-Inform. 9:429. doi: 10.3390/ijgi9070429

King, J. L. and Parada, F. J. (2021). Using mobile brain/body imaging to advance research in arts, health, and related therapeutics. Eur. J. Neurosci. 54, 8364–8380. doi: 10.1111/ejn.15313

Kundu, S. and Ari, S. (2022). Brain-computer interface speller system for alternative communication: a review. IRBM, 43, 317–324. doi: 10.1016/j.irbm.2021.07.001

LabStreamingLayer (2023). LabStreamingLayer. Available online at: https://github. com/sccn/labstreaminglayer (accessed October 30, 2023).

Langer, N., Ho, E. J., Alexander, L. M., Xu, H. Y., Jozanovic, R. K., Henin, S., et al.

(2017). A resource for assessing information processing in the developing brain using EEG and eye tracking. Sci. Data 4:170040. doi: 10.1038/sdata.2017.40

Leske, S. and Dalal, S. S. (2019). Reducing power line noise in EEG and MEG data via spectrum interpolation. NeuroImage 189, 763–776. doi: 10.1016/j.neuroimage.2019.01.026

Li, F., Tian, Y., Zhang, Y., Qiu, K., Tian, C., Jing, W., et al. (2015). The enhanced information ﬂow from visual cortex to frontal area facilitates SSVEP response: evidence from model-driven and data-driven causality analysis. Sci. Rep. 5:14765. doi: 10.1038/srep14765

Lim, J. Z., Mountstephens, J., and Teo, J. (2020). Emotion recognition using eye-tracking: taxonomy, review and current challenges. Sensors 20:2384. doi: 10.3390/s20082384

Lin, Y.-T., Wu, C.-C., Hou, T.-Y., Lin, Y.-C., Yang, F.-Y., and Chang, C.-H. (2016). Tracking students cognitive processes during program debugging an eye-movement approach. IEEE Trans. Educ. 59, 175–186. doi: 10.1109/TE.2015.2487341

Liu, Y., Jiang, X., Cao, T., Wan, F., Mak, P. U., Mak, P.-I., et al. (2012). “Implementation of SSVEP based BCI with Emotiv EPOC,” in 2012 IEEE International Conference on Virtual Environments Human-Computer Interfaces and Measurement Systems (VECIMS) Proceedings 34–37. doi: 10.1109/VECIMS.2012.6273184

López, N. (2015). Hybrid human-machine interface to mouse control for severely disabled people. Int. J. Eng. Innov. Technol. 4, 164–171.

Luck, S. J. (2012). “Event-related potentials,” in APA handbook of research methods in psychology, Vol 1: Foundations, planning, measures, and psychometrics, APA handbooks in psychology (Washington, DC: American Psychological Association), 523–546. doi: 10.1037/13619-028

Mannan, M. M. N., Kamran, M. A., Kang, S., Choi, H. S., and Jeong, M. Y. (2020). A hybrid speller design using eye tracking and SSVEP brain computer interface. Sensors, 20:891. doi: 10.3390/s20030891

Mashrur, F. R., Rahman, K. M., Miya, M. T. I., Vaidyanathan, R., Anwar, S. F., Sarker, F., et al. (2023). Intelligent neuromarketing framework for consumers’ preference prediction from electroencephalography signals and eye tracking. J. Consumer Behav. 10:2253. doi: 10.1002/cb.2253

Maslova, O., Komarova, Y., Shusharina, N., Kolsanov, A., Zakharov, A., Garina, E., et al. (2023). Non-invasive EEG-based BCI spellers from the beginning to today: a mini-review. Front. Hum. Neurosci. 17:1216648. doi: 10.3389/fnhum.2023.1216648

McMullen, D. P., Hotson, G., Katyal, K. D., Wester, B. A., Fifer, M. S., McGee, T. G., et al. (2014). Demonstration of a semi-autonomous hybrid brain machine

interface using human intracranial EEG, eye tracking, and computer vision to control a robotic upper limb prosthetic. IEEE Trans. Neural Syst. Rehabilit. Eng. 22, 784–796. doi: 10.1109/TNSRE.2013.2294685

Ocklenburg, S. and Peterburs, J. (2023). “Monitoring brain activity in VR: EEG and neuroimaging,” in Virtual Reality in Behavioral Neuroscience: New Insights and Methods, Current Topics in Behavioral Neurosciences, eds. C. Maymon, G. Grimshaw, and Y. C. Wu (Cham: Springer International Publishing), 47–71. doi: 10.1007/7854_2023_423

OpenBCI (2023). Galea. Available online at: https://galea.co (accessed October 30, 2023).

Parsons, T. D. (2015). Virtual reality for enhanced ecological validity and experimental control in the clinical, aﬀective and social neurosciences. Front. Hum. Neurosci. 9:660. doi: 10.3389/fnhum.2015.00660

Pereira, J., Kobler, R., Ofner, P., Schwarz, A., and Müller-Putz, G. R. (2021). Online detection of movement during natural and self-initiated reach-and-grasp actions from EEG signals. J. Neural Eng. 18:046095. doi: 10.1088/1741-2552/ac0b52

Pradhan, A. and Kumar, E. (2022). “Cognitive workload estimation using eye tracking: a review,” in Advancements in Interdisciplinary Research, Communications in Computer and Information Science, eds. V. Sugumaran, D. Upadhyay, and S. Sharma (Cham: Springer Nature Switzerland), 544–552. doi: 10.1007/978-3-031-23724-9_49

Punde, P. A., Jadhav, M. E., and Manza, R. R. (2017). “A study of eye tracking technology and its applications,” in 2017 1st International Conference on Intelligent Systems and Information Management (ICISIM) 86–90. doi: 10.1109/ICISIM.2017.8122153

Ryan, J. D. and Shen, K. (2020). The eyes are a window into memory. Curr. Opin. Behav. Sci. 32, 1–6. doi: 10.1016/j.cobeha.2019.12.014

Sharma, K., Jain, N., and Pal, P. K. (2020). Detection of eye closing/opening from EOG and its application in robotic arm control. Biocyber. Biomed. Eng. 40, 173–186. doi: 10.1016/j.bbe.2019.10.004

Srivastava, K., Das, R. C., and Chaudhury, S. (2014). Virtual reality applications in mental health: challenges and perspectives. Ind. Psychiat. J. 23:83. doi: 10.4103/0972-6748.151666

Stein, N., Niehorster, D. C., Watson, T., Steinicke, F., Rifai, K., Wahl, S., et al. (2021). A comparison of eye tracking latencies among several commercial head-mounted displays. i-Percept. 12:2041669520983338. doi: 10.1177/20416695209 83338

Tobii (2023). Tobii XR API. Available online at: https://developer.tobii.com/xr/ (accessed October 30, 2023).

ValveSoftware (2023). ValveSoftware/openvr. Available online at: https://github. com/ValveSoftware/openvr (accessed October 30, 2023).

Vehlen, A., Spenthof, I., Tönsing, D., Heinrichs, M., and Domes, G. (2021). Evaluation of an eye tracking setup for studying visual attention in face-to-face conversations. Sci. Rep. 11:2661. doi: 10.1038/s41598-021-81987-x

Wen, D., Liang, B., Zhou, Y., Chen, H., and Jung, T.-P. (2021). The current research of combining multi-modal brain-computer interfaces with virtual reality. IEEE J. Biomed. Health Inform. 25, 3278–3287. doi: 10.1109/JBHI.2020.3047836

Zerafa, R., Camilleri, T., Falzon, O., and Camilleri, K. P. (2018). To train or not to train? A survey on training of feature extraction methods for SSVEP-based BCIs. J. Neural Eng. 15:051001. doi: 10.1088/1741-2552/aaca6e

Zhu, L. and Lv, J. (2023). Review of studies on user research based on EEG and eye tracking. Appl. Sci. 13:6502. doi: 10.3390/app13116502

