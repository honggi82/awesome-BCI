[Figure 1]

[FiachraMatthews,BarakA.Pearlmutter,TomasE.Ward,

ChristopherSoraghan,andCharlesMarkham]

©STOCKBYTE&DIGITALVISION

## Hemodynamics for Brain-Computer Interfaces

[Opticalcorrelatesofcontrolsignals]

# T

his article brings together the various elements that constitute the signal processing challenges presented by a hemodynamics-driven functional near-infrared spectroscopy (fNIRS) based brain-computer interface (BCI). We discuss the use of optically derived measures of cortical hemodynamics as control signals for next generation BCIs. To this end we present a suitable introduction to the underlying measurement

principle, we describe appropriate instrumentation and highlight how and where performance improvements can be made to current and future embodiments of such devices. Key design

Digital Object Identifier 10.1109/MSP.2007.909011

1053-5888/08/$25.00©2008IEEE IEEE SIGNAL PROCESSING MAGAZINE [87] JANUARY 2008

the modality, we will explore the unique aspects of fNIRS and its potential for use in a BCI in this regard. Taking a systems perspective, we will explore avenues for improvement of fNIRS-BCI systems in terms of signal enhancement. This will include examining the capabilities of NIRS and the physiological effects it can observe, the importance of the hardware in maintaining signal quality, reviewing the current status of fNIRS-BCI research, and a detailed review of digital signal processing methods and feature extraction techniques. Finally we will discuss the implications of this article with reference to furthering research into fNIRS-BCI.

elements of a simple fNIRS-BCI system are highlighted while in the process identifying signal processing problems requiring improved solutions and suggesting methods by which this might be accomplished.

#### INTRODUCTION

A BCI is a mechanism that allows a user to interact with the outside world through the measurement of correlates of neural activity associated with mental processes. Interest in such devices has increased due to technological advancement, reduction of equipment costs and improved signal processing methods.

BCIs can be characterized in a number of ways based on the different modalities of physiological measurement (electroencephalography (EEG) [1], [2]; electrocorticography (ECoG) [3]; magneto-encephalography (MEG); magnetic resonance imaging (MRI) [4], [5]), mental activation strategies (dependent versus independent), degree of invasiveness, and so on.

METHOD OF NEAR-INFRARED SPECTROSCOPY

THE HEMODYNAMIC RESPONSE TO NEURAL ACTIVATION

During mental activation, neural metabolism is supported through a localized vascular response that causes an inrush of oxygen-rich blood to the active area and surrounding tissue. In general, this manifests as an increase in oxyhemoglobin (HbO) and a decrease in deoxyhemoglobin (Hb). Figure 1 is an example of the typical hemodynamic response to activation [6]. Such features are the measurement basis of existing fNIRS-BCIs.

While EEG is the most widespread BCI modality, increasingly researchers are investigating alternative and perhaps ultimately complementary measurements from which to derive suitable control signals for BCIs. In this article we will focus on the detection of hemodynamic correlates of neural activity using fNIRS and its application to BCI. In particular, we take a complete performance perspective into account for a survey, review, and analysis of the key signal processing challenges that present themselves throughout the system including hardware, digital signal processing, and feature extraction.

#### NEAR-INFRARED SPECTROSCOPY

Near-infrared spectroscopy (NIRS) is an analysis method that uses electromagnetic radiation in the near-infrared spectrum (around 650–950 nm). Radiation at these wavelengths is passed through a substance and the collected light intensities are used to determine the properties of the substance. NIRS has been used in the areas of quality control,

The main goals in BCI design are maximizing information throughput and usability. This entails careful design of each component of the system. As optimization of communication throughput, in particular, is heavily dependent on

pharmaceuticals, and medical diagnostics [7] to name but a few applications. In the context of this article, discussion is confined to the ability of NIRS to interrogate cerebral tissue to determine functional brain activity.

Rest Activation Rest

× 10−6

Oxy-Hemoglobin

Deoxy-Hemoglobin

Time (s) dConcentration(mM.cm)

| | |
|---|---|
| | |
| | |

| | |
|---|---|
| | |
| | |

#### FUNCTIONAL NEAR-INFRARED SPECTROSCOPY

The scalp, skull, and surrounding tissues of the brain exhibit an optical window of tissue transparency in the near-infrared (NIR) range allowing interrogatory measurements of neurochemistry at the cortex [8]. Initially used for monitoring cerebral oxygen saturation, subsequent technological developments yielded sensitivity sufficient for localized tissue oxygenation measurements [9]. Using the changes in detected NIR light intensities, it is

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

−0.5

−1

−1.5

−2

0 5 10 15 20 25

- [FIG1] Average of motor cortex activations. Vertical dashed lines denote the beginning and end of the activation.

digm are essential elements in obtaining repeatable performance, optimizing the signal-to-noise ration (SNR) and hence reducing the workload on the DSP component. This element of the signal pipeline is crucial for improved performance and is discussed here.

possible to calculate concentrations of absorbers (termed chromophores) in the tissue such as Hb and HbO. The relationship between light intensities and chromophore concentration is commonly expressed using the Beer-Lambert law.

#### LIGHT ABSORPTION AND CHROMOPHORE CONCENTRATION

#### INTRODUCTION

Measurement methods for NIRS are primarily based around three distinct technologies: continuous wave (cw), frequency domain, and time domain. The latter two allow for direct measurement of the DPF and hence can be used for absolute

BEER-LAMBERT LAW The Beer-Lambert law states that the attenuation in light intensity is proportional to the concentration of an absorbing compound in a nonabsorbing medium and the path length of the photons.

measurement of chromophore concentration. Continuous wave systems yield only relative concentration measurements but are, in contrast, relatively simple to implement. As a fNIRS-BCI only requires knowledge of the relative concentration changes, the research favors this modality and hence this paper will only deal with

### BCI SYSTEMS REPRESENT ARGUABLY THE ULTIMATE IN HUMAN-COMPUTER INTERFACE TECHNOLOGY.

If we let A be the attenuation in decibels; I0, the intensity of the incident light; I1, the intensity of the detected light; l, the distance that the light travels through the material (the path length); c, the concentration of chromophores; α, the absorption coefficient of the chromophore; λ, the wavelength of the light; and k, the extinction coefficient then

its operation. More detail on other NIRS modalities can be found in [11]. cwNIRS systems can be described in terms of their optical sources, detectors and amplifier technology.

4πk λ

I0 I1

#### LIGHT SOURCE

A = αlc = log10

(1)

, α =

The most basic cwNIRS system requires a light source that can be modulated by a carrier wave from dc up to several kilohertz. Both laser diodes and LEDs can achieve this. The development of high power NIR LEDs, such as those used by Coyle et al. [12] (average output power 10 mW) allow sufficient photons to reach the depths necessary for cortical tissue interrogation. Perpendicular application of the LEDs with a narrow beam angle (e.g., 8◦) is also important for maximum light delivery since light incident on the scalp at grazing angles is less likely to be transmitted through the epidermis [13]. Laser diodes are commonly used in NIRS but the short transport scattering length (the distance over which a collimated beam effectively becomes diffuse) at these wavelengths remove any coherency advantages although for quantitative measurements, their stability may be preferable.

Equation (1) provides a simple means to relate light absorption to underlying chemical concentration.

MODIFIED BEER-LAMBERT LAW

When considering the interrogation of brain tissue it is necessary to modify this equation to account for the highly scattering nature of the medium. The modification must include an additive term to account for scattering losses and a term for the change in the optical path length

I0 I1 = α l cDPF + G. (2)

A = log10

A key requirement for reliably separating the Hb and HbO components is the choice of appropriate wavelengths. Studies performed by Uludag et al. [14] shows that the careful selection of wavelengths greatly increases the quality of the hemodynamic signal. Interestingly, these researchers also indicate that the wavelengths used by some commercial systems are not the optimal combinations.

The differential path length factor (DPF) is a scaling term to account for the increased path length due to scattering while G is an additive scalar term incorporating the scattering losses. The DPF can be determined from experimentally derived studies [10] making the key measurement the change in transmitted light intensity. It is this change that constitutes a signal correlated with neural activity. An fNIRS-BCI utilizes this measurement principal along with instrumentation capable of measuring A accurately to determine optical correlates of hemodynamics.

#### DETECTORS

Due to the high attenuation (of the order of 70 dB) at even optimal wavelengths, it is important to have detectors of high sensitivity and quantum efficiency [12]. In practice this leads to two device options: photomultipliers and avalanche photodiodes (APDs). Both devices can be operated in current mode or photon-counting mode. Photon-counting methods

#### fNIRS INSTRUMENTATION DESIGN

As with any physiological measurement, the standardization of sensor placement, coupling, signal preprocessing, and conditioning together with a well-described experimental para-

(Ametek 7265), two APDs (Hamamatsu C5460-01), two fiber optic bundles, an LED driver driving nine triple wavelength LEDs (760 nm, 800 nm and 880 nm, Opto Diode Corp. APT0101), and function generators. Two data acquisition systems are employed (NI USB6009 DAQ and Biopac MP100). The first is for simple online subject interaction, and the other is for higher resolution data capture for offline analysis. This system achieved 50–85% accuracy in online trials. Offline analysis and classification increased this to 70–90%. In this system only the HbO signal is processed to yield features for classification.

Low-Frequency Oscillations

1,000

Magnitude(a.u.)

800

Heart Rate

600

Breathing Rate

400

200

0

0.5 1 1.5 2 2.5

Ranganatha et al., harness a commercial, multichannel NIRS measurement system (OMM-1000, Shimadzu Corporation). This system emits three wavelengths (780, 805, and 830 nm) with an average output power of 3 mWmm−2. Although no online experimental results are presented this system achieved similar results to Coyle’s offline analysis but used both Hb and HbO trends to classify a response which is believed to be a more accurate measure of volitional activation [22].

Frequency (Hz)

- [FIG2] Sources of noise in the fNIRS signal.

given high integration times can provide signals with low noise, although in some cases the count rates and response times limit their application. Current-based detectors require brighter sources to achieve similarly good statistics. Photomultipliers in general have lower dark currents, high-

NOISE REMOVAL AND FEATURE EXTRACTION

- er sensitivity, and lower quantum efficiency than APDs. Practically, integrated APDs with protection, amplification and bias electronics are physically more robust and simplify the implementation of a cwNIRS system.

NOISE REMOVAL

The energy of the optical fNIRS signals are dominated by noise of both physical and physiological origin. Subject move-

ment, heartbeat, respiration effects, and other physiological trends make functional activation difficult to detect without substantial post-processing. Figure 2 shows the frequency spectrum of a single wavelength fNIRS time series during an experiment. The physiological noise sources are particularly apparent in this domain.

#### SIGNAL RECOVERY

Even with highly accurate optical detection technologies, cwNIRS systems require algorithms to recover the transmitted signal recorded in very noisy environments. One method of signal recovery employed by fNIRS-BCI is the use of lock-in amplifiers [12]. Lock-in amplification can recover a signal on a known carrier wave and act as a very narrow-band filter.

A BCI IS A MECHANISM THAT ALLOWS A USER TO INTERACT WITH THE OUTSIDE WORLD THROUGH THE MEASUREMENT OF CORRELATES OF NEURAL ACTIVITY ASSOCIATED WITH MENTAL PROCESSES.

Many approaches to fNIRS noise removal evolved from methods used in other brain scanning modalities. Experiences with EEG and fMRI serve as good examples for extension to fNIRS. Many of these methods have been implemented in clinical fNIRS research but have yet to be incorporated into an fNIRS-BCI system. There are still many avenues available to improve the SNR prior to feature extraction in an fNIRS-BCI. This section explores the major sources of noise and examines the methods that have been implemented to deal with these artifacts in all areas of fNIRS research. We will discuss these methods and highlight those that may prove most useful to fNIRS-BCIs.

Another possible avenue for developing a more scalable multichannel NIRS system is to use a software-based frequency demultiplexing system. Specteral analysis is performed on the data in software to recover the raw intensities at each frequency [15]. Software demultiplexing greatly reduces the cost and size of the equipment needed for a multichannel system in comparison to a multiple hardware lock-in based system.

CURRENT EMBODIMENTS OF fNIRS IN PROTOTYPE BCI SYSTEMS

Published descriptions of fNIRS-BCI include those developed by Coyle et al. [12], [16]–[18] and Ranganatha et al. [19]–[21]. Such systems give an excellent exposition of the methods, technologies, and mental strategies for a basic fNIRS-BCI.

MOTION ARTIFACT

Subject motion is a source of significant disruption in the fNIRS signal and is termed motion artifact. Motion artifact disruption is caused by many different factors. Movement of the optodes and detectors can change the angle of incidence

The system by Coyle is a custom-built, continuous-wave fNIRS-BCI. The system is composed of two lock-in amplifiers

[TABLE 1] NOISE REMOVAL ALGORITHMS IMPLEMENTED FOR INDIVIDUAL ARTIFACTS. ENTRIES WITHOUT REFERENCES WERE IMPLEMENTED BY THE AUTHORS.

##### FILTERING TECHNIQUE PURPOSE REAL-TIME IMPLEMENTATION CITATION USE IN BCI

MOVING AVERAGE FILTER CARDIAC/RESPIRATION Y [17] Y DETRENDING MAYER WAVE N [25] N FIR FILTERING CARDIAC/RESPIRATION Y Y PULSE REGRESSION CARDIAC/RESPIRATION N [25] N PEAKS AVERAGE CARDIAC/RESPIRATION N [18] Y SINE FIT MAYER WAVE N [18] Y WAVELET DENOISING FAST SIGNAL N [29] N ICA FAST SIGNAL N [29] N LMS ADAPTIVE FILTERING CARDIAC Y Y LMS ADAPTIVE FILTERING MOTION ARTIFACT Y N LMS ADAPTIVE FILTERING MAYER WAVE Y N WEINER FILTERING MOTION ARTIFACT N [23] N WEINER FILTERING CARDIAC/RESPIRATION N [23] N SAVITZKY-GOLAY SMOOTHER CARDIAC Y Y

Reducing this interference is a problem in nearly all functional brain scanning modalities. The simplest approach to removal of this noise is standard FIR and infinite impulse response filtering. Online fNIRS-BCIs have used moving average filters to

of the transmitted and detected light, increasing the affect of the reflectance of the skin surface. Motion can cause an increase in blood flow through the scalp or, more rarely, an increase in blood pressure in the interrogated cerebral regions. Orientation of the head can effect the signal due to gravity’s effect on the blood [23]. These compounded effects are a significant source of noise especially if the head is not physically restricted. Implementing fNIRS in a completely mobile scenario increas-

### WE FOCUS ON THE DETECTION OF HEMODYNAMIC CORRELATES OF NEURAL ACTIVITY USING fNIRS AND ITS APPLICATION TO BCI.

reduce the effect of the spikes prior to the thresholding for feature extraction [17].

The previously mentioned analysis software HomER [24] uses a Type II Chebyshev low-pass filter by default to smooth out the heart rate [20]. It is also possible to calculate an average point over the course of each beat. A line is then interpolated through these points to produce the cleaned signal [18]. Another approach is to use a system where all the beats are averaged. This average waveform is then matched against each individual beat using a linear regression algorithm and the resulting waveform is subtracted from the signal [25].

- es these effects. The ambulatory interference of walking and totally free head motion would further increase the amplitude and change the nature of the artifact.

A common approach to motion artifact removal in many brain scanning modalities is that of adaptive finite impulse response (FIR) filtering. This requires the collection of additional information about the noise to alter the filter coefficients. Such information can be collected through accelerometers attached to the head to record any movement. The advantage of this approach is that it makes real-time filtering possible. Weiner filtering functions effectively for offline cleaning of data in both stationary and ambulatory scenarios but has yet to be implemented in a fNIRS-BCI [23].

Effects of Postural Differences on Spectral Characteristics

|Standing Seated Supine|
|---|

[Figure 2]

0.25

As motion artifacts cause the largest statistical variance within the data set, it is possible to implement a principal component analysis filter to remove it. This method is used in the NIRS analysis software ‘HomER’ [24] and has performed well in offline BCI analysis [20].

Magnitude(a.u.)

0.2

0.15

0.1

PULSE ARTIFACT

0.05

The heart beat constitutes a major source of noise when searching for target hemodynamic responses with fNIRS. The systoles cause periodic increases in blood pressure and volume through the body. This increases the absorption of NIR radiation, leaving a periodic series of spikes in the data. Generally this interference resides between 0.8–1.2 Hz.

0

0 0.2 0.4 0.6 0.8 1 1.2

Frequency (Hz)

[FIG3] Effect of subject position on Mayer wave [12].

versus blood oxygenation and look into strategies for differentiating left versus right activation.

Currently another method in use for offline fNIRS-BCI analysis is the Savitzky-Golay (SG) smoothing filter. The SG filter performs a local polynomial regression over a specified length while still preserving the relative maxima, minima, and width of the signal distribution. These can be lost using many standard filtering techniques.

CEREBRAL BLOOD VOLUME

An increase in rCBV is indicative of possible activation in the interrogated region. Using fNIRS this increase in rCBV is characterized by a decrease in detected light intensity because of higher absorption in the tissue.

Experiments have also been conducted using least mean squares (LMS) and recursive mean squares (RMS) adaptive FIR filters using modeled data but the nonstationary nature of the pulse artifact presents a more difficult challenge.

BLOOD OXYGENATION

Using the modified Beer-Lambert law outlined earlier, it is possible to calculate the concentration changes in both Hb and HbO. These have proven to be a more reliable way to confirm an activation [9]. fNIRS-BCI implementations have done this

MAYER WAVE Spontaneous low-frequency oscillations of approximately 0.1 Hz exist within the signal and are generally referred to as the Mayer Wave [26], although it also has been termed as vasomotion, V-signal, and spontaneous oscillations [27]. Its causes are not well understood but the dominant hypothesis is that it relates to baroreceptormediated blood pressure control [26]. Placing a subject in a near-supine position reduces the amplitude of the oscillation (Figure 3) but does not entirely eliminate it. The Mayer Wave is a particularly problematic noise source given its spectral overlap with volitionally induced hemodynamic changes. One approach to its removal is to use an algorithm from IEEE Standard 1057 to fit a sine wave to the data [18]. This sine wave is then subtracted from the data to produce the cleaned signal. As with the pulse artifact, LMS and RMS adaptive FIR filters have been tested experimentally using modeled data.

in two ways. The first follows HbO trends alone and the second combines the trends of both Hb and HbO to more accurately define an activation [22]. During an activation HbO rises sharply in the first 3–5 s. This is due to the “watering-the-garden” effect

### MOTOR CORTEX ACTIVATION IS THE MOST COMMON MENTAL STRATEGY FOR fNIRS-BCI CONTROL.

where the brain oversaturates an active area to supply neurons with oxygen [22]. Comparing the HbO levels during activation to an average of those collected during the rest period is the first simple method of classifying an activation [17].

Another feature extraction method relies on both Hb and HbO trends. As can be seen in Figure 1, the Hb level decreases during an activation. Studies have shown that this is a more reliable indicator of activation in the interrogated region [22]. This is because the larger HbO response can perfuse into other areas and a HbO rise may not be directly correlated with an experimentally derived activation.

More speculatively, a recent study was carried out with reference to the fast oxygen response in capillary event (FORCE) [30]. This study stated that there was an oxygen exchange event occurring in capillaries in the activated region. This event is detectable using NIRS and occurs faster than the Hb/HbO trends. Should these results be adequately replicated this effect holds promise for improving the throughput in an fNIRS-BCI.

NOISE REMOVAL METHODS

Table 1 lists the most common signal processing methods used in fNIRS. Two of the entries (ICA, wavelet denoising) have only been employed in the retrieval of the fast optical response to neuronal activation [28]. This signal is believed to be associated with the propagation of the action potential and is much smaller than the vascular response described up to now. Methods used in the search for this elusive signal may well be applicable in the area of fNIRS-BCI research. Many of these methods are, as yet, not implemented in a BCI but there are significant gains possible from their use.

RIGHT-LEFT SEPARATION

During a single handed activation it is assumed that only the contralateral hemisphere of the brain demonstrates a response. It has been shown experimentally that both hemispheres can respond similarly [12]. It is therefore necessary to develop systems to correctly classify differences between left and right activations. Two methods that have improved classification rates are hidden Markov models (HMMs) and support vector machines (SVMs). Using finger tapping and motor imagery experiments on five subjects these systems were able to achieve accuracy above 80% for finger tapping and above 70% for motor imagery [20]. HMM performed best overall, bettering SVM by 16% in motor imagery classification.

#### FEATURE EXTRACTION/CLASSIFICATION

Motor cortex activation is the most common mental strategy for fNIRS-BCI control. Using both hemispheres of the brain separately for control purposes offers the advantage of increasing the number of channels available. Left- versus right-hand activation detection can be difficult due to the mirroring of activations in both hemispheres during motor tasks. The following section will outline the methods used for interpreting activations in online and offline situations. We will investigate the advantages of utilizing changes in regional cerebral blood volume (rCBV)

the possibility of a composite signal based on both measurement modalities may hold the key to a higher bandwidth communication stream in future systems.

Feature extraction and classification represent the final step in an optical BCI design process. Ultimately the overall performance is determined through careful consideration of every stage in the signal processing schema.

#### CONCLUSIONS

BCI systems represent arguably the ultimate in humancomputer interface technology. Notwithstanding that the basic principle has been realized in very many prototypes and some commercial devices, there is concerted and accelerating development in realizing faster and more convenient systems. Consequently, there has been inquiry into alternative means for

DISCUSSION The majority of the working examples of BCI technology utilize electrical measurements of neural activity to ascertain user intention. Such systems offer the signal processing community an array of challenging problems whose nature and complexity reflect the electromagnetic origin of the measurement modality itself. The nascent field of optical brain-computer interfacing offers similarly difficult challenges, which so far have not been so thoroughly explored and developed. While there are many hundreds of papers published each year on improved processing of EEG signals for noninvasive electrical potentialsbased BCIs, the corresponding figure for even hemodynamics-oriented BCIs are in single figures by and large. We distinguish hemodynamics from optical correlates of hemodynamics in the present discussion so as to include reported work in the use of functional magnetic resonance imaging for BCIs. With such systems the BOLD response is believed to be correlated with localized Hb concentrations. In any case the use of such hemodynamic signals offers unique challenges and a series of intriguing signal processing problems. From the source of the signal itself where the precise features of interest and even the causal relationships between the underlying neural activity and vascular response is still debated through to the rejection of hemodynamic events unrelated to the feature of interest, a myriad of problems present themselves. This article in a very condensed format has offered an overview of some of these issues, has suggested solutions to some, has described current prototype devices, and elucidated to some extent the nature of the problems inherent in the paradigm from experimental methods through to artifact rejection. We feel that perhaps the application of robust adaptive signal processing to eliminate the Mayer wave artifact in particular is a key element to an improved fNIRS-BCI. From an instrumentation viewpoint, extension to multiple wavelengths and sites allowing topographic mapping based on more subtle features of the chromophore concentrations changes should also yield considerable improvements.

determining brain state and ultimately user intention to produce enhanced control signals. Measurement of hemodynamics associated with such brain states has emerged recently as a potential area worthy of investigation. Currently, fNIRS represents the most convenient means for determining such measurements and

THE MAJORITY OF THE WORKING EXAMPLES OF BCI TECHNOLOGY UTILIZE ELECTRICAL MEASUREMENTS OF NEURAL ACTIVITY TO ASCERTAIN USER INTENTION.

this has been recognized by a number of research groups who have harnessed the technology for potential BCI systems. This article has presented these developments in terms of their efficacy and shortcomings. Further, a synthesis of the signal processing problem within a BCI framework has been developed.

#### AUTHORS

Fiachra Matthews (fiachra.matthews@nuim.ie) graduated form the National University of Ireland (NUI) Maynooth in 2005 with a B.Sc. in computer science and software engineering. He is currently researching for his Ph.D. in the Hamilton Institute in NUI Maynooth in the area of signal processing for optical brain computer interfaces.

Barak A. Pearlmutter (barak@cs.nuim.ie) received the Ph.D. in computer science from Carnegie Mellon University and is currently a professor at the Hamilton Institute and in the Department of Computer Science at National University of Ireland Maynooth. His research focuses on sensory substitution and augmentation using unusual computer output devices; the theory and implementation of programming languages with first-class automatic differentiation operators; novel brain-computer interface techniques and algorithms for brain imaging; information-theoretic account of fictive percepts; and signal processing in animals and machines using sparse representations.

Tomas E. Ward (tomas.ward@nuim.ie) received the B.E., M.Eng.Sc., and Ph.D degrees from University College, Dublin, Ireland in 1994, 1996, and 1999, respectively. He is currently a senior lecturer in the Department of Electronic Engineering at the National University of Ireland, Maynooth. His primary research interests lie in the areas of optical brain computer interfaces and distributed interactive simulations.

Clearly fNIRS is not, as yet, a mainstream BCI technology and perhaps it may never be. However the current level of research and development in this area has not been of sufficient scale to suggest an exhaustion of the potential performance improvement for such methods. Also given the complementary nature of the hemodynamics response with respect to the electrical potentials associated with the responsible neural activity,

Christopher Soraghan (christopher.j.soraghan@nuim.ie) received the B.E. degree in electronic engineering from the

- Int. Conf. IEEE Engineering in Medicine and Biology Society, San Francisco, CA, Sept. 2004, [CD-ROM].
- [13] D. Sliney and M. Wolbarsht, Safety with Lasers and Other Optical Sources: A Comprehensive Handbook, 1st ed. New York: Plenum, 1980.
- [14] K. Uludag, J. Steinbrink, A. Villringer, and H. Obrig, “Separability and cross talk: optimizing dual wavelength combinations for near-infrared spectroscopy of the adult head,” Neuroimage, vol. 22, pp. 583–589, June 2004.
- [15] N.L. Everdell, A.P. Gibson, I.D.C. Tullis, T. Vaithianathan, J.C. Hebden, and D.T. Delpy, “A frequency multiplexed near-infrared topography system for imaging functional activation in the brain,” Rev. Sci. Instrum., vol. 76, no. 9, p. 093705, 2005.
- [16] S. Coyle, T. Ward, C. Markham, and G. McDarby, “On the suitability of nearinfrared (NIR) systems for next-generation brain-computer interfaces,” Physiol. Meas., vol. 25, pp. 815–822, July 2004.
- [17] C. Soraghan, F. Matthews, D. Kelly, T. Ward, C. Markham, B. Pearlmutter, and R. O’Neill, “A dual-channel optical brain-computer interface in a gaming environment,” in Proc. 9th Int. Conf. Computer Games: AI, Animation, Mobile, Educational and Serious Games, Dublin, Ireland, Nov. 2006, pp. 35–39.
- [18] S.M. Coyle, T.E. Ward, and C.M. Markham, “Brain-computer interface using a simplified functional near-infrared spectroscopy system,” J. Neural Eng., vol. 4, no. 3, pp. 219–226, 2007.
- [19] S. Ranganatha, Y. Hoshi, and C. Guan, “Near infrared spectroscopy based brain-computer interface,” in Proc. 3rd Int. Conf. Experimental Mechanics and 3rd Conf. Asian Committee Experimental Mechanics, Singapore, 2004.
- [20] S. Ranganatha, H. Zhang, C. Guan, M. Thulasidas, Y. Hoshi, A. Ishikawa, K. Shimizu, and N. Birbaumer, “Temporal classification of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain-computer interface,” Neuroimage, vol. 34, pp. 1416–1427, Feb. 2007.
- [21] Z. Haihong and G. Cuntai, “A kernel-based signal localization method for nirs brain-computer interfaces,” in Proc. ICPR ’06: Proc. 18th Int. Conf. Pattern Recognition, Washington, DC, 2006, pp. 1158–1161.
- [22] J.E.W. Mayhew, “Neuroscience: A measured look at neuronal oxygen consumption,” Science, vol. 299, no. 5609, pp. 1023–1024, 2003.
- [23] M. Izzetoglu, A. Devaraj, S. Bunce, and B. Onaral, “Motion artifact cancellation in nir spectroscopy using wiener filtering,” IEEE Trans. Biomed. Eng., vol. 52, pp. 934–938, May 2005.
- [24] T. Huppert (2006), “HomER nirs analysis software,” [Online]. Available: http://www.nmr.mgh.harvard.edu/DOT/resources/homer/home.htm
- [25] G. Gratton and P.M. Corballis, “Removing the heart from the brain: Compensation for the pulse artifact in the photon migration signal,” Psychophys., vol. 32, pp. 292–299, May 1995.
- [26] R.L. Cooley, N. Montano, C. Cogliati, P. van de Borne, W. Richenbacher, R. Oren, and V.K. Somers, “Evidence for a central origin of the low-frequency oscillation in RR-interval variability,” Circulat., vol. 98, no. 6, pp. 556–561, 1998.
- [27] C.E. Elwell, R. Springett, E. Hillman, and D.T. Delpy, “Oscillations in cerebral hemodynamics: Implications for functional activation studies,” Adv. Exp. Med. Biol., vol. 471, pp. 57–65, 1999.
- [28] M. Wolf, U. Wolf, J.H. Choi, R. Gupta, L.P. Safonova, L.A. Paunescu, A. Michalos, and E. Gratton, “Functional frequency-domain near-infrared spectroscopy detects fast neuronal signal in the motor cortex,” NeuroImage, vol. 17, no. 4, pp. 1868–1875, 2002.
- [29] U.E. Emir, C.B. Akgül, A. Aky´n, A. Ertüzün, B. Sankur, and K. Harmancy´, “Wavelet denoising vs ica denoising for functional optical imaging,” in Proc. 1st Int. IEEE EMBS Conf. Neural Engineering, Capri Island, Italy, Mar. 2003, pp. 384-387.
- [30] T. Kato, “Principle and technique of NIRS-imaging for human brain force: Fast-oxygen response in capillary event,” in Proc. ISBET 2004, vol. 1270, Aug. 2004, pp. 85–90. [SP]

National University of Ireland, Maynooth, in 2005. He is currently pursuing a Ph.D. as part of the Biomedical Engineering Research Group of NUI Maynooth. His research is focused on developing a multichannel near-infrared spectroscopy based brain-computer interface.

Charles Markham (charles.markham@nuim.ie) is a lecturer in the Computer Science Department of the National University of Ireland Maynooth. Prior to joining Maynooth in 1998 he specialized in medical imaging in the area of element specific imaging using computed tomography at Dublin City University. Research interests include optical brain-computer interfacing, medical imaging, and automated veichle guidance.

#### REFERENCES

- [1] C. Guger, A. Schlögl, C. Neuper, D. Walterspacher, T. Strein, and G. Pfurtscheller, “Rapid prototyping of an EEG-based brain-computer interface (BCI),” IEEE Trans. Neural Syst. Rehab. Eng., vol. 9, no. 1, pp. 49–58, 2001.
- [2] G. Pfurtscheller, R. Leeb, C. Keinrath, D. Friedman, C. Neuper, C. Guger, and M. Slater, “Walking from thought,” Brain Res., vol. 1071, no. 1, pp. 145–152, 2006.
- [3] N.J. Hill, T.N. Lal, M. Schroder, T. Hinterberger, B. Wilhelm, F. Nijboer, U. Mochty, G. Widman, C. Elger, B. Scholkopf, A. Kubler, and N. Birbaumer, “Classifying EEG and ECoG signals without subject training for fast BCI implementation: Comparison of nonparalyzed and completely paralyzed subjects,” IEEE Trans. Neural Syst. Rehab. Eng., vol. 14, pp. 183–186, June 2006.
- [4] N. Weiskopf, K. Mathiak, S.W. Bock, F. Scharnowski, R. Veit, W. Grodd, R. Goebel, and N. Birbaumer, “Principles of a brain-computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI),” IEEE Trans. Biomed. Eng., vol. 51, pp. 966–970, June 2004.
- [5] S.-S. Yoo, T. Fairneny, N.-K. Chen, S.-E. Choo, L.P. Panych, H. Park, S.-Y. Lee, and F.A. Jolesz, “Brain-computer interface using fMRI: Spatial navigation by thoughts,” Neuroreport, vol. 15, no. 10, pp. 1591–1595, 2004.
- [6] T.E. Ward, C.J. Soraghan, F. Matthews, and C.M. Markham, “A concept for extending the applicability of constraint induced movement therapy through motor cortex activity feedback using a neural prosthesis,” Comput. Intell. Neurosci. 2007 [Online]. Available: http://hindawi.com/Getarticle.aspx? doi=10.1155/2007/51363
- [7] M. Cope, “The application of near infrared spectroscopy to noninvasive monitering of cerebral oxygenation in the newborn infant,” Ph.D. dissertation, Dept. Medical Physics Bioeng., Univ. College London, London, England, Apr. 1991.
- [8] F.F. Jobsis, “Noninvasive infrared monitoring of cerebral and myocardial oxygen sufficiency and circulatory parameters,” Science, vol. 198, no. 4323, pp. 1264–1267, 1977.
- [9] A. Villringer, J. Planck, C. Hock, L. Schleinkofer, and U. Dirnagl, “Near infrared spectroscopy (NIRS): A new tool to study hemodynamic changes during activation of brain function in human adults,” Neurosci. Lett., vol. 154, pp. 101–104, May 1993.
- [10] A. Duncan, J.H. Meek, M. Clemence, C.E. Elwell, L. Tyszczuk, M. Cope, and D. Delpy, “Optical path length measurements on adult head, calf and forearm and the head of the newborn infant using phase resolved optical spectroscopy,” Phys. Med. Biol., vol. 40, no. 2, pp. 295–304, 1995.
- [11] A.P. Gibson, J.C. Hebden, and S.R. Arridge, “Recent advances in diffuse optical imaging,” Phys. Med. Bio.l, vol. 50, pp. 1–43, Feb. 2005.
- [12] S. Coyle, T. Ward, and C. Markham, “Physiological noise in near-infrared spectroscopy: Implications for optical brain computer interfacing,” in Proc. 26th Annu.

