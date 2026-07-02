# Europe PMC Funders Group

#### Author Manuscript Neuroimage. Author manuscript; available in PMC 2018 February 15.

Published in final edited form as:

Neuroimage. 2017 February 15; 147: 130–142. doi:10.1016/j.neuroimage.2016.12.004.

[Figure 1]

# Decoding hand gestures from primary somatosensory cortex using high-density ECoG

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

##### Mariana P. Branco1, Zachary V. Freudenburg1, Erik J. Aarnoutse1, Martin G. Bleichner2, Mariska J. Vansteensel1, and Nick F. Ramsey1,*

1Brain Center Rudolf Magnus, Department of Neurology and Neurosurgery, University Medical Center Utrecht, Utrecht, the Netherlands 2Neuropsychology Lab, Department of Psychology, Cluster of Excellence Hearing4all, University of Oldenburg, Oldenburg, Germany

## Abstract

Electrocorticography (ECoG) based Brain-Computer Interfaces (BCIs) have been proposed as a way to restore and replace motor function or communication in severely paralyzed people. To date, most motor-based BCIs have either focused on the sensorimotor cortex as a whole or on the primary motor cortex (M1) as a source of signals for this purpose. Still, target areas for BCI are not confined to M1, and more brain regions may provide suitable BCI control signals. A logical candidate is the primary somatosensory cortex (S1), which not only shares similar somatotopic organization to M1, but also has been suggested to have a role beyond sensory feedback during movement execution. Here, we investigated whether four complex hand gestures, taken from the American sign language alphabet, can be decoded exclusively from S1 using both spatial and temporal information. For decoding, we used the signal recorded from a small patch of cortex with subdural high-density (HD) grids in five patients with intractable epilepsy. Notably, we introduce a new method of trial alignment based on the increase of the electrophysiological response, which virtually eliminates the confounding effects of systematic and non-systematic temporal differences within and between gestures execution. Results show that S1 classification scores are high (76%), similar to those obtained from M1 (74%) and sensorimotor cortex as a whole (85%), and significantly above chance level (25%). We conclude that S1 offers characteristic spatiotemporal neuronal activation patterns that are discriminative between gestures, and that it is possible to decode gestures with high accuracy from a very small patch of cortex using subdurally implanted HD grids. The feasibility of decoding hand gestures using HD-ECoG grids encourages further investigation of implantable BCI systems for direct interaction between the brain and external devices with multiple degrees of freedom.

[Figure 2]

##### Keywords

Brain-Computer Interface; Decoding; Electrocorticography; Primary motor cortex; Primary somatosensory cortex

*Corresponding author: N.F. Ramsey. Brain Center Rudolf Magnus, Department of Neurology and Neurosurgery, Division of Neuroscience, University Medical Center Utrecht, Room G.03.124, Heidelberglaan 100, 3584 CX, Utrecht, the Netherlands. N.F.Ramsey@umcutrecht.nl.

[Figure 3]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 4]

## 1 Introduction

The research of Brain-Computer Interface (BCI) systems for restoring and replacing motor function or communication in severely paralyzed people has increased significantly in the last decades (Daly and Wolpaw, 2008; Miller and Hatsopoulos, 2012). To date, most BCI studies have focused on the sensorimotor cortex (Brodmann areas, BA, 1-4) (Yuan and He, 2014), which is known to have a direct relationship with movement execution, attempt and imagery (Hochberg et al., 2006; Leuthardt et al., 2004; Miller et al., 2009b, 2010; Pistohl et al., 2008). The sensorimotor cortex can be divided into the primary motor cortex (M1, BA4) and the primary somatosensory cortex (S1, BA1-3). Both areas are somatotopically organized (Penfield and Boldrey, 1937) and provide rich spatial detail that could be exploited for BCIs with multiple degrees-of-freedom. In particular, a distinct portion of M1 denoted the “hand knob” has been proven to directly control hand movements (Yousry et al.,

1997) and there is strong evidence from micro-array and needle recordings from both nonhuman primate (Georgopoulos et al., 1986) and human (Hochberg et al., 2006) studies that this region allows decoding of arm and hand motor movements.

Even though M1 has been the main target for motor-related BCI control studies, S1 would be a logical alternative candidate due to its somatotopic organization. On the one hand, S1 is known to be related to afferent signal processing in humans, mostly present during touch, proprioception and pain perception (Martuzzi et al., 2014; Stringer et al., 2014). On the other hand, there is evidence for a role of sensory information during movement execution and attempted movement (Cramer et al., 2005; Kikkert et al., 2016). Recent predictive and feedback models for voluntary control, for example, suggest that there may be driving connections from S1 to M1 (Adams et al., 2012; Scott, 2012), providing good reason to believe that S1 would encode similar topographical activation patterns as M1 during movement execution and attempted movement tasks, and thus be a potential target for future BCIs.

Several studies in humans have shown successful decoding of hand related tasks from the sensorimotor cortex (M1 and S1 combined) using subdurally implanted electrodes (electrocorticography, ECoG) (Chestek et al., 2013; Kubánek et al., 2009; Miller et al., 2009b; Pistohl et al., 2011; Schalk et al., 2007), but so far, only one study (Chestek et al.,

2013) has indicated that S1 alone may provide informative signals for BCI purposes. In these studies, standard clinical grids were used, which cover a relatively large area of cortex with spatial resolution of one electrode (or small clusters of microelectrodes) per cm2. Notably, we have previously shown that motor representations of the different fingers are located within an area of about 1 cm2 (Siero et al., 2014), meaning that standard clinical grids fail to capitalize on the spatial detail of this cortical feature. Additionally, decoding from large regions of cortex that extend widely beyond the topographical representation associated with the movement of interest (e.g., “hand knob” for hand movements), makes it unclear what cortical functions are involved in decoding.

In the present study, we specifically address the question whether hand movements can be decoded from the S1 hand region alone. We investigate whether four complex hand gestures, previously shown by our group to be spatially decodable from the sensorimotor cortex as a

[Figure 5]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 6]

whole (Bleichner et al., 2014), can be decoded exclusively from S1 using both spatial and temporal information. Additionally, in order to investigate whether the S1 discriminative neuronal information is decoupled from sensory feedback, we analyzed the spatiotemporal response prior to movement onset. To prevent spatial undersampling, we used grids with a high-density of electrodes (9/cm2). We focus on the high-frequency broadband or gammaband power change of the ECoG signal (70-125 Hz) (Crone et al., 1998; K. Miller et al., 2009a; Miller et al., 2009b), which has been shown to have a time-locked response to motor execution, is commonly spatially specific (Buzsáki and Wang, 2012; Hermes et al., 2012; Siero et al., 2014), and allows for optimal decoding of hand gestures (Bleichner et al., 2014). In short, in the current study, we compare the classification scores based on spatiotemporal gamma-band features between high-density-ECoG electrodes localized over S1, M1 and both M1 and S1 (sensorimotor cortex). Additionally, we introduce a new method for trial realignment that minimizes confounding effects caused by the temporal differences in the electrophysiological response to the task.

## 2 Materials and Methods

2.1 Subjects Subjects of the study were five patients (mean age 31, range 19-45; see Table 1) with intractable epilepsy who were implanted with subdural ECoG grids to localize the seizure focus. This study was approved by the Medical Ethical Committee of the Utrecht University Medical Center. All patients signed informed consent according to the Declaration of Helsinki (2008).

Both standard clinical ECoG and high-density ECoG grids were implanted. Standard ECoG grids had an inter-electrode distance center-to-center of 1 cm and 2.3 mm exposed surface diameter (AdTech, Racine, USA). High-density grids had either 32 or 64 channels, with 1.3 mm exposed surface diameter and an inter-electrode distance of 3 mm center to center (AdTech, Racine, USA). The 32-channel grid covered an area of 2.5 cm2 (4x8 electrode layout), whereas the 64-channel grid covered an area of 5.2 cm2 (8x8 electrode layout).

The current study focuses only on the high-density grids that covered (parts of) the sensorimotor cortex (see Table 1 for details), including the hand knob region. Some electrodes were excluded from the analysis due to technical problems (e.g., a broken lead, causing flat or unstable signals) or high power-line noise level. Notably, for none of the patients, the epileptic focus overlapped with the hand knob region. For each subject, the electrodes (Table 1) were localized using co-registration between a high resolution postimplantation Computerized Tomography (CT) scan (Philips Tomoscan SR7000, Best, the Netherlands) and a pre-operative T1-weighed anatomical scan on a 3T Magnetic Resonance system (Philips 3T Achieva, Best, the Netherlands) with algorithms published in (Hermes et al., 2010) and displayed on a cortex surface rendering (Figure 1). By visual inspection, the projected electrodes anterior to central sulcus were labeled as M1 electrodes, whereas the ones posterior to central sulcus were labeled S1 electrodes. Electrodes over the central sulcus were labeled according to the closest gyrus.

[Figure 7]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 8]

##### 2.2 Task

The task (Figure 2), as described in (Bleichner et al., 2014), involved the execution of four different hand gestures (G1, G2, G3 and G4), which were taken from the American Sign Language finger spelling alphabet (‘D’, ‘F’, ‘V’ and ‘Y’, respectively). The participants were asked to copy the gesture presented on the screen using the hand contralateral to grid implantation and hold it for 6 seconds. The trials were interleaved with a rest condition (6 seconds), where the subject was asked to place their hand in a relaxed open hand position. Each run consisted of 40 gesture trials of randomly presented gestures (10 times per gesture) and 41 rest trials. Participant 5 performed two (equal) runs. All subjects had their gestures recorded by a data glove (5DT Inc., Irvine, USA) for performance verification, based on which incongruent or erroneous trials (i.e., performing an incorrect or no gesture, moving additional fingers or correcting the gesture) were excluded from the analysis.

##### 2.3 ECoG acquisition and preprocessing

ECoG signals were continuously recorded using a 128 channel Micromed system (Treviso, Italy; 22 bits, hardware band-pass filter 0.15-134.4 Hz) with 512 Hz sampling frequency. The data was analyzed offline and preprocessed using the open source FieldTrip® toolbox (Oostenveld et al., 2010) for MATLAB® (MathWorks Inc.) as follows: first, the continuous data were filtered using a notch filter (center at 50 and 100 Hz) and re-referenced using the common average reference (CAR) of all included high-density electrodes facing the surface

[Figure 9]

of the brain second, the data were divided into trials that were aligned using an electrophysiology marker, as described in section 2.5

##### 2.4 Feature extraction

The gamma-band power trace was extracted using a Morlet wavelet dictionary, with multiplication in the frequency domain (length equal to 3 standard deviations of the implicit Gaussian kernel and width 7 cycles), as implemented in FieldTrip® Toolbox. The power was extracted with a temporal resolution of one sample every 0.01 s and subsequently smoothed using a moving average filter with a window size of 0.5 s. For each trial, the mean power over the gamma-band frequency bins (70-125 Hz) was calculated per channel, for a time window of -1 to 2.6 s (see Supplementary Figure 1 for the effect of different time windows on the classification scores) around an electrophysiology marker (see following section for more details). The resulting feature space is a three-dimensional matrix (channels x time x trials) per gesture. Notably, the intrinsic wavelet duration per time sample for the frequency range we used (70-125 Hz) varies between 18 ms (for 125 Hz) and 32 ms (for 70 Hz). Therefore, the maximum expected temporal “leakage” is 16 ms.

##### 2.5 Trial alignment

The alignment of trials is a crucial step for classification of labeled events using not only spatial, but also temporal features. There are two potential sources of error when considering temporal (mis)alignment. First, jitter across trials for a given gesture causes blurring of spatiotemporal patterns used for classification (based on the averagedgamma-band power trace) leading to an underestimation of classification. Second, systematic differences

[Figure 10]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 11]

between gestures in finger movement order or in speed of movement may inflate classification by introducing differences in gamma-band responses onsets (see Supplementary Figure 2). Here, we developed a method of trial alignment that virtually eliminates these confounding effects by using the broadband gamma-band electrophysiological response to the task. The method detects the averaged gamma-band electrophysiological response to the task across channels (i.e., not specific to channels) and is described in detail below.

The implemented method is subject-specific and consists of three steps. First, we identified the channels that were involved in performing the task, more specifically, we selected the channels with a significant response to the task (i.e., that responded to all four gestures). A channel was considered to have significant activity when the mean power across trials was significantly different between task and rest periods (independent t-test, p < 0.05 uncorrected). The task period was manually centered on the gamma-band peak, while the rest period was taken before the gesture’s cue. Note that this step does not bias the classification measures in the subsequent analysis since all gestures are included and it is only used to select channels used for the extraction of the new marker.

Second, we applied an algorithm for extracting a marker (t0) based on the slope of the gamma-band power response. To do so, the gamma-band power trace was calculated per trial by averaging over the channels with significant response (previous step) and provisionally smoothed until the response revealed a peak with a clear rising slope (Figure 3A). Subsequently, the horizontal distance between a sliding line segment S(k) and the epoched trace F(n) was calculated for every position ni of the line segment (Figure 3B). The line segment S(k) is a unique set of amplitude values of F(n), with n denoting the discrete time points in the epoched interval, defined as:

[Figure 12]

(1)

where mis the slope of S(k), k is the set of domain values such that S(k) is limited by the range [smin, smax] of the trace F(n), and ni is the x-intercept of S(k). The line segment’s slope, m, is subject-specific (constant parameter) and was determined so that it fitted the subject’s average response. The horizontal distance, dni(k), between S(k) and F(n) was calculated for every point of S(k) by subtracting the abscissa values of points with equal ordinate (2). The overall distance between the line segment and the trace for a given ni, D(ni) (Figure 3C), was defined by the summation across all distances dni(k) which were smaller than a thresholdεni (3). This value was also subject-specific and defined according to the domain of S(k).

[Figure 13]

(2)

[Figure 14]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 15]

[Figure 16]

(3)

The gamma-slope marker (GSM) t0 (Figure 3D) was, then, mathematically calculated by extracting the midpoint of the line segment Sb(k) that best fits the trace F(n) using:

[Figure 17]

- (4)

[Figure 18]

- (5)

[Figure 19]

(6)

where b is the position where the trace best matches the line segment, smin and smax are the minimum and maximum values of the line segment, respectively, and the marker t0 is the midpoint of the line segment. In this step, three empirical parameters were defined per subject, the power trace smoothing, the slope m and the threshold valueεni. Both the smoothing value and threshold were defined through visual inspection, while the slope was determined as a fraction of the maximum amplitude of the trace.

Third, we aligned all (unsmoothed) trials using the new GSM t0 = 0 s (Figure 4). The aligned trials were epoched into segments of 3.6 s around t0 (-1 to 2.6 s; see section 2.4). Since the alignment was based on the mean gamma-band trace over all significant channels as opposed to separate channels, any time differences between channels were preserved. The gamma-band power trial alignment method was performed only once and considered all included channels of each subject, and was therefore not dependent on the electrode M1/S1 grouping.

2.6 Feature Classification Gesture data were classified using a spatiotemporal template matching correlation with a leave-one-out cross-validation scheme. This straightforward classification method has previously yielded robust results when used to discriminate spatial patterns (Bleichner et al., 2014). In fact, it showed similar results as other frequently used state-of-the-art classifiers, such as the regularized latent discriminant analysis method (Bleichner et al., 2014), but is computationally easier to use. Here we extended this method to spatiotemporal patterns.

As already described above, the feature space consisted of a three-dimensional matrix per gesture, where channels, time and trials were the three dimensions. For each gesture the average activation pattern (hereafter referred to as spatiotemporal template, Figure 5) was computed by averaging the feature space over trials, excluding the single trial that was to be

[Figure 20]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 21]

classified. This resulted in one 2D (i.e., channels x time) spatiotemporal template per gesture. The single trial spatiotemporal feature was then compared with the four templates (one per gesture) by mean of Pearson Correlation (between each spatiotemporal template feature and each trial feature) and labeled as the gesture (spatiotemporal template) with which it had the highest correlation score. The classification accuracy was defined as the percentage of correctly labeled trials. In order to compare classification scores between electrodes on the primary motor cortex (M1), electrodes on the primary somatosensory cortex (S1) and the combination thereof, the classification step was repeated using all (sensorimotor) electrodes, only M1 electrodes and only S1 electrodes (Figure 1). The most informative electrodes were estimated by calculating the contribution of each individual electrode for classification. For this purpose, the classification accuracy was re-computed using combinations of increasing number of electrodes. The set sizes varied from an individual electrode to all electrodes. For each set size the classification accuracy was computed using up to 1000xN random combinations of electrodes, where N is total number of electrodes. Note that for the set sizes with less than 1000xN possible combinations, all possible electrode combinations were used. The contribution of each individual electrode was then computed based on the average classification achieved when that electrode was part of the combination.

Lastly, the classification chance level was computed both by randomly permuting the observations across classes (as many times as possible permutations) and by feeding the classifier with generated zero-mean Gaussian white noise (Combrisson and Jerbi, 2015). The former resulted in a chance level of 23.68±0.84% and the latter in 25.01±1.30%. The statistical significance level of decoding (mean across subjects 39.17±1.17%) was determined by the 95th percentile (p < 0.05) of the empirical distribution obtained by randomly permuting the data (Combrisson and Jerbi, 2015). Hence, for the purpose of the present study the theoretical chance level of 25% (for four classes) and the significance level of 40% are adequate and will be used.

Notably, since subject 5 performed two runs, we could also assess the reproducibility of the results. This was tested by using one of the two runs as a template in the cross-validation step. Both combinations (template run 1, test run 2 and template run 2, test run 1) were performed using each of the three electrode selections, i.e., all sensorimotor, only M1 and only S1 electrodes.

2.7 Timing of M1 and S1 responses In order to understand the basis of the discriminative information comprised in the primary motor and somatosensory cortices, and to investigate whether S1 comprises pertinent neuronal information decoupled from the movement-induced sensory feedback, we performed an extra analysis in which we analyzed the increase in broadband activity prior to movement onset. For this particular purpose, epoched data were re-aligned using movement onset markers. The latter were determined, per trial, by visual inspection, as being the time point preceding the one of the first finger to move in the data glove traces.

[Figure 22]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 23]

## 3 Results

##### 3.1 Task performance and gamma-band response

Overall, the task performance, as measured by the data glove traces, of the five subjects was quite reliable. Per individual, only a maximum 7 trials out of a total of 40 trials (Table 2) were excluded, due to the execution of an incorrect gesture, either by moving additional fingers or correcting the gesture. In most subjects, changes in the data glove traces occurred shortly after the gamma slope marker (Figure 6 and Supplementary Figure 3). Inspection of the timing of the mean gamma-band response, the cue and movement onset indeed revealed that the movement onset occurred consistently after the cortical activity onset – approximately one second after the cue, half a second after the gamma-band activity onset and shortly after the gamma-band peak in activity (Supplementary Figure 4).

Spatiotemporal gamma-band traces per gesture aligned using the GSM (Figure 7A), show different spatial and temporal signatures per gesture, which could allow for decoding. In particular, when zooming in into two visibly responsive channels over M1 and S1 areas (Figure 7B), one can appreciate the fact that the temporal features provide additional valuable information for decoding besides spatial features (i.e., difference between channels).

##### 3.2 Classification results

All classification scores (Figure 8A) were significantly above chance level (p < 0.05). Subjects who had sufficient coverage of M1 and S1 (subject 2, 3 and 5) showed accurate classification for each region individually. The average classification over the sensorimotor cortex (all electrodes of subjects 2, 3 and 5) was 85.0%, over S1 (subjects 1, 2, 3 and 5) 76.25% and over M1 (subjects 2, 3, 4 and 5) 74.63% (Figure 8B). There was no significant difference between the scores of the three conditions (sensorimotor, M1 and S1 electrodes; N = 3, subject 2, 3 and 5) as assessed by a Friedman’s test for one-way repeated measures with non-parametric data, χ2(2) = 3.20, ns. The variation in scores between subjects can be mostly explained from the grid coverage of M1 and S1 (Figure 1), since the lowest M1 (subject 5) and S1 (subject 2) scores were from the patients with the lowest number of electrodes over M1 (11 electrodes, compared with 15 or more in all other cases) and S1 (9 electrodes, compared with 15 or more in all other cases), respectively (Table 1).

Reproducibility of the classification results for the three electrode selections (sensorimotor, M1 and S1) was tested using the two runs of subject 5. Two combinations of test and experimental datasets were used: 1) derive the template from run 1 and classify run 2, and 2) derive the template from run 2 and classify run 1. Results (Table 3) show good reproducibility of the classification across runs of the same subject, suggesting that the gestures pattern encoded in the sensorimotor cortex can be well discriminated across sessions using high-density ECoG grids.

For the subjects with sensorimotor (both M1 and S1) coverage (subjects 2, 3 and 5) the most informative electrodes (Figure 9) appeared to be distributed over both the M1 and S1 areas, indicating that S1 may offer discrimination features as good as M1 to distinguish between the four gestures on this spatial-temporal scale. In particular, subject 3, who had the most

[Figure 24]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 25]

extensive hand knob coverage and the highest performance, showed four ‘most informative’ electrodes, two over M1 and two other over S1. Note that, even when a single electrode cannot be considered ‘most informative’, it still may be essential for accurate classification. Indeed, the decoding accuracy has been shown to increase with the number of electrodes used for classification (Bleichner et al., 2014).

3.3 Timing of M1 and S1 responses The results above indicate that S1 contains sufficient neuronal information to discriminate between four hand gestures. However, the nature of this S1 neural information also plays an important role, especially for BCI applications, where end-users may lack sensory feedback. Hence, we further investigated the temporal dynamics of the signal of S1 (and M1), in relation to movement onset. For this purpose, we analyzed the temporal signatures of the signals in the following three steps and show the results for a representative subject (subject 3).

Firstly, the two representative channels shown in Figure 7 with clear response over both S1 and M1 were re-aligned with respect to movement onset markers. Indeed, in these two channels all gamma-band power traces (Figure 10B) showed an increase in activity before movement onset. Secondly, to investigate whether the same trend was common to all S1 channels, time-frequency plots (Figure 10C) of the mean over S1 channels with significant response during the task (p < 0.05, Figure 10A) were computed per gesture. This analysis revealed a clear broadband (~50-130 Hz) increase in S1 channels prior to movement onset combined with a decrease in the beta frequency band starting between one to half a second before movement onset (t0 = 0 s). Thirdly, we investigated whether the broadband increase in activity is significantly different from baseline prior to movement. For this purpose, normalized z-score traces in the gamma-band (Figure 10D) of each gesture were calculated by subtracting and dividing the real amplitude trace by the mean and standard deviation, respectively, of a surrogate ensemble of mean amplitude values, where the stimuli onsets are shifted randomly in time 10000 times (Canolty et al., 2007). These traces were used to determine the uncorrected two-tailed probability that the deviation seen in the real amplitude trace at a given time is due to chance (p < 0.05). Results (Figure 10D) confirmed that a significant power increase occurs before movement onset for each gesture individually, when using the mean trace over S1 channels with significant response (Figure 10A).

Similar results were found across subjects, where the mean time-point corresponding to a significant power increase (-99.75±36.96 ms, mean ± standard error) was significantly lower than zero (one-sample t-test, p < 0.05, N=4). Altogether, these results indicate that there is information over S1 hand area that is decoupled from sensory feedback. Notably, an alternative strategy to investigate the nature of S1 responses could be to decode the gestures prior to movement onset. Following this analysis, however, decoding accuracies for both M1 and S1 coverages were on average not significantly above chance level (p < 0.05), indicating that this method would be inconclusive. Failure to decode prior to movement onset may be due to the limited time window with significant power increase before movement onset.

[Figure 26]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 27]

## 4 Discussion

In this study we have shown that the primary somatosensory cortex (S1) offers characteristic spatiotemporal discriminative patterns during executed hand gestures, providing classification rates similar to that obtained for primary motor cortex (M1) only and the sensorimotor cortex as a whole (M1 and S1 together). All five subjects achieved classification scores significantly (p < 0.05) above chance level, ranging from 59 to 100%. This indicates that S1 can be used as a source of signals for implantable BCI systems with multiple degrees-of-freedom. Further, regardless of the grid position, a mean (over subjects) classification accuracy of 80% was achieved when using a patch of cortex as small as 2 cm2, suggesting that decoding sign language using high-density ECoG grids is a potential strategy to increase the degrees-of-freedom of implantable BCI systems.

Previous articles from our group showed that decoding four hand gestures can be successfully achieved in a subset of patients by only considering spatial features (Bleichner et al., 2014). Notably, the execution of sign language gestures is not instantaneous, in that fingers are flexed/extended in sequence (albeit quite rapid) to obtain the gesture. Accordingly, one may expect to observe differences in the onset of a gamma-band response across electrodes, assuming that different electrodes record from somatotopically different cortical patches. Therefore, in the current study, we performed a reanalysis of the data of Bleichner and colleagues (Bleichner and Ramsey, 2014; Bleichner et al., 2014) and classified the four gestures using spatial and temporal features combined. Results showed that, even though the grid location for some subjects might not be optimal, high classification scores are achieved, not only in sensorimotor cortex as a whole (40-97% in the previous analysis compared to 59-100% in the current study), but also separately for M1 and S1. In order to understand the spatial-temporal pattern, which characterizes each single gesture, the trials had to be temporally aligned. Standard methods of alignment (such as relative to the cue or movement onset) may result in temporal jitter and/or bias, which may artificially alter the classification results (either positively or negatively). We introduced a new method of aligning trials, using the gamma-slope marker (GSM), which is based on the robust rise in gamma-band power following each cue. The use of the GSM method was introduced for the single purpose of classification by allowing a correct assessment of the temporal signature of each gesture. Indeed, with this approach, the (spatio)temporal differences between the gamma-band power traces of the four gestures can be safely interpreted to be from neuronal origin, and not due to different movement speed responses or the order in which the fingers are moved. Therefore, it allowed for minimization of both classification inflation due to systematic temporal differences in onset between gestures, and classification deflation caused by temporal jitter between trials.

4.1 Subjects’ performance Overall, the subjects’ performance, as recorded with the data glove, was robust across trials. Notably, hand movement onset occurred consistently half a second after the cortical activity onset, approximately one second after the cue and shortly after the gamma-band peak in activity. The delay between the cue and hand movement onset was larger than the typical reaction time (around 400 ms) between visual cues and muscle response in humans (Thorpe

[Figure 28]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 29]

et al., 1996). This can be attributed to the fact that, despite a brief practice period before the experiments, the sign language gestures were not trained enough to be automatic, thereby requiring some cognitive processing (notably to process the visual cue) before they were executed. In addition, reaction times may have been slowed due to the medical procedure and medication. The delay between gamma-band activity onset and hand movement onset was also larger than we would expect for automated responses, which agrees with the notion of a deliberate preparation and execution of gestures involving cognitive processes.

##### 4.2 Source of classification scores variance

Due to the limited number of subjects in this study, the source of variance in classification scores between subjects is difficult to account for. Two issues are worth mentioning, however. A first source of variance is the coverage of the hand knob. From the classification results of the three subjects with coverage over sensorimotor cortex (both M1 and S1), and the location of the most informative electrodes, we conclude that M1 and S1 are both good options for BCI control. On average, the classification scores for the combination of the two were slightly higher than for S1 or M1 separately, but this difference did not reach statistical significance. It has to be noted that statistics over the relatively small number of patients in our study is of limited value and a larger sample size will be needed to compare S1, M1 and the combination of the two in more detail. Two subjects had only one type of coverage (either S1 or M1) and both showed high classification scores for the four hand gestures. Although the subject with M1 coverage appeared to have a better classification score, the subject with only S1 coverage had the least hand knob coverage. Not surprisingly, the subject with best grid position over sensorimotor cortex (subject 3) was also the one reporting the highest scores. Indeed, Bleichner and colleagues (Bleichner et al., 2014) already suggested that the optimal location of the high-density grid over the hand knob might be essential for good classification results.

Second, the quality of the gesture performance likely affects classification, as suggested in an fMRI study in decoding gestures (Bleichner et al., 2013). Indeed, the subject with the 100% classification accuracy presented, besides the best grid position, the least excluded trials and the best gestures performance, as recorded with the data glove, with equal training time as the other subjects. This subject not only performed the gestures very consistently, but also displayed a consistent reaction time (Figure 7), indicating that accurate and consistent performance of the gestures may lead to better classification. In future applications, this level of performance may often require somewhat more intensive practice and training than our current subjects received.

##### 4.3 Role of S1 in motor execution and attempt

The results of the current study agree to some extent with those of Chestek and colleagues (Chestek et al., 2013), who showed above-chance level classification of nine different isometric hand motions using electrodes over M1, S1, mesial and parietal areas in three epileptic patients with low resolution sensorimotor coverage. In their study, M1 classification outperforms S1 classification most of the times, although there was substantial variation in the results. Here, we show that when using optimal spatial resolution and

[Figure 30]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 31]

employing the temporal information of the recorded signals, S1 decoding can be as accurate as M1 decoding.

Although ECoG-based BCIs aim to replace motor output for completely paralyzed patients, who can only attempt movement, the current study used able-bodied epilepsy patients who performed the actual movements. Chestek and colleagues (Chestek et al., 2013) argued that actual movement may inflate S1 decoding accuracy due to sensory feedback from the movements. However, even though S1 is correctly identified to integrate sensory feedback information, spinal cord injury fMRI studies have indicated activation of both M1 and S1 during attempted movements (Cramer et al., 2005; Hotz-Boendermaker et al., 2011, 2008), suggesting that S1 activation also occurs without direct sensory feedback. Furthermore, a recent 7T fMRI study shows that S1 topography remains intact after amputation, and presents a detailed representation of individual fingers upon attempted digit movement (Kikkert et al., 2016). Similarly interesting ECoG results have been obtained by Wang et al. (Wang et al., 2013) and Gharabaghi et al. (Gharabaghi et al., 2014) in individuals with tetraplegia and amputees, respectively. The former showed that attempted movement could be used to control 3D cursor movement with a success rate of 87% with a grid that was positioned entirely over S1, while the latter indicated high R2 values (in gamma-band) during phantom hand movement mostly over the post-central gyrus. Also the significant rise of S1 activity before movement onset in the present study supports the notion that sensory feedback is not necessary for S1 to be activated and that the area plays a role beyond only sensory feedback. However, a more convincing approach would be to record electromyographic signals (starting before movement onset) to exclude sensory feedback before movement. Yet, a role beyond only sensory feedback has been similarly supported in the last decades by data derived from anatomy, cortical stimulation and neurophysiological recordings (Cramer et al., 2005). Particularly interesting are cortical stimulation studies with subchronically implanted epilepsy patients showing that electrocortical stimulation in M1, but also in S1, results in isolated and complex hand motor responses (Haseeb et al., 2007; Nii et al., 1996).

Even though S1 seems to clearly play an important role during motor output (Cramer et al., 2005; Kikkert et al., 2016), the role of S1 during movement execution and its interaction with M1 are far from being understood. Besides a reflection of the proprioceptive feedback from muscle and joint receptors (Ashe, 2005; Miller and Hatsopoulos, 2012) the movementrelated activation over the somatosensory cortex may relate, for example, to a predictive driving connection from S1 to M1 (Adams et al., 2012; Scott, 2012), or modulation by a topdown mechanism involved in motor preparation (Christensen et al., 2007) or even execution. Interestingly, predictive theories of motor control have recently hypothesized that S1 may play a role in generating an efference copy, which is an internal prediction of sensory consequence of a volitional movement (Adams et al., 2012). In fact, Sun and colleagues (Sun et al., 2015) presented the first evidence of an efference copy in humans using standard ECoG grids during cued finger movements. A logical step would be to further investigate the information delay between M1 and S1 using high-density ECoG grids. Another possible theory for the role of S1 is one in top-down attentional control (Hopfinger et al., 2001), which is a higher-order mechanism that regulates sensory areas. This phenomenon has been described in detail for visual (Brefczynski and DeYoe, 1999) and auditory cortex (Fritz et

[Figure 32]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 33]

al., 2007), where presentation of a cue predicting an ensuing stimulus leads to an increase in neural activity before arrival of the stimulus, and even when the stimulus is withheld. Similar phenomena are described for the somatosensory system with magnetoencephalography (e.g., Haegens et al., 2011). In addition, covert attention to the thumb proved to increase functional MRI activity in the somatosensory contralateral cortex (Bauer et al., 2014). Given that the somatosensory cortex, like the visual and auditory cortex is topographically organized, it is to be expected that attempting to execute specific gestures may give rise to decodable patterns of elevations in neural activity in S1. Clearly, further research is necessary in order to assess in detail what role is played by S1 in movement preparation, execution and, especially during attempted movement.

## 5 Conclusion

In conclusion, this study shows that S1 may be as good of a target as M1 (or the two combined) for motor-based ECoG-BCIs, and contains sufficient somatotopic information to distinguish between four hand gestures. Although promising, the exact mechanisms leading to S1 activation and its exact role in executed (and attempted) hand movements are yet to be determined. The current study also indicates that optimal hand knob coverage and consistent gesture execution are essential for accurate decoding. Moreover, it encourages the use of both spatiotemporal information and high-density subcortical grids as a robust and reliable BCI platform for fine movement decoding.

## Supplementary Material

Refer to Web version on PubMed Central for supplementary material.

## Acknowledgements

This research was funded by the ERC-Advanced ‘iConnect’ project (grant ADV 320708), the BrainGain Smart Mix Programme (grant SSM06011) and the Dutch Technology Foundation STW (grant UGT7685). We thank Frans Leijten, Cyrille Ferrier, Geertjan Huiskamp, and Tineke Gebbink for their help in collecting data, Peter Gosselaar and Peter van Rijen for implanting the electrodes, as well as the technicians, the staff of the clinical neurophysiology department and the subjects for their time and effort.

## References

Adams R, Shipp S, Friston K. Predictions not commands: active inference in the motor system. Brain

Struct Funct. 2012; 218:611–643. [PubMed: 23129312] Ashe, J. What is coded in the primary motor cortex?. CRC Press LLC; 2005. Bauer C, Díaz J-L, Concha L, Barrios F. Sustained attention to spontaneous thumb sensations activates

brain somatosensory and other proprioceptive areas. Brain and Cognition. 2014; 87:8696.

Bleichner, MG., Ramsey, NF. Give Me a Sign: Studies on the Decodability of Hand Gestures Using Activity of the Sensorimotor Cortex as a Potential Control Signal for Implanted Brain Computer Interfaces. Springer International Publishing; 2014. p. 7-17.

Bleichner M, Freudenburg Z, Jansma J, Aarnoutse E, Vansteensel M, Ramsey N. Give me a sign: decoding four complex hand gestures based on high-density ECoG. Brain Structure and Function. 2014:1–14.

Bleichner MG, Jansma JM, Sellmeijer J, Raemaekers M, Ramsey NF. Give Me a Sign: Decoding Complex Coordinated Hand Movements Using High-Field fMRI. Brain Topography. 2013; 27:248– 257.

[Figure 34]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 35]

Brefczynski J, DeYoe E. A physiological correlate of the “spotlight” of visual attention. Nat Neurosci. 1999; 2:370–374. [PubMed: 10204545] Buzsáki G, Wang X-J. Mechanisms of Gamma Oscillations. Annu Rev Neurosci. 2012; 35:203–225. [PubMed: 22443509]

Canolty RT, Soltani M, Dalal SS, Edwards E, Dronkers NF, Nagarajan SS, Kirsch HE, Barbaro NM, Knight RT. Spatiotemporal dynamics of word processing in the human brain. Frontiers in neuroscience. 2007; 1:185. [PubMed: 18982128]

Chestek C, Gilja V, Blabe C, Foster B, Shenoy K, Parvizi J, Henderson J. Hand posture classification using electrocorticography signals in the gamma band over human sensorimotor brain areas. J Neural Eng. 2013; 10:026002. [PubMed: 23369953]

Christensen M, Lundbye-Jensen J, Geertsen S, Petersen T, Paulson O, Nielsen J. Premotor cortex modulates somatosensory cortex during voluntary movements without proprioceptive feedback. Nat Neurosci. 2007; 10:417–419. [PubMed: 17369825]

Combrisson E, Jerbi K. Exceeding chance level by chance: The caveat of theoretical chance levels in brain signal classification and statistical assessment of decoding accuracy. Journal of Neuroscience Methods. 2015; 250:126136.

Cramer S, Lastra L, Lacourse M, Cohen M. Brain motor system function after chronic, complete spinal cord injury. Brain. 2005; 128:2941–2950. [PubMed: 16246866]

Crone NE, Miglioretti DL, Gordon B, Lesser RP. Functional mapping of human sensorimotor cortex with electrocorticographic spectral analysis. II. Event-related synchronization in the gamma band. Brain. 1998; 121(Pt 12):2301–15. [PubMed: 9874481]

Daly J, Wolpaw J. Brain–computer interfaces in neurological rehabilitation. The Lancet Neurology. 2008; 7 Fritz JB, Elhilali M, David SV, Shamma SA. Auditory attention—focusing the searchlight on sound. Current opinion in neurobiology. 2007; 17:437–455. [PubMed: 17714933] Georgopoulos AP, Schwartz AB, Kettner RE. Neuronal population coding of movement direction. Science. 1986; 233:1416–9. [PubMed: 3749885]

Gharabaghi A, Naros G, Walter A, Roth A, Bogdan M, Rosenstiel W, Mehring C, Birbaumer N. Epidural electrocorticography of phantom hand movement following long-term upper-limb amputation. Front Hum Neurosci. 2014; 8:285. [PubMed: 24834047]

Haegens S, Händel BF, Jensen O. Top-down controlled alpha band activity in somatosensory areas determines behavioral performance in a discrimination task. The Journal of Neuroscience. 2011; 31:5197–5204. [PubMed: 21471354]

Haseeb A, Asano E, Juhász C, Shah A, Sood S, Chugani HT. Young patients with focal seizures may have the primary motor area for the hand in the postcentral gyrus. Epilepsy Res. 2007; 76:131–9. [PubMed: 17723289]

Hermes D, Miller KJ, Noordmans HJ. Automated electrocorticographic electrode localization on individually rendered brain surfaces. Journal of neuroscience methods. 2010; 185:293–298. [PubMed: 19836416]

Hermes D, Miller K, Vansteensel M, Aarnoutse E, Leijten F, Ramsey N. Neurophysiologic correlates of fMRI in human motor cortex. Hum Brain Mapp. 2012; 33:1689–1699. [PubMed: 21692146]

Hochberg L, Serruya M, Friehs G, Mukand J, Saleh M, Caplan A, Branner A, Chen D, Penn R, Donoghue J. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature. 2006; 442:164–171. [PubMed: 16838014]

Hopfinger JB, Woldorff MG, Fletcher EM, Mangun GR. Dissociating top-down attentional control from selective perception and action. Neuropsychologia. 2001; 39:1277–91. [PubMed: 11566311]

Hotz-Boendermaker S, Funk M, Summers P, Brugger P, Hepp-Reymond M-C, Curt A, Kollias S. Preservation of motor programs in paraplegics as demonstrated by attempted and imagined foot movements. NeuroImage. 2008; 39:383394.

Hotz-Boendermaker S, Hepp-Reymond M-C, Curt A, Kollias S. Movement observation activates lower limb motor networks in chronic complete paraplegia. Neurorehabil Neural Repair. 2011; 25:469–

76. [PubMed: 21343526] Kikkert S, Kolasinski J, Jbabdi S, Tracey I, Beckmann CF, Johansen-Berg H, Makin TR. Revealing the neural fingerprints of a missing hand. Elife. 2016; 5

[Figure 36]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 37]

Kubánek J, Miller K, Ojemann J, Wolpaw J, Schalk G. Decoding flexion of individual fingers using electrocorticographic signals in humans. J Neural Eng. 2009; 6:066001. [PubMed: 19794237]

Leuthardt E, Schalk G, Wolpaw J, Ojemann J, Moran D. A brain-computer interface using electrocorticographic signals in humans. Journal of Neural Engineering. 2004; 1:63. [PubMed: 15876624]

Martuzzi R, Zwaag W, Farthouat J, Gruetter R, Blanke O. Human finger somatotopy in areas 3b, 1, and 2: A 7T fMRI study using a natural stimulus. Hum Brain Mapp. 2014; 35:213–226. [PubMed: 22965769]

Miller K, Schalk G, Fetz E, Nijs M, Ojemann J, Rao R. Cortical activity during motor execution, motor imagery, and imagery-based online feedback. Proceedings of the National Academy of Sciences. 2010; 107:4430–4435.

Miller K, Sorensen L, Ojemann J, Nijs M. Power-Law Scaling in the Brain Surface Electric Potential. PLoS Computational Biology. 2009a; 5 Miller, L., Hatsopoulos, N. Neuronal Activity in Motor Cortex and Related Areas. Oxford Univeristy Press; 2012. p. 15-33.

Miller, Zanos, Fetz, den Nijs, Ojemann. Decoupling the Cortical Power Spectrum Reveals Real-Time Representation of Individual Finger Movements in Humans. J Neurosci. 2009b; 29:3132–3137. [PubMed: 19279250]

Nii Y, Uematsu S, Lesser RP, Gordon B. Does the central sulcus divide motor and sensory functions? Cortical mapping of human hand areas as revealed by electrical stimulation through subdural grid electrodes. Neurology. 1996; 46:360–7. [PubMed: 8614495]

Oostenveld R, Fries P, Maris E. FieldTrip: open source software for advanced analysis of MEG, EEG,

and invasive electrophysiological data. Computational intelligence and neuroscience. 2010; 2011 Penfield W, Boldrey E. Somatic motor and sensory representation in the cerebral cortex of man as

studied by electrical stimulation. Brain. 1937; 60:389–443. Pistohl T, Ball T, Schulze-Bonhage A, Aertsen A, Mehring C. Prediction of arm movement trajectories

from ECoG-recordings in humans. Journal of Neuroscience Methods. 2008; 167:105114. Pistohl T, Schulze-Bonhage A, Aertsen A, Mehring C, Ball T. Decoding natural grasp types from

human ECoG. Neuroimage. 2011; 59:248–60. [PubMed: 21763434]

Schalk G, Kubánek J, Miller K, Anderson N, Leuthardt E, Ojemann J, Limbrick D, Moran D, Gerhardt L, Wolpaw J. Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. J Neural Eng. 2007; 4:264. [PubMed: 17873429]

Scott S. The computational and neural basis of voluntary motor control and planning. Trends in Cognitive Sciences. 2012; 16:541549.

Siero JC, Hermes D, Hoogduin H, Luijten PR, Ramsey NF, Petridou N. BOLD matches neuronal activity at the mm scale: a combined 7T fMRI and ECoG study in human sensorimotor cortex. Neuroimage. 2014; 101:177–84. [PubMed: 25026157]

Stringer E, Qiao P, Friedman R, Holroyd L, Newton A, Gore J, Chen L. Distinct fine-scale fMRI activation patterns of contra- and ipsilateral somatosensory areas 3b and 1 in humans. Human Brain Mapping. 2014; 35:4841–4857. [PubMed: 24692215]

Sun H, Blakely TM, Darvas F, Wander JD, Johnson LA, Su DK, Miller KJ, Fetz EE, Ojemann JG. Sequential activation of premotor, primary somatosensory and primary motor areas in humans during cued finger movements. Clin Neurophysiol. 2015; 126:2150–61. [PubMed: 25680948] Thorpe S, Fize D, Marlot C. Speed of processing in the human visual system. Nature. 1996; 381:520–

522. [PubMed: 8632824]

Wang W, Collinger J, Degenhart A, Tyler-Kabara E, Schwartz A, Moran D, Weber D, Wodlinger B, Vinjamuri R, Ashmore R, Kelly J, et al. An Electrocorticographic Brain Interface in an Individual with Tetraplegia. PLoS ONE. 2013; 8

Yousry T, Schmid U, Alkadhi H, Schmidt D, Peraud A, Buettner A, Winkler P. Localization of the motor hand area to a knob on the precentral gyrus. A new landmark. Brain. 1997; 120:141–157. [PubMed: 9055804]

Yuan H, He B. Brain-Computer Interfaces Using Sensorimotor Rhythms: Current State and Future Perspectives. Biomedical Engineering, IEEE Transactions on. 2014; 61:1425–1435.

[Figure 38]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 39]

[Figure 40]

Figure 1. Position of the electrode grids of all individual subjects.

The central sulcus (CS, black line) separates the primary motor cortex (M1, in blue) from the primary somatosensory cortex (S1, in orange). Dashed yellow lines indicate the hand knob region as determined with pre-surgical functional MRI. Electrodes over the blue areas were labeled as M1 electrodes, electrodes over orange areas were labeled as S1 electrodes and electrodes in black were excluded from the analysis.

[Figure 41]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 42]

[Figure 43]

Figure 2. Task paradigm.

A) Four hand gestures (G1, G2, G3 and G4), taken from the American Sign Language finger spelling alphabet (‘D’, ‘F’, ‘V’ and ‘Y’, respectively), were executed during the task. B) The task paradigm comprised 10 trials per gesture, presented in the screen for 6 seconds, interleaved with 6 seconds of rest trials (open relaxed hand). The gestures were recorded using a data glove device, which measured the flexion of each finger. The figure shows the a representative data glove trace for gesture D, where the light blue line is the thumb, the orange line is the index finger, the yellow line is the middle finger, the purple line is the ring finger and the green line the little finger.

[Figure 44]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 45]

[Figure 46]

Figure 3. Gamma-slope method for alignment of the trials.

A) Representative example of an epoched gamma-band trace F(n) for one trial (e.g., subject 3 G1, trial 1), for n discrete time points. B) The horizontal distance dni(k) between all points k in the line segment, S(k), and F(n), was calculated for every ni in the domain of F(n). As an example, the figure shows the line segment in three representative time ni points (ni = 2286, 3499 and 5208). The line segment’s slope is subject-specific and constant. C) The overall distance, D(ni), between S(k) and F(n) was calculated by summing the distances, between all points in S(k) and the points in F(n) with the same amplitude, which were

inferior toεni. The argument which minimized the D(ni) curve, b, identified the line segment which best fitted the trace. In this example, b was 3499. D) The gamma-slope marker (GSM)

t0 was calculated as the midpoint of the line segment Sb(k) which best fitted the trace.

[Figure 47]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 48]

[Figure 49]

Figure 4. Trial alignment for a representative dataset of subject 4 (G2).

After having identified the gamma-slope-markers over smoothed traces all unsmoothed trials were aligned to each other, such that all markers were coincident. For that, the first trial (blue trace) was kept unchanged, while the remaining trials (orange traces) were aligned to it. In this figure power amplitude is given in μV2 and t0 = 0 s corresponds to the movement onset.

[Figure 50]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 51]

[Figure 52]

Figure 5. Representative feature space and spatiotemporal template for classification of the four gestures for subject 3.

A) The three-dimensional feature space used for classification consisted, per gesture, of a 3D matrix of included channels (32) by included trials (9, 8, 9, 10 for G1-4, respectively) and by time points (-1 to 2.6 s around gamma-band activity onset). B) Spatiotemporal template derived from the mean gamma-band power over trials per gesture. The color code displayed on the left of each template graph indicates the location of the electrode: the M1 electrodes in blue and the S1 electrodes in orange. The time reference (t0 = 0 s) is the gamma-slope marker (GSM). The color bar on the right of the figure indicates the power over the gamma-band in μV2.

[Figure 53]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 54]

[Figure 55]

Figure 6. Representative examples of data glove traces for each gesture (G1-G4) of subject 3.

The average finger position over trials is represented in an interval -2 to 2 s around the gamma-slope marker (t0 = 0 s, dashed gray line). The mean cue time and corresponding standard deviation (relative to the gamma-slope marker) is indicated by the solid gray line and gray shaded area. For each trace, a dashed line with the same color of the respective finger trace indicates the error. The movement response is seen to consistently occur half a second after the gamma-band activity onset and approximately 1 second after the cue. This pattern in response timing is representative for the remaining subjects (see Supplementary Figure 3). Note that, due to the device calibration, the thumb movement is inverted when compared to the remaining fingers.

[Figure 56]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 57]

[Figure 58]

Figure 7. Representative gamma-band traces per channel of subject 3.

A) Gamma-band power (average over trials) in the time window -1 to 5 s around the gamma-slope marker (t0 = 0 s). Each gesture is represented with a different line color. The standard deviation across trials is represented by the shaded region with the color corresponding to the respective gesture. Power amplitudes were normalized (arbitrary units, a.u.) to all channels, in order to visualize differences between them. B) Two representative channels from M1 (solid black square) and S1 (dashed black square) areas, respectively. The mean power amplitude (arbitrary units, a.u.) over trials per gesture is plotted over a time

[Figure 59]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 60]

window -1 to 5 s around movement onset. As in A) standard deviations are shown using the shaded regions with respective gesture color. CS – Central Sulcus; A – Anterior; P – Posterior.

[Figure 61]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 62]

[Figure 63]

Figure 8. Classification scores for the five subjects (subject 1-5).

A) For each subject one to three bars show the classification scores, by means of leave-oneout cross-validation, for the different electrode coverages: sensorimotor cortex in gray, M1 in blue and S1 in orange. Subject 1 and subject 4 had partial sensorimotor coverage (i.e., only S1 or M1, respectively), while the remaining subjects had electrodes over both the precentral and postcentral parts of the sensorimotor cortex. B) Mean classification scores across subjects for sensorimotor (N=3), M1 (N=4) and S1 (N=4) coverage. For both panels,

[Figure 64]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 65]

the theoretical chance level is 25% (dashed gray line) for classification of four classes and the significance level is 40% (solid gray line).

[Figure 66]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 67]

[Figure 68]

Figure 9. Most informative electrodes.

The most informative electrodes for each subject were determined by calculating the contribution of each individual electrode for classification. The classification accuracy was re-computed using combinations of increasing number of electrodes. The set sizes varied from an individual electrode to all electrodes. The contribution of each individual electrode was then computed based on the average classification achieved when that electrode was part of the combination (c.f. the color bar on the right, in which yellow (smallest radius) corresponds to the least informative electrode and blue (biggest radius) to the most informative electrode). CS – Central Sulcus; A – Anterior; P – Posterior.

[Figure 69]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 70]

[Figure 71]

Figure 10. Representative gamma-band traces of subject 3 aligned to movement onset.

A) Schematic of the ECoG grid for subject 3, with two channels highlighted with squared boxes and S1 channels with significant response during the task highlighted in orange. CS Central sulcus; A - Anterior; P - Posterior. B) Two representative channels are selected from M1 and S1 areas. The gamma-band traces of each channel were aligned with respect to movement onset (t0 = 0 s) and the mean power amplitude (arbitrary units, a.u.) over trials per gesture is plotted here over a time window -1 to 5 s around movement onset. The standard deviation across trials is represented by the shaded region with the color corresponding to

[Figure 72]

### EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 73]

the respective gesture. C) Average time-frequency power plots (baseline correction in dB using -2 to -1 time window) across S1 channels (highlighted in orange) for each gesture

(G1-G4). Movement onset (t0 = 0 s) is indicated with a vertical black line, while broadband (~50-130 Hz) activity is indicated with a dashed line. For all gestures there is an increase in broadband power, which starts before movement onset, coupled with a decrease in the beta band (~10-30 Hz). D) Normalized z-score (a.u.) traces used to determine the uncorrected two-tailed probability that the deviation seen in the real amplitude trace at a given time is due to chance. For each gesture, the dashed gray line indicates the first time point correspondent to a significant power increase (p < 0.05), while the solid gray line indicates the movement onset (t0 = 0 s).

[Figure 74]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 75]

Table 1

Patient characteristics and high-density grid information.

|Patient No.|Subject 1|Subject 2|Subject 3|Subject 4|Subject 5|
|---|---|---|---|---|---|
|Age|29|42|19|19|45|
|Gender|Male|Male|Female|Male|Female|
|Handedness|Right|Right|Right|Right|Left|
|Implanted hemisphere|Left|Left|Left|Left|Right|
|Epileptic resected area|Posterior high parietal|Temporal lobe (including amygdala and hippocampus)|Posterior medial frontal gyrus until precentral gyrus|Anterior temporal lobe (including amygdala and hippocampus)|Frontal-para-sagittal|
|High-density grid location|Hand knob (post-central)|Hand knob (precentral and superior postcentral|Hand knob (pre- and post-central)|Hand knob (superior precentral)|Hand knob (primarily post-central)|
|Total number of included electrodes|29/32|24/32|32/32|31/32|59/64|
|Number of electrodes over M1|-|15|16|31|11|
|Number of electrodes over S1|29|9|16|-|48|

[Figure 76]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 77]

Included trials per subject.

| |Number of included trials| | | |
|---|---|---|---|---|
|Patient No.|G1|G2|G3|G4|
|Subject 1|8|10|10|6|
|Subject 2|5|10|10|9|
|Subject 3|9|8|9|10|
|Subject 4|9|7|8|10|
|Subject 5 – run 1|5|10|8|10|
|Subject 5 – run2|5|10|10|10|

Table 2

[Figure 78]

EuropePMCFundersAuthorManuscriptsEuropePMCFundersAuthorManuscripts

[Figure 79]

Table 3

Reproducibility of classification results for subject 5 using two independent runs.

| |Decoding Accuracy| | |
|---|---|---|---|
| |Sensorimotor cortex|M1|S1|
|Template run1 - classify run 2|80%|51%|80%|
|Template run2 - classify run 1|85%|53%|82%|

