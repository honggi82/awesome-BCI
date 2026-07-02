##### REVIEW ARTICLE

published: 28 January 2015 doi: 10.3389/fnhum.2015.00003

## HUMAN NEUROSCIENCE

# fNIRS-based brain-computer interfaces: a review

### Noman Naseer1 and Keum-Shik Hong1,2*

- 1 Department of Cogno-Mechatronics Engineering, Pusan National University, Busan, Republic of Korea
- 2 School of Mechanical Engineering, Pusan National University, Busan, Republic of Korea

Edited by: Arthur M. Jacobs, Freie Universität Berlin, Germany

Reviewed by: Martin J. Herrmann, Universtity of Würzburg, Germany Vadim Nikulin, Charite University Hospital, Germany

*Correspondence: Keum-Shik Hong, Department of Cogno-Mechatronics Engineering, Pusan National University, 2 Busandaehak-ro, Guemjeong-gu, Busan 609-735, Republic of Korea e-mail: kshong@pusan.ac.kr

A brain-computer interface (BCI) is a communication system that allows the use of brain activity to control computers or other external devices. It can, by bypassing the peripheral nervous system, provide a means of communication for people suffering from severe motor disabilities or in a persistent vegetative state. In this paper, brain-signal generation tasks, noise removal methods, feature extraction/selection schemes, and classiﬁcation techniques for fNIRS-based BCI are reviewed. The most common brain areas for fNIRS BCI are the primary motor cortex and the prefrontal cortex. In relation to the motor cortex, motor imagery tasks were preferred to motor execution tasks since possible proprioceptive feedback could be avoided. In relation to the prefrontal cortex, fNIRS showed a signiﬁcant advantage due to no hair in detecting the cognitive tasks like mental arithmetic, music imagery, emotion induction, etc. In removing physiological noise in fNIRS data, band-pass ﬁltering was mostly used. However, more advanced techniques like adaptive ﬁltering, independent component analysis (ICA), multi optodes arrangement, etc. are being pursued to overcome the problem that a band-pass ﬁlter cannot be used when both brain and physiological signals occur within a close band. In extracting features related to the desired brain signal, the mean, variance, peak value, slope, skewness, and kurtosis of the noised-removed hemodynamic response were used. For classiﬁcation, the linear discriminant analysis method provided simple but good performance among others: support vector machine (SVM), hidden Markov model (HMM), artiﬁcial neural network, etc. fNIRS will be more widely used to monitor the occurrence of neuro-plasticity after neuro-rehabilitation and neuro-stimulation. Technical breakthroughs in the future are expected via bundled-type probes, hybrid EEG-fNIRS BCI, and through the detection of initial dips.

Keywords: brain-computer interface, functional near-infrared spectroscopy (fNIRS), feature extraction, feature classiﬁcation, physiological noise, brain-machine interface

### INTRODUCTION

A brain-computer interface (BCI) system provides its users with control channels that are independent of the brain’s output channels (i.e., the peripheral nervous system and muscles) (Wolpaw et al., 2002). Such systems can be used as a means for communications and restoration of motor functions (through a neuroprosthesis) for people with motor disorders such as amyotrophic lateral sclerosis (ALS) and spinal cord injury, and/or people in the persistent locked-in state (LIS). It can also be used as a neurorehabilitation tool to improve motor and/or cognitive performance of such people.

A typical BCI system consists of ﬁve stages (see Figure 1): brain-signal acquisition, preprocessing, feature extraction/selection, classiﬁcation, and application interface. In the ﬁrst brain-signal acquisition stage, suitable signals are acquired using an appropriate brain-imaging modality. Since the acquired signals are normally weak and contain noises (physiological and instrumental) and artifacts, preprocessing is needed, which is the second stage. In the third stage, some useful data so called “features” are extracted. These features, in the fourth stage, are classiﬁed using a suitable classiﬁer. Finally, in the ﬁfth

stage, the classiﬁed signals are transmitted to a computer or other external devices for generating the desired control commands to the devices. In neurofeedback applications, a real-time display of brain activity is desirable, which enables self-regulation of brain functions. Figure 1 depicts a schematic of (hybrid) functional near-infrared spectroscopy (fNIRS) and electroencephalography (EEG) BCI.

Several modalities have been used for brain signal acquisition, which include EEG (Wolpaw et al., 2002; Turnip et al., 2011; Turnip and Hong, 2012; Wang et al., 2012; Hwang et al., 2013; Kleih and Kubler, 2013; Ko and Sim, 2013; Hammer et al., 2014; Kim et al., 2014; Soekadar et al., 2014), magnetoencephalography (MEG) (Mellinger et al., 2007; Buch et al., 2008; Sardouie and Shamsollahi, 2012), functional magnetic resonance imaging (fMRI) (Weiskopf et al., 2004; LaConte, 2011; van der Heiden et al., 2014), and fNIRS (Ferrari et al., 1985, 2004; Kato et al., 1993; Hu et al., 2013; Bhutta et al., 2014; Rea et al., 2014; Santosa et al., 2014). Among them, fNIRS is relatively new, which uses near-infrared-range light (usually of 650∼1000nm wavelength) to measure the concentration changes of oxygenated hemoglobin (HbO) and deoxygenated hemoglobin (HbR) (Villringer et al.,

|[Figure 1]<br><br>FIGURE 1 | Schematic of a hybrid fNIRS-EEG BCI.|
|---|

1993; Hoshi et al., 1994; Hoshi and Tamura, 1997; Villringer and Chance, 1997; Boas et al., 2004a,b; Hong and Nguyen, 2014). Its main advantages are relatively low cost, portability, safety, low noise (compared to fMRI), and easiness to use. Unlike EEG and MEG, its data are not much susceptible to electrical noise, since it is an optical imaging modality. fNIRS measures the blood ﬂow changes in the local capillary network caused by neuron ﬁrings. Since the hemoglobin is an oxygen carrier, the changes of HbO and HbR concentration levels after a neuronal activation can be related to the relevant neuronal ﬁrings. fNIRS uses near-infrared (NI) light emitter-detector pairs operating with two or more wavelengths. The NI light emitted into the scalp diffuses through the brain tissues resulting in multiple scattering of photons. Some of these photons exit the head after passing through the cortical region of the brain, wherein the chromophores (i.e., HbO and HbR) are changing in time. These exited photons are then detected by using strategically positioned detectors. Since HbO and HbR have different absorption coefﬁcients for different wavelengths of NI light, the relationship between the exiting-photon intensity and the incident-photon intensity can be used to calculate the changes of the concentrations of HbO and HbR [ cHbO(t) and cHbR(t)] along the path of the photons by applying the modiﬁed Beer-Lamberts law (Delpy et al., 1988).

The principle of fNIRS measurement, ﬁrst reported by Jobsis (1977), has been applied to the study of cerebral hemodynamics for more than two decades, even though its BCI use is only a few years old. The ﬁrst study who demonstrated the feasibility of fNIRS for BCI was Coyle et al. (2004). They asked the subjects to perform motor imagery of continuous squeezing and releasing of a soft ball. Based on the activity threshold of cHbO(t), they determined whether the brain was activated or at rest.

In 2007, three studies demonstrated the feasibility of controlling the output of fNIRS BCI: Coyle et al. (2007) used a custom-built fNIRS system (named Mindswitch) to test on-off control. Their protocol consisted of two options alternately presented to the subjects: When a desired option was highlighted, the subject performed motor imagery of squeezing and releasing a soft ball to enhance the HbO signals in the motor cortex and, in this way, expressed their choice mentally. The signals during motor imagery were classiﬁed against those during the rest period with an average accuracy of more than 80%. Sitaram et al. (2007) showed that fNIRS signal patterns during execution movement and imagery were distinguishable with the accuracy of 80% (or above) using support vector machines (SVM) and hidden Markov model (HMM). On the other hand, the ﬁrst investigation on ALS patients was done by Naito et al. (2007): Forty ALS patients (17 of them were totally locked-in) were asked to encode their response

the head and the paths traveled by light to reach two detectors are shown in Figure 2. A suitable number of emitter/detector pairs for adequate extraction of neuronal activity vary depending on the type of brain signals that are used for BCI purpose. For the prefrontal cortex, 3 emitters and 8 detectors may be enough to adequately acquire most brain signals corresponding to prefrontal tasks (Luu and Chau, 2009; Power et al., 2010, 2011, 2012a,b; Khan et al., 2014; Naseer et al., 2014). For brain activities corresponding to motor cortex tasks, 6 emitters and 6 detectors can cover the entire motor cortex. In the previous studies, 4 emitters and 4 detectors (Sitaram et al., 2007), 6 emitters and 6 detectors (Naseer and Hong, 2013), and 5 emitters and 4 detectors have been applied to acquire motor-cortex activities.

to several questions as “yes” or “no.” They were requested to respond “yes” by performing mental calculation, music imagery and other such tasks, and to respond “no” by remaining relaxed. The instantaneous amplitude and phase of the light-intensity signals were then used as the features for a quadratic discriminant analysis classiﬁer, which successfully decoded the responses of 70% of the ALS patients who were not totally locked-in. However, for totally locked-in ALS patients, the method worked only 40% of subjects (with the classiﬁcation accuracy of about 80%).

- In 2008, Utsugi et al. (2008) showed the feasibly of a “Go-Stop” control. They measured the spatiotemporal averages of cHbO(t) and cHbR(t) arising from mental calculations. Bauernfeind et al. (2008) developed an fNIRS system and reported that changes in cHbO(t) and cHbR(t) were observed during mental arithmetic tasks over the prefrontal cortex. The measured signals were relatively stable across 13 subjects. Based on that, the authors suggested its application to BCI.
- In 2009, Luu and Chau (2009) demonstrated the preferencedecoding possibilities using fNIRS signals acquired from the prefrontal cortex. Nine subjects were asked to mentally evaluate two presented drinks and decide which one they preferred. Instead of using a speciﬁc activity to choose the preferred drink, they used the direct neural correlates in decision making. The accuracy of this preference decoding, using light-intensity signals directly and linear discriminant analysis (LDA), was around 80%. In the same year, Tai and Chau (2009) showed the feasibility for BCI development of fNIRS-signal classiﬁcation from emotion-induction tasks. The subjects preformed several trials of positive- and negative-emotion-induction tasks, and the optimal features were selected using a genetic algorithm. Then, LDA and SVM were used to classify different sets of features to the average accuracies ranging from 75 to 94%. Since 2009, several studies have successfully demonstrated the use of fNIRS for efﬁcient BCI. Although EEG-based BCIs are most common noninvasive versions, the trend of using fNIRS for BCI is continuously increasing.

#### MOTOR CORTEX ACTIVITIES

Activities from the primary motor cortex are a good choice for fNIRS-BCI application, as they are natural means of providing BCI control over external devices. Moreover, these might also be useful from the perspective of neurorehabilitation. The two most commonly acquired activities from the motor cortex are motor execution and motor imagery.

Motor execution

The motor execution task stands for moving a body part to activate the motor cortex, which involves the development of muscular tensions through muscular actions. Since motor execution involves contraction of muscles, motor execution-based BCIs are affected by proprioceptive feedback from contracting muscles and, therefore, the neuronal modulation may not be solely from the central nervous system. Several motor execution tasks including ﬁnger tapping (Cui et al., 2010a,b; Seo et al., 2012), hand tapping (Hai et al., 2013; Khan et al., 2014), arm lifting (Shin and

|[Figure 2]<br><br>FIGURE 2 | Example of emitter-detector pairs showing the banana-shaped paths of light.|
|---|

### BRAIN-SIGNAL ACQUISITION

BCI uses brain signals to collect information on the user’s intensions. The ﬁrst step in developing an fNIRS-BCI system is to acquire suitable brain signals. The two most common brain areas are the primary motor cortex and the prefrontal cortex. Signals corresponding to motor execution and motor imagery tasks are acquired from the motor cortex; whereas those corresponding to mental arithmetic, mental counting, music imagery, landscape imagery, etc. are acquired from the prefrontal cortex. Although several different emitter-detector conﬁgurations have been used in these two areas, the emitter-detector distance is usually kept within a speciﬁc range, as it plays an important role in fNIRS measurement. For example, an increase in emitter-detector distance corresponds to an increase in imaging depth (McCormick et al., 1992). To measure hemodynamic response signals from the cortical areas, an emitter-detector separation of around 3cm was suggested (Gagnon et al., 2012). A separation of less than 1cm might contain only skin-layer contribution, whereas that of more than 5cm might result in weak and therefore unusable signals (Gratton et al., 2006). A typical emitter-detector conﬁguration on

Jeong, 2014), knee extension (Shin and Jeong, 2014) and hand grasping/gripping (Nagaoka et al., 2010; Fazli et al., 2012) have been used in the previous studies.

Motor imagery

Motor imagery can be deﬁned as a covert cognitive process of kinesthetic imagining of the movement of one’s own body part without the involvement of muscular tension, contraction or ﬂexion. Since the primary objective of BCI is to form a communication pathway for motor-disabled people, motor imagery is one of the most commonly utilized tasks in fNIRS-BCI. The motor imagery tasks include imagination of the squeezing of a soft ball (Coyle et al., 2004, 2007; Stangl et al., 2013), covert imagery of a simple or complex sequence of ﬁnger tapping (Sitaram et al.,

- 2007; Holper and Wolf, 2011), imagination of feet tapping (Kaiser

- et al., 2014), imagination of hand grasping/gripping (Nagaoka et al., 2010; Fazli et al., 2012; Kaiser et al., 2014), imagination of wrist ﬂexion (Naseer and Hong, 2013), imagination of ﬂexion and extension of elbow (Mihara et al., 2013), and folding and unfolding of speciﬁc ﬁngers (Mihara et al., 2013). Unlike motor execution tasks, the motor imagery signals are free of proprioceptive feedback.

PREFRONTAL CORTEX ACTIVITIES

The activities in the prefrontal cortex are also a good choice for fNIRS-BCI, because they involve less motion artifacts and signal attenuation due to the slippage in hairs. Also, they are likely to be more effective in the case of motor-function related disability. Given these advantages, most studies have used the prefrontal activities showing promising results (Naito et al., 2007; Bauernfeind et al., 2008, 2011; Utsugi et al., 2008; Luu and Chau, 2009; Power et al., 2010, 2011, 2012a,b; Abibullaev et al.,

- 2011; Falk et al., 2011; Tanaka and Katura, 2011; Abibullaev and An, 2012; Adhika et al., 2012; Chan et al., 2012; Hu et al.,
- 2012; Moghimi et al., 2012; Sagara and Kido, 2012; Faress and Chau, 2013; Power and Chau, 2013; Stangl et al., 2013; Hwang et al., 2014; Naseer et al., 2014; Schudlo and Chau, 2014; Hong

- et al., 2015). Some of the commonly used prefrontal activities for fNIRS-BCI are mental arithmetic, music imagery, mental counting, and landscape imagery.

Mental arithmetic

Mental arithmetic (sometimes called mental calculation) means performing covert calculation using the brain without any help in the form of paper, pen, calculator, computer, etc. It activates the prefrontal cortex. Since it does not involve any body movement, it is widely used for fNIRS-BCI. A number of studies have successfully demonstrated its feasibility as a mental task for BCI (Naito et al., 2007; Bauernfeind et al., 2008, 2011; Utsugi et al.,

- 2008; Power et al., 2010, 2011, 2012a,b; Adhika et al., 2012; Sagara and Kido, 2012; Power and Chau, 2013; Stangl et al., 2013; Hwang et al., 2014; Naseer et al., 2014; Hong et al., 2015). Mental arithmetic entails mental multiplication (Hwang et al., 2014) or other arithmetic tasks. However, the most commonly utilized mental arithmetic is backwards subtraction, which involves subtraction of a small number (for example, a two-digit number) from a large number (for example, a three-digit number) with successive subtraction of a randomly appearing small number from the result

of the previous subtraction (e.g., 450-15, 435-10, 425-19, etc.) (Power et al., 2010; Hwang et al., 2014; Naseer et al., 2014).

Music imagery

Music imagery (also called mental singing) consists of organizing and analyzing music in the brain without any external auditory stimulus. Naito et al. (2007), Power et al. (2010), Falk et al. (2011), Power et al. (2011), Chan et al. (2012) and Hwang et al. (2014) successfully demonstrated music imagery as a brain activity that can be effectively used for fNIRS-BCI.

Other prefrontal activities

Besides mental arithmetic and music imagery, various other tasks in the prefrontal cortex have been shown to work well. These include mental counting (Naito et al., 2007; Khan et al., 2014), landscape imagery (Naito et al., 2007), mental character writing (Hwang et al., 2014), object rotation (Abibullaev et al., 2011; Abibullaev and An, 2012; Faress and Chau, 2013; Hwang et al., 2014), change-detection tasks (Tanaka and Katura, 2011), labyrinth tasks (Misawa et al., 2012), and emotion-induction tasks (Tai and Chau, 2009; Moghimi et al., 2012). Some studies have demonstrated direct decoding of neural correlates corresponding to subjective preferences (Luu and Chau, 2009), deception (Hu et al., 2012), visual stimuli (Faress and Chau, 2013), and others (Ayaz et al., 2009, 2012).

The best selection of optimal mental activities for the improvement of classiﬁcation accuracy remains an open question. Hwang et al. (2014) evaluated the use of a variety of mental task combinations for BCI. These tasks included motor imagery (right- and left-hand imagery and foot imagery), mental singing, mental arithmetic (multiplication and subtraction), mental rotation, and mental character writing. Out of the 28 different combinations tested, the mental arithmetic/mental rotation and mental arithmetic/right-hand motor imagery combinations yielded the best LDA classiﬁcation results using mean hemoglobin concentration values. Prefrontal activities have been used in more than half of fNIRS-BCI studies, owing primarily to the easy application of fNIRS to the prefrontal area. Activity selection, however, depends on the given fNIRS-BCI application. For example, for the purposes of limb neurorehabilitation, it is desirable to use motor cortex activities.

### PREPROCESSING

The acquired fNIRS signals can contain various noises, which can be categorized into instrumental noise, experimental error, and physiological noise. Since the instrumental noise and experimental error are not related to the brain activities, it is better to remove them prior to converting the raw optical density signals to the concentration changes of HbO and HbR through the modiﬁed Beer-Lambert law (Huppert et al., 2009).

#### REMOVAL OF INSTRUMENTAL NOISE

Instrumental noise is the noise of fNIRS signals present in hardware or caused by the surrounding environment (i.e., instrumental degradation is an example). It usually involves (constant) high frequencies. Such high frequency can be easily removed by a low-pass ﬁlter (for instance, 3∼5Hz of cutoff frequency).

Furthermore, by minimizing the variation of the external light, instrument noise can be signiﬁcantly reduced.

#### REMOVAL OF EXPERIMENTAL ERRORS

Experimental errors include motion artifacts like head motions, which causes the movement of optodes from the assigned positions. This can cause a sudden change in the light intensity resulting in a spike-like noise. Several methods for motion-artifact correction have been proposed in the literature; the Wiener ﬁltering-based method (Izzetoglu et al., 2005), eigenvector-based spatial ﬁltering (i.e., principle component analysis (PCA)-based ﬁltering) (Zhang et al., 2005), wavelet-analysis-based methods (Sato et al., 2006; Power et al., 2010), Savitzky-Golay type ﬁlters (Hai et al., 2013; Shin and Jeong, 2014), and others (Cui et al., 2010a,b; Fekete et al., 2011; Cooper et al., 2012). Please see Cooper et al. (2012) for thorough comparison of various techniques.

### PHYSIOLOGICAL NOISE

Physiological noises include those due to heartbeat (1∼1.5Hz), respiration (0.2∼0.5Hz), Mayer waves (∼0.1Hz), which are related to blood pressure ﬂuctuations (Boas et al., 2004a,b; Zhang et al., 2005; Franceschini et al., 2006; Huppert et al., 2009). Several methods including band-pass ﬁltering, adaptive ﬁltering, PCA, and independent component analysis (ICA) have been used to remove them.

#### BAND-PASS FILTERING

Since the frequency ranges of aforementioned physiological signals are usually known, a band-pass ﬁlter can be an effective means. Some fNIRS-BCI studies have shown promising results using a simple low-pass, or a high-pass, or a band-pass ﬁltering to remove physiological noises (Coyle et al., 2004, 2007; Naito et al., 2007; Sitaram et al., 2007; Bauernfeind et al., 2008; Luu and Chau,

- 2009; Power et al., 2010, 2011; Hu et al., 2012; Liu et al., 2013; Hong et al., 2015).

Various cut-off frequencies for band-pass ﬁltering have been reported in the literature: For example, Luu and Chau (2009), Power et al. (2011), Hu et al. (2012) and Tomita et al. (2014) have used the frequency bands of 0.01∼0.8Hz, 0.1∼0.5Hz, 0.01∼0.2Hz, and 0.1∼0.5Hz, respectively. In general, the band of 0.1∼0.4Hz can effectively remove a large portion of physiological noises including heartbeat and Mayer waves without eliminating the fNIRS signal elicited by a task of 10s period. The types of band-pass ﬁltering include Butterworth ﬁlters (Luu and Chau, 2009; Naseer and Hong, 2013; Naseer et al., 2014), elliptic ﬁlters (Hu et al., 2012), and Chebyshev ﬁlters (Sitaram et al., 2007; Power et al., 2012b). However, no absolute advantage of a particular ﬁltering method over others has been reported yet.

ADVANCED FILTERING METHODS

Band-pass ﬁltering cannot be used to ﬁlter physiological noises whose frequencies overlap with the band of the hemodynamic response signal, for example, due to respiration. Therefore, other methods, such as adaptive ﬁltering (Zhang et al., 2007; Hu et al.,

- 2010; Aqil et al., 2012a,b; Kamran and Hong, 2013, 2014), PCA (Zhang et al., 2005), and ICA (Kohno et al., 2007; Santosa et al., 2013), have also been used to remove physiological noise. To

account for physiological noises, additional noise-related elements can be added into the regression model. In addition to modeling the canonical functional response, a series with adaptive amplitudes and phase components in order to model speciﬁc physiological noise contribution from heartbeat, respiration, and blood pressure can be included. The auto-regressive moving average with exogenous signals (ARMAX) model-based approach incorporating physiological signals as exogenous signals can be used to predict the brain state during a particular cognitive task. The fNIRS signal at each channel can be regarded as an output from a linear combination of various components. The components include the dynamical characteristics of the HbO and HbR changes in a speciﬁc brain region (the inﬂuence from the current/previous stimuli), the physiological signals, the baseline ﬂuctuation, and other noises.

#### ICA AND PCA

ICA can separate physiological noises from the mixed signals allowing the restoration of the original hemodynamic signals. The independent components (ICs) associated with the physiological signals can be identiﬁed by their spectral densities. Isolating the main IC associated with the original hemodynamic response results in a physiological-noise-free signal. Hu et al. (2011) and Santosa et al. (2013) used ICA to separate physiological noise from the original signals. Then, the original hemodynamic response was reconstructed using all the ICs (with weights derived from their t-values) as well as the primary IC. They applied the proposed method to a mental arithmetic task and compared the results with those of the conventional low-pass ﬁltering method, revealing that the ICA method outperformed the low-pass ﬁltering method. Funane et al. (2014) used ICA to evaluate signal contributions from the shallow and deep tissue layers using multi-distance optodes. They assumed that the optical path length in the shallow layer did not change, but it increased linearly with the increase of emitter-detector distance. The reconstructions of the deep and shallow layer signals were performed by summing all the ICs that had been weighted by the deep and shallow contribution ratio in accordance with the emitter-detector distance.

PCA can be used to remove physiological noises (similarly to the case of motion-artifact removal), because systematic ﬂuctuations are covariant among fNIRS measurements from different channels. Reducing such covariance, accordingly, ﬁlters systematic physiological noises from the signals. However, the performance of PCA is greatly dependent on the number of channels and the number of eigenvectors to be removed (Cooper et al., 2012) and, therefore, PCA is not suggested for physiological noise removal when the number of channels is small. Furthermore, a real-time application of ICA for physiological noise removal is still under investigation (a moving window approach for computing ICs can be explored). Henceforth, due to the non-realtimeness of the ICA approach, band-pass ﬁltering techniques are still dominant (Mihara et al., 2012, 2013; Kober et al., 2014).

The fNIRS signals are also affected by the skin blood ﬂow and other contributions from the superﬁcial tissues (Kohno et al., 2007; Takahashi et al., 2011; Kirilina et al., 2012, 2013; Sato

et al., 2013). It has been shown that the removal of these artifacts from cerebral signals is possible by employing several different methods: the use of additional short-distance detector(s) (Saager and Berger, 2005; Luu and Chau, 2009; Saager et al., 2011), adaptive ﬁltering (Zhang et al., 2009), statistical parametric mapping (SPM) in which the artifacts are included as regressors into the model (Tachtsidis et al., 2010), and ICA (Kohno et al., 2007; Funane et al., 2014). Kohno et al. (2007) revealed that the spatial distribution of one of the ICs was directly related to the skin blood ﬂow, which was again veriﬁed by a laser Doppler tissue blood ﬂow meter. Funane et al. (2014), on the other hand, used ICA to separate the absorption changes in deep and shallow tissues (due to the scalp and the skin) using multiple emitterdetector distances. Zhang et al. (2007, 2009) used an adaptive ﬁlter to estimate the global interference in the signals measured from short emitter-detector separations. This global interference was then removed from the target signals measured from long emitter detector separations.

### FEATURE EXTRACTION/SELECTION

After data preprocessing, the different brain activities are classiﬁed on the basis of certain features. In fNIRS-BCI, although some features are extracted directly from detected light-intensity signals (Naito et al., 2007; Luu and Chau, 2009; Power et al., 2010, 2011), most are extracted from hemodynamic signals. The reason for this is that HbO, HbR, total hemoglobin (HbT), and cerebral oxygen exchange (COE = HbO - HbR) provide more options for selection of appropriate features. Selection of an optimal feature set for classiﬁcation is essential for good classiﬁcation. It is necessary to select such features that have similarities with a certain class and differences from other classes. Different combinations of such features provide the necessary discriminatory information for classiﬁcation.

#### HEURISTIC METHODS

After noise removal, the shape of the hemodynamic signal is usually clear. By observing the hemodynamic signals arising from different activities, one can determine the differences in the signals: peak amplitude, mean value, variance, slope, skewness, kurtosis, etc. These can then be used as features for classiﬁcation of different signals. The most commonly used features for discrimination of different activities for fNIRS-BCI are signal mean (Coyle et al., 2004, 2007; Sitaram et al., 2007; Luu and Chau, 2009; Power et al.,

- 2010; Holper and Wolf, 2011; Fazli et al., 2012; Moghimi et al., 2012; Faress and Chau, 2013; Naseer and Hong, 2013; Naseer et al., 2014; Hong et al., 2015), signal slope (Power et al., 2011, 2012a,b; Hai et al., 2013; Naseer and Hong, 2013; Power and Chau, 2013; Schudlo and Chau, 2014; Hong et al., 2015), signal variance (Tai and Chau, 2009; Holper and Wolf, 2011), amplitude (Naito et al., 2007; Cui et al., 2010b; Bauernfeind et al.,
- 2011; Stangl et al., 2013), skewness (Tai and Chau, 2009; Holper and Wolf, 2011), kurtosis (Tai and Chau, 2009; Holper and Wolf,

- 2011), and zero crossing (Tai and Chau, 2009).

#### FILTER COEFFICIENTS

Some fNIRS-BCI studies have proposed the use of ﬁlter coefﬁcients (as classiﬁcation features) obtained by Kalman ﬁltering

(Abdelnour and Huppert, 2009), recursive least square estimation (Aqil et al., 2012a), and wavelet transform (Khoa and Nakagawa, 2008; Abibullaev et al., 2011; Abibullaev and An, 2012). They assumed that different brain activities will produce different ﬁlter coefﬁcients, in which different signals can be classiﬁed. This method has been shown to work well, even though no signiﬁcant classiﬁcation-accuracy improvement over the heuristic methods has been demonstrated.

#### GENETIC ALGORITHMS

Genetic algorithms are an optimization technique that is used to select the most efﬁcient features from a set. Power et al. (2012a) used a genetic algorithm to select features by employing LDA as a ﬁtness function. For more details on genetic algorithms, please see Pernkopf and O’Leary (2001) and Nicolas-Alonso and Gomez-Gil (2012).

Although feature selection is also dependent on individual activities, the mean values and slope values of HbO, HbR, or HbT frequently have been used in fNIRS-BCI. Almost half of fNIRSBCI studies have used either the mean value or the slope value of the signal as one of the features for classiﬁcation. It has been shown that HbO performs more robustly than HbR and HbT for assessing task-related cortical activation (Mihara et al., 2012; Naseer and Hong, 2013; Naseer et al., 2014). Plichta et al. (2006) showed that the retest reliability and stability over time of HbO signals are higher than those of HbR signals. From the above reasons, feature extraction using HbO signals is more suitable for classiﬁcation in fNIRS-BCI.

### CLASSIFICATION TECHNIQUES

Classiﬁcation techniques are used to identify the different brain signals that are generated by the user. These identiﬁed signals are then translated into control commands for application interface purposes. In most existing fNIRS-BCIs, such identiﬁcation is performed by using classiﬁcation techniques to discriminate various brain signals based on appropriate features. Classiﬁcation algorithms, as calibrated by the users through supervised learning during the training phase, are able to detect brain-signal patterns during the testing stage. Some of the commonly used classiﬁcation methods in fNIRS-BCI are LDA, SVM, HMM, and artiﬁcial neural networks (ANN).

#### LDA

LDA is the most commonly used classiﬁcation in fNIRS-BCI studies (see Figure 3). It utilizes discriminant hyperplane(s) to separate data representing two or more classes. Because of its simplicity and low computational requirements, it is highly suitable for online BCI systems. Not surprisingly, it has been used in a number of fNIRS-BCI studies. In LDA, the separating hyperplane is found by seeking such data projection by maximizing the distance between the two classes’ means and minimizing the interclass variances. LDA assumes a normal data distribution along with an equal covariance matrix for both classes (Lotte et al., 2007). An LDA algorithm tries to ﬁnd a vector v in the feature space such that two projected classes 1 and 2 in the vdirection can be well separated from each other while maintaining a small variance for each (see Figure 4). This can be accomplished by maximizing the Fisher’s criterion given by:

|[Figure 3]<br><br>FIGURE 3 | Types of classiﬁers in fNIRS BCI (from 2004 to 2014).|
|---|

|[Figure 4]<br><br>FIGURE 4 | LDA classiﬁcation depicting the best separating hyperplane.|
|---|

vTSbv vTSwv

J(v) =

(1)

where Sb and Sw are the between-class and within-class scatter matrices deﬁned as:

Sb = (m1 − m2)(m1 − m2)T, (2) Sw =

(xn−m1)(xn−m2)T+

(xn−m1)(xn−m2)T (3)

xn∈ C1

xn∈ C2

where m1 and m2 represent the group means of classes C1 and C2, respectively, and, xn denotes samples. It can be seen that a vector v that satisﬁes (1) can be reformulated as a generalized eigenvalue problem as:

|[Figure 5]<br><br>FIGURE 5 | SVM classiﬁcation illustrating the optimal hyperplane that maximizes the distance from the nearest support vectors.|
|---|

S−w1Sbv = λv. (4)

The optimal v is then the eigenvector corresponding to the largest eigenvalue of S−w1Sb or is directly obtained as:

v = S−w1(m1 − m2) (5) provided that Sw is non-singular.

Many fNIRS studies have successfully demonstrated the use of LDA for BCI (Luu and Chau, 2009; Bauernfeind et al., 2011; Holper and Wolf, 2011; Power et al., 2011, 2012a,b; Abibullaev and An, 2012; Fazli et al., 2012; Moghimi et al., 2012; Faress

- and Chau, 2013; Naseer and Hong, 2013; Power and Chau, 2013; Stangl et al., 2013; Kaiser et al., 2014; Naseer et al., 2014; Schudlo
- and Chau, 2014; Hong et al., 2015).

#### SVM

The SVM classiﬁer tries to maximize the distance between the separating hyperplane and the nearest training point(s) (the so-called support vectors) (see Figure 5). The separating hyperplane in the 2D feature space is given by the equation:

f (x) = r.x + b, (6)

where r, x∈R2 and b∈R1 (see Figure 5). The optimal solution r∗ that maximizes the distance between the hyperplane and the nearest training point(s) can be obtained by minimizing the cost function.

- 1

- 2

J (r,ξ) =

2

+ C.

r

while satisfying the constraints:

z

ξn, (7)

n=1

(xn.r + b) ≥ 1 − ξn for yn = +1, (8) (xn.r + b) ≥ −1 + ξn for yn = −1,

ξn ≥ 0 ∀ n,

where r 2 = rTr, C is the positive regularization parameter chosen by the user (a large value of C corresponds to a higher penalty for classiﬁcation errors), ξn is the measure of training error, z is the number of misclassiﬁed samples, and yn is the class label (+1 or −1 in the case of binary classiﬁcation) for the n-th sample.

Since SVM maximizes the distance from the nearest training point(s), it is known to enhance the generalization capabilities. Also, the regularization parameter C allows for accommodating the outliers and therefore reduces errors on the training sets (Burges, 1998). Although SVM is a linear classiﬁer because it uses one or more hyperplanes, it is possible to make SVM with non-linear decision boundaries. This can be done by using kernel functions such as the Gaussian or radial basis functions (known commonly as RBF). Non-linear SVM provides a more ﬂexible decision boundary that can result in an increased classiﬁcation accuracy. Using the kernel functions might, however, be computationally more demanding.

SVM has been shown to work well in a number of fNIRS-BCI studies (Sitaram et al., 2007; Tai and Chau, 2009; Cui et al., 2010b; Tanaka and Katura, 2011; Abibullaev and An, 2012; Hu et al.,

- 2012; Misawa et al., 2012; Hai et al., 2013; Naseer et al., 2014).

#### ANN

ANNs are non-linear classiﬁers that have been used in a few fNIRS-BCI studies (Abibullaev et al., 2011; Chan et al., 2012; Hai et al., 2013). ANNs were inspired by the fact that the human and animal brains are able to react adaptively to changes in internal and external environments. An appropriate model of the nervous system can produce a similar process in an artiﬁcial system. ANNs therefore try to mimic brain activity to solve problems. ANNs are widely used in pattern recognition problems, owing to their post-training capability to recognize sets of training-data-related patterns. ANNs consist of assemblies of several artiﬁcial neurons that allow for the drawing of nonlinear decision boundaries. They can be used in several different architectures including multilayer perception, Gaussian classiﬁer, learning vector quantization, RBF neural networks, and others. For more details on these architectures, please see (Anthony and Bartlett, 2009).

#### HMM

HMM is a non-linear probabilistic classiﬁer that provides the probability of observing a given set of features that are suitable primarily for classiﬁcation of time series (Rabiner, 1989). Some fNIRS studies, for example, have successfully demonstrated the feasibility of using HMM for BCI (Sitaram et al., 2007; Power et al., 2010; Falk et al., 2011; Chan et al., 2012; Zimmermann et al., 2013).

Two other classiﬁers that have been used in fNIRS-BCI are partial least squares discriminant analysis (PLSDA) (Seo et al.,

- 2012) and quadratic discriminant analysis (QDA) (Naito et al., 2007). Although some non-linear classiﬁers have been shown to

increase classiﬁcation accuracies over those of linear classiﬁers, the high-speed execution of the linear classiﬁers has made them the preferred ones for fNIRS-BCI. Almost 45% of fNIRS-BCI studies have utilized LDA for classiﬁcation (see Figure 3), due speciﬁcally to its ﬁne balance between the classiﬁcation accuracy and the execution speed.

### fNIRS-BCI APPLICATIONS

In recent years, signiﬁcant progress has been made in fNIRS-BCI research; however, the applications have been designed mostly for training and demonstration purposes only. fNIRS-BCI has two main drawbacks that have limited its use in real-world applications: a slow information transfer rate, and high error rates. Another problem is the fact that most fNIRS-BCIs are tested in controlled laboratory environments where the user can comfortably concentrate well on mental tasks; whereas in real situations, performance of concentration-dependent mental tasks (e.g., motor imagery, mental arithmetic, etc.) is much more challenging.

#### NEURO-REHABILITATION

BCI systems can be used to restore some of the lost motor and/or cognitive functions in individuals with stroke and spinal cord injury. The underlying idea of doing so is the ability of BCI feedback to induce self-regulation of brain activity. EEG, due to its high temporal resolution, has been used in a large number of previous neurofeedback studies (please see Gruzelier, 2013, for a review of EEG-based neurofeedback studies). However, since EEG has the limitations of imprecise localization and inaccessibility of subcortical areas, the hemodynamic activity measured by fMRI has been used in neurofeedback studies to overcome these problems. A comprehensive review of fMRI-based BCI and neurofeedback studies is provided by LaConte (2011) and Weiskopf (2012).

fNIRS is very attractive, in comparison with fMRI, in accessing subcortical brain signals. It is low cost, easy to use, and most of all it is portable. It can be used even in an ambulance. It also has a better temporal resolution than most of fMRI scanners (Huppert et al., 2006). Moreover, fNIRS is less sensitive to motion artifacts because it can be attached (or worn) to the brain or on the body. Given the above points, the potential of use of fNIRS in neurofeedback studies is very high. Mihara et al. (2012) demonstrated the possibility of using fNIRS-based neurofeedback to allow the users to willfully regulate their hemodynamic responses. They also showed that fNIRS-based neurofeedback enhances the hemodynamic correlates corresponding to motor imagery. Further, the same group have also reported similar results for stoke patients (Mihara et al., 2013). Recently, Kober et al. (2014) revealed that fNIRS-based neurofeedback can be used for a long-term training as well, and such repetitive neurofeedback can induce speciﬁc and focused brain activation: In contrast, sham feedback has led to diffuse brain activation patterns over broader brain areas. One important disadvantage of using hemodynamics (either fMRI or fNIRS) for neurofeedback is the inherent delay in its response, which makes the generation of commands slow compared to EEG. However, in the case of fNIRS, this kind of disadvantage can be solved if the initial dip (i.e., the phenomenon that HbO decreases

and HbR increases with neural ﬁring) can be measured (instead of hemodynamics).

#### COMMUNICATION

The primary application of BCI is to serve as a means of communication for people with motor disorders such as ALS, spinal cord injury and/or who are suffering from a persistent LIS. Naito et al. (2007) and Naseer et al. (2014) developed an fNIRS-BCI system for binary communication based on activations from the prefrontal area. The subjects were required to perform a speciﬁc task such as mental arithmetic or music imagery to increase the cognitive load and, thereby, respond “yes” or to remain relax and, thus, respond “no” to the given question. The average accuracies obtained by Naseer et al. (2014) with online classiﬁcation were approximately 82%. Sitaram et al. (2007) proposed an fNIRS-BCI-based online word speller. Their system involves using right-hand and left-hand motor imagery to move a cursor on a two-dimensional to select letters.

#### MOTOR RESTORATION/REHABILITATION

Another important application of fNIRS-BCI is the restoration of movement capability for people with motor disabilities. The control commands generated by a BCI system can be used to control a prosthetic limb or a wheelchair. It is desirable to have a portable system for these applications so that the user can move freely. Also these applications, for safety purposes, cannot afford high error rates, and must be fast enough to provide real-time control. Several fNIRS-BCI studies have tried to improve classiﬁcation accuracies and information transfer rates (Shin and Jeong, 2014). Using neurofeedback, induction of neuroplasticity of selected brain areas which has the potential to improve cognitive performance, also can be accomplished.

#### OTHER APPLICATIONS

Other applications of fNIRS-BCI include environment control and entertainment. Environment control applications (for instance, remote control, lights and temperature control) are very useful for motor-disabled people. Recently, BCI has also been used for healthy individuals’ entertainment purposes, although this is not a main priority of BCI research. The feasibility of braincontrolled video games has been demonstrated using EEG-BCI; however, no such fNIRS-based application has been introduced to date. For training purposes though, such games might be useful.

Table 1 provides a summary of most studies published from 2004 to 2014 that demonstrated important roles in brain-signalacquisition, signal pre-processing, feature-selection, and classiﬁcation stages for fNIRS-BCI.

### FUTURE PROSPECTS OF fNIRS-BCI

Given the advantages (non-invasive, cheap, portable, and silent), the use of fNIRS for BCI purposes is more suitable than fMRI. Furthermore, its use is easier than EEG that uses wet electrodes. A limitation of using fNIRS for BCI is that the information transfer rate is limited by the inherent delay in the hemodynamic response. However, the detections of the fast optical response (Gratton et al., 2006; Hu et al., 2011) and the initial dip (Akin et al., 2006; Yoshino and Kato, 2012) have been demonstrated, which can offer faster information transfer rate and better

control. Since the speed of EEG can be utilized, the authors believe that the future of non-invasive, portable and wearable BCIs lies in the use of hybrid EEG-fNIRS systems, as it has shown to work superior to EEG-BCIs and fNIRS-BCIs alone (Fazli et al., 2012; Kaiser et al., 2014; Khan et al., 2014; Koo et al., 2014). The reason for using a hybrid or combined fNIRS-EEG system is that it either improves the classiﬁcation accuracy or increases the number of control commands for BCI. This can be done by extracting some relevant features from fNIRS and combining them with EEG system. Fazli et al. (2012) demonstrated signiﬁcantly enhanced performance, in terms of classiﬁcation accuracy, by combined feature sets from both fNIRS and EEG. Tomita et al. (2014) showed that an optimal time slot for command generation can be estimated using indications from fNIRS signals in hybrid fNIRS-EEG. Khan et al. (2014) demonstrated an efﬁcient control strategy for active BCI by placing fNIRS and EEG at different brain locations. Koo et al. (2014) have also shown that the self-paced motor imagery can be detected more efﬁciently using a hybrid fNIRS-EEG system. Since the information contents of EEG and fNIRS are very distinctive, the hybrid fNIRS-EEG system has a strong potential for future neurorehabilitation and neurofeedback applications.

### CONCLUSIONS

In this paper, we have reviewed the state-of-the-art of fNIRSbased BCI systems, discussing all the procedures appearing in the standard BCI. Several different brain activities have been used for fNIRS-BCI, including, most commonly, those from the motor and prefrontal cortices. Motor cortex activities such as motor execution and motor imagery have been shown to work well and, indeed, are useful from the neurorehabilitation perspective. Prefrontal activities, on the other hand, offer the advantages of being free from artifacts due to hair. Both, despite of their drawbacks, have been shown to work well for fNIRS-BCI purposes. Use of other brain-imaging modalities, such as EEG in combination with fNIRS in a hybrid fashion, has been shown to effectively improve BCI performance. Such hybrid systems can acquire brain signals from the same as well as different brain areas, thereby increasing the number of control commands.

Different signal-processing and noise-removal methods including band-pass ﬁltering, ICA, principle component analysis, wavelet transform and adaptive-ﬁltering-based methods have been discussed. Because band-pass ﬁlters are simple and incur only low computational costs, they are still mostly used in fNIRS BCI.

BCI-applied classiﬁcation algorithms must be both accurate and fast. Although SVM, hidden Markov models, and artiﬁcial neural networks provide good classiﬁcation accuracies, the linear discriminant analysis (in its simple structure) has a low computational cost and also provides a good performance in classiﬁcation accuracy.

Considering all these points, it is concluded that there is much room for future fNIRS-BCI research, particularly in its applications. Although fNIRS-BCI applications for communication and control have been demonstrated in a number of studies, no commercial fNIRS-BCI application currently is available. All of the relevant research trends predict that interest in fNIRS-BCI will

Table1|ImportantfNIRS-BCIstudiesfrom2004to2014.

removal FeaturesClassiﬁerClassiﬁcation

accuracy(%)

ReferencesBrainareaTaskFilterusedfornoise

SVM80(spatialpatterns)>

62.7(mentalsinging)

LDA92.6(EEGHbRfor+

83.1(EEGHbRfor+

motorexecution)

motorimagery)

andHMM 90.2(PLSDA)

Low-passSlopeoflight-intensitysignalsLDA71.2(mental

85.7(HMM)

55.7(HMM)

94.6(SVM)

arithmetic)

LDAandSVM96.6(LDA)

89(HMM)

channels SVMandHMM73(SVM)

selectedchannels ANNandHMM63(ANN)

ANN94>

Bauernfeindetal.,2011PrefrontalcortexMentalarithmeticHigh-passAntagonistic HbOsignalsLDA79.7

Low-pass/WaveletﬁlterMeanvaluesoflightintensityHMM77.2

Low-passAmplitudeoflightintensityQDA80

Coyleetal.,2004MotorcortexMotorimageryLow-passMeanvaluesof HbOThreshold-based75

Coyleetal.,2007MotorcortexMotorimageryLow-passMeanvaluesof HbOThreshold-based80

signals LDA80

kurtosisof HbO LDA81

single,twoandthreechannels SVM77

wavelettransform HMM83

points PLSDA

and2ndordergradientof HbOand

andbandpowerofLaplacianﬁltered

adaptiveﬁlter Mean,variance,zerocrossing,root

averageﬁlter Amplitude,history,historygradient

motorimagery Low-passMeanvaluesof HbOand HbR

etc.oftheﬁltercoefﬁcientsfrom

subjectivepreference Low-passMeanamplitudeoflight-intensity

WaveletﬁlterMean,power,standarddeviation

Sitarametal.,2007MotorcortexMotorimageryLow-passMeanof HbOand HbRforall

average/band-pass Raw HbOvaluesatthreetime

HolperandWolf,2011MotorcortexMotorimageryLow-passMean,variance,skewnessand

Chanetal.,2012PrefrontalcortexMentalsingingLow-pass HbOand HbRsignalsfrom

Band-select HbOand HbRvaluesfrom

Falketal.,2011PrefrontalcortexMusicimageryLow-pass HbOand HbRvaluesafter*

kurtosisof HbOand HbR

meansquare,skewnessand

HbR,spatialpatterns

wavelettransform

EEGdata

Cuietal.,2010bMotorcortexFingertappingExponentialmoving

associatedwithimages Least-meansquare

cortex Change-detectiontaskMovingaverage/

Seoetal.,2012MotorcortexFingertappingMoving

Abibullaevetal.,2011PrefrontalcortexObjectrotation,verbal

MotorcortexMotorexecutionandFazlietal.,2012**

LuuandChau,2009PrefrontalcortexNeuralcorrelatesof

ﬂuencyandmental

musicimageryand

landscapeimagery

Naitoetal.,2007PrefrontalcortexMentalarithmetic,

TaiandChau,2009PrefrontalcortexEmotionrehearsal

arithmetic/Mental

arithmetic/Music

arithmetic

imagery

singing

Poweretal.,2010PrefrontalcortexMental

Poweretal.,2011PrefrontalcortexMental

TanakaandKatura,2011PrefrontalandVisual

(Continued)

Table1|Continued

Band-passMeanvaluesofHbO,HbRandHbTLDA70(mentalarithmetic>

andmentalrotation)

87.2(signalslope)

LDA77.5(meanvalue)

91.5(quaternary)

removal FeaturesClassiﬁerClassiﬁcation

accuracy(%)

92.4(ternary)

classiﬁer 95.5(binary)

82.1(SVM)

regression SVMandANN79.1(SVM)

83.3(ANN)

90(SVM)>

SVM 75(ANN)>

85(LDA)>

Naseeretal.,2014PrefrontalcortexMentalarithmeticLow-passMeanvaluesof HbOand HbRLDAandSVM74.2(LDA)

arithmetic Band-passMeanandslopeofHbOMulti-classLDA75>

HMM88.5

Huetal.,2012PrefrontalcortexDeceptionBand-passAbsolutevaluesof HbOand HbRSVM83.4

Poweretal.,2012bPrefrontalcortexMentalarithmeticLow-passSignalslopeLDA72.6

Band-passMeanvaluesof HbOand HbRLDA80>

LDA 90>

andnoiseof HbOand HbR LDA71.9

PowerandChau,2013PrefrontalcortexMentalarithmeticLow-passSignalslopeof HbOand HbRLDA71.1

3differenttimewindows LDA77.4

arithmetic MovingaverageAmplitudeof HbOLDA65

2013*** PrefrontalcortexVerbalﬂuencyLow-passSlopeofHbO,HbRandHbTLDA86

transform ANN,LDAand

varianceandmedian NaïveBayes

andEEGamplitudes Step-wise

musiclistening Low-passMeananddifferencebetweensignal

SchudloandChau,2014PrefrontalcortexMentalarithmeticLow-passSlopeof HbO, HbRand HbTin

visualstimulus Band-passMeanvaluesof HbOand HbR

2013* MotorcortexMotorexecutionBand-passCombinationof HbOand HbR

andbiosignalsbelongingtosame

NaseerandHong,2013MotorcortexMotorimageryLow-passMeanandslopevaluesof HbO

WaveletﬁlterFiltercoefﬁcientsfromwavelet

Savitzky-Golay Mean,amplitude,slope,delay,

and HbRinseveraltemporal

Haietal.,2013MotorcortexHandtappingSavitzky-GolaySignalvaluesafterpolynomial

locationandsametime

- *Forclassiﬁcationpurpose,theyalsousedsomeadditionalfeaturesfromECG,respiration,bloodpressure,skinconductanceresponse,etc.
- **TheyusedcombinedfNIRSandEEGmodalitiesforbrainsignalacquisition.
- ***ThisstudyusedadditionaltranscranialDopplerultrasonographysignalstogetherwithfNIRSsignals.

windows

ReferencesBrainareaTaskFilterusedfornoise

ShinandJeong,2014MotorcortexMotorexecutionBand-passand

Prefrontalcortex MotorImagery,mental

prefrontalcortex Motorimagery,mental

prefrontalcortex Motorimagery,mental

AbibullaevandAn,2012PrefrontalcortexObjectrotation,letter

mentalcountingand

Liuetal.,2013PrefrontalcortexNeuralcorrelationof

rotationandmental

arithmetic,mental

mentalarithmetic

Moghimietal.,2012PrefrontalcortexEmotionallyrated

prefrontalcortex Motorexecution,

characterwriting

singing,mental

multiplication

paddingand

Hwangetal.,2014Motorcortex,

Hongetal.,2015Motorcortex,

Motorcortex,Khanetal.,2014**

Stangletal.,2013Motorcortex,

Zimmermannetal.,

FaressandChau,

continue to grow. In the near future, several breakthroughs via bundled-type fNIRS probes, hybrid EEG-fNIRS, and detection of the initial dip are expected.

### ACKNOWLEDGMENTS

This work was supported by the National Research Foundation of Korea under the Ministry of Science, ICT and Future Planning, Korea (grant no. NRF-2014R1A2A1A10049727).

### REFERENCES

Abdelnour, A. F., and Huppert, T. (2009). Real-time imaging of human brain function by near-infrared spectroscopy using an adaptive general linear model. Neuroimage 46, 133–143. doi: 10.1016/j.neuroimage.2009. 01.033

Abibullaev, B., and An, J. (2012). Classiﬁcation of frontal cortex hemodynamic responses during cognitive tasks using wavelet transforms and machine learning algorithms. Med. Eng. Phys. 34, 1394–1410. doi: 10.1016/j.medengphy.2012.01.002

Abibullaev, B., An, J., and Moon, J. I. (2011). Neural network classiﬁcation of brain hemodynamic responses from four mental tasks. Int. J. Optomechatronics 5, 340–359. doi: 10.1080/15599612.2011.633209

Adhika, D. R., Hazrati, M. K., and Hofmann, U. G. (2012). An experimental setup for brain activity measurement based on near infrared spectroscopy. Biomed. Tech. 57, 609–612. doi: 10.1515/bmt-2012-4487

Akin, A., Bilensoy, D., Emir, U. E., Gulsoy, M., Candansayar, S., and Bolay, H. (2006). Cerebrovascular dynamics in patients with migraine: near-infrared spectroscopy study. Neurosci. Lett. 400, 86–91. doi: 10.1016/j.neulet.2006.02.016

Anthony, M., and Bartlett, P. L. (2009). Neural Network Learning: Theoretical Foundations. New York, NY: Cambridge University Press.

- Aqil, M., Hong, K.-S., Jeong, M.-Y., and Ge, S. S. (2012a). Cortical brain imaging by adaptive ﬁltering of NIRS signals. Neurosci. Lett. 514, 35–41. doi: 10.1016/j.neulet.2012.02.048
- Aqil, M., Hong, K.-S., Jeong, M.-Y., and Ge, S. S. (2012b). Detection of eventrelated hemodynamic response to neuroactivation by dynamic modeling of brain activity. Neuroimage 63, 553–568. doi: 10.1016/j.neuroimage.2012.07.006

Ayaz, H., Shewokis, P. A., Bunce, S., Izzetoglu, K., Willems, B., and Onaral, B.

(2012). Optical brain monitoring for operator training and mental workload assessment. Neuroimage 59, 36–47. doi: 10.1016/j.neuroimage.2011.06.023

Ayaz, H., Shewokis, P., Bunce, S., Schultheis, M., and Onaral, B. (2009). “Assessment of cognitive neural correlates for a functional near infrared-based brain computer interface system,” in Foundations of Augmented Cognition. Neuroergonomics and Operational Neuroscience, eds D. D. Schmorrow, I. V. Estabrooke, and M. Grootjen (Heidelberg: Springer-Verlag), 699–708.

Bauernfeind, G., Leeb, R., Wriessnegger, S. C., and Pfurtscheller, G. (2008). Development, set-up and ﬁrst results for a one-channel near-infrared spectroscopy system. Biomed. Tech. 53, 36–43. doi: 10.1515/BMT.2008.005

Bauernfeind, G., Scherer, R., Pfurtscheller, G., and Neuper, C. (2011). Single-trial classiﬁcation of antagonistic oxyhemoglobin responses during mental arithmetic. Med. Biol. Eng. Comput. 49, 979–984. doi: 10.1007/s11517-011-0792-5

Bhutta, M. R., Hong, K.-S., Kim, B.-M., Hong, M. J., Kim, Y.-H., and Lee, S.-H. (2014). Note: three wavelengths near-infrared spectroscopy system for compensating the light absorbance by water. Rev. Sci. Intrum. 85:026111. doi: 10.1063/1.4865124

Boas, D. A., Chen, K., Grebert, D., and Franceschini, M. A. (2004b). Improving the diffuse optical imaging spatial resolution of the cerebral hemodynamic response to brain activation in humans. Opt. Lett. 29, 1506–1508. doi: 10.1364/OL.29.001506

Boas, D. A., Dale, A. M., and Franceschini, M. A. (2004a). Diffuse optical imaging of brain activation: approaches to optimizing image sensitivity, resolution, and accuracy. Neuroimage 23, S275–S288. doi: 10.1016/j.neuroimage.2004.07.011 Buch, E., Weber, C., Cohen, L. G., Braun, C., Dimyan, M. A., Ard, T., et al. (2008). Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39, 910–917. doi: 10.1161/STROKEAHA.107.505313

Burges, C. J. C. (1998). A tutorial on support vector machines for pattern recognition. Knowl. Discov. Data Min. 2, 121–167. doi: 10.1023/A:1009715923555

Chan, J., Power, S., and Chau, T. (2012). Investigating the need for modeling temporal dependencies in a brain-computer interface with real-time feedback

based on near infrared spectra. J. Near Infrared Spectrosc. 20, 107–116. doi: 10.1255/jnirs.971

Cooper, R. J., Selb, J., Gagnon, L., Phillip, D., Schytz, H. W., Iversen, H. K., et al. (2012). A systematic comparison of motion artifact correction techniques for functional near-infrared spectroscopy. Front. Neurosci. 6:147. doi: 10.3389/fnins.2012.00147

Coyle, S. M., Ward, T. E., and Markham, C. M. (2007). Brain-computer interface using a simpliﬁed functional near-infrared spectroscopy system. J. Neural Eng. 4, 219–226. doi: 10.1088/1741-2560/4/3/007

Coyle, S., Ward, T., Markham, C., and McDarby, G. (2004). On the suitability of near-infrared (NIR) systems for next-generation brain-computer interfaces. Physiol. Meas. 25, 815–822. doi: 10.1088/0967-3334/25/4/003

- Cui, X., Bray, S., and Reiss, A. L. (2010a). Functional near infrared spectroscopy (NIRS) signal improvement based on negative correlation between oxygenated and deoxygenated hemoglobin dynamics. Neuroimage 49, 3039–3046. doi: 10.1016/j.neuroimage.2009.11.050
- Cui, X., Bray, S., and Reiss, A. L. (2010b). Speeded near-infrared spectroscopy (NIRS) response detection. PLoS ONE 5:e15474. doi: 10.1371/journal.pone.0015474

Delpy, D. T., Cope, M., van der Zee, P., Arridge, S., Wray, S., and Wyatt, J. (1988). Estimation of optical pathlength through tissue from direct time of ﬂight measurement. Phys. Med. Biol. 33, 1433–1442. doi: 10.1088/0031-9155/33/12/008

Falk, T. H., Guirgis, M., Power, S., and Chau, T. (2011). Taking NIRS-BCIs outside the lab: towards achieving robustness against environment noise. IEEE Trans. Neural Syst. Rehabil. Eng. 19, 136–146. doi: 10.1109/TNSRE.2010.2078516

Faress, A., and Chau, T. (2013). Towards a multimodal brain-computer interface: combining fNIRS and fTCD measurements to enable higher classiﬁcation accuracy. Neuroimage 77, 186–194. doi: 10.1016/j.neuroimage.2013.03.028

Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Muller, K. R., et al.

(2012). Enhanced performance by a hybrid NIRS-EEG brain-computer interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084

Fekete, T., Rubin, D., Carlson, J. M., and Mujica-Parodi, L. R. (2011). The NIRS analysis package: noise reduction and statistical inference. PLoS ONE 6:e24322. doi: 10.1371/journal.pone.0024322

Ferrari, M., Giannini, I., Sideri, G., and Zanette, E. (1985). Continuous non invasive monitoring of human brain by near infrared spectroscopy. Adv. Exp. Med. Biol. 191, 873–882. doi: 10.1007/978-1-4684-3291-6_88

Ferrari, M., Mottola, L., and Quaresima, V. (2004). Principles, techniques, and limitations of near infrared spectroscopy. Can. J. Appl. Physiol. 29, 463–487. doi: 10.1139/h04-031

Franceschini, M. A., Joseph, D. K., Huppert, T. J., Diamond, S. G., and Boas, D. A.

(2006). Diffuse optical imaging of the whole head. J. Biomed. Opt. 11:054007. doi: 10.1117/1.2363365

Funane, T., Atsumori, H., Katura, T., Obata, A. N., Sato, H., Tanikawa, Y., et al. (2014). Quantitative evaluation of deep and shallow tissue layers’ contribution to fNIRS signal using multi-distance optodes and independent component analysis. Neuroimage 85, 150–165. doi: 10.1016/j.neuroimage.2013.02.026

Gagnon, L., Yucel, M. A., Dehaes, M., Cooper, R. J., Perdue, K. L., Selb, J., et al. (2012). Quantiﬁcation of the cortical contribution to the NIRS signal over the motor cortex using concurrent NIRS-fMRI measurements. Neuroimage 59, 3933–3940. doi: 10.1016/j.neuroimage.2011.10.054

Gratton, G., Brumback, C. R., Gordon, B. A., Pearson, M. A., Low, K. A., and Fabiani, M. (2006). Effects of measurement method, wavelength, and sourcedetector distance on the fast optical signal. Neuroimage 32, 1576–1590. doi: 10.1016/j.neuroimage.2006.05.030

Gruzelier, J. H. (2013). EEG-neurofeedback for optimising performance. I: a review of cognitive and affective outcome in healthy participants. Neurosci. Biobehav. Rev. 44, 124–141. doi: 10.1016/j.neubiorev.2013.09.015

Hai, N. T., Cuong, N. Q., Khoa, T. Q. D., and Toi, V. V. (2013). Temporal hemodynamic classiﬁcation of two hands tapping using functional near-infrared spectroscopy. Front. Hum. Neurosci. 7:516. doi: 10.3389/fnhum.2013.00516 Hammer, E. M., Kaufmann, T., Kleih, S. C., Blankertz, B., and Kubler, A. (2014). Visuo-motor coordination ability predicts performance with brain-computer interfaces controlled by modulation of sensorimotor rhythms (SMR). Front. Hum. Neurosci. 8:574. doi: 10.3389/fnhum.2014. 00574

Holper, L., and Wolf, M. (2011). Single-trial classiﬁcation of motor imagery differing in task complexity: a functional near-infrared spectroscopy study. J. Neuroeng. Rehabil. 8:34. doi: 10.1186/1743-0003-8-34

Hong, K.-S., Naseer, N., and Kim, Y.-H. (2015). Classiﬁcation of prefrontal and motor cortex signals for three-class fNIRS-BCI. Neurosci. Lett. 587, 87–92. doi: 10.1016/j.neulet.2014.12.029

Hong, K.-S., and Nguyen, H.-D. (2014). State-space models of impulse hemodynamic responses over motor, somatosensory, and visual cortices. Biomed. Opt. Express 5, 1778–1798. doi: 10.1364/BOE.5.001778

Hoshi, Y., Onoe, H., Watanabe, Y., Andersson, J., Bergstrom, M., Lilja, A., et al. (1994). Non-synchronous behavior of neuronal-activity, oxidative-metabolism and blood-supply during mental tasks in man. Neurosci. Lett. 172, 129–133. doi: 10.1016/0304-3940(94)90679-3

Hoshi, Y., and Tamura, M. (1997). Near-infrared optical detection of sequential brain activation in the prefrontal cortex during mental tasks. Neuroimage 5, 292–297. doi: 10.1006/nimg.1997.0270

- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2011). Recognition of stimulus-evoked neuronal optical response by identifying chaos levels of near-infrared spectroscopy time series. Neurosci. Lett. 504, 115–120. doi: 10.1016/j.neulet.2011.09.011
- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2012). fNIRS-based online deception decoding. J Neural Eng. 9:026012. doi: 10.1088/1741-2560/9/2/026012
- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2013). Reduction of trial-to-trial variations in functional near-infrared spectroscopy signals by accounting for resting-state functional connectivity. J. Biomed. Opt. 18:017003. doi: 10.1117/1.JBO.18.1.017003

Hu, X.-S., Hong, K.-S., Ge, S. S., and Jeong, M.-Y. (2010). Kalman estimator- and general linear model-based on-line brain activation mapping by near-infrared spectroscopy. Biomed. Eng. Online 9:82. doi: 10.1186/1475-925X-9-82

Huppert, T. J., Diamond, S. G., Fransceshini, M. A., and Boas, D. A. (2009). HomER: a review of time-series analysis methods for near-infrared spectroscopy of the brain. Appl. Opt. 48, D280–D298. doi: 10.1364/AO.48.00D280

Huppert, T. J., Hoge, R. D., Diamond, S. G., Franceschini, M. A., and Boas, D. A. (2006). A temporal comparison of BOLD, ASL, and NIRS hemodynamic responses to motor stimuli in adult humans. Neuroimage 29, 368–382. doi: 10.1016/j.neuroimage.2005.08.065

Hwang, H.-J., Kim, S., Choi, S., and Im, C.-H. (2013). EEG-based brain-computer interfaces: a thorough literature survey. Int. J. Hum. Comp. Int. 29, 814–826. doi: 10.1080/10447318.2013.780869

Hwang, H.-J., Lim, J.-H., Kim, D.-W., and Im, C.-H. (2014). Evaluation of various mental task combinations for near-infrared spectroscopy-based braincomputer interfaces. J. Biomed. Opt. 19:077005. doi: 10.1117/1.JBO.19.7.077005

Izzetoglu, M., Devaraj, A., Bunce, S., and Onaral, B. (2005). Motion artifact cancellation in NIR spectroscopy using Wiener ﬁltering. IEEE Trans. Biomed. Eng. 52, 934–938. doi: 10.1109/TBME.2005.845243

Jobsis, F. F. (1977). Noninvasive, infrared monitoring of cerebral and myocardial oxygen sufﬁciency and circulatory parameters. Science 198, 1264–1267. doi: 10.1126/science.929199

Kaiser, V., Gauernfeind, G., Kreilinger, A., Kaufmann, T., Kubler, A., Neuper, C., et al. (2014). Cortical effects of user training in a motor imagery based braincomputer interface measured by fNIRS and EEG. Neuroimage 85, 432–444. doi: 10.1016/j.neuroimage.2013.04.097

- Kamran, M. A., and Hong, K.-S. (2013). Linear parameter-varying model and adaptive ﬁltering technique for detecting neuronal activities: an fNIRS study. J. Neural Eng. 10:056002. doi: 10.1088/1741-2560/10/5/056002
- Kamran, M. A., and Hong, K.-S. (2014). Reduction of physiological effects in fNIRS waveforms for efﬁcient brain-state decoding. Neurosci. Lett. 580, 130–136. doi: 10.1016/j.neulet.2014.07.058

Kato, T., Kamei, A., Takashima, S., and Ozaki, T. (1993). Human visual cortical function during photic stimulation monitoring by means of near-infrared spectroscopy. J. Cereb. Blood Flow Metab. 13, 516–520. doi: 10.1038/jcbfm.1993.66

Khan, M. J., Hong, M. J., and Hong, K.-S. (2014). Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface. Front. Hum. Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244

Khoa, T. Q. D., and Nakagawa, M. (2008). Functional near-infrared spectroscope for cognition brain tasks by wavelets analysis and neural networks. Int. J. Biol. Life Sci. 4, 28–33. doi: 10.1186/1753-4631-2-3

Kim, J.-Y., Kang, H.-C., Cho, J.-H., Lee, J.-H., Kim, H.-D., and Im, C.-H. (2014). Combined use of multiple computational intracranial EEG analysis techniques for the localization of epileptogenic zones in Lennox-Gastaut syndrome. Clin. EEG Neurosci. 45, 169–178. doi: 10.1177/1550059413495393

Kirilina, E., Jelzow, A., Heine, A., Niessing, M., Wabnitz, H., Brühl, R., et al. (2012). The physiological origin of task-evoked systemic artefacts

in functional near infrared spectroscopy. Neuroimage 61, 70–81. doi: 10.1016/j.neuroimage.2012.02.074

Kirilina, E., Yu, N., Jelzow, A., Wabnitz, H., Jacobs, A. M., and Tachtsidis, I. (2013). Identifying and quantifying main components of physiological noise in functional near infrared spectroscopy on the prefrontal cortex. Front. Hum. Neurosci. 7:864. doi: 10.3389/fnhum.2013.00864

Kleih, S. C., and Kubler, A. (2013). Empathy, motivation, and P300-BCI performance. Front. Hum. Neurosci. 7:642. doi: 10.3389/fnhum.2013.00642

Ko, K. E., and Sim, K. B. (2013). Harmony search-based hidden Markov model optimization for online classiﬁcation of single trial EEGs during motor imagery tasks. Int. J. Control. Autom. 11, 608–613. doi: 10.1007/s12555-012-0035-z

Kober, S. E., Wood, G., Kurzmann, J., Friedrich, E. V., Stangl, M., Wippel, T., et al. (2014). Near-infrared spectroscopy based neurofeedback training increases speciﬁc motor imagery related cortical activation compared to sham feedback. Biol. Psychol. 95, 21–30. doi: 10.1016/j.biopsycho.2013.05.005

Kohno, S., Miyai, I., Seiyama, A., Oda, I., Ishikawa, A., Tsuneishi, S., et al. (2007). Removal of the skin blood ﬂow artifact in functional near-infrared spectroscopic imaging data through independent component analysis. J. Biomed. Opt. 12:062111. doi: 10.1117/1.2814249

Koo, B., Lee, H.-G., Nam, Y., Kang, H., Koh, C.-S., Shin, H.-C., et al. (2014). A hybrid NIRS-EEG system for self-paced brain computer interface with online motor imagery. J. Neurosci. Methods. doi: 10.1016/j.jneumeth.2014.04.016. [Epub ahead of print].

LaConte, S. M. (2011). Decoding fMRI brain states in real-time. Neuroimage 56, 440–454. doi: 10.1016/j.neuroimage.2010.06.052

Liu, Y., Ayaz, H., Curtin, A., and Onarall, B. (2013). “Towards a hybrid P300based BCI using simultaneous fNIR and EEG,” in Foundations of Augmented Cognition, eds D. Schmorrow and C. Fidopiastis (Heidelberg: Springer-Verlag), 335–344.

Lotte, F., Congedo, M., Lecuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces. J. Neural Eng. 4:R1. doi: 10.1088/1741-2560/4/2/R01

Luu, S., and Chau, T. (2009). Decoding subjective preferences from single-trial near-infrared spectroscopy signals. J. Neural Eng. 6:016003. doi: 10.1088/17412560/6/1/016003

McCormick, P. W., Stewart, M., Lewis, G., Dujovny, M., and Ausman, J. I. (1992). Intracerebral penetration of infrared light: technical note. J. Neurosurg. 76, 315–318. doi: 10.3171/jns.1992.76.2.0315

Mellinger, J., Schalk, G., Braun, C., Preissl, H., Rosenstiel, W., Birbaumer, N., et al. (2007). An MEG-based brain-computer interface (BCI). Neuroimage 36, 581–593. doi: 10.1016/j.neuroimage.2007.03.019

Mihara, M., Hattori, N., Hatakenaka, M., Yagura, H., and Kawano, T. (2013). Nearinfrared spectroscopy-mediated neurofeedback enhances efﬁcacy of motor imagery-based training in poststroke victims a pilot study. Stroke 44, 1091–1098. doi: 10.1161/STROKEAHA.111.674507

Mihara, M., Miyai, I., Hattori, N., Hatakenaka, M., Yagura, H., Kawano, T., et al. (2012). Neurofeedback using real-time near-infrared spectroscopy enhances motor imagery related cortical activation. PLoS ONE 7:e32234. doi: 10.1371/journal.pone.0032234

Misawa, T., Takano, S., Shimokawa, T., and Hirobayashi, S. (2012). A braincomputer interface for motor assist by the prefrontal cortex. Electron. Comm. Jpn. 95, 1–8. doi: 10.1002/ecj.11426

Moghimi, S., Kushki, A., Power, S., Guerguerian, A. M., and Chau, T. (2012). Automatic detection of a prefrontal cortical response to emotionally rated music using multi-channel near-infrared spectroscopy. J. Neural Eng. 9:026022. doi: 10.1088/1741-2560/9/2/026022

Nagaoka, T., Sakatani, K., Awano, T., Yokose, N., Hoshino, T., Murata, Y., et al. (2010). “Development of a new rehabilitation system based on a braincomputer interface using near-infrared spectroscopy,” in Experimental Medicine and Biology, Oxygen Transport in Tissue XXXI, eds E. Takashi and D. F. Bruley (New York, NY: Springer), 497–503.

Naito, M., Michioka, Y., Ozawa, K., Ito, Y., Kiguchi, M., and Kanazawa, T. (2007). A communication means for totally locked-in ALS patients based on changes in cerebral blood volume measured with near-infrared light. IEICE T. Inf. Syst. E90D, 1028–1037. doi: 10.1093/ietisy/e90-d.7.1028

Naseer, N., and Hong, K.-S. (2013). Classiﬁcation of functional near-infrared spectroscopy signals corresponding to the right- and left-wrist motor imagery for development of a brain-computer interface. Neurosci. Lett. 553, 84–49. doi: 10.1016/j.neulet.2013.08.021

Naseer, N., Hong, M. J., and Hong, K.-S. (2014). Online binary decision decoding using functional near-infrared spectroscopy for the development of braincomputer interface. Exp. Brain Res. 232, 555–564. doi: 10.1007/s00221-0133764-1

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 2, 1211–1279. doi: 10.3390/s120201211

Pernkopf, F., and O’Leary, P. (2001). “Feature selection for classiﬁcation using genetic algorithms with a novel encoding,” in Computer Analysis of Images and Patterns, ed W. Skarbek (Heidelberg: Springer-Verlag), 161–168.

Plichta, M., Herrmann, M., Baehne, C., Ehlis, A.-C., Richter, M., Pauli, P., et al. (2006). Event-related functional near-infrared spectroscopy (fNIRS): are the measurements reliable? Neuroimage 31, 116–124. doi: 10.1016/j.neuroimage.2005.12.008

Power, S., and Chau, T. (2013). Automatic single-trial classiﬁcation of prefrontal hemodynamic activity in an individual with Duchenne muscular dystrophy. Dev. Neurorehabil. 16, 67–72. doi: 10.3109/17518423.2012.718293

Power, S. D., Falk, T. H., and Chau, T. (2010). Classiﬁcation of prefrontal activity due to mental arithmetic and music imagery using hidden Markov models and frequency domain near-infrared spectroscopy. J. Neural Eng. 7:026002. doi: 10.1088/1741-2560/7/2/026002

Power, S. D., Khushki, A., and Chau, T. (2012a). Automatic single trial discrimination of mental arithmetic, mental singing and the no-control state from the prefrontal activity: towards a three-state NIRS-BCI. BMC Res. Notes 5:141. doi: 10.1186/1756-0500-5-141

- Power, S. D., Kushki, A., and Chau, T. (2011). Towards a system-paced near-infrared spectroscopy brain-computer interface: differentiating prefrontal activity due to mental arithmetic and mental singing from the no-control state. J. Neural Eng. 8:066004. doi: 10.1088/1741-2560/8/6/066004
- Power, S. D., Kushki, A., and Chau, T. (2012b). Intersession consistency of singletrial classiﬁcation of the prefrontal response to mental arithmetic and the nocontrol state by NIRS. PLoS ONE 7:e37791. doi: 10.1371/journal.pone.0037791

Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech recognition. Proc. IEEE 77, 257–286. doi: 10.1109/5. 18626

Rea, M., Rana, M., Lugato, N., Terekhin, P., Gizzi, L., Brotz, D., et al. (2014). Lower limb movement preparation in chronic stroke: a pilot study toward an fNIRS-BCI for gait rehabilitation. Neurorehabil. Neural Repair 28, 564–575. doi: 10.1177/1545968313520410

Saager, R. B., and Berger, A. J. (2005). Direct characterization and removal of interfering absorption trends in two-layer turbid media. J. Opt. Soc. Am. A Opt. Image Sci. Vis. 22, 1874–1882. doi: 10.1364/JOSAA.22.001874

Saager, R. B., Telleri, N. L., and Berger, A. J. (2011). Two-detector corrected near infrared spectroscopy (C-NIRS) detects hemodynamic activation responses more robustly than single-detector NIRS. Neuroimage 55, 1679–1685. doi: 10.1016/j.neuroimage.2011.01.043

Sagara, K., and Kido, K. (2012). Evaluation of a 2-channel NIRS-based optical brain switch for motor disabilities’ communication tools. IEICE T. Inf. Syst. E95D, 829–834. doi: 10.1587/transinf.E95.D.829

Santosa, H., Hong, M. J., and Hong, K.-S. (2014). Lateralization of music processing with noises in the auditory cortex: an fNIRS study. Front. Behav. Neurosci. 8:418. doi: 10.3389/fnbeh.2014.00418

Santosa, H., Hong, M. J., Kim, S.-P., and Hong, K.-S. (2013). Noise reduction in functional near-infrared spectroscopy signals by independent component analysis. Rev. Sci. Instrum. 84:073106. doi: 10.1063/1.4812785

Sardouie, S. H., and Shamsollahi, M. B. (2012). Selection of efﬁcient features for discrimination of hand movements from MEG using a BCI competition IV data set. Front. Neurosci. 6:42. doi: 10.3389/fnins.2012.00042

Sato, H., Tanaka, N., Uchida, M., Hirabayashi, Y., Kanai, M., Ashida, T., et al. (2006). Wavelet analysis for detecting body-movement artifacts in optical topography signals. Neuroimage 33, 580–587. doi: 10.1016/j.neuroimage.2006. 06.028

Sato, H., Yahata, N., Funane, T., Takizawa, R., Katura, T., Atsumori, H., et al. (2013). A NIRS-fMRI investigation of prefrontal cortex activity during a working memory task. Neuroimage 83C, 158–173. doi: 10.1016/j.neuroimage.2013. 06.043

Schudlo, L. C., and Chau, T. (2014). Dynamic topographical pattern classiﬁcation of multichannel prefrontal NIRS signals: II. Online differentiation of mental arithmetic and rest. J. Neural Eng. 11:016003. doi: 10.1088/17412560/11/1/016003

Seo, Y., Lee, S., Koh, D., and Kim, B.-M. (2012). Partial least squares-discriminant analysis for the prediction of hemodynamic changes using near-infrared spectroscopy. J. Opt. Soc. Korea 16, 57–62. doi: 10.3807/JOSK.2012.16.1.057

Shin, J., and Jeong, J. (2014). Multiclass classiﬁcation of hemodynamic responses for performance improvement of functional near-infrared spectroscopy-based brain-computer interface. J. Biomed. Opt. 19:067009. doi: 10.1117/1.JBO.19.6.067009

Sitaram, R., Zhang, H. H., Guan, C. T., Thulasidas, M., Hoshi, Y., Ishikawa, A., et al. (2007). Temporal classiﬁcation of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain-computer interface. Neuroimage 34, 1416–1427. doi: 10.1016/j.neuroimage.2006.11.005

Soekadar, S. R., Witkowski, M., Cossio, E. G., Birbaumer, N., and Cohen, L. G. (2014). Learned EEG-based brain self-regulation of motor-related oscillations during application of transcranial electric brain stimulation: feasibility and limitations. Front. Behav. Neurosci. 8:93. doi: 10.3389/fnbeh.2014. 00093

Stangl, M., Bauernfeind, G., Kurzmann, J., Scerer, R., and Neuper, C. (2013). A hemodynamic brain-computer interface based on real-time classiﬁcation of near infrared spectroscopy signals during motor imagery and mental arithmetic. J. Near Infrared Spectrosc. 21, 157–171. doi: 10.1255/ jnirs.1048

Tachtsidis, I., Koh, P. H., Stubbs, C., and Elwell, C. E. (2010). “Functional optical topography analysis using statistical parametric mapping (SPM) methodology with and without physiological confounds,” in Oxygen Transport to Tissue XXXI, eds E. Takahashi and D. F. Bruley (Boston, MA, Springer), 237–243

Tai, K., and Chau, T. (2009). Single-trial classiﬁcation of NIRS signals during emotional induction tasks: towards a corporeal machine interface. J. Neuroeng. Rehabil. 6:39. doi: 10.1186/1743-0003-6-39

Takahashi, T., Takikawa, Y., Kawagoe, R., Shibuya, S., Iwano, T., and Kitazawa, S. (2011). Inﬂuence of skin blood ﬂow on near-infrared spectroscopy signals measured on the forehead during a verbal ﬂuency task. Neuroimage 57, 991–1002. doi: 10.1016/j.neuroimage.2011.05.012

Tanaka, H., and Katura, T. (2011). Classiﬁcation of change detection and change blindness from near-infrared spectroscopy signals. J. Biomed. Opt. 16:087001. doi: 10.1117/1.3606494

Tomita, Y., Vialatte, F. B., Dreyfus, G., Mitsukura, Y., Bakardjian, H., and Cichocki, A. (2014). Bimodal BCI using simultaneously NIRS and EEG. IEEE Trans. Biomed. Eng. 61, 1274–1284. doi: 10.1109/TBME.2014.2300492

Turnip, A., and Hong, K.-S. (2012). Classifying mental activities from EEG-P300 signals using adaptive neural network. Int. J. Innovat. Comput. Inform. Control 8, 6429–6443

Turnip, A., Hong, K.-S., and Jeong, M.-Y. (2011). Real-time feature extraction of EEG-based P300 using adaptive nonlinear principal component analysis. Biomed. Eng. Online 10:83. doi: 10.1186/1475-925X-10-83

Utsugi, K., Obata, A., Sato, H., Aoki, R., Maki, A., Koizumi, H., et al. (2008). GO-STOP control using optical brain-computer interface during calculation task. IEICE T. Commun. E91B, 2133–2141. doi: 10.1093/ietcom/e91-b. 7.2133

van der Heiden, L., Liberati, G., Sitaram, R., Kim, S., Jaœkowski, P., Raffone, A., et al. (2014). Insula and inferior frontal triangularis activations distinguish between conditioned brain responses using emotional sounds for basic BCI communication. Front. Behav. Neurosci. 8:247. doi: 10.3389/fnbeh.2014. 00247

Villringer, A., and Chance, B. (1997). Non-invasive optical spectroscopy and imaging of human brain function. Trends Neurosci. 20, 435–442. doi: 10.1016/S01662236(97)01132-6

Villringer, A., Planck, J., Hock, C., Schleinkofer, L., and Dirnagl, U. (1993). Near infrared spectroscopy (NIRS): a new tool to study hemodynamic changes during activation of brain function in human adults. Neurosci. Lett. 154, 101–104. doi: 10.1016/0304-3940(93)90181-J

Wang, D., Miao, D., and Blohm, G. (2012). Multi-class motor imagery EEG decoding for brain-computer interfaces. Front. Neurosci. 6:151. doi: 10.3389/fnins.2012.00151

Weiskopf, N. (2012). Real-time fMRI and its application to neurofeedback. Neuroimage 62, 682–692. doi: 10.1016/j.neuroimage.2011.10.009

Weiskopf, N., Mathiak, K., Bock, S. W., Scharnowski, F., Veit, R., Grodd, W., et al. (2004). Principles of a brain-computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI). IEEE Trans. Biomed. Eng. 51, 966–970. doi: 10.1109/TBME.2004.827063

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Yoshino, K., and Kato, T. (2012). Vector-based phase classiﬁcation of initial dips during word listening using near-infrared spectroscopy. Neuroreport 23, 947–951. doi: 10.1097/WNR.0b013e328359833b

Zhang, Q., Brown, E. N., and Strangman, G. E. (2007). Adaptive ﬁltering to reduce global interference in evoked brain activity detection: a human subject case study. J. Biomed. Opt. 12:064009. doi: 10.1117/1.2804706

Zhang, Q., Strangman, G. E., and Ganis, G. (2009). Adaptive ﬁltering to reduce global interference in non-invasive NIRS measures of brain activation: how well and when does it work?. Neuroimage 45, 788–794. doi: 10.1016/j.neuroimage.2008.12.048

Zhang, Y., Brooks, D., Franceschini, M., and Boas, D. (2005). Eigenvector-based spatial ﬁltering for reduction of physiological interference in diffuse optical imaging. J. Biomed. Opt. 10:011014. doi: 10.1117/1.1852552

Zimmermann, R., Marchal-Crespo, L., Edelmann, J., Lambercy, O., Fluet, M.C., Riener, R., et al. (2013). Detection of motor execution using hybrid

fNIRS-biosignal BCI: a feasibility study. J. Neuroeng. Rehabil. 10:4. doi: 10.1186/1743-0003-10-4

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 27 October 2014; accepted: 02 January 2015; published online: 28 January 2015. Citation: Naseer N and Hong K-S (2015) fNIRS-based brain-computer interfaces: a review. Front. Hum. Neurosci. 9:3. doi: 10.3389/fnhum.2015.00003 This article was submitted to the journal Frontiers in Human Neuroscience. Copyright © 2015 Naseer and Hong. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

