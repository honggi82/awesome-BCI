SYSTEMATIC REVIEW published: 14 July 2021 doi: 10.3389/fnhum.2021.643294

[Figure 1]

# Brain-Computer Interfaces for Children With Complex Communication Needs and Limited Mobility: A Systematic Review

Silvia Orlandi1, Sarah C. House1, Petra Karlsson2, Rami Saab1 and Tom Chau1,3*

1 Bloorview Research Institute, Holland Bloorview Kids Rehabilitation Hospital, Toronto, ON, Canada, 2 Cerebral Palsy Alliance, The University of Sydney, Sydney, NSW, Australia, 3 Institute of Biomedical Engineering (BME), University of Toronto, Toronto, ON, Canada

Brain-computer interfaces (BCIs) represent a new frontier in the effort to maximize the ability of individuals with profound motor impairments to interact and communicate. While much literature points to BCIs’ promise as an alternative access pathway, there have historically been few applications involving children and young adults with severe physical disabilities. As research is emerging in this sphere, this article aims to evaluate the current state of translating BCIs to the pediatric population. A systematic review was conducted using the Scopus, PubMed, and Ovid Medline databases. Studies of children and adolescents that reported BCI performance published in English in peer-reviewed journals between 2008 and May 2020 were included. Twelve publications were identiﬁed, providing strong evidence for continued research in pediatric BCIs. Research evidence was generally at multiple case study or exploratory study level, with modest sample sizes. Seven studies focused on BCIs for communication and ﬁve on mobility. Articles were categorized and grouped based on type of measurement (i.e., non-invasive and invasive), and the type of brain signal (i.e., sensory evoked potentials or movement-related potentials). Strengths and limitations of studies were identiﬁed and used to provide requirements for clinical translation of pediatric BCIs. This systematic review presents the state-of-the-art of pediatric BCIs focused on developing advanced technology to support children and youth with communication disabilities or limited manual ability. Despite a few research studies addressing the application of BCIs for communication and mobility in children, results are encouraging and future works should focus on customizable pediatric access technologies based on brain activity.

Edited by: Gernot R. Müller-Putz,

Graz University of Technology, Austria Reviewed by: Angela Riccio, Santa Lucia Foundation (IRCCS), Italy Carmen Vidaurre, Public University of Navarre, Spain *Correspondence:

Tom Chau tom.chau@utoronto.ca

Specialty section: This article was submitted to

Brain-Computer Interfaces,

a section of the journal Frontiers in Human Neuroscience

Received: 17 December 2020 Accepted: 18 May 2021 Published: 14 July 2021

Keywords: brain-computer interface, children, youth, assistive technology, severe disability, communication, environmental control

Citation: Orlandi S, House SC, Karlsson P,

Saab R and Chau T (2021) Brain-Computer Interfaces for

## INTRODUCTION

Children With Complex Communication Needs and Limited

Technology is often exploited as a tool to support children aﬀected by severe brain disorders or injury in their daily activities. These technologies are especially pertinent to children who are not capable of using speech to communicate or who are limited in motor skills and require mobility aids. Worldwide, only 1 in 10 people have access to assistive technology devices when required

Mobility: A Systematic Review. Front. Hum. Neurosci. 15:643294. doi: 10.3389/fnhum.2021.643294

[World Health Organization (WHO), 2020] and in Canada 95% of 3,775,920 individuals living with a disability use at least one aid or device to assist movement, communication, learning, or daily activities of life (Berardi et al., 2020).

The need for novel assistive technology and techniques for neurorehabilitation eﬀective for children is high (Mikołajewska and Mikołajewski, 2014). One of the most advanced technical solutions is the brain-computer interface (BCI). BCIs can be deﬁned as a link between the brain and an extra-corporeal apparatus, whereby signals from the brain can directly control the external device entirely bypassing the peripheral nervous system (Wolpaw et al., 2000). BCIs utilize changes in brain activity occurring when we react to stimuli, perform speciﬁc mental tasks, or experience diﬀerent psychological or emotional states. Non-invasive BCIs typically detect and utilize electromagnetic potentials directly related to ensemble neuronal ﬁring, or the associated hemodynamic changes including regional changes in relative oxyhemoglobin and deoxyhemoglobin concentrations (Proulx et al., 2018; Schudlo and Chau, 2018; Sereshkeh et al., 2018, 2019) and changes in arterial blood ﬂow velocities (Myrden et al., 2011, 2012; Goyal et al., 2016), due to neurovascular coupling. Clinically, BCIs enable brain-based control of communication aids and environmental technologies (Moghimi et al., 2013; Rupp et al., 2014), assist in diagnosis (De Venuto et al., 2016; Lech et al., 2019), and enhance rehabilitation therapies (Daly and Wolpaw, 2008; Pichiorri and Mattia, 2020).

A long-term objective of translational BCI research is providing a channel for communication and environmental control for people with severe and multiple physical disabilities who otherwise lack the means to interact with people and the environment around them (Wolpaw et al., 2002). Hence, BCI-based control has been explored for: computer cursors (Wolpaw et al., 2002; Wirth et al., 2020); virtual keyboards (Birbaumer et al., 1999; Thompson et al., 2014a; Hosni et al., 2019); augmentative and alternative access systems (Thompson et al., 2013, 2014b; Brumberg et al., 2018); prosthetic devices (McFarland and Wolpaw, 2008; Vilela and Hochberg, 2020); wheelchairs (Punsawad and Wongsawat, 2013; Yu et al., 2017); entertainment/gaming (Holz et al., 2013; Van de Laar et al., 2013; Cattan et al., 2020); Internet browsing (Mugler et al., 2010; Milsap et al., 2019); and painting (Münßinger et al., 2010; Zickler et al., 2013; Kübler and Botrel, 2019). Given these explorations, BCIs have potential to serve as an alternative access method for people with severe motor deﬁcits (Huggins et al., 2014), who are not well-served by commercially available access solutions. Nonetheless, research on novel BCI solutions for target populations has been limited to laboratory settings (Fager et al., 2012; Wolpaw and Wolpaw, 2012; Guy et al., 2018) and able-bodied adults (Pires et al., 2011; Oken et al., 2018). A modest subset of BCI studies has recruited adults with disabilities, including: amyotrophic lateral sclerosis (Nijboer et al., 2008; Huggins et al., 2011; Oken et al., 2014); multiple sclerosis (Papatheodorou et al., 2019); brainstem stroke (Sellers et al., 2014); muscular dystrophy (Zickler et al., 2011); acquired brain injury (Huang et al., 2019) and cerebral palsy (CP) (Taherian et al.,

- 2016).

The adult BCI focus is at least partially attributable to the relative ease of acquiring from this population, robust brain signals that can be well-characterized. While the ﬁndings of adult studies are promising, BCI algorithms optimized for adults cannot be directly applied to pediatric users due, in part, to agerelated diﬀerences in the brain responses of interest (Volosyak et al., 2017; Manning et al., 2021). For example, compared to adults, children exhibit less language lateralization (Holland et al., 2001), attenuated movement-related cortical potentials (MRCPs) (Pangelinan et al., 2011), and greater attentional eﬀects on the latencies of auditory evoked potentials (Choudhury et al., 2015). Well-established BCI tasks for adults, such as verbal ﬂuency, a verbal working memory task that requires to recall words associated with a common criterion from memory (Schudlo and Chau, 2018), are not suitable for children without developmentally appropriate modiﬁcations (Gaillard et al., 2003; Schudlo and Chau, 2018). Children with congenital impairments may have atypical brain anatomy and functional organization that preclude the simple translation of timehonored BCI protocols, including those validated in adults with acquired impairments.

Developmental diﬀerences may also manifest behaviorally. Children may experience diﬃculties maintaining focus (Gavin and Davies, 2007; Kinney-Lang et al., 2020) and their brain signals can contain excessive movement artifacts (Bell and Wolfe, 2007). It is imperative that research expands beyond able-bodied adults and involves more end-users, including children, ensuring any new developments are optimized from an individual’s perspective. Diﬀerences in brain structure, topography, cognitive processing pathways and psycho-behavioral predisposition ought to be considered (Weyand and Chau, 2017).

Mikołajewska and Mikołajewski (2014) published a minireview of BCI applications in children identifying several issues unique to pediatric applications of BCI and a paucity of research thereof. Among these pediatric-speciﬁc challenges included the absence of guidelines for processing brain signals from children, heightened neural plasticity including evolving cortical organization and frequency content of signals, and child engagement considerations such as fear, comfort, and positioning (Mikołajewska and Mikołajewski, 2014). Notwithstanding these concerns, the need for pediatric BCI research remains high given the lack of viable access technologies for children and youth with severe and multiple disabilities (Myrden et al., 2014).

Brain Computer Interfaces

BCI systems deploy either invasive or non-invasive signal acquisition modalities. Invasive BCIs monitor brain activity on a cortex’s surface using electrocorticography (ECoG), within the gray matter using intracortical microelectrodes (Simeral et al., 2011) or in deep subcortical structures using depth electrodes (Krusienski and Shih, 2011; Herﬀ et al., 2020). Noninvasive BCIs instead measure electrophysiological activity with electroencephalography (EEG) or magnetoencephalography (MEG), or hemodynamic activity using magnetic resonance imaging (MRI), near-infrared spectroscopy (NIRS) or transcranial Doppler ultrasound (Myrden et al., 2011, 2012). A third category, the hybrid BCI, is deﬁned as systems using

two or more measurement modalities such as NIRS-EEG and EEG-electrocardiogram (Pfurtscheller et al., 2010; Zephaniah and Kim, 2014) either simultaneously or sequentially.

BCIs can be categorized according to the paradigm invoked for eliciting machine-discernible brain signals. Reactive BCI paradigm elicits an event-related potential (ERP). Popular ERPs leveraged in BCIs include the P300, which is evoked by an oddball stimulus and characterized by a large positive deﬂection that occurs between 200–250 to 700–750ms after stimulus onset (Amiri et al., 2013; He et al., 2020), and the steady-state visual evoked potential (SSVEP) and auditory steady-state response, wherein brain responses are evoked, respectively, by ﬂickering lights or pure tones at speciﬁc frequencies. Active BCI paradigms elicit machine-discernible brain signals for BCI control via deliberate mental tasks such as motor imagery (MI), which involves the mental rehearsal of: a given movement (Rejer, 2012); mental arithmetic, music imagery (Weyand and Chau, 2015); spelling (Obermaier et al., 2003); covert speech (Birbaumer et al., 2010); observing pictures (Kushki et al., 2012); among others. Typical BCI taxonomies include passive BCIs that simply monitor the user’s psychological state (Myrden and Chau, 2016,

- 2017). Once acquired, signals generated by a BCI task are fed through

a processing pipeline. Signal processing procedures for BCIs can be “oﬄine” (retrospective) or “online” (suitable for realtime applications). A typical BCI processing pipeline (Bamdad et al., 2015) for communication and mobility is depicted in Figure 1. Typical pipeline elements include algorithms to suppress artifacts, extract features, and classify the signals. Pipeline outputs are then used to control an assistive device that supports communication or mobility.

Objectives and Research Question

This article appraises the pediatric BCI literature systematically, considering speciﬁc inclusion criteria and highlighting the current information processing methods applied to pediatric brain signals. Through this systematic review, we set out to address two research questions: (1) What is the state of science

in applying BCIs to support communication and manual ability in the pediatric population?; (2) What is current knowledge about the necessary considerations to render BCIs suitable for children?

METHODS Study Design

This systematic review included all levels of research evidence and aimed to integrate best practice systematic review methodology, the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (Moher et al., 2009).

Search Strategy

Identiﬁcation Process

Based on a preliminary search-string with the PubMed database, the syntax was developed for the search across three databases during May 2020: Scopus, PubMed, and Ovid. The SPIDER (Sample, Phenomenon of Interest, Design, Evaluation, Research type) tool was used to structure the search related to the research questions (Cooke et al., 2012). Electronic database searches were performed using the following key-terms related to “Sample:” pediatric or pediatric; or child or children; or youth(s) or adolescent(s) or teen(s) or teenager(s). These were combined with the following “Phenomenon of Interest” terms: BCI or brain computer interface or brain-computer interface or brain-machine interface or brain machine interface or mind machine interface or direct neural interface or neural control interface. The search strategy did not specify design, evaluation, or research type in order to capture all potentially relevant articles. These terms were considered in the inclusion and exclusion criteria. After retrieving studies from the searches, duplicates were removed and the paper titles, abstracts, and associated meta-data were compiled into a single table for further review.

Screening Process: Inclusion and Exclusion Criteria

All research within Oxford levels of evidence I–IV (Howick et al., 2011), including case studies and single-case experimental design

|[Figure 2]<br><br>FIGURE 1 | Typical BCI processing pipeline. The input signal acquired from the human brain is ﬁltered (signal processing), classiﬁed and transferred to an output device (device interface), forming the BCI application.|
|---|

studies reporting objective outcome measures were eligible for inclusion, if they: (1) reported in full text; (2) were published in English in peer-reviewed journals between January 2008 and May 2020; (3) included children and adolescents, under the age of 19 (Sawyer et al., 2018), using BCIs; (4) described the design of the protocol used for data collection (“Design”); (5) measured outcomes related to the performance of the BCI (“Evaluation”); and (6) included quantitative methods (“Research type”). Studies that presented only aggregate results from participating adults and children were excluded. Those studies that related to the general diagnosis of brain disorders or diseases were excluded. Publications related to passive BCI without a ﬁnal goal of developing assistive technology devices were excluded. Gray literature and unpublished works were not eligible for inclusion. Strictly qualitative research, book chapters, review articles, and conference publications were excluded.

Eligibility Process: Study Selection, Data Collection Process, and Synthesis of Results

Two of the ﬁve authors (SO and SCH) conducted the search across the databases and produced a list of articles based on the title and abstract according to the inclusion criteria. A two-step procedure was carried out independently by four authors (SO, SCH, PK, RS) to identify articles for inclusion. The ﬁrst step involved screening titles and abstracts for potential eligibility and, thereafter, screening the full text of potentially eligible articles. Four authors independently completed data extraction. An almost perfect level of agreement was obtained for title and abstract screening (Cohen’s kappa coeﬃcient, k = 0.96, percentage of agreement 98%). After a full-text review of the eligible papers, articles were excluded for any of the following reasons: the performance was reported for a heterogeneous group composed of adults and children without a two-group comparison (e.g., only averaged accuracy was reported, or children and adults’ classiﬁcation performance was not distinguishable); BCIs were not developed for pediatric participants; BCIs developed for adults but included a limited number of children (only one or two adolescents not suﬃcient for a two-group comparison); only adult participants were included in the study; results were not reported in terms of BCI performance; the study was not related to BCIs; passive BCIs were applied; the study did not include participants’ data; participants’ ages were not reported. Twelve articles remained eligible for further review. Twelve articles remained eligible for further review.

Data Extraction and Analysis

For each eligible study, the following data were extracted: number of participants and their ages; study design and data acquisition protocol; signal features; classiﬁer; and performance metrics. It was not appropriate to conduct a meta-analysis or any statistical analyses of the results due to the small number and heterogeneity of the included studies. Instead, key ﬁndings were summarized and presented narratively clustering the selected full-text papers into two sub-groups based on the functional activities identiﬁed (communication or manual ability) and the type of measurement applied (non-invasive or invasive). No

additional articles were found by consulting the references of the included full-text articles.

Quality Appraisal and Risk of Bias

Considering the heterogeneity of the 12 articles, the “QualSyst” quality assessment tool (Alberta Heritage Foundation for Medical Research) was used to gauge the quality of the overall body of evidence (Kmet et al., 2004). We applied a 14-criteria checklist for quantitative studies, where raters scored each criterion as being fully (2 points), partially (1 point), or not (0 points) fulﬁlled. A summary score was calculated for each paper as the sum of the scores across all applicable criteria and expressed as a percentage of the total possible score. When a speciﬁc criterion was not applicable to a given study, the criterion was omitted from the calculation of the summary score. Two reviewers (SO and SCH) independently assessed the quality (inter-rater reliability, k = 0.77 and 86% level of agreement) and the risk of bias for all the included studies. The sample sizes of the multiple-case-study articles were reported in terms of the number of pediatric participants recruited in the studies. Adult participants were not included in Tables 1–6. To further elucidate the overall quality of the evidence, each of the included articles received a quality grade as: limited (score of ≤50%); adequate (>50 and ≤70%); good (>70 and ≤80%); or strong (>80%) (Lee et al., 2008). Discrepancies were discussed between the two reviewers and consensus was reached. The risk of bias was identiﬁed for each study by two authors (SO and SCH) using the Agency for Healthcare Research and Quality (AHRQ) criteria (Viswanathan et al., 2017). The risk of bias was assessed through the evaluation and discussion of each article in terms of selection, performance, attrition, detection, and reporting (inter-rater reliability, k = 0.94 and 95% level of agreement). Responses for each criterion were scored as “low risk,” “high risk,” “unclear,” and “not applicable.” Low risk of bias was assumed when studies met all the risk-of-bias criteria, medium risk of bias if at least one of the risk-of-bias criteria was not met and high risk of bias if three or more risk-of-bias criteria were not fulﬁlled. An unknown risk of bias was considered as high risk.

RESULTS Study Selection and Taxonomy

The search strategy identiﬁed 850 potential papers; 340 duplicates and 151 reviews, book chapters, conference articles were removed. Then 359 titles and abstracts were reviewed and 203 were removed, according to the inclusion criteria (section Screening Process: Inclusion and Exclusion Criteria), leaving 156 articles that required full-text review. Twelve articles were subsequently identiﬁed as eligible for inclusion and grouping into sub-categories: seven relating to communication (Beveridge et al., 2017, 2019; Taherian et al., 2017; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020); and ﬁve concerning mobility (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013; Jochumsen et al., 2018). The ﬂowchart in Figure 2 details outcomes of: identiﬁcation; screening; eligibility; inclusion steps.

|[Figure 3]<br><br>FIGURE2|Studyselectionﬂowchart.Theﬂowdiagramdescribesidentiﬁcation,screening,eligibility,andinclusionprocedures.|
|---|

|[Figure 4]<br><br>FIGURE 3 | Taxonomy of the selected articles. SSVEP, steady state visual evoked potential; mVEP, motion-onset visual evoked potential; ERD, event-related desynchronization; MRCP, movement-related cortical potential.|
|---|

We categorized the selected papers (see Figure 3). At the ﬁrst level of the taxonomy, we grouped papers according to the type of measurement, either non-invasive or invasive. Under the noninvasive category, we further subdivided papers by the type of brain signals harnessed, which includes three types of sensory evoked potentials, MRCP, or event-related desynchronization (ERD). This taxonomy roughly reﬂects the readiness for clinical translation, with the non-invasive alternatives being more readily implementable. For each study, we adhere to a uniform presentation structure, highlighting the participants, task paradigm, analytical approach, and key ﬁndings.

Objectives, participants’ information (e.g., age, health conditions, participant number), methods and ﬁndings related to online and oﬄine BCI performance are reported in Tables 1–4.

Non-invasive Pediatric BCIs

Eight studies (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Taherian et al., 2017; Jochumsen et al., 2018; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020) in this category used EEG as the non-invasive modality for interrogating the pediatric brain. The study by Jochumsen et al. (2018) is the only one on non-invasive pediatric BCI related to manual ability. The other seven noninvasive BCI studies (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Taherian et al., 2017; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020) focused on new systems to support communication and computer interaction.

Evoked Potentials

Five studies harnessed evoked brain responses: steady-state visual evoked potential (SSVEP) (Ehlers et al., 2012; Norton et al., 2018); motion-onset visual evoked potential (mVEP) (Beveridge et al., 2017, 2019); P300 (Vaˇreka, 2020) following the presentation of a visual stimulus.

Ehlers et al. (2012) investigated the inﬂuence of developmentspeciﬁc changes in the background EEG on stimulus-driven BCI with 37 typically developing (TD) children and 14 adults, aged 6–33, using SSVEPs and mouse control and spelling tasks. Only online results but no chance level were reported. Participants navigated a letter matrix to spell six words, two in three diﬀerent stimuli conditions (low, medium, high frequency), by focusing on one of ﬁve target LEDs (corresponding to four directions and a select command) placed around a screen where the letter in the middle of the matrix was highlighted. Participants practiced by spelling their names; however, the youngest participants were assisted by the investigator in locating the target LED given their less developed visual searching abilities. Ehlers et al. (2012) used the Bremen-BCI (Friman et al., 2007) to classify ﬁve diﬀerent SSVEP targets. Poor signals due to insuﬃcient electrode contact were given a low weight or ignored. Classiﬁcation of signals used to generate the correct-to-complete commands ratio was based on a 2s sliding window every 125ms. Accuracies, regarding correct-to-complete commands ratio, were lower than 60% for pediatric participants. Results showed low classiﬁcation performance (accuracy: ∼40%) for the young subjects (age 7–10 years), based on stimulation of 7 and 11Hz. When a low-frequency (7–11Hz) visual stimulus was presented to participants, adults consistently achieved higher accuracies (∼78%) than those achieved by the three groups of children (group 1 accuracy: ∼40%; groups 2 and 3: ∼50%). In the medium frequency (13–17Hz) condition, diﬀerences in achieved accuracies were found only between the adults (accuracy: ∼78%) and youngest group of children with an average age of 6.73 years (group 1 accuracy: ∼55%; group 2: 50%; group 3: 75%). In contrast, no diﬀerence between the four groups was found when a high-frequency (30–48Hz) stimulus was presented (group 1

- July2021|Volume15|Article6432947FrontiersinHumanNeuroscience|www.frontiersin.org

TABLE 1 | Research articles on pediatric non-invasive BCIs: study objectives and data collection details.

References Study objective Sample size [females]

Age (years)

Diagnosis Applications BCI paradigm

Mode of operation

Signal type

Data acquisition Task and sessions

Ehlers et al.

(2012)

Norton et al.

(2018)

Examine age-related performance differences on an SSVEP-BCI

N = 51 [31]

Pediatric

- Group 1:

- N = 11 [6]

Group 2:

- N = 12 [9]

- Group 3: N = 14 [3]

Compare the performance of 9–11-year-old children using SSVEP-based BCI to adults

N = 26 [n/a]

Pediatric N = 15 [n/a]

Beveridge et al. (2017)

Evaluate mVEP paradigm for BCI-controlled video game

Pediatric N = 15 [4]

Beveridge et al. (2019)

Study trade-off between accuracy of control and gameplay speed using an mVEP BCI

Vaˇreka (2020) Compare CNN with

baseline classiﬁers using large subject P300 BCI dataset

N = 48 [10]

Pediatric N = 15 [4]

Pediatric N = 250 [112]

6–33

Pediatric Avg. 6.73

- Avg. 8.08
- Avg. 9.86

9–68

Pediatric 9–11

Pediatric 13–16

13–40

Pediatric 13–16

TD Mouse control/ spelling

SSVEP # stimuli: 3 Low: 7–11Hz Medium: 13–17Hz High: 30, 32, 34, 36, 38Hz

TD Graphical interface comprising three white circle targets

SSVEP # stimuli: 3 [6.2, 7.7, 10Hz]

Synch EEG Location: parietal and occipital (PZ, PO3, PO4, O1, OZ, O2, O9, O10) # Channels: 8 Hardware and Software:

- -Ag/Ag-Cl EEG electrodes
- -Wet system
- -BCI2000 -C++ (Bremen BCI)

Synch EEG Location: PO3, POZ, PO4, O1, OZ, O2 # Channels: 6 Hardware and Software:

- -Tin electrodes
- -Wet system
- -BCI2000

TD Neurogaming mVEP # stimuli: 5

Synch EEG Location: Cz, TP7, CPz, TP8, P7, P3, Pz, P4, P8, O1, Oz, and O2 # Channels: 12 Hardware and Software:

- -g.LADYbird
- -g.BSamp and g.GAMMAbox
- -MATLAB®
- -Unity 3D

Pediatric data is pulled from Beveridge et al. (2017) to compare to newly collected adult data. Adult protocol differed slightly from pediatric protocol (e.g., slow medium and fast lap rather than 3 slow laps + compare experienced vs. naive adults).

Task: cursor control to complete a spelling task # Sessions: 1 Session duration: 45min Task duration: 2min per run (6 words and at least 20 commands per word)

Task: focus visual attention on one of three white circle targets # Sessions: 1 Session duration: 5 trials/stimulus (15 trials total) for training, 20 trials/stimulus (60 trials total) for testing. Task duration: 5s

Task: 3D car-racing video game # Sessions: 1 Session duration: 1h Task duration: 1,000ms to activate 5 stimuli (300 trials per calibration and 60 per testing)

7–17 No identifying physical symptoms were asked or recorded

Guess the number game

P300 # stimuli: 1-9 ﬂashings

Synch EEG Location: Fz, Cz, Pz # Channels: 3 Hardware and Software:

- -BrainVision standard V-Amp
- -Neurobehavioural Systems Inc.
- -BrainVision Recorder
- -MATLAB®

Task: P300 # Sessions: 1 Session duration: Task duration: 1,000ms (532 trials)

(Continued)

Brain-ComputerInterfacesforChildrenOrlandietal.

- July2021|Volume15|Article6432948FrontiersinHumanNeuroscience|www.frontiersin.org

TABLE 1 | Continued

References Study objective Sample size [females]

Age (years)

Diagnosis Applications BCI paradigm

Mode of operation

Signal type

Data acquisition Task and sessions

Taherian et al.

(2017)

Employ a commercial EEG based BCI with people with CP

N = 8 [4]

Pediatric N = 5 [2]

Jochumsen et al. (2018)

Movement intention detection in adolescents with CP from single-trial EEG

Pediatric N = 8 [1]

Zhang et al.

(2019)

Evaluate if children can use simple BCIs

Pediatric N = 26 [7]

7–43

Pediatric

- P1: 17
- P2: 17
- P3: 7
- P4: 9
- P5: 9

Spastic quadriplegic CP

Puzzle games MI-ERD Synch EEG Location: unknown number—includes C3 and C4 # Channels: 14 Hardware and Software:

- -Emotiv EPOC BCI headset
- -Saline felt electrodes
- -Emotiv software

11–17

- P1: 16
- P2: 15
- P3: 11
- P4: 15
- P5: 13
- P6: 15
- P7: 17
- P8: 16

6–18 P1–2: 6

- P3: 8
- P4: 9 P5–7: 10 P8–9: 11 P10–11: 12 P12–14: 13 P15–16: 14 P17: 15 P18–19: 16 P20–22:17 P23–26: 18

Hemiplegia or diplegia CP with GMFCS of I-V

Neurorehabilitation Movement preparationMRCP/ dorsiﬂexions of the ankle joint

TD Mouse control and remotecontrolled car

MI and goal-oriented thinking—ERD

EEG Location: F3, FZ, F4, C3, CZ, C4, P3, PZ, P4 # Channels: 9 Hardware and Software:

Asynch (selfpaced)

- -Neuroscan EEG ampliﬁers
- -Wet system
- -EMG for movement detection
- -MATLAB®

Synch EEG Location: AF3, AF4, F3, F4, F7, F8, FC5, FC6, P7, P8, T7, T8, O1, O2 # Channels: 14 Hardware and Software:

- -Emotiv EPOC BCI headset
- -Saline felt electrodes
- -Emotiv software

Task: imagined arm

movements associated with the ability to move a virtual cube

# Sessions: 5–7 Session duration: 30min Task duration: 16–55 8s trials

Task: dorsiﬂexion of the ankle joint # Sessions: 1 Session duration: 15 min—avg. 65 ± 18 movements performed per participant Task duration: 4–6s

Tasks: imagine opening and closing both hands, “goal-oriented thoughts,” and rest # Sessions: 2 Session duration: <1h Task duration: eight 8s trials per task for training; 10–20s trials with 5s rest for testing

CP, cerebral palsy; avg., average; MI, motor imagery; N, number of participants; P#, pediatric participant number; SSVEP, steady state visual evoked potential; synch, synchronous; asynch, asynchronous; TD, typically developing; CNN, convolutional neural network; mVEP, motion-onset visual evoked potential; EEG, electroencephalography; EMG, electromyography; ERD, event-related desynchronization; MRCP, movement-related cortical potential; GMFCS, gross motor function classiﬁcation system; n/a, not applicable.

Brain-ComputerInterfacesforChildrenOrlandietal.

TABLE 2 | Research articles on pediatric non-invasive BCIs: signal processing techniques and results (only for pediatric age).

References Online/ofﬂine/# of classes Signal processing and features

Classiﬁer or analysis Results

Ehlers et al.

(2012)

Online only 5 classes: 5 visual stimulation frequency targets in low, medium, or high frequency range

Chance level: n/a

Fs: 2,048Hz Filtering: High-pass (fc = 0.1Hz) Low-pass (fc = 552.96Hz)

Features: Minimum energy combination spatial ﬁlter

Classiﬁer: Bremen-BCI Outcome Measure: (i) Accuracy

Ofﬂine accuracy: n/a Online accuracy: Low-frequency stimulation Group 1: 40%; Group 2: 50%; Group 3: 50% Medium-frequency stimulation Group 1: 55%; Group 2: 50%; Group 3: 75% High-frequency stimulation Group 1: 38%; Group 2: 45%; Group 3: 55% Additional measures: n/a

Norton et al.

- (2018)

Ofﬂine and Online 3 classes: 3 SSVEP targets

Chance level: n/a

Fs: 128Hz Filtering: Bandpass 1–30Hz Features:

- (i) Threshold
- (ii) Window-length

Classiﬁer: Canonical correlation analysis Outcome Measure:

- (i) Classiﬁcation accuracy
- (ii) Latency
- (iii) Nykopp bitrate

Ofﬂine accuracy: 11 of 14 children exceeded the threshold of success: 40–100% Online accuracy: P: 79% Additional measures: Latency: 2.106s Nykopp bitrate: 0.5 bits s −1

Beveridge

- et al. (2017)

Ofﬂine 5 classes: 5 target locations for mVEP

and 2 classes: Leave one out cross validation among the 5 targets

Online 5 target locations classiﬁed using target vs. non-target binary classiﬁcation

Chance level: 20% (0 bpm) for 5 class-classiﬁer 50% for 2 class-classiﬁer (theoretical chance level)

Fs: 250Hz, resampled to 20Hz Filtering: Baseline-corrected, Low-pass ﬁlter (fc = 10Hz) Features: (i) mVEP components (e.g., P100, N200, and P300): data averaged over 5 trials (12 feature vectors per stimulus)

Classiﬁer: LDA Outcome Measure:

- (i) Classiﬁcation accuracy
- (ii) ITR

Ofﬂine accuracy (LOOCV & 5-class):

- P1: 84.58 & 76.67 P9: 94.79 & 98.33
- P2: 94.58 & 96.67 P10: 78.75 & 71.67
- P3: 84.79 & 81.67 P11: 90.42 & 91.67
- P4: 83.54 & 70.00 P12: 77.50 & 68.33
- P5: 86.46 & 85.00 P13: 88.75 & 85.00
- P6: 77.29 & 76.67 P14: 82.29 & 75.00
- P7: 88.96 & 85.00 P15: 72.92 & 70.00
- P8: 91.88 & 81.67 Mean: 85.17 & 80.89 Online accuracy:

- P1: 54%* P9: 75%*
- P2: 88%* P10: 51%*
- P3: 45%* P11: 58%*
- P4: 65%* P12: 60%*
- P5: 83%* P13: 85%*
- P6: 61%* P14: 82%*
- P7: 82%* P15: 40%*
- P8: 92%* Mean: 68%** Additional measures: ITR

- P1: 4 bpm* P9: 13 bpm*
- P2: 19 bpm* P10: 4 bpm*
- P3: 3 bpm* P11: 6 bpm*
- P4: 8 bpm* P12: 7 bpm*
- P5: 16 bpm* P13: 17 bpm*
- P6: 7 bpm* P14: 16 bpm*
- P7: 16 bpm* P15: 2 bpm*
- P8: 21 bpm* Mean: 11 bpm**

(Continued)

TABLE 2 | Continued

References Online/ofﬂine/# of classes Signal processing and features

Classiﬁer or analysis Results

Beveridge et al. (2019)

Ofﬂine 5 classes: 5 target locations for mVEP

and 2 classes: LOOCV among the 5 targets

Online 5 target locations classiﬁed using target vs. non-target binary classiﬁcation

Fs: 250Hz, resampled to 20Hz Filtering: Baseline-corrected, Low-pass ﬁlter (fc = 10 Hz) Features: (i) mVEP components (e.g., P100, N200, and P300): data averaged over 5 trials (12 feature vectors per stimulus)

Classiﬁer: LDA Outcome Measure:

- (i) Classiﬁcation accuracy
- (ii) ITR
- (iii) mVEP latency
- (iv) mVEP amplitude

- -Same results as Beveridge et al.

(2017)

- -Online results showed that BCI naïve adults achieved higher accuracies than BCI naïve children (the difference is not always statistically signiﬁcant)

Chance level: 20% (0 bpm) for 5 class-classiﬁer 50% for 2 class-classiﬁer (theoretical chance level)

Vaˇreka (2020) Ofﬂine only 10 classes: 10 P300 targets

Chance level: n/a

Fs: 1,000Hz Filtering: Baseline-corrected, amplitude threshold 100 µV Features: (i) Averaged time intervals and feature scaled to zero mean and unit variance

Classiﬁer: LDA, SVM, and CNN in leave one out cross validation Outcome Measure:

- (i) Accuracy
- (ii) Precision
- (iii) Recall
- (iv) AUC

Taherian et al.

(2017)

Jochumsen

- et al. (2018)

Zhang et al.

- (2019)

Online only 2 classes: Left and right arm motor imagery

Chance level: n/a

Ofﬂine only 2 classes: idle vs. movement-related activity

Chance level: 60–65%

Online only 2 classes: MI/goal-oriented thought and rest

Chance level: 70% (0.40 Cohen’s Kappa)

Fs: n/a Filtering: Proprietary Emotiv software Features: Proprietary Emotiv software (Cognitiv suite)—ERD

Fs:1,000Hz Filtering: 4th order zero phase shift Butterworth bandpass 0.1–45Hz, baseline correction Features:

- (i) Mean amplitudes
- (ii) Absolute band power
- (iii) Template matching
- (iv) All features combined

Fs: 2,048Hz resampled to 128Hz Filtering: Proprietary Emotiv software

Features: Proprietary Emotiv software—ERD

Classiﬁer: Emotiv classiﬁer—proprietary output from Emotiv Software Development Kit Outcome Measure: (i) peak performance score

Classiﬁer: Random forest classiﬁer in LOOCV Outcome Measure: (i) Classiﬁcation accuracy

Classiﬁer: Emotiv classiﬁer—PNN and RBF Outcome Measure: (i) Cohen’s kappa

Ofﬂine accuracy: Single-trial classiﬁcation accuracy 62–64% Accuracy with trial averaging 76–79% Online accuracy: n/a Additional measures:

- (i) Single-trial classiﬁcation
- (ii) Precision-−61.5–63.5%***
- (iii) Recall-−60.5–67.5%***
- (iv) AUC-−62–66%*** all tested models achieved comparable classiﬁcation results

Ofﬂine accuracy: n/a Online accuracy: n/a Additional measures:

Peak performance score for left and right arm

Ofﬂine accuracy: 75–85% Online accuracy: n/a Additional measures: n/a

Ofﬂine accuracy: n/a Online accuracy: n/a Additional measures:

Average Kappa score of 0.46, range of 0.025–0.9

Fs, sampling frequency; fc, cut-off frequency; SSVEP, steady state visually evoked potential; mVEP, motion-onset visual evoked potential; MI, motor imagery; ITR, information transfer rate; LOOCV, leave-one-out cross-validation; CNN, convolutional neural network; LDA, linear discriminant analysis; SVM, support vector machine; AUC, area under the ROC curve; *Averaged across all 3 laps (estimated from bar graph); **Averaged across all 3 laps; ***Estimated from bar graph-range includes achieved averages for all three classiﬁer results; ERD, event-related desynchronization; PNN, probabilistic neural network; RBF, radial basis function; bpm, bits per minute; P#, pediatric participant number; n/a, not applicable.

accuracy: ∼38%; group 2: ∼45%; group 3: 55%; adults: ∼62%). An age-speciﬁc shift was observed in the peak synchronization frequency. Peak synchronization increases from 8 to 9Hz in

the lowest age group to 10–11Hz in adults. Aborted attempts decreased with increasing age and increased as the accuracy level decreased (particularly evident in the high drop-out rates of the

July2021|Volume15|Article64329411FrontiersinHumanNeuroscience|www.frontiersin.org

TABLE 3 | Research articles on pediatric invasive BCIs: Study objectives and data collection details.

References Study objective Sample size [females]

Age (years) Diagnosis Applications BCI paradigm

Mode of operation

Signal type

Data acquisition Task and sessions

Sanchez et al.

(2008)

Present techniques to spatially localize motor potentials

Pediatric N = 2 [2]

14–15

- P1: 14
- P2: 15

Breshears et al.

- (2011)

Decodable nature of pediatric brain signals for the purpose of neuroprosthetic control

N = 11 [n/a]

Pediatric N = 6 [1]

9–46

Pediatric 9–15

- P1: 15
- P2: 11
- P3: 15
- P4: 9
- P5: 12
- P6: 13

Intractable epilepsy

Neuroprosthetics/mouse control

MI or motor execution (hand opening/closing, tongue protrusions, phoneme articulation)

Synch ECoG Location: motor, temporal, and prefrontal areas, depending on the patient # Channels: 48 or 64 Hardware and Software:

- -AdTech electrode arrays
- - g.tec ampliﬁer
- -BCI2000
- -MATLAB®

Task: move a cursor on a screen along one-dimension using motor execution or imagined movement # Sessions: 1 Session duration: 10–37min Task duration: 2–3s

Pistohl et al.

- (2012)

ECoG signal decoding for hand conﬁgurations in an everyday environment

Pediatric N = 3 [3]

14–16

- P1: 14
- P2: 16
- P3: 15

Epilepsy Neuroprosthetics/reachto-grasp

Motor execution

Asynch (selfpaced)

ECoG Location: electrodes residing over hand-arm motor cortex as identiﬁed through anatomical location and electrical stimulation # Channels: 48 or 64 Hardware and Software:

-IT-Med clinical EEG-System

Task: reach-to-grasp

movements (self-paced and largely self-chosen movements)

# Sessions: 1 Session duration: – Time of analyzed data:

- P1: 32min (303 grasps)
- P2: 35.3min (338 grasps)
- P3: 25.4min (320 grasps) Task duration: 60ms per grasp

Pistohl et al.

- (2013)

Time of grasps from human ECoG recording from the motor cortex during a sequence of natural and continuous reach-to-grasp movements

Pediatric N = 3 [3]

14–16

- P1: 14
- P2: 16
- P3: 15

Intractable epilepsy

Neuroprosthetics Arm reaching and pointing

Synch ECoG Location: sensorimotor cortex # Channels: 36 and 32 Hardware and Software: -MATLAB®

Task: arm reaching and pointing # Sessions: 1 Session duration: 6 task repetitions Task duration: 5s

Same as Pistohl et al. (2012) as the participants and experimental paradigm is the same.

N, number of participants; ECoG, electrocorticography; P#, pediatric participant number; MI, motor imagery; synch, synchronous; asynch, asynchronous; n/a, not applicable.

Brain-ComputerInterfacesforChildrenOrlandietal.

TABLE 4 | Research articles on pediatric invasive BCIs: signal processing techniques and results (only for pediatric age).

References Online/ofﬂine/# of classes

Signal processing and features Classiﬁer/outcome measures Results

Sanchez et al. (2008)

n/a

Chance level: n/a

Breshears et al. (2011)

Online only 2 classes: Imagined or performed motor movement vs. rest

Chance level: 50% (theoretical chance level)

Pistohl et al.

- (2012)

Ofﬂine 2 classes: precision grip, whole-hand grip 10-fold cross-validation (20 repetitions)

Chance level: 50% (theoretical chance level)

Fs: 256Hz Filtering: Re-referenced to common average, average voltage subtracted, normalized voltage, low pass ﬁltered component (fc ∼5Hz) Features: (i) Signal components

Classiﬁer: rLDA Outcome Measure:

- (i) Decoding accuracy
- (ii) Temporal evolution of grasp discriminability

Ofﬂine accuracy:

- P1: 97%
- P2: 84%
- P3: 96% Online accuracy: n/a Additional measures: Temporal evolution of grasp discriminability: 0.2s

Pistohl et al.

- (2013)

Ofﬂine only 2 classes: grasp and no grasp

Chance level: n/a

Fs: 381.5Hz Filtering: FIR ﬁlter (1–6kHz) Features:

- (i) Equiripple FIR ﬁlter: 1–60Hz, 60–100Hz, 100–300Hz, 300 Hz−6kHz
- (ii) FIR ﬁlter topology trained using the Wiener solution

Classiﬁer: n/a Outcome Measure: (i) Pearson’s r

Fs: 1,200Hz Filtering: Autoregressive spectral coefﬁcients in 2Hz frequency bins from 0 to 250Hz for each electrode Features:

- (i) Spectral power of ﬁltered frequency bins
- (ii) Spectral power of electrodes

Classiﬁer: Real-time translational algorithm based on the weighted linear summation of the identiﬁed features (showing power increases were assigned positive weights, or power decreases were assigned negative weights) Outcome Measure: (i) Accuracy for each action

Ofﬂine accuracy: n/a Online accuracy: n/a Additional measures: Pearson’s r for X-position; Y-position

- P1: 0.39 ± 0.26; 0.48 ± 0.27
- P2: 0.42 ± 0.26; 0.45 ± 0.25 Highest r achieved with 300 Hz−6kHz feature

Ofﬂine accuracy: n/a Online accuracy:

- P1: 70.8–99.0%
- P2: 72.7–77.4%
- P3: 82.7–85.1%
- P4: 75.0–100%
- P5: 88.8 %
- P6: 93.3 % Additional measures: n/a

Fs: 256 or 1,024 Hz Filtering: LFC: 2nd order Savitzky-Golay ﬁlter (window length: 250ms) Features:

- (i) LFC
- (ii) Frequency band amplitudes within consecutive bands of 4Hz width from 0 to 128Hz. Band pass ﬁltering by 4th order elliptic digital ﬁlter design

Classiﬁer: rLDA in 10-fold cross-validation Outcome Measures:

- (i) True positive ratio (TPR)
- (ii) False positive ratio (FPR)
- (iii) False positive min−1 (FP-rate)

Ofﬂine accuracy: After 0.25s (TPR/FPR/FP-rate):

- P1: 0.75/0.26/2.5
- P2: 0.50/0.36/2.7
- P3: 0.75/0.25/3.1 After 0.50s (TPR/FPR/FP-rate):

- P1: 0.92/0.10/0.9
- P2: 0.69/0.12/0.9
- P3: 0.91/0.08/1.0 After 0.75s (TPR/FPR/FP-rate): P1: 0.97/0.05/0.4 P2: 0.74/0.05/0.4 P3: 0.96/0.03/0.4 Online accuracy: n/a Additional measures: n/a

Fs, sampling frequency; fc, cut-off frequency; rLDA, regularized linear discriminant analysis; FPR, false positive ratio; TPR, true positive ratio; FP-rate, false positive rate; P#, pediatric participant number; LFC, low-pass ﬁltered component; FIR, ﬁnite impulse response; n/a, not applicable.

youngest age group under low-frequency stimulation). Lastly, the authors discovered the inability to adequately control a BCI using the low-frequency rates. The age factor gains inﬂuence with decreasing stimulation frequency.

Similarly, Norton et al. (2018) used the SSVEP paradigm to compare the performance between 15 TD children (aged 9– 11) and 11 adults (aged 19–68) in a laboratory environment using a graphical interface. Oﬄine and online results but no chance level were reported. Authors included a minimum oﬄine accuracy requirement for the online analysis. Authors did not specify the number of sessions in their study. We assumed that participants performed only one session preceded by BCI calibration. Participants were asked to focus their attention on

three white circles, each alternating between white and black at three diﬀerent frequencies (6.2, 7.7, and 10Hz) on the screen. During calibration, participants were directed to focus on the circle highlighted by an on-screen arrow. Participants subsequently repeated the same task without the arrow to test the system online. Norton et al. (2018) applied a calibration phase and a longer experimental phase to classify three diﬀerent SSVEP targets. If the calibration phase accuracy was <85%, the participant could not proceed to the experimental phase (online phase). Eleven children and all adults met the minimum accuracy requirement. Children and adults achieved similar performance during the experimental phase (accuracy: 79 vs. 78%; latency: 2.1 vs. 1.9s; bitrate: 0.05 vs. 0.56 bits s−1).

Feature extraction and classiﬁcation were based on the canonical correlation analysis (CCA) and used to determine the SSVEP targets. Norton et al. (2018) used a method similar to that applied by Lin et al. (2006) wherein EEG signals from multiple channels were used to calculate the CCA coeﬃcients considering the stimulus frequencies in the systems. The frequency with the highest coeﬃcient indicates the SSVEP frequency. This study demonstrated that children can use an SSVEP-based BCI with higher accuracy (average accuracy: 79%) than Ehlers et al. (2012) when low-frequency stimulus is applied. However, their good performance could be dependent on the diﬀerent environments. Participants completed a target selection task and not a text-entry task. Also, they applied diﬀerent stimulus frequencies.

Beveridge et al. (2017) evaluated whether 15 TD adolescents (aged 13–16) could gain control of an mVEP-BCI paradigm for video game playing. Oﬄine and online accuracy of target vs. non-target stimuli classiﬁcation (chance level: 50%) and 5class discrimination results (chance level: 20%) were reported. Participants were engaged in a 3D car racing video game that involved changing lanes at several checkpoints performing three laps. As participants approached a checkpoint, one of the ﬁve motion stimuli was presented above each of ﬁve lanes with an arrow indicating the target lane for positioning the car. Participants attended to the motion stimulus associated with the target lane. If the target lane was selected correctly by the BCI, participants were rewarded with points and speed boost. The authors collected 300 mVEP trials from 12 gel-based EEG electrodes to calibrate a classiﬁer tested with additional 300 trials. Beveridge et al. (2019) subsequently reported performance achieved by BCI-naïve and BCI-experienced adults with a nearidentical protocol. For this review, Beveridge et al. (2017) and Beveridge et al. (2019) were considered identical as they relied on the same adolescent dataset. The two studies by Beveridge et al. (2017, 2019) report results from a single adolescent mVEP dataset. The collected mVEP data were resampled from 250 to 20Hz and ﬁltered. Data were averaged over ﬁve trials to generate 12 feature vectors for each stimulus which corresponded to the 12 EEG channels. Oﬄine and online accuracies and information transfer rate (ITR) were reported for each participant. Participants achieved 85.17% oﬄine accuracy through a leave-one-out cross-validation, and 68% accuracy and 11 bits per minute during online trials. The authors reported Cz, P7, and O1 as the most discriminative channels across participants. Beveridge et al. (2019) also compared the group of BCI naïve teenagers with nine BCI naive adults. Adults achieved higher classiﬁcation accuracies compared to teenagers (average accuracies in 3 laps: 75.4 vs. 68%), but the diﬀerence between adults and teenager was signiﬁcant only in the third lap.

Lastly, Vaˇreka (2020) entailed large-scale oﬄine analysis of P300 visually-evoked potential signals collected from 250 children (aged 7–17) without any identifying physical symptoms, playing “Guess the Number.” This game requires participants to focus on a self-selected number between 1 and 9 as a series of numbers (1–9) ﬂash on a screen in random order. When ﬂashed, the selected number elicits a P300 response. Thus, the algorithm predicts the selected number. Oﬄine results but no chance levels were reported. Vaˇreka (2020) collected 532 trials

using three channels. The study aimed to compare convolutional neural networks (CNNs) against linear discriminant analysis (LDA) and support vector machines (SVM). The author applied a baseline to correct each epoch and eliminated epochs containing amplitudes exceeding 100 µV. Epochs were divided into 20 equal-sized intervals wherein the amplitudes were averaged. Features were classiﬁed separately using CNN, LDA, and SVM. All classiﬁers produced similar classiﬁcation accuracies. Singletrial classiﬁcation accuracies ranged between 62 and 64%, while trial averaging raised accuracies to 76–79%. Precision, recall, and area under a receiver operating characteristic (ROC) curve (AUC) were 61.5–63.5%, 60.5–67.5%, and 62–66%, respectively, for single-trial classiﬁcation. Averaging groups of one to six neighboring epochs instead of single trials improved classiﬁcation accuracies.

Motor-Related Activities

Three studies investigated motor-related activities with children (Taherian et al., 2017; Jochumsen et al., 2018; Zhang et al., 2019).

Two studies applied a MI paradigm (Taherian et al., 2017; Zhang et al., 2019) and EMOTIV system, a commercially available headset. Although both studies reported the use of the same EEG device (EMOTIV Epoc R ), Zhang et al. (2019) referred to a dry system while Taherian et al. (2017) described a wet device. Zhang et al. (2019) reported that the electrode foam pads were immersed in a saline solution to ensure reliable connection before being placed on the child’s head. Both studies should have described the EMOTIV Epoc R as a headset with salinesoaked felt pads. These sensors are not wet in the traditional sense, but they are not considered truly dry. Both studies explored the possibility of implementing an EEG-based visual motion BCI and they used the Emotiv Software Development Kit (SDK) for the analysis and classiﬁcation. Both studies extracted modulation features. Classiﬁcation results were obtained based on ERD phenomenon.

Taherian et al. (2017) evaluated the feasibility of implementing an EEG-based BCI using the 14-saline-based electrode version of this headset in ﬁve children (aged 9–17) with spastic quadriplegic CP. The EMOTIV is packaged with software that provides visual feedback of cognitive tasks and a gamiﬁed training protocol. Participants donned the EMOTIV Epoc R headset and completed six 30-min training sessions where they were guided through the EMOTIV software to move a virtual cube up, down, left, or right using MI of the limbs. EEG signals were processed using CognitivTM Suite provided by EMOTIV Epoc R . The Cognitiv system processes the brainwaves and matches them to the patterns of thought trained, relying on ERD, detected on the EEG signals within the frequency range of 0.2 and 43Hz (Lang, 2012). The authors developed a puzzle game and participants were asked to complete the puzzle after each training session. The puzzle was completed in an online paradigm using the same MI tasks from the training sessions while continuous visual feedback was provided. When participants were able to produce MI tasks with precision, they were rewarded with a puzzle piece. Participants completed ﬁve to seven sessions. Unfortunately, Taherian et al. (2017) reported only online performance scores for left and right arm for some participants in graphs and do not report accuracy,

latency, or bitrate. Performance values were approximated and based on graph readings. All participants experienced challenges following protocol for various reasons related to their condition, including: diﬃculties focusing; seizures during trials; anxiety; equipment discomfort; lack of enjoyment when playing. All pediatric participants demonstrated inconsistent and unreliable control of BCI. They concluded that existing commercial BCIs are not designed according to the needs of end-users with CP.

Zhang et al. (2019) conducted a cross-over interventional study on 26 TD children (aged 6–18) to estimate the performance of two tasks (driving a remote-control car and moving a computer cursor). Children participated in two sessions where they performed a MI task (imagery of opening and closing both hands to move the car or the cursor) and a “goal-oriented thought” task (think of moving the car or the cursor toward a target). During each session, participants completed eight trials as training data for the BCI followed by 10 testing trials to evaluate the system performance. The BCI’s goal was to complete the designated task (car or cursor) using one of two strategies (MI or goal-oriented thought). We assumed that Zhang et al. (2019) used the Emotiv SDK to extract ERD features using an 8-s window. They reported good performance using the EPOC headset and Radial Basis Probabilistic Neural Network to distinguish between baseline and training epochs. Zhang et al. (2019) reported online results (chance level: 70% classiﬁcation accuracy, 0.4 Cohen’s kappa) in terms of Cohen’s kappa scores (range 0.025–0.90). Performance correlated with increasing age, but sex was not associated. A Cohen’s kappa of 0.4 or higher indicated successful control.

Jochumsen et al. (2018) deployed motor execution tasks to elicit MRCP in the motor cortex. MRCP is an event-related potential locked to the onset of a movement, reﬂecting the preparatory brain activity. They detected MRCPs in 8 adolescents with hemiplegia or diplegia CP (aged 11–17) via EEG, with the goal of maximizing motor learning by temporally aligning aﬀerent feedback with the cortical manifestation of movement intention. Oﬄine classiﬁcation accuracy (chance level: 60–65%) was reported. Participants dorsiﬂexed an ankle at self-determined pace during a single 15-min session. Electromyographic signal was used to divide continuous EEG into epochs. Mean amplitudes, absolute band power, and template matching were extracted from each channel after ﬁltering. Template matching was obtained by calculating the cross-correlation between the template of the movement epochs (averaged epochs for each channel for each participant) and the epochs. A random forest discriminated movement intention epochs from idle epochs using a leave-one-out cross-validation and achieved up to 85% accuracy.

For study objective, population, and tasks of non-invasive BCIs see Table 1. For signal processing techniques and results see Table 2.

Invasive Pediatric BCIs

Four articles (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013) included in this category used ECoG as invasive modality for interrogating the pediatric brain. Three of these studies applied motor execution paradigms while one

additionally invoked MI (Breshears et al., 2011). Studies recruited individuals with epilepsy who had implanted electrode grids used to monitor brain activity prior to surgery.

First invasive pediatric BCI study was presented by Sanchez et al. (2008). They explored motor control paradigm with two adolescents aged 14 and 15 years who had an electrode array implanted to monitor their intractable epilepsy prior to surgery. Participants engaged in six repetitions of arm reaching and pointing tasks. ECoG signals were decoded from premotor, motor, somatosensory, and parietal cortices using a linear adaptive ﬁnite impulse response (FIR) ﬁlter trained with Wiener solution. Sanchez et al. (2008) reported the ﬁrst example of the ability to decode pediatric ECoG signals for an online BCI model. They processed ECoG signals collected during reaching and pointing task by ﬁrst ﬁltering the data between 1 and 6kHz. Features from each channel were fed into the above FIR ﬁlter topology to generate estimate of arm trajectory. Pearson’s correlation was used to determine how closely the decoded signals matched the true arm’s trajectory. The highest Pearson’s correlations were achieved using the 300 Hz−6kHz frequency band feature.

Breshears et al. (2011) demonstrated the decodable nature of ECoG signals from motor and/or language (Wernicke’s or Broca’s area) cortices by six pediatric participants (aged 9–15) who required invasive monitoring for intractable epilepsy. To move a cursor on the screen, children performed a motor (e.g., hand opening and closing, repetitive tongue protrusion) or phoneme articulation (oo, ah, eh, ee) task. Participants were asked to move the cursor along one dimension to hit a target on the opposite side of the screen during a single online session. Trials were grouped into runs of up to 3min with a rest period of <1min. Breshears et al. (2011) applied an autoregressive spectral estimation in 2Hz bins ranging between 0 and 250Hz to decode ECoG signals. For each electrode and frequency bin, power increases or decreases in the signiﬁcant task-related spectral power were identiﬁed by calculating the r2 correlation between baseline spectra and activity spectra for each active task. Online performance accuracy (chance level: 50%) was calculated considering the number of successes (i.e., hit the target) divided by the total number of movements after each block. Results were compared to a previous study (Leuthardt et al., 2004; Wisneski et al., 2008) conducted with ﬁve adult participants (aged 23–46). The results showed that the pediatric participants’ performance matched the adults’ one and signals can be decoded and aﬀected in the same way as adult brain signals. Within 9min of training, children achieved 70–99% target accuracy in experiments where multiple cognitive modalities were used to achieve an imagined action to control a cursor on the screen. Children controlled the cursor using hand movements using β (15–40Hz) and γ (60–130Hz) frequency ranges and, two with tongue movements using high-γ (107.5– 155Hz) frequency range. Four of the six participants began with achieved accuracies <70%. Two participants were able to generate BCI control using imagined movement rather than over performance of the task. The mean accuracy was 81% and the mean training time was 11.6min. The adult group required 12.5min and reported a mean accuracy of 72%. Table 4 outlines the range of accuracies for each participant using one or diﬀerent

movements. These ﬁndings form proof of concept that decoding signals from the pediatric cortex is possible and may be used for BCI control.

Turning attention speciﬁcally to grasping movements, Pistohl et al. (2012) conducted a single-session of study with three pediatric participants (aged 14–16) who had electrodes implanted for pre-surgical epilepsy diagnostics. Participants’ self-initiated reach-to-grasp of a cup with either precision or whole-hand grip, relocated the cup and ﬁnally returned their hand to a central resting position. Participants completed between 303 and 338 trials. Pistohl et al. (2012) focused on two-class classiﬁcation of precision grip and whole-hand grip on oﬄine analysis (chance level: 50% classiﬁcation accuracy). Common average reference and low-pass ﬁltering were applied. The authors utilized an rLDA classiﬁer and reported decoding accuracy and temporal evolution of grasp discriminability. The three participants achieved between 84 and 97% decoding accuracy. Temporal evolution of grasp discriminability was 0.2 s.

Subsequently, Pistohl et al. (2013) utilized the same data to automatically detect the time of grasping movements within a continuous ECoG recording. After ﬁltering, authors extracted frequency band amplitudes and trained an rLDA classiﬁer to distinguish two classes, occurrence of the grasp and no grasp. Ten-fold cross-validation was used to test detection performance for each subject. Oﬄine results were reported. Based on the previous work, we assumed that the chance level considered was 50% but the authors did not report it. Results showed amplitudes recorded in the high-gamma range from hand-arm motor-related channels were used to achieve the best performance. Local maxima between 56–128Hz and 16–28 Hz. Low-pass ﬁltered components, 16–28 and 56–128Hz amplitudes reported best classiﬁcation results when used together to feed the classiﬁer. Sensitivity and speciﬁcity depended on temporal precision of detection and on the delay between event detection and when the event occurred.

For study objective, population, and tasks of invasive BCIs

- see Table 3. For signal processing techniques and results
- see Table 4.

Quality Assessment and Risk of Bias

The quality of the included studies ranged from 45% (Taherian

- et al., 2017) to 91% (Zhang et al., 2019), with a median score of 0.70 and an interquartile range of 0.60–0.76. For breakdown of quality, appraisal markings see Table 5. Ten included papers present primary exploratory research using a multiple case study design, and two present cross-sectional studies (Ehlers et al., 2012; Zhang et al., 2019). Overall, the quality of the studies was adequate. One study was assessed as limited (Taherian et al., 2017), six as adequate (Sanchez et al., 2008; Breshears et al.,

- 2011; Pistohl et al., 2013; Beveridge et al., 2017, 2019; Norton

et al., 2018), three as good (Ehlers et al., 2012; Pistohl et al.,

- 2012; Jochumsen et al., 2018), and two as strong (Zhang et al., 2019; Vaˇreka, 2020). However, some of the algorithms used by Zhang et al. (2019) are proprietary, making it diﬃcult for the reproducibility of the experiments because the EMOTIV SDK may require buying a license to access some of the

APIs. For the quality assessment of the signal processing, we considered suﬃcient reporting information about the features extracted and the classiﬁcation algorithms applied. Also, we did not take into account open science (data and software/code sharing) and the reproducibility of the obtained results for the quality assessment. We highlight that Vaˇreka (2020) is the only included study that made publicly available data and software code. Table 6 and Figure 4 report the domain-level judgments for each study and a summary bar plot of the distribution of the risk-of-bias assessment within each bias domain. Breshears et al. (2011), Ehlers et al. (2012), Norton et al. (2018), and Beveridge et al. (2019) are the only studies comparing children to adults. Only six studies (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Jochumsen et al., 2018; Norton et al., 2018; Zhang et al., 2019) considered important inclusion and exclusion criteria for selection bias: information related to the dominant hand; previous experience with BCI; use of medication; individual participants’ age; gender; history of brain injury. Four studies (Sanchez et al., 2008; Breshears

- et al., 2011; Pistohl et al., 2012, 2013) included children with epilepsy but did not control for epilepsy-related brain activity or diﬀerences in the electrode positioning. Vaˇreka (2020) required large numbers of participants but did not report individual participants’ ages or handedness or report results for male vs. female. In terms of maintaining ﬁdelity to the study protocol, nine studies implement the same protocol consistently across participants. Three studies applied protocols including a diﬀerent number of sessions and trials across participants (Breshears et al., 2011; Ehlers et al., 2012; Taherian et al.,

- 2017). Missing data (e.g., participants who dropped out or researchers’ excluded trials or low performance) were considered and handled appropriately only in one study (Norton et al.,
- 2018). Three studies took missing data into consideration but did not discuss or analyze them appropriately (Ehlers

- et al., 2012; Taherian et al., 2017; Zhang et al., 2019). We did not consider questions related to assessors blinded to the intervention or exposure status of participants, because blinding is not appropriate for BCI studies. Two studies did not assess outcomes using valid and reliable measures (Ehlers et al., 2012; Taherian et al., 2017). Ehlers et al. (2012) reported an unclear deﬁnition of the performance evaluation (e.g., correctto-complete commands ratio). Taherian et al. (2017) did not include a reliable measure in their protocol (i.e., performance score). Table 7 summarizes the performance evaluation metrics used in the 12 studies in this review. In terms of confounding variables assessed, we considered participants’: age; gender; fatigue; psychological factors. Only one study did not introduce bias through confounding variables (Zhang et al., 2019). One article did not pre-specify outcomes (Taherian et al., 2017). Regarding bias that might aﬀect these 12 studies, we highlight only ﬁve studies reported concerns due to the small sample sizes (Sanchez et al., 2008; Breshears et al., 2011; Jochumsen et al., 2018; Zhang et al., 2019). Vaˇreka (2020) is the only study that recruited many participants. Self-reporting risk of bias was applicable only for one study (Zhang et al., 2019), which included: questionnaires for psychological and cognitive information; BCI workload.

July2021|Volume15|Article64329416FrontiersinHumanNeuroscience|www.frontiersin.org

TABLE 5 | QualSyst scores for quantitative papers.

References QUALSYST criteria (quantitative) Score (%)

Quality grade

measurement/misclassiﬁcation

ofsubjectswaspossible,was

ofinvestigatorswaspossible,

Someestimateofvarianceis

Resultsreportedinsufﬁcient

Analyticmethodsdescribed/

Outcomesand(ifapplicable)

allocationwaspossible,was

Ifinterventionalandblinding

Ifinterventionalandblinding

Ifinterventionalandrandom

reporterforthemainresults

bias?Meansofassessment

subject/comparisongroup

describedandappropriate

well-deﬁnedandrobustto

Conclusionssupportedby

information/inputvariable

Studydesignevidentand

justiﬁedandappropriate

Samplesizeappropriate

Subjectcharacteristic

selectionorsourceof

sufﬁcientlydescribed

sufﬁcientlydescribed

(pediatricpopulation)

exposuremeasures

Question/objective

wasitreported?

Controlledfor

itdescribed?

confounding

itreported?

appropriate

theresults

Methodof

reported?

detail

Sanchez et al.

(2008)

- 2 2 1 2 N/A N/A N/A 1 0 1 1 0 2 2 70 Adequate

Breshears et al.

(2011)

- 2 2 1 2 N/A N/A N/A 2 0 1 0 N/A 1 1 60 Adequate

Ehlers et al. (2012) 2 2 1 2 N/A N/A N/A 1 0 2 1 1 2 2 73 Good

- Pistohl et al. (2012) 2 2 1 2 N/A N/A N/A 2 0 2 0 0 2 2 75 Good
- Pistohl et al. (2013) 1 1 1 2 N/A N/A N/A 2 0 2 1 N/A 2 2 70 Adequate Beveridge et al.

- (2017)

- 1 2 1 2 N/A N/A N/A 1 0 1 0 1 1 2 60 Adequate

Taherian et al. (2017) 2 2 1 2 N/A N/A N/A 0 0 0 0 N/A 0 2 45 Limited Jochumsen et al.

(2018)

- 2 2 1 2 N/A N/A N/A 2 0 2 1 N/A 2 2 80 Good

- (2019)

Norton et al. (2018) 2 2 1 1 N/A N/A N/A 2 1 1 1 1 1 2 68 Adequate Beveridge et al.

1 2 1 2 N/A N/A N/A 1 0 1 0 1 1 2 60 Adequate

Zhang et al. (2019) 2 2 2 1 N/A N/A N/A 2 1 2 2 2 2 2 91 Strong Vaˇreka (2020) 2 2 1 1 N/A N/A N/A 1 2 2 2 1 2 2 90 Strong

Criteria were scored either 2 or 1 or 0 (2 = yes, 1 = partial, 0 = no) or if the criteria were not applicable to the paper it was scored N/A (not applicable). To make them comparative, overall scores are presented as a %. Quality grade: limited (score of ≤50%), adequate (>50% and ≤70%), good (>70% and ≤80%), strong (>80%) (Lee et al., 2008).

Brain-ComputerInterfacesforChildrenOrlandietal.

- TABLE 6 | Risk of bias.

References Source of bias Selection bias Performance bias Attrition bias Detection bias Reporting bias Overall bias

Sanchez et al.

+ – ? + – High

(2008)

Breshears et al.

+ – ? + – High

(2011)

Ehlers et al. (2012) – – + + – Medium

- Pistohl et al. (2012) + – ? + – High
- Pistohl et al. (2013) + – ? + – High Beveridge et al.

- (2017)

– – ? + – Medium

Taherian et al. (2017) + + + + + High Norton et al. (2018) – – – + – Low Jochumsen et al.

- (2018)

– – ? + – Medium

Beveridge et al.

- (2019)

– – ? + – Medium

Zhang et al. (2019) – – + – – Low Vaˇreka (2020) + – ? + – High

+, high-risk of bias; ?, uncertain/non-applicable risk of bias; –, low-risk of bias.

|[Figure 5]<br><br>FIGURE 4 | Bar plot visualization of risk-of-bias assessments.|
|---|

Evaluation Factors

Evaluation factors usually reported for BCI studies are: usability; performance; user’s satisfaction; evaluation of psychological factors; brain workload; fatigue; quality of life; cognitive evaluation (Nicolas-Alonso and Gomez-Gil, 2012; Choi et al., 2017). Only one study reported subject fatigue using a 5point Likert scale questionnaire (Zhang et al., 2019). Zhang et al. (2019) used a self-report questionnaire to investigate the psychological factors of participants during BCI experiments. Taherian et al. (2017) justiﬁed the absence of self-report questionnaires due to the severity of participants’ conditions and limited communication capabilities. In terms of performance,

most of the studies reported accuracy rates (see Table 7). Norton et al. (2018) was the only study with a self-report questionnaire for the usability of the BCI system.

DISCUSSION Pediatric BCIs

The primary objective of this systematic review was to examine studies related to the use of BCIs in pediatric populations. We described the current state-of-the-art for pediatric BCIs and assessed the quality and the risk of bias of the 12 articles. The included studies raise several challenges addressed in

- TABLE 7 | Performance evaluation metrics used in the 12 studies on pediatric BCIs.

References Performance

Sanchez et al. (2008) →Accuracy Breshears et al. (2011) →Accuracy Ehlers et al. (2012) →Accuracy

- Pistohl et al. (2012) →Correlation coefﬁcients
- Pistohl et al. (2013) →TPR/FPR/FP-rate

Beveridge et al. (2017) →Accuracy

→ITR Taherian et al. (2017) →Performance score Jochumsen et al. (2018) →Accuracy Norton et al. (2018) →Accuracy

→Latency

→Bitrate Beveridge et al. (2019) →Accuracy

→ITR

→Latency Zhang et al. (2019) →Cohen’s kappa Vaˇreka (2020) →Accuracy

→Precision

→Recall

→AUC

FPR, false positive ratio; TPR, true positive ratio; FP-rate, false positive rate; AUC, area under ROC curve; ITR, information transfer rate.

the following sections where we describe considerations for future research to make BCI technologies suitable for children. We also identify requirements to render BCIs suitable for clinical translation.

BCIs for Communication: State-of-the-Art

Regarding studies investigating BCIs for communication, a wide range of methods were implemented yielding various levels of success. Seven studies involved non-invasive EEG as the signal acquisition modality (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Taherian et al., 2017; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020). Five studies analyzed evoked potentials (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Norton et al., 2018; Vaˇreka, 2020) and two used movement-related potentials as the control signal (Taherian et al., 2017; Zhang et al., 2019).

Two studies took advantage of the active mental task MI (Taherian et al., 2017; Zhang et al., 2019). Taherian et al. (2017) deployed a consumer-grade EEG headset with ﬁve youth with spastic quadriplegic CP to decode left and right arm MI. This was the ﬁrst study that involved children and computer access with a commercial EEG-BCI using the EMOTIV Epoc R hardware, but participants achieved poor accuracies (0.08–0.56 peak performance score range). Zhang et al. (2019) utilized the same low-cost commercial EEG headset as Taherian et al.

- (2017) to compare MI and “goal-oriented thinking” as tasks to control either a toy car or computer cursor with TD children. Participants achieved an online Cohen’s kappa score of 0.46 pointing to successful control of the BCI. Importantly, they found performances were higher when users were controlling toy car vs. computer cursor. These results were attributed to the increased

engagement of the children when controlling the car. This study points to the potential of low-cost BCIs being successfully used as a binary switch with pediatric users. It is unclear whether the poor results achieved by Taherian et al. (2017) are due to neurological diﬀerences of children with CP compared to TD children. It is possible that the physical and cognitive limitations, common among children with CP, were the source of diﬀerences in achieved accuracies.

Many limitations in current methods emerge when translating BCIs for communication to the target population (e.g., children with severe disabilities). For example, in the study by Taherian et al. (2017), participating children had unique head shapes that limited the ability of the electrodes on the BCI to gain contact with the scalp. Additionally, individuals with CP have been known to produce large muscular artifacts due to involuntary movements. Since the authors were unable to record raw EEG data, it is unclear whether artifacts disrupted signal acquisition, ultimately aﬀecting their training data. The embedded EMOTIV system used by Taherian et al. (2017) may not have adequate artifact reduction methods, which would signiﬁcantly aﬀect the classiﬁcation of the signals. Lastly, the authors reported another issue due to the severity of participants’ conditions. They found many diﬃculties conducting 30min training sessions and mentioned the impossibility of collecting enough EEG data to adequately train the classiﬁers. Moreover, participants were unable to learn to reproduce speciﬁc MI tasks within the timeframe of the study. In contrast, Zhang et al. (2019) demonstrated that a goal-oriented strategy works better than MI task with children and it may be useful for teaching MI tasks to children with disabilities. They found a BCI illiteracy rate higher in children than in adults and emphasized the potential diﬃculty children experience when reproducing their thought strategy in each trial. These issues might be resolved by including additional training phases in the study acquisition protocol for pediatric BCIs. The lack of customization of commercial headsets for pediatric head sizes may also justify reduced performances of children as compared to adults. For this reason, Zhang et al. (2019) had many diﬃculties placing the electrodes in locations dictated by the international 10–20 system in pediatric BCI studies.

The other ﬁve communication-focused studies utilized the reactive tasks known as SSVEP (Ehlers et al., 2012; Norton et al., 2018), mVEP (Beveridge et al., 2017, 2019), and P300 (Vaˇreka, 2020). The two studies investigating SSVEP (i.e., where the user visually ﬁxates on a ﬂashing target to indicate its selection) utilized the EEG signal acquisition modality and achieved mixed results. There are three main performance measurements of an SSVEP-based BCI: accuracy (probability of predicted target matching the target), latency (mean time from target onset to classiﬁcation), and bit rate (transfer information rate, e.g., the amount of information conveyed per time unit). Ehlers et al. (2012) tested an SSVEP-BCI with ﬁve visual targets achieving quite poor results with 40 TD children. Accuracies ranged from 38 to 75%. Results reported by Ehlers et al. (2012) demonstrated that mean accuracy rates depend on age and frequency of the stimulation (10–11Hz). The adult comparison group obtained consistently higher accuracy rates compared to

all three children samples and an age-speciﬁc shift can be seen in the peak synchronization frequency. Their ﬁndings align with those reported by Roland et al. (2011). Using an ECoG and EEGBCI, Roland et al. (2011) found that higher frequency bands show signiﬁcant correlations with age in participants aged 11–59 years. This full-text was excluded because authors did not report BCI performance. Norton et al. (2018) built upon the work of Ehlers et al. (2012) by improving an SSVEP-BCI for TD children. Eleven of the 15 children exceeded the threshold of successful BCI control during oﬄine sessions and attained an average of 79% online classiﬁcation accuracy. This result was statistically similar to results achieved by the participating adult cohort. While the achieved bit rates of pediatric participants were lower than adults, this study points to the promise of successful control of SSVEP-BCIs by pediatric users. As noted in Norton et al. (2018), there are many methodological diﬀerences between their study and Ehlers et al. (2012), which may explain result diﬀerences. Methodological discrepancies include diﬀerences in the task controlled by the BCI, slightly diﬀerent stimulation frequencies, involvement of a calibration phase, dissimilar environmental settings, and exclusion of participants after a poor calibration phase. Lastly, Norton et al. (2018) is the only study where performance is reported in terms of accuracy, latency, and bit rates. The latency is the average amount of time between the onset of the stimuli and the classiﬁcation of the predicted target (Norton et al., 2018). Norton et al. (2018) showed that children were slower than adults, although this result was not signiﬁcant.

The two studies by Beveridge’s group (Beveridge et al., 2017, 2019) involve racetrack video games and are the ﬁrst studies with pediatric subjects using mVEP-BCI applications. The overarching goal of these two articles is to explore a BCI task that is less visually fatiguing than commonly investigated alternative BCI tasks such as SSVEP and P300. They demonstrated the feasibility of mVEP paradigm achieving an average accuracy of up to 72% but did not apply any measurement or questionnaires to evaluate visual fatigue among participants. The absence of a qualitative and quantitative evaluation of visual fatigue limits the reliability of these two papers despite the high performance reported.

Vaˇreka (2020) is the ﬁrst study that includes a large group of pediatric participants (e.g., 250) and that applied deep learning algorithms (e.g., CNN) in BCIs for children. The study showed that LDA, SVM, and CNN had similar classiﬁcation performance (62–64% accuracy) using P300 features. The article reports higher performance (∼77% accuracy) when the BCI employs averaging of P300 trials. Comparing trial groupings of various sizes (1–6 trials), average classiﬁcation accuracy increases with each group size increase. Vaˇreka (2020) reports an important limitation of CNN for BCIs: LDA and SVM showed faster computational time than CNN (300ms, 1,600ms vs. 46s CPU/26s GPU). Vaˇreka (2020) is the only study conducted in a school setting. The authors suggest that the school setting likely hindered the children’s performance. This is corroborated by the fact that 30.3% of epochs were rejected due to noise. Artifact correction was not possible due to the limited number of EEG channels used (only three electrodes). The authors could have employed a larger number of channels to increase spatial resolution and likely also the performance accuracy.

BCIs for Mobility: State-of-the-Art

Five studies exploring BCIs for mobility have involved children in the last 12 years (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013; Jochumsen et al., 2018). Four of the ﬁve studies utilized invasive techniques and acquired ECoG signals (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013).

Sanchez et al. (2008) investigated ECoG amplitude modulation for motor control tasks (e.g., reaching and grasping) for the ﬁrst time with a small group of pediatric participants. Sanchez et al. (2008) generated online predictive models to decode motor commands in the primary motor cortex. The predicted trajectories showed moderate correlations with actual trajectories. However, the estimates involved very large variances representing the models’ inability to distinguish the motor activity from noise in a realistic setting.

Breshears et al. (2011) conducted the ﬁrst study on pediatric ECoG-BCI presenting a comparison of results between adult and pediatric participants. Breshears et al. (2011) demonstrated that recent advances in neuroprosthetic research may be applied to BCI applications with children. The technology is ready to move beyond single case studies to be tested in wide-spectrum experimentation of BCI for mobility involving a pediatric population. They showed that prepubescent and peripubescent children can rapidly and eﬀectively achieve control of a computer cursor (accuracy: 70–99%), after short training times of 8– 18min, using a multitude of diﬀerent cognitive modalities and their associated cortical physiologies. Although neurofeedback on brain signals has been used previously with children, its use was primarily for diagnostic and therapeutic purposes, rather than the express purpose of control alone.

Pistohl et al. (2012, 2013) reported good performance in arm and grasp movement prediction with their ECoG-BCI. The authors recorded from hand and arm areas of the human motor cortex as sites likely to be utilized in future BCI applications. While predictions were quite reliable at sub-second precision, the observed temporal deviations might still be too large for applications requiring very precisely timed movement control. Their grasping detection method based on linear discriminant analysis on ECoG recordings from the motor cortex can predict events 125–250ms before their occurrence, without accuracy loss.

Jochumsen et al. (2018) investigated motor preparation and execution tasks performed by children with CP and collected with EEG. This is the only non-invasive mobility study captured by this review. Participants achieved accuracies as high as 85% when classifying ankle dorsiﬂexion activity vs. idle. Jochumsen’s group also demonstrated that children with CP can generate motorrelated cortical potentials that are visually discernable, creating the possibility of motor decoding using non-invasive modalities such as EEG with children with CP.

Pediatric Participants and Sample Size

The 12 publications included were speciﬁcally targeting BCIs for use with children (Sanchez et al., 2008; Breshears et al., 2011; Ehlers et al., 2012; Pistohl et al., 2012, 2013; Beveridge et al., 2017, 2019; Taherian et al., 2017; Jochumsen et al., 2018; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020). These studies

generally included a limited number of pediatric participants and combined children and youth. Three of the papers compared adults and children (Ehlers et al., 2012; Taherian et al., 2017; Beveridge et al., 2019), however only Beveridge et al. (2019) discussed possible diﬀerences in performance due to cognitive and neurological diﬀerences between participants. Thirteen fulltext articles were excluded because they included only a few pediatric participants among a heterogeneous age group, without developing a speciﬁc protocol for pediatric ages (e.g., Pistohl et al., 2008; Schalk et al., 2008; Perego et al., 2011; Milekovic

- et al., 2012; Zhang et al., 2013). An additional 28 papers were excluded due to the inclusion of a homogenous group of adults and children, without special consideration for diﬀerences between the two groups of participants (e.g., Treder et al., 2011; Weyand et al., 2015). It is critical that researchers acknowledge the physiological diﬀerences between adults and children when studies involve participants spanning the pediatric and adult age ranges.

Overall, the sample sizes of pediatric participants in the studies were small, ranging from two (Sanchez et al., 2008) to 250 (Vaˇreka, 2020). Half of the studies involved fewer than 10 pediatric participants (Tables 1, 3). Only one study exceeded 51 participants (Vaˇreka, 2020). Despite a large sample size, Vaˇreka (2020) did not perform any statistical analysis among results nor did they stratify participants into small age groups to determine eﬀect of age on performance. Median number of pediatric participants in reviewed studies was 11. In total, 370 pediatric participants were enrolled across 12 studies, with 250 contributed by Vaˇreka (2020). Excluding Norton et al. (2018) who did not report participant sex, 42% of children and youth were female. Average age of pediatric participants across studies was 13.3 ± 3.2 years. For mobility-related BCI studies, most of the participants clustered around mid-adolescence (14–16 years) while for communication BCI studies, participants were mostly scattered between 9 and 18 years. Notably, across all studies, only four participants were <9 years old. Figure 5 shows the age distribution of pediatric participants excluding Ehlers et al. (2012), Beveridge et al. (2017, 2019), Norton et al.

- (2018), and Vaˇreka (2020). Age data extracted from Zhang et al. (2019) data were interpolated and extracted from a graph reported in the article. Two studies (Ehlers et al., 2012; Norton et al., 2018) reported only the average of participants’ ages. Future studies should continue to increase sample sizes, as this will allow for more powerful investigations of age on performance.

Inclusion of Individuals With Disabilities

It is important to note the scarcity of studies involving individuals with disabilities in both the pediatric and adult BCI literature. Kübler et al. (2013) stated that <10% of published BCI papers include participants with severe motor disability, despite this group being the ultimate target population of the research. Among the papers examined in this review, only Taherian et al.

- (2017) and Jochumsen et al. (2018) included participants of the target population (namely, CP) of pediatric age. Jochumsen et al.
- (2018) involved youth with CP performing a motor task and found that the participants demonstrated MRCP. Researchers

questioned whether MRCP could be discriminated due to the atypical movements and reorganized motor cortical networks of individuals with CP (Papadelis et al., 2018).

The progression of research involving adult participants has progressed from involving typically developed adults to including adults with disabilities. Just as it has been for BCI studies involving adult participants, BCI research projects should ﬁrst include able-bodied children and then immediately extend to children with disabilities. BCI studies should be designed as prospective cohort studies with strong experimental designs involving pediatric participants with severe motor disabilities rather than solely TD controls. Several studies have investigated the use of BCIs for attention-deﬁcit hyperactivity disorder treatment in children showing promising results (Kulseng et al.,

- 2007; Sigurdardottir et al., 2010; Felton et al., 2012; Rohani et al., 2014; Gabis et al., 2015). P300 is typically used in this training and the successful results indicate that the BCIs can accurately distinguish P300 signals in the participating children. Unfortunately, we could not include these studies because they were published in conference proceedings or they did not report BCI performance measures.

BCI User Experience of Children

So far, studies have only reported that photosensitivity of some children may preclude the use of some BCI paradigms. None of the studies in this review reported any adverse events. Potential disadvantages of BCIs include the time and eﬀort required to learn to use a BCI system and the speed at which information can be transferred. Additionally, the inconvenience of the setup and cleanup of the hardware associated with the technology as well as its discomfort and portability may compromise integration into daily life. These considerations will need to be balanced with the promise that BCI holds to facilitate communication and quality of life for people who have explored all other options available. Researchers have the responsibility to provide accurate and balanced information for the young potential participants and their families. Assent should be encouraged, and longterm follow-up embedded within the study design. Moreover, as reported in a notable review on augmentative and alternative communication (AAC) by Akcakaya et al. (2014, p. 24): “some children with disabilities would certainly beneﬁt from using BCIs for communication and control, and researchers should begin to investigate this possibility.” BCIs have the potential to be used as assistive technology devices for pediatric users but only Breshears et al. (2011) addressed the use of a BCI for AAC devices. This study explores BCI assistive technologies for mobility support and customized communication devices activated using tasks such as vocalization (e.g., oo, ah, eh) or tongue protrusion. These tasks can be used to control a laptop, showing how a BCI can support children with disabilities in their daily life.

Mental Tasks and Brain Signals

With respect to the mental tasks used in the 12 articles, motor-related tasks, P300, SSVEP, and mVEP paradigms were investigated.

Seven studies applied motor-related BCIs (Sanchez et al.,

- 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013; Taherian

|[Figure 6]<br><br>FIGURE 5 | Age distribution in pediatric BCIs. Ehlers et al. (2012), Norton et al. (2018), Beveridge et al. (2017, 2019), and Vaˇreka (2020) were not considered as they did not provide a speciﬁc age breakdown for their participants.|
|---|

et al., 2017; Jochumsen et al., 2018; Zhang et al., 2019). Three studies (Breshears et al., 2011; Taherian et al., 2017; Zhang et al., 2019) applied MI paradigms. Three articles (Taherian et al., 2017; Jochumsen et al., 2018; Zhang et al., 2019) applied motor potential BCIs. There are many beneﬁts to the use of movement-related BCI tasks (Taherian et al., 2017; Zhang et al.,

- 2019), such as the ability to perform the task without intact visual abilities. Additionally, motor-related control may allow for control signals that are intuitive, such as imagining moving the right hand to turn a wheelchair to the right. Lastly, high achieved accuracies unlock the potential to control devices with as many degrees of freedom as physical movement. However, many researchers questioned the feasibility of MI tasks for children with congenital movement conditions, such as CP (Lust et al., 2016). The concept of MI is abstract and may be diﬃcult for some children to understand. Furthermore, children with severe physical disabilities who have never had functional control of their limbs might ﬁnd it very challenging to perform MI tasks. The included studies focusing on movement-initiated BCIs (Breshears et al., 2011; Pistohl et al., 2012, 2013; Jochumsen et al., 2018) made excellent ﬁrst steps toward decoding neuronal activity related to movement. For target users who are unable to perform these movements, the BCIs must be prepared to detect the imagination of these movements for these tasks to be useful.

Five included studies (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Norton et al., 2018; Vaˇreka, 2020) investigated the use of evoked potential paradigms (P300, SSVEP, and mVEP). One of the main beneﬁts of using evoked-potentials for BCIs is the ability to create a system with extremely large degrees of freedom as the detection of one evoked potential allows for quick selection among several presented options. The use of mVEP (Beveridge et al., 2017, 2019) and P300 (Vaˇreka, 2020) is quite

new in BCI research. P300 is the most successful BCI task in adult users due to its low training time to gain proﬁciency and high achievable accuracies (Abiri et al., 2018). P300 allows users to select among dozens of options and might be considered the best method for applications for assistive technology and AAC devices. Vaˇreka (2020) showed for the ﬁrst time the feasibility of P300 with children reaching promising classiﬁcation performance (62–79% accuracy). One of the ﬁndings of Vaˇreka (2020) study is the large variability of P300 components present in children’s signals. This is probably due to the large age range (7–17) used as participants’ inclusion criterion. Unfortunately, due to the rate of ﬂashing options, P300 may have the potential to induce photo-epileptic seizures in users with epilepsy or in young users who are unaware of their photosensitivity. For the same reason, SSVEP tasks must also be used with caution with children with disabilities, especially for children with CP who often have visual impairments (Gabis et al., 2015). mVEPs may be a possible alternative to ﬂash-based BCIs and have been applied in BCI spelling applications (Hong et al., 2009) and neurogaming (Beveridge et al., 2016) in adults. Beveridge et al. (2017) is the ﬁrst study that applied mVEP paradigm with children and youth obtaining reasonable online performance at 70% accuracy. mVEP-based BCIs are similar to P300 BCIs as users focus on a single option among several. The mVEP paradigm relies on N200 ERPs generated when visual motion occurs on the option that the user is focusing their attention on. This paradigm may be more suitable for children who are photosensitive as it does not involve any ﬂashing lights. Overall, these evoked tasks require immense focus and maintenance of gaze on the computer screen for the brain potentials to be evoked. This can be challenging to achieve for children with disabilities, especially for those who often have involuntary movements, such as children with CP.

Additionally, evoked potential paradigms require intact sensory function. Children with CP often have visual impairments which preclude the use of these evoked tasks (Gabis et al., 2015).

An alternative to visual evoked potentials is the P300-based BCI that uses covert speech or mental singing. Both tasks have been extensively investigated in adult BCI research and should be explored with children as it requires intact hearing alone. Agerelated diﬀerences in EEG responses have been explored in prior works related to auditory stimuli (Kolev and Yordanova, 1997; Sanders and Zobel, 2012). Although auditory evoked potentials are not fully mature until at least 16 years of age, research indicates that children around 5 years of age show spatially selective attention on auditory evoked potentials when listening to one of the two simultaneously presented non-verbal sounds (Sanders and Zobel, 2012). These ﬁndings are further supported by research studies (Kolev and Yordanova, 1997; Sanders and Zobel, 2012), which show clear evidence that auditory P300 signals in pediatric age should be investigated in future research.

Overall, when selecting a mental task for children, it is critical to implement tasks that are intuitive and require low eﬀort. Ehlers et al. (2012) reported pediatric-speciﬁc deﬁcits in the ability to perform a visual search task that the adult participants could perform. Additionally, user fatigue and visual annoyance are factors to consider when selecting a task. This systematic review revealed that only three studies (Breshears et al., 2011; Pistohl

- et al., 2013; Zhang et al., 2019) focused on mental tasks geared toward children and youth. Norton et al. (2018) noted that two children were visibly distracted during their calibration phase and attributed this to their choice of boring tasks. Beveridge et al. (2017, 2019) justiﬁed lower classiﬁer performance speculating fatigue and reduction of interest or waning concentration, but they did not introduce any qualitative assessment and they did not ask participants about these factors. It is critical that engaging tasks are selected for these studies. Zhang et al. (2019) speciﬁcally focused on comparing two types of activities: a toy car and a computer cursor. They found improved BCI control when children were controlling a toy car. This may be due to the improved engagement the toy created for the participating children. Future studies should focus on creating engaging tasks to foster the optimal performance of the children and collect qualitative and quantitative evaluation factors to describe how children’s performance vary along with their development.

Signal Acquisition Modality

Eight of the studies investigating BCIs as an access technology involved the non-invasive EEG signal acquisition modality (Ehlers et al., 2012; Beveridge et al., 2017, 2019; Taherian et al., 2017; Jochumsen et al., 2018; Norton et al., 2018; Zhang et al., 2019; Vaˇreka, 2020). The remaining four studies involved invasive ECoG-BCIs with children with intractable epilepsy (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013). As a result, electrode arrays were placed according to the requirements of the clinical epilepsy evaluation. Thus, not all the desired regions were included for motor task detection.

When discussing the use of ECoG-BCI research with children, it is important to consider whether brain signal acquisition is safe for a developing brain and whether there are negative long-term eﬀects. While the meta-analysis was not an appropriate approach

for this review, in general, studies involving ECoG yielded more successful outcomes than those involving EEG. This is likely due to the larger detectable frequency range, higher spatial resolution of ECoG than EEG (mm vs. cm), improved signal-to-noise ratio, and the potential to control more complex devices that require detecting small and speciﬁc patterns of brain activity.

EEG Signal Challenges

Main challenges faced when developing pediatric BCIs have previously been outlined by Ding et al. (2008) and Giedd et al. (1999) describing the ongoing development of a child’s brain and its reorganization in presence of a brain injury and in those with atypical brain organization (Johnston, 2009; Deng, 2010; Pannek et al., 2014). EEG potentials generated by developing pediatric brains diﬀer from adults, rendering signal features commonly extracted for successful adult BCIs potentially useless. Neurodevelopmental consequences of brain injury result in additional diﬀerences in EEG signal patterns when compared to able-bodied adults. Children’s psychological and physiological state can inﬂuence the performance as the prefrontal cortex continues to rapidly develop until the age of 25 (Arain et al., 2013). Structural and functional MRI studies involving tasks used in BCI systems can be referenced to inform electrode positioning and source localization. Also, age-speciﬁc headmodels are missing in EEG and MRI studies. Finally, challenges exist regarding EEG signal acquisition. High-density, gel-based, and wired EEG devices involving long training sessions are not ideal for children, especially those with disabilities. Children can experience more sensory sensitivities to gel, abrasion, and headgear. There is not a wide range of dry, active, and/or wireless headsets available for pediatric head sizes, nor for those with diﬀerences in head shape (Sellers et al., 2009; Slater et al., 2012; Hairston et al., 2014).

ECoG Signal Issues

Since the participants of the presented ECoG studies have intractable epilepsy and there was not a control group, it is possible their atypical brain activity contributed to identiﬁcation of features applicable only in children with epilepsy (Sanchez et al., 2008; Breshears et al., 2011; Pistohl et al., 2012, 2013). Another limitation of the ECoG modality is its invasive nature and requirement of a craniotomy to implant an electrode grid (Nicolas-Alonso and Gomez-Gil, 2012). This poses signiﬁcant health hazards (Nicolas-Alonso and Gomez-Gil, 2012) and creates a lack of feasibility for widespread use. Long-term stability of the signals acquired by ECoG and the longevity of the implanted grid are currently uncertain (Nicolas-Alonso and Gomez-Gil, 2012). The grids utilized in the ECoG studies were not placed for long-term use. As children grow and develop, it is unclear whether the implanted electrode grid would shift or cause damage. These considerations should be addressed in future studies on ECoG-BCI.

Personalized Methods

Each article presented in this review applied the same channels and features among participants included in each research study. Even when eﬀorts are made to create a homogenous group of participants, individual diﬀerences in brain activity when

performing the same task should be considered. Personalized channel and feature selection would maximize individual BCI performance. For example, a multitude of features could be extracted oﬄine and a feature selection algorithm would then implement the top features for online use.

Outcome Measures

Among the reviewed studies there is inconsistency in the metrics used for presenting results as summarized in Table 7. Included studies rarely reported classiﬁcation results in terms of sensitivity and speciﬁcity. Studies reported: accuracy (Sanchez et al., 2008; Breshears et al., 2011; Ehlers et al., 2012; Beveridge et al., 2017, 2019; Jochumsen et al., 2018; Norton et al., 2018; Vaˇreka, 2020); bit rates (Norton et al., 2018); correlation coeﬃcients (Pistohl

- et al., 2012); performance score (Taherian et al., 2017); ITR (Beveridge et al., 2017, 2019); latency (Norton et al., 2018; Beveridge et al., 2019); true positive and false positive ratios (Pistohl et al., 2013); Cohen’s Kappa score (Zhang et al., 2019); precision, recall and AUC (Vaˇreka, 2020). How much the decoding accuracy deviates from chance level should be always reported. Chance level refers to the rate achieved by random classiﬁcation. For a 2-class problem, the theoretical chance level is 50%, for a 5-class problem it is 20%, etc. Unfortunately, the theoretical chance level is valid only for a large number of samples (or trials). We noted that the chance level used by most of the studies was based on the theoretical level of chance (Breshears et al., 2011; Pistohl et al., 2012; Beveridge et al., 2017, 2019). Zhang et al. (2019) considered a 70% chance level based on previous studies with adult participants (Scherer
- et al., 2013; Jeunet et al., 2016). The chance level of a BCI system created from a relatively small data set depends on the number of classes, sample size, and threshold for statistical signiﬁcance of the classiﬁcation (Combrisson and Jerbi, 2015). A simple binomial distribution involving these variables generates the threshold that must be surpassed for statistically signiﬁcant classiﬁcation accuracies (Combrisson and Jerbi, 2015). Another method for determining statistical signiﬁcance of results is through the permutation test (Nichols and Holmes, 2002; Good, 2013).

Sanchez et al. (2008), Ehlers et al. (2012), Pistohl et al. (2013), Taherian et al. (2017), Norton et al. (2018), and Vaˇreka (2020) did not report the chance level. Jochumsen et al. (2018) is the only included study that estimated the chance level based on the number of trials (Müller-Putz et al., 2008).

Furthermore, for applications involving mobility, timing, and precision of the BCI output are of utmost importance. If the output were controls for a wheelchair, imprecise movements or timing delays could result in dangerous consequences for the user. Future research studies should consider reporting the same metrics at least in terms of accuracy, sensitivity, speciﬁcity, latency, and bit rates.

Future Research and Requirements for Clinical Translation

Although much of what we understand about BCI for communication and mobility has been gained by exploring

the responses of able-bodied adults to various brain activity protocols, research into BCI for individuals with disabilities has been increasing in recent years. Despite this, few research studies address the application of BCIs for communication and mobility in children. BCIs hold the potential to enable people with severe physical disabilities, who are unable to speak and who do not have voluntary muscle control, to communicate and operate other technologies without any physical movements (Wolpaw et al., 2002). A small number of studies provide encouraging evidence for continued research in children with studies demonstrating children as young as 7 years of age (Ehlers et al., 2012; Zhang et al., 2019) can learn to control their brain activity and perform activities on the computer. Recently, there has been an emergence of two new mental tasks being investigated with children (mVEP and P300) and a study that recruited unprecedented numbers of children (Vaˇreka, 2020). However, the clinical translation of pediatric BCIs still requires additional research to address several challenges. To summarize our recommendations, we report a list of potential requirements to be considered for BCI clinical translation. Future studies should:

- • Continue to recruit large numbers of participants akin to Vaˇreka (2020).
- • Collect smaller sub-groups of child age ranges, instead of large age ranges (e.g., 7–17), to investigate as neurodevelopment varies across childhood-adolescence.
- • Include comparisons between children and adults.
- • Include a TD group as a control, for studies focused on children with disabilities.
- • Report the age and sex information, as their correlation with BCI performance would result in a better understanding of how to customize BCIs for children across stages of neurodevelopment.
- • Collect more accompanying qualitative data, considering physiological factors, BCI experience, fatigue, and workload through standardized questionnaires to avoid bias.
- • Develop study protocols speciﬁc for children and include additional training phases for those who do not have experience with BCIs.
- • Increase preparation time and reduce the participant discomfort during data collection. An additional requirement is the comfort of wearable headsets and caps. Children are more sensitive to fatigue and discomfort, therefore wearing portable headsets for a long period of time can be challenging. Novel headsets speciﬁcally designed for children’s heads should be developed.
- • Include game activities. Considering the diﬃculty of children to maintain attention during mental tasks, BCI paradigms should be engaging and include customized activities and games. Also, games similar to those successfully implemented in the ADHD BCI studies could be utilized in future studies as pediatric appropriate activities. These reward-based attention games could be employed as training for BCI sessions to maintain focus as BCI sessions also require intense engagement of children through the presentation of cues and stimuli (Gavin and Davies, 2007).

- • Develop customizable BCI algorithms and investigate the best algorithms suitable for pediatric BCIs. As highlighted in this systematic review, there is still no feature extraction or machine learning technique clearly established as state-of-theart for pediatric BCIs.
- • Improve performance accuracy in predicting the user’s intent (Wolpaw and Wolpaw, 2012) especially in children, as they historically achieve inadequate performance for practical use (Mikołajewska and Mikołajewski, 2014).
- • Be consistent in reporting algorithm performance results. In the case of binary classiﬁcation, results should be reported in terms of accuracy and sensitivity (e.g., classiﬁer sensitivity, speciﬁcity, standard deviation, etc.). In multi-class paradigms, other performance metrics should be considered like recall, precision, and F1-score. In this case, accuracy may be diﬃcult to interpret, especially if unbalanced classiﬁcation (i.e., diﬀerent number of samples per class).
- • Share datasets and frameworks. In fact, we noticed that none of the publications mentioned the possibility of sharing children’s brain signals or sharing their code or framework, except the study by Vaˇreka (2020) that used a public dataset (Mouˇcek et al., 2019) and shared the software code used for reproducibility of the obtained results. Future studies should consider publishing their datasets and sharing data analysis frameworks to better understand the feasibility of introducing BCI technology in clinical practice.
- • Investigate new technologies combining multiple brain signals in pediatric populations. For example, hybrid BCI systems (e.g., fNIRS-EEG BCIs) could achieve better performance accuracy rates than single modality systems (Wolpaw and Wolpaw, 2012; Sereshkeh et al., 2019).
- • The error-related potential (ErrP) can be detected in the EEG if a person perceives the mistake. Two components of the ErrP can be identiﬁed: the error-related negativity (ERN or Ne) which is a negative potential peaking 50–100ms after an erroneous response, and the error-related positive potential, called error positivity (Pe), follows the ERN. Several studies examined ErrP in adults but only a few studies have investigated ErrP in children. Also, results are not consistent among these studies. ERN may be reliably detected before age 12 (Davies et al., 2004), or it may be present at 10 years of age (Santesso et al., 2006), or even at 7–8 years of age (Kim et al., 2007; Wiersema et al., 2007). The amplitude was found to be smaller for children compared to adults (Wiersema et al., 2007) but no signiﬁcant diﬀerences were found (Kim et al., 2007). Furthermore, ERN can even be reliably elicited in children as young as 5–7 years old (Torpey et al., 2009). As such, research on ErrP should investigate if ErrPs are clearly present in pediatric brain signals.
- • Prioritize BCI research with pediatric participants to better understand if a BCI system can be used as assistive technologies with children.

Limitations

Substantial heterogeneity in the included studies concerning the participant’s diagnosis, age, tasks, methods, and outcome measure prevented any pooling or meta-analysis of results for

this systematic review. Our conclusions may be inﬂuenced by the small sample sizes of the identiﬁed studies that included only case studies or small groups of pediatric participants. We excluded studies aimed at providing diagnoses or therapeutic interventions in this systematic review because we targeted communication and mobility BCIs. Also, the focus on English-written articles forms a limitation of this study as other languages were not captured. Our decision to appraise the quality of included studies using QualSyst may create limitations. The checklist items represent the authors’ perception of research quality and given the absence of gold standard BCI protocols, it is diﬃcult to accurately assess the validity of the tool itself, but it was the only one applicable to the study design of the 12 articles. Finally, the use of summary scores to categorize studies may introduce bias into a review (Kmet et al., 2004). It is important to note the two research papers, Lim et al. (2012) and Rohani et al. (2014), fall outside our inclusion criteria because they focused on improving attention in children with attention-deﬁcit and hyperactivity disorders (ADHD). They found successful results using EEG BCI-based games. Furthermore, to highlight the importance of this topic, we highlight that 10 papers screened were excluded only because they did not report BCI performance (e.g., Antle et al., 2018; Park et al., 2019).

## CONCLUSION

This systematic review presented the state-of-the-art of BCIs for children. It highlighted previously successful methods and paradigms and outlined actions that should be taken to develop new access technologies based on brain activity for children with severe disabilities. Despite very few research studies addressing the application of BCIs for communication and mobility in children, results are encouraging, and future research should investigate how BCIs can be better customized for pediatric ages.

## DATA AVAILABILITY STATEMENT

The data supporting this systematic review are from previously reported studies and datasets, which have been cited. The processed data used to generate tables and ﬁgures of this manuscript are available from the corresponding author upon request.

## AUTHOR CONTRIBUTIONS

SO and SCH performed data search, data analysis, and wrote the manuscript in consultation with PK, RS, and TC. SO, SCH, PK, and RS performed article identiﬁcation. Article’s design, data acquisition, and analysis of content were made by consensus among all the authors. TC supervised the project.

## FUNDING

This study has been supported by Project No. 512527 for ISED BCI SWITCH funded by the Government of Canada. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Frontiers in Human Neuroscience | www.frontiersin.org 24 July 2021 | Volume 15 | Article 643294

## REFERENCES

Abiri, R., Borhani, S., Sellers, E. W., Jiang, Y., and Zhao, X. (2018). A comprehensive review of EEG-based brain-computer interface paradigms. J. Neural Eng. 16:011001. doi: 10.1088/1741-2552/aaf12e

Akcakaya, M., Peters, B., Moghadamfalahi, M., Mooney, A. R., Orhan, U., Oken, B., et al. (2014). Noninvasive brain computer interfaces for augmentative and alternative communication. IEEE Rev. Biomed. Eng. 7, 31–49. doi: 10.1109/RBME.2013.2295097

Amiri, S., Fazel-Rezai, R., and Asadpour, V. (2013). A review of hybrid brain-computer interface systems. Adv. Hum. Comput. Interact. 2013:187024 doi: 10.1155/2013/187024

Antle, A. N., Chesick, L., Sridharan, S. K., and Cramer, E. (2018). East meets west: a mobile brain-computer system that helps children living in poverty learn to self-regulate. Pers. Ubiquitous Comput. 22, 839–866. doi: 10.1007/s00779-018-1166-x

Arain, M., Haque, M., Johal, L., Mathur, P., Nel, W., Rais, A., et al.

(2013). Maturation of the adolescent brain. Neuropsych. Dis. Treat. 9:449. doi: 10.2147/NDT.S39776

Bamdad, M., Zarshenas, H., and Auais, M. A. (2015). Application of BCI systems in neurorehabilitation: a scoping review. Disabil. Rehabil. Assist. Technol. 10, 355–364. doi: 10.3109/17483107.2014.961569

Bell, M. A., and Wolfe, C. D. (2007). Changes in brain functioning from infancy to early childhood: evidence from EEG power and coherence during working memory tasks. Dev. Neuropsychol. 31, 21–38. doi: 10.1207/s15326942dn3101_2

Berardi, A., Smith, E. M., and Miller, W. C. (2020). Assistive technology use and unmet need in Canada. Disabil. Rehabilitation. Assist. Technol. doi: 10.1080/17483107.2020.1741703. [Epub ahead of print].

Beveridge, R., Wilson, S., Callaghan, M., and Coyle, D. (2019). Neurogaming with motion-onset visual evoked potentials (mVEPs): adults versus teenagers. IEEE Trans. Neural. Syst. Rehabilitation Eng. 27, 572–581. doi: 10.1109/TNSRE.2019.29 04260

- Beveridge, R., Wilson, S., and Coyle, D. (2016). 3D graphics, virtual reality, and motion-onset visual evoked potentials in neuroimaging. Prog. Brain Res. 228, 329–353. doi: 10.1016/bs.pbr.2016.06.006
- Beveridge, R., Wilson, S., and Coyle, D. (2017). Can teenagers control a 3D racing game using motion-onset visual evoked potentials? Brain Computer Interfaces 4, 102–113. doi: 10.1080/2326263X.2016.1266725

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kübler, A., et al. (1999). A spelling device for the paralysed. Nature 398, 297–298. doi: 10.1038/18581

Birbaumer, N., Murguialday, A. R., Wildgruber, M., and Cohen, L. G. (2010). “Brain-computer-interface (BCI) in paralysis,” in The European Image of God and Man, eds H.-C. Günther and A. A. Robiglio (Brill Academic Publishers), 483–492. doi: 10.1163/ej.9789004184244.i-514.91

Breshears, J. D., Gaona, C. M., Roland, J. L., Sharma, M., Anderson, N. R., Bundy, D. T., et al. (2011). Decoding motor signals from the pediatric cortex: implications for brain-computer interfaces in children. Pediatrics 128, e160– e168. doi: 10.1542/peds.2010-1519

Brumberg, J. S., Pitt, K. M., Mantie-Kozlowski, A., and Burnison, J. D. (2018). Brain–computer interfaces for augmentative and alternative communication: a tutorial. Am. J. Speech. Lang. Pathol. 27, 1–12. doi: 10.1044/2017_AJSLP-16-0244

Cattan, G., Andreev, A., and Visinoni, E. (2020). Recommendations for integrating a P300-based brain-computer interface in virtual reality environments for gaming: an update. Computers 9:92. doi: 10.3390/computers9040092

Choi, I., Rhiu, I., Lee, Y., Yun, M. H., and Nam, C. S. (2017). A systematic review of hybrid brain-computer interfaces: taxonomy and usability perspectives. PLoS ONE 12:e0176674. doi: 10.1371/journal.pone.0176674

Choudhury, N. A., Parascando, J. A., and Benasich, A. A. (2015). Eﬀects of presentation rate and attention on auditory discrimination: a comparison of long-latency auditory evoked potentials in school-aged children and adults. PLoS ONE 10:e0138160. doi: 10.1371/journal.pone.0138160

Combrisson, E., and Jerbi, K. (2015). Exceeding chance level by chance: the caveat of theoretical chance levels in brain signal classiﬁcation and statistical assessment of decoding accuracy. J. Neurosci. Methods 250, 126–136. doi: 10.1016/j.jneumeth.2015.01.010

Cooke, A., Smith, D., and Booth, A. (2012). Beyond PICO: the SPIDER tool for qualitative evidence synthesis. Qual. Health Res. 22, 1435–1443. doi: 10.1177/1049732312452938

Daly, J. J., and Wolpaw, J. R. (2008). Brain-computer interfaces in neurological rehabilitation. Lancet Neurol. 7, 1032–1043. doi: 10.1016/S1474-4422(08)70223-0

Davies, P. L., Segalowitz, S. J., and Gavin, W. J. (2004). Development of responsemonitoring ERPs in 7-to 25-year-olds. Dev. Neuropsychol. 25, 355–376. doi: 10.1207/s15326942dn2503_6

De Venuto, D., Annese, V. F., Mezzina, G., Ruta, M., and Di Sciascio, E. (2016). “Brain-computer interface using P300: a gaming approach for neurocognitive impairment diagnosis,” in 2016 IEEE International High Level Design Validation and Test Workshop (HLDVT) (Santa Cruz, CA), 93–99.

Deng, W. (2010). Neurobiology of injury to the developing brain. Nat. Rev. Neurol. 6:328. doi: 10.1038/nrneurol.2010.53

Ding, X.-Q., Sun, Y., Braass, H., Illies, T., Zeumer, H., Lanfermann, H., et al. (2008). Evidence of rapid ongoing brain development beyond 2 years of age detected by ﬁber tracking. AJNR Am. J. Neuroradiol. 29, 1261–1265. doi: 10.3174/ajnr.A1097

Ehlers, J., Valbuena, D., Stiller, A., and Gräser, A. (2012). Age-speciﬁc mechanisms in an SSVEP-based BCI scenario: evidences from spontaneous rhythms and neuronal oscillators. Comp. Intel. Neurosc. 2012:967305. doi: 10.1155/2012/967305

Fager, S., Beukelman, D. R., Fried-Oken, M., Jakobs, T., and Baker, J. (2012). Access interface strategies. Assist. Technol. 24, 25–33. doi: 10.1080/10400435.2011.648712

Felton, E. A., Williams, J. C., Vanderheiden, G. C., and Radwin, R. G. (2012). Mental workload during brain-computer interface training. Ergonomics 55, 526–537. doi: 10.1080/00140139.2012.662526

Friman, O., Volosyak, I., and Graser, A. (2007). Multiple channel detection of steady-state visual evoked potentials for brain-computer interfaces. IEEE Trans. Biomed. Eng. 54, 742–750. doi: 10.1109/TBME.2006.889160

Gabis, L. V., Tsubary, N. M., Leon, O., Ashkenasi, A., and Shefer, S. (2015). Assessment of abilities and comorbidities in children with Cerebral Palsy. J. Child. Neurol. 30, 1640–1645. doi: 10.1177/0883073815576792

Gaillard, W. D., Sachs, B. C., Whitnah, J. R., Ahmad, Z., Balsamo, L. M., Petrella, J. R., et al. (2003). Developmental aspects of language processing: fMRI of verbal ﬂuency in children and adults. Hum. Brain Mapp. 18, 176–185. doi: 10.1002/hbm.10091

Gavin, W., and Davies, P. (2007). “Obtaining reliable psychophysiological data with child participants: methodological considerations,” in Developmental Psychophysiology: Theory, Systems, and Methods, eds L. Schmidt and S. Segalowitz (Cambridge: Cambridge University Press), 424–448.

Giedd, J. N., Blumenthal, J., Jeﬀries, N. O., Castellanos, F. X., Liu, H., Zijdenbos, A., et al. (1999). Brain development during childhood and adolescence: a longitudinal MRI study. Nat. Neurosci. 2, 861–863. doi: 10.1038/ 13158

Good, P. (2013). Permutation Tests: A Practical Guide to Resampling Methods for Testing Hypotheses. New York, NY: Springer Science & Business Media.

Goyal, A., Samadani, A.-A., Guerguerian, A.-M., and Chau, T. (2016). An online three-class Transcranial Doppler ultrasound brain computer interface. J. Neurosci. Res. 107, 47–56. doi: 10.1016/j.neures.2015.12.013

Guy, V., Soriani, M. H., Bruno, M., Papadopoulo, T., Desnuelle, C., and Clerc, M. (2018). Brain computer interface with the P300 speller: usability for disabled people with amyotrophic lateral sclerosis. Ann. Phys. Rehabil. Med. 61, 5–11. doi: 10.1016/j.rehab.2017.09.004

Hairston, W. D., Whitaker, K. W., Ries, A. J., Vettel, J. M., Bradford, J. C., Kerick, S. E., et al. (2014). Usability of four commercially-oriented EEG systems. J. Neural. Eng. 11:046018. doi: 10.1088/1741-2560/11/4/046018

He, B., Yuan, H., Meng, J., and Gao, S. (2020). “Brain?Computer Interfaces,” in: Neural Engineering, ed B. He (Cham: Springer). doi: 10.1007/978-3-030-43395-6_4

Herﬀ, C., Krusienski, D. J., and Kubben, P. (2020). The potential of stereotactic-EEG for brain-computer interfaces: current progress and future directions. Front. Neurosci. 14:123. doi: 10.3389/fnins.2020. 00123

Holland, S. K., Plante, E., Byars, A. W., Strawsburg, R. H., Schmithorst, V. J., and Ball,W. S. Jr. (2001). Normal fMRI brain activation patterns

in children performing a verb generation task. NeuroImage. 14, 837–843. doi: 10.1006/nimg.2001.0875

Holz, E. M., Höhne, J., and Staiger-Sälzer, P. (2013). Brain–computer interface controlled gaming: evaluation of usability by severely motor restricted endusers. Art. Intell. Med. 59, 111–120. doi: 10.1016/j.artmed.2013.08.001

Hong, B., Guo, F., Liu, T., Gao, X., and Gao, S. (2009). N200-speller using motion-onset visual response. Clin. Neurophysiol. 120, 1658–1666. doi: 10.1016/j.clinph.2009.06.026

Hosni, S. M., Shedeed, H. A., Mabrouk, M. S., and Tolba, M. F. (2019). EEG-EOG based virtual keyboard: toward hybrid brain computer interface. Neuroinformatics 17, 323–341. doi: 10.1007/s12021-018-9402-0

Howick, J., Chalmers, I., Library, J. L., Glasziou, P., Greenhalgh, T., Heneghan, C., et al. (2011). Oxford Centre for Evidence-Based Medicine Levels of Evidence. Available online at: http://www.cebm.net/index.aspx?o=5653

Huang, H., Xie, Q., Pan, J., He, Y., Wen, Z., Yu, R., et al. (2019). An EEGbased brain computer interface for emotion recognition and its application in patients with disorder of consciousness. IEEE Trans. Aﬀect. Comput. 1. doi: 10.1109/TAFFC.2019.2901456

Huggins, J. E., Guger, C., Allison, B., Anderson, C. W., Batista, A., Brouwer, A.-M., et al. (2014). Workshops of the ﬁfth international brain-computer interface meeting: deﬁning the future. Brain Computer Interfaces 1, 27–49. doi: 10.1080/2326263X.2013.876724

Huggins, J. E., Wren, P. A., and Gruis, K. L. (2011). What would brain-computer interface users want? Opinions and priorities of potential users with amyotrophic lateral sclerosis. Amyotroph. Lateral Scler. 12, 318–324. doi: 10.3109/17482968.2011.5 72978

Jeunet, C., Jahanpour, E., and Lotte, F. (2016). Why standard brain-computer interface (BCI) training protocols should be changed: an experimental study. J. Neural Eng. 13:036024. doi: 10.1088/1741-2560/13/3/036024

Jochumsen, M., Shaﬁque, M., Hassan, A., and Niazi, I. K. (2018). Movement intention detection in adolescents with cerebral palsy from single-trial EEG. J. Neural Eng. 15:066030. doi: 10.1088/1741-2552/aae4b8

Johnston, M. V. (2009). Plasticity in the developing brain: implications for rehabilitation. Dev. Disabil. Res. Rev. 15, 94–101. doi: 10.1002/ddrr.64

Kim, E. Y., Iwaki, N., Imashioya, H., Uno, H., and Fujita, T. (2007). Error-related negativity in a visual go/no-go task: children vs. adults. Dev. Neuropsychol. 31, 181–191. doi: 10.1080/87565640701190775

Kinney-Lang, E., Kelly, D., Floreani, E. D., Jadavji, Z., Rowley, D., Zewdie, et al. (2020). Advancing brain-computer interface applications for severely disabled children through a multidisciplinary national network: summary of the inaugural pediatric BCI Canada Meeting. Front. Hum. Neurosci. 14:593883. doi: 10.3389/fnhum.2020.593883

Kmet, L. M., Lee, R. C., and Cook, L. S. (2004). Standard Quality Assessment Criteria for Evaluating Primary Research Papers From a Variety of Fields. Edmonton, AB: Alberta Heritage Foundation for Medical Research (AHFMR). AHFMR - HTA Initiative #13. 2004.

Kolev, V., and Yordanova, J. (1997). Analysis of phase-locking is informative for studying event-related EEG activity. Biol. Cybern., 76, 229–235. doi: 10.1007/s004220050335

Krusienski, D. J., and Shih, J. J. (2011). Control of a visual keyboard using an electrocorticographic brain–computer interface. Neurorehabil. Neural. Repair. 25, 323–331. doi: 10.1177/1545968310382425

Kübler, A., and Botrel, L. (2019). “The making of brain painting-from the idea to daily life use by people in the locked-in state,” in Brain Art (Cham: Springer), 409–431.

Kübler, A., Holz, E., Kaufmann, T., and Zickler, C. (2013). A user centred approach for bringing BCI controlled applications to end-users. Brain Computer Interface Systems Recent Progress Future Prospects 19, 1–20. doi: 10.5772/55802

Kulseng, S., Jennekens-Schinkel, A., Naess, P., Romundstad, P., Indredavik, M., Vik, T., et al. (2007). Very-low-birthweight and term small-forgestational-age adolescents: attention revisited. Acta Paediatrica 95, 224–230. doi: 10.1111/j.1651-2227.2006.tb02211.x

Kushki, A., Andrews, A. J., Power, S. D., King, G., and Chau, T. (2012). Classiﬁcation of activity engagement in individuals with severe physical disabilities using signals of the peripheral nervous system. PLoS ONE 7:e30373. doi: 10.1371/journal.pone.0030373

Lang, M. (2012). Investigating the Emotiv EPOC for Cognitive Control in Limited Training Time. University of Canterbury. Available online at: https://www.cosc. canterbury.ac.nz/research/reports/HonsReps/2012/hons_1201.pdf

Lech, M., Kucewicz, M. T., and Czyzewski, A. (2019). Human computer interface for tracking eye movements improves assessment and diagnosis of patients with acquired brain injuries. Front. Neurol. 10:6. doi: 10.3389/fneur.2019. 00006

Lee, L., Packer, T. L., Tang, S. H., and Girdler, S. (2008). Self-management education programs for age-related macular degeneration: a systematic review. Austral. J. Educ. Technol. 27, 170–176. doi: 10.1111/j.1741-6612.2008. 00298.x

Leuthardt, E. C., Schalk, G., Wolpaw, J. R., Ojemann, J. G., and Moran, D. W. (2004). A brain–computer interface using electrocorticographic signals in humans. J. Neural Eng. 1:63. doi: 10.1088/1741-2560/1/2/001

Lim, C. G., Lee, T. S., Guan, C., Fung, D. S. S., Zhao, Y., Teng, S. S. W., et al. (2012). A brain-computer interface based attention training program for treating attention deﬁcit hyperactivity disorder. PLoS ONE 7:e46692. doi: 10.1371/journal.pone.0046692

Lin, Z., Zhang, C., Wu, W., and Gao, X. (2006). Frequency recognition based on canonical correlation analysis for SSVEP-based BCIs. IEEE Trans. Biomed. Eng., 53, 2610–2614. doi: 10.1109/TBME.2006.886577

Lust, J. M., Wilson, P. H., and Steenbergen, B. (2016). Motor imagery diﬃculties in children with Cerebral Palsy: a speciﬁc or general deﬁcit?. Res. Dev. Disabil. 57, 102–111. doi: 10.1016/j.ridd.2016.06.010

Manning, C., Wagenmakers, E. J., Norcia, A. M., Scerif, G., and Boehm, U. (2021). Perceptual decision-making in children: age-related diﬀerences and EEG correlates. Comput. Brain Behav. 4, 53–69. doi: 10.1007/s42113-020-00087-7 McFarland, D. J., and Wolpaw, J. R. (2008). Brain-computer interface operation of

robotic and prosthetic devices. Computer 41, 52–56. doi: 10.1109/MC.2008.409

Mikołajewska, E., and Mikołajewski, D. (2014). The prospects of braincomputer interface applications in children. Cent. Eur. J. Med. 9, 74–79. doi: 10.2478/s11536-013-0249-3

Milekovic, T., Fischer, J., Pistohl, T., Ruescher, J., Schulze-Bonhage, A., Aertsen, A., et al. (2012). An online brain-machine interface using decoding of movement direction from the human electrocorticogram. J. Neur. Eng. 9:046003. doi: 10.1088/1741-2560/9/4/046003

Milsap, G., Collard, M., Coogan, C., and Crone, N. E. (2019). BCI2000Web and WebFM: browser-based tools for brain computer interfaces and functional brain mapping. Front Neurosci. 12:1030. doi: 10.3389/fnins.2018.01030

Moghimi, S., Kushki, A., Marie Guerguerian, A., and Chau, T. (2013). A review of EEG-based brain-computer interfaces as access pathways for individuals with severe disabilities. Assist. Technol. 25, 99–110. doi: 10.1080/10400435.2012.723298

Moher, D., Liberati, A., Tetzlaﬀ, J., Altman, D. G., and The PRISMA Group (2009). Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. PLoS Med. 6:e1000097. doi: 10.1371/journal.pmed.1000097

Mouˇcek, R., Vaˇreka, L., Prokop, T., Štˇebeták, J., and B˚ruha, P. (2019). Replication Data for: Evaluation of Convolutional Neural Networks Using a Large MultiSubject P300 Dataset, Harvard Dataverse, V1. doi: 10.7910/DVN/G9RRLN

Mugler, E. M., Ruf, C. A., Halder, S., Bensch, M., and Kübler, A. (2010). Design and implementation of a P300-based brain-computer interface for controlling an Internet browser. IEEE Trans. Neural Syst. Rehabilitation Eng. 18, 599–609. doi: 10.1109/TNSRE.2010.2068059

Müller-Putz, G., Scherer, R., Brunner, C., Leeb, R., and Pfurtscheller, G. (2008). Better than random: a closer look on BCI results. Int. J Bioelectromagn. 10, 52–55.

Münßinger, J. I., Halder, S., Kleih, S. C., Furdea, A., Raco, V., Hösle, A., et al. (2010). Brain painting: ﬁrst evaluation of a new brain-computer interface application with ALS-patients and healthy volunteers. Front. Neurosci. 4:182. doi: 10.3389/fnins.2010.00182

- Myrden, A., and Chau, T. (2016). Towards psychologically adaptive brain-computer interfaces. J. Neur. Eng. 13:066022. doi: 10.1088/1741-2560/13/6/066022
- Myrden, A., and Chau, T. (2017). A passive EEG-BCI for single-trial detection of changes in mental state. IEEE Trans. Neural Syst. Rehabil. Eng. 25, 345–356. doi: 10.1109/TNSRE.2016.2641956

Myrden, A., Kushki, A., Sejdi,´c, E., and Chau, T. (2012). Towards increased data transmission rate for a three-class metabolic brain–computer interface based on transcranial Doppler ultrasound. Neurosci Lett. 528, 99–103. doi: 10.1016/j.neulet.2012.09.030

Myrden, A., Schudlo, L., Weyand, S., Zeyl, T., and Chau, T. (2014). Trends in communicative access solutions for children with cerebral palsy. J. Child. Neurol. 29, 1108–1118. doi: 10.1177/0883073814534320

Myrden, A. J., Kushki, A., Sejdi,´c, E., Guerguerian, A. M., and Chau, T. (2011). A brain-computer interface based on bilateral transcranial Doppler Ultrasound. PLoS ONE 6:e0024170. doi: 10.1371/journal.pone.0024170

Nichols, T. E., and Holmes, A. P. (2002). Nonparametric permutation tests for functional neuroimaging: a primer with examples. Hum. Brain Mapp. 15, 1–25. doi: 10.1002/hbm.1058

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., et al. (2008). A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916. doi: 10.1016/j.clinph.2008.03.034

Norton, J. J., Mullins, J., Alitz, B. E., and Bretl, T. (2018). The performance of 9–11year-old children using an SSVEP-based BCI for target selection. J. Neur. Eng. 15:056012. doi: 10.1088/1741-2552/aacfdd

Obermaier, B., Müller, G. R., and Pfurtscheller, G. (2003). “Virtual Keyboard” controlled by spontaneous EEG activity. IEEE Trans. Neural Syst. Rehabilitation Eng., 11, 422–426. doi: 10.1109/TNSRE.2003.816866

Oken, B., Memmott, T., Eddy, B., Wiedrick, J., and Fried-Oken, M. (2018). Vigilance state ﬂuctuations and performance using brain–computer interface for communication. Brain Comput. Interfaces 5, 146–156. doi: 10.1080/2326263X.2019.1571356

Oken, B. S., Orhan, U., Roark, B., Erdogmus, D., Fowler, A., Mooney, A., et al. (2014). Brain-computer interface with language modelelectroencephalography fusion for Locked-in Syndrome. Neurorehabil. Neural. Repair. 28, 387–394. doi: 10.1177/1545968313516867

Pangelinan, M. M., Kagerer, F. A., Momen, B., Hatﬁeld, B. D., and Clark, J. E. (2011). Electrocortical dynamics reﬂect age-related diﬀerences in movement kinematics among children and adults. Cereb. Cortex. 21, 737–747. doi: 10.1093/cercor/bhq162

Pannek, K., Boyd, R. N., Fiori, S., Guzzetta, A., and Rose, S. E. (2014). Assessment of the structural brain network reveals altered connectivity in children with unilateral cerebral palsy due to periventricular white matter lesions. NeuroImage Clin. 5, 84–92. doi: 10.1016/j.nicl.2014.05.018

Papadelis, C., Butler, E. E., Rubenstein, M., Sun, L., Zollei, L., Nimec, D., et al. (2018). Reorganization of the somatosensory cortex in hemiplegic cerebral palsy associated with impaired sensory tracts. NeuroImage Clin. 17, 198–212. doi: 10.1016/j.nicl.2017.10.021

Papatheodorou, N., Pino, A., Kouroupetroglou, G. T., Constantinides, V., Andreadou, E., and Papageorgiou, C. C. (2019). Upper limb motor skills performance evaluation based on point-and-click cursor trajectory analysis: application in early multiple sclerosis detection. IEEE Access. 7, 28999–29013. doi: 10.1109/ACCESS.2019.2901926

Park, K., Kihl, T., Park, S., Kim, M. J., and Chang, J. (2019). Fairy tale directed game-based training system for children with ADHD using BCI and motion sensing technologies. Behav. Inf. Technol. 38, 564–577. doi: 10.1080/0144929X.2018.1544276

Perego, P., Turconi, A. C., Andreoni, G., Maggi, L., Beretta, E., Parini, S., et al. (2011). Cognitive ability assessment by brain-computer interface: validation of a new assessment method for cognitive abilities. J. Neurosci. Methods 201, 239–250. doi: 10.1016/j.jneumeth.2011.06.025

Pfurtscheller, G., Allison, B. Z., Brunner, C., Bauernfeind, G., Solis-Escalante, T., Scherer, R., et al. (2010). The hybrid BCI. Front. Neurosci. 4:3. doi: 10.3389/fnpro.2010.00003

Pichiorri, F., and Mattia, D. (2020). “Brain-computer interfaces in neurologic rehabilitation practice,” in Handbook of Clinical Neurology, eds N. F. Ramsey and J. del R. Millán (Elsevier B.V.), 168, 101–116.

Pires, G., Nunes, U., and Castelo-Branco, M. (2011). Statistical spatial ﬁltering for a P300-based BCI: tests in able-bodied, and patients with cerebral palsy and amyotrophic lateral sclerosis. J. Neurosci. Methods 195, 270–281. doi: 10.1016/j.jneumeth.2010.11.016

Pistohl, T., Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2008). Prediction of arm movement trajectories from ECoG-recordings in humans. J. Neurosci. Methods 167, 105–114. doi: 10.1016/j.jneumeth.2007.10.001

Pistohl, T., Schmidt, T. S. B., Ball, T., Schulze-Bonhage, A., Aertsen, A., and Mehring, C. (2013). Grasp detection from human ECoG during natural reach-to-grasp movements. PLoS ONE 8:e54658. doi: 10.1371/journal.pone.00 54658

Pistohl, T., Schulze-Bonhage, A., Aertsen, A., Mehring, C., and Ball, T. (2012). Decoding natural grasp types from human ECoG. NeuroImage 59, 248–260. doi: 10.1016/j.neuroimage.2011.06.084

Proulx, N., Samadani, A.-A., and Chau, T. (2018). Online classiﬁcation of the nearinfrared spectroscopy fast optical signal for brain-computer interfaces. Biomed. Phys. Eng. Expres 4:065010. doi: 10.1088/2057-1976/aada1a

Punsawad, Y., and Wongsawat, Y. (2013). “Hybrid SSVEP-motion visual stimulus based BCI system for intelligent wheelchair,” in 2013 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 7416–7419. doi: 10.1109/EMBC.2013.6611272

Rejer, I. (2012). EEG feature selection for BCI based on motor imaginary task. Found. Comput. Decis. Sci. 37, 283–292. doi: 10.2478/v10209-011-0016-7

Rohani, D. A., Sorensen, H. B. D., and Puthusserypady, S. (2014). “Brain-computer interface using P300 and virtual reality: a gaming approach for treating ADHD,” in 2014 36th Annual International Conference of the (IEEE) Engineering in Medicine and Biology Society. doi: 10.1109/EMBC.2014.6944403

Roland, J., Miller, K., Freudenburg, Z., Sharma, M., Smyth, M., Gaona, C., et al. (2011). The eﬀect of age on human motor electrocorticographic signals and implications for brain-computer interface applications. J. Neur. Eng. 8:46013. doi: 10.1088/1741-2560/8/4/046013

Rupp, R., Kleih, S. C., Leeb, R., Millan, J. D. R., Kübler, A., and Müller-Putz, G. R. (2014). “Brain-computer interfaces and assistive technology,” in BrainComputer-Interfaces in Their Ethical, Social and Cultural Contexts (Dordrecht: Springer), 7–38. doi: 10.1007/978-94-017-8996-7_2

Sanchez, J. C., Gunduz, A., Carney, P. R., and Principe, J. C. (2008). Extraction and localization of mesoscopic motor control signals for human ECoG neuroprosthetics. J. Neurosci. Methods 167, 63–81. doi: 10.1016/j.jneumeth.2007.04.019

Sanders, L. D., and Zobel, B. H. (2012). Nonverbal spatially selective attention in 4- and 5-year-old children. Dev. Cogn. Neurosci. 2, 317–328. doi: 10.1016/j.dcn.2012.03.004

Santesso, D. L., Segalowitz, S. J., and Schmidt, L. A. (2006). Error-related electrocortical responses in 10-year-old children and young adults. Dev. Sci. 9, 473–481. doi: 10.1111/j.1467-7687.2006.00514.x

Sawyer, S. M., Azzopardi, P. S., Wickremarathne, D., and Patton, G. C.

(2018). The age of adolescence. Lancet Child Adolesc. Health. 2, 223–228. doi: 10.1016/S2352-4642(18)30022-1

Schalk, G., Miller, K. J., Anderson, N. R., Wilson, J. A., Smyth, M. D., and Ojemann, J. G., et al. (2008). Two-dimensional movement control using electrocorticographic signals in humans. J. Neur. Eng. 5:75. doi: 10.1088/1741-2560/5/1/008

Scherer, R., Faller, J., Balderas, D., Friedrich, E. V., Pröll, M., Allison, B., et al.

(2013). Brain–computer interfacing: more than the sum of its parts. Soft comput. 17, 317–331. doi: 10.1007/s00500-012-0895-4

Schudlo, L. C., and Chau, T. (2018). Development and testing an online nearinfrared spectroscopy brain-computer interface tailored to an individual with severe congenital motor impairments. Disabil. Rehabil. Assist. Technol. 13, 581–591. doi: 10.1080/17483107.2017.1357212

Sellers, E. W., Ryan, D. B., and Hauser, C. K. (2014). Noninvasive brain-computer interface enables communication after brainstem stroke. Sci. Transl. Med. 6:257re7. doi: 10.1126/scitranslmed.3007801

Sellers, E. W., Turner, P., Sarnacki, W. A., McManus, T., Vaughan, T. M., and Matthews, R. (2009). “A novel dry electrode for brain-computer interface,” in International Conference on Human-Computer Interaction (Berlin: Springer), 623–631.

Sereshkeh, A. R., Youseﬁ, R., Wong, A. T., and Chau, T. (2018). Online classiﬁcation of imagined speech using functional near-infrared spectroscopy signals. J. Neur. Eng. 16:016005. doi: 10.1088/1741-2552/ aae4b9

Sereshkeh, A. R., Youseﬁ, R., Wong, A. T., Rudzicz, F., and Chau, T. (2019). Development of a ternary hybrid fNIRS-EEG brain-computer

interface based on imagined speech. Brain Computer Interfaces 6, 128–140. doi: 10.1080/2326263X.2019.1698928

Sigurdardottir, S., Indredavik, M. S., Eiriksdottir, A., Einarsdottir, K., Gudmundsson, H. S., and Vik, T. (2010). Behavioural and emotional symptoms of preschool children with cerebral palsy: a population-based study. Dev. Med. Child Neurol. 52, 1056–1061. doi: 10.1111/j.1469-8749.2010.03698.x

Simeral, J. D., Kim, S.-P., Black, M. J., Donoghue, J. P., and Hochberg, L. R. (2011). Neural control of cursor trajectory and click by a human with tetraplegia 1000 days after implant of an intracortical microelectrode array. J. Neur. Eng. 8:025027. doi: 10.1088/1741-2560/8/2/025027

Slater, J. D., Kalamangalam, G. P., and Hope, O. (2012). Quality assessment of electroencephalography obtained from a “dry electrode” system. J. Neurosci. Methods 208, 134–137. doi: 10.1016/j.jneumeth.2012.05.011

Taherian, S., Selitskiy, D., Pau, J., and Claire Davies, T. (2017). Are we there yet? Evaluating commercial grade brain–computer interface for control of computer applications by individuals with cerebral palsy. Disabil. Rehabil. Assist. Technol. 12, 165–174. doi: 10.3109/17483107.2015.1111943

Taherian, S., Selitskiy, D., Pau, J., Davies, T. C., and Owens, R. G. (2016). Training to use a commercial brain-computer interface as access technology: a case study. Disabil. Rehabil. Assist. Technol. 11, 345–350. doi: 10.3109/17483107.2014.967313

Thompson, D. E., Blain-Moraes, S., and Huggins, J. E. (2013). Performance assessment in brain-computer interface-based augmentative and alternative communication. Bio. Med. Eng. 12:43. doi: 10.1186/1475-925X-12-43

Thompson, D. E., Gruis, K. L., and Huggins, J. E. (2014b). A plug-and-play braincomputer interface to operate commercial assistive technology. Disabil. Rehabil. Assist. Technol. 9, 144–150. doi: 10.3109/17483107.2013.785036

Thompson, D. E., Quitadamo, L. R., Mainardi, L., Laghari, K., Gao, S., Kindermans, P. J., et al. (2014a). Performance measurement for braincomputer or brain–machine interfaces: a tutorial. J. Neural. Eng. 11:35001. doi: 10.1088/1741-2560/11/3/035001

Torpey, D. C., Hajcak, G., and Klein, D. N. (2009). An examination of errorrelated brain activity and its modulation by error value in young children. Dev. Neuropsychol. 34, 749–761. doi: 10.1080/87565640903265103

Treder, M. S., Schmidt, N. M., and Blankertz, B. (2011). Gaze-independent braincomputer interfaces based on covert attention and feature attention. J. Neural. Eng. 8:066003. doi: 10.1088/1741-2560/8/6/066003

Van de Laar, B., Gürkök, H., Plass-Oude Bos, D., Poel, M., and Nijholt, A. (2013). Experiencing BCI control in a popular computer game. IEEE Trans. Comput. Intell. AI Games 5, 176–184. doi: 10.1109/TCIAIG.2013.2253778

Vaˇreka, L. (2020). Evaluation of convolutional neural networks using a large multi-subject P300 dataset. Biomed. Signal Process Control. 58:101837. doi: 10.1016/j.bspc.2019.101837

Vilela, M., and Hochberg, L. R. (2020). Applications of brain-computer interfaces to the control of robotic and prosthetic arms. Handb. Clin. Neurol. 168, 87–99. doi: 10.1016/B978-0-444-63934-9.00008-1

Viswanathan, M., Patnode, M. P. H., Berkman, N. D., Bass, E. B., Chang, S., Hartling, L., et al. (2017). “Assessing the risk of bias of individual studies in systematic reviews of health care interventions,” in Methods Guide for Eﬀectiveness and Comparative Eﬀectiveness Reviews. Agency for Healthcare Research and Quality (US). Available online at: https://www.ncbi.nlm.nih.gov/ sites/books/NBK519366/

Volosyak, I., Gembler, F., and Stawicki, P. (2017). Age-related diﬀerences in SSVEP-based BCI performance. Neurocomputing 250, 57–64. doi: 10.1016/j.neucom.2016.08.121

Weyand, S., and Chau, T. (2015). Correlates of near-infrared spectroscopy braincomputer interface accuracy in a multi-class personalization framework. Front. Hum. Neurosci. 9:536. doi: 10.3389/fnhum.2015.00536

Weyand, S., and Chau, T. (2017). Challenges of implementing a personalized mental task near-infrared spectroscopy brain–computer interface for a nonverbal young adult with motor impairments. Dev. Neurorehabilit. 20, 99–107. doi: 10.3109/17518423.2015.1087436

Weyand, S., Takehara-Nishiuchi, K., and Chau, T. (2015). Exploring methodological frameworks for a mental task-based near-infrared spectroscopy brain–computer interface. J. Neurosci. Methods 254, 36–45. doi: 10.1016/j.jneumeth.2015.07.007

Wiersema, J. R., van der Meere, J. J., and Roeyers, H. (2007). Developmental changes in error monitoring: an event-related potential study. Neuropsychologia 45, 1649–1657. doi: 10.1016/j.neuropsychologia.2007.01.004

Wirth, C., Toth, J., and Arvaneh, M. (2020). “You have reached your destination”: a single trial EEG classiﬁcation study. Front. Neurosci. 14:66. doi: 10.3389/fnins.2020.00066

Wisneski, K. J., Anderson, N., Schalk, G., Smyth, M., Moran, D., and Leuthardt, E. C. (2008). Unique cortical physiology associated with ipsilateral hand movements and neuroprosthetic implications. Stroke 39, 3351–3359. doi: 10.1161/STROKEAHA.108.518175

Wolpaw, J. R., Birbaumer, N., Heetderks, W. J., McFarland, D. J., Peckham, P. H., Schalk, G., et al. (2000). Brain-computer interface technology: a review of the ﬁrst international meeting. IEEE Trans. Rehab. Eng. 8, 164–173. doi: 10.1109/TRE.2000.847807

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain–computer interfaces for communication and control. Clin. Neurophysiol., 113, 767–791. doi: 10.1016/S1388-2457(02) 00057-3

Wolpaw, J. R., and Wolpaw, E. W. (2012). Brain-computer Interfaces: Principles and Practice. New York, NY: Oxford University Press.

World Health Organization (WHO) (2020). Policy Brief: Access to Assistive Technology. Available online at: https://apps.who.int/iris/handle/10665/332222. License: CC BY-NC-SA 3.0 IGO

Yu, Y., Zhou, Z., Liu, Y., Jiang, J., Yin, E., Zhang, N., et al. (2017). Selfpaced operation of a wheelchair based on a hybrid brain-computer interface combining motor imagery and P300 potential. IEEE Trans. Neural Syst. Rehabil. Eng. 25, 2516–2526. doi: 10.1109/TNSRE.2017.2766365

Zephaniah, P. V., and Kim, J. G. (2014). Recent functional near infrared spectroscopy based brain computer interface systems: developments, applications and challenges. Biomed. Eng. Lett. 4, 223–230. doi: 10.1007/s13534-014-0156-9

Zhang, D., Song, H., Xu, R., Zhou, W., Ling, Z., and Hong, B. (2013). Toward a minimally invasive brain–computer interface using a single subdural channel: a visual speller study. NeuroImage 71, 30–41. doi: 10.1016/j.neuroimage.2012.12.069

Zhang, J. Z., Jadavji, Z., Zewdie, E., and Kirton, A. (2019). Evaluating if children can use simple brain computer interfaces. Front. Hum. Neurosci. 13:24. doi: 10.3389/fnhum.2019.00024

Zickler, C., Halder, S., Kleih, S. C., Herbert, C., and Kübler, A. (2013). Brain painting: usability testing according to the user-centered design in end users with severe motor paralysis. Artif. Intell. Med. 59, 99–110. doi: 10.1016/j.artmed.2013.08.003

Zickler, C., Riccio, A., Leotta, F., Hillian-Tress, S., Halder, S., Holz, E., et al. (2011). A brain-Computer interface as input channel for a standard assistive technology software. Clin. EEG Neurosci. 42, 236–244. doi: 10.1177/155005941104200409

Conﬂict of Interest: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2021 Orlandi, House, Karlsson, Saab and Chau. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

