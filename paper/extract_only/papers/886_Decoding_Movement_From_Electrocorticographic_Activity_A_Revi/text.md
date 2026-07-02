REVIEW published: 03 December 2019 doi: 10.3389/fninf.2019.00074

# Decoding Movement From Electrocorticographic Activity: A Review

Ksenia Volkova1, Mikhail A. Lebedev1, Alexander Kaplan1,2,3 and Alexei Ossadtchi1*

1 Center for Bioelectric Interfaces, Higher School of Economics, National Research University, Moscow, Russia, 2 Center for Biotechnology Development, National Research Lobachevsky State University of Nizhny Novgorod, Nizhny Novgorod, Russia, 3 Laboratory for Neurophysiology and Neuro-Computer Interfaces, Faculty of Biology, Lomonosov Moscow State University, Moscow, Russia

Electrocorticography (ECoG) holds promise to provide efﬁcient neuroprosthetic solutions for people suffering from neurological disabilities. This recording technique combines adequate temporal and spatial resolution with the lower risks of medical complications compared to the other invasive methods. ECoG is routinely used in clinical practice for preoperative cortical mapping in epileptic patients. During the last two decades, research utilizing ECoG has considerably grown, including the paradigms where behaviorally relevant information is extracted from ECoG activity with decoding algorithms of different complexity. Several research groups have advanced toward the development of assistive devices driven by brain-computer interfaces (BCIs) that decode motor commands from multichannel ECoG recordings. Here we review the evolution of this ﬁeld and its recent tendencies, and discuss the potential areas for future development.

Keywords: electrocorticography, ECoG, brain-computer interface, BCI, movement decoding

Edited by: Gaute T. Einevoll,

## 1. INTRODUCTION

Norwegian University of Life Sciences, Norway

The brain is a unique organ of the human body. Containing myriads of neurons, the brain circuits continuously process multiple sensory, motor and cognitive signals, generate thoughts and decisions, and produce a subjective feeling of being conscious and free-willed. The brain enables us with the capacity to eﬀortlessly control such complex behaviors as voluntary movements of body parts, maintenance of posture and balance, speech production, and perception of the external world. Unfortunately, neurological disease or trauma may cause dramatic disruptions of these neuronal mechanisms, making an individual unable to move, feel and communicate. Many of such devastating neurological conditions currently have no cure, including amyotrophic lateral sclerosis (ALS), stroke, and spinal cord injury (SCI).

Reviewed by: Wim Van Drongelen,

University of Chicago, United States Pierre Berthet, University of Oslo, Norway

*Correspondence:

Alexei Ossadtchi aossadtchi@hse.ru

BCIs, also called brain-machine interfaces (BMIs) and neural prostheses, hold promise to provide revolutionary solutions to the treatment of brain disorders. BCIs connect neural circuits to external devices, such as prosthetic limbs, means of communication, computers, appliances for functional electrical stimulation, and even the other parts of the brain (Lebedev and Nicolelis, 2006). Medical applications of BCIs strive to restore functions lost to neurological disorders and aid in rehabilitation. For example, BCI approach to SCI consists of directly connecting the unaﬀected brain regions, such as the sensorimotor cortex, to a limb prosthesis (Hochberg et al., 2006, 2012; Collinger et al., 2013; Bouton et al., 2016). Many neuroprosthetic components have been proposed and developed over the last two decades. These are biocompatible implants for neural recordings, devices for stimulating neural circuits, and wireless recording systems. BCIs can connect the brain

Received: 03 May 2019 Accepted: 14 November 2019 Published: 03 December 2019

Citation: Volkova K, Lebedev MA, Kaplan A and Ossadtchi A (2019) Decoding

Movement From Electrocorticographic Activity: A Review. Front. Neuroinform. 13:74. doi: 10.3389/fninf.2019.00074

to computer cursors (Carmena et al., 2003; Lebedev et al., 2005), text generators (Pan et al., 2013; Akram et al., 2014), arm prostheses (Carmena et al., 2003; Velliste et al., 2008; Collinger et al., 2013), exoskeletons for assisted walking (Gancet et al., 2011; Contreras-Vidal and Grossman, 2013; Kwak et al., 2015), virtualreality objects (Badia et al., 2013), powered wheelchairs (Galán et al., 2008; Chai et al., 2014), drones (LaFleur et al., 2013), and automobiles (Göhring et al., 2013). Recently, futuristic BCIs have emerged that merge several individual brains into a brain-net (Pais-Vieira et al., 2013; Rao et al., 2014).

Among diﬀerent classes of BCIs, BCIs that operate in the motor domain have underwent a particularly extensive development because of the expectation that they could treat paralysis by enabling voluntary control of prosthetic limbs. Motor BCIs have been developed that enable movements of the arms (Wessberg et al., 2000; Carmena et al., 2003; Velliste et al., 2008; Collinger et al., 2013) and legs (Fitzsimmons et al., 2009). In addition to BCIs that enact movements, BCIs have emerged that handle cognitive functions, like executive control, attention, and decision making (Andersen et al., 2004, 2010; Mirabella and Lebedev, 2016). In the sensory domain, BCIs have been developed that apply stimulation to peripheral and central structures of the nervous system to evoke percepts mimicking natural senses, including hearing (House, 1976), vision (Dobelle, 2000; Normann et al., 2009), and touch (Bensmaia and Miller, 2014).

In this review, we focus on BCIs that are based on an invasive recording method called ECoG. We argue that ECoG could provide eﬃcient solutions for many clinical cases because, ﬁrst, ECoG grids sample neural signals with better spatial and temporal resolution compared to non-invasive recording methods, such as electroencephalography (EEG), and second, ECoG electrodes do not penetrate into the brain and thus oﬀer a safer solution compared to the techniques that require insertion of recording sensors into the nervous tissue (Leuthardt et al., 2004; Hill et al., 2012; Petroﬀ et al., 2016). The studies conducted up to date have demonstrated that ECoG-based BCIs are applicable to motor tasks. Yet, we suggest that accuracy of such motor BCIs could be improved by the implementation of more advanced neural decoding algorithms, particularly the ones based on deep neural networks.

We start with an overview of ECoG recording methods. Next, we review the motor tasks that have been utilized in ECoG decoding studies. Finally, we discuss the relevant decoding algorithms and software.

- 2. ECOG METHODOLOGY AND ITS ADVANTAGES COMPARED TO THE OTHER RECORDING METHODS

A multitude of methods for recording of brain activity have been developed during the last several decades. Depending on the biological and physical principles employed, these methods have diﬀerent spatial and temporal resolution. The recording methods range from classical single-unit techniques, where microelectrodes are inserted into the brain tissue, to non-invasive

approaches, such as EEG, magnetoencephalography (MEG), near-infrared spectroscopy and functional magnetic resonance imaging. The choice of method in each concrete case is based on a number of requirements, including an assessment of risk to human subjects.

With the advancement of BCIs, we have seen a development of multichannel recording methods that allow sampling signals from many brain regions simultaneously (Nicolelis and Lebedev, 2009). To build clinically relevant neural prostheses, such recording methods should be viable for long periods of time. Chronically implanted multielectrode arrays (MEAs) measure brain activity at high spatial (at the level of single neurons) and temporal (at the level of neuronal spikes) resolution. MEAsbased BCIs have been implemented in rats (Chapin et al., 1999; Song et al., 2009), non-human primates (Taylor et al., 2002; Carmena et al., 2003; Gilja et al., 2012; Schaﬀelhofer et al., 2015) and humans (Hochberg et al., 2006; Collinger et al., 2013; Gilja et al., 2015; Brandman et al., 2017). The number of motor degrees of freedom that such BCIs could handle has been steadily growing (Hochberg et al., 2012; Collinger et al., 2013; Wodlinger et al., 2014; Vaskov et al., 2018). Recordings with MEAs are, however, not without problems, particularly when utilized in humans, since intracortical electrodes may provoke infection, tissue damage and scarring – the factors that contribute to deterioration of recording quality over time (Perge et al., 2013; Nuyujukian et al., 2014; Murphy et al., 2016; Kim et al., 2018).

While non-invasive BCIs do not have appreciable health risks, they have limitations of their own. Thus, EEG-based BCIs, which are currently prevalent because of their ease of use (Nicolas-Alonso and Gomez-Gil, 2012), have a lower information transfer rate compared to invasive BCIs (Lebedev and Nicolelis, 2006). Signal to noise ratio and spatial resolution are low for EEG recordings because with this method electrical potentials are sampled at a distance from their source, get smeared due to propagation through brain meninges and skull, and are susceptible to contamination with mechanical, electrooculographic (EOG), and electromyographic (EMG) artifacts (Cooper et al., 1965). Classiﬁcation of several discrete motor states can be achieved with EEG recordings (for example, detecting the presence or absence of an actual or imagined limb movement). However, accurate decoding of ﬁne movement characteristics is diﬃcult with this method.

ECoG alleviates several problems related to using the other recording methods. With ECoG, electrical signal is recorded from the surface of the brain either epidurally (i.e., the electrodes are placed on the surface of the dura mater), or subdurally (i.e., the electrodes are placed underneath the dura mater.) While ECoG signals resemble EEG data (Kellis et al., 2016), they have greater amplitude, higher spatial resolution and broader frequency range (Schalk and Leuthardt, 2011). ECoG is superior to EEG for recordings of both cortical low-frequency oscillations (Hughes and Crunelli, 2005) and high-frequency activity in the gamma-range (Manning et al., 2009; Schalk and Leuthardt, 2011). The superior spatial and frequency resolution of ECoG enables obtaining detailed cortical maps, for example motor and sensory maps of individual ﬁngers, while sampling electrical activity from many cortical areas simultaneously. Additionally,

ECoG recordings are stable long-term (Blakely et al., 2009). By contrast, recordings of multiple single units with MEAs are not so stable, even though they could be considered a BCI control signal of superior quality. Although in the majority of studies ECoG grids have been implanted for a few days to minimize the infection risks associated to the use of tethered cables, it has been also shown that chronic ECoG implants are viable (Wyler et al., 1991; Weinand et al., 1994) and progress has been made toward the development of wireless, fully-implantable technologies (Vansteensel et al., 2016; Benabid et al., 2019). Based on these trends, it is reasonable to expect that clinically relevant, chronically implanted ECoG-based neural prostheses will emerge in the future for assisting patients suﬀering from neurological disorders. In summary, ECoG approach has multiple advantages for BCI applications, including an adequately high information transfer rate, stability of recordings, and a lower risk of medical complications. These features make ECoG method attractive for the developers of practical neuroprosthetic devices.

In clinical applications, ECoG electrodes are typically arranged into rectangular grids (for example, 6 × 8 or 8 × 8) or strips containing several electrodes in a single row. Platinum-iridium electrodes are often used, with the diameter of 4 mm most common for clinical applications. The commonly used 1-cm interelectrode distance yields an appropriate spatial resolution in many cases. Yet, the physical limit for resolution that could be achieved by decreasing the interelectrode distance is ∼1.25 mm for subdural recordings (Freeman et al., 2000) and ∼1.4 mm for epidural recordings (Slutzky et al., 2010). As a step toward reaching these limits of spatial resolution, ECoG grids with the spacing of 3–5 mm have been introduced and tested in a handful of studies conducted during the last decade (Wang et al., 2016). In such grids, neighboring electrodes carry suﬃciently diﬀerent information in the high gamma frequency range, as evident from the low coherence (∼ 0.3) between their signals (Wang et al., 2009). These grids have a superior spatial resolution compared to the 1-cm spaced grids not only because of the narrower inter-electrode spacing but also because of the smaller electrode size, which aids sampling local activity. With the 3–5 mm electrode spacing, accurate classiﬁcation of ﬁnger movements and multiple hand gestures has been achieved, as well as real-time control of a hand prosthesis (Wang et al., 2013; Bleichner et al., 2016; Hotson et al., 2016). More recently, even denser micro-ECoG grids have emerged with 40–80-micron wires and 1–3 mm spacing; these grid can occasionally sample activity of single cortical neurons (Khodagholy et al., 2015).

ECoG grids implanted for clinical reasons have been used as a testbed for diﬀerent types of BCIs. With epidural ECoG recordings (a safer option for clinical assessment), BCIs have been implemented for reliably detecting movements (Chavarriaga et al., 2016), recognizing diﬀerent movement types (Spüler et al., 2014b) and decoding movement timecourse (Flint et al., 2016). For widely spaced ECoG electrodes, decoding accuracy with epidural grids is similar to that achieved with subdural electrodes (Spüler et al., 2014a). Yet, if highdensity ECoG grids are used, they work better when implanted subdurally (Bundy et al., 2014). In theory, it is desirable to place ECoG implants over as many cortical sites as possible

because motor planning and execution engage multiple cortical areas. However, using many implants increases the health risk. Several studies have attempted to optimize the number and placement of ECoG electrodes (Bleichner et al., 2016; Li et al., 2017). Intraoperative assessment of electrical activity at diﬀerent cortical sites, before an ECoG grid is implanted (Xie et al., 2015), is one way to decrease the implant size and reduce the health risk.

## 3. MOTOR PARADIGMS

Movements can be decoded from the brain electrical activity owing to the existence of correlation between neural modulations and motor parameters, for a range of motor tasks (Lebedev, 2014). Thus, ECoG modulations are correlated with the movements of both the upper and lower limbs (Toro et al., 1994b; McCrimmon et al., 2017). BCI decoding algorithms convert neural modulations into the output signals of interest, such as limb position in space. While decoding algorithms are often evaluated oﬄine using previously collected neuronal data, their ultimate testing should be conducted in real-time settings, where subjects control actions performed by an external device directly with their brain activity.

The development of new decoding algorithms not only advances BCIs by improving their accuracy of performance and versatility, but also leads to new fundamental insights regarding the brain motor, sensory and cognitive mechanisms, the insights that emerge during BCI experiments and their trouble shooting (Nicolelis and Lebedev, 2009). Speciﬁcally, research on ECoGbased BCIs provides insights on the encoding of movements and sensations by the collective activity of cortical neuronal populations, functional signiﬁcance of diﬀerent cortical rhythms, somatotopic representation of body parts, as evident from ECoG activity at diﬀerent cortical sites and frequency bands, and the capacity of the brain to plastically adapt to novel BCI tasks.

A variety of movement types can be decoded from ECoG signals. These are wrist ﬂexion and extension (Satow et al., 2003; Gharabaghi et al., 2014; Spüler et al., 2014a; Jiang et al., 2015, 2017), various grasp types (Graimann et al., 2003; Miller et al., 2007; Pistohl et al., 2012; Chestek et al., 2013; Xie et al., 2015) hand gestures and postures (Graimann et al., 2003; Chestek et al., 2013; Bleichner et al., 2016; Li et al., 2017), individual ﬁnger movement (Graimann et al., 2003; Kubanek et al., 2009; Miller et al., 2009; Samiee et al., 2010; Wang et al., 2011; Elghrabawy and Wahed, 2012; Flamary and Rakotomamonjy, 2012; Liang and Bougrain, 2012; Chestek et al., 2013; Chen et al., 2014; Xie et al., 2018), tongue and lip protrusion (Graimann et al., 2003; Satow et al., 2003; Miller et al., 2007; Paul et al., 2017), and foot movements (Toro et al., 1994b; Satow et al., 2003). While cortical areas contralateral to the moving body part are usually used for decoding, the option of using ipsilateral cortex has been considered as well (Hotson et al., 2014).

In real-time BCIs, signals representing movements or their imagery are decoded from ECoG activity and sent as control signals to external devices, such as screen cursor. Cursor control has been implemented in one (Leuthardt et al., 2004, 2006), two

|[Figure 1]<br><br>FIGURE 1 | Experimental paradigms for decoding of movements from ECoG. (A) An arbitrary mapping paradigm, where the task performed by the subject and BCI output are dissimilar. In the illustrated example, clenching of the ﬁst produces an upward movement of the pointer. (B) A discrete classiﬁcation paradigm, where a BCI recognizes a posture or movement performed by the subject and reproduces it with an external device. The case is illustrated, where a subjects shapes his/her hand in one of three gestures, and the BCI generates a gesture of a virtual hand shown on the screen. (C) Continuous decoding paradigm, where movement parameters are decoded continuously (as a function of time or some other parameter) and reproduced by an external device. In the illustrated example, a virtual ﬁnger reproduces the trajectory of the subject’s ﬁnger.|
|---|

(Schalk et al., 2008), and three (Wang et al., 2013) dimensions. Additionally, ECoG-based BCIs have been demonstrated for the tasks of controlling a prosthetic hand (Yanagisawa et al., 2011; Chestek et al., 2013; Wang et al., 2013; Hotson et al., 2016; Li et al., 2017), enabling exoskeleton-assisted walking (Benabid et al., 2019), and selecting font characters with a speller application (Vansteensel et al., 2016).

Here we focus on ECoG-based motor BCIs, which are BCIs where users modulate their cortical activity to generate movements of external devices. Such BCIs can be grouped into three main categories by the relationship between the task performed by the subject and BCI output (Figure 1) (while this classiﬁcation can be applied to other types of BCIs, for example the ones based on EEG recordings, our review is restricted to ECoG-based systems). In the ﬁrst category, there is an arbitrary relationship between the subject’s action and the resulting movement of an external eﬀector. For example, a subject imagines moving the hand to generate an upward movement of the pointer and imagines moving the tongue to move the pointer downward (Leuthardt et al., 2006). In the second category, a discrete classiﬁer recognizes a motor action performed or imagined by the subject, for example moving one of the ﬁngers. Next, an external device executes the same action. The third category of BCIs decode diﬀerent motor parameters, such as movement direction, speed, acceleration, and force. The parameters are treated by the mathematical algorithm as continuous variables. An external device then reconstructs the movement from the decoded motor parameters.

- 3.1. Arbitrary-Mapping Paradigms The arbitrary-mapping paradigm was the earliest to be implemented with ECoG recordings. The early studies employed event-related potentials for extracting motor commands (Toro et al., 1994b; Huggins et al., 1999; Levine et al., 1999). Later, ECoG spectral changes during real or imagined movements were used for BCI control (Leuthardt et al., 2004). In both groups of studies,

actions performed by the subjects were mapped in an arbitrary way to actions executed by external devices.

To identify the most eﬃcient control strategy for such an arbitrary-mapping BCI, Leuthardt et al. (2004) introduced a pre-screening procedure, which has become a common practice (Leuthardt et al., 2006; Miller et al., 2007; Schalk et al., 2008). During pre-screening, subjects perform a range of tasks so that ECoG features with the most prominent modulations could be identiﬁed and used for BCI control. The tasks are performed with the body parts represented by the cortical areas covered by the implanted ECoG electrodes (Schalk et al., 2008). Subjects perform or imagine motor acts like opening and closing the hand, protruding and retracting the tongue, ﬂexing, and extending individual ﬁngers, pursing and unpursing the lips, moving the arm, leg or foot (Miller et al., 2007), moving the jaw, shrugging the shoulders (Schalk et al., 2008), and pronouncing words (Leuthardt et al., 2004, 2006). Based on ECoG activity patterns exhibited during these tasks, subsets of ECoG features (e.g., frequency bands and electrodes with the most prominent modulations) are selected for implementing a BCI.

With the pre-screening approach, actions causing the largest ECoG modulations could be quickly selected to improve accuracy of BCI control. In a pioneering study (Leuthardt et al., 2004), subjects reached the success rates of 74–100% after 3–24 min of training in closed-loop experiments where they performed or imagined a preselected action (like opening and closing the hand, protruding the tongue or saying the word “move”) to move a screen cursor in the vertical dimension. In these experiments, ECoG grids were placed over frontal, parietal and temporal cortical areas. In the next study (Leuthardt et al., 2006), the same group added to the experimental design an adjustment procedure, where the decoder settings were updated using the data from the initial online session. This adjustment accounted for the diﬀerences between ECoG modulations exhibited during the pre-screening procedure and the online control.

Schalk et al. (2008) designed an arbitrary-mapping approach for the case of two-dimensional cursor movements. ECoG

recordings were conducted from the frontal, temporal, and/or parietal cortex. During the pre-screening procedure, two tasks were selected that yielded the least correlated signal features (frequency bands and electrode locations) that were then used to independently control two coordinates of the cursor. After a training period of 12–26 min, ﬁve subjects achieved accuracy of 53–73% (with a 25% chance level) in a four-target task.

Wang et al. (2013) expanded the degrees of freedom of cursor movements to three dimensions. A tetraplegic subject with C4 level spinal cord injury underwent training for several weeks. ECoG activity was recorded using a high-density 32electrode grid with 4-mm spacing; electrode diameter was 2 or 3 mm. The grid was implanted over the hand and arm representing areas of the left sensorimotor cortex. The subject learned to activate his sensorimotor cortex by attempting voluntary movements. Distinct cortical modulations occurred for attempted movements of diﬀerent segments of the patient’s upper limb. The BCI control consisted of assigning of each type of attempted movement to a particular direction of cursor movement. The decoder processed ECoG modulations in the gamma band. An adapting decoding scheme was used, where the decoder alternated between the periods when the decoder weights were ﬁxed and when they underwent adjustments. The subject ﬁrst learned a two-dimensional control of the cursor in a virtual environment, then the third dimension was added by gradually merging the weights calculated for the attempted threedimensional task with the weights previously calculated for the two-dimensional control. The subject reached the success rate of 80% in the cursor control task, and also learned to control threedimensional reaching movements performed by a prosthetic arm. In the next study conducted by the same group (Degenhart et al., 2018), two additional subjects with arm paralysis were tested, one with ALS and the other with brachial plexus injury. The subjects used a somatotopic control strategy to operate a virtual cursor in two or three dimensions. In this strategy, spatiotemporal patterns of gamma-band cortical activity evoked by diﬀerent attempted upper-limb movements were converted into the direction of cursor movement. Cursor velocity was generated from ECoG gamma activity with an optimal linear estimator algorithm (Salinas and Abbott, 1994). Both subjects achieved control with up to three degrees of freedom.

Overall, the arbitrary-mapping approach has been shown suitable for building practical BCIs for the paralyzed patients capable of voluntarily modulating activity in the brain areas representing their paralyzed body parts (Spüler et al., 2014b; Chaudhary et al., 2016). Thus, Vansteensel et al. (2016) recently demonstrated a practical, a fully implanted ECoG-based BCI, where a patient with ALS learned to control a computer typing program by attempting voluntary hand movements. The ECoG grid was implanted subdurally over the motor cortex. This BCI enabled communication with a rate of two letters per minute. Notwithstanding the slow operation, BCIs of this kind oﬀer a practical solution for functional restoration, communication and rehabilitation of neurologically impaired patients. As such, this approach needs to be further developed.

3.2. Classiﬁcation and Reproduction of Movements

The second class of ECoG-based BCIs reproduces the same movements that subjects perform or imagine, which are recognized using a discrete classiﬁer. High spatial and temporal resolution of ECoG allows recognizing a suﬃciently large repertoire of movement types and executing them with an external device. Thus, areas corresponding to individual ﬁngers can be discerned with ECoG recordings (Miller et al., 2009), which allows implementing a BCI that recognizes the ﬁnger being moved or imagined being moved with a classiﬁer like Naïve Bayes (Chestek et al., 2013), linear discriminant analysis (LDA) (Wang et al., 2009; Hotson et al., 2016), or support vector machine (SVM) (Liu et al., 2010). Several studies have demonstrated that such classiﬁcation can be performed with high accuracy based on ECoG recordings from the hemisphere contralateral to the working hand. Wang et al. (2009) decoded the ﬁnger being moved from the signals recorded with a micro-ECoG grid that was placed over the contralateral motor cortex. In this study, one subject performed self-paced ﬁnger ﬂexions and extensions for ∼10 s. The active ﬁnger was identiﬁed with an accuracy of 73% with both LDA that processed the ECoG data reduced to the ﬁrst eight principal components and an SVM classiﬁer without dimensionality reduction. In the study by Kubanek et al. (2009) subjects responded to a cue by ﬂexing an individual ﬁnger 3–5 times over a time period of 1.5–3 s. ECoG activity was recorded from the frontal or temporal cortical areas. The relationship between the poser in diﬀerent ECoG spectral bands and ﬁnger trajectories was modeled using a linear decoder called PaceRegression. The active ﬁnger was then determined as the ﬁnger with the highest decoded ﬂexion amplitude. The acrosssubject average classiﬁcation accuracy was 77.1% when ECoG activity recorded at movement onset was analyzed. The accuracy increased to 80.3% when the analysis interval was optimized for each subject. Hotson et al. (2016) applied a hierarchical LDA classiﬁcation scheme to detect the ﬁnger being moved, reaching an accuracy of 76%. Furthermore, Liu et al. (2010) showed that ECoG activity in the sensorimotor cortex ipsilateral to the working hand could be used to determine the ﬁnger being moved. Their decoder incorporated logistic regression (LR) and a binary SVM.

Several studies have classiﬁed hand conﬁguration from ECoG recordings. Yanagisawa et al. (2011) recorded ECoG activity in the sensorimotor cortex of a subject performing three types of hand movements: grasping, hand-opening, and scissormimicking movements. With these tasks, they implemented online control of a prosthetic hand based on a two-step classiﬁcation scheme, where the ﬁrst step consisted of detecting movement intention and the second step was the decoding of movement type. Linear SVM was used as classiﬁcation algorithm for both steps. The intention to move was detected on average 37 ms earlier than the actual movement onset. Movement type was classiﬁed with the accuracy of 69.2%, which signiﬁcantly exceeded the 33.3% chance level. Pistohl et al. (2008) employed regularized LDA to decode two types of grasping movements from the ECoG recorded over the motor cortex. They decoded

the intention to move from ECoG 125-250 ms earlier than the actual movement onset. The subjects performed self-paced relocation of an object between several positions using either precision grip or whole-hand grasping. The grasp type was decoded with 93% accuracy based on the analysis of the time interval starting 1s before grasp till 0.5s after. Recording sites located anterior to the central sulcus were used for decoding whereas the sites posterior to the central sulcus were excluded as representing sensory responses.

Chestek et al. (2013) further increased the number of hand conﬁgurations decoded from the ECoG recorded over the sensorimotor-cortex. Their subjects conﬁgured the hands into one of four isometric postures: ﬁst, pinch, point or ﬁve-ﬁnger spray. Additionally, the subjects ﬂexed one or several ﬁngers. The interval −0.5–1.5s relative to movement onset was used in this analysis. Classiﬁcation was performed with a Naïve Bayes decoder applied to the gamma band of the ECoG. Four hand postures were classiﬁed with an accuracy of 68–81%, and 66– 98% accuracy was achieved in a ﬁve-class classiﬁcation, where classes represented four ﬁnger movements and a resting state. The same decoding methods were then utilized in the online sessions where subjects controlled a hand prosthesis with a BCI. Kapeller et al. (2014) classiﬁed three hand gestures: “open,” “peace,” and “ﬁst.” In their decoding method, the presence of hand movement was classiﬁed ﬁrst with a two-class LDA classiﬁer (with an accuracy of 86.6 and 97.7% in their ﬁrst and second subjects, respectively), and then a multi-class LDA detected the gesture (with an accuracy of 93.8 and 98.8%).

Furthermore, hand-gesture tasks have been used to investigate the ways the number of implanted electrodes could be reduced and conﬁned to a smaller cortical area. Bleichner et al. examined two subjects with high-density ECoG grids implanted over a small area (2.5–5.2 cm2) in the hand-representing area. Four hand gestures corresponded to letters D, F, V, and Y of the American sign language (ASL) (Bleichner et al., 2016). Gesture classiﬁcation was performed using a pattern-matching classiﬁcation algorithm that was applied to ECoG spectral bands and local motor potentials (LMPs). An accuracy of 97 and 74% was reached for their ﬁrst and second subjects, respectively. It was found that a selected electrode subset (two thirds of the total) was suﬃcient to reach the same classiﬁcation accuracy as the accuracy achieved with all electrodes. In the study of Li et al. (2017), participants produced three hand gestures (“scissor,” “rock,” and “paper”). Classiﬁcation accuracy with SVM classiﬁer applied to spectral features was in the range 69.7–85.7% when performed oﬄine and 80–82% during the online control of a prosthetic hand. The number of channels was reduced with a greedy algorithm. It was found that a subset of electrodes conﬁned to a small cortical area was suﬃcient to maintain good decoding performance.

Xie et al. (2015) decoded diﬀerent ﬁnger and hand movements from ECoG signals recorded intraoperatively in the motor cortex of awake subjects. They used an LDA classiﬁer applied to the features extracted with an autoregressive model, and a waveform length feature that represented signal complexity. The intraoperative decoding accuracy (91.8 and 93.0% in two subjects) was comparable to the accuracy reached with the ECoG

grids implanted for seizure monitoring (90.2 and 96.0% in the other two subjects). These results suggest that implementing BCI tasks during the implantation surgery could be useful for the adjustment of ECoG grid placement.

For proper reproduction of movements, movement onset needs to be decoded from neural activity in addition to the decoding of movement type. Early detection of the intention to move is important for BCI applications because it allows decreasing the delay between the brain activity and the response of the prosthetic device (Lebedev et al., 2008; Yanagisawa et al., 2011). Classiﬁcation algorithms, such as LDA (Kapeller et al., 2014; Hotson et al., 2016) and SVM (Yanagisawa et al., 2011) have been used to detect movement onset based on ECoG recordings.

In conclusion, the classiﬁcation and reproduction approach is suitable for neuroprosthetic applications where a ﬁnite set of motor outputs is suﬃcient, such as BCIs that enable sign language-like communications (Bleichner et al., 2016; Branco et al., 2017). Studies have shown that restoration of a ﬁnite set of movements is a practical BCI solution for amputees (Bruurmijn et al., 2017), and patients with hand paralysis (Shoham et al., 2001; Yanagisawa et al., 2012). Such BCIs could implement a shared control principle, where a general motor command is extracted from brain activity whereas the ﬁne details of movements are handled by the controller of a prosthetic limb (Li et al., 2014).

3.3. Decoding of Motor Parameters as Continuous Variables

The third class of ECoG-based BCIs treats the parameters of movements, such as limb position and velocity, as continuous variables that are decoded from brain activity. Many studies have employed a center-out task for continuous decoding. During this task, subjects repeatedly perform cued or self-paced arm or hand movements from a center into diﬀerent directions. These movements are usually converted into 2D or 3D movements of a cursor. The center-out task gained popularity after the studies of Georgopoulos et al. (1982) of the directional tuning properties of monkey motor cortical neurons. In ECoG studies with this design, four (Leuthardt et al., 2004; Reddy et al., 2009), six (Toro et al., 1994a), and eight (Leuthardt et al., 2004; Sanchez et al., 2008; Ball et al., 2009; Anderson et al., 2012; Wang et al., 2012; Nurse et al., 2015; Gunduz et al., 2016) targets locations have been used, all equidistant from the center. Center-out movements can be performed with a joystick (Reddy et al., 2009; Anderson et al., 2012; Wang et al., 2012), computer mouse (Kellis et al., 2012), stylus (Nurse et al., 2015), or the index ﬁnger moving on the surface of a touchscreen (Sanchez et al., 2008).

In a pioneering study that combined a center-out task with ECoG recordings in humans, Toro et al. (Toro et al., 1994a) evaluated tuning of ECoG in the 8–12 Hz band to the direction of arm movements. ECoG was sampled from the sensorimotor cortex and adjacent regions. Ten years later Leuthardt et al. (2004) analyzed a wider (0–200 Hz) range of frequencies and discovered directional tuning for various ECoG spectral bands. The center-out task was performed with a handheld joystick and incorporated four or eight targets. Ball et al.

(2009) decoded movement direction from ECoG during the execution of a center-out task and assessed the representation of directional information in diﬀerent cortical areas. Their subjects performed self-paced center-out movements with their arms to four target locations. Decoding was performed with regularized linear discriminant analysis (RLDA) applied to either smoothed ECoG signals or diﬀerent frequency bands. Decoding accuracy of 75% was achieved using the features calculated over the movement-execution period whereas 45% accuracy was achieved using the pre-movement period. ECoG channels corresponding to the hand and arm representing areas of the primary motor cortex were the most informative for the decoding. The analysis of additional data from a subject performing an eight-target task showed that ECoG activity (in the low-frequency and high-gamma bands) was cosine-tuned to the direction of arm movements. Anderson et al. (2012) investigated ECoG tuning to movement speed and velocity for center-out and tracing tasks performed with a force feedback joystick. ECoG recordings were conducted in multiple cortical areas. The strongest modulations to direction, speed, and velocity were observed in the primary motor cortex.

Wang et al. (2012) decoded movement direction with a timevarying dynamic Bayesian network. Center-out movements were performed with a joystick toward eight targets. Accuracy was quantiﬁed as the mean angular error between the actual and decoded direction; it was <90◦ in all subjects. Gunduz et al. (2016) reported a similar experimental design with center-out movements performed with a joystick, and eight targets. The task incorporated a delay period when the subjects prepared to move while holding the joystick still, which allowed decoding a person’s planned direction of movement. Direction was decoded with a stepwise multilinear regression applied to high gamma activity and/or LMPs. The median angular error was in the range 62– 70◦ across subjects. The authors observed directionally speciﬁc modulations of both high-gamma ECoG and LMPs during the delay and movement periods. Directionally tuned high-gamma activity was most prominent in the sensorimotor cortex whereas LMP modulations occurred in prefrontal cortices. The authors concluded that sampling directionally tuned ECoG from multiple cortical areas could improve the decoding of both planned and executed movements.

Reddy et al. (2009) enriched the center-out task with a tapping condition, which allowed testing how well centerout movements could be distinguished from the other types of movements. Center-out movements were performed with a joystick in response to arrows pointing in four possible directions. Additionally, subjects responded to a trigger cue (a square shown on the screen) by clicking on top of the joystick with the index ﬁnger. Decoding was performed using Naïve Bayes classiﬁer applied to time-frequency features. Decoding accuracy for movement direction was in the range 83–96% for the preparatory period and 58–86% for the movement period. The trigger condition was distinguished with 72–93% accuracy from the center-out conditions.

Bundy et al. (2016) added the third dimension to the centerout task. Their subjects performed arm reaching movements with the starting position located at the center of a cube and

cube vertices serving as targets. The kinematic parameters of movements were decoded with a hierarchical partial-least squares regression model. Correlation coeﬃcients between the true and predicted kinematic parameters ranged 0.31–0.80 across subjects for speed, 0.27–0.54 for velocity and 0.22–0.57 for position. The ﬁnal position was reconstructed with an accuracy of 49.0–66.2%.

Several studies employed reaching tasks that diﬀered from the classical center-out paradigm. In the study of Kellis et al. (2012), patients moved a cursor with a computer mouse from an initial position at the bottom of the screen to the upper right or upper left corner; trajectories were decoded from ECoG with a Kalman ﬁlter. Sanchez et al. (2008) continuously decoded kinematic parameters in two tasks: a center-out task where subjects tracked smoothly varying trajectories extending from the center to predeﬁned locations, and a target selection task where subjects performed reaches toward color-coded targets placed along the top edge of the screen. Cursor movements were decoded from ECoG frequency bands with a Wiener ﬁlter. Pistohl et al. (2008) had subjects acquire targets randomly positioned on a plane; hand coordinates were decoded with a Kalman ﬁlter. Schalk et al. (2007) reported highly accurate decoding of position and velocity using linear models for the task, performed with a joystick, where subjects pursued a target that moved counterclockwise along a circular trajectory. ECoG activity was cosine tuned to target angle, and decoding accuracy was comparable to the accuracy reported for monkeys implanted with MEAs.

In several studies, kinematics of ﬁnger movements was decoded from ECoG. Kubanek et al. (2009) extracted the timecourse of ﬁnger movements from motor cortical activity. The subjects repeatedly ﬂexed individual ﬁngers in response to a visual cue. Decoding was performed with PaceRegression algorithm. Several other decoding algorithms of diﬀerent complexity have been used for reproducing ﬁnger movements from ECoG, including switching linear model (Flamary and Rakotomamonjy, 2012; Liang and Bougrain, 2012) empirical mode decomposition (Hazrati and Hofmann, 2012), logisticweighted regression (Chen et al., 2014), and LSTM (Du et al., 2018; Xie et al., 2018).

In addition to the aforementioned reaching tasks and ﬁngermovement tasks, more complex motor tasks have been used in ECoG-BCI studies. Hammer et al. (2013) employed a gamelike continuous one-dimensional motor task where subjects controlled the horizontal position of a car with a steering wheel. Position, velocity and acceleration were decoded with a linear regression algorithm. In the study of Nakanishi et al. (2013), participants repositioned blocks on a board. ECoG features were transformed into a three-dimensional arm trajectory with a sparse linear regression algorithm. In the subsequent study by the same group, subjects repositioned blocks with three diﬀerent masses (Nakanishi et al., 2017). With this design, representations of intrinsic (e.g., muscle force) and extrinsic (e.g., target location) parameters of movements could be compared. ECoG recorded in the primary motor cortex was correlated mostly with the intrinsic parameters whereas ECoG recorded in pre-motor cortex was correlated with the extrinsic parameters. Wang et al. (2014) varied movement duration to investigate whether the entire movement course could be decoded from ECoG or only the

values of motor parameters at movement onset. Wu et al. (2016) implemented a three-dimensional isometric force task where subjects exerted force in diﬀerent directions without moving their arms. Directional information was extracted from the fronto-parietal ECoG recorded during both preparation and execution of the isometric task. The decoding algorithm incorporated a jPCA reduced-rank hidden Markov model (jPCARR-HMM), regularized shrunken centroid discriminant analysis, and LASSO regression.

Continuous-decoding BCIs based on ECoG recordings hold promise of eventually satisfying the requirements of paralyzed patients who need high-performance neuroprosthetic devices for restoration of mobility of their limbs. With a continuousdecoding neural prosthesis, patients would be able to execute a variety of movements in a near-normal way, where limb kinematics is constantly under the user’s voluntary control and ﬁne modiﬁcations of motor parameters could be done. Although a BCI with such an ideal control has not been demonstrated yet, recent advances in building fully implantable ECoG systems that perform continuous decoding (Vansteensel et al., 2016; Benabid et al., 2019) suggest that patients could improve in such BCI control through long-term practice that engages cortical plasticity mechanisms.

## 4. DECODING ALGORITHMS

In this section, we describe in more detail the decoding algorithms used in ECoG-based BCIs. These algorithms bear similarity to the decoders for EEG-based interfaces, which have been covered in several review articles (Lotte et al., 2007, 2018; McFarland and Wolpaw, 2017). Here we review only the literature on the decoding of movements from ECoG.

ECoG recordings capture electrical potentials of large neuronal populations formed by synchronous dendritic potentials and spikes (Buzsáki et al., 2012). Decoding of motor parameters from ECoG is possible because modulations of neuronal population activity are consistently correlated with task events and changes in motor parameters (Anderson et al., 2012; Lebedev, 2014). Multichannel ECoG data contains spatial (i.e., where in the cortex) and temporal (i.e., when and how) information that could be used for decoding of movement characteristics. Spatial ECoG components reﬂect, according to the somatotopic cortical map of the body, the body part engaged in a motor action. Temporal ECoG components reﬂect the time-dependent changes of motor parameters, such as limb position, speed, and acceleration.

An ECoG decoder takes multichannel ECoG data as the input and returns the signals of interest (the presence of movement, movement type, body part being moved, kinematic parameters, etc.) as the output. Many machine learning methods are applicable to this problem. The signal processing chain of a neural decoding algorithm comprises several blocks (Figure 2A). First, the raw data is transformed into features that contain information relevant to the BCI tasks. Ideally, these features should not contain redundant information. Next, a learning algorithm forms a decision rule that solves either a classiﬁcation

or regression problem. Classiﬁcation algorithms solve the problem of matching an input with one of the predeﬁned discrete classes. Regression algorithms match the input signals to the output continuously. For example, identiﬁcation of the ﬁnger being moved is a classiﬁcation problem, whereas decoding ﬁnger trajectory is a regression problem.

To properly set the decoder parameters, training data are needed that contain a suﬃcient number of examples of the inputs and their corresponding outputs. Based on the training data, a function is formed that, given the inputs from the dataset, returns values that are close to the corresponding desired outputs. A practicable decoder should be able to generalize to new data, that is, it should remain accurate when applied to the inputs not included in the training dataset. The case where decoding performs well for the training data but fails to work for the new data is called overﬁtting (Babyak, 2004). Overﬁtting often occurs when the decoder uses too many adjustable parameters, such as weights of the multiple linear regression. The presence of overﬁtting indicates that the transfer function is narrowly tuned to the anecdotal correlations between the input and output values taken from the training data rather than implements a generic transfer rule that reﬂects consistent input-output relationships. To avoid overﬁtting, feature space dimension reduction and appropriate regularization techniques should be employed. Thus, if an iterative approach is used to optimize decoder parameters, a proper stopping rule should be used to avoid overﬁtting.

Decoding algorithms have been developed that maintain generalization even when the sampled neural signals drift over time. Thus, Paul et al. (2017) used the higher-order statistics of ECoG bispectrum to overcome the diﬃculties decoding signals that were recorded during multiple task sessions. Their algorithm extracted signal features that were retained after a session-to-session transfer. This ﬁnding is consistent with the results of previous EEG-based studies (Shahid and Prasad, 2011; Das et al., 2016).

An additional important requirement is the versatility of training data, which means that the space of movements should be covered during sampling in such a way that the decoder interpolates to new data points rather than extrapolating to them. Practically, this means that experimental settings used to collect training data should be similar to the settings for online BCI control, including both the characteristics of movements and neural activity patterns. In the case of a mismatch between the training and online-BCI conditions, adjustments of the decoder may be needed to improve BCI performance.

4.1. Spectral Features

An important advantage of ECoG recordings compared to EEG is the wider range of signal frequencies that contain information useful for BCI control. ECoG activity comprises multiple frequency bands, from the low frequency activity (below 1 Hz) to high gamma (50–400 Hz). Some of these spectral components are clearly rhythmic, with clear peaks present in ECoG spectra (Miller et al., 2007). Each frequency band has speciﬁc functional correlates, which allows implementing decoders that capture diﬀerent aspects of the behavioral tasks, such as responses to stimuli, transition from rest to movement, characteristics of limb

|[Figure 2]<br><br>FIGURE 2 | Types of data processing chains employed in ECoG-based BCIs. (A) Classical approach, where preselected features are extracted from ECoG recordings, followed by a classiﬁcation or regression algorithm that generates BCI output. (B) Deep learning approach that handles both feature selection and decoding. (C) Hierarchical scheme with multiple decoders and processing chains that perform switching or relative weights adjustment.|
|---|

kinematics, and engaging diﬀerent body parts. An ECoG decoder that uses multiple frequency bands simultaneously is potentially more accurate and versatile compared to the decoder based on a single spectral band.

To extract task-related spectral features, ECoG signal is either bandpass ﬁltered (Liang and Bougrain, 2012; Chestek et al., 2013; Nakanishi et al., 2013) or converted into the frequency domain using non-parametric methods, such as Fourier transform (Chin

- et al., 2007; Miller et al., 2007; Blakely et al., 2009; Reddy

et al., 2009; Ryun et al., 2014), multitaper methods (Ball et al., 2009; Kellis et al., 2012; Pistohl et al., 2012; Elgharabawy and Wahed, 2016), parametric techniques, such as autoregressive model estimation (Leuthardt et al., 2004; Schalk et al., 2007; Kubanek et al., 2009; Wang et al., 2012; Xie et al., 2015), and the maximum entropy approach (van Vugt et al., 2007; Collinger et al., 2014; Bundy et al., 2016; Gunduz et al., 2016). Spectral features can be also extracted with ﬁlter bank methods, such as Gabor ﬁlters (Liu et al., 2010; Elghrabawy and Wahed, 2012;

|[Figure 3]<br><br>FIGURE 3 | Typical changes in ECoG activity that occur during the execution of a motor task (in this case, ﬁnger ﬂexion). Task-related activity is compared to ECoG activity recorded during a rest period. (A) Channel index × spectral frequency diagram with the color-coded values representing desynchronization index calculated as 2 PPtask−Prest<br><br>task+Prest . (B–D) Cortical distribution of desynchronization index for different ECoG frequency bands. (B) Data for the alpha band. It can be seen that, during a motor task, alpha-band activity is desynchronized over a large portion of the sensorimotor cortex. (C) Data for the beta band. Beta band activity is desychronization over a more compact cortical area as compared to the alpha-band. (D) Data for the beta band for the high frequency gamma activity (40–60 Hz), which exhibits a pronounced synchronization over a small cortical area. The light-gray shaded spot shows the localization of the hand-related sensorimotor are obtained with fMRI.|
|---|

Elgharabawy and Wahed, 2016; Wu et al., 2016). Ideally, neural signals should be processed in such a way that an optimal tradeoﬀ is reached between the temporal and spectral resolution.

ECoG mu (8–12 Hz) and beta (18–26 Hz) rhythms recorded in the sensorimotor are commonly used for decoding movements from ECoG. These oscillations are thought to reﬂect the activity in corticothalamic loops (Schalk and Leuthardt, 2011). The mu and beta rhythms are typically not conﬁned to local cortical areas but rather occur over large surfaces (Brunner et al., 2009). Movement and motor imagery cause desynchronization (i.e., decrease in amplitude) of these rhythms, which allows implementing BCIs that detect movement onset and time course. While ECoG recordings are useful for measuring the mu and beta activity, approximately the same measurements, albeit with a lower spatial resolution, could be accomplished with EEG recordings, which are suitable for monitoring cortical rhythms below 40 Hz. By contrast, gamma-band activity (40 Hz and higher) cannot be reliably recorded with EEG due to signal contamination by facial EMG activity that belongs to the same

frequency range. Yet, gamma activity is reliably sampled with ECoG. ECoG activity in the gamma band matches the activity of single neurons in the same area (Buzsáki et al., 2012) and, unlike the slower rhythms, it is not widespread but rather occurs in local cortical areas (Schalk and Leuthardt, 2011). These properties make ECoG gamma activity suitable for decoding based on cortical location and for decoding speciﬁc aspects of movement planning and execution with the accuracy comparable to the decoding from neuronal spikes (Anderson et al., 2012; Gunduz et al., 2016). ECoG gamma recordings are also useful to study cognitive mechanisms (Sturm et al., 2014). Thus, high-frequency ECoG components are especially valuable for implementing BCIs of diﬀerent kinds. Figure 3 shows the typical changes that occur in diﬀerent ECoG frequency bands during the execution of a motor task.

At the lower end of ECoG spectrum (<2 Hz), ECoG lowfrequency component (LFC) has been shown to be applicable for BCI decoding because it contains information about movement timecourse and kinematics (Mehring et al., 2003; Rickert et al.,

2005; Pistohl et al., 2008; Ball et al., 2009; Hammer et al., 2013). LFC can be extracted, for example, by smoothing the signal with Savitzky-Golay ﬁlters (Pistohl et al., 2008, 2012; Ball et al.,

- 2009). Schalk et al. (2007) called this component local motor potential (LMP) and computed it as a running average. LMP is modulated during motor behaviors, so it can be used for decoding limb kinematics (Kubanek et al., 2009; Acharya et al., 2010; Fifer et al., 2012; Wang et al., 2012; Chen et al., 2014; Hotson et al., 2014; Bleichner et al., 2016; Bundy et al., 2016; Wu et al., 2016). Hammer et al. suggested that LFC phase is more informative for motor decoding than LFC magnitude (Hammer et al., 2013). While LFC is highly informative for decoding, it can be easily contaminated by mechanical and electrical artifacts caused by the movements of the limbs and recording equipment. Because of this issue, a special care should be taken to minimize the artifacts, remove them from the data programmatically and ensure that they are not utilized for decoding.

Besides spectral band power modulations, within-band and across-band coupling features appear to be informative on movement intentions. Thus, Brunner et al. (2005) found extra information in the phase coupling between diﬀerent ECoG channels, measured as phase locking value (PLV). This method worked well when applied to the beta and gamma bands.

Several connectivity measures have been applied to the analysis of ECoG. Bayesian networks (TV-DBN) and eigenvector centrality analysis have been used to identify brain regions relevant to motor tasks (Newman et al., 2015). Benz et al. (2012) used TV-DBN to quantify task-related changes in connectivity and to decode hand kinematics. With this approach, higher accuracy was achieved compared to spectral feature decoders. Babiloni et al. (2017) utilized lagged linear connectivity (LLC) between several cortical areas in the delta-theta (<8 Hz) band to distinguish action execution from action observation.

- 4.2. Spatial Features Decoder accuracy is known to improve with increasing number of recording channels (Nicolelis and Lebedev, 2009). In addition to the mere number of channels, improvements in decoding can be gained by accounting for the spatial arrangement of recording sensors, such as the arrangement of electrodes in an ECoG grid. The procedure that improves decoding using the information about the electrode locations is referred to as spatial ﬁltering. Spatial ﬁlters treat diﬀerent ECoG channels as coordinates for multivariate data sampling. This coordinate system is transformed by the ﬁlter to improve decoding. For example, spatial ﬁltering could be used to reduce data dimensionality or improve separability of diﬀerent observations.

The initial spatial ﬁltering is usually accomplished with the reference schemes utilized during ECoG recordings. Common average reference (CAR) is typically used as a simple denoising technique (Schalk et al., 2007; Kubanek et al., 2009; Wang et al., 2012). This method reduces noise that is common to all recording channels but it does not handle channel-speciﬁc noise and it may also introduce noise into otherwise clean channels. Several alternative ﬁltering techniques have been proposed to address these problems. Morales-Flores et al. (2014) developed a non-supervised algorithm where the spatial ﬁlter coeﬃcients

are adjusted using a steepest descent method that minimizes the variance on diﬀerences of the linear combination of ECoG channels. This approach improved the decoding of ﬁnger ﬂexions from ECoG when compared to the data produced by CAR. Liu et al. (2015) considered the problem of the introduction of channel-speciﬁc noise when CAR is applied to the channel sets containing noisy channels. They tested several types of unsupervised spatial ﬁlters and techniques for detecting artifacts. After the noisy channels were automatically removed, data contamination was reduced. Moreover, they developed a median average reference ﬁlter that reduced channel-speciﬁc noise even when the noisy channels remained in the set.

Principal component analysis (PCA) is widely used in conjunction with spatial ﬁltering, primarily for dimensionality reduction (Freeman et al., 2000; Boye et al., 2008). This method transforms the original data into principal components, which are uncorrelated with each other and are created in such a way that the ﬁrst several components capture the largest possible amount of variance in the data. The principal components are quantitatively characterized in terms of how much variance (i.e., information contained in the data) they comprise. After the PCA transformation, the least informative (or least powerful) components can be discarded, reducing data dimensionality. This approach is, however, not optimal in the cases where information is present in the low-power features of the ECoG signal. In some cases, dimensionality reduction techniques, such as PCA, are applied not only to ECoG signals but also to motor parameters (Liu et al., 2010; Samiee et al., 2010; Hotson et al., 2014). This is particularly useful when movements are unconstrained. In this algorithm, the decoder ﬁrst generates output in PCA coordinates, and this output is then converted into the original coordinates. Canonical correlation analysis is another technique that can handle high multidimensionality of both ECoG and movement data. This method performs a linear transformation that maximizes the correlation between the ECoG activity and movements (Spüler et al., 2016).

Common spatial patterns (CSP) is a spatial ﬁltering technique that is often used in EEG- and ECoG-based BCIs to extract features that are useful for classiﬁcation (Kapeller et al., 2014, 2015; Xie et al., 2015; Jiang et al., 2017). When two classes of observations are used, CSP maximizes the ratio of their variances to increase the separability of the two classes. After the CSP transformation, dimensionality reduction can be carried out based on the separability of the two classes in diﬀerent dimensions. Additionally, CSP performs more robustly and exhibits better generalization properties when preceded by a separate dimension reduction step (Nicolae et al., 2017).

Source reconstruction methods are applicable to improve the performance of ECoG-based BCIs. The use of dynamical spatial features obtained from the reconstructed cortical current source density has been already shown to drastically improve the decoding accuracy in the MEG and EEG based BCIs where subjects generate outputs using motor imagery (Lin et al., 2013; Edelman et al., 2019). Raw ECoG recordings better reﬂect the surface distribution of cortical sources compared to non-invasive measurements (Schalk and Leuthardt, 2011). Yet, the activity of sources located deep in the sulci spreads into several recording

channels and therefore can not be assessed selectively in the raw data. As a solution to this problem, a suﬃciently ﬁne model can be built that describes the relationship between the activity of neuronal sources and the ECoG measurements (Gramfort et al.,

- 2010). Based on such forward model, reasonably accurate current source density reconstructions can be obtained for neuronal sources located within 1 cm from the cortical surface (Zhang

- et al., 2008; Pascarella et al., 2016; Todaro et al., 2018). We foresee that such reconstruction of sources from ECoG will be useful for BCI decoding by providing decoding algorithms with the inputs that discern the activity of more compact cortical areas compared raw ECoG data. To fully beneﬁt from this approach, care needs to be taken to accurately determine grid location with respect to the cortical surface. In addition to geometric calculations, the techniques exploiting functional data-driven methods based on maximizing model evidence (Henson et al., 2009) could improve the performance of these methods.

In addition to the methods described above that perform spatial ﬁltering and/or reduce data dimensionality (Gu et al., 2012), the decoding accuracy beneﬁts from techniques to determine the most informative features for classiﬁcation, such as requesting a certain separation in power for a certain ECoG spectral band for diﬀerent movements (Ryun et al., 2014), choosing features strongly correlated with the task (Leuthardt et al., 2004), successively adding features correlated to the class and not correlated to the previously selected features (Schalk et al., 2007), or choosing features according to a scatter-matrix based separability (Samiee et al., 2010). Several ﬁlter selection algorithms utilize a wrapper-based approach, where features are scored using the learning algorithm that is then used for regression or classiﬁcation (Gu et al., 2012). In this approach, the feature set is enhanced in consecutive steps, where features are added to the previous feature set to improve decoding accuracy estimated with cross-validation (Liang and Bougrain, 2012; Wang et al., 2012; Elgharabawy and Wahed, 2016; Li

- et al., 2017). When following these strategies, one should bear in mind that ECoG features assumed to be useful could be contaminated by noise that is accidentally correlated to the parameters being decoded.

- 4.3. Classiﬁcation and Regression Starting with the report of Levine et al. (1999) on movementrelated ECoG patterns, pattern matching techniques have been applied to derive motor commands from ECoG recordings. Thus, movement-related ECoG desynchronization was detected using an average ECoG template and cross-correlating it with ECoG samples (Huggins et al., 1999). More complex features can be used for the same purpose (Graimann et al., 2003). Such patternmatching approach has been successfully used to classify multiple movement types (Bleichner et al., 2016) and to implement BCI control (Levine et al., 2000).

As explained above, the capacity to generalize to new data is essential for both classiﬁcation and regression algorithms. Since the number of features is often large, regularization methods are applied to prevent overﬁtting. Algorithms with fewer parameters are less susceptible to overﬁtting and often perform no worse than more complex algorithms (Marjaninejad et al., 2017).

For decoding ECoG into discrete classes, linear discriminant analysis (LDA) is often used (Ball et al., 2009; Samiee et al., 2010; Pistohl et al., 2012; Xie et al., 2015; Bleichner et al., 2016; Jiang et al., 2017). Classiﬁcation can be performed as well using other algorithms, such as k-nearest neighbor method (Chin et al., 2007; Samiee et al., 2010; Paul et al., 2017) and Naïve Bayes classiﬁer (Chestek et al., 2013).

Support vector machines (SVM) is another class of models that solve the problem of separating samples of diﬀerent classes by maximizing the margin between them. This group of algorithms is versatile and allows constructing highly nonlinear decision surfaces. Linear kernel is often used to prevent overﬁtting and ensure robustness (Yanagisawa et al., 2009, 2011; Ryun et al., 2014; Elgharabawy and Wahed, 2016). Additionally, radial basis functions can be employed (Wang et al., 2012). The disadvantage of this approach is that kernel selection remains largely heuristic and is usually performed via some sort of crossvalidation that requires additional data.

For continuous decoding of motor parameters from ECoG, linear models are often used, including linear regression (Schalk et al., 2007; Liang and Bougrain, 2012; Hammer et al., 2013; Hotson et al., 2014; Gunduz et al., 2016) and its modiﬁcations designed to reduce overﬁtting (Kubanek et al., 2009; Nakanishi et al., 2013). Sanchez et al. used the Wiener ﬁlter, a linear model, to decode movement trajectory (Sanchez et al., 2008). Pistohl et al. (2008) and Kellis et al. (2012) utilized the Kalman ﬁlter, which better handles non-stationary inputs. Wang et al. (2012) employed a modiﬁcation of dynamic Bayesian network to capture non-stationarity in the temporal and spatial ECoG characteristics.

Several studies utilized prior knowledge of the task performance to improve decoding. Schalk and Leuthardt (2011) developed a Bayesian decoding model that incorporated constraints on ﬁnger ﬂexion. Wu et al. (2016) employed a hidden Markov model that highlighted rhythmic task behavior. Saa et al. (2016) enhanced their decoding algorithms with the assumption that subjects do not perform rapid changes between movement and rest.

Hierarchical algorithms (i.e., the ones that stack several models) are often used to enable online BCI tasks. In these schemes, diﬀerent regression and classiﬁcation tasks are performed in a certain order (Figure 2C). Yanagisawa et al. (2011) and Hotson et al. (2016) used a hierarchical algorithm, where one model classiﬁed between rest and movement and detected movement onset and the second model classiﬁes movement type. In several studies, switching between regression models was performed based on a classiﬁcation algorithm (Flamary and Rakotomamonjy, 2012; Bundy et al., 2016; Elgharabawy and Wahed, 2016). Additionally, Chen et al. developed an algorithm where the output of one model was used to weigh the output of the other model to improve prediction accuracy (Chen et al., 2014).

Artiﬁcial neural networks are the class of algorithms that handle complex, non-stationary patterns of brain activity. They can be applied to both classiﬁcation and regression problems. The primary advantage of artiﬁcial neural networks is their versatility. With suﬃcient number of model parameters (units or neurons),

complex neural patterns can be processed. While shallow neural networks with few layers are useful for decoding, during the last several years deep neural networks containing many layers have signiﬁcantly advanced. Advantages of deep learning models include their ability to automatically extract features useful for decoding rather than hand-engineering them (Figure 2B) and to generate representations at multiple levels of abstraction.

Deep learning is rapidly gaining popularity as a BCI decoding method. In the last few years, deep learning algorithms have been applied to ECoG data processing (Roy et al., 2019), seizure forecasting (Meisel and Bailey, 2019), language mapping (RaviPrakash et al., 2018), and speech decoding (Livezey et al., 2018; Angrick et al., 2019a,b). Several studies have already employed deep learning for decoding movements from ECoG. Xie et al. (2018) decoded ﬁnger trajectory with high accuracy using LSTM recurrent neural network. Du et al. (2018) applied LSTM to the same data and implemented real-time control of a robotic arm. Wang et al. (2018) employed a deep model to detect the upper body joints movement based on both ECoG recordings and video data. Pan et al. used recurrent neural networks that recognized temporal dependencies in ECoG signal for rapid and robust gesture decoding (Pan

- et al., 2018). We foresee further and fruitful development of deep learning approaches for ECoG-based BCIs. This is because of several advantages of this approach. Deep learning architectures applied to electrophysiological data (Roy et al.,
- 2019) perform on par or slightly better than the classical algorithms and do not require neural features to be deﬁned upfront. While such automated processing can be considered as an advantage, BCI researchers still would want to better understand the processing chain performed by a deep learning algorithm, and ideally to relate the processing steps to certain physiological characteristics of the recorded neural signals. Such understanding of the representation of information deep architectures employed for decoding purposes is crucial in order to assess validity of the obtained solutions (Hammer et al., 2013). Thus, it is important to understand the contribution to decoding from diﬀerent types of neuronal activity, such high-frequency ECoG components better corresponding to neuronal discharges and low-frequency ECoG reﬂecting synchronization of large neuronal populations (Aoki et al., 1999; Chestek et al., 2013). Additionally, one needs to be able to distinguish causal decoding that captures commands generated by the brain from the decoding based on the peripheral reaﬀerent signals resulting from overt behaviors (Livezey et al., 2019). With a better understanding of these functional relationships, BCI developers can make full use of the information carried by the neural signals, avoid inadvertent uses of informational confounds, establish practical utility of their algorithmic solutions, and gain fundamental neurophysiological insights.

## 5. SOFTWARE

ECoG-based BCIs can be implemented using several currently available software packages that perform real-time processing of multichannel neural data. OpenVIBE (Renard et al., 2010)

is one popular project that oﬀers tools for visual programming and scripting signal processing pipelines. Experimental task descriptions are saved as XML ﬁles. OpenVIBE is closed source software. Another popular closed source package for implementing BCIs is BCI2000 (Schalk et al., 2004). BCI2000 is written in C/C++. It incorporates several algorithms for processing multichannel recordings. In our laboratory, we have recently developed NFBLab1, an open-source software written in Python for implementing a variety of BCI designs (Smetanin et al., 2018b). This software accepts ECoG signals as inputs, as well as EEG and MEG recordings and synchronizes them with motion-tracking information and other multimodal data. Lab Streaming Layer2 protocol is used to interface NFBLab to data acquisition devices. NFBLab implements temporal and spatial ﬁlters for selecting signal feature and removing artifacts. Inverse solvers that generate source-space representation of multichannel inputs are implemented via an interface to MNE-Python software (Gramfort et al., 2014). Additionally, NFBLab incorporates algorithms that reduce processing latency (Smetanin et al., 2018a).

Several standard general purpose libraries are available for implementing deep learning approaches, such as PyTorch, TensorFlow, and Keras. Currently, only a few wrappers are available implementing speciﬁc functions that facilitate electrophysiological data processing. The Braindecode toolbox by Schirrmeister et al. (2017) is based on PyTorch and supports trialwise and cropped decoding of raw EEG data. This toolbox is applicable to ECoG data. A novel software package MNEFlow for dealing with EEG/MEG data is currently being developed3 with three architectures implemented so far: LFCNN, VARCNN (Zubarev et al., 2018), and EEGNet. The latter architecture (Lawhern et al., 2018) implements a compact convolutional network; it is available for download4. While these libraries have not been developed to speciﬁcally process ECoG, they can be rapidly adapted to process ECoG data.

The developers of decoding algorithms can utilize open ECoG datasets containing data from movement and motor imagery tasks. For instance, dataset 4 from international BCI competition IV5 contains data for ﬁnger movements. This dataset is often used as a benchmark for BCI decoders that classify the ﬁnger being moved and/or perform continuous reconstruction of ﬁnger movements. The other ECoG dataset from BCI competition III6 contains recordings from several experimental sessions, so it is useful for testing how well a BCI decoder generalizes from one session to another. Researches from Brunton Lab made available a large annotated dataset7 containing longterm ECoG recording along with joint kinematics. Stanford Collection of ECoG Data8 includes recordings from 250 subjects conducted over an 8-years period. This dataset includes ECoG

- 1https://github.com/nikolaims/nfb/wiki/Experiment-ﬁle-structure
- 2https://github.com/sccn/labstreaminglayer
- 3https://mneﬂow.readthedocs.io
- 4https://github.com/vlawhern/arl-eegmodels
- 5http://www.bbci.de/competition/iv/
- 6http://www.bbci.de/competition/iii/
- 7https://www.bingbrunton.com/data
- 8https://purl.stanford.edu/zk881ps0522

recordings from the sensorimotor cortex in patients performing motor tasks.

## 6. DISCUSSION

Over the last two decades we observe a growing number of ECoG-based BCI studies in patients who underwent implantation for clinical purposes. This research is clinically relevant and holds promise to provide new treatments for people suﬀering from severe motor and sensory disabilities caused by such conditions as spinal cord injury, stroke and amyotrophic lateral sclerosis. At the same time, these studies have already provided beneﬁts to the patients and materialized in take-home BCI systems for text-dialing purposes (Brunner et al., 2011), novel safer solutions for passive speech mapping of eloquent cortex during neurosurgery (Taplin et al., 2016; Sinkin et al., 2019) and wireless ECoG devices (Matsushita et al., 2018) that reduce septic risks and can be employed for chronic monitoring of patients with epilepsy. In recent years, it has become clear that ECoG-based BCIs are a viable approach to restoration and rehabilitation of motor functions. ECoG recordings are useful for decoding such motor parameters as movement onset (Wang et al., 2012; Pistohl et al., 2013), movement type (Pistohl et al., 2012; Ryun et al., 2014), and limb trajectory (Pistohl et al., 2008; Nakanishi et al., 2013; Eliseyev and Aksenova, 2014; Xie et al., 2018). These decoded signals can be then sent to external devices, such as hand prosthesis with many degrees of freedom (Yanagisawa et al., 2011; Hotson et al., 2016) or a lower-limb exoskeleton (Vansteensel et al., 2016; Benabid et al., 2019). ECoGbased BCIs can control two-dimensional and three-dimensional movements of a cursor or a prosthetic arm (Anderson et al., 2012; Yanagisawa et al., 2012). Several kinematic parameters can be extracted from ECoG, including position, velocity, and acceleration (Hammer et al., 2013). Extrinsic variables, such as target location, can also be also decoded from ECoG and utilized for BCI control (Nakanishi et al., 2017). The recently developed fully implantable ECoG-based BCIs (Vansteensel et al., 2016; Benabid et al., 2019) have extended the functionality of such systems as they enable long-term operations and engage cortical plasticity. With the rapid development of new technologies for high-ﬁdelity ECoG recordings (Viventi et al., 2011; Akinwande et al., 2014; Khodagholy et al., 2015) and of neural decoding methods (Faust et al., 2018; Richards et al., 2019), ECoG-based BCIs will likely continue to improve.

ECoG-based BCIs are clinically relevant due to their safety as compared to the intracortical implants (e.g., Utah array) and have a better spatial and temporal resolution than noninvasive, EEG-based BCIs. At the same time, the ECoG grids cover relatively cortical areas which allows to take advantage of the spatial-temporal encoding principles implemented by the brain. Such large-scale recordings improve BCI accuracy by allowing for simultaneous access to the information processed by many brain regions involved in programming and execution of movements.

Broad spectral and spatial extent of ECoG recordings open the opportunity to explore at various scales interregional interactions between and within several frequency bands from delta-band (Gunduz et al., 2016) correlates of movement, desynchronization in the alpha and beta bands in spatially distributed taskrelevant cortical areas to more localized synchronization in the high gamma range and cross-frequency coupling between bands and speciﬁc cytoarchitectonic assemblies. This ﬂexibility leads to signiﬁcant variability in the choice of features, decoded parameters and decoding models witnessed in the range of described ECoG studies. Thus, depending on the clinical needs, diﬀerent ECoG components and associated neurophysiological phenomena can be utilized in practical BCI system.

In recent years, an active development of the decoding algorithms is underway. Several strategies have been particularly useful, including switching models, adapting algorithms, and the decoders utilizing prior information on movement characteristics and the nature of physiological processes. Even more versatile methods are currently being developed, such as those based on deep learning which allows for capturing complex relationship between motor parameters and ECoG characteristics.

We foresee that the next series of major advances will be made in bidirectional BCI technology that combines motorcontrol loops with sensory feedback provided by cortical stimulation and/or sensory substitution methods (Wilson et al., 2012; Cronin et al., 2016; Hiremath et al., 2017). The development of bidirectional ECoG-based BCIs will bring new challenges for modeling the complex relationships between ECoG signals and diﬀerent motor and sensory parameters. Previous studies have reported a range of promising results regarding the possibility of building BCIs that employ ECoG recordings to enable motor functions. With the rapid developments in ECoG technologies (Shokoueinejad et al., 2019), surgical implantation procedures and mathematical algorithms for neural decoding, it is reasonable to expect that a variety of practical, fully-implantable (Vansteensel et al., 2016) ECoG-based neural prostheses will emerge for enabling motor and sensory functions to neurologically impaired patients.

## AUTHOR CONTRIBUTIONS

KV wrote the ﬁrst draft of the manuscript. KV, ML, AK, and AO revised the manuscript. All authors contributed to the ﬁnal revision, read, and approved the submitted version.

## FUNDING

This study has been funded by the Center for Bioelectric Interfaces NRU Higher School of Economics, RF Government grant, AG. No. 14.641.31.0003.

## REFERENCES

Acharya, S., Fifer, M. S., Benz, H. L., Crone, N. E., and Thakor, N. V. (2010). Electrocorticographic amplitude predicts ﬁnger positions during slow grasping motions of the hand. J. Neural Eng. 7:046002. doi: 10.1088/1741-2560/7/4/046002

Akinwande, D., Petrone, N., and Hone, J. (2014). Two-dimensional ﬂexible nanoelectronics. Nat. Commun. 5:5678. doi: 10.1038/ncomms6678

Akram, F., Han, H.-S., and Kim, T.-S. (2014). A p300-based brain computer interface system for words typing. Comput. Biol. Med. 45, 118–125. doi: 10.1016/j.compbiomed.2013.12.001

Andersen, R. A., Burdick, J. W., Musallam, S., Pesaran, B., and Cham, J. G. (2004). Cognitive neural prosthetics. Trends Cogn. Sci. 8, 486–493. doi: 10.1016/j.tics.2004.09.009

Andersen, R. A., Hwang, E. J., and Mulliken, G. H. (2010). Cognitive neural prosthetics. Annu. Rev. Psychol. 61, 169–190. doi: 10.1146/annurev.psych.093008.100503

Anderson, N. R., Blakely, T., Schalk, G., Leuthardt, E. C., and Moran, D. W. (2012). Electrocorticographic (ECoG) correlates of human arm movements. Exp. Brain Res. 223, 1–10. doi: 10.1007/s00221-012-3226-1

Angrick, M., Herﬀ, C., Johnson, G., Shih, J., Krusienski, D., and Schultz, T. (2019a). Interpretation of convolutional neural networks for speech spectrogram regression from intracranial recordings. Neurocomputing 342, 145–151. doi: 10.1016/j.neucom.2018.10.080

Angrick, M., Herﬀ, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. (2019b). Speech synthesis from ECoG using densely connected 3d convolutional neural networks. J. Neural Eng. 16:036019. doi: 10.1088/1741-2552/ab0c59

Aoki, F., Fetz, E. E., Shupe, L., Lettich, E., and Ojemann, G. A. (1999). Increased gamma-range activity in human sensorimotor cortex during performance of visuomotor tasks. Clin. Neurophysiol. 110, 524–537. doi: 10.1016/S1388-2457(98)00064-9

Babiloni, C., Del Percio, C., Lopez, S., Di Gennaro, G., Quarato, P. P., Pavone, L., et al. (2017). Frontal functional connectivity of electrocorticographic delta and theta rhythms during action execution versus action observation in humans. Front. Behav. Neurosci. 11:20. doi: 10.3389/fnbeh.2017.00020

Babyak, M. A. (2004). What you see may not be what you get: a brief, nontechnical introduction to overﬁtting in regression-type models. Psychosom. Med. 66, 411–421. doi: 10.1097/00006842-200405000-00021

Badia, S. B., García Morgade, A., Samaha, H., and Verschure, P. F. (2013). Using a hybrid brain computer interface and virtual reality system to monitor and promote cortical reorganization through motor activity and motor imagery training. IEEE Trans. Neural Syst. Rehabil. Eng. 21, 174–181. doi: 10.1109/TNSRE.2012.2229295

Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2009). Diﬀerential representation of arm movement direction in relation to cortical anatomy and function. J. Neural Eng. 6:016006. doi: 10.1088/1741-2560/6/1/016006

Benabid, A. L., Costecalde, T., Eliseyev, A., Charvet, G., Verney, A., Karakas, S., et al. (2019). An exoskeleton controlled by an epidural wireless brain–machine interface in a tetraplegic patient: a proof-of-concept demonstration. Lancet Neurol. 18, P1112–1122. doi: 10.1016/S1474-4422(19)30321-7

Bensmaia, S. J., and Miller, L. E. (2014). Restoring sensorimotor function through intracortical interfaces: progress and looming challenges. Nat. Rev. Neurosci. 15:313. doi: 10.1038/nrn3724

Benz, H. L., Zhang, H., Bezerianos, A., Acharya, S., Crone, N. E., Zheng, X., et al. (2012). Connectivity analysis as a novel approach to motor decoding for prosthesis control. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 143–152. doi: 10.1109/TNSRE.2011.2175309

Blakely, T., Miller, K. J., Zanos, S. P., Rao, R. P., and Ojemann, J. G. (2009). Robust, long-term control of an electrocorticographic brain-computer interface with ﬁxed parameters. Neurosurg. Focus 27:E13. doi: 10.3171/2009.4.FOCUS0977 Bleichner, M. G., Freudenburg, Z. V., Jansma, J. M., Aarnoutse, E. J., Vansteensel, M. J., and Ramsey, N. F. (2016). Give me a sign: decoding four complex hand gestures based on high-density ECoG. Brain Struct. Funct. 221, 203–216. doi: 10.1007/s00429-014-0902-x

Bouton, C. E., Shaikhouni, A., Annetta, N. V., Bockbrader, M. A., Friedenberg, D. A., Nielson, D. M., et al. (2016). Restoring cortical control of functional movement in a human with quadriplegia. Nature 533:247. doi: 10.1038/nature17435

Boye, A. T., Kristiansen, U. Q., Billinger, M., do Nascimento, O. F., and Farina, D. (2008). Identiﬁcation of movement-related cortical potentials with optimized spatial ﬁltering and principal component analysis. Biomed. Signal Process. Control 3, 300–304. doi: 10.1016/j.bspc.2008.05.001

Branco, M. P., Freudenburg, Z. V., Aarnoutse, E. J., Bleichner, M. G., Vansteensel, M. J., and Ramsey, N. F. (2017). Decoding hand gestures from primary somatosensory cortex using high-density ECoG. Neuroimage 147, 130–142. doi: 10.1016/j.neuroimage.2016.12.004

Brandman, D. M., Cash, S. S., and Hochberg, L. R. (2017). human intracortical recording and neural decoding for brain–computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 25, 1687–1696. doi: 10.1109/TNSRE.2017.2677443 Brunner, C., Graimann, B., Huggins, J. E., Levine, S. P., and Pfurtscheller, G. (2005). Phase relationships between diﬀerent subdural electrode recordings in man. Neurosci. Lett. 375, 69–74. doi: 10.1016/j.neulet.2004.11.052

Brunner, P., Ritaccio, A. L., Emrich, J. F., Bischof, H. and Schalk, G. (2011). Rapid communication with a “p300” matrix speller using electrocorticographic signals (ECoG). Front. Neurosci. 5:5. doi: 10.3389/fnins.2011.00005

Brunner, P., Ritaccio, A. L., Lynch, T. M., Emrich, J. F., Wilson, J. A., Williams, J. C., et al. (2009). A practical procedure for real-time functional mapping of eloquent cortex using electrocorticographic signals in humans. Epilepsy Behav. 15, 278–286. doi: 10.1016/j.yebeh.2009.04.001

Bruurmijn, M. L. C. M., Pereboom, I. P. L., Vansteensel, M. J., Raemaekers, M. A. H., and Ramsey, N. F. (2017). Preservation of hand movement representation in the sensorimotor areas of amputees. Brain 140, 3166–3178. doi: 10.1093/brain/awx274

Bundy, D. T., Pahwa, M., Szrama, N., and Leuthardt, E. C. (2016). Decoding three-dimensional reaching movements using electrocorticographic signals in humans. J. Neural Eng. 13:026021. doi: 10.1088/1741-2560/13/2/026021

Bundy, D. T., Zellmer, E., Gaona, C. M., Sharma, M., Szrama, N., Hacker, C., et al. (2014). Characterization of the eﬀects of the human dura on macro-and micro-electrocorticographic recordings. J. Neural Eng. 11:016006. doi: 10.1088/1741-2560/11/1/016006

Buzsáki, G., Anastassiou, C. A., and Koch, C. (2012). The origin of extracellular ﬁelds and currents—EEG, ECoG, LFP and spikes. Nat. Rev. Neurosci. 13:407. doi: 10.1038/nrn3241

Carmena, J. M., Lebedev, M. A., Crist, R. E., O’Doherty, J. E., Santucci, D. M., Dimitrov, D. F., et al. (2003). Learning to control a brain– machine interface for reaching and grasping by primates. PLoS Biol. 1:e42. doi: 10.1371/journal.pbio.0000042

Chai, R., Tran, Y., Craig, A., Ling, S. H., and Nguyen, H. T. (2014). Enhancing accuracy of mental fatigue classiﬁcation using advanced computational intelligence in an electroencephalography system. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 1318–1341. doi: 10.1109/EMBC.2014.6943846

Chapin, J. K., Moxon, K. A., Markowitz, R. S., and Nicolelis, M. A. (1999). Realtime control of a robot arm using simultaneously recorded neurons in the motor cortex. Nat. Neurosci. 2:664. doi: 10.1038/10223

Chaudhary, U., Birbaumer, N., and Ramos-Murguialday, A. (2016). Brain– computer interfaces in the completely locked-in state and chronic stroke. Prog. Brain Res. 228, 131–161. doi: 10.1016/bs.pbr.2016.04.019

Chavarriaga, R., Sobolewski, A., Leeb, R., Pralong, E., Bloch, J., and Millán, J. D. R. (2016). “Reliable BMI control using epidural ECoG by an hemiplegic user,” in Proceedings of the 6th International Brain-Computer Interface Meeting Number EPFL-CONF-218936 (Asilomar, CA), 86.

Chen, W., Liu, X., and Litt, B. (2014). Logistic-weighted regression improves decoding of ﬁnger ﬂexion from electrocorticographic signals. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 2629–2632. doi: 10.1109/EMBC.2014. 6944162

Chestek, C. A., Gilja, V., Blabe, C. H., Foster, B. L., Shenoy, K. V., Parvizi, J., et al. (2013). Hand posture classiﬁcation using electrocorticography signals in the gamma band over human sensorimotor brain areas. J. Neural Eng. 10:026002. doi: 10.1088/1741-2560/10/2/026002

Chin, C. M., Popovic, M. R., Thrasher, A., Cameron, T., Lozano, A., and Chen, R. (2007). Identiﬁcation of arm movements using correlation of electrocorticographic spectral components and kinematic recordings. J. Neural Eng. 4:146. doi: 10.1088/1741-2560/4/2/014

Collinger, J. L., Vinjamuri, R., Degenhart, A. D., Weber, D. J., Sudre, G. P., Boninger, M. L., et al. (2014). Motor-related brain activity during action observation: a neural substrate for electrocorticographic brain-computer interfaces after spinal cord

injury. Front. Integr. Neurosci. 8:17. doi: 10.3389/fnint.2014. 00017

Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber, D. J., et al. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. Lancet 381, 557–564. doi: 10.1016/S0140-6736(12)61816-9

Contreras-Vidal, J. L., and Grossman, R. G. (2013). Neurorex: a clinical neural interface roadmap for EEG-based brain machine interfaces to a lower body robotic exoskeleton. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2013, 1579–1582. doi: 10.1109/EMBC.2013.6609816

Cooper, R., Winter, A. L., Crow, H. J., and Walter, W. G. (1965). Comparison of subcortical, cortical and scalp activity using chronically indwelling electrodes in man. Clin. Neurophysiol. 18, 217–228. doi: 10.1016/0013-4694(65) 90088-X

Cronin, J. A., Wu, J., Collins, K. L., Sarma, D., Rao, R. P., Ojemann, J. G., et al. (2016). Task-speciﬁc somatosensory feedback via cortical stimulation in humans. IEEE Trans. Haptics 9, 515–522. doi: 10.1109/TOH.2016.2591952

Das, B., Talukdar, M., Sarma, R., and Hazarika, S. M. (2016). Multiple feature extraction of electroencephalograph signal for motor imagery classiﬁcation through bispectral analysis. Proc. Comput. Sci. 84, 192–197. doi: 10.1016/j.procs.2016.04.086

Degenhart, A. D., Hiremath, S. V., Yang, Y., Foldes, S., Collinger, J. L., Boninger, M., et al. (2018). Remapping cortical modulation for electrocorticographic brain–computer interfaces: a somatotopy-based approach in individuals with upper-limb paralysis. J. Neural Eng. 15:026021. doi: 10.1088/1741-2552/aa9bfb

Delgado Saa, J. F., De Pesters, A., and Cetin, M. (2016). Asynchronous decoding of ﬁnger movements from ECoG signals using long-range dependencies conditional random ﬁelds. J. Neural Eng. 13:036017. doi: 10.1088/1741-2560/13/3/036017

Dobelle, W. H. (2000). Artiﬁcial vision for the blind by connecting a television camera to the visual cortex. ASAIO J. 46, 3–9. doi: 10.1097/00002480-200001000-00002

Du, A., Yang, S., Liu, W., and Huang, H. (2018). “Decoding ECoG signal with deep learning model based on LSTM,” in TENCON 2018–2018 IEEE Region 10 Conference (Jeju: IEEE), 430–435.

Edelman, B. J., Meng, J., Suma, D., Zurn, C., Nagarajan, E., Baxter, B. S., et al. (2019). Noninvasive neuroimaging enhances continuous neural tracking for robotic device control. Sci. Robot. 4:eaaw6844. doi: 10.1126/scirobotics.aaw6844

Elgharabawy, A., and Wahed, M. A. (2016). “Decoding of ﬁnger movement using kinematic model classiﬁcation and regression model switching,” in 2016 8th Cairo International Biomedical Engineering Conference (CIBEC) (Cairo: IEEE), 84–89.

Elghrabawy, A., and Wahed, M. (2012). “Prediction of ﬁve-class ﬁnger ﬂexion using ECoG,” in Cairo International Biomedical Engineering Conference (Giza).

Eliseyev, A., and Aksenova, T. (2014). Stable and artifact-resistant decoding of 3d hand trajectories from ECoG signals using the generalized additive model. J. Neural Eng. 11:066005. doi: 10.1088/1741-2560/11/6/066005

Faust, O., Hagiwara, Y., Hong, T. J., Lih, O. S., and Acharya, U. R. (2018). Deep learning for healthcare applications based on physiological signals: a review. Comput. Methods Programs Biomed. 161, 1–13. doi: 10.1016/j.cmpb.2018.04.005

Fifer, M. S., Acharya, S., Benz, H. L., Mollazadeh, M., Crone, N. E., and Thakor, N. V. (2012). Toward electrocorticographic control of a dexterous upper limb prosthesis: building brain-machine interfaces. IEEE Pulse 3, 38–42. doi: 10.1109/MPUL.2011.2175636

Fitzsimmons, N. A., Lebedev, M. A., Peikon, I. D., and Nicolelis, M. A. (2009). Extracting kinematic parameters for monkey bipedal walking from cortical neuronal ensemble activity. Front. Integr. Neurosci. 3:3. doi: 10.3389/neuro.07.003.2009

Flamary, R., and Rakotomamonjy, A. (2012). Decoding ﬁnger movements from ECoG signals using switching linear models. Front. Neurosci. 6:29. doi: 10.3389/fnins.2012.00029

Flint, R. D., Rosenow, J. M., Tate, M. C., and Slutzky, M. W. (2016). Continuous decoding of human grasp kinematics using epidural and subdural signals. J. Neural Eng. 14:016005. doi: 10.1088/1741-2560/14/1/016005

Freeman, W. J., Rogers, L. J., Holmes, M. D., and Silbergeld, D. L. (2000). Spatial spectral analysis of human electrocorticograms including the alpha and

gamma bands. J. Neurosci. Methods 95, 111–121. doi: 10.1016/S0165-0270(99) 00160-0

Galán, F., Nuttin, M., Lew, E., Ferrez, P. W., Vanacker, G., Philips, J., et al. (2008). A brain-actuated wheelchair: asynchronous and non-invasive brain–computer interfaces for continuous control of robots. Clin. Neurophysiol. 119, 2159–2169. doi: 10.1016/j.clinph.2008.06.001

Gancet, J., Ilzkovitz, M., Cheron, G., Ivanenko, Y., Van Der Kooij, H., Van Der Helm, F., et al. (2011). “Mindwalker: a brain controlled lower limbs exoskeleton for rehabilitation. potential applications to space,” in 11th Symposium on Advanced Space Technologies in Robotics and Automation (Noordwijk), 12–14.

Georgopoulos, A. P., Kalaska, J. F., Caminiti, R., and Massey, J. T. (1982). On the relations between the direction of two-dimensional arm movements and cell discharge in primate motor cortex. J. Neurosci. 2, 1527–1537.

Gharabaghi, A., Naros, G., Walter, A., Roth, A., Bogdan, M., Rosenstiel, W., et al. (2014). Epidural electrocorticography of phantom hand movement following long-term upper-limb amputation. Front. Hum. Neurosci. 8:285. doi: 10.3389/fnhum.2014.00285

Gilja, V., Nuyujukian, P., Chestek, C. A., Cunningham, J. P., Byron, M. Y., Fan, J. M., et al. (2012). A high-performance neural prosthesis enabled by control algorithm design. Nat. Neurosci. 15:1752. doi: 10.1038/nn.3265

Gilja, V., Pandarinath, C., Blabe, C. H., Nuyujukian, P., Simeral, J. D., Sarma, A. A., et al. (2015). Clinical translation of a high-performance neural prosthesis. Nat. Med. 21:1142. doi: 10.1038/nm.3953

Göhring, D., Latotzky, D., Wang, M., and Rojas, R. (2013). “Semi-autonomous car control using brain computer interfaces,” in Intelligent Autonomous Systems 12 (Jeju Island: Springer), 393–408.

Graimann, B., Huggins, J. E., Schlögl, A., Levine, S. P., and Pfurtscheller, G. (2003). Detection of movement-related patterns in ongoing single-channel electrocorticogram. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 276–281. doi: 10.1109/TNSRE.2003.816863

Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., et al. (2014). Mne software for processing MEG and EEG data. Neuroimage 86, 446–460. doi: 10.1016/j.neuroimage.2013.10.027

Gramfort, A., Papadopoulo, T., Olivi, E., and Clerc, M. (2010). Openmeeg: opensource software for quasistatic bioelectromagnetics. Biomed. Eng. Online 9:45. doi: 10.1186/1475-925X-9-45

Gu, Q., Li, Z., and Han, J. (2012). Generalized ﬁsher score for feature selection. arXiv [Preprint]. arXiv:1202.3725.

Gunduz, A., Brunner, P., Sharma, M., Leuthardt, E. C., Ritaccio, A. L., Pesaran, B., et al. (2016). Diﬀerential roles of high gamma and local motor potentials for movement preparation and execution. Brain Comput. Interfaces 3, 88–102. doi: 10.1080/2326263X.2016.1179087

Hammer, J., Fischer, J., Ruescher, J., Schulze-Bonhage, A., Aertsen, A., and Ball, T. (2013). The role of ECoG magnitude and phase in decoding position, velocity, and acceleration during continuous motor behavior. Front. Neurosci. 7:200. doi: 10.3389/fnins.2013.00200

Hazrati, M. K., and Hofmann, U. G. (2012). Decoding ﬁnger movements from ECoG signals using empirical mode decomposition. Biomed. Eng. 57, 650–653. doi: 10.1515/bmt-2012-4489

Henson, R. N., Mattout, J., Phillips, C., and Friston, K. J. (2009). Selecting forward models for MEG source-reconstruction using model-evidence. Neuroimage 46, 168–176. doi: 10.1016/j.neuroimage.2009.01.062

Hill, N. J., Gupta, D., Brunner, P., Gunduz, A., Adamo, M. A., Ritaccio, A., et al. (2012). Recording human electrocorticographic (ECoG) signals for neuroscientiﬁc research and real-time functional cortical mapping. J. Vis. Exp. 64:e3993. doi: 10.3791/3993

Hiremath, S. V., Tyler-Kabara, E. C., Wheeler, J. J., Moran, D. W., Gaunt, R. A., Collinger, J. L., et al. (2017). Human perception of electrical stimulation on the surface of somatosensory cortex. PLoS ONE 12:e0176020. doi: 10.1371/journal.pone.0176020

Hochberg, L. R., Bacher, D., Jarosiewicz, B., Masse, N. Y., Simeral, J. D., Vogel, J., et al. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485:372. doi: 10.1038/nature11076

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., et al. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442:164. doi: 10.1038/nature 04970

Hotson, G., Fifer, M. S., Acharya, S., Benz, H. L., Anderson, W. S., Thakor, N. V., et al. (2014). Coarse electrocorticographic decoding of ipsilateral reach in patients with brain lesions. PLoS ONE 9:e115236. doi: 10.1371/journal.pone.0115236

Hotson, G., McMullen, D. P., Fifer, M. S., Johannes, M. S., Katyal, K. D., Para, M. P., et al. (2016). Individual ﬁnger control of a modular prosthetic limb using high-density electrocorticography in a human subject. J. Neural Eng. 13:026017. doi: 10.1088/1741-2560/13/2/026017

House, W. F. (1976). Cochlear implants. Ann. Otol. Rhinol. Laryngol. 85, 3–3. Huggins, J. E., Levine, S. P., BeMent, S. L., Kushwaha, R. K., Schuh, L. A., Passaro,

E. A., et al. (1999). Detection of event-related potentials for development of a direct brain interface. J. Clin. Neurophysiol. 16:448.

Hughes, S. W., and Crunelli, V. (2005). Thalamic mechanisms of EEG alpha rhythms and their pathological implications. Neuroscientist 11, 357–372. doi: 10.1177/1073858405277450

Jiang, T., Ince, N. F., Jiang, T., Wang, T., Mei, S., Li, Y., et al. (2015). “Investigation of the spatial and spectral patterns of hand extension/ﬂexion using high-density ECoG,” in 2015 7th International IEEE/EMBS Conference on Neural Engineering (NER) (Milan: IEEE), 589–592.

Jiang, T., Jiang, T., Wang, T., Mei, S., Liu, Q., Li, Y., et al. (2017). Characterization and decoding the spatial patterns of hand extension/ﬂexion using high-density ECoG. IEEE Trans. Neural Syst. Rehabil. Eng. 25, 370–379. doi: 10.1109/TNSRE.2016.2647255

Kapeller, C., Gergondet, P., Kamada, K., Ogawa, H., Takeuchi, F., Ortner, R., et al. (2015). Online control of a humanoid robot through hand movement imagination using CSP and ECoG based features. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2015, 1765–1768. doi: 10.1109/EMBC.2015.7318720

Kapeller, C., Schneider, C., Kamada, K., Ogawa, H., Kunii, N., Ortner, R., et al. (2014). Single trial detection of hand poses in human ECoG using CSP based feature extraction. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 4599–4602. doi: 10.1109/EMBC.2014.6944648

Kellis, S., Hanrahan, S., Davis, T., House, P. A., Brown, R., and Greger, B. (2012). Decoding hand trajectories from micro-electrocorticography in human patients. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 4091–4094. doi: 10.1109/EMBC.2012.6346866

Kellis, S., Sorensen, L., Darvas, F., Sayres, C., O’Neill, K., Brown, R. B., et al. (2016). Multi-scale analysis of neural activity in humans: implications for micro-scale electrocorticography. Clin. Neurophysiol. 127, 591–601. doi: 10.1016/j.clinph.2015.06.002

Khodagholy, D., Gelinas, J. N., Thesen, T., Doyle, W., Devinsky, O., Malliaras, G. G., et al. (2015). Neurogrid: recording action potentials from the surface of the brain. Nat. Neurosci. 18:310. doi: 10.1038/nn.3905

Kim, G. H., Kim, K., Lee, E., An, T., Choi, W., Lim, G., et al. (2018). Recent progress on microelectrodes in neural interfaces. Materials 11:1995. doi: 10.3390/ma11101995

Kubánek, J., Miller, K. J., Ojemann, J. G., Wolpaw, J. R., and Schalk, G. (2009). Decoding ﬂexion of individual ﬁngers using electrocorticographic signals in humans. J. Neural Eng. 6:066001. doi: 10.1088/1741-2560/6/6/066001

Kwak, N.-S., Müller, K.-R., and Lee, S.-W. (2015). A lower limb exoskeleton control system based on steady state visual evoked potentials. J. Neural Eng. 12:056009. doi: 10.1088/1741-2560/12/5/056009

LaFleur, K., Cassady, K., Doud, A., Shades, K., Rogin, E., and He, B. (2013). Quadcopter control in three-dimensional space using a noninvasive motor imagery-based brain–computer interface. J. Neural Eng. 10:046003. doi: 10.1088/1741-2560/10/4/046003

Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gordon, S. M., Hung, C. P., and Lance, B. J. (2018). EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces. J. Neural Eng. 15:056013. doi: 10.1088/1741-2552/aace8c

Lebedev, M. (2014). Brain-machine interfaces: an overview. Transl. Neurosci. 5, 99–110. doi: 10.2478/s13380-014-0212-z

Lebedev, M. A., Carmena, J. M., O’Doherty, J. E., Zacksenhouse, M., Henriquez, C. S., Principe, J. C., et al. (2005). Cortical ensemble adaptation to represent velocity of an artiﬁcial actuator controlled by a brain-machine interface. J. Neurosci. 25, 4681–4693. doi: 10.1523/JNEUROSCI.4088-04.2005

Lebedev, M. A., and Nicolelis, M. A. (2006). Brain–machine interfaces: past, present and future. Trends Neurosci. 29, 536–546. doi: 10.1016/j.tins.2006.07.004

Lebedev, M. A., O’doherty, J. E., and Nicolelis, M. A. (2008). Decoding of temporal intervals from cortical ensemble activity. J. Neurophysiol. 99, 166–186. doi: 10.1152/jn.00734.2007

Leuthardt, E. C., Miller, K. J., Schalk, G., Rao, R. P., and Ojemann, J. G. (2006). Electrocorticography-based brain computer interface-the seattle experience. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 194–198. doi: 10.1109/TNSRE.2006.875536

Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., and Moran, D. W.

(2004). A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1:63. doi: 10.1088/1741-2560/1/2/001

Levine, S. P., Huggins, J. E., BeMent, S. L., Kushwaha, R. K., Schuh, L. A., Passaro, E. A., et al. (1999). Identiﬁcation of electrocorticogram patterns as the basis for a direct brain interface. J. Clin. Neurophysiol. 16:439.

Levine, S. P., Huggins, J. E., BeMent, S. L., Kushwaha, R. K., Schuh, L. A., Rohde, M. M., et al. (2000). A direct brain interface based on event-related potentials. IEEE Trans. Rehabil. Eng. 8, 180–185. doi: 10.1109/86.847809

Li, T., Hong, J., Zhang, J., and Guo, F. (2014). Brain–machine interface control of a manipulator using small-world neural network and shared control strategy. J. Neurosci. Methods 224, 26–38. doi: 10.1016/j.jneumeth.2013.11.015

Li, Y., Zhang, S., Jin, Y., Cai, B., Controzzi, M., Zhu, J., et al. (2017). Gesture decoding using ECoG signals from human sensorimotor cortex: a pilot study. Behav. Neurol. 2017:3435686. doi: 10.1155/2017/3435686

Liang, N., and Bougrain, L. (2012). Decoding ﬁnger ﬂexion from band-speciﬁc ECoG signals in humans. Front. Neurosci. 6:91. doi: 10.3389/fnins.2012.00091

Lin, P. T., Sharma, K., Holroyd, T., Battapady, H., Fei, D.-Y., and Bai, O. (2013). “A high performance MEG based BCI using single trial detection of human movement intention,” in Functional Brain Mapping and the Endeavor to Understand the Working Brain (Norderstedt: IntechOpen).

Liu, Y., Coon, W. G., de Pesters, A., Brunner, P., and Schalk, G. (2015). The eﬀects of spatial ﬁltering and artifacts on electrocorticographic signals. J. Neural Eng. 12:056008. doi: 10.1088/1741-2560/12/5/056008

Liu, Y., Sharma, M., Gaona, C., Breshears, J., Roland, J., Freudenburg, Z., et al. (2010). “Decoding ipsilateral ﬁnger movements from ECoG signals in humans,” in Advances in Neural Information Processing Systems (Vancouver, BC), 1468–1476.

- Livezey, J. A., Bouchard, K. E., and Chang, E. F. (2018). Deep learning as a tool for neural data analysis: speech classiﬁcation and cross-frequency coupling in human sensorimotor cortex. arXiv [Preprint]. arXiv:1803.09807.
- Livezey, J. A., Bouchard, K. E., and Chang, E. F. (2019). Deep learning as a tool for neural data analysis: speech classiﬁcation and cross-frequency coupling in human sensorimotor cortex. PLoS Comput. Biol. 15:e1007091. doi: 10.1371/journal.pcbi.1007091

Lotte, F., Bougrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., et al. (2018). A review of classiﬁcation algorithms for EEG-based brain–computer interfaces: a 10 year update. J. Neural Eng. 15:031005. doi: 10.1088/1741-2552/aab2f2

Lotte, F., Congedo, M., Lécuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain–computer interfaces. J. Neural Eng. 4:R1. doi: 10.1088/1741-2560/4/2/R01

Manning, J. R., Jacobs, J., Fried, I., and Kahana, M. J. (2009). Broadband shifts in local ﬁeld potential power spectra are correlated with single-neuron spiking in humans. J. Neurosci. 29, 13613–13620. doi: 10.1523/JNEUROSCI.2041-09.2009

Marjaninejad, A., Taherian, B., and Valero-Cuevas, F. J. (2017). Finger movements are mainly represented by a linear transformation of energy in band-speciﬁc ECoG signals. In Conf. Proc. IEEE Eng. Med. Biol. Soc. 2017, 986–989. doi: 10.1109/EMBC.2017.8036991

Matsushita, K., Hirata, M., Suzuki, T., Ando, H., Yoshida, T., Ota, Y., et al. (2018). A fully implantable wireless ecog 128-channel recording device for human brain—machine interfaces: W-herbs. Front. Neurosci. 12:511. doi: 10.3389/fnins.2018.00511

McCrimmon, C. M., Wang, P. T., Heydari, P., Nguyen, A., Shaw, S. J., Gong, H., et al. (2017). Electrocorticographic encoding of human gait in the leg primary motor cortex. Cereb. Cortex 28, 2752–2762. doi: 10.1093/cercor/bhx155

McFarland, D., and Wolpaw, J. (2017). EEG-based brain–computer interfaces. Curr. Opin. Biomed. Eng. 4, 194–200. doi: 10.1016/j.cobme.2017.11.004 Mehring, C., Rickert, J., Vaadia, E., de Oliveira, S. C., Aertsen, A., and Rotter, S.

(2003). Inference of hand movements from local ﬁeld potentials in monkey motor cortex. Nat. Neurosci. 6:1253. doi: 10.1038/nn1158

Meisel, C., and Bailey, K. A. (2019). Identifying signal-dependent information about the preictal state: a comparison across ECoG, EEG and EKG using deep learning. EBioMedicine 45, 422–431. doi: 10.1016/j.ebiom.2019.07.001

Miller, K. J., Leuthardt, E. C., Schalk, G., Rao, R. P., Anderson, N. R., Moran, D. W., et al. (2007). Spectral changes in cortical surface potentials during motor movement. J. Neurosci. 27, 2424–2432. doi: 10.1523/JNEUROSCI.3886-06.2007

Miller, K. J., Zanos, S., Fetz, E. E., Den Nijs, M., and Ojemann, J. G. (2009). Decoupling the cortical power spectrum reveals real-time representation of individual ﬁnger movements in humans. J. Neurosci. 29, 3132–3137. doi: 10.1523/JNEUROSCI.5506-08.2009

Mirabella, G., and Lebedev, M. A. (2016). Interfacing to the brain’s motor decisions. J. Neurophysiol. 117, 1305–1319. doi: 10.1152/jn.00051.2016

Morales-Flores, E., Schalk, G., and Ramirez-Cortes, J. M. (2014). Non-supervised technique to adapt spatial ﬁlters for ECoG data analysis. in 2014 IEEE Symposium on Computational Intelligence in Brain Computer Interfaces (CIBCI) (Orlando, FL: IEEE), 43–48.

Murphy, M. D., Guggenmos, D. J., Bundy, D. T., and Nudo, R. J. (2016). Current challenges facing the translation of brain computer interfaces from preclinical trials to use in human patients. Front. Cell. Neurosci. 9:497. doi: 10.3389/fncel.2015.00497

Nakanishi, Y., Yanagisawa, T., Shin, D., Fukuma, R., Chen, C., Kambara, H., et al. (2013). Prediction of three-dimensional arm trajectories based on ECoG signals recorded from human sensorimotor cortex. PLoS ONE 8:e72085. doi: 10.1371/journal.pone.0072085

Nakanishi, Y., Yanagisawa, T., Shin, D., Kambara, H., Yoshimura, N., Tanaka, M., et al. (2017). Mapping ECoG channel contributions to trajectory and muscle activity prediction in human sensorimotor cortex. Sci. Rep. 7:45486. doi: 10.1038/srep45486

Newman, G., Fifer, M., Benz, H., Crone, N., and Thakor, N. (2015). “Eigenvector centrality reveals the time course of task-speciﬁc electrode connectivity in human ECoG,” in 2015 7th International IEEE/EMBS Conference on Neural Engineering (NER) (Montpellier: IEEE), 336–339.

Nicolae, I.-E., Acqualagna, L., and Blankertz, B. (2017). Assessing the depth of cognitive processing as the basis for potential user-state adaptation. Front. Neurosci. 11:548. doi: 10.3389/fnins.2017.00548

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Nicolelis, M. A., and Lebedev, M. A. (2009). Principles of neural ensemble physiology underlying the operation of brain–machine interfaces. Nat. Rev. Neurosci. 10:530. doi: 10.1038/nrn2653

Normann, R. A., Greger, B., House, P., Romero, S. F., Pelayo, F., and Fernandez, E.

(2009). Toward the development of a cortically based visual neuroprosthesis. J. Neural Eng. 6:035001. doi: 10.1088/1741-2560/6/3/035001

Nurse, E. S., Freestone, D. R., Oxley, T. J., Ackland, D. C., Vogrin, S. J., Murphy, M., et al. (2015). “Movement related directional tuning from broadband electrocorticography in humans,” in 2015 7th International IEEE/EMBS Conference on Neural Engineering (NER) (Montpellier: IEEE), 33–36.

Nuyujukian, P., Kao, J. C., Fan, J. M., Stavisky, S. D., Ryu, S. I., and Shenoy, K. V.

(2014). Performance sustaining intracortical neural prostheses. J. Neural Eng. 11:066003. doi: 10.1088/1741-2560/11/6/066003

Pais-Vieira, M., Lebedev, M., Kunicki, C., Wang, J., and Nicolelis, M. A. (2013). A brain-to-brain interface for real-time sharing of sensorimotor information. Sci. Rep. 3:1319. doi: 10.1038/srep01319

Pan, G., Li, J.-J., Qi, Y., Yu, H., Zhu, J.-M., Zheng, X.-X., et al. (2018). Rapid decoding of hand gestures in electrocorticography using recurrent neural networks. Front. Neurosci. 12:555. doi: 10.3389/fnins.2018.00555

Pan, J., Li, Y., Gu, Z., and Yu, Z. (2013). A comparison study of two p300 speller paradigms for brain–computer interface. Cogn. Neurodyn. 7, 523–529. doi: 10.1007/s11571-013-9253-1

Pascarella, A., Todaro, C., Clerc, M., Serre, T., and Piana, M. (2016). Source modeling of electrocorticography (ECoG) data: stability analysis and spatial ﬁltering. J. Neurosci. Methods 263, 134–144. doi: 10.1016/j.jneumeth.2016.02.012

Paul, S., Zabir, I., Sarker, T., Fattah, S. A., and Shahnaz, C. (2017). Higher order statistics of bispectrum and MRP of ECoG signals for motor imagery tasks classiﬁcation. in IEEE Region 10 Symposium (TENSYMP), 2017 (Cochin: IEEE), 1–4.

Perge, J. A., Homer, M. L., Malik, W. Q., Cash, S., Eskandar, E., Friehs, G., et al. (2013). Intra-day signal instabilities aﬀect decoding performance in an intracortical neural interface system. J. Neural Eng. 10:036004. doi: 10.1088/1741-2560/10/3/036004

Petroﬀ, O. A., Spencer, D. D., Goncharova, I. I., and Zaveri, H. P. (2016). A comparison of the power spectral density of scalp EEG and subjacent electrocorticograms. Clin. Neurophysiol. 127, 1108–1112. doi: 10.1016/j.clinph.2015.08.004

Pistohl, T., Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2008). Prediction of arm movement trajectories from ECoG-recordings in humans. J. Neurosci. Methods 167, 105–114. doi: 10.1016/j.jneumeth.2007.10.001

Pistohl, T., Schmidt, T. S., Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2013). Grasp detection from human ECoG during natural reach-to-grasp movements. PLoS ONE 8:e54658. doi: 10.1371/journal.pone.0054658

Pistohl, T., Schulze-Bonhage, A., Aertsen, A., Mehring, C., and Ball, T. (2012). Decoding natural grasp types from human ECoG. Neuroimage 59, 248–260. doi: 10.1016/j.neuroimage.2011.06.084

Rao, R. P., Stocco, A., Bryan, M., Sarma, D., Youngquist, T. M., Wu, J., et al.

(2014). A direct brain-to-brain interface in humans. PLoS ONE 9:e111332. doi: 10.1371/journal.pone.0111332

RaviPrakash, H., Korostenskaja, M., Castillo, E. M., Lee, K. H., Salinas, C. M., Baumgartner, J., et al. (2018). Deep learning provides exceptional accuracy to ECoG-based functional language mapping for epilepsy surgery. bioRxiv [Preprint]. doi: 10.1101/497644

Reddy, C. G., Reddy, G. G., Kawasaki, H., Oya, H., Miller, L. E., and Howard, M. A. III. (2009). Decoding movement-related cortical potentials from electrocorticography. Neurosurg. Focus 27:E11. doi: 10.3171/2009.4.FOCUS0990

Renard, Y., Lotte, F., Gibert, G., Congedo, M., Maby, E., Delannoy, V., et al. (2010). Openvibe: an open-source software platform to design, test, and use brain– computer interfaces in real and virtual environments. Presence Teleoper. Virtual Environ. 19, 35–53. doi: 10.1162/pres.19.1.35

Richards, B. A., Lillicrap, T. P., Beaudoin, P., Bengio, Y., Bogacz, R., Christensen, A., et al. (2019). A deep learning framework for neuroscience. Nat. Neurosci. 22, 1761–1770. doi: 10.1038/s41593-019-0520-2

Rickert, J., de Oliveira, S. C., Vaadia, E., Aertsen, A., Rotter, S., and Mehring, C. (2005). Encoding of movement direction in diﬀerent frequency ranges of motor cortical local ﬁeld potentials. J. Neurosci. 25, 8815–8824. doi: 10.1523/JNEUROSCI.0816-05.2005

Roy, Y., Banville, H., Albuquerque, I., Gramfort, A., Falk, T. H., and Faubert, J. (2019). Deep learning-based electroencephalography analysis: a systematic review. J. Neural Eng. 16:051001. doi: 10.1088/1741-2552/ab260c

Ryun, S., Kim, J. S., Lee, S. H., Jeong, S., Kim, S.-P., and Chung, C. K. (2014). Movement type prediction before its onset using signals from prefrontal area: an electrocorticography study. BioMed Res. Int. 2014:783203. doi: 10.1155/2014/783203

Salinas, E., and Abbott, L. (1994). Vector reconstruction from ﬁring rates. J. Comput. Neurosci. 1, 89–107.

Samiee, S., Hajipour, S., and Shamsollahi, M. B. (2010). “Five-class ﬁnger ﬂexion classiﬁcation using ECoG signals,” in 2010 International Conference on Intelligent and Advanced Systems (ICIAS) (Kuala Lumpur: IEEE), 1–4.

Sanchez, J. C., Gunduz, A., Carney, P. R., and Principe, J. C. (2008). Extraction and localization of mesoscopic motor control signals for human ecog neuroprosthetics. J. Neurosci. Methods 167, 63–81. doi: 10.1016/j.jneumeth.2007.04.019

Satow, T., Matsuhashi, M., Ikeda, A., Yamamoto, J., Takayama, M., Begum, T., et al. (2003). Distinct cortical areas for motor preparation and execution in human identiﬁed by bereitschaftspotential recording and ECoG-EMG coherence analysis. Clin. Neurophysiol. 114, 1259–1264. doi: 10.1016/S1388-2457(03)00091-9

Schaﬀelhofer, S., Agudelo-Toro, A., and Scherberger, H. (2015). Decoding a wide range of hand conﬁgurations from macaque motor, premotor, and parietal cortices. J. Neurosci. 35, 1068–1081. doi: 10.1523/JNEUROSCI.359414.2015

Schalk, G., Kubánek, J., Miller, K. J., Anderson, N. R., Leuthardt, E. C., Ojemann, J. G., et al. (2007). Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. J. Neural Eng. 4:264. doi: 10.1088/1741-2560/4/3/012

Schalk, G., and Leuthardt, E. C. (2011). Brain-computer interfaces using electrocorticographic signals. IEEE Rev. Biomed. Eng. 4, 140–154. doi: 10.1109/RBME.2011.2172408

Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw, J. R.

(2004). Bci2000: a general-purpose brain-computer interface (BCI) system. IEEE Trans. Biomed. Eng. 51, 1034–1043. doi: 10.1109/TBME.2004.827072 Schalk, G., Miller, K., Anderson, N., Wilson, J., Smyth, M., Ojemann, J., et al. (2008). Two-dimensional movement control using electrocorticographic signals in humans. J. Neural Eng. 5:75. doi: 10.1088/1741-2560/5/1/008

Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M., Eggensperger, K., Tangermann, M., et al. (2017). Deep learning with convolutional neural networks for EEG decoding and visualization. Hum. Brain Mapp. 38, 5391–5420. doi: 10.1002/hbm.23730

Shahid, S., and Prasad, G. (2011). Bispectrum-based feature extraction technique for devising a practical brain–computer interface. J. Neural Eng. 8:025014. doi: 10.1088/1741-2560/8/2/025014

Shoham, S., Halgren, E., Maynard, E. M., and Normann, R. A. (2001). Motorcortical activity in tetraplegics. Nature 413:793. doi: 10.1038/35101651

Shokoueinejad, M., Park, D.-W., Jung, Y. H., Brodnick, S. K., Novello, J., Dingle, A., et al. (2019). Progress in the ﬁeld of micro-electrocorticography. Micromachines 10:62. doi: 10.3390/mi10010062

Sinkin, M., Osadchiy, A., Lebedev, M., Volkova, K., Kondratova, M., Trifonov, I., et al. (2019). High resolution passive speech mapping in dominant hemisphere glioma surgery. Russ. J. Neurosurg. 21, 12–18. doi: 10.17650/1683-3295-2019-21-3-37-43

Slutzky, M. W., Jordan, L. R., Krieg, T., Chen, M., Mogul, D. J., and Miller, L. E.

(2010). Optimal spacing of surface electrode arrays for brain–machine interface applications. J. Neural Eng. 7:026004. doi: 10.1088/1741-2560/7/2/026004

Smetanin, N., Lebedev, M. A., and Ossadtchi, A. (2018a). Towards zero-latency neurofeedback. bioRxiv [preprint]. doi: 10.1101/424846

Smetanin, N., Volkova, K., Zabodaev, S., Lebedev, M., and Ossadtchi, A. (2018b). NFBLab–a versatile software for neurofeedback and brain-computer interface research. Front. Neuroinform. 12:100. doi: 10.3389/fninf.2018.00100

Song, W., Ramakrishnan, A., Udoekwere, U. I., and Giszter, S. F. (2009). Multiple types of movement-related information encoded in hindlimb/trunk cortex in rats and potentially available for brain–machine interface controls. IEEE Trans. Biomed. Eng. 56, 2712–2716. doi: 10.1109/TBME.2009.2026284

Spüler, M., Grimm, F., Gharabaghi, A., Bogdan, M., and Rosenstiel, W. (2016). “Comparing methods for decoding movement trajectory from ECoG in chronic stroke patients,” in Advances in Neurotechnology, Electronics and Informatics (Rome: Springer), 125–139.

Spüler, M., Rosenstiel, W., and Bogdan, M. (2014a). “Predicting wrist movement trajectory from ipsilesional ECoG in chronic stroke patients,” in Proceedings of 2nd International Congress on Neurotechnology, Electronics and Informatics (NEUROTECHNIX) (Rome), 38–45.

Spüler, M., Walter, A., Ramos-Murguialday, A., Naros, G., Birbaumer, N., Gharabaghi, A., et al. (2014b). Decoding of motor intentions from epidural ECoG recordings in severely paralyzed chronic stroke patients. J. Neural Eng. 11:066008. doi: 10.1088/1741-2560/11/6/066008

Sturm, I., Blankertz, B., Potes, C., Schalk, G., and Curio, G. (2014). Ecog high gamma activity reveals distinct cortical representations of lyrics passages, harmonic and timbre-related changes in a rock song. Front. Hum. Neurosci. 8:798. doi: 10.3389/fnhum.2014.00798

Taplin, A. M., de Pesters, A., Brunner, P., Hermes, D., Dalﬁno, J. C., Adamo, M. A., et al. (2016). Intraoperative mapping of expressive language cortex using passive real-time electrocorticography. Epilepsy Behav. Case Rep. 5, 46–51. doi: 10.1016/j.ebcr.2016.03.003

Taylor, D. M., Tillery, S. I. H., and Schwartz, A. B. (2002). Direct cortical control of 3d neuroprosthetic devices. Science 296, 1829–1832. doi: 10.1126/science.1070291

Todaro, C., Marzetti, L., Sosa, P. A. V., Valdés-Hernández, P. A., and Pizzella, V. (2018). Mapping brain activity with electrocorticography: resolution properties and robustness of inverse solutions. Brain Topogr. 32, 583–598. doi: 10.1007/s10548-018-0623-1

Toro, C., Cox, C., Friehs, G., Ojakangas, C., Maxwell, R., Gates, J. R., et al. (1994a). 8–12 Hz rhythmic oscillations in human motor cortex during two-dimensional arm movements: evidence for representation of kinematic parameters. Electroencephalogr. Clin. Neurophysiol. 93, 390–403.

Toro, C., Deuschl, G., Thatcher, R., Sato, S., Kufta, C., and Hallett, M. (1994b). Event-related desynchronization and movement-related cortical potentials on the ECoG and EEG. Electroencephalogr. Clin. Neurophysiol. 93, 380–389.

van Vugt, M. K., Sederberg, P. B., and Kahana, M. J. (2007). Comparison of spectral analysis methods for characterizing brain oscillations. J. Neurosci. Methods 162, 49–63. doi: 10.1016/j.jneumeth.2006.12.004

Vansteensel, M. J., Pels, E. G., Bleichner, M. G., Branco, M. P., Denison, T., Freudenburg, Z. V., et al. (2016). Fully implanted brain–computer interface in a locked-in patient with als. N. Engl. J. Med. 375, 2060–2066. doi: 10.1056/NEJMoa1608085

Vaskov, A. K., Irwin, Z. T., Nason, S. R., Vu, P. P., Nu, C. S., Bullard, A. J., et al.

(2018). Cortical decoding of individual ﬁnger group motions using reﬁt kalman ﬁlter. Front. Neurosci. 12:751. doi: 10.3389/fnins.2018.00751

Velliste, M., Perel, S., Spalding, M. C., Whitford, A. S., and Schwartz, A. B.

(2008). Cortical control of a prosthetic arm for self-feeding. Nature 453:1098. doi: 10.1038/nature06996

Viventi, J., Kim, D.-H., Vigeland, L., Frechette, E. S., Blanco, J. A., Kim, Y.-S., et al.

(2011). Flexible, foldable, actively multiplexed, high-density electrode array for mapping brain activity in vivo. Nat. Neurosci. 14:1599. doi: 10.1038/nn.2973 Wang, N. X., Farhadi, A., Rao, R. P., and Brunton, B. W. (2018). “Ajile movement prediction: multimodal deep learning for natural human neural recordings and video,” in Thirty-Second AAAI Conference on Artiﬁcial Intelligence (New Orleans, LA).

Wang, P. T., King, C. E., McCrimmon, C. M., Lin, J. J., Sazgar, M., Hsu, F. P., et al. (2016). Comparison of decoding resolution of standard and high-density electrocorticogram electrodes. J. Neural Eng. 13:026016. doi: 10.1088/1741-2560/13/2/026016

Wang, P. T., King, C. E., McCrimmon, C. M., Shaw, S. J., Millett, D. E., Liu, C. Y., et al. (2014). Electrocorticogram encoding of upper extremity movement duration. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 1243–1246. doi: 10.1109/EMBC.2014.6943822

Wang, W., Collinger, J. L., Degenhart, A. D., Tyler-Kabara, E. C., Schwartz, A. B., Moran, D. W., et al. (2013). An electrocorticographic brain interface in an individual with tetraplegia. PLoS ONE 8:e55344. doi: 10.1371/journal.pone.0055344

Wang, W., Degenhart, A. D., Collinger, J. L., Vinjamuri, R., Sudre, G. P., Adelson, P. D., et al. (2009). Human motor cortical activity recorded with micro-ecog electrodes, during individual ﬁnger movements. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2009, 586–589. doi: 10.1109/IEMBS.2009.5333704

Wang, Z., Gunduz, A., Brunner, P., Ritaccio, A. L., Ji, Q., and Schalk, G. (2012). Decoding onset and direction of movements using electrocorticographic (ECoG) signals in humans. Front. Neuroeng. 5:15. doi: 10.3389/fneng.2012.00015

Wang, Z., Ji, Q., Miller, K. J., and Schalk, G. (2011). Prior knowledge improves decoding of ﬁnger ﬂexion from electrocorticographic signals. Front. Neurosci. 5:127. doi: 10.3389/fnins.2011.00127

Weinand, M. E., Hermann, B., Wyler, A. R., Carter, L. P., Oommen, K., Labiner, D., et al. (1994). Long-term subdural strip electrocorticographic monitoring of ictal déjà vu. Epilepsia 35, 1054–1059.

Wessberg, J., Stambaugh, C. R., Kralik, J. D., Beck, P. D., Laubach, M., Chapin, J. K., et al. (2000). Real-time prediction of hand trajectory by ensembles of cortical neurons in primates. Nature 408:361. doi: 10.1038/35042582

Wilson, J. A., Walton, L. M., Tyler, M., and Williams, J. (2012). Lingual electrotactile stimulation as an alternative sensory feedback pathway for brain–computer interface applications. J. Neural Eng. 9:045007. doi: 10.1088/1741-2560/9/4/045007

Wodlinger, B., Downey, J., Tyler-Kabara, E., Schwartz, A., Boninger, M., and Collinger, J. (2014). Ten-dimensional anthropomorphic arm control in a human brain–machine interface: diﬃculties, solutions, and limitations. J. Neural Eng. 12:016011. doi: 10.1088/1741-2560/12/1/016011

Wu, J., Shuman, B. R., Brunton, B. W., Steele, K. M., Olson, J. D., Rao, R. P., et al. (2016). Multistep model for predicting upper-limb 3d isometric force application from pre-movement electrocorticographic features. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2016, 1564–1567. doi: 10.1109/EMBC.2016.7591010

Wyler, A. R., Walker, G., and Somes, G. (1991). The morbidity of long-term seizure monitoring using subdural strip electrodes. J. Neurosurg. 74, 734–737.

Xie, T., Zhang, D., Wu, Z., Chen, L., and Zhu, X. (2015). Classifying multiple types of hand motions using electrocorticography during intraoperative awake

craniotomy and seizure monitoring processes—case studies. Front. Neurosci. 9:353. doi: 10.3389/fnins.2015.00353

Xie, Z., Schwartz, O., and Prasad, A. (2018). Decoding of ﬁnger trajectory from ECoG using deep learning. J. Neural Eng. 15:036009. doi: 10.1088/1741-2552/aa9dbe

Yanagisawa, T., Hirata, M., Saitoh, Y., Goto, T., Kishima, H., Fukuma, R., et al. (2011). Real-time control of a prosthetic hand using human electrocorticography signals. J. Neurosurg. 114, 1715–1722. doi: 10.3171/2011.1.JNS101421

Yanagisawa, T., Hirata, M., Saitoh, Y., Kato, A., Shibuya, D., Kamitani, Y., et al. (2009). Neural decoding using gyral and intrasulcal electrocorticograms. Neuroimage 45, 1099–1106. doi: 10.1016/j.neuroimage.2008.12.069

Yanagisawa, T., Hirata, M., Saitoh, Y., Kishima, H., Matsushita, K., Goto, T., et al.

(2012). Electrocorticographic control of a prosthetic arm in paralyzed patients. Ann. Neurol. 71, 353–361. doi: 10.1002/ana.22613

Zhang, Y., van Drongelen, W., Kohrman, M., and He, B. (2008). Threedimensional brain current source reconstruction from intra-cranial ecog

recordings. Neuroimage 42, 683–695. doi: 10.1016/j.neuroimage.2008. 04.263

Zubarev, I., Zetter, R., Halme, H.-L., and Parkkonen, L. (2018). Adaptive neural network classiﬁer for decoding MEG signals. Neuroimage 197, 425–434. doi: 10.1016/j.neuroimage.2019.04.068

Conﬂict of Interest: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2019 Volkova, Lebedev, Kaplan and Ossadtchi. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

