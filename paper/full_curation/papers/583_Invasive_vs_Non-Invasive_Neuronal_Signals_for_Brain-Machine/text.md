OPINION published: 27 June 2016

doi: 10.3389/fnins.2016.00295

# Invasive vs. Non-Invasive Neuronal Signals for Brain-Machine Interfaces: Will One Prevail?

Stephan Waldert*

Sobell Department of Motor Neuroscience and Movement Disorders, University College London Institute of Neurology, University College London, London, UK

Keywords: Brain computer interface (BCI), intracortical, action potentials, LFP, EEG, neuroprosthetics, microstimulation, Ethics

Brain-machine interfaces (BMI) translate neuronal activity of the brain into signals driving an external eﬀector or aﬀecting internal body parts and functions. Initially, their applications were seen in the ﬁeld of rehabilitation and medical care for patients to restore social interaction or movement capabilities. Inspired by their success we can already witness the advent of bidirectional and commercial BMIs.

Contemporary BMIs allow for real-time control of prostheses (Gilja et al., 2015), communication (Chen et al., 2015) and “sensation” (O’doherty et al., 2011), notably, the cochlea implant could be considered as the most successful BMI. These applications exemplify that performance can be high but is far from natural interaction with the environment and success depends on manifold factors.

This Opinion is not about algorithms and paradigms but about possibilities and limitations of invasive vs. non-invasive means to electrically interface the brain, argued in the realm of BMIs for direct and intuitive motor control.

Edited by:

Current techniques allow to interface electric neuronal activity in vivo ranging from intracellular potentials over extracellular action potentials (APs) up to local ﬁeld potentials (LFPs). These neurophysiological processes are inherently coupled: neurons can interact ephaptically and via electric synapses, spikes change LFPs via synaptic input which in turn inﬂuences spiking activity, electric ﬁelds of APs can inﬂuence LFPs directly without involvement of synaptic currents. Although the LFP is diﬃcult to interpret (Einevoll et al., 2013), correlations between APs and LFPs vary (Buzsaki et al., 2012) and the information they convey can be independent (Belitski et al., 2008), this coupling may have given rise to discussions I have come across and which have triggered this Opinion: the misconception that, to a certain extent, information conveyed by invasive (APs/LFPs) vs. non-invasive (EEG) signals are similar enough for non-invasive signals, and thus non-invasive BMIs, not to be subject to intrinsic impediments.

Mikhail Lebedev, Duke University, USA

Reviewed by: Thomas G. Brochier, Centre National de la Recherche Scientiﬁque France, France

*Correspondence:

Stephan Waldert s.waldert@ucl.ac.uk

Specialty section: This article was submitted to Neuroprosthetics,

Such speculations may have been nourished by studies showing similar performance for intracortical BMIs based on APs vs. LFPs (Mehring et al., 2003) as the latter are detectable by EEG techniques. Similar performance might be evident for multi-unit APs vs. high-frequency LFPs (>≈200 Hz), which contain extracellular ﬁelds of APs. However, also low/band-pass ﬁltered LFPs below 8 Hz, generally free of such direct AP inﬂuences (Waldert et al., 2013), can show similar BMI performance as APs and are suitable for online BMIs (Stavisky et al., 2015). Importantly, this LFP component also carries information about movement parameters if recorded non-invasively (MEG, EEG; Waldert et al., 2008).

a section of the journal Frontiers in Neuroscience

Received: 04 February 2016 Accepted: 13 June 2016 Published: 27 June 2016

Citation: Waldert S (2016) Invasive vs. Non-Invasive Neuronal Signals for Brain-Machine Interfaces: Will One Prevail? Front. Neurosci. 10:295. doi: 10.3389/fnins.2016.00295

Non-invasive EEG yields lower performance than APs or LFPs (Waldert et al., 2009) but with the ﬁndings mentioned above and novel approaches: Could non-invasive BMIs catch up?

The source of neuronal signals extracted from EEG after thorough removal of noise, muscle, eye, and movement artifacts, are post-synaptic extracellular currents; in fact, the same currents that

Frontiers in Neuroscience | www.frontiersin.org 1 June 2016 | Volume 10 | Article 295

contribute to spike-free LFPs. Despite this common source, there are several diﬀerences, most of which well-documented, between invasive and non-invasive signals.

First, number and type of neurons: As electric ﬁelds produced by neurons decay exponentially with distance, the number of neurons that have to be simultaneously active in a conﬁned area for the ﬁelds to superimpose and produce a detectable signal, is magnitudes smaller for LFP than EEG. Hence, the activity of small neuronal clusters is undetectable or recorded at a lower SNR with EEG. In addition, EEG signals are dominated by ﬁelds of pyramidal neurons as only their morphology (long, parallel dendrites) and high number in the cortex allow ﬁelds to add up and reach the scalp. In contrast, LFPs reﬂect a superposition of a variety of electrophysiological processes, those underlying EEG plus interneurons, APs, etc.

Second, signal composition: Tissue acts as a low-pass ﬁlter generally attenuating high-frequency signals to the extent that buries them in background noise. Hence, with the exception of AP bursts in neuronal populations (Waterstraat et al., 2015), non-invasive signals mainly allow analysis of low-frequency neuronal activity (<≈90 Hz, lower for dry EEG electrodes). Invasive signals convey information up to several kHz. Moreover, frequency-dependent phase shifts might be stronger when signals spread across larger distances (EEG) and might disintegrate temporal consistency across signal components.

Third, spatial distortion: The extracellular space is composed of media with diﬀerent electrophysiological properties, which inﬂuence how ﬁelds spread before being detected as LFPs. On top of this, ﬁelds spread in the cerebrospinal ﬂuid, skull, and scalp, causing further spatial distortion before reaching EEG electrodes. Sophisticated head models and algorithms in combination with high-density EEG montages mitigate distortion (Michel and Murray, 2012) for signals above a certain noise level. To be similar to invasive signals, such models might need to be obtained in vivo for each user individually, rely on stable sensor positions, necessitate ﬁnite-element analysis and run near real-time (BMI performance depends on small delays, Cunningham et al., 2011).

These limitations are intrinsic to EEG and cannot be practicably (or theoretically) overcome. However, EEG oﬀers the paramount advantage to monitor large-scale neuronal activity of the entire brain adjacent to the neurocranium at a low cost and risk-free. Invasive recordings can be deeper but cannot cover the whole neocortex and are initially more laborious due to surgical interventions.

Invasive electrodes come in many forms: single electrodes, electrodes with multiple contacts at the tip or along the shaft, multi-electrode arrays (MEA), or combinations of these in diﬀerent designs. Electrodes can have arbitrary lengths up to several cm or, for example, up to 1.5 mm (Utah, Blackrock Microsystems) or 10 mm (FMA, MicroProbes) in a MEA. Intracortical electrodes typically yield LFPs and detectable APs of 0–5 identiﬁable neurons per intact contact. Electrodes can be speciﬁcally targeted at arbitrary cerebral areas although accuracy decreases with implantation depth (unless aided by MRI and/or CT).

Nevertheless, for several reasons high implantation accuracy seems not to be crucial for invasive motor BMIs as long as

contacts remain in gray matter. The general aim is to record APs and LFPs. In motor cortex, LFPs are recorded at diﬀerent depths and convey information about movement parameters; recorded APs are faint at layer 1 and usually increase in amplitude with electrode depth up to layer 5 because the size of pyramidal cell somas tends to increase from layer 3 to 5, possibly to support the longer dendrites necessary to project to superﬁcial (input) layers, and because layer 5 is the place of large corticospinal neurons, a main cortical output to control motor functions. This region may therefore often be targeted in invasive motor BMIs for high performance. Importantly, even MEAs with relatively short electrodes (Utah) should have access to this activity because: layer 4 is very thin in motor cortex (Rockel et al., 1980), ﬂoating MEAs sink into cortical tissue and APs of large pyramidal neurons can be recorded at several 100 µm distance (experimental and analytical experiences here in the Sobell Department, UCL). For deeper regions, like the anterior wall of the central sulcus, MEAs with longer electrodes can be used to follow layers into the sulcus.

Overall and in contrast to non-invasive signals, invasive signals reﬂect input to, local processing and output of cortical areas. They may even allow to deduce on intracellular states of neurons (Henze et al., 2000).

Hence, a main advantage of intracortical over non-invasive approaches are inherently possible higher information transfer rates. This and two further advantages are decisive for the future of motor BMIs: tuning and sensation.

BMI performance is still far from natural. After BMI initiation this is partly due to an undersampling of the neuronal network required for natural motor control. Performance then increases during BMI usage as the neurons’ tuning “improves” (Carmena et al., 2003), i.e., plasticity enables the brain to learn to control the BMI (closed-loop). This works with arbitrary neurons (Fetz, 1969) and is facilitated by using already tuned neuronal activity (Ganguly and Carmena, 2009) accompanied by a transition from externally assisted to full brain control (Collinger et al., 2013). LFPs seem to be more stable (Flint et al., 2013; Perge et al., 2014), i.e., less easy to tune; probably as in contrast to spiking activity of some neurons, activity of a neuronal cluster needs to change coherently. Although possible (Okazaki et al., 2015), this holds even more so for EEG.

Feedback in closed-loop BMIs has been mainly visual or acoustic. Such inadequate feedback also accounts for low BMI performance as the absence of direct forms of feedback (touch and proprioception) impoverishes information contained in brain signals (Galan et al., 2014) and can disturb the generation of appropriate motor commands (Galan and Baker, 2015). Researchers have begun to employ intracortical microstimulation to establish a direct BMI input channel (Klaes et al., 2014) with possible long-term stability (Callier et al., 2015). This should eventually improve performance as feedback may be delivered speciﬁcally to task-relevant cortical areas, which closes the output-feedback loop adequately. As electrodes may be used for stimulation and recording; stimulation could be adapted to ongoing brain activity to improve eﬃcacy.

In contrast to non-invasive BMIs, the great opportunity oﬀered by invasive BMIs thus lies in accurate control, a prerequisite for user acceptance, combined with restoration

of somatosensation: Prostheses will be controlled using highdimensional BMI output signals (Wodlinger et al., 2015) while at the same time BMI input signals, obtained from skin prostheses (Kim et al., 2014) during interaction with the environment, will be transmitted to cortical sensory areas. Providing such information may remain far oﬀ evoking natural percepts but the brain will learn to make use of such artiﬁcial input channels.

User acceptance is lower for invasive than non-invasive BMIs (Blabe et al., 2015). Invasive BMIs will for many years remain to be used in patients, either for research or if no other remedy is available. Present commercial BMIs are all non-invasive.

This lower acceptance mainly arises from medical concerns related to neurosurgery and the implant. Such risks are clearly not negligible but seem to be partly overrated. For example, validation of DBS showed that complications are rare and, with appropriate procedures, are reduced to 0.9% transient and no permanent deﬁcits (Zrinzo et al., 2012). Even if multiple subpial transection, a series of long cuts in gray matter used to treat epilepsy, is performed in the primary motor cortex, patients are left with no permanent motor deﬁcits (Blount et al., 2004). Implanting electrode arrays for invasive motor BMIs should appear innocuous against this procedure. They have been used in many laboratories for years now and also here in the Sobell Department, UCL, we have not experienced any motor deﬁcits after array implantations. Medical concerns might subside with better awareness of such evidence.

It is now crucial to overcome current challenges of invasive BMIs: better understanding of the “neuronal code,” implant miniaturization, wireless signal transmission (Borton et al., 2013), implants charged from outside (Ho et al., 2014) or by harvesting energy from the body (Hannan et al., 2014). BMIs need to be asynchronous for unrestricted control, adaptable to unstable signals and require better sensorymotor prostheses. A major challenge of intracortical implants is biocompatibility, time-dependent degradation of recording quality, and eventually implant failure due to tissue damage during implantation, array micromotion, and a breach of the blood-brain-barrier triggering glial scarring, neurodegeneration, and neuronal death. Only few APs are still recorded years after implantation (Hochberg et al., 2012). LFPs also deteriorate but might show better long-term stability (Flint et al., 2013;

Perge et al., 2014). To increase longevity and yield, electrodes need to be reduced in size, coated with neurointegrative, anti-inﬂammatory factors (Gunasekera et al., 2015), and/or redesigned (e.g., carbon nanotubes, Vitale et al., 2015; Lopez et al., 2016).

As an invasive but extracortical technique, miniaturized ECoG causes lesser cortical tissue damage/irritation and allows for epicortical recordings of LFPs at high spatial resolution and, as recently shown, also of spiking activity (Khodagholy et al., 2015). Beneﬁts derivable from such advances, especially regarding increased information transfer rates, biocompatibility, and long-term signal stability (Chao et al., 2010) over years, are being investigated and might be decisive for the development of future BMIs.

Once invasive BMIs are fully body-embeddable and their beneﬁts outweigh concerns, they might become acceptable to the majority (of patients). However, other, non-medical concerns have to be addressed as well. As invasive BMIs allow access to the brain, i.e., the individual as such, it is necessary to discuss (and regulate) socio-ethical issues: privacy, “mind reading,” remote control, brain enhancement, which accuracy legitimates control of potentially hazardous devices, liability, and eventually selfperception and perception through others.

This Opinion is not a polemic against EEG. EEG is a prime tool for many applications, e.g., medical, rehabilitation, current BMIs for communication.

The conclusion of this Opinion is that once technical, socioethical, and neuroscientiﬁc challenges are resolved, user concerns might subside, and invasive BMIs (using primarily intracortical and potentially epicortical recordings) will prevail in most applications; certainly those for restoration of motor functions and perhaps even in applications not medically indicated.

## AUTHOR CONTRIBUTIONS

SW conceived and wrote the paper.

## FUNDING

This work was supported by the Wellcome Trust (WT102849MA).

## REFERENCES

Belitski, A., Gretton, A., Magri, C., Murayama, Y., Montemurro, M. A., Logothetis, N. K., et al. (2008). Low-frequency local ﬁeld potentials and spikes in primary visual cortex convey independent visual information. J. Neurosci. 28, 5696–5709. doi: 10.1523/JNEUROSCI.000908.2008

Blabe, C. H., Gilja, V., Chestek, C. A., Shenoy, K. V., Anderson, K. D., and Henderson, J. M. (2015). Assessment of brain-machine interfaces from the perspective of people with paralysis. J. Neural Eng. 12:043002. doi: 10.1088/1741-2560/12/4/043002

Blount, J. P., Langburt, W., Otsubo, H., Chitoku, S., Ochi, A., Weiss, S., et al.

(2004). Multiple subpial transections in the treatment of pediatric epilepsy. J. Neurosurg. 100, 118–124. doi: 10.3171/ped.2004.100.2.0118

Borton, D. A., Yin, M., Aceros, J., and Nurmikko, A. (2013). An implantable wireless neural interface for recording cortical circuit dynamics in moving primates. J. Neural Eng. 10:026010. doi: 10.1088/1741-2560/10/2/026010

Buzsaki, G., Anastassiou, C. A., and Koch, C. (2012). The origin of extracellular ﬁelds and currents–EEG, ECoG, LFP and spikes. Nat. Rev. Neurosci. 13, 407–420. doi: 10.1038/nrn3241

Callier, T., Schluter, E. W., Tabot, G. A., Miller, L. E., Tenore, F. V., and Bensmaia, S. J. (2015). Long-term stability of sensitivity to intracortical microstimulation of somatosensory cortex. J. Neural Eng. 12:056010. doi: 10.1088/1741-2560/12/5/056010

Carmena, J. M., Lebedev, M. A., Crist, R. E., O’doherty, J. E., Santucci, D. M., Dimitrov, D. F., et al. (2003). Learning to control a brain-machine interface for reaching and grasping by primates. PLoS Biol. 1:e42. doi: 10.1371/journal.pbio.0000042

Chao, Z. C., Nagasaka, Y., and Fujii, N. (2010). Long-term asynchronous decoding of arm motion using electrocorticographic signals in monkeys. Front. Neuroeng. 3:3. doi: 10.3389/fneng.2010.00003

Chen, X., Wang, Y., Gao, S., Jung, T. P., and Gao, X. (2015). Filter bank canonical correlation analysis for implementing a high-speed SSVEP-based brain-computer interface. J. Neural Eng. 12:046008. doi: 10.1088/17412560/12/4/046008

Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber, D. J., et al. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. Lancet 381, 557–564. doi: 10.1016/S01406736(12)61816-9

Cunningham, J. P., Nuyujukian, P., Gilja, V., Chestek, C. A., Ryu, S. I., and Shenoy, K. V. (2011). A closed-loop human simulator for investigating the role of feedback control in brain-machine interfaces. J. Neurophysiol. 105, 1932–1949. doi: 10.1152/jn.00503.2010

Einevoll, G. T., Kayser, C., Logothetis, N. K., and Panzeri, S. (2013). Modelling and analysis of local ﬁeld potentials for studying the function of cortical circuits. Nat. Rev. Neurosci. 14, 770–785. doi: 10.1038/nrn3599

Fetz, E. E. (1969). Operant conditioning of cortical unit activity. Science 163, 955–958. doi: 10.1126/science.163.3870.955

Flint, R. D., Wright, Z. A., Scheid, M. R., and Slutzky, M. W. (2013). Long term, stable brain machine interface performance using local ﬁeld potentials and multiunit spikes. J. Neural Eng. 10:056005. doi: 10.1088/17412560/10/5/056005

Galan, F., Baker, M. R., Alter, K., and Baker, S. N. (2014). Degraded EEG decoding of wrist movements in absence of kinaesthetic feedback. Hum. Brain Mapp. 36, 643–654. doi: 10.1002/hbm.22653

Galan, F., and Baker, S. N. (2015). Deaﬀerented controllers: a fundamental failure mechanism in cortical neuroprosthetic systems. Front. Behav. Neurosci. 9:186. doi: 10.3389/fnbeh.2015.00186

Ganguly, K., and Carmena, J. M. (2009). Emergence of a stable cortical map for neuroprosthetic control. PLoS Biol. 7:e1000153. doi: 10.1371/journal.pbio.1000153

Gilja, V., Pandarinath, C., Blabe, C. H., Nuyujukian, P., Simeral, J. D., Sarma, A. A., et al. (2015). Clinical translation of a high-performance neural prosthesis. Nat. Med. 21, 1142–1145. doi: 10.1038/nm.3953

Gunasekera, B., Saxena, T., Bellamkonda, R., and Karumbaiah, L. (2015). Intracortical recording interfaces: current challenges to chronic recording function. ACS Chem. Neurosci. 6, 68–83. doi: 10.1021/cn5002864

Hannan, M. A., Mutashar, S., Samad, S. A., and Hussain, A. (2014). Energy harvesting for the implantable biomedical devices: issues and challenges. Biomed. Eng. 13:79. doi: 10.1186/1475-925X-13-79

Henze, D. A., Borhegyi, Z., Csicsvari, J., Mamiya, A., Harris, K. D., and Buzsaki, G. (2000). Intracellular features predicted by extracellular recordings in the hippocampus in vivo. J. Neurophysiol. 84, 390–400.

Ho, J. S., Yeh, A. J., Neofytou, E., Kim, S., Tanabe, Y., Patlolla, B., et al. (2014). Wireless power transfer to deep-tissue microimplants. Proc. Natl. Acad. Sci. U.S.A. 111, 7974–7979. doi: 10.1073/pnas.1403002111

Hochberg, L. R., Bacher, D., Jarosiewicz, B., Masse, N. Y., Simeral, J. D., Vogel, J., et al. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485, 372–375. doi: 10.1038/nature11076

Khodagholy, D., Gelinas, J. N., Thesen, T., Doyle, W., Devinsky, O., Malliaras, G. G., et al. (2015). NeuroGrid: recording action potentials from the surface of the brain. Nat. Neurosci. 18, 310–315. doi: 10.1038/nn.3905

Kim, J., Lee, M., Shim, H. J., Ghaﬀari, R., Cho, H. R., Son, D., et al. (2014). Stretchable silicon nanoribbon electronics for skin prosthesis. Nat. Commun. 5, 5747. doi: 10.1038/ncomms6747

Klaes, C., Shi, Y., Kellis, S., Minxha, J., Revechkis, B., and Andersen, R. A. (2014). A cognitive neuroprosthetic that uses cortical stimulation for somatosensory feedback. J. Neural Eng. 11:056024. doi: 10.1088/1741-2560/11/5/ 056024

Lopez, C. M., Mitra, S., Putzeys, J., Raducanu, B., Ballini, M., Andrei, A., et al. (2016). “A 966-electrode neural probe with 384 conﬁgurable channels in 0.13µm SOI CMOS,” in IEEE International Solid-State Circuits Conference (ISSCC) (San Fransisco, CA), 392–393. doi: 10.1109/ISSCC.2016.7418072

Mehring, C., Rickert, J., Vaadia, E., Cardoso De Oliveira, S., Aertsen, A., and Rotter, S. (2003). Inference of hand movements from local ﬁeld potentials in monkey motor cortex. Nat. Neurosci. 6, 1253–1254. doi: 10.1038/nn1158

Michel, C. M., and Murray, M. M. (2012). Towards the utilization of EEG as a brain imaging tool. Neuroimage 61, 371–385. doi: 10.1016/j.neuroimage.2011.12.039

O’doherty, J. E., Lebedev, M. A., Iﬀt, P. J., Zhuang, K. Z., Shokur, S., Bleuler, H., et al. (2011). Active tactile exploration using a brain-machine-brain interface. Nature 479, 228–231. doi: 10.1038/nature10489

Okazaki, Y. O., Horschig, J. M., Luther, L., Oostenveld, R., Murakami, I., and Jensen, O. (2015). Real-time MEG neurofeedback training of posterior alpha activity modulates subsequent visual detection performance. Neuroimage 107, 323–332. doi: 10.1016/j.neuroimage.2014.12.014

Perge, J. A., Zhang, S., Malik, W. Q., Homer, M. L., Cash, S., Friehs, G., et al. (2014). Reliability of directional information in unsorted spikes and local ﬁeld potentials recorded in human motor cortex. J. Neural Eng. 11:046007. doi: 10.1088/1741-2560/11/4/046007

Rockel, A. J., Hiorns, R. W., and Powell, T. P. (1980). The basic uniformity in structure of the neocortex. Brain 103, 221–244. doi: 10.1093/brain/103.2.221 Stavisky, S. D., Kao, J. C., Nuyujukian, P., Ryu, S. I., and Shenoy, K. V. (2015). A high performing brain-machine interface driven by low-frequency local ﬁeld potentials alone and together with spikes. J. Neural Eng. 12, 036009. doi: 10.1088/1741-2560/12/3/036009

Vitale, F., Summerson, S. R., Aazhang, B., Kemere, C., and Pasquali, M. (2015). Neural stimulation and recording with bidirectional, soft carbon nanotube ﬁber microelectrodes. ACS Nano 9, 4465–4474. doi: 10.1021/acsnano.5b01060

Waldert, S., Lemon, R. N., and Kraskov, A. (2013). Inﬂuence of spiking activity on cortical local ﬁeld potentials. J. Physiol. 591, 5291–5303. doi: 10.1113/jphysiol.2013.258228

Waldert, S., Pistohl, T., Braun, C., Ball, T., Aertsen, A., and Mehring, C. (2009). A review on directional information in neural signals for brain-machine interfaces. J. Physiol. Paris 103, 244–254. doi: 10.1016/j.jphysparis.2009.08.007

Waldert, S., Preissl, H., Demandt, E., Braun, C., Birbaumer, N., Aertsen, A., et al.

(2008). Hand movement direction decoded from MEG and EEG. J. Neurosci. 28, 1000–1008. doi: 10.1523/JNEUROSCI.5171-07.2008

Waterstraat, G., Burghoﬀ, M., Fedele, T., Nikulin, V., Scheer, H. J., and Curio, G. (2015). Non-invasive single-trial EEG detection of evoked human neocortical population spikes. Neuroimage 105, 13–20. doi: 10.1016/j.neuroimage.2014.10.024

Wodlinger, B., Downey, J. E., Tyler-Kabara, E. C., Schwartz, A. B., Boninger, M. L., and Collinger, J. L. (2015). Ten-dimensional anthropomorphic arm control in a human brain-machine interface: diﬃculties, solutions, and limitations. J. Neural. Eng. 12, 016011. doi: 10.1088/1741-2560/12/1/016011

Zrinzo, L., Foltynie, T., Limousin, P., and Hariz, M. I. (2012). Reducing hemorrhagic complications in functional neurosurgery: a large case series and systematic literature review. J. Neurosurg. 116, 84–94. doi: 10.3171/2011.8.JNS101407

Conﬂict of Interest Statement: The author declares that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2016 Waldert. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

