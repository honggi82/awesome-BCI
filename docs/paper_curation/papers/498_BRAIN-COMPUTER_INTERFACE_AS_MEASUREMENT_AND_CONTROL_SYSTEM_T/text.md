[Figure 2]

[Figure 3]

## METROLOGY AND MEASUREMENT SYSTEMS

Index 330930, ISSN 0860-8229 www.metrology.pg.gda.pl

BRAIN-COMPUTER INTERFACE AS MEASUREMENT AND CONTROL SYSTEM THE REVIEW PAPER

Remigiusz J. Rak, Marcin Kołodziej, Andrzej Majkowski

Warsaw University of Technology, Institute of the Theory of Electrical Engineering, Measurement and Information Systems, Koszykowa 75, 00-662 Warsaw, Poland, (remigiusz.rak@ee.pw.edu.pl, marcin.kolodziej@ee.pw.edu.pl, andrzej.majkowski@ee.pw.edu.pl)

## Abstract

In the last decade of the XX-th century, several academic centers have launched intensive research programs on the brain-computer interface (BCI). The current state of research allows to use certain properties of electromagnetic waves (brain activity) produced by brain neurons, measured using electroencephalographic techniques (EEG recording involves reading from electrodes attached to the scalp – the non-invasive method - or with electrodes implanted directly into the cerebral cortex - the invasive method). A BCI system reads the user's “intentions” by decoding certain features of the EEG signal. Those features are then classified and "translated" (on-line) into commands used to control a computer, prosthesis, wheelchair or other device. In this article, the authors try to show that the BCI is a typical example of a measurement and control unit.

Keywords: EEG, brain-computer interface, feature extraction, feature selection, measurement and control.

© 2012 Polish Academy of Sciences. All rights reserved

# 1. Introduction

A natural way for humans to communicate with the outside world is to use some individual muscles of the human body. Intentions born in the human brain are transmitted through the nervous system to selected parts of the body and stimulate their movement. Speech (throat, tongue, lips) is predominantly used for communication among people, as are also fingers in case of the sign language. Man-machine communication (MMC) means a type of communication where the same principles can be applied. Some simplification of the problem is a human-computer interaction (HCI) which traditionally involves a keyboard, touchpad and/or a mouse. An alternative way is to use a microphone and a sound board to issue voice commands or a camera to provide instructions in form of facial expressions and/or hand placement. Finally, we can imagine controlling a computer via electrical signals extracted from various parts of the peripheral nervous systems or even from the central nervous system - directly from the brain. The last type of communication is called a brain-computer interface (BCI). A summary of above-listed interfaces is illustrated in Fig. 1.

The main task of a brain-computer interface is to allow communication with the outside world for patients with severe stages of neurological diseases such as amyotrophic lateral sclerosis, cerebral subcortical stroke, Guillain-Barré syndrome, cerebral palsy or multiple sclerosis.

Measuring brain activity is centerpiece to BCI. However, detection of brain activity as such is not sufficient. BCI systems cannot read any “human thoughts". They can only classify some selected states of brain activity, associated with specific events or stimuli. Generally, the main task given to a user of the brain-computer interface is to “generate" appropriate models of brain activity by using certain mental strategies. Those strategies define what a BCI user

________________________________________________________________________________________________________________________________________________________________________________

Article history: received on Apr. 16, 2012; accepted on June 19, 2012; available online on Sept. 28, 2012; DOI: 10.2478/v10178-012-0037-4.

has to imagine or on what event his attention has to focus in order to “generate” appropriate EEG waves. Some strategies require long training.

Therefore, practical realization of a brain-computer interface requires several basic conditions to be fulfilled. Firstly, the system has to selectively measure brain activity. Next, user feedback has to be implemented. Finally, the system must have a “control block” to execute user's intentions. Devices that measure, in a passive manner, certain changes in brain activity, without the need to “read” user’s intentions (e.g. medical EEG recorders) are considered not to be BCI systems.

[Figure 5]

Fig. 1. Classification of man-machine interfaces.

Research in the field of brain-computer interfaces (BCI) has started in the 70s at the University of California (UCLA), Los Angeles, under a grant from the National Science Foundation. The paper “Toward Direct Brain-Computer Communication”, by Jacque Vidal can be considered a pioneer scientific publication, describing the study of BCI [1]. The very first international conference on BCI took place in 1999 (New York), where Jonathan R. Wolpaw formalized the definition of a BCI system [2]:

“A brain-computer interface (BCI) is a communication or control system in which the user’s messages or commands do not depend on the brain’s normal output channels. That is, the message is not carried by nerves and muscles and furthermore, neuromuscular activity is not needed to produce the activity that does carry the message”.

There are several other definitions of the same phenomenon in the literature, using slightly different terminology:

− Donoghue et al. [3]: “A major goal of a BMI (brain-machine interface) is to provide a command signal from the cortex. This command serves as a new functional output to control disabled body parts or physical devices, such as computers or robotic limbs” ;

− Levine et al. [4]: “A direct brain interface (DBI) accepts voluntary commands directly from the human brain without requiring physical movement and can be used to operate a computer or other technologies” ;

− Schwartz et al. [5]: “Microelectrodes embedded chronically in the cerebral cortex hold promise for using neural activity to control devices with enough speed and agility to replace natural, animate movements in paralyzed individuals. Known as cortical neural prostheses (CNPs), devices based on this technology are a subset of neural prosthetics, a larger category that includes stimulating, as well as recording, electrodes”.

Initially, the research was focused mainly on applications in the field of neuroprosthetics [6]. Its main purpose was to restore damaged senses such as hearing and vision or mobility of

patients. In neuroprosthetics, artificial devices are used to replace certain human organs/senses. In those cases, the brain has to "learn" how to read signals sent by the prosthesis or generate signals needed to control the prosthesis, throughout the entire nervous system. However, those signals are not required to be delivered directly to the brain or come directly from the brain (central nervous system), but rather to peripheral nerves. In general, it is assumed that in the field of neuroprosthetics a link can be established: nervous system (any part of it) ↔ device, while the BCI enables direct coupling: brain ↔ computer.

An artificial ear is a surgically implanted cochlear implant which can help a deaf person to retrieve hearing. The cochlear implant does not strengthen hearing, but works by direct stimulation of the auditory nerves leading to the brain. There are ongoing studies to improve the implant, whose trial electrodes are connected directly to the brainstem.

An artificial eye is a retina implant - a microelectronic circuit implanted into the eyeball and connected to a camera mounted in glasses. Signals read from the camera are sent from the implant to the brain through the nervous system to restore the ability to see for people with age-related macular degeneration.

Artificial limbs are artificial devices replacing body parts of patients after injuries and amputations, provided some muscles and nerves still function efficiently. Usually, prostheses are controlled by pulses from respective muscles. If we use for that purpose waves coming directly from the brain, obtained either in an invasive or noninvasive way, we have got a textbook brain-computer interface.

Mistakenly, the terms neuroprosthetics and brain-computer interface are often used interchangeably. This stems from the fact that both neuroprosthetics and the BCI are different means to achieve the same goal. Some elements of physical interfaces that could be connected to the human nervous system in order to improve senses, are given in Fig. 2 [7].

[Figure 7]

Fig. 2. Elements of physical interfaces that could be connected to the human nervous system.

It should be noted that the brain-computer interfaces differ from other interfaces because of using signals generated directly by the brain, rather than signals coming from muscle activity (electromyography, EMG). In fact, electrical signals coming from muscles are treated in that case as unwanted noise - so-called physiological artifacts. An example of such an artifact is an electrical signal generated while moving eyeballs (electrooculography, EOG). The problem is that usually the artifact signal amplitudes are grater (measured in mV) than the levels of the EEG signal (measured in µV).

As already mentioned, the possibility of human-computer communication, realized solely by means of signals coming directly from the brain, was suggested almost 40 years ago! A brain-computer interface proposed by J. Vidal in 1973 is illustrated in Fig. 3. However, only in the last decade of the twentieth century, several research centers worldwide made bold attempts to use electroencephalography (EEG) for direct communication between the brain and the computer.

[Figure 9]

Fig. 3. The brain-computer interface proposed by J. Vidal [8].

# 2. Methods of detecting brain activity

Brain activity - related to neuronal activity - boils down to the motion of electric charges which produce electric and magnetic fields. Brain-computer interfaces measure that activity of the brain which is the consequence of certain stimuli or mental task. Suitable sensors, placed or attached close to the selected areas of the brain, allow measurement of both electric and magnetic brain activity.

# 2.1. Invasive and semi-invasive methods

First experiments with BCI had an invasive character and typically for such cases, were conducted on animals (mice, rats, cats, monkeys). Invasive methods require surgical intervention, such as cutting the skin or opening the skull (intracranial recording). When the electrodes are placed on the surface of the cortex (partially invasive method), we are talking about electrocorticography (ECoG). ECoG does not damage neurons because the electrodes are not entered inside the brain. If the signal is measured with the electrodes placed inside the cerebral cortex (invasive method) we are talking about intracortical recording. In general, invasive methods have very good signal quality (high level of amplitude, low-noise) and very good spatial resolution. Internal electrodes allow registration of the activity of small areas of the brain or even individual neurons (brain cells). Artifacts associated with muscle movement are not burdensome in that case. However, those methods have a serious disadvantage. They require complex surgical intervention into the brain and attract very legitimate ethical controversy. Moreover, from a purely physical standpoint, long lasting signal recording with electrodes placed inside the brain can be problematic because the electrodes react with bodily fluids. It can significantly deteriorate the quality of measured signals.

# 2.2. Noninvasive methods

Of course, a lot more convenient to use is a brain-computer interface that operates in a non-invasive way. At least three different BCI designs of that sort have been developed thus far. The most commonly used is the one where the electrical signal is measured across the surface of the scalp (electroencephalogram) [9, 10].

Theoretically it is possible to use other non-invasive sensors placed on the surface of the head. These can be magnetoencephalography (MEG) that measures the magnetic activity of the brain and functional magnetic resonance imaging (fMRI) that measures the changes in oxygenation of active brain areas. Instead of fMRI, near infrared spectroscopy (NIRS) may also be used as a technique to measure the activity of the cerebral cortex [11, 12]. All these methods can be used in a brain-computer interface, but they have practical disadvantages. Equipment for the MEG and fMRI is cumbersome and very expensive. NIRS and fMRI have poor temporal resolution [7].

# 3. Electroencephalography (EEG)

Electroencephalography (EEG) is a non-invasive method of measuring the bioelectrical activity of the brain. Signals are acquired through electrodes placed on the surface of the scalp which detect potential changes caused by the activity of neurons of the cerebral cortex. EEG is very useful to monitor and diagnose epilepsy, sleep disorders, head trauma, brain tumors, disorders of consciousness and other brain conditions. The examination itself is not unpleasant for the patient, and lasts 15 to 20 minutes. During the test, the patient sits or lies comfortably with electrodes stuck to the scalp. Position the patient assumes depends on what is the purpose of the examination. Typically 6 to 64 electrodes are used (there are also known solutions using a much greater number of electrodes, e.g. 256). Usually, the electrodes are attached using an adhesive paste (gel) and are connected through an amplifier to a recording device.

[Figure 11]

Fig. 4. Distinctive rhythms (waves) of the EEG signal.

The measured EEG signal is largely an individual feature and varies depending on the psychophysiological state of a person. Both the signal amplitude and dominant frequencies undergo changes. It is assumed that a healthy human brain generates waves at frequencies ranging from 0.5 Hz to 100 Hz and amplitudes from several to several hundred µV. There are

some distinctive rhythms of the EEG signal, usually slightly different defined by various authors (Fig. 4): − alpha rhythms with frequencies from 8 Hz to 13 Hz, which are particularly evident during

the absence of visual stimuli, − beta rhythms with frequencies from 12 Hz to 30 Hz, which can be seen in the frontal region of the brain and are observed during concentration, − gamma rhythms found between 30 Hz – 100 Hz, which can be seen during motor activities, − delta rhythms with frequencies from 0.5 Hz to 4 Hz, which can be observed at stage 3 and 4 of sleep, − theta rhythms with frequencies from 4 Hz to 8 Hz, which occur during light sleep and are observed during hypnosis,

− mu motor rhythm in the range 8 Hz  12 Hz which is used in Motor Imagery (MI) BCI paradigm. In-depth studies of measured EEG signals led to the discovery of properties and rules that not only allow diagnosing diseases, but also identifying the specific signals evoked by certain stimuli. It was also found that the characteristic signals appear not only in the event of a real stimulus, but also in when somebody thinks (mental task) about doing a particular movement (muscle activity). Measurement of this activity could be the basis for constructing algorithms for human-computer communication and apparatus for controlling devices using “human thoughts”.

Normally during an examination, a set of 19 EEG electrodes is used, according to the socalled 10-20 system, which is recommended by the International Federation of Clinical Neurophysiology (IFCN) (Fig. 5). In a brain-computer interface which does not have to comply with medical standards, a different number of electrodes can be used, sometimes up to 512, according to need. The number of electrodes (BCI channels) and their distribution on the scalp is one of the major problems of BCI.

[Figure 13]

Fig. 5. Arrangement of electrodes according to the 10-20 standard [13].

Sticking a large number of electrodes to the surface of the scalp is a very laborious and time-consuming task. Normally, medical examination requires proper preparation of skin before sticking on the electrodes. The places where electrodes are located are applied with a special paste or gel. Moreover, the electrodes have to be stuck in right places. Many research

teams, including the authors, have tried to minimize the number of required electrodes, what would simplify preparation prior to an EEG signal measurement. It is very convenient to use a special cap with integrated electrodes. The best results are obtained with active electrodes (with built-in electronic amplifiers). In each case it is necessary to use gel, which from a practical point of view, is a huge inconvenience.

# 3.1. Evoked potentials

In addition to the traditional analysis of EEG signals, so-called evoked potentials (EP) [14] are used to support medical diagnostics. Evoked potentials are electrical signals measured on the surface of the head (with a few electrodes) after stimulation administered by an appropriate external stimulus. Most stimuli are visual (e.g. a flash of light), auditory or sensory, so we distinguish visual, auditory and somatosensory evoked potentials.

Also the term Event Related Potential (ERP) is commonly used. It denotes both EP as well as other brain responses that are the result of cognitive processes accompanying and following external stimuli or of preparatory mechanisms preceding motor action [15, 16].

Amplitudes of potentials measured on the scalp are very small. In addition, there is the spontaneous electrical activity of the brain. Therefore, when evoked potentials are used, a given stimulus is repeated and then the results are averaged. An example of averaged visual evoked potential is given in Fig. 6. At t = 0 stimulus exposure took place. One can see the socalled N75, P100 and N135 waves. By analyzing their latency a doctor can diagnose the state of the nervous system. These signals can also be implemented in a BCI.

[Figure 15]

Fig. 6. Example of visually evoked potential.

# 3.2. SSVEP

In BCI systems, the so called steady state visually evoked potentials (SSVEP) [17-20] can also be applied. SSVEP come from the visual cortex and are collected at the back of the skull. Let us assume that a user observes a light source (stimulus) pulsing with certain frequency (645 Hz). Such stimulus induces waves of the same frequency in the visual cortex of the brain. While analyzing the EEG signal, we can observe that this frequency in the signal is by far the most dominant. In case where the user is exposed to multiple light sources, pulsating with different frequencies, it is possible to determine, by measuring a dominant frequency of the EEG potential, which light source is observed by the user at a given moment. In practice,

each command sent to control the machine is usually associated with light source pulsating with a particular frequency. Interfaces based on SSVEP are relatively popular, because they operate outside the user's perception, do not require any training and are effective for most people. Unfortunately, there is a certain percentage of people who exposed to a pulsating light source can have an epilepsy attack.

# 3.3. P300

The most widely used and mostly written upon is the P300 evoked potential [21, 13]. This potential appears as a response to a visual or auditory stimulus awaited by a user, often highly emotionally. The P300 potential occurs after approximately 300 ms after the appearance of the stimulus - hence its name. The precise parameters, like amplitude and latency of the response to a stimulus, depend on many psychophysical factors and are unpredictable. In practice, for visual stimulation, the user observes a set of randomly illuminated signs like letters or other characters. At the moment of illumination of the sign expected by the user (on which the user focused his attention), an EEG potential of a small amplitude appears in the top area of the brain. In order to measure the P300 potential more precisely, the user watches the same character highlighted several times and his responses to stimuli are averaged. By moving his attention to another sign, the user is able to write a text. Often, to speed up selection of appropriate characters, the entire rows and columns are highlighted. A typical display panel that appears on the user’s monitor is presented in Fig. 7. Fig. 8 shows P300 and non-P300 responses and Fig. 9 - the location of brain activity generating the P300 potential.

[Figure 17]

Fig. 7. Typical panel displayed on the monitor screen of a BCI system based on the P300 potential [21].

[Figure 18]

Fig. 8. Localization of brain activity for the P300 potential [22].

As already mentioned, the advantage of interfaces built using evoked potentials is that they work outside human perception and therefore do not require much training. Several methods of using P300 and SSVEP interfaces have been proposed i.e. for writing text, moving the cursor, robot and intelligent building controlling [23, 24]. The principal drawback of those interfaces (P300 and SSVEP) is that they require the user to move his eyes. It is often difficult or not possible at all for a completely paralyzed person.

[Figure 20]

Fig. 9. P300 response and non-P300 response.

# 3.4. Potentials associated with imagining movement

The most technologically advanced and at the same time the most difficult to implement are asynchronous interfaces, which use signals generated as a result of imagining movement. It appears that the activity of the brain is very similar during movement and during imagining movement (mental task). Hence, the user does not need to make any movement, but only to imagine it. In addition, different areas of the brain are active when a person imagines movement of different body parts. This enables classification of user intents, and thus makes possible to build a system which would execute them and control the machine. For example, the thought of moving the right hand will turn a wheelchair to the right side, the left hand to the left, and so on. When analyzing the EEG signals invoked by imagining movement we talk about so called desynchronization and synchronization of brain potentials, associated with these intentions (Event-Related Desynchronization/Synchronization - ERD/ERS) [9, 25-29]. As already mentioned, proper measurement and classification of EEG signals is possible as a result of functional division of the cortical areas. Some knowledge of anatomy allows one to indicate regions of the brain which are associated with imagining movement of certain parts of the body.

For example, imagining left hand movement increases activity of the brain within the area of the C3 electrode. Imagining feet movement manifests itself the most by reading of the Cz electrode. The distinction between imagining movement of right and left foot with help of EEG is not possible. The corresponding brain areas are too close. The same is true for imagining movement of each finger. Fortunately, areas connected with hands, feet and tongue are characterized by pretty large topographical differences, and therefore they are usually used as subjects of mental tasks.

What is important, the user can learn through use of feedback (biofeedback as a matter of fact) how to generate patterns by imagining movement [30]. Certain features of imagining movement are visible in the EEG signal in frequency bands 8 Hz÷12 Hz and 18 Hz÷26 Hz.

# 4. A review of EEG signal processing algorithms for use in BCI

In order to interpret and classify measured EEG potentials it is necessary to first extract and select their features. The feature extraction process delivers a set of values (data) which essentially describe signal properties. It can take place directly in the time domain or after some transformation, for example to the frequency domain. Feature selection is commonly used in processing large data sets, in order to choose the best ones and at the same time, to reduce their number. This process, in many scientific papers, is considered centrepiece to classification accuracy.

[Figure 22]

Fig. 10. The block diagram of a typical solution of brain-computer interface.

There are many methods of feature selection known that are optimized for:

- - increasing the effectiveness of classification,
- - reducing computational effort,
- - reducing the amount of stored data,
- - reducing data redundancy.

A block diagram of a typical solution of a brain-computer interface is shown in Fig. 10.

# 4.1. Acquisition and preprocessing of EEG signal

Acquisition of an EEG signal is a very difficult task. In this paper, only non-invasive methods will be considered, where sensors (electrodes) are arranged across the surface of the scalp. Normally, single disk electrodes made of gold or Ag/AgCl are used. For DC derivations with EEG frequencies below 0.1 Hz, Ag/AgCl electrodes perform better than pure gold electrodes. Passive electrodes consist only of the disk material and are connected to the amplifier with the electrode cable. Active electrodes have a special preamplifier with gain of about 10. It makes the electrode less sensitive to environmental noise such as power line interference.

It is known that different parts of the brain are responsible for activity of various parts of the human body, but their arrangement may be subject to change. Hence the right placement of electrodes is not a trivial task. Signals measured from the electrodes have very small

amplitudes (from 10 μV to 100 μV) and are very noisy. Some artifacts are also introduced, physiological - muscle activity, eye movements, heart rate and other as well as technical such as the power line (50 Hz). The useful frequency band of EEG signal ranges from 0.5 Hz to 100 Hz. A typical raw, disturbed EEG signal is given in Fig. 11. The 50 Hz artifact clearly dominates.

[Figure 24]

Fig. 11. A typical raw, disturbed EEG signal.

For those reasons, conditioning of the EEG signals is very important. At first the signal has to be significantly amplified. Then, the voltage generated by the skin-electrode contact should be taken into account. Next, the power line frequency disturbance (50 Hz) should be filtered out and simultaneously the signal filtered by a low-pass filter. The amplified measurement signal, coming from several - sometimes even a few dozen - electrodes, is further converted into digital form and transmitted to the computer. There, some further preprocessing, now already in digital form (DSP), is carried out.

An important element of EEG signal preprocessing is spatial filtering: Laplace Filters (LF) or Common Spatial Patterns (CSP). The Laplace filter subtracts from the signal recorded from an electrode a quarter of the signal amplitude coming from adjacent electrodes. The CSP method is more advanced and based on selection of weights assigned to all electrodes, by using a special algorithm. The weights selection algorithm maximizes the difference of variances of the signal in a certain band (usually 8 Hz to 30 Hz) for different class signal parts. In more advanced BCI systems, Blind Signal Separation (BSS) methods are used. For example, Independent Component Analysis (ICA) is used for separation of signals and removing artifacts. Individual components of a real EEG signal are presented in Fig. 12.

[Figure 25]

Fig. 12. Real EEG signal components.

After preprocessing one obtains the filtered EEG signal, without suppressed artifacts, that can more clearly expose the expected features. It is worth noting that the operating speed of digital signal processing algorithms is very important, because they operate in real time.

# 4.2. Feature extraction

The next step is feature extraction from the EEG signal. Features which best describe expected properties of the signal are sought after. These features can be related to the shape of the waveform (time analysis), to individual frequency components (frequency analysis), to the power density spectrum, time-frequency analysis (Short-Time Fourier Transform - STFT, Wavelet Transform - DWT), autoregressive models (AR) or higher order statistical parameters (HOS) - variance, skewness, kurtosis [31].

The most commonly measured features are signal amplitudes (for P300 potential) or the spectral components (for SSVEP and ERD/ERS). For example, in case of the P300 potential, we know when to start the signal analysis. Hence, we can even average the signal, and then extract features that are used to train the classifier. In case of asynchronous interfaces (ERD/ERS) we do not know when to start and in order to extract features it is necessary to analyze the entire recorded signal. To do this, a window of fixed width is chosen. The window is shifted in time and for each of its positions the features are extracted from the signal [32, 33] (Fig. 13).

[Figure 27]

Fig. 13. Feature generation using a time window.

# 4.3. Feature selection

Feature vectors are obtained through extraction. For example, for a 1-second time window we typically obtain 40 features (FFT spectral components: 1 Hz ÷ 40 Hz) [34]. In this way, 1280 features are created in the 32-electrode system [35]. Note that the number of features can be very high, moreover some features may be redundant or unreliable (do not bring significant information). Hence we need a method to eliminate redundant features before classification – a selection.

Selection of features is a very difficult and important task. Although some characteristic features of an EEG signal assigned to specific events are known, they can be different for different users. Not only that, they can also vary from day to day and even from session to session for the same user. Therefore, feature selection is worth repeating before each use of the BCI interface.

There are many methods of feature selection – starting from fast ranking methods to end up with complex and time consuming methods. The simplest, ranking methods are based on tstatistics, K-Fisher coefficients or cross-correlation. More advanced methods use complex classifiers: Sequence Forward Selection (SFS) and genetic algorithms (GA). The Linear Dicriminant Analysis (LDA) is also often used. Implementation of these methods usually brings better results but is much more time consuming [36].

Another important task, partly connected with the feature selection process, is the best electrodes selection - from which the EEG signal should be measured. It can be done through counting signal features that are attributed to specific electrodes. Next, for a specific user, a limited number of electrodes can be used, which are located in designated areas. This considerably increases ergonomics of the BCI system [4, 15, 32, 33, 37, 38].

# 4.4. Classification

Certain characteristic features of the EEG signal (obtained in the selection process), are next used in the classification process. There are many algorithms that enable classification of EEG signal features. Most often used are: Support Vector Machine (SVM), Multilayer Perceptron (MLP), Naive Bayes Classifier (NBC), K - Nearest Neighbor Classifier – KNN, Linear Discriminant Analysis (LDA) and Hidden Markov Models (HMM). Note that an important component of any brain-computer interface is the calibration session, during which the measured EEG signals are analyzed and classifiers are trained. A summary of typical usage of different algorithms in brain-computer interfaces is presented in Table 1.

Table 1. A summary of algorithms associated with particular stages of brain-computer interface operations.

|Signal acquisition|Amplification, analog filtering, A/D conversion|
|---|---|
|Preprocessing|Digital filtering, spatial filtering: Laplace filters, common spatial patterns (CSP), blind signal separation (BSS), independent component analysis (ICA), Kalman filter.|
|Feature extraction|Discrete Fourier transform (DFT), spectrum density (PSD), discrete wavelet transform (DWT) of higher order statistics (HOS), autoregressive models (AR), principal component analysis (PCA).|
|Feature selection|Ranking methods: K-Fisher, statistics, non-ranking methods: genetic algorithms (GA), sequence forward selection (SFS), principal component analysis (PCA), linear discriminant analysis (LDA).|
|Classification|MLP neural networks, support vector machines (SVM), linear discriminant analysis (LDA), Bayesian classifier (NBC), nearest neighbour classifier (KNN), K-means, hidden Markov models (HMM), decision trees (DT), clustering (C).|

At the final stage, the output signal from the classifier is used to drive the actuator, which generates a certain event as a result of user intentions.

# 5. BCI systems quality evaluation

The quality of brain-computer interfaces can be measured in many ways. The simplest measure is the classification accuracy (classification rate), defined as the number of events correctly classified, divided by the total number of possible trials. Often, instead of the correct classification rate the classification error is given. Another way to determine the quality of

BCI systems is to give the effective speed of its operation. It is a measure which describes how many operations are done in a time unit (for example number of alphanumeric characters “written” per minute).

A more general measure is the Information Transfer Rate (ITR) [39]. ITR depends on the number of possible choices (classes), the time required to classify a single choice, and the average classification error. ITR (in bits per sample) for a BCI system with N possible choices is given by [39]:

[Figure 30]

P B N P P P

1 log log (1 )log

[Figure 31]

, (1)

[Figure 32]

2 2 2

N

1

where P denotes the accuracy of classification. If the time period for this classification is Tk , then the ITR can be expressed in bits per minute (B/Tk).

- Fig. 14 presents the dependence of the ITR expressed in bits per sample (B) on the

accuracy (P) of the classifier. Of course, the chart holds for a classifier accuracy greater than 1/N, where N is the number of choices.

[Figure 33]

Fig. 14. Dependence of the ITR in bits per sample (B) on the accuracy (P) of the classifier.

- Fig. 15 shows the graphical comparison of interfaces depending on the speed of operation

(ITR) and the time spent on learning to operate the interface.

[Figure 34]

Fig. 15. Comparison of BCI interfaces (speed versus the time needed to learn to operate the interface).

Typically, BCI systems based on evoked potentials (SSVP, P300) have a higher value of ITR than systems using movement imagining strategy (ERD/ERS). This is a consequence of the fact that systems which require focusing attention, usually have to detect a larger number of classes. There are practical interfaces that enable transmission of information at 30 bits/min, 60 bits/min or 90 bits/min [40].

Table 2 gives a brief summary of achievements in the construction of brain-computer interfaces [41]. Mental tasks (potentials), applied electrodes and the ITR coefficients have been presented.

The quality of operation of BCI, however, is not the same across the population and is a rather individual feature. Note that from an objective point of view, the speed of the interface is rather small. Nonetheless it is sufficient for people with disabilities, especially if the BCI system is the only way they can communicate with the environment.

Table 2. Summary of selected BCI systems.

|Research group|Mental tasks/ used potentials|Selected electrodes applied algorithms|Application|ITR (averaged) training time|
|---|---|---|---|---|
|Rochester University USA|P300 potential|Fz, Cz, Pz, P3, P4 averaging, threshold classifier|Synchronous control of five elements in a virtual building|12 bit/min minutes|
|Tübingen University Germany|CSP potentials|Fz, Pz, Cz Low Pass Filter threshold classifier|Synchronous switching on and off a device|6 bit/min months|
|Wadsworth Center USA|mu and beta rhythms|64 electrodes mu and beta rhythms linear classifier|Moving the cursor|22.5 bit/ min weeks|
|Graz University of Technology Austria|Imagining of left / right hand and feet movement|C3 and C4 alpha and beta rhythms LDA, HMM|Synchronous keyboard interface, control of prostheses|17 bit/min days|
|Tsinghua University, Beijing China|SSVEP potentials|O1 and O2 comparing the frequencies|Synchronous control by panel|27 bit/min minutes|
|University of Illinois USA|P300 potential|Fz, Cz, Pz, O1, O2 averaging, threshold classifier|66 virtual keyboard|9 bit/min minutes|
|ABI EU project JRC|Relax, imagining of right hand movement, rotate the cube, math calc.|F3, F4, C3, Cz, C4, P3, Pz, P4 Frequencies from 8 to 30 Hz, neural networks|Asynchronous control over mobile robot|33 bit/min (maximum) days|
|EPFL Switzerland|Imagining of finger movement, counting objects|Fp1, Fp2, F7, F3, F4, F8, T3, C3, C4, T4, T5, P3, P4, T6, O1, O2|Asynchronous control over a 2D object|25 bit/sec days|

# 6. Conclusions

Measuring specific brain waves throughout the EEG is not a trivial task. Such a system must implement typical functions known from measurement techniques like: data acquisition, data processing and data presentation. Signals acquired from electrodes have very small amplitudes and are strongly disturbed by noise and series of physiological and technical artifacts. Therefore those signals have to be carefully conditioned and then converted into

digital form. Next action is sophisticated signal preprocessing. After that, an EEG signal is ready for feature extraction. There are several feature extraction algorithms. Each of them is expected to generate features which will, to the greatest possible extent, describe selected properties of the signal in the current application. There is often need to eliminate some redundant features throughout the selection process. Finally, the classification process is implemented to feature vectors. Then some control process can be executed. At the same time BCI system quality should be evaluated.

Design and implementation of brain-computer interfaces is one of greatest challenges posed to modern science. This is proved true by numerous publications in scientific journals as well as extensive media coverage. The possibility of direct human-computer interaction (without manual manipulation of peripheral devices) opens new channels of communication in medicine, psychology, media and military. Use of such an interface in medicine is of particular importance, both in terms of studying human brain, and for supporting people affected by neurological inefficiency. Brain-computer interfaces can help people with severe neurological conditions such as amyotrophic lateral sclerosis, brain stroke, Guillain-Barré syndrome, amyotrophic lateral sclerosis, cerebral palsy or multiple sclerosis to communicate with the outside world. Many people suffer from amyotrophic lateral sclerosis, the neurodegenerative disease of the nervous system that destroys part of the central nervous system responsible for movement, but does not influence senses, cognitive abilities and intellect. People, who suffer from it, gradually lose control over their own body and within 2 to 3 years reach a state where they have no ability to communicate with the environment. Another group of people who could communicate with the environment by BCI are those who have strokes, particularly the brain stem strokes. Victims of traffic accidents, which resulted in damage to the cervical spinal cord, could also belong to those groups.

The barriers to dissemination of direct brain-computer communication methods, using the EEG signals, are high price and complexity of the apparatus. In fact the amplifiers used for BCI are designed for applications in medical diagnostics, containing from 32 to 512 channels. In addition, they are usually designed to work with other types of medical equipment, often through a specialized interface whose communication protocol is not widely known. This raises the need for a dedicated, cheaper amplifier and other signal conditioning modules for use in BCI. Although, according to studies, it is possible to reduce the number of electrodes, their minimum number and location remain unknown. Besides, deployment of electrodes may be different for each user. The knowledge and intuition of a doctor is most helpful here. Also important is the fact that the features of the EEG signal can change with changes in mental states of the user. Additionally, in ERD/ERS interfaces the features strongly depend on the process of "imagining movement." Furthermore, the tools that enable quick and effective selection of the best features have not been tested thoroughly. Resolving those issues will help to overcome barriers to effective use of brain-computer interfaces in practice.

# Acknowledgements

This work was supported in part by the Ministry of Science and Higher Education, Poland. Grant No. Nr N N510 526239.

# References

- [1] Vidal, J.J. (1973). Toward direct brain-computer communication. Annu. Rev. Biophys. Bioeng., 2, 157-180.
- [2] Wolpaw, J.R., Birbaumer, N., McFarland, D.J., Pfurtscheller, G., Vaughan, T.M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol, 113, 767-791.

- [3] Donoghue, J.P. (2002). Connecting cortex to machines: recent advances in brain interfaces. Nat. Neurosci, 5, 1085-1088.
- [4] Kołodziej, M., Majkowski, A., Rak, R. (2012). Linear discriminant analysis as a feature reduction technique of EEG signal for brain-computer interfaces. Electrotechnical Review, 88, 28-30.
- [5] Schwartz, A.B. (2004). Cortical neural prosthetics. Annu. Rev. Neurosci, 27, 487-507.
- [6] Farwell, L.A., Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalographz Clin. Neurophysiol, 70, 510-532.
- [7] Graimann, B., Allison, B., Pfurtscheller, G. (2011). Brain–Computer Interfaces, ISBN: 978-3-64202090-2.
- [8] Vidal, J.J. (1977). Real-time detection of brain events in EEG. In IEEE Proc: Special Issue on BiolSignal Processing and Analysis, 65, 633-664.
- [9] Dornhege, G., Blankertz, B., Curio, G., Mulle, K. (2004). Boosting bit rates in non-invasive EEG singletrial classifications by feature combination and multi-class paradigms. IEEE Transactions on Biomedical Engineering, 51, 993-1002.
- [10] Wolpaw, J.R., McFarland, D.J., Vaughan, T.M. (2000). Brain-computer interface research at the Wadsworth Center. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 8, 222-226.
- [11] Bauernfeind, G., Leeb, R., Wriessnegger, S.C., Pfurtscheller, G. (2008). Development, set-up and first results for a one-channel near-infrared spectroscopy system. Biomedizinische Technik, 53, 36-46.
- [12] Burghoff, M., Albrecht, H.-H., Hartwig, S., Hilschenz, I., Körber, R., Sander-Thömmes, T., Scheer, H., Voigt, J., Trahms, L. (2009). Squid system for meg and low field magnetic resonance. Metrol. Meas. Syst., 16(3), 371-376.
- [13] Sanei, S., Chambers, J.A. (2007). EEG Signal Processing, ISBN: 978-0-470-02581-9.
- [14] Celesia, G.G., Peachey, N.S. (2004). Visual Evoked Potentials and Electroretinograms. In E. Niedermeyer and F.H.L da Silva (Eds.), Electroencephalography: Basic principles, clinical applications, and related fields, Williams and Wilkins, Baltimore, MA.
- [15] Kołodziej, M., Majkowski, A., Rak, R. (2011). A new method of EEG classification for BCI with feature extraction based on higher order statistics of wavelet components and selection with genetic algorithms. Adaptive and Natural Computing Algorithms Lecture Notes in Computer Science, 6593, 280-289.
- [16] Donchin, E., Ritter, W., McCallum, C. (1978). Cognitive psychophysiology: the endogenous components of the ERP. Brain-event related potentials in man, Academic, New York.
- [17] Regan, D. (1977). Steady-state evoked potentials. J. Opt. Soc. Am., 67,1475-1489.
- [18] Allison, B.Z., McFarland, D.J., Schalk, G., Zheng, S.D., Jackson, M.M., Wolpaw, J.R. (2008). Towards an independent brain-computer interface using steady state visual evoked potentials. Clin. Neurophysiol, 119, 339-408
- [19] Byczuk, M. (2011). Rotary visual stimulator for research into visual evoked potentials. Electrotechnical Review, 87, 49-51.
- [20] Byczuk, M., Poryzała, P., Materka, A. (2011). On possibility of stimulus parameter selection for SSVEPbased brain-computer interface. Advances in Intelligent and Soft Computing, 103, 57-64.
- [21] Donchin, E., Spencer, K.M., Wijesinghe, R. (2000). The mental prosthesis: assessing the speed of a P300based brain-computer interface. IEEE Trans Rehabil. Eng., 8, 174-179.
- [22] Schalk, G., McFarland, D., Hinterberger, T., Birbaumer, N., Wolpaw, J. (2004). BCI2000: A GeneralPurpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering, 51, 10340-10430.
- [23] Byczuk, M., Materka, A. (2003). EEG signal-based human-computer communication. Department of Electrotechnics of Łódź University of Technology. (in Polish)
- [24] Nijholt, A., Tan, D. (2008). Brain-Computer Interfacing for Intelligent Systems. Intell. Syst. IEEE, 23, 72-79.
- [25] Hyekyoung, Lee, Cichocki, A., Seungjin, Choi. (2009). Kernel nonnegative matrix factorization for spectral EEG feature extraction. Neurocomputing, 72, 3182-3190.

- [26] Pfurtscheller, G. (1999). EEG event-related desynchronization (ERD) and event-related synchronization (ERS). In: E. Niedermeyer and L.F.H. da Silva (Eds.), Electroencephalography: Basic principles, clinical applications and related fields. Williams and Wilkins, Baltimore, MD.
- [27] Rak, R., Kołodziej, M. (2008). Implementation of EEG signal spectrum in Brain-Computer Interface design. Electrotechnical Review, 84, 283-286. (in Polish)
- [28] Ince, N., Fikri, Goksu, Tewfik, A., Sami, Arica. (2009). Adapting subject specific motor imagery EEG patterns in space–time–frequency for a brain computer interface. Biomedical Signal Processing and Control, 4, 236-246.
- [29] McFarland, D.J., Miner, L.A., Vaughan, T.M., Wolpaw, J.R. (2000). Mu and Beta rhythm topographies during motor imagery and actual movements. Brain Topogr., 12, 117-86.
- [30] Elbert, T., Rockstroh, B., Lutzenberger, W., Birbaumer, N. (1980). Biofeedback of slow cortical potentials. I. Electroencephalogr Clin. Neurophysiol, 48, 293-301.
- [31] Bang-hua, Yanga, Guo-zheng, Yanb, Ting, Wub, Rong-guo, Yanb. (2007). Subject-based feature extraction using fuzzy wavelet packet in brain–computer interfaces. Signal Processing, 87, 1569-1574.
- [32] Kołodziej, M., Majkowski, A., Rak, R. (2009). Matlab FE_Toolbox - an universal utility for feature extraction of EEG signals for Brain-Computer Interface realization. Electrotechnical Review, 86, 44-46.
- [33] Kołodziej, M., Majkowski, A., Rak, R. (2010). A new method of feature extraction from EEG signal for brain-computer interface design. Electrotechnical Review, 86, 35-38.
- [34] Incea, N., Ahmed, H. Tewfika, Sami, Aricab. (2007). Extraction subject-specific motor imagery time– frequency patterns for single trial EEG classification. Computers in Biology and Medicine, 37, 499-508.
- [35] Majkowski, A., Kołodziej, M., Rak, R. (2012). Implementation of automatic feature selection methods for BCI realization IEEE International Instrumentation and Measurement Technology Conference - I2MTC.
- [36] Gutiérrez, D., Escalona-Vargas, D. (2010). EEG data classification through signal spatial redistribution and optimized linear discriminants. Computer methods and programs in biomedicine, 97, 39-47.
- [37] Kołodziej, M., Majkowski, A., Rak, R. (2010). Implementation of genetic algorithms to feature selection for the use of brain-computer interface. Electrotechnical Review, 87, 71-73.
- [38] Majkowski, A., Kołodziej, M., Rak, R. (2012). Implementation of selected EEG signal processing algorithms in asynchronous BCI. In Proc. IEEE International Symposium on Medical Measurements and Applications – MeMeA’2012.
- [39] Obermaier, B., Neuper, C., Guger, C., Pfurtscheller, G. (2001). Information Transfer Rate in a FiveClasses Brain–Computer Interface. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 9, 283-288.
- [40] Wolpaw, J.R., Loeb, G.E., Allison, B.Z., Donchin, E., Nascimento, O.F., Heetderks, W.J., Nijboer, F., Shain, W.G., Turner, J.N. (2006). BCI Meeting 2005 – workshop on signals and recording methods. IEEE Trans. Neural Syst. Rehabil. Eng.: A Pub IEEE Eng. Med. Biol. Soc., 14, 138-141.
- [41] Garcia, M.G.N. (2004). Direct brain-computer communication through scalp recorded EEG signals. Ëcole Polytechnique F D Rale De Lausanne.

