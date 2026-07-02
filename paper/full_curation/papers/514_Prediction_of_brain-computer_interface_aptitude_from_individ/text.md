###### ORIGINAL RESEARCH ARTICLE

published: 02 April 2013 doi: 10.3389/fnhum.2013.00105

## HUMAN NEUROSCIENCE

# Prediction of brain-computer interface aptitude from individual brain structure

### S. Halder1,2,3*†, B. Varkuti1†, M. Bogdan3,4, A. Kübler1, W. Rosenstiel3, R. Sitaram5 and N. Birbaumer2,6

- 1 Department of Psychology I, University of Würzburg, Würzburg, Germany
- 2 Institute of Medical Psychology and Behavioral Neurobiology, University of Tübingen, Tübingen, Germany
- 3 Wilhelm-Schickard Institute for Computer Science, University of Tübingen, Tübingen, Germany
- 4 Department of Computer Engineering, University of Leipzig, Leipzig, Germany
- 5 Department of Biomedical Engineering, University of Florida, Gainesville, FL, USA
- 6 Ospedale San Camillo, Laboratorio di Neuroscience Comportamentale, Istituto di Ricovero e Cura a Carattere Scientiﬁco, Venezia, Italy

Edited by: Cuntai Guan, Institute for Infocomm Research, Singapore

Reviewed by: Clemens Brunner, Graz University of Technology, Austria Michal Lavidor, Bar Ilan University, Israel

*Correspondence: S. Halder, Department of Psychology I, University of Würzburg, Marcusstr. 9-11, 97070 Würzburg, Germany. e-mail: sebastian.halder@ uni-wuerzburg.de †These authors have contributed equally to this work.

Objective: Brain-computer interface (BCI) provide a non-muscular communication channel for patients with impairments of the motor system. A signiﬁcant number of BCI users is unable to obtain voluntary control of a BCI-system in proper time. This makes methods that can be used to determine the aptitude of a user necessary.

Methods: We hypothesized that integrity and connectivity of involved white matter connections may serve as a predictor of individual BCI-performance. Therefore, we analyzed structural data from anatomical scans and DTI of motor imagery BCI-users differentiated into high and low BCI-aptitude groups based on their overall performance.

Results: Using a machine learning classiﬁcation method we identiﬁed discriminating structural brain trait features and correlated the best features with a continuous measure of individual BCI-performance. Prediction of the aptitude group of each participant was possible with near perfect accuracy (one error).

Conclusions: Tissue volumetric analysis yielded only poor classiﬁcation results. In contrast, the structural integrity and myelination quality of deep white matter structures such as the Corpus Callosum, Cingulum, and Superior Fronto-Occipital Fascicle were positively correlated with individual BCI-performance.

Signiﬁcance: This conﬁrms that structural brain traits contribute to individual performance in BCI use.

Keywords: BCI, motor imagery, aptitude, DTI, fractional anisotropy

- 1. INTRODUCTION Brain-computer interface (BCI) provide a non-muscular control channel that can be used for communication, device control, or rehabilitation. Most non-invasive BCI rely on control signals that are extracted from components of the electroencephalogram (EEG), ﬁrst described by Berger (1929), that can be voluntarily modulated. One of the earliest control signals used successfully for communication with severely paralyzed amyotrophic lateral sclerosis (ALS) patients were slow cortical potential (SCP) (Birbaumer et al., 1990, 1999). Later studies were often based on event-related potential (ERP), mainly the P300, [(Farwell and Donchin, 1988; Polich, 2007; Nijboer et al., 2008b; Silvoni et al., 2009; Lulé et al., 2013); see Kleih et al. (2011) for a review]. P300 BCI have the advantage of requiring almost no user training. Steady state-evoked potential (SSEP) share this advantage and have also been successfully used for BCI (Regan, 1977; Middendorf et al., 2000; Allison et al., 2008). It is also possible to control a BCI by performing motor imagery of different body parts such as hands or feet which causes event-related desynchronization (ERD) and event-related synchronization (ERS) of

the sensorimotor rhythm (SMR) (also referred to as µ-rhythm) (Pfurtscheller and da Silva, 1999; Neuper et al., 2003; Kübler et al., 2005). Novel approach utilize the principles of semantic classical conditioning to establish a communication channel (Furdea et al., 2012; De Massari et al., 2013; Ruf et al., 2013).

In the context of this study BCI paradigms that rely on user training are of particular interest. This includes BCI based on the modulation of SMR or SCP. Of these we will focus on BCI based on the modulation of the SMR using motor imagery. The SMR is a brain rhythm in the frequency range of 8–15Hz which is insensitive to visual input (Kuhlman, 1978). Distinct rhythms originating from the somatosensory cortex are modulated by executed movement or movement imagery depending on the body part involved in the task (Hari and Salmelin, 1997; Pfurtscheller et al., 1997). In addition to modulation in the alpha band, modulation can also occur in a second peak in the beta band (16–30Hz). This peak is located anteriorly to the sources of the alpha component of the SMR (Hari and Salmelin, 1997).

Two approaches to achieving high accuracies with SMR bases BCI have been established. Studies more focused on single sessions with high information transfer rate (ITR) with healthy participants use a large number of EEGsensors to which advanced spatial ﬁltering methods such as common spatial patterns (CSP) are applied (Ramoser et al., 2000; Blankertz et al., 2008). This requires fewer sessions of user training. In studies focused on BCI usage with patients multiple sessions should be possible with a minimum preparatory overhead (such as applying a large number of sensors) which is why user training enabling BCI usage with a low number of sensors is the preferred approach (Neuper et al., 2003, 2009; Kübler et al., 2005; Nijboer et al., 2008a). The time of training is one the reasons for the need of a reliable predictor that estimates the aptitude of a potential user to control such a BCI before training. Additionally, current research on the use of EEG-based BCI suggests that a certain percentage of users would not at all be able to gain sufﬁcient voluntary control of an EEG-BCI within an acceptable timeframe: a phenomenon recently referred to as BCI inefﬁciency (Kübler et al., 2011). The criterion level of free control is deﬁned to be at 70% selection accuracy Kübler et al. (2001, 2004). In Guger et al. (2009) 50% of participants (N = 99) did not achieve accuracies above 70% with an SMR based BCI, in Hammer et al. (2012) 37.5% of participants (N = 80) failed to achieve accuracies above 70%. The availability of reliable performance prediction methods would also considerably improve the process of selecting the most promising paradigm for a particular user. Additionally, training programs could be adapted to the aptitude of a particular user at a much earlier stage. Considering that BCI are primarily intended for patients who are diagnosed with severe diseases that not only lead to motor impairment but also to a reduced attention span it would be advantageous to be able to quickly choose a suitable BCI and training strategy that best ﬁts the patients needs (Birbaumer et al., 2008). It was shown that the amplitude of the SMR during rest strongly predicts the performance of a participant in a subsequent SMR-BCI session (Blankertz et al., 2010). A study using functional magnetic resonance imaging (fMRI) has shown that there is a strong difference in supplementary motor area (SMA) activation between high and low aptitude SMR-BCI users when performing motor imagery (Halder et al., 2011). This difference is enhanced when the participants observe motor tasks. For P300- based BCI it could be shown that prediction is possible using data collected from auditory oddball ERP recorded before the experiment but also using features extracted during stimulation (Mak et al., 2012; Halder et al., 2013).

In the light of recent studies on the association of bundle speciﬁc white matter integrity and EEG features in healthy subjects (Valdés-Hernández et al., 2010), the link of interhemispheric white matter connectivity with EEG frontal coherence (Teipel et al., 2009) and the relation of interhemispheric transfer time to DTI derived measures of white matter integrity, it is apparent that the conduction properties (e.g., conduction velocity, myelinization, and local ﬁber density) of the brain are determined by the underlying white matter network and that these properties might in turn signiﬁcantly inﬂuence EEG features on both the trait and state level. Speciﬁcally, the dynamics of the resting state

alpha rhythm appear to be connected to white matter architecture (Valdés-Hernández et al., 2010). Due to the dependence of the resting state SMR that was shown in Blankertz et al. (2010) and the reported link between EEG features in that frequency range and white matter architecture (Valdés-Hernández et al., 2010), we assumed that there may be a link between white matter architecture and SMR-BCI aptitude.

Based on these ﬁndings we hypothesized, that structural characteristics of the user such as head size, white matter integrity, or cortical surface area also inﬂuence BCI aptitude. We hypothesized that structural differences in the brains of high and low aptitude users can be identiﬁed and that these features not only differ between the groups of high and low aptitude users, but are strongly correlated with individual BCI aptitude. In order to investigate this relationship we conducted a single EEG-BCI session and a structural MRI measurement with 20 healthy participants. We refer to the potential skill of BCI usage of an individual as aptitude. The performance achieved by naive BCI users has been shown to be predictive of subsequent peformance in previous studies (Neumann and Birbaumer, 2003; Kübler et al., 2004). Thus, aptitude is used a synonym for the performance in the ﬁrst BCI session in the context of this paper.

### 2. METHODS

- 2.1. PARTICIPANTS Twenty healthy participants (7 female, mean age 24.5 years, SD ±
- 3.7, range 19–36) took part in the study which was approved by the Ethical Review Board of the Medical Faculty, University of Tübingen. Each participant was informed about the purpose of the study and signed informed consent prior to participation. Additionally, each participant signed a form informing him or her about potential risks and exclusion criteria of functional magnetic resonance imaging. Participants were payed 8e/h. All participants had no prior experience with SMR BCI, had no history of neurological diseases and were German native speakers. Psychological measurements before the experiment showed that both groups had equal levels of intelligence using Raven’s standard progressive matrices [mean 66.75, (SD ± 19.29), high aptitude users 71.9 (SD ± 8.31), low aptitude users 61.6 (SD ± 25.64), Wilcoxon rank test p = 0.4]. The datasets of four participants could not be used in the ofﬂine analysis. The dataset of VPTAB was not complete, the anatomical scan of VPTBJ revealed an incidental ﬁnding of a brain abnormality (a large portion of the right hemisphere was missing making normalization impossible), a scanner artifact rendered the data from VPTBS useless (frontal signal extinction possibly caused by radio frequency spike artifacts during acquisition due to a mechanical defect) and ﬁnally the data of participant VPTBT had missing slices in the structural scan. A detailed overview of EEG-BCI performance, imagery tasks, and demographic data of all participants can be found in Halder et al. (2011). Thus, N = 9 subjects were in the low and N = 7 subjects in the high aptitude group.

Participants took part in the MRI session depending on individual willingness and suitability. The MRI session was always conducted after the EEG experiement, on average 13.9 days later.

##### 2.2. PROCEDURE

- 2.2.1. EEG-BCI and neurofeedback Each of the 20 participants performed a single EEG-BCI session. This included measurements in which the participant had to perform motor execution, observation, and imagery. Three imagery measurements which totalled 75 trials of three classes (left hand, right hand, preferred foot) were used to calibrate the feedback parameters. The calibration trials lasted 8s, in 4 of which the participant performed the task. After calibration three feedback measurements were performed in which the participant had to use the two classes which showed the highest discriminability in the calibration data to control a cursor. Feedback trials had a length of 9s, 4 of which with feedback. The additional second was used to indicate which class had to be performed in the current trial. In total 300 feedback trials were performed (150 per class). For a summary of the number of trials per task see Table 1. The accuracy the participants achieved in these 300 trials was used to categorize them into high and low aptitude SMR-BCI users by a median split. About 2.5h were needed for preparation and collecting the calibration data of the system. In total, 5.5–6.5h were needed to complete the session. For further information and illustrations of the feedback method see Blankertz et al. (2010).
- 2.3. DATA ACQUISITION

#### 2.3.1. EEG recording Participants were seated in a chair approximately one meter away from a digital computer screen on which cues and feedback were displayed. The EEG recording was performed using four 32-channel BrainAmp direct current (DC) ampliﬁers manufactured by Brainproducts, Munich, Germany. A 128-channel cap manufactured by Easy Cap, Munich, Germany was used. Of these 119 were used for EEG recording and positioned according to the extended 10–20 system (Sharbrough et al., 1991), referenced to the nasion and grounded to an electrode between Fz and Fpz. The EEG was recorded at 1000Hz, band-pass ﬁltered between 0.05 and 200Hz and notch ﬁltered at 50Hz. Electromyogram (EEG) artifacts were monitored with bipolar electrodes on both forearms and the participants preferred leg. EOG artifacts were recorded with electrodes placed above and below the right eye for vertical EOG (superior and inferior orbital fossa), and for horizontal EOG with electrodes placed at the outer canthi of the eyes. This data was used to exclude artifact contaminated trials.

[Figure 1]

- Table 1 | Details of EEG experiments.

[Figure 2]

Motor task Trial duration Trials/class Number of classes

[Figure 3]

Execution 8s 25 3 Observation 10s 20 3 Imagery calibration 8s 75 3 Imagery feedback 9s 150 2

[Figure 4]

Each participant performed motor execution, observation, and imagery used for calibration of the classiﬁer of the BCI and ﬁnally motor imagery with SMRfeedback with the optimal combination of two of the three classes (right hand vs. left hand, right hand vs. foot, or left hand vs. foot).

- 2.3.2. MRI recording The MRI experiments were performed in a Siemens Magneton Trio Tim 3T whole body scanner using a standard 12-channel head coil. Each subject participated in one DTI measurement (1.8 × 1.8 × 6.5mm voxels, 5mm gap, TR = 3s, TE = 93ms, FoV = 1150 × 1150, Flip Angle = 90◦, 20 transversal slices, 128 × 128 voxels per slice, 20 diffusion directions, b-value = 1000s/mm2) with the FoV comprising the full cerebrum and parts of the rostral cerebellum (how much of the cerebellum was included was dependent on individual overall brain size). Anatomical images were acquired using a high resolution T1 sequence (0.5 × 0.5 × 1mm voxels, 0.5mm gap, TR = 1.9s, TE = 2.26ms, ﬂip angle = 9◦, 176 sagittal slices, 448 × 512 voxels per slice).
- 2.4. ANALYSIS OF DTI DATA First, the fractional anisotropy (FA) image from the DTI data was calculated for each individual. Subsequently the normalization parameters to Montreal Neurological Institute (MNI) standard space (using the SPM8 echo-planar imaging (EPI) template) were estimated for the FA-image aligned B0-image of the DTI sequence using SPM Version 8. The normalization parameters were then inverted to warp the standard label image of the ICBMDTI-81 Atlas into each participants original DTI space, avoiding any interpolation of the original FA values. For each of the 50 ICBM-DTI-81 Atlas regions the median of FA values for all voxels with an FA value above 0.25 was extracted and saved in the participant/regional FA value table.
- 2.5. ANALYSIS OF ANATOMICAL DATA We performed a voxel-based morphometry (VBM) Analysis of the T1 weighted anatomical scans to derive descriptors regarding the relative gray matter volume of each Automated Anatomical Labeling (AAL) region as well as the relative white matter volume of each ICBM-DTI-81 Atlas region. The Voxel-based Morphometry Toolbox (VBM5.1) was used for estimation of the individual modulated and unmodulated segmentation outputs. As the modulated outputs can be corrected for non-linear warping only and therefore make any further correction for different brain size redundant, these images can be used directly for volume estimations. For the uniﬁed segmentation approachrepeated segmentation, bias correction, and warping iterations as described in Ashburner and Friston (2005)—used in this study the tissue probability maps provided within the SPM5 template set were used because the subjects were drawn from the appropriate population. We applied the thorough clean-up option of the VBM toolbox and a medium Hidden Markov Random Field model for denoising of the T1 image. A check of sample homogeneity of the modulated images [using the standard deviation (SD) approach within VBM5.1] revealed that the VBM results of the images were all within a tolerable range (not considering the previously excluded participants). In order to smooth the resulting images we applied a three dimensional Gaussian smoothing kernel (FWHM = 3mm, signiﬁcantly below the rounded cubic root of the volume of the smallest AAL-region in equal voxel-space). Subsequently the images were re-sliced into the 1 × 1 × 1mm voxel space of the atlas images containing the

- respective region labels. For each AAL and ICBM-DTI-81 Atlas region the number of gray matter and white matter voxels within the atlas derived volumes of interest was counted—equalling the regional volume of the respective tissue relative to the entire individual brain. These volume values are strongly correlated across our healthy sample as they all measure brain volumes for identical regions. The total raw volume values [ml] for each participant were also extracted, resulting in absolute volume estimates of the individual amount of gray matter, white matter, and cerebro-spinal ﬂuid (CSF) and the respective gray/white matter ratio.
- 2.6. CATEGORIZATION INTO HIGH AND LOW APTITUDE USERS The anatomical data extracted with the methods described in the previous sections was used to predict the performance of the participants. Prediction was performed with four distinct feature sets calculated as described in the previous section: relative gray matter volume, relative white matter volume, FA values and total raw volumes of gray and white matter, CSF and gray/white matter ratio. Shrinkage linear discriminant analysis (LDA) was used to classify the participants into high and low aptitude users Blankertz et al. (2011). Participants were assigned to one of the two groups based on their performance in the EEG-BCI experiment. The classiﬁer performance was validated using a leaveone-participant-out cross validation scheme. At the beginning of each cross validation step features were selected from the current

training set based on the signiﬁcance of the correlation (Pearson’s r, p < 0.1) between feature and BCI performance (all excluding the test set). Then the classiﬁer was trained using these features and was applied to the test set (the participant that was not included in the current training). All features were scaled to [0, 1].

### 3. RESULTS

- 3.1. EEG-BCI ONLINE ACCURACY The median EEG-BCI performance of the 20 participants was at 82.1%. This value was used to split the participants into high and low aptitude BCI users. After the exclusion of the four participants mentioned in the Methods section this resulted in 7 high and 9 low aptitude users. Further details on the sample can be found in Blankertz et al. (2010); Halder et al. (2011), and Hammer et al. (2012).
- 3.2. PERFORMANCE PREDICTION RESULTS All reported results are based on the leave-one-participant-out cross validation scheme described in the Methods section. If none of the features fulﬁlled the inclusion criteria in the current step an accuracy of 0.5 (chancel level) is assumed. Using relative gray matter, relative white matter or absolute gray/white matter led only to chance level performance prediction. Using the FA features led to an error of 6.25% (binomial test to quantify signiﬁcance of prediction p < 0.0001). This means that only one

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

be a horizontal line (dashed green line). It is optimally placed anywhere between VPTBP and VPTAJ. This placement causes the single error in our classiﬁcation procedure (prediction of the group of VPTAQ, marked by a black “x”). The weights used to calculate the position of each participant are the ones obtained when this participant comprises the test dataset.

FIGURE 1 | The result of the multiplication of the weight and feature vector is shown on the x-axis. The high and low aptitude users are grouped on two separate horizontal lines on the y-axis (red circles high aptitude users, blue circles low aptitude users). This is only used to visually differentiate high from low aptitude users visually. The decision plane used by the classiﬁer therefore has to

[Figure 9]

- Table 2 | Correlations between FA value and BCI performance of the regions used most often for prediction of the aptitude group.

[Figure 10]

Correlation p-value Signiﬁcant ICBM-DTI Abbreviation Region Feature region code usage (%)

[Figure 11]

0.63 0.009 Yes 38 CGH-R Cingulum (Hippocampus) right 100 0.54 0.029 Yes 43 SFO-L Superior Fronto-Occipital 100

Fasciculus left

0.54 0.032 Yes 4 BCC Body of Corpus Callosum 100 0.52 0.040 Yes 15 CP-L Cerebral Peduncle left 100 0.51 0.043 Yes 28 PCR-R Posterior Corona 87.5

Radiata right

[Figure 12]

0.50 0.051 No 34 EC-R External Capsule right 100 0.48 0.060 No 1 MCP Middle Cerebellar peduncle 87.5 0.47 0.065 No 16 CP-R Cerebral Peduncle right 93.75 0.21 0.429 No 17 ALIC-L Anterior limb of 81.25

Internal Capsule left

−0.01 0.956 No 21 RLIC-L Retrolenticular part 68.75

of Internal Capsule left

[Figure 13]

Only correlations above the second to last horizontal black line are signiﬁcant (FDR corrected, p < 0.05).

participant (VPTAQ, see Figure 1 for a graphical representation of the classiﬁer output) was classiﬁed incorrectly. The number of times each feature was selected for classiﬁcation is given in Table 2.

- 3.3. SELECTED FEATURES The T1-based anatomical MRI information (rel. GM, rel. WM, and absolute GM/WM/CSF/TIV) could not be used to predict the performance category of the participants of this study. Therefore, all selected features originated from the regionwise extraction of average local FA values for the regions described in the ICBMDTI-81 Atlas. See Table 2 for the number of times each feature was selected. The areas with highest discrimination were the Body of Corpus Callosum (regioncode 4, selected in 16 CV-folds), the right Cerebral Peduncle (regioncode 15, selected in 16 CVfolds), the right External Capsule (regioncode 34, selected in 16 CV-folds), the right Cingulum at Hippocampus (regioncode 38, selected in 16 CV-folds), the left Superior Fronto-Occipital Fasciculus (regioncode 43, selected in 16 CV-folds), the left Posterior limb of the Internal Capsule (regioncode 16, selected in 15 CV-folds), the Middle Cerebellar Peduncle (regioncode 1, selected in 14 CV-folds), the right Posterior Corona Radiata (regioncode 28, selected in 14 CV-folds), the right Posterior limb of the Internal Capsule (regioncode 17, selected in 13 CVfolds) and the right rentrolenticular part of the Internal Capsule (regioncode 21, selected in 11 CV-folds). Seven further white matter regions (regioncodes 5, 10, 14, 26, 41, 46, and 49) were selected in only one CV-fold. White matter regions with high discriminatory value are illustrated in Figure 2.
- 3.4. CORRELATION OF LOCAL FRACTIONAL ANISOTROPY AND EEG-BCI PERFORMANCE

After identifying local FA as the most discriminating feature, the top-discriminating WM regions were selected (based on selection in CV-folds) and local FA values were correlated with individual accuracy (as described in section EEG-BCI and Neurofeedback),

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

FIGURE 2 | The top ﬁve white matter regions which were most discriminating in the low vs. high BCI-aptitude group comparison (based on feature use over CV-folds) and showed signiﬁcant correlations (FDR corrected, p < 0.05) with individual BCI-performance. Red, Body of Corpus Callosum; Green, left Cerebral

Peduncle; Blue, right Posterior Corona Radiata; Lilac, right Cingulum (Hippocampus area); Yellow, left Superior Fronto-Occipital Fasciculus.

[Figure 18]

as a measure of EEG-BCI performance. The correlations in the Cingulum at Hippocampus, left Superior Fronto-Occipital Fasciculus, Body of Corpus Callosum, left Cerebral Peduncle, and the right Posterior Corona Radiata showed positive correlations (0.51–0.63) with the individual accuracy (FDR corrected, p < 0.05). Note that these signiﬁcances are calculated over the whole dataset whereas the signiﬁcances used for feature selection were calculated over the subsets of the corresponding cross-validation fold. This can lead to discrepancies such as the FA value of the retrolenticular part of internal capsule left being includedin the majority of the folds but still having a large p-value

if correlated with individual accuracy over full data set. Higher FA in these regions of the brain is related to better individual EEG-BCI performance. This is shown in Figure 2 for the regions whose FA valuescorrelate the strongest with BCI performance. An overview of all regions used during the prediction of the aptitude groupis given in Table 2. Forcomparison purposes we appliedthe predictor presented in Blankertz et al. (2010) to the data of this study. The resting SMR-based predictor correlates with accuracy with r = 0.73 (p < 0.01) in this sample.

- 4. DISCUSSION Using only structural MRI data we were able to predict with 93.75% accuracy which aptitude group a participant belonged to according to his or her EEG-BCI performance. This prediction was possible using structural features extracted from DTI images (speciﬁcally the FA value), but not using structural features extracted from T1 images. Strong signiﬁcant correlations between BCI performance and FA values of the region of interest (ROI) deﬁned in the AAL atlas were found for right Cingulum, left superior Fronto-occipital Fasciculus, Body of Corpus Callosum, left Cerebral Peduncle, and right posterior Corona Radiata (see Table 2 for details). Even though the correlation of the FA-values (e.g., the cingulum in Table 2) in this study with BCI accuracy is weaker than the correlation of the SMR amplitude with accuracy (r = 0.63 vs. r = 0.73) we believe that the presented data is a valuable contribution to the construction of a comprehensive model of BCI performance in addition to the data that is already available (Blankertz et al., 2010; Kleih et al., 2010; GrosseWentrup et al., 2011; Halder et al., 2011, 2013; Kaufmann et al., 2011; Hammer et al., 2012). This knowledge can be used to design novel BCI training paradigms which speciﬁcally increase the microstructural integrity of central white matter.

Local FA values can be an indicator of myelinization quality, which is critical to the maintenance of appropriate conduction velocities for interregional communication in the brain. It is noteworthy that Valdés-Hernández et al. (2010) report a statistical relation of the spectral position of the alpha peak or the alpha frequency and FA values in a large sample of 222 participants in regions similar to those identiﬁed here. Thalamocortical/corticothalamic ﬁbers, commissural ﬁbers, and association ﬁbers such as parts of the Fronto-Occipital Fascicles show a relation to EEG measures also in their sample. In accordance with our ﬁndings on TIV and relative volume estimations, purely volumetric anatomical MRI information (head size and neocortical surface area) did not yield any signiﬁcant relation with the EEG measures in Valdés-Hernández et al. (2010). The probability of an association between EEG phenomena and the structure of thalamocortical connections rather than the thalamus itself, which would have shown in our anatomical volumetric analysis (e.g., through structures such as the thalamocortical parts of the corona radiata) is strengthened by our present data.

Further, both Whitford et al. (2010) and Teipel et al. (2009) report an association of white matter FA in commissural regions with interhemispheric transfer times (Whitford et al., 2010), as well as an association of FA in the middle Cerebellar Peduncle, the Cingulum and frontal and occipital white matter with measures of interhemispheric alpha coherence at various sites (Teipel et al., 2009).

While activity in the alpha-band and the SMR are phenomena which emerge from distinct neurophysiological origins their frequency (Alpha 8–12Hz, SMR 8–15Hz) overlaps considerablyand both are generated through thalamo-cortical loops. With regard to the strong association of white matter FA and phenomena within these frequencies it is possible, that localized differences in white matter structural integrity are most apparent in these EEG features.

With respect to the SMR, the fact that discriminatory information could be found in the present sample in white matter structures associated with the somatomotoric system (Internal Capsule, Cerebral Peduncle, Middle Cerebellar Peduncle) indicates that microstructural characteristics of the white matter system connecting motor and somatosensory regions within the brain and with the periphery are highly relevant to the formation of an individual SMR and the ability to utilize it for communication and control.

The fact that extra-motoric white matter tracts (e.g., the Fronto-Occipital Fasciculus) also contained information for the discrimination suggests, that these tracts—connecting higher order association cortices—are critical for the large-scale integration and intentional modulation of the SMR via motor imagery. Successful motor imagery requires the recollection of memorized kinesthetic percepts, the assembly of these percepts into a coherent mental image and the ability to intentionally manipulate that mental image by performing sequences of imaginary movements. The microstructure of cingular white matter in the vicinity of the Hippocampus might be responsible for the recollection process, while interhemispheric and fronto-occipital tracts affect imagery and control of that mental image in the frame of the entire BCI task.

Whether such differences—found in the domain of structural traits and functional activation differences (Halder et al., 2011)all originate from a latent factor which causes these differences and also inﬂuences BCI-aptitude, or whether the identiﬁed features are of causal relevance for BCI-aptitude themselves can only be resolved by future experiments.

Although based on the present data a link between local FA and BCI performance seems highly intuitive, the underlying causal mechanism remains only poorly understood. In order to investigate a causal link between psychological (Hammer et al., 2012) and neurophysiological predictors of BCI performance with white matter properties we need to record DTI in a larger sample of BCI-users that is as well assessed psychologically. A hypothetical relationship of conduction velocity and local FA could be investigated by combining an interhemispheric transfer time experiment (Whitford et al., 2010) with an assessment of BCI performance. Furthermore, a relationship between EEG features in the Alpha/SMR frequency domain could be characterized further by systematically associating these phenomena with FA measures from a large population, in which the metrics in question vary across a considerable range. More sophisticated DTI measurement schemes with a higher number of applied diffusion directions and better spatial resolution will enable the reconstruction of white matter tracts using tractography methods, which could provide an indication whether the observed differences in local FA merely originate from variations across the dimension of myelinization quality/tissue integrity or whether the

anisotropy of some diffusion tensors is reduced due to a higher number of crossing, kissing, or splitting ﬁber tracts in the voxels of the deep white matter structures in question. Such a ﬁnding could indicate more diverse white matter wiring patterns in subjects with low local FA in these structures, rather than indicate variations in myelinization quality. Graph theoretical analysis of white matter connectivity in BCI-users could bring new insights regarding this question and is already beginning to be explored (Buch et al., 2012).

A real time-fMRI training (Caria et al., 2010; Lee et al., 2011) for voluntary up-regulation of SMA-activity (Halder et al., 2011) or extensive training-interventions to increase the FA in the identiﬁed white matter regions could yield further insight into the role of these features in the formation of individual BCIaptitude. Recently it has been shown that extensive training with an EEG-BCI increases motor cortex responsiveness (assessed with transcranial magnetic stimulation) and also the global efﬁciency index of the scalp electrode connectivity matrix (Pichiorri et al., 2011). It is conceivable that these changes will also be reﬂected in a change of FA values. Such an association between white matter connectivity features (such as FA) and the factors that inﬂuence motor learning (such as SMR features) is subject of ongoing research in the area of stroke rehabilitation (Buch et al., 2012).

One of the central purposes of BCI is their potential to enable communication in patients with progressive degeneration of the motor system such as ALS. While ALS was long considered a disease with mainly motor system speciﬁc cerebral involvement, this notion is changing in the light of recent ﬁndings on the extensive involvement of extra-motor white matter structures such as the Corpus Callosum (Filippini et al., 2010), Cingulum (Woolley et al., 2011), Uncinate Fasciculus (Sato et al., 2010) or in regions such as the Insula, Hippocampus, the ventrolateral Pre-motor Cortex (PMC), Parietal Cortex, and bilateral Frontal Cortex (Senda et al., 2011). Based on these ﬁndings it can be assumed that the pathology in late-stage ALS spreads to multiple central white matter regions, which may be considered critical for the control of those EEG features that are presently used in most BCI applications (e.g., P300, SMR), hence impairing the ability of the patients to utilize present BCI. Birbaumer et al. (2008) proposed that in complete locked-in state (CLIS) output oriented goal directed thinking and imagery impedes and extinguishes instrumental learning of BCI-control leading to an inability of these patients to communicate (Kübler and Birbaumer, 2008). The dysfunctional ﬁber structure may thus be the consequence or the cause of this deﬁcit.

Fortunately, the notion that white matter microstructure and connectivity no longer change in the adult brain had to be corrected in the light of present ﬁndings on the effectiveness of learning interventions such as meditation (Tang et al., 2010), training of working memory (Takeuchi et al., 2010), or juggling training (Scholz et al., 2009) in increasing local FA in certain motor and extra-motor structures—indicating that countermeasures against the deterioration of central white matter in certain pathologies and for the maintenance of individual BCIaptitude for late-stage communication in ALS should be possible.

Besides for communication, BCIs are being used more and more for other applications such as motor restoration in patients

with stroke or other brain damage (Birbaumer et al., 2008; Silvoni et al., 2011). In this ﬁeld in particular a reliable prediction of BCI aptitude is useful due to the high amount of effort and time involved in this form rehabilitation. In addition to this MRI scans are routinely performed as part of the diagnosis and the DTI data can thus be collected with only a small amount of additional effort. In addition BCI technology has also been used to detect if patients with disorders of consciousness can follow commands, often using MRI, but recently also using EEG (Owen et al., 2006; Lulé et al., 2013). In both usage scenarios, success is already important on a single case basis. Thus, we believe the additional effort of collecting DTI data, that will make successful communication more probable, to be easily justiﬁable.

The data presented in this paper does not explain 100% of the variance of performance. Thus, other factors besides the ones evaluated here must inﬂuence BCI performance. Besides the dependency of performance on brain structure psychological factors such as motivation have been shown to have an inﬂuence (Kleih et al., 2010; Hammer et al., 2012). In addition to this physiological traits such as heart-rate-variability or the amplitude of the resting state SMR have been shown to impact BCI performance (Blankertz et al., 2010; Kaufmann et al., 2011). Another aspect of performance will be inﬂuenced by more transient factors such as the current level of fatigue or attentiveness. Thus, one limitation of the current study is that the session-tosession stability of the investigated factor was not investigated. Finally, to gain a conclusive predictor of performance all of the aforementioned factors will have to be integrated into a single model.

### 5. CONCLUSIONS

Microstructural characteristics of cerebral white matter have a strong (93.75% correct prediction) predictive power of SMR-BCI performance, which may have implications for these training procedures. We can assume that the identiﬁed white matter traits will not change within a single session of BCI training. Therefore, our ﬁndings indicate that the best strategy of improving BCI performance in low aptitude users is by conducting a long-term BCI training program consisting of multiple sessions, that does not only target to increase proﬁciency in BCI usage for communication and control but attempts to incorporate interventions that increase or stabilize the microstructural integrity of BCI-critical central white matter.

### ACKNOWLEDGMENTS

Funded by Deutsche Forschungsgemeinschaft (DFG) BI 195/58-1. This work is supported by SFB 550/B5 and C6, BMBF (Bundesministerium für Bildung und Forschung) Bernstein Center for Neurocomputation (Nr 01GQ0831), the European Research Council Grant (ERC 227632-BCCI), and European ICT Programm Project FP7-288566. This paper reﬂects the authors’ views only and funding agencies are not liable for any use that may be made of the information contained herein. This publication was funded by the German Research Foundation (DFG) and the University of Wuerzburg in the funding programme Open Access Publishing.

### REFERENCES

Allison, B. Z., McFarland, D. J., Schalk, G., Zheng, S. D., Jackson, M. M., and Wolpaw, J. R. (2008). Towards an independent braincomputer interface using steady state visual evoked potentials. Clin. Neurophysiol. 119, 399–408.

Ashburner, J., and Friston, K. J. (2005). Uniﬁed segmentation. Neuroimage 26, 839–851.

Berger, H. (1929). Über das elektrenkephalogramm des menschen. Arch. Psychiatr. Nervenkr. 87, 527–570.

Birbaumer, N., Elbert, T., Canavan, A. G., and Rockstroh, B. (1990). Slow potentials of the cerebral cortex and behavior. Physiol. Rev. 70, 1–41.

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kübler, A., et al. (1999). A spelling device for the paralysed. Nature 398, 297–298. Birbaumer, N., Murguialday, A. R., and Cohen, L. (2008). Brain-computer interface in paralysis. Curr. Opin. Neurol. 21, 634–638.

Blankertz, B., Lemm, S., Treder, M., Haufe, S., and Müller, K.-R. (2011). Single-trial analysis and classiﬁcation of ERPcomponents – a tutorial. Neuroimage 56, 814–825.

Blankertz, B., Losch, F., Krauledat, M., Dornhege, G., Curio, G., and Müller, K.-R. (2008). The Berlin Brain–Computer Interface: accurate performance from ﬁrstsession in BCI-naive subjects. IEEE Trans. Biomed. Eng. 55, 2452–2462.

Blankertz, B., Sannelli, C., Halder, S., Hammer, E. M., Kübler, A., Müller, K.-R., et al. (2010). Neurophysiological predictor of SMR-based BCI performance. Neuroimage 51, 1303–1309.

Buch, E. R., Modir Shanechi, A., Fourkas, A. D., Weber, C., Birbaumer, N., and Cohen, L. G. (2012). Parietofrontal integrity determines neural modulation associated with grasping imagery after stroke. Brain 135(Pt 2), 596–614.

Caria, A., Sitaram, R., Veit, R., Begliomini, C., and Birbaumer, N. (2010). Volitional control of anterior insula activity modulates the response to aversive stimuli. a real-time functional magnetic resonance imaging study. Biol. Psychiatry 68, 425–432.

De Massari, D., Matuz, T., Furdea, A., Ruf, C. A., Halder, S., and Birbaumer, N. (2013). Braincomputer interface and semantic

classical conditioning of communication in paralysis. Biol. Psychol. 92, 267–274.

Farwell, L. A., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing even-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523.

Filippini, N., Douaud, G., Mackay, C. E., Knight, S., Talbot, K., and Turner, M. R. (2010). Corpus callosum involvement is a consistent feature of amyotrophic lateral sclerosis. Neurology 75, 1645–1652.

Furdea, A., Ruf, C. A., Halder, S., De Massari, D., Bogdan, M., Rosenstiel, W., et al. (2012). A new (semantic) reﬂexive braincomputer interface: in search for a suitable classiﬁer. J. Neurosci. Methods 203, 233–240.

Grosse-Wentrup, M., Schölkopf, B., and Hill, J. (2011). Causal inﬂuence of gamma oscillations on the sensorimotor rhythm. Neuroimage 56, 837–842.

Guger, C., Daban, S., Sellers, E., Holzner, C., Krausz, G., Carabalona, R., et al. (2009). How many people are able to control a P300-based brain-computer interface (BCI)? Neurosci. Lett. 462, 94–98.

Halder, S., Agorastos, D., Veit, R., Hammer, E. M., Lee, S., Varkuti, B., et al. (2011). Neural mechanisms of brain-computer interface control. Neuroimage 55, 1779–1790.

Halder, S., Hammer, E. M., Kleih, S. C., Bogdan, M., Rosenstiel, W., Birbaumer, N., et al. (2013). Prediction of auditory and visual P300 brain-computer interface aptitude. PLoS ONE 8:e53513. doi: 10.1371/journal.pone.0053513

Hammer, E. M., Halder, S., Blankertz, B., Sannelli, C., Dickhaus, T., Kleih, S., et al. (2012). Psychological predictors of SMR-BCI performance. Biol. Psychol. 89, 80–86.

Hari, R., and Salmelin, R. (1997). Human cortical oscillations: a neuromagnetic view through the skull. Trends Neurosci. 20, 44–49.

Kaufmann, T., Vögele, C., Sütterlin, S., Lukito, S., and Kübler, A. (2011). Effects of resting heart rate variability on performance in the P300 brain-computer interface. Int. J. Psychophysiol. 83, 336–341.

Kleih, S. C., Kaufmann, T., Zickler, C., Halder, S., Leotta, F., Cincotti, F., et al. (2011). Out of the frying pan into the ﬁre–the P300-based BCI faces real-world challenges. Prog. Brain Res. 194, 27–46.

Kleih, S. C., Nijboer, F., Halder, S., and Kübler, A. (2010). Motivation

modulates the P300 amplitude during brain-computer interface use. Clin. Neurophysiol. 121, 1023–1031.

Kübler, A., and Birbaumer, N. (2008). Brain-computer interfaces and communication in paralysis: extinction of goal directed thinking in completely paralysed patients? Clin. Neurophysiol. 119, 2658–2666.

Kübler, A., Blankertz, B., Müller, K.-R., and Neuper, C. (2011). “A model of BCI control,” in Proceedings of the 5th International BrainComputer Interface Conference, eds G. R. Müller-Putz, R. Scherer, M. Billinger, A. Kreilinger, V. Kaiser, and C. Neuper, 100–103.

Kübler, A., Neumann, N., Kaiser, J., Kotchoubey, B., Hinterberger, T., and Birbaumer, N. P. (2001). Brain-computer communication: self-regulation of slow cortical potentials for verbal communication. Arch. Phys. Med. Rehabil. 82, 1533–1539.

Kübler, A., Neumann, N., Wilhelm, B., Hinterberger, T., and Birbaumer, N. (2004). Brain-computer predictability of brain-computer communication. J. Psychophysiol. 18, 121–129.

Kübler, A., Nijboer, F., Mellinger, J., Vaughan, T. M., Pawelzik, H., Schalk, G., et al. (2005). Patients with ALS can use sensorimotor rhythms to operate a braincomputer interface. Neurology 64, 1775–1777.

Kuhlman, W. N. (1978). Functional topography of the human Murhythm. Electroencephalogr. Clin. Neurophysiol. 44, 83–93.

Lee, S., Ruiz, S., Caria, A., Veit, R., Birbaumer, N., and Sitaram, R. (2011). Detection of cerebral reorganization induced by real-time fMRI feedback training of insula activation: a multivariate investigation. Neurorehabil. Neural Repair 25, 259–267.

Lulé, D., Noirhomme, Q., Kleih, S. C., Chatelle, C., Halder, S., Demertzi, A., et al. (2013). Probing command following in patients with disorders of consciousness using a brain-computer interface. Clin. Neurophysiol. 124, 101–106.

Mak, J. N., McFarland, D. J., Vaughan, T. M., McCane, L. M., Tsui, P. Z., Zeitlin, D. J., et al. (2012). EEG correlates of P300-based brain-computer interface (BCI) performance in people with amyotrophic lateral sclerosis. J. Neural Eng. 9:026014. doi: 10.1088/1741-2560/9/2/026014

Middendorf, M., McMillan, G., Calhoun, G., and Jones, K. S.

(2000). Brain-computer interfaces based on the steady-state visual-evoked response. IEEE Trans. Rehabil. Eng. 8, 211–214.

Neumann, N., and Birbaumer, N. (2003). Predictors of successful self control during braincomputer communication. J. Neurol Neurosurg. Psychiatry 74, 1117–1121.

Neuper, C., Müller, G. R., Kübler, A., Birbaumer, N., and Pfurtscheller, G. (2003). Clinical application of an EEG-based brain-computer interface: a case study in a patient with severe motor impairment. Clin. Neurophysiol. 114, 399–409.

Neuper, C., Scherer, R., Wriessnegger, S., and Pfurtscheller, G. (2009). Motor imagery and action observation: modulation of sensorimotor brain rhythms during mental control of a brain-computer interface. Clin. Neurophysiol. 120, 239–247.

Nijboer, F., Furdea, A., Gunst, I., Mellinger, J., McFarland, D. J., Birbaumer, N., et al. (2008a). An auditory brain-computer interface (BCI). J. Neurosci. Methods 167, 43–50.

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., et al. (2008b). A P300-based braincomputer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916.

Owen, A. M., Coleman, M. R., Boly, M., Davis, M. H., Laureys, S., and Pickard, J. D. (2006). Detecting awareness in the vegetative state. Science 313, 1402.

Pfurtscheller, G., and da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857.

Pfurtscheller, G., Neuper, C., Andrew, C., and Edlinger, G. (1997). Foot and hand area mu rhythms. Int. J. Psychophysiol. 26, 121–135.

Pichiorri, F., De Vico Fallani, F., Cincotti, F., Babiloni, F., Molinari, M., Kleih, S. C., et al. (2011). Sensorimotor rhythm-based braincomputer interface training: the impact on motor cortical responsiveness. J. Neural Eng. 8:025020. doi: 10.1088/1741-2560/8/2/025020

Polich, J. (2007). Updating P300: an integrative theory of P3a and P3b. Clin. Neurophysiol. 118, 2128–2148.

Ramoser, H., Müller-Gerking, J., and Pfurtscheller, G. (2000). Optimal spatial ﬁltering of single trial EEG during imagined hand movement. IEEE Trans. Rehabil. Eng. 8, 441–446.

Regan, D. (1977). Steady-state evoked potentials. J. Opt. Soc. Am. 67, 1475–1489.

Ruf, C. A., De Massari, D., Furdea, A., Matuz, T., Fioravanti, C., van der Heiden, L., et al. (2013). Semantic classical conditioning and braincomputer interface (BCI) control: encoding of afﬁrmative and negative thinking. Front. Neurosci 7:23. doi: 10.3389/fnins.2013.00023

Sato, K., Aoki, S., Iwata, N. K., Masutani, Y., Watadani, T., Nakata, Y., et al. (2010). Diffusion tensor tract-speciﬁc analysis of the uncinate fasciculus in patients with amyotrophic lateral sclerosis. Neuroradiology 52, 729–733.

Scholz, J., Klein, M. C., Behrens, T. E. J., and Johansen-Berg, H. (2009). Training induces changes in white-matter architecture. Nat. Neuroscience 12, 1370–1371.

Senda, J., Kato, S., Kaga, T., Ito, M., Atsuta, N., Nakamura, T., et al. (2011). Progressive and widespread brain damage in ALS: MRI voxelbased morphometry and diffusion tensor imaging study. Amyotroph. Lateral Scler. 12, 59–69.

Sharbrough, F. W., Chatrian, G.-E., Lesser, R. P., Lüders, H., Nuwer, M.,

and Picton, T. W. (1991). American electroencephalographic society guidelines for standard electrode position nomenclature. J. Clin. Neurophysiol. 8, 200–202.

Silvoni, S., Ramos-Murguialday, A., Cavinato, M., Volpato, C., Cisotto, G., Turolla, A., et al. (2011). Braincomputer interface in stroke: a review of progress. Clin. EEG Neurosci. 42, 245–252.

Silvoni, S., Volpato, C., Cavinato, M., Marchetti, M., Priftis, K., Merico, A., et al. (2009). P300-based brain-computer interface communication: evaluation and followup in amyotrophic lateral sclerosis. Front. Neurosci. 3:60. doi: 10.3389/neuro.20.001.2009

Takeuchi, H., Sekiguchi, A., Taki, Y., Yokoyama, S., Yomogida, Y., Komuro, N., et al. (2010). Training of working memory impacts structural connectivity. J. Neurosci. 30, 3297–3303.

Tang, Y.-Y., Lu, Q., Geng, X., Stein, E. A., Yang, Y., and Posner, M. I. (2010). Short-term meditation induces white matter changes in the anterior cingulate. Proc. Natl. Acad. Sci. U.S.A. 107, 15649–15652.

Teipel, S. J., Pogarell, O., Meindl, T., Dietrich, O., Sydykova, D., Hunklinger, U., et al. (2009). Regional networks underlying interhemispheric connectivity: an EEG and DTI study in healthy ageing and amnestic mild cognitive impairment. Hum. Brain Mapp. 30, 2098–2119.

Valdés-Hernández, P. A., OjedaGonzález, A., Martínez-Montes, E., Lage-Castellanos, A., ViruésAlba, T., Valdés-Urrutia, L., et al. (2010). White matter architecture rather than cortical surface area correlates with the EEG alpha rhythm. Neuroimage 49, 2328–2339.

Whitford, T. J., Kubicki, M., Ghorashi, S., Schneiderman, J. S., Hawley, K. J., McCarley, R. W., et al. (2010). Predicting inter-hemispheric transfer time from the diffusion properties of the corpus callosum in healthy individuals and schizophrenia patients: a combined ERP and DTI study. Neuroimage 54, 2318–2329.

Woolley, S. C., Zhang, Y., Schuff, N., Weiner, M. W., and Katz, J. S. (2011). Neuroanatomical correlates of apathy in ALS using

4 Tesla diffusion tensor MRI. Amyotroph. Lateral Scler. 12, 52–58.

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 02 January 2013; accepted: 13 March 2013; published online: 02 April 2013. Citation: Halder S, Varkuti B, Bogdan M, Kübler A, Rosenstiel W, Sitaram R and Birbaumer N (2013) Prediction of brain-computer interface aptitude from individual brain structure. Front. Hum. Neurosci. 7:105. doi: 10.3389/fnhum. 2013.00105

Copyright © 2013 Halder, Varkuti, Bogdan, Kübler, Rosenstiel, Sitaram and Birbaumer. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in other forums, provided the original authors and source are credited and subject to any copyright notices concerning any third-party graphics etc.

