MINI REVIEW
published: 18 October 2017
doi: 10.3389/fnhum.2017.00503
Edited by:
Stephane Perrey,
Université de Montpellier, France
Reviewed by:
Noman Naseer,
Air University, Pakistan
Christian Herff,
University of Bremen, Germany
Anirban Dutta,
University at Buffalo, United States
*Correspondence:
Sung C. Jun
scjun@gist.ac.kr
Received: 29 July 2017
Accepted: 05 October 2017
Published: 18 October 2017
Citation:
Ahn S and Jun SC (2017)
Multi-Modal Integration of EEG-fNIRS
for Brain-Computer
Interfaces – Current Limitations
and Future Directions.
Front. Hum. Neurosci. 11:503.
doi: 10.3389/fnhum.2017.00503
Multi-Modal Integration of
EEG-fNIRS for Brain-Computer
Interfaces – Current Limitations
and Future Directions
Sangtae Ahn1,2 and Sung C. Jun3*
1 School of Electronic and Electrical Engineering, Kyungpook National University, Daegu, South Korea, 2 School of Electronics
Engineering, Kyungpook National University, Daegu, South Korea, 3 School of Electrical Engineering and Computer Science,
Gwangju Institute of Science and Technology, Gwangju, South Korea
Multi-modal integration, which combines multiple neurophysiological signals, is gaining
more attention for its potential to supplement single modality’s drawbacks and yield
reliable results by extracting complementary features. In particular, integration of
electroencephalography (EEG) and functional near-infrared spectroscopy (fNIRS) is cost-
effective and portable, and therefore is a fascinating approach to brain-computer
interface (BCI). However, outcomes from the integration of these two modalities
have yielded only modest improvement in BCI performance because of the lack of
approaches to integrate the two different features. In addition, mismatch of recording
locations may hinder further improvement. In this literature review, we surveyed studies
of the integration of EEG/fNIRS in BCI thoroughly and discussed its current limitations.
We also suggested future directions for efﬁcient and successful multi-modal integration
of EEG/fNIRS in BCI systems.
Keywords: multi-modal integration, electroencephalography (EEG), functional near-infrared spectroscopy
(fNIRS), brain-computer interface (BCI)
INTRODUCTION
Electroencephalography (EEG) can record electrical changes induced by extra- and intra-cellular
electric currents associated with neuronal activity passively using scalp electrodes. EEG is one of
the most common techniques used to investigate the brain’s underlying mechanisms and is used
widely in a variety of neuroscience ﬁelds. To extract features from EEG data, temporal and spectral
analysis are used after elaborate pre-processing steps, such as removing artifacts from eye-blinking
or muscle movement. Event-related potentials, according to average in response to time-locked
repetitive sensory stimuli and rhythmic neural oscillations caused by interactions between neurons,
are conventional temporal and spectral features, respectively. One of the advantages of EEG is
its higher temporal resolution, but it has a lower spatial resolution and lower signal-to-noise
ratio attributable to the inherent low conductivity of the skull than does functional magnetic
resonance imaging (fMRI), which relies on the fact that cerebral blood ﬂow and neural activations
are associated closely.
Measuring cerebral blood ﬂow can give us signiﬁcant information necessary to investigate brain
dynamics as well as electrical activity. Similarly, functional near-infrared spectroscopy (fNIRS) is
a portable technique suitable for cost-eﬀective measurement of cerebral blood ﬂow in the brain
(Villringer et al., 1993). fNIRS is based on in the amount of measure photons using light in the
Frontiers in Human Neuroscience | www.frontiersin.org
1
October 2017 | Volume 11 | Article 503

Ahn and Jun
Multi-Modal Integration of EEG-fNIRS
near-infrared
range
(700–900
nm).
Quantiﬁcation
of
chromophore concentration and its relative changes between
two diﬀerent frequencies of infrared are fundamental processes
that can be explained by the modiﬁed Beer-Lambert’s law (Delpy
et al., 1988). Because oxygenated (HbO) and deoxygenated
hemoglobin
(HbR)
have
characteristic
optical
properties
in the visible and near-infrared light range, the changes in
concentration of these molecules are the main features of fNIRS.
Although this technique has attracted attention because of its
ability to measure hemodynamic responses, similar to fMRI, the
problems of low spatial- and depth-resolution still remain.
Overall, integration of EEG and fNIRS can provide us
with two diﬀerent sources of information about the brain,
electrical activities and hemodynamic responses; this integration
has the advantages of non-invasiveness, portability, and cost-
eﬀectiveness, among others. For these reasons, one of the primary
targets for their integration is brain-computer interface (BCI).
BCI using EEG has been used widely since Vidal ﬁrst introduced
a direct BCI (Vidal, 1973). Intendix, Corp.1 commercialized the
ﬁrst visual EEG-BCI system with high accuracy and reliability.
Recently, fNIRS-BCI has emerged as a new potential approach
(Naseer and Hong, 2013, 2015). fNIRS can measure HbO and
HbR in the superﬁcial layers of the human cortex, and may be
less susceptible to electrical noise and movement artifacts. Thus,
multi-modal integration of EEG and fNIRS has received attention
as a new BCI paradigm.
However,
improvement
in
BCI
performance
using
multi-modal integration is still in its infancy. The modest
improvement may be caused by the lack of computational
approaches to combine the two diﬀerent features. One obstacle
in the development of novel computational approaches to
combine two diﬀerent features is the mismatch in their temporal
resolution and inherent delays in hemodynamic responses, which
can disrupt the simultaneous integration of features. In addition,
a mismatch in recording locations between EEG and fNIRS
attributable to technical problems may hinder improvement
in BCI performance and interpretation of neurophysiological
ﬁndings from the two diﬀerent locations. In this literature review,
we reviewed reports of multi-modal integration of EEG-fNIRS in
BCI (summarized in Table 1), and discuss its current limitations.
Further, we suggest future directions for successful multi-modal
integration of EEG-fNIRS in BCI.
STUDIES OF MULTI-MODAL
INTEGRATION OF EEG-fNIRS
Although visual EEG-BCI systems work well and demonstrate
high reliability and performance, motor imagery EEG-BCI
still suﬀers from low performance (far lower than 70%
accuracy, which is commonly acceptable in EEG-BCI) and inter-
subject variation (Ahn and Jun, 2015). Reportedly, some users
intrinsically do not produce classiﬁable sensorimotor rhythms
(Blankertz et al., 2010) or produce artifacts and ambient noise,
neither of which can be addressed easily by mathematical
1www.intendix.com
algorithms. Some biological noise, such as eye-blinking or muscle
movements, can be removed with elaborate preprocessing steps,
but individual variation caused by diﬀerent brain structures still
may degrade BCI performance. Consequently, an optical BCI that
uses fNIRS has been introduced (Coyle et al., 2004), and since
then, a number of studies has been conducted on this technique
(Naseer and Hong, 2015). In addition, numerous multi-modal
approaches (Dornhege et al., 2004; Pfurtscheller et al., 2010) have
been shown to improve BCI performance successfully.
For these reasons, the ﬁrst study of EEG-fNIRS BCI
was conducted to enhance performance of motor execution
and
imagery
(Fazli
et
al.,
2012).
The
authors
collected
EEG-fNIRS data simultaneously in the sensorimotor region,
and 14 subjects were instructed to perform hand gripping
and visual feedback-controlled motor imagery. They used
Laplacian ﬁltered band-power from EEG and HbO/HbR
from fNIRS as features. An individual Linear discriminant
analysis (LDA) classiﬁer was computed ﬁrst for EEG, HbO,
and HbR, followed by a meta-classiﬁer. They found that
simultaneous EEG-fNIRS improved classiﬁcation by 5% on
average compared to a single modality. This was the ﬁrst
study of the potential use of EEG-fNIRS in BCI. A similar
study was performed to decode motor imagery of the force
and speed of hand clenching (Yin et al., 2015). They collected
EEG-fNIRS data simultaneously in the sensorimotor region,
and six subjects were asked to perform motor imagery using
diﬀerent forces and speeds of hand clenching for 10 s. Band-
power, amplitude, phase, and frequency were combined to
construct a time-phase-frequency feature from EEG, and the
diﬀerence between HbO and HbR was extracted as a fNIRS
feature. Importantly, they developed a feature optimization
method using joint mutual information (Meyer et al., 2008) to
remove redundant information that may reduce classiﬁcation
accuracy. Thereafter, they classiﬁed signals using the extreme
learning machine (Huang et al., 2012). They achieved improved
performance (up to a 5% increase) in decoding motor imagery
of hand clenching by adopting a combination of EEG-fNIRS
features.
It is known well that feedback training can improve BCI
performance (Nyberg et al., 2006; Gentili et al., 2010). Speciﬁcally,
patients with spinal cord injury showed preserved activation
in the sensorimotor cortex after long-term training (Enzinger
et al., 2008). However, little is known about the way in how
BCI training inﬂuences brain activity and plastic changes over
multiple training sessions. One study investigated these changes
in the brain using multi-channel fNIRS with multiple visual
feedback EEG-BCI training sessions (Kaiser et al., 2014). They
designed an experimental paradigm that consisted of alternate
fNIRS and EEG training sessions. All data were collected in
the sensorimotor cortex and 15 subjects were asked to perform
motor imagery (right hand and both feet) in all sessions. They
found that training with the visual feedback BCI increased
HbO in low BCI performers (<70%) accompanied by strong
beta activity in EEG over sessions. This study demonstrated
the way in how visual feedback EEG-BCI training aﬀects
brain activations associated with hemodynamic responses using
fNIRS.
Frontiers in Human Neuroscience | www.frontiersin.org
2
October 2017 | Volume 11 | Article 503

Ahn and Jun
Multi-Modal Integration of EEG-fNIRS
TABLE 1 | Summarized ﬁndings in multi-modal integration of EEG-fNIRS (EEG, electroencephalography; fNIRS, functional near-infrared spectroscopy; HbO/HbR,
concentration changes of oxygenated/deoxygenated hemoglobin; ERD, event-related desynchronization; SSVEP, steady-state visual evoked potential).
Reference
Regions of recording
Task
Feature
Major ﬁndings
Fazli et al., 2012
Frontal, sensorimotor,
and parietal
Motor execution and
imagery
EEG: band power;
fNIRS: HbO and HbR
Classiﬁcation accuracies in motor execution and imagery
for 14 healthy subjects improved signiﬁcantly using
simultaneous EEG and fNIRS compared to signal modality.
Kaiser et al., 2014
Sensorimotor
Motor imagery
EEG: band-power;
fNIRS: HbO and HbR
EEG-based feedback training increased HbO in fNIRS and
a stronger ERD in the beta band were achieved in low BCI
performers (<70%).
Khan et al., 2014
EEG: sensorimotor;
fNIRS: prefrontal
Mental arithmetic and
motor imagery
EEG: peak amplitudes;
fNIRS: HbO and HbR
Mental arithmetic and hand tapping were decoded from
fNIRS and EEG signals, respectively. High classiﬁcation
accuracies (>80%) were obtained in four tasks.
Tomita et al., 2014
Occipital
Visual attention to
ﬂickering visual stimuli
EEG: SSVEP; fNIRS:
HbO and HbR
fNIRS signal in the occipital region was used as a brain
switch to activate the SSVEP BCI. Improvement in SSVEP
classiﬁcation and a reduction of error rates for 13 subjects
were achieved.
Morioka et al., 2014
EEG: whole scalp;
fNIRS: parietal and
occipital
Spatial attention
EEG: alpha and beta
spectral power; fNIRS:
HbO
EEG-fNIRS decoder using cortical current estimation
yielded performance that was signiﬁcantly better than with
decoding methods based on EEG sensor signals alone.
Putze et al., 2014
EEG: whole scalp;
fNIRS: temporal and
occipital
Visual and auditory
perception
EEG: event-related
potential and power
spectral density; fNIRS:
HbO and HbR
Subject-dependent approach achieved a high classiﬁcation
accuracy (>90%) in discriminating between visual and
auditory perception and an idle state.
Yin et al., 2015
Sensorimotor
Motor imagery
EEG:
time-frequency-phase
feature; fNIRS: HbO
and HbR
Simultaneous EEG-fNIRS features for decoding motor
imagery of both force and speed of hand clenching
achieved improved classiﬁcation accuracy compared to
signal modality.
Koo et al., 2015
Sensorimotor
Motor imagery
EEG: alpha-band
power; fNIRS: HbO
A new system to block leaking light from fNIRS was
developed. An online self-paced motor imagery was
performed using EEG-fNIRS and fNIRS signals were used
as a brain switch. The system has a true positive rate of
88%, a false positive rate of 7% with an average response
time of 10.36 s
Buccino et al., 2016
Sensorimotor
Motor execution
EEG: band-power;
fNIRS: HbO and HbR
Newly developed slope indicators, which are used to detect
immediate changes, decreased the delays of peak
classiﬁcation accuracy up to 2 s in fNIRS.
Ahn et al., 2016
EEG: whole scalp;
fNIRS: prefrontal
Simulated driving
EEG: alpha/beta power
fNIRS: HbO
A new feature combination method was proposed based
on normalization of each feature. EEG-fNIRS feature
combination distinguished clearly between well-rested and
sleep-deprived conditions.
Nguyen et al., 2017
EEG: whole scalp;
fNIRS: prefrontal
Simulated driving
EEG: beta power
fNIRS: HbO
HbO and beta band-power in the frontal region detected
drowsiness more rapidly than did eye-blinking.
Inspired by the successful classiﬁcation of mental arithmetic
using fNIRS (Verner et al., 2013), one study attempted to decode
mental arithmetic and motor execution from fNIRS and EEG,
respectively (Khan et al., 2014). They designed an experimental
paradigm that consisted of performing four diﬀerent tasks for
60 s and calculated the classiﬁcation accuracies between each task
period and baseline. EEG and fNIRS sensors were placed on the
sensorimotor and prefrontal regions, respectively. They achieved
high classiﬁcation accuracies (>80%) for all four tasks that can be
applied in BCI systems.
The major limitation of fNIRS BCI is the inherent delay of
the hemodynamic response, which makes it diﬃcult to construct
real-time BCI applications. In a previous study (Fazli et al.,
2012), peak classiﬁcation accuracy in fNIRS was delayed up
to 7 s compared to that in EEG. Therefore, to overcome and
adjust for this inherent delay, a recent study developed a new
feature referred to as a slope indicator, which is the diﬀerence
between the current time segment average and that computed
from a previous time segment (Buccino et al., 2016). Band-
power and HbO/HbR were used as inputs for LDA classiﬁers
and 15 subjects were asked to perform four motor movements
(left/right arm or hand). For all four tasks, EEG-fNIRS achieved
higher classiﬁcation accuracy compared to single modality and
the slope indicator as a new feature in fNIRS reduced the
delay in peak performance up to 2 s from onset. In addition
to sensorimotor tasks, visual and auditory perception could
be classiﬁed with high accuracy (>90%) using simultaneous
EEG and fNIRS (Putze et al., 2014). This study suggested that
passive BCI used to detect perceptual activity is also feasible
for more natural BCI from the perspective of human–computer
interaction.
A self-paced (asynchronous) BCI is able to discriminate
between ongoing brain activity and that generated intentionally
and reduce error rates as well. Some studies have used fNIRS
Frontiers in Human Neuroscience | www.frontiersin.org
3
October 2017 | Volume 11 | Article 503

Ahn and Jun
Multi-Modal Integration of EEG-fNIRS
features as a brain switch to design self-paced BCI. Koo et al.
(2015) employed a novel experimental paradigm to detect the
occurrence of motor imagery with fNIRS data. Threshold-based
detection with a feature value of fNIRS data determined whether
or not the action of a motor imagery task was attempted.
Improving the performance of motor imagery is a primary
issue in multi-modal integration of EEG-fNIRS, as performance
using a single modality is relatively inferior to that in other
BCI tasks. In addition to motor imagery, Tomita et al. (2014)
merged two modalities in a steady-state visual evoked potential
(SSVEP) BCI, which is the paradigm known best. They used
an fNIRS signal in the occipital region as a brain switch to
activate the SSVEP BCI. They extracted features from EEG
and fNIRS, and classiﬁed SSVEP using a joint classiﬁer. They
achieved some improvement in SSVEP classiﬁcation and reduced
13 subjects’ error rates. Although SSVEP BCI has worked
well, designing self-paced BCI systems is essential to reduce
the error rate, and to consider a subject’s intention in more
naturalistic BCI.
Generally, EEG signals measured on the scalp consist of a
mixture of neuronal activity that originates from diﬀerent cortical
areas and is contaminated inherently by background noise.
To overcome this, various cortical current estimation methods
have been developed (Grech et al., 2008). However, estimation
of source current is an ill-posed inverse problem; thus, some
prior assumptions are required to obtain a unique solution.
Recently, hierarchical Bayesian estimation has been proposed
to combine fMRI (Sato et al., 2004; Yoshioka et al., 2008) and
fNIRS (Aihara et al., 2012) data as prior information. Consistent
with these approaches, Morioka et al. (2014) employed fNIRS
data as prior information for EEG cortical source estimation in
BCI. Eight subjects were asked to perform a spatial attention
task and normalized t-values (attention vs. control) from HbO
features were used as the hierarchical prior information. They
decoded directions (left or right) of spatial attention using a
sparse logistic regression classiﬁer based on cortical current
sources and found an average 8% improvement in performance
compared to EEG alone. Although this must be optimized well
with respect to the number of dipoles or computational time
for real-time BCI, this is the ﬁrst study to use fNIRS data as
prior information, which overcomes the inherent delay after task
onset.
In addition to BCI studies, simultaneous EEG-fNIRS can
be feasible in other ﬁelds. For example, monitoring long-
term driving is quite suitable to determine drivers’ complex
mental states and overcome delays in hemodynamic responses.
Therefore, researchers have monitored performance during
long-term simulated driving (Ahn et al., 2016; Nguyen et al.,
2017) by using a custom-built fNIRS device compatible with
a commercial EEG system to integrate the features from the
two diﬀerent modalities. They found that feature integration has
great potential in monitoring driving performance while in a
drowsy state, and investigated the interaction overall between
two diﬀerent features. Finally, they proposed neurophysiological
correlates for monitoring good driving states using two non-
invasive, portable techniques.
CURRENT LIMITATIONS AND FUTURE
DIRECTIONS
We reviewed studies that employed multi-modal integration of
EEG-fNIRS for BCI. Most BCI studies have used each feature
as an input for classiﬁers and achieved improvement in BCI
performance. However, in all studies, this improvement (<10%)
was modest compared to that obtained with a single modality.
The ultimate purpose of multi-modal integration in BCI is
to improve BCI performance, but this remains in its infancy.
We may assume that the modest improvement is caused by
the lack of computational approaches to feature integration
and the mismatch in the recording locations between the two
modalities. Therefore, in the sections that follow, we discuss
current limitations and future directions for successful multi-
modal integration of EEG-fNIRS.
Integration of Two Different Features
To date, HbO and HbR are unique features of fNIRS recordings,
and have been used widely. Because HbO and HbR are both
temporal features, it is important in signal processing to
determine the temporal period and apply ﬁltering methods
FIGURE 1 | Commercial EEG-fNIRS devices: (A) fNIRS-EEG package (Courtesy of Artinis Medical Systems, Netherlands, http://www.artinis.com, up to 112-ch
fNIRS and 128-ch EEG); (B) LABNIRS (Courtesy of Shimadzu Corporation, Japan, http://www.shimadzu.com, up to 142-ch fNIRS and 64-ch EEG); (C) NIRScout
(Courtesy of NIRx Medical Technologies, http://nirx.net, Up to 182-ch fNIRS and 32-ch EEG) created by Buccino et al. (2016).
Frontiers in Human Neuroscience | www.frontiersin.org
4
October 2017 | Volume 11 | Article 503

Ahn and Jun
Multi-Modal Integration of EEG-fNIRS
based on the temporal domain. In contrast, both spectral and
temporal features can be used in EEG, and thus, subjects
often are presented with rapid and short stimuli. However,
such stimuli are not applicable in fNIRS recordings because
of the inherent response delays and low temporal resolution.
An fNIRS system measures hemodynamic responses, which
take several seconds to develop. Delays in hemodynamic
responses have been estimated with modeling simulations
and computational methods (Liao et al., 2002; Buxton et al.,
2004). An invasive approach also has demonstrated the delays
in hemodynamic responses (Duckett et al., 2011). Therefore,
temporal synchronization for diﬀerent temporal resolutions
and measurement delays between fNIRS and EEG must be
addressed carefully before simultaneous recordings. In BCI
systems in particular, temporal synchronization could be a
critical problem because the information transfer rate is the
most important factor used to assess BCI systems. To handle
these problems, computational methods, such as using prior
information (Morioka et al., 2014) or normalized features (Ahn
et al., 2016), are necessary to obtain BCI performance better than
that with a single modality. Morioka et al. (2014) used fNIRS
features as prior information to estimate cortical current in EEG,
while Ahn et al. (2016) combined EEG and fNIRS features by
normalizing all features that ranged from 0 to 1, and applying
a summation of the features. Although further optimization steps
still are required, these two novel approaches may be future
solutions that overcome the current limitations in integrating the
features of EEG-fNIRS.
Sensor Conﬁguration of Two Different
Devices
Although there are several commercial devices on the market
that allow simultaneous measurement of EEG-fNIRS (Figure 1),
it is diﬃcult to record neuronal activity from the same location.
Because hemodynamic responses are recorded from the middle
of emitters and detectors in fNIRS, EEG electrodes should be
placed in the middle of these emitter and detectors to achieve the
same channel conﬁguration. EEG electrodes can be very small,
but emitters and detectors in fNIRS devices must be relatively
sizable to emit and detect infrared lights properly. In addition, the
quantiﬁcation of emitted and detected infrared light is aﬀected
substantially by dense hair (Gervain et al., 2011). Dense hair may
generate a low signal-to-noise ratio in fNIRS measurements such
that it is diﬃcult to measure sensitive hemodynamic changes in
the brain. These technical problems also hinder same-channel
conﬁguration and the ability to cover the entire brain region. One
possible way to equip an EEG-fNIRS device in the laboratory
is to combine them manually without a well-tuned hardware
combination. One study (Koo et al., 2015) designed a blocking
frame made of black acrylic plastic with a compression rubber
pad and obtained fNIRS and EEG data simultaneously. In
addition, researchers have custom-built compact and wireless
EEG-fNIRS devices (Safaie et al., 2013; Sawan et al., 2013; von
Lühmann et al., 2015, 2017). Such hardware developments may
enable us to resolve current technical limitations to some extent.
CONCLUSION
In this work, we reviewed studies of the multi-modal integration
of EEG-fNIRS. In our literature review, we found that BCI using
EEG-fNIRS has considerable potential to improve performance
by measuring two diﬀerent brain activities. However, it suﬀers
from two major problems: the lack of computational methods
to integrate the features and optimized sensor conﬁguration.
We suggested possible ways to overcome the current limitations
based on previous work. Computational integration methods
should be developed that consider the characteristics of features
from multi-modal EEG/fNIRS signals. Further, sophisticated
hardware developments are needed that address the size of
sensors and light leakage in fNIRS. We believe that our review
and suggestions for multi-modal integration can be a stepping
stone in making a signiﬁcantly advanced brain measurement tool
with better portability than EEG or fNIRS alone.
AUTHOR CONTRIBUTIONS
SA did literature surveys. SA and SJ discussed all ﬁndings and
wrote this manuscript. SJ coordinated all necessary procedures.
ACKNOWLEDGMENTS
This work was supported by GIST Research Institute (GRI)
grant funded by the GIST in 2017, the Brain Research Program
through the National Research Foundation of Korea (NRF)
funded by the Ministry of Science, ICT & Future Planning
(NRF-2016M3C7A1905475), and Institute for Information &
Communications Technology Promotion (IITP) grant funded by
the Korea government (MSIT) (No. 2017-0-00451).
REFERENCES
Ahn, M., and Jun, S. C. (2015). Performance variation in motor imagery
brain–computer interface: a brief review. J. Neurosci. Methods 243, 103–110.
doi: 10.1016/j.jneumeth.2015.01.033
Ahn, S., Nguyen, T., Jang, H., Kim, J. G., and Jun, S. C. (2016). Exploring neuro-
physiological correlates of drivers’ mental fatigue caused by sleep deprivation
using simultaneous EEG, ECG, and fNIRS data. Front. Hum. Neurosci. 10:219.
doi: 10.3389/fnhum.2016.00219
Aihara, T., Takeda, Y., Takeda, K., Yasuda, W., Sato, T., Otaka, Y., et al.
(2012). Cortical current source estimation from electroencephalography
in
combination
with
near-infrared
spectroscopy
as
a
hierarchical
prior.
Neuroimage
59,
4006–4021.
doi:
10.1016/j.neuroimage.2011.
09.087
Blankertz, B., Sannelli, C., Halder, S., Hammer, E. M., Kübler, A., Müller,
K.-R., et al. (2010). Neurophysiological predictor of SMR-based BCI
performance. Neuroimage 51, 1303–1309. doi: 10.1016/j.neuroimage.2010.
03.022
Frontiers in Human Neuroscience | www.frontiersin.org
5
October 2017 | Volume 11 | Article 503

Ahn and Jun
Multi-Modal Integration of EEG-fNIRS
Buccino, A. P., Keles, H. O., Omurtag, A., Bleichner, M., Benedictus, M.,
and Orellana, C. (2016). Hybrid EEG-fNIRS asynchronous brain-computer
interface for multiple motor tasks. PLOS ONE 11:e0146610. doi: 10.1371/
journal.pone.0146610
Buxton, R. B., Uludaˇg, K., Dubowitz, D. J., and Liu, T. T. (2004). Modeling
the hemodynamic response to brain activation. Neuroimage 23, S220–S233.
doi: 10.1016/j.neuroimage.2004.07.013
Coyle, S., Ward, T., Markham, C., and McDarby, G. (2004). On the suitability
of near-infrared (NIR) systems for next-generation brain–computer interfaces.
Physiol. Meas. 25, 815–822. doi: 10.1088/0967-3334/25/4/003
Delpy, D. T., Cope, M., van der Zee, P., Arridge, S., Wray, S., and Wyatt, J.
(1988). Estimation of optical pathlength through tissue from direct time of ﬂight
measurement. Phys. Med. Biol. 33, 1433–1442. doi: 10.1088/0031-9155/33/
12/008
Dornhege, G., Blankertz, B., Curio, G., and Muller, K.-R. (2004). Boosting bit
rates in noninvasive EEG single-trial classiﬁcations by feature combination and
multiclass paradigms. IEEE Trans. Biomed. Eng. 51, 993–1002. doi: 10.1109/
TBME.2004.827088
Duckett, S. G., Ginks, M., Shetty, A. K., Bostock, J., Gill, J. S., Hamid, S.,
et al. (2011). Invasive acute hemodynamic response to guide left ventricular
lead implantation predicts chronic remodeling in patients undergoing cardiac
resynchronization therapy. J. Am. Coll. Cardiol. 58, 1128–1136. doi: 10.1016/j.
jacc.2011.04.042
Enzinger, C., Ropele, S., Fazekas, F., Loitfelder, M., Gorani, F., Seifert, T., et al.
(2008). Brain motor system function in a patient with complete spinal cord
injury following extensive brain–computer interface training. Exp. Brain Res.
190, 215–223. doi: 10.1007/s00221-008-1465-y
Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Müller, K.-R.,
et al. (2012). Enhanced performance by a hybrid NIRS–EEG brain computer
interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084
Gentili, R., Han, C. E., Schweighofer, N., and Papaxanthis, C. (2010). Motor
learning without doing: trial-by-trial improvement in motor performance
during mental training. J. Neurophysiol. 104, 774–783. doi: 10.1152/jn.00257.
2010
Gervain, J., Mehler, J., Werker, J. F., Nelson, C. A., Csibra, G., Lloyd-Fox, S.,
et al. (2011). Near-infrared spectroscopy: a report from the McDonnell infant
methodology consortium. Dev. Cogn. Neurosci. 1, 22–46. doi: 10.1016/j.dcn.
2010.07.004
Grech, R., Cassar, T., Muscat, J., Camilleri, K. P., Fabri, S. G., Zervakis, M.,
et al. (2008). Review on solving the inverse problem in EEG source analysis.
J. Neuroeng. Rehabil. 5:25. doi: 10.1186/1743-0003-5-25
Huang, G.-B., Zhou, H., Ding, X., and Zhang, R. (2012). Extreme learning machine
for regression and multiclass classiﬁcation. IEEE Trans. Syst. Man Cybern. B 42,
513–529. doi: 10.1109/TSMCB.2011.2168604
Kaiser, V., Bauernfeind, G., Kreilinger, A., Kaufmann, T., Kübler, A., Neuper, C.,
et al. (2014). Cortical eﬀects of user training in a motor imagery based brain–
computer interface measured by fNIRS and EEG. Neuroimage 85, 432–444.
doi: 10.1016/j.neuroimage.2013.04.097
Khan, M. J., Hong, M. J., and Hong, K.-S. (2014). Decoding of four movement
directions using hybrid NIRS-EEG brain-computer interface. Front. Hum.
Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244
Koo, B., Lee, H.-G., Nam, Y., Kang, H., Koh, C. S., Shin, H.-C., et al. (2015).
A hybrid NIRS-EEG system for self-paced brain computer interface with online
motor imagery. J. Neurosci. Methods 244, 26–32. doi: 10.1016/j.jneumeth.2014.
04.016
Liao, C. H., Worsley, K. J., Poline, J.-B., Aston, J. A. D., Duncan, G. H., and
Evans, A. C. (2002). Estimating the delay of the fMRI response. Neuroimage
16, 593–606. doi: 10.1006/nimg.2002.1096
Meyer, P. E., Schretter, C., and Bontempi, G. (2008). Information-theoretic feature
selection in microarray data using variable complementarity. IEEE J. Sel. Top.
Signal Process. 2, 261–274. doi: 10.1109/JSTSP.2008.923858
Morioka, H., Kanemura, A., Morimoto, S., Yoshioka, T., Oba, S., Kawanabe, M.,
et al. (2014). Decoding spatial attention by using cortical currents estimated
from
electroencephalography
with
near-infrared
spectroscopy
prior
information.
Neuroimage
90,
128–139.
doi:
10.1016/j.neuroimage.2013.
12.035
Naseer, N., and Hong, K.-S. (2013). Classiﬁcation of functional near-infrared
spectroscopy signals corresponding to the right- and left-wrist motor imagery
for development of a brain–computer interface. Neurosci. Lett. 553, 84–89.
doi: 10.1016/j.neulet.2013.08.021
Naseer, N., and Hong, K.-S. (2015). fNIRS-based brain-computer interfaces: a
review. Front. Hum. Neurosci. 9:3. doi: 10.3389/fnhum.2015.00003
Nguyen, T., Ahn, S., Jang, H., Jun, S. C., Kim, J. G., and Hu, L. D. (2017). Utilization
of a combined EEG/NIRS system to predict driver drowsiness. Sci. Rep. 7:43933.
doi: 10.1038/srep43933
Nyberg, L., Eriksson, J., Larsson, A., and Marklund, P. (2006). Learning by
doing versus learning by thinking: an fMRI study of motor and mental
training. Neuropsychologia 44, 711–717. doi: 10.1016/j.neuropsychologia.2005.
08.006
Pfurtscheller, G., Allison, B. Z., Brunner, C., Bauernfeind, G., Solis-Escalante, T.,
Scherer, R., et al. (2010). The hybrid BCI. Front. Neurosci. 4:30. doi: 10.3389/
fnpro.2010.00003
Putze, F., Hesslinger, S., Tse, C. Y., Huang, Y. Y., Herﬀ, C., Guan, C., et al. (2014).
Hybrid fNIRS-EEG based classiﬁcation of auditory and visual perception
processes. Front. Neurosci. 8:373. doi: 10.3389/fnins.2014.00373
Safaie, J., Grebe, R., Moghaddam, H. A., and Wallois, F. (2013). Toward a fully
integrated wireless wearable EEG-NIRS bimodal acquisition system. J. Neural
Eng. 10:56001. doi: 10.1088/1741-2560/10/5/056001
Sato, M., Yoshioka, T., Kajihara, S., Toyama, K., Goda, N., Doya, K., et al. (2004).
Hierarchical Bayesian estimation for MEG inverse problem. Neuroimage 23,
806–826. doi: 10.1016/j.neuroimage.2004.06.037
Sawan, M., Salam, M. T., Le Lan, J., Kassab, A., Gelinas, S., Vannasing, P., et al.
(2013). Wireless recording systems: from noninvasive EEG-NIRS to invasive
EEG devices. IEEE Trans. Biomed. Circuits Syst. 7, 186–195. doi: 10.1109/
TBCAS.2013.2255595
Tomita, Y., Vialatte, F.-B., Dreyfus, G., Mitsukura, Y., Bakardjian, H., and
Cichocki, A. (2014). Bimodal BCI using simultaneously NIRS and EEG.
IEEE Trans. Biomed. Eng. 61, 1274–1284. doi: 10.1109/TBME.2014.230
0492
Verner, M., Herrmann, M. J., Troche, S. J., Roebers, C. M., and Rammsayer, T. H.
(2013). Cortical oxygen consumption in mental arithmetic as a function of task
diﬃculty: a near-infrared spectroscopy approach. Front. Hum. Neurosci. 7:217.
doi: 10.3389/fnhum.2013.00217
Vidal, J. J. (1973). Toward direct brain-computer communication. Annu. Rev.
Biophys. Bioeng. 2, 157–180. doi: 10.1146/annurev.bb.02.060173.001105
Villringer, A., Planck, J., Hock, C., Schleinkofer, L., and Dirnagl, U. (1993). Near
infrared spectroscopy (NIRS): a new tool to study hemodynamic changes
during activation of brain function in human adults. Neurosci. Lett. 154,
101–104. doi: 10.1016/0304-3940(93)90181-J
von Lühmann, A., Herﬀ, C., Heger, D., and Schultz, T. (2015). Toward a
wireless open source instrument: functional near-infrared spectroscopy in
mobile neuroergonomics and BCI applications. Front. Hum. Neurosci. 9:617.
doi: 10.3389/fnhum.2015.00617
von Luhmann, A., Wabnitz, H., Sander, T., and Muller, K.-R. (2017).
M3BA: a mobile, modular, multimodal biosignal acquisition architecture
for miniaturized EEG-NIRS-based hybrid BCI and monitoring. IEEE Trans.
Biomed. Eng. 64, 1199–1210. doi: 10.1109/TBME.2016.2594127
Yin, X., Xu, B., Jiang, C., Fu, Y., Wang, Z., Li, H., et al. (2015). A hybrid BCI
based on EEG and fNIRS signals improves the performance of decoding motor
imagery of both force and speed of hand clenching. J. Neural Eng. 12:36004.
doi: 10.1088/1741-2560/12/3/036004
Yoshioka, T., Toyama, K., Kawato, M., Yamashita, O., Nishina, S., Yamagishi, N.,
et al. (2008). Evaluation of hierarchical Bayesian method through retinotopic
brain activities reconstruction from fMRI and MEG signals. Neuroimage 42,
1397–1413. doi: 10.1016/j.neuroimage.2008.06.013
Conﬂict of Interest Statement: The authors declare that the research was
conducted in the absence of any commercial or ﬁnancial relationships that could
be construed as a potential conﬂict of interest.
Copyright © 2017 Ahn and Jun. This is an open-access article distributed under the
terms of the Creative Commons Attribution License (CC BY). The use, distribution or
reproduction in other forums is permitted, provided the original author(s) or licensor
are credited and that the original publication in this journal is cited, in accordance
with accepted academic practice. No use, distribution or reproduction is permitted
which does not comply with these terms.
Frontiers in Human Neuroscience | www.frontiersin.org
6
October 2017 | Volume 11 | Article 503
