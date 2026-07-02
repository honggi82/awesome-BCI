##### ORIGINAL RESEARCH ARTICLE

published: 07 July 2014

## NEUROENGINEERING doi:10.3389/fneng.2014.00019

# Brain-computer interface with somatosensory feedback improves functional recovery from severe hemiplegia due to chronic stroke

### Takashi Ono1, Keiichiro Shindo2, Kimiko Kawashima1, Naoki Ota1, Mari Ito2, Tetsuo Ota3, Masahiko Mukaino3, Toshiyuki Fujiwara2, Akio Kimura2, Meigen Liu2 and Junichi Ushiba1*

- 1 Department of Biosciences and Informatics, School of Fundamental Science and Technology, Graduate School of Keio University, Kanagawa, Japan
- 2 Department of Rehabilitation Medicine, Keio University School of Medicine, Tokyo, Japan
- 3 Department of Rehabilitation Medicine, Asahikawa Medical University Hospital, Asahikawa, Japan

Edited by: Aleksandra Vuckovic, University of Glasgow, UK

Reviewed by: Christoph Guger, University of Technology Graz, Austria Damien Coyle, University of Ulster, UK

*Correspondence: Junichi Ushiba, Department of Biosciences and Informatics, Faculty of Science and Technology, Keio University, Kanagawa, Japan e-mail: ushiba@bio.keio.ac.jp

Recent studies have shown that scalp electroencephalogram (EEG) based brain-computer interface (BCI) has a great potential for motor rehabilitation in stroke patients with severe hemiplegia. However, key elements in BCI architecture for functional recovery has yet to be clear. We in this study focused on the type of feedback to the patients, which is given contingently to their motor-related EEG in a BCI context. The efﬁcacy of visual and somatosensory feedbacks was compared by a two-group study with the chronic stroke patients who are suffering with severe motor hemiplegia. Twelve patients were asked an attempt of ﬁnger opening in the affected side repeatedly, and the event-related desynchronization (ERD) in EEG of alpha and beta rhythms was monitored over bilateral parietal regions. Six patients were received a simple visual feedback in which the hand open/grasp picture on screen was animated at eye level, following signiﬁcant ERD. Six patients were received a somatosensory feedback in which the motor-driven orthosis was triggered to extend the paralyzed ﬁngers from 90 to 50◦. All the participants received 1-h BCI treatment with 12–20 training days. After the training period, while no changes in clinical scores and electromyographic (EMG) activity were observed in visual feedback group after training, voluntary EMG activity was newly observed in the affected ﬁnger extensors in four cases and the clinical score of upper limb function in the affected side was also improved in three participants in somatosensory feedback group. Although the present study was conducted with a limited number of patients, these results imply that BCI training with somatosensory feedback could be more effective for rehabilitation than with visual feedback. This pilot trial positively encouraged further clinical BCI research using a controlled design.

Keywords: brain-computer interface rehabilitation, motor imagery, somatosensory feedback, visual feedback

### INTRODUCTION

Stroke leads to a rapid loss of brain function through a disturbance in the blood supply to the brain and usually causes hemiparesis. Data from an earlier study suggest that practicing or observing movements that are highly similar to normal movements helps to improve motor functions (Ertelt et al., 2007; Garrison et al., 2010; Arya et al., 2011). Experience-based plasticity mechanisms, that involve the relative re-weighing of synaptic inputs, are constantly shaping network organization and are more likely driven by the formation and elimination of dendritic spines (Johnston, 2004; Carmichael, 2006; Murphy and Corbett, 2009). Some animal studies suggest that such plasticity occurs at both the peri-lesion and remote areas (Nudo, 2006). The results of several randomized, controlled, trials have indicated that the intensive practice of important motor tasks, while constraining the non-paretic limb, can substantially improve upper limb function in individuals whose movements have been mildly impaired

by stroke (Grotta et al., 2004; Mark et al., 2006; Taub et al., 2006; Lin et al., 2010). In the case of moderate impairment, assisted voluntary movement with functional electrical stimulation through surface electrodes is effective in improving ﬁnger and wrist motor functions (Peckham et al., 1980; Kimberley et al., 2004).

Recently, electroencephalogram (EEG)-based brain-computer interface (BCI) has been regarded as a new rehabilitation technique for patients with severe impairment after stroke, who cannot use the other above-mentioned rehabilitation strategies owing to a lack of volitional muscle activity (Buch et al., 2008; Daly et al., 2009). Motor imagery is often used in EEGbased BCI, because it is deﬁned as the mental rehearsal of a motor act without overt movement (Alkadhi et al., 2005). BCI estimates the patients’ motor imagery from the amplitude of the arc-shaped waveform on an EEG, or a magnetoencephalogram recorded over the primary sensorimotor cortex (SM1) and translates it into feedback (e.g., visual guidance, electrical

stimulation of muscles, or motor-driven orthosis). Imagery, or an actual hand movement, activates the SM1 and rhythmic activity in the alpha and beta band over the hand region results in amplitude attenuation or event-related desynchronization (ERD). This enables movement observation or provides afferent feedback in the BCI, and such feedback is believed to help direct brain reorganization, resulting in some functional recovery from stroke hemiplegia (Daly and Wolpaw, 2008). The prolonged use of this BCI training induces plastic changes in the brain activity of patients with stroke (Rozelle and Budzynski, 1995; Buch et al., 2008) and clinical improvement of upper limb function (Prasad et al., 2009; Caria et al., 2011; Shindo et al., 2011; Ramos-Murguialday et al., 2013; Mukaino et al., 2014)

However, speciﬁcations of the BCI paradigm that are needed for functional recovery are as yet unknown. As Daly and Wolpaw speculated, neural plasticity will be guided in different ways depending on the feedback modality. Visual feedback of ongoing SM1 excitability trains patients to produce normal SM1 activity, whereas robotic assistance of paretic movement following SM1 excitation will produce sensory input that induces neural plasticity to restore more normal motor control. To date, different types of feedback have been separately tested in some research groups. Thus, the validation of feedback type and protocol standardization in a BCI rehabilitation context will be beneﬁcial for further research development.

In this paper we compared two different types of feedback (i.e., visual feedback and sensory feedback with robotic movement assistance) contingent to motor-related EEG in stroke patients with chronic hemiplegia with a view toward functional recovery, using the Stroke Impairment Assessment Set (SIAS) which is a known standard scoring test, consisting of 22 subcategories, and has high reliability. BCI settings, except feedback and the task design, were shared between the two paradigms in order to minimize the potential inﬂuences of factors such as training intensity, duration, and adaptation to the EEG classiﬁcation rules. Since such an experiment was ﬁrst designed as a pilot trial, the experiments were conducted as a group comparison study to minimize participants’ burden from an ethical point of view. We note here that data in this BCI paradigm (sensory feedback) was previously reported elsewhere as a preliminary case series study (Shindo et al., 2011). On the other hand, the goal of our study was to compare two different types of feedback. Thus, the same data was used for another research purpose in this article.

### METHODS

#### PARTICIPANTS

The study group consisted of 12 participants who had had a stroke (three with right and nine with left hemiplegia) and met the following inclusion criteria: (1) the ﬁrst episode was a subcortical stroke; (2) they had severe upper limb paralysis and a score ≤2 for ﬁnger movement on SIAS (see Appendix) (Chino et al., 1994), indicating very clumsy ﬁnger movement and absence of isolated individual ﬁnger movement; (3) they had no cognitive impairment; and (4) their chronic stroke injury occurred more than 13 weeks prior to the study to ensure that further neurological and clinical recovery were less likely (Nakayama et al., 1994; Jørgensen

et al., 1995; Duncan et al., 2000). Detailed clinical information of the 12 participants is shown in Table 1. Twelve participants had little or no detectable surface electromyogram (EMG) activity from the affected extensor digitorum communis (EDC) when they attempted to extend their ﬁngers. All participants provided written informed consent prior to participating in the study.

#### EXPERIMENTAL PARADIGM

The experimental protocol was conducted in accordance with the Helsinki Declaration and was approved by the ethical committee of Keio University. The experiment consisted of BCI training and brain activity assessment using EEG. The BCI training protocol was similar to that reported previously (Neuper et al., 2009). Participants were seated in a comfortable chair with their arms supported and relaxed on the armrests in pronation. A 15.4-inch computer monitor was placed about 60cm in front of their eyes. EEG signals were recorded using 10 Ag/AgCl disc electrodes (ϕ = 10mm) placed on both hemispheres (Figure 1A). The reference electrode was placed at the left auricle. The signals were ampliﬁed (g.USBamp; Guger Technologies, Graz, Austria) and digitized (sampling frequency, 256Hz). The surface EMG was recorded bilaterally from the EDC muscles (high-pass ﬁlter 5Hz; sampling rate 256Hz). Impedance of EMG electrodes was kept under 10kOhm.

EEG signals were processed using MATLAB (MathWorks Inc., USA). Firstly, all bipolar combinations were calculated from ﬁve electrodes over each hemisphere. Secondly, all EEG trials were visually controlled for artifacts and contaminated trials were discarded (Neuper et al., 2009). EEG spectra were estimated by fast Fourier transformation, using 1-s window lengths, 90% overlap, and a Hanning window. Feedback was generated on the ERD value calculated for predeﬁned participant-speciﬁc frequency

Table 1 | Patient characteristic and clinical evaluation.

Participant Age Lesion TFO SIAS Feedback (month)

- 1 41 Right putamen 4 1a Visual
- 2 84 Right caudate nucleus

4 1b Visual

- 3 63 Right corona radiate 7 1c Visual
- 4 52 Middle cerebral artery area

31 1a Visual

- 5 49 Right putamen 13 1a Visual
- 6 65 Right putamen 10 0 Visual
- 7 47 Right thalamus 23 1a Somatosensory
- 8 65 Right corona radiate 155 1a Somatosensory
- 9 65 Right corona radiate 25 1a Somatosensory
- 10 60 Right internal capsule

51 1a Somatosensory

- 11 54 Left putamen 23 1a Somatosensory
- 12 46 Left putamen 24 1b Somatosensory

TFO, time from onset.

|[Figure 1]<br><br>FIGURE 1 | (A) Electrode position (B) Visual feedback paradigm (C) Somatosensory feedback paradigm cited from Shindo et al. (2011), partially revised.|
|---|

bands (Pfurtscheller et al., 1997) using the following equation:

R(f) − A(f,t) R(f) × 100

ERD(f,t) =

where A(f,t) is the power spectrum of the EEG at frequency f at time t, with reference to the onset of the motor task (see BCI training below), and R(f) is the power spectrum of a 1-s epoch of the reference period (2–3s) in each trial. By using this deﬁnition, ERD was expressed as a positive number. The time-frequency map of each bipolar signal was calculated from a 1-s EEG window after every 125ms. This time-frequency data was used to select the most reactive frequency band and a bipolar montage. If an ERD was not observed at the beginning of BCI training, we used EEG power at a base frequency (9–12Hz) with a bipolar montage of C3a-C3, which was the best electrode scheme in general (Neuper et al., 2006). A three-factor [time (pre-, post-training), side (damaged, undamaged hemisphere), feedback type (visual, somatosensory)] analysis of variance (ANOVA) for the ERD.

#### BCI TRAINING SESSION

In this study, there were two feedback groups. Six participants performed BCI training with visual feedback and six participants performed BCI training with somatosensory feedback.

Visual feedback

The trial was initiated upon presentation of the word “Relax” on a monitor, and a countdown was presented at the bottom of the monitor to prepare participants to attempt extension of an affected ﬁnger. The word and countdown disappeared 5s later. Six

participants received a visual feedback stimulus from the EEG in the form of a picture of the affected hand on the monitor. The ERD value in response to the resulting action of the feedback was determined before training as follows: ﬁrstly, participants generally achieved an increase in sensorimotor rhythm during voluntary relaxation and an ERD while imagining maximal ﬁnger extension on the paralyzed side. Pictures of the hand with varying degrees of hand movement were then mapped according to ERD magnitude. We prepared 20 pictures depicting different hand positions, ranging from a full-hand grasp to a fully open hand. A hand opening in the picture was associated with increasing ERD (Figure 1B). Pictures of a hand closing were associated with decreasing ERD because the participants’ hands were normally positioned in a more grip-like posture during the passive state, caused by spasticity. The ERD was divided into 20 parts from 0 to 80%, and each part was assigned 1 hand picture. The hand picture on the screen then remained stable, and the participants were asked to relax for 5s. This 15-s trial was repeated for approximately 1h, and a total of 100 trials were performed. This training was conducted on 5 weekdays for 1 month. The experiment was discontinued for the day if the participant complained of exhaustion. Because some participants complained of exhaustion during multiple sessions, the training time was shortened; however, these participants were asked to perform at least 60 trials on that day.

Sensory feedback

The participants had to imagine the paretic hand opening or at rest for 5s according to the task cue. The height of the cursor reﬂected the accumulated value of the output of classiﬁcation of ERD performed every 30ms since the beginning of the task. Thus, the cursor ﬂuctuated around the baseline if diminution of ERD was not clearly seen. The cursor went down if the diminution of ERD was continuously observed. The gain of cursor movement was within approximately one-tenth of the vertical range of the monitor during the resting phase in the calibration experiment. From the 4th training day, when the cursor reached the lower half on the right edge of the monitor, the motor-driven orthosis was triggered to extend the paralyzed ﬁngers from 90 to 50◦ (Figure 1C). Each training run consisted of 10 trials, with 5 trials per class, presented in randomized order. Ten training runs were recorded per day, with a total of 100 trials.

Outcome assessment

Surface EMG activities of the affected EDC muscle and ERD were compared between the ﬁrst and last training days. The task was slightly modiﬁed from the BCI training paradigm in order to easily perform paretic ﬁnger movements. The cursor moved from the left to right over a period of 8s on the monitor, and the task cue was presented 5s after the cursor had appeared. Participants were instructed to perform “unaffected hand opening” or “affected hand opening” voluntarily for 3s. This training run consisted of 10 trials with 5 trials per class, alternately.

In assessing improvement of ﬁnger movement impairment, SIAS was used at pre- and post-BCI training. It consists of a scale from 0 to 5, with 0 indicating complete paralysis and 5 no paresis (see Appendix).

### RESULTS

#### NEUROPHYSIOLOGICAL CHANGES

ERD in most participants was detected over both the damaged and undamaged hemispheres, in alpha and/or beta frequency bands throughout the experiment. Figure 2 showed the ERD value before/after trainings in both hemispheres. Statistical evaluation of ERD values revealed signiﬁcant enhancement over both damaged and undamaged hemispheres after BCI training in participants in both feedback categories (ERD values were shown in Table 2). Three-Way ANOVA showed no signiﬁcant differences of side and feedback type, but it became signiﬁcantly greater over both hemispheres (p < 0.05). Figure 3 shows BCI performance. BCI performance increased in both feedback groups, while there was no signiﬁcant difference between feedback groups (p < 0.05; Two-Way ANOVA).

Figure 4 showed EMG activities of affected EDC before/after trainings. Four participants in the somatosensory feedback group, who had little or no muscle activity before training, showed EMG activity voluntarily, while no participants in the visual feedback group improved their EMG activity. These results indicated that participants in the sensory feedback group improved in ﬁnger function and/or voluntary EMG activity. Note here that the visual feedback group did not show any improvement even when they received a longer training period.

#### CLINICAL BEHAVIORAL CHANGES

Figure 5 showed scores of SIAS ﬁnger function test. While no participants in the visual feedback group showed improvement in their ﬁnger function, three participants in the sensory feedback group showed improvement in ﬁnger function. All participants felt that they could relax more easily, although no participants in the visual feedback group improved on any scores. In addition, participants in the somatosensory feedback group indicated that they became more aware of the use of their paretic upper extremity in daily activities.

### DISCUSSION

These results show that EEG-based BCI training with visual or sensory feedback enhanced ERD following attempted motor activity, but only sensory feedback improved motor function.

Though only a limited number of patients participated in the current study, the results of this preliminary study suggest that a randomized controlled trial to complement these results be completed in the future.

#### ERD AND FINGER FUNCTION

Participants in this study learned to increase ERD after training. In addition, BCI performance also increased in both groups. These results follow those of previous studies (Pfurtscheller and Neuper, 2001; Buch et al., 2008; Hwang et al., 2009; Broetz et al., 2010; Hashimoto et al., 2010; Shindo et al., 2011; Cincotti et al., 2012; Mukaino et al., 2014). However, in the visual feedback group, no functional improvement was seen in any participants. From these results, we can say that ERD may not be a direct correlate of functional recovery in ﬁnger movement. ERD likely reﬂects desynchronized neural assembly as a result of the interaction between the thalamic nuclei and cortical areas, that are controlled by the interplay among thalamic relay cells and reticulo-thalamic pathway cells (Steriade and Llinás, 1988; Lopes da Silva, 1991). Desynchronization that is not directly related to motor output is potentially learned by visual feedback BCI.

ERD may reﬂect SM1 excitability during the relevant motor task (Takemi et al., 2013), thus a proper sensory feedback which engages the participant in the task may facilitate motor reorganization. Moreover, since the nature of neural activity is non-linear, a supplemental neural excitation factor, i.e., timing-dependent cortical excitation by contingent somatosensory feedback to the motor cortex, may promote further excitation of the SM1, resulting in functional recovery. These possibilities could explain why only sensory feedback BCI had a tendency to promote functional recovery in stroke hemiplegia.

Table 2 | ERD values of each hemisphere (mean ± SD %).

Visual Somatosensory Before After Before After

Undamaged 12.1 ± 8.3 20.0 ± 9.2 15.9 ± 9.7 22.2 ± 11.1 Damaged 13.6 ± 10.4 27.9 ± 5.0 14.1 ± 9.0 26.3 ± 16.9

|[Figure 2]<br><br>FIGURE 2 | ERD evaluation over both primary sensorimotor areas. White bars represent ERD values before training and black bars represent the ERD values after training. Numbers on x axis represent participant numbers.|
|---|

|[Figure 3]<br><br>FIGURE 3 | BCI performance accuracy. White bars represent ERD values before training and black bars represent the ERD values after training. Numbers on x axis represent participant numbers.|
|---|

|[Figure 4]<br><br>FIGURE 4 | Comparison of EMG activity before and after BCI. The horizontal bars represent the period during which participants opened their paralyzed hands. The data from participant 7 to participant 12 are from Shindo et al. (2011). Permission from Foundation for Rehabilitation Information.|
|---|

#### TRAINING INTERVAL

Due to a limitation in hospital regulations, visual feedback training was done on 5 weekdays for 1 month and somatosensory

|[Figure 5]<br><br>FIGURE 5 | Stroke Impairment Assessment Set (SIAS) ﬁnger function scores.|
|---|

feedback training was done once or twice a week for a period of 4–7 months. Of course, the training schedule should be the same between groups, however the results and remarks remain valid, since even intensive (everyday) and longer (1 month) training with visual feedback BCI did not show functional recovery. This suggests that sensory feedback following a motor attempt may be essential for reorganization of motor function. Intensive bodily sensation of the paralyzed limb may also be helpful to regain body awareness (or ownership), which is needed for motor planning. Such a compound effect may make sensory feedback more advantageous that visual feedback BCI

### CONCLUSION

We performed ERD-regulated motor imagery training in a BCI framework in stroke patients who have chronic, severe, hemiplegia, and observed ERD enhancement. Sensory feedback rather than visual feedback of ERD tended to restore paretic ﬁnger movement. These results reveal the importance of peripheral bodily sensation contingent to voluntary excitation of the cortical motor system, which is a key in promoting behavioral improvement. This is a serial case study with clinical limitations. Although

the small number of participants, differences in training intervals and duration since stroke are limiting factors, these results provide interesting, positive, data which indicate that a further, large-scale, clinical trial be undertaken, which we expect would support these preliminary insights.

### FUNDING SOURCES

This study was partially supported by the Strategic Research Program for Brain Sciences (SRPBS) of the Ministry of Education, Culture, Sports, Science, and Technology, Japan.

### ACKNOWLEDGMENTS

This study resulted from “Brain Machine Interface Development” under the Strategic Research Program for Brain Sciences by the Ministry of Education, Culture, Sports, Science, and Technology of Japan.

### REFERENCES

Alkadhi, H., Brugger, P., Boendermaker, S. H., Crelier, G., Curt, A., HeppReymond, M.-C., et al. (2005). What disconnection tells about motor imagery: evidence from paraplegic patients. Cereb. Cortex 15, 131–140. doi: 10.1093/cercor/bhh116

Arya, K. N., Pandian, S., Verma, R., and Garg, R. K. (2011). Movement therapy induced neural reorganization and motor recovery in stroke: a review. J. Bodyw. Mov. Ther. 15, 528–537. doi: 10.1016/j.jbmt.2011.01.023

Broetz, D., Braun, C., Weber, C., Soekadar, S. R., Caria, A., and Birbaumer, N. (2010). Combination of brain-computer interface training and goal-directed physical therapy in chronic stroke: a case report. Neurorehabil. Neural Repair 24, 674–679. doi: 10.1177/1545968310368683

Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., et al. (2008). Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. doi: 10.1161/STROKEAHA.107.505313

Caria, A., Weber, C., Brötz, D., Ramos, A., Ticini, L. F., Gharabaghi, A., et al. (2011). Chronic stroke recovery after combined BCI training and physiotherapy: a case report. Psychophysiology 48, 578–582. doi: 10.1111/j.1469-8986.2010.01117.x Carmichael, S. T. (2006). Cellular and molecular mechanisms of neural repair after

stroke: making waves. Ann. Neurol. 59, 735–742. doi: 10.1002/ana.20845

Chino, N., Sonoda, S., Domen, K., Saitoh, E., and Kimura, A. (1994). Stroke Impairment Assessment Set (SIAS). A new evaluation instrument for stroke patients. Jpn. J. Rehabil. Med. 31, 119–125. doi: 10.2490/jjrm1963.31.119

Cincotti, F., Pichiorri, F., Aricò, P., Aloise, F., Leotta, F., de Vico Fallani, F., et al. (2012). EEG-based brain-computer interface to support post-stroke motor rehabilitation of the upper limb. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 4112–4115. doi: 10.1109/EMBC.2012.6346871

Daly, J. J., Cheng, R., Rogers, J., Litinas, K., Hrovat, K., and Dohring, M. (2009). Feasibility of a new application of noninvasive brain computer interface (BCI): a case study of training for recovery of volitional motor control after stroke. J. Neurol. Phys. Ther. 33, 203–211. doi: 10.1097/NPT.0b013e3181c1fc0b

Daly, J. J., and Wolpaw, J. R. (2008). Brain-computer interfaces in neurological rehabilitation. Lancet Neurol. 7, 1032–1043. doi: 10.1016/S1474-4422(08)70223-0

Duncan, P. W., Lai, S. M., and Keighley, J. (2000). Deﬁning post-stroke recovery: implications for design and interpretation of drug trials. Neuropharmacology 39, 835–841. doi: 10.1016/S0028-3908(00)00003-4

Ertelt, D., Small, S., Solodkin, A., Dettmers, C., McNamara, A., Binkofski, F., et al. (2007). Action observation has a positive impact on rehabilitation of motor deﬁcits after stroke. Neuroimage 36(Suppl. 2), T164–T173. doi: 10.1016/j.neuroimage.2007.03.043

Garrison, K. A., Winstein, C. J., and Aziz-Zadeh, L. (2010). The mirror neuron system: a neural substrate for methods in stroke rehabilitation. Neurorehabil. Neural Repair 24, 404–412. doi: 10.1177/1545968309354536

Grotta, J. C., Noser, E. A., Ro, T., Boake, C., Levin, H., Aronowski, J., et al. (2004). Constraint-induced movement therapy. Stroke J. Cereb. Circ. 35, 2699–2701. doi: 10.1161/01.STR.0000143320.64953.c4

Hashimoto, Y., Ushiba, J., Kimura, A., Liu, M., and Tomita, Y. (2010). Change in brain activity through virtual reality-based brain-machine communication in a chronic tetraplegic subject with muscular dystrophy. BMC Neurosci. 11:117. doi: 10.1186/1471-2202-11-117

Hwang, H.-J., Kwon, K., and Im, C.-H. (2009). Neurofeedback-based motor imagery training for brain-computer interface (BCI). J. Neurosci. Methods 179, 150–156. doi: 10.1016/j.jneumeth.2009.01.015

Johnston, M. V. (2004). Clinical disorders of brain plasticity. Brain Dev. 26, 73–80. doi: 10.1016/S0387-7604(03)00102-5

Jørgensen, H. S., Nakayama, H., Raaschou, H. O., Vive-Larsen, J., Støier, M., and Olsen, T. S. (1995). Outcome and time course of recovery in stroke. Part II: time course of recovery. The Copenhagen Stroke Study. Arch. Phys. Med. Rehabil. 76, 406–412.

Kimberley, T. J., Lewis, S. M., Auerbach, E. J., Dorsey, L. L., Lojovich, J. M., and Carey, J. R. (2004). Electrical stimulation driving functional improvements and cortical changes in subjects with stroke. Exp. Brain Res. 154, 450–460. doi: 10.1007/s00221-003-1695-y

Lin, K.-C., Chung, H.-Y., Wu, C.-Y., Liu, H.-L., Hsieh, Y.-W., Chen, I.-H., et al. (2010). Constraint-induced therapy versus control intervention in patients with stroke: a functional magnetic resonance imaging study. Am. J. Phys. Med. Rehabil. 89, 177–185. doi: 10.1097/PHM.0b013e3181cf1c78

Lopes da Silva, F. (1991). Neural mechanisms underlying brain waves: from neural membranes to networks. Electroencephalogr. Clin. Neurophysiol. 79, 81–93. Mark, V. W., Taub, E., and Morris, D. M. (2006). Neuroplasticity and constraintinduced movement therapy. Eur. Medicophys. 42, 269–284.

Mukaino, M., Ono, T., Shindo, K., Fujiwara, T., Ota, T., Kimura, A., et al. (2014). Efﬁcacy of brain-computer interface-driven neuromuscular electrical stimulation for chronic paresis after stroke. J. Rehabil. Med. 46, 378–382. doi: 10.2340/ 16501977-1785

Murphy, T. H., and Corbett, D. (2009). Plasticity during stroke recovery: from synapse to behaviour. Nat. Rev. Neurosci. 10, 861–872. doi: 10.1038/nrn2735 Nakayama, H., Jørgensen, H. S., Raaschou, H. O., and Olsen, T. S. (1994). Recovery of upper extremity function in stroke patients: the Copenhagen Stroke Study. Arch. Phys. Med. Rehabil. 75, 394–398.

Neuper, C., Scherer, R., Wriessnegger, S., and Pfurtscheller, G. (2009). Motor imagery and action observation: modulation of sensorimotor brain rhythms during mental control of a brain-computer interface. Clin. Neurophysiol. 120, 239–247. doi: 10.1016/j.clinph.2008.11.015

Neuper, C., Wörtz, M., and Pfurtscheller, G. (2006). ERD/ERS patterns reﬂecting sensorimotor activation and deactivation. Prog. Brain Res. 159, 211–222. doi: 10.1016/S0079-6123(06)59014-4

Nudo, R. J. (2006). Mechanisms for recovery of motor function following cortical damage. Curr. Opin. Neurobiol. 16, 638–644. doi: 10.1016/j.conb.2006.10.004 Peckham, P. H., Mortimer, J. T., and Marsolais, E. B. (1980). Controlled prehension and release in the C5 quadriplegic elicited by functional electrical stimulation of the paralyzed forearm musculature. Ann. Biomed. Eng. 8, 369–388.

Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct brain-computer communication. Proc. IEEE 89, 1123–1134. doi: 10.1109/5.939829

Pfurtscheller, G., Neuper, C., Flotzinger, D., and Pregenzer, M. (1997). EEGbased discrimination between imagination of right and left hand movement. Electroencephalogr. Clin. Neurophysiol. 103, 642–651.

Prasad, G., Herman, P., Coyle, D., McDonough, S., and Crosbie, J. (2009). “Using motor imagery based brain-computer interface for post-stroke rehabilitation,” in 4th International IEEE/EMBS Conference on Neural Engineering, 2009. NER’09 (Antalya), 258–262.

Ramos-Murguialday, A., Broetz, D., Rea, M., Läer, L., Yilmaz, O., Brasil, F. L., et al.

(2013). Brain-machine-interface in chronic stroke rehabilitation: a controlled study. Ann. Neurol. 74, 100–108. doi: 10.1002/ana.23879

Rozelle, G. R., and Budzynski, T. H. (1995). Neurotherapy for stroke rehabilitation: a single case study. Biofeedback Self-Regul. 20, 211–228.

Shindo, K., Kawashima, K., Ushiba, J., Ota, N., Ito, M., Ota, T., et al. (2011). Effects of neurofeedback training with an electroencephalogram-based braincomputer interface for hand paralysis in patients with chronic stroke: a preliminary case series study. J. Rehabil. Med. 43, 951–957. doi: 10.2340/16501977-0859

Steriade, M., and Llinás, R. R. (1988). The functional states of the thalamus and the associated neuronal interplay. Physiol. Rev. 68, 649–742.

Takemi, M., Masakado, Y., Liu, M., and Ushiba, J. (2013). Event-related desynchronization reﬂects down-regulation of intracortical inhibition in human primary motor cortex. J. Neurophysiol. 110, 1158–1166. doi: 10.1152/jn. 01092.2012

Taub, E., Uswatte, G., King, D. K., Morris, D., Crago, J. E., and Chatterjee, A. (2006). A placebo-controlled trial of constraint-induced movement therapy for upper extremity after stroke. Stroke 37, 1045–1049. doi: 10.1161/01.STR.0000206463.66461.97

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

07

Received: 06 March 2014; accepted: 12 June 2014; published online: July 2014. Citation: Ono T, Shindo K, Kawashima K, Ota N, Ito M, Ota T, Mukaino M, Fujiwara T, Kimura A, LiuM and Ushiba J (2014) Brain-computer interface with somatosensory feedback improves functional recovery from severe hemiplegia due to chronic stroke. Front. Neuroeng. 7:19. doi: 10.3389/fneng.2014.00019

This article was submitted to the journal Frontiers in Neuroengineering. Copyright © 2014 Ono, Shindo, Kawashima, Ota, Ito, Ota, Mukaino, Fujiwara, Kimura, Liu and Ushiba. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

### APPENDIX

STROKE IMPAIRMENT ASSESSMENT SET (SIAS)

Motor Function (Finger)

Finger test: Individual ﬁnger movements are tested. The patient ﬂexes each digit from the thumb to the little ﬁnger, in that order, and then extends them from the little ﬁnger to the thumb.

- 0: No voluntary ﬁnger movement
- 1a: Minimal voluntary movement or mass ﬂexion

- 1b: Mass extension
- 1c: Minimal individual movement

- 2: Individual movement of each ﬁnger is possible, but ﬂexion or extension is not complete
- 3: Individual movement of each ﬁnger is possible with adequate ﬂexion and extension of the digits; however, the patient carries out the task with severe or moderate clumsiness
- 4: The patient carries out the task with mild clumsiness
- 5: The patient carries out the task as smoothly as for the unaffected side

