REVIEW
published: 07 August 2019
doi: 10.3389/fnins.2019.00804
Edited by:
Aysegul Gunduz,
University of Florida, United States
Reviewed by:
Peter Brunner,
Albany Medical College, United States
David Thomas Bundy,
University of Kansas Medical Center
Research Institute, United States
*Correspondence:
Rajesh P. N. Rao
rao@cs.washington.edu
Specialty section:
This article was submitted to
Neuroprosthetics,
a section of the journal
Frontiers in Neuroscience
Received: 01 March 2019
Accepted: 18 July 2019
Published: 07 August 2019
Citation:
Caldwell DJ, Ojemann JG and
Rao RPN (2019) Direct Electrical
Stimulation in Electrocorticographic
Brain–Computer Interfaces: Enabling
Technologies for Input to Cortex.
Front. Neurosci. 13:804.
doi: 10.3389/fnins.2019.00804
Direct Electrical Stimulation in
Electrocorticographic
Brain–Computer Interfaces: Enabling
Technologies for Input to Cortex
David J. Caldwell1,2,3, Jeffrey G. Ojemann3,4 and Rajesh P. N. Rao1,3,5*
1 Department of Bioengineering, University of Washington, Seattle, WA, United States, 2 Medical Scientist Training Program,
University of Washington, Seattle, WA, United States, 3 Center for Neurotechnology, University of Washington, Seattle, WA,
United States, 4 Department of Neurological Surgery, University of Washington, Seattle, WA, United States, 5 Paul G. Allen
School of Computer Science and Engineering, University of Washington, Seattle, WA, United States
Electrocorticographic
brain
computer
interfaces
(ECoG-BCIs)
offer
tremendous
opportunities for restoring function in individuals suffering from neurological damage
and for advancing basic neuroscience knowledge. ECoG electrodes are already
commonly used clinically for monitoring epilepsy and have greater spatial speciﬁcity
in recording neuronal activity than techniques such as electroencephalography (EEG).
Much work to date in the ﬁeld has focused on using ECoG signals recorded
from cortex as control outputs for driving end effectors. An equally important
but less explored application of an ECoG-BCI is directing input into cortex using
ECoG electrodes for direct electrical stimulation (DES). Combining DES with ECoG
recording enables a truly bidirectional BCI, where information is both read from
and written to the brain. We discuss the advantages and opportunities, as well
as the barriers and challenges presented by using DES in an ECoG-BCI. In this
article, we review ECoG electrodes, the physics and physiology of DES, and the
use of electrical stimulation of the brain for the clinical treatment of disorders such
as epilepsy and Parkinson’s disease. We brieﬂy discuss some of the translational,
regulatory, ﬁnancial, and ethical concerns regarding ECoG-BCIs. Next, we describe
the use of ECoG-based DES for providing sensory feedback and for probing and
modifying cortical connectivity. We explore future directions, which may draw on
invasive animal studies with penetrating and surface electrodes as well as non-invasive
stimulation methods such as transcranial magnetic stimulation (TMS). We conclude by
describing enabling technologies, such as smaller ECoG electrodes for more precise
targeting of cortical areas, signal processing strategies for simultaneous stimulation and
recording, and computational modeling and algorithms for tailoring stimulation to each
individual brain.
Keywords: electrocorticography, brain–computer interface (BCI), direct electrical stimulation, intracranial
electrodes, plasticity induction, neuroprosthetic, sensory restoration, neuromodulation
Frontiers in Neuroscience | www.frontiersin.org
1
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
INTRODUCTION
Electrocorticography (ECoG) is used clinically as a recording
modality for diagnosing speciﬁc spatial regions of focal epilepsy
onset in individuals suﬀering from medically intractable epilepsy.
By using invasive monitoring, the origins of seizures can
be identiﬁed, and subsequent surgical removal of the seizure
foci can reduce the frequency of or eliminate seizures. After
surgical resection, approximately 50% or greater of patients
experience signiﬁcantly improved seizure control following
surgical treatment (Englot and Chang, 2014). For monitoring,
patients are routinely implanted for 1–2 weeks with electrodes
either directly on top of the dura (epidural), beneath the dura
(subdural), or implanted in cortex [depth electrodes, or stereo
electroencephalography (sEEG)]. The term intracranial EEG, or
iEEG, is often used to describe all implanted electrodes. We will
use the term ECoG electrodes in this article to encompass surface
as well as penetrating depth electrodes. Following electrode
implantation, patients remain in the hospital under clinical
monitoring by a team of neurologists and epilepsy technicians,
until the clinical team has collected enough data to precisely
localize the focal seizure zones for surgical resection.
To complement the passive recording of epileptic events,
direct electrical stimulation (DES) (Vincent et al., 2016b)
[or when applied particularly to cortex, known as direct
cortical stimulation (DCS) (Giussani et al., 2010), or direct
electrical cortical stimulation (DECS)] through ECoG electrodes
is commonly performed for clinical mapping purposes, both
intraoperatively and during the patients’ clinical observation.
For clinical mapping the clinical team electrically stimulates
diﬀerent brain regions to delineate regions of cortex important
for language, motor, and sensory function. By stimulating
particular brain areas and observing the eﬀects by querying the
patient, the clinical team can avoid resecting areas important for
cognitive function and preserve these functions in an individual
after surgical resection. The combination of recording and
mapping through stimulation enables the clinical team to be
best informed when making clinical decisions regarding reducing
or eliminating seizures through resection, while maintaining
cortical function. Clinical teams perform stimulation of both
cortical and subcortical structures and pathways. We use
the term DES here to refer to general electrical stimulation
of any brain region through implanted electrodes, while we
consider DCS a subcategory speciﬁcally describing stimulation of
surface gray matter.
Direct electrical stimulation for clinical uses goes beyond
delineating cortical regions of activity. For example, deep
brain stimulation (DBS) is a therapy currently being used for
therapeutic treatment of movement disorders and psychiatric
illnesses. Electrodes similar to those used for sEEG are implanted
into deep brain structures, and stimulation helps ameliorate
clinical symptoms. The space of DBS research is vast, and we will
not go into extensive detail in this review. Instead, we highlight
the widespread use of DBS as a demonstration of the therapeutic
use of clinical stimulation through implanted electrodes, and we
draw from current research in the DBS ﬁeld to frame future
directions for DES.
In this article, we ﬁrst review the characteristics of implanted
electrodes, the eﬀect of electrical stimulation through them on
cortex, and the nature of signals recorded through them. We then
discuss current clinical uses of DES for disorders such as epilepsy,
and brieﬂy cover DBS and its applications for diseases such as
Parkinson’s disease and essential tremor. We also discuss some
of the translational, regulatory, ﬁnancial, and ethical concerns
with ECoG-BCIs. We subsequently describe how ECoG-based
DES can be used to provide sensory feedback and to probe and
modify cortical connectivity. We then review future applications
of DES in ECoG-BCIs, which may draw from invasive animal
studies with penetrating and surface electrodes and non-invasive
stimulation methods such as transcranial magnetic stimulation
(TMS) and transcranial electrical stimulation (TES). We discuss
how enabling technologies, such as smaller ECoG electrodes for
more precise targeting on smaller spatial scales, software and
hardware that allow simultaneous stimulation and recording, and
computational modeling for tailoring stimulation to individual
patients, could enable the realization of full-ﬂedged bidirectional
ECoG-BCIs for a variety of applications.
THE ELECTRICAL-NEURAL INTERFACE
Electrodes
Current clinically used ECoG electrodes are often embedded in a
silicone sheet and are made of platinum or stainless steel. The
electrodes are 1.5 mm diameter circular contacts with 4 mm
spacing (“micro”-ECoG electrodes)1, to 2.3–3 mm diameter
contacts with 10 mm spacing for “macro”-ECoG electrodes
(Chang, 2015). Depth electrodes are frequently comprised of
platinum, with cylindrical contacts, and can be inserted with
or without stereotactic guidance. These are commonly used to
localize seizures coming from deep brain structures, such as the
hippocampus. DBS electrodes are similar to depth electrodes in
that they are linear probes with cylindrical contacts, although
they can be of smaller diameter, with tighter electrode spacing
and fewer contacts.
Stimulation
Implanted electrodes can be used for direct modulation of
neural activity through electrical stimulation. In order to better
understand the underlying mechanisms of stimulation, we
ﬁrst consider the eﬀects of stimulation on a single neuron.
At the single neuron level, the redistribution of charge, and
subsequent depolarization, where the inside of the cell becomes
more positive relative to the extracellular ﬂuid, can cause an
action potential to be generated which propagates down the
cell’s axon. Hyperpolarization, which occurs when the inside
of the cell becomes more negative relative to the outside of
the cell, can inhibit action potentials. Electrical stimulation,
through a redistribution of charge within an axon, can result
either in hyperpolarization or depolarization. When suﬃcient
1We discuss advances in research-grade microECoG electrodes with much smaller
electrode contact size and tighter spacing in the section “Enabling Technologies –
Materials and Electronics.”
Frontiers in Neuroscience | www.frontiersin.org
2
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
depolarization is achieved, an action potential is generated
through the diﬀusion of ions through sodium, potassium,
and calcium channels (Bean, 2007). Subthreshold intracellular
stimulation, where an action potential is not generated, can result
in the potentiation of synaptic strength with NMDA receptor
mediation in the neuron’s synapses (Alonso et al., 1990).
In solutions, electrical stimulation results in the redistribution
of ions through non-Faradaic reactions, and the transfer of
electrons to electrolytes in the solution through Faradaic
reactions (Merrill et al., 2005). There exist both reversible and
irreversible Faradaic reactions: which one occurs depends on
the rate of the electron transfers relative to the mass transport
of the reactant. We discuss these reactions further and the
impact of stimulation parameters on them in the section
“Limitations and Considerations.” Through these mechanisms,
charge is redistributed. When this redistribution of charge
causes depolarization directly beneath the electrode, for the
case of a single neuron, the stimulation is often referred to as
cathodal stimulation, while electrical stimulation which causes
hyperpolarization directly beneath the electrode is referred to as
anodal stimulation (Figure 1A). On the scale of larger electrodes,
such as with ECoG arrays, cathodal stimulation often refers to
negative voltages and currents directly beneath the electrode,
while anodal stimulation refers to positive voltages and currents.
Stimulation on a local scale can be achieved through
intracortical
microstimulation
(ICMS),
where
electrical
stimulation activates neurons primarily through their axons
passing through the region of cortex stimulated (Nowak and
Bullier, 1998; Tehovnik et al., 2006). However, other regions of
the cell such as the cell body and dendrites may also be activated
depending on stimulus polarity and orientation. Anodal pulses
best activate cell bodies and terminals, compared to cathodal
pulses which best activate axons (McIntyre and Grill, 2000).
In both cases, it is the outward ﬂowing current at the axon
initial segment or nodes of Ranvier along the axon that results
in neuronal excitation (McIntyre and Grill, 2000; Tehovnik
et al., 2006). ICMS is thought to sparsely activate a population
of cortical neurons, rather than just ones proximal to the
stimulation electrode tip (Histed et al., 2009).
The distance of neuron elements from the stimulation source
changes whether or not these elements will be hyperpolarized
or depolarized by a corresponding cathodic or anodic stimulus.
Directly beneath a cathode, a membrane will become depolarized,
and hence can generate an action potential. During the case
of anodal stimulation, the area directly beneath the electrode
is hyperpolarized, but further away from the anode, action
potentials may be generated, resulting in a “virtual cathode”
(Merrill et al., 2005) (Figure 1A). Stimulation beneath the anode
can occur with surface anodal stimulation of neocortical cells,
where current hyperpolarizes apical dendrites, and subsequently
leaves through the axon resulting in depolarization (Ranck, 1975)
(Figure 1B). For the case of bipolar stimulation, an axon is
generally depolarized beneath the cathode and hyperpolarized
beneath the anode (Ranck, 1975).
Physiologically, ICMS is thought to activate both inhibitory
and excitatory populations of cells (Butovas and Schwarz,
2003), and is not thought to evoke natural patterns of cortical
activity (Millard et al., 2015). Functional magnetic resonance
imaging (fMRI) along with microstimulation has demonstrated
that microstimulation, at least in the visual cortical pathway,
suppresses the output activity of neurons which have their
aﬀerents stimulated (Logothetis et al., 2010). Further work in
microstimulation of the visual cortex has demonstrated that
microstimulation in V1 may locally activate cells, but silence
neurons further downstream (Klink et al., 2017).
The frequency of ICMS also has an impact on whether
neurons are excited or inhibited. High frequency stimulation
(>10 Hz) is thought to potentiate neural activity (long-term
potentiation) (Bliss and Lomo, 1973; Douglas, 1977), while low
frequency stimulation (<1 Hz) is thought to depress neural
activity (long-term depression) (Mulkey and Malenka, 1992).
Compared to ICMS, DES of human cortex using larger
electrodes, such as ECoG or DBS electrodes, injects current
over a larger surface area, and subsequently large amounts of
current could lead to greater activation with the potential to
spread to a larger area (Vincent et al., 2016a) (Figures 1C,D).
Additionally, depending on the anatomic location of DES,
stimulation can either evoke or inhibit neural activity (Borchers
et al., 2012). For example, DES of language areas during a
language task can disrupt speech production while DES of
somatosensory cortex can evoke sensations and DES of motor
cortex can evoke movements. In terms of subdural ECoG
stimulation in humans, the patterns and types of cells activated
are thought to depend on the intricate details of cortical
geometry, cell ﬁber orientation (Kudela and Anderson, 2015),
and whether the pulses are anodal or cathodal (Seo et al., 2015)
(Figures 1C,D). A ﬁnite element model (FEM) of subdural
cortical stimulation with integrated neuron models was used
to demonstrate that neurons deeper in the bank (buried in
cortex) are more activated during cathodal subdural stimulation,
while those in the wider crown are activated during anodal
stimulation (Seo et al., 2015). DES through ECoG electrodes can
result in both local eﬀects, and eﬀects remote to stimulation.
The resultant signals at other electrodes are often referred
to as cortico-cortico evoked potentials (CCEP) (Keller et al.,
2014b). These have been reviewed thoroughly by Keller et al.
(2014b, for more details). We will therefore only review some
of the relevant physiology here. Pyramidal cells, which are the
source of the majority of cortical output, and lie in cortical
layers 2, 3, 5, and 6 can have their superﬁcial dendritic trees
depolarized. Layer 2/3 inhibitory GABA interneurons can be
depolarized, which then synapse preferentially near the soma
of pyramidal cells (Brill and Huguenard, 2009) and cause
a decrease in pyramidal cell activity due to the inhibitory
nature of GABA signaling. If there are axons passing through
the region of stimulation, both orthodromic and antidromic
stimulation can occur (Keller et al., 2014b). The measured surface
potentials are therefore a combination of the initial monosynaptic
connections, cortico-cortical pathways, and cortico-subcortical
pathways which would explain the polymorphic response lasting
hundreds of milliseconds (Matsumoto et al., 2006).
The mechanisms of DBS stimulation are not yet currently
understood, and are thought to involve the modulation of the
networks targeted by the stimulation, rather than involving solely
Frontiers in Neuroscience | www.frontiersin.org
3
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
FIGURE 1 | Effect of stimulation on a single neuron and on a population of neurons. (A) Stimulation along a nerve ﬁber results in depolarization beneath the cathode,
and hyperpolarization beneath an anode. (B) Single neurons can be stimulated by both anodal and cathodal stimulation depending on their orientation. In this
example, anodal current enters the dendrites of the neuron and leaves through the axon, which results in depolarization of the axon and an action potential. (C) In
the case of stimulation through ECoG electrodes, a large population of neurons can be activated by stimulation. Shown are approximate scales of an ECoG
electrode relative to the precentral and postcentral gyrus, along with a representative mixed population of pyramidal neurons potentially depolarized by stimulation. In
the zoomed-in region, we highlight the multiple orientations of neurons that could be activated. (D) An axial slice in a co-registered CT and MRI image following
implantation with an ECoG array shows the potential current paths that different stimulation conﬁgurations would have to pass through, illustrating the large
populations of neurons present within the potential current path. (A,B) Inspired by Ranck (1975).
immediate inhibitory eﬀects on the targeted anatomic region
(Montgomery and Gale, 2008; Ashkan et al., 2017).
In summary, the results reviewed in this section speak to the
immense complexities of engineering stimulation in humans and
the work that remains to be done in understanding both its
physical and neural eﬀects.
Sensing
A key part of a BCI is the recording of neural activity to use
as a control signal in order to successfully modulate the system
using stimulation. The summed activity of many hundreds of
thousands of neurons in the cortical tissue under an ECoG
electrode contributes to the electric voltage recorded from the
electrode. The increased ﬁring rate of populations of neurons
results in a broad increase in power across all frequencies,
which is more easily separable in the broadband gamma band
(above 50 Hz), rather than the lower frequency bands (Miller
et al., 2008). This is because other frequency bands modulate
up and down independently during diﬀerent tasks and brain
states, masking the broadband increase in power. The higher
frequency components are more asynchronous, and therefore
are not as subject to this masking eﬀect (Hermes et al., 2017).
Lower frequency bands, such as the alpha (8–12 Hz) and beta
(13–30 Hz) band, are thought to represent pulsed inhibition that
serves to gate and coordinate neuronal ﬁring (Schalk, 2015).
Therefore, analysis of broadband gamma activity reveals the local
neuronal ﬁring dynamics, while analysis of theta (4–8 Hz), alpha,
and beta frequency regimes yields insight into the coordinating
mechanisms across the brain.
The diﬀerent oscillatory features discussed above have been
explored for advancing our understanding of how diﬀerent
cortical regions function during motor movement and language
function (Bouchard et al., 2013; Flint et al., 2017). Measurements
of these signals during motor and speech imagery have been
employed in ECoG brain–computer interfaces to drive end
eﬀectors such as computer cursors (Leuthardt et al., 2004,
2006a,b) and robotic arms (Hotson et al., 2016). Furthermore,
non-motor regions can be used to drive ECoG-BCIs as well,
illustrating the general utility of oscillatory band driven BCIs
(Ramsey et al., 2006; Wilson et al., 2006).
CURRENT CLINICAL USES OF DIRECT
ELECTRICAL STIMULATION
Functional Mapping for Epilepsy and
Tumors
As detailed in the introduction, DES is frequently used both
intraoperatively and during a patient’s stay at the hospital for
functional mapping and identifying areas of cortex associated
Frontiers in Neuroscience | www.frontiersin.org
4
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
with important cognitive functions (Berger et al., 1989; Ojemann
et al., 1989; Berger and Ojemann, 1992). These mapping
procedures are done both for epilepsy surgery and tumor
resections (Berger et al., 1989; Ojemann et al., 1989; Berger and
Ojemann, 1992). Clinicians, using implanted ECoG electrodes
or stimulators in the operating room, apply DES to various
cortical and subcortical structures and pathways, and observe
location dependent eﬀects, including speech arrest in language
regions, motor movements in motor cortex, and sensory percepts
in somatosensory cortex. The results of these stimulation studies
inform where the surgeons will plan to resect; for example, if the
seizure focus is close to a language region, the surgeon and patient
may decide the surgery is not worth the risk of a permanent
language deﬁcit.
Deep Brain Stimulation
Deep brain stimulation is a prominent example of electrical
stimulation of the brain. It is currently being used for
therapeutic treatment of movement disorders [Parkinson’s
disease (Bronstein et al., 2011) and Essential Tremor (Della Flora
et al., 2010)], and is also being explored for treating psychiatric
illnesses (post-traumatic stress disorder, depression, obsessive
compulsive disorder, Tourette syndrome, Schrock et al., 2015)
and epilepsy treatment. Traditionally, linear probes of cylindrical
contacts are inserted into deep brain structures such as the
globus pallidus internus (GPi), subthalamic nucleus (STN), or
ventral intermediate nucleus of the thalamus (VIM). Following
implantation, clinicians may either be guided by intraoperative
CT imaging, or wake the patient up intraoperatively to test
for adverse eﬀects of stimulation on diﬀerent contacts, using
a monopolar (one stimulating electrode and a distant return
electrode), bipolar (two similarly sized electrodes), or multipolar
arrangement of electrodes for the steering of current.
Advances in BCI related to DBS have explored the use
of closed loop DBS to trigger stimulation of deep brain
structures in response to signals recorded from the surface
of the cortex (Herron et al., 2017). Herron et al. used
threshold crossing in the beta-band regime of recorded
ECoG
signals
over
motor
cortex
as
a
control
decision
to trigger DBS stimulation. This enables control of DBS
stimulation solely through recorded neural signals. Besides
potentially reducing the side-eﬀects of open-loop stimulation,
such closed-loop control of stimulation conserves power
and helps extend the life of the DBS device, reducing the
number of replacement surgeries needed over the life of a
user. Adaptive DBS based on recordings in STN has been
demonstrated to improve motor scores over traditional open-
loop DBS (Little et al., 2013). In addition, primate models
of Parkinson’s disease demonstrate that closed-loop DBS has
a greater eﬀect than open-loop DBS on akinesia and on the
neuronal output in both cortical and subcortical structures
(Rosin et al., 2011).
Finally, DBS is also being explored for the treatment of
particular types of epilepsy. Partial onset seizures often spread
through the circuitry of the basal ganglia, and therefore could
be controlled using DBS strategies similar to those used for
movement disorders (Halpern et al., 2008; Lega et al., 2010).
Closed Loop Stimulation for Epilepsy
Closed loop stimulation to control seizures is currently clinically
available to epilepsy patients through the Neuropace RNS system
(Morrell, 2011; Lee et al., 2015). A neurosurgeon implants ECoG
electrodes either on the cortical surface or in deeper structures
near the putative seizure focus. If an impending seizure is
detected, high frequency stimulation is triggered near the seizure
focus to control the seizure. This is a demonstration of clinically
eﬀective and already implemented DES in an ECoG-BCI, where
neural control signals are acquired in real time from the brain and
used to trigger stimulation.
ADVANTAGES OF DES RELATIVE TO
OTHER STIMULATION TECHNIQUES
An advantage of DES relative to non-invasive electrical
stimulation modalities is the delivery of much greater amounts
of the applied current to neurons. During TES2, as much as
75% of the current is shunted through the scalp and the skull
(Vöröslakos et al., 2018; Widge, 2018). This greatly blunts the
eﬃcacy of cortical stimulation, and suggests that some of the
published results using TES are due to mechanisms other than
direct neuronal excitation. In contrast, by directly stimulating the
brain and bypassing the skull and scalp, DES delivers current to
cortical structures more eﬀectively. Although the currents applied
during TES could be raised to a high enough level to reach a
desired electric ﬁeld strength at a target location in the brain,
there would be potential oﬀ-target eﬀects and skin damage due
to the amount of current required, in contrast to DES through
electrodes implanted precisely at the targeted site for this same
electric ﬁeld strength. This reinforces a large advantage of the
DES relative to TES, which is the ability to place electrodes close
to the target structures, and consequently minimize the amount
of current passing through oﬀ-target structures.
Even with epidural and subdural stimulation, not all current
reaches neurons in the cortex. Epidural stimulation results
in current shunting by the dura (Wongsarnpigoon and Grill,
2008), while both epidural and subdural stimulation have some
degree of cerebrospinal ﬂuid (CSF) shunting depending on the
characteristics of the CSF beneath or surrounding the electrodes
(Wongsarnpigoon and Grill, 2008; Guler et al., 2018).
A factor in epidural and subdural stimulation is the presence
of pain receptors within the dura which can be activated
with dural stimulation (Wirth and Van Buren, 1971). However,
previous clinical trials with epidural stimulation made no reports
of dural pain with stimulation up to 6.5 mA and 250 µs pulse
widths (Levy et al., 2008).
Transcranial magnetic stimulation has primarily been used to
induce motor movements, rather than isolated sensory percepts
(although phosphenes can often be produced via TMS, and
tapping sensations and auditory clicks can accompany TMS)
(Sliwinska et al., 2014). A method such as DES aﬀords the ability
2We use this term to encompass transcranial direct current stimulation (tDCS)
and transcranial alternating current stimulation or (tACS).
Frontiers in Neuroscience | www.frontiersin.org
5
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
to focally and speciﬁcally produce sensations that would not be
achievable through TMS.
Additionally, traditional ﬁgure-8 TMS coils are currently
unable to target cortical structures beyond 2–3 cm deep (Roth
et al., 1991; Wagner et al., 2009). DES electrodes, on the other
hand, can be physically placed in deeper regions of interest in
order to elicit the desired stimulation eﬀects. Another advantage
of DES over TMS is the fact that the maximum of the electric
ﬁeld strength induced by TMS has to occur at the cortical
surface rather than deeper structures (Heller and van Hulsteyn,
1992). This means that oﬀ-target eﬀects in cortical layers near
the surface are possible when targeting deeper structures. Even
with more sophisticated coils, such as the H-coil, the maximum
stimulation strength still occurs at the surface and greater depth
of stimulation (4–6 cm) is achieved with a loss of focality (Zangen
et al., 2005; Wagner et al., 2009). Although the ﬁeld strength
is greatest at the cortical surface for TMS, the orientation of
neurons is a critical component in the activation of neurons, as
both experimental and modeling work has shown that electric
ﬁelds tangential to the sulcal walls can activate neurons oriented
perpendicularly to them (Fox et al., 2004; Silva et al., 2008;
Seo et al., 2016). Similarly, diﬀerent layered pyramidal neurons
are activated diﬀerently between the gyral crown and sulcus
walls (Silva et al., 2008; Seo et al., 2016). This in total points
to the complex physiologic eﬀects of TMS, and the potential
diﬃculties in activating groups of neurons both on the crown of
the gyrus and within the sulcus together. A further disadvantage
of TMS is that with current hardware, use outside of the lab
is limited due to the bulky hardware and the need to maintain
a precise spatial relationship between the coil and the head
for stimulation.
The fact that DES electrodes can be placed near the deeper
structures of interest is vital for the treatment of Parkinson’s
and Essential Tremor through DBS. As these structures cannot
currently be eﬀectively stimulated through alternative methods
such as TMS, eﬀective clinical treatment relies upon DES via
electrodes near the desired brain regions.
FINANCIAL, TRANSLATIONAL,
REGULATORY, AND ETHICAL
CONCERNS FOR DES IN ECOG-BCIS
Translational, Regulatory, and Financial
Concerns
We expect early applications of ECoG-BCIs to leverage existing
clinical devices. This has been a pathway forward for many
prior medical devices. Advances in early DBS devices were
based largely oﬀof prior work in cardiac pacemaker and spinal
cord stimulation devices (Coﬀey, 2009). We imagine a similar
trajectory for DES in ECoG-BCIs. Preliminary use of DES has
been enabled by investigational device exemptions (Harvey and
Winstein, 2009). Further iterations of Medtronic DBS devices,
such as the PC + S device, have been granted an investigational
device exemption in research studies, and are improvements
upon an already clinically approved device (Herron et al., 2017).
Whenever new technology is implemented for clinical
treatment, a question of cost eﬃcacy is raised. However,
we suggest that ECoG-BCIs have the potential to be cost
eﬀective long-term devices if clinical eﬃcacy is demonstrated, as
illustrated by examples such as vagus nerve stimulators and DBS.
Vagus nerve stimulation for epilepsy has been show to be eﬀective
long-term, and cost beneﬁt analysis has shown that the cost of
the treatment pays oﬀwithin a 2 year period (Boon et al., 1999).
Although it is not universally the case, DBS in general is thought
to be cost eﬀective, when looking at studies across European and
North American Centers (Pereira et al., 2007). It has been noted
that during the adoption of DBS large-volume hospitals had lower
prices and superior short-term outcomes, which is something
to be aware of in the translation of ECoG-BCIs into the clinic
(Eskandar et al., 2009).
Ethical Concerns
Ethical concerns are critical to address for any engineered device
which is implanted in a patient. A previous review has explored
some of the ethical concerns for BCIs (Klein and Ojemann, 2016),
and we seek here to highlight some of the concerns which are
particularly relevant to ECoG-BCIs with DES.
Articulating the potential risks and long-term requirements
for an ECoG-BCI, particularly with DES, is essential for
appropriate informed consent. Biologic risks such as infection,
seizures, and tissue damage from stimulation (Cogan et al., 2016)
are accompanied by technological concerns such as repeated
surgeries for battery replacements, heating due to potential
wireless charging, and lifetime electrode wear from repeated
stimulation (Klein and Ojemann, 2016).
Privacy and security are another key aspect in implantable
medical devices, particularly with any BCIs that communicate
signals wirelessly or can be programed wirelessly. One can
imagine situations where a stimulator could be set to either
less than therapeutic levels or to unsafe levels, by malware
transmitted to the ECoG-BCI device. Research eﬀorts that build
on current security and privacy protocols for medical devices are
required to ensure neural signal security and protection against
malevolent programing.
RESEARCH DIRECTIONS FOR DES IN
ECOG-BCI
We discuss various research directions for ECoG-BCIs, with
an emphasis on future engineered applications. A previous
review (Wander and Rao, 2014) has explored the use of brain–
computer interfaces for investigating scientiﬁc questions in the
nervous system. Further information on classical ECoG-BCIs and
comparison to other types of BCIs can be found in Rao (2013).
Sensory Feedback Through DES
One potential use of ECoG-based stimulation currently being
explored is the restoration of sensory feedback for those suﬀering
from disorders such as paralysis. There is a large clinical need,
as it is estimated that 5.4 million Americans are living with
paralysis, with an estimated 41.8% of people with paralysis unable
Frontiers in Neuroscience | www.frontiersin.org
6
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
to work (Christopher and Dana Reeve Foundation, 2013). The
restoration of sensation is a priority for prosthetics users (Biddiss
et al., 2007) as well as potential BCI end users such as individuals
with paralysis (Anderson, 2004; Collinger et al., 2013). Sensory
feedback to cortex would enhance the eﬃcacy of a prosthetic
arm to aid with independent tasks, or help an individual better
interpret data from body mounted sensors. The lack of sensory
feedback in many existing brain–computer interfaces (BCIs) may
limit performance (Bensmaia and Miller, 2014; Delhaye et al.,
2016). Indeed, integration of somatosensory feedback into BCIs
has been demonstrated to improve task performance with BCIs
(Suminski et al., 2010; Klaes et al., 2014; Dadarlat et al., 2015;
Pistohl et al., 2015; Schiefer et al., 2016).
Prior work has shown that humans can respond to DES of
the surface of the primary somatosensory (S1) cortex (Ray et al.,
1999; Libet et al., 1964; Johnson et al., 2013; Hiremath et al.,
2017), which results in an artiﬁcial sensory percept organized
according to the standard somatotopy of cortex. Cronin et al.
(2016) demonstrated that DES of S1 could be used by an
individual in the absence of visual feedback to perform a motor
task. Although these percepts would not be mistaken by the
individuals for natural touch (Johnson et al., 2013; Cronin et al.,
2016; Collins et al., 2017), they are useful for performing closed-
loop BCI tasks. An open question is how using DES for feedback
compares to a normal somatosensory pathway. One way of
assessing this is through response times, which have recently
been demonstrated to be slower for DES relative to natural
touch (Caldwell et al., 2019). This speaks to the complex eﬀects
of stimulation and requires further exploration. Another key
consideration for neuroprosthetic use is the embodiment of the
prosthetic device. DES through ECoG has been shown to induce
prosthetic hand ownership, suggesting that prostheses could be
made to feel more natural as a result of DES (Collins et al., 2017).
With recent advances in materials and manufacturing,
spatially smaller microECoG arrays are able to target smaller
volumes of cortex. More targeted DES through microECoG grids
allows higher spatial selectivity relative to larger clinical electrode
grids (Hiremath et al., 2017; Lee et al., 2018), opening up the
possibility of encoding more complex percepts compared to
larger electrodes.
Although short term studies have demonstrated that these
percepts induced by DES do not feel natural, the principles of
neuroplasticity, which are prevalent in somatosensory cortex and
other associated regions, and adaptation within the cortex (Miller
and Weber, 2011; Weber et al., 2012; Thomson et al., 2013) will be
relevant in the long-term implementation of DES in ECoG-BCIs
for sensory restoration.
A BCI application with DES (Figure 2) could use signals
from motor cortex to drive a sensorized prosthetic arm, which
could provide feedback about the task via DES of primary
somatosensory cortex (Figure 2A). Depending on the potential
parameter space of discernible stimulation percepts, a user
could learn to map physical contact locations on the prosthetic
arm to distinct stimulation percepts (Figure 2B) providing
feedback from external sensors directly to the brain The recent
demonstrations of usable sensory signals in humans via DES
brings us a step closer to such closed-loop human BCIs.
Quantiﬁcation of Cortical Connectivity
An additional application of DES is in quantifying cortical
connectivity. DES of a cortical site can produce a cortico-
cortical evoked potential (CCEP) at local and remote sites
depending on the cortical area stimulated and the intensity of
stimulation (Keller et al., 2014b). Studies have explored CCEPs
in the context of diﬀerent cortical networks, including language
(Matsumoto et al., 2004) and motor regions (Matsumoto et al.,
2006). The connections probed with CCEPs correspond well
with known functional networks observed through fMRI as
well as white matter pathways conﬁrmed by diﬀusion tensor
imaging (DTI) (Keller et al., 2014a). Such evoked potentials
could have utility in BCI applications where depending on
the presence or modulation of these CCEPs, an algorithmic
decision could be made.
Modiﬁcation of Cortical Excitability and
Induction of Plasticity
Another use for DES currently being explored is the induction
of cortical plasticity. This refers to enhancement or other
modiﬁcation of connectivity between diﬀerent cortical regions,
which could aid in the recovery of individuals suﬀering from
disrupted neuronal communication due to injuries such as
stroke. To put the clinical need in perspective, there are
millions of individuals worldwide who are disabled due to
stroke. It is estimated that in the US alone for the year
2016, healthcare and economic costs related to stroke disability
totaled $34 billion with stroke being a leading cause of serious
long-term disability (CDC, 2015). 50–70% of stroke survivors
reach functional independence, but 15–30% of survivors are
permanently disabled (Lloyd-Jones et al., 2010). Therapies
using targeted activity-dependent neuromodulation may help
restore motor recovery (Harvey et al., 2009) but the biological
eﬀects of cortical stimulations are not well understood, and
the parameters for potentially eﬀective stimulation protocols
need further development. Studies with smaller populations of
neurons, animal models, and non-invasive stimulation may lend
insight into the optimal protocols for plasticity induction.
A persistent theme in cortical connectivity is the idea of
Hebbian plasticity, a type of synaptic plasticity ﬁrst proposed
by Hebb (1949): presynaptic ﬁring of one neuron (site A) can
strengthen the connection between it and a postsynaptic neuron
(site B) that ﬁres soon after A. Bi and Poo demonstrated a
version of this plasticity rule, known as spike timing dependent
plasticity (STDP), in rat hippocampal slice cells: consistent ﬁring
of a presynaptic cell (site A) within a time window of 20–30 ms
before another postsynaptic cell (site B) led to a strengthened
connection (LTP) from A to B, while B ﬁring in a time window
of 20–30 ms before A led to a weakened connection (LTD) (Bi
and Poo, 1998). Both of these mechanisms were determined to be
dependent on NMDA receptors.
These principles have been applied to induce plasticity in non-
human primate (NHP) motor cortex (Jackson et al., 2006) and
rodent rehabilitation experiments, where triggering stimulation
in somatosensory cortex several milliseconds after premotor
cortex ﬁring in rats that suﬀered from damage to motor
Frontiers in Neuroscience | www.frontiersin.org
7
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
FIGURE 2 | Somatosensory BCI with closed-loop stimulation. (A) Neural signals recorded from cortical regions such as primary motor cortex could be used to drive
a sensorized prosthetic arm. Feedback about task performance or object manipulation could then be conveyed to the user by DES of primary somatosensory
cortex. (B) Different stimulation parameters, such as amplitude, frequency, and carrier frequency shape, could convey different percepts which a user could learn to
map to locations on the neuroprosthetic arm.
cortex resulted in increased functional performance (Guggenmos
et al., 2013). Other work has explored the use of paired-
pulse paradigms in NHPs to induce plasticity: where concurrent
surface to depth stimulation at one site was consistently followed
by stimulation at another site with a ﬁxed time lag (Seeman
et al., 2017). The optimal time lag for potentiation was found
to be between 10–30 ms, with longer delays not resulting in
potentiation. Only a fraction of the sites in this study were
potentiated, and eﬀects were often seen globally, illustrating the
complex factors inﬂuencing cortical plasticity. A recent study
in NHPs examined the timing of DES relative to the aggregate
activity of neurons: DES delivered during beta oscillations during
the depolarizing potential (negative peak as recorded through
LFPs) caused potentiation of cortical connectivity, while DES
delivered during the hyperpolarizing potential caused depression
of cortical connectivity as assessed through cortically evoked
potentials (Zanos et al., 2018).
Beyond work in animals, and importantly, for applications
such
as
stroke
rehabilitation,
recent
work
has
reported
improvements in physiological measures of motor function
with non-invasive stimulation such as movement triggered
TMS compared to random TMS stimulation (Bueteﬁsch et al.,
2011). Adding further support to the importance of brain
state dependent stimulation for rehabilitation is a recent study
that demonstrated TMS delivery during movement-related
beta-band (16–22 Hz) desynchronization caused a signiﬁcant
increase in corticospinal excitability, as evaluated through motor
evoked potentials, lasting beyond the period of stimulation
(Kraus et al., 2016).
Keller et al. (2018) demonstrated that repetitive 10 Hz
DES using subdural electrodes induced both potentiation and
suppression in diﬀerent cortical sites, depending on the baseline
network characteristics. This suggests that plasticity can indeed
be modulated through DES in humans, and that individual
patient models of connectivity may inform the optimal sites to
target to either enhance or decrease connection strength.
An example BCI application for neuromodulation (Figure 3)
could include an oscillatory feature at a surface electrode, such
as activity in the beta band or high gamma activity representing
coordinated neuronal ﬁring, driving stimulation at a damaged
cortical region to enhance cortical connectivity and help restore
motor function. This activity dependent stimulation could be
similar to the activity-dependent DBS paradigms being explored
(Herron et al., 2017). A more sophisticated approach, based on
the concept of neural co-processors (Rao, 2019), could utilize
artiﬁcial neural networks to map complex ECoG activity patterns
at multiple recording sites to stimulation patterns at multiple
stimulation sites to achieve goal-directed rehabilitation.
The combination of theoretical, animal, and human data
discussed above suggests that activity-dependent DES is a
promising approach to enhance and modify connectivity in
humans, oﬀering a new type of therapy for targeted restoration
of function after neural injury. ECoG-BCIs are well-suited to
acquiring and decoding appropriate control signals and when
coupled with DES, can be used to inﬂuence cortical activity and
induce activity-dependent plasticity.
LIMITATIONS AND CONSIDERATIONS
While ECoG based bi-directional BCIs oﬀer several advantages
over other types of BCIs, there are limitations and considerations
Frontiers in Neuroscience | www.frontiersin.org
8
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
FIGURE 3 | Neural plasticity induction through neuromodulation via DES in ECoG-BCIs. (A) The basic principles of neural plasticity involve the timing of activity
between neurons resulting in the strengthening of connections, where potentiation occurs if the neurons ﬁre with the appropriate timing in a causal manner, and
depression occurs if neurons do not ﬁre with the appropriate timing. (B) These principles could be used for neuromodulation through DES and ECoG-BCIs by
stimulating near a particular damaged cortical region (purple), based on activity at a spared cortical region (gray). This activity could be a marker of neuronal ﬁring, or
a local ﬁeld potential representing when neurons are more likely to be ﬁring synchronously. Appropriately timed stimulation could then result in increased connectivity,
measured through markers such as evoked potentials, and restored motor function relative to baseline. A damaged region not undergoing neuromodulation is
shown in red, where evoked potentials are not positively modulated and motor function is not restored.
that must be taken into account. For either subdural or
epidural electrodes, neurosurgery is required. The size of
the electrodes, relative to other invasive methods such as
ICMS, results in larger population of neurons being targeted.
Furthermore, there is no ability to target speciﬁc types of
cells. Additionally, larger neurons with larger diameter axons
are more likely to be activated by electrical stimulation
(Tehovnik et al., 2006).
The developing ﬁeld of optogenetics (Deisseroth, 2011;
Yizhar et al., 2011) describes the use of genetic modiﬁcation
and optical methods to either activate or inactivate speciﬁc
neurons in vivo. Optogenetics has been demonstrated to
change functional connectivity in sensorimotor cortex in NHPs
(Yazdan-Shahmorad et al., 2018). Although optogenetics may
oﬀer a more targeted approach to activating neurons, progress
to humans may be slow due to the technique’s reliance on genetic
modiﬁcation of neurons.
Another current consideration when developing technologies
and protocols to induce plasticity is our current lack of
understanding of the mechanisms of plasticity induction
(Feldman, 2012). Beyond the single neuron spiking level,
plasticity is a complex phenomenon as discussed above, and
in a human brain, the potential factors inﬂuencing plasticity
can be complex and numerous. Optogenetics, with its ability
to selectively target diﬀerent populations of neurons will help
provide critical insight into the mechanisms of plasticity.
Frontiers in Neuroscience | www.frontiersin.org
9
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
Although DES may oﬀer a promising approach to inducing
plasticity, it has yet to be demonstrated to be unequivocally
eﬀective in a stroke model. Limited subgroups of stroke patients
with residual motor function were shown to beneﬁt from open-
loop DES in the EVEREST trial, but other groups showed no
beneﬁt (Levy et al., 2016). As better animal models of stroke
are developed (Sommer, 2017), one can hope to gain a better
mechanistic understanding of how DES can be used for stroke
rehabilitation, leading to optimized therapies for maximizing
functional recovery following cortical injury.
The issue of particular patient subgroup beneﬁt as discussed
above speaks to the broader issue of patient variability. Due
to anatomic or surgical variations, results from one group
of subjects may not necessarily apply to another. Careful
consideration of these individual factors will be important for
future bidirectional ECoG-BCIs.
An additional consideration is the durability of electrodes with
repeated stimulation. As mentioned in section “The Electrical-
Neural Interface” above, charge transfer can occur through
irreversible Faradaic reactions, where electrolysis occurs, and
depending on the polarity of stimulation, either hydrogen gas
or oxygen gas are the by products (Merrill et al., 2005). In
this electrolytic window, accelerated corrosion and electrode
damage can occur. Even below the voltage required for
the electrolysis of water, detrimental byproducts such as the
formation of metal chloride and hydrogen peroxide can occur,
leading to electrode corrosion. Therefore, long-term use of
stimulating ECoG electrodes will require careful selection of
stimulation parameters and materials to minimize adverse
eﬀects. Relative to monophasic pulses, both charge balanced
and imbalanced biphasic waveforms result in less electrode
potential shift and accumulation of charge. Accumulation of
charge during monophasic stimulation can result in additional
undesirable Faradaic reactions, and the formation of reactive
oxygen species which can cause tissue damage (Merrill et al.,
2005). When comparing charge balanced and charge imbalanced
biphasic waveforms, charge imbalanced waveforms have the
advantage that at the end of each stimulation pulse, the
electrode potential is closer to that of the open-circuit potential,
resulting in less charge going to irreversible oxidation reactions
(Merrill et al., 2005).
Beyond
electrode
damage,
tissue
damage
induced
by
stimulation is a key consideration for long-term use of DES.
The study of electrical stimulation through platinum electrodes
in cats (McCreery et al., 1990) was used to deﬁne the Shannon
equation (Shannon, 1992), which has been used frequently for
assessing safe stimulation levels. Earlier research established a
30 µC/cm2 limit on the charge per phase of stimulation for
macro-scale electrodes (in particular, DBS electrodes) (Kuncel
and Grill, 2004), but tissue damage can occur above and below
this threshold (Cogan et al., 2016). There are factors inﬂuencing
whether or not tissue damage occurs that are not included in the
Shannon equation, for example, the scale of the electrode (macro
vs. micro), the current density, duty cycle, pulse frequency, and
the uniformity of current distribution (Cogan et al., 2016). These
complex factors will require further modeling and laboratory
testing to establish what the appropriate stimulation parameters
are to minimize tissue damage, particularly with the use of novel
materials and stimulation patterns.
With penetrating microelectrodes (such as with the Utah
array), there is a signiﬁcant change in the electrode-tissue
interface over time (Williams et al., 2007). In addition,
stimulation can change the characteristics of the electrode-tissue
interface. A recent study analyzing the impedance characteristics
of DBS electrodes following implantation and stimulation
has shown that DBS electrode impedance increases after
implantation and decreases with clinically relevant stimulation
(Lempka et al., 2009). Other work has shown that the stimulation
parameters used aﬀect the impedance measured for DBS
electrodes (Wei and Grill, 2009). ECoG electrode impedance
measurements from 191 persons implanted with the Neuropace
RNS system, over a median time period of 802 days, did not reveal
signiﬁcant diﬀerences between stimulating and non-stimulating
electrodes in peri-implant changes in impedance or impedance
stability (Ryapolova-Webb et al., 2014). In this study, while there
were statistically signiﬁcant short-term changes in impedance
following implantation, long-term impedances were stable. These
results suggest that ECoG-BCIs with concurrent DES may prove
viable as chronic implants.
ENABLING TECHNOLOGIES
Materials and Electronics
Advances in materials science and electronics are enabling
the creation of robust intracranial arrays with thousands of
electrode contacts, with closer spacing than is currently used
clinically. Current ECoG arrays based on silicone and platinum
have been extended to microECoG arrays (Chao et al., 2010).
Further reductions in electrode diameter and increases in
array density are enabled by micromanufacturing techniques,
and in particular, microelectricomechanical systems (MEMS)
technologies. Platinum electrodes and polyimide foil substrates
similarly have been patterned using micromachining, allowing
for electrode contact diameters of 1 mm with electrode spacings
between 2 and 3 mm (Rubehn et al., 2009). Through these MEMS
technologies, electrode arrays with tighter spacings and smaller
diameters can be constructed and placed across large regions
of cortex and within sulci (Fukushima et al., 2014). Fukushima
et al. (2014) created an array with 0.8 mm diameter electrodes
and 1.8 mm spacing.
MicroECoG arrays have recently been used to resolve ﬁner
features of cortical activity, particularly in the broadband gamma
range, for measurement of phonetic features in single electrodes
(Mesgarani et al., 2014). Arrays with electrode diameters of
0.87 mm and spacings of 1.68 mm have resolved cortical
activity patterns with response peaks less than the standard
clinical spacing of 1 cm apart, pointing to the advantages seen
with smaller electrode arrays (Wang et al., 2017). Novel, thin
ﬁlm MEMS arrays are being implanted in humans (Muller
et al., 2016), illustrating the translation of these materials
and manufacturing techniques to humans. The ability to place
more electrodes within a given area could allow for ﬁner
patterning of stimulation.
Frontiers in Neuroscience | www.frontiersin.org
10
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
Advances in materials science are enabling electrodes and
arrays made of other materials, such as glassy carbon (Kassegne
et al., 2015; Goshi et al., 2018). Glassy carbon electrodes have
higher charge injection capacities (CIC, which is the amount of
charge that can be injected before irreversible chemical reactions
take place) than traditional platinum electrodes, and require less
stimulation current to activate neurons (Kassegne et al., 2015).
Combinations of ECoG and penetrating electrode arrays are
also being constructed for recording and stimulating both surface
and deeper structures simultaneously (Orsborn et al., 2015; Goshi
et al., 2018; Kleinbart et al., 2018). Currently being used in animal
models, such arrays will open the door to a better understanding
of network-wide and across cortex eﬀects of stimulation.
Computational Modeling
Computational modeling may help inform the design of DES
targeting strategies by delineating which areas of cortex are
activated during diﬀerent polarities of stimulation, and which
combinations of electrodes may prove eﬀective. For example,
a computational model of subdural cortical stimulation based
on anisotropy estimates from DTI revealed that neurons deeper
in the cortex are activated more during cathodal subdural
stimulation, while those in the wider crown are activated during
anodal stimulation (Seo et al., 2015). The inﬂuence of anisotropy
on neuronal excitation from DES illustrates the importance of
detailed, accurate anatomy for understanding and predicting
the eﬀects of DES.
A multicompartment computational model for subdural
DES illustrated the eﬀect of the neuronal structure, size, and
orientation on activation thresholds (Kudela and Anderson,
2015). In the model, the speciﬁc parameters of stimulation
and
structure
of
the
axons
inﬂuenced
the
presynaptic
terminal activation.
The combination of FEM and patient speciﬁc CT and MRI
imaging has enabled the optimization of current delivery to
various cortical regions depending on desired parameters, such
as minimizing current density in particular regions (Guler
et al., 2018). Combining individual patient MRIs with accurate
computational models of how neurons are activated will allow
precise DES targeting, with potentially fewer oﬀ-target eﬀects.
The DBS ﬁeld is replete with examples of new modeling
techniques to optimize stimulation of deep cortical targets. These
advances could carry over more generally to DES in ECoG-
BCIs. Patient speciﬁc models of the volume of tissue activated
(VTA) enable better understanding of the eﬀects of stimulation
at various locations in a given individual (Butson et al., 2007).
With the advent of electrodes with many contacts and diﬀerent
geometries, an open question is how to best target the region
of interest. Recent algorithmic advances combine electrodes with
diﬀerent contact geometries, including cylindrical and directional
leads, and patient speciﬁc models, including tissue anisotropy,
to best target the sub-thalamic nucleus (STN) (Anderson et al.,
2018). A multi-objective particle swarm optimization technique
to select a combination of stimulation electrodes was found
to be more eﬀective than a single monopolar electrode in
targeting the desired eﬀerents from the STN (Peña et al.,
2018). As ECoG electrodes become smaller and more numerous,
algorithmic techniques such as the ones described above and
more advanced ones based on artiﬁcial neural networks (Rao,
2019) would enable precisely targeted DES with the right
combination of electrodes.
Concurrent Recording and Stimulation
In any closed-loop application involving concurrent stimulation
and recording, the electrical artifact due to stimulation is
many orders of magnitude greater than the neural signals
being recorded. Disentangling the volume conduction of the
stimulation pulse from the neural responses is a topic of active
research. Diﬀerent approaches have been used for handling
artifacts, ranging from hardware approaches to mitigate artifacts
before signal acquisition to post-processing techniques to
minimize artifacts after the signals have been acquired.
An example system manufactured with CMOS technology
enables both common mode and diﬀerential real time artifact
cancelation (Smith et al., 2017). In combination with this, new
CMOS stimulator front-ends are being developed which could
allow for more scalable, integrated BCI devices with wireless,
signal processing, and stimulator blocks (Pepin et al., 2016).
Advances in this area will permit a better understanding of how
the brain responds to electrical stimulation, as well as permit
more complex closed loop applications (Zhou et al., 2018a) where
neural activity in close temporal and spatial relation to the site of
stimulation can be integrated into the control system.
Recent technology development in industry for simultaneous
stimulation and recording in DBS applications both illustrates
widespread
interest
in
the
development
of
concurrent
stimulation and recording devices, and suggests potential
combined hardware and software solutions for ECoG-BCIs
(Stanslaski et al., 2012; Herron et al., 2018). These techniques
include careful consideration of the stimulation and recording
conﬁguration to mitigate the measured artifact, front-end
ﬁltering, heterodyning to minimize stimulation harmonics
in neural frequency bands of interest, and selection of
stimulation parameters to aid in the separation of neural
signals from stimulation artifacts (Stanslaski et al., 2012).
Medtronic’s Summit RC + S system extends the previously
mentioned
approaches
to
simultaneous
stimulation
and
recording, and further includes oversampling to reduce noise
in the signal bands of interest, decimators designed to ﬁlter
out higher-order harmonics from stimulation, as well as
options to only suggest sense-friendly stimulation parameters
to the researcher or clinician (Herron et al., 2018). Such
techniques could be applied more broadly to include ECoG-BCI
systems with DES.
Wireless Technologies
Recent advances in hardware have allowed both real time artifact
cancelation and wireless communication with 128 channels of
local ﬁeld potential recording in NHPs (Zhou et al., 2018b). Other
implantable devices with microelectrode arrays in NHP model
have included wireless charging and data transfer capabilities
(Borton et al., 2013), which are critical for an out-of-hospital
device. The development of wireless technologies, as well as
real time simultaneous stimulation and recording techniques,
Frontiers in Neuroscience | www.frontiersin.org
11
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
opens the door to explorations of the neural basis of naturalistic
behavior and long-term eﬀects of closed-loop stimulation. Recent
work in non-human primates has demonstrated both wireless
recording and stimulation of motor regions over a 6 months
time period, with no observed neurological or behavioral
consequences (Romanelli et al., 2018). This points to the future
translatability of wireless long-term ECoG implants with both
recording and stimulation.
CONCLUSION
Direct electrical stimulation of the human brain is currently
used clinically for functional mapping, as well as therapeutic
treatment
of
disorders
such
as
epilepsy
and
movement
disorders.
In
this
article,
we
have
explored
DES
can
also be used as a new modality for providing input to
cortex
in
electrocorticographic
(ECoG)
brain
computer
interfaces (BCIs). DES oﬀers distinct advantages over other
stimulation modalities such as TES and TMS by virtue
of delivering electrical stimulation directly to the brain.
We discussed some of the barriers for DES translation
to ECoG-BCIs, and highlighted the progress being made
in the use of DES for restoration of somatosensation and
induction of cortical plasticity for targeted rehabilitation
in
stroke.
We
also
have
reviewed
how
advances
in
technology, including new materials for electrode design,
manufacturing techniques for smaller electrode arrays, and
computational
modeling
for
tailoring
stimulation
to
the
patient’s needs oﬀer opportunities for radically expanding the
applications of DES in bi-directional ECoG-BCIs for restoring
neurological function.
AUTHOR CONTRIBUTIONS
DC, JO, and RR planned the study and conducted some
of
the
research
on
the
topic
of
sensation
induced
by
electrocorticographic stimulation described in this manuscript.
DC wrote the ﬁrst draft of the manuscript. DC, JO, and RR edited
the draft and ﬁnalized the manuscript.
FUNDING
This work was supported by the National Science Foundation
(NSF) Center for Neurotechnology (CNT) (Award Number
EEC-1028725) and NSF Award Number IIS-1514790. DC was
supported by the Big Data for Genomics & Neuroscience
Training Grant under Grant Number 1T32CA206089-01A1 and
by the Washington Research Foundation Funds for Innovation
in Neuroengineering. RR is supported by the CJ and Elizabeth
Hwang Endowed Professorship for Computer Science and
Engineering and Electrical and Computer Engineering. The
content is solely the responsibility of the authors and does not
necessarily represent the oﬃcial views of the National Science
Foundation or the National Institutes of Health.
ACKNOWLEDGMENTS
The authors would like to thank the patients who dedicated their
time and energy to the experiments which allow the ﬁeld of
electrocortigraphic BCIs to move forward, and without whom,
this research would not be possible. The authors would also like
to thank Jeﬀrey Herron for valuable conversation and feedback.
REFERENCES
Alonso, A., De Curtis, M., and Llinast, R. (1990). Postsynaptic Hebbian and non-
Hebbian long-term potentiation of synaptic eﬃcacy in the entorhinal cortex in
slices and in the isolated adult guinea pig brain (synaptic plasticity/intracellular
recording/N-methyl-n-aspartate/ionic channels). Neurobiology 87, 9280–9284.
doi: 10.1073/pnas.87.23.9280
Anderson, D. N., Osting, B., Vorwerk, J., Dorval, A. D., and Butson, C. R.
(2018). Optimized programming algorithm for cylindrical and directional deep
brain stimulation electrodes. J. Neural Eng. 15:026005. doi: 10.1088/1741-2552/
aaa14b
Anderson, K. D. (2004). Targeting recovery: priorities of the spinal cord-
injured population. J. Neurotrauma 21, 1371–1383. doi: 10.1089/neu.2004.21.
1371
Ashkan, K., Rogers, P., Bergman, H., and Ughratdar, I. (2017). Insights into
the mechanisms of deep brain stimulation. Nat. Rev. Neurol. 13, 548–554.
doi: 10.1038/nrneurol.2017.105
Bean, B. P. (2007). The action potential in mammalian central neurons. Nat. Rev.
Neurosci. 8, 451–465. doi: 10.1038/nrn2148
Bensmaia, S. J., and Miller, L. E. (2014). Restoring sensorimotor function through
intracortical interfaces: progress and looming challenges. Nat. Rev. Neurosci. 15,
313–325. doi: 10.1038/nrn3724
Berger, M. S., Kincaid, J., Ojemann, G. A., and Lettich, E. (1989). Brain mapping
techniques to maximize resection, safety, and seizure control in children with
brain tumors. Neurosurgery 25, 786–792. doi: 10.1227/00006123-198911000-
00015
Berger, M. S., and Ojemann, G. A. (1992). Intraoperative brain mapping techniques
in neuro-oncology. Stereotact. Funct. Neurosurg. 58, 153–161. doi: 10.1159/
000098989
Bi, G. Q., and Poo, M. M. (1998). Synaptic modiﬁcations in cultured hippocampal
neurons: dependence on spike timing, synaptic strength, and postsynaptic cell
type. J. Neurosci. 18, 10464–10472. doi: 10.1038/25665
Biddiss, E., Beaton, D., and Chau, T. (2007). Consumer design priorities for upper
limb prosthetics. Disabil. Rehabil. Assist. Technol. 2, 346–357. doi: 10.1080/
17483100701714733
Bliss, T. V. P., and Lomo, T. (1973). Long-lasting poteniation of synpatic
transmission in the dentate area of the anaesthetized rabbit following
stimulation fo the perforant path. J. Physiol. 232, 331–356. doi: 10.1113/jphysiol.
1973.sp010273
Boon, P., Vonck, K., Vandekerckhove, T., D’have, M., Nieuwenhuis, L., Michielsen,
G., et al. (1999). Vagus nerve stimulation for medically refractory epilepsy;
eﬃcacy and cost-beneﬁt analysis. Acta Neurochir. 141, 447–453. doi: 10.1007/
s007010050324
Borchers, S., Himmelbach, M., Logothetis, N., and Karnath, H.-O. (2012). Direct
electrical stimulation of human cortex — the gold standard for mapping brain
functions? Nat. Rev. Neurosci. 13, 63–70. doi: 10.1038/nrn3140
Borton, D. A., Yin, M., Aceros, J., and Nurmikko, A. (2013). An implantable
wireless neural interface for recording cortical circuit dynamics in moving
primates. J. Neural Eng. 10:026010. doi: 10.1088/1741-2560/10/2/026010
Bouchard, K. E., Mesgarani, N., Johnson, K., and Chang, E. F. (2013). Functional
organization of human sensorimotor cortex for speech articulation. Nature 495,
327–332. doi: 10.1038/nature11911
Frontiers in Neuroscience | www.frontiersin.org
12
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
Brill, J., and Huguenard, J. R. (2009). Robust short-latency perisomatic inhibition
onto neocortical pyramidal cells detected by laser-scanning photostimulation.
J. Neurosci. 29, 7413–7423. doi: 10.1523/jneurosci.6098-08.2009
Bronstein, J. M., Tagliati, M., Alterman, R. L., Lozano, A. M., Volkmann, J., Stefani,
A., et al. (2011). Deep brain stimulation for Parkinson disease. Arch. Neurol. 68,
165–171. doi: 10.1001/archneurol.2010.260
Bueteﬁsch, C., Heger, R., Schicks, W., Seitz, R., and Netz, J. (2011). Hebbian-type
stimulation during robot-assisted training in patients with stroke. Neurorehabil.
Neural Repair 25, 645–655. doi: 10.1177/1545968311402507
Butovas, S., and Schwarz, C. (2003). Spatiotemporal eﬀects of microstimulation
in rat neocortex: a parametric study using multielectrode recordings.
J. Neurophysiol. 90, 3024–3039. doi: 10.1152/jn.00245.2003
Butson, C. R., Cooper, S. E., Henderson, J. M., and McIntyre, C. C. (2007). Patient-
speciﬁc analysis of the volume of tissue activated during deep brain stimulation.
Neuroimage 34, 661–670. doi: 10.1016/j.neuroimage.2006.09.034
Caldwell, D. J., Cronin, J. A., Wu, J., Weaver, K. E., Ko, A. L., Rao, R. P. N., et al.
(2019). Direct stimulation of somatosensory cortex results in slower reaction
times compared to peripheral touch in humans. Sci. Rep. 9:3292. doi: 10.1038/
s41598-019-38619-2
CDC, (2015). Stroke Facts. Available at: https://www.cdc.gov/stroke/facts.htm%
5Cnhttp://www.cdc.gov/stroke/index.htm (accessed February 11, 2016).
Chang,
E.
F.
(2015).
Towards
large-scale,
human-based,
mesoscopic
neurotechnologies. Neuron 86, 68–78. doi: 10.1016/j.neuron.2015.03.037
Chao, Z. C., Nagasaka, Y., and Fujii, N. (2010). Long-term asynchronous decoding
of arm motion using electrocorticographic signals in monkey. Front. Neuroeng.
3:3. doi: 10.3389/fneng.2010.00003
Christopher and Dana Reeve Foundation (2013). Stats About Paralysis. Available at:
https://www.christopherreeve.org/living-with-paralysis/stats-about-paralysis
(accessed March 1, 2019).
Coﬀey, R. J. (2009). Deep brain stimulation devices: a brief technical history and
review. Artif. Organs 33, 208–220. doi: 10.1111/j.1525-1594.2008.00620.x
Cogan, S. F., Ludwig, K. A., Welle, C. G., and Takmakov, P. (2016). Tissue damage
thresholds during therapeutic electrical stimulation. J. Neural Eng. 13:021001.
doi: 10.1088/1741-2560/13/2/021001
Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber,
D. J., et al. (2013). High-performance neuroprosthetic control by an individual
with tetraplegia. Lancet 381, 557–564. doi: 10.1016/S0140-6736(12)61816-9
Collins, K. L., Guterstam, A., Cronin, J., Olson, J. D., Ehrsson, H. H., and
Ojemann, J. G. (2017). Ownership of an artiﬁcial limb induced by electrical
brain stimulation. Proc. Natl. Acad. Sci. U.S.A. 114, 166–171. doi: 10.1073/pnas.
1616305114
Cronin, J. A., Wu, J., Collins, K. L., Sarma, D., Rao, R. P. N., Ojemann, J. G.,
et al. (2016). Task-speciﬁc somatosensory feedback via cortical stimulation in
humans. IEEE Trans. Haptics 9, 515–522. doi: 10.1109/TOH.2016.2591952
Dadarlat, M. C., O’Doherty, J. E., and Sabes, P. N. (2015). A learning-based
approach to artiﬁcial sensory feedback leads to optimal integration. Nat.
Neurosci. 18, 138–144. doi: 10.1038/nn.3883
Deisseroth, K. (2011). Optogenetics. Nat. Methods 8, 26–29. doi: 10.1038/nmeth.
f.324
Delhaye, B. P., Saal, H. P., and Bensmaia, S. J. (2016). Key considerations in
designing a somatosensory neuroprosthesis. J. Physiol. Paris 110, 402–408.
doi: 10.1016/j.jphysparis.2016.11.001
Della Flora, E., Perera, C. L., Cameron, A. L., and Maddern, G. J. (2010). Deep
brain stimulation for essential tremor: a systematic review. Mov. Disord. 25,
1550–1559. doi: 10.1002/mds.23195
Douglas, R. M. (1977). Long lasting synaptic potentiation in the rat dentate
gyrus following brief high frequency stimulation. Brain Res. 126, 361–365.
doi: 10.1016/0006-8993(77)90733-8
Englot, D. J., and Chang, E. F. (2014). Rates and predictors of seizure freedom
in resective epilepsy surgery: an update. Neurosurg. Rev. 37, 389–405.
doi: 10.1007/s10143-014-0527-9
Eskandar, E. N., Flaherty, A., Cosgrove, G. R., Shinobu, L. A., and Barker, F. G.
(2009). Surgery for Parkinson disease in the United States, 1996 to 2000: practice
patterns, short-term outcomes, and hospital charges in a nationwide sample.
J. Neurosurg. 99, 863–871. doi: 10.3171/jns.2003.99.5.0863
Feldman, D. E. (2012). The Spike-timing dependence of plasticity. Neuron 75,
556–571. doi: 10.1016/j.neuron.2012.08.001
Flint, R. D., Rosenow, J. M., Tate, M. C., and Slutzky, M. W. (2017). Continuous
decoding of human grasp kinematics using epidural and subdural signals.
J. Neural Eng. 14:016005. doi: 10.1088/1741-2560/14/1/016005
Fox, P. T., Narayana, S., Tandon, N., Sandoval, H., Fox, S. P., Kochunov, P., et al.
(2004). Column-based model of electric ﬁeld excitation of cerebral cortex. Hum.
Brain Mapp. 22, 1–14. doi: 10.1002/hbm.20006
Fukushima, M., Saunders, R. C., Mullarkey, M., Doyle, A. M., Mishkin, M., and
Fujii, N. (2014). An electrocorticographic electrode array for simultaneous
recording from medial, lateral, and intrasulcal surface of the cortex in macaque
monkeys. J. Neurosci. Methods 233, 155–165. doi: 10.1016/j.jneumeth.2014.
06.022
Giussani, C., Roux, F. E., Ojemann, J., Sganzerla, E. P., Pirillo, D., and Papagno,
C. (2010). Is preoperative functional magnetic resonance imaging reliable for
language areas mapping in brain tumor surgery? Review of language functional
magnetic resonance imaging and direct cortical stimulation correlation studies.
Neurosurgery 66, 113–120. doi: 10.1227/01.NEU.0000360392.15450.C9
Goshi, N., Castagnola, E., Vomero, M., Gueli, C., Cea, C., Zucchini, E., et al. (2018).
Glassy carbon MEMS for novel origami-styled 3D integrated intracortical and
epicortical neural probes. J. Micromech. Microeng. 28:065009. doi: 10.1088/
1361-6439/aab061
Guggenmos, D. J., Azin, M., Barbay, S., Mahnken, J. D., Dunham, C., Mohseni,
P., et al. (2013). Restoration of function after brain damage using a neural
prosthesis. Proc. Natl. Acad. Sci. U.S.A. 110, 21177–21182. doi: 10.1073/pnas.
1316885110
Guler, S., Dannhauer, M., Roig-Solvas, B., Gkogkidis, A., Macleod, R., Ball, T.,
et al. (2018). Computationally optimized ECoG stimulation with local safety
constraints. Neuroimage 173, 35–48. doi: 10.1016/j.neuroimage.2018.01.088
Halpern, C. H., Samadani, U., Litt, B., Jaggi, J. L., and Baltuch, G. H. (2008). Deep
brain stimulation for epilepsy. Neurotherapeutics 5, 59–67.
Harvey, R. L., and Winstein, C. J. (2009). Design for the everest randomized trial
of cortical stimulation and rehabilitation for arm function following stroke.
Neurorehabil. Neural Repair 23, 32–44. doi: 10.1177/1545968308317532
Harvey, R. L., Winstein, C. J., and Everest Trial, G. (2009). Design for the
everest randomized trial of cortical. Neurorehabil. Neural Repair 23, 32–44.
doi: 10.1177/1545968308317532
Hebb, D. O. (1949). The Organization of Behavior; A Neuropsychological Theory.
Oxford: Wiley, doi: 10.2307/1418888
Heller, L., and van Hulsteyn, D. B. (1992). Brain stimulation using electromagnetic
sources: theoretical aspects. Biophys. J. 63, 129–138. doi: 10.1016/S0006-
3495(92)81587-4
Hermes, D., Nguyen, M., and Winawer, J. (2017). Neuronal synchrony and the
relation between the blood-oxygen-level dependent response and the local ﬁeld
potential. PLoS Biol. 15:e2001461. doi: 10.1371/journal.pbio.2001461
Herron, J., Stanslaski, S., Chouinard, T., Corey, R., Denison, T., and Orser, H.
(2018). “Bi-directional brain interfacing instrumentation,” in Proceedings of
the I2MTC 2018 - 2018 IEEE International Instrumentation and Measurement
Technology Conference: Discovering New Horizons in Instrumentation and
Measurement, (houston, TX: IEEE), 1–6. doi: 10.1109/TNSRE.2012.2183617
Herron, J., Thompson, M., Brown, T., Chizeck, H., Ojemann, J., and Ko, A. (2017).
Cortical brain computer interface for closed-loop deep brain stimulation. IEEE
Trans. Neural Syst. Rehabil. Eng. 25, 1–1. doi: 10.1109/TNSRE.2017.2705661
Hiremath, S. V., Tyler-Kabara, E. C., Wheeler, J. J., Moran, D. W., Gaunt, R. A.,
Collinger, J. L., et al. (2017). Human perception of electrical stimulation on the
surface of somatosensory cortex. PLoS One 12:e0176020. doi: 10.1371/journal.
pone.0176020
Histed, M. H., Bonin, V., and Reid, R. C. (2009). Direct activation of sparse,
distributed populations of cortical neurons by electrical microstimulation.
Neuron 63, 508–522. doi: 10.1016/j.neuron.2009.07.016
Hotson, G., McMullen, D. P., Fifer, M. S., Johannes, M. S., Katyal, K. D., Para,
M. P., et al. (2016). Individual ﬁnger control of a modular prosthetic limb using
high-density electrocorticography in a human subject. J. Neural Eng. 13:026017.
doi: 10.1088/1741-2560/13/2/026017
Jackson, A., Mavoori, J., and Fetz, E. E. (2006). Long-term motor cortex plasticity
induced by an electronic neural implant. Nature 444, 56–60. doi: 10.1038/
nature05226
Johnson, L. A., Wander, J. D., Sarma, D., Su, D. K., Fetz, E. E., and Ojemann, J. G.
(2013). Direct electrical stimulation of the somatosensory cortex in humans
Frontiers in Neuroscience | www.frontiersin.org
13
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
using electrocorticography electrodes: a qualitative and quantitative report.
J. Neural Eng. 10:036021. doi: 10.1088/1741-2560/10/3/036021
Kassegne, S., Vomero, M., Gavuglio, R., Hirabayashi, M., Özyilmaz, E., Nguyen, S.,
et al. (2015). Electrical impedance, electrochemistry, mechanical stiﬀness, and
hardness tunability in glassy carbon MEMS µECoG electrodes. Microelectron.
Eng. 133, 36–44. doi: 10.1016/j.mee.2014.11.013
Keller, C. J., Honey, C. J., Entz, L., Bickel, S., Groppe, D. M., Toth, E., et al. (2014a).
Corticocortical evoked potentials reveal projectors and integrators in human
brain networks. J. Neurosci. 34, 9152–9163. doi: 10.1523/JNEUROSCI.4289-13.
2014
Keller, C. J., Honey, C. J., Mégevand, P., Entz, L., Ulbert, I., and Mehta,
A. D. (2014b). Mapping human brain networks with cortico-cortical evoked
potentials. Philos. Trans. R. Soc. Lond. Ser. B Biol. Sci. 369:20130528.
doi: 10.1098/rstb.2013.0528
Keller, C. J., Huang, Y., Herrero, J. L., Fini, M., Du, V., Lado, F. A., et al.
(2018). Induction and quantiﬁcation of excitability changes in human cortical
networks. J. Neurosci. 38, 5384–5398. doi: 10.1523/JNEUROSCI.1088-17.2018
Klaes, C., Shi, Y., Kellis, S., Minxha, J., Revechkis, B., and Andersen, R. A. (2014).
A cognitive neuroprosthetic that uses cortical stimulation for somatosensory
feedback. J. Neural Eng. 11:056024. doi: 10.1088/1741-2560/11/5/056024
Klein, E., and Ojemann, J. (2016). Informed consent in implantable BCI research:
identiﬁcation of research risks and recommendations for development of best
practices. J. Neural Eng. 13:043001. doi: 10.1088/1741-2560/13/4/043001
Kleinbart, J. E., Orsborn, A. L., Choi, J. S., Wang, C., Qiao, S., Viventi, J.,
et al. (2018). “A Modular Implant System for Multimodal Recording and
Manipulation of the Primate Brain,” in Proceedings of the 2018 40th Annual
International Conference of the IEEE Engineering in Medicine and Biology
Society (EMBC), (Honolulu: IEEE), 3362–3365. doi: 10.1109/EMBC.2018.
8512993
Klink, P. C., Dagnino, B., Gariel-Mathis, M. A., and Roelfsema, P. R. (2017).
Distinct feedforward and feedback eﬀects of microstimulation in visual cortex
reveal neural mechanisms of texture segregation. Neuron 95, 209.e–220.e.
doi: 10.1016/j.neuron.2017.05.033
Kraus, D., Naros, G., Bauer, R., Khademi, F., Leão, M. T., Ziemann, U., et al. (2016).
Brain state-dependent transcranial magnetic closed-loop stimulation controlled
by sensorimotor desynchronization induces robust increase of corticospinal
excitability. Brain Stimul. 9, 415–424. doi: 10.1016/j.brs.2016.02.007
Kudela, P., and Anderson, W. S. (2015). computational modeling of subdural
cortical stimulation: a quantitative spatiotemporal analysis of action potential
initiation in a high-density multicompartment model. Neuromodulation 18,
552–565. doi: 10.1111/ner.12327
Kuncel, A. M., and Grill, W. M. (2004). Selection of stimulus parameters for deep
brain stimulation. Clin. Neurophysiol. 115, 2431–2441. doi: 10.1016/j.clinph.
2004.05.031
Lee, B., Kramer, D., Armenta Salas, M., Kellis, S., Brown, D., Dobreva, T., et al.
(2018). Engineering artiﬁcial somatosensation through cortical stimulation in
humans. Front. Syst. Neurosci. 12:24. doi: 10.3389/fnsys.2018.00024
Lee, B., Zubair, M. N., Marquez, Y. D., Lee, D. M., Kalayjian, L. A., Heck, C. N.,
et al. (2015). A Single-center experience with the neuropace RNS system: a
review of techniques and potential problems. World Neurosurg. 84, 719–726.
doi: 10.1016/j.wneu.2015.04.050
Lega, B. C., Halpern, C. H., Jaggi, J. L., and Baltuch, G. H. (2010). Neurobiology
of Disease Deep brain stimulation in the treatment of refractory epilepsy?:
update on current data and future directions. Neurobiol. Dis. 38, 354–360.
doi: 10.1016/j.nbd.2009.07.007
Lempka, S. F., Miocinovic, S., Johnson, M. D., Vitek, J. L., and McIntyre, C. C.
(2009). In vivo impedance spectroscopy of deep brain stimulation electrodes.
J. Neural Eng. 6:046001. doi: 10.1088/1741-2560/6/4/046001
Leuthardt, E. C., Miller, K. J., Schalk, G., Rao, R. P. N., and Ojemann, J. G. (2006a).
Electrocorticography-based brain computer interface — the seattle experience.
IEEE Trans. Neural Syst. Rehabil. Eng. 14, 194–198. doi: 10.1109/TNSRE.2006.
875536
Leuthardt, E. C., Schalk, G., Moran, D., and Ojemann, J. G. (2006b). The emerging
world of motor neuroprosthetics: a neurosurgical perspective. Neurosurgery 59,
1–13. doi: 10.1227/01.NEU.0000221506.06947.AC
Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., and Moran, D. W.
(2004). A brain-computer interface using electrocorticographic signals in
humans. J. Neural Eng. 1, 63–71. doi: 10.1088/1741-2560/1/2/001
Levy, R., Ruland, S., Weinand, M., Lowry, D., Dafer, R., and Bakay, R. (2008).
Cortical stimulation for the rehabilitation of patients with hemiparetic stroke:
a multicenter feasibility study of safety and eﬃcacy. J. Neurosurg. 108, 707–714.
doi: 10.3171/JNS/2008/108/4/0707
Levy, R. M., Harvey, R. L., Kissela, B. M., Winstein, C. J., Lutsep, H. L., Parrish,
T. B., et al. (2016). Epidural electrical stimulation for stroke rehabilitation:
results of the prospective, multicenter, randomized, single-blinded everest
trial. Neurorehabil. Neural Repair 30, 107–119. doi: 10.1177/15459683155
75613
Libet, B., Alberts, W. W., Wright, E. W., Delattre, L. D., Levin, G., and Feinstein,
B. (1964). Production of threshold levels of conscious sensation by electrical
stimulation of human somatosensory cortex. J. Neurophysiol. 27, 546–578.
doi: 10.1152/jn.1964.27.4.546
Little, S., Pogosyan, A., Neal, S., Zavala, B., Zrinzo, L., Hariz, M., et al. (2013).
Adaptive deep brain stimulation in advanced Parkinson disease. Ann. Neurol.
74, 449–457. doi: 10.1002/ana.23951
Lloyd-Jones, D., Adams, R. J., Brown, T. M., Carnethon, M., Dai, S., De Simone,
G., et al. (2010). Heart disease and stroke statistics–2010 update: a report
from the American heart association. Circulation 121, e46–e215. doi: 10.1161/
CIRCULATIONAHA.109.192667
Logothetis, N. K., Augath, M., Murayama, Y., Rauch, A., Sultan, F., Goense, J., et al.
(2010). The eﬀects of electrical microstimulation on cortical signal propagation.
Nat. Neurosci. 13, 1283–1291. doi: 10.1038/nn.2631
Matsumoto, R., Nair, D. R., LaPresto, E., Bingaman, W., Shibasaki, H., and Luders,
H. O. (2006). Functional connectivity in human cortical motor system: a
cortico-cortical evoked potential study. Brain 130, 181–197. doi: 10.1093/brain/
awl257
Matsumoto, R., Nair, D. R., LaPresto, E., Najm, I., Bingaman, W., Shibasaki,
H., et al. (2004). Functional connectivity in the human language system: a
cortico-cortical evoked potential study. Brain? J. Neurol. 127(Pt 10), 2316–2330.
doi: 10.1093/brain/awh246
McCreery, D. B., Agnew, W. F., Yuen, T. G. H., and Bullara, L. (1990). Charge
density and charge per phase as cofactors in neural injury induced by
electrical stimulation. IEEE Trans. Biomed. Eng. 37, 996–1001. doi: 10.1109/10.
102812
McIntyre, C. C., and Grill, W. M. (2000). Selective microstimulation of central
nervous system neurons. Ann. Biomed. Eng. 28, 219–233. doi: 10.1114/1.262
Merrill, D. R., Bikson, M., and Jeﬀerys, J. G. R. (2005). Electrical stimulation of
excitable tissue: design of eﬃcacious and safe protocols. J. Neurosci. Methods
141, 171–198. doi: 10.1016/j.jneumeth.2004.10.020
Mesgarani, N., Cheung, C., Johnson, K., and Chang, E. F. (2014). Phonetic
feature encoding in human superior temporal gyrus. Science 43, 1006–1010.
doi: 10.1126/science.1245994
Millard, D. C., Whitmire, C. J., Gollnick, C. A., Rozell, C. J., and Stanley,
G. B. (2015). Electrical and optical activation of mesoscale neural circuits
with implications for coding. J. Neurosci. 35, 15702–15715. doi: 10.1523/
JNEUROSCI.5045-14.2015
Miller, K. J., Shenoy, P., den Nijs, M., Sorensen, L. B., Rao, R. P. N., and Ojemann,
J. G. (2008). Beyond the Gamma band: the role of high-frequency features in
movement classiﬁcation. IEEE Trans. Biomed. Eng. 55, 1634–1637. doi: 10.1109/
TBME.2008.918569
Miller, L. E., and Weber, D. J. (2011). Guest editorial brain training: cortical
plasticity and aﬀerent feedback in brain-machine interface systems. IEEE Trans.
Neural Syst. Rehabil. Eng. 19, 465–467. doi: 10.1109/tnsre.2011.2168989
Montgomery, E. B., and Gale, J. T. (2008). Mechanisms of action of deep
brain stimulation (DBS). Neurosci. Biobehav. Rev. 32, 388–407. doi: 10.1016/
J.NEUBIOREV.2007.06.003
Morrell, M. J. (2011). Responsive cortical stimulation for the treatment of medically
intractable partial epilepsy. Neurology 77, 1295–1304. doi: 10.1212/WNL.
0b013e3182302056
Mulkey, R. M., and Malenka, R. C. (1992). Mechanisms underlying induction of
homosynaptic long-term depression in area CA1 of the hippocampus. Neuron
9, 967–975. doi: 10.1016/0896-6273(92)90248-C
Muller, L., Felix, S., Shah, K. G., Lee, K., Pannu, S., and Chang, E. F. (2016). “Thin-
ﬁlm, high-density micro-electrocorticographic decoding of a human cortical
gyrus,” in Proceedings of the 2016 38th Annual International Conference of the
IEEE Engineering in Medicine and Biology Society (EMBC), (Orlando, FL: IEEE),
1528–1531. doi: 10.1109/EMBC.2016.7591001
Frontiers in Neuroscience | www.frontiersin.org
14
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
Nowak, L. G., and Bullier, J. (1998). Axons, but not cell bodies, are activated
by electrical stimulation in cortical gray matter. I. Evidence from chronaxie
measurements. Exp. Brain Res. 118, 477–488. doi: 10.1007/s002210050304
Ojemann, G., Ojemann, J., Lettich, E., and Berger, M. (1989). Cortical language
localization in left, dominant hemisphere. An electrical stimulation mapping
investigation in 117 patients. J. Neurosurg. 71, 316–326. doi: 10.3171/jns.1989.
71.3.0316
Orsborn, A. L., Wang, C., Chiang, K., Maharbiz, M. M., Viventi, J., and
Pesaran, B. (2015). “Semi-chronic chamber system for simultaneous subdural
electrocorticography, local ﬁeld potentials, and spike recordings,” in Proceedings
of the International IEEE/EMBS Conference on Neural Engineering, NER, 2015,
(Montpellier: IEEE), 398–401. doi: 10.1109/NER.2015.7146643
Peña, E., Zhang, S., Patriat, R., Aman, J. E., Vitek, J. L., Harel, N., et al. (2018). Multi-
objective particle swarm optimization for postoperative deep brain stimulation
targeting of subthalamic nucleus pathways. J. Neural Eng. 15:066020.
doi: 10.1088/1741-2552/aae12f
Pepin, E., Uehlin, J., Micheletti, D., Perlmutter, S. I., and Rudell, J. C. (2016).
“A high-voltage compliant, electrode-invariant neural stimulator front-end
in 65nm bulk-CMOS,” in Proceedings of the ESSCIRC Conference 2016:
42nd European Solid-State Circuits Conference, (Ecublens: IEEE), 229–232.
doi: 10.1109/ESSCIRC.2016.7598284
Pereira, E. A., Green, A. L., Nandi, D., and Aziz, T. Z. (2007). Deep brain
stimulation: indications and evidence. Expert Rev. Med. Devices 4, 591–603.
doi: 10.1586/17434440.4.5.591
Pistohl, T., Joshi, D., Ganesh, G., Jackson, A., and Nazarpour, K. (2015). Artiﬁcial
proprioceptive feedback for myoelectric control. IEEE Trans. Neural Syst.
Rehabil. Eng. 23, 498–507. doi: 10.1109/TNSRE.2014.2355856
Ramsey, N. F., Heuvel, M. P. V. D., Kho, K. H., and Leijten, F. S. S. (2006). Towards
human BCI applications based on cognitive brain systems: an investigation of
neural signals recorded from the dorsolateral prefrontal cortex. IEEE Trans.
Neural Syst. Rehabil. Eng. 14, 214–217. doi: 10.1109/TNSRE.2006.875582
Ranck, J. B. (1975). Which elements are excited in electrical stimulation of
mammalian central nervous system: a review. Brain Res. 98, 417–440. doi:
10.1016/0006-8993(75)90364-9
Rao, R. P. (2019). Towards neural co-processors for the brain: combining decoding
and encoding in brain–computer interfaces. Curr. Opin. Neurobiol. 55,
142–151. doi: 10.1016/j.conb.2019.03.008
Rao, R. P. N. (2013). Brain-Computer Interfacing: An Introduction. New York, NY:
Cambridge University Press.
Ray, P. G., Meador, K. J., Smith, J. R., Wheless, J. W., Sittenfeld, M., and Clifton,
G. L. (1999). Physiology of perception: cortical stimulation and recording in
humans. Neurology 52, 1044–1049. doi: 10.1212/WNL.52.5.1044
Romanelli, P., Piangerelli, M., Ratel, D., Gaude, C., Costecalde, T., Puttilli, C., et al.
(2018). A novel neural prosthesis providing long-term electrocorticography
recording and cortical stimulation for epilepsy and brain-computer interface.
J. Neurosurg. 1, 1–14. doi: 10.3171/2017.10.jns17400
Rosin, B., Slovik, M., Mitelman, R., Rivlin-Etzion, M., Haber, S. N., Israel, Z.,
et al. (2011). Closed-loop deep brain stimulation is superior in ameliorating
parkinsonism. Neuron 72, 370–384. doi: 10.1016/j.neuron.2011.08.023
Roth, B. J., Saypol, J. M., Hallett, M., and Cohen, L. G. (1991). A theoretical
calculation of the electric ﬁeld induced in the cortex during magnetic
stimulation. Electroencephalogr. Clin. Neurophysiol. 81, 47–56. doi: 10.1016/
0168-5597(91)90103-5
Rubehn, B., Bosman, C., Oostenveld, R., Fries, P., and Stieglitz, T. (2009). A MEMS-
based ﬂexible multichannel ECoG-electrode array. J. Neural Eng. 6:036003.
doi: 10.1088/1741-2560/6/3/036003
Ryapolova-Webb, E., Afshar, P., Stanslaski, S., Denison, T., de Hemptinne,
C., Bankiewicz, K., et al. (2014). Chronic cortical and electromyographic
recordings from a fully implantable device: preclinical experience in a
nonhuman primate. J. Neural Eng. 11:016009. doi: 10.1088/1741-2560/11/1/
016009
Schalk, G. (2015). A general framework for dynamic cortical function: the function-
through-biased-oscillations (FBO) hypothesis. Front. Hum. Neurosci. 9:352.
doi: 10.3389/fnhum.2015.00352
Schiefer, M., Tan, D., Sidek, S. M., and Tyler, D. J. (2016). Sensory feedback by
peripheral nerve stimulation improves task performance in individuals with
upper limb loss using a myoelectric prosthesis. J. Neural Eng. 13:016001.
doi: 10.1088/1741-2560/13/1/016001
Schrock, L. E., Mink, J. W., Woods, D. W., Porta, M., Servello, D., Visser-
Vandewalle, V., et al. (2015). Tourette syndrome deep brain stimulation: a
review and updated recommendations. Mov. Disord. 30, 448–471. doi: 10.1002/
mds.26094
Seeman, S. C., Mogen, B. J., Fetz, E. E., and Perlmutter, S. I. (2017). Paired
stimulation for spike-timing-dependent plasticity in primate sensorimotor
cortex. J. Neurosci. 37, 1935–1949. doi: 10.1523/JNEUROSCI.2046-16.2017
Seo, H., Kim, D., and Jun, S. C. (2015). Computational study of subdural cortical
stimulation: eﬀects of simulating anisotropic conductivity on activation of
cortical neurons. PLoS One 10:e0128590. doi: 10.1371/journal.pone.0128590
Seo, H., Schaworonkow, N., Jun, S. C., and Triesch, J. (2016). A multi-scale
computational model of the eﬀects of TMS on motor cortex. F1000Research
5:1945. doi: 10.12688/f1000research.9277.1
Shannon, R. V. (1992). A model of safe levels for electrical stimulation. IEEE Trans.
Biomed. Eng. 39, 424–426. doi: 10.1109/10.126616
Silva, S., Basser, P. J., and Miranda, P. C. (2008). Elucidating the mechanisms
and loci of neuronal excitation by transcranial magnetic stimulation using a
ﬁnite element model of a cortical sulcus. Clin. Neurophysiol. 119, 2405–2413.
doi: 10.1016/j.clinph.2008.07.248
Sliwinska, M. W., Vitello, S., and Devlin, J. T. (2014). Transcranial magnetic
stimulation for investigating causal brain-behavioral relationships and their
time course. J. Vis. Exp. 89:e51735. doi: 10.3791/51735
Smith, W. A., Uehlin, J. P., Perlmutter, S. I., Rudell, J. C., and Sathe, V. S.
(2017). “A scalable, highly-multiplexed delta-encoded digital feedback ECoG
recording ampliﬁer with common and diﬀerential-mode artifact suppression,”
in Proceedings of the 2017 IEEE Symposium on VLSI Circuits, Digest of Technical
Papers, (Kyoto: IEEE), C172–C173. doi: 10.23919/VLSIC.2017.8008470
Sommer, C. J. (2017). Ischemic stroke: experimental models and reality. Acta
Neuropathol. 133, 245–261. doi: 10.1007/s00401-017-1667-0
Stanslaski, S., Afshar, P., Cong, P., Giftakis, J., Stypulkowski, P., Carlson, D.,
et al. (2012). Design and validation of a fully implantable, chronic, closed-loop
neuromodulation device with concurrent sensing and stimulation. IEEE Trans.
Neural Syst. Rehabil. Eng. 20, 410–421. doi: 10.1109/TNSRE.2012.2183617
Suminski, A. J., Tkach, D. C., Fagg, A. H., and Hatsopoulos, N. G. (2010).
Incorporating feedback from multiple sensory modalities enhances brain-
machine interface control. J. Neurosci. 30, 16777–16787. doi: 10.1523/
JNEUROSCI.3967-10.2010
Tehovnik, E. J., Tolias, A. S., Sultan, F., Slocum, W. M., and Logothetis,
N. K. (2006). Direct and indirect activation of cortical neurons by electrical
microstimulation. J. Neurophysiol. 96, 512–521. doi: 10.1152/jn.00126.2006
Thomson, E. E., Carra, R., and Nicolelis, M. A. L. (2013). Perceiving invisible
light through a somatosensory cortical prosthesis. Nat. Commun. 4:1482. doi:
10.1038/ncomms2497
Vincent, M., Rossel, O., Duﬀau, H., Bonnetblanc, F., and Guiraud, D. (2016a).
“A measure of cortico-cortical potentials evoked by 10Hz direct electrical
stimulation of the brain and by means of a diﬀerential recording mode
of electrocorticographic signals,” in Proceedings of the Annual International
Conference of the IEEE Engineering in Medicine and Biology Society, EMBS,
(Orlando, FL: IEEE), 4543–4546. doi: 10.1109/EMBC.2016.7591738
Vincent, M., Rossel, O., Hayashibe, M., Herbet, G., Duﬀau, H., Guiraud, D.,
et al. (2016b). The diﬀerence between electrical microstimulation and direct
electrical stimulation - Towards new opportunities for innovative functional
brain mapping? Rev. Neurosci. 27, 231–258. doi: 10.1515/revneuro-2015-0029
Vöröslakos, M., Takeuchi, Y., Brinyiczki, K., Zombori, T., Oliva, A., Fernández-
Ruiz, A., et al. (2018). Direct eﬀects of transcranial electric stimulation on brain
circuits in rats and humans. Nat. Commun. 9:483. doi: 10.1038/s41467-018-
02928-3
Wagner, T., Rushmore, J., Eden, U., and Valero-Cabre, A. (2009). Biophysical
foundations underlying TMS: setting the stage for an eﬀective use of
neurostimulation in the cognitive neurosciences. Cortex 45, 1025–1034. doi:
10.1016/j.cortex.2008.10.002
Wander, J. D., and Rao, R. P. N. (2014). Brain-computer interfaces: a powerful
tool for scientiﬁc inquiry. Curr. Opin. Neurobiol. 25, 70–75. doi: 10.1016/j.conb.
2013.11.013
Wang, X., Gkogkidis, A., Iljina, O., Fiederer, L., Henle, C., Mader, I., et al. (2017).
Mapping the ﬁne structure of cortical activity with diﬀerent micro-ECoG
electrode array geometries. J. Neural Eng. 265, 197–212. doi: 10.1088/1741-
2552/aa785e
Frontiers in Neuroscience | www.frontiersin.org
15
August 2019 | Volume 13 | Article 804

Caldwell et al.
DES in ECoG-BCIs
Weber, D. J., Friesen, R., and Miller, L. E. (2012). Interfacing the somatosensory
system to restore touch and Proprioception: essential considerations. J. Mot.
Behav. 44, 403–418. doi: 10.1080/00222895.2012.735283
Wei, X. F., and Grill, W. M. (2009). Impedance characteristics of deep brain
stimulation electrodes in vitro and in vivo. J. Neural Eng. 6:046008. doi: 10.1088/
1741-2560/6/4/046008
Widge, A. S. (2018). Cross-Species neuromodulation from high-intensity
transcranial electrical stimulation. Trends Cogn. Sci. 22, 372–374. doi: 10.1016/
j.tics.2018.03.006
Williams, J. C., Hippensteel, J. A., Dilgen, J., Shain, W., and Kipke, D. R. (2007).
Complex impedance spectroscopy for monitoring tissue responses to inserted
neural implants. J. Neural Eng. 4, 410–423. doi: 10.1088/1741-2560/4/4/007
Wilson, J. A., Felton, E. A., Garell, P. C., Schalk, G., and Williams, J. C. (2006).
ECoG factors underlying multimodal control of a brain-computer interface.
IEEE Trans. Neural Syst. Rehabil. Eng. 14, 246–250. doi: 10.1109/TNSRE.2006.
875570
Wirth, F. P., and Van Buren, J. M. (1971). Referral of pain from dural stimulation
in man. J. Neurosurg. 34, 630–642. doi: 10.3171/jns.1971.34.5.0630
Wongsarnpigoon, A., and Grill, W. M. (2008). Computational modeling of
epidural cortical stimulation. J. Neural. Eng. 5, 443–454. doi: 10.1088/1741-
2560/5/4/009
Yazdan-Shahmorad, A., Silversmith, D. B., Kharazia, V., and Sabes, P. N. (2018).
Targeted cortical reorganization using optogenetics in non-human primates.
eLife 7, 1–21. doi: 10.7554/elife.31034
Yizhar, O., Fenno, L. E., Davidson, T. J., Mogri, M., and Deisseroth, K. (2011).
Optogenetics in Neural Systems. Neuron 71, 9–34. doi: 10.1016/j.neuron.2011.
06.004
Zangen, A., Roth, Y., Voller, B., and Hallett, M. (2005). Transcranial
magnetic stimulation of deep brain regions: evidence for eﬃcacy of
the H-Coil. Clin. Neurophysiol. 116, 775–779. doi: 10.1016/j.clinph.2004.
11.008
Zanos, S., Rembado, I., Chen, D., and Fetz, E. E. (2018). Phase-locked stimulation
during cortical beta oscillations produces bidirectional synaptic plasticity
in awake Monkeys. Curr. Biol. 28, 2515.e–2526.e. doi: 10.1016/j.cub.2018.
07.009
Zhou, A., Johnson, B. C., and Muller, R. (2018a). Toward true closed-loop
neuromodulation: artifact-free recording during stimulation. Curr. Opin.
Neurobiol. 50, 119–127. doi: 10.1016/j.conb.2018.01.012
Zhou, A., Santacruz, S. R., Johnson, B. C., Alexandrov, G., Moin, A.,
Burghardt, F. L., et al. (2018b). A wireless and artefact-free 128-channel
neuromodulation device for closed-loop stimulation and recording in non-
human primates. Nat. Biomed. Eng. 3, 15–26. doi: 10.1038/s41551-018-
0323-x
Conﬂict of Interest Statement: The authors declare that the research was
conducted in the absence of any commercial or ﬁnancial relationships that could
be construed as a potential conﬂict of interest.
Copyright © 2019 Caldwell, Ojemann and Rao. This is an open-access article
distributed under the terms of the Creative Commons Attribution License (CC BY).
The use, distribution or reproduction in other forums is permitted, provided the
original author(s) and the copyright owner(s) are credited and that the original
publication in this journal is cited, in accordance with accepted academic practice. No
use, distribution or reproduction is permitted which does not comply with these terms.
Frontiers in Neuroscience | www.frontiersin.org
16
August 2019 | Volume 13 | Article 804
