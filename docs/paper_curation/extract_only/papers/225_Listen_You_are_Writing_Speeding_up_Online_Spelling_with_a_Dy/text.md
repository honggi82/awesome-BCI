#### ORIGINAL RESEARCH ARTICLE

published: 14 October 2011 doi: 10.3389/fnins.2011.00112

# Listen, you are writing! Speeding up online spelling with a dynamic auditory BCI

## Martijn Schreuder1*,Thomas Rost1,2 and MichaelTangermann1

- 1 Machine Learning Laboratory, Berlin Institute ofTechnology, Berlin, Germany
- 2 Bernstein Center for Computational Neuroscience, Berlin, Germany

Edited by: Leonardo Cohen, National Institutes of Health, USA

Reviewed by: Kenji Kansaku, Research Institute of National Rehabilitation Center for Persons with Disabilities, Japan Michal Lavidor, Bar Ilan University, Israel Surjo R. Soekadar, National Institutes of Health, USA

*Correspondence: Martijn Schreuder, Machine Learning Laboratory, Berlin Institute of Technology, FR6-9, Franklinstraße 28/29, 10587 Berlin, Germany. e-mail: schreuder@tu-berlin.de

Representing an intuitive spelling interface for brain–computer interfaces (BCI) in the auditory domain is not straight-forward. In consequence, all existing approaches based on event-related potentials (ERP) rely at least partially on a visual representation of the interface.This online study introduces an auditory spelling interface that eliminates the necessity for such a visualization. In up to two sessions, a group of healthy subjects (N =21) was asked to use a text entry application, utilizing the spatial cues of theAMUSE paradigm (Auditory Multi-class Spatial ERP).The speller relies on the auditory sense both for stimulation and the core feedback. Without prior BCI experience, 76% of the participants were able to write a full sentence during the ﬁrst session. By exploiting the advantages of a newly introduced dynamic stopping method, a maximum writing speed of 1.41char/min (7.55bits/min) could be reached during the second session (average: 0.94char/min, 5.26bits/min). For the ﬁrst time, the presented work shows that an auditory BCI can reach performances similar to state-of-the-art visual BCIs based on covert attention. These results represent an important step toward a purely auditory BCI.

Keywords: brain–computer interface, directional hearing, auditory event-related potentials, P300, N200, dynamic subtrials

## INTRODUCTION

Recent successes have been booked in the application of brain– computer interface (BCI) technology at the end-user’s home,both for communication (Nijboer et al., 2008b; Sellers et al., 2010) and other purposes (Münssinger et al., 2010). BCIs allow for a direct connection between the brain and the external world. Interpretation of the brain signals is generally performed in realtime and users can thus interact with a device by changing their brain state. Apart from applications for healthy users (Nijholt et al., 2009; Tangermann et al., 2009; Blankertz et al., 2010), BCI technology was ultimately meant to allow otherwise paralyzed people to communicate and interact with their environment again.

Most of the aforementioned studies are based on visual eventrelated potentials (ERP). Their use in BCI was introduced by Farwell and Donchin (1988) and they have been a major focus in BCI research. This study describes a BCI that is based on auditory ERPs, which may extend the work on visual ERPs in several important aspects.

In an exploratory study (Huggins et al., 2011), 61 people suffering from mid-stage amyotrophic lateral sclerosis (ALS) were included with ALSFRS-R ratings ranging from 18 to 33 (Cedarbaum et al., 1999). The authors found that a larger portion of their population suffered from auditory (42%) than visual (25%) deﬁcits.Ontheotherhand,arecentstudywhichfollowedapatient with ALS through the late stages of the disease, reported that a disease-resistant BCI may only be possible through the auditory orproprioceptivepathways(Murguialdayetal.,2010).Indeed,several studies show that the traditional visual BCI paradigms may

not function well when eye-gaze control is limited (Brunner et al., 2010; Treder and Blankertz, 2010). A user group with such heterogeneous abilities and needs clearly stipulates the necessity for a range of diverse BCI systems. For these reasons, the interest in additional BCI paradigms has grown in recent years.

Some studies report that by using a different interface, a visual ERP BCI can be realized that does not depend on eye-gaze control (Acqualagna et al., 2010; Liu et al., 2011; Treder et al., 2011). Anotherapproachcouldbetoswitchtoadifferentsensorydomain altogether, by using auditory- (Hinterberger et al., 2004; Kanoh et al., 2008; Nijboer et al., 2008a; Kim et al., 2011; Vlek et al., 2011) or vibrotactile cues (Cincotti et al., 2007; Brouwer and van Erp, 2010) for feedback or stimulation. Auditory stimulation usually involves an oddball paradigm where the user is exposed to stimuli that differ from each other on some property. The user is required to focus attention to one of them. Such paradigms generallyinvolvetoneswithdifferencesinpitch,resultinginabinaryBCI (Hill et al., 2005; Halder et al., 2010). Multi-class approaches have been described using different environmental sounds (Klobassa et al., 2009) or spoken words or numbers (Sellers and Donchin, 2006; Furdea et al., 2009; Kübler et al., 2009; Guo et al., 2010). Though this increases the number of options per selection, presentation of such stimuli is inherently slower. Furthermore, the mapping is often not intuitive, so that the matrix is still shown (albeit not ﬂashed).

Of special interest is a recent study (Kübler et al., 2009), which describes a patient trial with the paradigm previously reported in (Furdea et al., 2009). Four subjects suffering from ALS received extensive training with the auditory BCI. Three of them were close

to, or in the locked-in state (LIS, only residual eye-movement), whereas the forth was entering the totally LIS (TLIS, no residual eye-movement). Though all four subjects had control over a visual BCI, they performed poorly on the auditory BCI. The authors acknowledge however the importance of the auditory modality for BCI. One of their suggestions for improvement is a spatial distribution of the stimuli.

Several studies indeed show that using stimuli with spatial features can improve performance (Schreuder et al., 2009; Höhne et al., 2010). In ofﬂine studies, adding spatial information to an auditorystimuluswasbeneﬁcialtotherecognition,bothexpressed in reaction times or accuracy (Belitski et al., 2011) and classiﬁcation performance (Schreuder et al., 2010). Furthermore, it allows for an intuitive multi-class auditory BCI without sacriﬁcing speed. Such paradigms could even be used to extend traditional (visual) BCIs to improve performance or facilitate training during the late stages of ALS (Belitski et al., 2011).

The current study is an extension of Schreuder et al. (2010), where the principle of a paradigm using spatial auditory stimuli was ﬁrst shown (it was later called Auditory Multi-class Spatial ERP, or AMUSE). Here, AMUSE drives a spelling interface in online mode. Using six spatial locations and a two-step, hex-ospell like speller interface (Blankertz et al., 2006), subjects were enabled to write by attending tones in space.

It is shown here that AMUSE, combined with the speller interface, allows for reliable online spelling for a majority of healthy subjects. The proposed speller interface is intuitive and easy to learn. Its core components (stimulation, spelling tree navigation, and result feedback) are realized in the auditory domain. Average spelling performance was high, out-performing current auditory BCIs. Furthermore, a new method for dynamically changing the number of stimuli was introduced. Based on the data gathered, a trial could thus either be stopped if a threshold was reached, or continued. This method further increased the performance signiﬁcantly by reducing trial length.

## MATERIALS AND METHODS

### PARTICIPANTS

Participants were 21 subjects that had never worked with a BCI before (BCI naïve). They reported no current or prior neurological disorder and normal hearing. The latter was not formally tested. Subjects were ﬁnancially compensated for their participation. Age ranged from 20 to 57 (m =34.1, SD=11.4). Procedures were approved by the Ethics Committee of the Charité University Hospital. All subjects provided verbal and written informed consent and subsequent analysis and presentation of data was anonymized.

### DATA ACQUISITION

EEG was recorded using a ﬁxed set of 56 Ag/AgCl electrodes and BrainAmp ampliﬁers (Brain Products, Munich, Germany). Channels were referenced to the nose. Electrooculogram (EOG) was co-recorded with two bipolar channels. All impedances were kept below 15kΩ. Only for subject VPfce did the impedance exceeded this threshold at the end of the session. The signals were sampled at 1kHz and ﬁltered by a hardware analog band-pass ﬁlter between 0.1 and 250Hz before being digitized and stored for

ofﬂine analyses. For online use, the signal was low-pass ﬁltered below 40Hz, down sampled to 100Hz and streamed to the online Berlin BCI system.

Thestimuluspresentation,theonlineBerlinBCIsystemandthe ofﬂine analyses were implemented in Matlab (MathWorks), making use of the Psychophysics Toolbox (Brainard, 1997) for multichannel audio presentation and the open-source text-to-speech system Mary (Schröder and Trouvain,2003).A multichannel,lowlatency ﬁrewire soundcard from M-Audio (M-Audio FireWire 410) was used to individually control the active, off-the-shelf computer speakers (type Sony SRS-A201).

### PARAMETER SCREENING

A dependence of ERP amplitude and latency on stimulus amplitudeandduration,particularlyintheearlycomponents,haspreviously been reported (Gonsalvez et al.,2007). To investigate this for the AMUSE paradigm, two parameter screenings were conducted, testing for the inﬂuence of stimulus loudness and duration on classiﬁcation performance. The studies were performed with six and seven healthy subjects, respectively.

Results of both the parameter screening did not expose a systematic inﬂuence on the classiﬁcation performance. Also, the subjectivelyreportedfavorite conditioncouldnotbematchedwith the condition giving the highest score. Parameters were therefore ﬁxed to those used in Schreuder et al. (2010; ∼58dB and 40ms).

### STIMULI

Thelocalizationof astimulusintheazimuthplanedependsmainly on two principles, interaural timing differences (ITD) and interaural level differences (ILD), which both have their own optimal frequency range (Middlebrooks and Green, 1991). Where the ITD effect is most efﬁcient for frequencies up to 1–1.3KHz, the ILD effectprovidesthelocalizationinformationforhigherfrequencies, roughly >3KHz. Ofﬂine analyses showed that spatial location as a discriminative feature is enough to reliably elicit a P3 response (Schreuder et al., 2009, 2010). However, to optimally exploit both effects, stimuli consisted of a low frequent tone with harmonics and a high frequent,band-pass ﬁltered noise overlay (see Table 1). To further increase resolution, each of the six directions was associated with a unique combination of tone and noise to add an additional cue property. Stimuli can be found in Data Sheet 1 of the supplementary data.

Table 1 | Stimulus properties.

Direction Base tone (Hz) Noise range (KHz)

- 1 762 3.6–9.2
- 2 528 3.2–8.0
- 3 1099 4.0–10.5
- 4 635 3.4–8.6
- 5 915 3.8–9.8
- 6 440 3.0–7.5

The stimulus of each direction (see Figure 1) was a complex of a tone (base frequency and harmonics) and noise.

### PROCEDURE

Subjects sat in a reclining chair, facing a screen with a ﬁxation cross at ∼1m. They were surrounded by six speakers at ear height, evenly distributed in a circle with 60˚ distance between them (see Figure 1A) which is well over the resolution of spatial hearing in the azimuth plane (Grantham et al., 2003). Circle radius was ∼65cmandspeakerswerecalibratedtoacommonstimulusintensityof ∼58dB.Theroomwasneitherelectromagneticallyshielded, norwereextensivesoundattenuatingprecautionstaken.Beforethe experiments,subjects were asked to minimize eye movements and muscle contractions during recording periods.

The experimental protocol is visualized in Figure 1B. A run, or sentence, consisted of several trials. Each trial, or selection, consisted of several iterations. During one iteration all speaker locations were stimulated exactly once in a pseudo-random order, before proceeding to the next iteration. This pseudo-random sequence was generated such that (1) between two stimuli from one speaker, there were at least two other stimuli and, (2) two successive stimuli never came from neighboring speakers. A single stimulus is hereafter referred to as a subtrial. The stimulus onset asynchrony (SOA) was set to 175ms.

The amount of iterations/trial inﬂuences the efﬁciency of the system. A high number is likely to increase the accuracy, but at the same time it increases the time needed for a selection. Vice versa, a low number will allow for quicker selections, but they are likely to contain more errors. Therefore, two settings were tested: (1) a ﬁxed number of 15 iterations and, (2) a method which allows for determining the number of iterations on runtime.

During a trial, the subject’s task was to focus attention to one (target) of the six directions and mentally count the number of appearances. During the calibration phase the target was given to the subject explicitly. During the writing phase the target direction

was not given explicitly, but had to be inferred from the spelling interface.

All 21 subjects performed a ﬁrst session (Session 1), and those that reached a performance level that allowed them to write the given sentence were invited for a second session (Session 2).

### SPELLING INTERFACE

For online writing, an adapted version of the hex-o-spell speller (Blankertz et al., 2006) was created in which a character can be selected in two steps. First a group of characters is selected (group “F–J”in Figure1B) by focusing on the corresponding direction. In the second step the characters of this group are divided over ﬁve of the directions and an individual letter can be selected. Choosing the sixth direction returns the user back to the ﬁrst selection step, thus preventing a wrong letter selection. Which (group of) letter(s) corresponds to a direction – and which direction had been selected – could be read out to the user using speech synthesis (Schröder and Trouvain, 2003). The copy text and progress were presented visually.

### SESSION 1

First,subjects were familiarized with the sounds,after which about 30min of calibration data were recorded. Subjects performed 48 trials,8 for each direction.At the start of a trial the target direction was indicated both visually (one of six on-screen dots highlighted) and auditory (by playing the direction speciﬁc cue from the target location). After that, stimulation was purely auditory and subjects were asked to count the number of target appearances in the trial and report them. Each calibration trial consisted of 15 iterations. However, in order to have a varying number of targets and thus have a more challenging task, a prequel consisting of varying

|[Figure 1]<br><br>FIGURE 1 | Experimental protocol. (A) Subjects were surrounded by six speakers at ear height. Speakers were equally spaced with 60˚ angle between neighbors, with a circle diameter of 65cm. (B) Visualization of the<br><br>experimental protocol in the online phase. In Session 1, the number of iterations j was set to 15. For Session 2, j was determined by the dynamic stopping method. No labels were read aloud (RL) in Session 2.|
|---|

length (1–3 iterations) was added. That the visual target presentation was not necessary was proven in a session with a single, blind subject.

Then, subjects were asked to write word for word one of two sentences:“FRANZJAGTIMTAXIDURCHBERLIN”or“SYLVIA WAGT QUICK DEN JUX BEI PFORZHEIM.” Sentence assignment was random. Wrong letters had to be corrected by the user by performing a backspace action, requiring two selections. No prequel was included. The stimulation sequence and the overhead of label, and result presentation for a single trial took around 34s. With a two-step letter selection process, the maximum theoretical speed is thus 0.89char/min.

### SESSION 2

Subjects who were able to successfully write with the system in Session 1 came back for Session 2. This session consisted of a calibration phase – equal to Session 1 – and the online writing of two German sentences. For Session 2 the protocol was adjusted in several ways. First,a dynamic stopping method was introduced which could stop a trial after 4–15 iterations when enough evidence for a correct selection was found (see below). Second, subjects were asked to study the selections that are needed for each character at home. They were no longer provided with auditory labels prior to a trial, which reduced the trial time by about 6.2s. The maximum theoretical speed with 15 iterations was thus 1.10char/min.

During the ﬁrst sentence, subjects got visual information on the labels to familiarize them again with the interface. During the second sentence this was turned off,thus relying exclusively on the auditory sense. During both sentences,subjects still received auditory information after a selection to know their current location in the spelling tree. The ﬁrst sentence was the remaining sentence from Session 1, whereas the second sentence could be chosen by the subject but should be at least ﬁve words long.

### FEATURES AND CLASSIFIER

Classiﬁcation was done on each subtrial, thus reducing the problem to a binary task,i.e.,to classify each subtrial as a target or nontarget. Spatio-temporal features for classiﬁcation were extracted accordingtothefollowingprocedure.Firstthedatawerebaselined, using the 150-ms pre stimulus data as reference. Then,the samplewise r2 coefﬁcient was calculated for targets vs. non-targets. Based on this, a set of two to four intervals with high discriminative information content were hand-picked, such that both early and late components were represented. All samples within each interval were then averaged,so that one interval was represented by one feature per channel. This resulted in an overall dimensionality of 112–224 features.

The beneﬁt of this method over conventional sub sampling (Krusienski et al., 2006; Schreuder et al., 2010) is a relatively small number of features per channel which capture most of the discriminative information. Furthermore, by combining consecutive samplesinsteadof pickingindividualsamples,asisthecaseinstepwise linear discriminant analysis (Farwell and Donchin,1988),the interpretation of the chosen features is straight-forward and a priori knowledge can be included during the selection. Using this feature vector, a linear, binary classiﬁer was trained. In order to

prevent overﬁtting, the classiﬁer was conditioned using shrinkage regularization (Ledoit and Wolf, 2004; Blankertz et al., 2011).

### DECISION MAKING

The classiﬁer was trained to assign negative scores to target subtrials and positive scores to non-target subtrials. Let X∈RC ×J be a matrix of classiﬁer scores of a trial, where C is the number of classes (six in our case),and J the number of performed iterations. If c ={1,...,C}, then let x˜ be a row vector, where x˜c denotes the median value of classiﬁer scores for class c. The winning class c∗ can be described as c∗ = argminc x˜c, i.e., the class with the lowest median value. For Session 1 J was ﬁxed to 15.

In order to further optimize the spelling speed,a dynamic stopping method was introduced in Session 2. Such a method allows for trials with less than 15 iterations, when the obtained data support an early stop. Different methods for tackling this have been introduced to BCI before (Serby et al., 2005; Lenhardt et al., 2008; Zhang et al., 2008; Liu et al., 2010), and were mainly tested in the context of visual ERP based BCI and one-step interfaces.

It can be assumed that at a low number of iterations the quality of a decision will be susceptible to sporadic outlying classiﬁer scores,andthattheinﬂuenceof thesewilldecreasewithanincreasingnumberof iterations.Inlinewiththisassumption,anapproach which uses iteration-speciﬁc thresholds was designed. Thresholds are based on the calibration data, and are thus subject speciﬁc.

The variable p is deﬁned as the distance from x˜c∗ to the second lowest value in x˜. It represents a conﬁdence measure of the winning class. Note that, as this is a relative value, it is robust to linear biases that might arise when moving from the calibration phase to the online phase. In the online setting, the BCI checks after each iteration j ∈{1,...,J} if pj – based on the data gathered thus far – exceeds threshold Tj (see below). If so,the trial is stopped and class c∗ is selected.

Heuristic for decision threshold determination

For ﬁnding the decision thresholds T, the trained classiﬁer is reapplied to the complete calibration data. Although this can be considered overﬁtting and might lead to an overestimation of the class distances, it is not consider as a caveat when ﬁnding a conservative threshold.

For calculating Tj, we consider all calibration data collected within a trial,up to iteration j. First,the winning class for this iteration cj∗ and the conﬁdence pj are calculated and pj is assigned a label; true (pj+) if cj∗ corresponds to the target direction, and false (pj−) otherwise. This is repeated for each trial n ∈{1,..., N} and iteration j, and results are collected in the matrices P+ ∈ RN×J and P− ∈ RN×J. In order to approximate a smooth upper error bound,athirdorderpolynomialF isﬁttedtotheupperlimitof P−. Then,if fj referstothevalueof F atiterationj,theiteration-speciﬁc thresholdTj isdeﬁnedasthemaximumof fj andtheproductof the median of column j in P+ and R. The hyperparameter R is used to control the number of false negative stops. In this study, R was set to 1, which means that maximally only 50% of possible correct early stops is recognized. The above is visualized in Figure 2.

The threshold is rather conservative, as it is biased away from false positives (incorrect early stops). The rational behind such

pair of directions. This should expose any systematic directional preference, if present.

|[Figure 2]<br><br>FIGURE 2 |Visualization of iteration-speciﬁc decision threshold.The conﬁdence measure p is plotted for correct (P+) and incorrect (P−) decisions as a function of the number of iterations j.The black line F is ﬁtted to the maximum values of P−.The decision thresholdT is deﬁned as the maximum of F and the median of P+.|
|---|

Given a confusion matrix CMN ×N, where N is the number of classes and each row is normalized, we deﬁne the sensitivity and recall for pairs of classes i, j ∈{1,...,6} as follows

CM(i,i) CM(i,i) + CM(i,j) ∗ (N − 1)

sensitivity(i,j) =

(1)

CM(i,i) CM(i,i) + CM(j,i) ∗ (N − 1)

recall(i,j) =

(2)

The matrix FN ×N of pairwise F-scores is then deﬁned as

sensitivity(i,j) ∗ recall(i,j) sensitivity(i,j) + recall(i,j)

F(i,j) = 2 ×

(3)

where 1≤i≤C and 1≤j≤C. It is thus the harmonic mean of sensitivity (the ability to identify a target) and recall (the ability to reject a non-target).

a conservative threshold is that any false positive is costly, as correcting an error takes up to four selections. For applications where a false selection is less costly, the threshold can be set less conservative by taking a smaller value for R.

### DATA ANALYSES

The BCI performance evaluation was done online, unless stated otherwise. Three evaluation metrics were calculated for each subject and each sentence: accuracy (acc), characters per minute (char/min), and information transfer rate (ITR; Schlögl et al., 2007). We deﬁne accuracy as the number of correct selections divided by the total amount of selections. Accuracy assesses the performance of the BCI, irrespective of the application interface.

For assessing the BCI in combination with the spelling application we used char/min as the preferred metric for writing proﬁciency. Char/min is deﬁned as the number of correctly written letters divided by the time it took to write all letters (including incorrect letters). Here, it gives a particular conservative estimate, as subjects had to correct any mistakes. Thus, all letters are in the endcorrectatthecostof longerwritingtime(andlowerchar/min). This is a more realistic assessment of the system’s usefulness, as it includes the error recovery strategy. In a real user setting, errors will occur and may have to be corrected.

For the sake of comparison,the ITR is also reported.We use the calculation method proposed by Schlögl et al. (2007), as there are systematic confusions between directions. ITR combines the accuracy, number of possible decisions, and the number of selections per minute into a single number. Originating from information theory, it assesses information transfer over a noisy channel. Although often used in BCI, it is a theoretical measure and its interpretability in terms of practical relevance of a BCI is difﬁcult.

### DIRECTIONAL PREFERENCE

The confusion matrix (CM) provides a lot of information about the discriminability of the different classes. From it, the pairwise F-scores were calculated to assess the confusion between each

## RESULTS

Of the 21 subjects, 16 subjects (or 76%) were able to write a full German sentence at ﬁrst try (Session 1). The other ﬁve subjects got at most one word correct, before their experiment was stopped. In Session 2, 14 out of 15 returning subjects wrote both full German sentences. Subject VPfch was able to write the ﬁrst sentence, but took so long that the session had to be aborted after this. Subject VPfax was unable to return for the second session, although successful in the ﬁrst session. In the following, sentence 1 refers to the sentence written in the ﬁrst session, and sentence 2a and 2b to those written in the second session. Individual performance measures for each subject can be found in Table 2. Movie S1 in Supplementary Material shows an example of a user operating the system.

### BCI PERFORMANCE

Brain–computer interface performance did neither correlate with age (r<0.01, p=0.75), nor with gender (Kolmogorov–Smirnov test: p=0.42). Average accuracy per sentence was 77.4, 84.3, and 86.1% for sentence 1, 2a, and 2b, respectively. The increase in performance from Session 1 to Session 2 is due to the drop out of less-performing subjects. This is shown in Figure 3A, which gives the overall accuracy for each subject and each session. Three meanswerecalculated;ﬁrst,theblacklineindicatesthemeanwhen considering all subjects for a session, as given above. However, as those subjects that were unable to write in the ﬁrst session did not participate in the second session, the gray line includes only those subjects (N =14) that ﬁnished all three sentences,which is a fairer comparison of the sessions (0.88, 0.86, and 0.86 for sentence 1, 2a, and 2b respectively). No signiﬁcant difference existed (p=0.97) between performance in sentence 2a (m =0.86,SD=0.08) and 2b (m =0.86, SD=0.11). The difference between these conditions is that for sentence 2b the visually presented support labels were switched off. This shows that the spelling tree can easily be learned and thus need not be presented visually.

Asthenumberof iterationsvariedinSession2,anofﬂineanalysis was performed to objectively assess any learning effect between

Table 2 | Performance summary.

User Gender Age Session 1 Session 2

Sentence 1 Sentence 2a Sentence 2b

Acc (%) Char/min ITR Acc (%) Char/min ITR Acc (%) Char/min ITR

VPfaz F 27 98.4 0.83 4.59 95.9 1.26 7.12 100.0 1.41 7.55 VPfcc M 28 98.4 0.84 4.64 85.1 0.88 5.07 88.6 0.88 5.38 VPkw F 57 97.0 0.81 4.51 86.5 0.94 5.45 86.5 0.95 5.68 VPfca M 23 94.7 0.77 4.35 97.0 1.30 7.32 94.2 1.14 6.66 VPfcd M 25 92.9 0.77 4.26 91.3 1.10 6.05 97.9 1.35 7.01

- VPfaw M 40 91.7 0.73 4.15 92.7 1.01 5.96 94.3 1.03 6.05

- VPfar M 31 85.6 0.58 3.55 89.8 0.96 5.58 83.3 0.76 4.70 VPfav M 40 84.9 0.59 3.51 88.3 1.01 5.94 96.8 1.38 7.27 VPfcb M 21 84.7 0.49 3.51 81.7 0.65 4.45 85.1 0.75 5.47 VPfck M 43 83.2 0.50 3.28 78.0 0.61 4.20 68.5 0.40 2.47 VPfau F 25 81.9 0.50 3.16 93.4 1.03 6.08 83.9 0.74 4.74 VPfcj F 23 80.6 0.41 3.00 75.3 0.50 3.68 69.3 0.65 2.32 VPfcg F 33 79.5 0.40 3.20 77.8 0.92 4.14 88.5 1.06 6.07 VPfch M 55 79.3 0.46 2.79 57.9 0.36 0.64 x x x VPfcm M 51 78.3 0.47 2.72 73.4 0.51 2.72 68.1 0.61 2.32

VPfax M 28 72.1 0.32 2.02 x x x x x x VPfci M 28 58.6 – 1.47 x x x x x x VPfat F 25 54.1 – 0.58 x x x x x x VPfcl F 44 51.7 – 0.27 x x x x x x VPfce M 47 40.0 – 0.00 x x x x x x

- VPfas F 29 37.5 – 0.00 x x x x x x Session mean 34.1 77.4 0.59 2.84 84.3 0.87 4.96 86.1 0.94 5.26 In all sessions mean 33.4 88.0 0.62 3.75 86.2 0.91 5.27 86.1 0.94 5.26

Performance measures accuracy (Acc), characters per minute (Char/min), and information transfer rate (ITR) are given for all subjects and all sentences, as well as age and gender. Two means are calculated over each measure. Session mean refers to the mean when considering all available subjects, whereas In all sessions refers to the mean of only those subjects that succeeded in all sentences.The latter is included for cross session comparison. Subjects are sorted according to their accuracy on the ﬁrst session. Missing values are either because a the sentence was not written by the user (x) or because the Char/min could not be calculated (–). The non-linear relation between accuracy and characters per minutes can be explained by the type of errors committed, i.e., on the ﬁrst or second level.

|[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>FIGURE 3 | Session differences. Session differences in accuracy (A) and char/min (B) are plotted for all subjects.The black line represents the mean of all subjects in a session and the gray line represents the mean of the 14 subjects that succeeded on all three sentences. (A) No signiﬁcant difference was found between sessions in the accuracy. No learning effect was found even when the number of iterations was reduced to four, as<br><br>represented by the red, dotted line. (B)The char/min for Session 2 was signiﬁcantly better than for Session 1, which is due to early stopping and less label vocalization. Some subjects performed higher than the theoretic maximum char/min, indicating a particular beneﬁt from the dynamic stopping mechanism. Points are slightly displaced on the horizontal axis to prevent clutter.|
|---|

To assess the inﬂuence of the dynamic stopping method independently, the 6.2-s time gain from the second modiﬁcation was added again to sentence 2b in an ofﬂine simulation. A signiﬁcant increase of 37% remains from sentence 1 to the simulated sentence 2b (m =0.85, SD=0.26; t=4.05; p=0.001). Thus, the dynamic stopping method increases performance signiﬁcantly by itself. Statistical testing was done using two-sided paired t-tests.

|[Figure 6]<br><br>FIGURE 4 | Accuracy over time. Selection accuracy of Session 1 is plotted for each subject as a function of the word written, which approximates time.The gray line represents the mean over the subjects that ﬁnished the entire sentence, which shows no signiﬁcant slope.The red dotted line represents the mean over all subjects.|
|---|

### DYNAMIC STOPPING METHOD

Over all subjects, a total of 3297 online trials were recorded in Session 2. The dynamic method produced early stops in 41.3% of these trials. The maximum number of 15 iterations (full trial) was reached in the remaining 58.7% of the trials. This was in cases where the threshold was not exceeded in iterations 4–14. Early stops before the fourth iteration were not allowed.

About 12.6% of early stops resulted in an incorrect decisions, which is only 5.2% of the overall number of trials. This reﬂects the conservative threshold policy as described in the methods. At 23.5%, the percentage of errors was almost twice as high for full trials. An obvious explanation is that mostly the “difﬁcult-to-decide-trials” reach the full number of iterations.

session. For each sentence, the online classiﬁcation scores of the ﬁrst four iterations were used to take a decision (the minimum number of iterations in Session 2 was 4). The red, dotted line in Figure 3A shows these results. No systematic learning effect was present. As sentence 1 (m =0.88, SD=0.07) and sentence 2b showed no signiﬁcant performance difference (p=0.40), it can thus be concluded that early stopping did not introduce additional errors. Statistical testing was done using two-sided paired t-tests.

As depicted in Figure 5A, the majority of early stops is performed directly at the fourth iteration, with the number of stops decreasing until ﬁnally remaining trials are stopped at the 15th trial. At each individual iteration the percentage of incorrect decisions is lower than for full trials.

Figure 5B gives the different errors for each subject and sentence 2a and 2b. It shows that the error rate for early stops is relatively low, and similar for all subjects. Only subject VPfch had such a high error rate – both for early stops and full trials – that there was no time left for writing the second sentence. The black lines indicate the minimum number of decisions necessary for writing the particular sentence.

Figure 4 shows the accuracy for each subject as a function of the word written in the ﬁrst sentence, which we take as an approximation of time. Considering only those subjects that were able to ﬁnish the session, the slope of the linear least-squares ﬁt between performance and the word number is close to 0, implying that subjects are able to use the interface straight away.

The average ITR over all 21 subjects of Session 1 was

- 2.84bits/min (maximum 4.59bits/min), which includes also subjects that did not reach a performance level appropriate for writing (see Table 2). When considering only those subjects that performed well on all sentences, the average ITR over Session 1 was
- 3.75bits/min. During the second session this increased by 40% to an average of 5.26bits/min, with a maximum of 7.55bits/min.

### PHYSIOLOGY

Calibration data from the ﬁrst session of all subjects was pooled and the grand-average calculated. Artifacts were rejected according to a ﬁxed variance criterium and a peak-to-peak difference criterium. Figure 6A shows the grand-average time series for channel Cz. An early component is consistently present, peaking about 130ms after each stimulus. This causes a rhythmic perturbation of the EEG signal, thereby masking the generally described ERP components. Although present in both target and non-target trials, it is more negative for target trials, i.e., it is attention modulated. An interval from 95 to 200ms was selected to capture this peak.

### WRITING EFFICIENCY

Figure 3B presents the writing proﬁciency for each subject and each session in terms of characters per minute (char/min). The black line represents the sentence-wise mean for all subjects who ﬁnished that sentence. The gray line represents the sentence-wise mean for only those subjects that ﬁnished all sentences (N =14), which will be considered for further analyses. As expected from the accuracy, there is no signiﬁcant difference between sentence 2a (m =0.91, SD=0.25) and sentence 2b (m =0.94, SD=0.31) of Session 2 (p=0.57). However, when comparing sentence 1 (m =0.62, SD=0.16) with sentence 2b, a signiﬁcant increase of 52% can be observed (t=4.68; p<0.001). As the accuracy was equal, the increase must be due to improvements in the interface’s efﬁciency. These were twofold: (1) dynamic stopping was introduced and (2) the vocalization of the labels was omitted.

A positive component is found for target trials, captured in the intervalfrom280to450ms.Duetobothtimingandscalplocation, we consider this to be what is described as the P3 component.

Figure 6B shows the grand-average scalp topography for both target and non-target trials for both selected intervals, whereas Figure 6C displays the discriminability between those, expressed in signed AUC values (Schreuder et al., 2010). Low voltage amplitude and AUC values are due to inter subject differences. Online data are similar and thus not presented here. It is apparent that the early negative component is found mainly over the frontal

|[Figure 7]<br><br>[Figure 8]<br><br>[Figure 9]<br><br>FIGURE 5 | Early stopping performance. For (A), data is collapsed over all subjects that participated in Session 2.The number of correct and incorrect trials are plotted as a function of the iteration in which a trial was stopped. Accuracy is high in general, and particularly for those trials that were stopped<br><br>before the 15th iteration.The same data is plotted in (B), but separately for each subject and for sentences 2a and 2b.The black markers indicate the minimum number of selections necessary for writing a sentence. Subject VPfch did not perform sentence 2b.|
|---|

Table 3 | Grand-average confusion matrix.

|[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>FIGURE 6 | Grand-average physiology. Calibration data of the ﬁrst session is collapsed over subjects and trials. Average time series for channel Cz are plotted together with the positions of ﬁve consecutive stimuli (A). Scalp potential distributions for target and non-target trials are shown in (B) and distributions of class-discriminative information in (C).Two intervals were hand-picked based on the signed AUC values, and are represented by the shaded gray areas. Early negative components over frontal and temporal regions are followed by a positive component over centro-parietal areas.|
|---|

Selected class

1 2 3 4 5 6 Sensitivity N

Target 1 765 9 72 16 27 23 83.9 912 class 2 18 881 26 29 37 72 82.9 1063

- 3 24 18 543 12 41 9 83.9 647
- 4 24 26 15 629 54 54 78.4 802
- 5 12 8 10 12 539 7 91.7 588
- 6 44 84 66 71 59 773 70.5 1097

PPV 86.2 85.9 74.2 81.8 71.2 82.4

Confusion matrix of classiﬁcation results over all subjects. Sensitivity, positive predictive value (PPV), and the occurrence (N) of each target are given for convenience.

and bilateral auditory cortical areas. The later positive component is focused over the central mid-line electrodes and toward the temporal areas. This is in line with previous ofﬂine results (Schreuder et al., 2010). It can be noted that in the manual feature extraction procedure, different intervals can be assessed based on this physiological plausibility before being included for online use.

### DIRECTIONAL PREFERENCE

The grand-average CM can be found in Table 3. Figure 7 displays matrix F of the pairwise F-scores,where high values indicate a good separability between the indicated classes. Diagonal values are irrelevant and marked X. Other elements are marked as location neighbors (l), sound neighbors with 1.5 tone pitch difference (s) and locations that are symmetric in the front–back plane (fb); all are expected to hamper separability. Tone locations were optimized such that no entry has two such labels.

Directions without any degrading factor had an average pairwise F-score of 0.89 (SD: 0.15). This was only slightly degraded for spatial neighbors (0.87, SD: 0.16), but both pitch neighbors (0.82, SD: 0.19) and especially the front–back confusion (0.76, SD: 0.22) had a larger effect on pairwise discriminability. These effects were investigated by performing pairwise t-tests

### PERFORMANCE

|[Figure 14]<br><br>FIGURE 7 | Pairwise F-scores between speaker locations.The matrix visualizes the pairwise confusions between an intended location (y axis) and a distracting location (x axis), expressed in F-scores. Lighter colors mean better discrimination. Entries are labeled as l =location neighbor, s =sound neighbor, and fb =front–back symmetric location.|
|---|

To assess the practical relevance of a BCI speller, the most intuitive metric is the number of characters that a user can write per minute. However, as this is not uniformly utilized in BCI literature, it makes direct comparison troublesome. For this reason, the ITR as deﬁned by (Schlögl et al., 2007) was reported. The current setup without any dynamic stopping (Session 1) shows ITR values that are en par with the online results of the state-of-the-art auditory BCI systems (Sellers and Donchin, 2006; Furdea et al., 2009; Klobassa et al., 2009; Höhne et al., 2010), all of which showed the spelling tree through the visual domain. Owing to the intuitive mapping, this need was eliminated here.

With the use of the dynamic stopping method in Session 2, the ITR increased to an average of 5.26bits/min and a maximum of 7.55bits/min, which comes close to currently available covert visual BCI systems (Liu et al., 2011; Treder et al., 2011).

### FRONT–BACK CONFUSION

Learning from Schreuder et al. (2010,2009),the stimuli were optimized for better performance. As shown in Figure 7, the number of detrimental factors was limited. However, speakers with the same angle from the frontal and posterior mid-line – speakers 1 and 3 or speakers 4 and 6 in Figure 1 – were confused relatively often. This type of error is well known in hearing research as the front–back confusion and results from an ambiguity in primary interaural differences, ITD in particular (Wightman and Kistler, 1999).

on the F-scores of each degrading factor with those pairs without degrading factors. After Bonferroni correction,the front–back confusion showed a trend of negative inﬂuence on recognition (p=0.056).

Fromthepitchneighbors,thehighestandlowestpairweremost often confused. All this was in line with subjective reporting of the subjects, and gives indicators for future improvements.

It was shown that differentiation in the front–back plane relies on at least two features: (1) spectral cues in the range from 8 to 16kHz, referred to as the extended high frequency range (EHF; Langendijk and Bronkhorst,2002) and (2) small head movements (Wightman and Kistler,1999). Bearing in mind the potential enduser and the short stimulus length, the latter may be out of reach. However, for the ﬁrst feature the noise component of the stimuli usedinthecurrentstudycouldbeconsideredsuboptimal.Though with aging the sensitivity to this EHF is reduced for a considerable number of people (Fozard and Gordon-Salant, 2001), the upper bound on the noise ﬁlter should be increased to 20kHz to provide a more optimal range.

## DISCUSSION

A previous ofﬂine study already showed the potential of the AMUSE paradigm (Schreuder et al., 2009, 2010). Now, coupled to a spelling interface, it allowed a majority of healthy subjects to write a full sentence with an average speed of 0.59char/min on the ﬁrst session, and up to a maximum speed of 1.41char/min in the second session. To our knowledge, this is the fastest online auditory BCI speller described in literature. For the sake of comparison, it is important to emphasize once more the conservative nature of the protocol.

Furthermore, it is known that for posterior sound sources the intensity of high frequencies is reduced when compared to frontal sources (Blauert, 1983). In this study, the frontal speakers (1 and 6) both had lower frequency ranges in the stimulus complex than their respective confusers in the back (speakers 3 and 4), which may also account for some of the front–back confusion.

In the ﬁrst session, 16 out of 21 subjects (or 76%) were able to write a full German sentence. According to Guger et al. (2009) over 90% of people is “able to control a P300-based BCI.” However, as both their tested conditions were overt visual paradigms this may be a too optimistic estimate. The selected BCI paradigms are most prevalent in literature, but may not match fully with the user’s needs and abilities (Brunner et al., 2010; Murguialday et al., 2010; Treder and Blankertz, 2010). Furthermore, for such overt ERP BCI paradigms the learning effect is generally small and average performance is high and consistent over subsequent trials. However, recently Klobassa et al. (2009) showed that for their auditory P3 paradigm the performance increased signiﬁcantly after 11 sessions. With subjects performing only up to two sessions, such an increase was not observed here. However, with more training the percentage of people able to use the setup could increase.

As shown in (Carlile et al., 1997), most front–back errors occur for locations within 30˚ of the median plane. Unfortunately, the before mentioned speakers in this study fall exactly within this range, which introduces a tertiary source for the found confusion.

A simple remedy could be to restrict all speakers to the frontal half, as done ofﬂine before (Schreuder et al., 2010; Belitski et al., 2011). When strictly adhering to the azimuth plane, this leads to a decreased angle between neighboring speakers. For a large number of classes it would be an interesting extension to use the vertical plane as an additional dimension to sustain the number of classes without compromising the spatial resolution of human hearing (Grantham et al., 2003). This is however not without

caveats itself, as up–down localization may suffer from similar problems as front–back localization.

### DYNAMIC STOPPING METHOD

Increase in performance due to any dynamic stopping method is promising but largely neglected in literature. Though several methods have been introduced before (Serby et al.,2005; Lenhardt et al., 2008; Zhang et al., 2008; Liu et al., 2010), they seldom ﬁnd their way into online studies other than for the purpose of validating the methods themselves. With an early decision in 41% of all trials and a false positive rate of 5%, we succeeded in constructingaconservativeyeteffectivemethodfordynamicstopping. The method is loosely based on Lenhardt et al. (2008). However, instead of one global threshold, subject- and iteration-speciﬁc thresholds are used. By taking a relative conﬁdence measure (p), the method is robust against biases. The results show again that dynamic stopping can signiﬁcantly increase performance.

Performance in traditional visual ERP application is generally good even at a low number of iterations. However,things get more difﬁcult when overt attention is impossible (Brunner et al., 2010; Treder and Blankertz,2010),where performance breaks down and a quality check as provided by a dynamic stopping method may be desirable. The same can be said for auditory paradigms, where covert attention is the standard and the resulting ERPs are less strong. Dynamic stopping methods should thus ﬁnd their way into BCI research and applications.

Here a decision is enforced after 15 iterations,but an additional beneﬁt of dynamic stopping methods could be to refrain from any decision if no threshold is surpassed. It might prove useful to allow for trials were no decisions is made, to implement a nocontrol state or to simply refrain from taking uncertain decisions. This could be particularly useful in long-term use of a system, where at times the user may be in a no-control state (Huggins et al., 2011).

### TOWARD A PURELY AUDITORY MODALITY

Most auditory BCI spellers described in literature depend to a certain extend on the visual modality for presenting a helping matrix(Furdeaetal.,2009;Klobassaetal.,2009;Kübleretal.,2009; Höhne et al., 2010; Belitski et al., 2011) to the user. By designing an intuitive interface, presentations of such a (static) matrix was not necessary in the current study. Users could easily learn the required steps for writing a letter. Sentence 1 and 2b were written without any visual feedback other than the writing progress. Although this requires some additional time to present to the user his current position in the spelling tree, it represents a new step toward a purely auditory BCI. Though not presented here, it is worth noting that the system has been used successfully by a blind collaboratortospellasentence,usingexclusivelytheauditorycues.

Of course, a completely auditory BCI is not always required. Residual eye control may not sufﬁce for a visual BCI, but could be good enough for presenting a static matrix. Furthermore, there are cases imaginable where auditory stimulation may be preferable over visual ones even when the visual modality is in tact. For instance, auditory stimuli may be easier to ignore and less intrusive when the user is engaged in a (primary) visual task such as reading.

In a recent study it was shown that auditory distraction has no effect on BCI systems based on mental tasks Friedrich et al. (2011). It is not clear if this holds true for auditory ERP BCI systems, as interaction in the same modality occurs. The level of distraction could depend on the relative loudness and the user’s ability to concentrate. That this is not necessarily a problem became obvious when subject VPkw helped us out in a demonstration for the local television. She performed a near-perfect spelling session, whilst TV cameras were being set up in the room and the crew was talking.

Though not explicitly tested here,the current setup with added pitch cues may be particularly suited for patients that are practiced musicians, as their improved tone hearing can increase the beneﬁt from these pitch cues (Micheyl et al., 2006).

### FUTURE RECOMMENDATIONS

Although the AMUSE paradigm was now embedded in a speller system, it may proof useful in other domains. For instance, the speaker distribution on the azimuth plane could provide a user with an intuitive set of commands for spatial navigation. Also, by including secondary ERP signals such as the ErrP (Schalk et al., 2000; Schmidt et al., 2011) for post hoc analysis of a decision, the system could be expected to increase in usability.

The SOA of 175ms used in this study was not optimized. Any SOA represents a trade-off between single-subtrial SNR and the number of repetitions needed. On the one hand, each subtrial is expected to contribute more class-discriminant information with a longer SOA. This can be explained by changed average amplitudes of target components, e.g., increased target P3 and N2, due to larger target-to-target distances (Gonsalvez and Polich, 2002; Allison and Pineda, 2006) and longer inter-stimulus intervals (Polich et al., 1991). But even other non-target ERPs can have an inﬂuence on the classiﬁcation accuracy, e.g., the sensitivity of N1 and P2 to SOA and target-to-target distances (Budd et al., 1998; Allison and Pineda, 2006). On the other hand, the BCI system agglomerates evidence over time by repeated presentation of the stimuli. With a fast SOA, more repetitions can be performed within the same time, which compensates for the lower information content in each individual subtrial. Due to increased overlap in fast paradigms, this interaction has to be considered carefully. As the best SOA value is probably subject dependent, an individualization for patients or other long-term users seems advisable.

Investigations of the basic ERP characteristics of ALS patients report a decrease of amplitude not only for the P3(a) (Silvoni et al., 2009)component,butalsofortheN1andMMN(N2)components (Raggi et al., 2008) in auditory and visual oddball paradigms. An increase of P3 latency has also been described (Hanagasi et al., 2002;Paulusetal.,2002),evenindirectcorrelationwithALSseverityandmonthsfromdiseaseonset(Raggietal.,2008).Still,reports on ERP based BCI systems for patients are encouraging. Silvoni et al. (2009) found no correlation between clinical data and BCI performance for 21 early and mid-stage ALS patients in an auditory ERP BCI, even though the P3 amplitude was reduced when compared to healthy controls. Furthermore, several applications for ALS patients have been published that show the feasibility of visual and auditory ERP paradigms (Sellers and Donchin, 2006;

Nijboer et al., 2008b). The question if ERP paradigms are suited for late stage ALS patients still remains open.

Recently an alternative auditory method was introduced,called PASS2D (Höhne et al., 2011), which is based on (Schreuder et al., 2010). Instead of using a free-ﬁeld setup, a headphone setup was tested using cues differing in two dimensions (tone and location). The PASS2D and AMUSE paradigm have similarly high performances, which are competitive with state-of-the-art visual, covert attention BCIs. They furthermore complement each other in several interesting aspects. A headphone setup is portable, small, and requires very little alteration to the home environment. It may be better suited for mobile user. On the downside, headphones may lead to social exclusion as the user might have limited perception of environmental sounds. The AMUSE paradigm is less mobile and requires an initial mechanical setup to position the speakers around the user. However, no social exclusion occurs, as the user can perceive stimuli and environmental sound at the same time. As end-users might be relatively immobile, the choice between AMUSE and PASS2D depends on the user’s liking.

In conclusion,the AMUSE paradigm complements the current visual BCI systems with a realistic and high performing alternative. The majority of users can successfully control the system

and concrete steps of improvement have been offered. Furthermore, a method for dynamic trial stopping was introduced, which signiﬁcantly increased performance.

## ACKNOWLEDGMENTS

The authors would like to thank Thomas Denck, David List and Larissa Queda for their help with performing the experiments. Furthermore, they thank Klaus-Robert Müller and Benjamin Blankertz for their fruitful discussions on the methodology. This work was partly supported by the European Information and Communication Technologies (ICT) Programme Project FP7224631 and 216886,by grants of the Deutsche Forschungsgemeinschaft (DFG; MU 987/3-2) and Bundesministerium fur Bildung und Forschung (BMBF; FKZ 01IB001A, 01GQ0850) and by the FP7-ICT Programme of the European Community, under the PASCAL2 Network of Excellence, ICT-216886. This publication only reﬂects the authors’views. Funding agencies are not liable for any use that may be made of the information contained herein.

## SUPPLEMENTARY MATERIAL

The Data Sheet 1 andVideo 1 for this article can be found online at http://www.frontiersin.org/neuroprosthetics/10.3389/fnins.2011. 00112/abstract

## REFERENCES

Acqualagna,L.,Treder,M. S.,Schreuder, M.,andBlankertz,B.(2010).Anovel brain-computer interface based on the rapid serial visual presentation paradigm. Conf. Proc. IEEE Eng. Med. Biol. Soc. 1, 2686–2689.

Allison, B. Z., and Pineda, J. A. (2006). Effects of SOA and ﬂash pattern manipulations on ERPs, performance, and preference: implications for a BCI system. Int. J. Psychophysiol. 59, 127–140.

Belitski, A., Farquhar, J., and Desain, P.

(2011). P300 audio-visual speller. J. Neural Eng. 8, 025022.

Blankertz, B., Dornhege, G., Krauledat,M.,Schröder,M.,Williamson,J., Murray-Smith, R., and Müller, K.-R. (2006). “The Berlin brain-computer interface presents the novel mental typewriter Hex-o-Spell,” in Proceedings of the 3rd International BrainComputer Interface Workshop and Training Course 2006 (Graz: Verlag der Technischen Universität Graz), 108–109.

Blankertz, B., Lemm, S., Treder, M. S., Haufe, S., and Müller, K.-R. (2011). Single-trial analysis and classiﬁcation of ERP components – a tutorial. Neuroimage 56, 814–825.

Blankertz, B., Tangermann, M., Vidaurre, C., Fazli, S., Sannelli, C., Haufe, S., Maeder, C., Ramsey, L. E., Sturm, I., Curio, G., and Müller, K.-R. (2010). The Berlin brain-computer interface: non-medical uses of BCI technology. Front. Neurosci. 4:198. doi: 10.3389/fnins.2010.00198

Blauert, J. (1983). Spatial Hearing: The Psychophysics of Human Sound Localization. Cambridge, MA: MIT Press.

Brainard, D. H. (1997). The psychophysics toolbox. Spat. Vis. 10, 433–436.

Brouwer, A.-M., and van Erp, J. B. F. (2010). A tactile P300 braincomputer interface. Front. Neurosci. 4:19. doi: 10.3389/fnins.2010.00019

Brunner, P., Joshi, S., Briskin, S., Wolpaw, J. R., Bischof, H., and Schalk, G. (2010). Does the “P300” speller depend on eye gaze? J. Neural Eng. 7, 056013.

Budd, T. W., Barry, R. J., Gordon, E., Rennie, C., and Michie, P. T. (1998). Decrementof theN1auditoryeventrelated potential with stimulus repetition: habituation vs. refractoriness. Int. J. Psychophysiol. 31, 51–68.

Carlile, S., Leong, P., and Hyams, S. (1997). The nature and distribution of errors in sound localization by human listeners. Hear. Res. 114, 179–196.

Cedarbaum, J. M., Stambler, N., Malta, E., Fuller, C., Hilt, D., Thurmond, B., and Nakanishi, A. (1999). The ALSFRS-R: a revised als functional rating scale that incorporates assessments of respiratory function. J. Neurol. Sci. 169, 13–21.

Cincotti, F., Kauhanen, L., Aloise, F., Palomäki, T., Caporusso, N., Jylänki, P., Mattia, D., Babiloni, F., Vanacker, G., Nuttin, M., Marciani, M. G., and Millán, J. R. (2007). Vibrotactile feedback for brain-computer

interface operation. Intell. Neurosci. 2007, 12.

Farwell, L., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523.

Fozard,J.,andGordon-Salant,S.(2001). Handbook of the Psychology of Aging, Chapter Changes in Vision and Hearing with Aging, 5th Edn. San Diego, CA: Academic Press, 241–266

Friedrich, E. V., Scherer, R., Sonnleitner, K., and Neuper, C. (2011). Impact of auditory distraction on user performance in a brain-computer interface driven by different mental tasks. Clin. Neurophysiol. 122, 2003–2009.

Furdea, A., Halder, S., Krusienski, D. J., Bross, D., Nijboer, F., Birbaumer, N., and Kübler, A. (2009). An auditory oddball (P300) spelling system for brain-computer interfaces. Psychophysiology 46, 617–625.

Gonsalvez, C., and Polich, J. (2002). P300 amplitude is determined by target-to-target interval. Psychophysiology 39, 388–396.

Gonsalvez, C. J., Barry, R. J., Rushby, J. A., and Polich, J. (2007). Target-totarget interval, intensity, and P300 from an auditory single-stimulus task. Psychophysiology 44, 245–250.

Grantham,D.W.,Hornsby,B.W.Y.,and Erpenbeck, E. A. (2003). Auditory spatial resolution in horizontal, vertical, and diagonal planes. J. Acoust. Soc. Am. 114, 1009–1022.

Guger,C.,Daban,S.,Sellers,E.,Holzner, C., Krausz, G., Carabalona, R., Gramatica, F., and Edlinger, G. (2009). How many people are able to control a P300-based braincomputer interface (BCI)? Neurosci. Lett. 462, 94–98.

Guo, J., Gao, S., and Hong, B. (2010). An auditory brain-computer interface using active mental response. IEEETrans.NeuralSyst.Rehabil.Eng. 18, 230–235.

Halder, S., Rea, M., Andreoni, R., Nijboer, F., Hammer, E. M., Kleih, S. C., Birbaumer, N., and Kübler, A. (2010). An auditory oddball brain-computer interface for binary choices. Clin. Neurophysiol. 121, 516–523.

Hanagasi, H. A., Gurvit, I. H., Ermutlu, N., Kaptanoglu, G., Karamursel, S., Idrisoglu, H. A., Emre, M., and Demiralp, T. (2002). Cognitive impairment in amyotrophic lateral sclerosis: evidence from neuropsychological investigation and eventrelated potentials. Brain Res. Cogn. Brain Res. 14, 234–244.

Hill,N.,Lal,T.,Bierig,K.,Birbaumer,N., and Schölkopf, B. (2005). “An auditory paradigm for brain–computer interfaces,” in Advances in Neural Information Processing Systems, Vol. 17, eds L. K. Saul, Y. Weiss, and L. Bottou (Cambridge, MA: MIT Press), 569–576.

Hinterberger, T., Neumann, N., Pham, M., Kübler, A., Grether, A., Hofmayer, N., Wilhelm, B., Flor, H., and Birbaumer,N.(2004).Amultimodal

brain-based feedback and communication system. Exp. Brain Res. 154, 521–526.

Höhne, J., Schreuder, M., Blankertz, B., and Tangermann, M. (2010). Twodimensional auditory P300 speller with predictive text system. Conf. Proc. IEEE Eng. Med. Biol. Soc. 1, 4185–4188.

Höhne, J., Schreuder, M., Blankertz, B., and Tangermann, M. (2011). A novel 9-class auditory erp paradigm driving a predictive text entry system. Front. Neurosci. 5:99. doi: 10.3389/fnins.2011.00099

Huggins, J. E., Wren, P. A., and Gruis, K. L. (2011). What would braincomputer interface users want? opinions and priorities of potential users with amyotrophic lateral sclerosis. Amyotroph. Lateral Scler. doi: 10.3109/17482968. 2011.572978. [Epub ahead of print].

Kanoh, S., Miyamoto, K., and Yoshinobu, T. (2008). A brain-computer interface (BCI) system based on auditory stream segregation. Conf. Proc. IEEE Eng. Med. Biol. Soc. 642–645. doi: 10.1109/IEMBS.2008. 4649234

Kim, D.-W., Hwang, H.-J., Lim, J.-H., Lee, Y.-H., Jung, K.-Y., and Im, C.H. (2011). Classiﬁcation of selective attention to auditory stimuli: toward vision-free brain-computer interfacing.J.Neurosci.Methods 197, 180–185.

Klobassa, D. S., Vaughan, T. M., Brunner,P.,Schwartz,N. E.,Wolpaw,J. R., Neuper,C.,and Sellers,E.W. (2009). Toward a high-throughput auditory P300-based brain-computer interface. Clin. Neurophysiol. 120, 1252–1261.

Krusienski, D. J., Sellers, E. W., Cabestaing, F., Bayoudh, S., McFarland, D. J., Vaughan, T. M., and Wolpaw, J. R. (2006). A comparison of classiﬁcation techniques for the P300 speller. J. Neural Eng. 3, 299–305.

Kübler, A., Furdea, A., Halder, S., Hammer, E. M., Nijboer, F., and Kotchoubey, B. (2009). A braincomputer interface controlled auditory event-related potential (p300) spelling system for locked-in patients. Ann. N. Y. Acad. Sci. 1157, 90–100.

Langendijk, E. H. A., and Bronkhorst, A. W. (2002). Contribution of spectral cues to human sound localization. J. Acoust. Soc. Am. 112, 1583–1596.

Ledoit, O., and Wolf, M. (2004). A wellconditioned estimator for largedimensional covariance matrices. J. Multivar. Anal. 88, 365–411.

Lenhardt, A., Kaper, M., and Ritter, H. (2008). An adaptive P300based online brain-computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 16, 121–130.

Liu, T., Goldberg, L., Gao, S., and Hong, B.(2010).Anonlinebrain-computer interface using non-ﬂashing visual evoked potentials. J. Neural Eng. 7, 036003.

Liu, Y., Zhou, Z., and Hu, D. (2011). Gaze independent braincomputer speller with covert visual search tasks. Clin. Neurophysiol. 122, 1127–1136.

Micheyl, C., Delhommeau, K., Perrot, X.,andOxenham,A.J.(2006).Inﬂuence of musical and psychoacoustical training on pitch discrimination. Hear. Res. 219, 36–47.

Middlebrooks, J. C., and Green, D. M. (1991). Sound localization by human listeners. Annu. Rev. Psychol. 42, 135–159.

Münssinger, J. I., Halder, S., Kleih, S. C., Furdea, A., Raco, V., Hösle, A., and Kübler, A. (2010). Brain painting: ﬁrst evaluation of a new brain-computer interface application with ALS patients and healthy volunteers. Front. Neurosci. 4:182. doi: 10.3389/fnins.2010. 00182

Murguialday, A. R., Hill, J., Bensch, M., Martens, S., Halder, S., Nijboer, F., Schölkopf, B., Birbaumer, N., and Gharabaghi, A. (2010). Transition from the locked in to the completely locked-in state: a physiological analysis. Clin. Neurophysiol. 122, 925–933.

Nijboer, F., Furdea, A., Gunst, I., Mellinger, J., McFarland, D., Birbaumer, N., and Kübler, A. (2008a). An auditory brain-computer interface (BCI). J. Neurosci. Methods 167, 43–50.

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., Halder,S.,Mochty,U.,Krusienski,D. J.,Vaughan,T. M.,Wolpaw,J. R.,Birbaumer, N., and Kübler, A. (2008b). A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916.

Nijholt, A., Bos, D. P.-O., and Reuderink, B. (2009). Turning shortcomingsintochallenges:brain-computer interfaces for games. Entertainment Comput. 1, 85–94.

Paulus, K. S., Magnano, I., Piras, M. R., Solinas, M. A., Solinas, G., Sau, G. D., and Aiello, I. (2002). Visual and auditory event-related potentials in sporadic amyotrophic lateral sclerosis. Clin. Neurophysiol. 113, 853–861.

Polich, J., Brock, T., and Geisler, M. W. (1991). P300 from auditory and somatosensory stimuli: probability and inter-stimulus interval. Int. J. Psychophysiol. 11, 219–223.

Raggi, A., Consonni, M., Iannaccone, S., Perani, D., Zamboni, M., Sferrazza, B., and Cappa, S. F. (2008). Auditory event-related potentials in non-demented patients with sporadic amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 342–350. Schalk, G.,Wolpaw, J. R., McFarland, D. J., and Pfurtscheller G. (2000). EEGbased communication: presence of an error potential. Clin. Neurophysiol. 111, 2138–2144.

Schlögl, A., Kronegg, J., Huggins, J., and Mason, S. G. (2007). “Evaluation criteria for BCI research,” in TowardsBrain-ComputerInterfacing, eds G. Dornhege, R. del, J. Millán, T. Hinterberger, D. McFarland, and K.-R. Müller (Cambridge, MA: MIT press), 297–312.

Schmidt, N., Blankertz, B., and Treder, M. S. (2011). Online detection of error potentials increases information throughput in a braincomputer interface. Neurosci. Lett. 500(Suppl.), e19–e20.

Schreuder, M., Blankertz, B., and Tangermann, M. (2010). A new auditory multi-class braincomputer interface paradigm: spatial hearing as an informative cue. PLoS ONE 5, e9813. doi: 10.1371/journal.pone.0009813

Schreuder, M., Tangermann, M., and Blankertz, B. (2009). Initial results of a high-speed spatial auditory BCI. Int. J. Bioelectromagn. 11, 105–109.

Schröder, M., and Trouvain, J. (2003). The German text-to-speech synthesis system MARY: a tool for research, development and teaching. Int. J. Speech Tech. 6, 365–377.

Sellers, E. W., and Donchin, E. (2006). A P300-based brain-computer interface: initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548. Sellers, E. W.,Vaughan, T. M., and Wolpaw, J. R. (2010). A brain-computer interface for long-term independent home use. Amyotroph. Lateral Scler. 11, 449–455.

Serby, H., Yom-Tov, E., and Inbar, G. (2005). An improved P300-based brain-computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 13, 89–98.

Silvoni, S., Volpato, C., Cavinato, M., Marchetti, M., Priftis, K., Merico, A., Tonin, P., Koutsikos, K., Beverina, F., and Piccione, F. (2009). P300-based brain-computer interface communication:evaluation and follow-up in amyotrophic lateral

sclerosis. Front. Neurosci. 3:60. doi: 10.3389/neuro.20.001.2009

Tangermann, M., Krauledat, M., Grzeska, K., Sagebaum, M., Blankertz, B., Vidaurre, C., and Müller, K.-R. (2009). “Playing pinball with non-invasive BCI,” in Advances in Neural Information Processing Systems, eds D. Koller, D. Schuurmans, Y. Bengio, and L. Bottou (Cambridge, MA: MIT Press), 1641–1648.

Treder, M. S., and Blankertz, B. (2010). (C)overt attention and visual speller design in an ERP-based braincomputer interface. Behav. Brain Funct. 6, 28.

Treder, M. S., Schmidt, N. M., and Blankertz, B. (2011). Gazeindependent brain-computer interfaces based on covert attention and feature attention. J. Neural Eng. (in press).

Vlek, R., Schaefer, R., Gielen, C., Farquhar, J., and Desain, P. (2011). Sequenced subjective accents for brain-computer interfaces. J. Neural Eng. 8, 036002.

Wightman, F., and Kistler, D. (1999). Resolution of front-back ambiguity in spatial hearing by listener and sourcemovement.J.Acoust.Soc.Am. 105, 2841.

Zhang, H., Guan, C., and Wang, C. (2008). Asynchronous P300-based brain-computer interfaces: a computational approach with statistical models.IEEETrans.Biomed.Eng.55, 1754–1763.

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 20 May 2011; accepted: 01 September 2011; published online: 14 October 2011. Citation: Schreuder M, Rost T and Tangermann M (2011) Listen, you are writing! Speeding up online spelling with adynamicauditoryBCI.Front.Neurosci. 5:112. doi: 10.3389/fnins.2011.00112 This article was submitted to Frontiers in Neuroprosthetics, a specialty of Frontiers in Neuroscience. Copyright © 2011 Schreuder, Rost and Tangermann. This is an open-access article subject to a non-exclusive license between the authors and Frontiers Media SA, which permits use, distribution and reproduction in other forums, provided the original authors and source are credited and other Frontiers conditions are complied with.

