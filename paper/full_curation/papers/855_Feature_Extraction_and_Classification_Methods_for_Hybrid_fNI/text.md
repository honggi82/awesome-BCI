REVIEW published: 28 June 2018 doi: 10.3389/fnhum.2018.00246

# Feature Extraction and Classiﬁcation Methods for Hybrid fNIRS-EEG Brain-Computer Interfaces

Keum-Shik Hong1,2*, M. Jawad Khan2 and Melissa J. Hong3

1 Department of Cogno-Mechatronics Engineering, Pusan National University, Busan, South Korea, 2 School of Mechanical Engineering, Pusan National University, Busan, South Korea, 3 Early Learning, FIRST 5 Santa Clara County, San Jose, CA, United States

In this study, a brain-computer interface (BCI) framework for hybrid functional near-infrared spectroscopy (fNIRS) and electroencephalography (EEG) for locked-in syndrome (LIS) patients is investigated. Brain tasks, channel selection methods, and feature extraction and classiﬁcation algorithms available in the literature are reviewed. First, we categorize various types of patients with cognitive and motor impairments to assess the suitability of BCI for each of them. The prefrontal cortex is identiﬁed as a suitable brain region for imaging. Second, the brain activity that contributes to the generation of hemodynamic signals is reviewed. Mental arithmetic and word formation tasks are found to be suitable for use with LIS patients. Third, since a speciﬁc targeted brain region is needed for BCI, methods for determining the region of interest are reviewed. The combination of a bundled-optode conﬁguration and threshold-integrated vector phase analysis turns out to be a promising solution. Fourth, the usable fNIRS features and EEG features are reviewed. For hybrid BCI, a combination of the signal peak and mean fNIRS signals and the highest band powers of EEG signals is promising. For classiﬁcation, linear discriminant analysis has been most widely used. However, further research on vector phase analysis as a classiﬁer for multiple commands is desirable. Overall, proper brain region identiﬁcation and proper selection of features will improve classiﬁcation accuracy. In conclusion, ﬁve future research issues are identiﬁed, and a new BCI scheme, including brain therapy for LIS patients and using the framework of hybrid fNIRS-EEG BCI, is provided.

Edited by:

Srikantan S. Nagarajan, University of California, San Francisco,

United States Reviewed by:

Noman Naseer, Air University, Pakistan

Rifai Chai, University of Technology Sydney, Australia

*Correspondence:

Keum-Shik Hong kshong@pusan.ac.kr

Keywords: brain-computer interface, electroencephalography, functional near-infrared spectroscopy, locked-in syndrome patient, feature extraction, classiﬁcation

Received: 10 February 2018 Accepted: 29 May 2018 Published: 28 June 2018

## INTRODUCTION

The primary function of a brain-computer interface (BCI) is to provide a means of communication for patients with the real world. A large proportion of the patients targeted for BCI applications are those who cannot control their muscle movements voluntarily, particularly the patients deﬁned as “locked-in.” However, most current BCI research involves movement controlling devices with brain signals from healthy subjects. Patients with movement disorders may not be able to generate commands as eﬀectively as healthy subjects, hence they may not be able to control these devices with high accuracy (McFarland and Wolpaw, 2010, 2011; Pan et al., 2014; Visani et al., 2015).

Citation: Hong K-S, Khan MJ and Hong MJ (2018) Feature Extraction and Classiﬁcation Methods for Hybrid fNIRS-EEG Brain-Computer Interfaces.

Front. Hum. Neurosci. 12:246. doi: 10.3389/fnhum.2018.00246

Locked-in patients can use only cognitive functions, such as mental counting, listening, and imagination. In this paper, a new framework for hybrid feature extraction and classiﬁcation for patients in the locked-in state is proposed by which they may be able to achieve smooth control of external devices such as a robotic arm or wheelchair in a real-world environment (Muller-Putz et al., 2015; Naseer and Hong, 2015a).

To ﬁnd a solution for this problem, we ﬁrst need to understand the components of a BCI (Banville and Falk, 2016; Ramadan and Vasilakos, 2017) that can be modiﬁed to achieve better solutions. The brain signals for a BCI are usually acquired either directly from the electrical activity of the brain or from the secondary route known as hemodynamics. Electroencephalography (EEG) signals reﬂect electrical activity originating as a result of neuronal ﬁring when a task or activity is performed (Olejniczak, 2006). This activity is measured as diﬀerences in voltage between diﬀerent locations on the surface of the head. The diﬀerences are caused by postsynaptic potentials in the cell membranes of cortical neurons. On the other hand, hemodynamic activity appears in the form of blood ﬂow changes that result from neuronal ﬁring, which can be measured by functional nearinfrared spectroscopy (fNIRS) (Matthews et al., 2008; Min et al., 2010). Blood ﬂow increases in an area of activated neurons at a greater rate than in areas of inactive neurons. The increased blood ﬂow results in a surplus of oxyhemoglobin in the veins of the active area and a distinguishable change in the local ratio of oxyhemoglobin to deoxyhemoglobin. In the current literature, EEG and fNIRS are the only two modalities used for non-invasive BCI for locked-in patients (Hong and Khan, 2017).

As a modality for BCI, EEG is the most common method of recording neuronal signals, due to its portability. The signals most frequently used for BCI derive from motor imagery (MI), steady-state visual evoked potentials (SSVEP), and the P300 evoked potential (Trejo et al., 2006; Turnip et al., 2011; Turnip and Hong, 2012; Wang et al., 2012, 2016; Gruzelier, 2014; Ahn and Jun, 2015). These three signals have been used for controlling wheelchairs (Wang et al., 2014; Ramli et al., 2015; Zhang et al., 2016) and quadcopters (Kim et al., 2014). In addition to EEG, fNIRS is another widely used modality for BCI. Recent studies have shown the portability of fNIRS, thus making it a viable option (Santosa et al., 2013; Bhutta et al., 2014; Boas et al., 2014; Hong et al., 2015). Even though no study has yet shown the ability to control a wheelchair using fNIRS alone, several projects have used fNIRS to generate multiple commands (Power et al., 2012a; Naseer and Hong, 2013; Naseer et al., 2014). In some studies, EEG and fNIRS have been combined to improve classiﬁcation accuracy (Fazli et al., 2012; Safaie et al., 2013; Tomita et al., 2014; Buccino et al., 2016). For locked-in patients, several projects have used hybrid systems of this type to decode brain activity for control and brain imaging (Blokland et al., 2014; Dutta et al., 2015; Das et al., 2016). However, there is still a large gap between the currently achievable performance and the accuracy needed for a practically usable interface for locked-in patients. Taking into account both non-invasiveness and portability, currently fNIRS and EEG form the best available combination of modalities for BCI. Methods of command generation methods using these modalities are the focus of this review.

The ﬁrst issue to consider is selection methods for monitoring the best brain regions of interest. Most BCI studies use the international 10–20 (or 10–10) system for placement of EEG electrodes (Homan et al., 1987; Jurcak et al., 2007). Because EEG responses such as the P300 are highly variable across brain areas, channel selection algorithms are applied to determine a region of interest (ROI) (Feess et al., 2013; Alotaiby et al., 2015). In fNIRS, channel averaging is used because the hemodynamic responses are not distinctive among channels (Bhutta et al., 2015; Naseer and Hong, 2015b; Liu and Hong, 2017). These methods may be eﬀective for able-bodied persons, but not necessarily for lockedin patients, since their brain activity patterns may not be correctly identiﬁed. Smith and Delargy (2005) found that the cerebral cortex of a locked-in patient might not show clear evidence of activation. Therefore, it is desirable to improve brain region selection methods.

Next, selection of the best type of brain activity to use for generating control commands can be an issue. A healthy person can perform a wide variety of tasks easily. Thus, an able-bodied person usually has a better understanding of the experimental paradigm and the activities that are to be performed. Many EEG-based wheelchair control examples are available in the literature, but of 35 recent studies on wheelchair control using EEG (Fernández-Rodríguez et al., 2016), no study investigated a locked-in patient. As most of these studies employed SSVEPand P300-based schemes, the participants could adapt themselves to the scheme quickly (Hwang et al., 2012, 2013; Li et al., 2013a; Fan et al., 2015). However, for a locked-in patient, it is diﬃcult to concentrate on a screen to receive stimuli and generate commands. Therefore, a second aspect to consider is the type of BCI: active, reactive, or passive. The majority of BCIs have been designed using reactive tasks (Zander and Kothe, 2011). In these cases, the stimuli are given in the form of an audio, video or pain cue (Hu et al., 2012; Zhang et al., 2013, 2014; Hong and Nguyen, 2014; Santosa et al., 2014). These result in high accuracies when used with normal, healthy subjects. Again, however, it can be diﬃcult for a patient to concentrate on such stimuli. An active-type BCI may be more eﬀective for these patients. For example, a Yes/No decoding scheme has been successfully implemented for patients using a noninvasive active BCI (Chaudhary et al., 2017). Another point to consider is the number of distinct commands the patients can perform.

The third issue is how to convert the detected brain signals into machine commands. Identiﬁable features contained in brain signals need to be deﬁned, extracted, and classiﬁed to translate the analog brain signals into digital commands (Ortiz-Rosario and Adeli, 2013). Because diﬀerent types of brain activity patterns can be decoded from locked-in patients, the feature selection and classiﬁcation criteria developed for healthy people may need to be reevaluated. It is not clear yet whether the same feature sets used for healthy persons will work for patients (Naseer et al., 2016a). However, if proper features are selected, conventional classiﬁers (e.g., Bayesian, linear discriminant analysis) may complete the job. Moreover, to achieve fault-tolerance, it would be better to use both neuronal and hemodynamic features simultaneously (Hong and Khan, 2017).

Figure 1 depicts a typical BCI scheme, including signal acquisition, ﬁltering, feature extraction, classiﬁcation, and interfacing to external devices. After classiﬁcation, a control interface completes the system. An average classiﬁcation accuracy of at least 70% is essential for practical use. Most experiments conducted in a laboratory environment using able-bodied subjects could achieve accuracies higher than this. However, the accuracy drops drastically in the case of patients. If the necessary accuracy is not achieved in the early stages, physical stimulation of the brain may be useful. To improve the results for patients (e.g., stroke patients), additional measures using repetitive transcranial magnetic stimulation (rTMS) or transcranial direct current stimulation (tDCS) to improve brain functions may be needed (Dutta, 2015; Dutta et al., 2015). In general, the classiﬁcation accuracy and the number of distinguishable commands can be improved by i) combining signals from a nonbrain signal acquisition modality (e.g., a camera) with those from a brain signal acquisition modality, ii) developing a predictive model for early detection of a brain signal from a slow modality (e.g., fNIRS) in combination with a fast modality (e.g., EEG), and iii) identifying multiple cognitive activities simultaneously by integrating neuronal and hemodynamic signals.

In this review, we discuss the feasibility of hemodynamic and hybrid methods that can provide better results for achieving a high accuracy for BCI. In section What Patients Should BCI Focus?, the types of locked-in patients are categorized to clarify the brain regions that can most usefully be targeted in lockedin patients. In section Brain Activity Selection, channel selection schemes for brain region identiﬁcation that can be used for these patients are reviewed. In section Methods to Determine the Region of Interest, the types of brain activities that can be used by locked-in patients for control are discussed. In section Feature Extraction and Classiﬁcation Criteria, features that may provide more compatibility for command generation are examined. Moreover, classiﬁcation techniques are examined. Section Device Interfaces discusses external device interface techniques. Finally, in section What Future Direction to Adopt?, our own scheme for BCI (for, e.g., multiple choice selection or wheelchair control) is proposed, and the challenges involved in implementation of the scheme are discussed. In this review, the primary foci are fNIRS-based BCI and hybrid fNIRS-EEGbased BCI, because several reviews of EEG-based BCI, including brain region selection and feature extraction, are available in the literature. However, EEG-based schemes are brieﬂy explained where necessary.

## WHAT PATIENTS SHOULD BCI FOCUS?

Patients can be categorized based on their conscious state, attentional state, executive functions, intellectual ability, perception, and visual and verbal memories. However, the two aspects most commonly used to categorize patients are motor state and cognitive state (Guger et al, 2017). In general, BCI is well suited for patients who have limited motor activity but good cognitive skills. BCI may not be as eﬀective for those in impaired cognitive states, as they may not be able to

understand or perform the mental tasks used for controlling a device. Table 1 shows a classiﬁcation of patients based on motor and cognitive states. By examining the table, we can see that BCI is probably suitable for patients with locked-in syndrome (LIS) and completely LIS (CLIS). Studies have shown that patients with LIS sometimes progress to the CLIS state. BCI research should target these patients. According to Nicolas-Alonso and Gomez-Gil (2012), a high grade of disability among LIS patients forces them to use BCI rather than relying on conventional interfaces. In any case, the ﬁrst step is to determine the type of patients for whom a BCI is essentially needed.

The study of Kennedy and Adams (2003) categorized patients into six types. Four out of the six types showed detectable brain activity: Type (i) patients are capable of movement; type (ii) patients are incapable of movement but show some detectable motor activity due to partial muscle movements; type (iii) are locked-in patients with no muscular activity signals but with detectable eye-movement; and type (iv) are completely locked-in patients. The remaining two types are not suitable for non-invasive BCI. The ﬁfth type is patients in whom implanted electrodes can detect brain signals (even though EEG electrodes cannot), and the sixth type includes those whose brain activity is non-detectable. Since our focus is on BCI using noninvasive methods, we will discuss only the ﬁrst four types of patients.

Patients Capable of Movements

These patients are probably not suitable for BCI, because at least some of their motor functions are still intact. The brain states of these patients are working properly (Kawase et al., 2017). For those who cannot move their lower limbs, they can generate commands by conventional methods (e.g., pressing a button/switch) using their ﬁngers to control a wheelchair.

Patients With Minor Muscular Movements

These patients may not have visible motor movements. However, some muscular movements (e.g., minor shoulder ﬂexion/extension) are detectable. In these patients, the motor cortex is working properly, and the minor muscular movements are caused by signals sent from the brain to the muscles (de Oliveira et al., 2017). Most commonly, such movements are detectable by electromyography (EMG), which can be used for control purposes. Thus, with an appropriate interface, these patients are capable of controlling devices with partial muscular movements. In this case, generation of a suﬃcient number of commands to handle the required number of degrees of freedom is essential (e.g., for control of a wheelchair). Hybridization (e.g., EEG or EMG in addition to EMG) can be used to increase the number of commands available.

Patients With Minor Eye Movements

These patients may not be able to control most of their motor functions, but can perform very minor but detectable eye movements. In this case, the motor cortex is partially working (Käthner et al., 2015). The level of eye movement is an important factor. If the eye movement is signiﬁcant, electrooculography

|[Figure 1]<br><br>FIGURE 1 | Typical brain-computer interface scheme for control applications with brain function recovery.|
|---|

TABLE 1 | Categories of patients based on motor and cognitive states (Guger et al, 2017).

Cognitive state No cognition Minor

Major cognition Normal

cognition

Motor state

No response

Comma patient

Completely locked-in syndrome patient (CLIS)

Minimal conscious disorder (MCD)

Unresponsive wakeful state (UWS)

Minor motor response

Locked-in syndrome patient (LIS)

Motor impairment patient (MI)

Major motor response

Normal Cognitive impairment patient (CI)

BCI can be pursued for patients in the shaded area.

(EOG) can be used to generate commands based on eyemovements. However, it may be diﬃcult for these patients to concentrate on eye movements over long periods of time. Moreover, control of a wheelchair using eye movements may not be an eﬀective strategy, because it interferes with the ability of the subject to watch the environment. For these patients, the use of a hybrid scheme will be a better option. If multiple commands are needed, EOG can be combined with EEG to increase the number of commands. Furthermore, SSVEP- and P300-based stimuli can be used to generate multiple commands and to control external devices. It would be desirable to generate commands using reactive visual stimuli, and using EOG for improved control.

Fully-Locked in Patients

These patients cannot perform any type of motor activity. Any patient below this condition is in the vegetative state (VS). In

these case, the motor cortex in the brain is not working, but these patients can perform cognitive functions (Kübler et al., 2001, 2005). A BCI is the most eﬀective solution for such patients. The prefrontal cortex may be the best option for generating commands. It may be diﬃcult for these patients to control a wheelchair, but “Yes/No” decoding based on a choice selection can be performed. Moreover, to achieve better results, a hybrid EEG-fNIRS interface may be best, as it gives the richest signals.

Figure 2 shows a categorization of patients based on the types of movements and the types of mental tasks that may be useful to generate commands for control applications. Based on the discussion above, it is emphasized again that a BCI is suitable for patients who have lost motor functions.

## BRAIN ACTIVITY SELECTION

The brain signals suitable for use with LIS patients have been discussed in several papers (Nicolas-Alonso and Gomez-Gil, 2012; Moghimi et al., 2013). However, only general mental and motor tasks were discussed, and the focus was on neuronal signals (EEG-based). As discussed in section What Patients Should BCI Focus?, signals generated from the prefrontal cortex may be the best choice for LIS patients. For partially lockedin patients, motor cortex activity can be considered as well, since the total number of cognitive functions that can be used for BCI purposes may be limited. The study by Weyand et al. (2015a) found that eleven diﬀerent patterns of activity could be decoded from the prefrontal cortex. Therefore, focusing on the hemodynamic response, the following types of brain activity may be eﬀective for partially and completely locked-in patients:

Prefrontal Activity

Prefrontal cortex signals are the cognitive activity patterns that are most suitable for LIS patients, as no motor task is involved. These signals may be generated by simple calculation or imagination tasks, and can be used in an fNIRS-based BCI.

|[Figure 2]<br><br>FIGURE 2 | An illustration for BCI domain: BCI is required if there is no detectable muscular movement (BCI, brain-computer interface; LIS, locked-in syndrome; UWS, unresponsive wakeful state; MCD, minimal conscious disorder; MI, motor impairment; CI, cognitive impairment).|
|---|

As discussed earlier, the study by Weyand et al. (2015a) provided the list of eleven activity patterns that can be detected from the prefrontal cortex. In a later study, a total of thirteen tasks are shown to be distinguishable in the prefrontal cortex using fNIRS (Naito et al., 2007; Naseer and Hong, 2015a). They are brieﬂy discussed as follows.

region of the brain, mental counting task takes on a diﬀerent form/feature in the prefrontal cortex. In the case of mental counting, a patient is asked to count numbers backward from a three-digit number for a given duration slowly while relaxing. In comparison to mental arithmetic, mental counting is an easier task for patients (Naseer and Hong, 2015b).

Mental Arithmetic

This task uses a simple mathematical calculation to generate the brain activity. Usually, a two-digit number is required to be subtracted from a three-digit number. This may be the most eﬀective prefrontal active task; many studies have reported its eﬃcacy for generating a command. One study reported that such brain activity could be made more prominent by increasing the complexity of the mathematical problem (Verner et al., 2013). The use of this task has been reported in both an fNIRS-based BCI (Bauernfeind et al., 2008; Power et al., 2012b) and a hybrid EEG-fNIRS-based BCI (Khan et al., 2014; Khan and Hong, 2017).

Mental Counting

This is another mathematical task, similar to the mental arithmetic task above. Although both appear in the same

Mental Singing

The mental singing task involves imagining oneself singing a song. Not many studies have used this type of task for research. As per the literature, the resulting activity appears in the prefrontal brain region (Power et al., 2010, 2011).

Word Formation

The activity-generation method for this task has been described in three diﬀerent ways. One approach is to give a speciﬁc letter to the subject (e.g., “d”) and ask them to form words (e.g., “door,” “deer,” “desk” using “d”) (Faress and Chau, 2013). The second approach is to give a scrambled 6–7 letter word (e.g., “tocekr”) and ask the subject to form the correct word (“rocket” in this example) (Khan and Hong, 2017). The third is to ask the subjects

to recognize a letter displayed on a screen (Hofmann et al., 2008). The third method has shown promising results with patients.

Puzzle Solving

For this, a screen is required to give a stimulus. A tangram puzzle is shown on the screen and the subjects are asked to imagine a puzzle solution by rotating the pieces. A few studies have reported signiﬁcant results using this puzzle-solving paradigm (Zafar and Hong, 2017).

Mental Rotation

Similar to mental counting, mental rotation is a type of puzzlesolving task. In this case, an object is shown on a screen, and the subjects are asked to imagine the rotation of the object (Abibullaev and An, 2012; Qureshi et al., 2017). To some patients, this might be an easy task to perform.

Happy Thoughts

This may not be a very eﬀective task, as only two studies have reported using it to drive prefrontal activity (Tai and Chau, 2009). The brain activity is detected when one imagines a past happy event. It may be a possible option for LIS patients, but further research is required.

Stroop Test

For this case, the participants are shown a series of color names. The color names are each written in a single color, but the colors named by the words do not always match the colors they are written in. For example, the word “green” may be written in blue. The participants asked to think about the name of the color that the word is written in. This task has been used in a few fNIRS studies (Schroeter et al., 2002; Ehlis et al., 2005).

Future Visualization

The subjects are asked to imagine their life after 5 years, speciﬁcally focusing on day-to-day activities. There is a lack of evidence on the suitability of this task for use with patients. Further research is required (Buckner et al., 2008).

Focus

Usually, in this type of task, the subject is asked to focus on a screen. Most commonly, the subjects are asked to scrutinize signals appearing on the screen, which could be brain signals or pictures of a ball moving on the screen. This may be not an eﬀective task, as it is diﬃcult for LIS patients to focus on a screen (Izzetoglu et al., 2011).

Motor Imagery in the Prefrontal Cortex

Motor imagery is a motor function-related activity that can be deﬁned as imagination of a movement of a part of one’s own body, without any actual movement. According to the current literature, an activity related to motor imagery appears in the premotor cortex region (Holper and Wolf, 2011; Stangl et al., 2013; Kaiser et al., 2014). Some studies also indicate that it appears in the prefrontal cortex (Hatakenaka et al., 2007; Leﬀ et al., 2011; Weyand et al., 2015a). Although a healthy person can perform motor imagery, it is often diﬃcult for a disabled person to do so. Since the primary objective of a BCI is to form a communication

pathway for motor-disabled people, it is a problem that only limited numbers of patients can perform this task. Both EEG and fNIRS are good options for detection motor imagery. For patients with tetraplegia, a hybrid EEG-fNIRS scheme is the best option for detection of motor imagery (Blokland et al., 2014).

Picture Imagery

Like musical imagery, the brain activity is generated by imagining a picture. This task was used in an early fNIRS-based BCI (Naito et al., 2007).

Other

Several studies have reported that brain activity increases if subjects are asked to relax and put their minds to rest (Schudlo et al., 2013, Schudlo and Chau, 2014).

In the fNIRS-BCI literature, there are only two studies that have used patients to record the brain signals (see Table 3): Mental arithmetic and metal listening based tasks were used in these two studies to measure the hemodynamic signals. Since listening is a reactive brain activity that requires external stimuli to generate the brain activity, a mental arithmetic task (being an active task) can be a better option for a patient. However, the literature has no conclusive evidence about the best task for patients for BCI. The pie-chart in Figure 3 shows the distribution of tasks that have appeared in the literature (2002–2017, 102 articles). This may give an overall idea of the possibilities for the selection of an activity for patients to perform.

METHODS TO DETERMINE THE REGION OF INTEREST

It is obvious that if the wrong brain region is selected, proper signals for a BCI cannot be obtained. If we know the exact brain location to be monitored, the burden of placing heavy caps/electrodes/optodes for activity detection can be avoided. A healthy subject may be able to perform the given tasks correctly even using a complex brain signal acquisition system; however, a patient may not be able to do any sort of activity while wearing heavy head-gear. The research issue in this regard is how to select a small brain region, so that the BCI system can be controlled using a limited number of electrodes/optodes. A very comprehensive study of EEG electrode selection has been performed by Alotaiby et al. (2015). However, for fNIRS, no study has fully explored channel selection methodologies yet. Therefore, in this paper, strategies for fNIRS channel selection, which plays a vital role for LIS patients, will be the focus of attention.

Algorithms for Determining the Region of Interest

There are several algorithms that can be used to select the region of interest for BCI. The methods reported in the literature when choosing meaningful fNIRS channels are discussed below:

|[Figure 3]<br><br>FIGURE 3 | Distribution of the prefrontal tasks used for brain-computer interfaces: This chart was constructed using 102 papers (2002–2017) from the Web of Science (www.isiknowledge.com).|
|---|

Channel Averaging

This is the simplest approach, adopted in a number of fNIRS BCI studies (also in EEG and hybrid EEG-fNIRS studies) (Sagara and Kido, 2012; Naseer and Hong, 2013; Scarpa et al., 2013; Naseer

- et al., 2014). Here, all the channels used to detect brain activity are averaged. Equation (1) shows the channel averaging scheme:

M

HbX(k,j) M

j=1

HbXavg(k) =

, (1)

where HbX∈ {HbO, HbR} represents a type of hemoglobin, M is the total number of channels, k represents the discrete time for which the signal is recorded, and j represents the channel number. This technique has a drawback in the case that the brain activity appears in only a few channels and the remaining channels do not show any activation. Averaging over the inactive channels signiﬁcantly reduces the intensity (peak) of the data. This also leads to a signiﬁcant drop in accuracy. Thus, this scheme may not be suited for LIS patients.

Averaging Over a Local Region

This technique has a better chance of achieving high accuracy than the previous scheme. In this case, the brain region on which optodes are placed is divided into 2–3 smaller sub-regions (Scarpa et al., 2013; Ichikawa et al., 2014; Aghajani et al., 2017; Ge et al., 2017; Zhang et al., 2017). During the training phase, the channels in each sub-region are averaged and their accuracies are computed oﬄine. The brain sub-region showing the highest accuracy is selected for the subsequent testing phase. A study by Khan and Hong (2015) used a total of 28 channels in the prefrontal region, which was divided into three sub-regions; sub-region A (the right side, 8 channels), sub-region B (the middle part, 12 channels), and sub-region C (the left side, 8 channels). Their study showed that sub-region A was more active than B or C. This approach is more eﬀective than universal averaging, as it can narrow down the activated brain region. Moreover, fewer inactive channels are used for classiﬁcation, thus

improving the classiﬁcation accuracy. Figure 4 shows an example of partitioning the prefrontal cortex. It is important to note that if only active channels are used for averaging, the accuracy can be further improved.

t-value Based Channel Selection

If a stimulation paradigm is known, the t-value between the measured hemodynamic response and the expected hemodynamic response caused by the given stimulation can be computed. A t-value-based channel selection approach means that only those channels showing positive t-values are used for further analyses. In this case, a threshold value for t in selecting active channels can be set.

In computing the expected/desired hemodynamic response (dHRF), a type of standard hemodynamics response function, named the canonical hemodynamic response function (cHRF), h(k), is used. The dHRF is calculated by convolving the cHRF with the known stimulation interval, s(k), as follows.

u(k) =

k−1

h(n)s(k − n), (2)

n=0

where u(k) is the dHRF and the stimulation interval s(k) is deﬁned as

s(k) =

- 0,if k ∈ rest
- 1,if k ∈ task

, (3)

where rest and task stand for the rest and task periods, respectively. The cHRF, h(k), is generated as a linear combination of two (or three) Gamma variant functions. If the rise of HbO upon brain stimulation and its undershoot afterward are considered, the cHRF is generated by two gamma functions as follows.

h(k) = α1

(k/τ1)(φ1−1)e−(k/τ1) τ1(φ1 − 1)! − α2

(k/τ2)(φ2−1)e−(k/τ2) τ2(φ2 − 1)!

, (4)

|[Figure 4]<br><br>FIGURE 4 | Partitioning the prefrontal cortex: Only a subregion showing the highest accuracy can be used for brain-computer interface purposes (for example, Region A was used by Khan and Hong, 2015).|
|---|

where α1 is the amplitude, τi and φi (i =1, 2) tune the shape and scale respectively, and α2 is the ratio of the peak to the undershoot. If, on the other hand, the initial dip of HbO together with the peak and the undershoot of HbO need to be modeled, three gamma functions can be used as follows (Shan et al., 2014).

3

h(k) =

i=1

kφi−1τiφie−τik Ŵ(φi)

), (5)

(αi

where αi, τi, and φi for i =1, 2, and 3 are the amplitude, time to peak, and width at the half peak value of the initial dip, main hemodynamic response, and undershoot, respectively.

For obtaining t-values, a typical linear regression model using the desired HR can be formulated as follows (Santosa et al., 2013,

- 2014).

hsj(k) = φjsu(k) + ψsj · 1 + εjs, (6)

where the superscript s denotes the stimulation number, u(k) ∈ RN×1 is the modeled hemodynamic response in (2), φ is an unknown coeﬃcient that indicates the activity strength of the modeled hemodynamic response, ψ is a coeﬃcient to compensate for baseline drift of the signal, 1∈ RN×1is a column vector of ones for correcting the baseline, and ε ∈ RN×1 is the error term in the regression model. The coeﬃcient φjs is estimated

- as φjs using a recursive least squares algorithm (Ye et al., 2009). The idea is to test the null hypothesis that the estimated

parameter φjs is equal to zero. If φjs is positive, the speciﬁc activation is assumed to be active, and if it is negative, the speciﬁc activation is not active at the j-th channel, for which the t-value

test has been used. The t-value is computed using the formula

φˆjs SE(φˆjs)

tjs =

, (7)

where SE is the standard error of the estimated coeﬃcient. Two criteria to assess the selection reliability of a particular activation can be used: tjs > 0 and psj < αc, where p denotes the p-value and αc is the conﬁdence interval. Alternatively, this could be done by checking tjs > tcrt, where tcrt denotes the critical t-value that depends on the degree of freedom (which is N −1). In the literature, the t-value based method is widely used for ROI selection, and also for brain imaging, in which the criterion is used to locate the activated brain areas (Hu et al., 2010; Al-Shargie et al., 2016; Li et al., 2017).

Baseline Correction

Instead of computing the t-values for individual channels, the baseline during the rest period can be used as a criterion in selecting channels for further analysis. In this case, the maximum value during the task period and that of the rest period are compared. If the diﬀerence is positive, the channel is considered active (Hu et al., 2013). For example, the following criterion was used for channel selection by Khan and Hong (2017):

δptrial(j) = max(HbOtrial(k3 :k4,j)) − max(HbOrest(k1 :k2,j)),(8)

where δp(j) represents the diﬀerence of the peak during the speciﬁed interval from that of the rest period, j is the channel number, k1 and k2 represent the interval for the rest period, and k3 and k4 represent the interval for the trial period. If δp(j) is positive, the channel is selected as active; otherwise, the channel

is discarded. Thus, this criterion reduces the computational time. For patients who might not be able to keep their heads steady during the acquisition of brain data, computation time becomes important. However, this criterion may result in higher variability throughout the BCI process. Due to this drawback, the baseline correction approach is seldom used. Therefore, it is better to track brain activity on each task to determine the correct brain regions.

Vector-Phase Analysis

This is a relatively new scheme in comparison to the methods described above. Since the vector phase plane is made of HbO and HbR, this method is available only for fNIRS-based BCIs; that is, this method is not applicable to EEG or fMRI. The term (i.e., phase-based analysis) does exist in EEG analysis, but applies to amplitude and phase analyses. The real component in the EEG vector plane is the original band-passed signal, and the imaginary component is the Hilbert transform of the signal, which corresponds to a 90◦ rotation of the real component (Foster et al., 2016). Therefore, the approach used for EEG has no relation with vector phase analysis as used for fNIRS.

Current research indicates that this method is suitable for hemodynamics-based systems for determination of the correct channels. The method was initially proposed for evaluating hemodynamics (Yoshino and Kato, 2012; Sano et al., 2013; Yoshino et al., 2013; Oka et al., 2015). Moreover, it is capable of predicting the trajectory of hemodynamic responses, which can be used for correct channel estimation. Furthermore, the detection of initial dips has been done by using vectorbased phase analysis with a threshold circle as a decision criterion (Hong and Naseer, 2016), in which two independent vectors deﬁned by oxy- and deoxy-hemoglobin ( HbO and

HbR) signals are orthogonally positioned. In addition to HbO and HbR, two other components can be deﬁned as

follows:

HbT =

1 √2

COE =

1 √2

( HbO + HbR), (9)

( HbR − HbO), (10)

where HbT indicates the total hemoglobin concentration change and COE denotes the cerebral oxygen change. Alternatively, these two components can be obtained by rotating the vector coordinate plane deﬁned by HbO and HbR by 45◦ counterclockwise (see Figure 5). The magnitude and phase of a vector, p, in the plane can now be calculated as follows:

p = HbO2 + HbR2, (11)

COE HbT

HbR HbO

) = tan−1(

p = tan−1(

) + 45o. (12)

The ratio of COE and HbT in (12) deﬁnes the degree of oxygen exchange, since COE represents the oxygen exchange in the blood vessels and thus represents neuronal activity. Using the four indices, the phase plane is divided into eight

|[Figure 5]<br><br>FIGURE 5 | Vector-phase diagram proposed by Kato (2003).|
|---|

TABLE 2 | Vector phases for initial dip and hemodynamics (Hong and Naseer, 2016).

Phases HbO and HbR states

HbT and COE states

Conclusion

- 1 Both positive HbO > HbR

HbT is positive COE is negative

Initial dip phase

- 2 Both positive HbO < HbR

Both positive HbT > COE

- 3 HbO is negative HbR is positive

Both positive HbT < COE

- 4 HbO is negative HbR is positive

HbT is negative COE is positive

- 5 Both negative HbO < HbR

HbT is negative COE is positive

- 6 Both negative HbO > HbR

HbT is positive COE is negative

Hemodynamic phase

- 7 HbO is positive HbR is negative

Both negative HbT > COE

- 8 HbO is positive HbR is negative

Both negative HbT < COE

phases (see Figure 5). The description of each phase is given in Table 2.

The use of a threshold circle as a decision criterion, incorporated in the phase plane analysis, helps to minimize possible misidentiﬁcations of initial dips. The radius of the threshold circle for each channel is determined by detecting (i) the peak value of (11), or (ii) max( HbO), or (iii) max( HbR) during the rest state. The initial dip occurrence is concluded when the trajectories of (11) break out the threshold circle while its phase lies within the dip phases (i.e., phases 1–5). For hemodynamics, the activity can be considered concluded if the trajectory crosses the threshold circle in phases 6–8.

The key aspect of vector-phase analysis is the ability to detect the neural activity before the occurrence of hemodynamics. If we are able to tag the locations of individual brain signals, multiple brain signals can be detected as well. In this case, the addition of another threshold circle based on peak values of HbO may be useful to distinguish multiple brain activities using the analysis.

Hardware Conﬁguration

For fNIRS-BCI, the majority of studies have used a sourcedetector-pair conﬁguration, in which a source and a detector are separated at a distance of 3∼5cm for signal recording. Recently, a dense optode conﬁguration has emerged in the literature as a potential tool for a condensed brain imaging. The methods for selecting the region of interest based on hardware coﬁguration are discussed below:

Conventional Conﬁguration

Several diﬀerent emitter-detector conﬁgurations have been used for fNIRS to record brain activities. The emitter-detector distance is usually kept within a speciﬁc range. To measure hemodynamic responses, an emitter-detector separation at around 3cm is used. A separation of less than 1cm might contain only skin-layer contribution, whereas that of more than 5cm might result in weak signal detection. For the prefrontal cortex, 3 emitters and 8 detectors combination is usually used to record the brain activity for BCI (Naseer and Hong, 2015a). Mostly, for this conﬁguration, channel averaging is used for selecting the region of interest.

Bundled-Optode-based Selection

The bundled-optode approach is a recent method of determining a precise brain region, which is currently being pursued for faster fNIRS-based brain imaging. This methodology involves spatially resolved spectroscopy (SRS) (Boas et al., 2014). The SRS approach was initially used to measure optical properties of tissues (Hunter et al., 2002; Kek et al., 2008). In this method, one emitter and

- at least two associated detectors are used, which means that at least two channels are required. The absorption coeﬃcient can then be computed based on the absorbance gradient with respect to the emitter-detector distance. In this case, the NIRS optodes are grouped together to form a bundle. First, the brain location is determined using the International 10–20 system of electrode placement. The optode bundle is then placed on the activated brain region determine which portion is most active (Nguyen and Hong, 2016; Nguyen et al., 2016). In comparison to the optode placement method discussed in section Conventional Conﬁguration, the bundled optode method is more spatially accurate as it removes the skin and skull absorption from the detected signal. Also, all the cortices of a patient may not be able to generate the desired brain activity for BCI. The conventional BCI system is not spatially precise in identifying the desired brain region (or channels) for a command generation. The bundledoptode scheme is able to distinguish the multiple tasks in a small brain region and it is spatially more accurate in identifying the designated brain. Therefore, it can contribute better in locating the activated brain region of a patient for BCI in comparison to the scheme that uses a few channels. Although the current setup may be bulky but, in the future, a micro-array type fNIRS can be developed.

Figure 6 shows the conﬁguration used for the bundledoptode-based scheme. The ﬁgure illustrates the concept of a bundled-optode conﬁguration for the detection of a brain activity in a local brain region. The circles indicate emitters/detectors while the blue arrows illustrate the direction of light from emitters to detectors. The brain activity of each channel is

|[Figure 6]<br><br>FIGURE 6 | Bundled optode scheme: A schematic of densely conﬁgured fNIRS probes for deep brain imaging.|
|---|

detected as the mean values of HbX (i.e., HbO and HbR) that are encoded in to make the 3D color map. The t- or p-values can also be used for the reconstruction of the 3D image. Further research on this approach is needed, as it has a high potential of detecting a precise brain region of interest for each patient.

FEATURE EXTRACTION AND CLASSIFICATION CRITERIA

For generation of proper commands, the identiﬁcation of correct features is essential. For use with patients this is even more crucial, as the use of poor features for classiﬁcation may result in a signiﬁcant drop in accuracy. The signal mean, signal peak, signal slope, latency, skewness, kurtosis, and power spectrum density are the most widely used features for both EEG and fNIRS (Lotte et al., 2007; Naseer and Hong, 2015a,b). Usually the features are categorized as temporal, spatial and spatio-temporal based on their characteristics (Robinson et al., 2016). The temporal features are evaluated using a speciﬁc time window for given data. The spatial features contain frequency-related information about the data in a speciﬁc time window. Increasing the number of features in a classiﬁer increases the processing time. Typically, in fNIRS, a command for an active task is generated using a 2–7-s window. Thus, the extraction of features is directly dependent on the types of signals recorded.

Feature Extraction

In the fNIRS literature, various features have been reported for various types of tasks. In this section, we discuss the features most commonly used for an fNIRS-BCI.

fNIRS-based Feature Extraction

Many features can be estimated based on the HbO and HbR activity in a patient’s brain. Among these features, the mean, peak, and slope are most commonly used (Hwang et al., 2014). A predetermined window is required to estimate these features (Gateau et al., 2015). Research has examined various sizes of windows, but a 2–7-s window from the onset time seems to show the best outcome for a 10-s task (Naseer and Hong, 2013).

### Signal mean

The signal means of HbO and HbR are calculated as follows.

k2

1 Nw

µw =

k=k1

HbX(k), (13)

where the subscript w denotes “window,” µw is the mean value for a given window, k1 and k2 denote the start and end time of the window, Nw is the number of observations in the window, and

HbX represents the HbO or HbR data. Most fNIRS-based BCIs include the signal mean as a feature for classiﬁcation (Hwang et al., 2016; Noori et al., 2017).

### Signal slope

There are two ways to calculate the signal slope. The ﬁrst method is to directly obtain the diﬀerence of the values at the start and end points of a predetermined interval (for example, from 2–7s from the onset time of a stimulus, or the entire stimulus period plus a portion of the subsequent rest period) and to use them to compute the slope (Shin and Jeong, 2014). The second method uses a curve-ﬁtting approach to ﬁt a line to the hemodynamic signal for the predetermined interval. The ﬁrst method is more widely used, but the second method may be preferable (Weyand

- et al., 2015b).

### Signal peak

This feature is the peak value of the signal in a given window. Some studies have reported that peak values worked best in fNIRS (Stangl et al., 2013; Shin and Jeong, 2014).

### Signal minimum

This feature is the minimum value of the signal in a given window. Most commonly this feature has been used to identify an initial dip for a 2-s window. To the best of our knowledge, only three studies have so far used this feature for fNIRS-BCI (Khan and Hong, 2017; Li et al., 2017; Zafar and Hong, 2017).

### Skewness and Kurtosis

The skewness is computed as follows:

Ex( HbXw − µw)3 σ3

, (14)

skeww =

where skew is the skewness, σ is the standard deviation of HbX for the given window, and Ex is the expectation of HbX. The kurtosis is computed as follows.

Ex( HbXw − µw)4 σ4

, (15)

kurtw =

where kurt is the kurtosis of HbX. Both skewness and kurtosis have been reported to work moderately well for fNIRS (Hong and Santosa, 2016; Hwang et al., 2016).

### Number and sum of peaks

The number of peaks is calculated by measuring the local maxima of the HbO signal in a single time window. The ﬁndpeaks function available in MATLAB can be used to measure the number of peaks (either online or oﬄine). The sum of peaks is obtained by summing the local maxima in a given window (Khan and Hong, 2015).

### Others

A few other features such as the variance (Holper and Wolf, 2011), root mean square (Tai and Chau, 2009; Watanabe et al., 2016), standard deviation (Abibullaev et al., 2011) and median (Shin and Jeong, 2014) have also been reported to work for fNIRS. The fast optical response can be used as a feature (Hu et al., 2013). The conversion of optical signals into HbO and HbR can give more information about the brain activity.

Feature Extraction for Hybrid Modalities

EEG and fNIRS are the two main BCI modalities where mobility is required, and recent research has shown that these two systems can be integrated to improve the BCI performance. Most commonly, EEG features are extracted from frequency bands that are related to speciﬁc brain activity. For current control applications, event-related desynchronization/eventrelated synchronization (ERD/ERS) based features are combined with fNIRS to improve the system performance. There is a study that combined EEG and fNIRS for a SSVEP task (Tomita et al., 2014). In our opinion, ERD/ERS based activities can be more useful for patients than SSVEP, as they can be generated deliberately. EEG feature extraction schemes are now brieﬂy discussed.

### Power spectrum density

The power spectral density (PSD) describes the strength of a signal as a function of frequency. For nonparametric methods, the autocorrelation sequence for a given set of data is ﬁrst estimated. The PSD is then calculated by Fourier transforming the estimated autocorrelation sequence. One way of doing this is using the Welch’s method. The method is applied to a moving window, producing a modiﬁed periodogram. The power spectrum density is expressed as follows:

N

1 N

2

xnse−j2πfn

Pfs =

, (16)

n=1

where Pfs denotes the power of the f-th frequency band in the s-th data sequence, xns is the magnitude of the s-th sequence, and N

is the number of samples. Several EEG based control studies have used this method for evaluation of features (Tanaka et al., 2005; Carlson and Millan, 2013). Moreover, most hybrid EEG-fNIRS BCI studies have used the power spectrum as a classiﬁcation feature (Putze et al., 2014; Tomita et al., 2014).

### Logarithmic band power

As the name suggests, this feature is estimated using the logarithms of the power of diﬀerent bands of EEG data. To estimate this feature, ﬁrst the power value of each frequency band is estimated (see Equation 16). The logarithm of the signal power is taken to estimate the highest value in the band:

LPf = log(Pf ), (17)

where LPf is the logarithmic power of the signal. This approach is used in some wheelchair control studies (Tsui et al., 2011; Lee et al., 2015).

### Common spatial patterns

Common spatial patterns (CSP) for EEG feature extraction and classiﬁcation are used to project the multi-channel EEG data into a low-dimensional spatial subspace with a projection matrix of which each row consists of weights for channels. This transformation can maximize the variance of two-class signal matrices. The CSP method is based on simultaneous diagonalization of covariance matrices for the two classes.

To calculate the CSP features, ﬁrst a sample covariance matrix for a trial is calculated as follows:

XXT tr(XXT)

, (18)

R =

where X is the sample data, tr(X) denotes the trace of a matrix, and T denotes the transpose of a matrix. The composite spatial covariance is estimated as follows:

R¯1 + R¯2 = UAUT, (19)

where U denotes the matrix of eigenvectors, and A denotes the diagonal matrix of corresponding eigenvalues. The full projection matrix is then formed as follows:

W = BT

√

A−1UT, (20)

where B denotes the matrix of Eigen vectors for the whitened spatial covariance matrix. The eigenvalues and eigenvectors are sorted in descending order, from ﬁrst to last:

Z = WTX. (21)

A 2-dimensional feature is then constructed from the variance of the rows of Z:

var(Zq) 2

fq = log(

), (22)

var(Zi)

i=1

where Zqis the q-th row of vector Z. The CSP method of feature extraction has been adopted for wheelchair control using both active and reactive tasks (Li et al., 2013b, 2014; Cao et al., 2014; Buccino et al., 2016; Zhang et al., 2016; Ge et al., 2017; Shin et al., 2017).

### Others

There have been a few studies that have also used the time frequency phase (Yin et al., 2015b) and the coeﬃcients of a wavelet transform (Li et al., 2017) as features for EEG, which were combined with fNIRS for hybridization. In an example of hybrid EEG-fNIRS, Blokland et al. (2014) used band power and logistic regression coeﬃcients as features with a 0–15-s window for EEG and a 3–18-s window for fNIRS for tetraplegia patients.

Classiﬁers for Hybrid EEG-fNIRS

Classiﬁcation techniques are used to identify diﬀerent brain signals that are generated by the user. These identiﬁed signals are then translated into control commands for application interface purposes. In most existing fNIRS-BCIs, identiﬁcation is performed by using classiﬁcation techniques to discriminate various brain signals based on appropriate features. Classiﬁcation algorithms, calibrated by supervised learning during a training phase, can detect brain-signal patterns during the testing stage. Here, we will discuss only the classiﬁers that are most commonly used for hybrid EEG-fNIRS.

Linear Discriminant Analysis

Linear discriminant analysis (LDA) is the most commonly used classiﬁcation method in fNIRS and hybrid EEG-fNIRS studies. It utilizes discriminant hyperplane(s) to separate data representing two or more classes. Because of its simplicity and low computational requirements, it is highly suitable for online BCI systems. In LDA, the separating hyperplane is found by seeking a data projection that maximizes the distance between the means of two or more classes and minimizes the interclass variances. LDA assumes a normal data distribution along with equal covariance matrices for both classes.

The optimal projection matrix V for LDA that maximizes the corresponding Fisher’s criterion is given as follows:

det(VTSBV) det(VTSWV)

J(V) =

, (23)

where SB and SW are the between-class scatter matrix and the within-class scatter matrix, respectively, which are deﬁned as follows:

m

(x − µi)(x − µi)T (24)

SW =

i=1 xk∈ class i

m

ni (µi − µ)(µi − µ)T. (25)

SB =

i=1

Here, x ∈ R2 denotes the samples, µi is the sample mean of class i, and µ is the total mean of all the samples, m is the total number

of classes, ni is the number of samples of class i, and n is the total number of samples. Equation (27) is treated as an eigenvalue problem to obtain the optimal vector V that corresponds to the largest eigenvalues. Many fNIRS and hybrid EEG-fNIRS studies have successfully used LDA for BCIs (Luu and Chau, 2009; Bauernfeind et al., 2011; Fazli et al., 2012; Moghimi et al., 2012; Khan et al., 2014; Lee et al., 2015; Ahn et al., 2016; Buccino et al., 2016; Shin et al., 2017).

Support Vector Machines

The support vector machine (SVM) is a very popular pattern recognition technique for brain signal classiﬁcation. It has been used in various fNIRS studies (Sitaram et al., 2007; Cui et al., 2010; Tanaka and Katura, 2011; Putze et al., 2014; Koo et al.,

- 2015). It is a supervised classiﬁer that can deﬁne two or more classes by determining the maximum class separation, known as the “maximum margin hyperplane.” The algorithm does this by mapping the input data to a feature space that can be divided using linear or non-linear decision boundaries, depending on the kernel. The SVM classiﬁer tries to maximize the distance between the separating hyperplane and the nearest training point(s) (the so-called support vectors). The separating hyperplane in the 2D feature space is given by the equation

f(x) = r · x + b1, (26)

where r, x ∈ R2 and b ∈ R1. The optimal solution r∗ that maximizes the distance between the hyperplane and the nearest training point(s) can be obtained by minimizing the cost function

- 1

- 2

r 2 + C · Z

L(r,ξ) =

n=1

while satisfying the constraints

ξn, (27)

(xn.r + b1) ≥ 1 − ξn for yn = +1, (28) (xn.r + b1) ≥ −1 + ξn for yn = −1

ξn ≥ 0 ∀n,

where r 2 = rTr, C is a positive regularization parameter chosen by the user (a large value of C corresponds to a high penalty for classiﬁcation errors), ξn is a measure of training error, z is the number of misclassiﬁed samples, and yn is the class label (+1 or −1 in the case of binary classiﬁcation) for the n-th sample.

The radial basis function (RBF) kernel is widely used, as it allows complex separation surfaces requiring a reduced number of hyper-parameters to tune. The hyper-parameters for this SVM give an upper bound on the fraction of margin errors and a lower bound on the fraction of support vectors. For a multiclass problem, the data are subdivided into several binary class problems and used in a one-against-one approach. Thus, for an m-class problem, m(m − 1)/2 machines are trained.

Extreme Learning Machine

The extreme learning machine (ELM) is a learning algorithm in which single-hidden-layer feedforward neural networks are used for classiﬁcation and regression. The ELM training algorithm can adaptively set the number of hidden layer nodes and randomly

assigns the input weights and hidden layer biases. The output layer weights are obtained by the least squares method, and the whole learning process is completed in one calculation stage without iteration (Deng et al., 2010). The ELM for N arbitrary distinct samples (xi, li), where xi =[xi1, xi2, ... xin]T ∈ Rn and li =[li1, li2, ... lim]T ∈ Rm, and (xi, li) ∈ Rn x Rm (i-1,2,...,N), for a standard single-layer feedforward neural network with NH hidden nodes and activation function g(x), is given as follows:

N

N

βigi(ai.xd + bi) = od,d = 1,2,...,N, (29)

βigi(xd) =

i=1

i=1

where ai is the weight vector connecting the i-th hidden neuron to the input, and bi is the threshold of the i-th hidden neuron, βi is the weight vector connecting the i-th hidden neuron to the output, and od is the d-th output vector of single layer feed forward neural network. The above equation can be written as follows:

Hβ = O,

f(a1.x1 + b1) ··· f(aN.xN + bN) . ··· . f(a1.xN + b1) ··· f(aN.xN + bN)

  

  

, (30)

N×N

β1T . βNT

oT1 . oTN

  

  

  

  

,O =

β =

N×m

N×m

where H(a1, a2, ..., aN, b1, b2, ..., bN, x1, x2, ..., xN) is called the hidden layer output matrix of the neural network. After the input weights and hidden layers biases are determined in accordance with the random assignment, the input samples are used to obtain the hidden layer output matrix H. A least squares solution for the above equation can be found as follows:

∧ β = H†O, (31)

where H represents the Moore-Penrose generalized inverse of the hidden layer output matrix H. The optimal solution βˆ controls the minimal training error gain of the algorithm. A few fNIRS studies have used ELM for BCI (Yin et al., 2015a,b).

Vector Phase Analysis as a Classiﬁer

As discussed earlier, vector phase analysis can be used for identiﬁcation of brain regions (see the Vector-Phase Analysis section). It has applications in classiﬁcation as well. To the best of our knowledge, only one study has used this classiﬁer to decode two diﬀerent brain states (Zafar and Hong, 2017). The current limitation in this method is that it has been used only to distinguish between resting and activity states. Further research in this area is needed to improve the usability of the method for decoding multiple tasks. Figure 7 shows the strategy adopted by vector phase analysis for decoding two choices.

Deep learning algorithms can also be a potential candidate for classiﬁcation of brain images. The conventional classiﬁers may

|[Figure 7]<br><br>FIGURE 7 | Illustration of vector-phase analysis for two choice decoding.|
|---|

not be eﬀective for identiﬁcation of neuro-plasticity from brain images. So far, only one fNIRS study has used deep learning approach for BCI (Trakoolwilaiwan et al., 2017). As described in the study, a Convolutional Neural Network (CNN) can be eﬀective for classiﬁcation of multiple brain activities from a brain image. Just like the extreme learning machine, a CNN is comprised of one or more layers that are convolutional followed by one or more fully connected layers. The architecture of a CNN

is designed to take advantage of the 2D structure of an input image that can be beneﬁcial to detect an activity from a brain map. CNN can be trained with a few parameters and thus the command generation for BCI control may not be increased.

Figure 8 shows distributions of the features and classiﬁers that have been used during 2010–2017 for fNIRS. The lower part of the ﬁgure shows information on hybrid EEG-fNIRS features and classiﬁers used to generate multiple commands.

|[Figure 8]<br><br>FIGURE 8 | Features and classiﬁers used in fNIRS and hybrid EEG-fNIRS studies (64 fNIRS-BCI papers and 14 hybrid EEG-fNIRS papers from 2010 to 2017).|
|---|

## DEVICE INTERFACES

The purpose of a BCI is not achieved if a ﬁnal interface with a machine is not provided for communication with a patient. It can

be diﬃcult for a patient to generate multiple commands needed to operate a complex system. A simpliﬁed and easy interface is required for a BCI to be taken out of the laboratory environment. The BCI should be designed in accordance with the number of

commands that a patient is able to generate. Even if a reactive BCI may be able to generate multiple commands, it may not be a viable option for real life. It is obvious that if the wrong brain region is selected for activity detection, a proper signal for BCI cannot be generated. Most fNIRS studies have not yet provided a device interface that can prove its utility for patients. To discuss the major role of device interfaces in fNIRS and fNIRS-based hybrid BCI, we categorize the existing studies based on the types of applications.

Choice Selection

A great majority of fNIRS studies for BCI have focused on decoding only two commands. A list of these studies was provided in Table 3. It can be clearly seen from the table that only a single study was able to implement their BCI for LIS patients. The remaining studies do not show any evidence of working with patients. The table also shows that the signal mean was used most often as a feature, with LDA for classiﬁcation. Moreover, none of the studies was able to implement their BCI in real-time. Probably the inherent delay of the hemodynamic signals was a restricting factor; this problem is not easy to overcome, because implementation of the results for real-time applications may signiﬁcantly reduce the accuracy. Even so, after examining the literature, we can say that fNIRS-based BCIs have the capability to decode two choices for patients using active paradigms. Further research with LIS patients as subjects can focus on ﬁnding optimal features that can be used to enhance the classiﬁcation accuracy and to increase the number of commands available for control.

Gait and Balance Control

Mihara et al. (2008) have reported that the cortical activation associated with postural adjustment of a patient results in a signiﬁcant increase in HbO in the bilateral prefrontal cortex. These activations can be used to control a robotic interface for postural control and balancing of a locked-in patient (Khan et al., 2018). However, further research is needed in this domain to decode multiple postures for patients.

Brain Plasticity Monitoring

fNIRS can serve as a tool for monitoring of neuroplasticity and functional recovery after brain injury. Patients with acute brain injury such as stroke can take months to recover from the injury (Jørgensen et al., 1999). fNIRS can be used for estimating the cortical plasticity of the patient’s brain. However, deep brain imaging may be required to estimate diﬀerent stages of brain recovery/plasticity of a patient. For these cases, deep learning algorithms like convolutional neural network can play a vital role in estimation of brain plasticity/recovery.

Wheelchair Control

In this category, we selected only fNIRS and hybrid EEG-fNIRS studies in which more than two commands were generated. The list of these studies is provided in Tables 3, 4. It can be seen from Table 3 that the accuracy of fNIRS-BCI is very low for 5-command decoding. However, the accuracy for four or more commands becomes higher if a hybrid EEG-fNIRS

technique is used. Patients who suﬀer severely from motor disorders may not be able to generate many commands even with hybridization. However, an increase in the number of commands and enhancement in accuracy promises more safety and ﬂexibility for patients. The main reason is that the commands generated using one brain signal acquisition modality can be veriﬁed with the other; thus, the accuracy is improved. Although wheelchair control has not yet been implemented using fNIRS alone, hybridization might achieve this objective with enhanced accuracy.

## WHAT FUTURE DIRECTION TO ADOPT?

From the information presented here, it can be deduced that we are still far from successfully implementing a BCI for a patient that works in real-time. However, the current research trends are headed in the right direction and the goal may not be impossible to achieve. There are certain issues that must be resolved ﬁrst to allow more rapid progress toward achieving the goal.

The ﬁrst requirement is to use patients instead of healthy subjects to validate a BCI method. Even if BCI schemes can be successfully implemented on healthy persons, it may be diﬃcult to use the same methods for patients. Many studies suggest that high accuracy for patients should be possible, but the reality may be diﬀerent (Chaudhary et al., 2017).

The second necessity is the selection of appropriate brain activity for LIS patients. Currently, we cannot say for sure which brain task is best suited for a patient. A healthy person can perform any reasonable task, but a patient requires a task from a number of options. Strong conclusions can only be drawn if large samples of patients are used to evaluate diﬀerent types of brain tasks.

Another issue is the selection of a good brain region. As discussed, most studies have focused on averaging or selecting a single channel for BCI. A precisely localized brain location is required for high-quality detection of brain activity. In this context, further research on the bundled optode scheme using fNIRS is required to narrow down the optimal brain region for a patient. Moreover, deep brain imaging techniques may have a possibility of better discriminating brain signals than conventional methods (Nguyen and Hong, 2016; Nguyen et al., 2016).

Another point raised here is that most fNIRS studies have not physically implemented their BCI. There might be beneﬁt in using additional external sensors (e.g., blood-pressure monitoring, respiration, and cardiac monitoring at the same time) to make the ﬁnal decision to generate a command. Even for a very basic problem of Yes/No decoding (see section Choice Selection), an incorrectly generated command may lead to severe consequences in a real environment; especially for a lockedin patient who may not be able to respond to a misclassiﬁed decision. Therefore, improvement in this category is needed.

Most BCI studies have found that the output from hemodynamic or neuronal signals are suﬃcient for device control. However, the high accuracy sometimes occurs due to false detection of brain signals. For real-time control, this false

TABLE 3 | fNIRS-BCI studies (2012–2017) that decoded brain activities from the prefrontal cortex.

References Type of subject

Brain region selection scheme

Analysis type Task Features Classiﬁer Possible application

Number of commands

Classiﬁcation accuracy (%)

Hu et al., 2012

Healthy Channel averaging

Online Truth/lie Absolute values of HbO and HbR

SVM 2 choice decoding

2 83.4

Power et al.,

- 2012a

Healthy Channel averaging

Ofﬂine Mental arithmetic

Signal slope LDA 2 choice selection

2 72.6

Power et al.,

- 2012b

LDA Can be used for wheel chair control

3 56.2

Healthy Channel averaging

Ofﬂine Mental arithmetic and mental singing

Signal slope of linear regressing line

Chan et al.,

- 2012

Healthy Channel averaging

Ofﬂine Mental singing

Peak of HbO and HbR

HMM and ANN

2 choice decoding

2 55.7 for HMM and 63 for ANN

Abibullaev and An, 2012

Healthy Single channel selection based on wavelet coefﬁcients

Ofﬂine Object rotation, letter padding and multiplication

Filter coefﬁcients from wavelet transform

LDA and SVM

Applicable for wheelchair control

2 (can be used to generate 4 commands)

> 85 (LDA) > 90 (SVM)

Moghimi et al., 2012

Healthy Channel averaging

Ofﬂine Music listning Mean and

difference between signal and noise of

HbO and HbR

LDA 2 choice decoding

2 71.9

Power and Chau, 2013

Duchenne muscular dystrophy patient

Individual channel used

Online Mental arithmetic

Signal slope of HbO and HbR

LDA 2 choice decoding

2 71.1

Stangl et al.,

- 2013

Healthy Channel averaging

Online Motor imagery, mental arithmetic

Amplitude of HbO

LDA 2 choice decoding

2 65

Faress and

- Chau, 2013

Healthy Individual channel used

Ofﬂine Verbal ﬂuency Slope of HbO, HbR and HbT

LDA 2 choice decoding

2 86

Schudlo and

- Chau, 2014

Healthy Individual channel used

Online Mental arithmetic

Slope of HbO, HbR and HbT

LDA 2 choice decoding

2 77.4

Naseer et al.,

- 2014

Healthy Channel averaging

Online Mental arithmetic

Mean values of HbO and HbR

LDA and SVM

2 choice decoding

2 74.2 (LDA)

82.1 (SVM) Hwang et al.,

LDA 2 choice decoding

2 > 70 (mental arithmetic and mental rotation)

Healthy Channel averaging

Ofﬂine Motor Imagery, mental singing, mental arithmetic, mental rotation and mental character writing

Mean values of HbO, HbR and HbT

- 2014

2 78

Slope of HbO and HbR

LDA Mental workload measurement

Herff, 2014 Healthy Individual channel used

Ofﬂine n-back task for mental workload

Online Active and drowsy state

Mean, peak and sum of pekas of

Khan and Hong, 2015

Healthy Brain segmentation to identify precise location

LDA and SVM

Drowsiness detection

2 83.1 (using LDA) 84.4 (using SVM)

HbO

(Continued)

- TABLE 3 | Continued

References Type of subject

Brain region selection scheme

Analysis type Task Features Classiﬁer Possible application

Number of commands

Classiﬁcation accuracy (%)

Hong et al.,

- 2015

Healthy Channel averaging

Naseer and Hong, 2015b

Healthy Channel averaging

Bhutta et al.,

- 2015

Healthy Channel averaging

Online Truth and lie Signal mean and signal slope

LDA 2 choice decoding

2 86.5

Weyand

- et al., 2015a

Healthy Individual channel used

Online 11 mental tasks

Changes in HbO, HbR and HbT

LDA 2 choice decoding

2 76.0

Yin et al., 2015a

Healthy Individual channel

Online Motor Difference of HbO and HbR

ELM Applicable to wheelchair control

3 >75

C Schudlo and Chau,

- 2015a

Healthy Individual channel used

Online Verbal ﬂuency, Stroop and rest

Slope of HbO, HbR and HbT

LDA Can be used for wheelchair control

3 71.7

Schudlo and Chau, 2015b

Healthy Individual channel used

Ofﬂine Verbal ﬂuency, Stroop and rest

Slope of HbO, HbR and HbT

LDA 2 choice decoding

2 82.8

Weyand et al., 2015b

Healthy Individual channel

Online 5 mental tasks

Temporal changes in HbO, HbR and HbT

LDA 2 choice decoding

2 76.6

Weyand and Chau, 2015

Healthy Individual channel

Online 6 mental tasks

Temporal changes in HbO, HbR and HbT

LDA Can be tested for wheelchair control

Upto 5 78.0 for 2 class 37.0 for 5 class

Durantin

- et al., 2016

Healthy Averaging Ofﬂine Digit memorization

Peak of HbO and HbR

SVM 2 choice decoding

2 77.8%

Naseer et al., 2016a

Healthy Averaging Ofﬂine Mental arithmetic

Mean, slope, variance, peak and kurtosis

LDA 2 choice decoding

2 93.0

Naseer et al., 2016b

Healthy Averaging Ofﬂine Mental arithmetic

Mean, slope, variance, peak and kurtosis

LDA, QDA, KNN, Bayes, SVM and ANN

2 choice decoding

2 96.3

Zafar and Hong, 2017

Healthy Averaging on speciﬁc channels

Ofﬂine Mental arithmetic, mental counting and puzzle solving

Initial dip features (signal mean and signal minimum of

HbO)

Vector phase analysis and: LDA

2 choice decoding

2 57.5 for initial dip

Qureshi et al., 2017

Healthy Averaging Ofﬂine Motor imagery and mental rotation

Coefﬁcients of GLM

LDA Can be used for wheelchair control

3 87.8

Chaudhary

- et al., 2017

Online Motor imagery, mental arithmetic

Online Motor imagery and mental arithmetic

Mean and slope of HbO

Mean and slope of HbO and HbR

LDA Can be used for wheelchair control

LDA 4 choice selection (can be used for wheelchair control)

3 75.6

4 73.3

Individual channel

Amyotrophic lateral sclerosis

Online Mental listening task

Signal mean SVM Choice decoding

2 70.0

- TABLE 4 | Features and classiﬁers used for hybrid EEG-fNIRS.

References Type of subject

Analysis type Task NIRS features

EEG features

Classiﬁer Possible application

Number of commands

Classiﬁcation accuracy (%)

Fazli et al., 2012

Tomita et al.,

- 2014

Healthy Ofﬂine SSVEP First and second derivative of

HbO and HbR

Band power

Joint classiﬁer Multiple choice selection and wheelchair control

2 >90

Khan et al.,

- 2014**

Healthy Online Motor execution, mental counting and mental arithmetic

Mean values of HbO and

HbR

Band power

LDA Wheelchair control

4 > 80

Blokland et al., 2014

Tetraplegia patients

Ofﬂine Motor task Mean of HbO and HbR in 3∼18 sec window

Band power

Linear logistic regression classiﬁer

Choice decoding

2 Average accuracy >80

Putze et al.,

- 2014

Healthy Ofﬂine Audio and video perception

Difference of mean of HbO and HbR

Band power

SVM Choice decoding

2 Highest accuracy>90

Koo et al.,

- 2015

Healthy Online Motor task Threshold for HbO

CSP SVM for EEG and threshold for fNIRS

Choice decoding

2 >85

Lee et al.,

- 2015

Healthy Online Motor task Mean amplitude of HbO and HbR

CSP and Logarithmic power

LDA Choice decoding

2 >85

Yin et al.,

- 2015b

Healthy Online Motor Difference of HbO and HbR

Timefrequency Phase

ELM Choice decoding

2 >89

Buccino

- et al., 2016

Healthy Ofﬂine Motor Signal mean and Signal slope of HbO

CSP LDA Applicable to wheelchair control

4 >70

Ahn et al., 2016

Healthy Online Drowsiness Amplitude of HbO and HbR

Band power

LDA Sleep task 2 >75

Khan and Hong, 2017

Healthy Online Mental task Initial dip and hemodynamic features (Mean, minimum and peak of HbO in 2 sec window)

Band power and Peak amplitude

LDA Quadcopter control (More possibilities for wheelchair control)

8 >75

Li et al., 2017 Healthy Online Motor Mean values of HbO and HbR in 2 sec window

Coefﬁcient of wavelet transform

SVM Choice decoding in 2 sec window

2 >90

Aghajani

- et al., 2017

- 2017

Ge et al.,

Healthy Ofﬂine Motor tasks Mean HbO, HbR and HbT

Band power

LDA Choice decoding

2 >90

Healthy Online Working memory

Peak, slope, standard deviation, skewness and kurtosis of HbO and HbR

Healthy Ofﬂine Motor Hurst exponent

Band power and phase locking value

SVM Mental fatigue estimation

2 >80

CSP SVM Choice decoding

2 >80

|[Figure 9]<br><br>FIGURE 9 | Proposed brain-computer interface (BCI) scheme to improve the BCI performance for device control for locked-in syndrome patients.|
|---|

positive detection may create a safety issue for LIS patients. Therefore, a better approach is to hybridize neuronal and hemodynamic signals. Current research on hybridization has only used system based on combinations of probability scores (Buccino et al., 2016). There is a need to develop new methods of integrating neuronal and hemodynamic deep brain activity.

One more issue in achieving device control is reliability of the brain signals from patients. It may be diﬃcult for a patient to concentrate on the brain task for a long duration. Thus, the accuracy for controlling a machine will be reduced signiﬁcantly. It will be better if a shared control is implemented to achieve better outcome for a patient. The shared control is to use an artiﬁcial intelligence technique combined with a BCI to improve the control performance. For example, in the case of a wheelchair control, a semi-autonomous control can be implemented. The brain signals are used to activate/deactivate the wheelchair whereas a motion planning algorithm can be implemented for the wheelchair to reach the destination. In this case, the patient can concentrate less on generating the brain activity for control, and this will reduce the stress and anxiety level of the patient.

Brain therapy is also an important factor in the quest to improve brain state decoding. Many studies have shown that tDCS- and rTMS-based stimulation can signiﬁcantly improve brain activity for purposes of BCI. In stroke patients, it is essential that the brain be monitored for signs of improvement (Sood et al., 2016). In our opinion, along with the use of hybrid brain-signal acquisition modalities, there is a need for continuous brain stimulation to improve the brain recovery process. Figure 9 shows our proposed scheme. As indicated in Figure 9, brain therapy is essential when brain activity detection is not workable. The correct brain region needs to be targeted for therapy. Integration of neuronal and hemodynamic signals may prove to be a good method for localizing it.

In comparison to the conventional fNIRS-BCIs (Blokland et al., 2014; Chaudhary et al., 2017), the suggested BCI scheme

has an advantage of being more eﬀective for patients. Currently, a speciﬁc brain region is not targeted and most BCIs are implemented by averaging the channels. For a patient, it is important to know the speciﬁc brain region that can be used for BCI. As per the authors’ opinion shown in Figure 9, a speciﬁc brain region needs to be identiﬁed ﬁrst for using EEG/fNIRS for command generation. If the activity recorded for BCI is not signiﬁcant, a neuroplasticity in that brain region can be pursued. If the unresponsive brain region is identiﬁed by an adaptive algorithm, rTMS/tDCS stimulation can be applied to improve the neuroplasticity. Then, the brain region that shows improvement after brain stimulation can be used.

We suggest that the most pressing current need for fNIRS and hybrid EEG-fNIRS is to take experimentation out of the lab and test the results on real patients. To achieve this objective, a signiﬁcant improvement in hardware development is needed. A hybrid system for hemodynamic and neuronal signal detection and integration is required in a package that is comfortable for patients (less bulky). The hardware should be able to handle the motion artifacts generated by LIS patients. Moreover, it is important to detect deep brain activation. Therefore, research should focus on development of hardware that can reliably acquire deep brain activity in real-time. Furthermore, algorithms are needed that can integrate the neuronal and hemodynamic signals to generate a reliable brain image. Perhaps, a breakthrough in fNIRS-BCI can be achieved by using brain imaging features instead of conventional features (Hong et al., 2017).

## CONCLUSIONS

In this paper, we have reviewed recent work on functional nearinfrared spectroscopy (fNIRS) and hybrid fNIRS-EEG studies for brain-computer interfaces (BCI). The focus was on ﬁnding the brain activity patterns, channel selection criteria, feature extraction schemes, and classiﬁcation algorithms that are most suitable for locked-in patients.

We discussed brain activities that can cause a signiﬁcant increase in the hemodynamic response. We noted that mental arithmetic is the most widely used activity for fNIRS-BCI. However, there is no speciﬁc activity that can be claimed to be most suitable for locked-in patients. Similarly, there exist diﬀerent algorithms for brain area identiﬁcation, but their true potential for patients is yet to be seen. Moreover, signal mean and signal peak are the most appropriate features for classiﬁcation of hemodynamics, but only a limited literature show evidences of these features giving good results for patients. For hybridization, most commonly the mean fNIRS signal is combined with the power spectrum density from EEG to improve the system accuracy. Lastly, linear discriminant analysis is the most widely used classiﬁer for fNIRS and hybrid fNIRS-BCI. However, vector phase analysis is a new method that has potential both for identiﬁcation of brain regions and classiﬁcation of

hemodynamic responses. Further research on this algorithm is warranted.

## AUTHOR CONTRIBUTIONS

K-SH has conceived the idea, corrected the manuscript, and ﬁnalized the work. MK conducted the literature survey and wrote the ﬁrst draft of the manuscript. MH participated in revising the manuscript. All the authors have approved the ﬁnal manuscript.

## ACKNOWLEDGMENTS

This work was supported by the National Research Foundation (NRF) of Korea under the auspices of the Ministry of Science and ICT, Republic of Korea (grant nos. NRF-2017R1A2A1A17069430 and NRF-2017R1A4A1015627).

## REFERENCES

Abibullaev, B., An, J., and Moon, J. I. (2011). Neural network classiﬁcation of brain hemodynamic responses from four mental tasks. Int. J. Optomechatr. 5, 340–359. doi: 10.1080/15599612.2011.633209

Abibullaev, B., and An, J. (2012). Classiﬁcation of frontal cortex hemodynamic responses during cognitive tasks using wavelet transforms and machine learning algorithms. Med. Eng. Phys. 34, 1394–1410. doi: 10.1016/j.medengphy.2012.01.002

Aghajani, H., Garbey, M., and Omurtag, A. (2017). Measuring mental workload with EEG plus fNIRS. Front. Hum. Neurosci. 11:359. doi: 10.3389/fnhum.2017.00359

Ahn, M., and Jun, S. C. (2015). Performance variation in motor imagery brain-computer interface: a brief review. J. Neurosci. Methods 243, 103–110. doi: 10.1016/j.jneumeth.2015.01.033

Ahn, S., Nguyen, T., Jang, H., Kim, J. G., and Jun, S. C. (2016). Exploring neurophysiological correlates of drivers’ mental fatigue caused by sleep deprivation using simultaneous EEG, ECG, and fNIRS data. Front. Hum. Neurosci. 10:219. doi: 10.3389/fnhum.2016.00219

Al-Shargie, F., Kiguchi, M., Badruddin, N., Dass, S. C., Hani, A. F., and Tang, T. B.

(2016). Mental stress assessment using simultaneous measurement of EEG and fNIRS. Biomed. Optics Exp. 7, 3882–3898. doi: 10.1364/BOE.7.003882

Alotaiby, T., Abd El-Samie, F. E., Alshebeili, S. A., and Ahmad, I. (2015). A review of channel selection algorithm for EEG signal processing. EURASIP J. Adv. Sig. Pro. 2015:66. doi: 10.1186/s13634-015-0251-9

Banville, H., and Falk, T. H. (2016). Recent advances and open challenges in hybrid brain-computer interfacing: a technological review of non-invasive human research. Brain Comput. Interf. 3, 9–46. doi: 10.1080/2326263X.2015.1134958

Bauernfeind, G, Leeb, R., Wriessnegger, S. C., and Pfurtscheller, G. (2008). Development, set-up and ﬁrst results for a one-channel near-infrared spectroscopy system. Biomed. Tech. 53, 36–43. doi: 10.1515/BMT.2008.005 Bauernfeind, G., Scherer, R., Pfurtscheller, G., and Neuper, C. (2011). Single-trial classiﬁcation of antagonistic oxyhemoglobin responses during mental arithmetic. Med. Biol. Eng. Comput. 49, 979–984. doi: 10.1007/s11517-011-0792-5

Bhutta, M. R., Hong, K. S., Kim, B. M., Hong, M. J., Kim, Y. H., and Lee, S. H. (2014). Note: Three wavelengths near-infrared spectroscopy system for compensating the light absorbance by water. Rev. Sci. Instrum. 85:026111. doi: 10.1063/1.4865124

Bhutta, M. R., Hong, M. J., Kim, Y. H., and Hong, K. S. (2015). Single-trial lie detection using a combined fNIRS-polygraph system. Front. Psychol. 6:709. doi: 10.3389/fpsyg.2015.00709

Blokland, Y., Spyrou, L., Thijssen, D., Eijsvogels, T., Colier, W., FloorWesterdijk, M., et al. (2014). Combined EEG-fNIRS decoding of motor

attempt and imagery for brain switch control: an oﬄine study in patients with tetraplegia. IEEE Trans. Neural Syst. Rehabil. Eng. 22, 222–229. doi: 10.1109/TNSRE.2013.2292995

Boas, D. A., Elwell, C. E., Ferrari, M., and Taga, G. (2014). Twenty years of functional near-infrared spectroscopy: introduction for the special issue. Neuroimage 85, SI(Part 1), 1–5. doi: 10.1016/j.neuroimage.2013.11.033

Buccino, A. P., Keles, H. O., and Omurtag, A. (2016). Hybrid EEG-fNIRS asynchronous brain-computer interface for multiple motor tasks. PLoS ONE 11:e0146610. doi: 10.1371/journal.pone.0146610

Buckner, R. L., Andrews-Hanna, J. R., and Schacter, D. L. (2008). The brain’s default network: anatomy, function, and relevance to disease. Ann. N. Y. Acad. Sci. 11, 1–38. doi: 10.1196/annals.1440.011

Cao, L., Li, J., Ji, H., and Jiang, C. (2014). A hybrid brain computer interface system based on the neurophysiological protocol and brainactuated switch for wheelchair control. J. Neurosci. Methods 229, 33–43. doi: 10.1016/j.jneumeth.2014.03.011

Carlson, T., and Millan, J. D. (2013). Brain-controlled wheelchairs a robotic architecture. IEEE Robot. Autom. Mag. 20, 65–73. doi: 10.1109/MRA.2012.2229936

Chan, J., Power, S., and Chau, T. (2012). Investigating the need for modeling temporal dependencies in a brain-computer interface with real-time feedback based on near infrared spectra. J. Near Infrared Spectrosc. 20, 107–116. doi: 10.1255/jnirs.971

Chaudhary, U., Xia, B., Silvoni, S., Cohen, L. G., and Birbaumer, N. (2017). Braincomputer interface-based communication in the completely locked-in state. PLoS Biol. 15:e1002593. doi: 10.1371/journal.pbio.1002593

Cui, X., Bray, S., and Reiss, A. L. (2010). Speeded near-infrared spectroscopy (NIRS) response detection. PLoS ONE 5:e15474. doi: 10.1371/journal.pone.0015474

Das, A., Guhathakurta, D., Sengupta, R., and Dutta, A. (2016). EEG-NIRS joint-imaging based assessment of neurovascular coupling in stroke: a novel technique for brain monitoring. Int. J. Stroke 11, 271–272.

Deng, W., Zheng, Q., Lian, S. G., Chen, L., and Wang, X. (2010). Ordinal extreme learning machine. Neurocomputing 74, 447–456. doi: 10.1016/j.neucom.2010.08.022

de Oliveira, F. C. L., Bouyer, L. J., Ager, A. L., and Roy, J. S. (2017). Electromyographic analysis of rotator cuﬀ muscles in patients with rotator cuﬀ tendinopathy: a systematic review. J. Electromyogr. Kinesiol. 35, 100–114. doi: 10.1016/j.jelekin.2017. 06.002

Durantin, G., Scannella, S., Gateau, T., Delorme, A., and Dehais, F. (2016). Processing functional near infrared spectroscopy signal with a kalman ﬁlter to assess working memory during simulated ﬂight. Front. Hum. Neurosci. 9:707. doi: 10.3389/fnhum.2015.00707

Dutta, A. (2015). Bidirectional interactions between neuronal and hemodynamic responses to transcranial direct current stimulation (tDCS): Challenges for brain-state dependent tDCS. Front. Syst. Neurosci. 9:107. doi: 10.3389/fnsys.2015.00107

Dutta, A., Jacob, A., Chowdhury, S. R., Das, A., and Nitsche, M. A. (2015). EEGNIRS based assessment of neurovascular coupling during anodal transcranial direct current stimulation - a stroke case series. J. Med. Syst. 39:36. doi: 10.1007/s10916-015-0205-7

Ehlis, A. C., Herrmann, M. J., Wagener, A., and Fallgatter, A. J. (2005). Multichannel near-infrared spectroscopy detects speciﬁc inferior-frontal activation during incongruent Stroop trials. Biol. Psychol. 69, 315–331. doi: 10.1016/j.biopsycho.2004.09.003

Fan, X. A., Bi, L. Z., Teng, T., Ding, H. S., and Liu, Y. L. (2015). A brain-computer interface-based vehicle destination selection system using P300 and SSVEP signals. IEEE Trans. Intell. Transp. Syst. 16, 274–283. doi: 10.1109/TITS.2014.2330000

Faress, A., and Chau, T. (2013). Towards a multimodal brain-computer interface: combining fNIRS and fTCD measurements to enable higher classiﬁcation accuracy. Neuroimage 77, 186–194. doi: 10.1016/j.neuroimage.2013.03.028 Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Müller, K. R., et al. (2012). Enhanced performance by a hybrid NIRS-EEG brain computer interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084 Feess, D., Krell, M. M., and Metzen, J. H. (2013). Comparision of sensor selection mechanism for an ERP-based brain-computer interface. PLoS ONE 8:e67543. doi: 10.1371/journal.pone.0067543

Fernández-Rodríguez, Á., Velasco-Álvarez, F., and Ron-Angevin, R. (2016). Review of real brain-controlled wheelchairs. J. Neural Eng. 13:061001. doi: 10.1088/1741-2560/13/6/061001

Foster, B. L., He, B. J., Honey, C. J., Jerbi, K., Maier, A., and Saalmann, Y. B.

(2016). Spontaneous neural dynamics and multi-scale network organization. Front. Syst. Neurosci. 10:7. doi: 10.3389/fnsys.2016.00007

Ge, S., Yang, Q., Wang, R. M., Lin, P., Gao, J. F., Leng, Y., et al. (2017). A braincomputer interface based on a few-channel EEG-fNIRS bimodal system. IEEE Access 5, 208–218. doi: 10.1109/ACCESS.2016.2637409

Gateau, T., Durantin, G., Lancelot, F., Scannella, S., and Dehais, F. (2015). Realtime state estimation in a ﬂight simulator using fNIRS. PLoS ONE 10:e0121279. doi: 10.1371/journal.pone.0121279

Gruzelier, J. H. (2014). EEG-neurofeedback for optimising performance. I: a review of cognitive and aﬀective outcome in healthy participants. Neurosci. Biobehav. Rev. 44, 124–141. doi: 10.1016/j.neubiorev.2013.09.015

Guger, C., Spataro, R., Allison, B. Z., Heilinger, A., Ortner, R., Cho, W., et al. (2017). Complete locked-in and locked-in patients: command following assessment and communication with vibro-tactile p300 and motor imagery brain-computer interface tools. Front. Neurosci. 11:251. doi: 10.3389/fnins.2017.00251

Hatakenaka, M., Miyai, I., Mihara, M., Sakoda, S., and Kubota, K. (2007). Frontal regions involved in learning of motor skill - A functional NIRS study. Neuroimage 34, 109–116. doi: 10.1016/j.neuroimage.2006.08.014

Herﬀ, C, Heger, D, Fortmann, O, Hennrich, J, Putze, F, and Schultz, T (2014). Mental workload during n-back task—quantiﬁed in the prefrontal cortex using fNIRS. Front. Hum. Neurosci. 7:935. doi: 10.3389/fnhum.2013. 00935

Hofmann, M. J., Herrmann, M. J., Dan, I., Obrig, H., Conrad, M., Kuchinke, L., et al. (2008). Diﬀerential activation of frontal and parietal regions during visual word recognition: an optical topography study. Neuroimage 40, 1340–1349. doi: 10.1016/j.neuroimage.2007.12.037

Homan, R. W., Herman, J., and Purdy, P. (1987). Cerebral location of international 10-20 system electrode placement. Electroencephalogr. Clin. Neurophysiol. 66, 376–382. doi: 10.1016/0013-4694(87)90206-9

Holper, L., and Wolf, M. (2011). Single-trial classiﬁcation of motor imagery diﬀering in task complexity: a functional near-infrared spectroscopy study. J. Neuroeng. Rehabil. 8:34. doi: 10.1186/1743-0003-8-34

Hong, K. S., and Nguyen, H. D. (2014). State-space models of impulse hemodynamic responses over motor, somatosensory, and visual cortices. Biomed. Opt. Express 5, 1778–1798. doi: 10.1364/BOE.5.001778

Hong, K. S., Bhutta, M. R., Liu, X., and Shin, Y. I. (2017). Classiﬁcation of somatosensory cortex activities using fNIRS. Behav Brain Res. 333, 225–234. doi: 10.1016/j.bbr.2017.06.034

Hong, K.-S., and Khan, M. J. (2017). Hybrid-BCI techniques for improved classiﬁcation accuracy and increased number of commands: a review. Front. Neurorobot. 11:35. doi: 10.3389/fnbot.2017.00035

Hong, K. S., Naseer, N., and Kim, Y. H. (2015). Classiﬁcation of prefrontal and motor cortex signals for three-class fNIRS-BCI. Neurosci. Lett. 587, 87–92. doi: 10.1016/j.neulet.2014.12.029

Hong, K. S., and Naseer, N. (2016). Reduction of delay in detecting initial dips from functional near-infrared spectroscopy signals using vector-based phase analysis. Int. J. Neural Syst. 26:1650012 doi: 10.1142/S012906571650012X

Hong, K. S., and Santosa, H. (2016). Decoding four diﬀerent sound-categories in the auditory cortex using functional near-infrared spectroscopy. Hear. Res. 333, 157–166. doi: 10.1016/j.heares.2016.01.009

Hu, X. S., Hong, K. S., Ge, S. S., and Jeong, M. Y. (2010). Kalman estimator-and general linear model-based on-line brain activation mapping by near-infrared spectroscopy. BioMed. Eng. Online 9:82. doi: 10.1186/1475-925X-9-82

- Hu, X. S., Hong, K. S., and Ge, S. S. (2012). fNIRS-based online deception decoding. J. Neural Eng. 9:026012. doi: 10.1088/1741-2560/9/2/026012
- Hu, X. S., Hong, K. S., and Ge, S. S. (2013). Reduction of trial-to-trial variability in functional near-infrared spectroscopy signals by accounting for resting-state functional connectivity. J. Biomed. Opt. 18:017003. doi: 10.1117/1.JBO.18.1.017003

Hunter, R. J., Patterson, M. S., Farrell, T. J., and Hayward, J. E. (2002). Haemoglobin oxygenation of a two-layer tissue-simulating phantom from time-resolved reﬂectance: eﬀect of top layer thickness. Phys. Med. Biol. 47, 193–208. doi: 10.1088/0031-9155/47/2/302

Hwang, H. J., Lim, J. H., Jung, Y. J., Choi, H., Lee, S. W., and Im, C. H. (2012). Development of an SSVEP-based BCI spelling system adopting a QWERTY-style LED keyboard. J. Neurosci. Methods 208, 59–65. doi: 10.1016/j.jneumeth.2012.04.011

Hwang, H.-J., Kim, S., Choi, S., and Im, C.-H. (2013). EEG-based brain-computer interfaces: a thorough literature survey. Int. J. Hum. Comput. Interact. 29, 814–826. doi: 10.1080/10447318.2013.780869

Hwang, H. J., Lim, J. H., Kim, D. W., and Im, C. H. (2014). Evaluation of various mental task combinations for near-infrared spectroscopy-based braincomputer interfaces. J. Biomed. Opt. 19:077005. doi: 10.1117/1.JBO.19.7.077005

Hwang, H. J., Choi, H., Kim, J. Y., Chang, W. D., Kim, D. W., Kim, K., et al. (2016). Toward more intuitive brain-computer interfacing: classiﬁcation of binary covert intentions using functional near-infrared spectroscopy. J. Biomed. Opt. 21:091303. doi: 10.1117/1.JBO.21.9.091303

Ichikawa, H., Kitazono, J., Nagata, K., Manda, A., Shimamura, K., Sakuta, R., et al. (2014). Novel method to classify hemodynamic response obtained using multichannel fNIRS measurements into two groups: exploring the combinations of channels. Front. Hum. Neurosci. 8:480. doi: 10.3389/fnhum.2014.00480

Izzetoglu, K., Ayaz, H., Merzagora, A., Izzetoglu, M., Shewokis, P. A., Bunce, S. C., et al. (2011). The evolution of ﬁeld deployable fNIR spectroscopy from bench to clinical settings. J. Innov. Opt. Health Sci. 4, 239–250. doi: 10.1142/S1793545811001587

Jørgensen, H. S., Reith, J., Nakayama, H., Kammersgaard, L. P., Raaschou, H. O., and Olsen, T. S. (1999). What determines good recovery in patients with the most severe strokes? The Copenhagen stroke study. Stroke 30, 2008–2012. doi: 10.1161/01.STR.30.10.2008

Jurcak, V., Tsuzuki, D., and Dan, I. (2007). 10/20, 10/10, and 10/5 system revisited: their validity as head-surface-based positioning system. Neuroimage 34, 1600–1611. doi: 10.1016/j.neuroimage.2006.09.024

Käthner, I., Kübler, A., and Halder, S. (2015). Comparison of eye tracking, electrooculography and an auditory brain-computer interface for binary communication: a case study with a participant in the locked-in state. J. NeuroEng. Rehabil. 12:76. doi: 10.1186/s12984-0150071-z

Kaiser, V., Bauernfeind, G., Kreilinger, A., Kaufmann, T., Kübler, A., Neuper, C., et al. (2014). Cortical eﬀects of user training in a motor imagery based braincomputer interface measured by fNIRS and EEG. Neuroimage 85, 432–444. doi: 10.1016/j.neuroimage.2013.04.097

Kato, T. (2003). Apparatus for Evaluating Biological Function. Japan, Patent no. WO/2003/068070.

Kawase, T., Sakurada, T., Koike, Y., and Kansaku, K. (2017). A hybrid BMI-based exoskeleton for paresis: EMG control for assisting arm movements. J. Neural Eng. 14:016015. doi: 10.1088/1741-2552/aa525f

Kek, K. J., Kibe, R., Niwayama, M., Kudo, N., and Yamamoto, K. (2008). Optical imaging instrument for muscle oxygenation based on spatially resolved spectroscopy. Opt. Express 16, 18173–18187. doi: 10.1364/OE.16.018173

Kennedy, P. R., and Adams, K. D. (2003). A decision tree for brain-computer interface devices. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 148–150. doi: 10.1109/TNSRE.2003.814420

Khan, M. J., Hong, M. J., and Hong, K. S. (2014). Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface. Front. Hum. Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244

Khan, M. J., and Hong, K. S. (2015). Passive BCI based on drowsiness detection: an fNIRS study. Biomed. Opt. Express 6, 4063–4078. doi: 10.1364/BOE.6.004063

Khan, M. J., and Hong, K.-S. (2017). Hybird EEG-fNIRS-based eight command decoding for BCI: application to quadcopter control. Front. Neurorobotics 11:6. doi: 10.3389/fnbot.2017.00006

Khan, R. A., Naseer, N., Qureshi, N. K., Noori, F. M., Nazeer, H., and Khan, M. U.

(2018). fNIRS-based neurorobotic interface for gait rehabilitation. J. Neuroeng. Rehabil. 15:7. doi: 10.1186/s12984-018-0346-2

Kim, B. H., Kim, M., and Jo, S. (2014). Quadcopter ﬂight control using a low-cost hybrid interface with EEG-based classiﬁcation and eye tracking. Comput. Biol. Med. 51, 82–92. doi: 10.1016/j.compbiomed.2014.04.020

Koo, B., Lee, H. G., Nam, Y., Kang, H., Koh, C. S., Shin, H. C., et al. (2015). A hybrid NIRS-EEG system for self-paced brain computer interface with online motor imagery. J. Neurosci. Methods 244, 26–32. doi: 10.1016/j.jneumeth.2014. 04.016

Kübler, A., Kotchoubey, B., Kaiser, J., Wolpaw, J., and Birbaumer, N. (2001). Brain-computer communication: unlocking the locked-in. Psychol. Bull. 127, 358–375. doi: 10.1037/0033-2909.127.3.358

Kübler, A., Nijboer, F., Mellinger, J., Vaughan, T. M., Pawelzik, H., Schalk, G., et al. (2005). Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface. Neurology 64, 1775–1777. doi: 10.1212/01.WNL.0000158616.43002.6D

Lee, M. H., Fazli, S., Mehnert, J., and Lee, S. W. (2015). Subject-dependent classiﬁcation for robust idle state detection using multi-modal neuroimaging and data-fusion techniques in BCI. Pattern Recognit. 48, 2725–2737. doi: 10.1016/j.patcog.2015.03.010

Leﬀ, D. R., Orihuela-Espina, F., Elwell, C. E., Athanasiou, T., Delpy, D. T., Darzi, A. W., et al. (2011). Assessment of the cerebral cortex during motor task behaviours in adults: A systematic review of functional near infrared spectroscopy (fNIRS) studies. Neuroimage 54, 2922–2936. doi: 10.1016/j.neuroimage.2010.10.058

Li, Y., Pan, J., Wang, F., and Yu, Z. (2013a). A Hybrid BCI system combining P300 and SSVEP and its application to wheelchair control. IEEE Trans. Biomed. Eng 60, 3156–3166. doi: 10.1109/TBME.2013.2270283

Li, J., Liang, J., Zhao, Q., Li, J., Hong, K., and Zhang, L. (2013b). Design of assistive wheelchair system directly steered by human thoughts. Int. J. Neural Syst. 23:

1350013. doi: 10.1142/S0129065713500135

Li, J., Ji, H., Cao, L., Zang, D., Gu, R., Xia, B., et al. (2014). Evaluation and application of a hybrid brain computer interface for real wheelchair parallel control with multi-degree of freedom. Int. J. Neural Syst. 24:1450014. doi: 10.1142/S0129065714500142

Li, R., Potter, T., Huang, W., and Zhang, Y. (2017). Enhancing performance of a hybrid eeg-fnirs system using channel selection and early temporal features. Front. Hum. Neurosci. 11:462. doi: 10.3389/fnhum.2017. 00462

Liu, X., and Hong, K.-S. (2017). Detection of primary RGB colors projected on a screen using fNIRS. J. Innov. Opt. Health Sci. 10:6. doi: 10.1142/S1793545817500067

Lotte, F., Congedo, M., Lécuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces. J. Neural Eng. 4:R1. doi: 10.1088/1741-2560/4/2/R01

Luu, S., and Chau, T. (2009). Decoding subjective preferences from single-trial near-infrared spectroscopy signals. J. Neural Eng. 6:016003. doi: 10.1088/1741-2560/6/1/016003

Matthews, F., Pearlmutter, B. A., Ward, T. E., Soraghan, C., and Markham, C.

(2008). Hemodynamics for brain computer interfaces. IEEE Signal Process. Mag. 25, 87–94. doi: 10.1109/MSP.2008.4408445

- McFarland, D. J., and Wolpaw, J. R. (2010). Brain-computer interfaces for the operation of robotic and prosthetic devices. Adv. Comput. 79, 169–187. doi: 10.1016/S0065-2458(10)79004-5
- McFarland, D. J., and Wolpaw, J. R. (2011). Brain-computer interfaces for communication and control. Commun. ACM 54, 60–66. doi: 10.1145/1941487.1941506

Mihara, M., Miyai, I., Hatakenaka, M., Kubota, K., and Sakoda, S. (2008). Role of the prefrontal cortex in human balance control. Neuroimage, 43, 329–336. doi: 10.1016/j.neuroimage.2008.07.029

Min, B. K., Marzelli, M. J., and Yoo, S. S. (2010). Neuroimaging-based approaches in brain-computer interface. Trends Biotechnol. 28, 552–560. doi: 10.1016/j.tibtech.2010.08.002

Moghimi, S., Kushki, A., Power, S., Guerguerian, A. M., and Chau, T. (2012). Automatic detection of a prefrontal cortical response to emotionally rated music using multi-channel near-infrared spectroscopy. J. Neural Eng. 9:026022, doi: 10.1088/1741-2560/9/2/026022

Moghimi, S., Kushki, A., Guerguerian, A. M., and Chau, T. (2013). A review of EEG-based brain-computer interfaces as access pathways for individuals with severe disabilities. Assist. Technol. 25, 99–10. doi: 10.1080/10400435.2012.723298

Muller-Putz, G., Leeb, R., Tangermann, M., Hohne, J., Kubler, A., Cincotti, F., et al. (2015). Towards noninvasive hybrid brain-computer interfaces: Framework, practice, clinical application, and beyond. Proc. IEEE 103, 926–943. doi: 10.1109/JPROC.2015.2411333

Naito, M., Michioka, Y., Ozawa, K., Ito, Y., Kiguchi, M., and Kanazawa, T. (2007). A communication means for totally locked-in ALS patients based on changes in cerebral blood volume measured with near-infrared light. IEICE Trans. Inf. Syst. E90-D, 1028–1037. doi: 10.1093/ietisy/e90-d.7.1028

Naseer, N., and Hong, K. S. (2013). Classiﬁcation of functional near-infrared spectroscopy signals corresponding to the right- and left-wrist motor imagery for development of a brain-computer interface. Neurosci. Lett. 553, 84–89. doi: 10.1016/j.neulet.2013.08.021

Naseer, N., Hong, M. J., and Hong, K. S. (2014). Online binary decision decoding using functional near-infrared spectroscopy for the development of brain-computer interface. Exp. Brain Res. 232, 555–564. doi: 10.1007/s00221-013-3764-1

Naseer, N., and Hong, K.-S. (2015b). Decoding answers to four-choice questions using functional near infrared spectroscopy. J. Near Infrared Spectrosc. 23, 23–31. doi: 10.1255/jnirs.1145

Naseer, N., and Hong, K.-S. (2015a). fNIRS-based brain-computer interfaces: a review. Front. Hum. Neurosci. 9:3. doi: 10.3389/fnhum.2015.00003

Naseer, N., Noori, F. M., Qureshi, N. K., and Hong, K. S. (2016a). Determining optimal feature-combination for LDA classiﬁcation of functional near-infrared spectroscopy signals in brain-computer interface application. Front. Hum. Neurosci. 10:237. doi: 10.3389/fnhum.2016.00237

Naseer, N., Qureshi, N. K., Noori, F. M., and Hong, K. S. (2016b). Analysis of diﬀerent classiﬁcation techniques for two-class functional near-infrared spectroscopy-based brain-computer interface. Comput. Intell. Neurosci. 2016:5480760. doi: 10.1155/2016/5480760

Nguyen, H. D., and Hong, K. S. (2016). Bundled-optode implementation for 3D imaging in functional near-infrared spectroscopy. Biomed. Opt. Express 7, 3491–3507. doi: 10.1364/BOE.7.003491

Nguyen, H. D., Hong, K. S., and Shin, Y. I. (2016). Bundled-optode method in functional near-infrared spectroscopy. PLoS ONE 11:e0165146. doi: 10.1371/journal.pone.0165146

Noori, F. M., Naseer, N., Qureshi, N. K., Nazeer, H., and Khan, R. A. (2017). Optimal feature selection from fNIRS signals using genetic algorithms for BCI. Neurosci. Lett. 647, 61–66. doi: 10.1016/j.neulet.2017.03.013

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Oka, N., Yoshino, K., Yamamoto, K., Takahashi, H., Li, S., Sugimachi, T., et al. (2015). Greater activity in the frontal cortex on left curves: a vectorbased fnirs study of left and right curve driving. PLoS ONE 10:e0127594. doi: 10.1371/journal.pone.0127594

Olejniczak, P. (2006). Neurophysiologic basis of EEG. J. Clin. Neurophysiol. 23, 186–189. doi: 10.1097/01.wnp.0000220079.61973.6c

Ortiz-Rosario, A., and Adeli, H. (2013). Brain-computer interface technologies: from signal to action. Rev. Neurosci. 24, 537–552. doi: 10.1515/revneuro-2013-0032

Pan, J., Xie, Q., He, Y., Wang, F., Di, H., Laureys, S., et al. (2014). Detecting awareness in patients with disorders of consciousness using a hybrid brain-computer interface. J. Neural Eng. 11:056007. doi: 10.1088/1741-2560/11/5/056007

Power, S. D., Falk, T. H., and Chau, T. (2010). Classiﬁcation of prefrontal activity due to mental arithmetic and music imagery using hidden Markov models and frequency domain near-infrared spectroscopy. J. Neural Eng. 7:026002. doi: 10.1088/1741-2560/7/2/026002

- Power, S. D., Kushki, A., and Chau, T. (2011). Towards a system-paced nearinfrared spectroscopy brain-computer interface: diﬀerentiating prefrontal activity due to mental arithmetic and mental singing from the no-control state. J. Neural Eng. 8:066004. doi: 10.1088/1741-2560/8/6/066004
- Power, S. D., Kushki, A., and Chau, T. (2012a). Intersession consistency of singletrial classiﬁcation of the prefrontal response to mental arithmetic and the nocontrol state by NIRS. PLoS ONE 7:e37791. doi: 10.1371/journal.pone.0037791

Power, S. D., Khushki, A., and Chau, T. (2012b). Automatic single trial discrimination of mental arithmetic, mental singing and the no-control state from the prefrontal activity: towards a three-state NIRS-BCI. BMC Res. Notes 5:141. doi: 10.1186/1756-0500-5-141

Power, S. D., and Chau, T. (2013). Automatic single-trial classiﬁcation of prefrontal hemodynamic activity in an individual with Duchenne muscular dystrophy. Dev. Neurorehabil 16, 67–72. doi: 10.3109/17518423.2012.718293

Putze, F., Hesslinger, S., Tse, C. Y., Huang, Y., Herﬀ, C., Guan, C., et al. (2014). Hybrid fNIRS- EEG based classiﬁcation of auditory and visual perception processes. Front. Neurosci. 8:373. doi: 10.3389/fnins.2014.00373

Qureshi, N. K., Naseer, N., Noori, F. M., Nazeer, H., Khan, R. A., and Saleem, S. (2017). Enhancing classiﬁcation performance of functional near-infrared spectroscopy brain-computer interface using adaptive estimation of general linear model coeﬃcients. Front. Neurorobot. 11:33. doi: 10.3389/fnbot.2017.00033

Ramadan, R. A., and Vasilakos, A. V. (2017). Brain computer interface: control signals review. Neurocomputing 223, 26–44. doi: 10.1016/j.neucom.2016.10.024

Ramli, R., Arof, H., Ibrahim, F., Mokhtar, N., and Idris, M. Y.I. (2015). Using ﬁnite state machine and a hybrid of EEG signal and EOG artefacts for an asynchronous wheelchair navigation. Expert Syst. Appl. 42, 2451–2463. doi: 10.1016/j.eswa.2014.10.052

Robinson, N., Zaidi, A. D., Rana, M., Prasad, V. A., Guan, C., Birbaumer, N., et al. (2016). Real-time subject-independent pattern classiﬁcation of overt and covert movements from fnirs signals. PLoS ONE 11:e0159959. doi: 10.1371/journal.pone.0159959

Safaie, J., Grebe, R., Moghaddam, H. A., and Wallois, F. (2013). Toward a fully integrated wireless wearable EEG-NIRS bimodal acquisition system. J. Neural Eng. 10:056001. doi: 10.1088/1741-2560/10/5/056001

Sagara, K., and Kido, K. (2012). Evaluation of a 2-channel nirs-based optical brain switch for motor disabilities’ communication tools. IEICE Trans. Inf. Syst. E95D, 829–834. doi: 10.1587/transinf.E95.D.829

Sano, M., Sano, S., Oka, N., Yoshino, K., and Kato, T. (2013). Increased oxygen load in the prefrontal cortex from mouth breathing: a vector-based near-infrared spectroscopy study. Neuroreport 24, 935–940. doi: 10.1097/WNR.00000000000 00008

Santosa, H., Hong, M. J., Kim, S. P., and Hong, K. S. (2013). Noise reduction in functional near-infrared spectroscopy signals by independent component analysis. Rev. Sci. Instrum. 84:073106. doi: 10.1063/1.4812785

Santosa, H., Hong, M. J., and Hong, K. S. (2014). Lateralization of music processing auditory cortex: an fNIRS study. Front. Behav. Neurosci. 8:418. doi: 10.3389/fnbeh.2014.00418

Scarpa, F., Brigadoi, S., Cutini, S., Scatturin, P., Zorzi, M., Dell’acqua, R., et al. (2013). A reference-channel based methodology to improve estimation of event-related hemodynamic response from fNIRS measurements. Neuroimage 72, 106–119. doi: 10.1016/j.neuroimage.2013. 01.021

Schroeter, M. L., Zysset, S., Kupka, T., Kruggel, F., and Yves von Cramon, D. (2002). Near-infrared spectroscopy can detect brain activity during a colorword matching Stroop task in an event-related design. Hum. Brain Mapp. 17, 61–71. doi: 10.1002/hbm.10052

- Schudlo, L. C., and Chau, T. (2014). Dynamic topographical pattern classiﬁcation of multichannel prefrontal NIRS signals?: II. Online diﬀerentiation of mental arithmetic and rest. J. Neural. Eng. 11:016003. doi: 10.1088/1741-2560/11/1/016003

Schudlo, L. C., Power, S. D., and Chau, T. (2013). Dynamic topographical pattern classiﬁcation of multichannel prefrontal NIRS signals. J. Neural Eng. 10:046018. doi: 10.1088/1741-2560/10/4/046018

C Schudlo, L., and Chau, T. (2015a). Towards a ternary NIRS-BCI: single-trial classiﬁcation of verbal ﬂuency task, Stroop task and unconstrained rest. J. Neural Eng. 12:066008. doi: 10.1088/1741-2560/12/6/066008

- Schudlo, L. C., and Chau, T. (2015b). Single-trial classiﬁcation of near-infrared spectroscopy signals arising from multiple cortical regions. Behav. Brain Res. 290, 131–142. doi: 10.1016/j.bbr.2015.04.053

Shin, J., and Jeong, J. (2014). Multiclass classiﬁcation of hemodynamic responses for performance improvement of functional near-infrared spectroscopy-based brain-computer interface. J. Biomed. Opt. 19:067009. doi: 10.1117/1.JBO.19.6.067009

Shan, Z. Y., Wright, M. J., Thompson, P. M., Mcmahon, K. L., Blokland, G. G., de Zubicaray, G. I., et al. (2014). Modeling of the hemodynamic responses in block design fMRI studies. J. Cereb. Blood Flow Metab. 34, 316–324. doi: 10.1038/jcbfm.2013.200

Shin, J., Müller, K. R., Schmitz, C. H., Kim, D. W., and Hwang, H. J. (2017). Evaluation of a compact hybrid brain-computer interface system. Biomed Res. Int. 2017:6820482. doi: 10.1155/2017/6820482

Sitaram, R., Zhang, H., Guan, C., Thulasidas, M., Hoshi, Y., Ishikawa, A., et al. (2007). Temporal classiﬁcation of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain-computer interface. Neuroimage 34, 1416–1427. doi: 10.1016/j.neuroimage.2006.11.005

Smith, E., and Delargy, M. (2005). Locked-in syndrome. BMJ, 330, 406–409. doi: 10.1136/bmj.330.7488.406

Sood, M., Besson, P., Muthalib, M., Jindal, U., Perrey, S., Dutta, A., et al. (2016). NIRS-EEG joint imaging during transcranial direct current stimulation: Online parameter estimation with an autoregressive model. J. Neurosci. Methods 274, 71–80. doi: 10.1016/j.jneumeth.2016.09.008

Stangl, M., Bauernfeind, G., Kurzmann, J., Scherer, R., and Neuper, C. (2013). A haemodynamic brain-computer interface based on real-time classiﬁcation of near infrared spectroscopy signals during motor imagery and mental arithmetic. J. Near Infrared Spectrosc. 21, 157–171. doi: 10.1255/jnirs.1048

Tai, K., and Chau, T. (2009). Single-trial classiﬁcation of NIRS signals during emotional induction tasks: towards a corporeal machine interface. J. Neuroeng. Rehabil. 6, 1–14. doi: 10.1186/1743-0003-6-39

Tanaka, K., Matsunaga, K., and Wang, H. O. (2005). Electroencephalogrambased control of an electric wheelchair. IEEE Trans. Robot. 21, 762–766. doi: 10.1109/TRO.2004.842350

Tanaka, H., and Katura, T. (2011). Classiﬁcation of change detection and change blindness from near-infrared spectroscopy signals. J. Biomed. Opt. 16:087001. doi: 10.1117/1.3606494

Tomita, Y., Vialatte, F. B., Dreyfus, G., Mitsukura, Y., Bakardjian, H., and Cichocki, A. (2014). Bimodal BCI using simultaneously NIRS and EEG. IEEE Trans. Biomed. Eng 61, 1274–1284. doi: 10.1109/TBME.2014.2300492

Trakoolwilaiwan, T., Behboodi, B., Lee, J., Kim, K., and Choi, J. W. (2017). Convolutional neural network for high-accuracy functional near-infrared spectroscopy in a brain–computer interface: three-class classiﬁcation of rest, right-, and left-hand motor execution. Neurophotonics 5:1. doi: 10.1117/1.NPh.5.1.011008

Trejo, L. J., Rosipal, R., and Matthews, B. (2006). Brain-computer interfaces for 1-D and 2-D cursor control: Designs using volitional control of the EEG spectrum or steady-state visual evoked potentials. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 225–229. doi: 10.1109/TNSRE.2006.875578

Tsui, C. S., Gan, J. Q., and Hu, H. (2011). A self-paced motor imagery based brain-computer interface for robotic wheelchair control. Clin. EEG Neurosci. 42, 225–229. doi: 10.1177/155005941104200407

Turnip, A., Hong, K. S., and Jeong, M. Y. (2011). Real-time feature extraction of P300 component using adaptive nonlinear principal component analysis. Biomed. Eng. Online 10:83. doi: 10.1186/1475-925X-10-83

Turnip, A., and Hong, K.-S. (2012). Classifying mental activities from EEG-P300 signals using adaptive neural networks. Int. J. Innov. Comp. Inf. Control 8, 6429–6443.

Verner, M., Herrmann, M. J., Troche, S. J., Robers, C. M., and Rammsyaer, T. H. (2013). Cortical oxygen consumption in mental arithmetic as a function task diﬃculty: a near-infrared spectroscopy approach. Front. Hum. Neurosci. 7:217. doi: 10.3389/fnhum.2013.0 0217

Visani, E., Canafoglia, L., Gilioli, I., Sebastiano, D. R., Contarino, V. E., Duran, D., et al. (2015). Hemodynamic and EEG time-courses during unilateral hand movement in patients with cortical myoclonus. An EEG-fMRI and EEG-TD-fNIRS study. Brain Topogr. 28, 915–925. doi: 10.1007/s10548-0140402-6

Wang, D., Miao, D., and Blohm, G. (2012). Multi-class motor imagery EEG decoding for brain-computer interfaces. Front. Neurosci. 6:151. doi: 10.3389/fnins.2012.00151

Wang, H., Li, Y., Long, J., Yu, T., and Gu, Z. (2014). An asynchronous wheelchair control by hybrid EEG-EOG brain-computer interface. Cogn. Neurodyn. 8, 399–409. doi: 10.1007/s11571-014-9296-y

Wang, H., Zhang, Y., Waytowich, N. R., Krusienski, D. J., Zhou, G. X., Jin, J., et al. (2016). Discriminative feature extraction via multivariate linear regression for SSVEP-Based BCI. IEEE Trans. Neural Syst. Rehabil. Eng. 24, 532–541. doi: 10.1109/TNSRE.2016.2519350

Watanabe, K., Tanaka, H., Takahashi, K., Niimura, Y., Watanabe, K., and Kurihara, Y. (2016). NIRS-based language learning BCI system. IEEE Sens. J. 16, 2726–2734. doi: 10.1109/JSEN.2016.2519886

Weyand, S., and Chau, T. (2015). Correlates of near-infrared spectroscopy brain-computer interface accuracy in a multi-class personalization framework. Front. Hum. Neurosci. 9:536. doi: 10.3389/fnhum.2015. 00536

- Weyand, S., Takehara-Nishiuchi, K., and Chau, T. (2015a). Weaning oﬀ mental tasks to achieve voluntary self-regulatory control of a near-infrared spectroscopy brain-computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 23, 548–561. doi: 10.1109/TNSRE.2015.2399392
- Weyand, S., Takehara-Nishiuchi, K., and Chau, T. (2015b). Exploring methodological frameworks for a mental task-based near-infrared spectroscopy brain-computer interface. J. Neurosci. Methods 254, 36–45. doi: 10.1016/j.jneumeth.2015.07.007

Ye, J. C., Tak, S., Jang, K. E., Jung, J., and Jang, J. (2009). NIRS-SPM: statistical parametric mapping for near-infrared spectroscopy. Neuroimage 44, 428–447. doi: 10.1016/j.neuroimage.2008.08.036

- Yin, X., Xu, B., Jiang, C., Fu, Y., Wang, Z., Li, H., et al. (2015a). Classiﬁcation of hemodynamic responses associated with force and speed imagery for a brain-computer interface. J. Med. Syst. 39:53. doi: 10.1007/s10916-015-0236-0
- Yin, X., Xu, B., Jiang, C., Fu, Y., Wang, Z., Li, H., et al. (2015b). A hybrid BCI based on EEG and fNIRS signals improves the performance of decoding motor

imagery of both force and speed of hand clenching. J. Neural Eng. 12:036004. doi: 10.1088/1741-2560/12/3/036004

Yoshino, K., and Kato, T. (2012). Vector-based phase classiﬁcation of initial dips during word listening using near-infrared spectroscopy. Neuroreport 23, 947–951. doi: 10.1097/WNR.0b013e328359833b

Yoshino, K., Oka, N., Yamamoto, K., Takahashi, H., and Kato, T. (2013). Functional brain imaging using near-infrared spectroscopy during actual driving on an expressway. Front. Hum. Neurosci. 7:882. doi: 10.3389/fnhum.2013.00882

Zafar, A., and Hong, K. S. (2017). Detection and classiﬁcation of three class initial dips from prefrontal cortex. Biomed. Opt. Express 8, 367–383. doi: 10.1364/BOE.8.000367

Zander, T. O., and Kothe, C. (2011). Towards passive brain-computer interfaces: applying brain-computer interface technology to human-machine systems in general. J. Neural Eng. 8:025005. doi: 10.1088/1741-2560/8/2/025005

Zhang, Y., Zhou, G., Jin, J., Wang, M. J., Wang, X., and Cichocki, A. (2013). L1-Regularized multiway canonical correlation analysis for SSVEP-based BCI. IEEE Trans. Neural Syst. Rehabil. Eng. 21, 887–896. doi: 10.1109/TNSRE.2013.2279680

Zhang, Y., Zhou, G., Jin, J., Wang, X., and Cichocki, A. (2014). Frequency recognition in SSVEP-based BCI using multiset canonical correlation analysis. Int. J. Neural Syst. 24:1450013. doi: 10.1142/S0129065714500130

- Zhang, R., Li, Y., Yan, Y., Zhang, H., Wu, S., Yu, T., et al. (2016). Control of a wheelchair in an indoor environment based on a brain-computer interface and automated navigation. IEEE Trans. Neural Syst. Rehabil. Eng. 24, 128–139. doi: 10.1109/TNSRE.2015.2439298
- Zhang, S., Zheng, Y., Wang, D., Wang, L., Ma, J., Zhang, J., et al. (2017). Application of a common spatial pattern-based algorithm for an fNIRSbased motor imagery brain-computer interface. Neurosci. Lett. 655, 35–40. doi: 10.1016/j.neulet.2017.06.044

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

The reviewer NN declared a past co-authorship with one of the authors K-SH to the handling Editor.

Copyright © 2018 Hong, Khan and Hong. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

