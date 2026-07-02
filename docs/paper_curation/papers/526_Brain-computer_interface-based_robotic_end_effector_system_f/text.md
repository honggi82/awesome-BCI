##### ORIGINAL RESEARCH ARTICLE

published: 29 July 2014 doi: 10.3389/fneng.2014.00030

## NEUROENGINEERING

# Brain-computer interface-based robotic end effector system for wrist and hand rehabilitation: results of a three-armed randomized controlled trial for chronic stroke

### Kai Keng Ang1*, Cuntai Guan1, Kok Soon Phua1, Chuanchu Wang1, Longjiang Zhou1, Ka Yin Tang1, Gopal J. Ephraim Joseph2, Christopher Wee Keong Kuah2 and Karen Sui Geok Chua2

- 1 Institute for Infocomm Research, Agency for Science, Technology and Research (A*STAR), Singapore
- 2 Department of Rehabilitation Medicine, Tan Tock Seng Hospital, Singapore

Edited by: Christoph Guger, Guger Technologies OEG, Austria

Reviewed by: Robert Leeb, Ecole Polytechnique Fédérale de Lausanne, Switzerland Surjo R. Soekadar, University Hospital of Tübingen, Germany

*Correspondence: Kai Keng Ang, Institute for Infocomm Research, Agency for Science, Technology and Research (A*STAR), 1 Fusionopolis Way, #21-01, Connexis (South Tower), Singapore 138632, Singapore e-mail: kkang@i2r.a-star.edu.sg

The objective of this study was to investigate the efﬁcacy of an Electroencephalography (EEG)-based Motor Imagery (MI) Brain-Computer Interface (BCI) coupled with a Haptic Knob (HK) robot for arm rehabilitation in stroke patients. In this three-arm, single-blind, randomized controlled trial; 21 chronic hemiplegic stroke patients (Fugl-Meyer Motor Assessment (FMMA) score 10–50), recruited after pre-screening for MI BCI ability, were randomly allocated to BCI-HK, HK or Standard Arm Therapy (SAT) groups. All groups received 18 sessions of intervention over 6 weeks, 3 sessions per week, 90min per session. The BCI-HK group received 1h of BCI coupled with HK intervention, and the HK group received 1h of HK intervention per session. Both BCI-HK and HK groups received 120 trials of robot-assisted hand grasping and knob manipulation followed by 30min of therapist-assisted arm mobilization. The SAT group received 1.5h of therapist-assisted arm mobilization and forearm pronation-supination movements incorporating wrist control and grasp-release functions. In all, 14 males, 7 females, mean age 54.2 years, mean stroke duration 385.1 days, with baseline FMMA score 27.0 were recruited. The primary outcome measure was upper extremity FMMA scores measured mid-intervention at week 3, end-intervention at week 6, and follow-up at weeks 12 and 24. Seven, 8 and 7 subjects underwent BCI-HK, HK and SAT interventions respectively. FMMA score improved in all groups, but no intergroup differences were found at any time points. Signiﬁcantly larger motor gains were observed in the BCI-HK group compared to the SAT group at weeks 3, 12, and 24, but motor gains in the HK group did not differ from the SAT group at any time point. In conclusion, BCI-HK is effective, safe, and may have the potential for enhancing motor recovery in chronic stroke when combined with therapist-assisted arm mobilization.

Keywords: electroencephalography, motor imagery, brain-computer interface, stroke rehabilitation, robotic

### INTRODUCTION

Stroke is the third leading cause of severe disabilities worldwide (Hankey, 2013). Despite multimodality rehabilitation efforts, 40% of stroke survivors live with various disabilities. Of these, the lack of functional arm, wrist, or hand recovery contributed to signiﬁcant losses in independence vocation and quality of life. Task speciﬁc technique such as constrained-induced movement therapy (CIMT) is highly effective in reducing learned non-use and improving arm and hand function with enduring gains in chronic stroke. However, only ∼20 to 25% of stroke patients meet minimum criteria for CIMT (Fritz et al., 2005). Since physical practice (PP) of the stroke-impaired extremity is often difﬁcult or not possible using CIMT; motor imagery (MI), the mental practice of movements without physical execution, represents an alternate rehabilitation approach (Sharma et al., 2009). Although MI in chronic stroke is promising, integrating MI in rehabilitation had yielded inconclusive clinical outcome (Braun et al., 2006; Ietswaart et al., 2011; Malouin et al., 2013).

One of the key issues for integrating MI in rehabilitation is that while PP is observable, MI is a concealed mental process. Nevertheless, brain-computer interfaces (BCIs) (Wolpaw et al., 2002) that acquire, analyze and translate brain signals into control commands of output devices (Shih et al., 2012) can be used to detect event-related desynchronization or synchronization (ERD/ERS) (Pfurtscheller and Lopes Da Silva, 1999) when MI is performed. In this way, stroke patients who suffer from severe limb weakness but who are still able to imagine movements of the paretic hand can receive BCI contingent feedback upon detection of MI-related brain signals (Birbaumer et al., 2008; Buch et al., 2008; Ramos-Murguialday et al., 2013). By re-establishing contingency between cortical activity related to MI and feedback, BCI might strengthen the sensorimotor loop and foster neuroplasticity that facilitates motor recovery (Dobkin, 2007; Dimyan and Cohen, 2011). A recent clinical study had shown that Electroencephalography (EEG)-based MI-BCI can be used to detect cortical activity related to MI in a majority of

stroke patients (Ang et al., 2011). Hence the use of EEG-based MI-BCI presents a prospective approach for detecting MI for stroke rehabilitation.

There were many studies that reported the use of BCI for stroke rehabilitation (Ang and Guan, 2013). Recent trials that reported clinical efﬁcacy included: Mihara et al. (2013) reported a randomized control trial (RCT) performed on 10 stroke patients who received near-infrared spectroscopy (NIRS)-based MI-BCI with visual feedback vs. 10 stroke patients who received NIRSbased MI-BCI with irrelevant feedback. The results showed that the patients who received MI-BCI visual feedback attained significantly greater motor improvements measured using Fugl-Meyer motor assessment (FMMA) (Fugl-Meyer et al., 1975) compared to the sham group. The FMMA is a well-designed, feasible, and efﬁcient clinical examination method that has been widely used in the stroke population for measuring sensorimotor stroke recovery (Gladstone et al., 2002). The motor score ranges from 0 for hemiplegia to a maximum of 100 points for normal motor performance, divided into 66 points for the upper extremity and 34 points for the lower extremity. Ramos-Murguialday et al. (2013) reported a RCT on 16 chronic stroke patients who received MIBCI with hand and arm orthoses feedback vs. 14 chronic stroke patients who received random orthoses feedback not linked to BCI. Both groups received physiotherapy, and the results showed that the patients who received BCI orthoses feedback attained signiﬁcantly greater motor improvement in FMMA score. Recently, Ang et al. (2014) reported a RCT on 11 chronic stroke patients who received MI-BCI with MIT MANUS shoulder-elbow robotic feedback vs. 15 chronic stroke patients who received intense movement exercises using the MIT MANUS robot. The results showed the patients who received MI-BCI intervention attained an average of FMMA gains of 4.5, and the patients who received intense robot-assisted movement therapy attained an average of FMMA gains of 6.3. However, no signiﬁcant differences between the two groups were found.

In a systematic review, Nilsen et al. (2010) attested that MI added to PP was an effective intervention for stroke. However, existing RCTs have demonstrated motor improvements in chronic stroke patients who received MI-BCI intervention, but there is still scanty clinical efﬁcacy to indicate the beneﬁts of performing MI compared to PP or standard arm therapy (SAT) in stroke rehabilitation (Ietswaart et al., 2011). Hence we sought to investigate the clinical beneﬁts of concomitant MI, PP interventions for stroke rehabilitation by integrating MI and PP using an EEG-based MI-BCI coupled with a haptic knob (HK) robot (Lambercy et al., 2007, 2011). We then investigated the hypothesis that this integration could facilitate the beneﬁcial effects of therapist-assisted arm mobilization for stroke patients compared to robot-assisted PP and SAT in current rehabilitation program.

### MATERIALS AND METHODS

#### ETHICS STATEMENT

Ethics Committee approval was obtained from the Institution’s Domain Speciﬁc Review Board, National Healthcare Group, Singapore. The trial was registered in ClinicalTrials.gov (NCT01287975). Informed consent was obtained prior to study enrollment.

#### STUDY DESIGN

The randomized controlled trial was conducted over ∼2.5 year period from 1 January 2011 to 31 June 2013 at an outpatient rehabilitation facility, involving subjects who had completed inpatient rehabilitation at the Tan Tock Seng Hospital, Singapore. Figure 1 shows a ﬂow chart of the trial (refer Supplementary Material for CONSORT checklist).

Inclusion criteria included ﬁrst-ever clinical stroke conﬁrmed on neuroimaging, ages 21–80 years of age, duration >4 months post stroke, moderate to severe impairment of upper extremity function assessed by FMMA (Fugl-Meyer et al., 1975) score 10–50; motor power assessed by Medical Research Council (MRC) (Compston, 2010) grades >2/5 in shoulder abductors, and >2/5 in the elbow ﬂexors, and 1–3 in wrist dorsiﬂexors and ﬁnger ﬂexors and ability to understand simple instructions.

Subjects were excluded if they had medical instability such as unresolved sepsis; postural hypotension; end stage renal failure terminal illness; severe aphasia, inattention; hemi spatial neglect; severe visual impairment; epilepsy; severe depression; psychiatric disorder; recurrent stroke; skull defects compromising EEG cap ﬁt; severe spasticity assessed [modiﬁed Ashworth scale (MAS) (Bohannon and Smith, 1987) >2 in any shoulder, elbow or wrist/ﬁnger muscles]; pain assessed by visual analog scale (VAS) (Price et al., 1999) >4/10; ﬁxed joint contractures; skin conditions such as infections or eczema which could be worsened by robotic exoskeletal or EEG cap contact.

#### EEG DATA ACQUISITION

In this study, EEG data from 27 channels were collected using the Nuamps EEG acquisition hardware1 with unipolar Ag/AgCl electrodes channels, digitally sampled at 250Hz with a resolution of 22 bits for voltage ranges of ±130mV. EEG recordings from all channels were bandpass ﬁltered from 0.05 to 40Hz by the acquisition hardware.

#### HAPTIC KNOB ROBOT

The haptic knob (HK) robot is a two-degree-of-freedom robotic hand interface for hand grasping and knob manipulation PP (Lambercy et al., 2007, 2011). The hand interface was designed using two parallelogram structures that supported an exchangeable handle in order to adapt to various hand sizes, ﬁnger orientations, and subjects with right or left stroke-impaired hand. The HK robot-assisted hand grasping PP involved ﬁnger ﬂexion and extension exercises performed using the linear degree-of-freedom (DOF) of the HK, while the rotational DOF was held in a static position. The HK robot-assisted knob manipulation PP involved wrist pronation or supination, and hand coordination exercises performed using the rotational DOF of the HK, while the linear DOF was held in a static position.

During training with the HK, subjects were seated comfortably in a padded, height adjustable chair with 2-point chest strapping without arm rests to reduce compensatory trunk movements. For

1Neuroscan Nuamps EEG Ampliﬁer. Compumedics USA, Compumedics Neuroscan and Compumedics DWL, 6605 West W.T. Harris Blvd, Suite F, Charlotte, NC 28269, USA.

each subject, the stroke-impaired forearm was placed on a padded support and the subject was instructed to grasp the end effector of the HK. The height of the chair was adjusted until a comfortable level, the subject’s shoulder abducted at about 40◦ and the elbow ﬂexed at about 90◦. The digits of the subject stroke-impaired hand were then strapped to the HK’s end effector with Velcro bands to prevent them from slipping.

Instructions and feedbacks were provided on a computer screen for the progress of the HK robot-assisted PP in a form of a picture manipulation task using a solid frame to represent the current position, and a dotted frame to represent the target position. For the HK robot-assisted hand grasping PP, an outward-pointing

arrow was shown to instruct the subject to perform hand opening (Figure 2A). Once the target outer limit was reached, an inwardpointing arrow was shown to instruct the subject to perform hand closing (Figure 2B). This open-and-close action formed a single trial. Subsequently, a different picture was used for the next trial. For the HK robot-assisted knob manipulation PP, a right-curved arrow was shown to instruct the subject to perform a clockwise wrist rotation (Figure 2C). Once the target limit is reached, a left-curved arrow was shown to instruct the subject to perform counter-clockwise wrist rotation (Figure 2D). This wrist pronation-and- supination action formed a single trial. Similarly, a different picture was used for the next trial. For both the hand

|[Figure 1]<br><br>FIGURE 1 | CONSORT Diagram: a ﬂow from recruitment through follow-up and analysis.|
|---|

|[Figure 2]<br><br>FIGURE 2 | Cues used in BCI-HK and HK interventions. (A) Hand opening; (B) hand closing; (C) wrist pronation; and (D) wrist supination.|
|---|

grasping and knob manipulation PP, HK robot-assisted movement was initiated if no movement from the subject was detected after an interval of 2s.

#### EEG-BASED MI-BCI SCREENING

A study on 99 healthy subjects had shown that ∼7% of the subjects achieved below 60% classiﬁcation accuracies (Guger et al., 2003). Subsequently, a study on 54 stroke patients had shown that ∼13% of the patients achieved classiﬁcation accuracies below chance level (Ang et al., 2011). Hence there is a small minority of subjects who cannot operate EEG-based MI-BCI. Thus, in this study, eligible subjects were ﬁrst screened for their ability to operate EEG-based MI-BCI.

The screening session comprised 4 runs of EEG data collection. The ﬁrst 2 runs collected EEG from subjects who performed kinesthetic MI (Stinear et al., 2006) of the stroke-impaired hand while strapped to the HK, and idle condition. The subjects were seated comfortably and instructed to imagine moving their stroke-impaired hand in an open-and-close action, and voluntary movements were restrained by static resistance from the HK robot. Subjects were also instructed to minimize voluntary head and body movements. Electromyography (EMG) were recorded from the stroke-impaired hand to check for attempted movements while performing motor imagery (Figure 3). In the subsequent 2 runs, the subjects were instructed to relax while passive movement (PM) of the stroke-impaired hand was performed using the HK robot for the hand grasping action. The entire screening session consisted of 4 runs of 80 trials each for a total of 320 trials, and an inter-run break of at least 2min was provided. Each run comprised 40 trials of MI or PM, and 40 trials of idle condition. Figure 4A shows the timing for a single-trial from the screening section. Each trial lasted ∼12s and each run lasted ∼8min. The screening session lasted ∼1h inclusive of EEG setup time. The EEG from the ﬁrst 2 runs were used to compute the 10×10-fold cross-validation accuracy of classifying MI of the

|[Figure 3]<br><br>FIGURE 3 | Setup of BCI-HK and HK intervention for stroke rehabilitation at a local hospital. The setup comprised Electroencephalography (EEG) cap, Electromyography (EMG) electrodes, EEG ampliﬁer, and Haptic Knob (HK) robot.|
|---|

stroke-impaired hand vs. the idle condition using the ﬁlter bank common spatial pattern (FBCSP) algorithm (Ang et al., 2012).

#### RANDOMIZATION AND BLINDING

Subjects who passed BCI screening were randomly assigned to receive either one of 3 interventions:

- (1) BCI-HK which concomitantly comprised EEG-based MI-BCI coupled with HK robot-assisted PP therapy (60min) followed by therapist-assisted arm mobilization (30min).
- (2) HK which comprised HK robot-assisted PP therapy (60min) followed by therapist-assisted arm mobilization (30min).
- (3) SAT which comprised distal arm training of forearm pronation-supination movements incorporating wrist control and grasp-release of various objects (60min) and overall therapist-assisted arm mobilization (30min) conducted by a trained occupational therapist.

The randomization block size was 3 and the allocation sequence was 1:1:1 generated using STATA software version 10.2 (Stata Corp, College Station, TX, USA). Enrollment and assignment of participants was provided by KSGC. As subject blinding was not feasible, all outcome assessments for this study were performed by occupational therapist DXD who was blinded to allocation. There were no protocol deviations.

All groups received 18 sessions of supervised interventions for a total of 27h over 6 weeks, 3 times per week, 90min per session, by occupational therapist GJEJ and engineer KSP. This included 15min for set up and breaks for short rests. Adverse events via questionnaire were monitored after each intervention session. Discontinuation criteria included new neurological or serious adverse events; increase in arm pain or spasticity of greater than 30% from baseline; or severe fatigue resulted from the interventions.

BCI-HK intervention

The BCI-HK intervention consisted of a calibration session and 18 therapy sessions of MI-BCI coupled with HK robot-assisted PP therapy. Figure 3 shows the setup for the BCI-HK intervention.

The calibration session comprised 4 runs of EEG data collection that was similar to the screening session whereby subjects performed MI in the ﬁrst 2 runs and PM in the subsequent 2 runs. The EEG from the ﬁrst 2 runs were used to compute a subjectspeciﬁc calibration model using the FBCSP algorithm (Ang et al., 2012) to classify MI vs. the idle condition in the subsequent therapy sessions. The EEG data collected from performing PM were not analyzed in this study.

Each therapy session comprised 4 runs of 30 concomitant MI and PP trials each, for a total of 120 trials. An inter-run break of 3–5min was provided after each run. Allowable pain-free ranges of motion for the hand grasping and knob manipulation PP were ﬁrst individually pre-determined by GJEJ. This HK calibration involved calibrating six positions: closing, opening, and static position for hand grasping; clockwise, counter clockwise and static position for knob manipulation. For the ﬁrst 2 runs, the subjects are instructed to perform kinesthetic MI of the

|[Figure 4]<br><br>FIGURE 4 | Acquisition of EEG for BCI-HK intervention. (A) Timing of performing kinesthetic MI of the stroke-impaired hand and idle condition for the calibration session; (B) timing of performing kinesthetic MI of the stroke-impaired coupled with HK robot-assisted PP for the rehabilitation session.|
|---|

stroke-impaired hand for the hand grasping action. Subjects were also instructed to minimize voluntary head and body movements. EMG from the stroke-impaired hand was checked to ensure that there was no attempted movement during MI. If MI-related brain signals was successfully detected by the FBCSP algorithm (Ang et al., 2012) using the subject-speciﬁc calibration model, then the HK robot-assisted hand grasping PP would be initiated. For the subsequent 2 runs, the subjects are instructed to perform kinesthetic MI of the stroke-impaired hand for the knob manipulation action. If MI was successfully detected, then the HK robot-assisted knob manipulation PP would be initiated. If MI was not detected in 2 consecutive trials, then the HK robot-assisted PP would be automatically initiated. Figure 4B shows the timing for a singletrial from the therapy session. Each trial lasted ∼17 to 23s and each run lasted ∼12min. Each therapy session lasted ∼1.5h inclusive of breaks and setup time.

HK intervention

The HK intervention comprised 18 therapy sessions of HK robotassisted hand grasping, and knob manipulation PP. Figure 3 shows the setup for the HK intervention, which is the same as the BCI-HK intervention. EEG data was also collected for the HK intervention but was not analyzed in this report.

Each therapy session comprised 4 runs of 30 PP trials each for a total of 120 trials. An inter-run break of 3–5min was provided after each run. Similar to the BCI-HK intervention, allowable pain-free ranges of motion were pre-determined, and HK calibration was performed by GJEJ prior to the start of the therapy session. For the ﬁrst 2 runs, the subjects performed HK robotassisted hand grasping PP. For the subsequent 2 runs, the subjects performed HK robot-assisted knob manipulation PP. If no movements from the subject were detected, the HK would initiate fully assisted PP after 2s. Each trial lasted ∼9 to 15s and each run lasted ∼8min. Each therapy session lasted ∼ 1h inclusive of breaks and setup time.

SAT intervention

The SAT intervention comprised 18 therapist-assisted sessions. Each session comprised 60min of repetitive task training

(Langhorne et al., 2011) focusing on forearm pronationsupination movements incorporating wrist control and grasp-release of various objects.

Therapist-assisted arm mobilization

All 3 groups received 30min of therapist-assisted arm mobilization following the principles of the professionally recognized Neuro-developmental Treatment Approach for stroke rehabilitation (Howle, 2002), which included tone management and facilitation toward normal arm movement patterns via various closed-chain functional reach activities.

#### SAMPLE SIZE STATISTICAL ANALYSIS

The sample size was estimated with an assumption of a 4 point gains in total FMMA score for the BCI-HK and HK groups compared to the SAT group, and a standard deviation of 6.3 points based on the gains of the robot-assisted intervention in the previous study (Ang et al., 2014). The expected number in each group was found to be 20 subjects to achieve statistical power of 80%. Sample size calculation was performed in MATLAB.

#### STATISTICAL METHODS

Analysis of variance (ANOVA) was used to examine the demographic and baseline group differences. Analysis of covariance (ANCOVA) was used to examine the group differences at each measurement point between the three groups after adjusting for baseline differences. Two-sided t-tests were performed to analyze for signiﬁcant difference at each measurement point from baseline in each group. One-sided t-tests were then performed to analyze if the BCI-HK and HK interventions were better than the SAT intervention. Data analysis was performed using MATLAB and the level of signiﬁcance was set at 5%.

#### OUTCOMES

The primary outcome was the total FMMA score (range, 0–66) for the stroke-impaired upper extremity. Outcomes were measured at 5 time points during the study: at baseline (week 0), at midintervention (week 3), at completion of intervention (week 6), 6

#### EEG SPATIAL PATTERNS AND FEATURES

weeks follow-up (week 12), and 18 weeks follow-up (week 24). There were no protocol deviations.

The EEG from the calibration sessions of patients in the BCIHK group were used to compute a subject-speciﬁc calibration model using the FBCSP algorithm (Ang et al., 2012). Figure 5A shows the EEG spatial patterns from patient A006 who performed MI of right stroke-impaired hand vs. the idle condition. The patterns for detecting MI-related brain signals of right hand showed a weak contra-lateral negative region on the left hemisphere and a relatively stronger ipsi-lateral positive region on the right hemisphere around the motor cortex area. The patterns from these two regions corresponded to ERD and ERS respectively for performing right hand motor imagery (Blankertz et al., 2008). Figure 5B shows the EEG spatial patterns from patient A031 who performed MI of left hand vs. the idle condition. Similarly, the patterns for detecting MI-related brain signals of left hand showed a weak contra-lateral negative region on the right hemisphere and a relatively stronger ipsi-lateral positive region on the left hemisphere around the motor cortex

### RESULTS

#### PATIENT ENROLLMENT

Thirty-four subjects were found eligible and subsequently screened for their ability to use EEG-based MI BCI. The EEG data collected from the screening session showed 5 subjects achieved accuracies that were lower than chance level (57.5%) and were thus excluded. The chance level performance was computed based on 95% conﬁdence estimate of the accuracy using the inverse of binomial cumulative distribution. Seven subjects declined further participation in the trial. The remaining 22 subjects gave consent and were randomized into 3 intervention groups as follows: BCI-HK (7 subjects), HK (8 subjects) and SAT (7 subjects) respectively. Twenty-one subjects completed the study and follow-up with 1 drop out (4.6%) (Figure 1). The study terminated in June 2013 due to funding cessation, thus not all 60 intended subjects could be recruited.

Table 1 shows the demographic of the 21 subjects who completed the study by intervention. Altogether, there were 14 men and 7 women [mean age 54.2 years (30–79)], mean stroke duration, 385.1 days (191–651). BCI-HK group had more subcortical strokes, shorter time after the stroke, and higher FMMA score at week 0. SAT group had higher proportion of cerebral infarctions compared to hemorrhagic strokes. There were no signiﬁcant baseline differences in all 3 groups in terms of stroke type [F(2, 18) =

|[Figure 5]<br><br>FIGURE 5 | EEG Spatial patterns and frequency bands used to classify motor imagery of stroke-impaired hand vs. idle condition. (A) Spatial patterns of patient A006 with right stroke-impaired hand; (B) spatial pattern of patient A031 with left stroke-impaired hand; (C) frequency bands used for patients A006 and A031. Blue and red colors in the spatial patterns correspond to negative (ERD) and positive (ERS) values respectively.|
|---|

- 0.90, p = 0.42], stroke nature [F(2, 18) = 0.53, p = 0.60], duration since stroke [F(2, 18) = 3.41, p = 0.06], FMMA at week 0 [F(2, 18) = 0.83, p = 0.45], and other demographic.

- Table 1 | Demographics and baseline characteristics of subjects by intervention.

Intervention Variable Total BCI-HK HK SAT

N 21 6 8 7 Age (years) 54.2 ± 12.4 54.0 ± 8.9 51.1 ± 6.3 58.0 ± 19.3 GENDER N(%)

Male 14 (66.7%) 4 (66.7%) 6 (75.0%) 4 (57.1%) Female 7 (33.3%) 2 (33.3%) 2 (25.0%) 3 (42.9%) DOMINANT HAND AFFECTED N(%)

Yes 11 (52.4%) 2 (33.3%) 5 (62.5%) 4 (57.1%) No 10 (47.6%) 4 (66.7%) 3 (37.5%) 3 (42.9%) STROKE TYPE N(%)

Infarction 11 (52.4%) 2 (33.3%) 4 (50.0%) 5 (71.4%) Hemorrhage 10 (47.6%) 4 (66.7%) 4 (50.0%) 2 (28.6%) STROKE NATURE N(%)

Cortical 6 (28.6%) 1 (16.7%) 2 (25.0%) 3 (42.9%) Subcortical 15 (71.4%) 5 (83.3%) 6 (75.0%) 4 (57.1%) Duration since stroke (days)

385.1 ± 131.8 285.7 ± 64.0 398.2 ± 150.9 455.4 ± 109.6

FMMA (Week 0)

27.0 ± 13.8 33.0 ± 16.2 25.5 ± 11.5 23.4 ± 14.5

FMMA, Fugl-Meyer Motor Assessment.

#### ADVERSE EVENTS

area. The patterns from these two regions corresponded to ERD and ERS respectively for performing left hand MI (Blankertz et al., 2008). The weaker stroke-affected contra-lateral regions compared to unaffected ipsi-lateral regions may be due to the relatively lower baseline ERD in stroke patients compared to healthy subjects reported in the study by Kasashima et al. (2012). For both patients, the EEG spatial patterns for the idle condition were not coherent since this condition was not controlled. Figure 5C shows the frequency bands selected by the FBCSP algorithm for both patients.

There were no reported serious adverse events, deaths, or signiﬁcant increases in shoulder or hand pain for any of the 3 intervention groups at any time during the study duration. One subject (4.6%) from the BCI-HK group dropped out in the 5th week of intervention due to a transient mild seizure occurring several hours after the intervention.

### DISCUSSION

This is the ﬁrst RCT that compared 3 arms of MI-BCI, robotassisted PP and SAT. Difﬁculties were encountered in recruiting patients for this study due to the strict inclusion and exclusion criteria. In addition, some patients who were clinically eligible did not pass the BCI screening or voluntarily declined to participate due to the length of the study.

#### EFFICACY MEASUREMENTS

At week 6, upon completion of interventions, all groups demonstrated signiﬁcant FMMA score gains compared to baseline FMMA score at week 0: BCI-HK group [(M = 7.2, SD = 2.3),

- t(5) = 7.58, p = 0.001], HK group [(M = 7.3, SD = 4.7), t(7) = 4.35, p = 0.003], and SAT group [(M = 4.9, SD = 4.1), t(6) = 3.10, p = 0.021]. At weeks 12 and 24, signiﬁcant FMMA score gains compared to baseline FMMA score at week 0 were sustained for BCI-HK group [(M = 8.2, SD = 2.9), t(5) = 6.83, p = 0.001; and (M = 9.7, SD = 2.9), t(5) = 8.04, p = 0.001] and HK group [(M = 6.5, SD = 4.4), t(7) = 4.14, p = 0.004; and (M = 8.3, SD = 5.0), t(7) = 4.66, p = 0.002]; but not for SAT group [(M = 3.6, SD = 5.5), t(6) = 1.71, p = 0.14; and (M = 3.6, SD = 5.9),
- t(6) = 1.60, p = 0.16] (Table 2). No signiﬁcant intergroup differences were observed at any

The results on the discriminative spatial patterns and frequency band used to classify MI of stroke-impaired hand vs. the

|[Figure 6]<br><br>FIGURE 6 | FMMA improvements for BCI-HK, HK and SAT interventions relative to week 0.|
|---|

time point during the study among all the 3 groups after adjusting for baseline FMMA score at week 0: week 3 [F(2, 17) =

- 1.51, p = 0.250], week 6 [F(2, 17) = 0.66, p = 0.531], week 12 [F(2, 17) = 1.12, p = 0.349], and week 24 [F(2, 17) = 2.39, p = 0.122]. Signiﬁcant greater upper extremity FMMA score gains were observed in the BCI-HK group compared to the SAT group at week 3 [t(11) = 2.14, p = 0.028], week 12 [t(11) = 1.82, p =

- 0.048], and week 24 [t(11) = 2.28, p = 0.022]; but not at week 6, [t(11) = 1.21, p = 0.13] (Figure 6). However, no signiﬁcant greater FMMA score gains were observed in the HK group compared to the SAT group at any time point: week 3 [t(13) =
- 1.27, p = 0.114], week 6 [t(13) = 1.04, p = 0.159], week 12 [t(13) = 1.14, p = 0.138], and week 24 [t(13) = 1.66, p = 0.060] (Figure 6).

- Table 2 | Efﬁcacy measures by FMMA scores for each intervention group (N = 6 for BCI-HK, n = 8 for HK, and N = 7 for SAT).

Outcome Group Baseline Improvements relative to week 0

Week 0 Week 3 Week 6 Week 12 Week 24

Proximal (0∼42) BCI-HK 24.2±7.5 3.3±4.2 3.8±2.7 5.0±2.4 5.5±2.1 HK 19.5±7.7 2.3±2.7 4.4±2.7 4.0±3.5 5.8±2.9 SAT 18.1±10.4 1.1±2.2 3.0±2.7 2.6±4.4 3.3±4.0

Distal (0∼24) BCI-HK 8.8±9.2 2.5±2.4 3.3±2.3 3.2±2.7 4.2±3.1 HK 6.0±4.7 1.6±2.5 2.9±3.0 2.5±2.6 2.5±3.0 SAT 5.3±4.7 0.4±1.1 1.9±1.9 1.0±1.3 0.3±2.1

Upper Extremity (0∼66) BCI-HK 33.0±16.2 5.8±4.7 7.2±2.3 8.2±2.9 9.7±2.9 HK 25.5±11.5 3.9±4.3 7.3±4.7 6.5±4.4 8.3±5.0 SAT 23.4±14.5 1.6±2.2 4.9±4.1 3.6±5.5 3.6±5.9

idle condition in the BCI-HK group differed from patient-topatient, demonstrating the necessity to perform subject-speciﬁc calibration. The amount of movement repetitions were standardized between the BCI-HK and HK group. However, the number of arm repetitions were not measured in the SAT group, but the duration of training was similar with respect to the other 2 groups. The results showed signiﬁcant efﬁcacy in reducing both proximal and distal motor impairment, low dropout rate and safety. The results also showed the importance of distal training of the arm for proximal improvement, which is consistent with the study by Lambercy et al. (2011) on 15 chronic patients using the HK robot.

Compared to other chronic stroke patients in robot-assisted PP for proximal and distal (Lo et al., 2010; Lambercy et al., 2011), the FMMA score gains from the BCI-HK and HK groups were higher (∼7 at week 6 vs. ∼3 to 4). Possible reasons included a relatively younger stroke study cohort (mean age 54 years) and larger proportion of cerebral hemorrhages (∼50%) compared to the Caucasian populations who typically have a higher proportion of infarctions.

FMMA score gains at week 6 for all 3 groups were sustained till week 24. Further gains of 2.5 and 1.0 were observed in the BCI-HK and HK groups, and a loss of 1.3 in the SAT group was observed at week 24 relative to week 6. This may be due to the reduction in motor impairment that facilitated further home-based PP.

A signiﬁcant greater FMMA score gains were observed in the BCI-HK compared to the SAT group. This may be due to the performance of MI in the BCI-HK group that facilitated neuroplasticity, which was suggested from the functional Magnetic Resonance Imaging (fMRI) study on resting state changes in functional connectivity on patients who underwent BCI with robot-assisted rehabilitation after stroke by Varkuti et al. (2013). A greater FMMA score gains were also observed in the HK group compared to the SAT group, but the gains were not signiﬁcant. This may be due to the highly repetitive and thus higher intensity of PP in the robot-assisted HK group compared to the therapist-assisted SAT group, but lacked the additional positive effects of MI in the BCI-HK group. Similar beneﬁts of MI were seen in another study that investigated chronic stroke patients who received MI-BCI with hand and arm orthoses feedback vs. those who received random orthoses feedback not linked to BCI (Ramos-Murguialday et al., 2013), suggesting a possible role for BCI in rehabilitation for stroke.

#### STUDY LIMITATIONS

The major limitations of our study were its small sample size and under-powering. This was likely due to the strict criteria required for BCI-related training in terms of cognitive and attention requirements. Due to the small sample size, our results need to be interpreted with caution. Due to a younger and larger proporation of hemorrhagic strokes, which may be expected from a predominantly Chinese population (85.7%), results from our study may lack the ability for generalization as to how the general stroke population will respond to BCI-related rehabilitation. As the number of repetitions was not monitored for the SAT group, there was a lack of standardization on the number of PP trials

for this group. In addition, the motor improvements measured by FMMA are limited by a ceiling effect and focused more on proximal arm (Gladstone et al., 2002), thus such gains may not directly translate to changes in activities of daily living.

### CONCLUSIONS

There was signiﬁcant higher motor gain up to 6 months for subjects in the BCI-HK intervention compared with SAT. This adds support to the potential of BCI-HK coupled with rehabilitation therapy as an adjunctive rehabilitation tool for wrist and hand rehabilitation after chronic stroke. Overall side effects were minimal and interventions were well-tolerated. Additional research and larger studies are needed to study neuroplasticityrelated changes from the use of BCI in stroke rehabilitation, and to enhance the portability and usability of BCI interfaces.

### ACKNOWLEDGMENTS

We thank the study participants and their caregivers for their participation in this trial. We acknowledge Mr. Donald Xu Dong, Senior Occupational Therapist, who performed the independent clinical outcome assessments. We also acknowledge the ﬁnancial support from the Science and Engineering Research Council of the Agency for Science, Technology and Research, Singapore (Grant number: 092 148 0066)

### SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: http://www.frontiersin.org/journal/10.3389/fneng.2014. 00030/abstract

### REFERENCES

Ang, K. K., Chin, Z. Y., Wang, C., Guan, C., and Zhang, H. (2012). Filter bank common spatial pattern algorithm on BCI competition IV datasets 2a and 2b. Front. Neurosci. 6:39. doi: 10.3389/fnins.2012.00039

Ang, K. K., Chua, K. S. G., Phua, K. S., Wang, C., Chin, Z. Y., Kuah, C. W. K., et al. (2014). A randomized controlled trial of EEG-based motor imagery braincomputer interface robotic rehabilitation for stroke. Clin. EEG Neurosci. doi: 10.1177/1550059414522229. [Epub ahead of print].

Ang, K. K., and Guan, C. (2013). Brain-computer interface in stroke rehabilitation. J. Comput. Sci. Eng. 7, 139–146. doi: 10.5626/JCSE.2013.7.2.139

Ang, K. K., Guan, C., Chua, K. S. G., Ang, B. T., Kuah, C. W. K., Wang, C., et al. (2011). A large clinical study on the ability of stroke patients to use EEG-based motor imagery brain-computer interface. Clin. EEG Neurosci. 42, 253–258. doi: 10.1177/155005941104200411

Birbaumer, N., Murguialday, A. R., and Cohen, L. (2008). Braincomputer interface in paralysis. Curr. Opin. Neurol. 21, 634–638. doi: 10.1097/WCO.0b013e328315ee2d

Blankertz, B., Tomioka, R., Lemm, S., Kawanabe, M., and Muller, K.-R. (2008). Optimizing spatial ﬁlters for robust EEG single-trial analysis. IEEE Signal Process Mag. 25, 41–56. doi: 10.1109/MSP.2008.4408441

Bohannon, R. W., and Smith, M. B. (1987). Interrater reliability of a modiﬁed ashworth scale of muscle spasticity. Phys. Ther. 67, 206–207.

Braun, S. M., Beurskens, A. J., Borm, P. J., Schack, T., and Wade, D. T. (2006). The effects of mental practice in stroke rehabilitation: a systematic review. Arch. Phys. Med. Rehabil. 87, 842–852. doi: 10.1016/j.apmr.2006. 02.034

Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., et al. (2008). Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. doi: 10.1161/STROKEAHA.107. 505313

Compston, A. (2010). Aids to the Investigation of Peripheral Nerve Injuries. Medical Research Council: Nerve Injuries Research Committee. His Majesty’s Stationery Ofﬁce: 1942; pp. 48 (iii) and 74 ﬁgures and 7 diagrams; with Aids to

the Examination of the Peripheral Nervous System. By Michael O’Brien for the Guarantors of Brain. Saunders Elsevier: 2010; pp. [8] 64 and 94 Figures. Brain 133, 2838–2844. doi: 10.1093/brain/awq270

Dimyan, M. A., and Cohen, L. G. (2011). Neuroplasticity in the context of motor rehabilitation after stroke. Nat. Rev. Neurol. 7, 76–85. doi: 10.1038/nrneurol. 2010.200

Dobkin, B. H. (2007). Brain-computer interface technology as a tool to augment plasticity and outcomes for neurological rehabilitation. J. Physiol. 579, 637–642. doi: 10.1113/jphysiol.2006.123067

Fritz, S. L., Light, K. E., Patterson, T. S., Behrman, A. L., and Davis, S. B. (2005). Active ﬁnger extension predicts outcomes after constraint-induced movement therapy for individuals with hemiparesis after stroke. Stroke 36, 1172–1177. doi: 10.1161/01.STR.0000165922.96430.d0

Fugl-Meyer, A. R., Jääskö, L., Leyman, I., Olsson, S., and Steglind, S. (1975). The post-stroke hemiplegic patient. 1. a method for evaluation of physical performance. Scand. J. Rehabil. Med. 7, 13–31.

Gladstone, D. J., Danells, C. J., and Black, S. E. (2002). The fugl-meyer assessment of motor recovery after stroke: a critical review of its measurement properties. Neurorehabil. Neural Repair 16, 232–240. doi: 10.1177/154596802401105171 Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain-computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147. doi: 10.1109/TNSRE.2003.814481

Hankey, G. J. (2013). The global and regional burden of stroke. Lancet Glob. Health 1, e239–e240. doi: 10.1016/S2214-109X(13)70095-0 Howle, J. M. (2002). Neuro-developmental Treatment Approach: Theoretical Foundations & Principles. Laguna Beach, CA: NDTA.

Ietswaart, M., Johnston, M., Dijkerman, H. C., Joice, S., Scott, C. L., Macwalter, R. S., et al. (2011). Mental practice with motor imagery in stroke recovery: randomized controlled trial of efﬁcacy. Brain 134, 1373–1386. doi: 10.1093/brain/awr077

Kasashima, Y., Fujiwara, T., Matsushika, Y., Tsuji, T., Hase, K., Ushiyama, J., et al. (2012). Modulation of event-related desynchronization during motor imagery with transcranial direct current stimulation (tDCS) in patients with chronic hemiparetic stroke. Exp. Brain Res. 221, 263–268. doi: 10.1007/s00221-0123166-9

Lambercy, O., Dovat, L., Gassert, R., Burdet, E., Chee Leong, T., and Milner, T.

(2007). A haptic knob for rehabilitation of hand function. IEEE Trans. Neural Syst. Rehabil. Eng. 15, 356–366. doi: 10.1109/TNSRE.2007.903913

Lambercy, O., Dovat, L., Yun, H., Wee, S. K., Kuah, C., Chua, K., et al. (2011). Effects of a robot-assisted training of grasp and pronation/supination in chronic stroke: a pilot study. J. Neuroeng. Rehabil. 8:63. doi: 10.1186/1743-0003-8-63 Langhorne, P., Bernhardt, J., and Kwakkel, G. (2011). Stroke rehabilitation. Lancet

377, 1693–1702. doi: 10.1016/S0140-6736(11)60325-5

Lo, A. C., Guarino, P. D., Richards, L. G., Haselkorn, J. K., Wittenberg, G. F., Federman, D. G., et al. (2010). Robot-assisted therapy for long-term upper-limb impairment after stroke. N. Engl. J. Med. 362, 1772–1783. doi: 10.1056/NEJMoa0911341

Malouin, F., Jackson, P. L., and Richards, C. L. (2013). Towards the integration of mental practice in rehabilitation programs. A critical review. Front. Hum. Neurosci. 7:576 doi: 10.3389/fnhum.2013.00576

Mihara, M., Hattori, N., Hatakenaka, M., Yagura, H., Kawano, T., Hino, T., et al. (2013). Near-infrared spectroscopy-mediated neurofeedback enhances efﬁcacy of motor imagery-based training in poststroke victims: a pilot study. Stroke 44, 1091–1098. doi: 10.1161/STROKEAHA.111.674507

Nilsen, D. M., Gillen, G., and Gordon, A. M. (2010). Use of mental practice to improve upper-limb recovery after stroke: a systematic review. Am. J. Occup. Ther. 64, 695–708. doi: 10.5014/ajot.2010.09034

Pfurtscheller, G., and Lopes Da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857. doi: 10.1016/S1388-2457(99)00141-8

Price, C. I. M., Curless, R. H., and Rodgers, H. (1999). Can stroke patients use visual analogue scales? Stroke 30, 1357–1361. doi: 10.1161/01.STR.30.7.1357 Ramos-Murguialday, A., Broetz, D., Rea, M., Läer, L., Yilmaz, Ö., Brasil, F. L., et al.

(2013). Brain-machine interface in chronic stroke rehabilitation: a controlled study. Ann. Neurol. 74, 100–108. doi: 10.1002/ana.23879

Sharma, N., Simmons, L. H., Jones, P. S., Day, D. J., Carpenter, T. A., Pomeroy, V. M., et al. (2009). Motor imagery after subcortical stroke: a functional magnetic resonance imaging study. Stroke 40, 1315–1324. doi: 10.1161/STROKEAHA.108.525766

Shih, J. J., Krusienski, D. J., and Wolpaw, J. R. (2012). Brain-computer interfaces in medicine. Mayo Clin. Proc. 87, 268–279. doi: 10.1016/j.mayocp.2011.12.008 Stinear, C., Byblow, W., Steyvers, M., Levin, O., and Swinnen, S. (2006). Kinesthetic, but not visual, motor imagery modulates corticomotor excitability. Exp. Brain Res. 168, 157–164. doi: 10.1007/s00221-005-0078-y

Varkuti, B., Guan, C., Pan, Y., Phua, K. S., Ang, K. K., Kuah, C. W. K., et al. (2013). Resting state changes in functional connectivity correlate with movement recovery for BCI and robot-assisted upper-extremity training after stroke. Neurorehabil. Neural Repair 27, 53–62. doi: 10.1177/1545968312 445910

Wolpaw, J. R., Birbaumer, N., Mcfarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 15 April 2014; accepted: 08 July 2014; published online: 29 July 2014. Citation: Ang KK, Guan C, Phua KS, Wang C, Zhou L, Tang KY, Ephraim Joseph GJ, Kuah CWK and Chua KSG (2014) Brain-computer interface-based robotic end effector system for wrist and hand rehabilitation: results of a three-armed randomized controlled trial for chronic stroke. Front. Neuroeng. 7:30. doi: 10.3389/fneng. 2014.00030 This article was submitted to the journal Frontiers in Neuroengineering. Copyright © 2014 Ang, Guan, Phua, Wang, Zhou, Tang, Ephraim Joseph, Kuah and Chua. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

