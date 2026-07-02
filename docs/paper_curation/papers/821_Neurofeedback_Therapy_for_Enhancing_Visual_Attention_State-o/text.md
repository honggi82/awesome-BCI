REVIEW

published: 03 August 2016 doi: 10.3389/fnins.2016.00352

# Neurofeedback Therapy for Enhancing Visual Attention: State-of-the-Art and Challenges

Mehdi Ordikhani-Seyedlar1*, Mikhail A. Lebedev2,3, Helge B. D. Sorensen1 and Sadasivan Puthusserypady1

1 Division of Biomedical Engineering, Department of Electrical Engineering, Technical University of Denmark, Lyngby, Denmark, 2 Department of Neurobiology, Duke University, Durham, NC, USA, 3 Center for Neuroengineering, Duke University, Durham, NC, USA

We have witnessed a rapid development of brain-computer interfaces (BCIs) linking the brain to external devices. BCIs can be utilized to treat neurological conditions and even to augment brain functions. BCIs offer a promising treatment for mental disorders, including disorders of attention. Here we review the current state of the art and challenges of attention-based BCIs, with a focus on visual attention. Attention-based BCIs utilize electroencephalograms (EEGs) or other recording techniques to generate neurofeedback, which patients use to improve their attention, a complex cognitive function. Although progress has been made in the studies of neural mechanisms of attention, extraction of attention-related neural signals needed for BCI operations is a difﬁcult problem. To attain good BCI performance, it is important to select the features of neural activity that represent attentional signals. BCI decoding of attention-related activity may be hindered by the presence of different neural signals. Therefore, BCI accuracy can be improved by signal processing algorithms that dissociate signals of interest from irrelevant activities. Notwithstanding recent progress, optimal processing of attentional neural signals remains a fundamental challenge for the development of efﬁcient therapies for disorders of attention.

Edited by: Stefano Ferraina, Sapienza University of Rome, Italy

Reviewed by: Olivia Carter,

University of Melbourne, Australia Tomasz Maciej Rutkowski, University of Tokyo, Japan

*Correspondence:

Mehdi Ordikhani-Seyedlar mehdi.ordikhani@gmail.com

Keywords: visual attention, electroencephalography, brain-computer interface, feature extraction

Specialty section: This article was submitted to Neural Technology,

### INTRODUCTION

a section of the journal Frontiers in Neuroscience

The visual system in both human and non-human organisms transforms complex input information into robust neural representation of the visual world. Because the amount of information can only decrease during stochastic neural processing, it is crucial for the visual system to selectively process behaviorally relevant information (Sprague et al., 2015). For instance, when a driver approaches a busy intersection it is important to detect and respond to the relevant traﬃc light rather than any light source in the visual scene. Attention is the ability to block the irrelevant information to the current task and to enhance the processing of the important information. This key neural function can deteriorate due to some disorders. Patients with disorders of attention are unable to allocate their focus of attention continuously to one task or easily get distracted by irrelevant information. One of the most common disorders of attention, attention deﬁcit hyperactivity disorder (ADHD), is a mental condition characterized by inattention, hyperactivity and impulsivity. ADHD symptoms are dominant in childhood, and extend to adulthood in 15–40%

Received: 19 April 2016 Accepted: 12 July 2016

Published: 03 August 2016 Citation:

Ordikhani-Seyedlar M, Lebedev MA, Sorensen HBD and Puthusserypady S

(2016) Neurofeedback Therapy for Enhancing Visual Attention: State-of-the-Art and Challenges.

Front. Neurosci. 10:352. doi: 10.3389/fnins.2016.00352

Frontiers in Neuroscience | www.frontiersin.org 1 August 2016 | Volume 10 | Article 352

of cases (Biederman et al., 2000; Faraone et al., 2006). ADHD impairs performance in academic, occupational and social tasks (Fleming and McMahon, 2012). According to a meta-regression analysis of 102 studies, ADHD has 5% prevalence worldwide (Polanczyk and Rohde, 2007; Skounti et al., 2007; Millichap, 2008). Treatment strategies have been mostly pharmacological, such as prescription of psychostimulants. However, long-term treatment with pharmacological agents is hindered by side-eﬀects (Conners et al., 2001; Greenhill et al., 2001). Children develop anxiety symptoms after being treated with psychostimulants for 6 months and longer (Vance et al., 1999). There is also a considerable risk of drug misuse and abuse (Kollins, 2008; Steiner et al., 2014a). Psychological therapy, an alternative approach, relieves ADHD symptoms in 30% of cases (Zarin et al., 1998). Overall, currently available therapies for ADHD are only partially eﬀective.

Here we review a novel strategy for enhancing the attention capability in patients with disorders of attention. This strategy is based on brain-computer interface (BCI) approach (Arns et al., 2009; Lim et al., 2010, 2012). BCIs establish uni- or bidirectional communication between the brain and external devices (Wolpaw et al., 2000; Donoghue et al., 2004; Lebedev and Nicolelis, 2006; Nicolelis and Lebedev, 2009; Lebedev, 2014; Schwarz et al., 2014). BCIs decode neural signals using mathematical algorithms. Such decoding often utilizes templates of neural patterns deﬁned based on prior knowledge of the characteristics of diﬀerent neural states. A computer algorithm then compares neural activities with the set of templates to ﬁnd the best match and determine the current neural state. Additionally, the algorithm can evaluate how well the brain signals match certain requirements, and generate a feedback based on the diﬀerence. Such feedback can be used to improve neural function in patients: patients observe their own brain activity in real time, and learn to self-regulate this activity in order to bring it to normal state. This paradigm is called “neurofeedback” and the corresponding therapeutic approach is called “neurofeedback therapy.” BCIs for humans most commonly utilize electroencephalographic (EEG) recordings (Kus et al., 2013; Tonin et al., 2013; Bamdadian et al., 2014; De Vos et al., 2014; Kashihara, 2014; Yang et al., 2014). Additionally, BCIs can employ magnetoencephalography (MEG) (Mellinger et al., 2007; Bianchi et al., 2010; Ahn et al., 2013), near infrared spectroscopy (NIRS) (Coyle et al., 2004; Sitaram et al., 2007; Power et al., 2012; Waldert et al., 2012; Khan et al., 2014), functional magnetic resonance imaging (fMRI) (Logothetis, 2003; deCharms et al., 2005; Ruiz et al., 2013; Sato et al., 2013), electrocortigraphy (ECoG) (Freeman et al., 2003; Leuthardt et al., 2004, 2009; Schalk, 2010), and multi-electrode intracranial implants (Nicolelis and Ribeiro, 2002; Carmena et al., 2003; Nicolelis et al., 2003; Lebedev et al., 2005, 2011; Zacksenhouse et al., 2007; Peikon et al., 2009; Iﬀt et al., 2013; see Figure 1 for comparison).

Neurofeedback therapy is applicable to a number of neurological disorders of attention (Lofthouse et al., 2012b; Hillard et al., 2013; Gevensleben et al., 2014; Steiner et al., 2014c; Zandi Mehran et al., 2014). Attention-based neurofeedback paradigms for ADHDs are usually based on visual attention (Arns et al., 2014). As to recording methods, some (EEG, NIRS,

|[Figure 1]<br><br>FIGURE 1 | Temporal and spatial resolution of different BCI techniques. Although EEG has a relatively poor spatial resolution, its high temporal resolution is an adequate characteristic for real-time BCIs. Abbreviations: EEG, electroencephalography; MEG, magneto-encephalogram; NIRS, near-infrared spectroscopy; fMRI, functional magnetic resonance imaging; ECoG, electro-corticogram; LFPs, local ﬁeld potentials. Image is inspired from Van Gerven et al. (2009).|
|---|

ECoG) have been already shown eﬀective for attention control and for treatment of ADHDs, whereas the applicability of others, such as MEG and fMRI, is being researched (Ahn et al., 2013; Sulzer et al., 2013; Sokunbi et al., 2014; Stoeckel et al., 2014; Bruhl, 2015; Okazaki et al., 2015). Implementing an attentionbased BCI is a challenging task because the neural representation of attention is highly complex (Ming et al., 2009; Rossini et al., 2012). A good understanding of neurophysiology of attention is required to extract attentional signals from neural recordings and dissociate them from the other ongoing activities in the brain (Sanei and Chambers, 2008). Notwithstanding these diﬃculties, visual-attention based BCI systems have been already developed and applied to ADHD (Christiansen et al., 2014; Heinrich et al., 2014; Holtmann et al., 2014a,b; Micoulaud-Franchi et al., 2014; Steiner et al., 2014b). In this article, we cover the current state of the art and future challenges in this research.

DECODING OF VISUAL ATTENTION FROM NEURAL SIGNALS

Neural Mechanisms of Visual Attention

In everyday life, we constantly deal with multiple sensory streams from our complex and dynamic environment. The brain starts the processing of this incoming information by ﬁltering out irrelevant signals, which are not consciously experienced because of the ﬁltering. Only a tiny amount of the incoming information enters the higher-order processing levels and becomes available to consciousness (Posner, 1994, 2012). Selective attention is a key function that enables the brain to eﬀectively use its limited information processing capability when confronted with an immense number of inputs from all sensory modalities. High-level cortical areas, particularly the areas of the frontal cortex, play a key role in attentional control. It has been long known that damage to prefrontal cortex (PFC) causes mental deﬁcits which are consistent with a loss of attentional control

(Ferrier, 1876). Neurophysiological and functional neuroimaging studies by Posner’s group (Fan et al., 2005; Posner and Rothbart, 2007; Petersen and Posner, 2012) have provided a wealth of information on cortical circuitry for attentional control. The main conclusion of these studies is that attention is controlled by a network of interconnected areas that also involved in oculomotor control. These areas include the frontal eye ﬁeld (FEF), parietal areas and subcortical structures, importantly superior colliculus. This attentional selection network works together with yet another, overlapping network of areas that sustains the focus of attention, called sustained attention. The latter system maintains the focus of attention on the selected stimulus. It is composed of the parietal cortex, right frontal cortex and locus coeruleus (Corbetta et al., 2008). Volumetric analysis in ADHD subjects showed that they have smaller frontal cortex compared to healthy subjects (He et al., 2015). This ﬁnding explains the deﬁcits in both selective and sustained attention (Pritchard et al., 2008; Avisar and Shalev, 2011; Gomes et al., 2012; Wang et al., 2013). Notably, attention-based BCIs usually require both selecting a visual target and focusing on it (i.e., selective attention) and mental endurance training (i.e., sustained attention).

Selective attention is not a unitary process; it is driven by distinct functional sub-processes associated with diﬀerent selection criteria (Brosch et al., 2011). Two major sub-processes are: stimulus-driven (exogenous) attention and observerdependent (endogenous) attention. Exogenous attention is driven by intrinsic low-level features of sensory inputs (Egeth and Yantis, 1997; Wolfe and Horowitz, 2004). Low-level properties include such features as stimulus intensity, color and contrast. They all trigger involuntary responses. Endogenous attention refers to selection of a target based on an internal state and conscious expectation of a speciﬁc object or location (Posner et al., 1980; Desimone and Duncan, 1995). Endogenous selection is performed based on the current aim of the observer. In the classical Posner experiment that dissociated endogenous and exogenous eﬀects, participants were instructed to press a button in response to a visual stimulus that appeared either to the left or right of a central ﬁxation point (Posner, 1980). They were asked to keep their eyes ﬁxed at the center of the screen throughout the task and covertly (i.e., without looking at the target) attend to the peripheral location. To guide this covert attention, a symbolic cue was presented at the center of the screen, which instructed the location to attend. This cue preceded the stimulus onset, and correctly speciﬁed the upcoming stimulus location in 80% of the trials. In the remaining 20% of trials, the target appeared at a location that disagreed with the cue. This study showed that the reaction time was signiﬁcantly shorter when the stimulus was presented at the attended location than when it appeared in the opposite location and there was a misalignment between the endogenous and exogenous attention. Busse et al. investigated neurophysiological mechanisms underlying these two types of attention (Busse et al., 2008). They recorded from single neurons in macaque middle temporal area while monkeys’ endogenous and/or exogenous attention was manipulated by the task events. They used a double-cueing paradigm where the ﬁrst cue instructed the monkey to attend (endogenous attention) to

one of three moving random dot patterns (RDPs) until a second cue. The second cue was unpredictable, and therefore captured exogenous attention. It signaled to either shift or maintain the current focus of attention. Findings of this experiment showed that the neural activity was enhanced when attention was endogenously shifted to the ﬁrst cue. Then, attention was exogenously attracted to the second cue, which was manifested by a transient interruption of neural activity for approximately 70ms, after which the endogenous attention restored neural representation of the previously relevant stimulus. These results showed that the interruption of endogenous attention by exogenous attention is not a simple refocusing to the new stimulus. Rather, there are separate ongoing processes with distinct neural correlates for endogenous and exogenous eﬀects, as well as an interaction between these mechanisms.

Both endogenous and exogenous attention can be maintained with and without eye movements (i.e., overtly or covertly, respectively). The premotor theory of attention (Rizzolatti et al., 1987) suggests that essentially the same neural circuits in the frontal and parietal areas control the orientation of both overt and covert attention. For overt shifts of attention, eye movements are prepared and executed, whereas for covert shifts they are prepared but not executed. The premotor theory of attention is supported by the fMRI studies showing an overlap between the frontal and parietal regions activated for covert and overt attentional tasks (de Haan et al., 2008). Additionally, neurons in the intermediate layer of superior colliculus which has been long known for their involvement in saccades, are also engaged in the covert attentional shifts (Ignashchenkova et al., 2004). Golla et al. reported a clinical case of impaired overt attention in a cerebellar disorder, and suggested that the cerebellum plays a role in spatial attention (Golla et al., 2005).

Lebedev, Wise and their colleagues compared neural representation of attention with the representation of other behavioral variables, such as spatial memory, target of movement and gaze angle, which often coincide with the orientation of attention, but still can be controlled independently by the brain. In one study (Lebedev and Wise, 2001), they compared neuronal activity in monkey’s dorsal premotor cortex (PMd) that reﬂected the orientation of selective spatial attention with neuronal activities that represented motor preparation, gaze angle, and saccades. The monkeys’ attention was attracted by a robot, to which they attended in order to know when to initiate a reaching movement. The target of movement varied. It was either the location of the feeder mounted on the robot or a location of a diﬀerent feeder. This study showed that approximately 20% of PMd reﬂected the orientation of selective spatial attention, which could be disengaged from the other spatial variables. These attention-tuned PMd neurons could account for gaze-independent (covert) attentional eﬀects in behaviors with stimulus-response incompatibility. In another study (Lebedev et al., 2004), Lebedev et al. tested the theory that the main function of prefrontal cortex (PF) is the maintenance of working memory. To investigate alternative possibilities, activity of PF neurons was recorded while the monkeys performed an oculomotor task that required remembering one location, but attending to a diﬀerent location. The largest subpopulation of

PF neurons was linked to attention, not to working memory, which indicated that PF has a major contribution to selective spatial attention. Consistent with these ﬁndings, studies in human subjects demonstrated the crucial role of frontal cortex in ADHDs (Praamstra et al., 2005; Dirlikov et al., 2015). Dirlikov et al. (2015) used brain imaging technique to explore the cortical morphology in 93 children with ADHD. They found a reduction in cortical surface of PF and premotor cortex (Dirlikov et al., 2015). Several neuroimaging studies suggested that visual attention is controlled by a network of cortical areas interconnected with the FEF. Gray matter is substantially aﬀected in ADHD in the structures of this network, including dorsal and ventral prefrontal cortices, dorsal anterior cingulate area and inferior parietal cortex (Valera et al., 2007; Szuromi et al., 2011). Jonkman and colleagues suggested that the frontal lobe performs early selective ﬁltering, and disorders of this function cause ADHD (Jonkman et al., 2004). A recent resting-state EEG study also suggested that frontal cortex abnormalities are a reliable marker for ADHD (Keune et al., 2015).

Neural oscillations is another neural marker of attention. Oscillations represent synchronous activity of neuronal populations of diﬀerent sizes, from local to very large. They can be detected in local ﬁeld potentials (LFPs) recorded with invasive electrodes, or EEGs recorded non-invasively from the scalp (Kahana, 2006). Oscillations are conventionally classiﬁed into ﬁve frequency bands: δ (1–4Hz), θ (4–8Hz), α (8–12Hz), β (12– 30Hz), and γ (30–80Hz). Attentional eﬀects have been reported for each of these bands. For instance, attending to a spatial location and anticipating a stimulus at that location is associated with α rhythm attenuation (Rohenkohl and Nobre, 2011). α oscillations are involved in attentional gating of information ﬂow between brain regions (Fu et al., 2001; ter Huurne et al.,

- 2013). To investigate the relationship between brain oscillations and ADHD, ter Huurne used a motion coherence detection task where subjects were instructed to direct attention to either left or right visual ﬁeld. The attended stimulus was a random dot kinematogram, a ﬁeld of chaotically moving dots. Subjects were instructed to respond after the dot pattern started to move coherently in the horizontal, but not vertical dimension in the attended hemiﬁeld. Dot movements in the unattended hemiﬁeld had to be ignored. In healthy subjects, lateralized and sustained α oscillations were detected in the visual cortex during the period when the subjects prepared to respond. In patients with ADHD, oscillations started, but they were not sustained and often stopped before the stimulus onset. Furthermore, lateralization of α oscillation was highly correlated with the degree of spatial attention in the healthy group, but not in the ADHD group (ter Huurne et al., 2013). In neurofeedback training experiments, children with ADHD were able to increase α-power following 18 training sessions (Escolano et al., 2014). Overall, these studies suggest that brain oscillations can be used to monitor neural regulation of attention and improve it using neurofeedback therapy.

BCIs for Visual Attention

Early attempts to treat disorders of attention using neurofeedback date back to the mid-eighties and nineties (Elbert et al., 1980; Lutzenberger et al., 1980; Wolpaw et al., 1991). Since

then, considerable progress has been made in the development of computer algorithms for the decoding of attention-related neural signals. In a typical setting, subjects endeavor to keep their visual attention while playing a video game. Attention related brain signals are extracted from the neural recordings and fed back to the subjects using visual feedback. Successful performance is rewarded. Repeated training sessions with such a BCI system engage brain plasticity mechanisms, and eventually improve attention (Dobkin, 2007; Rossini et al., 2012).

Both invasive and non-invasive recordings have been used in BCIs. Invasive BCIs utilize electrodes that penetrate the brain (LFPs and single-unit recordings) or are placed on the brain surface (ECoG). These systems require an invasive surgical procedure to implant the electrodes. Non-invasive BCIs, on the other hand, do not require any surgery and can be safely and easily implemented. Non-invasive sensors are placed on the scalp (EEG, fNIRS), or in some implementations make no contact with the head (fMRI, MEG) (see Table 1 for details). Additionally, hybrid or multimodal BCIs employ combinations of diﬀerent recording methods in order to improve performance. Fazli et al. (2012) developed a multimodal BCI consisting of the combination of EEG and NIRS that improved the signal classiﬁcation accuracy in 90% of participants. That multimodal BCI had higher sensitivity and speciﬁcity and were resistant to environmental noise. Such combined EEG-NIRS neurofeedback can be used by subjects who cannot operate a BCI solely by their EEG activity (Fazli et al., 2012).

The research on BCIs that improve attention has experienced a steady growth, especially BCIs for ADHD patients. Some of these results are controversial. A number of studies reported positive outcome of neurofeedback training (Leins et al., 2007; Gevensleben et al., 2009; Steiner et al., 2011; Wangler et al., 2011), whereas others questioned these ﬁndings. In the camp of neurofeedback advocates, Arns et al. (2009) analyzed literature on neurofeedback therapy for ADHD and concluded that this treatment was “eﬃcient and speciﬁc” (Arns et al., 2009). Lofthouse et al. (2012a) called this therapy “probably eﬃcacious” based on their analysis of research conducted from 1994 to 2010, where the majority of studies utilized θ/β ratio (see below) (Lofthouse et al., 2012a). However, Vollebregt et al. (2014a) came to a diﬀerent conclusion in their systematic review of frequency-band based BCIs for ADHD. They concluded that there was no signiﬁcant eﬀect of treatment on any neurocognitive variables aﬀected by ADHD (Vollebregt et al., 2014a). This negative result highlights the need for further research on EEG features that would better suit attention-based BCIs. Here we review these features and the ways they could be used to improve neurofeedback therapy for ADHD.

FEATURE EXTRACTION FOR VISUAL-ATTENTION BCIs

Feature extraction is a critical part of BCI implementation and design (Shahid and Prasad, 2011). During this processing stage, a speciﬁc characteristics are extracted from brain recordings, which are then decoded and converted into control commands or neurofeedback. Depending on the recording method, diﬀerent

- TABLE 1 | Comparison of different signal acquisition methods used for BCI application.

BCI method (measured signal type)

Advantages Disadvantages

LFPs (Firing rate of bundles of neurons)

High SNR; low variability during the experiment; targeting the activity in speciﬁc brain areas; higher resolution of detecting temporal and spatial features in several parallel-activated brain regions.

Intracranial surgery; very susceptible to signal-loss in long-term implantation (Shain et al., 2003; Donoghue et al., 2004); requires precise source localization in order to implant the electrodes in the right location; less common in human studies.

ECoG (Electrical activity from brain surface)

Supports accurate BCI operation with little training (Leuthardt et al., 2004); higher spatial resolution and amplitude than EEG (Freeman et al., 2000; Leuthardt et al., 2009); far less EMG and EOG artifacts (Freeman et al., 2003; Ball et al., 2009); greater long-term functionality compared to LFPs (Margalit et al., 2003); more stable SNR compared to EEG (Schalk, 2010).

Intracranial surgery; Limited long-term functional stability and signal loss (Schalk and Leuthardt, 2011); very rare research application (Sutter and Tran, 1992).

EEG (Electrical activity from the scalp)

Superior temporal resolution (suitable for real-time experiments); ease of use (non-invasive) even by inexpert individuals; inexpensive (compared to other devices); least ethical concern and medical risks compared to other methods; portable.

Susceptible to noise (EMG, EOG and environmental); Low spatial resolution (harder to localize brain activities); requires a substantial degree of user training in BCI development.

fMRI [Blood oxygenation level dependent (BOLD)]

Superior spatial resolution (deCharms et al., 2005; Lee et al., 2009); signal detection from whole brain including the subcortical structures (Logothetis, 2003; Weiskopf et al., 2004).

Signal drift due to imperfection of magnetic gradient ﬁeld (Lee et al., 2009); limited to BOLD-signal-based analysis (can be done in ERP experiments but not in frequency-range analysis); less suitable for real-time BCI due to low temporal resolution; strict physical restriction of subjects inside the scanner due to motion artifacts; requires expensive devices and expertise to operate the system.

NIRS (Measure of oxygenated hemoglobin)

Robust when dealing with noise (Coyle et al., 2004; Waldert et al., 2012); superior in detection of stimulation onsets and offsets (reducing the false positive commands) (Tomita et al.,

2014); precise parameter setting to extract features is not needed to detect information on the brain (Kanoh et al., 2009).

Lower temporal resolution compared to EEG (Tomita et al., 2014).

MEG (Magnetic ﬁeld)

Higher spatiotemporal resolution (Mellinger et al., 2007) than EEG; less training sessions than EEG; more robust in detectability of different frequency-band compared to EEG (Mellinger et al., 2007).

Expensive (at least 10 times more expensive than EEG cost) and non-portable; lower spatial resolution compared to fMRI; poorer localization for deeper brain structures compared to fMRI.

features can be used. For example, single-unit recording are usually converted into neuronal ﬁring rates, and EEGs are converted either into the spectral power or parameters of event related potentials. The selection of features depends on the way the user communicates with the BCI system. In the BCI design called endogenous BCI, subjects self-generate neural patterns (Nicolas-Alonso and Gomez-Gil, 2012). Alternatively, in the BCI design called exogenous BCI, neural responses are evoked by an external stimulus, and subjects modulate these responses, usually by focusing attention on relevant stimuli. Table 2 compares these two BCI types.

Endogenous BCI

Attention-Based BCIs That Utilize Neural Oscillations

Spectral analysis of EEGs recorded at diﬀerent scalp locations is commonly used to extract features for endogenous BCIs. Here, time-dependent changes in the EEG spectra for diﬀerent electrodes are detected using EEG time-frequency (TF) analysis.

For example, TF analysis can detect the occurrence of brain oscillations that result from transient synchronization of neuronal discharges over a millisecond time scale (Sanei and Chambers, 2008). This method can be applied to measure EEG changes associated with attention, such as synchronization of speciﬁc EEG bands associated with attention to an object. Attention-related synchronization of neural activity can be detected using a variety of recording methods, including singleunit recordings from brain neurons. Fries et al recorded from individual neurons in cortical area V4 while macaque monkeys attended to behaviorally relevant stimuli and ignored distractors (Fries et al., 2001). The neurons increased their gammaband synchrony while decreasing low-frequency (<17Hz) synchrony when the monkeys attended. Several studies showed attention related eﬀects in ECoGs. Rougeul-Buser and Buser recorded ECoGs in freely moving cats and observed that 10– 14Hz oscillation over sensorimotor cortex, called µ-rhythm or “expectancy rhythm,” increased when an animal actively attended

- TABLE 2 | Comparison of endogenous and exogenous BCIs and their corresponding protocols.

Category Protocol Advantages Drawbacks

Endogenous BCI - Source of the brain activity

- Frequency bands

- - Independent of any speciﬁc task
- - Useful for patients with sensory deﬁcits
- - Perfect for freely moving operations (since subjects are not instructed to stare at speciﬁc stimulus)

- - Requires several sessions of trainings
- - Some patients may not be able to communicate with BCI (BCI illiterate)
- - Low information transfer rate
- - Low signal-to-noise ratio
- - Low spatial resolution of EEG-based BCIs (harder for source localization analysis)
- - Requires many EEG electrodes

Exogenous BCI - ERP

- SSVEP

- - Low training session
- - High information transfer rate (explained in the next section)
- - Feasible with a few EEG channels
- - Higher signal-to-noise ratio

- - System failure if the subject is not attending to the stimuli
- - Fatigue in subjects (especially in SSVEP tasks due to constant ﬂickering objects)

to a place where a mouse was expected to appear (RougeulBuser and Buser, 1997). The µ-rhythm epochs were often followed by a brief 20Hz (β-range) ECoG burst. Thorpe et al reported topographical details of these ECoG patterns. Attention was associated with µ-rhythm increases over parietal regions, whereas, β-band activity increased in motor areas (Thorpe et al.,

- 2012). Daitch et al. suggested that these oscillatory patterns serve to increase functional connectivity between the areas that process relevant information while suppressing unwanted crosstalk within the neural network areas that could be caused by irrelevant stimuli (Daitch et al., 2013).

EEG studies have shown that high-frequency oscillations (>30Hz) are correlated with increased attention (Kaiser and Lutzenberger, 2005; Koelewijn et al., 2013; Musch et al., 2014). Similar results were obtained using microelectrode recordings in freely behaving monkeys (Fries et al., 2001). Attention-related oscillations can have the frequency higher than the typical γ -band range (30–80Hz) (Crone et al., 2006). Ray et al. (2008) presented human subjects with a sequence of tactile and auditory stimuli separated by pseudo-random time intervals. The tactile stimuli were delivered using a tactile stimulating cylinder, which the subjects gripped with their hands. The auditory stimuli were delivered through a headset. The subjects were instructed to attend to one of the two modalities (auditory or tactile) and respond to the attended stimulus with a button press (Ray

- et al., 2008). The attended stimuli enhanced high γ activity (80– 150Hz) in the cortical areas that processed the corresponding modality: attention to auditory stimuli activated auditory cortex, and attention to somatosensory stimuli activated somatosensory cortex. Additionally, these high-gamma oscillations occurred in PFC irrespective of the attended modality. This result is consistent with PFC being involved in the global attentional system (Dirlikov et al., 2015; Keune et al., 2015) regardless of the modalities of input information. Another study reported that attention in humans was associated with high frequency oscillations of approximately 350Hz that occurred in frontal and centro-parietal regions in response to somatosensory stimuli (Ozaki et al., 2006). Several hypotheses have been proposed to explain the role of high-frequency oscillations in attention.

One hypothesis states that low-amplitude, ultra-high frequency activity is a background neural noise that enhances neural processing (Benzi et al., 1982). For example, adding a small amount of noise to a neural circuit makes its component ﬁre more synchronous (Ward et al., 2006). Here, the performance is improved due to stochastic resonance (Benzi et al., 1982), where high-frequency noise lowers detection threshold for the relevant stimulus-. The stochastic resonance driven by γ waves can play a role in high cognitive functions (Ward et al., 2006). A similar resonance can be produced by injecting noise to the brain using electrical stimulation (Medina et al., 2012).

A number of BCIs for controlling attention have been developed based on EEG spectral bands. A recent study showed that healthy subjects can quickly learn to self-modulate their γoscillation in superior parietal cortex by alternating between the attentive and rest states (Grosse-Wentrup and Scholkopf, 2014). This BCI system correctly decoded brain state in 70.2% of cases. Several of studies on attention-based BCIs employed the ratio of power in speciﬁc spectral bands as the signal feature to be classiﬁed. This ratio was calculated as β/(α+θ) in many reports (Nagendra et al., 2015). The higher the ratio, the higher is the level of attention. Other studies used θ/β ratio (Clarke et al., 2013; Dupuy et al., 2013; Heinrich et al., 2014; Vollebregt et al., 2014b) that decreased with enhanced attention. These ratios reﬂect the fact that θ and α rhythms are stronger in drowsiness and the inattentive states; whereas, β rhythm is stronger in attentive states. For example, spectral EEG composition prior to stimulus presentation is indicative of the level of visual attention (Busch et al., 2009). Several characteristics of EEG rhythms can be also used to assess the level of attention. Instantaneous phase of EEG oscillations is one such characteristic (Busch et al., 2009). In the experiments of Busch et al. (2009), subjects were instructed to detect a brief (6ms) light ﬂash presented either at an attended or unattended location. Hit and miss rates were found to be correlated with the phase of EEG oscillations at the time of stimulus presentation. Additionally, stimuli preceded by strong α activity were less likely to be detected, an observation reported in the previous literature (Ergenoglu et al., 2004; Babiloni et al., 2006; Thut et al., 2006; Hanslmayr et al., 2007). In the other

study on the relationship between EEG phase and detection of attended and unattended stimuli, Busch and VanRullen (Busch and VanRullen, 2010) analyzed the relationship between the prestimulus EEG pattern and the EEG response to the stimulus. They found that EEG responses were higher when EEG was at a certain phase the just prior to the stimulus onset and the EEG response was the lowest for the opposite EEG phase (Busch and VanRullen, 2010). The periodicity of EEG was 100–150ms in these experiments. Several studies reported similar results (Makeig et al., 2002; Lakatos et al., 2008; Busch and VanRullen, 2010).

Exogenous BCI

Event-Related Potential (ERP) Paradigms

Event-relate potentials (ERPs) represent a compound response to a stimulus of large neuronal populations. An ERP consists of several voltage deﬂections that occur on a millisecond time scale. Speciﬁc ERP components have been linked to diﬀerent neural origins (Cohen, 2013), including the components that are associated with attention. ERP is one of the most commonly used protocols for attention studies (Wu et al., 2009; Gherri and Eimer, 2011; Jones et al., 2013; Matheson et al., 2014; Zheng et al., 2014). ERPs recorded in primary sensory areas increase when the corresponding stimulus modality is attended to Harter et al. (1984). Selection of the appropriate ERP components and scalp locations to sample is essential to achieve good performance of an ERP-based BCI. The ﬁrst ERP-based BCI was designed by Farwell and Donchin (1988). Subjects looked at a 6 × 6 matrix of alphanumeric characters. A single electrode was placed over the Pz (central-parietal) site. Subjects were instructed to attend to a speciﬁc character within the matrix while rows and columns periodically ﬂashed. Attended stimuli evoked stronger ERPs and thus could be identiﬁed. Averaging over 30 trials was required to improve the signal-to-noise ratio and assure BCI accuracy.

For better design of ERP-based BCIs, it is important to take into consideration the detailed sequence of ERPs components. The ﬁrst component is the C1-wave which is detected mostly by the posterior midline electrodes in the EEG. The onset of the C1-wave is typically 40–60ms after the stimulus with the peak at 80–100ms post-stimulus. C1 is generated in the primary visual cortex (Luck, 2014) and its polarity changes as a function of location of the stimulus in the visual ﬁeld, i.e., whether the response comes from upper or lower bank of calcarine sulcus. This change in polarity has been identiﬁed as a unique feature for C1-wave compared to other components and has been used by many studies as a marker for V1 sources. However, later neuroimaging studies challenged this view. Ales et al. (2010) used fMRI retinotopic mapping to identify the location of V1, V2, and V3 overlaid on the high-resolution structural MRI (Ales et al.,

- 2010). This technique allowed them to acquire a 3D shape of the upper and lower visual ﬁeld projection in V1 and adjacent areas, V2 and V3. Contrary to previous studies, they found that sources in V1 do not fully conform to the sign reversal. Furthermore, V2 and V3 also showed a polarity change for upper and lower ﬁeld stimuli. This suggested that the polarity inversion criterion was not a reliable method for source localization. Yet another

study challenged this conclusion. Kelly et al. claimed that C1 does initiate from V1 (Kelly et al., 2013). It has been also reported that attention is not important to generate the C1 component (Martinez et al., 1999; Fu et al., 2010). According to Martinez et al., although primary visual cortex is involved in attention, it does not serve as the locus of initial sensory gain control for attended and unattended inputs. Kelly et al. (2008) disagreed with this and proposed that attentional selection occurs at the early visual processing stage reﬂected by C1 generation in V1 (Kelly et al., 2008). In that study, target brightness and location were adjusted for each participant in order to reduce inter-subjective variability of C1. After this correction, it became clear that C1 was enhanced due to spatial attention, which indicated that this early sensory component was adjusted before the visual information arrived in V1.

The second component is the P1-wave that starts 60–90ms after the stimulus and peaks at 100–130ms. It contains an early portion generated from middle occipital gyrus and a late-portion generated more ventrally, from fusiform gyrus (Di Russo et al., 2002). P1 is sensitive to the direction of spatial attention (Hillyard and Anllo-Vento, 1998). Luck and Hillyard (1995) studied attentional modulation of P1 using a stimulus display that consisted of 14 gray items and 2 colored items (Luck and Hillyard, 1995). Subjects were instructed to report presence or absence of speciﬁc colored-item (feature detection condition) or the shape of a speciﬁc colored-item (conjunction discrimination condition). Just after the onset of the search array, a task-irrelevant stimulus appeared either at the location of relevant or irrelevant items. The irrelevant stimulus evoked larger ERPs for the relevant location compared to irrelevant location. P1-wave was present in that ERP only in the discrimination condition and not in the feature detection condition, indicating that conjunction discrimination recruited additional attentional resources. In the traditional paradigm, where subjects are instructed to pay attention to one direction and ignore the other, Mangun et al. (2001) showed that the P1 magnitude is larger for the attended compared to unattended location. The study of Mangum et al. also showed that P1 response was generated not only by the contralateral hemisphere but also by the ipsilateral one, the observation that was diﬃcult to explain in terms of redistribution of attentional resources between the hemispheres. Klimesch (2011) suggested that these results is due to inhibition eﬀect of the P1 in two diﬀerent levels. In the taskirrelevant pathways (e.g., ipsilateral hemisphere) inhibition is used to block the information processing, whereas, in the taskrelevant pathways it is used to increase the SNR by enabling precisely timed activity in neurons with high level of excitation and suppressing the neurons with low-level of excitation. It seems that the inhibition increased when an attentional demand increases to make the response to the relevant stimulus sharper.

N1-wave contains an early component generated in the frontal (140ms) and two late components between 150 and 200ms generated parietal cortex and the lateral occipital cortex, respectively (Clark and Hillyard, 1996; Luck, 2005; Ceballos and Hernandez, 2015). The magnitude of N1-potential is highly inﬂuenced by visual spatial attention (Hillyard et al., 1998). N1

is insensitive to the physical properties of the paradigm such as light intensity and the contrast. This point was clariﬁed in the experiment where a 6 × 6 matrix alphanumeric matrix (similar to Farwell and Donchin’s paradigm) could be either highcontrast or low-contrast (Shishkin et al., 2009). Although the visual stimuli were designed in a very diﬀerent contrasts, N1 characteristics between high- and low-contrast tasks remained the same. N1 is an interesting feature from two aspects: ﬁrst N1 seems to be reproduce robust feature regardless of design on the paradigm which makes it suitable to compare diﬀerent studies; second, there is no need to make detection paradigm hard to enhance N1 as it works well for clearly visible stimuli, and therefore, N1-based BCIs can be visually comfortable for ADHD subjects. This is important for ADHD subjects as they have higher tendency for fatigue or visual discomfort (Cao et al., 2014; Kooij and Bijlenga, 2014). It has been shown that about two-third of children with ADHD suﬀer from visual problems such as irritability by light (Kooij and Bijlenga, 2014). If BCIs are intended to be used on a daily basis for training and rehabilitation purposes, the rapid visual fatigue would be a great disadvantage (Sakurada et al., 2015). Therefore, presenting a paradigm with less discomfort eﬀect should enhance the endurance of patients in long-lasting training sessions and consequently increase the chance of successful therapy.

N1 properties are inﬂuenced by repetitive training which can be a potential marker for evaluating the eﬀect of neurofeedback therapy. For example, training to play a video game aﬀects N1 (Latham et al., 2013). In that study, checkerboard stimuli appeared for a short time (92ms) either in the left or right hemiﬁeld against a gray background. Subjects were instructed to respond to the ﬂash of checkerboards by pressing a button while EEG was being recorded. Participants were divided into two groups: professional video-game players (VGP) and non-professional VGP. Expert VGPs had signiﬁcantly shorter N1 latencies compared to inexperienced VGPs, and no other diﬀerence in ERP components was found between the groups.

- P2-wave, that follows N1, occurs mostly for the anterior and central electrodes. P2 is larger when the stimulus occurs relatively infrequently (oddball). From this point of view, the anterior P2 is similar to P3-wave (see below) with the diﬀerence that P2 represents simple features (e.g., color) of the stimulus, whereas P3 is related to complex stimulus features (e.g., color and shape). For posterior electrodes, P2 component is often diﬃcult to distinguish from the overlapping N1, N2, and P3 (Luck,

- 2014). P2 magnitude has been reported to diﬀer between healthy and ADHD individuals (Banaschewski et al., 2003, 2008; Broyd et al., 2005). The P2 component is associated with automatic processing and inhibition of irrelevant information (Barry et al., 2003). Studies have shown that P2 has larger amplitude and diﬀerent topographical distribution in ADHD (Banaschewski et al., 2003; Broyd et al., 2005; Barry et al., 2009; Ortega et al.,

- 2013). Therefore, P2 amplitude could be used in BCIs as an indicator for improvement scale for ADHDs.

- P3 component (also called the P300 since it peaks at 300– 500ms post-stimulus) consists of two sub-components P3a and P3b. The P3b amplitude varies between 5 and 15µV for the parietal electrodes (Soltani and Knight, 2000). It appears

following the occurrence of the oddball stimulus among a sequence of frequently repeating background stimuli. P3a, on the other hand, is distributed more in the fronto-central scalp region and peaks about 60–80ms prior to P3b for all sensory modalities. An important characteristic of P3a component is its habituation in frontal sites within 5–10 stimulus presentations; i.e., the P3a disappears when the same type of stimulus is repeatedly presented (Lynn and Eysenck, 1966; Sokolov, 1969; Friedman et al., 2001). P3b, in many publications, is simply referred to P3 or P300. It was proposed that P3 is a possible endophenotype for ADHD (Doyle et al., 2005; Szuromi et al., 2011). Patients with ADHD have signiﬁcantly lower P3 amplitude during the attention task (Szuromi et al., 2011). Szuromi et al. (2011) proposed that the P3 may be used as an ADHD marker that characterizes the deﬁcits in the level of attentional allocation and information processing. P3 magnitude has been reported to represent the eﬀort of attentional allocation, whereas, the latency of P3 indexes the processing speed of stimulus evaluation (Polich, 2007). Yet, P3 should be considered conservatively as a unique indicator for attention deﬁciency since its characteristics can be aﬀected also by other disorders such as externalizing psychopathology (substance use, conduct disorder and antisocial behavior) (Bertoletti et al., 2014; Burwell et al., 2014).

ERP-based BCIs is one of the early developed methods in the ﬁeld of BCI (Farwell and Donchin, 1988). ERP-based BCIs have a relatively low information transfer rate (ITR) or bit-rate. Bitrate in a BCI system is an index of how much information can be communicated between the brain and the computer in the time-unit (van der Waal et al., 2012). In Farwell and Donchin’s BCI, the ITR was about 12 bits min−1. Zhang et al developed a visual P300-speller BCI which was able to communicate at 20 bits min−1. BCI performance is substantially higher for visual ERPs compared to auditory (1.54 bit min−1) and tactile (7.8 bit min−1) ERPs (Furdea et al., 2009; van der Waal et al., 2012). Combination of ERP with other protocols such as steady-state visual evoked potential (SSVEP) increases the ITR up to 19.05 bit min−1 (Panicker et al., 2011).

ERP-based BCIs increase SNR by performing an ensemble averaging across several responses. Only the time-locked activities survive the averaging and irrelevant activities are canceled out. However, averaging is also considered as a drawback of ERP-based BCIs as the system has to obtain two or more ERP events to improve performance. Collecting data in multiple trials slows down the system speed. Thus, choosing this ERP-BCI method is a trade-oﬀ between the speed and accuracy of the system. Another limitation of ERP-based BCI is the acrosstrial variability in ERP amplitude and timing. The amplitude of P3 decreases if inter-trial intervals are short. To keep P3 amplitude in the standard range (10–20µV) inter-trial interval should be around 8s (Polich and Bondurant, 1997). This long interval limits BCI performance. In most experimental designs, intervals between oddball stimuli are random, which introduces ERP variability. Variability in the P3-characteristics makes it an unstable feature in attention experiments where the rigidity of ERP depend both on factors such as the designed paradigm and the mental states of the subjects.

Signal Characteristics in Steady-State Visual Evoked Potential (SSVEP) Paradigms

Another widely used BCI protocol is the SSVEP (Zhang et al., 2010; Palomares et al., 2012; Lesenfants et al., 2014; Wu and Su, 2014; Reuter et al., 2015). Visual evoked potential (VEP) is the brain responses to a visual stimulus such as light ﬂash or ﬂickering of a checker board at a speciﬁc frequency (Punsawad and Wongsawat, 2012). Presentation of a ﬂickering visual object leads to VEPs entrained to the stimulus frequency. SSVEP-based BCIs usually detect this entrained response in the EEG of the visual and parietal cortices. These BCIs achieve high SNR over a few seconds of stimulation (Dmochowski et al., 2015). In a typical SSVEP-based BCI, several objects ﬂicker at diﬀerent frequencies while the subject attends to one the object. The subject usually looks at the attended object. SSVEP-based BCIs can be easily implemented using graphical interfaces such as video games (Leins et al., 2007; Lim et al., 2010, 2012; Bakhshayesh et al.,

- 2011). SSVEP-based BCIs have good accuracy and resistance to

artifacts. As such, they can be used to build practical assistive systems for disabled users (Muller-Putz and Pfurtscheller, 2008). For example, Bin et al reported a SSVEP-based BCI that attained 95.3% accuracy and the ITR of 58 ± 9.6 bits min−1 (Bin

- et al., 2009). This is a substantially higher ITR compared to other BCI types, such as ERP-based BCIs. Muller and Hillyard

(2000) designed a paradigm in which ERPs were embedded within a ﬂicker sequence. They found that the magnitude of SSVEP and that of the N1 and N2 component of ERP varied together (positive correlation), whereas no signiﬁcant correlation was found with other ERP components (Muller and Hillyard, 2000). SSVEP paradigms usually utilize the ﬂickering frequency greater than 6Hz. In a recent study (Dreyer and Herrmann, 2015), ﬂickering frequency of up to 100 Hz was used by utilizing a novel technology. High-frequency SSVEPs are of great advantage because subjects do not perceive the ﬂicker and are not annoyed. The ﬂicker is not perceived for stimulus frequencies higher than 40Hz (Lin et al., 2012). Sakurada et al. (2015) demonstrated that using BCIs with SSVEP frequency above 50–60Hz enhanced the classiﬁcation accuracy and decreased visual fatigue (Sakurada et al., 2015). Training time is also improved, particularly in ADHD subjects, as they are less irritated by light ﬂicker (Kooij and Bijlenga,

- 2014). SSVEPs can be detected not only in awake subjects, but in

anesthetized subjects, as well. Several experiments employed the SSVEP technique in fully or partially anesthetized animals whose eyes were kept open in front of a visual display (Harnois et al., 1984; Xu et al., 2013). The ﬂicker frequency was detected from the occipital electrodes.

Harmonics of the ﬂickering frequency in some cases give a better BCI readout (Muller-Putz and Pfurtscheller, 2008; Allison et al., 2010; Ordikhani-Seyedlar et al., 2014). Müller-Putz and his colleagues reported particularly good results when they used three harmonic peaks (Muller-Putz et al., 2005). In our study (Ordikhani-Seyedlar et al., 2014) that employed a covert attention paradigm, the power of the second harmonic was higher compared to the ﬁrst harmonic. This result is in agreement with Kim et al. (2011) and others Garcia et al. (2013), Zhang et al.

(2015) who also reported that visual spatial attention modulates the second, but not the ﬁrst harmonic of the SSVEP frequency.

PROSPECTS FOR BCIs IN RESEARCH OF ATTENTION

We are witnessing a rapid development of the BCI ﬁeld. The number of peer-reviewed articles has been rapidly increasing over the past 20 years. Many of BCIs reported in the literature enable sensorimotor functions (O’Doherty et al., 2011; Iﬀt et al., 2013; Pais-Vieira et al., 2013; Yoo et al., 2013). While BCIs for cognitive functions are less developed, there has been a growing interest to such systems. In our opinion, the most important future challenges for attention-based BCIs include:

- (1) Filtering out noise: Noise can be caused by mechanical and electrical artifacts, and it can be a neural signal that is irrelevant to the function that the BCI enables and/or augments. Noise can be reduced by proper selection of features representing a brain function of interest. Choosing the right features is especially important for therapeutic BCIs because if features are selected incorrectly, unwanted functions could be enhanced instead of the desired alleviation of an individual’s disability. For instance, using the α-band to regulate attention has certain caveats. Ideally, the α-band represents suppression of irrelevant information in an attention paradigm. However, if the subject is not attending, such suppression could be confused with the drowsiness state, and the BCI would enhance drowsiness instead of working properly to enhance attention. This problem could be addressed by adding features, such as topographical information about the source of the αoscillations.
- (2) Developing of reliable criteria to quantify BCI training eﬀects: Neurofeedback therapy is usually evaluated using a comparison of speciﬁc features before and after the training. However, enhancement in EEG features does not guarantee a behavioral improvement. For example, increase in βband power is a popular feature indicating high attention level. If the aim is just to increase β-band oscillation, this frequency band might also be increased due to some other brain function unrelated to attention per se. For example, the β-band increased when motor movement had to be voluntarily suppressed in macaque monkeys (Zhang et al., 2008). Therefore, we suggest that the evaluation of neurofeedback therapy outcome should include behavioral and psychological tests to that evaluate the target function.
- (3) Accounting for intra- and inter-individual variability: Sources of variability include non-stationarity of EEG signals (Vidaurre et al., 2011) as well as non-stationarities induced by the task (Iturrate et al., 2013) and diﬀerent mental states of diﬀerent subjects. The BCI algorithms should be able to accommodate individual characteristics of subjects, and to adapt to EEG variability during the neurofeedback therapy.
- (4) Developing BCIs for individual use: current methods of NFtraining require the presence of an expert to conduct the training session from the installation of scalp electrode to running the programs and maintaining the system. These

procedures impose restrictions on the usage of BCIs by patients. More user-friendly, highly automated BCIs should be developed in the future.

## CONCLUSIONS

BCIs oﬀer exciting opportunities for enhancing neural functions and developing therapies for neural disabilities, including BCIs that assist subject to regulate their neural function. Attention is a fundamental brain mechanism for selection of relevant and essential information while suppressing irrelevant signals. Disorders of this mechanism result in dysfunctions, such as ADHD. BCIs hold promise to provide eﬀective rehabilitation strategies for individuals with impairments of attention. Several attention-based BCIs have been already developed whereas many challenges still remain. The main challenge is to combine highly technical knowledge needed to build eﬀective BCIs with the

expertise from neuroscience and psychology. Merging these multidisciplinary contributions is key to developing clinically relevant BCIs to treat attentional dysfunctions.

## AUTHOR CONTRIBUTIONS

MO, ML: wrote the paper; HS, SP: edited the paper.

## ACKNOWLEDGMENTS

The authors gratefully appreciate Karoline B. Doser for her valuable comments on the manuscript and Dr. Sean Bowen for editorial assistance on an earlier version of this manuscript. The original project was supported by the Department of Electrical Engineering (Biomedical Engineering) at the Technical University of Denmark (DTU), the Lundbeck Foundation and Radiometer.

## REFERENCES

Ahn, M., Ahn, S., Hong, J. H., Cho, H., Kim, K., Kim, B. S., et al. (2013). Gamma band activity associated with BCI performance: simultaneous MEG/EEG study. Front. Hum. Neurosci. 7:848. doi: 10.3389/fnhum.2013. 00848

Ales, J. M., Yates, J. L., and Norcia, A. M. (2010). V1 is not uniquely identiﬁed by polarity reversals of responses to upper and lower visual ﬁeld stimuli. Neuroimage 52, 1401–1409. doi: 10.1016/j.neuroimage.2010.05.016

Allison, B. Z., Brunner, C., Kaiser, V., Müller-Putz, G. R., Neuper, C., and Pfurtscheller, G. (2010). Toward a hybrid brain-computer interface based on imagined movement and visual attention. J. Neural Eng. 7, 1–9. doi: 10.1088/1741-2560/7/2/026007

Arns, M., de Ridder, S., Strehl, U., Breteler, M., and Coenen, A. (2009). Eﬃcacy of neurofeedback treatment in ADHD: the eﬀects on inattention, impulsivity and hyperactivity: a meta-analysis. Clin. EEG Neurosci. 40, 180–189. doi: 10.1177/155005940904000311

Arns, M., Feddema, I., and Kenemans, J. L. (2014). Diﬀerential eﬀects of theta/beta and SMR neurofeedback in ADHD on sleep onset latency. Front. Hum. Neurosci. 8:1019. doi: 10.3389/fnhum.2014.01019

Avisar, A., and Shalev, L. (2011). Sustained attention and behavioral characteristics associated with ADHD in adults. Appl. Neuropsychol. 18, 107–116. doi: 10.1080/09084282.2010.547777

Babiloni, C., Brancucci, A., Del Percio, C., Capotosto, P., Arendt-Nielsen, L., Chen, A. C., et al. (2006). Anticipatory electroencephalography alpha rhythm predicts subjective perception of pain intensity. J. Pain 7, 709–717. doi: 10.1016/j.jpain.2006.03.005

Bakhshayesh, A. R., Hansch, S., Wyschkon, A., Rezai, M. J., and Esser, G. (2011). Neurofeedback in ADHD: a single-blind randomized controlled trial. Eur. Child Adolesc. Psychiatry 20, 481–491. doi: 10.1007/s00787-011-0208-y

Ball, T., Kern, M., Mutschler, I., Aertsen, A., and Schulze-Bonhage, A. (2009). Signal quality of simultaneously recorded invasive and non-invasive EEG. NeuroImage 46, 708–716. doi: 10.1016/j.neuroimage.2009.02.028

Bamdadian, A., Guan, C., Ang, K. K., and Xu, J. (2014). The predictive role of pre-cue EEG rhythms on MI-based BCI classiﬁcation performance. J. Neurosci. Methods 235, 138–144. doi: 10.1016/j.jneumeth.2014.06.011

Banaschewski, T., Brandeis, D., Heinrich, H., Albrecht, B., Brunner, E., and Rothenberger, A. (2003). Association of ADHD and conduct disorder–brain electrical evidence for the existence of a distinct subtype. J. Child Psychol. Psychiatry 44, 356–376. doi: 10.1111/1469-7610.00127

Banaschewski, T., Yordanova, J., Kolev, V., Heinrich, H., Albrecht, B., and Rothenberger, A. (2008). Stimulus context and motor preparation in attention-deﬁcit/hyperactivity disorder. Biol. Psychol. 77, 53–62. doi: 10.1016/j.biopsycho.2007.09.003

Barry, R. J., Clarke, A. R., McCarthy, R., Selikowitz, M., Brown, C. R., and Heaven, P. C. (2009). Event-related potentials in adults with AttentionDeﬁcit/Hyperactivity Disorder: an investigation using an inter-modal

auditory/visual oddball task. Int. J. Psychophysiol. 71, 124–131. doi: 10.1016/j.ijpsycho.2008.09.009

Barry, R. J., Johnstone, S. J., and Clarke, A. R. (2003). A review of electrophysiology in attention-deﬁcit/hyperactivity disorder: II. Event-related potentials. Clin. Neurophysiol. 114, 184–198. doi: 10.1016/S1388-2457(02)00363-2

Benzi, R., Parisi, G., Sutera, A., and Vulpiani, A. (1982). Stochastic resonance in climatic change. Tellus 34, 10–16. doi: 10.1111/j.2153-3490.1982.tb01787.x Bertoletti, E., Michelini, G., Moruzzi, S., Ferrer, G., Ferini-Strambi, L., Stazi, M. A., et al. (2014). A general population twin study of conduct problems and the auditory P300 waveform. J. Abnorm. Child Psychol. 42, 861–869. doi: 10.1007/s10802-013-9836-7

Bianchi, L., Sami, S., Hillebrand, A., Fawcett, I. P., Quitadamo, L. R., and Seri, S. (2010). Which physiological components are more suitable for visual ERP based brain-computer interface? A preliminary MEG/EEG study. Brain Topogr. 23, 180–185. doi: 10.1007/s10548-010-0143-0

Biederman, J., Mick, E., and Faraone, S. V. (2000). Age-dependent decline of symptoms of attention deﬁcit hyperactivity disorder: impact of remission deﬁnition and symptom type. Am. J. Psychiatry 157, 816–818. doi: 10.1176/appi.ajp.157.5.816

Bin, G., Gao, X., Wang, Y., Hong, B., and Gao, S. (2009). VEP-based braincomputer interfaces: time, frequency, and code modulations. IEEE Comput. Intell. Mag. 4, 22–26. doi: 10.1109/MCI.2009.934562

Brosch, T., Pourtois, G., Sander, D., and Vuilleumier, P. (2011). Additive eﬀects of emotional, endogenous, and exogenous attention: behavioral and electrophysiological evidence. Neuropsychologia 49, 1779–1787. doi: 10.1016/j.neuropsychologia.2011.02.056

Broyd, S. J., Johnstone, S. J., Barry, R. J., Clarke, A. R., McCarthy, R., Selikowitz, M., et al. (2005). The eﬀect of methylphenidate on response inhibition and the event-related potential of children with attention deﬁcit/hyperactivity disorder. Int. J. Psychophysiol. 58, 47–58. doi: 10.1016/j.ijpsycho.2005.03.008

Bruhl, A. B. (2015). Making sense of real-time functional magnetic resonance imaging (rtfMRI) and rtfMRI neurofeedback. Int. J. Neuropsychopharmacol. 18:pyv020. doi: 10.1093/ijnp/pyv020

Burwell, S. J., Malone, S. M., Bernat, E. M., and Iacono, W. G. (2014). Does electroencephalogram phase variability account for reduced P3 brain potential in externalizing disorders? Clin. Neurophysiol. 125, 2007–2015. doi: 10.1016/j.clinph.2014.02.020

Busch, N. A., Dubois, J., and VanRullen, R. (2009). The phase of ongoing EEG oscillations predicts visual perception. J. Neurosci. 29, 7869–7876. doi: 10.1523/JNEUROSCI.0113-09.2009

Busch, N. A., and VanRullen, R. (2010). Spontaneous EEG oscillations reveal periodic sampling of visual attention. Proc. Natl. Acad. Sci. U.S.A. 107, 16048–16053. doi: 10.1073/pnas.1004801107

Busse, L., Katzner, S., and Treue, S. (2008). Temporal dynamics of neuronal modulation during exogenous and endogenous shifts of visual attention in macaque area MT. Proc. Natl. Acad. Sci. U.S.A. 105, 16380–16385. doi: 10.1073/pnas.0707369105

Cao, T., Wan, F., Wong, C. M., da Cruz, J. N., and Hu, Y. (2014). Objective evaluation of fatigue by EEG spectral analysis in steady-state visual evoked potential-based brain-computer interfaces. Biomed. Eng. Online 13:28. doi: 10.1186/1475-925x-13-28

Carmena, J. M., Lebedev, M. A., Crist, R. E., O’Doherty, J. E., Santucci, D. M., Dimitrov, D. F., et al. (2003). Learning to control a brain-machine interface for reaching and grasping by primates. PLoS Biol. 1:E42. doi: 10.1371/journal.pbio. 0000042

Ceballos, G. A., and Hernandez, L. F. (2015). Non-target adjacent stimuli classiﬁcation improves performance of classical ERP-based brain computer interface. J. Neural Eng. 12:026009. doi: 10.1088/1741-2560/12/2/026009

Christiansen, H., Reh, V., Schmidt, M. H., and Rief, W. (2014). Slow cortical potential neurofeedback and self-management training in outpatient care for children with ADHD: study protocol and ﬁrst preliminary results of a randomized controlled trial. Front. Hum. Neurosci. 8:943. doi: 10.3389/fnhum.2014.00943

Clark, V. P., and Hillyard, S. A. (1996). Spatial selective attention aﬀects early extrastriate but not striate components of the visual evoked potential. J. Cogn. Neurosci. 8, 387–402. doi: 10.1162/jocn.1996.8.5.387

Clarke, A. R., Barry, R. J., Dupuy, F. E., McCarthy, R., Selikowitz, M., and Johnstone, S. J. (2013). Excess beta activity in the EEG of children with attention-deﬁcit/hyperactivity disorder: a disorder of arousal? Int. J. Psychophysiol. 89, 314–319. doi: 10.1016/j.ijpsycho.2013.04.009

Cohen, M. X. (ed.). (2013). “Overview of time-domain EEG analyses,” in Analyzing Neural Time Series Data: Theory and Practice (London: MIT Press), 97–106. Conners, C. K., Epstein, J. N., March, J. S., Angold, A., Wells, K. C., Klaric, J., et al. (2001). Multimodal treatment of ADHD in the MTA: an alternative outcome analysis. J. Am. Acad. Child Adolesc. Psychiatry 40, 159–167. doi: 10.1097/00004583-200102000-00010

Corbetta, M., Patel, G., and Shulman, G. L. (2008). The reorienting system of the human brain: from environment to theory of mind. Neuron 58, 306–324. doi: 10.1016/j.neuron.2008.04.017

Coyle, S., Ward, T., Markham, C., and McDarby, G. (2004). On the suitability of near-infrared (NIR) systems for next-generation brain-computer interfaces. Physiol. Meas. 25, 815–822. doi: 10.1088/0967-3334/25/4/003

Crone, N. E., Sinai, A., and Korzeniewska, A. (2006). High-frequency gamma oscillations and human brain mapping with electrocorticography. Prog. Brain Res. 159, 275–295. doi: 10.1016/S0079-6123(06)59019-3

Daitch, A. L., Sharma, M., Roland, J. L., Astaﬁev, S. V., Bundy, D. T., Gaona, C. M., et al. (2013). Frequency-speciﬁc mechanism links human brain networks for spatial attention. Proc. Natl. Acad. Sci. U.S.A. 110, 19585–19590. doi: 10.1073/pnas.1307947110

deCharms, R. C., Maeda, F., Glover, G. H., Ludlow, D., Pauly, J. M., Soneji, D., et al. (2005). Control over brain activation and pain learned by using realtime functional MRI. Proc. Natl. Acad. Sci. U.S.A. 102, 18626–18631. doi: 10.1073/pnas.0505210102

de Haan, B., Morgan, P. S., and Rorden, C. (2008). Covert orienting of attention and overt eye movements activate identical brain regions. Brain Res. 1204, 102–111. doi: 10.1016/j.brainres.2008.01.105

Desimone, R., and Duncan, J. (1995). Neural mechanisms of selective visual attention. Annu. Rev. Neurosci. 18, 193–222. doi: 10.1146/annurev.ne.18. 030195.001205

De Vos, M., Kroesen, M., Emkes, R., and Debener, S. (2014). P300 speller BCI with a mobile EEG system: comparison to a traditional ampliﬁer. J. Neural Eng. 11:036008. doi: 10.1088/1741-2560/11/3/036008

Dirlikov, B., Shiels Rosch, K., Crocetti, D., Denckla, M. B., Mahone, E. M., and Mostofsky, S. H. (2015). Distinct frontal lobe morphology in girls and boys with ADHD. Neuroimage Clin. 7, 222–229. doi: 10.1016/j.nicl.2014.12.010

Di Russo, F., Martinez, A., Sereno, M. I., Pitzalis, S., and Hillyard, S. A. (2002). Cortical sources of the early components of the visual evoked potential. Hum. Brain Mapp. 15, 95–111. doi: 10.1002/hbm.10010

Dmochowski, J. P., Greaves, A. S., and Norcia, A. M. (2015). Maximally reliable spatial ﬁltering of steady state visual evoked potentials. Neuroimage 109, 63–72. doi: 10.1016/j.neuroimage.2014.12.078

Dobkin, B. H. (2007). Brain-computer interface technology as a tool to augment plasticity and outcomes for neurological rehabilitation. J. Physiol. 579, 637–642. doi: 10.1113/jphysiol.2006.123067

Donoghue, J. P., Nurmikko, A., Friehs, G., and Black, M. (2004). Development of neuromotor prostheses for humans. Suppl. Clin. Neurophysiol. 57, 592–606. doi: 10.1016/S1567-424X(09)70399-X

Doyle, A. E., Willcutt, E. G., Seidman, L. J., Biederman, J., Chouinard, V. A., Silva, J., et al. (2005). Attention-deﬁcit/hyperactivity disorder endophenotypes. Biol. Psychiatry 57, 1324–1335. doi: 10.1016/j.biopsych.2005.03.015

Dreyer, A. M., and Herrmann, C. S. (2015). Frequency-modulated steady-state visual evoked potentials: a new stimulation method for brain-computer interfaces. J. Neurosci. Methods 241, 1–9. doi: 10.1016/j.jneumeth.2014.12.004

Dupuy, F. E., Clarke, A. R., Barry, R. J., McCarthy, R., and Selikowitz, M. (2013). EEG diﬀerences between the combined and inattentive types of attention-deﬁcit/hyperactivity disorder in girls: a further investigation. Clin. EEG Neurosci. 45, 231–237. doi: 10.1177/1550059413501162

Egeth, H. E., and Yantis, S. (1997). Visual attention: control, representation, and time course. Annu. Rev. Psychol. 48, 269–297. doi: 10.1146/annurev.psych.48. 1.269

Elbert, T., Rockstroh, B., Lutzenberger, W., and Birbaumer, N. (1980). Biofeedback of slow cortical potentials. I. Electroencephalogr. Clin. Neurophysiol. 48, 293–301. doi: 10.1016/0013-4694(80)90265-5

Ergenoglu, T., Demiralp, T., Bayraktaroglu, Z., Ergen, M., Beydagi, H., and Uresin, Y. (2004). Alpha rhythm of the EEG modulates visual detection performance in humans. Brain Res. Cogn. Brain Res. 20, 376–383. doi: 10.1016/j.cogbrainres.2004.03.009

Escolano, C., Navarro-Gil, M., Garcia-Campayo, J., Congedo, M., and Minguez, J. (2014). The eﬀects of individual upper alpha neurofeedback in ADHD: an open-label pilot study. Appl. Psychophysiol. Biofeedback 39, 193–202. doi: 10.1007/s10484-014-9257-6

Fan, J., McCandliss, B. D., Fossella, J., Flombaum, J. I., and Posner, M. I.

(2005). The activation of attentional networks. Neuroimage 26, 471–479. doi: 10.1016/j.neuroimage.2005.02.004

Faraone, S. V., Biederman, J., and Mick, E. (2006). The age-dependent decline of attention deﬁcit hyperactivity disorder: a meta-analysis of follow-up studies. Psychol. Med. 36, 159–165. doi: 10.1017/S003329170500471X

Farwell, L. A., and Donchin, E. (1988). Talking oﬀ the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523. doi: 10.1016/0013-4694(88)90149-6

Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Muller, K. R., et al. (2012). Enhanced performance by a hybrid NIRS-EEG brain computer interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084

Ferrier, D. (1876). The Function of the Brain. London: Smith, Elder & Co. Fleming, A. P., and McMahon, R. J. (2012). Developmental context and treatment

principles for ADHD among college students. Clin. Child Fam. Psychol. Rev. 15, 303–329. doi: 10.1007/s10567-012-0121-z

Freeman, W. J., Holmes, M. D., Burke, B. C., and Vanhatalo, S. (2003). Spatial spectra of scalp EEG and EMG from awake humans. Clin. Neurophysiol. 114, 1053–1068. doi: 10.1016/S1388-2457(03)00045-2

Freeman, W. J., Rogers, L. J., Holmes, M. D., and Silbergeld, D. L. (2000). Spatial spectral analysis of human electrocorticograms including the alpha and gamma bands. J. Neurosci. Methods 95, 111–121. doi: 10.1016/S0165-0270(99) 00160-0

Friedman, D., Cycowicz, Y. M., and Gaeta, H. (2001). The novelty P3: an event-related brain potential (ERP) sign of the brain’s evaluation of novelty. Neurosci. Biobehav. Rev. 25, 355–373. doi: 10.1016/S0149-7634(01) 00019-7

Fries, P., Reynolds, J. H., Rorie, A. E., and Desimone, R. (2001). Modulation of oscillatory neuronal synchronization by selective visual attention. Science 291, 1560–1563. doi: 10.1126/science.1055465

Fu, K. M., Foxe, J. J., Murray, M. M., Higgins, B. A., Javitt, D. C., and Schroeder, C. E. (2001). Attention-dependent suppression of distracter visual input can be cross-modally cued as indexed by anticipatory parieto-occipital alpha-band oscillations. Brain Res. Cogn. Brain Res. 12, 145–152. doi: 10.1016/S09266410(01)00034-9

Fu, S., Fedota, J. R., Greenwood, P. M., and Parasuraman, R. (2010). Dissociation of visual C1 and P1 components as a function of attentional load: an event-related potential study. Biol. Psychol. 85, 171–178. doi: 10.1016/j.biopsycho.2010.06.008

Furdea, A., Halder, S., Krusienski, D. J., Bross, D., Nijboer, F., Birbaumer, N., et al. (2009). An auditory oddball (P300). spelling system for braincomputer interfaces. Psychophysiology 46, 617–625. doi: 10.1111/j.14698986.2008.00783.x

Garcia, J. O., Srinivasan, R., and Serences, J. T. (2013). Near-real-time featureselective modulations in human cortex. Curr. Biol. 23, 515–522. doi: 10.1016/j.cub.2013.02.013

Gevensleben, H., Holl, B., Albrecht, B., Vogel, C., Schlamp, D., Kratz, O., et al. (2009). Is neurofeedback an eﬃcacious treatment for ADHD? A randomised controlled clinical trial. J. Child Psychol. Psychiatry 50, 780–789. doi: 10.1111/j.1469-7610.2008.02033.x

Gevensleben, H., Moll, G. H., Rothenberger, A., and Heinrich, H. (2014). Neurofeedback in attention-deﬁcit/hyperactivity disorder - diﬀerent models, diﬀerent ways of application. Front. Hum. Neurosci. 8:846. doi: 10.3389/fnhum.2014.00846

Gherri, E., and Eimer, M. (2011). Active listening impairs visual perception and selectivity: an ERP study of auditory dual-task costs on visual attention. J. Cogn. Neurosci. 23, 832–844. doi: 10.1162/jocn.2010.21468

Golla, H., Thier, P., and Haarmeier, T. (2005). Disturbed overt but normal covert shifts of attention in adult cerebellar patients. Brain 128, 1525–1535. doi: 10.1093/brain/awh523

Gomes, H., Duﬀ, M., Ramos, M., Molholm, S., Foxe, J. J., and Halperin, J. (2012). Auditory selective attention and processing in children with attention-deﬁcit/hyperactivity disorder. Clin. Neurophysiol. 123, 293–302. doi: 10.1016/j.clinph.2011.07.030

Greenhill, L. L., Swanson, J. M., Vitiello, B., Davies, M., Clevenger, W., Wu, M., et al. (2001). Impairment and deportment responses to diﬀerent methylphenidate doses in children with ADHD: the MTA titration trial. J. Am. Acad. Child Adolesc. Psychiatry 40, 180–187. doi: 10.1097/00004583200102000-00012

Grosse-Wentrup, M., and Scholkopf, B. (2014). A brain-computer interface based on self-regulation of gamma-oscillations in the superior parietal cortex. J. Neural Eng. 11:056015. doi: 10.1088/1741-2560/11/5/056015

Hanslmayr, S., Aslan, A., Staudigl, T., Klimesch, W., Herrmann, C. S., and Bauml, K. H. (2007). Prestimulus oscillations predict visual perception performance between and within subjects. Neuroimage 37, 1465–1473. doi: 10.1016/j.neuroimage.2007.07.011

Harnois, C., Bodis-Wollner, I., and Onofrj, M. (1984). The eﬀect of contrast and spatial frequency on the visual evoked potential of the hooded rat. Exp. Brain Res. 57, 1–8. doi: 10.1007/BF00231126

Harter, M. R., Aine, C., and Schroeder, C. (1984). Hemispheric diﬀerences in event-related potential measures of selective attention. Ann. N.Y. Acad. Sci. 425, 210–211. doi: 10.1111/j.1749-6632.1984.tb23535.x

He, N., Li, F., Li, Y., Guo, L., Chen, L., Huang, X., et al. (2015). Neuroanatomical deﬁcits correlate with executive dysfunction in boys with attention deﬁcit hyperactivity disorder. Neurosci. Lett. 600, 45–49. doi: 10.1016/j.neulet.2015.05.062

Heinrich, H., Busch, K., Studer, P., Erbe, K., Moll, G. H., and Kratz, O. (2014). EEG spectral analysis of attention in ADHD: implications for neurofeedback training? Front. Hum. Neurosci. 8:611. doi: 10.3389/fnhum.2014.00611

Hillard, B., El-Baz, A. S., Sears, L., Tasman, A., and Sokhadze, E. M. (2013). Neurofeedback training aimed to improve focused attention and alertness in children with ADHD: a study of relative power of EEG rhythms using custom-made software application. Clin. EEG Neurosci. 44, 193–202. doi: 10.1177/1550059412458262

Hillyard, S. A., and Anllo-Vento, L. (1998). Event-related brain potentials in the study of visual selective attention. Proc. Natl. Acad. Sci. U.S.A. 95, 781–787. doi: 10.1073/pnas.95.3.781

Hillyard, S. A., Vogel, E. K., and Luck, S. J. (1998). Sensory gain control (ampliﬁcation) as a mechanism of selective attention: electrophysiological and neuroimaging evidence. Philos. Trans. R. Soc. Lond. B. Biol. Sci. 353, 1257–1270. doi: 10.1098/rstb.1998.0281

Holtmann, M., Pniewski, B., Wachtlin, D., Worz, S., and Strehl, U. (2014a). Neurofeedback in children with attention-deﬁcit/hyperactivity disorder (ADHD)–a controlled multicenter study of a non-pharmacological treatment approach. BMC Pediatr. 14:202. doi: 10.1186/1471-2431-14-202

Holtmann, M., Sonuga-Barke, E., Cortese, S., and Brandeis, D. (2014b). Neurofeedback for ADHD: a review of current evidence. Child Adolesc. Psychiatr. Clin. N. Am. 23, 789–806. doi: 10.1016/j.chc.2014.05.006

Iﬀt, P. J., Shokur, S., Li, Z., Lebedev, M. A., and Nicolelis, M. A. (2013). A brainmachine interface enables bimanual arm movements in monkeys. Sci. Transl. Med. 5, 210ra154. doi: 10.1126/scitranslmed.3006159

Ignashchenkova, A., Dicke, P. W., Haarmeier, T., and Their, P. (2004). Neuronspeciﬁc contribution of the superior colliculus to overt and covert shifts of attention. Nat. Neurosci. 7, 56–64. doi: 10.1038/nn1169

Iturrate, I., Montesano, L., and Minguez, J. (2013). Shared-control braincomputer interface for a two dimensional reaching task using EEG errorrelated potentials. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2013, 5258–5262. doi: 10.1109/embc.2013.6610735

Jones, A., Hughes, G., and Waszak, F. (2013). The interaction between attention and motor prediction. An ERP study. Neuroimage 83, 533–541. doi: 10.1016/j.neuroimage.2013.07.004

Jonkman, L. M., Kenemans, J. L., Kemner, C., Verbaten, M. N., and van Engeland, H. (2004). Dipole source localization of event-related brain activity indicative of an early visual selective attention deﬁcit in ADHD children. Clin. Neurophysiol. 115, 1537–1549. doi: 10.1016/j.clinph.2004.01.022

Kahana, M. J. (2006). The cognitive correlates of human brain oscillations. J. Neurosci. 26, 1669–1672. doi: 10.1523/JNEUROSCI.3737-05c.2006

Kaiser, J., and Lutzenberger, W. (2005). Human gamma-band activity: a window to cognitive processing. Neuroreport 16, 207–211. doi: 10.1097/00001756200502280-00001

Kanoh, S., Murayama, Y. M., Miyamoto, K., Yoshinobu, T., and Kawashima, R. (2009). A NIRS-based brain-computer interface system during motor imagery: system development and online feedback training. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2009, 594–597. doi: 10.1109/IEMBS.2009.5333710

Kashihara, K. (2014). A brain-computer interface for potential non-verbal facial communication based on EEG signals related to speciﬁc emotions. Front. Neurosci. 8:244. doi: 10.3389/fnins.2014.00244

Kelly, S. P., Gomez-Ramirez, M., and Foxe, J. J. (2008). Spatial attention modulates initial aﬀerent activity in human primary visual cortex. Cereb. Cortex 18, 2629–2636. doi: 10.1093/cercor/bhn022

Kelly, S. P., Schroeder, C. E., and Lalor, E. C. (2013). What does polarity inversion of extrastriate activity tell us about striate contributions to the early VEP? A comment on Ales et al. (2010). Neuroimage 76, 442–445. doi: 10.1016/j.neuroimage.2012.03.081

Keune, P. M., Wiedemann, E., Schneidt, A., and Schonenberg, M. (2015). Frontal brain asymmetry in adult attention-deﬁcit/hyperactivity disorder (ADHD): extending the motivational dysfunction hypothesis. Clin. Neurophysiol. 126, 711–720. doi: 10.1016/j.clinph.2014.07.008

Khan, M. J., Hong, M. J., and Hong, K. S. (2014). Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface. Front. Hum. Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244

Kim, Y. J., Grabowecky, M., Paller, K. A., and Suzuki, S. (2011). Diﬀerential roles of frequency-following and frequency-doubling visual responses revealed by evoked neural harmonics. J. Cogn. Neurosci. 23, 1875–1886. doi: 10.1162/jocn.2010.21536

Klimesch, W. (2011). Evoked alpha and early access to the knowledge system: the P1 inhibition timing hypothesis. Brain Res. 1408, 52–71. doi: 10.1016/j.brainres.2011.06.003

Koelewijn, L., Rich, A. N., Muthukumaraswamy, S. D., and Singh, K. D. (2013). Spatial attention increases high-frequency gamma synchronisation in human medial visual cortex. Neuroimage 79, 295–303. doi: 10.1016/j.neuroimage.2013. 04.108

Kollins, S. H. (2008). ADHD, substance use disorders, and psychostimulant treatment: current literature and treatment guidelines. J. Atten. Disord. 12, 115–125. doi: 10.1177/1087054707311654

Kooij, J. J., and Bijlenga, D. (2014). High prevalence of self-reported photophobia in adult ADHD. Front. Neurol. 5:256. doi: 10.3389/fneur.2014.00256

Kus, R., Duszyk, A., Milanowski, P., Labecki, M., Bierzynska, M., Radzikowska, Z., et al. (2013). On the quantiﬁcation of SSVEP frequency responses in human EEG in realistic BCI conditions. PLoS ONE 8:e77536. doi: 10.1371/journal.pone.0077536

Lakatos, P., Karmos, G., Mehta, A. D., Ulbert, I., and Schroeder, C. E. (2008). Entrainment of neuronal oscillations as a mechanism of attentional selection. Science 320, 110–113. doi: 10.1126/science.1154735

Latham, A. J., Patston, L. L., Westermann, C., Kirk, I. J., and Tippett, L. J. (2013). Earlier visual N1 latencies in expert video-game players: a temporal basis of enhanced visuospatial performance? PLoS ONE 8:e75231. doi: 10.1371/journal.pone.0075231

Lebedev, M. A. (2014). How to read neuron-dropping curves? Front. Syst. Neurosci. 8:102. doi: 10.3389/fnsys.2014.00102

Lebedev, M. A., Carmena, J. M., O’Doherty, J. E., Zacksenhouse, M., Henriquez, C. S., Principe, J. C., et al. (2005). Cortical ensemble adaptation to represent

velocity of an artiﬁcial actuator controlled by a brain-machine interface. J. Neurosci. 25, 4681–4693. doi: 10.1523/JNEUROSCI.4088-04.2005

Lebedev, M. A., Messinger, A., Kralik, J. D., and Wise, S. P. (2004). Representation of attended versus remembered locations in prefrontal cortex. PLoS Biol. 2:e365. doi: 10.1371/journal.pbio.0020365

Lebedev, M. A., and Nicolelis, M. A. (2006). Brain-machine interfaces: past, present and future. Trends Neurosci. 29, 536–546. doi: 10.1016/j.tins.2006.07.004

Lebedev, M. A., Tate, A. J., Hanson, T. L., Li, Z., O’Doherty, J. E., Winans, J. A., et al. (2011). Future developments in brain-machine interface research. Clinics 66(Suppl. 1), 25–32. doi: 10.1590/s1807-59322011001300004

Lebedev, M. A., and Wise, S. P. (2001). Tuning for the orientation of spatial attention in dorsal premotor cortex. Eur. J. Neurosci. 13, 1002–1008. doi: 10.1046/j.0953-816x.2001.01457.x

Lee, J. H., Ryu, J., Jolesz, F. A., Cho, Z. H., and Yoo, S. S. (2009). Brain-machine interface via real-time fMRI: preliminary study on thought-controlled robotic arm. Neurosci. Lett. 450, 1–6. doi: 10.1016/j.neulet.2008.11.024

Leins, U., Goth, G., Hinterberger, T., Klinger, C., Rumpf, N., and Strehl, U. (2007). Neurofeedback for children with ADHD: a comparison of SCP and Theta/Beta protocols. Appl. Psychophysiol. Biofeedback 32, 73–88. doi: 10.1007/s10484-0079031-0

Lesenfants, D., Habbal, D., Lugo, Z., Lebeau, M., Horki, P., Amico, E., et al.

(2014). An independent SSVEP-based brain-computer interface in locked-in syndrome. J. Neural Eng. 11:035002. doi: 10.1088/1741-2560/11/3/035002

Leuthardt, E. C., Freudenberg, Z., Bundy, D., and Roland, J. (2009). Microscale recording from human motor cortex: implications for minimally invasive electrocorticographic brain-computer interfaces. Neurosurg. Focus 27:E10. doi: 10.3171/2009.4.FOCUS0980

Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., and Moran, D. W. (2004). A brain-computer interface using electrocorticographic signals in humans. J. Neural Eng. 1, 63–71. doi: 10.1088/1741-2560/1/2/001

Lim, C. G., Lee, T. S., Guan, C., Fung, D. S., Zhao, Y., Teng, S. S., et al. (2012). A brain-computer interface based attention training program for treating attention deﬁcit hyperactivity disorder. PLoS ONE 7:e46692. doi: 10.1371/journal.pone.0046692

Lim, C. G., Lee, T. S., Guan, C., Sheng Fung, D. S., Cheung, Y. B., Teng, S. S., et al.

(2010). Eﬀectiveness of a brain-computer interface based programme for the treatment of ADHD: a pilot study. Psychopharmacol. Bull. 43, 73–82.

Lin, F. C., Zao, J. K., Tu, K. C., Wang, Y., Huang, Y. P., Chuang, C. W., et al. (2012). SNR analysis of high-frequency steady-state visual evoked potentials from the foveal and extrafoveal regions of human retina. Conf. Proc. IEEE. Eng. Med. Biol. Soc. 2012, 1810–1814. doi: 10.1109/EMBC.2012.6346302

Lofthouse, N., Arnold, L. E., Hersch, S., Hurt, E., and DeBeus, R. (2012a). A review of neurofeedback treatment for pediatric ADHD. J. Atten. Disord. 16, 351–372. doi: 10.1177/1087054711427530

Lofthouse, N., Arnold, L. E., and Hurt, E. (2012b). Current status of neurofeedback for attention-deﬁcit/hyperactivity disorder. Curr. Psychiatry Rep. 14, 536–542. doi: 10.1007/s11920-012-0301-z

Logothetis, N. K. (2003). MR imaging in the non-human primate: studies of function and of dynamic connectivity. Curr. Opin. Neurobiol. 13, 630–642. doi: 10.1016/j.conb.2003.09.017

Luck, S. J. (2005). An Introduction to the Event-Related Potential Technique. Cambridge, MA: MIT.

Luck, S. J. (ed.). (2014). “Overview of common ERP components” in An Introduction to the Event-Related Potential Technique (London: MIT Press), 71–118.

Luck, S. J., and Hillyard, S. A. (1995). The role of attention in feature detection and conjunction discrimination: an electrophysiological analysis. Int. J. Neurosci. 80, 281–297. doi: 10.3109/00207459508986105

Lutzenberger, W., Elbert, T., Rockstroh, B., and Birbaumer, N. (1980). Biofeedback of slow cortical potentials. II. Analysis of single event-related slow potentials by time series analysis. Electroencephalogr. Clin. Neurophysiol. 48, 302–311. doi: 10.1016/0013-4694(80)90266-7

Lynn, R., and Eysenck, H. J. (1966). Attention, Arousal and the Orientation Reaction: International Series of Monographs in Experimental Psychology. Oxford: Pergamon Press.

Makeig, S., Westerﬁeld, M., Jung, T. P., Enghoﬀ, S., Townsend, J., Courchesne, E., et al. (2002). Dynamic brain sources of visual evoked responses. Science 295, 690–694. doi: 10.1126/science.1066168

Mangun, G. R., Hinrichs, H., Scholz, M., Mueller-Gaertner, H. W., Herzog, H., Krause, B. J., et al. (2001). Integrating electrophysiology and neuroimaging

of spatial selective attention to simple isolated visual stimuli. Vision Res. 41, 1423–1435. doi: 10.1016/S0042-6989(01)00046-3

Margalit, E., Weiland, J. D., Clatterbuck, R. E., Fujii, G. Y., Maia, M., Tameesh, M., et al. (2003). Visual and electrical evoked response recorded from subdural electrodes implanted above the visual cortex in normal dogs under two methods of anesthesia. J. Neurosci. Methods 123, 129–137. doi: 10.1016/S01650270(02)00345X

Martinez, A., Anllo-Vento, L., Sereno, M. I., Frank, L. R., Buxton, R. B., Dubowitz, D. J., et al. (1999). Involvement of striate and extrastriate visual cortical areas in spatial attention. Nat. Neurosci. 2, 364–369. doi: 10.1038/7274

Matheson, H., Newman, A. J., Satel, J., and McMullen, P. (2014). Handles of manipulable objects attract covert visual attention: ERP evidence. Brain Cogn. 86, 17–23. doi: 10.1016/j.bandc.2014.01.013

Medina, L. E., Lebedev, M. A., O’Doherty, J. E., and Nicolelis, M. A. (2012). Stochastic facilitation of artiﬁcial tactile sensation in primates. J. Neurosci. 32, 14271–14275. doi: 10.1523/JNEUROSCI.3115-12.2012

Mellinger, J., Schalk, G., Braun, C., Preissl, H., Rosenstiel, W., Birbaumer, N., et al. (2007). An MEG-based brain-computer interface (BCI). Neuroimage 36, 581–593. doi: 10.1016/j.neuroimage.2007.03.019

Micoulaud-Franchi, J. A., Geoﬀroy, P. A., Fond, G., Lopez, R., Bioulac, S., and Philip, P. (2014). EEG neurofeedback treatments in children with ADHD: an updated meta-analysis of randomized controlled trials. Front. Hum. Neurosci. 8:906. doi: 10.3389/fnhum.2014.00906

Millichap, J. G. (2008). Etiologic classiﬁcation of attention-deﬁcit/hyperactivity disorder. Pediatrics 121, e358–e365. doi: 10.1542/peds.2007-1332

Ming, D., Xi, Y., Zhang, M., Qi, H., Cheng, L., Wan, B., et al. (2009). Electroencephalograph (EEG) signal processing method of motor imaginary potential for attention level classiﬁcation. IEEE Eng. Med. Biol. Soc. 2009, 4347–4351. doi: 10.1109/iembs.2009.5332743

Muller, M. M., and Hillyard, S. (2000). Concurrent recording of steady-state and transient event-related potentials as indices of visual-spatial selective attention. Clin. Neurophysiol. 111, 1544–1552. doi: 10.1016/S1388-2457(00)00371-0

Muller-Putz, G. R., and Pfurtscheller, G. (2008). Control of an electrical prosthesis with an SSVEP-based BCI. IEEE Trans. Biomed. Eng. 55, 361–364. doi: 10.1109/TBME.2007.897815

Muller-Putz, G. R., Scherer, R., Brauneis, C., and Pfurtscheller, G. (2005). Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components. J. Neural Eng. 2, 123–130. doi: 10.1088/17412560/2/4/008

Musch, K., Hamame, C. M., Perrone-Bertolotti, M., Minotti, L., Kahane, P., Engel, A. K., et al. (2014). Selective attention modulates high-frequency activity in the face-processing network. Cortex 60, 34–51. doi: 10.1016/j.cortex.2014. 06.006

Nagendra, H., Kumar, V., and Mukherjee, S. (2015). Cognitive behavior evaluation based on physiological parameters among young healthy subjects with yoga as intervention. Comput. Math. Methods Med. 2015:821061. doi: 10.1155/2015/821061

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Nicolelis, M. A., Dimitrov, D., Carmena, J. M., Crist, R., Lehew, G., Kralik, J. D., et al. (2003). Chronic, multisite, multielectrode recordings in macaque monkeys. Proc. Natl. Acad. Sci. U.S.A. 100, 11041–11046. doi: 10.1073/pnas. 1934665100

Nicolelis, M. A., and Lebedev, M. A. (2009). Principles of neural ensemble physiology underlying the operation of brain-machine interfaces. Nat. Rev. Neurosci. 10, 530–540. doi: 10.1038/nrn2653

Nicolelis, M. A., and Ribeiro, S. (2002). Multielectrode recordings: the next steps. Curr. Opin. Neurobiol. 12, 602–606. doi: 10.1016/S0959-4388(02) 00374-4

O’Doherty, J. E., Lebedev, M. A., Iﬀt, P. J., Zhuang, K. Z., Shokur, S., Bleuler, H., et al. (2011). Active tactile exploration using a brain-machine-brain interface. Nature 479, 228–231. doi: 10.1038/nature10489

Okazaki, Y. O., Horschig, J. M., Luther, L., Oostenveld, R., Murakami, I., and Jensen, O. (2015). Real-time MEG neurofeedback training of posterior alpha activity modulates subsequent visual detection performance. Neuroimage 107, 323–332. doi: 10.1016/j.neuroimage.2014.12.014

Ordikhani-Seyedlar, M., Sorensen, H. B., Kjaer, T. W., Siebner, H. R., and Puthusserypady, S. (2014). SSVEP-modulation by covert and overt attention: novel features for BCI in attention neuro-rehabilitation. IEEE Eng. Med. Biol. Soc. 2014, 5462–5465. doi: 10.1109/embc.2014.6944862

Ortega, R., Lopez, V., Carrasco, X., Anllo-Vento, L., and Aboitiz, F. (2013). Exogenous orienting of visual-spatial attention in ADHD children. Brain Res. 1493, 68–79. doi: 10.1016/j.brainres.2012.11.036

Ozaki, I., Yaegashi, Y., Baba, M., and Hashimoto, I. (2006). High-frequency oscillatory activities during selective attention in humans. Suppl. Clin. Neurophysiol. 59, 57–60. doi: 10.1016/S1567-424X(09)70012-1

Pais-Vieira, M., Lebedev, M., Kunicki, C., Wang, J., and Nicolelis, M. A. (2013). A brain-to-brain interface for real-time sharing of sensorimotor information. Sci. Rep. 3:1319. doi: 10.1038/srep01319

Palomares, M., Ales, J. M., Wade, A. R., Cottereau, B. R., and Norcia, A. M.

(2012). Distinct eﬀects of attention on the neural responses to form and motion processing: a SSVEP source-imaging study. J. Vis. 12:15. doi: 10.1167/12.10.15

Panicker, R. C., Puthusserypady, S., and Sun, Y. (2011). An asynchronous P300 BCI with SSVEP-based control state detection. IEEE Trans. Biomed. Eng. 58, 1781–1788. doi: 10.1109/TBME.2011.2116018

Peikon, I. D., Fitzsimmons, N. A., Lebedev, M. A., and Nicolelis, M. A. (2009). Three-dimensional, automated, real-time video system for tracking limb motion in brain-machine interface studies. J. Neurosci. Methods 180, 224–233. doi: 10.1016/j.jneumeth.2009.03.010

Petersen, S. E., and Posner, M. I. (2012). The attention system of the human brain: 20 years after. Annu. Rev. Neurosci. 35, 73–89. doi: 10.1146/annurev-neuro062111-150525

Polanczyk, G., and Rohde, L. A. (2007). Epidemiology of attentiondeﬁcit/hyperactivity disorder across the lifespan. Curr. Opin. Psychiatry 20, 386–392. doi: 10.1097/YCO.0b013e3281568d7a

Sutter, E. E., and Tran, D. (1992). The ﬁeld topography of ERG components in man–I. The photopic luminance response. Vision Res. 32, 433–446. doi: 10.1016/0042-6989(92)90235-B

Polich, J. (2007). Updating P300: an integrative theory of P3a and P3b. Clin. Neurophysiol. 118, 2128–2148. doi: 10.1016/j.clinph.2007.04.019

Polich, J., and Bondurant, T. (1997). P300 sequence eﬀects, probability, and interstimulus interval. Physiol. Behav. 61, 843–849. doi: 10.1016/S00319384(96)00564-1

Posner, M. I. (1980). Orienting of attention. Q. J. Exp. Psychol. 32, 3–25. doi: 10.1080/00335558008248231 Posner, M. I. (1994). Attention: the mechanisms of consciousness. Proc. Natl. Acad. Sci. U.S.A. 91, 7398–7403. doi: 10.1073/pnas.91.16.7398 Posner, M. I. (2012). Attentional networks and consciousness. Front. Psychol. 3:64. doi: 10.3389/fpsyg.2012.00064

Posner, M. I., and Rothbart, M. K. (2007). Research on attention networks as a model for the integration of psychological science. Annu. Rev. Psychol. 58, 1–23. doi: 10.1146/annurev.psych.58.110405.085516

Posner, M. I., Snyder, C. R., and Davidson, B. J. (1980). Attention and the detection of signals. J. Exp. Psychol. 109, 160–174. doi: 10.1037/0096-3445.109.2.160

Power, S. D., Kushki, A., and Chau, T. (2012). Automatic single-trial discrimination of mental arithmetic, mental singing and the no-control state from prefrontal activity: toward a three-state NIRS-BCI. BMC Res. Notes 5:141. doi: 10.1186/1756-0500-5-141

Praamstra, P., Boutsen, L., and Humphreys, G. W. (2005). Frontoparietal control of spatial attention and motor intention in human EEG. J. Neurophysiol. 94, 764–774. doi: 10.1152/jn.01052.2004

Pritchard, V. E., Neumann, E., and Rucklidge, J. J. (2008). Selective attention and inhibitory deﬁcits in ADHD: does subtype or comorbidity modulate negative priming eﬀects? Brain Cogn. 67, 324–339. doi: 10.1016/j.bandc.2008.02.002 Punsawad, Y., and Wongsawat, Y. (2012). Motion visual stimulus for SSVEPbased BCI system. IEEE Eng. Med. Biol. Soc. 2012, 3837–3840. doi: 10.1109/embc.2012.6346804

Ray, S., Niebur, E., Hsiao, S. S., Sinai, A., and Crone, N. E. (2008). High-frequency gamma activity (80-150Hz) is increased in human cortex during selective attention. Clin. Neurophysiol. 119, 116–133. doi: 10.1016/j.clinph.2007.09.136

Reuter, E. M., Bednark, J., and Cunnington, R. (2015). Reliance on visual attention during visuomotor adaptation: an SSVEP study. Exp. Brain Res. 233, 2041–2051. doi: 10.1007/s00221-015-4275-z

Rizzolatti, G., Riggio, L., Dascola, I., and Umilta, C. (1987). Reorienting attention across the horizontal and vertical meridians: evidence in favor of a premotor theory of attention. Neuropsychologia 25, 31–40. doi: 10.1016/00283932(87)90041-8

Rohenkohl, G., and Nobre, A. C. (2011). alpha oscillations related to anticipatory attention follow temporal expectations. J. Neurosci. 31, 14076–14084. doi: 10.1523/JNEUROSCI.3387-11.2011

Rossini, P. M., Noris Ferilli, M. A., and Ferreri, F. (2012). Cortical plasticity and brain computer interface. Eur. J. Phys. Rehabil. Med. 48, 307–312.

Rougeul-Buser, A., and Buser, P. (1997). Rhythms in the alpha band in cats and their behavioural correlates. Int. J. Psychophysiol. 26, 191–203. doi: 10.1016/S0167-8760(97)00764-2

Ruiz, S., Birbaumer, N., and Sitaram, R. (2013). Abnormal neural connectivity in schizophrenia and fMRI-brain-computer interface as a potential therapeutic approach. Front. Psychiatry 4:17. doi: 10.3389/fpsyt.2013.00017

Sakurada, T., Kawase, T., Komatsu, T., and Kansaku, K. (2015). Use of highfrequency visual stimuli above the critical ﬂicker frequency in a SSVEP-based BMI. Clin. Neurophysiol. 126, 1972–1978. doi: 10.1016/j.clinph.2014.12.010 Sanei, S., and Chambers, J. (2008). “Brain-computer interface,” in EEG Signal Processing, eds S. Sanei and J. Chambers (Chichester: John Wiley & Sons), 239–261.

Sato, J. R., Basilio, R., Paiva, F. F., Garrido, G. J., Bramati, I. E., Bado, P., et al. (2013). Real-time fMRI pattern decoding and neurofeedback using FRIEND: an FSL-integrated BCI toolbox. PLoS ONE 8:e81658. doi: 10.1371/journal.pone. 0081658

Schalk, G. (2010). Can electrocorticography (ECoG) support robust and powerful brain-computer interfaces? Front. Neuroeng. 3:9. doi: 10.3389/fneng.2010.

- 00009

Schalk, G., and Leuthardt, E. C. (2011). Brain-computer interfaces using electrocorticographic signals. IEEE Rev. Biomed. Eng. 4, 140–154. doi:

- 10.1109/RBME.2011.2172408

Schwarz, D. A., Lebedev, M. A., Hanson, T. L., Dimitrov, D. F., Lehew, G., Meloy, J., et al. (2014). Chronic, wireless recordings of large-scale brain activity in freely moving rhesus monkeys. Nat. Methods 11, 670–676. doi: 10.1038/nmeth.2936

Shahid, S., and Prasad, G. (2011). Bispectrum-based feature extraction technique for devising a practical brain-computer interface. J. Neural Eng. 8:025014. doi: 10.1088/1741-2560/8/2/025014

Shain, W., Spataro, L., Dilgen, J., Haverstick, K., Retterer, S., Isaacson, M., et al. (2003). Controlling cellular reactive responses around neural prosthetic devices using peripheral and local intervention strategies. IEEE Trans Neural. Syst. Rehabil. Eng. 11, 186–188. doi: 10.1109/TNSRE.2003.814800

Shishkin, S. L., Ganin, I. P., Basyul, I. A., Zhigalov, A. Y., and Kaplan, A. Y. (2009). N1 wave in the P300 BCI is not sensitive to the physical characteristics of stimuli. J. Integr. Neurosci. 8, 471–485. doi: 10.1142/S0219635209002320

Sitaram, R., Zhang, H., Guan, C., Thulasidas, M., Hoshi, Y., Ishikawa, A., et al. (2007). Temporal classiﬁcation of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain-computer interface. Neuroimage 34, 1416–1427. doi: 10.1016/j.neuroimage.2006.11.005

Skounti, M., Philalithis, A., and Galanakis, E. (2007). Variations in prevalence of attention deﬁcit hyperactivity disorder worldwide. Eur. J. Pediatr. 166, 117–123. doi: 10.1007/s00431-006-0299-5

Sokolov, E. N. (1969). Handbook of Contemporary Soviet Psychology. New York, NY: Basic Books.

Sokunbi, M. O., Linden, D. E., Habes, I., Johnston, S., and Ihssen, N. (2014). Realtime fMRI brain-computer interface: development of a “motivational feedback” subsystem for the regulation of visual cue reactivity. Front. Behav. Neurosci. 8:392. doi: 10.3389/fnbeh.2014.00392

Soltani, M., and Knight, R. T. (2000). Neural origins of the P300. Crit. Rev. Neurobiol. 14, 199–224. doi: 10.1615/CritRevNeurobiol.v14.i3-4.20

Sprague, T. C., Saproo, S., and Serences, J. T. (2015). Visual attention mitigates information loss in small- and large-scale neural codes. Trends Cogn. Sci. 19, 215–226. doi: 10.1016/j.tics.2015.02.005

Steiner, H., Warren, B. L., Van Waes, V., and Bolanos-Guzman, C. A. (2014a). Life-long consequences of juvenile exposure to psychotropic drugs on brain and behavior. Prog. Brain Res. 211, 13–30. doi: 10.1016/B978-0-444-63425-2. 00002-7

- Steiner, N. J., Frenette, E. C., Rene, K. M., Brennan, R. T., and Perrin, E. C. (2014b). In-school neurofeedback training for ADHD: sustained improvements from a randomized control trial. Pediatrics 133, 483–492. doi: 10.1542/peds.2013-2059
- Steiner, N. J., Frenette, E. C., Rene, K. M., Brennan, R. T., and Perrin, E. C. (2014c). Neurofeedback and cognitive attention training for children with attentiondeﬁcit hyperactivity disorder in schools. J. Dev. Behav. Pediatr. 35, 18–27. doi: 10.1097/DBP.0000000000000009

Steiner, N. J., Sheldrick, R. C., Gotthelf, D., and Perrin, E. C. (2011). Computer-based attention training in the schools for children with attention deﬁcit/hyperactivity disorder: a preliminary trial. Clin. Pediatr. 50, 615–622. doi: 10.1177/0009922810397887

Stoeckel, L. E., Garrison, K. A., Ghosh, S., Wighton, P., Hanlon, C. A., Gilman, J. M., et al. (2014). Optimizing real time fMRI neurofeedback for therapeutic discovery and development. Neuroimage Clin. 5, 245–255. doi: 10.1016/j.nicl.2014.07.002

Sulzer, J., Haller, S., Scharnowski, F., Weiskopf, N., Birbaumer, N., Blefari, M. L., et al. (2013). Real-time fMRI neurofeedback: progress and challenges. Neuroimage 76, 386–399. doi: 10.1016/j.neuroimage.2013.03.033

Szuromi, B., Czobor, P., Komlosi, S., and Bitter, I. (2011). P300 deﬁcits in adults with attention deﬁcit hyperactivity disorder: a meta-analysis. Psychol. Med. 41, 1529–1538. doi: 10.1017/S0033291710001996

ter Huurne, N., Onnink, M., Kan, C., Franke, B., Buitelaar, J., and Jensen, O. (2013). Behavioral consequences of aberrant alpha lateralization in attention-deﬁcit/hyperactivity disorder. Biol. Psychiatry 74, 227–233. doi: 10.1016/j.biopsych.2013.02.001

Thorpe, S., D’Zmura, M., and Srinivasan, R. (2012). Lateralization of frequencyspeciﬁc networks for covert spatial attention to auditory stimuli. Brain Topogr. 25, 39–54. doi: 10.1007/s10548-011-0186-x

Thut, G., Nietzel, A., Brandt, S. A., and Pascual-Leone, A. (2006). Alpha-band electroencephalographic activity over occipital cortex indexes visuospatial attention bias and predicts visual target detection. J. Neurosci. 26, 9494–9502. doi: 10.1523/JNEUROSCI.0875-06.2006

Tonin, L., Leeb, R., Sobolewski, A., and Millan Jdel, R. (2013). An online EEG BCI based on covert visuospatial attention in absence of exogenous stimulation. J. Neural Eng. 10:056007. doi: 10.1088/1741-2560/10/5/056007

Tomita, Y., Vialatte, F. B., Dreyfus, G., Mitsukura, Y., Bakardjian, H., and Cichocki, A. (2014). Bimodal BCI using simultaneously NIRS and EEG. IEEE Trans. Biomed. Eng. 61, 1274–1284. doi: 10.1109/TBME.2014.2300492

Valera, E. M., Faraone, S. V., Murray, K. E., and Seidman, L. J. (2007). Meta-analysis of structural imaging ﬁndings in attention-deﬁcit/hyperactivity disorder. Biol. Psychiatry 61, 1361–1369. doi: 10.1016/j.biopsych.2006.06.011

Vance, A. L., Luk, E. S., Costin, J., Tonge, B. J., and Pantelis, C. (1999). Attention deﬁcit hyperactivity disorder: anxiety phenomena in children treated with psychostimulant medication for 6 months or more. Aust. N.Z. J. Psychiatry 33, 399–406. doi: 10.1046/j.1440-1614.1999.00575.x

van der Waal, M., Severens, M., Geuze, J., and Desain, P. (2012). Introducing the tactile speller: an ERP-based brain-computer interface for communication. J. Neural Eng. 9:045002. doi: 10.1088/1741-2560/9/4/045002

Van Gerven, M., Farquhar, J., Schaefer, R., Vlek, R., Geuze, J., Nijholt, A., et al.

(2009). The brain-computer interface cycle. J. Neural Eng. 6:041001. doi: 10.1088/1741-2560/6/4/041001

Vidaurre, C., Kawanabe, M., von Bunau, P., Blankertz, B., and Muller, K. R. (2011). Toward unsupervised adaptation of LDA for brain-computer interfaces. IEEE Trans. Biomed. Eng. 58, 587–597. doi: 10.1109/TBME.2010.2093133

Vollebregt, M. A., van Dongen-Boomsma, M., Buitelaar, J. K., and Slaats-Willemse, D. (2014a). Does EEG-neurofeedback improve neurocognitive functioning in children with attention-deﬁcit/hyperactivity disorder? A systematic review and a double-blind placebo-controlled study. J. Child Psychol. Psychiatry 55, 460–472. doi: 10.1111/jcpp.12143

Vollebregt, M. A., van Dongen-Boomsma, M., Slaats-Willemse, D., Buitelaar, J. K., and Oostenveld, R. (2014b). How the individual alpha peak frequency helps unravel the neurophysiologic underpinnings of behavioral functioning in children with attention-deﬁcit/hyperactivity disorder. Clin. EEG Neurosci. 46, 285–291. doi: 10.1177/1550059414537257

Waldert, S., Tushaus, L., Kaller, C. P., Aertsen, A., and Mehring, C. (2012). fNIRS exhibits weak tuning to hand movement direction. PLoS ONE 7:e49266. doi: 10.1371/journal.pone.0049266

Wang, S., Yang, Y., Xing, W., Chen, J., Liu, C., and Luo, X. (2013). Altered neural circuits related to sustained attention and executive control in children with ADHD: an event-related fMRI study. Clin. Neurophysiol. 124, 2181–2190. doi: 10.1016/j.clinph.2013.05.008

Wangler, S., Gevensleben, H., Albrecht, B., Studer, P., Rothenberger, A., Moll, G. H., et al. (2011). Neurofeedback in children with ADHD: speciﬁc event-related potential ﬁndings of a randomized controlled trial. Clin. Neurophysiol. 122, 942–950. doi: 10.1016/j.clinph.2010.06.036

Ward, L. M., Doesburg, S. M., Kitajo, K., MacLean, S. E., and Roggeveen, A. B.

(2006). Neural synchrony in stochastic resonance, attention, and consciousness. Can. J. Exp. Psychol. 60, 319–326. doi: 10.1037/cjep2006029

Weiskopf, N., Mathiak, K., Bock, S. W., Scharnowski, F., Veit, R., Grodd, W., et al. (2004). Principles of a brain-computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI). IEEE Trans. Biomed. Eng. 51, 966–970. doi: 10.1109/TBME.2004.827063

Wolfe, J. M., and Horowitz, T. S. (2004). What attributes guide the deployment of visual attention and how do they do it? Nat. Rev. Neurosci. 5, 495–501. doi: 10.1038/nrn1411

Wolpaw, J. R., Birbaumer, N., Heetderks, W. J., McFarland, D. J., Peckham, P. H., Schalk, G., et al. (2000). Brain-computer interface technology: a review of the ﬁrst international meeting. IEEE Trans. Rehabil. Eng. 8, 164–173. doi: 10.1109/TRE.2000.847807

Wolpaw, J. R., McFarland, D. J., Neat, G. W., and Forneris, C. A. (1991). An EEGbased brain-computer interface for cursor control. Electroencephalogr. Clin. Neurophysiol. 78, 252–259. doi: 10.1016/0013-4694(91)90040-B

Wu, J., Li, Q., Bai, O., and Touge, T. (2009). Multisensory interactions elicited by audiovisual stimuli presented peripherally in a visual attention task: a behavioral and event-related potential study in humans. J. Clin. Neurophysiol. 26, 407–413. doi: 10.1097/WNP.0b013e3181c298b1

Wu, Z., and Su, S. (2014). A dynamic selection method for reference electrode in SSVEP-based BCI. PLoS ONE 9:e104248. doi: 10.1371/journal.pone.0104248 Xu, P., Tian, C., Zhang, Y., Jing, W., Wang, Z., Liu, T., et al. (2013). Cortical network properties revealed by SSVEP in anesthetized rats. Sci. Rep. 3, 1–11. doi: 10.1038/srep02496

Yang, L., Leung, H., Peterson, D. A., Sejnowski, T. J., and Poizner, H. (2014). Toward a semi-self-paced EEG brain computer interface: decoding initiation state from non-initiation state in dedicated time slots. PLoS ONE 9:e88915. doi: 10.1371/journal.pone.0088915

Yoo, S. S., Kim, H., Filandrianos, E., Taghados, S. J., and Park, S. (2013). Noninvasive brain-to-brain interface (BBI): establishing functional links between two brains. PLoS ONE 8:e60410. doi: 10.1371/journal.pone.0060410

Zacksenhouse, M., Lebedev, M. A., Carmena, J. M., O’Doherty, J. E., Henriquez, C., and Nicolelis, M. A. (2007). Cortical modulations increase in early sessions with brain-machine interface. PLoS ONE 2:e619. doi: 10.1371/journal.pone.00 00619

Zandi Mehran, Y., Firoozabadi, M., and Rostami, R. (2014). Improvement of neurofeedback therapy for improved attention through facilitation of brain activity using local sinusoidal extremely low frequency magnetic ﬁeld exposure. Clin. EEG Neurosci. 46, 100–112. doi: 10.1177/1550059414524403

Zarin, D. A., Suarez, A. P., Pincus, H. A., Kupersanin, E., and Zito, J. M. (1998). Clinical and treatment characteristics of children with attentiondeﬁcit/hyperactivity disorder in psychiatric practice. J. Am. Acad. Child Adolesc. Psychiatry 37, 1262–1270. doi: 10.1097/00004583-199812000-00009

Zhang, D., Maye, A., Gao, X., Hong, B., Engel, A. K., and Gao, S. (2010). An independent brain-computer interface using covert non-spatial visual selective attention. J. Neural Eng. 7:16010. doi: 10.1088/1741-2560/7/1/016010

Zhang, Y., Chen, Y., Bressler, S. L., and Ding, M. (2008). Response preparation and inhibition: the role of the cortical sensorimotor beta rhythm. Neuroscience 156, 238–246. doi: 10.1016/j.neuroscience.2008.06.061

Zhang, Y., Guo, D., Cheng, K., Yao, D., and Xu, P. (2015). The graph theoretical analysis of the SSVEP harmonic response networks. Cogn. Neurodyn. 9, 305–315. doi: 10.1007/s11571-015-9327-3

Zheng, H. Y., Peng, G., Chen, J. Y., Zhang, C., Minett, J. W., and Wang, W. S. (2014). The inﬂuence of tone inventory on ERP without focal attention: a cross-language study. Comput. Math. Methods Med. 2014:961563. doi: 10.1155/2014/961563

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2016 Ordikhani-Seyedlar, Lebedev, Sorensen and Puthusserypady. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

