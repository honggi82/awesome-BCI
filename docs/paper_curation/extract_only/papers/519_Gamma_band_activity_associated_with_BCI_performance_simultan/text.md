#### ORIGINAL RESEARCH ARTICLE

published: 06 December 2013 doi: 10.3389/fnhum.2013.00848

# Gamma band activity associated with BCI performance: simultaneous MEG/EEG study

## Minkyu Ahn1, Sangtae Ahn1, Jun H. Hong1, Hohyun Cho1, Kiwoong Kim2, Bong S. Kim3, JinW. Chang3 and Sung C. Jun1,4*

- 1 School of Information and Communications, Gwangju Institute of Science andTechnology, Gwangju, South Korea
- 2 Korea Research Institute of Standards and Science, Daejeon, South Korea
- 3 Department of Neurosurgery, Brain Research Institute,Yonsei University College of Medicine, Seoul, South Korea
- 4 Wadsworth Center, NewYork State Health Department, Albany, NY, USA

Edited by: Markus Butz, University College London, UK

Reviewed by: Karim Jerbi, Institut National de la Santé et de la Recherche Médicale, France Moritz Grosse-Wentrup, Max Planck Institute for Biological Cybernetics, Germany

*Correspondence: Sung C. Jun, School of Information and Communications, Gwangju Institute of Science andTechnology, 1 Oryong-dong, Buk-gu, Gwangju 500-712, South Korea e-mail: scjun@gist.ac.kr

While brain computer interface (BCI) can be employed with patients and healthy subjects there are problems that must be resolved before BCI can be useful to the public. In the mos popular motor imagery (MI) BCI system, a signiﬁcant number of target users (called “BCI Illiterates”) cannot modulate their neuronal signals sufﬁciently to use the BCI system.Thi causes performance variability among subjects and even among sessions within a subject The mechanism of such BCI-Illiteracy and possible solutions still remain to be determined Gamma oscillation is known to be involved in various fundamental brain functions, and ma play a role in MI. In this study, we investigated the association of gamma activity with M performance among subjects.Ten simultaneous MEG/EEG experiments were conducted MI performance for each was estimated by EEG data, and the gamma activity associate with BCI performance was investigated with MEG data. Our results showed that gamm activity had a high positive correlation with MI performance in the prefrontal area. Thi trend was also found across sessions within one subject. In conclusion, gamma rhythm generated in the prefrontal area appear to play a critical role in BCI performance.

, t -

s . .

y I ;

d a s s

Keywords: BCI-illiteracy, motor imagery BCI, performance prediction, gamma activity, MEG, EEG

## INTRODUCTION

Over the past several decades, considerable attention has been paid to the subject of brain computer interface (BCI) technology (Wolpaw etal., 2002), as it is an attractive notion that BCI can translate a user’s intention or mental state through brain waves. From the early days of this research until now, and especially in recent decades, BCI has been improved and its accuracy has been much enhanced with the help of machine learning algorithms. For control use, motor imagery (MI)-based BCI has been one of the most popular designs, such as P300 and steady state visual evoked potential (SSVEP) BCIs (Bashashati etal., 2007; Guger etal., 2011). Pfurtscheller and Lopes da Silva (1999) observed that mu-rhythms over sensorimotor areas involved with motor function are attenuated notably when a person imagines body part movement. Brain signal patterns associated with this phenomenon are extracted commonly for the purpose of controlling the system.

The investigations and development of this technology have been conducted in non-invasive (Wolpaw etal., 2002; Blankertz etal., 2006, 2008a; Jerbi etal., 2011; Ortner etal., 2012) as well as invasive systems (Leuthardt etal., 2004; Jerbi etal., 2009). Recent studies have reported success in decoding the direction of movement(Mehringetal.,2004; Rickertetal.,2005;Waldertetal.,2008,

- 2009; Ball etal., 2009), target (Hammon etal., 2008; Ubeda etal., 2013), velocity (Bradberry etal., 2009; Lv etal., 2010; Ofner and Müller-Putz, 2012; Robinson etal., 2013), trajectory (Schalk etal., 2007), grasp type (Pistohl etal., 2012) and real-time detection of visuo-spatial working memory (Hamamé etal., 2012).

It is expected that these successes may soon be applied to BCI and allow public marketing. However, obstacles that need to be resolved still exist, even in accurate BCI systems; a crucial hurdle is that BCI performance varies signiﬁcantly across and even within users. Reportedly, approximately 20–30% of target users do not generate controllable brain signals (extractable and classiﬁable by existing techniques) in MI (Guger etal., 2003; Blankertz etal., 2008b; Ahn etal., 2013). Such problems exist commonly in other current BCI systems and must be overcome before BCI technology can advance further. Even though one shows good decoding accuracy during the calibration phase, it may yield poor performance in the online phase; alternatively, although one may be able to control a BCI system at one time, a loss of control may occur at another time. This indicates that performance variation is observed not only across people, but also at different times within subjects. Therefore, understanding why this problem occurs and investigation of its causes/correlates are important in making BCI a usable interface.

In recent studies, efforts to ﬁnd correlates with BCI performance have yielded interesting outcomes. Blankertz etal. (2010) reported the importance of idling alpha activity in the motor cortex, which is associated implicitly with a potential decrease of power below baseline. They observed that subjects with high alpha levels during the resting state are likely to have great potential to yield larger power decreases, which can be used as a main feature for MI BCI. Further, Ahn etal. (2013) found that high alpha and low theta is a typical pattern among those who perform MI BCI well. These ﬁndings are highly beneﬁcial in establishing applicable

- Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 1

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 1 — #1

BCIsystemsinbothhealthyandillusers. Itispossibletopre-screen usersof theBCIsystem,andthosewhodemonstratepoorBCIperformance may be trained through biofeedback before actual BCI use (Hwang etal., 2009). Even users themselves may decide without difﬁculty to choose other interfaces or BCI control paradigms that are better suited for them (Volosyak etal., 2010).

Another noteworthy factor is psychological state. It has been reported that motivation (Leeb etal., 2007; Hammer etal., 2012) and mindfulness (Mahmoudi and Erfanian, 2006; Lakey etal., 2011) inﬂuence BCI performance. In an intensive study with 83 subjects, the ability for visuo-motor coordination and concentrationonataskwasrevealedtohaveasigniﬁcantpositivecorrelation with classiﬁcation accuracy of MI (Hammer etal., 2012). Nijboer etal. (2010) concluded that motivational factors may be related to performance in patients with amyotrophic lateral sclerosis (ALS). Fear of the BCI system has also been suggested as a factor that degrades performance (Burde and Blankertz, 2006; Nijboer etal.,

- 2010; Kleih etal., 2013; Witte etal., 2013). Burde and Blankertz

(2006) reported that highly conﬁdent subjects are likely to show better control in MI BCI.

Performance variability is observed not only between, but also within users. Usually, BCI performance is estimated by means of hit-trials in online cases and average accuracy through crossvalidationinofﬂineanalysis. However,subjectsmayyielddifferent performance over runs, even within the same experiment. Performance may ﬂuctuate considerably when a user is tested over a period of days, as environment and mental states vary over time. Moreover, this variability may occur even within seconds across trials. Grosse-Wentrup etal. (2011) tried to explain the trial-wise variability in relation to the gamma (55–85 Hz) rhythm. They reported that the causal effect of gamma on sensory motor rhythm (SMR) was induced through the framework of causal inﬂuence (Pearl, 2000; Spirtes etal., 2001). The empirical results of Grosse-Wentrup etal. (2011) revealed that gamma activity in the fronto-parietal network played a critical role in the MI process. Frontal gamma may affect MI ability because high frequency oscillations reﬂect attention and cognitive processes (Uhlhaas etal., 2009). Therefore, it has been inferred that the level of a user’s concentration has some effect on the process of imagining body movement. Conversely, increases in gamma power in corresponding areas during MI have also been reported (Pfurtscheller and Lopes da Silva,1999). In an invasive study, further support for this gamma increase was obtained in the electrocorticogram (ECoG) work of Aoki etal. (1999). They found a power decrease in the 11–20 Hz range and an increase in the 31–60 Hz range in the forearm sensorimotor cortex during performance of visuo-motor tasks. As the hypothesis that gamma reﬂects functions in a speciﬁc brain area with highly precise synchronization in local networks (Fries etal., 2007; Womelsdorf etal., 2007), Halder etal. (2011) found in an fMRI study that the number of activated voxels in the supplementary motor area (SMA) was larger for users with relatively higher MI ability. Therefore, it is evident that gamma increases on SMA reﬂect a larger ensemble of neurons for certain types of processing (Jensen etal., 2007). In a trial-wise manner, Grosse-Wentrup etal. (2011) also reported a weak negative correlation between centro-parietal gamma oscillation and trial-wise SMR quality scores, which are the magnitude of output from a

classiﬁer, such as a support vector machine (SVM). This indicates thatthebrainstateinwhichtherearerelativelylowlevelsof gamma in the MI-related brain area during the resting state may facilitate the MI process because a high resting alpha rhythm is essential for good performance of MI BCI.

Summarizing these studies, two types of gamma originating from different brain areas seem to be important in MI:

- • Frontal gamma, which inﬂuences MI indirectly
- • Directly linked gamma, which increases in the centro-parietal area during MI

However, it remains unclear whether these gamma activities inﬂuence MI performance across or within subjects, or perhaps both. The inﬂuence of high frequencies (>30 Hz) above beta on MI performance has rarely been studied, although high frequency information is being investigated actively (Worrell etal., 2012). In particular, individual differences in gamma across subjects have neverbeeninvestigated,andonlyoneEEGstudy(Grosse-Wentrup etal., 2011) on trial-wise variability has been reported, although there have been some studies (Muthukumaraswamy etal., 2009, 2010) of visual gamma powers. In high frequency analyses, EEG has yielded reasonable results in some studies (Darvas etal., 2010; Grosse-Wentrup and Schölkopf, 2012); however, it is understood that EEG has low spatial resolution and volume conduction problems, especially in source reconstruction. For in-depth analysis of gamma activity, magnetoencephalography (MEG) is another choice; it has comparatively good temporal and relatively higher spatial resolution than EEG. For this reason, MEG facilitates the investigation of gamma, and thus has been introduced for MEGbased BCI (Lal etal., 2005; Mellinger etal., 2007; Buch etal., 2008; Battapadyetal.,2009; Bianchietal.,2010; Sudreetal.,2011; Zhang etal., 2011) and related work (Battapady etal., 2009; Bradberry etal., 2009; Ko and Jun, 2010; Wang etal., 2010; Hong and Jun, 2012; Chowdhury etal., 2013; Hong etal., 2013).

The purpose of this study was to identify individual differences in gamma activity and the extent of their inﬂuence on MI performance across subjects. For this purpose,a total of ten simultaneous MEG and EEG datasets were recorded from ten subjects. First, the MI classiﬁcation accuracy of each subject was evaluated by EEG and the resting state of MEG was used for correlation analysis between gamma activity and BCI performance. Simultaneous MEG/EEG acquisition and methods are explained in Section“Materials and Methods.”Results are presented in Section “Results.”Finally,furtherinterpretationsandpossibleapplications are discussed in Section“Discussion.”

## MATERIALS AND METHODS

### SUBJECTS

Ten subjects (ages: 25.3 ± 2.0 years old; 8 males, 2 females) participated in this study. The experiment was approved by the Institutional Review Board of Gwangju Institute of Science and Technology. All subjects were informed of the experimental process and purpose, and written consent letters were collected from them before the experiment.

### SIMULTANEOUS MEG/EEG DATA ACQUISITION

All experiments were conducted with MEG in a magnetically and electrically shielded room developed by Korea Research Institute

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 2

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 2 — #2

of Standards and Science in South Korea (152 channels axial gradiometer, sampling rate: 1 kHz or 512 Hz, notch ﬁltering at 60 Hz and bandpass ﬁltering with 0.1–100 Hz), Biosemi EEG (19 channels electrodes, sampling rate: 512 Hz) and Brain Products EEG (19 channels, sampling rate: 500 Hz, notch ﬁltering at 60 Hz) systems. EEG electrodes were attached to the entire scalp (Fp1, Fp2, F3, F4, C3, C4, P3, P4, O1, O2, F7, F8, T3, T4, T5, T6, Fz, Cz, Pz) according to the 10–20 international system. For three subjects (H, I and J), MEG/EEG was digitized at 1 kHz and downsampled to 500 Hz using the Brain Products EEG system. Signals were recorded in two different states, the resting state, which is recorded at the beginning of the experiment, and the mental state while performing MI. Here, MEG and EEG were also recorded simultaneously, but EEG was used only to estimate the performance of MI BCI. In general, EEG has been used most often for BCI due to its portability and low cost; thus, BCI performance estimated by EEG alone is more realistic than that estimated by MEG alone or both MEG/EEG.

### RESTING STATE

Subjects were seated in a comfortable armchair and instructions were projected onto a screen approximately 80 cm away. The resting state signal was acquired before the MI task. This resting state acquisition lasted 60 s, while the subjects did nothing but let their minds wander with eyes open.

### MI TASK

A conventional left and right hand imagery movement task was introduced to estimate each subject’s MI ability. Each subject conducted three runs during this task. One run consisted of twenty trials for each class (left or right hand movement imagination),for a total of forty trials. A trial began with a gray ﬁxation cross on a blackbackground. Subjectswereaskedtomovetheireyesaslittleas possible during each trial. Either a left or right arrow appeared on the gray ﬁxation cross after 2 s of preparation. The MI phase began with the appearance of a randomly selected directional arrow, and subjects were instructed to imagine their hand movement, such as making a ﬁst with the left or right hand according to the arrow until it disappeared. The MI phase lasted 3 s for each trial. Afterward, the screen went blank and subjects were allowed to relax for 2 s. A randomized interval of 0–2 s was allocated between consecutive (randomly chosen right or left) trials to avoid subjects’ adaptation. Figure 1 illustrates one trial of this MI experiment. A total of 120 trials were collected during the experiments.

of trials; for each iteration, 10 groups were divided randomly into 7 (training data) and 3 groups (testing data), respectively. The number of cases required to choose 7 out of 10 groups is 120; for each case, a classiﬁer was constructed from the training data, and testing data were evaluated to yield a hit-rate (%). The common spatial pattern (CSP; Ramoser etal., 2000) was applied to these training data and 10 CSP spatial ﬁlters that best discriminated the two conditions were selected. These spatial ﬁlters projected each training trial into a new domain; ﬁnally, the variances of projected signals were used as features. A classiﬁer was generated by Fisher linear discriminant analysis (FLDA), which constructed classiﬁcation lines in the feature domain between two MI conditions. This classiﬁerwasappliedtotestingdataandyieldedclassiﬁcationaccuracy. Using the same procedure, 120 iterations were performed, thereby yielding 120 estimates of accuracy. The mean of these estimates was used as performance in the given window. As the window was sliding, the best performance time interval for each subject was determined and the best classiﬁcation accuracy was used as the subject’s MI accuracy. The time interval yielding the best results for each experiment is presented in Table 1.

### RESTING STATE MEG ANALYSIS

Before or during MEG recording, bad channels showing abnormal behavior were checked carefully; 10 among 152 channels were declared as bad channels and excluded from the analysis. MEG was bandpass-ﬁltered with frequencies between 1 and 100 Hz. FrequencypowerswerecalculatedthroughEEGLABlibrary(Delorme and Makeig, 2004). We adopted four spectral band ranges: theta (4–8 Hz); alpha (8–13 Hz); beta (13–30 Hz), and gamma (30– 70 Hz). The powers of these frequency intervals were summed and normalized by a total frequency power of 4–70 Hz and were dividedbythetotalpoweroverchannels. Thisfacilitatedourinvestigation across different channels and subjects without speciﬁc channel or band biases. We deﬁned this value as a relative power level (RPL) that was used primarily throughout this work.

## RESULTS

### MI PERFORMANCE

Figure 2 presents classiﬁcation accuracy estimated by the conventionalcross-validationmethoddescribedinSection“Classiﬁcation Accuracy From EEG.” Looking at the performance behaviors, ﬁve subjects (A, D, E, H, and J) showed reasonably moderate performance (accuracy > 70%) while the other ﬁve subjects (B, C, F,

|[Figure 1]<br><br>FIGURE 1 | One trial of MI task.|
|---|

### CLASSIFICATION ACCURACY FROM EEG

The MI trials acquired were used to quantify the subjects’ MI performance. As in previous studies (Ahn etal.,2012),each signal was bandpass-ﬁlteredwith8–30Hztoincludealphaandbetarhythms, as these bands are well known to contain very informative features that classify two different MI conditions (Pfurtscheller and Lopes da Silva, 1999; Ahn etal., 2012). Next, a temporally moving window with a window size of 2 s and sliding step of 100 ms were applied in order to calculate time variable classiﬁcation accuracy from onset. The classiﬁcation accuracy in each window was obtained through cross validation using 120 iterations, as follows: trials were separated into 10 groups containing an equal number

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 3

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 3 — #3

Table 1 | Experimental information.

Contents A B C D E F G H I J MEG

Number of channels 152 152 152 152 152 152 152 152 152 152 Sampling rate (Hz) 500 512 512 512 512 512 512 500 500 500 EEG

Number of channels 19 19 19 19 19 19 19 19 19 19 Sampling rate (Hz) 512 512 512 512 512 512 512 500 500 500 Start time of 2 s time window for best accuracy (s) 0.4 0.1 0.8 1 0.2 0.5 0.9 0.6 0.6 0.1

|[Figure 2]<br><br>FIGURE 2 | Classiﬁcation accuracy in EEG. Accuracy of each subject is presented with its standard deviation.|
|---|

|[Figure 3]<br><br>FIGURE 3 |Topographic images for MEG gamma. Images are sorted in descending order of MI performance with EEG.|
|---|

G, and I) yielded around chance level (50%) or slightly higher accuracy.

### SPATIAL DISTRIBUTION OF GAMMA ACTIVITY

Topographical distributions for gamma RPL over all experiments are illustrated in Figure 3 under the ﬁxed color bar scale. It is notable that most experiments yielding relatively better classiﬁcation accuracy had higher levels of gamma in the frontal area. Subject F also seemed to show a high gamma power level in the frontal area; however, high RPL distribution was spread out in the temporal area, and thus was not focused on the frontal mid-line.

### REGION ANALYSIS

To investigate spatial gamma effects on MI accuracy, we separated sensor areas into ﬁve regions along the midline from the frontal to occipital areas. Through the linear ﬁtting method and Pearson correlation analysis, we observed how averaged resting state gamma levels in each region and MI performance were correlated (Figure 4). For statistical validation, we used student t-tests for each comparison. In the prefrontal area, we found a highly positive correlation (r = 0.73), indicating that gamma level was related strongly to MI performance. Such a positive correlation continued until the frontal area, and then switched to a negative correlation after the central area, where it peaked in the occipital region (r = –0.21). Thus, we inferred

that frontal gamma may play an important role in MI; meanwhile, the central area was the border at which the relationship changed from a positive to a negative inﬂuence on MI performance. Finally, the negative role of gamma activity was maximized in the parietal area. However, looking at the significance level, the negative correlation after the central area was not as high as that of the prefrontal (p = 0.02) or frontal areas (p = 0.06).

### CORRELATION ANALYSES OF FOUR SPECTRAL BANDS

In the previous section, we found that resting frontal gamma may play a critical role with respect to the capacity for MI, while resting-state gamma power in the centro-occipital region may have a negative association. Such a pattern may affect other spectral rhythms in order to achieve an overall mental state suitable for MI. In this section, frequency band powers other than gamma were investigated using RPL, and these were compared with respect to classiﬁcation accuracy. For each channel, we conducted Pearson correlation analyses to achieve correlation values and statistical p-values from the student t-test. Next, a statistical p-value topographical distribution for each subject was FDR (false discovery rate)-corrected over all channels for multiple

- Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 4

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 4 — #4

|[Figure 4]<br><br>FIGURE 4 | Regional analysis of MEG gamma.The selected channels in each region are marked as shaded round squares and their mean gamma RPL is plotted against MI accuracy.The direction of the ﬁtted line and the correlation coefﬁcient changed from the prefrontal to occipital areas.|
|---|

comparison analysis (Benjamini and Hochberg, 1995; Genovese etal., 2002).

|[Figure 5]<br><br>FIGURE 5 |Topographical plot of correlation distribution between MI performance with EEG and MEG band power. MEG Gamma p-value is shown in the right-bottom; other bands were not statistically signiﬁcant with FDR-correction threshold (q = 0.1).The signiﬁcant threshold for p-values is shown with an arrow in the p-value color bar.|
|---|

Figure 5 describes the results of correlation analyses for four bands at rest; the ﬁndings are summarized as follows:

- • Gamma showed positive correlations near the front of the head and those increased in the frontal mid-line area, while other areas showed negative correlations. We inferred from this observation that the frontal midline may be an important point of origin for imagination processing in motor function.
- • Beta had a pattern similar to that of gamma; however, it was not focused to the same degree as gamma. Rather, its pattern spread out to cover broad areas.
- • Theta showed the reverse pattern to beta and gamma. Correlations near the prefrontal area were negative; theta became weakly positive from the frontal to occipital areas.
- • Alpha is known to be the most critical factor in the MI process (Blankertz etal., 2010), especially near the somaticmotor area. This was also observed in Figure 5 (Alpha). The correlation analysis revealed that alpha had positive correlations over all areas from the front to the back of the head.

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 5

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 5 — #5

features. Mellinger etal. (2007) recommended using Laplacian spatial ﬁltering rather than more sophisticated methods, such as independent component analysis (ICA), CSP and beamforming (Ahn etal.,2012), where accurate correction of channel location is not guaranteed. In our investigation,we also obtained better accuracy in some subjects by using a time-averaging feature without CSP ﬁltering and rejecting bad trials after examination. In addition, Dornhege etal. (2007) demonstrated that CSP and ICA in MEG could work more poorly than the approach without spatial ﬁltering, while those approaches could improve performance in EEG. In summary, spatial ﬁltering and channel mismatch may be critical factors in MEG processing.

|[Figure 6]<br><br>FIGURE 6 | Classiﬁcation accuracy in MEG. MEG accuracy of each subject is presented as a mean with a standard deviation, and for comparison, EEG accuracy is plotted as a small ﬁlled square (r = 0.91, p < 0.0005).|
|---|

### EEG GAMMA IN RESTING STATE

EEG gamma activity in the resting state was investigated in the same manner as MEG, as shown in Figure 3. The topographical images of EEG gamma activity for all subjects are illustrated in Figure 7. Due to the small number of EEG channels (N = 19), spatial resolution of the EEG image is considerably lower than that of MEG. Unlike MEG gamma in Figure 3, any noticeable tendency and statistically signiﬁcant correlation between resting state gamma and MI performance were not observed in the frontal or centro-occipital areas (p > 0.1) in EEG. This result shows that MEG has an advantage over EEG in the investigation of gamma activity. However, this may be due to the speciﬁcity of our analysis or the equipment we used here (19 EEG channels).

## DISCUSSION

### MI PERFORMANCE IN MEG

In this work, MI performance was evaluated by EEG because EEG is used more commonly than MEG in the BCI system. However, it is understood that, in general, the MEG signal seems to have a relatively higher signal-to-noise ratio than EEG; thus, it would be quite interesting to see if MEG yields better results than EEG in MI BCI. We investigated MI performance with MEG brieﬂy in a manner similar to EEG. Classiﬁcation accuracy was estimated through cross-validation as described in Section “Classiﬁcation Accuracy From EEG.” The same temporal/spectral ﬁltering processingasthoseinEEGandfurtherchannelselectionwereapplied. Next, the best classiﬁcation accuracy of MEG was chosen. As a result, MEG yielded 64.8 ± 7.9 in classiﬁcation accuracy, which is slightly inferior to and almost comparable to EEG performance (66.4 ± 9.4). Detailed performances for each subject are depicted in Figure 6. Both MEG and EEG performance distributions are correlated strongly (r = 0.91, p < 0.0005). Even though MEG performance seemed almost comparable to EEG performance in this work, there are still many factors affecting classiﬁcation performance, such as preprocessing, ﬁltering, feature extractions, and classiﬁcation. Thus, a solid comparison between MEG and EEG performance is not easy. In addition, we found that the following issues should be considered in MEG processing. First, as reported in Dornhege etal. (2007), a large number of MEG channels may yield over-ﬁtting and it may fail to ﬁnd reasonable spatial ﬁlters. In our brief investigation, we observed that the whole channels (N = 152) yielded quite inferior performance (56.7 ± 7.8) to a far smaller number of selected channels (N = 20) when only CSP was applied. Second, compared to EEG electrodes attached on the head, the location of MEG sensors is more likely to move due to head movements of subjects during long experiments. There are reports that location mismatch may also inﬂuence classiﬁcation accuracy (Mellinger etal., 2007; Park etal., 2013). According to Park etal.’s (2013) report, the location change of channels degraded classiﬁcation accuracy and phase-based features (for example, phase locking value) are more stable than power-based

### MEG GAMMA AND BCI PERFORMANCE

In this work, we observed empirical evidence that MEG gamma correlates with MI performance. Prefrontal gamma seems to have a strong association with the MI process (at least in our study),but this may be the result of an indirect association. Speciﬁcally, we observed that prefrontal gamma yielded highly signiﬁcant results (r = 0.73, p = 0.02). Thus, we may infer that frontal gamma is the target neurophysiological factor to differentiate between good and poor MI task performers. However, there are some issues

|[Figure 7]<br><br>FIGURE 7 |Topographic images for resting state gamma in EEG. Images are sorted in descending order of MI performance with EEG.|
|---|

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 6

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 6 — #6

on a task accounted for 19% of the variance in BCI performance. Generally, a high frequency wave like gamma in the prefrontal cortex is interpreted as reﬂecting attention and memory processes (Jensen etal., 2007; Benchenane etal., 2011). Therefore, one can interpret that the high prefrontal gamma represents considerable activation and synchronization of neurons, and that this facilitates the imagination process for motor function.

|[Figure 8]<br><br>FIGURE 8 | Prefrontal MEG gamma and accuracy variation in two sessions.|
|---|

Interestingly, the gamma correlations in this study were as high as 0.80 (Figure 5), while other bands showed correlations of approximately 0.50 to 0.60. This is a very large range and suggests that frontal gamma may be more important than other bands,consideringsimilarstudiesshowingcorrelationsof r <0.40 across subjects (Ahn etal., 2013) and r < 0.10 within subjects (Grosse-Wentrup etal., 2011). We believe that MEG, rather than EEG,maybetterdetecthighfrequencyinformation,therebyresulting in higher correlations. Although we did not include the results of EEGs recorded during the resting state, it was difﬁcult to see a clear relationship with respect to gamma. Therefore, we may use theadvantagesof MEGoverEEG,andprescreensubjects’potential performance with MEG before a user begins to play with EEGbased BCI. EEG-based BCI will probably remain the most popular because of its advantages of portability, low cost and simple operation. MEG is large and expensive, and thus it is unrealistic to use for the BCI system. Rather, it is more likely that MEG will contribute to the pre-screening or diagnosis of a user’s traits and mental state.

that must be considered further. The ﬁrst is that frontal gamma maybecontaminatedbyfacialelectromyogram(EMG)noise. This EMG artifact may yield a substantial effect in our analysis and may be associated with notable patterns in gamma rhythm. To examine such possible EMG effects, we evaluated the correlations of several channels (Fp1, Fp2, F3, F4, F7, F8, Fz) in the frontal area against classiﬁcation accuracy. We observed that there were no signiﬁcantly correlated channels; thus, we are convinced that there was no substantial EMG effect in our MEG analysis. The second consideration is that some subjects may not be in a good mental state to conduct imagination. If this is the case, a subject who demonstrates poor accuracy at one time may perform well on another occasion. Because there are reports that attention is related to human performance (Pashler etal.,2001; Liu etal.,2005; Jensen etal., 2007; Lakey etal., 2011; Hammer etal., 2012), the second consideration is well worth investigation. To this end, we compared two different sessions for three subjects who had multisession data. In Figure 8, we plotted frontal gamma RPLs for the ﬁrst (A, B, C are the same as in Figure 4) and second session data (A2, B2 and C2) against BCI performance, and a positive slope over sessions was observed in all three subjects (Figure 6). We inferred from this result that high prefrontal gamma during the resting state is likely to yield good classiﬁcation accuracy. Even thoughotherareachannels(frontal,central,parietalandoccipital) were investigated similarly, notable patterns such as the positive correlation in the prefrontal area channels were absent. This is an interesting avenue to pursue in future investigations with more datasets.

As does the indirect association in the frontal area, we should understand the direct association with MI-related areas. It is known that larger alpha yields stronger event-related desynchronization, which is used as a most informative feature. This tendency was reported not only in MI (Blankertz etal., 2010; Ahn etal., 2013), but also in memory (Vogt etal., 1998; Klimesch etal., 1999) and visual (Salenius etal., 1995; Doppelmayr etal., 1998) processing. To process a task, it is considered that neurons ﬁringincertaincorticalareasaresynchronized(Jensenetal.,2007) and that this synchrony produces high frequency oscillations such as gamma. Thus, we may pose the hypothesis that the existing alpha power before MI may shift to rather high frequencies thereafter through neuronal communication in MI-related areas. Thus, low levels of gamma could reﬂect an idling state in that area, while it is producing high alpha rhythms. In this context, we expected that the centro-parietal gamma rhythm at rest might be correlated negatively with classiﬁcation accuracy. However, we observed a weak (non-signiﬁcant) negative correlation with MI performance in the centro-occipital regions (Figure 5). Therefore, it was difﬁcult to support our hypothesis, but it is still worth continuing this investigation with more and better data that have good quality high frequency information. We believe that an invasive approach like ECoG may have signiﬁcant potential in this type of study.

## CONCLUSION

In addition to our preliminary within-subjects results (Figure 6), there are other studies that have demonstrated the importance of prefrontal gamma. Halder etal. (2011) reported high correlations (r = 0.72) from fMRI comparisons between MI performance and voxel activations in the prefrontal area. Hammer etal. (2012) concluded that attention resources support BCI performance; importantly,they showed that the ability to concentrate

This study employed ten subjects to provide empirical evidence for the importance of gamma in MI accuracy. With simultaneous MEG/EEG data on MI and resting states before and after MI, we found that performance was correlated positively with gamma activity in the prefrontal area. This indicates that the way inwhichthegammarhythmisgeneratedintheprefrontalareaisof

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 7

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 7 — #7

great importance in MI processing. In conclusion, high prefrontal gamma – possibly related to concentration level – represents a goodmentalstateforreachingacceptableperformancesinMIBCI. This ﬁnding will facilitate the development of more advanced BCI designs that reﬂect users’ mental states in the system itself.

## ACKNOWLEDGMENTS

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MEST; No. 2010-0006135), and the Korea Research Council of Fundamental Science and Technology (KRCF) through Basic Research Project managed by KRISS.

## REFERENCES

Ahn, M., Cho, H., Ahn, S., and Jun, S. C. (2013). High theta and low alpha powers may be indicative of BCI-Illiteracy in motor imagery. PLoS ONE 8:e80886. doi: 10.1371/journal.pone.0080886

Ahn, M., Hong, J. H., and Jun, S. C. (2012). Feasibility of approaches combining sensor and source features in brain-computer interface. J. Neurosci. Methods 204, 168–178. doi: 10.1016/j.jneumeth.2011.11.002

Aoki, F., Fetz, E. E., Shupe, L., Lettich, E., and Ojemann, G. A. (1999). Increased gamma-range activity in human sensorimotor cortex during performance of visuomotor tasks. Clin. Neurophysiol. 110, 524–537. doi: 10.1016/S13882457(98)00064-9

Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2009). Differential representation of arm movement direction in relation to cortical anatomy and function. J. Neural Eng. 6, 016006. doi: 10.1088/1741-2560/6/1/016006

Bashashati, A., Fatourechi, M., Ward, R. K., and Birch, G. E. (2007). A survey of signal processing algorithms in brain-computer interfaces based on electrical brain signals. J. Neural Eng. 4, R32–R57. doi: 10.1088/1741-2560/4/2/R03

Battapady, H., Lin, P., Holroyd, T., Hallett, M., Chen, X., Fei, D.-Y., etal. (2009). Spatial detection of multiple movement intentions from SAMﬁltered single-trial MEG signals. Clin. Neurophysiol. 120, 1978–1987. doi: 10.1016/j.clinph.2009.08.017

Benchenane, K., Tiesinga, P. H., and Battaglia, F. P. (2011). Oscillations in the prefrontal cortex: a gateway to memory and attention. Curr. Opin. Neurobiol. 21, 475–485. doi: 10.1016/j.conb.2011.01.004

Benjamini, Y., and Hochberg, Y. (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. J. R. Statistical Soc. B (Methodological) 57, 289–300. doi: 10.2307/2346101

Bianchi, L., Sami, S., Hillebrand, A., Fawcett, I. P., Quitadamo, L. R., and Seri, S. (2010). Which physiological components are more suitable for visual ERP based brain-computer interface? A preliminary MEG/EEG study. Brain Topogr. 23, 180–185. doi: 10.1007/s10548-010-0143-0

Blankertz, B., Dornhege, G., Krauledat, M., Muller, K., Kunzmann, V., Losch, F., etal. (2006). The Berlin brain-computer interface: EEG-based communication without subject training. IEEE Trans. Neural. Syst. Rehabil. Eng. 14, 147–152. doi: 10.1109/TNSRE.2006.875557

Blankertz, B., Losch, F., Krauledat, M., Dornhege, G., Curio, G., and Muller, K.R. (2008a). The Berlin brain–computer interface: accurate performance from ﬁrst-session in BCI-naive subjects. IEEE Trans. Biomed. Eng. 55, 2452–2462. doi: 10.1109/TBME.2008.923152

Blankertz, B., Popescu, F., Krauledat, M., Fazli, S., Tangermann, M., and Müller, K.-R. (2008b). “Challenges for brain–computer interface research for human– computer interaction Applications,” in Proceedings of the SIGCHI Conference on HumanFactorsincomputingSystems,edsR.Grinter,T.Rodden,P.Aoki,E.Cutrell, R. Jeffries, and G. Olson (Florence: ACM Press).

Blankertz, B., Sannelli, C., Halder, S., Hammer, E. M., Kübler, A., Müller, K.R., etal. (2010). Neurophysiological predictor of SMR-based BCI performance. Neuroimage 51, 1303–1309. doi: 10.1016/j.neuroimage.2010.03.022

Bradberry, T. J., Rong, F., and Contreras-Vidal, J. L. (2009). Decoding center-out hand velocity from MEG signals during visuomotor adaptation. Neuroimage 47, 1691–1700. doi: 10.1016/j.neuroimage.2009.06.023

Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., etal. (2008). Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. doi: 10.1161/STROKEAHA.107.505313

Burde, W., and Blankertz, B. (2006). “Is the locus of control of reinforcement a predictor of brain-computer interface performance?” in Proceedings of the 3rd International Brain–Computer Interface Workshop and Training Course (Austria: Verlag der Technischen Universität Graz), 76–77.

Chowdhury, R. A., Lina, J. M., Kobayashi, E., and Grova, C. (2013). MEG source localization of spatially extended generators of epileptic activity: comparing entropic and hierarchical Bayesian approaches. PLoS ONE 8:e55969. doi: 10.1371/journal.pone.0055969

Darvas, F., Scherer, R., Ojemann, J. G., Rao, R. P., Miller, K. J., and Sorensen, L. B. (2010). High gamma mapping using EEG. Neuroimage 49, 930–938. doi: 10.1016/j.neuroimage.2009.08.041

Delorme, A., and Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. J. Neurosci. Methods 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

Doppelmayr, M. M., Klimesch, W., Pachinger, T., and Ripper, B. (1998). The functional signiﬁcance of absolute power with respect to event-related desynchronization. Brain Topogr. 11, 133–140. doi: 10.1023/A:1022206622348 Dornhege, G., Millán, J. D. R., Hinterberger, T., McFarland, D., and Müller, K.

(2007). Toward Brain–Computer Interfacing. Cambridge: MIT Press. Fries, P., Nikoli´c, D., and Singer, W. (2007). The gamma cycle. Trends Neurosci. 30, 309–316. doi: 10.1016/j.tins.2007.05.005

Genovese, C. R., Lazar, N. A., and Nichols, T. (2002). Thresholding of statistical maps in functional neuroimaging using the false discovery rate. Neuroimage 15, 870–878. doi: 10.1006/nimg.2001.1037

Grosse-Wentrup, M., and Schölkopf, B. (2012). High gamma-power predicts performance in sensorimotor-rhythm brain–computer interfaces. J. Neural Eng. 9,

046001. doi: 10.1088/1741-2560/9/4/046001

Grosse-Wentrup, M., Schölkopf, B., and Hill, J. (2011). Causal inﬂuence of gamma oscillations on the sensorimotor rhythm. Neuroimage 56, 837–842. doi: 10.1016/j.neuroimage.2010.04.265

Guger, C., Bin, G., Gao, X., Guo, J., Hong, B., and Liu, T. (2011). “State-of-the-art in BCI research: BCI Award 2010,” in Recent Advances in Brain–Computer Interface Systems, ed. R. Fazel (InTech). Available at: http://www.intechopen.com/books/howtoreference/recent-advances-inbrain-computer-interface-systems/state-of-the-art-in-bci-research-bci-award-20 10 (Accessed April 15, 2013).

Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain–computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147. doi: 10.1109/TNSRE.2003.814481

Halder, S., Agorastos, D., Veit, R., Hammer, E. M., Lee, S., Varkuti, B., etal. (2011). Neural mechanisms of brain–computer interface control. NeuroImage 55, 1779–

1790. doi: 10.1016/j.neuroimage.2011.01.021

Hamamé, C. M., Vidal, J. R., Ossandón, T., Jerbi, K., Dalal, S. S., Minotti, L., etal. (2012). Reading the mind’s eye: online detection of visuo-spatial working memory and visual imagery in the inferior temporal lobe. Neuroimage 59, 872– 879. doi: 10.1016/j.neuroimage.2011.07.087

Hammer, E. M., Halder, S., Blankertz, B., Sannelli, C., Dickhaus, T., Kleih, S., etal. (2012). Psychological predictors of SMR-BCI performance. Biol. Psychol. 89, 80–86. doi: 10.1016/j.biopsycho.2011.09.006

Hammon, P. S., Makeig, S., Poizner, H., Todorov, E., and Sa, V. R. D. (2008). Predicting reaching targets from human EEG. IEEE Signal Process. Mag. 69–77. doi: 10.1109/MSP.2008.4408443

Hong, J. H., Ahn, M., Kim, K., and Jun, S. C. (2013). Localization of coherent sources by simultaneous MEG and EEG beamformer. Med. Biol. Eng. Comput. 51, 1121–1135. doi: 10.1007/s11517-013-1092-z

Hong, J. H., and Jun, S. C. (2012). Scanning reduction strategy in MEG/EEG beamformer source imaging. J. Appl. Math. 2012, 528469. doi: 10.1155/2012/528469 Hwang,H.-J.,Kwon,K.,andIm,C.-H.(2009). Neurofeedback-basedmotorimagery training for brain–computer interface (BCI). J. Neurosci. Methods 179, 150–156. doi: 10.1016/j.jneumeth.2009.01.015

Jensen, O., Kaiser, J., and Lachaux, J.-P. (2007). Human gamma-frequency oscillations associated with attention and memory. Trends Neurosci. 30, 317–324. doi: 10.1016/j.tins.2007.05.001

Jerbi, K., Freyermuth, S., Minotti, L., Kahane, P., Berthoz, A., and Lachaux, J.-P. (2009). Watching brain TV and playing brain ball exploring novel BCI strategies using real-time analysis of human intracranial data. Int. Rev. Neurobiol. 86, 159– 168. doi: 10.1016/S0074-7742(09)86012-1

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 8

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 8 — #8

Jerbi, K., Vidal, J. R., Mattout, J., Maby, E., Lecaignard, F., Ossandon, T., etal. (2011). Inferring hand movement kinematics from MEG, EEG and intracranial EEG: from brain–machine interfaces to motor rehabilitation. IRBM 32, 8–18. doi: 10.1016/j.irbm.2010.12.004

Kleih, S. C., Kaufmann, T., Hammer, E., Pisotta, I., Pichiorri, F., Riccio, A., etal. (2013). “Motivation and SMR-BCI: fear of failure affects BCI performance,” in Proceedings of the Fifth International Brain-Computer Interface Meeting 2013 (Austria: Verlag der Technischen Universität Graz).

Klimesch, W., Vogt, F., and Doppelmayr, M. (1999). Interindividual differences in alpha and theta power reﬂect memory performance. Intelligence 27,347–362. doi: 10.1016/S0160-2896(99)00027-6

Ko, S., and Jun, S. C. (2010). Beamformer for simultaneous magnetoencephalography and electroencephalography analysis. J. Appl. Phys. 107, 09B315. doi: 10.1063/1.3360184

Lakey,C.E.,Berry,D.R.,andSellers,E.W.(2011). Manipulatingattentionviamindfulness induction improves P300-based brain–computer interface performance. J. Neural Eng. 8, 025019. doi: 10.1088/1741-2560/8/2/025019

Lal, T. N., Schröder, M., Hill, N. J., Preissl, H., Hinterberger, T., Mellinger, J., etal. (2005). “A brain computer interface with online feedback based on MEG,” Proceedings of the 22nd International Conference on Machine Learning, Germany.

Leeb, R., Lee, F., Keinrath, C., Scherer, R., Bischof, H., and Pfurtscheller, G. (2007). Brain–computer communication: motivation, aim, and impact of exploring a virtual apartment. IEEE Trans. Neural. Syst. Rehabil. Eng. 15, 473–482. doi: 10.1109/TNSRE.2007.906956

Leuthardt, E. C., Schalk, G.,Wolpaw, J. R., Ojemann, J. G., and Moran, D. W. (2004). A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1, 63–71. doi: 10.1088/1741-2560/1/2/001

Liu, T., Pestilli, F., and Carrasco, M. (2005). Transient attention enhances perceptual performance and FMRI response in human visual cortex. Neuron 45, 469–477. doi: 10.1016/j.neuron.2004.12.039

Lv, J., Li, Y., and Gu, Z. (2010). Decoding hand movement velocity from electroencephalogram signals during a drawing task. BioMed Eng. OnLine 9, 1–21. doi: 10.1186/1475-925X-9-64

Mahmoudi, B., and Erfanian, A. (2006). Electro-encephalogram based brain– computer interface: improved performance by mental practice and concentration skills. Med. Biol. Eng. Comput. 44, 959–969. doi: 10.1007/s11517-0060111-8

Mehring, C., Nawrot, M. P., de Oliveira, S. C.,Vaadia, E., Schulze-Bonhage,A.,Aertsen, A., etal. (2004). Comparing information about arm movement direction in single channels of local and epicortical ﬁeld potentials from monkey and human motor cortex. J. Physiol. Paris 98, 498–506. doi: 10.1016/j.jphysparis.2005.09.016

Mellinger, J., Schalk, G., Braun, C., Preissl, H., Rosenstiel, W., Birbaumer, N., etal. (2007). An MEG-based brain–computer interface (BCI). Neuroimage 36, 581–593. doi: 10.1016/j.neuroimage.2007.03.019

Muthukumaraswamy, S. D., Edden, R. A. E., Jones, D. K., Swettenham, J. B., and Singh,K.D.(2009). RestingGABAconcentrationpredictspeakgammafrequency and fMRI amplitude in response to visual stimulation in humans. PNAS 106, 8356–8361. doi: 10.1073/pnas.0900728106

Muthukumaraswamy, S. D., Singh, K. D., Swettenham, J. B., and Jones, D. K. (2010). Visual gamma oscillations and evoked responses: variability, repeatability and structural MRI correlates. NeuroImage 49, 3349–3357. doi: 10.1016/j.neuroimage.2009.11.045

Nijboer, F., Birbaumer, N., and Kübler, A. (2010). The inﬂuence of psychological state and motivation on brain–computer interface performance in patients with amyotrophic lateral sclerosis – a longitudinal study. Front. Neurosci. 4. doi: 10.3389/fnins.2010.00055

Ofner, P., and Müller-Putz, G. R. (2012). Decoding of velocities and positions of 3D arm movement from EEG. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 6406–6409. doi: 10.1109/EMBC.2012.6347460

Ortner, R., Irimia, D.-C., Scharinger, J., and Guger, C. (2012). A motor imagery based brain–computer interface for stroke rehabilitation. Stud. Health Technol. Inform. 181, 319–323. doi: 10.3233/978-1-61499-121-2-319

Park, S.-A., Hwang, H.-J., Lim, J.-H., Choi, J.-H., Jung, H.-K., and Im, C.-H. (2013). Evaluation of feature extraction methods for EEG-based brain–computer interfaces in terms of robustness to slight changes in electrode locations. Med. Biol. Eng. Comput. 51, 571–579. doi: 10.1007/s11517-012-1026-1

Pashler, H., Johnston, J. C., and Ruthruff, E. (2001). Attention and performance. Annu. Rev. Psychol. 52, 629–651. doi: 10.1146/annurev.psych.52.1.629

Pearl, J. (2000). Causality: Models, Reasoning, and Inference. Boston: Cambridge University Press.

Pfurtscheller, G., and Lopes da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857. doi: 10.1016/S1388-2457(99) 00141-8

Pistohl, T., Schulze-Bonhage, A., Aertsen, A., Mehring, C., and Ball, T. (2012). Decoding natural grasp types from human ECoG. Neuroimage 59, 248–260. doi: 10.1016/j.neuroimage.2011.06.084

Ramoser, H., Muller-Gerking, J., and Pfurtscheller, G. (2000). Optimal spatial ﬁltering of single trial EEG during imagined hand movement. IEEE Trans. Rehabil. Eng. 8, 441–446. doi: 10.1109/86.895946

Rickert, J., de Oliveira, S. C., Vaadia, E., Aertsen, A., Rotter, S., and Mehring, C. (2005). Encoding of movement direction in different frequency ranges of motor cortical local ﬁeld potentials. J. Neurosci. 25, 8815–8824. doi: 10.1523/JNEUROSCI.0816-05.2005

Robinson, N., Vinod, A. P., Ang, K., Tee, K., and Guan, C. (2013). EEG-based classiﬁcation of fast and slow hand movements using wavelet-CSP algorithm. IEEE Trans. Biomed. Eng. 60, 2123–2132. doi: 10.1109/TBME.2013.2248153

Salenius,S.,Kajola,M.,Thompson,W.L.,Kosslyn,S.,andHari,R.(1995). Reactivity of magnetic parieto-occipital alpha rhythm during visual imagery. Electroencephalogr. Clin. Neurophysiol. 95, 453–462. doi: 10.1016/0013-4694(95)00155-7

Schalk, G., Kubánek, J., Miller, K. J., Anderson, N. R., Leuthardt, E. C., Ojemann, J. G., etal. (2007). Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. J. Neural Eng. 4, 264–275. doi: 10.1088/1741-2560/4/3/012

Spirtes, P., Glymour, C., and Scheines, R. (2001). Causation, Prediction, and Search, 2nd Edn. Cambridge: A Bradford Book.

Sudre, G., Parkkonen, L., Bock, E., Baillet, S., Wang, W., and Weber, D. J. (2011). rtMEG: a real-time software interface for magnetoencephalography. Comput. Intell. Neurosci. 2011, 327953. doi: 10.1155/2011/327953

Ubeda, A., Ianez, E., Hortal, E., and Azorin, J. M. (2013). “Linear decoding of 2D hand movements for target selection tasks using a non-invasive BCI system,” in Systems Conference (SysCon), (Orlando: 2013 IEEE International) 778–782.

Uhlhaas, P. J., Pipa, G., Lima, B., Melloni, L., Neuenschwander, S., Nikoli´c, D., etal. (2009). Neural synchrony in cortical networks: history, concept and current status. Front. Integr. Neurosci. 3:17. doi: 10.3389/neuro.07.017.2009

Vogt, F., Klimesch, W., and Doppelmayr, M. (1998). High-frequency components in the alpha band and memory performance. J. Clin. Neurophysiol. 15, 167–172. doi: 10.1097/00004691-199803000-00011

Volosyak, I., Guger, C., and Gräser, A. (2010). “Toward BCI Wizard – best BCI approach for each user,” in 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC: Buenos Aires), 4201–4204.

Waldert, S., Pistohl, T., Braun, C., Ball, T., Aertsen, A., and Mehring, C. (2009). A review on directional information in neural signals for brain-machine interfaces. J. Physiol. Paris 103, 244–254. doi: 10.1016/j.jphysparis.2009.08.007

Waldert, S., Preissl, H., Demandt, E., Braun, C., Birbaumer, N., Aertsen, A., etal.

(2008). Hand movement direction decoded from MEG and EEG. J. Neurosci. 28, 1000–1008. doi: 10.1523/JNEUROSCI.5171-07.2008

Wang, W., Sudre, G. P., Xu, Y., Kass, R. E., Collinger, J. L., Degenhart, A. D., etal. (2010). Decoding and cortical source localization for intended movement direction with MEG. J. Neurophysiol. 104,2451–2461. doi: 10.1152/jn.00239.2010

Witte,M.,Kober,S. E.,Ninaus,M.,Neuper,C.,andWood,G. (2013). Control beliefs can predict the ability to up-regulate sensorimotor rhythm during neurofeedback training. Front. Hum. Neurosci. 7:478. doi: 10.3389/fnhum.2013.00478

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Womelsdorf, T., Schoffelen, J.-M., Oostenveld, R., Singer, W., Desimone, R., Engel, A. K., etal. (2007). Modulation of neuronal interactions through neuronal synchronization. Science 316, 1609–1612. doi: 10.1126/science.1139597

Worrell, G. A., Jerbi, K., Kobayashi, K., Lina, J. M., Zelmann, R., and Le Van Quyen, M. (2012). Recording and analysis techniques for high-frequency oscillations. Prog. Neurobiol. 98, 265–278. doi: 10.1016/j.pneurobio.2012.02.006

Zhang, J., Sudre, G., Li, X., Wang, W., Weber, D. J., and Bagic, A. (2011). Clustering linear discriminant analysis for MEG-based brain computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 19, 221–231. doi: 10.1109/TNSRE.2011. 2116125

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 9

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 9 — #9

Conflictof InterestStatement:Theauthorsdeclarethattheresearchwasconducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 28 May 2013; accepted: 21 November 2013; published online: 06 December 2013. Citation: Ahn M, Ahn S, Hong JH, Cho H, Kim K, Kim BS, Chang JW and Jun SC (2013) Gamma band activity associated with BCI performance: simultaneous

MEG/EEG study. Front. Hum. Neurosci. 7:848. doi: 10.3389/fnhum.2013. 00848 This article was submitted to the journal Frontiers in Human Neuroscience. Copyright © 2013 Ahn, Ahn, Hong, Cho, Kim, Kim, Chang and Jun. This is an openaccess article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

##### Frontiers in Human Neuroscience www.frontiersin.org December 2013 | Volume 7 | Article 848 | 10

“fnhum-07-00848” — 2013/12/4 — 17:46 — page 10 — #10

