INTRODUCTION
Brain–machine interfaces (BMIs) enable direct communication 
between the brain and machines [1, 2]. Due to advancements in 
information and communication technology, BMIs have gained 
attention for their promising applications in medical, industrial, 
and household settings [3-6].
In a unidirectional BMI, the system consists of three compo-
nents: devices used to record neural signals, components used 
to analyze the signals, and devices used to provide commands to 
operate the machine, as illustrated in Fig. 1. In a bidirectional BMI, 
additional components are required to provide feedback from the 
machine to the brain [7, 8]. While both invasive and non-invasive 
methods have been developed for the acquisition of neural signals, 
the present review focuses on implantable neural probes. Thus, 
hereafter, we will use the terms “neural probes” and “invasive meth-
Implantable Neural Probes for Brain-Machine 
Interfaces – Current Developments and Future 
Prospects
Jong-ryul Choi
1, Seong-Min Kim
2,3, Rae-Hyung Ryu
4,  
Sung-Phil Kim
5 and Jeong-woo Sohn
2,3*
1Medical Device Development Center, Daegu-Gyeongbuk Medical Innovation Foundation (DGMIF), Daegu 41061, 
2Department of Medical Science, College of Medicine, Catholic Kwandong University, Gangneung 25601,  
3Biomedical Research Institute, Catholic Kwandong University International St. Mary’s Hospital, Incheon 21711,  
4Laboratory Animal Center, Daegu-Gyeongbuk Medical Innovation Foundation (DGMIF), Daegu 41061,  
5Department of Human Factors Engineering, Ulsan National Institute of Science and Technology (UNIST), Ulsan 44919, Korea
https://doi.org/10.5607/en.2018.27.6.453
Exp Neurobiol. 2018 Dec;27(6):453-471.
pISSN 1226-2560 • eISSN 2093-8144
Review Article
A brain–machine interface (BMI) allows for direct communication between the brain and machines. Neural probes for recording 
neural signals are among the essential components of a BMI system. In this report, we review research regarding implantable neural 
probes and their applications to BMIs. We first discuss conventional neural probes such as the tetrode, Utah array, Michigan probe, 
and electroencephalography (ECoG), following which we cover advancements in next-generation neural probes. These next-gener-
ation probes are associated with improvements in electrical properties, mechanical durability, biocompatibility, and offer a high de-
gree of freedom in practical settings. Specifically, we focus on three key topics: (1) novel implantable neural probes that decrease the 
level of invasiveness without sacrificing performance, (2) multi-modal neural probes that measure both electrical and optical signals, 
(3) and neural probes developed using advanced materials. Because safety and precision are critical for practical applications of BMI 
systems, future studies should aim to enhance these properties when developing next-generation neural probes.
Key words: Implantable neural probes, Brain-machine interface, Multi-channel electrodes, Neural probes with advanced materials
Received October 5, 2018, Revised November 15, 2018,
Accepted November 15, 2018
*To whom correspondence should be addressed.
TEL: 82-32-280-6523, FAX: 82-32-280-6510
e-mail: jsohn@ish.ac.kr
Copyright © Experimental Neurobiology 2018.
www.enjournal.org
This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License 
(http://creativecommons.org/licenses/by-nc/4.0) which permits unrestricted non-commercial use, distribution, and 
reproduction in any medium, provided the original work is properly cited.

454
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
ods” interchangeably. 
Electroencephalography (EEG) is widely utilized in non-invasive 
BMI systems due to its high temporal resolution, which makes it 
useful for mapping associations between EEG signals and cogni-
tive function [9-11]. For example, NeuroSky, Inc. (San Jose, CA, 
USA) introduced an EEG-based brain–medicine interfacing 
headset for use in healthcare settings. In addition, Emotiv, Inc. (San 
Francisco, CA, United Sates) provides a 14-channel system for 
measuring EEG and other bio-signals for use in brain–computer 
interfacing games and neurofeedback treatment. Functional near-
infrared spectroscopy (fNIRS) and magnetoencephalography 
(MEG) have also been used to develop non-invasive BMI systems 
[12-15]. However, non-invasive neural methods are limited in 
that neural signals from non-invasive probes are typically insuf-
ficient for complicated tasks that require a high degree of freedom, 
such as robot control [16-19]. For this reason, implantable neural 
probes are preferred for BMI systems that demand accurate con-
trols and adjustments (e.g., neuroprosthetic devices).
Implantable neural probes are defined as devices implanted into 
the brain or other nervous tissues. Communication between neu-
rons in the brain occurs via electrical and chemical signals. In most 
cases, electrical signals are the main source of information in BMI 
systems. In particular, single-unit activity (i.e., spikes) is regarded 
as most appropriate for extracting meaningful information, such 
as movement-related activity [20]. While non-invasive methods 
record neural activity through different media such as the dura 
matter, cerebral spinal fluid (CSF), and skull, implanted neural 
probes can record extracellular activity or local field potentials 
closer to neurons. To maximize the signal-to-noise ratio, the con-
ductive material is often exposed at the end of the electrode, the 
shank of which is insulated with non-conductive material. Typi-
cally, single-wire electrodes [21] and glass micropipette electrodes 
are used in electrophysiological studies [22, 23]. Recent advance-
ments have enabled the development of implantable neural probes 
with the technical characteristics necessary for practical BMI 
applications, which include high spatiotemporal resolution and 
high signal-to-noise ratio. Biocompatibility, biochemical stability, 
and miniaturization are also important, as neural probes must be 
Fig. 1. A schematic of a bidirectional brain-machine interface. As the figure illustrated, the system of brain-machine interface consists of three compo-
nents. First one is the system that acquires neural signal, for example, neural recording systems with a neural probe. Second one is decoding component 
to translate neural activities into machine operational languages. Third one is encoding component that analyze feedback data from sensors and stimu-
late the specific regions in the brain. A fundamental concept in the bidirectional interface is referred to [8] with a permission of Frontiers Media S.A. 
under the terms of the Creative Commons Attribution License (CC BY).

455
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
inserted into the brain. Indeed, implantable multi-array neural 
probes with these characteristics have been developed and applied 
for research, diagnosis, and treatment purposes. Representative 
neural probes in this category include the tetrode, Utah array, and 
Michigan probe.
In the present report, we review the features of these three im-
plantable neural probes and their applications in BMI systems. 
Furthermore, we describe several novel technical approaches for 
improving the measurement of neural signals in BMI systems: (1) 
decreasing the invasiveness of implantable neural probes while 
maintaining performance, (2) using multi-modal probes to mea-
sure both electrical and optical signals from neurons, and (3) using 
flexible neural probes to enhance signal quality and biocompat-
ibility. We further discuss (4) novel fabrication techniques and ma-
terials that can be utilized to improve neural probes. By exploring 
recent developments in implantable neural probe technology, we 
offer insight into the performance required to create practical, ef-
ficient, and accurate BMI systems.
APPLICATION OF IMPLANTABLE NEURAL PROBES IN BMIs
BMIs have been successfully applied in the field of neuropros-
thetics, enabling patients with paralysis to control robot arms 
using their thoughts. The underlying neural principle of this 
phenomenon involves population vectors, in which each neuron 
“votes” for the intended movement [20]. Increasing the number 
of neuronal signals increases the likelihood of movement in the 
population vector. Thus, probes including a high number of chan-
nels are suitable for BMIs. In this section, we discuss three popular 
implantable neural probes with high numbers of channels.
TETRODE
The tetrode is widely utilized to record extracellular electrical po-
tentials in neural systems. As the prefix (tetr-) indicates, the tetrode 
consists of four electrodes at which neuronal signals are detected 
from slightly different spatial points originating from the same 
source. Such electrodes are typically constructed from a platinum–
tungsten alloy and insulated with quartz coating. The metal end of 
the electrode is exposed to acquire electrical signals. The diameter 
of each electrode at the metal end is usually less than 30 μm, and 
may be up to100 μm at the coated end. The coating functions to 
minimize the interference of electrophysiological signals across 
electrodes. As illustrated in Fig. 2A, a single tetrode can measure 
the extracellular potentials of approximately 1,100 neurons within 
a 140-μm radius in the rat cortex [24-26]. One main advantage of 
this method over single-channel electrodes is that users can clas-
sify the extracellular potentials of adjacent neurons using a cluster-
ing approach [27-29]. The extracellular potentials of each neuron 
are detected by the four electrodes in the tetrode with different 
temporal points and waveforms because due to the difference in 
spatial distance between each electrode and the neuron. Spikes 
from multiple neurons can thus be separated in the post-processing 
stage. However, the tetrode cannot provide direct measurements 
of spatially multi-dimensional extracellular potential distributions 
unless multiple tetrodes are precisely implanted and arranged at 
regular intervals. Recently, several research groups have developed 
multi-tetrode arrays to compensate for these shortcomings [30, 
Fig. 2. (A) A schematic to represent detectable areas of neural activities by a tetrode. By improved clustering and spike sorting methods, the tetrode can 
detect neural activities in areas of neural assembles with 280 μm diameters. The reprint of this figure in [26] was permitted by Nature Publishing Group 
(Springer Nature). (B) A schematic of an experimental setup to study the control of a robot by neural signals recorded by multiple tetrodes, which were 
implanted in the cortex of the rat. This figure published in [34] is reprinted with a permission of Society for Neuroscience.

456
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
31].
The tetrode has been used as an implantable neural probe in 
BMI platforms, especially in small animals. Giszter et al. described 
a neurorobotic platform, which consisted of a tetrode-based 
neural recording module and a three-dimensional (3D) robotic 
module, for use with spinal or cortical prosthetics in small animals 
(i.e., frogs and rats) [32]. Song et al. developed a novel BMI system 
to identify movement-related information in the rat cortex during 
treadmill walking [33]. Using decoded neural activity acquired 
from six implanted tetrodes, specific regions related to proximal 
limb and trunk movements were identified in the rat motor cor-
tex. In a follow-up study, Song and Giszter introduced a pelvis-
attached robot that can be controlled by cortical neural signals 
using a multi-tetrode array implanted in the rat brain (Fig. 2B) [34]. 
Bender et al. investigated that activity of central complex neurons 
in the insect brain during walking using a tetrode-based system 
[35]. The authors reported a close association between move-
ments and sensory responses, providing insight into the feasibility 
of such methods for use in larger animals with more developed 
brains. Additional groups have also reported advancements in 
post-processing techniques that enable sorting of spikes in practi-
cal BMI systems. For example, Oweiss introduced a novel spatio-
temporal signal processing method to improve data compression 
and reduce latency in multi-tetrode BMI systems [36]. Kubo et 
Fig. 3. (A) A figure of implanted two 96-channel Utah arrays on a motor and posterior cortex of a non-human primate to record neural signals for an 
investigation of a brain-machine interfacing platform under approve of Institutional Animal Care and Use Committee at Daegu-Gyeongbuk Medical 
Innovation Foundation, Korea. (B) A schematic of a brain-spine interface to produce the signal of the spinal cord for walking based on neural activities 
of the motor cortex. To be specific, neural activities of the motor cortex were recorded by a 96-channel Utah array and decoded information from the 
acquired neural activities was transmitted to an electrical pulse generator inserted in the spine. The pulse generator produced electrical stimulations for 
walking of a spine-injured non-human primate. The re-use of this figure published in [41] was permitted by Nature Publishing Group (Springer Nature). 
(C) Experimental procedures, a technological setup, and a map of implanted Utah and floating electrode arrays for generating contacting senses in an 
artificial hand with targeted neuro-stimulations in the somatosensory cortex. This figure in [42] is re-used with a permission of National Academy of 
Sciences. (D) A schematic of a paralyzed patient assistant platform based on on-site available neural cursor adjustments from neural signals, which were 
measured by implanted Utah array. A right figure illustrates radial-8 cursor trajectories of three participants (S3, T6, and T7). The re-use of this figure 
published in [47] was approved by Nature Publishing Group (Springer Nature).

457
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
al. further investigated the 3D distributions of neurons based on 
multi-site neural activity using the tetrode [37].
UTAH ARRAY
Advancements in semiconductor fabrication processes dur-
ing the late 20
th century have led to the development of multi-
channel arrays that perform better than single-channel electrodes 
in multiple respects. The Utah array is a commercially available 
intracortical electrode array consisting of up to 100 silicon needle-
shaped electrodes, which are produced via microscale fabrication 
techniques such as thermomigration, a combination of mechani-
cal and chemical micromachining, metal deposition, and encap-
sulation with a polymer made of imide monomers [38]. Due to 
the large number of electrodes, the Utah array has been mostly 
used in large animals, especially non-human primates (Fig. 3A). 
Velliste et al. investigated the ability of a BMI system to provide 
neuroprosthetic arm control via cortical motor activity in rhesus 
monkeys (Macaca mulatta) using Utah arrays [39]. In this study, 
the BMI system produced natural levels of multi-dimensional 
arm and hand movements. In addition, the same research group 
reported meaningful associations between visuomotor adaptation 
and neural activity in the primary motor cortex measured via the 
Utah arrays [40]. Capogrosso et al. developed a BMI platform to 
electrically stimulate the spinal cord according to decoded neural 
signals from the Utah array in the motor cortex of monkeys [41]. 
As described in Fig. 3B, the brain–spine interface enabled mon-
keys with spinal cord injuries to walk again based on commands 
from the motor cortex. Utah arrays have not only been used for 
recording, but also for stimulation purposes. For example, Tabot 
et al. induced tactile sensations in the hand via targeted neural 
stimulation with Utah arrays implanted in the somatosensory cor-
tex, as illustrated in Fig. 3C [42, 43]. This type of sensory feedback 
may aid in increasing the accuracy of various BMI devices and 
neuro-rehabilitation instruments. In addition, Suner et al. verified 
the reliability of chronic implementations of the Utah array in the 
brains of non-human primates [44].
The Utah array and its recording systems have been approved 
for clinical applications by the United States Food and Drug Ad-
ministration (FDA). Several clinical trials of Utah array-based 
BMI systems involving human patients have been conducted. 
Simeral et al. reported that one patient with tetraplegia could 
control a computer cursor (including point-and-click functions) 
based on neural signals from the motor cortex [45]. Pandarinath 
et al. analyzed neural population dynamics during movement in 
two patients with amyotrophic lateral sclerosis (ALS) as they at-
tempted to use their finger to move a computer cursor [46]. One 
year after implantation, the system still produced adequate signals 
for neural cursor control (Fig. 3D) [47] or virtual typing [48]. A 
more challenging task was performed by a human subject with 
Utah array implantation. Wodlinger et al. developed a BMI system 
for the control of an anthropomorphic robot arm and hand with 
10 degrees of freedom [49]. Some studies have also indicated that 
BMI systems can bypass the spinal cord circuit to recover hand 
function in select patients. Bouton et al. introduced a platform for 
controlling a neuromuscular electrical stimulation sleeve using 
neural signals from an implanted Utah array, enabling the patient 
to perform accurate and continuous movements (e.g., grasp-pour-
and-stir tasks) [50]. Ajiboye et al. developed an interfacing plat-
form between intracortical neural signals recorded by two Utah 
arrays and functional electrical stimulation of peripheral muscles 
to restore arm and hand movements in patients with paralysis [51]. 
As experiments of tactile feedbacks has been successful in non-
human primate, this type of research has begun to be applied to 
human subject. As tactile feedback experiments using Utah arrays 
have been successful in non-human primates, researchers have be-
gun to apply such systems in human patients. For example, Flesher 
et al. stimulated the somatosensory cortex using Utah arrays to 
recover tactile sensation in human patients [52].
MICHIGAN PROBE
The previous two neural probes enable users to acquire neural 
activity from different cortical areas. However, they are limited in 
their ability to target deep neural structures in the axial direction 
[53, 54]. In the late 1970s, the first prototype of Michigan probe, 
a multi-channel depth electrode prototype, was developed based 
on electron-beam lithographic techniques [55], which was before 
production of Utah array. Several preclinical studies involving 
small animals have demonstrated the safety of long-term implan-
tation for the Michigan probe, suggesting that such probes can be 
utilized in BMI systems [56-58]. Electrodes in the Michigan probe 
(2 to 15 mm) are longer than those in the Utah array (0.5 to 1.5 
mm for research). Thus, the Michigan probe may be more suitable 
when recording from deeper cortical structures.
Vetter et al. applied the Michigan probe to examine extracellular 
neural activity in the motor cortex of rats using a BMI system [56]. 
In a preclinical study on the control of emotions and memories, 
the Michigan probe was used to measure neural activity and pro-
vide electrical stimulation. Frost et al. investigated neural activity in 
the hindlimbs of rats with spinal cord injuries using a 16-channel 
Michigan probe and explored treatment methods based on neuro-
stimulation [59]. Guggenmos et al. investigated the use of a neural 
interfacing system to recover neural function after brain injuries 

458
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
in small animals (i.e., rats) demonstrating that the missing brain 
functions can be restored using a brain–machine–brain interface 
as described in Fig. 4 [60]. Such findings suggest that neuropros-
thetics can successfully applied in the treatment of various neural 
diseases. Michigan probes have also been validated in non-human 
primates [61], supporting the notion that such probes can be used 
to develop neuroprosthetic systems for use in humans.
RECENT ADVANCES IN NEURAL PROBES FOR IMPROVE-
MENTS OF BMI SYSTEMS
In the previous session, we described the most widely used 
implantable neural probes in BMI applications. While the electri-
cal characteristics, biological compatibility, and stability of these 
probes are sufficient, researchers have attempted to improve their 
impedance, flexibility, wireless communication, recording area, 
and accuracy to ultimately improve BMI systems. In this section, 
we present an overview of recent studies that have responded to 
these technical challenges for practical BMI applications.
NOVEL IMPLANTABLE NEURAL PROBES WITH DECREASING A 
DEGREE OF INVASIVENESS AND MAINTAINING PERFORMANCE
High-performance ECoG electrode
Electrocorticography (ECoG) is used to monitor signals from 
the cerebral cortex using electrodes placed on the surface of the 
brain (subdural) or dura matter (epidural). In contrast to implant-
ed neural probes, which rely on single-unit activity, ECoG relies 
on local field potentials (LFPs). Although a craniotomy is still re-
quired to implement ECoG, no brain scarring occurs because the 
ECoG electrodes are not inserted into the brain tissue. ECoG pro-
vides more accurate neural signals than non-invasive approaches 
because due to direct (subdural) or close (epidural) contact with 
brain tissue. Since ECoG has clear advantages in terms of neural 
signal quality when compared with current non-invasive methods, 
it is widely used in the development of minimally invasive BMI 
systems [62-65]. Neural responses can be recorded from multiple 
sites in the human brain with high spatiotemporal resolution fol-
lowing tactile stimulation, supporting the use of ECoG in medical 
BMI applications [66]. For example, Wang et al. recorded activity in 
the human motor cortex during individual finger movement using 
micro-ECoG electrodes [67]. Subsequent studies demonstrated 
that a 32-channel ECoG electrode grid could be used to record 
LFPs in the sensorimotor cortex of a participant with tetraplegia 
[68]. Shin et al. introduced method for decoding muscle activation 
from neural activity based on ECoG signals in the motor cortex 
of non-human primates [69]. In this study, they investigated the 
potential for several advanced ECoG electrodes for use as neural 
probes in BMI systems.
Microfabrication techniques have been employed to develop 
Fig. 4. A theoretical model of a neural interfacing system to recover neural functions after brain injuries by neuro-prosthetic treatments. A schematic of 
a preclinical test with an implanted Michigan probe was shown. The plot in the lower right corner shows transient neural signals and artifact due to an 
electrical stimulation from the premotor cortex. The reprint published in [60] was approved by National Academy of Sciences.

459
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
high-resolution ECoG electrodes. Rubehn et al. developed a flex-
ible, high-resolution (252 channels) ECoG electrode array to mea-
sure neural activity in the human brain by optimizing designs and 
implementing high-resolution MEMS fabrication techniques [70]. 
Henle et al. developed a microscale ECoG electrode array using a 
laser-based high-speed and high-resolution fabrication method 
[71]. Due to their biocompatibility, these types of electrode arrays 
are promising for use in various long-term, in vivo BMI applica-
tions. Toda et al. developed a mesh-type multi-channel ECoG elec-
trode array with narrow spacing by simplifying fabrication steps, 
including oxygen plasma etching [72]. In a preliminary in vivo 
study, the authors measured neural signals in the rat visual cortex, 
reporting that ocular selectivity could be predicted with 90% ac-
curacy by decoding the neural signals from their ECoG electrode 
array. Several research groups have proposed novel and optimized 
strategies for ECoG electrode arrangement. Slutzky et al. opti-
mized the spacing of each ECoG electrode to reduce invasiveness 
in ECoG-based BMI systems without sacrificing performance 
using finite element modeling of the electrical and physical prop-
erties of each component (i.e., scalp, skull, etc.) in the brain [73]. 
Tolstosheeva et al. investigated the application of a flexible ECoG 
neural probe (Fig. 5A) consisting of electrodes with three different 
sizes efficiently distributed on a soft pad [74, 75].
Advancements in ECoG recording systems have occurred with 
regard to both detection and transmission. Indeed, several studies 
have suggested that wireless ECoG recording systems can be im-
plemented in BMI systems. For instance, Charvet et al. developed 
a promising wireless 64-channel neural probe for the acquisition 
of neural activity as recorded via ECoG [76]. Similarly, wireless 
microscale ECoG neural probes have been used to investigate 
reach-and-grasp movements in non-human primates [77]. In ad-
dition, Chang and Chiou developed a chronic ECoG system that 
can be used to measure neural activity without communicating 
wires or batteries [78]. Such findings suggest that this type of neu-
ral probe can be integrated not only in freely moving animals, but 
also in humans.
Based on our review of studies involving high-performance 
ECoG with a large number of channels, we conclude that ECoG 
would be advantageous in BMI applications due to its relatively 
low level of invasiveness [79] and the potential for long-term LFP 
recording [80]. In addition, ECoG electrodes can be applied to 
brain regions of various shapes, enabling the application of BMI 
systems for various functions [74, 75]. We expect that advances in 
ECoG electrodes will further facilitate BMI applications.
Injectable neural probe
Some research groups have introduced flexible, syringe-inject-
able electronic devices for the measurement of chronic in vivo 
neural activity (Fig. 5B) [81]. To establish injectable neural probes, 
Liu et al. applied nanotechnology-based fabrication techniques to 
develop electronics composed of flexible mesh [82, 83]. Injectable 
mesh electronics can be produced via multiple fabrication tech-
niques such as photolithography, which can be used to define the 
structures and regions of nanoscale silicon wires, metal deposition, 
and in the chemical development of nanostructures [82-85]. One 
preliminary study revealed that such devices could be used to re-
cord neural activity in freely moving mice [86]. The mesh record-
ing electrodes has less invasiveness compared to other counterpart 
implantable probes due to their microscale size and high flexibility. 
If the biocompatibility and quality of acquired neural signals can 
be secured in the future, we believe that the injectable neural probe 
offers a better alternative for detecting brain activity in various 
BMI applications.
Stent electrodes array
A stent is a medical tube that can be implanted into the vessels 
to maintain an opening for blood flow. Stents are widely utilized 
in the treatment of arteriosclerosis since its appearance [87], as 
they are significantly less invasive than traditional methods [88, 
89]. To achieve minimal invasiveness and long-term biocompat-
ibility, Oxley et al. developed an endovascular stent-electrode 
array, as pictured in Fig. 5C [90]. Stent-electrode arrays can be 
installed by inserting a catheter into the appropriate cerebral 
blood vessel. Accurate induction of each electrode array position 
can be acquired using x-ray angiographic fluorography. One pre-
clinical study reported that stent-electrode arrays with multiple 
neural probes could be used for the long-term measurement of 
somatosensory evoked potentials in the sheep brain. The feasibil-
ity and sustainable biocompatibility of long-term/chronic neural 
interfaces in brain blood vessels have been confirmed via x-ray 
micro-tomography and histological assays [91]. Recent studies 
have demonstrated that endovascular stent-electrode arrays can 
be used to acquire vascular ECoG signals [92] and detect electro-
chemical changes via impedance spectroscopy [93]. Despite such 
advancements, no studies have demonstrated that state-of-the-art 
stent electrodes can provide immediately usable neural signals (e.g., 
movement-related activity) for BMI applications. Nonetheless, 
researchers have successfully acquired somatosensory evoked po-
tentials from stent electrodes implanted in the superficial cortical 
vein overlying the motor cortex in sheep via catheter angiography 
[90]. Therefore, future studies may be able to harness movement-
related information conveyed to stent electrodes to enhance BMI 
development.

460
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
Wireless neural probes for BMIs
The use of physical wires inside the brain to acquire neural sig-
nals is associated with several disadvantages, such as the risk of 
infection and reduced freedom of movement. To overcome these 
shortcomings, researchers have investigated the application of 
wireless neural recording techniques to BMI systems. For instance, 
Schwarz et al. developed a wireless multi-channel platform for 
monitoring neural activity, which was applied successfully in freely 
moving non-human primates [94]. This system, which resembles a 
crown, consists of hundreds to thousands of microwire electrodes, 
a wireless recording/transmitting module, and a battery. In addi-
tion, the same research group introduced a wheelchair robot that 
could be controlled based on neural activity recorded wirelessly 
from an onboard monkey [95]. Similarly, Libedinsky et al. inves-
tigated the application of a robotic vehicle independently moved 
by neural signals using a 100-channel wireless probe. Su et al. in-
troduced a wireless implantable recording/stimulating probe for 
bidirectional BMIs, as described in Fig. 5D [96]. This latter probe is 
Fig. 5. (A) A flex-rigid 124-channel ECoG electrode array to measure neural activities. This neural probe was manufactured with advanced and high-
resolution microscale fabrication techniques. This figure in [75] is reprinted with a permission of MDPI, Basel, Switzerland under the terms and condi-
tions of the Creative Commons Attribution License. (B) Implant procedures, in vivo insertion and single-unit neural recording of an injectable neural 
probe. The re-use of this figure published in [81] was approved by Nature Publishing Group (Springer Nature). (C) A stent electrode array (middle) with 
8 electrodes to acquire neural signals in the brain vessel and pre- and post-implant images in a delivery of the stent electrode array by X-ray venography. 
This figure published in [90] is reprinted with a permission of Nature Publishing Group (Springer Nature). (D) An implantable wireless implantable re-
cording and stimulating probe for bidirectional BMI instruments. The reprint of this figure in [96] was permitted by MDPI, Basel, Switzerland under the 
terms and conditions of the Creative Commons Attribution License.

461
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
advantageous due to its small size and ability for remote charging.
Researchers have also investigated the application of ultrasound 
technology as a carrier of neural signals from medium-depth tis-
sue. Such “neural dust” systems are advantageous in that they are 
able to send and receive information non-invasively in certain ar-
eas of the brain. Seo et al. investigated a neural dust system consist-
ing of recording electrodes, a piezoelectric ultrasound generator, 
drive electrodes, and a wireless cortical recording platform [97]. 
In this system, an external ultrasound probe sends out an echo 
with a specific waveform, following which a reflected wave (i.e., 
neural signal) is emitted from the system. This neural signal can 
be isolated by examining the specific waveform transmitted and 
the backscattered signal. Preliminary studies designed to measure 
neural activity in the peripheral nervous system using a neural 
dust system in rats have demonstrated the potential of these sys-
tems for application in BMI technologies.
We anticipate that advancements in the following areas will 
promote the use of wireless neural electrodes in practical BMI 
applications: ultra-low power consumption, high signal-to-noise 
ratio, sufficient maximum communication distance for receiving 
and transmitting data, and channel number [76, 98]. Furthermore, 
wireless BMI systems must be designed to prevent malfunctions 
by erasing noise from the external environment, to have an ef-
ficient means of changing the battery, and to function for a long 
period of time on single charge [99, 100].
MULTI-MODAL NEURAL PROBES TO MEASURE BOTH ELEC-
TRICAL AND OPTICAL SIGNALS
While direct electrical measurements can be obtained using im-
plantable neural probes as described in previous sections, optical 
measurement methods are also utilized to record neural activity 
at the level of single neurons and neuronal assemblies. Optical 
methods rely on indices such as the influx of calcium ions (Ca
2+) 
and changes in voltage. Since changes in Ca
2+ can represent neural 
activity, several optical indicators have been applied in studies 
ranging from in vitro cellular assays [101, 102] to in vivo investiga-
tions in freely moving animals [103]: a bioluminescent Ca
2+ prob-
ing protein (Aequorin) [104], chemical Ca
2+ indicators (calcium 
green, fura-2 etc.) [105, 106], genetically encoded Ca
2+ indicators 
based on a single fluorophore [107] and Förster resonance energy 
transfer (FRET) [108]. In addition, voltage-sensitive optical dyes 
can be used to identify transient changes in action potentials in 
neurons [109-111]. In addition, voltage-sensitive optical dyes 
can be used to identify transient changes in action potentials in 
neurons. Indeed, researchers have developed optical implantable 
neural probes for use in freely behaving animals by combining 
fiberoptic and wireless communication technologies. For instance, 
Murayama et al. designed a miniaturized neuro-endoscopic 
periscope using graded-index (GRIN) lenses and micro-prism 
coupled fibers. This periscope was used to study dendritic Ca
2+ 
changes in freely moving mice [112]. Ghosh et al. introduced a 
prototype of a miniaturized wide-field fluorescence microscope 
with which they could measure neural activity when the device 
was mounted on the head of freely moving animals [113]. Besides, 
optical neuro-stimulations were exercised since the discovery of 
optogenetics stimulation. Furthermore, optical devices can be used 
for stimulation purposes as well: In the case of Channelrhodopsin 
(ChR), trans-membrane pores are opened when ChR-integrated 
ion channels absorb blue light at a wavelength of 470 nm, causing 
ions to flow into the neurons [114-116]. Preclinical studies have 
confirmed that fiber-coupled illumination devices function well 
in freely moving animals. Aravanis et al. designed a fiber-coupled 
optical neural interface guided by ChR2-mCherry fluorescence 
images for use in rats [117]. Several research groups have also 
developed prototypes of wirelessly integrated LED-based implant-
able neural stimulation modules for use in freely moving animals 
[118-120].
Electrical and optical signals can be measured without interfer-
ence from one another because their frequency domains are dif-
ferent. For this reason, several prototypes of multi-modal neural 
probes have been developed to measure both electrical and optical 
activity in preclinical studies [121, 122]. LeChasseur et al. devel-
oped a micro-probe, which consists of a dual-core optical fiber 
and a 50-μm electrical wire probe for recording both electrical and 
optical neural activities, as illustrated in Fig. 6A [123]. In a compar-
ative study, the authors recorded optical and electrical neural sig-
nals from the same neuron in rats, observing that the two modali-
ties were complementary and highly correlated with one another. 
Anikeeva et al. developed an optetrode, which is composed of a 
200-μm single-channel optical fiber and a tetrode, to investigate 
optical stimulation and neural responses (recorded by the tetrode), 
as described in Fig. 6B [124]. The optetrode detected multi-unit 
neural activity and transient changes when optical stimulation was 
provided at different frequencies. Voigts et al. investigated an ultra-
light weight neural probe (i.e., FlexDrive) consisting of a single-
core optical fiber and 16, 32, or 64-channel electrodes for studies 
of multi-dimensional neural responses to optogenetic stimula-
tion [125]. Kwon and colleagues combined a transparent ECoG 
electrode array and an optical illumination device for optogenetic 
stimulation [126]. In another preliminary in vivo study, the au-
thors proposed a prototype of a multi-modal neural probe termed 
the Opto-μECoG array, which exhibits sufficient biocompatibility. 
Several researchers have also introduced variations of the Utah 

462
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
array combined with miniaturized optical components to acquire 
high-resolution electrical neural signals following optical neuro-
stimulation [127, 128]. Similarly, previous studies have reported 
the success of BMI systems based on optogenetic neuromodula-
tion and electrical neural recordings in small animals [129-135]. 
For example, Liu et al. developed a compact optogenetics system 
using graphene electrodes to reduce artifacts [136]. We expect that 
multi-modal BMI systems will evolve toward more specific ap-
plications when the safety and stability of both probes have been 
demonstrated.
Based on previous research, we expect the following benefits to 
be associated with the use of multi-modal neural probes that com-
bine optical and electrophysiological modalities in BMI systems. 
When using neural probes to record both optical and electrical 
neural signals, cross-validation of fidelity between the two signals 
can increase signal reliability. In particular, since the noise sources 
of the two signals are likely to be different, one signal can be used 
when another signal is perturbed. In the context of BMI applica-
tions, multi-modal probes may be useful when the patient is in 
an electromagnetically noisy environment. Such probes may also 
be advantageous for advanced BMI systems that require precise 
stimulation and minimal interference between signals. However, 
few optogenetic genes have been identified and cleared for use in 
humans due to safety concerns [137, 138]. Genetic engineering 
remains quite challenging due to its unknown long-term impact 
on humans, although it is expected that these technologies will be 
utilized in various BMI systems once issues regarding safety and 
stability have been addressed.
NEURAL PROBES WITH ADVANCED MATERIALS
In order for successful implantation in the human brain, neural 
probes must exhibit sufficient biocompatibility, safety, stability, 
and electrical performance. However, electrodes composed of 
classic materials such as iridium oxide and platinum are limited in 
their ability to meet these conditions. To overcome these limita-
tions, advanced materials with special functions and properties 
including metals, inorganic materials, and polymers have been ap-
plied to the development of neural probes.
Carbon nanotubes (CNTs) are cylindrically structured allotropes 
of carbon that are stronger and have better elasticity and electri-
cal properties than more traditional materials [139, 140]. As such, 
various studies have aimed to develop neural probes using CNTs. 
Wang et al. designed a microelectrode array composed of CNTs, 
reporting significant improvements in the charge injection limit 
when CNT electrodes were used to stimulate cultured hippocam-
pal neurons [141]. Keefer et al. developed a CNT coating to en-
hance charge transfer in microelectrode arrays [142]. In this study, 
Fig. 6. (A) A multimodal microprobe with optical and electrical measurements of neural activities. The multimodal probe consisted of a dual-core opti-
cal fiber, which excited fluorescent indicators and collected emitted signals, and an electrical wire to record electrical activities in neurons. This figure in 
[123] is reprinted with a permission of Nature Publishing Group (Springer Nature). (B) A schematic of an optetrode, which consisted of a single optical 
fiber with 200 μm core diameters for optogenetic stimulations and a tetrode to record neural activities and changes when the optical stimulation occurs. 
The re-use of this figure published in [124] was approved by Nature Publishing Group (Springer Nature).

463
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
the authors obtained stronger neural activity from CNT-coated 
electrodes in the primate visual cortex, with an improvement fac-
tor of 7.4 dB (Fig. 7A). Guitchounts et al. developed 16-channel 
carbon fiber neural probes with which they could acquire long-
term chronic neural signals due to the strength and stability of the 
carbon fiber [143]. In addition, previous studies have demonstrat-
ed the successful integration of a soft CNT fiber microelectrode 
array in long-term bidirectional neural interfaces. Such findings 
suggest that this system can be used to develop high-performance 
and biocompatible BMI devices and neuroprosthetic instruments 
[144]. Graphene, a two-dimensional carbon allotrope, can also be 
utilized to improve the performance of neural probes due to its 
mechanical stiffness, flexibility, and superior electrical properties 
[145]. For instance, Chen et al. designed flexible graphene micro-
probes that can be applied to record electrical signals associated 
with neural or cardiac activity [146]. Graphene-based flexible elec-
trodes have also been fabricated to acquire ECoG signals by im-
proving contact with the brain. Additional studies have indicated 
that graphene can be used to investigate changes in neural activity 
due to optogenetic stimulation due to its high transparency [147]. 
Similarly, Kuzum et al. developed a graphene electrode array with 
high flexibility and transparency: They acquired electrical neural 
signals and fluorescence images indicating changes in calcium 
flux using the same electrode [148]. Furthermore, graphene-based 
electrodes can be integrated into multi-functional neural probes. 
For instance, Liu et al. introduced neural probes that consist of 
graphene-oxide and gold-oxide electrodes, as illustrated in Fig. 
7B [149]. This novel probe can be used to obtain measurements 
of both electrophysiological neural signals and electrochemical 
information via cyclic voltammetry. Indeed, this type of electrode 
can be used to monitor neural activity and various electrochemical 
changes after the induction of brain damage due to photo-throm-
bosis. Apollo et al. also investigated the application of needle-type 
flexible neural probes made from graphene oxide for use in bidi-
rectional neural interfaces [150].
Due to the development of efficient techniques for fabricating 
and manufacturing nanoscale structures and particles, nanotech-
nology has quickly become relevant to biological and biomedical 
applications Indeed, nanoscale structures and particles have been 
applied to improve neural probes. Park et al. developed a nanopo-
rous platinum electrode that can be used to record neural signals 
[151]. In this study, the authors reported that the nanoporous elec-
trodes were associated with improvements in electrical proper-
ties, impedance, and charge injection limits when compared with 
commercially available alternatives such as platinized platinum 
and iridium oxide electrodes. Other studies have demonstrated 
the enhanced biocompatibility of gallium phosphide nanowire 
electrodes [152]. These nanowire electrodes were tested in the rat 
primary somatosensory cortex. Abidian and colleagues introduced 
nanostructured polymer-coated conducting electrodes with en-
hanced electrical properties, improved mechanical adhesion, and 
better neuronal attachment capabilities [153]. Piret et al. developed 
boron-doped diamond electrodes with three dimensionally fab-
ricated nanostructures using multiple semiconductor fabrication 
Fig. 7. (A) Carbon nanotubes coated microelectrode arrays to improve electrical property in recording neural activities. Left plots illustrates local field 
potential and power spectral density with frequencies in ranging from 1 to 300 Hz comparing microelectrodes coated with carbon nanotube to ones 
without coating. The reprint of this figure in [142] was permitted by Nature Publishing Group (Springer Nature). (B) A schematic of in vivo experimen-
tal setup in a study recording neural activities and electrochemical changes during photo-thrombosis. The neural probes used in this setup consist of 
graphene-oxide and gold-oxide combined electrodes. The figure published in [149] is reprinted with a permission of American Chemical Society.

464
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
techniques [154]. Relative to conventional boron-doped diamond 
electrodes, the nanostructured electrodes offer higher sensitivity 
to neural activity while maintaining stability and biocompatibility, 
suggesting that these electrodes can be applied in the development 
of highly sensitive BMI systems and rehabilitation instruments.
CONCLUSIONS
In this report, we have reviewed the application of current multi-
channel neural probes (i.e., the tetrode, Utah array, and Michigan 
probe) to BMI systems, as well as developments regarding next-
generation neural probes. When comparing the electrodes cur-
rently in use, it is important to choose the proper neural probe 
based on the function and purpose of the BMI application. For 
instance, for measurement and stimulation of pyramidal neurons 
in deep sulcus areas—which are known to directly control fine 
muscles such as those in the hand—a neural probe with a longer 
shank is required. We also discussed several developing neural 
probes, which aim to improve upon the electrical properties, bio-
compatibility, and reliability of current devices using multi-modal 
approaches. If high-density electrodes with improved biocompati-
bility can be developed, flexible ECoG systems can be more widely 
applied in both clinical and preclinical BMI studies. Although 
stent electrodes are currently at the proof-of-concept stage, their 
minimal invasiveness suggests that they can replace many other 
methods for acquiring neural signals in the future. Safety concerns 
represent the greatest challenge for BMI systems based on optoge-
netic stimulation. The application of new materials, high-resolu-
tion integrated technologies, and nanotechnology will ultimately 
contribute to the development of high-performance neural probes 
and BMI systems.
While the long-term fidelity of neural recordings is critical for 
success in BMI systems, several subsequent stages of processing 
are critical for ensuring the efficiency of these systems (Fig. 1). 
Decoding algorithms that allow for accurate analysis of acquired 
neural signals and encoding techniques that transfer outward 
information to the brain are also important components of a BMI 
system [155-158]. High-speed computing and wireless signal pro-
cessing are also critical for the development of high-performance 
BMI systems that can be applied in real-world settings.
Perhaps the most important issue facing developers is the bio-
compatibility and mechanical suitability of implantable neural 
probes. Advancements in material science and mechanical tech-
niques will aid in developing strategies for minimizing brain 
scarring while maintaining adequate electrode contact [159, 160]. 
Assessments of signal quality and side effects should be performed 
in both in vitro and in vivo systems (e.g., non-human primates) to 
determine the practical applications of novel BMI systems prior to 
use in humans. For these reasons, it is also necessary to choose ap-
propriate packaging techniques to enhance the biocompatibility of 
implantable neural probes.
Mass production and security concerns should also be addressed 
in the development of neural probes for commercial and real-
world use. Because the electrode is inserted into the brain, proper 
mass manufacturing technologies are required, without sacrificing 
the quality of the probe from production to packaging. Thus, sys-
tematic inspection methods should also develop. Several security 
experts have cautioned that information leakage may occur when 
using BMI systems [161, 162]. Therefore, establishing technolo-
gies to prevent information leakage is another issue that must be 
addressed when considering the practical applications of BMI sys-
tems. In conjunction with technological advancements, consensus 
regarding social and ethical concerns will lead to widespread utili-
zation of implantable neural probes and BMI systems. 
ACKNOWLEDGEMENTS
This research was supported by grants of the Brain Re-
search Program through the National Research Foundation 
of Korea (NRF) funded by the Ministry of Science and ICT 
(2016M3C7A1904986).
REFERENCES
1.	Nair P (2013) Brain-machine interface. Proc Natl Acad Sci U 
S A 110:18343.
2.	Fetz EE (2015) Restoring motor function with bidirectional 
neural interfaces. Prog Brain Res 218:241-252.
3.	Merritt B (2016) The digital revolution. In: Synthesis lectures 
on emerging engineering technologies (Iniewski K, ed), pp 
1-109. Morgan & Claypool Publishers, San Rafael, CA.
4.	Patil PG, Turner DA (2008) The development of brain-ma-
chine interface neuroprosthetic devices. Neurotherapeutics 
5:137-146.
5.	Bell CJ, Shenoy P, Chalodhorn R, Rao RP (2008) Control of a 
humanoid robot by a noninvasive brain-computer interface 
in humans. J Neural Eng 5:214-220.
6.	Kansaku K, Hata N, Takano K (2010) My thoughts through 
a robot’s eyes: an augmented reality-brain-machine interface. 
Neurosci Res 66:219-222.
7.	Miranda RA, Casebeer WD, Hein AM, Judy JW, Krotkov EP, 
Laabs TL, Manzo JE, Pankratz KG, Pratt GA, Sanchez JC, We-
ber DJ, Wheeler TL, Ling GS (2015) DARPA-funded efforts in 
the development of novel brain-computer interface technolo-

465
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
gies. J Neurosci Methods 244:52-67.
8.	Panzeri S, Safaai H, De Feo V, Vato A (2016) Implications of 
the dependence of neuronal activity on neural network states 
for the design of brain-machine interfaces. Front Neurosci 
10:165.
9.	Millán Jdel R, Renkens F, Mouriño J, Gerstner W (2004) Non-
invasive brain-actuated control of a mobile robot by human 
EEG. IEEE Trans Biomed Eng 51:1026-1033.
10.	Rebsamen B, Guan C, Zhang H, Wang C, Teo C, Ang MH Jr, 
Burdet E (2010) A brain controlled wheelchair to navigate in 
familiar environments. IEEE Trans Neural Syst Rehabil Eng 
18:590-598.
11.	Müller KR, Tangermann M, Dornhege G, Krauledat M, Curio 
G, Blankertz B (2008) Machine learning for real-time single-
trial EEG-analysis: from brain-computer interfacing to men-
tal state monitoring. J Neurosci Methods 167:82-90.
12.	Fazli S, Mehnert J, Steinbrink J, Curio G, Villringer A, Müller 
KR, Blankertz B (2012) Enhanced performance by a hybrid 
NIRS-EEG brain computer interface. Neuroimage 59:519-
529.
13.	Coyle SM, Ward TE, Markham CM (2007) Brain-computer 
interface using a simplified functional near-infrared spectros-
copy system. J Neural Eng 4:219-226.
14.	Kauhanen L, Nykopp T, Lehtonen J, Jylänki P, Heikkonen 
J, Rantanen P, Alaranta H, Sams M (2006) EEG and MEG 
brain-computer interface for tetraplegic patients. IEEE Trans 
Neural Syst Rehabil Eng 14:190-193.
15.	Yeom HG, Kim JS, Chung CK (2013) Estimation of the veloc-
ity and trajectory of three-dimensional reaching movements 
from non-invasive magnetoencephalography signals. J Neu-
ral Eng 10:026006.
16.	Iturrate I, Antelis JM, Kubler A, Minguez J (2009) A noninva-
sive brain-actuated wheelchair based on a P300 neurophysio-
logical protocol and automated navigation. IEEE Trans Robot 
25:614-627.
17.	Waldert S (2016) Invasive vs. non-invasive neuronal signals 
for brain-machine interfaces: will one prevail? Front Neurosci 
10:295.
18.	Wodlinger B, Downey JE, Tyler-Kabara EC, Schwartz AB, 
Boninger ML, Collinger JL (2015) Ten-dimensional anthro-
pomorphic arm control in a human brain-machine interface: 
difficulties, solutions, and limitations. J Neural Eng 12:016011.
19.	Baranauskas G (2014) What limits the performance of cur-
rent invasive brain machine interfaces? Front Syst Neurosci 
8:68.
20.	Georgopoulos AP, Schwartz AB, Kettner RE (1986) Neuronal 
population coding of movement direction. Science 233:1416-
1419.
21.	Adrian ED, Bronk DW (1929) The discharge of impulses in 
motor nerve fibres: part II. The frequency of discharge in re-
flex and voluntary contractions. J Physiol 67:i3-i151.
22.	Ling G, Gerard RW (1949) The normal membrane potential 
of frog sartorius fibers. J Cell Comp Physiol 34:383-396.
23.	Bretag AH (2017) The glass micropipette electrode: a history 
of its inventors and users to 1950. J Gen Physiol 149:417-430.
24.	Henze DA, Borhegyi Z, Csicsvari J, Mamiya A, Harris KD, 
Buzsáki G (2000) Intracellular features predicted by extracel-
lular recordings in the hippocampus in vivo. J Neurophysiol 
84:390-400.
25.	Holmgren C, Harkany T, Svennenfors B, Zilberter Y (2003) 
Pyramidal cell communication within local networks in layer 
2/3 of rat neocortex. J Physiol 551:139-153.
26.	Buzsáki G (2004) Large-scale recording of neuronal ensem-
bles. Nat Neurosci 7:446-451.
27.	Takahashi S, Anzai Y, Sakurai Y (2003) A new approach to 
spike sorting for multi-neuronal activities recorded with a 
tetrode--how ICA can be practical. Neurosci Res 46:265-272.
28.	Gray CM, Maldonado PE, Wilson M, McNaughton B (1995) 
Tetrodes markedly improve the reliability and yield of mul-
tiple single-unit isolation from multi-unit recordings in cat 
striate cortex. J Neurosci Methods 63:43-54.
29.	Shoham S, Fellows MR, Normann RA (2003) Robust, auto-
matic spike sorting using mixtures of multivariate t-distribu-
tions. J Neurosci Methods 127:111-122.
30.	Nguyen DP, Layton SP, Hale G, Gomperts SN, Davidson TJ, 
Kloosterman F, Wilson MA (2009) Micro-drive array for 
chronic in vivo recording: tetrode assembly. J Vis Exp 26:1098.
31.	Xie K, Fox GE, Liu J, Tsien JZ (2016) 512-channel and 13-re-
gion simultaneous recordings coupled with optogenetic ma-
nipulation in freely behaving mice. Front Syst Neurosci 10:48.
32.	Giszter SF, Hart CB, Udoekwere UI, Markin S, Barbe C (2005) 
A real-time system for small animal neurorobotics at spinal 
or cortical levels. Int IEEE EMBS Conf Neural Eng 2005:450-
453.
33.	Song W, Ramakrishnan A, Udoekwere UI, Giszter SF (2009) 
Multiple types of movement-related information encoded 
in hindlimb/trunk cortex in rats and potentially available for 
brain-machine interface controls. IEEE Trans Biomed Eng 
56:2712-2716.
34.	Song W, Giszter SF (2011) Adaptation to a cortex-controlled 
robot attached at the pelvis and engaged during locomotion 
in rats. J Neurosci 31:3110-3128.
35.	Bender JA, Pollack AJ, Ritzmann RE (2010) Neural activity in 
the central complex of the insect brain is linked to locomotor 

466
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
changes. Curr Biol 20:921-926.
36.	Oweiss KG (2006) A systems approach for data compression 
and latency reduction in cortically controlled brain machine 
interfaces. IEEE Trans Biomed Eng 53:1364-1377.
37.	Kubo T, Katayama N, Karashima A, Nakao M (2008) The 3D 
position estimation of neurons in the hippocampus based 
on the multi-site multi-unit recordings with silicon tetrodes. 
Conf Proc IEEE Eng Med Biol Soc 2008:5021-5024.
38.	Campbell PK, Jones KE, Huber RJ, Horch KW, Normann RA 
(1991) A silicon-based, three-dimensional neural interface: 
manufacturing processes for an intracortical electrode array. 
IEEE Trans Biomed Eng 38:758-768.
39.	Velliste M, Perel S, Spalding MC, Whitford AS, Schwartz AB 
(2008) Cortical control of a prosthetic arm for self-feeding. 
Nature 453:1098-1101.
40.	Chase SM, Kass RE, Schwartz AB (2012) Behavioral and 
neural correlates of visuomotor adaptation observed through 
a brain-computer interface in primary motor cortex. J Neuro-
physiol 108:624-644.
41.	Capogrosso M, Milekovic T, Borton D, Wagner F, Moraud 
EM, Mignardot JB, Buse N, Gandar J, Barraud Q, Xing D, Rey 
E, Duis S, Jianzhong Y, Ko WK, Li Q, Detemple P, Denison T, 
Micera S, Bezard E, Bloch J, Courtine G (2016) A brain-spine 
interface alleviating gait deficits after spinal cord injury in 
primates. Nature 539:284-288.
42.	Tabot GA, Dammann JF, Berg JA, Tenore FV, Boback JL, Vo-
gelstein RJ, Bensmaia SJ (2013) Restoring the sense of touch 
with a prosthetic hand through a brain interface. Proc Natl 
Acad Sci U S A 110:18279-18284.
43.	Kim S, Callier T, Tabot GA, Gaunt RA, Tenore FV, Bensmaia 
SJ (2015) Behavioral assessment of sensitivity to intracortical 
microstimulation of primate somatosensory cortex. Proc Natl 
Acad Sci U S A 112:15202-15207.
44.	Suner S, Fellows MR, Vargas-Irwin C, Nakata GK, Donoghue 
JP (2005) Reliability of signals from a chronically implanted, 
silicon-based electrode array in non-human primate primary 
motor cortex. IEEE Trans Neural Syst Rehabil Eng 13:524-
541.
45.	Simeral JD, Kim SP, Black MJ, Donoghue JP, Hochberg LR 
(2011) Neural control of cursor trajectory and click by a hu-
man with tetraplegia 1000 days after implant of an intracorti-
cal microelectrode array. J Neural Eng 8:025027.
46.	Pandarinath C, Gilja V, Blabe CH, Nuyujukian P, Sarma AA, 
Sorice BL, Eskandar EN, Hochberg LR, Henderson JM, She-
noy KV (2015) Neural population dynamics in human motor 
cortex during movements in people with ALS. Elife 4:e07436.
47.	Gilja V, Pandarinath C, Blabe CH, Nuyujukian P, Simeral JD, 
Sarma AA, Sorice BL, Perge JA, Jarosiewicz B, Hochberg LR, 
Shenoy KV, Henderson JM (2015) Clinical translation of a 
high-performance neural prosthesis. Nat Med 21:1142-1145.
48.	Jarosiewicz B, Sarma AA, Bacher D, Masse NY, Simeral JD, 
Sorice B, Oakley EM, Blabe C, Pandarinath C, Gilja V, Cash 
SS, Eskandar EN, Friehs G, Henderson JM, Shenoy KV, 
Donoghue JP, Hochberg LR (2015) Virtual typing by people 
with tetraplegia using a self-calibrating intracortical brain-
computer interface. Sci Transl Med 7:313ra179.
49.	Wodlinger B, Downey JE, Tyler-Kabara EC, Schwartz AB, 
Boninger ML, Collinger JL (2015) Ten-dimensional anthro-
pomorphic arm control in a human brain-machine interface: 
difficulties, solutions, and limitations. J Neural Eng 12:016011.
50.	Bouton CE, Shaikhouni A, Annetta NV, Bockbrader MA, 
Friedenberg DA, Nielson DM, Sharma G, Sederberg PB, 
Glenn BC, Mysiw WJ, Morgan AG, Deogaonkar M, Rezai AR 
(2016) Restoring cortical control of functional movement in 
a human with quadriplegia. Nature 533:247-250.
51.	Ajiboye AB, Willett FR, Young DR, Memberg WD, Murphy 
BA, Miller JP, Walter BL, Sweet JA, Hoyen HA, Keith MW, 
Peckham PH, Simeral JD, Donoghue JP, Hochberg LR, Kirsch 
RF (2017) Restoration of reaching and grasping movements 
through brain-controlled muscle stimulation in a person 
with tetraplegia: a proof-of-concept demonstration. Lancet 
389:1821-1830.
52.	Flesher SN, Collinger JL, Foldes ST, Weiss JM, Downey JE, 
Tyler-Kabara EC, Bensmaia SJ, Schwartz AB, Boninger ML, 
Gaunt RA (2016) Intracortical microstimulation of human 
somatosensory cortex. Sci Transl Med 8:361ra141.
53.	Normann RA (2007) Technology insight: future neuropros-
thetic therapies for disorders of the nervous system. Nat Clin 
Pract Neurol 3:444-452.
54.	Wark HA, Sharma R, Mathews KS, Fernandez E, Yoo J, 
Christensen B, Tresco P, Rieth L, Solzbacher F, Normann RA, 
Tathireddy P (2013) A new high-density (25 electrodes/mm²) 
penetrating microelectrode array for recording and stimulat-
ing sub-millimeter neuroanatomical structures. J Neural Eng 
10:045003.
55.	Pochay P, Wise KD, Allard LF, Rutledge LT (1979) A multi-
channel depth probe fabricated using electron-beam lithog-
raphy. IEEE Trans Biomed Eng 26:199-206.
56.	Vetter RJ, Otto KJ, Marzullo TC, Kipke DR (2003) Brain-
machine interfaces in rat motor cortex: neuronal operant 
conditioning to perform a sensory detection task. Int IEEE 
EMBS Conf Neural Eng 2003:637-640.
57.	Kipke DR, Vetter RJ, Williams JC, Hetke JF (2003) Silicon-
substrate intracortical microelectrode arrays for long-term 

467
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
recording of neuronal spike activity in cerebral cortex. IEEE 
Trans Neural Syst Rehabil Eng 11:151-155.
58.	Vetter RJ, Williams JC, Hetke JF, Nunamaker EA, Kipke DR 
(2004) Chronic neural recording using silicon-substrate mi-
croelectrode arrays implanted in cerebral cortex. IEEE Trans 
Biomed Eng 51:896-904.
59.	Frost SB, Dunham CL, Barbay S, Krizsan-Agbas D, Winter 
MK, Guggenmos DJ, Nudo RJ (2015) Output properties of 
the cortical hindlimb motor area in spinal cord-injured rats. J 
Neurotrauma 32:1666-1673.
60.	Guggenmos DJ, Azin M, Barbay S, Mahnken JD, Dunham 
C, Mohseni P, Nudo RJ (2013) Restoration of function after 
brain damage using a neural prosthesis. Proc Natl Acad Sci U 
S A 110:21177-21182.
61.	Barz F, Livi A, Lanzilotto M, Maranesi M, Bonini L, Paul O, 
Ruther P (2017) Versatile, modular 3D microelectrode arrays 
for neuronal ensemble recordings: from design to fabrication, 
assembly, and functional validation in non-human primates. J 
Neural Eng 14:036010.
62.	Schalk G, Leuthardt EC (2011) Brain-computer interfaces 
using electrocorticographic signals. IEEE Rev Biomed Eng 
4:140-154.
63.	Pistohl T, Ball T, Schulze-Bonhage A, Aertsen A, Mehring C 
(2008) Prediction of arm movement trajectories from ECoG-
recordings in humans. J Neurosci Methods 167:105-114.
64.	Chao ZC, Nagasaka Y, Fujii N (2010) Long-term asynchro-
nous decoding of arm motion using electrocorticographic 
signals in monkeys. Front Neuroeng 3:3.
65.	Rouse AG, Williams JJ, Wheeler JJ, Moran DW (2016) Spatial 
co-adaptation of cortical control columns in a micro-ECoG 
brain-computer interface. J Neural Eng 13:056018.
66.	Ryun S, Kim JS, Lee H, Chung CK (2017) Tactile frequency-
specific high-gamma activities in human primary and sec-
ondary somatosensory cortices. Sci Rep 7:15442.
67.	Wang W, Degenhart AD, Collinger JL, Vinjamuri R, Sudre GP, 
Adelson PD, Holder DL, Leuthardt EC, Moran DW, Boninger 
ML, Schwartz AB, Crammond DJ, Tyler-Kabara EC, Weber DJ 
(2009) Human motor cortical activity recorded with Micro-
ECoG electrodes, during individual finger movements. Conf 
Proc IEEE Eng Med Biol Soc 2009:586-589.
68.	Wang W, Collinger JL, Degenhart AD, Tyler-Kabara EC, 
Schwartz AB, Moran DW, Weber DJ, Wodlinger B, Vinjamuri 
RK, Ashmore RC, Kelly JW, Boninger ML (2013) An electro-
corticographic brain interface in an individual with Tetraple-
gia. PLoS One 8:e55344.
69.	Shin D, Watanabe H, Kambara H, Nambu A, Isa T, Nishimura 
Y, Koike Y (2012) Prediction of muscle activities from electro-
corticograms in primary motor cortex of primates. PLoS One 
7:e47992.
70.	Rubehn B, Bosman C, Oostenveld R, Fries P, Stieglitz T (2009) 
A MEMS-based flexible multichannel ECoG-electrode array. 
J Neural Eng 6:036003.
71.	Henle C, Raab M, Cordeiro JG, Doostkam S, Schulze-
Bonhage A, Stieglitz T, Rickert J (2011) First long term in 
vivo study on subdurally implanted micro-ECoG electrodes, 
manufactured with a novel laser technology. Biomed Micro-
devices 13:59-68.
72.	Toda H, Suzuki T, Sawahata H, Majima K, Kamitani Y, 
Hasegawa I (2011) Simultaneous recording of ECoG and 
intracortical neuronal activity using a flexible multichannel 
electrode-mesh in visual cortex. Neuroimage 54:203-212.
73.	Slutzky MW, Jordan LR, Krieg T, Chen M, Mogul DJ, Miller 
LE (2010) Optimal spacing of surface electrode arrays for 
brain-machine interface applications. J Neural Eng 7:26004.
74.	Tolstosheeva E, Gordillo-González V, Hertzberg T, Kempen 
L, Michels I, Kreiter A, Lang W (2011) A novel flex-rigid and 
soft-release ECoG array. Conf Proc IEEE Eng Med Biol Soc 
2011:2973-2976.
75.	Tolstosheeva E, Gordillo-González V, Biefeld V, Kempen L, 
Mandon S, Kreiter AK, Lang W (2015) A multi-channel, flex-
rigid ECoG microelectrode array for visual cortical interfac-
ing. Sensors (Basel) 15:832-854.
76.	Charvet G, Foerster M, Chatalic G, Michea A, Porcherot J, 
Bonnet S, Filipe S, Audebert P, Robinet S, Josselin V, Reverdy 
J, D’Errico R, Sauter F, Mestais C, Benabid AL (2012) A wire-
less 64-channel ECoG recording electronic for implantable 
monitoring and BCI applications: WIMAGINE. Conf Proc 
IEEE Eng Med Biol Soc 2012:783-786.
77.	Mollazadeh M, Greenwald E, Thakor NV, Schieber M, Cau-
wenberghs G (2011) Wireless micro-ECoG recording in 
primates during reach-to-grasp movements. IEEE Biomed 
Circuits Syst Conf 2011:237-240.
78.	Chang CW, Chiou JC (2013) A wireless and batteryless mi-
crosystem with implantable grid electrode/3-dimensional 
probe array for ECoG and extracellular neural recording in 
rats. Sensors (Basel) 13:4624-4639.
79.	Flint RD, Wright ZA, Scheid MR, Slutzky MW (2013) Long 
term, stable brain machine interface performance using local 
field potentials and multiunit spikes. J Neural Eng 10:056005.
80.	Henle C, Raab M, Cordeiro JG, Doostkam S, Schulze-
Bonhage A, Stieglitz T, Rickert J (2011) First long term in 
vivo study on subdurally implanted micro-ECoG electrodes, 
manufactured with a novel laser technology. Biomed Micro-
devices 13:59-68.

468
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
81.	Liu J, Fu TM, Cheng Z, Hong G, Zhou T, Jin L, Duvvuri M, 
Jiang Z, Kruskal P, Xie C, Suo Z, Fang Y, Lieber CM (2015) 
Syringe-injectable electronics. Nat Nanotechnol 10:629-636.
82.	Tian B, Liu J, Dvir T, Jin L, Tsui JH, Qing Q, Suo Z, Langer R, 
Kohane DS, Lieber CM (2012) Macroporous nanowire na-
noelectronic scaffolds for synthetic tissues. Nat Mater 11:986-
994.
83.	Liu J, Xie C, Dai X, Jin L, Zhou W, Lieber CM (2013) Multi-
functional three-dimensional macroporous nanoelectronic 
networks for smart materials. Proc Natl Acad Sci U S A 
110:6694-6699.
84.	Patolsky F, Zheng G, Lieber CM (2006) Fabrication of silicon 
nanowire devices for ultrasensitive, label-free, real-time de-
tection of biological and chemical species. Nat Protoc 1:1711-
1724.
85.	Javey A, Nam S, Friedman RS, Yan H, Lieber CM (2007) 
Layer-by-layer assembly of nanowires for three-dimensional, 
multifunctional electronics. Nano Lett 7:773-777.
86.	Fu TM, Hong G, Zhou T, Schuhmann TG, Viveros RD, Lieber 
CM (2016) Stable long-term chronic brain mapping at the 
single-neuron level. Nat Methods 13:875-882.
87.	Cakulev I, Efimov IR, Waldo AL (2009) Cardioversion: past, 
present, and future. Circulation 120:1623-1632.
88.	Roubin GS, Cannon AD, Agrawal SK, Macander PJ, Dean LS, 
Baxley WA, Breland J (1992) Intracoronary stenting for acute 
and threatened closure complicating percutaneous translu-
minal coronary angioplasty. Circulation 85:916-927.
89.	Jiang WJ, Wang YJ, Du B, Wang SX, Wang GH, Jin M, Dai 
JP (2004) Stenting of symptomatic M1 stenosis of middle 
cerebral artery: an initial experience of 40 patients. Stroke 
35:1375-1380.
90.	Oxley TJ, Opie NL, John SE, Rind GS, Ronayne SM, Wheeler 
TL, Judy JW, McDonald AJ, Dornom A, Lovell TJ, Steward C, 
Garrett DJ, Moffat BA, Lui EH, Yassi N, Campbell BC, Wong 
YT, Fox KE, Nurse ES, Bennett IE, Bauquier SH, Liyanage 
KA, van der Nagel NR, Perucca P, Ahnood A, Gill KP, Yan B, 
Churilov L, French CR, Desmond PM, Horne MK, Kiers L, 
Prawer S, Davis SM, Burkitt AN, Mitchell PJ, Grayden DB, 
May CN, O’Brien TJ (2016) Minimally invasive endovascular 
stent-electrode array for high-fidelity, chronic recordings of 
cortical neural activity. Nat Biotechnol 34:320-327.
91.	Opie NL, van der Nagel NR, John SE, Vessey K, Rind GS, 
Ronayne SM, Fletcher EL, May CN, OBrien TJ, Oxley TJ 
(2017) Micro-CT and histological evaluation of an neural in-
terface implanted within a blood vessel. IEEE Trans Biomed 
Eng 64:928-934.
92.	Sefcik RK, Opie NL, John SE, Kellner CP, Mocco J, Oxley TJ 
(2016) The evolution of endovascular electroencephalogra-
phy: historical perspective and future applications. Neurosurg 
Focus 40:E7.
93.	Opie NL, John SE, Rind GS, Ronayne SM, Grayden DB, 
Burkitt AN, May CN, O’Brien TJ, Oxley TJ (2016) Chronic 
impedance spectroscopy of an endovascular stent-electrode 
array. J Neural Eng 13:046020.
94.	Schwarz DA, Lebedev MA, Hanson TL, Dimitrov DF, Lehew 
G, Meloy J, Rajangam S, Subramanian V, Ifft PJ, Li Z, Ramak-
rishnan A, Tate A, Zhuang KZ, Nicolelis MA (2014) Chronic, 
wireless recordings of large-scale brain activity in freely mov-
ing rhesus monkeys. Nat Methods 11:670-676.
95.	Rajangam S, Tseng PH, Yin A, Lehew G, Schwarz D, Lebedev 
MA, Nicolelis MA (2016) Wireless cortical brain-machine 
interface for whole-body navigation in primates. Sci Rep 
6:22170.
96.	Su Y, Routhu S, Moon KS, Lee SQ, Youm W, Ozturk Y (2016) A 
wireless 32-channel implantable bidirectional brain machine 
interface. Sensors (Basel) 16:E1582.
97.	Seo D, Carmena JM, Rabaey JM, Maharbiz MM, Alon E 
(2015) Model validation of untethered, ultrasonic neural dust 
motes for cortical recording. J Neurosci Methods 244:114-
122.
98.	Song YK, Borton DA, Park S, Patterson WR, Bull CW, Laiwal-
la F, Mislow J, Simeral JD, Donoghue JP, Nurmikko AV (2009) 
Active microelectronic neurosensor arrays for implantable 
brain communication interfaces. IEEE Trans Neural Syst Re-
habil Eng 17:339-345.
99.	Bashirullah R, Harris JG, Sanchez JC, Nishida T, Principe 
JC (2007) Florida wireless implantable recording electrodes 
(FWIRE) for brain machine interfaces. IEEE Int Symp Cir-
cuits Syst Proc 2007:2084-2087.
100.	Azin M, Guggenmos DJ, Barbay S, Nudo RJ, Mohseni P (2011) 
A battery-powered activity-dependent intracortical micro-
stimulation IC for brain-machine-brain interface. IEEE J 
Solid-State Circuits 46:731-745.
101.	Takahara Y, Matsuki N, Ikegaya Y (2011) Nipkow confocal 
imaging from deep brain tissues. J Integr Neurosci 10:121-
129.
102.	Martial FP, Hartell NA (2012) Programmable illumination 
and high-speed, multi-wavelength, confocal microscopy us-
ing a digital micromirror. PLoS One 7:e43942.
103.	Warden MR, Cardin JA, Deisseroth K (2014) Optical neural 
interfaces. Annu Rev Biomed Eng 16:103-129.
104.	Baubet V, Le Mouellic H, Campbell AK, Lucas-Meunier E, 
Fossier P, Brúlet P (2000) Chimeric green fluorescent protein-
aequorin as bioluminescent Ca
2+ reporters at the single-cell 

469
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
level. Proc Natl Acad Sci U S A 97:7260-7265.
105.	Wachowiak M, Cohen LB (2001) Representation of odorants 
by receptor neuron input to the mouse olfactory bulb. Neu-
ron 32:723-735.
106.	Williams DA, Fogarty KE, Tsien RY, Fay FS (1985) Calcium 
gradients in single smooth muscle cells revealed by the digital 
imaging microscope using Fura-2. Nature 318:558-561.
107.	Mank M, Reiff DF, Heim N, Friedrich MW, Borst A, Gries-
beck O (2006) A FRET-based calcium biosensor with fast sig-
nal kinetics and high fluorescence change. Biophys J 90:1790-
1796.
108.	Horikawa K, Yamada Y, Matsuda T, Kobayashi K, Hashimoto 
M, Matsu-ura T, Miyawaki A, Michikawa T, Mikoshiba K, 
Nagai T (2010) Spontaneous network activity visualized by 
ultrasensitive Ca(2+) indicators, yellow Cameleon-Nano. Nat 
Methods 7:729-732.
109.	Slovin H, Arieli A, Hildesheim R, Grinvald A (2002) Long-
term voltage-sensitive dye imaging reveals cortical dynamics 
in behaving monkeys. J Neurophysiol 88:3421-3438.
110.	Petersen CC, Grinvald A, Sakmann B (2003) Spatiotemporal 
dynamics of sensory responses in layer 2/3 of rat barrel cortex 
measured in vivo by voltage-sensitive dye imaging combined 
with whole-cell voltage recordings and neuron reconstruc-
tions. J Neurosci 23:1298-1309.
111.	Ferezou I, Bolea S, Petersen CC (2006) Visualizing the cortical 
representation of whisker touch: voltage-sensitive dye imag-
ing in freely moving mice. Neuron 50:617-629.
112.	Murayama M, Larkum ME (2009) In vivo dendritic calcium 
imaging with a fiberoptic periscope system. Nat Protoc 
4:1551-1559.
113.	Ghosh KK, Burns LD, Cocker ED, Nimmerjahn A, Ziv Y, Ga-
mal AE, Schnitzer MJ (2011) Miniaturized integration of a 
fluorescence microscope. Nat Methods 8:871-878.
114.	Nagel G, Szellas T, Huhn W, Kateriya S, Adeishvili N, Berthold 
P, Ollig D, Hegemann P, Bamberg E (2003) Channelrhodop-
sin-2, a directly light-gated cation-selective membrane chan-
nel. Proc Natl Acad Sci U S A 100:13940-13945.
115.	Zhang F, Wang LP, Boyden ES, Deisseroth K (2006) Channel-
rhodopsin-2 and optical control of excitable cells. Nat Meth-
ods 3:785-792.
116.	Wong J, Abilez OJ, Kuhl E (2012) Computational optogenet-
ics: a novel continuum framework for the photoelectrochem-
istry of living systems. J Mech Phys Solids 60:1158-1178.
117.	Aravanis AM, Wang LP, Zhang F, Meltzer LA, Mogri MZ, 
Schneider MB, Deisseroth K (2007) An optical neural inter-
face: in vivo control of rodent motor cortex with integrated 
fiberoptic and optogenetic technology. J Neural Eng 4:S143-
S156.
118.	Wentz CT, Bernstein JG, Monahan P, Guerra A, Rodriguez 
A, Boyden ES (2011) A wirelessly powered and controlled 
device for optical neural control of freely-behaving animals. J 
Neural Eng 8:046021.
119.	Iwai Y, Honda S, Ozeki H, Hashimoto M, Hirase H (2011) A 
simple head-mountable LED device for chronic stimulation 
of optogenetic molecules in freely moving mice. Neurosci Res 
70:124-127.
120.	Dagnew R, Lin YY, Agatep J, Cheng M, Jann A, Quach V, Mon-
roe M, Singh G, Minasyan A, Hakimian J, Kee T, Cushman 
J, Walwyn W (2017) CerebraLux: a low-cost, open-source, 
wireless probe for optogenetic stimulation. Neurophotonics 
4:045001.
121.	Yashiro H, Nakahara I, Funabiki K, Riquimaroux H (2017) 
Micro-endoscopic system for functional assessment of neu-
ral circuits in deep brain regions: simultaneous optical and 
electrical recordings of auditory responses in mouse’s inferior 
colliculus. Neurosci Res 119:61-69.
122.	Zhao Z, Luan L, Wei X, Zhu H, Li X, Lin S, Siegel JJ, Chitwood 
RA, Xie C (2017) Nanoelectronic coating enabled versatile 
multifunctional neural probes. Nano Lett 17:4588-4595.
123.	LeChasseur Y, Dufour S, Lavertu G, Bories C, Deschênes M, 
Vallée R, De Koninck Y (2011) A microprobe for parallel 
optical and electrical recordings from single neurons in vivo. 
Nat Methods 8:319-325.
124.	Anikeeva P, Andalman AS, Witten I, Warden M, Goshen I, 
Grosenick L, Gunaydin LA, Frank LM, Deisseroth K (2011) 
Optetrode: a multichannel readout for optogenetic control in 
freely moving mice. Nat Neurosci 15:163-170.
125.	Voigts J, Siegle JH, Pritchett DL, Moore CI (2013) The flex-
Drive: an ultra-light implant for optical control and highly 
parallel chronic recording of neuronal ensembles in freely 
moving mice. Front Syst Neurosci 7:8.
126.	Kwon KY, Sirowatka B, Weber A, Li W (2013) Opto-μECoG 
array: a hybrid neural interface with transparent μECoG elec-
trode array and integrated LEDs for optogenetics. IEEE Trans 
Biomed Circuits Syst 7:593-600.
127.	Wang J, Wagner F, Borton DA, Zhang J, Ozden I, Burwell RD, 
Nurmikko AV, van Wagenen R, Diester I, Deisseroth K (2012) 
Integrated device for combined optical neuromodulation and 
electrical recording for chronic in vivo applications. J Neural 
Eng 9:016001.
128.	Boutte RW, Merlin S, Yona G, Griffiths B, Angelucci A, Kahn 
I, Shoham S, Blair S (2017) Utah optrode array customization 
using stereotactic brain atlases and 3-D CAD modeling for 
optogenetic neocortical interrogation in small rodents and 

470
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Jong-ryul Choi, et al.
nonhuman primates. Neurophotonics 4:041502.
129.	Pashaie R, Anikeeva P, Lee JH, Prakash R, Yizhar O, Prigge M, 
Chander D, Richner TJ, Williams J (2014) Optogenetic brain 
interfaces. IEEE Rev Biomed Eng 7:3-30.
130.	Baumgartner RA (2014) An optogenetic brain-machine in-
terface for spatiotemporal neuromodulation. The University 
of Wisconsin-Milwaukee [dissertation]. Milwaukee, WI.
131.	Pashaie R, Baumgartner R, Richner TJ, Brodnick SK, Azimi-
pour M, Eliceiri KW, Williams JC (2015) Closed-loop optoge-
netic brain interface. IEEE Trans Biomed Eng 62:2327-2337.
132.	Iseri E, Kuzum D (2017) Implantable optoelectronic probes 
for in vivo optogenetics. J Neural Eng 14:031001.
133.	Ramezani R, Liu Y, Dehkhoda F, Soltan A, Haci D, Zhao H, 
Firfilionis D, Hazra A, Cunningham MO, Jackson A, Con-
standinou TG, Degenaar P (2018) On-probe neural interface 
ASIC for combined electrical recording and optogenetic 
stimulation. IEEE Trans Biomed Circuits Syst 12:576-588.
134.	Jia Y, Khan W, Lee B, Fan B, Madi F, Weber A, Li W, Ghovanloo 
M (2018) Wireless opto-electro neural interface for experi-
ments with small freely behaving animals. J Neural Eng 
15:046032.
135.	Mendrela AE, Kim K, English D, McKenzie S, Seymour JP, 
Buzsáki G, Yoon E (2018) A high-resolution opto-electro-
physiology system with a miniature integrated headstage. 
IEEE Trans Biomed Circuits Syst 99:1-11.
136.	Liu X, Lu Y, Iseri E, Shi Y, Kuzum D (2018) A compact closed-
loop optogenetics system based on artifact-free transparent 
graphene electrodes. Front Neurosci 12:132.
137.	Chow BY, Boyden ES (2013) Optogenetics and translational 
medicine. Sci Transl Med 5:177ps5.
138.	Gaub BM, Berry MH, Visel M, Holt A, Isacoff EY, Flannery JG 
(2018) Optogenetic retinal gene therapy with the light gated 
GPCR vertebrate rhodopsin. In: Retinal gene therapy (Boon 
CJF, Wijnholds J, eds), pp 177-189. Humana Press, New York, 
NY.
139.	Baughman RH, Zakhidov AA, de Heer WA (2002) Carbon 
nanotubes--the route toward applications. Science 297:787-
792.
140.	Coleman JN, Khan U, Blau WJ, Gun’ko YK (2006) Small 
but strong: a review of the mechanical properties of carbon 
nanotube-polymer composites. Carbon 44:1624-1652.
141.	Wang K, Fishman HA, Dai H, Harris JS (2006) Neural stimu-
lation with a carbon nanotube microelectrode array. Nano 
Lett 6:2043-2048.
142.	Keefer EW, Botterman BR, Romero MI, Rossi AF, Gross GW 
(2008) Carbon nanotube coating improves neuronal record-
ings. Nat Nanotechnol 3:434-439.
143.	Guitchounts G, Markowitz JE, Liberti WA, Gardner TJ (2013) 
A carbon-fiber electrode array for long-term neural record-
ing. J Neural Eng 10:046016.
144.	Vitale F, Summerson SR, Aazhang B, Kemere C, Pasquali M 
(2015) Neural stimulation and recording with bidirectional, 
soft carbon nanotube fiber microelectrodes. ACS Nano 
9:4465-4474.
145.	Zhu Y, Murali S, Cai W, Li X, Suk JW, Potts JR, Ruoff RS (2010) 
Graphene and graphene oxide: synthesis, properties, and ap-
plications. Adv Mater 22:3906-3924.
146.	Chen CH, Lin CT, Hsu WL, Chang YC, Yeh SR, Li LJ, Yao DJ 
(2013) A flexible hydrophilic-modified graphene microprobe 
for neural and cardiac recording. Nanomedicine (Lond) 
9:600-604.
147.	Park DW, Schendel AA, Mikael S, Brodnick SK, Richner TJ, 
Ness JP, Hayat MR, Atry F, Frye ST, Pashaie R, Thongpang S, 
Ma Z, Williams JC (2014) Graphene-based carbon-layered 
electrode array technology for neural imaging and optoge-
netic applications. Nat Commun 5:5258.
148.	Kuzum D, Takano H, Shim E, Reed JC, Juul H, Richardson 
AG, de Vries J, Bink H, Dichter MA, Lucas TH, Coulter DA, 
Cubukcu E, Litt B (2014) Transparent and flexible low noise 
graphene electrodes for simultaneous electrophysiology and 
neuroimaging. Nat Commun 5:5259.
149.	Liu TC, Chuang MC, Chu CY, Huang WC, Lai HY, Wang CT, 
Chu WL, Chen SY, Chen YY (2016) Implantable graphene-
based neural electrode interfaces for electrophysiology and 
neurochemistry in in vivo hyperacute stroke model. ACS 
Appl Mater Interfaces 8:187-196.
150.	Apollo NV, Maturana MI, Tong W, Nayagam DAX, Shivdasani 
MN, Foroughi J, Wallace GG, Prawer S, Ibbotson MR, Garrett 
DJ (2015) Soft, flexible freestanding neural stimulation and 
recording electrodes fabricated from reduced graphene oxide. 
Adv Funct Mater 25:3551-3559.
151.	Park S, Song YJ, Boo H, Chung TD (2010) Nanoporous Pt 
microelectrode for neural stimulation and recording: in vitro 
characterization. J Phys Chem C 114:8721-8726.
152.	Suyatin DB, Wallman L, Thelin J, Prinz CN, Jörntell H, Samu-
elson L, Montelius L, Schouenborg J (2013) Nanowire-based 
electrode for acute in vivo neural recordings in the brain. 
PLoS One 8:e56673.
153.	Abidian MR, Corey JM, Kipke DR, Martin DC (2010) 
Conducting-polymer nanotubes improve electrical proper-
ties, mechanical adhesion, neural attachment, and neurite 
outgrowth of neural electrodes. Small 6:421-429.
154.	Piret G, Hébert C, Mazellier JP, Rousseau L, Scorsone E, Cot-
tance M, Lissorgues G, Heuschkel MO, Picaud S, Bergonzo P, 

471
www.enjournal.org
https://doi.org/10.5607/en.2018.27.6.453
Implantable Neural Probes for BMI
Yvert B (2015) 3D-nanostructured boron-doped diamond 
for microelectrode array neural interfacing. Biomaterials 
53:173-183.
155.	Kim SP, Simeral JD, Hochberg LR, Donoghue JP, Black MJ 
(2008) Neural control of computer cursor velocity by decod-
ing motor cortical spiking activity in humans with tetraplegia. 
J Neural Eng 5:455-476.
156.	Li Z, O’Doherty JE, Lebedev MA, Nicolelis MA (2011) Adap-
tive decoding for brain-machine interfaces through Bayesian 
parameter updates. Neural Comput 23:3162-3204.
157.	Shoham S, Paninski LM, Fellows MR, Hatsopoulos NG, 
Donoghue JP, Normann RA (2005) Statistical encoding mod-
el for a primary motor cortical brain-machine interface. IEEE 
Trans Biomed Eng 52:1312-1322.
158.	Nishimoto S, Vu AT, Naselaris T, Benjamini Y, Yu B, Gallant JL 
(2011) Reconstructing visual experiences from brain activity 
evoked by natural movies. Curr Biol 21:1641-1646.
159.	Egert D, Najafi K (2011) New class of chronic recording mul-
tichannel neural probes with post-implant self-deployed sat-
ellite recording sites. Int Solid State Sens Actuators Microsyst 
Conf 2011:958-961.
160.	Daneshvar ED, Kipke D, Smela E (2012) Navigating conju-
gated polymer actuated neural probes in a brain phantom. 
Proc SPIE 8340:834009.
161.	Denning T, Matsuoka Y, Kohno T (2009) Neurosecurity: se-
curity and privacy for neural devices. Neurosurg Focus 27:E7.
162.	Bonaci T, Herron J, Matlack C, Chizeck HJ (2015) Securing 
the exocortex: a twenty-first century cybernetics challenge. 
IEEE Technol Soc Mag 34:44-51.
