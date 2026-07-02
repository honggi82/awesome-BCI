ORIGINAL RESEARCH ARTICLE

published: 15 August 2013 doi: 10.3389/fnhum.2013.00478

HUMAN NEUROSCIENCE

[Figure 1]

# Control beliefs can predict the ability to up-regulate sensorimotor rhythm during neurofeedback training

## Matthias Witte1, Silvia Erika Kober1, Manuel Ninaus1, Christa Neuper1,2 and Guilherme Wood1*

- 1 Department of Psychology, University of Graz, Graz, Austria
- 2 Laboratory of Brain-Computer Interfaces, Institute for Knowledge Discovery, Graz University of Technology, Graz, Austria

Edited by: Reinhold Scherer, Graz University of Technology, Austria

Reviewed by: Juliana Yordanova, Institute of Neurobiology, Bulgarian Academy of Sciences, Bulgaria Stefano Silvoni, I.R.C.C.S. S.Camillo Hospital Foundation, Italy Moritz Grosse-Wentrup, Max Planck Institute for Biological Cybernetics, Germany

*Correspondence: Guilherme Wood, Department of Psychology, University of Graz, Universitaetsplatz 2/III, 8010 Graz, Austria e-mail: guilherme.wood@uni-graz.at

Technological progress in computer science and neuroimaging has resulted in many approaches that aim to detect brain states and translate them to an external output. Studies from the ﬁeld of brain-computer interfaces (BCI) and neurofeedback (NF) have validated the coupling between brain signals and computer devices; however a cognitive model of the processes involved remains elusive. Psychological parameters usually play a moderate role in predicting the performance of BCI and NF users. The concept of a locus of control, i.e., whether one’s own action is determined by internal or external causes, may help to unravel inter-individual performance capacities. Here, we present data from 20 healthy participants who performed a feedback task based on EEG recordings of the sensorimotor rhythm (SMR). One group of 10 participants underwent 10 training sessions where the amplitude of the SMR was coupled to a vertical feedback bar. The other group of ten participants participated in the same task but relied on sham feedback. Our analysis revealed that a locus of control score focusing on control beliefs with regard to technology negatively correlated with the power of SMR. These preliminary results suggest that participants whose conﬁdence in control over technical devices is high might consume additional cognitive resources. This higher effort in turn may interfere with brain states of relaxation as reﬂected in the SMR. As a consequence, one way to improve control over brain signals in NF paradigms may be to explicitly instruct users not to force mastery but instead to aim at a state of effortless relaxation.

Keywords: EEG, locus of control, neurofeedback, performance prediction, sensorimotor rhythm

## INTRODUCTION

In the last twenty years of neuroimaging research a clear view has emerged that patterns of brain activity can be directly linked to different cognitive states. Users of neurofeedback (NF) can learn to modulate their brainsignals over severaltraining sessions. Alternatively, using multivariate analysis methods one can try to decode these brain states and use the output of a classiﬁer to control external devices in a so-called brain-computer interface (BCI). A key concept behind all these approaches is the assumption that the brain activations associated with a cognitive state are stable over time, highly speciﬁc and distinct from other states. However, these prerequisites are not always fulﬁlled and the neural correlates of a cognitive state are masked by various sources of physiological and environmental noise. The search for reliable predictors of performance therefore remains one of the major challenges in this ﬁeld of research.

To achieve a reliable readout of brain patterns most BCI studies have put the primary load on the machine-learning side. This seems a straightforward approach as the goal of many BCIs is to detect overt brain states, like decoding movement parameters or stimulus-evoked activity (for review see: Donoghue, 2008; Green and Kalaska, 2011). Here, a standard procedure is to adapt the classiﬁcation across participants and sessions

(McFarland et al., 2005; Shenoy et al., 2006; Blumberg et al., 2007; Vidaurre et al., 2007). In contrast, NF is inspired by conditioning and often modulates a covert, unconscious state by immediate reward. One of the best described examples is the voluntary regulation of slow cortical potentials in healthy participants and paralyzed patients (Birbaumer et al., 1999; Kubler et al., 1999, 2001; Neumann and Birbaumer, 2003). It has been shown that self-regulation of these brain signals is optimally learned without giving deﬁnite strategies (Birbaumer et al., 1988; Neumann et al., 2003). An issue in this design is that users may feel lost at early stages of training and start to explore different ways to regulate their brain activity. Due to the immediate closed-loop feedback this “trial-and-error” learning can result in progressively better control and is believed to ultimately lead to an automated skill (Wolpaw and McFarland, 1994; Neumann and Birbaumer, 2003; Hinterberger et al., 2005). However, the literature has also described a signiﬁcant proportion of people who are unable to gain control over signals in BCI and NF paradigms (Guger et al., 2003; Kübler et al., 2004; Nijboer et al., 2008; Blankertz et al., 2010b). The reasons for this phenomenon of “illiteracy” are still unknown and only few studies tried to assess predictors of successful performance. Factors like mood, motivation, intelligence and personal traits

[Figure 2]

have been reported to show only moderate correlations to performance in healthy and impaired participants (Nijboer et al., 2008, 2010; Kleih et al., 2010; Hammer et al., 2012). Yet there is evidence from neuropsychological tests that part of the variations seen in NF training may be connected to memory and attentional abilities of participants (Roberts et al., 1989; Daum et al., 1993; Holzapfel et al., 1998). In particular, frontoparietal gamma-band activity has been reported to inﬂuence sensorimotor activity, presumably reﬂecting attentional networks (Grosse-Wentrup and Schölkopf, 2012). Furthermore, the initial performance level was shown to have some predictive value for future performance (Neumann and Birbaumer, 2003; Kübler et al., 2004). These results may thus suggest that the overall, not necessarily task-related, cognitive resources impact the level of control in NF and BCI tasks.

Given that all experiments in the ﬁeld of BCI and NF imply the use and interaction with technologic environments it is surprising that only one study directly assessed how technology commitment may impact performance (Burde and Blankertz, 2006). The authors evaluated the “locus of control of reinforcement” (LOC), a psychological construct developed by Rotter’s social learning theory (Rotter, 1966). According to this theory, people with an external LOC tend to attribute the result of their own actions to external sources like luck, chance or unpredictable circumstances. Conversely, an internal LOC describes the personal trait to link results and own actions and thus people feel that they are in control of the situation. Burde and Blankertz (2006) assessed the general control belief with an IPC (Internal, Powerful Others and Chance) questionnaire (Krampen, 1981) and the speciﬁc interaction with technology as indexed by the KUT (Kontrollueberzeugug im Umgang mit Technik), i.e., control beliefs while dealing with technology (Beier, 1999, 2004). They reported a positive correlation between KUT scores and BCI performance in 12 healthy participants partaking in a motor imagery task. However, only a single session was recorded and the features for classiﬁcation were individually adapted for each participant.

We therefore sought to clarify whether control beliefs while dealing with technology, as reﬂected in the KUT score, can predict performance in NF training over several sessions. To this end, 10 participants trained to gain control over their sensorimotor rhythm (SMR, 12–15 Hz) in 10 sessions spanning up to ﬁve weeks via real-time visual feedback. An additional control group of 10 participants took part in the same protocol but received sham visual feedback. SMR is known to originate from thalamo-cortical loops and increased SMR amplitude is found during states of relaxed wakefulness with reduced sensory and motor excitability (Gruzelier et al., 2006; Serruya and Kahana, 2008). Because SMR desynchronizes during movement execution and during motor imagery in an event-related manner (Pfurtscheller and Neuper, 1997; Pfurtscheller and Lopes Da Silva, 1999; McFarland et al., 2000), it has been extensively used in BCI research (Cincotti et al., 2003; Pfurtscheller et al., 2006; Mellinger et al., 2007; Blankertz et al., 2010a). The opposing effect of voluntarily increasing SMR amplitude can also be learned through NF training (Vernon et al., 2003; Egner et al., 2004; Hoedlmoser et al., 2008; Weber et al., 2011; de Zambotti et al., 2012). However, only few studies

investigated the changes of SMR over longer time periods of training and, to our knowledge, there is no report on the inﬂuence of technology commitment in training scenarios.

## MATERIALS AND METHODS

### PARTICIPANTS

Twenty healthy participants (10 males, mean ± SD age: 24.4 ± 1.8 years) participated in this study after giving written informed consent. The study was approved by the local ethical committee of the University of Graz in accordance to the Declaration of Helsinki. No participant had any experience in NF- and BCIparadigms prior to this study. In a double-blinded approach participants were randomly assigned to one group of 10 participants: either receiving real visual feedback coupled to brain rhythms experimental group (EG) or receiving a video of sham feedback randomly taken from one of these real feedback sessions control group (CG).

### EXPERIMENTAL PARADIGM

We recorded brain signals with a 16 Ag/AgCl electrode system (g.USBamp, g.tec medical engineering GmbH, Austria) mounted according to the International 10–20 EEG system and referenced to the left mastoid. Ground electrode was set on Fpz electrode and signals digitized at a sampling frequency of 256 Hz. In addition, electrooculography (EOG) was recorded to eliminate eye movement artifacts post-hoc.

Online visual NF was implemented via SIMULINK software (The MathWorks, Natick, USA). Raw signals were band-pass ﬁltered in the respective target bands (precise frequencies see below; 6th order butterworth IIR) and squared to obtain power estimates. To ensure a smooth visual feedback we then applied a moving average of 256 samples and updated the computer screen at a rate of 10 Hz. The feedback design was adopted from a previous study (Weber et al., 2011): while a central bar was coupled to the user’s absolute power of the SMR (12–15 Hz) recorded at electrode Cz, two smaller ﬂanking bars reﬂected absolute power in θ (4–7 Hz) and β (21–35 Hz) ranges at Cz, respectively. This setup of three moving bars was chosen to ensure voluntary regulation of SMR and at the same time minimize inﬂuence of eye movements (θ), muscle activations and other task-unrelated components (β). Each of the 10 sessions started with a ﬁrst baseline run (3 min) where participants were instructed to relax and watch the moving feedback bars coupled to their brain activity without trying to control them. Then six feedback runs (3 min each) were recorded and participants tried to gain voluntary control over their brain rhythms, i.e., an increase of power was associated with an increase of the feedback bar.

Participants’ task was to increase the height of the central bar and at the same time keep the two smaller bars as low as possible. To facilitate the recognition of current performance, participants received an additional rewarding feedback whenever the bigger central bar reached a pre-deﬁned threshold without concomitant artifacts: a number in the middle of the bar served as reward counter and was incremented by one unit each time this target state was achieved for 250 ms (i.e., between 0 and 720 points could be earned per run). The individual threshold was initially determined on the median absolute SMR power of the

baseline run and progressively adapted using the median power of each previous feedback run. Similarly, the small ﬂanker bars were calibrated once on the baseline recording of each day (threshold: mean power + 1 SD) and feedback bars changed color from green to red whenever inﬂuence of artifacts reached the individual thresholds.

### DATA ANALYSIS

All preprocessing and data analysis of EEG recordings were performed ofﬂine using the Brain Vision Analyzer software (version 2.01, Brain Products GmbH, Munich, Germany). First, 1 s epochs of data were inspected for eye movement artifacts by a trained investigator and contaminated epochs were manually rejected. Next, we applied an automated rejection of additional artifacts like muscular activity, high-frequency noise or drifts (rejection criteria: step >50.00 µV per sampling point, absolute voltage value >120.00 µV).

In line with past studies (Weber et al., 2011; de Zambotti et al., 2012), absolute values of SMR power in a ﬁxed range (12–15 Hz) were calculated for all epochs of length 1 s using Brain Vision Analyzer’s built-in method of complex demodulation. For each run,this procedureoutputsmean SMR power overthe whole time window of 3 min.

### LOCUS OF CONTROL OF REINFORCEMENT

The LOC was assessed in the context of dealingwith technology by the KUT questionnaire (Beier, 1999, 2004). This one dimensional construct of LOC is a subjective 5-point Likert scale rating that considers actual technologic biography in eight items (range of total score: 8–40). The questionnaire is available in German and has a high reliability. To monitor control beliefs over time each participant was asked twice, before the ﬁrst and after the 10th training session.

### STATISTICAL DATA ANALYSIS

Absolute SMR power values were calculated for each run separately and mean power was tested for differences using a 2 ×

- 3 × 2 repeated measures ANOVA with between-factor group (EG vs. CG) and within-factors session (sessions 1–3, sessions 4–7, sessions 8–10) and run (runs 2–4, runs 5–7). Measures of effect size were reﬂected in partial eta-squared (η2) and observed power

(Obspow). Post-hoc tests, if necessary, were run on signiﬁcant effects using Fisher’s Least Signiﬁcant Difference (LSD) test.

To report trends of power changes we used a linear ﬁt and assessed the signiﬁcance of the regression slope using t-statistics of the regression model implemented in MATLAB (The MathWorks, Natick, USA). Group-wise comparisons of power and KUT values were assessed using paired t-test. All statistics considered a nominal probability level of p < 0.05 signiﬁcant.

## RESULTS

### CONTROL BELIEFS AND NEUROFEEDBACK TRAINING

As a ﬁrst step, we quantiﬁed the distribution and changes of our predictor variable across the population of participants. Our assessment of control beliefs while dealing with technology before NF training revealed no differences (t(18) = −0.15, p = 0.88 n.s., paired t-test) in KUT scores between the EG using real NF and

the CG that relied on sham feedback. Overall scores were rather high varying only little around a value of 33 on average. Next, we intended to characterize differences within the groups in more detail. When dividing each group into subgroups using mediansplit, signiﬁcant differences of 7.42 and 7.2 scores on average were observed between subgroups of high and low KUT within EG and CG respectively (t(8) = −4.82 for the EG and t(8) = −4.14 for the CG, p < 0.05, paired t-test, see also Table 1). Re-evaluating KUT scores after the last session revealed no signiﬁcant changes so that in the following sections we will refer to values of the ﬁrst assessment on day one.

Our main goal was to explore whether the observeddifferences in individual control beliefs were reﬂected in differential changes of SMR. Analysis of mean absolute SMR power did not reveal any signiﬁcant effects over sessions. However, SMR power changed within session as indicated by the signiﬁcant main effect of run (F(1,18) = 4.51, p < 0.05, η2 = 0.20, Obspow = 0.52). To further characterize this trend, we applied a linear ﬁt for each group separately (Figure 1). While for the CG no trends were found (slope = 0.008, p = 0.35, R2 = 0.22, n = 10 participants), SMR of the EG consistently increased across runs (slope = 0.023, p < 0.01, R2 = 0.86, n = 10 participants). As evident in Figure 1B this effect was dominated by participants with low KUT scores (slope = 0.035, p < 0.05, R2 = 0.78, n = 5 participants) who also showed signiﬁcantly higher SMR values when compared to participants of the EG with high KUT scores (t(8) = 3.37, p < 0.01, paired t-test). In contrast, this difference of SMR power between subgroups did not reach statistical signiﬁcance for the CG (t(8) = 1.11, p = 0.30 n.s., paired t-test).

### CHANGES OF SMR POWER IN BASELINE

To check for possible lasting effects of NF training we additionally compared baseline SMR power for the different groups. This analysis failed to show modulations across sessions. However, similar to the power changes over runs, we found that participants with lower KUT generally had increased SMR power compared to those with high KUT (Figure 2B and Table 1). Again, this difference was more pronounced for the EG

[Figure 6]

Table 1 | Grand average SMR power (in µV2) of the respective subgroups for electrode Cz across 10 training sessions and while watching the feedback bars (baseline), as well as ratings of control beliefs on day one.

[Figure 7]

EG CG

[Figure 8]

[Figure 9]

low KUT

high KUT all

low KUT

high KUT

all

[Figure 10]

KUT mean 32.7 29.0 36.4 33.0 29.4 36.6 SEM 1.4 1.3 0.8 1.5 1.7 0.2

SMR mean 2.06 2.66 1.46 1.86 2.23 1.50

training SEM 0.26 0.35 0.09 0.33 0.62 0.23 SMR mean 1.97 2.46 1.48 1.94 2.39 1.48

baseline SEM 0.22 0.31 0.05 0.38 0.70 0.22

[Figure 11]

EG, experimental group; CG control group; KUT, control beliefs while dealing with technology; SMR, sensorimotor rhythm; SEM, standard error of the mean; note that subgroups “low” and “high” of n = 5 participants were obtained using median split on KUT scores of “all” n = 10 participants.

[Figure 15]

[Figure 16]

linear correlation for both groups. This revealed a signiﬁcant negative correlation between KUT and overall SMR power during training of r = −0.69 for the EG (p < 0.05). A strong trend for negative correlation of the same variables in the CG (r = −0.36,p = 0.31) was observed, only corrupted by one participant

[Figure 17]

- (Figure 3A). As the within group differences in absolute SMR power were

also evident in baseline, we additionally evaluated correlation coefﬁcients between KUT and average SMR of these runs

- (Figure 3B). The overall picture was similar to training runs in that participants of the EG showed a negative correlation of r = −0.73 (p < 0.05) and participants of the CG displayed a similar trend (r = −0.42,p = 0.23). DISCUSSION

- As reliable predictors of NF performance still remain elusive, the goal of the current study was to assess whether control beliefs of users correlate with brain activity over several training sessions. Our main results show that voluntary up-regulation of absolute SMR power is more successful in those participants who report a lower subjective level of control while dealing with technology.

This novel ﬁnding is supported by several lines of evidence. Firstly, the overall power of SMR in the 12–15 Hz range across ten training sessions negatively correlated with KUT scores for the EG. In other words, participants with lower ratings of control belief were more successful in our training paradigm. According to Krampen (1981) control belief is deﬁned as the individuals’ expectancy for a contingent result of an action. The KUT questionnaire quantiﬁes a speciﬁc aspect of control, namely how comfortable and conﬁdent users feel when interacting with technology (Beier, 2004; Burde and Blankertz, 2006). How this psychological trait may be used to characterize NF performance has remained unexplored so far. Our ﬁndings of a negative correlation between KUT and SMR power indicate a higher relaxation in people who subjectively do not expect a major inﬂuence on technology. This state of relaxation in turn is known to promote increased SMR amplitudes (Pfurtscheller, 1992; Gruzelier et al., 2006, 2010; Pfurtscheller et al., 2006; Serruya and Kahana, 2008).

- At the same time our results imply that users with strong control beliefs may try harder to master the feedback paradigm and thus activate resources interfering with the SMR synchronization. This idea of “processing interference” has been proposed in healthy participants and seizure patients (Sterman, 1996, 2000).

FIGURE 1 | Changes of SMR power during training. (A) Mean absolute SMR power (12–15 Hz) across sessions during six runs of neurofeedback training for the experimental group using real feedback (EG, n = 10 participants) and the control group using sham feedback (CG, n = 10 participants). Dotted line indicates a signiﬁcant slope of 0.023 µV2 per run. (B,C) Comparison of subgroups (n = 5 participants) obtained by

In the literature there is only one study that assessed the link between control belief and modulation of brain signals: Burde and Blankertz (2006) reported a positive correlation between KUT and BCI performance. However, their task under investigation and the methods to reveal changes of brain activity clearly differ from our approach. These authors conducted a single session and relied on highly participant-optimized spectro-spatial features for providing feedback. Also they did not directly use the power of SMR for correlation analyses but rather assessed the number of runs in which participants successfully moved a cursor from the center to the target edge of a computer screen. Most importantly, this BCI control implied a motor imagery task where the classiﬁed pattern is that of a

median-split according to the individual control beliefs of low and high KUT scores. Dotted line indicates a signiﬁcant slope of 0.035 µV2 per run. Note that all error bars represent the standard error of the mean (SEM).

[Figure 18]

(t(8) = 3.09,p < 0.05, paired t-test) when compared to the CG (t(8) = 1.24,p = 0.25 n.s., paired t-test).

### OVERALL CORRELATION OF KUT AND SMR POWER

The results described hitherto all indicate a trend for differences in SMR power between participants of low and high KUT scores. As a direct measure of this relationship we calculated Pearson’s

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

activations without trying to gain control, while participants of the CG were watching a pre-recorded video (B,C) comparison according to the individual control beliefs (same conventions as in Figure 1).

FIGURE 2 | Changes of SMR power during baseline. (A) Mean absolute SMR power across 10 training sessions during the baseline condition. Participants of the EG were watching a visual feedback of their own brain

[Figure 25]

desynchronization of the SMR. In this light, participants with higher level of control belief could be more successful simply because they will likely try to actively control the feedback and thus down-regulate their SMR stronger during motor imagery. This decrease of activity is also depending on the level of SMR during rest (Blankertz et al., 2010a). In contrast, our NF paradigm directly trained the increase of absolute SMR power. In this task our ﬁndings suggest that stronger control beliefs can hinder participants’ relaxation and thus an effective up-regulation of SMR power during training. The ability of an

individual user to succeed in both up- and down-regulation of SMR may therefore differ based on the different physiological processes and may furthermore depend on the task and method used to evaluate these modulations.

A second aspect of our training in the EG was an increase of SMR power over runs within sessions. Because we applied an online visual feedback, an overall higher level of relaxation may thus have promoted a self-rewarding positive loop. This within session increase is therefore believed to reﬂect successful training (Vernon et al., 2003; Gruzelier et al., 2006). The fact

[Figure 29]

[Figure 30]

tion that control belief is directly linked to the success of SMR feedback training.

[Figure 31]

It has to be noted however that we did not ﬁnd any signiﬁcant modulations or interactions across training sessions. Yet, this does not conﬂict with past ﬁndings as those studies reporting intersessionchanges either used ratios of the power within two or more frequency bands or relied on relative power changes (Ros et al., 2009; Gruzelier et al., 2010; de Zambotti et al., 2012). In contrast, our measure of absolute SMR power represents a direct index of brain activity. A distinct increase of this index over sessions actually would not have been expected. de Zambotti et al. (2012) recently reported an increase of the SMR-θ ratio across weeks of NF training. However, this ratio was calculated with respect to a baseline and authors mentioned a decrease of SMR-θ in this baseline. As a consequence, the observed training effect in the study of de Zambotti et al. (2012) may not have been solely caused by brain processes in the active period. Our results during baseline did not show a change of SMR power ruling out the possibility of a pseudo training effect. Yet, we again observed a markedly higher SMR for participants of low KUT scores underlining the general validity of this relationship. An important difference to previous work is that during baseline in our approach participants watched feedback bars coupled to their actual brain activity without trying to control the feedback bars. This might explain why overall baseline SMR power was not different to training runs. The role of baseline recordings in assessing changes of power over sessions may thus need further research.

To check for the task-speciﬁcity of the observed effects, we included the CG receiving a video of sham feedback. Although the overall SMR power was not signiﬁcantly different to the EG and since a strong trend for a negative correlation between KUT and SMR was evident, some important points should be considered. First, participants of the CG tended to show lower power values and a higher variance across participants was observed (Figures 1,2). Second, there was no clear increase of power over runs (Figure 1C). And third, the within-group difference between participants of low and high KUT scores was less pronounced than in the EG. Altogether, we thus conclude that in contrast to other studies our CG experienced a residual, although less effective, training as well. This is supported by the fact that no member of this group identiﬁed the sham feedback. Instead, the randomized replay of moving bars was accepted as real feedback so that a similar pattern of the relationship between KUT and SMR power emerged. The greater amount of variability and the non-signiﬁcant dissociation of SMR power between KUT subgroups of the CG suggest, however, that only contingent feedback training can produce clear task-speciﬁc effects.

FIGURE 3 | SMR power correlates with control belief. (A) Scatter plot of individual KUT scores against overall SMR power during feedback training (total n = 60 runs per participant). (B) Same as in (A) for baseline runs (total n = 10 runs per participant). For details of the relationships please see subsection “Overall Correlation of KUT and SMR Power” in Results.

[Figure 32]

that absolute SMR power increased only moderately may partly originate from our experimental design: in line with suggestions of other studies (Kubler and Birbaumer, 2008; Nijboer et al., 2010) we adapted the difﬁculty of our task from run to run in the EG. While this procedure was believed to maintain a high level of motivation and interest in the task, past results also mentioned the risk of incompetence fear (Nijboer et al., 2008). In particular, these authors suggested that when performance in visual SMR feedback is initially high, incompetence fear may hamper further learning. Indeed, we do have evidence for a correlate of negative emotions in insular brain regions during our paradigm (Ninaus et al., submitted to the current special issue). How precisely emotions, task complexity and reward expectancy interact with performance thus needs to be explored in further studies. Interestingly, median split of participants of the EG revealed that those users with low KUT had distinctly higher SMR amplitudes over all runs and showed a signiﬁcantly increasing trend. In our view, this corroborates the interpreta-

Our ﬁndings support the existing NF literature that has suggested a state of relaxed but focused mind for successful performance. For example, a recent study showed a strong inhibition of SMR in initial sessions which was attributed to increased arousal of participants who most likely needed to get used to the experimental setup (de Zambotti et al., 2012). Hammer and colleagues (Hammer et al., 2012) also reported that, besides ﬁne motor skills, the ability to concentrate on the task explained a signiﬁcant proportion of 19% of the variations seen in BCI

performance. At the same time all other psychologicalparameters, like verbal and non-verbal learning abilities, empathy or mood, did not predict performance in this study. Similarly, motivational factors seem to be only weak predictors of performance and need to be considered at a single subject level (Nijboer et al., 2008, 2010; Kleih et al., 2010). Still, the ﬁnding that initial performance during voluntary regulation of brain activity has predictive value (Neumann and Birbaumer, 2003; Kübler et al., 2004) may suggest that personal traits can impact the ability to successfully use feedback paradigms. One important factor in NF and BCI is clearly the individual control beliefs of participants because the tasks per se imply the interaction with technology. The only study in this context we are aware of has already demonstrated a strong correlation between control belief and BCI performance. We clearly extend this knowledge as we identiﬁed control beliefs while dealing with technology as a strong predictor of performance in several training sessions. Whether our ﬁndings generalize to other frequency-bands and experimental setups needs further validation. In studies that focus on brain activity associated with relaxation, e.g., in treatment of attention deﬁcit hyperactivity disorder, one would expect similar predictive effects. In general, we strongly suggest that concepts of control belief, self-perception

and awareness should be considered in more detail during BCI and NF operation.

## CONCLUSION

In summary, we demonstrate that control beliefs negatively correlated with the ability to increase SMR during 10 NF sessions. An important implication for future training studies therefore is that participants may not focus on gaining control over the feedback but instead should try to relax themselves. In the light of our results, assessment of individual control beliefs can be used as a predictor of future performance and may thus help to avoid lengthy training.

## ACKNOWLEDGMENTS

This work is supported by the European STREP ProgramCollaborative Project no. FP7-287320—CONTRAST. Possible inaccuracies of information are under the responsibility of the project team. The text reﬂects solely the views of its authors. The European Commission is not liable for any use that may be made of the information contained therein. The authors are grateful to Mathias Leitner, Iris Tomantschger, René Steﬁtz and Tanja Jauk for data acquisition.

## REFERENCES

Beier, G. (1999). Kontrollüberzeugungen im umgang mit technik. Report Psychologie 9, 684–693.

Beier, G. (2004). Kontrollüberzeugungen im umgang mit technik: ein persönlichkeitsmerkmal mit relevanz für die gestaltung technischer systeme (Doctoral thesis). Available from GESIS database, Record No. 20040112708.

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kubler, A., et al. (1999). A spelling device for the paralysed. Nature 398, 297–298. doi: 10. 1038/18581

Birbaumer, N., Lang, P. J., Cook, E., 3rd, Elbert, T., Lutzenberger, W., and Rockstroh, B. (1988). Slow brain potentials, imagery and hemispheric differences. Int. J. Neurosci. 39, 101–116. doi: 10. 3109/00207458808985696

Blankertz, B., Sannelli, C., Halder, S., Hammer, E. M., Kubler, A., Muller, K. R., et al. (2010a). Neurophysiological predictor of SMRbased BCI performance. NeuroImage 51, 1303–1309. doi: 10.1016/j. neuroimage.2010.03.022

Blankertz, B., Tangermann, M., Vidaurre, C., Fazli, S., Sannelli, C., Haufe, S., et al. (2010b). The berlin braincomputer interface: non-medical uses of BCI technology. Front. Neurosci. 4:198. doi: 10.3389/fnins. 2010.00198

Blumberg, J., Rickert, J., Waldert, S., Schulze-Bonhage, A., Aert-

sen, A., and Mehring, C. (2007). Adaptive classiﬁcation for brain computer interfaces. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2007, 2536–2539.

Burde, W., and Blankertz, B. (2006). “Is the locus of control of reinforcement a predictor of brain-computer interface performance?” in Proceedings of the 3rd International Brain-Computer Interface Workshop and Training Course, Graz, Austria, 76–77.

Cincotti, F., Mattia, D., Babiloni, C., Carducci, F., Salinari, S., Bianchi, L., et al. (2003). The use of EEG modiﬁcations due to motor imagery for brain-computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 131–133. doi: 10.1109/tnsre.2003. 814455

Daum, I., Rockstroh, B., Birbaumer, N., Elbert, T., Canavan, A., and Lutzenberger, W. (1993). Behavioural treatment of slow cortical potentials in intractable epilepsy: neuropsychological predictors of outcome. J. Neurol. Neurosurg. Psychiatry 56, 94–97. doi: 10.1136/jnnp. 56.1.94

de Zambotti, M., Bianchin, M., Magazzini, L., Gnesato, G., and Angrilli, A. (2012). The efﬁcacy of EEG neurofeedback aimed at enhancing sensory-motor rhythm theta ratio in healthy subjects. Exp. Brain Res. 221, 69–74. doi: 10.1007/s00221012-3148-y

Donoghue, J. P. (2008). Bridging the brain to the world: a perspective

on neural interface systems. Neuron 60, 511–521. doi: 10.1016/j.neuron. 2008.10.037

Egner, T., Zech, T. F., and Gruzelier, J. H. (2004). The effects of neurofeedback training on the spectral topography of the electroencephalogram. Clin. Neurophysiol. 115, 2452– 2460. doi: 10.1016/j.clinph.2004. 05.033

Green, A. M., and Kalaska, J. F. (2011). Learning to move machines with the mind. Trends Neurosci. 34, 61–75. doi: 10.1016/j.tins.2010.11.003

Grosse-Wentrup, M., and Schölkopf, B. (2012). High gamma-power predicts performance in sensorimotorrhythm brain-computer interfaces. J. Neural. Eng. 9:046001. doi: 10. 1088/1741-2560/9/4/046001. [Epub ahead of print].

Gruzelier, J., Egner, T., and Vernon, D. (2006). Validating the efﬁcacy of neurofeedback for optimising performance. Prog. Brain Res. 159, 421–431. doi: 10.1016/s00796123(06)59027-2

Gruzelier, J., Inoue, A., Smart, R., Steed, A., and Steffert, T. (2010). Acting performance and ﬂow state enhanced with sensory-motor rhythm neurofeedback comparing ecologically valid immersive VR and training screen scenarios. Neurosci. Lett. 480, 112–116. doi: 10.1016/j. neulet.2010.06.019

Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain-

computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147. doi: 10.1109/tnsre.2003. 814481

Hammer, E. M., Halder, S., Blankertz, B., Sannelli, C., Dickhaus, T., Kleih, S., et al. (2012). Psychological predictors of SMR-BCI performance. Biol. Psychol. 89, 80–86. doi: 10. 1016/j.biopsycho.2011.09.006

Hinterberger, T., Veit, R., Wilhelm, B., Weiskopf, N., Vatine, J. J., and Birbaumer, N. (2005). Neuronal mechanisms underlying control of a brain-computer interface. Eur. J. Neurosci. 21, 3169–3181. doi: 10.1111/j.1460-9568.2005. 04092.x

Hoedlmoser, K., Pecherstorfer, T., Gruber, G., Anderer, P., Doppelmayr, M., Klimesch, W., et al. (2008). Instrumental conditioning of human sensorimotor rhythm (12–15 Hz) and its impact on sleep as well as declarative learning. Sleep 31, 1401–1408.

Holzapfel, S., Strehl, U., Kotchoubey, B., and Birbaumer, N. (1998). Behavioral psychophysiological intervention in a mentally retarded epileptic patient with brain lesion. Appl. Psychophysiol. Biofeedback 23, 189–202.

Kleih, S. C., Nijboer, F., Halder, S., and Kubler, A. (2010). Motivation modulates the P300 amplitude during brain-computer interface use. Clin. Neurophysiol. 121, 1023– 1031. doi: 10.1016/j.clinph.2010. 01.034

Krampen, G. (1981). Differentialpsychologische korrelate von kontrollüberzeugungen. Diagnostica 27, 78–80.

Kubler, A., and Birbaumer, N. (2008). Brain-computer interfaces and communication in paralysis: extinction of goal directed thinking in completely paralysed patients? Clin. Neurophysiol. 119, 2658– 2666. doi: 10.1016/j.clinph.2008. 06.019

Kubler, A., Kotchoubey, B., Hinterberger, T., Ghanayim, N., Perelmouter, J., Schauer, M., et al. (1999). The thought translation device: a neurophysiological approach to communication in total motor paralysis. Exp. Brain Res. 124, 223– 232. doi: 10.1007/s002210050617 Kubler, A., Kotchoubey, B., Kaiser, J., Wolpaw, J. R., and Birbaumer, N. (2001). Brain-computer communication: unlocking the locked in. Psychol. Bull. 127, 358–375. doi: 10. 1037//0033-2909.127.3.358

Kübler, A., Neumann, N., Wilhelm, B., Hinterberger, T., and Birbaumer, N. (2004). Predictability of braincomputer communication. J. Psychophysiol. 18, 121–129. doi: 10. 1027/0269-8803.18.23.121

McFarland, D. J., Miner, L. A., Vaughan, T. M., and Wolpaw, J. R. (2000). Mu and beta rhythm topographies during motor imagery and actual movements. Brain Topogr. 12, 177–186. doi: 10. 1023/A:1023437823106

McFarland, D. J., Sarnacki, W. A., Vaughan, T. M., and Wolpaw, J. R. (2005). Brain-computer interface (BCI) operation: signal and noise during early training sessions. Clin. Neurophysiol. 116, 56–62. doi: 10. 1016/j.clinph.2004.07.004

Mellinger, J., Schalk, G., Braun, C., Preissl, H., Rosenstiel, W., Birbaumer, N., et al. (2007). An MEGbased brain-computer interface (BCI). NeuroImage 36, 581–593.

doi: 10.1016/j.neuroimage.2007. 03.019

Neumann, N., and Birbaumer, N. (2003). Predictors of successful self control during brain-computer communication. J. Neurol. Neurosurg. Psychiatry 74, 1117–1121. doi: 10.1136/jnnp.74.8.1117

Neumann, N., Kubler, A., Kaiser, J., Hinterberger, T., and Birbaumer, N. (2003). Conscious perception of brain states: mental strategies for brain-computer communication. Neuropsychologia 41, 1028– 1036. doi: 10.1016/s0028-3932 (02)00298-1

Nijboer, F., Birbaumer, N., and Kubler, A. (2010). The inﬂuence of psychological state and motivation on brain-computer interface performance in patients with amyotrophic lateral sclerosis—a longitudinal study. Front. Neurosci. 4:55. doi: 10. 3389/fnins.2010.00055

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., et al. (2008). A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916. doi: 10.1016/j.clinph.2008.03.034 Pfurtscheller, G. (1992). Event-related synchronization (ERS): an electrophysiological correlate of cortical areas at rest. Electroencephalogr. Clin. Neurophysiol. 83, 62–69. doi: 10.1016/0013-4694(92)90133-3

Pfurtscheller, G., and Lopes da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857. doi: 10.1016/s13882457(99)00141-8

Pfurtscheller, G., and Neuper, C. (1997). Motor imagery activates primary sensorimotor area in humans. Neurosci. Lett. 239, 65–68. doi: 10. 1016/s0304-3940(97)00889-6

Pfurtscheller, G., Brunner, C., Schlogl, A., and Lopes Da Silva, F. H. (2006).

Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of different motor imagery tasks. NeuroImage 31, 153–159. doi: 10. 1016/j.neuroimage.2005.12.003

Roberts, L. E., Birbaumer, N., Rockstroh, B., Lutzenberger, W., and Elbert, T. (1989). Self-report during feedback regulation of slow cortical potentials. Psychophysiology 26, 392–403. doi: 10.1111/j.1469-8986. 1989.tb01941.x

Ros, T., Moseley, M. J., Bloom, P. A., Benjamin, L., Parkinson, L. A., and Gruzelier, J. H. (2009). Optimizing microsurgical skills with EEG neurofeedback. BMC Neurosci. 10:87. doi: 10.1186/1471-2202-10-87

Rotter, J. B. (1966). Generalized expectancies for internal versus external control of reinforcement. Psychol. Monogr. 80, 1–28. doi: 10. 1037/h0092976

Serruya, M. D., and Kahana, M. J. (2008). Techniques and devices to restore cognition. Behav. Brain Res. 192, 149–165. doi: 10.1016/j.bbr. 2008.04.007

Shenoy, P., Krauledat, M., Blankertz, B., Rao, R. P., and Muller, K. R. (2006). Towards adaptive classiﬁcation for BCI. J. Neural. Eng. 3, R13–R23. doi: 10.1088/1741-2560/3/1/r02

Sterman, M. B. (1996). Physiological origins and functional correlates of EEG rhythmic activities: implications for self-regulation. Biofeedback Self Regul. 21, 3–33. doi: 10.1007/bf 02214147

Sterman, M. B. (2000). Basic concepts and clinical ﬁndings in the treatment of seizure disorders with EEG operant conditioning. Clin. Electroencephalogr. 31, 45–55.

Vernon, D., Egner, T., Cooper, N., Compton, T., Neilands, C., Sheri, A., et al. (2003). The effect of training distinct neurofeedback protocols on aspects of cognitive performance. Int. J. Psychophysiol. 47, 75–85. doi: 10.1016/s0167-8760(02)00091-0

Vidaurre, C., Schlogl, A., Cabeza, R., Scherer, R., and Pfurtscheller, G. (2007). Study of on-line adaptive discriminant analysis for EEG-based brain computer interfaces. IEEE Trans. Biomed. Eng. 54, 550–556. doi: 10.1109/tbme. 2006.888836

Weber, E., Koberl, A., Frank, S., and Doppelmayr, M. (2011). Predicting successful learning of SMR neurofeedback in healthy participants: methodological considerations. Appl. Psychophysiol. Biofeedback 36, 37–45. doi: 10.1007/s10484-0109142-x

Wolpaw, J. R., and McFarland, D. J. (1994). Multichannel EEG-based brain-computer communication. Electroencephalogr. Clin. Neurophysiol. 90, 444–449. doi: 10. 1016/0013-4694(94)90135-x

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 14 April 2013; accepted: 29 July 2013; published online: 15 August 2013. Citation: Witte M, Kober SE, Ninaus M, Neuper C and Wood G (2013) Control beliefs can predict the ability to up-regulate sensorimotor rhythm during neurofeedback training. Front. Hum. Neurosci. 7:478. doi: 10.3389/fnhum.2013.00478 Copyright © 2013 Witte, Kober, Ninaus, Neuper and Wood. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

