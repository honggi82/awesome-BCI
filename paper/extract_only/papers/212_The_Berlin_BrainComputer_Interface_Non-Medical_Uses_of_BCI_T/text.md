www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  1
Review Article
published: 08 December 2010
doi: 10.3389/fnins.2010.00198
The Berlin brain–computer interface: non-medical uses of  
BCI technology
Benjamin Blankertz1,2*, Michael Tangermann1, Carmen Vidaurre1, Siamac Fazli1, Claudia Sannelli1,  
Stefan Haufe1, Cecilia Maeder1, Lenny Ramsey1,3, Irene Sturm1, Gabriel Curio4 and Klaus-Robert Müller1
1	 Machine Learning Laboratory, Berlin Institute of Technology, Berlin, Germany
2	 Intelligent Data Analysis Group, Fraunhofer FIRST, Berlin, Germany
3	 Rudolf Magnus Institute, Utrecht, Netherlands
4	 Department of Neurology, Charité – Campus Benjamin Franklin, Berlin, Germany
Brain–computer interfacing (BCI) is a steadily growing area of research. While initially BCI research 
was focused on applications for paralyzed patients, increasingly more alternative applications in 
healthy human subjects are proposed and investigated. In particular, monitoring of mental states 
and decoding of covert user states have seen a strong rise of interest. Here, we present some 
examples of such novel applications which provide evidence for the promising potential of BCI 
technology for non-medical uses. Furthermore, we discuss distinct methodological improvements 
required to bring non-medical applications of BCI technology to a diversity of layperson target 
groups, e.g., ease of use, minimal training, general usability, short control latencies.
Keywords: brain–computer interface, mental state monitoring, decoding of mental states, BCI deficiency, sensory motor 
rhythms, event-related desynchronization
Edited by:
Cuntai Guan, Institute for Infocomm 
Research, Singapore
Reviewed by:
Reinhold Scherer, Graz University of 
Technology, Austria
Fabien Lotte, Institute for Infocomm 
Research, Singapore
*Correspondence:
Machine Learning Laboratory, Berlin 
Institute of Technology, Room 6056, 
Franklinstr. 28/29, 10587 Berlin, 
Germany.
e-mail: benjamin.blankertz@tu-berlin.de
only through the use of modern machine learning and signal 
processing methods, that allowed to relocate the burden of train-
ing from a learning subject toward statistical learning machines 
and thereby achieve BCI communication for a naïve user already 
in the first session (Blankertz et al., 2002, 2007a, 2008b). This issue 
as well as technological requirements of non-medical BCI use are 
discussed in Section 2. In Section 3, we outline how the real-time 
decoding of mental states, such as fatigue or workload, can be used 
to optimize an operator’s performance. Then, BCI for multimedia 
applications and gaming, i.e., for a novel type of user performance 
is discussed in Section 4, and finally we briefly conclude with some 
remarks on the future of man–machine interaction.
2 Improvements in BCI Technology
A broader applicability of BCI technology for alternative uses 
requires additional methodological steps that have not been in 
the focus of BCI research aiming at patients’ applications. Here, 
we discuss improvements in ease of use as well as broad and robust 
applicability: short preparation: Section 2.1; minimal user training: 
Section 2.2; minimal calibration of the system: Section 2.3; applica-
bility for a broad range of users: Section 2.4; practicing short latency 
BCI operation: Section 2.5; BCI control that takes into account the 
current state of the user: Section 2.6.
2.1 Dry Electrodes
Wet electrodes are very time-consuming to setup. This is one main 
reason why EEG technology is not adopted easily by a wider audi-
ence. Early prototypes of dry electrode technology were developed in 
the late 1960s and early 1970s (Richardson et al., 1968; Bergey et al., 
1971) and since then various dry and insulating electrode materi-
als have been tested (Searle and Kirkup, 2000) and also a capaci-
tive electrode coupling approach has been achieved (Oehler et al., 
1 Introduction
Brain–computer interfacing (BCI), i.e., the ability to transfer and 
use information from distinct brain states for communicating 
with a machine has in the past years received considerable atten-
tion (Wolpaw et al., 2002; Birbaumer, 2006; Allison et al., 2007; 
Dornhege et  al., 2007a; Schalk, 2008; Krusienski and Wolpaw, 
2009). While the mainstream of research addressed improve-
ments of paradigms (Hill et al., 2005; Citi et al., 2008; McFarland 
et al., 2008; Hwang et al., 2009; Williamson et al., 2009; Höhne 
et al., 2010; Schaefer et al., 2010; Schreuder et al., 2010; Treder 
and Blankertz, 2010) and data analysis technology (Parra et al., 
2005, 2008; Dornhege et al., 2007b; Lotte et al., 2007; Blankertz 
et al., 2008a; Tomioka and Müller, 2010) as to allow for an easier, 
more convenient and faster use of BCI, this was mainly done for 
communication purposes with the overall aim to help paralyzed 
patients (Kübler et al., 1999, 2000, 2001, 2005; Birbaumer et al., 
2000, 2003; Neuper et al., 2003; Pfurtscheller et al., 2003; Birbaumer 
and Cohen, 2007; Dobkin, 2007; Müller-Putz et al., 2007; Cincotti 
et al., 2008; Daly and Wolpaw, 2008; Conradi et al., 2009). Recently 
BCI technology has also been used for a larger audience, namely for 
non-medical purposes. Here, not only communication is central, but 
BCI technology has gained popularity in the form of measurement 
devices, that allow to access respectively decode macroscopic brain 
states such as attention, performance capability, emotion etc., in 
real-time (Dornhege et al., 2007a; Müller et al., 2008). The signals 
extracted by BCI techniques are then employed to exploit this novel 
information for improved man–machine interaction. This allows 
to optimize and to enhance human performance and to achieve 
potentially novel types of skills.
This paper discusses these recent non-medical developments, 
with a focus on the work of the authors, and puts them into perspec-
tive. Clearly, a wider use of BCI technology has become ­possible 

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  2
Blankertz et al.	
Non-medical uses of BCI technology
this operant conditioning variant of BCI, the subject has to learn 
the self-control of slow cortical potentials at central scalp position 
(Elbert et al., 1980; Rockstroh et al., 1984; Birbaumer et al., 2000), 
which requires intensive training on the side of the user. Later, 
an approach was introduced relying on voluntary modulation of 
sensorimotor rhythms (SMR; Neuper et al., 1999; Pfurtscheller and 
da Silva, 1999; Wolpaw et al., 2000; Krusienski and Wolpaw, 2009), 
which substantially reduced the required training time (Vaughan 
et al., 2006). But still user training in the order of several sessions 
was necessary in most cases due to the relatively fixed way of fea­
ture extraction which does not completely account for the high 
inter-personal variability with respect to the brain signatures of 
natural (i.e., untrained) control commands. BCI systems that are 
based on the detection of potentials that are related to external 
stimuli (Wolpaw et al., 2002) typically require less user training. 
In the following we only focus on system which use endogenously 
altered mental states.
Machine learning based BCIs use EEG features of larger com­
plexity that can be fitted better to the individual characteristics 
of brain patterns of each user. To this end, there is often an initial 
calibration period, in which signals are acquired while the user 
generates control commands according to cues without receiv­
ing feedback. Machine learning algorithms are applied to these 
labeled data to infer features (e.g., spatial filters, frequency bands) 
that are optimized for the BCI performance of the individual user 
(Blankertz et al., 2002, 2007a; Parra et al., 2003; Dornhege et al., 
2007a). In Blankertz et al. (2008b) we investigated which proportion 
of naive subjects could successfully use an SMR-based system in 
the very first session. Participants of the study were 14 individuals 
who never performed in a BCI experiment before. For one sub­
ject, no distinguishable classes were identified from the calibration 
data. The other 13 subjects performed feedback: 1 near chance 
level, 3 with 70–80%, 6 with 80–90%, and 3 with 90–100% hits. 
The results of all feedback runs using the Berlin brain–computer 
interface (BBCI) are shown in Figure 1.
Instead of an offline calibration, it is also possible to start 
with BCI feedback right from the beginning by using a subject-
­independent classifier which is then adapted to the individual trial-
by-trial. Although some research groups claim that it is possible to 
do this in an unsupervised manner (Li and Guan, 2006; Blumberg 
et  al., 2007), all online studies published so far use supervised 
adaptation method for the initial period (Vidaurre et al., 2006, 
2007; Wang et al., 2007; Vidaurre and Blankertz, 2010). The term 
“supervised” means that the system needs to know the true inten­
tion of the subject for adaptation, which is typically done by cue­
ing the subject to generate certain control commands. The true 
application that can be controlled by the user can start only after 
this adaptive calibration.
Relying on an adaptive calibration users can be led efficiently 
and fast to a successful BCI control within their first session. As an 
illustrative example, Figure 2 shows the feedback performance of 
a naive subject within her very first session from the very first trial 
on (using the technique presented in Section 2.4). Dots indicate the 
average performance of 20 trials. Runs of adaptive calibration are 
show in magenta and orange color. After only 20 trials, performance 
is at 85%, and after 60 trials performance is almost perfect for the 
rest of the session. More details about the method can be found 
2008). Since this technology represents an easy-to-use ­alternative to 
­classical wet electrodes, dry electrodes are still a sought-after solution 
today. Besides the shortened setup time there are also other benefits 
for long-term monitoring. Electrodes, dependent on gel could dry 
up, while dry electrodes can stay functional. For example, long-term 
ECG measurements for patient monitoring could indicate potential 
cardio-vascular problems for patients in high risk groups and vari­
ous attempts have been made to increase practicability by combining 
it with wireless technology (Catrysse et al., 2004; Coosemans et al., 
2006), flexible electrodes (Hoffmann and Ruff, 2007; Baek et al., 
2008) and by including such devices into wearable textiles (Muhlsteff 
and Such, 2004; Carpi and Rossi, 2005).
A recent development (Gargiulo et al., 2010) uses little dry sen­
sors made of silicone conductive rubber that are attached to the 
scalp using a skin compatible super glue. Although BCI paradigms 
have been used, data is not evaluated in the sense of BCI perform­
ance but rather as correlation coefficient between signals recorded 
from the novel dry sensors and concurrently acquired standard 
EEG. At the optimal delay of 50 samples, a mean correlation coef­
ficient of 0.76 was found.
A different development was evaluated in Sellers et al. (2009) in 
the context of the matrix speller (Farwell and Donchin, 1988). EEG 
signals were acquired concurrently with a novel hybrid dry elec­
trode sensor array (HESA) and conventional wet electrodes (Cz, Pz, 
PO7, PO8 from each system with a spatial distance of about 4 cm). 
Data recorded from both type of sensors during a standard spelling 
task was classified offline using the same algorithm. Performance 
was comparable for both systems (mean accuracy across eight par­
ticipants was 67.5 vs. 70.5% for dry vs. wet sensors).
Two dry sensor systems have been evaluated with respect to an SSVEP 
(Morgan et al., 1996; Middendorf et al., 2000; Cheng et al., 2002; Allison 
et al., 2008) paradigm: Luo and Sullivan (2010) used a single-channel 
dry sensor in a four-class setting. An average detection rate of 75.8% was 
obtained in offline analysis for the best parameter setting with a very 
high variability between participants ranging from 5 to 100%. A helmet 
with 28 capacitive sensors is used in (Oehler et al., 2008) for a two-class 
SSVEP setting. The mean detection accuracy across four participants 
was 81% for the classification of 7 s long-time windows. Both report 
about online BCI operation restricted to one participant.
The only systematic study to date in which dry sensor technology 
was used to provide online BCI feedback is (Popescu et al., 2007). 
Here, a prototype solution with six dry electrodes was evaluated 
with respect to motor imagery driven BCIs. The electrodes were 
gold-coated and had a square shape of 0.5 × 0.5 cm2 with multiple 
pins attached. Various springs and joints were necessary to ensure 
a comfortable fit. A classic BCI 1D feedback paradigm was tested 
and compared to the results of a cap with 64 wet electrodes. While 
the information rate was approx. 20% lower for the dry electrodes, 
peak information rates of 36 bits/min were reached on occasion, 
which is on par with state-of-the-art gel-based BCI performance. 
Note that the use of only six electrodes would easily allow to run 
the new system with a tiny EEG amplifier and a pocket PC.
2.2 Minimal user training
The first approach to establish a pure BCI communication channel, 
which does not rely on any neuromuscular output pathways was 
described in Birbaumer et al. (1999) and Elbert et al. (1980). In 

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  3
Blankertz et al.	
Non-medical uses of BCI technology
were shown to provide better generalization properties compared 
to single-session filters and could therefore be used in following ses­
sions without the need to recalibrate the system for these subjects. 
The offline results were confirmed by online experiments and no 
loss of classification performance was observed. However, still a 
fairly large number of sessions of the same subject were required. 
More recently, a subject-independent zero-training SMR-based 
BCI system was developed by harvesting a large library of previ­
ous BCI experiments (Fazli et al., 2009). This large library allowed 
to combine a very large set of subject-dependent classifiers into 
a single subject-independent classifier by choosing appropriate 
weights for creating a very sparse set of voting classifiers. Among 
several tested methods (such as k-nearest neighbor (kNN), sup­
port vector machines (SVMs), linear discriminant analysis (LDA) 
and others) l1 regularized regression performed best. The resulting 
subject-independent classifier performed almost as well as stand­
ard, state-of-the-art subject-calibrated methods across the data 
from 91 participants.
A different approach is presented in Lotte et al. (2009). In the 
offline evaluation which is limited to data sets of nine subjects, the 
best subject-independent classifier obtains on average 10% less in 
accuracy compared to the best subject-specific classifier.
2.4 BCI Deficiency and Countermeasures
One of the major obstacles before BCI technology can be widely 
applied in non-medical fields is the problem of “BCI Deficiency,” 
meaning that for a non-negligible portion of users, BCI systems 
cannot detect their intentions accurate enough to let them control 
applications. Gaining a deeper understanding of this phenomenon 
and finding approaches to broaden the efficiency of BCI systems to 
all potential users is one pivotal challenge in BCI research.
Note that the problem of deficiency is less prominent, but still sig­
nificantly existing, in some BCI approaches based on event-­related 
potentials. For results on large-scale studies and performance-re­
lated demographics, see Allison et al. (2009) for an SSVEP- and 
Guger et al. (2009) for a P300-based system. In SMR-based BCI 
in Section 2.4. These studies show that a machine learning based 
approach to BCI is able to let BCI novices perform well from the 
first session on. Still, we would like to remark that there is a non-
negligible portion of users, for which this quick-start approach is 
not successful, see Section 2.4.
2.3 Minimal Calibration: Subject-Independent Classifiers
Even when user training is avoided by taking a machine learning 
approach to BCI, see Section 2.2, there remains a reduced but still 
time-consuming preparatory step: the calibration of the system 
to the user’s characteristic activation pattern. Lately, a number of 
attempts have been made to overcome the calibration by means of 
specifically developed machine learning techniques, e.g., Kaper and 
Ritter (2004), Lu et al. (2009) for P300 and Allison et al. (2008), 
Cecotti (2010) for SSVEP as well as Krauledat et al. (2008) for 
SMR-based BCIs where feedback and calibration data of multiple 
sessions of BCI-experienced subjects were employed to identify 
subject-dependent prototypical spatial filters. These spatial filters 
50
60
70
80
90
feedback accuracy (%)
cm ct cp zp cs cu ea at zr co eb cr cn
0
5
10
15
20
25
30
35
40
<60
60−70
70−80
80−90
90−100
(%) of feedback runs
Figure 1 | Left: Feedback accuracy of all runs (gray dots) and intra-subject averages (black crosses). Right: Histogram of accuracies obtained in BBCI-
controlled cursor movement task in all feedback runs of the study.
40
50
60
70
80
90
100
BCI feedback accuracy  (%)
fixed Lap
CSP + sel. Lap
CSP
8
7
6
5
4
3
2
1
Figure 2 | The graph shows the feedback performance of one BCI-naive 
subject from the very first trial on. Results are from one single session in 
which 8 runs of 100 trials (about 15 min) each have been recorded. There was 
no calibration period before. Feedback started with a general, subject-
independent classifier which was adapted trial-by-trial. Dots indicate the 
average feedback performance (1D cursor control) of 20 trials. The mean 
performances of each run of 100 trials is shown as bars. The three colors relate 
to three different processing methods, which are explained in Section 2.4.

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  4
Blankertz et al.	
Non-medical uses of BCI technology
a ­subject-­independent classifier pretrained on simple features 
(band-power in alpha-frequency (8–15 Hz) and beta-frequency 
(16–32 Hz) ranges in three Laplacian channels at C3, Cz, C4) was 
used and adapted (covariance matrix and pooled mean; Vidaurre 
et al., 2008) to the subject after each trial. For the subsequent three 
runs, a classifier was trained on a more complex band-power fea­
ture in a subject-specific narrow band composed from optimized 
CSP filters in six Laplacian channels. While CSP filters were static, 
the position of the Laplacians was updated based on a statistical 
criterion, and the classifier was retrained on the combined CSP 
plus Laplacians feature in order to provide flexibility with respect 
to spatial location of modulated brain activity. Finally, for the last 
two runs, a classifier was trained on CSP features, which have been 
calculated on runs 4–6. The pooled mean of the linear classifier was 
adapted after each trial (Vidaurre et al., 2008).
Initially, we verified the novel experimental design with six sub­
jects of Cat. I. Here, very good feedback performance was obtained 
within the first run after 20–40 trials (3–6 min) of adaptation, and 
further increased in subsequent runs. In the present pilot study, two 
subjects of Cat. II and three subjects of Cat. III took part. All those 
five subjects did not have control in the first three runs, but they 
became able to gain it when the machine learning based techniques 
came into play in runs 4–6 (a jump from run 3 to run 4 in Cat. II, 
and a continuous increase in runs 4 and 5 in Cat. III, see Figure 3). 
This level of performance could be kept or even improved in runs 
7 and 8 which used unsupervised adaptation. Summarizing, it was 
demonstrated that subjects suffering from BCI deficiency before 
could gain BCI control within one session. In particular, one subject 
who had no SMR idle rhythm in the beginning of the measure­
ment could develop it with the feedback training, see Figure 3. This 
fundamental finding provides a perspective for the development 
of neurofeedback training (NFT) procedures that might help to 
alleviate BCI deficiency.
2.5 Guided Practice for a Fast-Decision BCI
Typically SMR-based BCIs suffer from a long latency between 
intention of the user and actual BCI control. Here, we introduce 
a “goalkeeper paradigm” that aims at improving online BCI per­
formance by subject training under time pressure conditions (cf. 
Ramsey et al., 2009).
Multi-channel EEG of eight BCI-experienced subjects was 
acquired while they were playing three runs (100 trials each) of 
a BCI-controlled computer game that imitated the task of a goal­
keeper during a penalty kick. During a trial, a ball was moving from 
the top of the screen toward one of its bottom corners. Using two 
different types of motor imagery (chosen from left hand, right hand, 
and foot) the subjects had to control the horizontal movements of a 
bar at the bottom of the screen in order to block the ball. Consistent 
with the goalkeeper metaphor, the bar could only be moved once 
(like a jump) into one or the other corner. The speed of the ball 
increased linearly from trial to trial and over the three runs. Subjects 
had to catch the ball within 2500 ms (at the beginning of run 1) 
to 1250 ms (at the end of run 3). Late arrival in a correct corner or 
arrival in a wrong corner were interpreted as misses.
In order to achieve a constant goalkeeping performance, the 
subjects were thus required to generate faster and/or stronger ERD 
responses in the later runs to steer the bar quickly into the correct 
systems deficiency is encountered regardless of whether a machine 
learning or an operant conditioning approach is used (Kübler and 
Müller, 2007). The actual rate of deficiency is difficult to determine, 
in particular since only a few BCI studies are published that have a 
sufficiently large number of participants who were not prescreened 
for being potentially good performers. There rate of deficiency in 
SMR-based non-invasive BCI systems can roughly be estimated to 
be about 15–30% and therefore poses a major obstacle for general 
broad BCI deployment. Still, very little is known about possible 
reasons of such failures in BCI control. A deeper understanding 
of this phenomenon requires determining factors that may serve 
to predict BCI performance and developing methods to quantify 
a predictor value from given psychological and/or physiological 
data. Such predictors may then help to identify strategies for future 
development of training methods to combat BCI deficiency and 
thereby provide more people with BCI communication.
With respect to SMR-based BCI systems, there is recent evidence 
that gamma oscillations play an important role. In a study with 
N = 10 participants, a relationship between gamma-power dur­
ing motor imagery and classification accuracy (left hand vs. right 
hand) was found (Grosse-Wentrup et al., 2010). In particular, the 
probability of correct offline classification of a motor imagery trial 
was positively correlated with power in a broad gamma-frequency 
range (55–85 Hz) during that trial in frontal and occipital areas. 
Note, however, that these findings do not give rise to a predictor 
of BCI performance.
Such a neurophysiological predictor of BCI performance was 
proposed in Blankertz et al. (2010a). It is computed as band-power 
in physiologically specified frequency bands (below 50 Hz) from 
only 2 min of recording in a “relax with eyes open” condition using 
two Laplacian channels selectively placed over motor cortex areas. 
A correlation of r = 0.53 between the proposed predictor and BCI 
feedback performance was obtained on a large data base with 
N = 80 BCI-naive participants.
In a screening study, N = 80 subjects performed motor imagery 
first in a calibration measurement (i.e., without feedback) and then 
in a feedback measurement in which they could control a 1D cur­
sor application. Basically, we observed three categories of subjects: 
subjects for whom (I) a classifier could be successfully trained and 
who performed feedback with good accuracy; (II) a classifier could 
be successfully trained, but feedback did not work well; (III) no 
classifier with acceptable accuracy could be trained. While subjects 
of Cat. II had obviously difficulties with the transition from offline 
to online operation, subjects of Cat. III did not show the expected 
modulation of SMRs: either no SMR idle rhythm was observed over 
motor areas, or this idle rhythm was not attenuated during motor 
imagery. For the latter case, a novel motor instruction for “quasi-
movements” (i.e., movement intentions minimized to the extent 
that neither a mechanical limb change nor even an EMG activation 
remain detectable) has been proposed which led to a significant 
improvement of BCI performance (Nikulin et al., 2008).
Here, we present preliminary results of a pilot study (Vidaurre 
and Blankertz, 2010; Vidaurre et  al., 2010) that investigated 
whether co-adaptive learning using machine learning techniques 
could help subjects suffering from BCI deficiency (i.e., being Cat. 
II or III) to achieve successful feedback. In this setup, the session 
immediately started with BCI feedback. In the first three runs, 

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  5
Blankertz et al.	
Non-medical uses of BCI technology
a task on outcome performance has been extensively studied 
and different effects have been reported. A first body of evidence 
links medium and lower amplitudes in the alpha-frequency band 
(7–14 Hz) to better perception in somatosensory and visual dis­
crimination tasks (Pfurtscheller and da Silva, 1999; Hanslmayr 
et al., 2005; Palva and Palva, 2007; van Dijk et al., 2008). As high 
activity in this frequency band is hypothesized to represent an idle 
state of cortical structures, i.e., no active processing (Pfurtscheller 
and da Silva, 1999), this effect can be explained by the fact that the 
sensory cortices involved in the task need to be in an appropriate 
excitation stage to process the upcoming stimulus. On the other 
hand, higher amplitudes over the sensorimotor cortices are cor­
related with better sensorimotor processing (Del et al., 2007), but 
less accurate inhibition of motor responses (Mazaheri et al., 2009). 
This suggests that a higher relaxation state of the motor system 
leading to higher inhibition could cause the motor system to be 
less responsive to signals from other regions and thus induce more 
straight forward processing. Concerning cognition, better perform­
ance has also been shown in the case of stronger prestimulus alpha-
frequency band amplitude (Neubauer and Freudenthaler, 1995; 
Klimesch, 1999). Some groups even demonstrated that cognitive 
performance could be increased if the amplitude of the prestimulus 
corner. In an offline analysis, the goalkeeping performance, the 
reaction times (defined as the time needed to reach the correct 
corner) and EEG features were analyzed in relation to the block 
design of the experiment.
The goalkeeper paradigm effectively increased time pressure 
over the three runs. Performance was measured in terms of balls 
caught within the first 1250 ms. Seven out of eight subjects managed 
to respond with increased performance from run 1 to 3 (average of 
33.8 balls caught in run 1 to 41.6 in run 3, see Figure 4A).
A close analysis of time-frequency EEG features between suc­
cessful trials of run 1 and 3 revealed changing EEG signs of motor 
activation, i.e., earlier ERD or stronger ERD in the alpha-band under 
time pressure, cf. Figure 4B. As a side effect, the training introduced 
for some subjects an additional ERD in the beta-band (which had 
not been used for feedback). Earlier re-synchronization (ERS) could 
be observed for some subjects in run 3, where trials were shorter.
2.6 Exploiting Prestimulus Mental States for Better BCI 
Performance
Quantification of oscillatory brain activity in different frequency 
bands has already been widely used in the investigation of mental 
states. More precisely, the influence of these rhythms ­preceding 
−0.02
−0.01
0
0.01
0.02
40
50
60
70
80
90
100
Cat. I
BCI feedback accuracy  (%)
Cat. II
Cat. III
−0.02
−0.01
0
0.01
0.02
runs 1+2
runs 7+8
2
+( r  )
−
sel Lap
Lap
fixed
CSP+
CSP
8
7
6
5
4
3
2
1
10
15
20
[Hz]
10
15
20
[Hz]
Figure 3 | Left: Grand average of feedback performance within each run 
(horizontal bars and dots for each group of 20 trials) for subjects of Cat. 
I (N = 6), Cat. II (N = 2) and Cat. III (N = 3). An accuracy of 70% is assumed to be 
a threshold required for BCI applications. Note that all runs of one subject have 
been recorded within one session. Right: For one subject of Cat. III, spectra in 
channel CP3 and scalp topographies of band-power differences (signed 
r2-values) between the motor imagery conditions are compared between the 
beginning (runs 1 + 2) and the end (runs 7 + 8) of the experiment. 
Time (ms)
A
B
Figure 4 | (A) Brain–computer interfacing reaction times are shown for all participants (asterisk) and grand average (solid line) separately for all three runs which had 
increasing time pressure to enforce faster BCI decision. As “BCI reaction time” we denote the latency from cue presentation until the decision of the user as 
conveyed by the BCI system. (B) The time-frequency plot displays the contrast (r2 difference) between run 3 and run 1.

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  6
Blankertz et al.	
Non-medical uses of BCI technology
the ERD/ERS patterns over the whole scalp, clearly shows that the 
ipsilateral hemisphere stays in a higher synchronization level in the 
high group, that is not reach in the low-group.
Although the reason for better discriminability in the high group 
still has to be explored in detail, we conjecture it to be due to a bet­
ter relaxation state of the sensorimotor system leading to an ERD 
focalized to the contralateral hemisphere and an ERS (idling) over 
the ipsilateral one. These observations are in line with the findings 
by Mazaheri et al. (2009): high power in the alpha-frequency band 
makes the motor cortices immune to external inputs and thus are 
expected to generate clearer spatial patterns, which implies that 
they are also easier to classify.
Our findings suggest to explore NFT to increase users’ SMR 
amplitude and thus take advantage of the faster and more accurate 
classification in later BCI applications. But the effectiveness of the 
neurofeedback procedure, as well as the stability of its effects will 
have to be investigated thoroughly.
3 Mental State Monitoring
In the context of BCI technology, it is crucial to deal with the fact 
that brain signals exhibit an enormous trial-to-trial variability, even 
for constant behavioral performance. But when we turn to more 
difficult sensorimotor or cognitive tasks like the detection of peri-
threshold stimuli, to decisions in just-notable difference discrimi­
nation, or to high-load memory tasks, also on the behavioral level 
we can observe considerable moment-to-moment fluctuations in 
reaction to the very same stimuli. Many studies in cognitive neu­
roscience have set out to find neuronal correlates that explain this 
variability (e.g., Fernández et al., 1999; Thut et al., 2006; Chen et al., 
2008; Mathewson et al., 2009; Schubert et al., 2009). In particular, 
those studies that identify predictors from prestimulus intervals in 
the ongoing EEG for the performance in the subsequent task are 
potentially relevant for novel applications of BCI technology.
alpha rhythm was enhanced artificially, e.g., by external ­stimulation 
(Klimesch et al., 2003; Hanslmayr et al., 2005). This is in line with 
the idea that more inhibition allows less signals from other brain 
regions to reach the neuronal network performing the task and 
thus induces better processing. Put together, this demonstrates a 
clear difference in the activation requirements of the involved brain 
networks between strictly perceptual tasks and more complex cog­
nitive or motor processing tasks. In this subsection and later on, 
we will focus on complex cognitive and motor tasks for example 
motor imagery (cf. Maeder et al., 2010).
In BCI technology, SMR modulations induced by motor imagery 
are commonly used as task. However, performance varies exten­
sively from trial to trial and also between sessions in the same sub­
ject. According to evidence presented here, part of this variability 
could be attributed to ongoing fluctuations in the SMR rhythm, 
see also Section 2.4.
To investigate in detail the effect of prestimulus mental states on 
BCI classification performance, we conducted a study analyzing the 
influence of prestimulus SMR amplitude on timing and strength 
of motor imagery induced SMR modulations.
We used data from 30 naive subjects performing left and right 
motor imagery in a standard cued paradigm and split feedback trials 
into two groups on their prestimulus band-power (high- and low-
group). All trials were classified offline in sliding time intervals of 
1000 ms duration as used, e.g., in cursor control, and classification 
accuracies were averaged within the two groups and across subjects.
We found that the classification error for the high group was 
lower than for the low-group over the whole trial length, see Figure 5 
(left). Interestingly, this effect can be attributed to the ipsilateral 
rather than to the contralateral hemisphere, see the grand average 
ERD curves in Figure 5 (right), where the curves representing the 
ipsilateral side exhibit a higher difference in the post-stimulus inter­
val than the one for the contralateral class. Figure 6 (left) displaying 
0
1000
2000
3000
4000
5000
0
5
10
15
20
25
30
35
40
45
50
End of classififcation window (ms)
Classification error (%)
prestim low
prestim high
−0.04
−0.02
0
0.02
0.04
sgn r2
CSP channel 2 (Left)
−1000
0
1000
2000
3000
4000
0.4
0.6
0.8
1
1.2
1.4
1.6
Time (ms)
ERD (µV)
CSP channel 1 (Right)
Left Low
Left High
Right Low
Right High
Figure 5 | Left: Classification error for two groups of feedback trials with high and low prestimulus SMR amplitude. Classification was performed on a 
1000 ms sliding window with 50 ms overlap and significant differences are denoted by “*” (black: p < 0.01, gray p < 0.05). Right: ERD for the different groups of the 
two classes (high and low for left and right).

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  7
Blankertz et al.	
Non-medical uses of BCI technology
­suboptimal user interfaces reduces the number of critical mental 
states of the operators. Thus, it could lead to an increase in produc­
tion yield, less errors and accidents, and avoid user frustration.
Typically, information collected about mental states of interest 
is exploited in an offline data analysis and leads to a redesign of 
task or interface. In addition, a method for mental state monitor­
ing that can be applied online during the execution of a task might 
be desirable. Traditional methods for capturing mental states and 
user ratings are questionnaires, video surveillance of the task, or 
the analysis of errors made by the operator. However, question­
naires are of limited use for precisely assessing the information of 
interest, as the reported answers are often distorted by subjective­
ness. Questionnaires cannot determine the quantities of interest in 
real-time (during the execution of the task) but only in retrospect; 
moreover, they are intrusive because they interfere with the task.
As a new approach, we propose the use of EEG signals for mental 
state monitoring and combine it with BCI technology for real-time 
data analysis and classification. With this approach, the brain sig­
nals of interest can be isolated from background activity as in BCI 
systems; this combination allows for the non-intrusive evaluation 
of mental states in real-time and on a single-trial basis such that 
an online system with feedback can be built.
3.1 Attention
Mental state monitoring is of particular interest in safety-critical 
applications where human performance is often the least control­
lable factor. For example, consider that fatal car accidents are one 
of the leading causes of death in the United States (Mokdad et al., 
2004; Mokdad et al., 2005; Subramanian, 2007), and the leading 
cause among children (9–18 years) worldwide (Xu et al., 2010). The 
two main causes for crashes are distraction of (visual) attention and 
Combining such results from cognitive neuroscience with sys­
tems that allow the detection of specific mental states in real-time 
may eventually lead to devices that allow to optimize human per­
formance. For example, a neurotec-enhanced vocabulary trainer 
may adapt the presentation of new word pairs to a moment of time 
in which the user is in a good mental state for memory encoding, 
see Guderian et al. (2009). During periods of attenuated attention, 
a learning game is probably more effective than drilling vocables.
On a more basic side, the way of how neuroscience and psy­
chophysics experiments are performed may be extended in an 
important aspect. While upto now, participants are presented with 
a more or less preprogrammed sequence of stimuli (subject to some 
random factors), it becomes possible to adjust the presentation of 
stimuli to the momentary mental state of the subject.
While this area is still largely to be explored, we review here some 
initial approaches that show the application of BCI technology for 
mental state monitoring in settings that are relevant for real-world 
applications. See Zander and Jatzev (2009) for a general discussion 
of usage of BCI technology to detect covert user states. Note, that 
mental state monitoring has also medical use, like treating ADHD 
patients with neurofeedback based on an attention monitoring 
system, see Hamadicharef et al. (2009).
When aiming to optimize the design of user interfaces or, more 
general, of a work flow, the mental state of a user during task execu­
tion can provide valuable information. This information can not 
only be exploited for the improvement of BCI applications, but 
also for improving industrial production environments, the user 
interface of cars and for many other applications. Examples of these 
mental states are the levels of arousal, fatigue, emotion, workload 
or other variables the brain activity correlates of which are (at 
least partially) accessible by measurement. The improvement of 
 
 
 
 
 
 
−1000 to 0 ms
550 − 2650 ms
 
 
−0.5
0
0.5
1
left low
left high
right low
right high
Figure 6 | Left: Scalp distribution of the ERD in the prestimulus interval (−1000 to 0 ms) and the post-stimulus interval where the significant change in 
performance was observed (550–2650 ms).

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  8
Blankertz et al.	
Non-medical uses of BCI technology
on the factors reaction time (40% fastest/slowest), condition and 
electrode location (subdivision into groups of 22 frontal/central/
parieto-occipital electrodes) was investigated. Band-power was cal­
culated in the theta-, alpha-, beta-, and gamma-band by applying 
an FFT within the 3500 ms prestimulus interval.
Reaction times were significantly larger in the driving condi­
tion than during fixation, and reactions to frequent stimuli were 
significantly faster compared to infrequent stimuli. Alpha- and 
gamma-power decreased gradually from K0 to K2 conditions. Most 
importantly, within each condition alpha-power was significantly 
higher for short, compared to long auditory reaction times. At first 
sight, this seems in conflict with the established role of high alpha-
power as a marker of fatigue, as introduced above. However, it is in 
line with a study, in which a positive correlation was found between 
alpha-power and increasing task demand (Cooper et al., 2003). We 
suggest that for competing auditory and visual tasks, fast reactions 
to auditory stimuli can be performed only at the expense of a less 
efficient engagement of visual processing as revealed by a dimin­
ished alpha suppression. Our data show also that the potential range 
for attention-related alpha modulation gets smaller with increas­
ing visual flow, i.e., during driving a large amount of attention is 
inevitably bound to the visual system.
While this study is itself not an application of BCI technology, it 
points a way for future applications in driving assistance systems, 
and the results point out why subtle methods, as developed in the 
field of BCI, are required: inattentiveness cannot be detected as 
such, but only with respect to a certain input modality which in 
case of driving is the visual domain. Furthermore, the neural cor­
relates differ considerable between individuals, such that a specific 
calibration of the detector is needed.
3.2 Monitoring Performance Capability
Monitoring of mental states such as performance capability or task 
engagement can be of interest for industrial applications. A pilot 
study (Müller et al., 2008) with four participants evaluated the 
use of EEG signals in such a setting. The aim was to investigate 
the net effect of performance in a application oriented scenario. 
By choosing to simulate a real-world application, we accepted that 
different psychological concepts were lumped together, amongst 
those fatigue, concentration, task engagement. The design was not 
intended to disentangle those states, but rather to monitor the con­
tinuous performance capability of an operator.
The experimental paradigm simulates a security surveillance 
system where the sustained performance ability of the user in a 
monotonous task is crucial. The objective was to calibrate the BCI 
system to the individual user in order to recognize and predict 
mental states that correlate with a high or a low number of per­
formance errors of the subject. In the following we will use the 
term concentration for this concept.
Participants had to rate 2000 (simulated) X-ray images of lug­
gage objects as either dangerous or harmless by a key press with  the 
left or right index finger after each presentation, see Figure 7. EEG 
was recorded from 128 channels at 1000 Hz. The session was divided 
into 10 runs of 200 trials each. Due to the monotonous nature of the 
task and the long duration of the experiment, they were expected 
to show a fading level of arousal, which impairs concentration and 
leads to more and more erroneous decisions during later blocks.
lapses in vigilance due to fatigue. For assessment of such mental 
parameters, physiological measures have been developed, blink and 
heart rate being the most widely used among them (e.g., Papadelis 
et al., 2007). Although EEG-based markers might more directly 
reflect cognitive processing, they have been considered less often 
in driving applications so far (see Brookhuis and de Waard, 1993; 
Otmani et al., 2005; for EEG-based investigation of attention in car 
driving, and the reference in Section 3.3 concerning workload).
Parieto-occipital alpha-waves are believed to be linked to idling 
of the visual cortex, which is the assumed default mode if no vis­
ual information is processed. Thus, high alpha-power signifies 
potentially dangerous brain states with reduced visual attention. 
In the extreme case of sleep, alpha activity is most pronounced, 
and so-called sleep spindles can be observed even by the naked 
eye. However, microsleep detection from EEG is uncalled-for, since 
technically more simple systems based on eyelid closure detection 
already achieve good results.
On the other hand it is understood that the danger of driving 
errors increases already a certain time before microsleep onset. 
During that period, responsiveness to sudden unexpected events 
will be degraded due to the driver’s drowsiness. A similar degrada­
tion is expected to happen during longer periods of monotonous 
driving. The challenge for driving assistance systems is to detect 
such subtle deficiency in vigilance occurring while driver’s eyes 
are open. Importantly, incidence of being in such an inattentive 
mode might be hard to infer from facial expression and eye move­
ments alone, while neurophysiological measures could provide 
added value.
In a recent study the potential use of EEG-derived oscillatory 
features for driving assistance applications was investigated by relat­
ing band-power to driving performance in a realistic simulated 
scenario (Schubert et al., 2008). The experiment was designed to 
account for the complexity of driving, which requires attentiveness 
to both visual and auditory stimulation. Consequently, our investi­
gation included a whole range of frequency bands and topographic 
regions-of-interest, covering alpha activity from visual cortex as 
well as oscillatory signals related to other cognitive systems.
Eleven right-handed male subjects, all possessing a driver’s license, 
participated in the study. They had to perform three different primary 
tasks. In the first condition (K0) the task was simply to fixate at a 
cross placed in front of the subject. In the second condition (K1) the 
cross was replaced by a video presentation of a driving scene (passive 
driving). The third condition (K2) finally required active driving, 
using a steering wheel. The subject had to perform lane changes as 
quickly as possible upon presentation of corresponding signs. In all 
three conditions, high/low tone auditory stimuli (oddball, ratio 1:5, 
ISI 5–6 s randomized) had to be responded to as quickly as possible 
as a secondary task by pressing buttons attached at left/right thumbs, 
respectively. The time needed for pressing the appropriate button was 
regarded as a substitute for driving performance. The experiment 
was divided into four blocks, each containing 10 min intervals under 
K0 and K1 conditions, as well as 20 min of K2 driving. During the 
whole experiment, EEG from 128 channels was acquired.
The data underwent post hoc statistical analysis using repeated 
measures ANOVA. For the response times of the secondary task, a 
model with factors stimulus (frequent vs. infrequent) and condi­
tion was considered. Furthermore, the dependence of band-power 

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  9
Blankertz et al.	
Non-medical uses of BCI technology
of high and low error index, a so-called concentration insufficiency 
index (CII) was derived from EEG data. The output of the CII meas­
ure for each trial is plotted in Figure 8 together with the correspond­
ing error index. It can be observed that the calculated CII mirrors the 
error index for most blocks. More precisely, the CII mimics the error 
increase inside each block, and in blocks 3 and 4 it can anticipate the 
increase of later blocks, i.e., out-of-sample. For those later blocks, 
the CII reveals that the subject could not recover full arousal during 
the breaks. Instead, (s)he shows a short-time arousal for the time 
immediately after a break, but the CII accumulates over time.
The correlation coefficient of both time series with varying tem­
poral delay is shown in the right plot of Figure 8. The CII inferred by 
the classifier and the errors that the subject had actually produced 
correlate strongly. Furthermore, the correlation is high even for 
predictions that are upto 50 trials into the future.
Using a more abstract experimental paradigm, Makeig and Jung 
found increased theta (4–6 Hz) and decreased gamma (>35 Hz) 
activity to be predictive of upcoming failures in a difficult audi­
tory detection task, see Makeig and Jung (1996). More recently, the 
The time course of erroneous decisions taken by a participant 
was smoothed in order to form a continuous measure for arousal. 
This measure is hereafter called the error index and reflects the 
subject’s inability to concentrate and fulfill the security task. To 
enhance the contrast of the discrimination analysis, two thresholds 
were introduced for the error index and set after visual inspection. 
Trials outside these thresholds defined two sets of trials with either 
a rather high or low value. The EEG data of the trials were labeled 
as sufficiently concentrated or insufficiently concentrated depend­
ing on these thresholds for later analysis. Figure 8 shows the error 
index. The subject did perform nearly error-free during the first 
blocks, but then showed increasing errors beginning with block 
four. However, as the blocks were separated by short breaks, the 
subject could regain concentration at the beginning of each new 
block at least for a small number of trials.
As neuronal correlate of decreased concentration, a left parieto-
occipital increase of power in the alpha-frequency range was found. 
For a more detailed physiological analysis please refer to the original 
paper (Müller et al., 2008). Based on the contrast between periods 
Figure 7 | Stimuli used for the suitcase inspection study. The upper row shows three examples of (simulated) X-rays of suitcases that do not contain a weapon. 
They had to be discriminated from suitcases in which there is a weapon hidden, like the three in the lower row (machine pistol, knife, and axe).
temporal delay (trials)
correlation
error
CII
block 1
2
3
4
5
6
7
8
9
10
high CI
low CI
trials in chronological order
-100
100
50
0
-50
Figure 8 | Left: Comparison of the concentration insufficiency index 
(CII, dotted curve) and the error index for the subject. The error index (the 
true performed errors smoothed over time) reflects the inverse of the 
arousal of the subject. Right: Correlation coefficient between the CII 
(returned by the classifier) and the true performance for different time shifts. 
Highest correlation is around a zero time shift, as expected. Note that the CII 
has an increased correlation with the error even before the 
error appears.

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  10
Blankertz et al.	
Non-medical uses of BCI technology
German words links (left) and rechts (right)) which was given every 
7.5 s. This secondary task mimicked the interaction with a car’s 
electronic device. Furthermore, the obtained reaction times were 
used as a measure of the driver’s free cognitive capacity. This task 
was chosen to be simple and to have long inter-task periods such 
that it would not contribute substantially to the overall workload. 
Finally, in every second block of 2 min there was a tertiary task to 
induce workload. Two different conditions were used.
Mental calculation task (MC): Silently subtract iteratively 27 
starting from a given number, that was randomly chosen between 
800 and 999.
Auditory task (AT): Follow the story of an audio book while 
ignoring a simultaneously played news broadcast. For verification, 
a question related to the content of the audio book was ask after 
the end of the block.
These tasks had to be performed during blocks of 2 min duration 
(high workload condition) which were followed by blocks without 
tertiary task (load workload condition), see Figure 9.
In initial calibration phase (two runs with auditory task and two 
runs with calculation task), the developed BBCI workload detec­
tor was adapted to the individual driver. Roughly, the workload 
detector classified spatial patterns of band-power in subject-specific 
frequency band. Initially, unstable channels and channels presum­
ably containing muscle or eye movement artifacts were removed. 
Then different parameter configurations (frequency bands, sets of 
channels, spatial filters, hysteresis thresholds) have been validated 
and the setting that provides the best discrimination of the high vs. 
low workload conditions was selected. For a detailed description 
of the algorithms, see Kohlmorgen et al. (2007).
Using this approach, the system was able to continuously predict 
the cognitive workload of the driver online. The accuracy of the 
detector with respect to the induced levels of workload was on aver­
age above 70% but varied considerably between participants from 
50% (chance level) to 95.6%, see the example output in Figure 10 
for the participants with the best detection results. This information 
was used in the application phase (also two runs with auditory and 
two with calculation task) to switch off the auditory reaction task 
when high workload was detected (“mitigation”).
As a result of the mitigation strategy, the reaction time in 
the application phase was on average 100 ms faster than in the 
(un-mitigated) calibration phase (Kohlmorgen et al., 2007). The 
improvement in performance during the application phase can 
­so-called error-preceding potentials have been investigated, which 
are (changes in) event-related potentials that foreshadow behavio­
ral errors, see Eichele et al. (2010).
3.3 Workload
In the previous sections we exemplified ways in which BCI tech­
nology may help to improve human performance. In contrast, the 
approach presented here can be used to improve the design of 
products. We discuss a method for real-time monitoring of mental 
workload, and how it can be used for neuro-usability. Beyond this 
aspect, there is also a long-term perspective in which the work­
load monitor technology could also be used to improve the human 
performance: real-time measures of mental workload could be 
incorporated in future cars in order to reduce distractions (e.g., a 
navigation system is switched off during periods of high workload) 
to a minimum when the driver’s brain is already over-loaded by 
other demands during potentially hazardous situations.
In the development of many new products or in the improvement 
of existing products, usability studies play an important role. They are 
performed in order to measure to what degree a product meets the 
intended purpose with regard to the aspects effectiveness, efficiency 
and user satisfaction. A further goal is to quantify the joy of use. While 
effectiveness can be quantified quite objectively, e.g., in terms of task 
completion, the other aspects are more intricate to assess. Even psy­
chological variables consciously inaccessible to the subjects themselves 
might be involved. Furthermore, in usability studies it is of interest to 
perform an effortless continuous acquisition of usability parameters 
whilst not requiring any action on side of the subject as this might 
interfere with the task at hand. For these reasons, BCI technology 
could become a crucial tool for usability studies in the future.
One criterium for the usability of a car is the mental workload 
that is required from the car driver. If the manufacturer plans to 
endow the car with a new feature that uses an elaborate man–
machine interface technology, the producer should demonstrate 
that it does not distract the driver from the traffic (i.e., mental 
workload should not be unduly increased when the feature is used). 
If a manufacturer claims that a novel device relieves the driver from 
workload (e.g., by means of an automatic distance control), this 
effect should be “proven.” In both cases, neurophysiological moni­
toring of mental workload could provide an objective measure.
Since there is no ground truth available on the cognitive work­
load to which the driver is exposed, we designed a study1 in which 
additional workload was induced in a controlled manner. For 
details, confer Kohlmorgen et al. (2007). There are several precur­
sory studies that derived measures of workload under laboratory 
conditions (e.g., Gevins et al., 1998; Berka et al., 2007; Sassaroli 
et al., 2008) or in the context of real operational environments (e.g., 
Sterman and Mann, 1995; Hankins and Wilson, 1998; Lin et al., 
2005), but these have all been limited to offline analyses.
In our study, EEG was acquired from 12 male and 5 female sub­
jects while driving on a highway at a speed of 100 km/h (primary 
task). Second, the subjects performed an auditory reaction task: one 
of two buttons mounted on the left and right index finger had to be 
pressed as quick as possible according to a given vocal prompt (the 
Figure 9 | Experimental paradigm. The tertiary task was used to induce 
two different types of cognitive workload. An auditory task (AT) or mental 
calculation (MC) had to be performed in blocks of 2 min (high workload 
condition) interleaved with blocks of two duration without tertiary task (low 
workload condition). One run consisted of three pairs of blocks of high and low 
workload condition.
1This study was performed in cooperation with the Daimler AG. For further infor­
mation, we refer to Kohlmorgen (2007).

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  11
Blankertz et al.	
Non-medical uses of BCI technology
Consonance between chords plays an important role in the 
perception of the complex concept of tonality. From a sensory 
point of view, degrees of consonance can be distinguished regard­
ing psychoacoustic features, e.g., pitch distance, pitch common­
ality or sensory dissonance within each chord. From a cognitive 
point of view the consonance of chords can be judged regarding 
concepts from music theory like key relations or musical syntax. 
Inspired by Krumhansl’s probe tone experiments (Krumhansl and 
Kessler, 1982), the goal of this study is to find neural correlates of 
the processing of consonance in chord progression and the related 
perception of musical structure. As differences in corresponding 
ERP components are on a very small scale, advanced methods for 
ERP single-trial analysis, as developed within BCI research, are 
required for the extraction of the neuronal correlates.
Thirteen subjects, all musically active to a varying extent, took part 
in the study. Experiments consisted of several blocks of acoustic pres­
entation of continuous sequences of major triads in root position. A 
chord was repeated 7–11 times before changing to a new chord of the 
chromatic scale in a random fashion. The subject’s task was to rate 
the goodness of fit of the new chord with respect to the preceding 
chords on a scale from 1 to 7. This resulted in a modified oddball 
paradigm with the new chord as deviant and the last preceding chord 
as standard stimulus in a continuous sequence of chords.
The subjects’ ratings were inhomogeneous but can be attrib­
uted to two main influences: (1) pitch distance and (2) structures 
related to models of music theory. Analysis of ERP data revealed 
that the N2b-P3 complex shows the differences between the classes 
deviant and standard most pronounced. A state-of-the-art classi­
fier (Blankertz et al., 2010b), borrowed from BCI technology, was 
trained to discriminate deviant vs. standard ERPs. This classifier was 
then applied to deviant trials only and the output was averaged for 
the 11 subgroups according to the ascending interval between the 
root of the standard stimulus and of the deviant stimulus, resulting 
in an 11 dimensional profile – the neuronal correlate of a subject’s 
rating profile. These neuronal profiles formed for most subjects 
the same structure as in models of music theory. Strikingly, these 
structures were also found in subjects, whose behavioral data did 
not reveal them, suggesting an unconscious perception at this stage 
of processing, see Figure 11.
be explained by the fact that the workload detector successfully 
predicted periods of potentially reduced reactivity and exempted 
drivers from reacting during increased workload.
In this study, separate classifiers have been used for the workload 
induced by the AT and the MC type of tertiary task. The spatial maps 
of the classifier weights differed between those modes, but there was no 
systematic evaluation to dissociate between those types of workload.
Note that the high inter-subject variability, which is a challenge 
for many BCI applications, comes as an advantage here: for neuro-
usability studies, top subjects (with respect to the detectability of 
relevant EEG components) of a study can be selected according to 
the appropriateness of their brain signals.
3.4 Cognition of Music
In this section, we show how BCI technology can be applied to 
study the cognition of music. In particular, it is demonstrated that 
an advanced method for single-trial ERP classification, that was 
developed in BCI research (Blankertz et al., 2010b) allows to reveal 
unconsciously perceived structures of music (Sturm et al., 2010).
Time (min)
Figure 10 | The exact time course of the classifier output for the best 
performing subject (lower panel), and the corresponding binary high/
low workload indication used to control the mitigation (middle panel), in 
comparison with the true high and low workload conditions (upper 
panel) for auditory workload (95.6% correct).
(
)
(
)
Figure 11 | Left: Chord distances according to Lerdahl’s theory of tonal 
pitch space (Lerdahl, 2001). Right: The blue colored curve shows the 
subjective rating of participant VPcab which reflects only the distance of the 
fundamental tones, but does respect harmonical aspects. The orange 
colored line shows the output of the classifier. If reflects much better the 
musical structure of the stimuli than the behavioral data. (In the labels on 
the x-axis small and large font size corresponds to minor and 
major intervals).

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  12
Blankertz et al.	
Non-medical uses of BCI technology
the set of selectable items is reduced until a single link is chosen. 
More, (Scherer et al., 2007) reports Google Earth to be control­
led by BCI.
Creative activity is supported by a BCI-controlled brain painting 
application that exploits visual P300 signals. By concentration on 
selectable fields of a tool matrix the user can select simple paint­
ing tools, colors, shapes, etc., position the tools on a digital canvas 
and paint geometric shapes (Kübler et al., 2008). The application 
has been used by a number of ALS patients and a healthy artist. 
Although restricted in the type of tools, it enables an expression 
of creativity while by-passing motor pathways.
4.2 Games
There is a wide range from strictly medical to completely non-
medical BCI-controlled gaming applications. The design can be 
such that the applications is controlled by BCI alone, or that BCI 
is an additional input which augments a classical control. A sur­
vey that discusses approaches and requirements of BCI-controlled 
games on a general level is given in Nijholt (2009) and Lécuyer et al. 
(2008) provides a nice overview of several BCI games and virtual 
environment applications.
4.2.1 Games controlled by BCI only
The medical use of BCI-controlled games is quite obvious – gaming 
can be an excellent motivation to spend time with a BCI system 
in order to achieve better control. These improvements can be 
expected by playing games that demand long-time concentration 
by the subject if the game rewards a subject for an increased SNR 
of the EEG signal exploited for BCI control. This can be realized, 
e.g., by high scores for increased control speed or by a more precise 
timing of the control signals. Abilities acquired during gaming will 
have an immediate impact on the performance of the subject in 
other BCI applications, like spelling, environmental control, etc.
Gaming applications of this type typically have the simple char­
acter of a neuro-feedback training. Many of them are used in a 
research context and only a few examples can be mentioned here. 
The BrainBall game (Hjelm and Browall, 2000) was introduced to 
learn the control of the level of relaxation expressed by the occipital 
alpha intensity. To improve the concentration ability on blinking 
areas on the computer screen, e.g., an SSVEP game (Lalor et al., 
2005) can be used. Event-related potentials are exploited in the 
MindGame (Finke et al., 2009) which translates detected P300 com­
ponents into movements of a character on a three-dimensional 
game board. General control via motor paradigms can be trained 
with, e.g., BCI-PacMac (Krepki et al., 2007), the quick generation of 
brisk motor imagery based BCI-commands is used as feedback to 
train BCI reaction time in a goalkeeper game (Ramsey et al., 2009). 
Apart from their novel control concept (compared to standard 
games), these approaches do not have an outstanding attractiveness 
or long-time immersive character due to their simplicity whereas 
their usefulness for the training of patients is obvious.
A recently published gaming application that requires simple two-
class control but is more complex with respect to requirements for 
timing precision and its physical interactions, is a BCI-controlled pin­
ball machine (Tangermann et al., 2009), see Figure 12. This applica­
tion has proven that BCI control signals derived from motor imagery 
can be precise enough in timing to play a fast and reactive game in 
Different complex acoustical features of chords are processed 
in a sensory and a cognitive way in the brain. The inhomogeneity 
of the subjects’ behavior, however, suggests that the ability to uti­
lize these processes substantially differs between subjects even in a 
subgroup of 13 musicians. Utilizing machine learning based ERP 
analysis, developed in the framework of BCI research, can reveal 
at which stage of neuronal processing the perception of music is 
affected differently in certain subjects.
4 BCI for Entertainment
Finally, we discuss applications of BCI technology that have a dif­
ferent flavor than the ones discussed above. Here, we present some 
entertainment applications in which the appeal arise through the 
fact that they are controlled directly from the brain, like brain paint­
ing or games involving BCI control.
4.1 Media applications
Media applications are equally attractive to use for healthy sub­
jects and patients. It is worth to take a closer look at typical media 
of activities like the managing of photo-, video-, and music col­
lections, web surfing, the sharing of media with friends and rela­
tives, painting, presenting photos or videos in small shows to 
others, preparing playlists for later use, and of course the con­
sumption of music and media for pure self-entertainment or 
edutainment. On a more conceptual level, these activities can 
be categorized in exploration, social interaction, self-expression 
and consumption.
For severely paralyzed patients who are dependent on assistive 
technology like BCI to use media applications, the media applica­
tions have to take the limitations of control signals into consid­
eration. Ideally, the user should be enabled to express himself by 
creative or hedonic interaction with the media, and enjoy social 
activities triggered by the results of his interaction with the media, 
although the complexity of the user interface is limited and control 
signals are not fully reliable. As these restrictions are very similar 
to those that apply to mobile media applications on small hand-
held devices (Murray-Smith, 2009; Williamson et al., 2009), the 
development of BCI-controlled applications can profit from the 
community in the field of human–computer interaction (HCI) that 
constantly develops new interaction models for mobile use.
As the social interaction and embedding of a patient plays a 
crucial role for his/her quality of life, media applications have a 
high potential to improve the life of a patient, although they are 
of non-medical nature.
Although BCI-controlled media applications currently still are 
in their infancy, a number of interesting applications has been 
reported so far that go beyond the scope of text input applications 
like Hex-o-Spell (Blankertz et al., 2007b; Williamson et al., 2009), 
Dasher (Wills and MacKay, 2006), or applications inspired by the 
original P300 speller grid of Farwell and Donchin (1988).
The BCI-controlled web browser interface (Nessi, Bensch et al., 
2007) enables users not only to browse web pages, but to access 
web-based services and applications in general. It is platform-
independent and open source and has been used, e.g., with a two-
class motor imagery paradigm. Selectable items are highlighted 
by a color code. To select an item the user has to generate the type 
of control command with the corresponding color. Step by step, 

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  13
Blankertz et al.	
Non-medical uses of BCI technology
imagery commands and mental rotation) trained on an offline 
calibration run was applied online in sliding windows every 40 ms 
during the gaming phase. For each movement step within the tetris 
game, classifier outputs were accumulated and the action corre­
sponding to the highest value was triggered in case the probability 
exceeded a certain threshold. This game was not systematically 
evaluated in a study.
However, BCI-controlled gaming applications can provide even 
more added value in terms of social integration, as a paralyzed 
player can cooperate or compete with other, possibly healthy gam­
ers. In the simplest possible scenario, a slow strategic game like, e.g., 
chess that does not require fast decisions, a patient and a healthy 
player will meet on common ground, express and compare their 
cognitive abilities, learn about each other via the game. By empha­
sizing the interaction on a mental level, the degree of virtual dis­
ability is reduced during these interactions. Cooperational games, 
of course, where both players interact to reach a common goal, will 
provide even stronger added value in this respect.
Artificially biased gaming scenarios can provide for a fair bal­
ance: in a game like speed chess or tetris, where a player clearly 
profits from fast and precise-in-time control commands, healthy 
players can deliberately be slowed down until both gamers have 
approximately the same level of control. This can be accomplished, 
e.g., by adding delays to keyboard inputs of the able-bodied person 
and by adding an amount of uncertainty to each control decision. 
Although this might not look appealing to a healthy person on a 
first glance, it would be a good opportunity for healthy persons 
in the social environment of the patient to understand better the 
degree of handicap that the patient has to cope with.
Both approaches (slow strategic games and quick reactive 
games) open up the possibility to play remotely over the inter­
net. Joining a gaming community has the potential to create new 
contacts. Interaction via BCI-controlled gaming could build up 
patient- or mixed communities.
Planning the creation of a new game, the restricted information 
transfer rate has to be taken into account. The greatest challenge 
is to design a user interface for the game that hides the input 
complexity good enough from the user to be suitable, e.g., for a 
slow two-class control signal, but still to provide a rich enough 
decision space to be appealing. Partly, the lack of control accuracy 
can be compensated by rich and timely feedback during every 
control decision initiated by the user. This is a fruitful field of 
cooperation for the BCI research community with designers from 
the HCI community.
4.2.2 Games with additional input from BCI
Although using a BCI as the only source of control input for a game 
can be very appealing as it is considered a “cool” and still new form 
of interface (cf. for example the BCI-controlled pinball machine), 
it is, of course, possible to use BCI-control as an additional control 
channel for all types of games. In the near future, when hardware 
costs will have decreased to a suitable level, and when robustness 
of the EEG recording devices is increased to meet the expectations 
on the gaming market, healthy users will be able to explore BCI in 
addition to game-pad, mouse or keyboard input devices in order 
to enrich the interaction space. A further boost is to be expected, 
when sensitive and robust dry electrode systems appear on the 
real-time. Although a trade-off between timing precision and classifi­
cation precision had to be found individually even for good subjects, 
the game was perceived as highly immersive and motivating.
Brain–computer interfacing games involving other mental 
strategies for control can be used to confirm neurophysiological 
findings in a rigorous manner. An example that is appealing due 
to its ecological validity of the control paradigm is the video game 
Tetris (Wikipedia, 2009). In this game pieces which are falling down 
slowly can be moved horizontally either to the left or to the right 
and can be rotated in steps of 90° by the player. In the BCI-version 
of the game, left and right hand motor imagery is used to move 
the pieces and mental rotation (Ditunno and Mann, 1990) lets the 
piece rotate clockwise and foot motor imagery allows to drop it. 
While the motor commands have been extensively used in many 
BCI applications, the use of the cognitive task mental rotation adds 
in very naturally in the Tetris game. In our pilot study, we could 
confirm the right parietal focus (Farah, 1989; Harris et al., 2000; 
Heil, 2002; Roberts and Bell, 2003; Windischberger et al., 2003; 
Gootjes et al., 2008; depending on task and gender it may also be 
left parietal, Mehta and Newcombe, 1991; see also the discussion 
of laterality in Milivojevic et al., 2009) of neuronal activity during 
mental rotation, see Figure 13. A four-class classifier (three motor 
Figure 12 | Overview of a BCI system for the control of a pinball machine 
by motor imagery of, e.g., left and right hand imagined movements.
Figure 13 | Brain–computer interfacing controlled tetris game. Left: A 
volunteer is playing a BCI-controlled version of the Tetris computer game. He 
uses left and right hand motor imagery to move the falling pieces horizontally, 
mental rotation to rotate it clockwise and foot motor imagery to let it drop. 
Right: The map shows the activation pattern during mental rotation in the 
tetris game (band-power in the beta-band 18–24 Hz with red color indicating 
event-related desynchronization, i.e., activation of the corresponding cortical 
area). The right parietal focus is in line with the literature.

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  14
Blankertz et al.	
Non-medical uses of BCI technology
Blankertz, B., Lemm, S., Treder, M. S., 
Haufe, S., and Müller, K.-R. (2010b). 
Single-trial analysis and classifica­
tion of ERP components – a tuto­
rial. Neuroimage (in press). Available 
at http://dx.doi.org/10.1016/j.
neuroimage.2010.06.048
Blankertz, B., Tomioka, R., Lemm, S., 
Kawanabe, M., and Müller, K.-R. 
(2008a). Optimizing spatial filters 
for robust EEG single-trial analysis. 
IEEE Signal Process. Mag. 25, 41–56. 
Available at http://dx.doi.org/10.1109/
MSP.2008.4408441
Blankertz, B., Losch, F., Krauledat, M., 
Dornhege, G., Curio, G., and Müller, 
K.-R. (2008b). The Berlin brain–com­
puter interface: accurate performance 
from first-session in BCI-naive sub­
jects. IEEE Trans. Biomed. Eng. 55, 
2452–2462. Available at http://dx.doi.
org/10.1109/TBME.2008.923152
Blumberg, J., Rickert, J., Waldert, S., 
Schulze-Bonhage, A., Aertsen, A., and 
Mehring, C. (2007). Adaptive classifi­
cation for brain computer interfaces. 
Conf. Proc. IEEE Eng. Med. Biol. Soc. 
2007, 2536–2539.
Brookhuis, K., and de Waard, D. (1993). 
The use of psychophysiology to 
assess driver status. Ergonomics 36, 
1099–1110.
Carpi, F., and De Rossi, D. (2005). 
Electroactive polymer-based devices 
for e-textiles in biomedicine. IEEE 
Trans. Inf. Technol. Biomed. 9, 295–318. 
T., Olmstead, R. E., Tremoulet, P. D., 
and Craven, P. L. (2007). EEG corre­
lates of task engagement and mental 
workload in vigilance, learning, and 
memory tasks. Aviat. Space Environ. 
Med. 78, B231–B244.
Bießmann, F., Meinecke, F. C., Gretton, 
A., Rauch, A., Rainer, G., Logothetis, 
N., and Müller, K.-R. (2009). Temporal 
kernel canonical correlation analysis 
and its application in multimo­
dal neuronal data analysis. Mach. 
Learn. 79, 5–27. Available at http://
www.springerlink.com/content/
e1425487365v2227
Birbaumer, N. (2006). Brain–computer-
interface research: coming of age. Clin. 
Neurophysiol. 117, 479–483.
Birbaumer N., and Cohen, L. (2007). 
Brain–computer interfaces: commu­
nication and restoration of movement 
in paralysis. J. Physiol. 579, 621–636.
Birbaumer, N., Ghanayim, N., 
Hinterberger, T., Iversen, I., Kotchoubey, 
B., Kübler, A., Perelmouter, J., Taub, 
E., and Flor, H. (1999). A spelling 
device for the paralysed. Nature 398, 
297–298.
Birbaumer, N., Hinterberger, T., Kübler, 
A., and Neumann, N. (2003). The 
thought-translation device (TTD): 
neurobehavioral mechanisms and 
clinical outcome. IEEE Trans. Neural 
Syst. Rehabil. Eng. 11, 120–123.
Birbaumer, N., Kübler, A., Ghanayim, 
N., Hinterberger, T., Perelmouter, J., 
References
Allison, B., Lüth, T., Valbuena, D., 
Teymourian, A., Volosyak, I., and 
Gräser, A. (2009). BCI demograph­
ics: how many (and what kinds of) 
people can use an SSVEP BCI? IEEE 
Trans. Neural Syst. Rehabil. Eng. 18, 
107–116.
Allison, B., McFarland, D., Schalk, G., 
Zheng, S., Jackson, M., and Wolpaw, 
J. (2008). Towards an independent 
brain–computer interface using steady 
state visual evoked potentials. Clin. 
Neurophysiol. 119, 399–408.
Allison, B., Wolpaw, E., and Wolpaw, J. 
(2007). Brain–computer interface sys­
tems: progress and prospects. Expert 
Rev. Med. Devices 4, 463–474.
Baek, J.-Y., An, J.-H., Choi, J.-M., Park, 
K.-S., and Lee, S.-H. (2008). Flexible 
polymeric dry electrodes for the 
long-term monitoring of ECG. Sens. 
Actuators A Phys. 143, 423–429.
Bensch, M., Karim, A., Mellinger, J., 
Hinterberger, T., Tangermann, M., 
Bogdan, M., Rosenstiel, W., and 
Birbaumer, N. (2007). Nessi: an eeg 
controlled web browser for severely 
paralyzed patients. Comput. Intell. 
Neurosci. 2007, Article ID 71863.
Bergey, G. E., Squires, R. D., and Sipple, W. 
C. (1971). Electrocardiogram record­
ing with pasteless electrodes. IEEE 
Trans. Biomed. Eng. 18, 206–211.
Berka, C., Levendowski, D. J., Lumicao, 
M. N., Yau, A., Davis, G., Zivkovic, V. 
Kaiser, J., Iversen, I., Kotchoubey, B., 
Neumann, N., and Flor, H. (2000). 
The thought translation device 
(TTD) for completely paralyzed 
patients. IEEE Trans. Rehabil. Eng. 
8, 190–193.
Blankertz, B., Curio, G., and Müller, 
K.-R. (2002). Classifying single trial 
EEG: towards brain computer inter­
facing. Adv. Neural Inf. Process. Syst., 
14, 157–164.
Blankertz, B., Dornhege, G., Krauledat, M., 
Müller, K.-R., and Curio, G. (2007a). 
The non-invasive Berlin brain–com­
puter interface: fast acquisition of effec­
tive performance in untrained subjects. 
Neuroimage 37, 539–550. Available 
at http://dx.doi.org/10.1016/j.
neuroimage.2007.01.051
Blankertz, B., Krauledat, M., Dornhege, 
G., Williamson, J., Murray-Smith, R., 
and K.-Müller, R. (2007b). “A note 
on brain actuated spelling with the 
Berlin brain–computer interface,” in 
Universal Access in HCI, Part II, HCII 
2007, ser. LNCS, ed. C. Stephanidis, Vol. 
4555 (Berlin, Heidelberg: Springer), 
759–768.
Blankertz, B., Sannelli, C., Halder, S., 
Hammer, E. M., Kübler, A., Müller, 
K.-R., Curio, G., and Dickhaus, T. 
(2010a). Neurophysiological predic­
tor of SMR-based BCI performance. 
Neuroimage 51, 1303–1309. Available 
at http://dx.doi.org/10.1016/j.
neuroimage.2010.03.022
sider also applications that are beyond the classical paradigms 
for the disabled where BCI systems have helped to restore 
­communication ability.
Recently, building on BCI technology more general measure­
ment devices are developed capable of assessing and decoding more 
generic brain states in real-time. Successful examples of such brain 
state detection that have been outlined in this paper are seam­
less measurements of workload and performance capability. An 
accurate analysis of the human brain state can be employed to 
optimize state dependent man–machine interaction. Recent studies 
go beyond this by indicating that it might become possible to detect 
states that foreshadow errors during complex cognitive decision 
tasks (Eichele et al., 2010) with BCI technology.
We conclude that non-invasive BCI technology may change the 
way that we will in the future interact with computers. This will 
hold for both, healthy and disabled users.
Acknowledgments
We are indebted to the reviewers whose constructive comments on the 
original version of this paper help to greatly improve this paper. The 
studies were partly supported by the Bundesministerium für Bildung 
und Forschung (BMBF), Fkz 01IB001A/B, 01GQ0850, by the German 
Science Foundation (DFG, contract MU 987/3-1), and by the European 
ICT Programme Project FP7-224631 and 216886. This paper only 
reflects the authors’ views and funding agencies are not liable for any 
use that may be made of the information contained herein.
market that are capable of recording neural signals beyond occipi­
tal alpha or muscle artifacts only. However, it is yet unclear how 
smoothly the simultaneous use of traditional input devices and BCI 
can be coordinated, and what kind of BCI paradigms prove stable 
enough in such an environment. Significant further research will 
be required that allows to correlate activities between modalities 
(see Bießmann et al., 2009) and moreover that can compensate 
selectively non-stationarities within the different modalities (see 
von Bünau et al., 2009).
Given the availability of affordable recording devices, meth­
ods for mental state monitoring might have a strong impact for 
gaming. Mental state monitoring is a field strongly related to 
BCI, as it uses similar analysis methods to estimate user states 
in real-time. Examples are the monitoring of the level of mental 
workload, concentration ability, the ability to react quickly, etc. 
(see Section 3.2). If a game engine can make use of this additional 
user state information, the course of the game can be changed 
appropriately, the complexity level of tasks can be adapted, etc., 
in order to increase the level of immersion and entertainment. 
Applying this technique would enable to tailor a game individu­
ally to the gamer.
5 Conclusion
In the past years, BCI systems have become significantly more 
usable and accurate through the use of modern machine learn­
ing and signal processing technology. This has allowed to con­

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  15
Blankertz et al.	
Non-medical uses of BCI technology
Hoffmann, K.-P., and Ruff, R. (2007). 
“Flexible dry surface-electrodes for 
ECG long-term monitoring,” in 
Engineering in Medicine and Biology 
Society, EMBS 2007. 29th Annual 
International Conference of the IEEE, 
Lyon, 5739–5742.
Höhne, J., Schreuder, M., Blankertz, 
B., and Tangermann, M. (2010). 
“Two-dimensional auditory P300 
speller with predictive text system,” 
in Proceedings of the 32nd Annual 
International IEEE EMBS Conference 
(Buenos Aires, Argentina), Vol. 1, 
4185–4188.
Hwang, H. J., Kwon, K., and Im, C. H. 
(2009). Neurofeedback-based motor 
imagery training for brain–computer 
interface (BCI). J. Neurosci. Methods 
179, 150–156.
Kaper, M., and Ritter, H. (2004). 
“Generalizing to new subjects in 
brain–computer interfacing,” in 
Proceedings of the 26th Annual 
International Conference IEEE EMBS, 
San Francisco, 4363–4366.
Klimesch, W. (1999). EEG alpha and theta 
oscillations reflect cognitive and mem­
ory performance: a review and analy­
sis. Brain Res. Rev. 29, 169–195.
Klimesch, W., Sauseng, P., and Gerloff, C. 
(2003). Enhancing cognitive perform­
ance with repetitive transcranial mag­
netic stimulation at human individual 
alpha frequency. Eur. J. Neurosci. 17, 
1129–1133.
Kohlmorgen, J., Dornhege, G., Braun, M., 
Blankertz, B., Müller, K.-R., Curio, G., 
Hagemann, K., Bruns, A., Schrauf, M., 
and Kincses, W. (2007). “Improving 
human performance in a real oper­
ating environment through real-
time mental workload detection,” in 
Toward Brain–Computer Interfacing, 
eds G. Dornhege, J. del R. Millán, T. 
Hinterberger, D. J. McFarland, and 
K.-R. Müller (Cambridge, MA: MIT 
press), 409–422.
Krauledat, M., Tangermann, M., 
Blankertz, B., and Müller, K.-R. (2008). 
Towards zero training for brain–com­
puter interfacing. PLoS ONE 3, e2967. 
doi:10.1371/journal.pone.0002967
Krepki, R., Blankertz, B., Curio, G., and 
Müller, K.-R. (2007). The Berlin 
brain–computer interface (BBCI): 
towards a new communication chan­
nel for online control in gaming 
applications. J. Multimed. Tool Appl. 
33, 73–90. Available at http://dx.doi.
org/10.1007/s11042-006-0094-3
Krumhansl, C. L., and Kessler, E. J. (1982). 
Tracing the dynamic changes in per­
ceived tonal organization in a spatial 
representation of musical keys. Psychol. 
Rev. 89, 334–368.
Krusienski, D. J., and Wolpaw, J. R. (2009). 
Brain–computer interface research at 
the wadsworth center developments in 
recognition methods. Hum. Factors 
40, 79–91.
Gootjes, L., Bruggeling, E. C., Magnée, 
T., and Van Strien, J. W. (2008). Sex 
differences in the latency of the late 
event-related potential mental rota­
tion effect. Neuroreport 19, 349–353.
Grosse-Wentrup, M., Scholkopf, B., and 
Hill, J. (2010). Causal influence of 
gamma oscillations on the sensorimo­
tor rhythm. Neuroimage. doi:10.1016/j.
neuroimage.2010.04.265. [Epub ahead 
of print].
Guderian, S., Schott, B. H., Richardson-
Klavehn, A., and Düzel, E. (2009). 
Medial temporal theta state before an 
event predicts episodic encoding suc­
cess in humans. Proc. Natl. Acad. Sci. 
U.S.A. 106, 5365–5370.
Guger, C., Daban, S., Sellers, E., Holzner, 
C., Krausz, G., Carabalona, R., 
Gramatica, F., and Edlinger, G. (2009). 
How many people are able to control a 
P300-based brain–computer interface 
(BCI)? Neurosci. Lett. 462, 94–98.
Hamadicharef, B., Zhang, H., Guan, C., 
Wang, C., Phua, K. S., Tee, K. P., and 
Ang, K. K. (2009). “Learning eeg-
based spectral-spatial patterns for 
attention level measurement,” in IEEE 
International Symposium on Circuits 
and Systems (ISCAS2009), Taiwan, 
1465–1468. Available at http://hal.
archives-ouvertes.fr/inria-00441412/
en/
Hankins T. C., and Wilson, G. F. (1998). A 
comparison of heart rate, eye activity, 
EEG and subjective measures of pilot 
mental workload during flight. Aviat. 
Space Environ. Med. 69, 360–367.
Hanslmayr, S., Sauseng, P., Doppelmayr, 
M., Schabus, M., and Klimesch, W. 
(2005). Increasing individual upper 
alpha power by neurofeedback 
improves cognitive performance in 
human subjects. Appl. Psychophysiol. 
Biofeedback 30, 1–10.
Harris, I. M., Egan, G. F., Sonkkila, C., 
Tochon-Danguy, H. J., Paxinos, G., 
and Watson, J. D. (2000). Selective 
right parietal lobe activation during 
mental rotation: a parametric PET 
study. Brain 123(Pt 1), 65–73.
Heil, M. (2002). The functional signifi­
cance of ERP effects during men­
tal rotation. Psychophysiology 39, 
535–545.
Hill, N., Lal, T., Bierig, K., Birbaumer, N., 
and Schölkopf, B. (2005). “An audi­
tory paradigm for brain–computer 
interfaces,” in Advances in Neural 
Information Processing Systems, eds 
L. K. Saul, Y. Weiss, and L. Bottou, 
Vol. 17 (Cambridge, MA: MIT Press), 
569–576.
Hjelm, S., and Browall, C. (2000). 
“Brainball – Using brain activity for 
cool competition,” in Proceedings of 
NordiCHI, Stockholm.
for mental rotation in normals and 
brain damaged subjects. Cortex 26, 
177–188.
Dobkin, B. (2007). Brain–computer inter­
face technology as a tool to augment 
plasticity and outcomes for neuro­
logical rehabilitation. J. Physiol. 579, 
637–642.
Dornhege, G., del R. Millán J., 
Hinterberger, T., McFarland, D. J., 
and Müller, K.-R. (eds.) (2007a). 
Toward Brain–Computer Interfacing. 
Cambridge, MA: MIT Press.
Dornhege, G., Krauledat, M., Müller, 
K.-R., and Blankertz, B. (2007b). 
“General signal processing and 
machine learning tools for BCI,” in 
Toward Brain–Computer Interfacing, 
eds G. Dornhege, J. del R. Millán, T. 
Hinterberger, D. J. McFarland, and 
K.-R. Müller (Cambridge, MA: MIT 
Press), 207–233.
Eichele, H., Juvodden, H. T., Ullsperger, M., 
and Eichele, T. (2010). Mal-adaptation 
of event-related EEG responses pre­
ceding performance errors. Front. 
Hum. Neurosci. 4:65. doi: 10.3389/
fnhum.2010.00065
Elbert, T., Rockstroh, B., Lutzenberger, 
W., and Birbaumer, N. (1980). 
Biofeedback of slow cortical poten­
tials .I. Electroencephalogr. Clin. 
Neurophysiol. 48, 293–301.
Farah, M. J. (1989). The neural basis of 
mental imagery. Trends Neurosci. 12, 
395–399.
Farwell, L., and Donchin, E. (1988). 
Talking off the top of your head: 
toward a mental prosthesis utiliz­
ing event-related brain potentials. 
Electroencephalogr. Clin. Neurophysiol. 
70, 510–523.
Fazli, S., Popescu, F., Danóczy, M., 
Blankertz, B., Müller, K.-R., and Grozea, 
C. (2009). Subject-independent men­
tal state classification in single trials. 
Neural Netw. 22, 1305–1312.
Fernández, G., Effern, A., Grunwald, T., 
Pezer, N., Lehnertz, K., Dümpelmann, 
M., Van Roost, D., and Elger, C. E. 
(1999). Real-time tracking of memory 
formation in the human rhinal cor­
tex and hippocampus. Science 285, 
1582–1585.
Finke, A., Lenhardt, A., and Ritter, H. 
(2009). The mindgame: a P300-
based brain–computer interface game. 
Neural. Netw. 22, 1329–1333.
Gargiulo, G., Calvo, R. A., Bifulco, P., 
Cesarelli, M., Jin, C., Mohamed, A., 
and van Schaik, A. (2010). A new 
EEG recording system for passive dry 
electrodes. Clin. Neurophysiol. 121, 
686–693.
Gevins, A., Smith, M. E., Leong, H., L. 
McEvoy, Whitfield, S., Du, R., and 
Rush, G. (1998). Monitoring work­
ing memory load during compu­
ter-based tasks with EEG pattern 
Available at http://dx.doi.org/10.1109/
TITB.2005.854514
Catrysse, M., Puers, R., Hertleer, C., 
Langenhove, L. V., van Egmond, H., 
and Matthys, D. (2004). Towards the 
integration of textile sensors in a wire­
less monitoring suit. Sens. Actuators A 
Phys. 114, 302–311.
Cecotti, H. (2010). A self-paced and 
calibration-less SSVEP-based brain–
computer interface speller. IEEE Trans. 
Neural Syst. Rehabil. Eng. 18, 127–133.
Chen, Y. N., Mitra, S., and Schlaghecken, 
F. (2008). Sub-processes of working 
memory in the N-back task: an investi­
gation using ERPs. Clin. Neurophysiol. 
119, 1546–1559.
Cheng, M., Gao, X., Gao, S., and Xu, D. 
(2002). Design and implementation of 
a brain–computer interface with high 
transfer rates. IEEE Trans. Biomed. Eng. 
49, 1181–1186.
Cincotti, F., Mattia, D., Aloise, F., Bufalari, 
S., Schalk, G., Oriolo, G., Cherubini, 
A., Marciani, M. G., and Babiloni, F. 
(2008). Non-invasive brain–computer 
interface system: towards its applica­
tion as assistive technology. Brain Res. 
Bull. 75, 796–803.
Citi, L., Poli, R., Cinel, C., and Sepulveda, 
F. (2008). P300-based BCI mouse 
with genetically-optimized analogue 
control. IEEE Trans. Rehabil. Eng. 16, 
51–61.
Conradi, J., Blankertz, B., Tangermann, 
M., Kunzmann, V., and Curio, G. 
(2009). Brain–computer interfacing 
in tetraplegic patients with high spi­
nal cord injury. Int. J. Bioelectromagn. 
11, 65–68. Available at http://
ijbem.k.hosei.ac.jp/2006-/volume11/
number2/ 1102001.pdf
Cooper, N. R., Croft, R. J., Domineya, 
S. J., Burgessa, A. P., and Gruzeliera, 
J. H. (2003). Paradox lost? exploring 
the role of alpha oscillations dur­
ing externally vs. internally directed 
attention and the implications for 
idling and inhibition hypotheses. Int. 
J. Psychophysiol. 47, 65–74.
Coosemans, J., Hermans, B., and Puers, 
R. (2006). Integrating wireless ECG 
monitoring in textiles. Sens. Actuators 
A Phys. 130, 48–53.
Daly, J. J., and Wolpaw, J. R. (2008). 
Brain–computer interfaces in neuro­
logical rehabilitation. Lancet Neurol. 
7, 1032–1043.
Del Percio, C., Marzano, N., Tilgher, S., 
Fiore, A., Di Ciolo, E., Aschieri, P., Lino, 
A., Toràn, G., Babiloni, C., and Eusebi, 
F. (2007). Pre-stimulus alpha rhythms 
are correlated with post-stimulus sen­
sorimotor performance in athletes 
and non-athletes: a high-resolution 
EEG study. Clin. Neurophysiol. 118, 
1711–1720.
Ditunno, P. L., and Mann, V. A. (1990). 
Right hemisphere specialization 

Frontiers in Neuroscience  |  Neuroprosthetics	
	
December 2010  | Volume 4  |  Article 198  |  16
Blankertz et al.	
Non-medical uses of BCI technology
IEEE Eng. Med. Biol. Soc. 2008, 
4495–4498.
Otmani, S., Pebayle, T., Roge, J., and 
Muzet, A. (2005). Effect of driving 
duration and partial sleep deprivation 
on subsequent alertness and perform­
ance of car drivers. Physiol. Behav. 84, 
5, 715–724.
Palva, S., and Palva, J. M. (2007). New 
vistas for alpha-frequency band 
oscillations. Trends Neurosci. 30, 
150–158.
Papadelis, C., Chen, Z., Kourtidou-
Papadeli, C., Bamidis, P., Chouvarda, 
I., Bekiaris, E., and Maglaveras, 
N. (2007). Monitoring sleepi­
ness with on-board electrophysi­
ological recordings for preventing 
sleep-deprived traffic accidents. 
Clin. Neurophysiol. 118, 1906–
1922. Available at http://dx.doi.
org/10.1016/j.clinph.2007.04.031
Parra, L., Alvino, C., Tang, A., Pearlmutter, 
B., Yeung, N., Osman, A., and Sajda, 
P. (2003). Single-trial detection in 
EEG and MEG: keeping it linear. 
Neurocomputing 52–54, 177–183.
Parra, L., Christoforou, C., Gerson, A., 
Dyrholm, M., Luo, A., Wagner, M., 
Philiastides, M., and Sajda, P. (2008). 
Spatiotemporal linear decoding of 
brain state. IEEE Signal Process. Mag. 
25, 107–15.
Parra, L. C., Spence, C. D., Gerson, A. D., 
and Sajda, P. (2005). Recipes for the 
linear analysis of EEG. Neuroimage 
28, 326–341.
Pfurtscheller, G., and da Silva, F. H. L. 
(1999). Event-related EEG/MEG syn­
chronization and desynchronization: 
basic principles. Clin. Neurophysiol. 
110, 11, 1842–1857.
Pfurtscheller, G., Müller, G. R., 
Pfurtscheller, J., Gerner, H. J., and 
Rupp, R. (2003). “Thought” – control 
of functional electrical stimulation 
to restore hand grasp in a patient 
with tetraplegia. Neurosci. Lett. 351, 
33–36.
Popescu, F., Fazli, S., Badower, Y., Blankertz, 
B., and Müller, K.-R. (2007). Single 
trial classification of motor imagina­
tion using 6 dry EEG electrodes. PLoS 
ONE, 2, e637. doi: 10.1371/journal.
pone.0000637
Ramsey, L., Tangermann, M., Haufe, S., 
and Blankertz, B. (2009). Practicing 
fast-decision BCI using a ‘goalkeeper’ 
paradigm. BMC Neurosci. 10(Suppl. 
1), P69. doi: 10.1186/1471-2202-10-
S1-P69.
Richardson, P. C., Coombs, F. K., and 
Adams, R. M. (1968). Some new 
electrode techniques for long-term 
physiologic monitoring. Aerosp. Med. 
39, 745–750.
Roberts, J., and Bell, M. (2003). Two- 
and three-dimensional mental rota­
tion tasks lead to different parietal 
Correction: actual causes of death in 
the United States, 2000. JAMA 293, 
293–294.
Morgan, S. T., Hansen, J. C., and Hillyard, S. 
A. (1996). Selective attention to stimu­
lus location modulates the steady-state 
visual evoke potential. Proc. Natl. Acad. 
Sci. U.S.A. 93, 4770–4774.
Muhlsteff, J., and Such, O. (2004). “Dry 
electrodes for monitoring of vital signs 
in functional textiles,” in Engineering 
in Medicine and Biology Society, 2004. 
IEMBS ’04. 26th Annual International 
Conference of the IEEE, Vol. 1, 
San Francisco, CA, 2212–2215.
Müller, K.-R., Tangermann, M., Dornhege, 
G., Krauledat, M., Curio, G., and 
Blankertz, B. (2008). Machine learning 
for real-time single-trial EEG-analysis: 
from brain–computer interfacing to 
mental state monitoring. J. Neurosci 
Methods 167, 82–90. Available 
at http://dx.doi.org/10.1016/j.
jneumeth.2007.09.022
Müller-Putz, G., Zimmermann, D., 
Graimann, B., Nestinger, K., Korisek, 
G., and Pfurtscheller, G. (2007). Event-
related beta EEG-changes during pas­
sive and attempted foot movements in 
paraplegic patients. Brain Res. 1137, 
84–91.
Murray-Smith, R. (2009). Empowering 
people rather than connecting them. 
Int. J. Mob. Hum. Comput. Interact. 1, 
18–28.
Neubauer, A. C., and Freudenthaler, H. H. 
(1995). Ultradian rhythms in cognitive 
performance: no evidence for a 1.5-h 
rhythm. Biol. Psychol. 40, 281–298.
Neuper, C., Müller, G., Kübler, A., 
Birbaumer, N., and Pfurtscheller, G. 
(2003). Clinical application of an eeg-
based brain–computer interface: a case 
study in a patient with severe motor 
impairment. Clin. Neurophysiol. 114, 
399–409.
Neuper, C., Schlögl, A., and Pfurtscheller, 
G. (1999). Enhancement of left-right 
sensorimotor EEG differences during 
feedback-regulated motor imagery. J. 
Clin. Neurophysiol. 16, 4, 373–382.
Nijholt, A. (2009). “Bci for games: a 
‘state of the art’ survey,” in ICEC ’08: 
Proceedings of the 7th International 
Conference on Entertainment 
Computing (Berlin, Heidelberg: 
Springer-Verlag), 225–228.
Nikulin, V. V., Hohlefeld, F. U., Jacobs, 
A. M., and Curio, G. (2008). Quasi-
movements: a novel motor-cognitive 
phenomenon. Neuropsychologia 
46, 727–742. Available at 
http://dx.doi.org/10.1016/j.
neuropsychologia.2007.10.008
Oehler, M., Neumann, P., Becker, M., 
Curio, G., and Schilling, M. (2008). 
Extraction of SSVEP signals of a 
capacitive EEG helmet for human 
machine interface. Conf. Proc. 
spectrum analysis. EURASIP J. Appl. 
Signal Processing 19, 3165–3174.
Lotte, F., Congedo, M., Lécuyer, A., 
Lamarche, F., and Arnaldi, B. (2007). 
A review of classification algorithms 
for EEG-based brain–computer inter­
faces. J. Neural Eng. 4, R1–R13.
Lotte, F., Guan, C., and Ang, K. K. (2009). 
Comparison of designs towards a 
subject-independent brain–compu­
ter interface based on motor imagery. 
Conf. Proc. IEEE Eng. Med. Biol. Soc. 
2009, 4543–4546.
Lu, S., Guan, C., and Zhang, H. (2009). 
Unsupervised brain computer inter­
face based on intersubject informa­
tion and online adaptation. IEEE 
Trans. Neural Syst. Rehabil. Eng. 17, 
135–145.
Luo, A., and Sullivan, T. J. (2010). A user-
friendly SSVEP-based brain–computer 
interface using a time-domain classi­
fier. J. Neural Eng. 7, 26010.
Maeder, C., Sannelli, C., Haufe, S., Lemm, 
S., and Blankertz, B. (2010). “Effect of 
prestimulus SMR amplitude on BCI 
performance,” in Poster at the TOBI 
Workshop ‘Integrating Brain–Computer 
Interfaces with Conventional Assistive 
Technology’, Graz.
Makeig S., and Jung, T.-P. (1996). Tonic, 
phasic, and transient EEG correlates 
of auditory awareness in drowsiness. 
Cogn. Brain Res. 4, 15–25.
Mathewson, K. E., Gratton, G., Fabiani, 
M., Beck, D. M., and Ro, T. (2009). To 
see or not to see: prestimulus alpha 
phase predicts visual awareness. J. 
Neurosci. 29, 2725–2732.
Mazaheri, A., Nieuwenhuis, I. L., van Dijk, 
H., and Jensen, O. (2009). Prestimulus 
alpha and mu activity predicts failure 
to inhibit motor responses. Hum. 
Brain Mapp. 30, 1791–1800.
McFarland, D. J., Krusienski, D. J., 
Sarnacki, W. A., and Wolpaw, J. R. 
(2008). Emulation of computer 
mouse control with a noninvasive 
brain–computer interface. J. Neural 
Eng. 5, 101–110.
Mehta, Z., and Newcombe, F. (1991). A 
role for the left hemisphere in spatial 
processing. Cortex 27, 153–167.
Middendorf, M., McMillan, G., 
Calhoun, G., and Jones, K. (2000). 
Brain–computer interfaces based 
on the steady-state visual-evoked 
response. IEEE Trans. Rehabil. Eng. 
8, 211–214.
Milivojevic, B., Hamm, J. P., and Corballis, 
M. C. (2009). Hemispheric dominance 
for mental rotation: it is a matter of 
time. Neuroreport 20, 1507–1512.
Mokdad, A. H., Marks, J. S., Stroup, D. F., 
and Gerberding, J. L. (2004). Actual 
causes of death in the United States, 
2000. JAMA 291, 1238–1245.
Mokdad, A. H., Marks, J. S., Stroup, 
D. F., and Gerberding, J. L. (2005). 
noninvasive communication and con­
trol. Int. Rev. Neurobiol. 86, 147–157.
Kübler, A. (2000). Brain–Computer 
Communication – Development 
of a Brain–Computer Interface for 
Locked-in Patients on the Basis of the 
Psychophysiological Self-Regulation 
Training of Slow Cortical Potentials 
(SCP). Tübingen: Schwäbische 
Verlagsgesellschaft.
Kübler, A., Furdea, A., Halder, S., and 
Hösle, A. (2008). “Brain painting – 
BCI meets art,” in Proceedings of the 
4th International Brain–Computer 
Interface Workshop and Training 
Course 2008, eds G. R. Müller-Putz, 
C. Brunner, R. Leeb, G. Pfurtscheller, 
and C. Neuper (Graz: Verlag der 
Technischen Universität), 361–366.
Kübler, A., Kotchoubey, B., Hinterberger, 
T., Ghanayim, N., Perelmouter, J., 
Schauer, M., Fritsch, C., Taub, E., and 
Birbaumer, N. (1999). The thought 
translation device: a neurophysi­
ological approach to communication 
in total motor paralysis. Exp. Brain Res. 
124, 223–232.
Kübler, A., Kotchoubey, B., Kaiser, J., 
Wolpaw, J., and Birbaumer, N. (2001). 
Brain–computer communication: 
unlocking the locked in. Psychol. Bull. 
127, 358–375.
Kübler, A., and Müller, K.-R. (2007). 
“An introduction to brain com­
puter interfacing,” in Toward 
Brain–Computer Interfacing, eds 
G. Dornhege, J. del R. Millán, T. 
Hinterberger, D. J. McFarland, and 
K.-R. Müller (Cambridge, MA: MIT 
press), 1–25.
Kübler, A., Nijboer, F., Mellinger, J., 
Vaughan, T. M., Pawelzik, H., Schalk, 
G., D. J. McFarland, Birbaumer, N., 
and Wolpaw, J. R. (2005). Patients with 
ALS can use sensorimotor rhythms to 
operate a brain–computer interface. 
Neurology 64, 1775–1777.
Lalor, E., Kelly, S., Finucane, C., Burke, R., 
Smith, R., Reilly, R., and McDarby, G. 
(2005). Steady-state VEP-based brain–
computer interface control in an 
immersive 3D gaming environment. 
EURASIP J. Appl. Signal Processing 
19, 3156.
Lécuyer, A., Lotte, F., Reilly, R. B., Leeb, 
R., Hirose, M., and Slater, M. (2008). 
Brain–computer interfaces, virtual 
reality, and videogames. Computer 
41, 66–72.
Lerdahl, F. (2001). Tonal Pitch Space. New 
York: Oxford University Press.
Li, Y., and Guan, C. (2006). An extended 
EM algorithm for joint feature extrac­
tion and classification in brain–com­
puter interfaces. Neural. Comput. 18, 
2730–2761.
Lin, C. T., Wu, R. C., Jung, T. P., Liang, S. 
F., and Huang, T. Y. (2005). Estimating 
driving performance based on eeg 

www.frontiersin.org	
December 2010  | Volume 4  |  Article 198  |  17
Blankertz et al.	
Non-medical uses of BCI technology
for brain–computer interfaces? IEEE 
Trans. Neural Syst. Rehabil. Eng. 14, 
244–246.
Windischberger, C., Lamm, C., Bauer, H., 
and Moser, E. (2003). Human motor 
cortex activity during mental rotation. 
Neuroimage 20, 225–232.
Wolpaw, J. R., Birbaumer, N., McFarland, 
D. J., Pfurtscheller, G., and Vaughan, T. 
M. (2002). Brain–computer interfaces 
for communication and control. Clin. 
Neurophysiol. 113, 6, 767–791.
Wolpaw, J., McFarland, D., and Vaughan, 
T. (2000). Brain–computer interface 
research at the Wadsworth center. 
IEEE Trans. Rehabil. Eng. 8, 222–226.
Xu, J., Kochanek, K. D., Murphy, S. L., and 
Tejada-Vera, B. (2010). Deaths: final 
data for 2007. Natl. Vital Stat. Rep. 
58, 1–137.
Zander, T., and Jatzev, S. (2009). “Detecting 
affective covert user states with pas-
sive brain–computer interfaces,” in 
Affective Computing and Intelligent 
Interaction and Workshops, 2009. ACII 
2009. 3rd International Conference on 
September 2009, Amsterdam, 1–9.
Conflict of Interest Statement: The 
authors declare that the research was 
conducted in the absence of any com-
mercial or financial relationships that 
could be construed as a potential conflict 
of interest.
Received: 09 June 2010; accepted: 15 
November 2010; published online: 08 
December 2010.
Citation: Blankertz B, Tangermann M, 
Vidaurre C, Fazli S, Sannelli C, Haufe S, 
Maeder C, Ramsey L, Sturm I, Curio G 
and Müller K-R (2010) The Berlin brain–
computer interface: non-medical uses of 
BCI technology. Front. Neurosci. 4:198. 
doi: 10.3389/fnins.2010.00198
This article was submitted to Frontiers in 
Neuroprosthetics, a specialty of Frontiers 
in Neuroscience.
Copyright © 2010 Blankertz, Tangermann, 
Vidaurre, Fazli, Sannelli, Haufe, Maeder, 
Ramsey, Sturm, Curio and Müller. This is 
an open-access article subject to an exclusive 
license agreement between the authors and 
the Frontiers Research Foundation, which 
permits unrestricted use, distribution, and 
reproduction in any medium, provided the 
original authors and source are credited.
opment program: at home with BCI. 
IEEE Trans. Neural Syst. Rehabil. Eng. 
14, 229–233.
Vidaurre, C., and Blankertz, B. (2010). 
Towards a cure for BCI illiteracy. 
Brain Topogr. 23, 194–198 Available 
at http://dx.doi.org/10.1007/s10548-
009-0121-6
Vidaurre, C., Sannelli, C., Müller, K.-R., 
and Blankertz, B. (2010). Machine-
learning based Co-adaptive calibra-
tion. Neural Comput. (in press).
Vidaurre, C., Schlögl, A., Blankertz, B., 
Kawanabe, M., and Müller, K.-R. 
(2008). “Unsupervised adaptation of 
the LDA classifier for brain–compu-
ter interfaces,” in Proceedings of the 
4th International Brain–Computer 
Interface Workshop and Training Course 
2008 (Graz: Verlag der Technischen 
Universität), 122–127.
Vidaurre, C., Schlögl, A., Cabeza, R., 
Scherer, R., and Pfurtscheller, G. (2006). 
A fully on-line adaptive BCI. IEEE 
Trans. Biomed. Eng. 53, 6, 1214–1219.
Vidaurre, C., Schlögl, A., Cabeza, R., 
Scherer, R., and Pfurtscheller, G. 
(2007). Study of on-line adaptive 
discriminant analysis for EEG-based 
brain computer interfaces. IEEE Trans. 
Biomed. Eng. 54, 3, 550–556.
von Bünau, P., Meinecke, F. C., Király, F., 
and Müller, K.-R. (2009). Finding sta-
tionary subspaces in multivariate time 
series. Phys. Rev. Lett. 103, 214101.
Wang, Y., Hong, B., Gao, X., and Gao, 
S. (2007). “Implementation of a 
brain–computer interface based on 
three states of motor imagery,” in 
Engineering in Medicine and Biology 
Society, 2007 EMBS 2007 29t. Annual 
International Conference of the IEEE, 
Lyon, 14, 234–240.
Wikipedia. (2009). Tetris – wikipedia, the 
free encyclopedia. Available at http://
en.wikipedia.org/wiki/Tetris [Accessed 
06 October 2009].
Williamson, J., Murray-Smith, R., 
Blankertz, B., Krauledat, M., and 
Müller, K.-R. (2009). Designing 
for uncertain, asymmetric control: 
Interaction design for brain–computer 
interfaces. Int. J. Hum. Comput. Stud. 
67, 827–841. Available at http://dx.doi.
org/10.1016/j.ijhcs.2009.05.009
Wills, S., and MacKay, D. (2006). 
DASHER – an efficient writing ­system 
Sellers, E. W., Turner, P., Sarnacki, W. A., 
Mcmanus, T., Vaughan, T. M., and 
Matthews, R. (2009). “A novel dry elec-
trode for brain–computer interface,” 
in Proceedings of the 13th International 
Conference on Human-Computer 
Interaction. Part II, (Berlin, Heidelberg: 
Springer-Verlag), 623–631.
Sterman, M. B., and Mann, C. A. (1995). 
Concepts and applications of EEG 
analysis in aviation performance eval-
uation. Biol. Psychol. 40, 115–130.
Sturm, I., Curio, G., and Blankertz, B. 
(2010). “Single-trial ERP analysis 
reveals unconsciously perceived struc-
tures of music,” in Poster at the TOBI 
Workshop ‘Integrating Brain–Computer 
Interfaces with Conventional Assistive 
Technology, Graz.
Subramanian, R. (2007). Motor Vehicle 
Traffic Crashes as a Leading Cause 
of Death in the USA, 2004. NHTSA, 
NHTSA-Report DOT HS 810 742.
Tangermann, M., Krauledat, M., Grzeska, 
K., Sagebaum, M., Blankertz, B., 
Vidaurre, C., and Müller, K.-R. (2009). 
Playing Pinball with Non-Invasive BCI, 
in Advances in Neural Information 
Processing Systems, Vol. 21 (Cambridge, 
MA: MIT Press), 1641–1648.
Thut, G., Nietzel, A., Brandt, S. A., and 
Pascual-Leone, A. (2006). Alpha-band 
electroencephalographic activity over 
occipital cortex indexes visuospatial 
attention bias and predicts visual 
target detection. J. Neurosci. 26, 
9494–9502.
Tomioka, R., and Müller, K. R. (2010). 
A regularized discriminative frame-
work for EEG based communication. 
Neuroimage 49, 415–432.
Treder, M. S., and Blankertz, B. (2010). 
(C)overt attention and visual speller 
design in an ERP-based brain–
computer interface. Behav. Brain 
Funct. 6, 28. Available at http://www.
behavioralandbrainfunctions.com/
content/6/1/28
van Dijk, H., Schoffelen, J. M., Oostenveld, 
R., and Jensen, O. (2008). Prestimulus 
oscillatory activity in the alpha band 
predicts visual discrimination ability. 
J. Neurosci. 28, 1816–1823.
Vaughan, T., McFarland, D., Schalk, G., 
Sarnacki, W., Krusienski, D., Sellers, 
E., and Wolpaw, J. (2006). The 
Wadsworth BCI research and devel-
laterality for men and women. Int. J. 
Psychophysiol. 50, 235–246.
Rockstroh, B., Birbaumer, N., Elbert, T., 
and Lutzenberger, W. (1984). Operant 
control of EEG and event-related and 
slow brain potentials. Biofeedback Self 
Regul. 9, 2, 139–160.
Sassaroli, A., Zheng, F., Hirshfield, L. 
M., Girouard, A., Solovey, E. T., and 
Jacob, R. J. K. (2008). Discrimination 
of mental workload levels in human 
subjects with functional near-infrared 
spectroscopy. J. Innov. Opt. Health Sci. 
1, 227–237.
Schaefer, R. S., Vlek, R. J., and Desain, 
P. (2010). Decomposing rhythm 
processing: electroencephalography of 
perceived and self-imposed rhythmic 
patterns. Psychol. Res. doi: 10.1007/
s00426-010-0293-4. [Epub ahead of 
print].
Schalk, G. (2008). Brain–computer sym-
biosis. J. Neural Eng. 5, P1–P15.
Scherer, R., Schloegl, A., Lee, F., Bischof, 
H., Jansa, J., and Pfurtscheller, G. 
(2007). The self-paced graz brain–
computer interface: methods and 
applications. Comput. Intell. Neurosci. 
2007, 79826.
Schreuder, M., Blankertz, B., and 
Tangermann, M. (2010). A new audi-
tory multi-class brain–computer inter-
face paradigm: Spatial hearing as an 
informative cue. PLoS ONE, 5, e9813. 
doi: 10.1371/journal.pone.0009813
Schubert, R., Haufe, S., Blankenburg, F., 
Villringer, A., and Curio, G. (2009). 
Now you’ll feel it – now you won’t: 
EEG rhythms predict the effective-
ness of perceptual masking. J. Cogn. 
Neurosci. 21, 2407–2419. Available 
at http://dx.doi.org/10.1162/
jocn.2008.21174
Schubert, R., Tangermann, M., Haufe, 
S., Sannelli, C., Simon, M., Schmidt, 
E. A., Kincses, W. E., and Curio, G. 
(2008). “Parieto-occipital alpha power 
indexes distraction during simulated 
car driving,” abstracts of the 14th 
World Congress of Psychophysiology. 
Int. J. Psychophysiol. 69. Available 
at http://dx.doi.org/10.1016/j.
ijpsycho.2008.05.033
Searle, A., and Kirkup, L. (2000). A direct 
comparison of wet, dry and insulat-
ing bioelectric recording electrodes. 
Physiol. Meas. 21, 271–283.
