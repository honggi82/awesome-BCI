ORIGINAL RESEARCH ARTICLE
published: 07 May 2012
doi: 10.3389/fnins.2012.00060
Comparison of dry and gel based electrodes for P300
brain–computer interfaces
Christoph Guger 1*, Gunther Krausz 1, Brendan Z. Allison2 and Guenter Edlinger 1
1 g.tec medical engineering GmbH, Guger Technologies OG, Graz, Styria, Austria
2 Department of Cognitive Science, University of California at San Diego, La Jolla, California, USA
Edited by:
Cuntai Guan, Institute for Infocomm
Research, Singapore
Reviewed by:
Dennis J. McFarland, Wadsworth
Center for Laboratories and Research,
USA
Michal Lavidor, Bar-Ilan University,
Israel
*Correspondence:
Christoph Guger, g.tec medical
engineering GmbH, Guger
Technologies OG, Herbersteinstrasse
60, A8010 Graz, Styria, Austria.
e-mail: guger@gtec.at
Most brain–computer interfaces (BCIs) rely on one of three types of signals in the elec-
troencephalogram (EEG): P300s, steady-state visually evoked potentials, and event-related
desynchronization. EEG is typically recorded non-invasively with electrodes mounted on
the human scalp using conductive electrode gel for optimal impedance and data quality.The
use of electrode gel entails serious problems that are especially pronounced in real-world
settings when experts are not available. Some recent work has introduced dry electrode
systems that do not require gel, but often introduce new problems such as comfort and
signal quality.The principal goal of this study was to assess a new dry electrode BCI system
in a very common task: spelling with a P300 BCI. A total of 23 subjects used a P300 BCI to
spell the word “LUCAS” while receiving real-time, closed-loop feedback. The dry system
yielded classiﬁcation accuracies that were similar to those obtained with gel systems. All
subjects completed a questionnaire after data recording, and all subjects stated that the
dry system was not uncomfortable.This is the ﬁrst ﬁeld validation of a dry electrode P300
BCI system, and paves the way for new research and development with EEG recording
systems that are much more practical and convenient in ﬁeld settings than conventional
systems.
Keywords: brain–computer interface, brain–machine interface, dry electrodes, gel electrodes, EEG, ERP, P300,
intendiX.
INTRODUCTION
Brain–computer interfaces (BCIs) allow communication without
movement. In a typical BCI, a user performs voluntary mental
tasks that each produce distinct patterns of electrical activity in
the electroencephalogram (EEG). Automated signal processing
software tries to identify which mental tasks a user performed
at speciﬁc times and thereby infer user intent. Most modern BCIs
rely on one of three types of mental tasks, which are associated
with different types of brain activity (Wolpaw et al., 2002):
Imagined movement, which produces event-related desynchro-
nization (ERD; Guger et al., 2003; Pfurtscheller et al., 2006;
Neuper et al., 2009; McFarland et al., 2010; Vidaurre et al., 2011);
Attention to oscillating visual stimuli, which produces steady-
state visual evoked potentials (SSVEP; Friman et al., 2007; Lin
et al., 2007; Ortner et al., 2011; Allison et al., 2012);
Attention to transient stimuli, which produces the P300 event-
related potential (ERP; Sellers et al., 2006; Zhang et al., 2008;
Guger et al., 2009; Townsend et al., 2010; Jin et al., 2012).
Despite some delightfully strident arguments within the
research community, there is no general agreement on which
approach is best. Instead, different BCIs are better suited to differ-
ent users, needs, environments, applications, and other parame-
ters. The main drawback of the P300 BCI is that users must pay
attention to speciﬁc events, usually ﬂashes on a monitor. Hence,
users must pace themselves according to the system, and may ﬁnd
the ﬂashes annoying. On the other hand, P300 BCIs seem to work
for nearly all healthy users,unlike (at least) ERD BCIs (Guger et al.,
2003, 2009; Allison and Neuper, 2010). P300 BCIs require almost
no training for the system or user, and have always been relatively
fast; the ﬁrst BCI to exceed 100 bits/min was a P300 BCI (Brunner
et al., 2011). Recent work has highlighted many new options for
improving the P300 BCI (e.g., Münßinger et al., 2010; Townsend
et al., 2010; Frye et al., 2011; Kaufmann et al., 2011; Jin et al.,
2012). Therefore, P300 BCIs should remain prominent for at least
the near future.
Most P300 BCIs allow users to choose one target from several
options, such as letters or numbers presented on a monitor (Far-
well and Donchin, 1988; Townsend et al., 2010; Brunner et al.,
2011). The user is asked to focus on one item, such as the letter
“G,” and count each time it ﬂashes while ignoring other events.
Next, different groups of letters brieﬂy ﬂash, in sequence, until the
system has presented a prespeciﬁed number of targets (Farwell and
Donchin, 1988) or accurate classiﬁcation is possible based on the
EEG data (Jin et al., 2012). Since counting each ﬂash produces a
brainwave called the P300, which is not elicited by ignored ﬂashes,
the system can identify the target letter by identifying which ﬂashes
elicited a P300. The system presents this letter to the user, and then
moves to the next target.
However, like most BCIs, P300 BCIs are hampered by the need
for conductive gel to get a good contact between each electrode
and the scalp. Preparing a subject for conventional EEG record-
ing requires abrading the skin under each electrode, positioning
each electrode over the abraded area, and squirting electrode gel
underneath each electrode. Getting a good contact between each
www.frontiersin.org
May 2012 | Volume 6 | Article 60 | 1

Guger et al.
Dry and gel based BCI
electrode and the scalp usually requires further skin abrasion and
application of gel. The gel is uncomfortable to many subjects, and
must be washed out of both the cap and hair later. This procedure
greatly increases the time and inconvenience needed for any EEG
recording session. Also, after a few hours of use, the gel may dry,
and new gel must be applied (Ko and Hynecek, 1974).
Theseproblemsreducetheappealof EEG-basedtechnologiesto
most users, and can be especially pronounced for severely disabled
users – even though these are the people who need BCIs most.
Some conditions can increase skin sensitivity, making the skin
abrasion process more painful. Since some of these patients cannot
communicate without a BCI,they may have no way to convey their
distress during preparation. Hence, working with gel-based elec-
trodes increases dependence on friends,family,or other caretakers.
Numerous recent articles that survey different end users have
further conﬁrmed that dry electrodes are a very high priority. Cas-
son et al. (2010) surveyed neurologists and found that almost 90%
agreed there is a clinical need for “wearable electrodes.” Huggins
et al. (2011) surveyed 61 ALS patients and found one of their main
concerns was “set-up simplicity.” Zickler et al. (2011) surveyed
severely disabled users and found that major issues included“pos-
sibility of independent use” and “easiness of use.” Blain-Moraes
et al. (2012) presented a focus group study with eight ALS patients
and nine carers. Two of their main concerns were a more con-
venient way to sense brain signals, and facilitating independence
for both users and carers. The future BNCI roadmap, an extensive
analytical effort developed through many established BCI stake-
holders through 2010 and 2011, identiﬁed“practical electrodes”as
one of the two disruptive technologies in BCI research.
Since dry electrodes can substantially simplify EEG recording,
and are identiﬁed as important across numerous surveys, there
should be a strong interest in them. Indeed,numerous articles over
many years have explored dry electrodes to record EEG and other
physiological signals (e.g., Roman, 1966; Richardson, 1967, 1968;
Ko and Hynecek, 1974; Taheri et al., 1994; Gevins et al., 1995).
However, early dry electrodes had various problems including
reducedsignalquality,robustnesstomovement,electricalartifacts,
cost, and comfort.
There are two general approaches to dry electrodes, each with
distinct problems (Portnoy et al., 1974; Tam and Webster, 1977;
Gargiulo et al., 2008; Volosyak et al., 2010). One approach uses
capacitive sensors, which do not require direct contact with the
scalp. For such systems, motion artifact has been an insurmount-
able problem so far. The second approach relies on penetrating
the ﬁrst layer of the skin, such as through micro-needles, bristle
sensors, or mechanical springs that press electrodes into the skin
(Taheri et al., 1994; Matteucci et al., 2007; Popescu et al., 2007;
Grozea et al., 2011). These systems may be uncomfortable. And,
with any dry electrode, a paramount concern is validating signal
quality for a speciﬁc application in real-world circumstances.
Recently, interest in dry electrodes has increased considerably.
A PubMed search on February 1, 2012 for “dry electrode EEG”
revealed 37 articles; only ﬁve were published before 2000, and
another ﬁve were published before 2007. An otherwise identi-
cal search that replaced “EEG” with “BCI” found six articles, all
published 2007 or later. Many companies are also producing dry
electrode systems. Most sales are simple toy systems that detect
drowsiness or fatigue with one electrode, unlike more complex
multi-electrode systems that detect conventional BCI signals such
as P300, SSVEP, and ERD.
Of the six journal publications that include “EEG” and “BCI,”
there seems to be a dearth of P300 BCI work. Carabalona et al.
(2009) focuses primarily on rehabilitation rather than dry elec-
trodes. Popescu et al. (2007) only addressed motor imagery BCIs.
Luo and Sullivan (2010) and Chi et al. (2011) only worked with
SSVEP. Grozea et al. (2011) did explore P300s, but used an audi-
tory paradigm, which is appealing to blind users but much less
common and effective than a visual P300 approach. The article
relied on only three electrodes: Cz and P1, referenced to Fz. This
montage is not optimal for a visual P300 approach, which better
works using components from parieto-occipital regions. Also, an
Fz reference electrode is much more vulnerable to blink artifact
than the more conventional mastoid or earlobe reference – and
P300 BCIs are more vulnerable to eyeblink artifact than other
BCIs. Although the article states that feedback was provided, it
never mentions whether or how it was presented with the P300
BCI. Zander et al. (2011) explored ERPs and alpha activity. The
ERPworkusedacompletelynoveldisplay,unlikeanyP300BCIyet.
Their dry electrode system used only three electrodes,all located in
a horizontal line. As with the Grozea et al. (2011) article, the addi-
tional spatial information available from a broader montage would
have improved performance (e.g., Krusienski et al., 2006, 2008).
Furthermore, Zander et al. (2011) was an ofﬂine study – subjects
did not receive feedback, and classiﬁcation accuracy was only esti-
matedfromofﬂinedata.Mostimportantly,theirstudyshowedthat
dry electrodes were statistically signiﬁcantly worse (lower classi-
ﬁcation accuracy) than gel-based alternatives. Their classiﬁcation
accuracy was about 6% worse with the dry electrode system.
In addition to these journal publications, some conference
papers have presented dry electrode systems. For example, our
2007 conference paper evaluated a dry electrode system in a gam-
ing context, and a later conference paper used the same company’s
system in a P300 copy-spelling task (Trejo et al., 2007; Sellers et al.,
2009). Both of these studies used relatively few subjects, did not
report comfort, have never been translated to a journal paper,
and reported poor performance. For example, the latter article
reported only about 70% accuracy with a P300 BCI copy-spelling
task using row–column ﬂashes with a 6 × 6 matrix.
All of these factors underscore the opportunity and need to
explore well-established P300 methods with dry electrodes. The
primary goal of this study was to assess a new dry electrode system
in an otherwise conventional P300 BCI. A total of 23 subjects used
a P300 BCI that was very much like other P300 BCIs in terms of
the display,task,paradigm,signal processing,and other details.We
present conventional analyses such as accuracy as well as subjective
report regarding the comfort of the dry electrode system.
MATERIALS AND METHODS
EXPERIMENTAL PROCEDURE
Twenty-three subjects (six female, age: 22–60) participated in the
study. All subjects were free of medication, had normal vision
or vision corrected to normal, and no history of central nervous
system abnormalities. All subjects provided informed consent
before participating in the study. The procedure complied with
Frontiers in Neuroscience | Neuroprosthetics
May 2012 | Volume 6 | Article 60 | 2

Guger et al.
Dry and gel based BCI
the ethical review procedures within the BrainAble project. Sub-
jects were prepared for recording with the dry electrode system,
using eight recording sites plus a reference and ground as shown in
Figure 1. Subjects were not seated in a shielded room, but an open
ofﬁce environment with periodic distractions, typical of a real-
world setting. The entire preparation procedure took less than
5 min.
Subjects sat in front of a laptop computer and were instructed
to relax and remain as still as possible. The laptop used the inten-
diX row/column (RC) speller shown in Figure 1 (g.tec medical
engineering GmbH, Austria). The RC speller presented 50 char-
acters (the 26 letters of the English alphabet, integers from 0 to 9,
and 14 special characters) on the laptop monitor. Subjects were
instructed to silently count each time a target character ﬂashed
while ignoring other ﬂashes. Subjects were ﬁrst asked to spell the
word “WATER” in an ofﬂine mode to help calibrate the system.
Hence, the ﬁrst target letter was “W.” At the beginning of each
trial, the target letter was highlighted for several seconds so the
subject could identify the target. After a 2-s delay, the system then
began ﬂashing a randomly selected column or row for 100 ms,
followed by a 60-ms delay before a different row or column is
highlighted. Each row and column was highlighted 15 times for
each letter. Therefore, there were 225 ﬂashes per trial, and 1125
ﬂashes for a ﬁve-letter word.
After each trial, the signal processing software extracted indi-
vidual ERPs from 100 ms before to 700 ms after each ﬂash. The
100-ms time segment before each ﬂash was used for baseline cor-
rection. While subjects spelled the word “WATER,” they did not
receive any feedback. Next, the system performed linear discrim-
inant analysis (LDA) based on these ERPs to create the weight
vector for the upcoming online trials.
Next, the subject was asked to spell the word “LUCAS” in the
same fashion as“WATER,”except that the system used the updated
classiﬁer and provided real-time feedback. Only the results of the
effort to spell “LUCAS” are reported in this paper. After each trial,
the intendiX system presented the target character on the top of the
monitor. The delay between the last row or column ﬂash and the
presentation of this feedback was less than 1 s. After the feedback
was presented, there was a delay of 2.15 s before the subject was
cued to the next target character, and the highlighting sequence
began again.
At the end of the recording procedure, some subjects chose to
continue using the system in “free spelling” mode, in which they
spelled text of their choosing. The data from these runs are not
presented here, but Figure 1B presents one example of a subject
spelling freely. When the subjects were done, the electrode system
was removed. Unlike typical EEG recording sessions, it was not
necessary to wash the subject’s hair nor the electrodes to remove
gel. Subjects completed a brief questionnaire before departing that
asked about the discomfort produced by the electrodes.
After this procedure was complete, one of the 23 subjects then
repeated the procedure using gel-based electrodes as described
below. This additional recording was performed so we could
present a direct, within-subject comparison of the raw EEG, ERPs,
and BCI performance resulting from dry vs. gel electrodes, shown
in Figures 3–5.
HARDWARE AND SOFTWARE
Figure 1 shows the electrode conﬁguration and the electrode
locations used for the studies. Figure 2 shows a close-up of the
dry electrodes. There are two versions of the dry electrodes, which
FIGURE 2 | A photograph of the Sahara dry electrodes used in this
study. The left electrode is designed for people with longer hair, and the
right electrode is designed for people with less or no hair. In this study, the
experimenter selected the electrode that was best for each subject. Other
testing (not reported here) showed that these two electrodes produced
equivalent signals.
FIGURE 1 | (A) Shows the intendiX spelling matrix at the beginning of a
“copy-spelling” run. The phrase “WATER” is presented at the top of the
screen. The “W” is highlighted, indicating that it is the target letter. (B)
Presents a photograph of a subject using the system in free spelling mode.
(C) Shows the electrode montage used with both the gel and dry electrodes.
The ground is on the left mastoid, and the reference is on the right mastoid.
www.frontiersin.org
May 2012 | Volume 6 | Article 60 | 3

Guger et al.
Dry and gel based BCI
differ in the length of the gold pins that contact the surface of the
head. When preparing the subject for recording, the experimenter
chose one of these electrodes based on the subject’s hair length
and head shape.
Electroencephalogram data were acquired using a g.USBamp
(24 Bit biosignal ampliﬁcation unit, g.tec medical engineering
GmbH, Austria) with a sampling frequency of 256 Hz. The data
werethenconvertedtodoubleprecision,bandpassﬁlteredbetween
0.5 and 30 Hz, and then down-sampled to 64 Hz. The ground
electrode was mounted over the left mastoid and the reference
was mounted over the right mastoid; for both positions dispos-
able pre-gelled electrode pads were used. EEG electrodes were
ﬁxed to an EEG electrode cap (g.GAMMAcap) according to the
extended international 10/20 electrode system. EEG recordings
based on gel electrodes were done with the g.BUTTERﬂy electrode
(golden ring electrode type with a hole in the middle to inject the
gel); EEG recordings based on dry electrodes instead used the
g.SAHARA electrode (eight gold-coated pins with 7 mm/16 mm
length mounted in a circular arrangement,diameter 15 mm). Both
types of electrodes are active EEG electrodes with a small pre-
ampliﬁer located in the electrode itself. Both types of electrodes
do not penetrate the epidermis. The tips of the electrode con-
tacts in the g.SAHARA system are smooth, not pointed, to avoid
discomfort.
RESULTS
Before presenting results with the P300 speller, we ﬁrst address
the a priori question of whether the raw data from the two elec-
trode types looked similar. Figure 3 presents 8 s of raw EEG data
recorded from one subject with both gel and dry electrodes. The
raw data look similar for both electrode types, including the noise
created by eyeblink artifacts and some high frequency activity.
FIGURE 3 | Eight-channel EEG data from the P300 experiment acquired
with dry and gel electrodes for one subject over frontal, central, parietal,
and occipital sites.The EOG artifacts are mostly visible on Fz, Cz, P3, Pz, and
P4 and look fairly similar for gel and dry electrodes. The y-axis is scaled with
±100 μV, and the x-axis presents seconds. The data are bandpass ﬁltered
between 0.1 and 30 Hz with a 50 Hz notch ﬁlter.
Frontiers in Neuroscience | Neuroprosthetics
May 2012 | Volume 6 | Article 60 | 4

Guger et al.
Dry and gel based BCI
The next question is whether the ERPs look similar across both
electrode types. Figure 3 shows the EP for dry and gel based elec-
trodes at electrode position Cz for the training and copy-spelling
run for one subject. The EP reaches its maximum of about 6 μV
after about 240 ms in both cases. The EP looks very similar for the
dry and gel based electrodes and the comparison of the training
and copy-spelling run shows that the EP is very stable over time.
P300 BCI PERFORMANCE
Table 1 summarizes the results of the current study. One col-
umn presents the results with dry electrodes, and another column
summarizes results from a large group study with gel electrodes
(N = 81; Guger et al., 2009). We conducted a t-test to compare
subjects’ performance with gel vs. dry electrodes. We used the 81
subjects from the 2009 study who completed the row–column task
and compared their accuracies to the 23 subjects from the present
study. The difference was not statistically signiﬁcant.
Table 1 clearly shows that the dry electrode system delivers
performance comparable to the gel based system. However, it
is important to establish whether other differences between the
two studies might have created a bias toward the present study.
Both studies used identical hardware from the same manufacturer,
except for the electrodes. Both studies used very similar software,
with no relevant differences in signal processing nor classiﬁer
updating. Both studies used the same sampling frequency, band-
pass ﬁlter, and downsampling. In both studies, subjects spelled
“WATER”to calibrate the system, then spelled“LUCAS”with feed-
back. In both studies, each row or column was highlighted for
100 ms, followed by a delay of 60 ms before the next ﬂash.
There is one noteworthy paradigmatic difference that affects
classiﬁcation accuracy. The 2009 study used a display with 36
characters. Hence, chance performance was one in 36, or about
2.8%. The present study instead had a vocabulary of 50 characters,
corresponding to 2% chance performance. Therefore, in the 2009
study, correct classiﬁcation due to chance was slightly more likely
than in the present study.
The present study ﬂashed each character 15 times, consistent
with canonical work (Farwell and Donchin, 1988). However, we
expect that the intendiX system could be practical with fewer
Table 1 |This table summarizes subjects’ accuracy for gel electrodes in
an earlier study (Guger et al., 2009) and dry electrodes in the present
study.
Row-column speller
classiﬁcation
accuracy in %
Gel electrodes (N = 81;
Guger et al., 2009)
Dry electrodes
(N = 23)
100
72.8
69.6
80–100
88.9
87.0
60–79
6.2
8.7
40–59
3.7
4.4
20–39
0.0
0
0–19
1.2
0
Average accuracy of
all subjects
91.0 ± 18.5
90.4 ± 17.2
N speciﬁes the number of subjects summarized in each column.
ﬂashes, and we want to facilitate comparison with other articles,
which often present accuracy across different numbers of ﬂashes
to explore the speed–accuracy tradeoff (e.g.,Farwell and Donchin,
1988; Townsend et al.,2010; Jin et al.,2012). Therefore,in addition
to these results based on 15 ﬂashes of each row and column, we
also present accuracy with fewer ﬂashes. Figure 5 presents accu-
racy across 1–15 different such ﬂashes. Figure 5 shows that the dry
electrodes compete well with the gel electrodes in this comparison
as well.
SUBJECTIVE REPORT
All 23 subjects were asked whether the dry electrode system was
uncomfortable in a short questionnaire. None of the subjects
reported any discomfort through these questionnaires, nor did
they complain in any other way. In the 2009 study none of the sub-
jects reported any discomfort from the g.BUTTERFLY electrodes
that were used.
Furthermore, g.tec hosts several workshops a year, in which
hundreds of people have used g.BUTTERFLY electrodes, and
dozens have used the g.SAHARA electrodes. None of these partic-
ipants have reported any discomfort with either electrode. Hence,
at least with the conditions used in this study and g.tec workshops,
both electrode types were not uncomfortable.
DISCUSSION
This is the ﬁrst journal publication to show that dry electrodes can
yield performance comparable to gel electrodes with a P300 BCI.
This is an important outcome, given the promise and prominence
of both dry electrodes and P300 BCIs. Subjects did not consider
the dry electrode system uncomfortable, and it required no gel
and reduced preparation time. Although the dry electrode system
might be more prone to movement artifact and ambient elec-
trostatic charges, these were not a problem in the present study.
Overall, the new system is generally comparable to or better than
gel electrodes in many ways.
This work is also important because it demonstrates that the
dry electrode system can function in a relatively unconstrained
ﬁeld setting. Dry electrodes typically entail much higher imped-
ance values than gel electrodes. This is the main reason why
gel is so common; the gel provides contact between the scalp
and each electrode that greatly reduces impedance. Otherwise,
high impedance will impair signal quality and increase vulner-
ability to electrical artifact, such as from external devices or
movement. The dry electrode system allows good performance
despite high impedances by using multiple gold-coated pins in
each electrode, as well as an integrated ampliﬁer within each
electrode.
Interestingly,although the dry electrode system resulted in EEG
data, ERPs, and BCI accuracy comparable to gel electrodes, there
were notable differences. The average peak P300 amplitude was
lower in the present study. The dry electrodes showed higher signal
drifts below 3 Hz than gel based electrodes. Neither of these differ-
ence had a notable effect on classiﬁcation accuracy. However,these
differences might be relevant for other types of BCIs. For example,
BCIs that rely on slow cortical potential changes (Birbaumer et al.,
1999) might be more sensitive to signal drift below 3 Hz.
Although this is a promising start, there are many issues that
still need to be explored. As noted, dry electrodes need to be
www.frontiersin.org
May 2012 | Volume 6 | Article 60 | 5

Guger et al.
Dry and gel based BCI
FIGURE 4 |The P300 complex recorded with dry and gel electrodes for one subject over site Cz. Each ﬁgure reﬂects averaged data across all target
ﬂashes for one ﬁve-letter word (150 ﬂashes). The y-axis is scaled with ±10 μV, and the x-axis in presented in seconds.
FIGURE 5 | P300 BCI accuracy based on 1–15 ﬂashes for dry vs. gel
electrodes for one subject.
explored with a much wider variety of BCI systems, with different
mental tasks, EEG signals, and other details. Comfort and other
subjective factors should be assessed in other circumstances, such
as with electrodes mounted in other headwear, tasks requiring
physical movement, and long-term use. All of the subjects in this
study, like all published dry electrode studies, were healthy. Dry
electrodes should be validated with persons with severe disabil-
ities, since they often need BCIs more than healthy users. With
some such users, special concerns (such as fasciculations that pro-
duce uncontrolled movement) might be especially problematic for
dry electrodes. We also recommend focusing on other compar-
isons between dry and gel electrodes. While accuracy and comfort
are very important, research should also parametrically compare
preparation time, reliance on outside support, and other factors.
These may be more difﬁcult to paradigmatically assess, but are
critical factors in BCI adoption (Allison, 2010; Casson et al., 2010;
Huggins et al., 2011; Zickler et al., 2011; Blain-Moraes et al., 2012)
and are worth the extra trouble.
ACKNOWLEDGMENTS
This work was funded by EC projects: CSI, ALIAS, Brainable,
Decoder, and Better.
REFERENCES
Allison, B. Z., and Neuper, C. (2010).
“Could anyone use a BCI?”in Apply-
ing our Minds to Human–Computer
Interaction, eds D. S. Tan and A.
Nijholt (London: Springer Verlag),
35–54.
Allison, B. Z. (2010). “Toward ubiq-
uitous BCIs,” in Brain–Computer
Interfaces: Revolutionizing Human–
Computer
Interaction,
eds
B.
Graimann, B. Z. Allison, and G.
Pfurtscheller
(Berlin:
Springer
Verlag), 357–387.
Allison, B. Z., Leeb, R., Brunner, C.,
Müller-Putz, G. R., Bauernfeind, G.,
Kelly, J. W., and Neuper, C. (2012).
Toward smarter BCIs: extending
BCIs through hybridization and
intelligent control. J. Neural Eng. 9,
013001.
Blain-Moraes, S., Schaff, R., Gruis,
K. L., Huggins, J. E., and Wren,
P.
A.
(2012).
Barriers
to
and
mediators
of
brain–computer
interface
user
acceptance:
focus
group
ﬁndings.
Ergonomics.
doi:10.1080/00140139.2012.661082.
Birbaumer, N., Ghanayim, N., Hinter-
berger, T., Iversen, I., Kotchoubey,
B., Kübler, A., Perelmouter, J., Taub,
E., and Flor, H. (1999). A spelling
device for the paralysed. Nature 398,
297–298.
Brunner, P., Ritaccio, A. L., Emrich,
J. F., Bischof, H., and Schalk, G.
(2011).
Rapid
communication
with
a
“P300”
Matrix
Speller
using
electrocorticographic
sig-
nals (ECoG). Front. Neurosci. 5:5.
doi:10.3389/fnins.2011.00005
Carabalona, R., Castiglioni, P., and Gra-
matica, F. (2009). Brain–computer
interfaces and neurorehabilitation.
Stud. Health Technol. Inform. 145,
160–176.
Casson, A., Yates, D., Smith, S., Dun-
can,
J.,
and
Rodriguez-Villegas,
Frontiers in Neuroscience | Neuroprosthetics
May 2012 | Volume 6 | Article 60 | 6

Guger et al.
Dry and gel based BCI
E.
(2010).
Wearable
electroen-
cephalography. What is it, why is it
needed,and what does it entail? IEEE
Eng. Med. Biol. Mag. 29, 44–56.
Chi, Y., Wang, Y., Wang, Y., Maier,
C., Jung, T., and Cauwenberghs, G.
(2011). Dry and noncontact EEG
sensors for mobile brain–computer
interfaces. IEEE Trans. Neural Syst.
Rehabil. Eng. 20, 228–235.
Farwell, L. A., and Donchin, E. (1988).
Talking off the top of your head.
Electroencephalogr. Clin. Neurophys-
iol. 70, 510–523.
Friman, O., Volosyak, I., and Gräser,
A. (2007). Multiple channel detec-
tion of steady-state visual evoked
potentials for brain–computer inter-
faces. IEEE Trans. Biomed. Eng. 54,
742–750.
Frye, G. E., Hauser, C. K., Townsend,
G.,
and
Sellers,
E.
W.
(2011).
Suppressing ﬂashes of items sur-
rounding targets during calibration
of a P300-based brain–computer
interface improves performance. J.
Neural Eng. 8, 025024.
Gargiulo, G., Bifulco, P., Calvo, R. A.,
Cesarelli, M., Jin, C., and van Schaik,
A. (2008). “A mobile EEG system
with dry electrodes,” in IEEE Bio-
medical Circuits and Systems Confer-
ence (2008), 273–276.
Gevins, A., Leong, H., Du, R., Smith, M.
E., Le, J., DuRousseau, D., Zhang, J.,
and Libove, J. (1995). Towards mea-
surement of brain function in oper-
ational environments. Biol. Psychol.
40, 169–186.
Grozea, C., Voinescu, C. D., and Fazli,
S. (2011). Bristle-sensors – low-cost
ﬂexible passive dry EEG electrodes
for neurofeedback and BCI applica-
tions. J. Neural Eng. 8, 025008.
Guger, C., Edlinger, G., Harkam, W.,
Niedermayer, I., and Pfurtscheller,
G. (2003). How many people are
able to operate an EEG-based brain–
computer interface? IEEE Trans.
Neural
Syst.
Rehabil.
Eng.
11,
145–147.
Guger,C.,Daban,S.,Sellers,E.,Holzner,
C., Krausz, G., Carabalona, R., Gra-
matica, F., and Edlinger, G. (2009).
How many people are able to con-
trol a P300-based brain–computer
interface (BCI)? Neurosci. Lett. 462,
94–98.
Huggins, J. E., Wren, P. A., and Gruis,
K. L. (2011). What would brain–
computer
interface
users
want?
Opinions and priorities of potential
users with amyotrophic lateral scle-
rosis. Amyotroph. Lateral Scler. 12,
318–324.
Jin, J., Allison, B. Z., Wang, X., and Neu-
per, C. (2012). A combined brain–
computer interface based on P300
potentials and motion-onset visual
evoked potentials. J. Neurosci. Meth-
ods 205, 265–276.
Kaufmann,
T.,
Schulz,
S.
M.,
Grünzinger, C., and
Kübler, A.
(2011). Flashing characters with
famous
faces
improves
ERP-
based
brain–computer
interface
performance.
J.
Neural
Eng.
8,
056016.
Ko, W. H., and Hynecek, J. (1974). “Dry
electrodes and electrode ampliﬁers,”
in Biomedical Electrode Technology,
eds H. A. Miller and D. C. Harri-
son (NewYork,NY:Academic Press),
169–181.
Krusienski, D., Sellers, E., Cabestaing,
F., Bayoudh, S., McFarland, D.,
Vaughan, T., and Wolpaw, J. R.
(2006). A comparison of classiﬁca-
tion techniques for the P300 Speller.
J. Neural Eng. 6, 299–305.
Krusienski, D. J., Sellers, E. W., McFar-
land, D. J.,Vaughan, T. M., and Wol-
paw, J. R. (2008). Toward enhanced
P300 speller performance. J. Neu-
rosci. Methods 167, 15–21.
Lin, Z., Zhang, C., Wu, W., and Gao, X.
(2007). Frequency recognition based
on canonical correlation analysis for
SSVEP-based BCIs. IEEE Trans. Bio-
med. Eng. 54, 1172–1176.
Luo, A., and Sullivan, T. J. (2010).
A user-friendly SSVEP-based brain–
computer interface using a time-
domain classiﬁer. J. Neural Eng. 7,
26010.
Matteucci, M., Carabalona, R., Casella,
M., Di Fabrizio, E., Gramatica, F., Di
Rienzo, M., Snidero, E., Gavioli, L.,
and Sancrotti, M. (2007). Micropat-
terned dry electrodes for brain–
computer interface. Microelectron.
Eng. 84, 1737–1740.
McFarland, D. J., Sarnacki, W. A.,
and Wolpaw, J. R. (2010). Elec-
troencephalographic (EEG) control
of three-dimensional movement. J.
Neural Eng. 7, 036007.
Münßinger, J. I., Halder, S., Kleih,
S. C., Furdea, A., Raco, V., Hösle,
A., and Kübler, A. (2010). Brain
painting: ﬁrst evaluation of a new
brain–computer interface applica-
tion with ALS-patients and healthy
volunteers. Front. Neurosci. 4:182.
doi:10.3389/fnins.2010.00182
Neuper, C., Scherer, R.,Wriessnegger, S.,
and Pfurtscheller, G. (2009). Motor
imagery and action observation:
modulation of sensorimotor brain
rhythms during mental control of
a brain–computer interface. Clin.
Neurophysiol. 120, 239–247.
Ortner, R., Allison, B. Z., Korisek,
G., Gaggl, H., and Pfurtscheller, G.
(2011). An SSVEP BCI to control
a hand orthosis for persons with
tetraplegia. IEEE Trans. Neural Syst.
Rehabil. Eng. 19, 1–5.
Pfurtscheller, G., Leeb, R., Keinrath, C.,
Friedman, D., Neuper, C., Guger, C.,
and Slater, M. (2006). Walking from
thought. Brain Res. 1071, 145–152.
Popescu, F., Fazli, S., Badower, Y.,
Blankertz, B., and Müller, K. R.
(2007). Single trial classiﬁcation of
motor imagination using 6 dry
EEG electrodes. PLoS ONE 2, e637.
doi:10.1371/journal.pone.0000637
Portnoy, W., David, R. M., and Akers,
L. A. (1974). “Insulated ECG elec-
trodes,”in Biomedical ElectrodeTech-
nology, eds H. A. Miller and D. C.
Harrison (New York, NY: Academic
Press).
Richardson, P. C. (1967). “The insu-
lated electrode:a pasteless ECG tech-
nique,” in Proceedings of the 20th
ACEMB, Vol. 9, 157.
Richardson, P. C. (1968). “The con-
struction techniques for insulated
electrocardiographic electrodes,” in
Proceedings of 21st ACEM, Vol. 10,
13A1.
Roman, J. (1966). Dry electrodes for
physiological monitoring. Tech. Note
U S Natl. Aeronaut. Space Adm. D-
3414, 1–32.
Sellers, E. W., Krusienski, D. J., McFar-
land, D. J.,Vaughan, T. M., and Wol-
paw, J. R. (2006). A P300 event-
related potential brain–computer
interface (BCI): the effects of matrix
size and inter stimulus interval
on performance. Biol. Psychol. 73,
242–252.
Sellers, E. W., Turner, P., Sarnacki,
W.,
McManus,
T., Vaughan,
T.
M., and Matthews, R. (2009). “A
novel
dry
electrode
for
brain–
computer interface,” in Human–
Computer Interaction: Novel Inter-
action Methods and Techniques, ed.
J. Jacko (Berlin: Springer Verlag),
623–631.
Taheri, B. A., Knight, R. T., and Smith,
R. L. (1994). A dry electrode for EEG
recording. Electroencephalogr. Clin.
Neurophysiol. 90, 376–383.
Tam, H. W., and Webster, J. G. (1977).
Minimizing electrode motion arti-
fact by skin abrasion. IEEE Trans.
Biomed. Eng. 24, 134–139.
Townsend, G., LaPallo, B. K., Boulay,
C. B., Krusienski, D. J., Frye, G.
E., Hauser, C. K., Schwartz, N.
E., Vaughan, T. M., Wolpaw, J.
R., and Sellers, E. W. (2010). A
novel P300-based brain–computer
interface stimulus presentation par-
adigm: moving beyond rows and
columns. Clin. Neurophysiol. 121,
1109–1120.
Trejo, L. J., McDonald, N. J., Matthews,
R.,
and
Allison,
B.
Z.
(2007).
“Experimental design and testing
of a multimodal cognitive overload
classiﬁer,” in Automated Cognition
International Conference, Baltimore,
MD.
Vidaurre, C., Sannelli, C., Müller, K.
R., and Blankertz, B. (2011). Co-
adaptive calibration to improve BCI
efﬁciency. J. Neural Eng. 8, 025009.
Volosyak, I., Valbuena, D., Malechka,
T., Peuscher, J., and Gräser, A.
(2010). Brain–computer interface
using
water-based
electrodes.
J.
Neural Eng. 7, 066007.
Wolpaw, J. R., Birbaumer, N., McFar-
land, D. J., Pfurtscheller, G., and
Vaughan, T.
M.
(2002).
Brain–
computer interfaces for communi-
cation and control. Clin. Neurophys-
iol. 113, 767–791.
Zander, T. O., Lehne, M., Ihme, K.,
Jatzev, S., Correia, J., Kothe, C.,
Picht, B., and Nijboer, F. (2011).
A dry EEG-system for scientiﬁc
research and brain–computer inter-
faces. Front. Neurosci. 5:53. doi:
10.3389/fnins.2011.00053
Zhang, H., Guan, C., and Wang, C.
(2008). Asynchronous P300-based
brain–computer interfaces: a com-
putational approach with statistical
models. IEEE Trans. Biomed. Eng. 55,
1754–1763.
Zickler, C., Riccio,A., Leotta, F., Hillian-
Tress, S., Halder, S., Holz, E., Staiger-
Sälzer, P., Hoogerwerf, E. J., Desideri,
L., Mattia, D., and Kübler, A. (2011).
A brain–computer interface as input
channel for a standard assistive tech-
nology software. Clin. EEG Neurosci.
42, 236–244.
Conﬂict of Interest Statement: The
Christoph Guger, Gunther Krausz, and
Guenter Edlinger are full-time employ-
ees of g.tec medical engineering GmbH,
Guger
Technologies
OG,
and
the
Christoph Guger and Guenter Edlinger
are its co-CEOs.
Received: 08 March 2012; paper pend-
ing published: 26 March 2012; accepted:
09 April 2012; published online: 07 May
2012.
Citation: Guger
C, Krausz
G, Alli-
son
BZ
and
Edlinger
G
(2012)
Comparison
of
dry
and
gel
based
electrodes
for
P300
brain–computer
interfaces. Front. Neurosci. 6:60. doi:
10.3389/fnins.2012.00060
This article was submitted to Frontiers in
Neuroprosthetics, a specialty of Frontiers
in Neuroscience.
Copyright © 2012 Guger, Krausz, Alli-
son and Edlinger. This is an open-access
article distributed under the terms of
the Creative Commons Attribution Non
Commercial License, which permits non-
commercial use, distribution, and repro-
duction in other forums, provided the
original authors and source are credited.
www.frontiersin.org
May 2012 | Volume 6 | Article 60 | 7
