ORIGINAL RESEARCH published: 02 June 2015

doi: 10.3389/fnhum.2015.00308

# Effects of user mental state on EEG-BCI performance

Andrew Myrden1,2 and Tom Chau1,2∗

1 Holland Bloorview Kids Rehabilitation Hospital, Bloorview Research Institute, Toronto, ON, Canada, 2 Institute of Biomaterials and Biomedical Engineering, University of Toronto, Toronto, ON, Canada

Changes in psychological state have been proposed as a cause of variation in brain-computer interface performance, but little formal analysis has been conducted to support this hypothesis. In this study, we investigated the effects of three mental states—fatigue, frustration, and attention—on BCI performance. Twelve able-bodied participants were trained to use a two-class EEG-BCI based on the performance of user-speciﬁc mental tasks. Following training, participants completed three testing sessions, during which they used the BCI to play a simple maze navigation game while periodically reporting their perceived levels of fatigue, frustration, and attention. Statistical analysis indicated that there is a signiﬁcant relationship between frustration and BCI performance while the relationship between fatigue and BCI performance approached signiﬁcance. BCI performance was 7% lower than average when self-reported fatigue was low and 7% higher than average when self-reported frustration was moderate. A multivariate analysis of mental state revealed the presence of contiguous regions in mental state space where BCI performance was more accurate than average, suggesting the importance of moderate fatigue for achieving effortless focus on BCI control, frustration as a potential motivating factor, and attention as a compensatory mechanism to increasing frustration. Finally, a visual analysis showed the sensitivity of underlying class distributions to changes in mental state. Collectively, these results indicate that mental state is closely related to BCI performance, encouraging future development of psychologically adaptive BCIs.

Edited by: Aron K. Barbey,

University of Illinois at Urbana-Champaign, USA

Reviewed by: Alissa Fourkas,

National Institutes of Health, USA Hasan Ayaz, Drexel University, USA

Keywords: EEG, brain-computer interface, user mental state, fatigue, frustration, attention

*Correspondence: Tom Chau, Holland Bloorview Kids Rehabilitation Hospital, Bloorview Research Institute, 150 Kilgour Road, Toronto, ON M4G

1. Introduction

Brain-computer interfaces allow information to be conveyed to an external device, such as a computer, using cognitive activity alone (Mak and Wolpaw, 2009). Originally envisioned simply as a means of communication and environmental control for individuals with disabilities (Wolpaw et al., 2002), more and more prospective applications of BCIs have been proposed in recent years for both healthy and disabled individuals. BCIs have been harnessed for recreational purposes in gaming and virtual reality applications, where they provide an alternative input modality by which a simulation can be controlled (Lécuyer et al., 2008). BCIs have also been used to enable creative expression by translating cognitive activity into music and visual art (Miranda, 2006), to track changes in cognitive states such as alertness (Zander and Kothe, 2011), as a neurofeedback tool to achieve altered states of consciousness via meditation (Crowley et al., 2010), and in neurorehabilitation for individuals who have lost motor control due to stroke (Ang et al., 2010).

1R8, Canada tom.chau@utoronto.ca

Received: 19 February 2015

Accepted: 13 May 2015 Published: 02 June 2015

Citation: Myrden A and Chau T (2015) Effects of user mental state on EEG-BCI performance.

Front. Hum. Neurosci. 9:308. doi: 10.3389/fnhum.2015.00308

Frontiers in Human Neuroscience | www.frontiersin.org 1 June 2015 | Volume 9 | Article 308

Most current BCIs use electroencephalography (EEG) as a tool to infer mental state and communicative intent (Lotte et al., 2007). EEG provides a low-resolution spatial map of electrical activity on the cortex (Niedermeyer and da Silva, 2005). Despite this low resolution, it has generally been favored for BCI applications due to its relatively simple setup and low cost. Some recent research has also investigated the usage of hemodynamic imaging technologies such as near-infrared spectroscopy (Sitaram et al., 2007) and transcranial Doppler ultrasound (Myrden et al., 2011), but these technologies cannot currently match the information transfer rate of EEG-BCIs. However, these hemodynamic imaging technologies may be useful in combination with EEG. Recent work on hybrid EEG-NIRS BCIs has shown that simultaneous measurement of electrical and hemodynamic activity on the cerebral cortex may allow for more accurate BCI operation by combining features from both modalities (Leamy et al., 2011; Fazli et al., 2012). More complex arrangements are also possible—Liu et al. (2012) have shown that attention measured based on NIRS may improve the reliability of an EEG-BCI, while Koo et al. (2015) showed that NIRS can be used to detect whether motor imagery has been performed while EEG is used to diﬀerentiate diﬀerent types of motor imagery, allowing the development of a self-paced BCI.

EEG-BCIs that are used for communication and control typically employ one of two paradigms. The ﬁrst depends upon involuntary neuronal reactions to presented stimuli, and has been described as a “reactive BCI” (Zander and Kothe, 2011). This includes BCIs that detect the P300 response to anticipated visual, auditory, or tactile stimuli (Hoﬀmann et al., 2008) and steady-state visually evoked potential (SSVEP) BCIs that detect the ﬂicker frequency of the stimuli on which the user is ﬁxated (Cheng et al., 2002). Both of these types of BCIs allow the user to choose one option from a grid of stimuli and are most commonly used as the basis for a spelling system. The second paradigm depends upon the detection of a voluntary cognitive activation, typically produced by performing a speciﬁc mental task. This has been described as an “active BCI” (Zander and Kothe, 2011). Active BCIs diﬀerentiate two or more mental tasks from each other, allowing the user to employ each task to communicate a diﬀerent message. Diﬀerentiating more than two tasks from each other typically incurs a decrease in classiﬁcation accuracy, and it is rare for more than four mental tasks to be used (Schlögl et al., 2005). Mental tasks used for active BCIs in previous research have included a rest state, motor imagery, mental arithmetic, and a verbal ﬂuency task, among others (Pfurtscheller and Neuper, 2001; Curran and Stokes, 2003; Myrden et al., 2011).

One pervasive challenge in BCI research is the tendency for BCI accuracy to decrease over time due to the non-stationarity of the signals used (Shenoy et al., 2006). It is well-known that class distributions tend to change over time, and maintaining high BCI performance during long sessions and across weeks and months of usage is typically diﬃcult (Shenoy et al., 2006). This inconsistent performance is a signiﬁcant impediment to the adoption of BCIs as access modalities for individuals with disabilities and may also be a signiﬁcant risk factor for the abandonment of BCIs by these individuals (Phillips and Zhao, 1993). It has been proposed that one cause of this inconsistent

performance may be ﬂuctuations in psychological variables such as alertness and distraction (Curran and Stokes, 2003; Millán et al., 2010). Systems that track this type of involuntary ongoing cognitive user state can be categorized as passive BCIs (Zander and Kothe, 2011). Examples include estimation of task engagement and attention (Berka et al., 2007; Ayaz et al., 2012; Hasenkamp et al., 2012; Harrivel et al., 2013), mental workload (Berka et al., 2007; Hirshﬁeld et al., 2009), fatigue (Shen et al., 2008), and emotional state (Sitaram et al., 2011). These passive BCIs each use either EEG, NIRS, or fMRI, allowing them to be integrated with an active or reactive BCI that uses the same modality (or a complementary modality in the case of a hybrid BCI). Such a combination may allow adaptation to ﬂuctuations in mental state, mitigating the observed variation in BCI performance over time. However, it is ﬁrst imperative to verify that these ﬂuctuations in mental state are related to variation in BCI performance, as to the best of our knowledge, this hypothesis has not been formally tested.

This paper investigates the eﬀects of user mental state on BCI performance. Three mental states of particular interest were identiﬁed based on previous work—cognitive fatigue, frustation, and attention (Curran and Stokes, 2003). Subjective self-reported estimations of these three mental states were gathered from BCI users while playing a simple maze navigation game. These ratings were compared to BCI performance to identify relationships between mental state and classiﬁcation accuracy. A multivariate analysis was also performed to identify a region in mental state space for optimal BCI performance. Finally, the class distributions of the rest and active tasks were analyzed in the feature space to determine the eﬀects of changes in mental state on the individual signal features used for classiﬁcation.

2. Materials and Methods

- 2.1. Population Twelve able-bodied participants (two male, average age 27.7 years) were drawn from graduate students and staﬀ at Holland Bloorview Kids Rehabilitation Hospital. Participants had normal or corrected-to-normal vision and refrained from consuming caﬀeine for 4h prior to each session. Participants provided written informed consent, and the experimental protocol was approved by the Holland Bloorview Research Ethics Board.
- 2.2. Instrumentation During each session, electrical signals from the cortex were recorded using a B-Alert X24 wireless EEG headset (Advanced Brain Monitoring, Carlsbad, CA, USA). Signals were recorded from the Fz, F1, F2, F3, F4, Cz, C1, C2, C3, C4, CPz, Pz, P1, P2, and POz locations according to the international 10-20 system (Homan et al., 1987). Signals were band-pass ﬁltered between 2 and 30Hz, and artifacts resulting from eye movements were removed using independent component analysis (Mognon et al., 2011).
- 2.3. Training Sessions Participants completed two training sessions on separate days. The goal of these sessions was to identify a mental task that could

reliably be diﬀerentiated from rest for each participant. Four candidate mental tasks were considered—mental arithmetic, motor imagery, music imagery, and word generation. Multiple tasks were considered because the most eﬀective BCI task typically varies across participants (Guger et al., 2003). The mental arithmetic task required participants to perform a repeated addition or subtraction task in their head. The motor imagery task required participants to imagine performing ﬁngerto-thumb opposition with the hand of their choice. The music imagery task required participants to sing a song of their choice in their heads. The word generation task required participants to silently think of as many words as possible that began with a given letter.

During each training session, participants completed 150 trials. These were evenly divided between the four candidate mental tasks and a rest task, during which participants were instructed to relax and let theirminds wander. Each trial was 15 s long, consisting of a 5-s preparation period during which a visual cue was displayed to indicate the required task for the trial; a 5-s task period during which the participant performed the required task; and a 5-s cool-down period before the next trial began. Participants were instructed to remain silent and still during the preparation and task periods tominimize motor artifacts. The visual cue for each trial was displayed on a computer monitor using a custom LabVIEW interface. To avoid mislabeling training data, participants were prompted to report whether they had successfully completed each trial at the end of the cool-down period. This was done through an on-screen dialog box that had to be completed before the next trial could begin. At the end of each training session, participants ranked the four candidate mental tasks in order of preference for future BCI usage.

- 2.4. BCI Development Following the completion of the training sessions, a BCI was trained to diﬀerentiate each candidate mental task from the rest task. There were a total of 60 trials for each task. For each signal from each electrode, the spectral power within the signal in 1-Hz increments (from 0–1 to 29–30Hz) was estimated by summing the squares of the corresponding Fourier coeﬃcients. These local spectral power estimates yielded 450 individual features (30 frequencies from 15 electrodes) for each trial.

Two feature selection methods were used to reduce the dimensionality of the feature set to between 1 and 12 features for classiﬁcation. In the ﬁrst method, a fast correlation-based ﬁlter (FCBF) directly reduced the dimensionality from 450 to the target number of features. This resulted in most of the feature set being discarded. In the second, this 450-dimensional feature set was reduced by clustering highly correlated features and performing principal component analysis (PCA) on each cluster to compute 75 intermediate features before using a FCBF to arrive at the target number of features. The latter approach was included to accommodate tasks that elicited widely distributed cortical activation at varying frequencies.

For each feature space dimensionality, a linear discriminant analysis (LDA) classiﬁer (Bishop, 2006) was trained for each candidate task and feature selection method. Ten runs of ten-fold cross-validation were performed and the average classiﬁcation

accuracy across the folds was computed. This resulted in a set of 24 diﬀerent classiﬁers for each task. The classiﬁer that yielded the highest classiﬁcation accuracy was identiﬁed for each task and the tasks were then ranked by their maximum accuracy. Participants were presented with these accuracy-based task rankings along with their own rankings of task preference. Based on this information, they were allowed to choose which active task they wanted to use for the remainder of the study.

- 2.5. Testing Sessions Participants completed three testing sessions on separate days. During these sessions, they used a BCI based on the task that they selected at the end of the training sessions to play a simple maze navigation game that was programmed in LabVIEW. Participants attempted to complete a series of 10 mazes. Each session started with the ﬁrst (and simplest) maze. Mazes grew more diﬃcult as the session progressed, but this was primarily due to the number of intersections between the origin and destination rather than the cognitive diﬃculty of plotting a path through the maze.

Participants navigated through the maze by moving from intersection to intersection. Their current position was indicated by an image of a person, while the destination was indicated by an image of a door. At each intersection, there were between two and four potential directions (labeled as north, south, east, and west) in which movement to another intersection was possible. Participants were prompted to select the direction in which they wanted to travel from an on-screen window. Subsequently, the potential navigational directions were highlighted one at a time for 5 s each, constituting four task periods. Each task period was punctuated with a 5-s break. When a direction was highlighted, appropriate task cues were shown, namely the cue for the active task for the selected direction of travel and the cue for the rest task for all other directions. The selected direction of travel was recorded only to label data for future analysis and to ensure that appropriate task cues were presented during each task period. An example of the game, depicting an initial intersection, a BCI decision, and the subsequent intersection, is shown in Figure 1.

The EEG recording from each 5-s task period was classiﬁed in real-time by the BCI. When the task period had been completed for each potential direction, the BCI decided which task period was most likely to represent the active task rather than the rest task, and the image on screen was moved in the corresponding direction. However, before this movement was displayed, the participant was prompted to self-report their perceived levels of fatigue, frustration, and attention. Each of these mental states was rated by moving a slider on a continuous scale from 0 to 1 with textual anchors at either end (e.g., “Least fatigued” and “Most fatigued”). A new maze was automatically loaded when the current maze was completed (i.e., when the participant navigated to the door) and the session was terminated either after completion of the tenth maze or once 50min had elapsed.

- 3. Results

3.1. Choice of BCI Task

Oﬄine performance for each participant during the training sessions is summarized in Table 1. Word generation was selected

|[Figure 1]<br><br>FIGURE 1 | Maze navigation. The position of the participant is represented by the image of a person and the destination by the image of a door. The participant chose to move east at Intersection 1, so they are shown a cue for the word generation task when the arrow pointing east is highlighted. A cue for the rest task was shown when the north and west arrows were highlighted. The BCI analyzed the task period from each direction, predicting that the north and west task periods represented rest tasks (green bars)<br><br>while the east task represented the word generation task (red bar). Consequently, the BCI moved the participant to Intersection 2, ignoring the intermediate intersection where the only options would have been to continue moving in the same direction or to go back to the last intersection. At the new intersection, the participant chose to move west to continue approaching the exit, so a new word generation cue was shown when that direction was highlighted.|
|---|

TABLE 1 | Classiﬁcation accuracies for each participant during the training sessions for the mental arithmetic (MA), motor imagery (MI), music imagery (MuI), and word generation (WG) tasks.

Participant MA% MI% MuI% WG% Selected task

- 1 87 95 67 74 MI
- 2 63 60 63 70 WG
- 3 58 75 68 50 MI
- 4 65 64 66 70 WG
- 5 80 77 62 82 WG
- 6 62 55 57 60 WG
- 7 N/A 69 61 69 WG
- 8 50 71 65 71 WG
- 9 56 61 59 66 WG
- 10 82 81 73 83 WG
- 11 69 N/A 71 64 MuI
- 12 66 55 56 57 WG

Word generation was selected by nine participants, motor imagery by two participants, and music imagery by the remaining participant. Entries labeled as “N/A” indicate occasions when a mental task was removed from the second training session for a participant due to both poor classiﬁcation accuracy during the ﬁrst training session and placement as the least preferred task for that participant following the ﬁrst training session.

as the optimal BCI task by nine participants, motor imagery by two participants, and music imagery by the ﬁnal participant. The average classiﬁcation accuracy of the selected task was 72.4%. This exceeded theminimal BCI performance criteria of 70% despite the short task duration and relatively small selection of electrodes. Since the analysis focused on the eﬀects of mental state on BCI performance, it was not necessary to obtain extremely high accuracy. In fact, high accuracy may have inhibited the analysis, as it is likely that a smaller range of ratings would be

induced for each mental state if BCI performance was close to perfect.

3.2. Online BCI Performance

- Participant 7 was excluded from this analysis as he or she was not able to control the BCI during the testing sessions, and
- Participant 8 was unable to attend the testing sessions. One testing session for each of Participants 2 and 3 could not be analyzed due to signal quality issues. Three testing sessions were analyzed for all other participants. Although retraining the BCI after each testing session for all participants would have resulted in higher accuracies, it was avoided tominimize the number of factors aﬀecting classiﬁcation accuracy. Consequently, BCIs were retrained after testing sessions only when the experimenters felt it absolutely necessary in order to maintain motivation for participants. This occurred only for the ﬁnal testing sessions for Participants 11 and 12. All other participants used the same BCI for all testing sessions.

Two metrics were considered: the balanced individual classiﬁcation accuracy, referring simply to the average of sensitivity and speciﬁcity for the individual tasks; and the collective classiﬁcation accuracy, referring to the proportion of maze intersections at which the BCI correctly identiﬁed the intended direction of transit. There were typically three or four potential directions of transit, so the collective accuracy was expected to be lower than the individual accuracy.

Figures 2, 3 depict the individual and collective accuracies, respectively, for each participant during each online session. Despite the non-adaptive classiﬁer, four of ten participants exceeded the 70% threshold for individual classiﬁcation accuracy during one or more testing sessions. Furthermore, ﬁve of ten participants achieved a collective classiﬁcation accuracy that exceeded this threshold during one or more sessions.

Both individual and collective classiﬁcation accuracy increased in the second and third sessions, suggesting that participants became more proﬁcient with the BCI over time. For the third session, both individual and collective classiﬁcation accuracy neared the 70% threshold when averaged across all participants.

- 3.3. Effects of Fatigue, Frustration, and Attention on BCI Performance For each participant, self-reported ratings for each mental state during each session were quantized to two levels, deﬁned as, for example, “low fatigue” and “high fatigue.” The cut point for quantization was varied for each participant and mental state to ensure that each level contained as close to the same amount of

|[Figure 2]<br><br>FIGURE 2 | Balanced individual classiﬁcation accuracies for all participants during each session.|
|---|

|[Figure 3]<br><br>FIGURE 3 | Collective classiﬁcation accuracies for all participants during each session.|
|---|

trials as possible. Each individual trial was categorized as either low or high for each mental state and the classiﬁcation accuracy at each level across all participants was computed. By ensuring that each session was equally represented in the low and high categories for each mental state, this approach controlled for learning eﬀects. These results are presented in Table 2 for the individual classiﬁcation accuracy.

Classiﬁcation accuracy at low fatigue was about 2.5% inferior when compared to high fatigue, a result that approached signiﬁcance using the chi-squared test (p = 0.088). The 4% diﬀerence in classiﬁcation accuracy between low and high frustration was statistically signiﬁcant (p = 0.0038). There was no signiﬁcant diﬀerence between classiﬁcation accuracy at low attention and high attention levels. However, these ﬁndings collectively indicate that there is a signiﬁcant relationship between BCI performance and mental state.

To investigate whether the choice of mental task inﬂuenced the relationship between mental state and BCI performance, participants were split into two categories—those who chose word generation as the active task and those who did not—and the preceding analysis was repeated. The results for each group are depicted in Table 3. While frustration appeared to aﬀect the two groups similarly, fatigue had more impact on the WG group and attention on the not-WG group. However, due to the small sample sizes incurred by splitting the group in two, further research with control groups of equal size for each task would be necessary to draw signiﬁcant conclusions.

Since the two-level quantization of each rating was a simplistic means of investigating these eﬀects, further analysis was conducted using normalized values for each mental state. For each session, the self-reported ratings for each mental state were normalized to zero mean and unit variance. For each mental state, all trials across all participants were then sorted

- TABLE 2 | Individual classiﬁcation accuracies at low and high levels for each mental state. Level Fatigue Frustration Attention

Low 62.6 61.7 63.8 High 65.0 65.7 64.2

Classiﬁcation accuracies were based on 4814 trials across ten participants, and each level contained roughly the same number of trials.

- TABLE 3 | Classiﬁcation accuracies at low and high levels for each mental state. Task Level Fatigue Frustration Attention

WG Low 61.5 60.7 62.3 High 64.0 64.4 63.3

Not WG Low 66.7 64.3 68.8 High 67.2 68.8 66.0

Classiﬁcation accuracies were based on 4814 trials across ten participants, and each level contained roughly the same number of trials.

by their normalized rating. Since each trial was also associated with a classiﬁcation result (i.e., either a correct or incorrect decision by the BCI), this allowed the construction of a binary sequence representing BCI performance over the full range of normalized ratings. This sequence was smoothed tominimize the noise produced by the usage of individual classiﬁcation results, resulting in a classiﬁcation accuracy curve Cactual for each state.

Since ratings from each participants were not uniformly distributed within the range of ratings for each state, Cactual was biased due to individual variations in classiﬁcation accuracy. To mitigate this, an expected classiﬁcation accuracy curve Cexpected was constructed by replacing the actual classiﬁcation result from each trial with the average classiﬁcation accuracy from the session within which each trial originated. The same smoothing process was performed, and the eﬀects of mental state on BCI performance were assessed based on the diﬀerence between Cactual and Cexpected, as depicted in Figure 4. Through random sampling, the diﬀerence between actual and expected classiﬁcation accuracy was observed to follow a normal distribution with a 90% conﬁdence interval of 0 ± 0.032. The bounds of this conﬁdence interval are depicted in Figure 4.

These ﬁgures support the results from Table 2 while also providing a higher-resolution view of the trends in classiﬁcation accuracy. Performance was poor for low levels of self-reported fatigue, with the diﬀerence between actual and expected accuracy surpassing −7%, well outside of the 90% conﬁdence interval. For frustration, higher classiﬁcation accuracies than expected were exhibited for moderate values, peaking at approximately +7%. In contrast, the diﬀerence between actual and expected classiﬁcation accuracy over the full range of attention ratings was small, remaining almost entirely within the 90% conﬁdence interval.

|[Figure 4]<br><br>FIGURE 4 | Difference between actual and expected classiﬁcation accuracy across all participants for normalized values of self-reported fatigue, frustration, and attention ratings. The distributions of fatigue and frustration ratings were positively skewed while the distribution of attention ratings was negatively skewed, causing the apparent variation in range between states. Dotted lines represent the 90% conﬁdence interval for the mean of the deviation between actual and expected classiﬁcation accuracy.|
|---|

- 3.4. Multivariate Analysis The previous analysis considered only the eﬀects of each individual mental state. A multivariate analysis of the eﬀects of mental state on BCI performance was also conducted by analyzing the eﬀects of each combination of two states. The raw self-reported ratings were extracted for each participant without quantization. A grid was constructed across the full range from 0 to 1 for each mental state with a resolution of 0.01. At each point within the grid, the nearest 500 trials, regardless of participant, were identiﬁed. For this set of 500 trials, the actual

classiﬁcation accuracy Cactual was computed. In addition, the expected classiﬁcation accuracy was computed as:

Cexpected = pwpCp,s (1)

where wp represents the proportion of the nearest 500 trials which originated from Participant p and Cp,s represents the overall classiﬁcation accuracy of all trials originating from session s for Participant p. The diﬀerence between actual and expected classiﬁcation accuracies was used to characterize this point. The results of this process are depicted in Figures 5–7 for fatigue and frustration; fatigue and attention; and frustration and attention, respectively. Again, the diﬀerence between actual and expected

classiﬁcation accuracy was compared to the 90% conﬁdence interval, established previously as 0 ± 0.032.

The fatigue-frustration and fatigue-attention graphs reveal relatively contiguous optimal regions for BCI control. For fatigue-frustration, two optimal regions are apparent—one from moderate to high fatigue and low to moderate frustration and one from low to moderate fatigue and moderate to high frustration. Of these, the former is larger and more consistent across a wide region in mental state space. For fatigue-attention, there is an optimal region for moderate to high fatigue and attention. Again, these ﬁndings corroborate the univariate analyses despite the usage of raw ratings rather than quantized or normalized ratings.

The graph for frustration-attention is more equivocal. The area within mental state space that exceeded the bounds of the 90% conﬁdence interval was small and located in the high frustration and high attention region. This may imply that high attention is necessary to compensate for high frustration. However, given the small size of this region, this could also potentially be a result of random variation.

3.5. Effects of Mental State on Class Distributions

The eﬀects of mental state on BCI performance were also analyzed from a signal feature perspective. As in the univariate

|[Figure 5]<br><br>FIGURE 5 | Two-dimensional view of the difference between actual and expected classiﬁcation accuracies as a function of fatigue and frustration. The middle graph depicts the variation in classiﬁcation<br><br>accuracy as shown on the legend on the left, and the right graph shows only regions for which the difference exceeded 3.2% (in green) or was less than −3.2% (in red).|
|---|

|[Figure 6]<br><br>FIGURE 6 | Two-dimensional view of the difference between actual and expected classiﬁcation accuracies as a function of fatigue and attention. The middle graph depicts the variation in classiﬁcation accuracy<br><br>as shown on the legend on the left, and the right graph shows only regions for which the difference exceeded 3.2% (in green) or was less than −3.2% (in red).|
|---|

|[Figure 7]<br><br>FIGURE 7 | Two-dimensional view of the difference between actual and expected classiﬁcation accuracies as a function of frustration and attention. The middle graph depicts the variation in classiﬁcation<br><br>accuracy as shown on the legend on the left, and the right graph shows only regions for which the difference exceeded 3.2% (in green) or was less than −3.2% (in red).|
|---|

analyses, all trials for each participant were split into low and high categories for each mental state. In this case, the LDA classiﬁer trained for each participant after the training sessions was used to project each trial to one dimension. The separability of the rest and active tasks were then estimated by computing the Fisher score for each projection. The Fisher score is deﬁned as (Foley and Sammon, 1975):

|µ1 − µ2|2 s21 + s22

J =

(2)

where µ1 and s1 represent the mean and the variance of the projected values for the rest class and µ2 and s2 represent the mean and the variance of the projected values for the active class. The results of this analysis are depicted in Figure 8.

These results suggests that the classiﬁers trained based on the training sessions were much less eﬀective during the testing sessions, accentuating the importance of frequent retraining. However, the average diﬀerences between Fisher scores for low and high ratings for each mental state also suggest that, for some participants, mental state may aﬀect class distributions in feature space.

To verify this, the class distributions for the rest and active tasks under diﬀerent mental state conditions were inspected based on two of the features used for classiﬁcation. Figure 9 shows the class distributions of each task for Participant 4 under low and high attention conditions. The center of each ellipse represents the class mean under that condition while the size of the ellipse represents the 67% conﬁdence interval for the class, oriented along the eigenvectors of the covariance matrix. Even in this low-dimensional space (the classiﬁer for this participant used 10 features), it is evident that modulations in mental state aﬀect

class distributions, as the two classes are nearly separable when attention is high but inseparable when attention is low.

4. Discussion

4.1. Optimal Mental State for BCI Control

It is clear from our univariate analyses that mental state and BCI performance are closely intertwined. However, some of our observations were surprising. Online BCI performance was signiﬁcantly less accurate during the trials for which participants reported the lowest fatigue levels and signiﬁcantly more accurate during the trials for which participants reported high frustration levels. This was observed when each trial was categorized by quantized ratings for each state and also when ratings were normalized within each session. Based on the same analyses, attention seemed to have little impact on BCI performance. Analysis based on the choice of active task suggests that there may be task-related eﬀects, but further investigation would be necessary for statistical veriﬁcation.

Self-reported mental state ratings were quantized and normalized for these initial analyses in an attempt to account for the fact that diﬀerent participants may have anchored their ratings diﬀerently on the continuous scales used for each state. However, one shortcoming of this approach was that it ignored diﬀerences in average mental state. Since one participant reporting a higher average fatigue level than another could be either a result of variation in anchoring or a legitimate diﬀerence in fatigue levels, the raw ratings were used for the multivariate analysis in order to compare the results.

This multivariate analysis suggested the presence of optimal mental state regions for BCI control. The most interesting

|[Figure 8]<br><br>FIGURE 9 | Class distributions for the rest and active task for Participant 4 during the testing sessions. Each ellipse represents the distribution of one class (the rest task for solid lines and the active task for dashed lines) under one categorization of attention levels (low in blue lines, high in red lines). While classes were nearly separable when attention was high, they were unseparable when attention was low.|
|---|

|[Figure 9]<br><br>FIGURE 8 | Average Fisher scores across all participants during training sessions and testing sessions. Data from the testing sessions were split into low and high categories for each mental state before the Fisher score was computed. Error bars are extremely wide due to large variance in class separability (and thus classiﬁcation accuracy) between participants—see Table 1.|
|---|

observation came from the fatigue-attention analysis, which showed that the highest accuracies occurred when moderate values were maintained for fatigue and moderate to high values for attention. BCI performance decreased markedly when these states varied, particularly for low fatigue and high attention. The multivariate analysis also presented a more nuanced portrait of the eﬀects of each mental state on BCI perfomance. The fatigue-frustration and frustration-attention cases both showed interactions between pairs of states. In general, the former analysis showed that optimal performance occurred for either moderate fatigue and high frustration or high frustration and low fatigue. In contrast, the low fatigue and low frustration case exhibited notably poor performance.

Although there is no pre-existing BCI literature for comparison, some support for these results can be found in other disciplines. The state of psychological ﬂow has been identiﬁed as a requirement for excellent performance in many ﬁelds (Jackson et al., 2001; Demerouti, 2006; de Manzano et al., 2010). Flow is characterized by what Romero describes as eﬀortless attention, a state of deep concentration where perceived eﬀort is generally lower than would be expected (Romero and Calvillo-Gámez, 2014). This is contrasted with eﬀortful attention, in which the perceived eﬀort to achieve focus is quite high and individuals must ﬁght to maintain deep concentration. We hypothesize that, due to the high perceived eﬀort, eﬀortful attention is likely to be characterized by higher self-reported fatigue and potentially higher self-reported attention than eﬀortless concentration. Since optimal performance can be expected during eﬀortless attention, this could produce the pattern seen in Figure 6.

The role of frustration has also attracted attention in previous research. In learning studies, it has been observed that frustration, in moderation, is not necessarily a negative factor (Baker et al., 2010). In fact, the presence of frustration during a diﬃcult task may simply represent motivation, which is a factor likely to improve performance. However, studies have also observed that high frustration induces boredom, reducing attention and leading to poor performance (D’Mello and Graesser, 2012). This implies that optimal performance may be associated with moderate frustration, corroborating our ﬁndings, particularly those depicted in Figure 4.

There is one important caveat regarding this study. It has been shown that ﬂuctuations in mental state are related to ﬂuctuations in BCI performance. However, it stands to reason that since these ﬂuctuations aﬀect the underlying class distributions of the active and rest tasks, as seen in Figure 9, the classiﬁers used for each BCI were dependent upon the mental state experienced by each participant during the training sessions. Consequently, it may be that the optimal mental state for BCI control is simply that which most closely approximates the mental state from the training sessions. However, given the length of each training session, the commensurate unlikelihood that mental state was consistent throughout, and the unusual topography of the optimal mental state regions in Figures 5–7, it is more likely that the results were aﬀected by both the mental state during the training sessions and the inherent superiority of certain psychological conditions for BCI control. Regardless of which factor is most responsible for the relationship between mental state and BCI performance,

these results strongly suggest that such a relationship does exist. This motivates future investigation of psychologically adaptive BCIs.

4.2. Toward Psychologically Adaptive BCIs

It has been proposed that there are two ways in which a computer system can adapt to information regarding the cognitive state of a user. These are overt adaptation, in which the adaptation is apparent to the user, and covert adaptation, in which it is not apparent to the user (Fairclough, 2009). These deﬁnitions can also be applied to the design of psychologically adaptive BCIs.

Overt adaptation, although potentially more eﬀective than covert adaptation for modifying user state, also has a potentially higher cost (Fairclough, 2009). For a BCI, overt adaptation would require an attempt to modify user mental state to bring it closer to the optimal region, likely taking the form of an adaptive user interface (Tan and Nijholt, 2010). Such an interface could use targeted stimuli or helpful feedback to mitigate undesirable changes in mental state (Fairclough, 2009; Tan and Nijholt, 2010). The interface could also take more drastic steps, potentially going so far as to automatically deactivate the BCI when extremely low attention is detected, reactivating only when the user’s attention has returned. The interface could even modify the timing variables of the BCI, extending task durations when it is likely that classiﬁcation will be inaccurate, a psychologically-driven approach with some similarities to the evidence accumulation algorithms that are often used for online classiﬁcation. The danger of overt adaptation lies in the potential for false alarms (Fairclough, 2009). Explicit interventions that are not required may actually further inhibit BCI control by inducing additional frustration or distraction. It may be wise to use overt adaptation sparingly (Fairclough, 2009).

Covert adaptation, on the other hand, could involve modiﬁcations to the classiﬁer itself. There are several potential methods by which this could be implemented. First, we observed in Figures 2, 3 that there was little diﬀerence between individual and collective classiﬁcation accuracy even though the individual accuracy was based on a binary decision and the collective accuracy on a decision that typically involved three or four options. This implies, for the LDA classiﬁers that were used, that there was more diﬃculty locating an appropriate value for the bias parameter than for the weight vector. Thus, an adaptive bias parameter based on mental state may allow for covert adaptation without repeated classiﬁer retraining. Second, given the eﬀects of mental state on class distribution observed in Figure 9, it is possible that selective online resampling of the training set and retraining of a simple classiﬁer (such as LDA) could be implemented. This would require online estimation of user mental state, the selection of the training points most closely matching this current mental state, and the training of a classiﬁer based on this subset of the training data. Since these adaptations would go unnoticed by the BCI user, they could be employed as frequently as necessary (Fairclough, 2009).

There are two signiﬁcant limitations for any psychologically adaptive BCI. First, it is obviously necessary to achieve accurate detection of these changes in mental state. Our group is currently working on achieving reliable diﬀerentiation between low and

high values of the three mental states in question. Second, any psychological adaptation that is implemented must be adaptive in itself. Signiﬁcant diﬀerences were observed across participants in terms of the reactivity of BCI performance to changes in mental state, and it is unlikely that a “one size ﬁts all” approach will be suﬃcient.

- 5. Conclusions

In this study, we investigated the eﬀects of mental state on BCI performance. We observed that the relationships between these variables were complex, rather than monotonic. There appear to be optimal operating conditions where fatigue, frustration, and attention levels are most appropriate for eﬀective control of

an EEG-BCI. Moreover, signal features are aﬀected by changes in mental state, potentially necessitating classiﬁer adaptation. Future work should consider the development of BCIs that display both overt adaptation to keep user mental state within the optimal region and covert adaptation that automatically modiﬁes the BCI classiﬁcation algorithm to adapt to changes in mental state. This will allow the development of BCIs that are more robust to changes in mental state.

Acknowledgments

This research was supported by the University of Toronto and the Natural Sciences and Engineering Research Council of Canada (NSERC).

References

Ang, K. K., Guan, C., Sui Geok Chua, K., Ang, B. T., Kuah, C., Wang, C., et al. (2010). “Clinical study of neurorehabilitation in stroke using EEG-based motor imagery brain-computer interface with robotic feedback,” in Engineering in Medicine and Biology Society (EMBC), 2010 Annual International Conference of the IEEE (Buenos Aires: IEEE), 5549–5552.

Ayaz, H., Shewokis, P. A., Bunce, S., Izzetoglu, K., Willems, B., and Onaral, B.

(2012). Optical brain monitoring for operator training and mental workload assessment. Neuroimage 59, 36–47. doi: 10.1016/j.neuroimage.2011.06.023

Baker, R. S., D’Mello, S. K., Rodrigo, M. M. T., and Graesser, A. C. (2010). Better to be frustrated than bored: The incidence, persistence, and impact of learners’ cognitive-aﬀective states during interactions with three diﬀerent computerbased learning environments. Int. J. Hum. Comput. Stud. 68, 223–241. doi: 10.1016/j.ijhcs.2009.12.003

Berka, C., Levendowski, D. J., Lumicao, M. N., Yau, A., Davis, G., Zivkovic, V. T., et al. (2007). EEG correlates of task engagement and mental workload in vigilance, learning, and memory tasks. Aviat. Space Environ. Med. 78(Suppl. 1), B231–B244.

Bishop, C. M. (2006). Pattern Recognition and Machine Learning, Vol. 4. New York, NY: Springer.

Cheng, M., Gao, X., Gao, S., and Xu, D. (2002). Design and implementation of a brain-computer interface with high transfer rates. IEEE Trans. Biomed. Eng. 49, 1181–1186. doi: 10.1109/TBME.2002.803536

Crowley, K., Sliney, A., Pitt, I., and Murphy, D. (2010). “Evaluating a brain-computer interface to categorise human emotional response,” in IEEE 10th International Conference on Advanced Learning Technologies (Sousse), 276–278.

Curran, E. A., and Stokes, M. J. (2003). Learning to control brain activity: a review of the production and control of EEG components for driving brain– computer interface (bci) systems. Brain Cogn. 51, 326–336. doi: 10.1016/S02782626(03)00036-8

de Manzano, Ö., Theorell, T., Harmat, L., and Ullén, F. (2010). The psychophysiology of ﬂow during piano playing. Emotion 10, 301. doi: 10.1037/a0018432

Demerouti, E. (2006). Job characteristics, ﬂow, and performance: the moderating role of conscientiousness. J. Occup. Health Psychol. 11:266. doi: 10.1037/10768998.11.3.266

D’Mello, S., and Graesser, A. (2012). Dynamics of aﬀective states during complex learning. Learn. Instr. 22, 145–157. doi: 10.1016/j.learninstruc.2011.10.001 Fairclough, S. H. (2009). Fundamentals of physiological computing. Interact. Comput. 21, 133–145. doi: 10.1016/j.intcom.2008.10.011

Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Müller, K.-R., et al. (2012). Enhanced performance by a hybrid NIRS–EEG brain computer interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084 Foley, D. H., and Sammon, J. W. (1975). An optimal set of discriminant vectors.

IEEE Trans. Comput. 100, 281–289. doi: 10.1109/T-C.1975.224208

Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain-computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147. doi: 10.1109/TNSRE.2003.814481

Harrivel, A. R., Weissman, D. H., Noll, D. C., and Peltier, S. J. (2013). Monitoring attentional state with fNIRS. Front. Hum. Neurosci. 7: 861. doi: 10.3389/fnhum.2013.00861

Hasenkamp, W., Wilson-Mendenhall, C. D., Duncan, E., and Barsalou, L. W. (2012). Mind wandering and attention during focused meditation: a ﬁnegrained temporal analysis of ﬂuctuating cognitive states. Neuroimage 59, 750–760. doi: 10.1016/j.neuroimage.2011.07.008

Hirshﬁeld, L. M., Chauncey, K., Gulotta, R., Girouard, A., Solovey, E. T., Jacob, R. J., et al. (2009). “Combining electroencephalograph and functional near infrared spectroscopy to explore users mental workload,” in Foundations of Augmented Cognition. Neuroergonomics and Operational Neuroscience, eds D. D. Schmorrow, I. V. Estabrooke, and M. Grootjen (San Diego, CA: Springer), 239–247.

Hoﬀmann, U., Vesin, J.-M., Ebrahimi, T., and Diserens, K. (2008). An eﬃcient P300-based brain–computer interface for disabled subjects. J. Neurosci. Methods 167, 115–125. doi: 10.1016/j.jneumeth.2007. 03.005

Homan, R. W., Herman, J., and Purdy, P. (1987). Cerebral location of international 10–20 system electrode placement. Electroencephalogr. Clin. Neurophysiol. 66, 376–382. doi: 10.1016/0013-4694(87)90206-9

Jackson, S. A., Thomas, P. R., Marsh, H. W., and Smethurst, C. J. (2001). Relationships between ﬂow, self-concept, psychological skills, and performance. J. Appl. Sport Psychol. 13, 129–153. doi: 10.1080/104132001753149865

Koo, B., Lee, H.-G., Nam, Y., Kang, H., Koh, C. S., Shin, H.-C., et al. (2015). A hybrid NIRS-EEG system for self-paced brain computer interface with online motor imagery. J. Neurosci. Methods 244, 26–32. doi: 10.1016/j.jneumeth.2014.04.016

Leamy, D. J., Collins, R., and Ward, T. E. (2011). “Combining fNIRS and EEG to improve motor cortex activity classiﬁcation during an imagined movementbased task,” in Foundations of Augmented Cognition. Directing the Future of Adaptive Systems, eds D. D. Schmorrow and C. M. Fidopiastis (Orlando, FL: Springer), 177–185.

Lécuyer, A., Lotte, F., Reilly, R. B., Leeb, R., Hirose, M., Slater, M., et al. (2008). Brain-computer interfaces, virtual reality, and videogames. IEEE Comput. 41, 66–72. doi: 10.1109/MC.2008.410

Liu, Y., Ayaz, H., Curtin, A., Shewokis, P. A., and Onaral, B. (2012). “Detection of attention shift for asynchronous P300-based BCI,” in Engineering in Medicine and Biology Society (EMBC), 2012 Annual International Conference of the IEEE (San Diego, CA: IEEE), 3850–3853.

Lotte, F., Congedo, M., Lécuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain–computer interfaces. J. Neural Eng. 4, R1–R13. doi: 10.1088/1741-2560/4/2/r01

Mak, J. N., and Wolpaw, J. R. (2009). Clinical applications of brain-computer interfaces: current state and future prospects. IEEE Rev. Biomed. Eng. 2, 187–199. doi: 10.1109/RBME.2009.2035356

Millán, J. D. R., Rupp, R., Müller-Putz, G. R., Murray-Smith, R., Giugliemma, C., Tangermann, M., et al. (2010). Combining brain–computer interfaces and assistive technologies: state-of-the-art and challenges. Front. Neurosci. 4: 161. doi: 10.3389/fnins.2010.00161

Miranda, E. R. (2006). Brain-computer music interface for composition and performance. Int. J. Disabil. Hum. Dev. 5, 119–126. doi: 10.1515/IJDHD.2006.5.2.119

Mognon, A., Jovicich, J., Bruzzone, L., and Buiatti, M. (2011). Adjust: an automatic EEG artifact detector based on the joint use of spatial and temporal features. Psychophysiology 48, 229–240. doi: 10.1111/j.1469-8986.2010. 01061.x

Myrden, A. J., Kushki, A., Sejdi´c, E., Guerguerian, A.-M., and Chau, T. (2011). A brain-computer interface based on bilateral transcranial Doppler ultrasound. PLOS ONE 6:e24170. doi: 10.1371/journal.pone.0024170

Niedermeyer, E., and da Silva, F. L. (2005). Electroencephalography: Basic Principles, Clinical Applications, and Related Fields. Philadelphia, PA: Lippincott Williams & Wilkins.

Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct braincomputer communication. Proc. IEEE 89, 1123–1134. doi: 10.1109/5. 939829

Phillips, B., and Zhao, H. (1993). Predictors of assistive technology abandonment. Assist. Technol. 5, 36–45. doi: 10.1080/10400435.1993.10132205 Romero, P., and Calvillo-Gámez, E. (2014). An embodied view of ﬂow. Interact. Comput. 26, 513–527.

Schlögl, A., Lee, F., Bischof, H., and Pfurtscheller, G. (2005). Characterization of four-class motor imagery EEG data for the BCI-competition 2005. J. Neural Eng. 2:L14. doi: 10.1093/iwc/iwt051

Shen, K.-Q., Li, X.-P., Ong, C.-J., Shao, S.-Y., and Wilder-Smith, E. P. (2008). Eeg-based mental fatigue measurement using multi-class support vector

machines with conﬁdence estimate. Clin. Neurophysiol. 119, 1524–1533. doi: 10.1016/j.clinph.2008.03.012

Shenoy, P., Krauledat, M., Blankertz, B., Rao, R. P., and Müller, K.-R.

(2006). Towards adaptive classiﬁcation for BCI. J. Neural Eng. 3, R13. doi: 10.1088/1741-2560/3/1/R02

Sitaram, R., Lee, S., Ruiz, S., Rana, M., Veit, R., and Birbaumer, N. (2011). Real-time support vector classiﬁcation and feedback of multiple emotional brain states. Neuroimage 56, 753–765. doi: 10.1016/j.neuroimage.2010.08.007

Sitaram, R., Zhang, H., Guan, C., Thulasidas, M., Hoshi, Y., Ishikawa, A., et al. (2007). Temporal classiﬁcation of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain–computer interface. Neuroimage 34, 1416–1427. doi: 10.1016/j.neuroimage.2006.11.005

Tan, D., and Nijholt, A. (eds.). (2010). “Brain-computer interfaces and human-computer interaction,” in Brain-Computer Interfaces (London, UK: Springer), 3–19.

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain–computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Zander, T. O., and Kothe, C. (2011). Towards passive brain–computer interfaces: applying brain–computer interface technology to human–machine systems in general. J. Neural Eng. 8:025005. doi: 10.1088/1741-2560/8/2/025005

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2015 Myrden and Chau. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

