##### ORIGINAL RESEARCH ARTICLE

published: 15 July 2014 doi: 10.3389/fneng.2014.00026

## NEUROENGINEERING

# Changes in functional brain organization and behavioral correlations after rehabilitative therapy using a brain-computer interface

### Brittany M. Young1,2,3, Zack Nigogosyan1, Léo M. Walton3,4, Jie Song1,4, Veena A. Nair1, Scott W. Grogan1, Mitchell E. Tyler4, Dorothy F. Edwards5, Kristin Caldera6, Justin A. Sattin7, Justin C. Williams3,4 and Vivek Prabhakaran1,2,3,7*

- 1 Department of Radiology, University of Wisconsin–Madison, Madison, WI, USA
- 2 Medical Scientist Training Program, University of Wisconsin–Madison, Madison, WI, USA
- 3 Neuroscience Training Program, University of Wisconsin–Madison, Madison, WI, USA
- 4 Department of Biomedical Engineering, University of Wisconsin–Madison, Madison, WI, USA
- 5 Departments of Kinesiology and Medicine, University of Wisconsin–Madison, Madison, WI, USA
- 6 Department of Orthopedics and Rehabilitation, University of Wisconsin–Madison, Madison, WI, USA
- 7 Department of Neurology, University of Wisconsin–Madison, Madison, WI, USA

Edited by: Jaime A. Pineda, University of California, San Diego, USA

Reviewed by: Hun-Kuk Park, Kyung Hee University, Korea (South) Paul F. M. J. Verschure, Center for Neuro-Robotics and Autonomous Systems, Spain

*Correspondence: Vivek Prabhakaran, Department of Radiology, University of Wisconsin Hospital & Clinics, 600 Highland Avenue, Madison, WI 53792, USA e-mail: vprabhakaran@uwhealth.org

This study aims to examine the changes in task-related brain activity induced by rehabilitative therapy using brain-computer interface (BCI) technologies and whether these changes are relevant to functional gains achieved through the use of these therapies. Stroke patients with persistent upper-extremity motor deﬁcits received interventional rehabilitation therapy using a closed-loop neurofeedback BCI device (n = 8) or no therapy (n = 6). Behavioral assessments using the Stroke Impact Scale, the Action Research Arm Test (ARAT), and the Nine-Hole Peg Test (9-HPT) as well as task-based fMRI scans were conducted before, during, after, and 1 month after therapy administration or at analogous intervals in the absence of therapy. Laterality Index (LI) values during ﬁnger tapping of each hand were calculated for each time point and assessed for correlation with behavioral outcomes. Brain activity during ﬁnger tapping of each hand shifted over the course of BCI therapy, but not in the absence of therapy, to greater involvement of the non-lesioned hemisphere (and lesser involvement of the stroke-lesioned hemisphere) as measured by LI. Moreover, changes from baseline LI values during ﬁnger tapping of the impaired hand were correlated with gains in both objective and subjective behavioral measures. These ﬁndings suggest that the administration of interventional BCI therapy can induce differential changes in brain activity patterns between the lesioned and non-lesioned hemispheres and that these brain changes are associated with changes in speciﬁc motor functions.

Keywords: brain-computer interface, stroke rehabilitation, laterality index, LI, BCI therapy, UE motor recovery, fMRI

### INTRODUCTION

Stroke remains a growing source of disability, with nearly 800,000 individuals in the United States alone experiencing a stroke each year and a projected increase of 22% in stroke prevalence by 2030 (Go et al., 2013). Despite increases in stroke incidence, stroke deaths have declined in recent years (Go et al., 2013), such that the majority of stroke patients survive their initial stroke event. Individuals in this growing population of stroke survivors are often left with persistent functional deﬁcits. One common deﬁcit is the acquisition of a lasting motor impairment, with up to 50% of stroke survivors suffering from some degree of hemiparesis and 26% needing assistance with activities of daily living (ADLs) 6 months post-stroke (Kelly-Hayes et al., 2003).

It has long been known that most patients experience some amount of spontaneous functional recovery shortly after stroke,

with additional improvements that may be gained through the use of rehabilitative therapies in the months following the stroke event. Current guidelines note that there exists a lack of evidence to guide the optimal selection of a particular type, intensity, and amount of rehabilitative motor therapy for stroke survivors (Miller et al., 2010), and many stroke patients reach a functional plateau before complete recovery is achieved despite the use of currently available standard rehabilitative therapies. However, studies have suggested that clinically relevant plasticity and recovery potential still persist even after this plateau has been reached and that it may be possible to harness this reserve of recovery potential through the use of alternative, non-traditional therapies (Cramer, 2010) that incorporate components such as virtual reality (Orihuela-Espina et al., 2013), robot-assisted movement therapy (Lo et al., 2010; Pinter et al., 2013), and constraint-induced

movement therapy (CIMT) (Johansen-Berg et al., 2002a; Moss and Nicholas, 2006; Gauthier et al., 2008; Wolf et al., 2008, 2010; Dromerick et al., 2009; Volpe et al., 2009; Lang et al., 2013).

Another of these alternative non-traditional therapies that shows promise in stimulating additional recovery in stroke patients incorporates devices that use an emerging type of technology called brain-computer interface (BCI). EEG-based BCI is a developing technology that detects neural activity and can use these signals as a means of providing real-time feedback by which users may learn to modulate their brain activity. It has been shown that people with disabilities have no greater mental workload compared to healthy controls when using BCI devices (Felton et al., 2012), making the potential for BCI therapy in stroke patients with persistent motor disabilities both appropriate and accessible. Currently, BCI technology is being incorporated into a new class of devices intended to facilitate motor recovery in stroke patients, and early studies are beginning to show potential functional beneﬁts associated with the use of these devices (Buch et al., 2008; Daly et al., 2009; Broetz et al., 2010; Prasad et al., 2010; Caria et al., 2011; Shindo et al., 2011; Liu et al., 2012; Takahashi et al., 2012). One of the motivations behind this emerging trend is the idea that BCI technology may provide a means of promoting neuroplastic change, harnessing the recovery potential that remains once patients have reached a functional plateau with standard therapies.

There is reason to believe that therapy using BCI devices may produce changes in brain activation patterns concurrent with observed behavioral changes. Such changes have been observed using other interventional rehabilitative approaches in stroke patients (Carey et al., 2002; Gauthier et al., 2008; Richards et al.,

- 2008), and changes in brain activity patterns after stroke have also been associated with functional gains in stroke patients who experience spontaneous recovery (Ward et al., 2003). Since BCI therapies provide real-time feedback to the user, effectively rewarding the consistent production of some patterns of brain activity relative to others in the context of an intended task, there may be observable changes in the brain activation patterns produced when attempting tasks similar to those trained with BCI therapy. While this theoretical knowledge supports the possibility of inducing changes in brain activation through BCI therapy, little is yet known about the speciﬁc patterns of brain change induced in stroke patients by therapies that incorporate BCI devices.

Brain changes can be measured by laterality index (LI)– a means of quantifying the degree to which a particular task or function is lateralized between the two hemispheres of the brain. LI can be used as a measure of functional brain organization (Kundu et al., 2013) and has been used to examine functional brain reorganization in stroke patients with motor deﬁcits using other therapy modalities. For example, LI calculations have shown repetitive transcranial magnetic stimulation therapy to produce increased laterality toward the lesioned hemisphere in those with bilateral LI at baseline (Yamada et al., 2013). Improved function has also been observed with increases in laterality toward the lesioned hemisphere after mirror therapy (Bhasin et al., 2012) or CIMT (Johansen-Berg et al., 2002a), and recruitment of contralesional motor areas has been associated with better functional improvements after gesture therapy

(Orihuela-Espina et al., 2013). Still other studies of neuroimaging after rehabilitative motor therapy using such approaches have shown functional gains in the absence of detectable differences in LI after constraint-induced movement (Kononen et al., 2012) or robot-assisted (Pinter et al., 2013) therapies. Whether these conﬂicting patterns of change across studies represent underlying differences in the populations studied, differential effects to various interventional therapy modalities producing the functional gains, or other confounding effects remains a question that has yet to be deﬁnitively answered.

Studies that have examined changes in brain activity after BCI combined with other therapies in these patients have found brain-behavior correlations in the context of functional connectivity and its relationship to the rate at which individuals achieved gains in motor function using a BCI-robotics treatment protocol (Varkuti et al., 2013) as well as in the association between LI changes and motor function improvements using a BCI-physiotherapy treatment protocol (Caria et al., 2011; Ramos-Murguialday et al., 2013). However, such BCI studies and analyses to date remain few and limited in the context of combined therapies. The aim of the present study was to investigate the effect of interventional therapy using a closed-loop neurofeedback BCI device intended to improve motor function in stroke patients on task-derived patterns of brain activation and to assess whether any observable changes in these activation patterns correlated to changes in behavioral outcomes. We examined subjective and objective measures of motor function and obtained fMRI scans of brain activation patterns during a ﬁnger tapping task at four different time points with and without the administration of BCI therapy. We hypothesized that changes in brain activation during tapping would be observable with the administration of BCI therapy. We also examined the relationship between changes in LI with gains in motor function, hypothesizing that changes observed in LI would correlate with changes in motor function.

### MATERIALS AND METHODS

#### RECRUITMENT METHODS AND EXCLUSION CRITERIA

Patients with persistent upper extremity motor impairment resulting from ﬁrst-ever ischemic or hemorrhagic stroke were contacted regarding study participation after being identiﬁed as appropriate for participation in the study by one or more physicians responsible for their care at the University of Wisconsin Hospital and Clinics. Exclusion criteria included concurrent diagnoses of neurodegenerative disorders (e.g., dementia), other neurological or psychiatric disorders (e.g., epilepsy, schizophrenia, substance abuse), or cognitive deﬁcits that would preclude the ability to provide informed consent. Subjects were also excluded if they had any allergies to electrode gel, surgical tape, or metals, had undergone treatment for recent infectious diseases, had apparent lesions or inﬂammation of the oral mucosa, were pregnant or likely to become pregnant during the course of the study, or had any contraindications to MRI.

#### ETHICS STATEMENT

All subjects provided written informed consent. This study, including all measures assessed and therapies administered, was

approved by the Health Sciences Institutional Review Board of the University of Wisconsin–Madison.

#### RANDOMIZATION AND STUDY PARADIGM

A permuted-block design accounting for gender, stroke chronicity, and severity of motor impairment was used to randomize subjects to either a BCI therapy group or a crossover control group. Subjects assigned to the BCI therapy group began participation in the BCI therapy phase of the study and received interventional rehabilitation therapy using the BCI system with functional assessment and MRI scanning at four time points: before the start of BCI therapy, at the midpoint of BCI therapy, upon completion of all BCI therapy, and 1 month following the last BCI therapy session. Subjects assigned to the crossover control group ﬁrst received three additional functional assessments and MRI scans during the control phase of the study in which no BCI therapy was administered, with assessments spaced at intervals analogous to those administered during the BCI therapy phase of the study. Upon completion of the control phase of the study, subjects in the crossover control group crossed over to complete the BCI therapy phase of the study. This study paradigm is summarized in Figure 1.

#### FUNCTIONAL ASSESSMENTS

Subjects’ motor function of the impaired arm was assessed using a neuropsychological battery which included both subjective and objective measures. These measures included the Stroke Impact Scale 3.0 (SIS), which is a self-report measure used to assess the ability of a stroke survivor to perform in the domains of strength, hand function, activities of daily living, mobility, communication, emotion, memory and thinking, and participation (Duncan et al., 1999; Carod-Artal et al., 2008). For this study, scores from the Hand Function domain of the SIS were of particular interest,

- as the BCI therapy administered is designed to promote motor rehabilitation of the upper extremity. Also assessed were subject performance on the Action Research Arm Test (ARAT), which is a standardized series of scored movements designed to evaluate upper extremity motor function in the domains of grip, grasp, strength, and gross movement (Carroll, 1965; Lang et al., 2006), and the Nine-Hole Peg Test (9-HPT), which is a timed task in which the subject attempts to ﬁrst place then remove each of 9 pegs from a pegboard using only one hand (Beebe and Lang,

- 2009). In keeping with standard scoring practices, raw scores for

the hand function domain of the SIS were transformed to adjust for the lowest possible raw score and the possible raw score range. Scores for the ARAT were reported as the total points scored when using the impaired hand, and scores for 9-HPT were taken as an average of two timed trials using the impaired hand. At each of the visits for neuropsychological evaluation, anatomical and functional MRI scans were also obtained for each subject.

#### INTERVENTION

All subjects were administered at least 9 and up to 15 two-hour sessions of interventional BCI therapy using SmartFES, a closedloop neurofeedback device incorporating multi-modal feedback triggered by EEG. This multi-modal feedback included visual feedback, functional electrical stimulation (FES), and tongue stimulation (TS). A diagram of the device and the sequential stages of each interventional therapy session are provided in Figure 2. A detailed description of the procedures followed during each session is provided in the supplementary methods. These sessions took place over a period of up to 6 weeks with two to three therapy sessions per week.

fMRI PARADIGM

Subjects performed a block-design sequential ﬁnger tapping task during fMRI scans that consisted of alternating 20-s blocks of tapping vs. rest. Subjects were cued to rest or to tap the ﬁngers of one hand sequentially on a button box, using either visual or tactile (for visually impaired subjects) cues.

Subjects were asked to undergo two fMRI scans using this paradigm—once when tapping with the impaired hand (passive tapping if unable to generate sufﬁcient tappings independently) and again when tapping with the unimpaired hand. Subjects were instructed to hold their heads still throughout the scans, and sufﬁcient padding was provided to discourage head movement.

#### IMAGE ACQUISITION AND PROCESSING

MRI data was collected on one of two 3 Tesla GE MR750 scanners equipped with high-speed gradients (Sigma GE Healthcare, Milwaukee Wisconsin) using an 8-channel head coil. Padding around the subjects’ heads was used to help minimize movements during scans. Functional scans were run using a T2∗-weighted gradient-echo echo planar imaging (EPI) pulse sequence sensitive to BOLD contrast. Technical parameters used to acquire these EPI scans are as follows: ﬁeld of view 224mm, matrix

|[Figure 1]<br><br>FIGURE 1 | Study paradigm. Functional assessment using Stroke Impact Scale, Action Research Arm Test, Nine-Hole Peg Test, and neuroimaging using fMRI were performed at each assessment.|
|---|

|[Figure 2]<br><br>[Figure 3]<br><br>FIGURE 2 | Brain-Computer Interface interventional therapy schematic and session outline. (A) Sequence of BCI interventional therapy session with (B) SmartFES device setup with color coding indicating feedback stimuli for the relevant session stages. BCI, Brain-Computer Interface.|
|---|

64 × 64, TR 2600ms, TE 22ms, ﬂip angle 60◦, and 40 axial plane slices of 3.5mm thickness with 3.5mm spacing between slices. During each fMRI scan, 70 sequential whole-brain acquisitions were recorded. These scanning parameters allowed for complete mapping of the cortex. A T1-weighted high-resolution anatomical image was also obtained for each subject using a BRAVO FSPGR pulse sequence during each MRI scanning session. Technical parameters used to acquire these scans are: ﬁeld of view 256mm, matrix 256 × 256, TR 8.16ms, TE 3.18ms, ﬂip angle 12◦, and 156 axial plane slices of 1mm thickness with 1mm spacing between slices.

All pre- and post-processing of MRI data was performed using the AFNI software package (Cox, 1996). The ﬁrst four volumes of each functional sequence were discarded to allow for signal stabilization. EPI data sets were motion corrected and then spatially smoothed at 6mm with a full width at half maximum Gaussian kernel. Each voxel timeseries was scaled to a mean of 100, and AFNI’s 3dDeconvolve was then used to perform a voxelwise regression analysis with six motion parameters regressed out. This analysis yielded a voxel-wise t-statistic which was then thresholded based on subsequent analysis as described below. EPI data sets were visually inspected for alignment with anatomical T1 datasets. For cases in which alignment was not acceptable, align_epi_anat.py was used to alight the anatomical T1 scan to the EPI data set in AFNI.

#### GROUP-LEVEL ACTIVATION ANALYSES

EPI datasets were transformed to 3 × 3 × 3mm resolution into Talairach space (Talairach and Tournoux, 1988), and AFNI’s 3dttest++ was used to generate maps of average group-level

activation for each time point. Group-level activation maps were clustered after using AFNI’s 3dClustSim to calculate a minimum cluster size of 300 contiguous voxels needed for cluster-based correction for multiple comparisons (p ≤ 0.05).

For the subjects who had suffered a right-sided stroke with leftsided motor impairment, statistical maps of voxel-wise t-statistics were mirrored about the midline to produce scans demonstrating a stroke lesion in the left brain. These mirrored scans were then used in subsequent group analyses, such that as a group the stroke lesion is evidenced in the left hemisphere and the resulting motor impairment was in the right upper extremity. This process made the assumption that activity in the motor network is symmetric and that these mirrored scans would be otherwise comparable to scans from the subjects with left-sided strokes similar to other studies (Johansen-Berg et al., 2002a; Ward et al., 2003; Darling et al., 2007; Carter et al., 2010a; Confalonieri et al., 2012; Lotze et al., 2012; Stagg et al., 2012).

#### LI CALCULATIONS AND ANALYSIS

Masks of signiﬁcant clusters were made for each individual subject performing each task at each timepoint using these minimum clustersize values (range 163–310 contiguous voxels). These masks of signiﬁcant clusters were created in subject space using the original subject-space voxel-wise maps of t-statistics and also in Talairach space using voxel-wise maps of t-statistics that had been transformed into Talairach space for each scan.

Three sets of ROI masks were created to examine the lateralization of motor function in these subjects to examine changes in laterality not only throughout the brain but also within smaller regions of the brain most relevant to motor function. The ﬁrst was

a pair of masks designed to capture activity throughout the whole brain (Whole Brain mask). This set was hand drawn in Talairach space to ensure complete coverage of the entire brain and then applied to the Talairached masks of signiﬁcant clusters of activation for each subject. The second pair of masks (Motor Network mask) was constructed using spheres of radius 6mm based on regions previously identiﬁed as parts of the motor network using an independent component analysis of whole-brain resting state fMRI scans (Shirer et al., 2012). The third pair of masks (Motor Cortex mask) consisted of only the cortical components from the Motor Network mask for each hemisphere. These latter two masks were resampled into subject space and then applied to the masks of signiﬁcant clusters of activation for each subject. It is worth noting that because the motor network masks were originally based empirically on whole-brain resting state fMRI scans, these masks included areas of both primary and secondary areas of motor cortex and were not completely symmetric in shape. The cerebellum components of each half of the whole-brain and motor network masks were associated with cortical and subcortical structures on the opposite side of the brain because in a normal brain coordinated movement of a given hand is mediated by the contralateral brain hemisphere in conjunction with the ipsilateral cerebellum relative to the hand. A summary of the components of each mask is presented in Table S3.

LI was calculated for each fMRI scan using each of these three sets of masks at each of two thresholds to give a quantitative measure of ﬁnger tapping lateralization. The formula (VI−VC)/(VI+VC) was used to calculate each LI value, where VI is the number of voxels in the ipsilesional hemisphere mask that show signiﬁcant activation at a preset statistical threshold and VC is the number of voxels in the contralesional hemisphere mask. Using this system, LI values above 0.2 are considered to represent ipsilesionally lateralized activity, those below −0.2 represent contralesionally lateralized activity, and those between −0.2 and 0.2 correspond to bilateral activity (Springer et al., 1999). Since LI values may change slightly when evaluated at different thresholds of signiﬁcance (Pillai and Zaca, 2011), each mask was applied

- at the thresholds of t = 2.003 and t = 4 (which correspond to p < 0.05 and p < 0.0001 respectively) in order to evaluate potential trends at both a minimally stringent and a very stringent level of signiﬁcance.

For subjects who had suffered a right-sided stroke with leftsided motor impairment, ROI masks were applied to individual masks of signiﬁcant clusters without mirroring about the midline. LI analysis was performed using the formulas detailed above, with higher LI values corresponding to increasingly ipsilesional lateralization of ﬁnger tapping function. This process again made the assumption that activity in the motor network is symmetric.

A linear mixed-effects model was used to analyze raw LI values for each mask-threshold combination within data sets from the BCI therapy and control phases to assess for changes at each time point relative to baseline.

#### LI-BEHAVIORAL CORRELATION ANALYSIS

At the individual level, values for change from baseline LI during ﬁnger tapping of the impaired hand were calculated at each time point. Values for change from baseline ARAT, baseline normalized

SIS Hand Function domain, and baseline 9-HPT scores were also calculated at each time point for each subject able to complete each respective assessment. Data from subjects who exhibited ﬂoor or ceiling effects on a particular measure were not included in the LI-behavioral correlation analysis for that measure. Floor effects were noted when a subject was consistently unable to perform all tasks necessary to complete the assessment at all time points or when the minimum possible score was achieved for the assessment at each of the four time points within a given phase of the study. Ceiling effects were noted when a subject scored the maximum possible points at each of the four time points. Thus, instances of ﬂoor and ceiling effects captured zero functional change in the subject using a particular assessment over time. These changes in functional measures were then assessed for correlations with changes in LI using a Spearman’s rank correlation analysis, making the assumption of independence among data points. However, because these data were collected using a repeated measures experimental design, some data points are not truly independent of one another. Therefore, relationships found to be statistically signiﬁcant using the Spearman’s rank correlation analysis were then re-analyzed using generalized estimating equations in order to further examine and validate the conclusions of the initial correlation model. Generalized estimating equations provide a method for examining the relationship between two variables that, unlike Spearman correlation analysis, does account for the repeated measures aspect of the data collected but also require the assumption that independent and dependent variables be named explicitly in the model design. All statistical analyses were performed in R statistical software version 3.0.1, which is freely downloadable at http://www.r-project.org/.

### RESULTS

#### PARTICIPANT CHARACTERISTICS

At the time of this analysis, 11 subjects meeting inclusion and exclusion criteria had begun participation in this ongoing study. Among these participants, ﬁve were randomized to the BCI therapy group and had completed the BCI therapy phase, three had been assigned to the crossover control group and had completed both control and intervention phases, and data from three additional subjects that had been randomized to the crossover control group was available from the control phase of the study but not from the BCI therapy phase. Therefore, data used in this study represents information obtained from 11 individual subjects with control phase data available for six subjects and BCI therapy phase data available for eight subjects.

Participant characteristics are summarized in Table 1. Data from the experimental BCI therapy group comprised data from the BCI therapy phase of the experiment from subjects 1 to 8, while control group data comprised data from the control phase of the experiment from subjects 6 to 11. Among subjects who received BCI therapy, average age was 63 years (SD = 9.5 years), and average time from stroke onset was 13.13 months (SD = 8.44 months). More subjects had right-sided impairments than left-sided impairments, but this difference was not signiﬁcant (p = 0.14). More subjects also had cortical strokes than noncortical strokes, and more subjects were male than female; these differences were not signiﬁcant (p = 0.36 for both comparisons).

- Table 1 | Participant Characteristics.

Subject ID Sex (M/F) Age (years) Handedness Stroke location Impaired NIHSS Level of Time from stroke hand (score) impairment (months)

- 1 M 52 R L MCA R 8 Severe 15
- 2 F 61 R L frontal lobe R 8 Severe 16
- 3 M 68 R L centrum semiovale R 0 Mild 3
- 4 M 66 R L MCA R 6 Severe 23
- 5 F 73 R L MCA R 0 Mild 2
- 6 F 75 R R putamen L 7 Severe 23
- 7 M 61 R L basal ganglia R 0 Mild 17
- 8 M 48 L R pons L 3 Moderate 6
- 9 M 56 R L MCA R 2 Moderate 11
- 10 M 48 R R medulla L 6 Severe 5
- 11 M 51 R R MCA L 4 Severe 16

L, left; R, right; MCA, Middle cerebral artery.

Among subjects from whom data was collected during from the control phase, average age was 56.5 years (SD = 10.34 years), and average time from stroke was 13 months (SD = 6.96 months). More subjects who completed the control phase of the experiment had left-sided impairments than right-sided impairments, and more had non-cortical stroke than cortical strokes, but these differences were not signiﬁcant (p = 0.688 for both). Similar to subjects who received BCI therapy, more subjects were male than female, but this difference was not signiﬁcant (p = 0.22). In both groups, more subjects were right-handed than lefthanded, but this difference was again not signiﬁcant (p = 0.14 for BCI therapy recipients; p = 0.22 among control phase subjects).

#### SUBJECT RETENTION AND COMPLIANCE

Of the subjects enrolled, there were no drop outs due to subject desire to cease participation in the study or from any reported unpleasant experiences with the assessments or therapies administered. One participant, Subject 7, was not assessed or scanned at the ﬁnal time point 1 month after the cessation of all BCI therapy due to scheduling conﬂicts between subject availability and scanner availability that prevented him from participating during the appropriate time window.

#### FUNCTIONAL ACTIVATION MAPS

Group-level activation maps during ﬁnger tapping of the unimpaired hand (Figure 3) showed changes in overall activation patterns, with baseline bilateral activation progressing to largely contralesionally lateralized activation over the course of therapy. These changes appear to have persisted to some degree 1 month after the cessation of BCI therapy. When considering grouplevel activation patterns observed during ﬁnger tapping of the impaired hand (Figure 4), a progression from more ipsilesional activity at baseline to bilateral activation was observed over the course of therapy. These changes again persisted 1 month after the cessation of BCI therapy. No such trends in group-level activation during ﬁnger tapping were noted over the course of the control phase of the experiment among subjects who completed the control phase of therapy.

|[Figure 4]<br><br>FIGURE 3 | Group level activation maps for ﬁnger tapping of the unimpaired hand during the BCI therapy phase of the experiment. Panels demonstrate activation assessed (A) pre-therapy, (B) mid-therapy, (C) upon completion of therapy, and (D) 1 month after the cessation of all therapy, and show the development of a lateralized, focal pattern of activation with the administration of therapy. Maps are displayed according to radiological conventions, such that the right side of the image corresponds to the left hemisphere of the brain.|
|---|

#### GROUP-LEVEL LI MEASURES

Averaged LI values calculated using each set of ROI masks at each threshold during ﬁnger tapping of the unimpaired hand and during ﬁnger tapping of the impaired hand showed overall

|[Figure 5]<br><br>FIGURE 4 | Group level activation maps for ﬁnger tapping of the impaired hand during the BCI therapy phase of the experiment. Panels demonstrate activations assessed (A) pre-therapy, (B) mid-therapy, (C) upon completion of therapy, and (D) 1 month after the cessation of all therapy, and show the development of a bilateral pattern of activation with increased recruitment of contralesional areas with the administration of therapy. Maps are displayed according to radiological conventions, such that the right side of the image corresponds to the left hemisphere of the brain.|
|---|

decreases in LI associated with administration of BCI therapy (Figure 5). This decrease resulted in an average shift from ipsilesionally lateralized activity at baseline to bilateral activity at all subsequent time points in 4 of 6 mask-threshold combinations during tapping of the impaired hand and a shift from average bilateral activity at baseline to contralaterally lateralized activity in all mask-threshold combinations mid-therapy that persisted after therapy in 5 of 6 mask-threshold combinations during tapping of the unimpaired hand. Analysis of these trends using linear mixed effects modeling revealed these LI decreases to be signiﬁcantly different from baseline when using the Motor Network and Motor Cortex masks for LI calculations during unimpaired tapping and when using the Whole Brain mask to calculate LI during impaired tapping, as demonstrated by the black stars and plus symbols in Figure 5. These trends in LI changes with BCI therapy persisted even when only subjects in the chronic (at least 6 months from stroke onset) stage of stroke were analyzed (blue symbols in Figure 5). A similar analysis of LI values from the control phase of the experiment showed no similar trends and no signiﬁcant changes from baseline at any time point for any of the six mask-threshold combinations.

#### FUNCTIONAL ASSESSMENT SCORES

Behavioral results for each subject at each time point are provided in the Tables S1, S2. Floor effects were observed during both the control (Subject 6 ARAT and 9-HPT, Subject 10 SIS Hand Function and 9-HPT, Subjects 8 and 11 9-HPT) and BCI therapy phases (Subject 1 SIS Hand Function and 9-HPT, Subject 2 all assessments, Subjects 4, 6, and 8 9-HPT) of the experiment. Subjects 1, 2, 4, 6, 8, 10, and 11 were unable to complete the 9HPT task throughout the entire experiment and were therefore considered to be exhibiting a ﬂoor effect for this measure. These subjects were not included in subsequent analyses using data from the 9-HPT task. Ceiling effects were observed only during the BCI therapy phase of the experiment (Subject 3 ARAT). At the group level, the Sign test for paired samples was used to compare scores from each of the three behavioral measures mid-therapy, post-therapy, and 1 month after the end of therapy with baseline scores from the BCI therapy phase of the experiment and to compare scores from each assessment during the control phase with baseline control phase values. Changes in these scores were not signiﬁcantly different from baseline at any time point, even when data from subjects exhibiting ﬂoor and ceiling effects were excluded from the comparison.

#### LI-BEHAVIORAL CORRELATION ANALYSES

A summary of the relationships observed between individual changes in LI and individual changes in behavioral measures during the BCI therapy phase of the experiment is provided in Table 2. Of the LI-behavioral relationships from the BCI therapy phase identiﬁed as signiﬁcant at the p ≤ 0.05 level with the Spearman’s approach, two remained signiﬁcant when re-analyzed with GEE (p < 0.001 for both). Among LI-behavioral relationships examined from data obtained during the control phase of the experiment, only the relationship between changes in LI using the Whole Brain mask set at threshold t = 4 and changes in ARAT scores was found to be signiﬁcant using Spearman’s rank correlation analysis (p = 0.039), although this relationship did not survive when re-analyzed using GEE (p = 0.647).

The correlations found to be signiﬁcant using Spearman’s rank correlation analysis that remained signiﬁcant upon secondary analysis using generalized estimating equations are shown in Figure 6.

It is also notable that the calculated estimates for Spearman’s rho (Table 2) are consistent in sign among correlation analyses performed for the same functional measure (i.e., changes in ARAT and SIS Hand Function scores were all estimated to be negatively correlated with changes in LI, while changes in 9-HPT times were all estimated to be positively correlated with changes in LI). Furthermore, while the direction of the correlations is switched for the 9-HPT measure relative to the other two measures, it is important to interpret this difference while keeping in mind the scoring methods for each. In particular, ARAT and SIS Hand Function are scored positively, with improvements in performance reﬂected in higher scores, while the 9-HPT scores are reported as the time needed to complete the task in seconds, with improvements in (i.e., faster) performance reﬂected in lower times. Thus, all estimated Spearman correlations using data from the BCI therapy phase of the experiment were actually consistent

|[Figure 6]<br><br>FIGURE 5 | Average LI values over time during unimpaired and impaired tapping from 8 subjects who received BCI therapy. Values were calculated<br><br>using (A,D) Whole Brain mask set, (B,E) Motor Network mask set, and (C,F) Motor Cortex mask set. Error bars shown are ±1 standard error of the mean.<br><br>+0.05 ≤ p < 0.1, ∗p < 0.05, ∗∗p < 0.01. Symbols in black show signiﬁcant changefrombaselineforall8subjectswhoreceivedBCItherapy.Symbolsinblue indicate time points for signiﬁcant change from baseline among the 6 subjects in the chronic stage of stroke who received BCI therapy. LI, Laterality Index.|
|---|

- Table 2 | Correlation analyses between LI changes and functional changes during the BCI therapy phase of the study.

Functional Mask set Threshold (t) Spearman’s p-value measure rho

ARAT Whole brain 2.003 −0.5751 *0.025 ARAT Whole brain 4.000 −0.3773 0.166 ARAT Motor network 2.003 −0.315 0.253 ARAT Motor network 4.000 −0.3556 0.193 ARAT Motor cortex 2.003 −0.4945 +0.061 ARAT Motor cortex 4.000 −0.6031 *0.017 SISHF Whole brain 2.003 −0.3203 0.226 SISHF Whole brain 4.000 −0.5634 #*0.023 SISHF Motor network 2.003 −0.2734 0.305 SISHF Motor network 4.000 −0.3967 0.143 SISHF Motor cortex 2.003 −0.2493 0.352 SISHF Motor cortex 4.000 −0.3333 0.225 9-HPT Whole brain 2.003 0.4444 0.171 9-HPT Whole brain 4.000 0.3241 0.331 9-HPT Motor network 2.003 0.2315 0.493 9-HPT Motor network 4.000 0.205 0.57 9-HPT Motor cortex 2.003 0.6296 #*0.038 9-HPT Motor cortex 4.000 0.1429 0.694

*Signiﬁcant at p < 0.05; +trend toward signiﬁcance at 0.05 < p < 0.1; #also signiﬁcant with generalized estimating equations approach.

with an association between decreases in LI and gains in behavioral measures. In contrast, this consistency was not noted in correlation analyses examining potential relationships between changes in LI values and changes in functional measures assessed during the control phase of the experiment.

### DISCUSSION

The ﬁndings in this preliminary report on the neuroplastic effects of BCI therapy when applied to stroke rehabilitation show changes in task-related brain activation induced by interventional rehabilitative therapy using a closed-loop neurofeedback BCI device. Speciﬁcally, group-level changes in the patterns of brain activation associated with ﬁnger tapping of each hand were observed with the administration of BCI therapy, with tapping of the impaired hand producing a more bilateral activity pattern post-therapy and with tapping of the unimpaired hand eliciting more lateralized activity involving the hemisphere contralateral to the unimpaired hand (Figures 3–4).

These patterns of change noted in our activation maps were further quantiﬁed using LI analyses, which demonstrated shifts in activity with BCI therapy from the ipsilesional hemisphere to greater involvement of the contralesional hemisphere (i.e., to bilateral activity) during tapping of the impaired hand and increased lateralization of activity to the hemisphere contralateral to the unaffected hand (i.e., the contralesional hemisphere) during tapping of the unimpaired hand. These LI changes were observed using multiple sets of brain masks at multiple thresholds and generally persisted even when the two subacute stroke subjects in the sample were removed from the analysis (Figure 5). The persistence of these ﬁndings among chronic stroke subjects

|[Figure 7]<br><br>FIGURE 6 | Signiﬁcant correlations between changes in LI and changes in behavioral measures. (A) Relationship between individual changes in LI and individual changes in SIS Hand Function. Data from 4 subjects representing 15 data points assessed. (B) Relationship between individual changes in LI and individual changes in 9-HPT. Data from 3 subjects representing 11 data points assessed. Red lines represent data ellipses at the 95% conﬁdence level. LI, Laterality Index; SIS, Stroke Impact Scale; 9-HPT, Nine-Hole Peg Test.|
|---|

argues against this effect arising from a spontaneous recovery process, as chronic stroke is considered to be a time when little or no spontaneous recovery is expected (Nakayama et al., 1994). Furthermore, no such trends or changes in LI were observed in a similar series of scans obtained during a control period in which no BCI therapy was given. That the subanalysis of chronic stroke patients showed LI changes with BCI therapy further supports the hypothesis that these changes were effected, at least in part, by the BCI therapy in that the absence of such effects in the control data set cannot be attributed to the fact that two fewer subjects were assessed during the control phase compared to the full group who received BCI therapy (n = 8) as the two groups (chronic stroke patients who received BCI therapy and subjects who completed the control phase of the experiment) were of equal size (n = 6). Therefore, if the lack of results in the control group were due merely to a power issue, no such results should be present in the subanalysis using only the six chronic stroke subjects who received BCI therapy. These preliminary differences suggest that such changes in LI may be induced by administration of the BCI therapy used in this study. The persistence of these LI changes up to 1 month after the conclusion of BCI therapy further suggests the possibility for lasting effects to be achieved with the use of this rehabilitative approach.

Taken together, the changes observed in brain activation patterns and LI values during tapping of the impaired and

unimpaired hands associated with the administration of BCI therapy suggest that there may exist differential patterns of response to the same treatment with interventional BCI therapy between the impaired and unimpaired sides of the motor system. These differential responses may be characterized both in the direction of LI change (increasingly lateralized in the case of unimpaired movement vs. increasingly bilateral in the case of impaired movement) as well as in the time course or dose-response of each, with more time or therapy needed before a signiﬁcant reorganization effect can be observed in LI during an impaired task relative to that needed to observe a signiﬁcant reduction in LI during an unimpaired task. This difference in brain organization after stroke and re-organization in response to BCI therapy between the ipsilesional and contralesional hemispheres highlights the importance of examining neural responses to treatments such as BCI therapy in stroke survivors even after these systems have been validated in other populations, as it calls into question the degree to which patterns of brain reorganization demonstrated in early studies using healthy normal subjects or limited to stroke subjects with intact cortical functioning (Caria et al., 2011; Ramos-Murguialday et al., 2013) can be generalized to stroke patients and other populations with signiﬁcant cortical pathologies.

Changes in LI observed during and after the administration of BCI therapy also correlated to changes in behavior observed during the same time period when using some of the maskthreshold combinations. Of the four correlations found to be signiﬁcant using Spearman’s rank-correlation analysis on this data from the BCI therapy phase of the experiment, two remained signiﬁcant when reanalyzed using a generalized estimating equations approach. The relationship suggested by both signiﬁcant and non-signiﬁcant estimated Spearman’s coefﬁcients was also consistent across all mask-threshold combinations, with more bilateral LI values correlating to greater functional gains during tapping of the impaired hand across all three behavioral assessments. In contrast, similar correlation analyses performed on data from the control phase of the experiment found only one signiﬁcant correlation using Spearman’s rank-correlation analysis which did not survive when reanalyzed using generalized estimating equations, and the same consistency among the direction of LI change association with improvements in behavioral measures was not observed. The ﬁnding of only some mask-threshold combinations and not others giving rise to signiﬁcant relationships with the behavioral assessments may be due to limitations of the small sample size used, rendering the current preliminary analysis underpowered to detect more subtle relationships between LI changes and functional gains. It is also possible that some mask/threshold combinations are better suited to capturing brain-behavior relationships depending on the behavioral assessment used.

While overall changes in behavioral outcomes during the period of BCI therapy administration were not found to be statistically signiﬁcant at the group level, the correlations revealed by analyses of individual LI and functional changes suggest the presence of or potential for some degree of sub-clinical functional improvement not well-captured by the assessments used. Indeed, the presence of such correlations between gains in 9-HPT

performance and LI changes with BCI therapy further demonstrates the importance of capturing small subclinical gains in function. As only the three least impaired subjects in the group studied who received BCI therapy were able to complete this assessment, changes in 9-HPT performance and LI may show neurological changes that correlate with functional improvement during and after BCI therapy administration and allow us to begin characterizing this relationship present even in highly functioning stroke survivors. It may also be worth noting that while the ARAT and 9-HPT are objective measures of motor function, scores for SIS Hand Function constitute a more subjective measure reliant on self-report. Thus, these changes in brain activity being detected by fMRI may be effecting change both in a subjective measure of how well the subjects believe they are performing, as well as in objective measures of the amount of ability that they are able to demonstrate using standardized motor function tests.

When considering previous work examining correlations between changes in LI and behavioral measures after BCI therapy, one study by Ramos-Murguialday and colleagues found that BCI therapy induced changes in LI of activity in the motor and premotor cortices during attempted movement of the paretic hand, shifting LI toward the ipsilesional hemisphere and correlating the magnitude of these individual shifts with post-therapy motor performance. A similar ﬁnding was documented in a case study of a thalamic stroke survivor, in which treatment with BCI therapy was associated with both functional gains and a shift from bilateral brain activation to lateralized activation in the ipsilesional hemisphere (Caria et al., 2011). While the pattern of functional brain reorganization with BCI therapy for stroke rehabilitation documented in these studies appears to describe an LI-behavior correlation opposite that in our ﬁndings, it is important to note that these ﬁndings by Ramos-Murguialday and Caria were speciﬁc to subjects who had suffered subcortical strokes. Thus, these associations may not be generalizable to patients who have suffered cortical damage, as was true of the majority of subjects in the present study. In fact, the pattern of increasingly lateralized LI induced by BCI therapy observed by the Ramos-Murguialday study is similar in pattern and direction to that observed in the unlesioned hemisphere of our subjects during tapping of the unimpaired hand. Our study builds on ﬁndings from a feasibility study which indicated that the activity in the brain hemisphere ipsilateral to the affected hand (i.e., the contralesional hemisphere) can be used as control signals for a BCI system designed to respond to movement intention (Bundy et al., 2012) along with the knowledge that in some patients infarction and hypoperfusion may shift areas of activation toward the intact hemisphere in other domains such as language (Prabhakaran et al., 2007). Together, these ﬁndings suggest that increased laterality toward the contralateral hemisphere during attempted hand movement may be a typical pattern of response to this type of BCI training in unlesioned cortex.

In designing interventional BCI systems for rehabilitation therapy, such as that used in the present study and in studies referenced previously, there remains a fair amount of uncertainty regarding what patterns of brain reorganization after stroke are optimal in allowing for rehabilitation after stroke and what differences there may be in such patterns among various

subpopulations of stroke survivors. Two of the most prevalent competing theories take different stances regarding whether recruitment or activation of motor areas in the contralesional hemisphere during the chronic stage of stroke is beneﬁcial or detrimental to functional recovery. Each of these views has inﬂuenced the development of therapeutic approaches intended to facilitate better rehabilitative outcomes for patients in the subacute and chronic stages of stroke who have reached a functional plateau with traditional standard therapies alone.

Some of these new approaches promote the activation of ipsior peri-lesional cortex with or without additionally discouraging activation of contralesional motor areas, effectively encouraging the re-lateralization of functional motor activity to the lesioned hemisphere. These methods stem from observations in studies of spontaneous recovery suggesting that the best recovery outcomes are accompanied by an eventual return to pre-stroke lateralization for these functions. This pattern has been documented in both motor (Turton et al., 1996; Traversa et al., 1997, 1998; Marshall et al., 2000; Calautti et al., 2001; Johansen-Berg et al., 2002b; Richards et al., 2008; Dimyan and Cohen, 2011) and language (Saur et al., 2006; Saur and Hartwigsen, 2012) domains in chronic stroke patients. Additional evidence to support this approach comes from studies of functionally associated neuroplastic change to targeted rehabilitation interventions, which have been shown to correlate with neural plastic changes in the lesioned hemisphere. A systematic review and meta-analysis by Richards and colleagues in 2008 of movement-dependent approaches in stroke recovery including CIMT, task practice, virtual reality training, and bilateral movements also supported this model of ipsilesional lateralization coinciding with better recovery in the sub-acute and chronic phases of stroke (Richards et al., 2008).

In contrast, other approaches have been developed that aim to promote the development of new or secondary pathways in the functional organization of the brain, recruiting areas of the contralesional brain to assist in the motor control of the impaired hand. This theory is based on the fact that 8–10% of corticospinal tract ﬁbers project ipsilaterally in humans and other primates (Galea and Darian-Smith, 1994; Hoyer and Celnik, 2011) with the hypothesis that in some stroke patients, the lesioned hemisphere ceases to inhibit these ipsilateral motor projections which can then be used for control of the impaired arm (Stoeckel and Binkofski, 2010). There is some empirical evidence strengthening the case for attempting to maximize ipsilateral control of a paretic limb, with stroke survivors showing reductions in recovered motor performance after TMS of the contralesional hemisphere (Lotze et al., 2006) and one small study of showing contralesional activation increased with CIMT (Kopp et al., 1999). Motor performance has also been found to correlate more strongly with interhemispheric than ipsilesional functional connectivity following stroke (Carter et al., 2010a). Such studies support the idea that stroke recovery relies at least in part on the functional coordination and activation of the contralesional brain. It has been shown that motor performance in the chronic stage of stroke can be related in particular to the degree of corticospinal tract damage sustained by stroke patients (Stinear et al., 2007), suggesting that this tract plays an integral part in motor recovery. For those who are severely impaired due to a greater burden of irreversible

corticospinal tract damage, the recruitment of additional cortical areas may be necessary (Newton et al., 2006; Jayaram and Stinear, 2008), including alternate contralesional pathways, for maximal recovery of motor control. Even with the inclusion of mildly impaired stroke patients, the results of the current study appear to support the participation of the unlesioned hemisphere in the neural reorganization after stroke, which may facilitate recovery of function.

It has been shown that cortical activity in both humans and non-human primates reliably encodes a representation of ipsilateral arm movement (Ganguly et al., 2009) and that differential cortical patterns can be reliably detected within a single hemisphere to differentiate movements of the ipsilateral and contralateral hands (Wisneski et al., 2008). Building on this work, new BCI devices have been developed that can be controlled using only ipsilateral neural signals (Bundy et al., 2012). These devices are being studied primarily in severely impaired subjects most likely to beneﬁt from therapies using this type of approach, as individuals in this stroke population are those most likely to experience a motor recovery process that relies more heavily on new or accessory pathways after signiﬁcant damage to the ipsilesional corticospinal tract (Bundy et al., 2012). It is important to note that the targeting of these new BCI devices promoting ipsilateral control of the impaired arm to severely impaired stroke survivors, while theoretically motivated, does not necessarily mean that others with less severe impairments could not also beneﬁt from such therapies. Currently, there remains insufﬁcient evidence to determine deﬁnitively which of these newer therapies are best suited to stroke survivors with different levels of impairment.

It is also important to remember that the conclusions regarding optimal patterns of functional brain reorganization from the study of one therapy modality may not be generalizable to other therapy modalities such as BCI. For example, two studies following similar populations of chronic stroke patients (all but one with subcortical lesions) found motor function gains to be associated with increased ipsilesional activation laterality or with increased contralesional recruitment during motor tasks of the affected hand after using BCI and gesture therapy respectively (Orihuela-Espina et al., 2013; Ramos-Murguialday et al., 2013). With this in mind, it may not be necessary to identify an optimal pattern of change common across therapy modalities as long as respective approaches are able to induce neuroplastic change and maximize functional recovery in chronic stroke patients. Understanding these patterns of neuroplastic change might then serve simply to allow for optimization within the application of a particular modality.

Although our study had a small and somewhat heterogenous sample of stroke survivors both in terms of motor impairment (mild to severe) and chronicity of stroke (subacute to chronic), BCI induced consistent brain changes along with signiﬁcant brain-behavioral associative changes in these patients over time that were not observed during a control period in which no BCI therapy was administered. Changes in neural activation patterns were observed with BCI therapy in both primary and secondary motor areas in this population of stroke patients, and these activation patterns were then quantiﬁed in LI calculations using masks that included regions of both primary and secondary motor areas.

It is promising that these ﬁndings persisted across multiple mask sets at multiple thresholds, some of which were found to have signiﬁcant correlations to changes in behavioral measures when using both correlation and GEE models. Although the ﬁndings in this study are based on a small group of subjects, a subanalysis of only the chronic stroke patients who received BCI therapy showed consistent effects, supporting the hypothesis that administration of this BCI therapy helped to produce the effects observed. The lack of changes in the control group also argues against attributing the effects observed to spontaneous recovery, as the control group was similar to the group that received BCI therapy in numerous measures such as age, sex, handedness, and chronicity of stroke (Table 1).

Even though these preliminary analyses were potentially underpowered for the detection of smaller changes in LI earlier in the therapy time course and for the more consistent detection of signiﬁcant relationships between LI change and behavioral gains, future studies incorporating a larger sample of stroke patients will be able to better characterize these patterns of LI change with BCI therapy and to detect more subtle relationships that these LI changes may have with concurrent behavioral gains. Larger sample sizes will also allow for the investigation of potential cross over effects into domains not directly targeted by the BCI device, such

- as strength, participation, and activities of daily living, as such effects are expected to be more subtle than those observed in the targeted domain of upper extremity motor function. The use of additional assessments such as the Fugl–Meyer and Chedoke Arm and Hand Inventory may also allow for the detection of more subtle changes in functional capability that may accompany this type of therapy such that ﬂoor effects and ceiling effects might be a smaller limitation of future studies. Similarly, future studies on the effects of BCI therapy for stroke rehabilitation will be needed not only to characterize more subtle patterns of neuroplastic change that may result from this type of treatment but also to determine the optimal mask and threshold parameters that might allow LI to be used as an imaging biomarker to assess and track recovery in individuals receiving this type of therapy.

The ﬁndings of this study may provide further insight into what theoretical approaches might be optimal in designing future neurofeedback devices and paradigms for motor recovery after stroke, particularly with regard to which patterns of brain activity might be actively rewarded or discouraged by future systems in order to elicit the greatest possible recovery in these patients. In determining whether increased ipsilesional lateralization vs. increased bilateral recruitment is optimal for motor recovery, a review by Dimyan and Cohen documented the former pattern as associated with spontaneous recovery while a small number of interventional and disruptive studies supported the latter in the development of novel interventions to promote neural reorganization in poststroke rehabilitation (Dimyan and Cohen, 2011). This is consistent with the possibility that there exist multiple patterns of neural reorganization that facilitate better recovery after stroke and that such patterns may be modulated with the administration of interventional therapy using newer technologies that are different from those evidenced during spontaneous recovery.

In exploring optimal device design, it may be more important with developing BCI therapies than with the development

of other therapy modalities to determine what pattern of neural activity corresponds to the greatest behavioral gains because the BCI system can be programmed to preferentially reward predeﬁned neural signatures. If such patterns for maximal rehabilitation are discovered, it is not difﬁcult to envision the development and clinical use of customized BCI therapy interventions based on the functional and neurological proﬁle of an individual patient, a form of what have been previously termed as “prescriptive” interventions (Carter et al., 2010b).

As the ﬁeld of interventional rehabilitative therapy using BCI continues to develop, there remains a need for larger studies incorporating an element of randomized control to better understand and characterize the effects being elicited by the BCI therapy itself and also to identify subpopulations of stroke survivors with differential responses to this type of therapy. Ideally, such studies will also incorporate a wide range of behavioral assessments, neuroimaging measures, and connectivity analyses to capture and provide a comprehensive understanding of the various brain and behavior changes induced by BCI therapy and the relations between them.

### AUTHOR CONTRIBUTIONS

Brittany M. Young assisted in subject recruitment, data collection, data analysis, and writing. Zack Nigogosyan assisted with data collection, data analysis, and writing. Léo M. Walton assisted with data collection and writing. Jie Song assisted with subject recruitment and data collection. Veena A. Nair assisted with subject recruitment, data collection, data analysis, and writing. Scott W. Grogan assisted with data collection. Mitchell E. Tyler provided TDU hardware and expertise. Dorothy F. Edwards assisted with study design and outcome measure selection and interpretation. Kristin Caldera assisted with subject referral and recruitment. Justin A. Sattin assisted with study design and subject recruitment. Justin C. Williams is one of two lead PI’s on this project and supervised the technical and engineering aspects of the work. Vivek Prabhakaran is one of two lead PI’s on this project and supervised the neuroimaging aspects of this work.

### ACKNOWLEDGMENTS

We would like to thank all of our subjects and their families for making their participation in the study possible. We would also like to thank our study coordinators Jenny Swartz, Amanda Kolterman, and Tally Mitchell and our MR technologists Sara John and Jenelle Fuller. We would like to thank Hui-Chun (Ruby) Chen and colleagues in Occupational Therapy for their assistance with behavioral testing and FES electrode placement. This work was supported by NIH grants RC1MH090912-01, T32GM008692, UL1TR000427, and T32EB011434. Additional funding was also provided through a Coulter Translational Research Award, an American Heart Association Postdoctoral Fellow Research Award, UW Milwaukee-Madison Intercampus Grants, the UW Graduate School, and by Shapiro Foundation Grants. Portions of this work were previously presented in poster or e-poster form at the SFN Annual Meeting 2012, the International Stroke Conference 2013, the ISMRM Annual Meeting 2013, and as a platform talk at the RSNA Annual Meeting 2013.

### SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online

- at: http://www.frontiersin.org/journal/10.3389/fneng.2014. 00026/abstract

- Table S1 | Functional outcomes as assessed by SIS Hand Function, Action Research Arm Test, and Nine-Hole Peg Test during the BCI Therapy phase of the experiment. Subjects who were unsuccessful at completing the 9-HPT within 5min were noted as unable to perform this assessment. Subject numbers in this table match those in Table 1, which provides participant characteristics. SIS, Stroke Impact Scale; ARAT, Action Research Arm Test; 9-HPT, Nine-Hole Peg Test.
- Table S2 | Functional outcomes as assessed by SIS Hand Function, Action Research Arm Test, and Nine-Hole Peg Test among Subjects completing assessments during the control phase of the experiment. Subjects who were unsuccessful at completing the 9-HPT within 5min were noted as unable to perform this assessment. Subject numbers in this table match those in Table 1, which provides participant characteristics. SIS, Stroke Impact Scale; ARAT, Action Research Arm Test; 9-HPT, Nine-Hole Peg Test.
- Table S3 | Components of masks used for LI calculations. Mask regions with “motor and premotor cortex” included components of the precentral, postcentral, middle frontal, medial frontal, and superior frontal gyri. LI, Laterality Index.

### REFERENCES

Beebe, J. A., and Lang, C. E. (2009). Relationships and responsiveness of six upper extremity function tests during the ﬁrst six months of recovery after stroke. J. Neurol. Phys. Ther. 33, 96–103. doi: 10.1097/NPT.0b013e3181a33638

Bhasin, A., Padma Srivastava, M. V., Kumaran, S. S., Bhatia, R., and Mohanty, S. (2012). Neural interface of mirror therapy in chronic stroke patients: a functional magnetic resonance imaging study. Neurol. India 60, 570–576. doi: 10.4103/0028-3886.105188

Broetz, D., Braun, C., Weber, C., Soekadar, S. R., Caria, A., and Birbaumer, N. (2010). Combination of brain-computer interface training and goal-directed physical therapy in chronic stroke: a case report. Neurorehabil. Neural Repair 24, 674–679. doi: 10.1177/1545968310368683

Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., et al. (2008). Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. doi: 10.1161/STROKEAHA.107.505313

Bundy, D. T., Wronkiewicz, M., Sharma, M., Moran, D. W., Corbetta, M., and Leuthardt, E. C. (2012). Using ipsilateral motor signals in the unaffected cerebral hemisphere as a signal platform for brain-computer interfaces in hemiplegic stroke survivors. J. Neural Eng. 9, 036011. doi: 10.1088/1741-2560/9/3/036011

Calautti, C., Leroy, F., Guincestre, J. Y., Marie, R. M., and Baron, J. C. (2001). Sequential activation brain mapping after subcortical stroke: changes in hemispheric balance and recovery. Neuroreport 12, 3883–3886. doi: 10.1097/00001756-200112210-00005

Carey, J. R., Kimberley, T. J., Lewis, S. M., Auerbach, E. J., Dorsey, L., Rundquist, P., et al. (2002). Analysis of fMRI and ﬁnger tracking training in subjects with chronic stroke. Brain 125, 773–788. doi: 10.1093/brain/awf091

Caria, A., Weber, C., Brotz, D., Ramos, A., Ticini, L. F., Gharabaghi, A., et al. (2011). Chronic stroke recovery after combined BCI training and physiotherapy: a case report. Psychophysiology 48, 578–582. doi: 10.1111/j.1469-8986.2010.01117.x Carod-Artal, F. J., Coral, L. F., Trizotto, D. S., and Moreira, C. M. (2008). The stroke impact scale 3.0: evaluation of acceptability, reliability, and validity of the Brazilian version. Stroke 39, 2477–2484. doi: 10.1161/STROKEAHA.107. 513671

Carroll, D. (1965). A quantitative test of upper extremity function. J. Chronic Dis. 18, 479–491. doi: 10.1016/0021-9681(65)90030-5

Carter, A. R., Astaﬁev, S. V., Lang, C. E., Connor, L. T., Rengachary, J., Strube, M. J., et al. (2010a). Resting interhemispheric functional magnetic resonance imaging connectivity predicts performance after stroke. Ann. Neurol. 67, 365–375. doi: 10.1002/ana.21905

Carter, A. R., Connor, L. T., and Dromerick, A. W. (2010b). Rehabilitation after stroke: current state of the science. Curr. Neurol. Neurosci. Rep. 10, 158–166. doi: 10.1007/s11910-010-0091-9

Confalonieri, L., Pagnoni, G., Barsalou, L. W., Rajendra, J., Eickhoff, S. B., and Butler, A. J. (2012). Brain activation in primary motor and somatosensory cortices during motor imagery correlates with motor imagery ability in stroke patients. ISRN Neurol. 2012, 613595. doi: 10.5402/2012/613595

Cox, R. W. (1996). AFNI: software for analysis and visualization of functional magnetic resonance neuroimages. Comput. Biomed. Res. 29, 162–173. doi: 10.1006/cbmr.1996.0014

Cramer, S. C. (2010). Brain repair after stroke. N. Engl. J. Med. 362, 1827–1829. doi: 10.1056/NEJMe1003399

Daly, J. J., Cheng, R., Rogers, J., Litinas, K., Hrovat, K., and Dohring, M. (2009). Feasibility of a new application of noninvasive Brain Computer Interface (BCI): a case study of training for recovery of volitional motor control after stroke. J. Neurol. Phys. Ther. 33, 203–211. doi: 10.1097/NPT.0b013e3181c1fc0b

Darling, W. G., Seitz, R. J., Peltier, S., Tellmann, L., and Butler, A. J. (2007). Visual cortex activation in kinesthetic guidance of reaching. Exp. Brain Res. 179, 607–619. doi: 10.1007/s00221-006-0815-x

Dimyan, M. A., and Cohen, L. G. (2011). Neuroplasticity in the context of motor rehabilitation after stroke. Nat. Rev. Neurol. 7, 76–85. doi: 10.1038/nrneurol.2010.200

Dromerick, A. W., Lang, C. E., Birkenmeier, R. L., Wagner, J. M., Miller, J. P., Videen, T. O., et al. (2009). Very Early Constraint-Induced Movement during Stroke Rehabilitation (VECTORS): a single-center RCT. Neurology 73, 195–201. doi: 10.1212/WNL.0b013e3181ab2b27

Duncan, P. W., Wallace, D., Lai, S. M., Johnson, D., Embretson, S., and Laster, L. J. (1999). The stroke impact scale version 2.0. Evaluation of reliability, validity, and sensitivity to change. Stroke 30, 2131–2140. doi: 10.1161/01.STR.30. 10.2131

Felton, E. A., Williams, J. C., Vanderheiden, G. C., and Radwin, R. G. (2012). Mental workload during brain-computer interface training. Ergonomics 55, 526–537. doi: 10.1080/00140139.2012.662526

Galea, M. P., and Darian-Smith, I. (1994). Multiple corticospinal neuron populations in the macaque monkey are speciﬁed by their unique cortical origins, spinal terminations, and connections. Cereb. Cortex 4, 166–194. doi: 10.1093/cercor/4.2.166

Ganguly, K., Secundo, L., Ranade, G., Orsborn, A., Chang, E. F., Dimitrov, D. F., et al. (2009). Cortical representation of ipsilateral arm movements in monkey and man. J. Neurosci. 29, 12948–12956. doi: 10.1523/JNEUROSCI.247109.2009

Gauthier, L. V., Taub, E., Perkins, C., Ortmann, M., Mark, V. W., and Uswatte, G. (2008). Remodeling the brain: plastic structural brain changes produced by different. Stroke 39, 1520–1525. doi: 10.1161/STROKEAHA.107.502229

Go, A. S., Mozaffarian, D., Roger, V. L., Benjamin, E. J., Berry, J. D., Borden, W. B., et al. (2013). Heart disease and stroke statistics–2013 update: a report from the American Heart Association. Circulation 127, e6–e245. doi: 10.1161/CIR.0b013e318282ab8f

Hoyer, E. H., and Celnik, P. A. (2011). Understanding and enhancing motor recovery after stroke using transcranial magnetic stimulation. Restor. Neurol. Neurosci. 29, 395–409. doi: 10.3233/RNN-2011-0611

Jayaram, G., and Stinear, J. W. (2008). Contralesional paired associative stimulation increases paretic lower limb motor excitability post-stroke. Exp. Brain Res. 185, 563–570. doi: 10.1007/s00221-007-1183-x

Johansen-Berg, H., Dawes, H., Guy, C., Smith, S. M., Wade, D. T., and Matthews, P. M. (2002a). Correlation between motor improvements and altered fMRI activity after. Brain 125, 2731–2742. doi: 10.1093/brain/awf282

Johansen-Berg, H., Rushworth, M. F., Bogdanovic, M. D., Kischka, U., Wimalaratna, S., and Matthews, P. M. (2002b). The role of ipsilateral premotor cortex in hand movement after stroke. Proc. Natl. Acad. Sci. U.S.A. 99, 14518–14523. doi: 10.1073/pnas.222536799

Kelly-Hayes, M., Beiser, A., Kase, C. S., Scaramucci, A., D’agostino, R. B., and Wolf, P. A. (2003). The inﬂuence of gender and age on disability following ischemic stroke: the Framingham study. J. Stroke Cerebrovasc. Dis. 12, 119–126. doi: 10.1016/S1052-3057(03)00042-9

Kononen, M., Tarkka, I. M., Niskanen, E., Pihlajamaki, M., Mervaala, E., Pitkanen, K., et al. (2012). Functional MRI and motor behavioral changes obtained with constraint-induced movement therapy in chronic stroke. Eur. J. Neurol. 19, 578–586. doi: 10.1111/j.1468-1331.2011.03572.x

Kopp, B., Kunkel, A., Muhlnickel, W., Villringer, K., Taub, E., and Flor, H. (1999). Plasticity in the motor system related to therapy-induced improvement of movement after stroke. Neuroreport 10, 807–810. doi: 10.1097/00001756199903170-00026

Kundu, B., Penwarden, A., Wood, J. M., Gallagher, T. A., Andreoli, M. J., Voss, J., et al. (2013). Association of functional magnetic resonance imaging indices with postoperative language outcomes in patients with primary brain tumors. Neurosurg. Focus 34, E6. doi: 10.3171/2013.2.FOCUS12413

Lang, C. E., Wagner, J. M., Dromerick, A. W., and Edwards, D. F. (2006). Measurement of upper-extremity function early after stroke: properties of the action research arm test. Arch. Phys. Med. Rehabil. 87, 1605–1610. doi: 10.1016/j.apmr.2006.09.003

Lang, K. C., Thompson, P. A., and Wolf, S. L. (2013). The EXCITE Trial: reacquiring upper-extremity task performance with early versus late delivery of constraint therapy. Neurorehabil. Neural Repair 27, 654–663. doi: 10.1177/1545968313481281

Liu, M., Fujiwara, T., Shindo, K., Kasashima, Y., Otaka, Y., Tsuji, T., et al. (2012). Newer challenges to restore hemiparetic upper extremity after stroke: HANDS therapy and BMI neurorehabilitation. Hong Kong Physiother. J. 30, 83–92. doi: 10.1016/j.hkpj.2012.05.001

Lo, A. C., Guarino, P. D., Richards, L. G., Haselkorn, J. K., Wittenberg, G. F., Federman, D. G., et al. (2010). Robot-assisted therapy for long-term upper-limb impairment after stroke. N. Engl. J. Med. 362, 1772–1783. doi: 10.1056/NEJMoa0911341

Lotze, M., Beutling, W., Loibl, M., Domin, M., Platz, T., Schminke, U., et al. (2012). Contralesional motor cortex activation depends on ipsilesional corticospinal tract integrity in well-recovered subcortical stroke patients. Neurorehabil. Neural Repair 26, 594–603. doi: 10.1177/1545968311427706

Lotze, M., Markert, J., Sauseng, P., Hoppe, J., Plewnia, C., and Gerloff, C. (2006). The role of multiple contralesional motor areas for complex hand movements after internal capsular lesion. J. Neurosci. 26, 6096–6102. doi: 10.1523/JNEUROSCI.4564-05.2006

Marshall, R. S., Perera, G. M., Lazar, R. M., Krakauer, J. W., Constantine, R. C., and Delapaz, R. L. (2000). Evolution of cortical activation during recovery from corticospinal tract infarction. Stroke 31, 656–661. doi: 10.1161/01.STR. 31.3.656

Miller, E. L., Murray, L., Richards, L., Zorowitz, R. D., Bakas, T., Clark, P., et al. (2010). Comprehensive overview of nursing and interdisciplinary rehabilitation care of the stroke patient: a scientiﬁc statement from the American Heart Association. Stroke 41, 2402–2448. doi: 10.1161/STR.0b013e3181e7512b

Moss, A., and Nicholas, M. (2006). Language rehabilitation in chronic aphasia and time postonset: a review of single-subject data. Stroke 37, 3043–3051. doi: 10.1161/01.STR.0000249427.74970.15

Nakayama, H., Jorgensen, H. S., Raaschou, H. O., and Olsen, T. S. (1994). Recovery of upper extremity function in stroke patients: the copenhagen stroke study. Arch. Phys. Med. Rehabil. 75, 394–398. doi: 10.1016/0003-9993(94)90161-9

Newton, J. M., Ward, N. S., Parker, G. J., Deichmann, R., Alexander, D. C., Friston, K. J., et al. (2006). Non-invasive mapping of corticofugal ﬁbres from multiple motor areas–relevance to stroke recovery. Brain 129, 1844–1858. doi: 10.1093/brain/awl106

Orihuela-Espina, F., Fernandez Del Castillo, I., Palafox, L., Pasaye, E., SanchezVillavicencio, I., Leder, R., et al. (2013). Neural reorganization accompanying upper limb motor rehabilitation from stroke with virtual reality-based gesture therapy. Top. Stroke Rehabil. 20, 197–209. doi: 10.1310/tsr2003-197

Pillai, J. J., and Zaca, D. (2011). Relative utility for hemispheric lateralization of different clinical fMRI activation tasks within a comprehensive language paradigm battery in brain tumor patients as assessed by both threshold-dependent and threshold-independent analysis methods. Neuroimage 54(Suppl. 1), S136–S145. doi: 10.1016/j.neuroimage.2010.03.082

Pinter, D., Pegritz, S., Pargfrieder, C., Reiter, G., Wurm, W., Gattringer, T., et al. (2013). Exploratory study on the effects of a robotic hand rehabilitation device on changes in grip strength and brain activity after stroke. Top. Stroke Rehabil. 20, 308–316. doi: 10.1310/tsr2004-308

Prabhakaran, V., Raman, S. P., Grunwald, M. R., Mahadevia, A., Hussain, N., Lu, H., et al. (2007). Neural substrates of word generation during stroke recovery: the inﬂuence of cortical hypoperfusion. Behav. Neurol. 18, 45–52. doi: 10.1155/2007/430402

Prasad, G., Herman, P., Coyle, D., Mcdonough, S., and Crosbie, J. (2010). Applying a brain-computer interface to support motor imagery practice in people with

stroke for upper limb recovery: a feasibility study. J. Neuroeng. Rehabil. 7, 60. doi: 10.1186/1743-0003-7-60

Ramos-Murguialday, A., Broetz, D., Rea, M., Laer, L., Yilmaz, O., Brasil, F. L., et al.

(2013). Brain-machine interface in chronic stroke rehabilitation: a controlled study. Ann. Neurol. 74, 100–108. doi: 10.1002/ana.23879

Richards, L. G., Stewart, K. C., Woodbury, M. L., Senesac, C., and Cauraugh, J. H. (2008). Movement-dependent stroke recovery: a systematic review and meta-analysis of TMS. Neuropsychologia 46, 3–11. doi: 10.1016/j.neuropsychologia.2007.08.013

Saur, D., and Hartwigsen, G. (2012). Neurobiology of language recovery after stroke: lessons from neuroimaging studies. Arch. Phys. Med. Rehabil. 93, S15–25. doi: 10.1016/j.apmr.2011.03.036

Saur, D., Lange, R., Baumgaertner, A., Schraknepper, V., Willmes, K., Rijntjes, M., et al. (2006). Dynamics of language reorganization after stroke. Brain 129, 1371–1384. doi: 10.1093/brain/awl090

Shindo, K., Kawashima, K., Ushiba, J., Ota, N., Ito, M., Ota, T., et al. (2011). Effects of neurofeedback training with an electroencephalogram-based braincomputer interface for hand paralysis in patients with chronic stroke: a preliminary case series study. J. Rehabil. Med. 43, 951–957. doi: 10.2340/1650 1977-0859

Shirer, W. R., Ryali, S., Rykhlevskaia, E., Menon, V., and Greicius, M. D. (2012). Decoding subject-driven cognitive states with whole-brain connectivity patterns. Cereb. Cortex 22, 158–165. doi: 10.1093/cercor/bhr099

Springer, J. A., Binder, J. R., Hammeke, T. A., Swanson, S. J., Frost, J. A., Bellgowan, P. S., et al. (1999). Language dominance in neurologically normal and epilepsy subjects: a functional MRI study. Brain 122(Pt 11), 2033–2046. doi: 10.1093/brain/122.11.2033

Stagg, C. J., Bachtiar, V., O’shea, J., Allman, C., Bosnell, R. A., Kischka, U., et al. (2012). Cortical activation changes underlying stimulationinduced behavioural gains in chronic stroke. Brain 135, 276–284. doi: 10.1093/brain/awr313

Stinear, C. M., Barber, P. A., Smale, P. R., Coxon, J. P., Fleming, M. K., and Byblow, W. D. (2007). Functional potential in chronic stroke patients depends on corticospinal tract integrity. Brain 130, 170–180. doi: 10.1093/brain/awl333

Stoeckel, M. C., and Binkofski, F. (2010). The role of ipsilateral primary motor cortex in movement control and recovery from brain damage. Exp. Neurol. 221, 13–17. doi: 10.1016/j.expneurol.2009.10.021

Takahashi, M., Takeda, K., Otaka, Y., Osu, R., Hanakawa, T., Gouko, M., et al. (2012). Event related desynchronization-modulated functional electrical stimulation system for stroke rehabilitation: a feasibility study. J. Neuroeng. Rehabil. 9, 56. doi: 10.1186/1743-0003-9-56

Talairach, J., and Tournoux, P. (1988). Co-planar Stereotaxic Atlas of the Human Brain: 3-Dimensional Proportional System. New York, NY: Thieme Medical Pub.

Traversa, R., Cicinelli, P., Bassi, A., Rossini, P. M., and Bernardi, G. (1997). Mapping of motor cortical reorganization after stroke. A brain stimulation study with focal magnetic pulses. Stroke 28, 110–117. doi: 10.1161/01.STR.28.1.110

Traversa, R., Cicinelli, P., Pasqualetti, P., Filippi, M., and Rossini, P. M. (1998). Follow-up of interhemispheric differences of motor evoked potentials from the ‘affected’ and ‘unaffected’ hemispheres in human stroke. Brain Res. 803, 1–8. doi: 10.1016/S0006-8993(98)00505-8

Turton, A., Wroe, S., Trepte, N., Fraser, C., and Lemon, R. N. (1996). Contralateral and ipsilateral EMG responses to transcranial magnetic stimulation during recovery of arm and hand function after stroke. Electroencephalogr. Clin. Neurophysiol. 101, 316–328. doi: 10.1016/0924-980X(96)95560-5

Varkuti, B., Guan, C., Pan, Y., Phua, K. S., Ang, K. K., Kuah, C. W., et al. (2013). Resting state changes in functional connectivity correlate with movement recovery for BCI and robot-assisted upper-extremity training after stroke. Neurorehabil. Neural Repair 27, 53–62. doi: 10.1177/154596831 2445910

Volpe, B. T., Huerta, P. T., Zipse, J. L., Rykman, A., Edwards, D., Dipietro, L., et al.

(2009). Robotic devices as therapeutic and diagnostic tools for stroke recovery. Arch. Neurol. 66, 1086–1090. doi: 10.1001/archneurol.2009.182

Ward, N. S., Brown, M. M., Thompson, A. J., and Frackowiak, R. S. (2003). Neural correlates of motor recovery after stroke: a longitudinal fMRI study. Brain 126, 2476–2496. doi: 10.1093/brain/awg245

Wisneski, K. J., Anderson, N., Schalk, G., Smyth, M., Moran, D., and Leuthardt, E. C. (2008). Unique cortical physiology associated with ipsilateral hand movements and neuroprosthetic implications. Stroke 39, 3351–3359. doi: 10.1161/STROKEAHA.108.518175

Wolf, S. L., Thompson, P. A., Winstein, C. J., Miller, J. P., Blanton, S. R., NicholsLarsen, D. S., et al. (2010). The EXCITE stroke trial: comparing early and delayed constraint-induced movement therapy. Stroke 41, 2309–2315. doi: 10.1161/STROKEAHA.110.588723

Wolf, S. L., Winstein, C. J., Miller, J. P., Thompson, P. A., Taub, E., Uswatte, G., et al. (2008). Retention of upper limb function in stroke survivors who have received constraint-induced movement therapy: the EXCITE randomised trial. Lancet Neurol. 7, 33–40. doi: 10.1016/S1474-4422(07)70294-6

Yamada, N., Kakuda, W., Senoo, A., Kondo, T., Mitani, S., Shimizu, M., et al. (2013). Functional cortical reorganization after low-frequency repetitive transcranial magnetic stimulation plus intensive occupational therapy for upper limb hemiparesis: evaluation by functional magnetic resonance imaging in poststroke patients. Int. J. Stroke 8, 422–429. doi: 10.1111/ijs.12056

Conﬂict of Interest Statement: A pending patent on the closed-loop neurofeedback device used for the therapy administered in this study (Pending U.S. Patent Application No. 12/715,090) was ﬁled jointly by the two lead investigators Justin C. Williams and Vivek Prabhakaran. Otherwise, the authors declare that the research

was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 15 April 2014; accepted: 23 June 2014; published online: 15 July 2014. Citation: Young BM, Nigogosyan Z, Walton LM, Song J, Nair VA, Grogan SW, Tyler ME, Edwards DF, Caldera K, Sattin JA, Williams JC and Prabhakaran V (2014) Changes in functional brain organization and behavioral correlations after rehabilitative therapy using a brain-computer interface. Front. Neuroeng. 7:26. doi: 10.3389/ fneng.2014.00026 This article was submitted to the journal Frontiers in Neuroengineering. Copyright © 2014 Young, Nigogosyan, Walton, Song, Nair, Grogan, Tyler, Edwards, Caldera, Sattin, Williams and Prabhakaran. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

