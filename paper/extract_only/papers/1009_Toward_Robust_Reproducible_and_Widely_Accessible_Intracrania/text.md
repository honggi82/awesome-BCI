# arXiv:2603.12279v2[q-bio.NC]16Mar2026

TOWARD ROBUST, REPRODUCIBLE, AND WIDELY ACCESSIBLE INTRACRANIAL LANGUAGE BRAIN-COMPUTER INTERFACES: A COMPREHENSIVE REVIEW OF NEURAL MECHANISMS, HARDWARE, ALGORITHMS, EVALUATION, CLINICAL PATHWAYS AND FUTURE DIRECTIONS

Dongyi He1,2, Wai Ting Siok1,*, and Nizhuan Wang1,* 1Department of Language Science and Technology, The Hong Kong Polytechnic University, Hung Hom, Hong Kong SAR, China 2School of Artificial Intelligence, Chongqing University of Technology, Chongqing 401135, China *Correspondence: wai-ting.siok@polyu.edu.hk (W.T.S.); wangnizhuan1120@gmail.com (N.W.)

## ABSTRACT

Intracranial language brain-computer interfaces (BCIs) offer a promising route for restoring communication in individuals with severe motor and speech impairments, but clinical translation remains limited by fragmented and heterogeneous evidence, as well as unresolved design trade-offs across neuroscience, hardware, algorithms, validation methods, and clinical integration. This review synthesizes recent progress across four key domains in intracranial speech neuroprosthetics: i) the neural mechanisms underlying overt, mimed, and imagined speech; ii) decision-oriented hardware comparisons of surgically implanted recording modalities, including microelectrode array (MEA), electrocorticography (ECoG), and stereotactic electroencephalography (SEEG); iii) experimental strategies for achieving cross-subject and multilingual generalization; and iv) advances in neural decoding, including sequence models, attention-based architectures (e.g., transformers), articulatory intermediate representations, and language-prior-assisted frameworks. We highlight persistent bottlenecks, including weak cross-subject transfer, long-term non-stationarity and recalibration burden, heterogeneous and non-comparable evaluation practices, limited naturalistic expressivity (especially for tonal/logosyllabic languages), and the low signal-to-noise ratio (SNR) of neural activity in covert speech decoding. Our contributions are threefold: (1) an end-to-end, decision-oriented synthesis that links neural representations to recording choices, experimental design, decoding model architectures, and translational constraints; (2) a structured framework organized around five coupled design questions, accompanied by a unified evaluation framework and a cross-linguistic, cross-task benchmark template that integrates objective, perceptual, expressive, conversational, and longitudinal metrics; and (3) user-centered translational guidance that includes agency-preserving shared control, verifiable performance priorities, and scenario-specific minimum viable system (MVP) profiles for differentiating between reliability-first home communication and fidelity-first conversational speech restoration. We conclude with a call for larger multilingual, multi-center longitudinal datasets; harmonized benchmarks; adaptive yet interpretable decoders; prospective clinical validation; and transparent data-sharing and reporting practices with robust ethical safeguards. These efforts are essential to accelerate the safe and equitable deployment of speech neuroprostheses.

Keywords Language Brain-computer Interface (BCI) · Intracranial Recording · Hardware and Software Protocols · Neural Mechanism · Articulatory Representations · Neural Decoding · Cross-Subject Generalization · Clinical Translation

## 1 Introduction

Speech is the most natural and efficient channel for human communication, yet it is among the first abilities compromised in a range of devastating neurological conditions [1, 2, 3]. Individuals with locked-in syndrome (LIS), advanced amyotrophic lateral sclerosis (ALS), brainstem stroke, or severe paralysis may remain cognitively intact while unable to produce intelligible speech or purposeful movement [4, 5, 3, 6]. For these patients, language BCIs, systems that decode intended linguistic content (and ideally expressive prosody) directly from neural activity, offer a pathway to restore communication with greater speed, privacy, and user agency than conventional assistive technologies [1, 7, 8, 9, 10].

Over the past decade, intracranial neural recordings have catalyzed rapid progress in language BCI research. Compared with non-invasive modalities [11, 12, 13, 14, 15, 16], intracranial approaches provide higher SNR and access to highfrequency activity that tightly tracks local cortical computations [17, 18], enabling decoding at the levels of phonemes, words, and continuous speech [19, 20, 1]. In parallel, the field has shifted from proof-of-concept demonstrations toward system-level designs that must operate reliably in real-world settings: across days and months, across electrode configurations, across languages and speaking styles, and across the spectrum from overt to silently mouthed or imagined speech [21, 22]. As summarized in the lane-based timeline in Fig. 1, this evolution represents not only a chronology of decoder improvements but a broader shift toward chronic, online systems and frameworks that explicitly address cross-subject transfer, electrode heterogeneity, and deployment constraints. These requirements are more demanding than those of laboratory demonstrations and necessitate the tight integration of neuroscience, hardware, machine learning, evaluation methodology, and clinical translation.

At the mechanistic level, speech production and perception recruit distributed cortical and subcortical circuits, spanning ventral sensorimotor cortex, premotor and supplementary motor regions, inferior frontal and temporal language areas, and higher-order association networks. Intracranial recordings have revealed rich articulatory representations and population dynamics that support rapid sequencing, coarticulation, and context-dependent planning, and have clarified how neural signatures differ across overt, mimed (silent articulation), and imagined speech [8, 23, 24, 25, 26, 27]. For language BCIs, these observations motivate the choice of decoding targets (e.g., acoustics, phonemes, articulatory features, or semantic units), the selection of temporal context, and the design of intermediate representations that may improve robustness and interpretability [28, 29, 30, 31].

On the technology side, intracranial language BCIs sit at the intersection of multiple recording modalities, each with fundamentally different trade-offs. Intracortical MEAs can capture high-dimensional spiking activity with fine spatial granularity but typically cover limited cortical territory and face chronic stability challenges [1, 10]. ECoG grids and depth electrodes such as SEEG offer broader coverage and clinically established implantation pathways, yet they sample neural activity at different spatial scales and with different noise characteristics [19, 20, 32]. The “best” modality therefore depends on the intended use case (research vs. home use), surgical feasibility, target neural features, and acceptable calibration burden. Experiment design is another critical consideration. The field has evolved from small, single-subject datasets with limited linguistic diversity toward larger, multi-subject datasets that enable cross-subject learning and benchmarking. However, challenges remain in standardizing data collection protocols, ensuring multilingual coverage, and producing rich annotations that capture not only lexical content but also prosody, emphasis, and affective features [33, 34, 35, 36, 37, 38].

Algorithmically, language BCIs have evolved from feature-engineered pipelines and frame-wise classifiers to Seq2Seq models that jointly learn neural feature extraction, alignment, and decoding [9]. Advances such as transformers, convolutional temporal models, and hybrid architectures have enabled larger vocabularies, streaming or online decoding, and improved utilization of long-range context. Additionally, biologically grounded articulatory intermediates provide structural constraints that enhance data efficiency and generalization [32, 39]. More recently, language models and other linguistic priors have been integrated to reduce error rates and increase output coherence, raising new questions about controllability, bias, latency, and attribution of “who said what” in shared-control system [1, 10]. These trends underscore the importance of evaluating models not only in terms of accuracy but also considering calibration requirements, real-time constraints, robustness to neural non-stationarity, and interpretability.

Despite these advances, several core bottlenecks continue to hinder clinical translation of intracranial language BCIs. First, poor cross-subject generalization persists: many decoders remain subject-specific, do not transfer across electrode layouts, and cannot fully leverage data across participants or centers [32, 39, 9]. Second, long-term stability of both neural signals and end-to-end performance remains a central challenge, with MEAs often requiring frequent recalibration and ECoG/SEEG systems still necessitating rigorous chronic validation under naturalistic use [21, 20, 19, 22, 10]. Third, evaluation practices remain heterogeneous: inconsistent use of word error rate (WER), phoneme error rate (PER), latency, information-transfer measures, and human perceptual scoring makes cross-task comparisons difficult and can obscure clinically meaningful differences [40, 41, 42, 43]. Fourth, limited naturalistic expressivity restricts many systems to lexical content, while paralinguistic features such as prosody, intonation, emphasis, and affect are less

consistently modeled. This challenge is amplified for tonal languages (e.g., Mandarin, Cantonese) where pitch contours and syllable structure are integral to lexical meaning [28, 34, 35, 36, 37, 38, 44, 45]. Finally, covert speech decoding (silent articulation or imagined speech) poses unique difficulties, as neural signals are typically weaker, more variable, and less time-locked to measurable acoustic ground truth [46, 47].

Despite significant recent progress, the field of intracranial language BCI remains highly fragmented across neuroscience, hardware development, algorithmic design, evaluation methods, and clinical translation. This fragmentation makes it difficult to compare studies, identify clinically meaningful trade-offs, and derive actionable design principles. In particular, progress towards clinical translation is hindered by several unresolved challenges, such as poor cross-subject generalization, limited evidence of long-term stability, heterogeneous evaluation metrics, and insufficient consideration of naturalistic expressivity and covert speech. To address this gap, this review makes three core contributions. First, we provide an end-to-end, decision-oriented synthesis that links neural mechanisms, recording methodologies, experiment design, decoding models, evaluation strategies, and translational deployment into a cohesive framework. Fig. 2 previews this end-to-end pipeline, tracing the path from neural recordings (e.g., ECoG, EEG, MEA) through feature extraction and neural decoding to outputs including phonemes, text, speech features, and synthesized speech, while making explicit how hardware and software choices jointly shape each stage. Second, we organize the field around five interconnected design questions that span the entire BCI development pathway: (i) What neural representations best capture speech intention across overt, mimed, and imagined speech? (ii) Where and how should neural activity be recorded to balance coverage, resolution, chronic stability, and surgical feasibility? (iii) How should experimental datasets and annotations be designed to enable cross-subject generalization, multilingual applicability, and reproducible benchmarking? (iv) Which decoding architectures and intermediate representations best trade off accuracy, latency, robustness, and interpretability? and (v) How should systems be evaluated, governed, and translated while preserving user agency, identity, and safety? Third, we synthesize concrete translational guidance, including a unified evaluation framework and practical design priorities for user-centered clinical deployment. Consistent with these contributions, the following sections progress from a foundational framework of neural mechanisms to the trade-offs inherent in recording modalities and experimental design, followed by algorithmic advances, unified evaluation standards, and pathways for translational and ethical development. We then conclude with future directions and a synthesis of key priorities. More importantly, we use this synthesis to call for the field’s next phase: larger multilingual and multi-center datasets; longitudinal and standardized benchmarks; adaptive yet interpretable decoders; and prospective user-centered clinical validation with transparent reporting and data sharing.

## 2 Neural Mechanism Framework for Intracranial Language Decoding

As summarized in Fig. 3, this section links four neural-mechanistic themes to a common mechanism–recording–model– task framework, highlighting how biological constraints shape measurable signals and, in turn, influence choices in decoder architecture.

### 2.1 Somatotopic Organization and Articulatory Kinematics in Sensorimotor Cortex

Within the sensorimotor cortex, the ventral sensorimotor cortex (vSMC) and middle precentral gyrus (midPrCG) exhibit spatially intermixed but somatotopically organized tuning to vocal tract articulators, including the lips, tongue, jaw, and larynx [23, 25, 54]. This intermixing extends to the single-electrode and single-neuron level: in the ventral premotor cortex (Brodmann area 6), even a tiny region of just 3.2 × 3.2mm2 exhibits a dense and overlapping representation of multiple speech articulators. This pattern is not confined to ventral speech areas: even the dorsal ’hand knob’ of the precentral gyrus shows broad tuning across phonemes, with many electrodes modulated for multiple phonemes, further evidence that neural activity related to speech production is spatially intermixed [55]. Similarly, single neurons in the anterior precentral gyrus can be tuned to movements of multiple vocal-tract articulators or even whole-body movements [56, 57], and electrodes in vSMC encode coordinated trajectories involving multiple articulators rather than single articulator movements. Despite this intermixing, population-level somatotopic organization is evident. The vSMC and midPrCG are somatotopically organized along the ventral–dorsal axis, representing different muscle groups that control the speech articulators [8]. This results in an overall dorsoventral arrangement of articulator representations (e.g., lips, jaw, tongue, larynx) on the ventral pre- and post-central gyri. For example, the lips are represented more dorsally, while the tongue is distributed more broadly across ventral areas. These representations cluster into four main groups, corresponding to coronal, labial, dorsal, and vocalic articulatory configurations. The somatotopic organization is further supported by two lines of evidence. First, during passive listening to speech sounds, differential activation occurs in the precentral motor cortex that mirrors the somatotopic representation of the articulators used to produce those phonemes [58]. Second, spatial patterns of gamma band activity over the sensorimotor cortex show distinct organizations for consonants versus vowels, confirming the coordination of distinct articulatory representations [59]. The spatial arrangement of vocal tract articulators shows both somatotopic organization and intermixing, with linear

dictionary;Viterbidecodingofcontinuousphrases ReportedminimumWER25%andPER50%incontinuousspoken∼<

Table1:Comparativesummaryofrepresentativeintracranialspeech-decodingframeworksdiscussedinthisreview.

phrasedecoding(task-dependent)

Team(Year)Method/FrameworkCoreTechniquesRepresentativePerformance

decoding) ECoGphone-levelacousticmodeling+n-gramLM+pronunciation

Herffetal.[47](2015)Brain-to-Text(continuousphrase

Early-stageDecodingandNeuralSpeechSynthesisPipelines

low/high-frequencyneuralfeatures+autoencoderbottleneck DNN-vocoderpipelineimprovedintelligibilityby65%versuslinear∼

spectrogrambaselineindigitrecognitiontasks

(DNN-vocoder) Auditory-cortexdecodingtovocoderparametersusingDNNregression;

comparisonagainstlinearspectrogramreconstruction;

Akbarietal.[48](2019)Auditory-cortexspeechreconstruction

transcriptionratesreportedforclosedword-poolsettings);betterthan

representation Listenertranscriptionshowedusablesynthesizedspeech(e.g.,exact

random-decodingbaselines

articulatory-to-acousticsynthesis;explicitintermediatearticulatory

speechsynthesis ECoG-to-articulatorykinematics(BiLSTM)followedby

(2019) Two-stagearticulatoryacousticneural→

Anumanchipallietal.[28]

transferlearningforlow-datasettings MeanWERaslowas3%onparticipant-specificmedium-vocabulary∼

sentencetasks;transferlearningimprovedlow-dataperformance

translation End-to-endSeq2Seqencoder–decoder(ECoGtext),auxiliarylosses,→

Makinetal.[9](2020)Encoder–decodercorticalactivitytext→

decoding;density/spacingablation Reportedspeech-decodingaccuracyimprovementof35–36%versus∼

model;large-vocabularydecodinganalysis 62wpm;WER9.1%(50-word)and23.8%(125k-word)vocabularies

standardIEEG;performancesaturatednearsub-1.5mmspacing

(task-dependentthresholding)

neuroprosthesis MEArecordings(area6v/44)+RNNphoneme/textdecoder+language

(seq2seq+non-lineardecoders) Intraoperativehigh-densityECoG;SVD-LDA+seq2seqRNNµ

Duraiveletal.[49](2023)High-resolutionECoGspeechdecodingµ

Willettetal.[1](2023)High-performanceintracorticalspeech

High-PerformanceandClinical/Real-TimeNeuroprosthesisSystems

outputs Mediantextrate78wpmwithmedianWER25%;intelligible

personalizedaudioandavatarcontroldemonstrated

alignment-freesilentspeech;LMrescoring;personalizedvoice/avatar

+avatar) High-densityECoG+deepmultimodaldecoding;CTCfor

Metzgeretal.[50](2023)Multimodalneuroprosthesis(text+audio

speech-relatedcontrolcommands;long-horizondeploymentemphasis Medianaccuracy90.59%for3monthswithoutrecalibration∼

(6-commandcontrolparadigm)

withoutrecalibration ChronicECoGspeech-commandBCI;CNN-baseddecodingof

Luoetal.[21](2023)Stablechronicspeech-BCIcontrol

reconstruction Onlineclosed-vocabularywordsynthesiswithreportedhuman

intelligibilityaround80%intestedkeywordsetting

decoding/synthesis;high-gammafeatureextractionandspectral

(ALS) ChronicECoG+multi-stageRNNpipelineforonline

Angricketal.[22](2024)OnlinechronicBCIspeechsynthesis

textdecoding+TTSvoicerestoration;rapidrecalibrationworkflow 99.6%(50-word,day1),90.2%(125k-wordafter1.4htraining),32∼

wpmconversationaluse,sustaineduseover8.4months

neuroprosthesis(ALS) IntracorticalMEA+phonemeprediction(80msstep)+LM-assisted

Cardetal.[10](2024)Rapidlycalibratingspeech

processingontheorderof10ms;expressiveintonation/emphasiscontrol

+real-timevocoder;expressive/prosodiccontroldecoding Real-timepersonalizedspeechsynthesiswithreportedend-to-endneural

synthesis+textdecoding;implicitspeechdetection;80mschunks 90.9wpm(50-wordAACset),47.5wpm(1,024-wordset);median

latency1.12s(speech)/1.01s(text)∼∼

demonstrated

neuroprosthesis 256-channelintracorticalMEA+causalTransformeracousticdecoding

(bimodal) High-densityECoG+RNN-Tstreamingdecoder;simultaneousspeech

Littlejohnetal.[46](2025)Streamingbrain-to-voiceneuroprosthesis

Wairagkaretal.[37](2025)Instantaneousexpressivevoice-synthesis

left/righthemisphereevaluation 48-participantstudy;bestreportedspectrogramcorrelationPCC0.806∼

(ResNet)withstrongcausal/low-densityperformance

ResNet/Swin/LSTMcomparisons;causalandlow-densitysettings;

neuralspeechframework UnifiedECoGdecoder+differentiablespeechsynthesizer;

###### Generalization,Electrode-RobustModeling,andInterpretable/StructuredRepresentations

Chenetal.[32](2024)Deep-learning+differentiablesynthesis

comparableperformanceachievablewithfewelectrodesinsome

reconstruction;electrodecontributionanalysis RNN/Transformersignificantlyoutperformedlinearregression;

participants;stronglocationdependence

deeplearning LinearregressionvsRNNSeq2SeqvsTransformerformel-spectrogram

Wuetal.[51](2024)SEEGspeechdecodingwithadvanced

layouts PCC0.817(88ECoG),0.838(withextraelectrodes),0.798×

(SEEG-only),0.765(unseenparticipants)

MNI/brain-regionpositionalbias;multi-subjecttrainingacrossarbitrary

forECoG/SEEG) Transformerwithelectrode-wisetokens+temporalwindowattention+

Chenetal.[39](2025)SwinTW(topology-agnostictransformer

meanaccuracy87%(4%)withimprovedrobustnessandtransferto∼±

occlusionanalysis Group-deriveddecodersoutperformedsubject-onlymodels;reported

unseenpatients

distributedrecordings Seq2Seq(temporalconv+RNN+linearreadout),populationlatent

manifoldpretraining,sharedrecurrentlayers,regionalelectrode

Singhetal.[52](2025)Cross-subjecttransferlearningvia

multilingualgeneralization;metricsarenotdirectlycomparabletoBCI

disentanglement Reportedstrongcross-speaker/zero-shotvoiceconversionand

WER/PERtasks

(structuredrepresentation) Articulatorykinematicscoding(SPARC),self-supervisedspeech

modeling+acoustic-to-articulatoryinversion+speaker-identity

Choetal.[53](2024)SPARCarticulatorycodingframework

adaptor+TTS(Parler-TTS),fusedviavoicecloning(CosyVoice) With20min/subjectECoG:MOS4.0/5,mel-spectrogram∼∼

correlation0.824,WER18.9%,PER12%∼∼∼

speechreconstruction Dualpath:acousticbiLSTM+HiFi-GANandlinguisticTransformer

Lietal.[36](2025)Acoustic–linguisticdual-pathwayneural

[Figure 1]

- Figure 1: Lane-based timeline of representative intracranial language decoding frameworks (selected representatives from Table 1). The frameworks are grouped into three categories and ordered by publication year. Each card includes the representative studies with a short framework label and technical tags summarizing key methods.

transformations confirming the dominant contributions of articulators like the tongue tip, which is influenced by the tongue blade and dorsum [53], and with somatotopically organized yet spatially intermixed neural representations of orofacial articulatory kinematics observable through muscle activation patterns [60].

Emergent population-level representations and harmonic oscillator dynamics are key features of speech encoding in the sensorimotor cortex. Neural population activity yields low-dimensional kinematic state–space trajectories, with principal components capturing articulatory dynamics. These trajectories exhibit biphasic vowel-consonant oscillatory trajectories consistent with harmonic oscillator dynamics [28]. Individual electrodes in vSMC encode diverse, functionally stereotyped articulatory kinematic trajectories (AKTs). These out-and-back trajectories exhibit damped harmonic oscillator dynamics and correspond to the vocal tract constrictions that define phonemes [29]. Principal component analysis and clustering reveal that the cortical state-space is organized into clusters corresponding to major oral articulators and vowels, with consonants and vowels occupying distinct regions consistent across subjects [30]. This study also revealed harmonic oscillator-like dynamics underlying the temporal progression of articulatory representations. Population-level neural dynamics during speech include a large condition-invariant signal (CIS) at movement initiation, followed by rotatory (oscillatory) dynamics in the neural state during articulation [31]. The Directions Into Velocities of Articulators (DIVA) model identifies harmonic oscillator-like, population-level circuit dynamics emerging from interacting cortical areas during speech motor control [61]. These population-level representations enable high decoding accuracy: using naive Bayes classifiers on 1 s of neural population activity, 33 orofacial movements can be decoded with 92% accuracy, 39 phonemes with 62% accuracy, and 50 words with 94% accuracy [1]. Decoding performance improves with the number of electrodes in a log-linear relationship.

Controversies persist regarding the consistency of somatotopic patterns across individuals. Intracranial studies provide evidence for emergent population-level representations, but there is individual variability in spatial patterns. Speakerdependent variations in sensorimotor cortex responses captured by SEEG are attributed mostly to differences in electrode placement [62], with interindividual variability in neural activations and electrode placement contributing to inconsistencies in spatial activation patterns [63]. Variability is also observed in the extent and consistency of population dynamics and neural modulation between participants, with some showing stronger and more stable modulation than others. Additionally, while population-level articulatory dynamics are consistent across speakers [28], somatotopic articulatory representations in motor cortex are not consistently active or spatially organized during speech perception across individuals [64], and some consistencies in somatotopic tuning across subjects are observed alongside ongoing

[Figure 2]

- Figure 2: Schematic of intracranial language BCI decoding pipeline with hardware-software co-design. Neural activity from ECoG/EEG/MEA recordings is transformed into neural features and decoded into phonemes, text, speech features, or synthesized speech; hardware design largely constrains the performance ceiling, whereas software design determines how closely it is approached.

variability and inconsistencies. The generalizability of multi-subject models is supported by accommodating intersubject variability in electrode placement, though performance variability remains [39]. Variability across individuals in somatotopic patterns and tuning also contributes to controversies regarding the consistency of these representations [65].

To distill the mechanistic implications of evidence from somatotopy and population-level analyses, we summarize our synthesis in the ‘Somatotopy and Population Dynamics” column of Table 2. Specifically, mixed local tuning and low-dimensional trajectories jointly constrain feature design and decoding targets; intermixed-yet-somatotopic encoding coexists with robust CIS/oscillatory motifs, while substantial inter-individual variability persists. This synthesis corresponds to the somatotopy/population-dynamics branch in Fig. 3.

### 2.2 Hierarchical Functional Streams in Speech Processing

Speech processing is widely recognized to involve two hierarchical functional streams: a dorsal form-to-articulation stream and a ventral form-to-meaning stream [66, 67]. The dorsal stream, connecting temporal and frontal regions via the arcuate fasciculus, supports speech production and phonological processing, while the ventral stream, coursing through the extreme capsule fiber system, is responsible for comprehension and semantic processing [68]. This dual-stream architecture is substantiated by lesion studies, where dorsal stream damage leads to motor and phonological

[Figure 3]

- Figure 3: Mechanism–Recording–Model–Task framework for language decoding. Neural speech representations (somatotopy with mixed tuning, dorsal–ventral streams, overt–mimed–imagined SNR gradient, and temporal population dynamics) shape measurable multielectrode signals across distributed regions and frequency bands using ECoG, SEEG and MEAs. Decoders align with these signal properties via multibranch feature extraction, sequence modeling (CTC/RNN/Transformer), intermediate representations (phonemes, pitch, formants), and subject adaptation, enabling tasks from articulation/phoneme/word classification to continuous sentence decoding and speech waveform reconstruction.

deficits, and ventral stream damage results in comprehension and lexical-semantic impairments. Distributed networks for sensorimotor integration, including primary motor/premotor cortices and temporal areas, support dorsal stream form-to-articulation processing, with distinct topographies for local motor potential (LMP) and frequency-based features indicating different neural origins [69].

Intracranial recordings provide evidence for distributed networks encoding phonetic, spectrotemporal, and lexicalsemantic representations [70, 25, 71]. For spectrotemporal processing, the posteromedial Heschl’s gyrus (HG), the presumed core auditory cortex, resolves the temporal envelope of speech stimuli through mechanisms across a wide range of ECoG frequencies. High-frequency event-related band power (ERBP) reflects fine-grained temporal encoding in this region, even under conditions of compromised intelligibility [72]. High gamma power (70–150 Hz) tracking of speech is concentrated in the superior temporal gyrus (STG), while low-frequency phase tracking (1–7 Hz) is more widespread, encompassing the STG, anterior temporal cortex, and inferior frontal cortex [73]. Bilateral temporal and motor cortices encode speech envelopes, with the left STG specializing in fine-grained phonetic information and the right middle temporal gyrus (MTG) in slower, syllable-level representations [74]. Beyond cortical areas, deeper structures like the hippocampus and thalamus contribute to speech production, as shown by SEEG recordings covering diverse cortical and subcortical regions [33].

Phonetic representations are encoded in distributed neural populations. The STG exhibits a caudal-anterior functional gradient, with posterior "onset" zones sensitive to acoustic onsets and phrase boundaries, and anterior "sustained" zones encoding ongoing phonetic and lexical-semantic features [75]. Within STG, phonetic feature selectivity is organized by manner and place of articulation, with distinct clusters for obstruents (plosives, fricatives) and sonorants (vowels, nasals), forming a multidimensional acoustic feature space [76]. During speech production, phonetic features can be decoded from neural activity in the vSMC and STG, with confusion patterns clustering according to articulatory characteristics [77]. The face motor cortex (FMC) shows locally distributed neural assemblies encoding articulatory movements, enabling higher word classification accuracy than Wernicke’s area, which exhibits more abstract semantic encoding [78]. Phonetic discriminability during continuous speech production involves dynamic activation of Broca’s area (supporting articulation planning), sensorimotor areas (supporting articulation), and STG (supporting speech processing), with peak activation timing aligned to phone production [47]. Speech decoding leverages both articulatory information from the sensorimotor cortex and perceptual or semantic information from the temporal lobe. The vSMC often provides the most informative signals, with increased electrode coverage further improving decoding accuracy [43].

Lexical-semantic processing engages ventral stream regions. Word prediction primarily activates lower-order regions like the STG and MTG, while sentence-level prediction recruits default mode network (DMN) regions, such as the temporoparietal junction (TPJ), medial prefrontal cortex (mPFC), and precuneus [79, 80]. Lexical activation is associated with the left posterior MTG (pMTG), while lexical selection engages the left inferior frontal gyrus (LIFG) and medial frontal areas. Lesions to the left pMTG result in persistent word retrieval deficits [81]. Semantic information can be decoded from intracranial recordings in the inferior frontal gyrus (IFG) and STG, supporting the ventral stream’s role in form-to-meaning mapping.

Cross-stream interaction is evident in overlapping functional networks and dynamic information flow. The STG’s onset and sustained zones interact to support speech parsing, with onset activity providing temporal landmarks and sustained activity enabling continuous phonetic processing. Functional interactions between word and sentence prediction levels occur sparsely at sentence boundaries, supporting the sparse updating hypothesis. Conduction aphasia, arising from impaired integration between dorsal and ventral streams, underscores the critical role of cross-stream communication for fluent speech. Recurrent neural computations within the STG may enable the binding of form to articulation and meaning, rendering stream reliance context-sensitive [82].

Individual differences in stream localization are observed across spatial, spectral, and functional domains. In HG, envelope following shows considerable intersubject variability, with some subjects maintaining high-frequency ERBP envelope tracking even for unintelligible speech. The frequency profile of gamma reactivity (low vs high gamma) and its spatial topography vary across subjects, reflecting individual differences in functional anatomy [83]. STG phonetic feature clusters show systematic individual variation but share common organizational principles. Speechresponsive electrode distributions, including tone- and syllable-discriminative electrodes in vSMC and widespread speech-responsive regions, exhibit intersubject variance influenced by language behaviors and functional anatomy [84]. Sensorimotor cortex activation patterns during speech perception overlap with those observed during production but show individual-specific differences, potentially leading to false-positive activations in language BCIs trained on production data [85].

The signal gradient across different speech types modulates the degree of reliance on each stream. High gamma power, associated with bottom-up acoustic encoding in the dorsal stream, peaks early (<100 ms), while low-frequency phase responses, linked to hierarchical integration in the ventral stream [86], peak later ( 150 ms) [73]. Phonological production tasks rely more on the dorsal stream, while lexical-semantic comprehension tasks depend on the ventral stream. Decoding latency and speed vary with speech type and vocabulary complexity, indicating that stream utilization is dynamically modulated [46]. Different speech stimuli, such as phonemes, words, and sentences, engage distinct hierarchically organized networks [87], with acoustic-phonetic features driving dorsal stream reliance and lexicalsemantic features enhancing ventral stream engagement [88].

To frame hierarchical stream organization in a comparative way, the “Hierarchical Functional Streams“ column of Table 2 summarizes the central pattern, where convergent dorsal–ventral evidence is accompanied by unresolved questions about stream overlap and context-dependent dominance; this aligns with the dorsal–ventral pathway component of Fig. 3.

### 2.3 Neural Signatures of Overt, Mimed, and Imagined Speech

Overt, mimed, and imagined speech exhibit distinct neural correlates across frequency bands and cortical regions. For instance, power spectrum changes for overt and imagined speech are spatially comparable but less pronounced for imagined speech, with fewer cortical sites showing significant changes, particularly in broadband high-frequency

activity (BHA). BHA increases in sensory and motor regions for both overt and imagined speech, but only in the superior temporal cortex during overt speech, decreasing during imagined speech, likely due to the absence of auditory feedback [26, 27]. ECoG studies have demonstrated distinct spatio-temporal cortical activation patterns during continuous overt and covert speech production: fronto-motor regions (ventral primary motor cortex, ventral premotor cortex, inferior frontal gyrus) activate prior to speech output during overt speech, while temporal regions (superior and middle temporal gyri) activate primarily during and after speech output, reflecting auditory feedback processing [89, 90, 91]. Direct comparison of overt and covert speech ECoG signals reveals common activations in auditory cortex, premotor and primary motor cortex, frontal eye fields, and dorsolateral prefrontal cortex, but covert speech signals do not reliably encode acoustic features like the speech intensity envelope. Magnetoencephalography (MEG) studies further show distinct decoding performances across stages (pre-stimuli, perception, preparation/imagination, production/articulation) for overt and covert speech, with the highest accuracy during production, followed by imagination [92]. Additionally, speech imagery, including covert and imagined speech, involves distinct neural mechanisms engaging Broca’s and Wernicke’s areas with differential activation patterns [93, 94].

Evidence of hierarchical channel nesting and differential frequency contributions to decoding is substantial. While BHA provides the best signal for overt speech decoding, both low- and higher-frequency power and local cross-frequencycoupling (CFC) contribute importantly to imagined speech decoding, particularly in phonetic and vocalic spaces. Low-frequency power (e.g., theta, low-beta) and cross-frequency dynamics (e.g., phase-amplitude coupling between low-beta and BHA) contain key information for imagined speech decoding. Spatial-spectral-temporal convolutional neural network (CNN) approaches, which integrate spatial information from multiple sensors with spectral and temporal features, enhance decoding accuracy by capturing hierarchical channel nesting and whole-brain dynamics. Intracranial electroencephalography (iEEG) studies identify distinct frequency bands: high-frequency gamma band activity linked to phoneme articulation and low-frequency theta band activity associated with syllabic and prosodic modulation, with cross-frequency coupling (e.g., theta phase-gamma amplitude coupling) reflecting hierarchical neural dynamics [95]. Thalamocortical studies further reveal hierarchical processing, where thalamic neurons prefer higher temporal modulation rates, and cortical neurons show slower preferences, indicating differential frequency contributions across regions [96]. For overt speech, gamma band (70-170 Hz) activity is highly task-related, with spectrogram reconstruction showing correlations peaking around the first formant frequency ( 300 Hz) [97]. Combining lowfrequency components (0–50 Hz) with the high-gamma envelope (70–150 Hz) yields higher speech reconstruction accuracy than single bands, implicating complementary hierarchical encoding [48].

Controversies persist regarding how far imagined-speech decoding can scale beyond constrained paradigms. Supportive evidence includes low-/cross-frequency intracranial decoding above chance [26], word-pair classification from direct cortical recordings [98], non-invasive phrase decoding during imagination stages [92], and recent real-time decoding of attempted and imagined-speech in implanted users [99]. Counter-evidence includes weak acoustic-envelope recoverability under covert conditions [89], declines in decoding performance in earlier continuous speech pipelines [47], and systematic reviews emphasizing heterogeneity in tasks, compliance checks, and preprocessing choices [93]. Methodologically, limited paired neural and speech data for supervision and temporal misalignment persist as practical bottlenecks [32, 33, 100, 101]. Overall, current studies indicate feasibility for proof-of-concept tasks but suggest that clinical-grade reliability remains to be established.

Across multiple datasets, an SNR gradient is observed from overt to mimed (silently attempted without vocalization) to imagined speech, with overt conditions typically exhibiting stronger and more spatially extensive high-gamma (BHA) activity than imagined conditions [26, 89, 102]. This gradient both motivates and constrains imagined-speech decoding: positive feasibility evidence shows above-chance decoding of covert and imagined speech in constrained word and phrase paradigms using low-frequency and CFC features [26, 98, 92], with recent implanted-participant work reporting real-time decoding of attempted and imagined speech [99]. At the same time, negative findings indicate that covert signals encode acoustic detail less reliably and exhibit substantial variability across participants and tasks [89, 47, 93], suggesting that robust large-vocabulary communication is not yet achievable. Crucially, the SNR gradient guides the choice of intermediate representations for decoding. Overt speech-related motor signals are stronger and more directly linked to acoustic features, supporting decoding strategies that exploit high-frequency articulatory correlates [103, 29]. In contrast, imagined speech exhibits weaker, more spatially diffuse activity and poorer discriminability of articulatory representations in BHA; instead, it more reliably engages perceptual (phonetic and vocalic) representations indexed by low-frequency bands and CFC [26, 104, 27], consistent with the flexible abstraction hypothesis [105]. Given the weaker SNR and typical data scarcity in implanted settings, this motivates targeting low-frequency and CFC features [26, 104] and decoding through explicit articulatory–acoustic intermediate parameters (e.g., pitch, formant frequencies) [106] rather than direct spectrograms or latent vectors, which can reduce sample complexity and improve trainability with limited neural data [32, 22]. Thus, imagined-speech variability demands adaptation toward perceptual and low-frequency structure [26, 105, 27], while overt speech can exploit higher-SNR, high-frequency articulatory signals [103, 29].

To contextualize covert and imagined speech mechanisms for decoding design, the synthesis appears in the “Overt, Mimed and Imagined Speech” column of Table 2, where the current pattern suggests an overt-to-imagined SNR decline together with the practical contribution of low-frequency/CFC features; this is the SNR-gradient pathway highlighted in Fig. 3.

### 2.4 Temporal Dynamics and Context Integration in Speech Representation

The critical role of temporally recurrent connections in cortical regions for generating context-dependent phonological representations is reflected in both computational models and empirical neural data. This principle is computationally realized in the Long Short-Term Memory (LSTM) network introduced by Hochreiter and Schmidhuber in 1997 [107], which, through its memory cells featuring constant error carousels and multiplicative gate units, is designed to control information flow. This architecture enables the storage of context-dependent information over long intervals, thereby facilitating the production of dynamic, context-sensitive phonological representations. Building on this, Graves et al. [108] demonstrated in 2006 that bidirectional LSTM (BiLSTM) networks, trained with Connectionist Temporal Classification (CTC) loss, can implicitly model inter-label dependencies. This is achieved by predicting labels that frequently co-occur in connected patterns, reflecting how cortical recurrent connections may integrate temporal context to shape phonological encoding. The role of recurrent dynamics in speech processing is empirically reinforced by recent studies. Luo et al. (2022) [7] showed that deep learning models like BiLSTMs map temporally structured neural features to sequence-based speech representations, a process underpinned by recurrent cortical connections that enable context-dependent integration [23, 25]. Corroborating this, Metzger et al. (2023) [50] provided evidence that the sensorimotor cortex (SMC) maintains temporally recurrent articulatory representations. These representations are somatotopically organized by place of articulation (POA) and are actively involved in context-dependent phonological encoding.

Evidence from intracranial recordings reveal that dynamic neural population activity during speech production closely parallels patterns seen in motor control. Specifically, Metzger et al. (2023) [50] reported strong correlations between the neural encoding of individual phones and concurrent orofacial movements, including tongue raising and lip puckering. These findings suggest that the SMC encodes articulatory gestures through dynamic neural activity that directly parallel the motor control patterns governing speech articulation. Using high-density micro-electrocorticographic (µECoG) arrays, Duraivel et al. (2023) [49] showed that neural population dynamics in the SMC are organized by articulatory features and phonemes. The finding that decoding errors most frequently involve phonemes that share articulatory features provides compelling evidence for a motor control-based model of neural encoding. Further supporting this framework, Martin et al. (2016) [98] reported that dynamic high gamma time courses obtained from ECoG recordings reflect complex temporal neural dynamics during speech production. Their use of dynamic time warping (DTW) to accommodate temporal variability resulted in improved classification accuracy, thereby strengthening the association between recurrent neural dynamics and motor control variability in speech. Complementing this, Heelan et al. (2019) [109] applied LSTM decoders to reconstruct spectrotemporal and phonetic features from secondary auditory cortex recordings in non-human primates, providing additional evidence that temporally recurrent cortical population dynamics are consistent with motor control patterns essential for speech production.

The integration of contextual information through temporal dynamics enables the decoding of continuous, naturalistic speech by allowing models to process unsegmented sequences and leverage distributed neural representations. Graves et al. (2006) [108] showed that CTC eliminates the need for pre-segmented data, allowing BiLSTM networks to train directly on continuous input sequences and handle temporal variability, a capability critical for naturalistic speech processing. Metzger et al. (2023) [50] demonstrated that bidirectional recurrent neural networks (RNNs) with CTC loss could decode continuous speech from ECoG signals at naturalistic rates (median 78 words per minute), with the recurrent network itself proving critical for performance. This reflects the network’s ability to integrate neural activity over time. Supporting this, Luo et al. (2022) [7] reported that sentence-level neural activity encodes richer temporal information than isolated phonemes, and that multi-stage deep neural networks, bridging neural features to audio synthesis via intermediary representations, can capture the dynamics of speech motor patterns, enhancing continuous speech decoding. Duraivel et al.(2023) [49] demonstrated that RNN-based sequence-to-sequence architectures can successfully decode ordered phoneme sequences from µECoG high-gamma activations without explicit phoneme onset information, relying purely on temporal context. Further evidence comes from Soroush et al. (2023) [102], who identified multi-frequency temporal features (theta, alpha, beta, broadband gamma) proximal to speech onset that support continuous speech representation. Broader spatial integration also appears important: Heelan et al. (2019) [109] found that decoding performance improves with higher neural channel counts, reflecting the importance of integrating context across spatially distributed cortical populations [110]. Collectively, these findings underscore that temporally recurrent cortical dynamics and context integration are foundational mechanisms for decoding fluent, naturalistic speech from intracranial brain recordings.

- Table 2: Critical synthesis of neural mechanism evidences across four dimensions, organized by consensus, controversies, sources of discrepancies, and experiments to resolve them.

Somatotopy and Population Dynamics

Hierarchical Functional Streams

Overt, Mimed and Imagined Speech

Temporal Dynamics and Context Integration

Consensus Spatially intermixed but population-somatotopic speech representations are repeatedly observed in vSMC/midPrCG, with robust CIS and oscillatory motifs during initiation and articulation.

An overt-to-mimed-toimagined SNR gradient is robust across studies; overt speech relies more on high-gamma, while covert speech carries useful low-frequency and CFC information.

A dorsal form-to-articulation stream and a ventral form-to-meaning stream are consistently supported by lesion, stimulation, and intracranial decoding evidence.

Temporal recurrence and context integration consistently improve continuous-speech decoding, especially with unsegmented neural streams and sequence-level objectives.

Controversy Subject-level reproducibility of somatotopic layouts and the universality of CIS/oscillatory motifs remain uncertain.

Whether imagined-speech decoding can reach clinically reliable, large-vocabulary performance remains unresolved.

Performance gains may reflect biologically meaningful temporal mechanisms or simply larger model capacity and dataset scale.

The key dispute is the degree of dorsal-ventral segregation versus overlap and how dominance shifts with task context.

What causes discrepancies

Coverage and localization heterogeneity, inter-subject pathology differences, and task differences (phoneme/word/sentence; overt/mimed/imagined).

Uneven sampling of temporal/frontal/subcortical regions, inconsistent temporal alignment strategies, and non-uniform spectral feature definitions.

Low SNR, missing acoustic alignment labels, uncertain behavioral compliance, variable electrode sampling, and inconsistent CFC definitions.

Different sequence lengths, alignment assumptions (explicit vs. CTC-like), vocabulary complexity, and inconsistent handling of cross-session non-stationarity.

Experiments to resolve

Standardize cross-center electrode localization, map contacts to Montreal Neurological Institute (MNI)/atlas common space, and learn shared representations with uncertainty estimates.

Use harmonized multi-task protocols within participants and combine causal perturbation with recordings to test directional information flow.

Combine behavioral verification tasks, covert neural-alignment surrogates, selfsupervised/contrastive pretraining, and explicit multi-band feature fusion.

Run matched-capacity model comparisons with temporal ablations and longitudinal benchmarks to separate short-term fitting from stable context representations.

To integrate temporal-mechanistic interpretation with model-level results, a concise summary is provided in the “Temporal Dynamics and Context Integration” column of Table 2, where recurrent context integration improves sequence decoding but attribution to neural mechanism versus model capacity remains unsettled; in Fig. 3, this corresponds to the temporal population-dynamics pathway linked to sequence models such as CTC/RNN/Transformer.

## 3 Decision-Oriented Hardware Protocol of Intracranial Recording Modalities

As summarized in Fig. 2, the choice of recording modality and implant design directly determines which neural features can be captured (e.g., spikes versus field potentials), which anatomical targets can be accessed (surface, depth, or penetrating cortex), and the long-term maintenance burden in chronic use. These factors largely define the attainable information content and establish the upper bound on system performance, while decoder design primarily governs how closely a given implementation approaches this bound. Consequently, intracranial language BCIs should treat electrode selection as a primary design variable. In this section, we review intracranial electrode families, representative suppliers, and development trajectories. Quantitative comparisons emphasize hardware-level constraints that shape downstream decoding potential before considering software-side optimization.

### 3.1 Intracranial Electrode Families, Representative Suppliers, and Development Trajectories

Electrode choice is a foundational design decision that shapes the decoding target (e.g., text vs. speech synthesis), surgical workflow, calibration burden, packaging complexity, and the feasibility of eventual home deployment. The

- Table 3: Summary of intracranial electrode families and representative suppliers relevant to language BCI research and clinical translation. Supplier examples are non-exhaustive; availability and regulatory status vary by region, indication, and system compatibility.

Electrode family Typical geometry / signal scale Typical role in language BCI Representative suppliers or platform examples

Macro-ECoG grids/strips (subdural or epidural cortical surface)

Millimeter-scale contacts on flexible strips/grids; captures cortical field potentials and broadband high-gamma over broad peri-Sylvian cortex.

Clinical mapping-compatible pathway; strong option for reliability-first communication interfaces and broad cortical coverage studies.

Ad-Tech Medical (Subdural grids/strips); Integra LifeSciences (Epilepsy products/brain mapping lines); Neuracle (NEO; implantable wireless semi-invasive epidural system); Sinovation | HKHS (Intracranial Cortical Electrode: strip/grid models)

High-density surface ECoG / µECoG (thin-film cortical arrays)

Sub-millimeter to millimeter contact pitch with flexible/thin-film substrates; improves spatial sampling relative to macro-ECoG while preserving surface coverage.

Higher-fidelity articulatory and phonemic decoding, speech synthesis feature extraction, and research on fine cortical organization.

CorTec (°AirRay grid/strip electrodes); NeuroOne (Evo® Cortical thin-film electrode); Precision Neuroscience (Layer 7 cortical interface); NeuroXess (Surftrode; flexible cortical electrode).

DIXI Medical (MICRODEEP® SEEG); Ad-Tech Medical (Depth electrodes/SEEG); Rishena (Single-use Depth Electrode (SEEG)); Sinovation | HKHS (Intracranial Depth Electrode); NeuroXess (Silktrode; flexible deep electrode).

SEEG depth electrodes (stereotactic depth shafts)

Linear contact arrays along depth trajectories; samples distributed cortical and subcortical structures in 3D with clinically routine stereotactic workflows.

Network-level language/speech studies, deep target access, and clinically practical implantation in epilepsy-style pathways.

Penetrating intracortical MEA (Utah-style or shank-based arrays)

Highest-resolution speech-motor decoding and low-latency/high-rate decoding demonstrations, especially when local articulatory information density is critical.

Dense penetrating microelectrodes with highest local specificity; captures spikes/threshold crossings, spike-band power, and local field potentials from small cortical territories (often “up to ~100” electrodes per array depending on design).

Blackrock Neurotech (Utah Array); Blackrock Neurotech (Utah Slant Array); MicroProbes for Life Science (penetrating MEAs); StairMed (HNE ultra-flexible micro-nano electrode; shank-based penetrating arrays).

Emerging flexible penetrating/threaded arrays (investigational)

Flexible ultrathin penetrating elements and high channel counts; aims to improve channel scalability and chronic tissue interface properties.

Potential future route for combining high channel count with improved chronic packaging and fully implanted wireless systems.

Neuralink (threaded arrays; investigational); Paradromics (Connexus BCI; investigational); NeuroXess (Silktrode / Plextrode; investigational flexible electrodes); StairMed (ultra-flexible penetrating electrodes; platform ecosystem).

Hybrid recording-stimulation cortical/depth systems

Electrode systems designed for both neural recording and stimulation/functional mapping; actual capability depends on electrode specs + lead/connector + stim/record hardware ecosystem.

Useful for combined mapping-decoding workflows, causal perturbation studies, and translational systems that may require stimulation-assisted functions.

CorTec (°AirRay: record & stimulate stated); DIXI (SEEG + functional mapping / thermocoagulation context); Ad-Tech (mapping/stimulation ecosystem dependent); Sinovation | HKHS (Intracranial Depth Thermal Coagulation Electrode; mapping/ablation ecosystem); Rishena (SEEG ecosystem; thermocoagulation-oriented product lines described); NeuroXess (Plextrode; combined deep/cortical electrode).

Notes: this table emphasizes engineering categories used in review synthesis; exact electrode dimensions, contact counts, magnetic resonance (MR)-conditional labeling, stimulation rating, connectors, and approved indications vary within and across suppliers.

relevant electrode families used in language BCIs can be broadly categorized into surface cortical arrays (macro-ECoG and high-density/µECoG), SEEG depth electrodes, and penetrating intracortical MEAs. In parallel, emerging hybrid systems are seeking to integrate recording and stimulation modalities within chronically stable packaging. Across these electrode families, the primary design consideration involves a nuanced trade-off that balances coverage, spatial specificity, surgical accessibility, and long-term maintainability, factors that extend well beyond signal quality alone.

- Table 3 summarizes the major intracranial electrode families used in or adjacent to language BCI development, together with representative commercial suppliers and platform examples. Note that the supplier list is illustrative and nonexhaustive; verification against local regulatory approvals, regional distribution, and current product portfolios is essential prior procurement or clinical planning.

The trajectory of intracranial electrodes in language BCI reflects a progression from clinically available mapping hardware toward purpose-optimized neuroprosthetic interfaces. Early proof-of-concept decoding studies leveraged electrodes originally designed for epilepsy monitoring, beginning with macro-ECoG grids and strips, and later incorporating SEEG depth electrodes, thereby capitalizing on established neurosurgical workflows and clinical monitoring

infrastructure [19, 20, 47]. This foundational work demonstrated that cortical field potentials, especially in the highgamma band, contain rich speech information, and that intracranial recordings are capable of supporting continuous or near-continuous decoding in controlled settings.

The next phase focused on improving spatial resolution, task complexity, and decoding fidelity. High-density cortical recordings and improved modeling pipelines enabled stronger articulation-level decoding and speech synthesis, while broader datasets clarified how electrode placement and coverage heterogeneity shape performance [28, 9, 111, 7, 49]. In parallel, SEEG expanded the accessible anatomical search space beyond cortical surface coverage, supporting distributed language-network sampling and more flexible trajectory planning under clinical constraints [32, 51, 34]. Recent work represents a third phase in which electrode hardware is increasingly evaluated by chronic utility rather than acute signal quality alone. Intracortical MEAs enabled high-rate and high-fidelity speech neuroprosthesis demonstrations [1, 10, 112], while chronic ECoG systems demonstrated stronger home-use feasibility in selected users with ALS [21, 22]. This shift reframes the notion of the “best electrode” as a use-case-dependent decision – one that balances coverage, resolution, packaging, calibration burden, and care logistics, rather than simply maximizing any single signal metric [43, 113, 114].

Looking forward, the most important electrode-development directions for speech neuroprostheses are likely to include: (i) coverage–resolution co-optimization (e.g., hybrid macro+µECoG or surface+depth strategies), (ii) chronic biocompatibility improvements and lower-impedance stable interfaces, (iii) fully implanted wireless systems with onboard preprocessing to reduce infection risk and setup burden, (iv) high-channel-count active multiplexed arrays that preserve bandwidth within thermal/power limits, and (v) electrode designs that support both decoding and causal stimulation/mapping for adaptive closed-loop speech systems [115, 38, 37, 43]. These future directions are already visible in emerging recording technologies that advance high-fidelity neural capture for language BCIs by addressing limitations in spatial-temporal resolution, biocompatibility, and coverage. Among these, novel flexible electrode arrays and high-channel-count microelectrode systems have shown particular promise. Xu et al. (2025) [115] developed a flexible molybdenum disulfide (MoS2)-based active array with ultrahigh spatial resolution (up to 51 pixels mm−2), a broad bandwidth (0.5 Hz–10 kHz), and fast sampling rates ( 80 kHz), enabling capture of fine-grained high-frequency multiunit activity with µV-range amplitude. Fabricated on flexible polyimide substrates, this array demonstrated excellent biocompatibility and stable SNRs over 4 weeks of chronic implantation, outperforming commercial graphenebased passive arrays in tuning curve selectivity, latency, and amplitude variance.

Intracortical MEAs have also shown significant advancements in capturing speech-related neural activity. Willett et al. (2023) [1] used high-resolution spiking activity recordings from intracortical arrays to achieve a 9.1% WER on a 50-word vocabulary and 23.8% on a 125,000-word vocabulary, with decoding speeds of 62 words per minute. They further identified that the ventral premotor cortex (area 6v) contains a dense, intermixed representation of speech articulators within a small (3.2 × 3.2 mm²) region, with phoneme articulation details preserved even years after paralysis. Notably, decoding accuracy improved log-linearly with electrode count, suggesting that denser arrays could further enhance performance. Similarly, Wood et al. (2025) [112] implanted 256 microelectrodes in the precentral gyrus, capturing neural activity that drove a voice synthesizer to generate speech resembling the participant’s pre-ALS voice with 25 ms latency, including paralinguistic features like intonation and emphasis for modulating speech style (e.g., statements vs. questions). For ECoG, Luo et al. (2022) [7] highlighted innovations such as 32 recording contacts per electrode, robotic insertion techniques to minimize tissue trauma, and flexible array designs, which address traditional limitations in spatial density and coverage. These advances, combined with deep learning methods mapping ECoG high gamma activity to vocal tract trajectories, support improved neural capture for speech decoding. While long-term ECoG stability for speech remains under investigation, motor BCI research has demonstrated reliable chronic decoding, and safety in individuals with late-stage ALS has been reported.

These emerging technologies, including MoS2-based active arrays with ultrahigh spatiotemporal resolution, highchannel-count intracortical microelectrodes, and advanced ECoG configurations, overcome traditional constraints by enhancing resolution, biocompatibility, and coverage. They enable the capture of fine-grained speech-related neural activity, from spiking dynamics to paralinguistic features, and hold significant potential for advancing the clinical translation of language BCIs.

### 3.2 Quantitative Trade-offs in Resolution, Signal Quality, and Clinical Feasibility

Willett et al. (2023) [1] conducted a comprehensive investigation on intracranial MEAs, providing key insights into their performance metrics and comparisons with other intracranial recording modalities. In terms of spatial sampling density, the 3.2 x 3.2 mm² MEAs used in their study contained 128 channels each, exhibiting rich and spatially intermixed tuning to speech articulators, which allows for precise decoding from a small cortical area [1]. For signal quality, threshold crossing rates with root-mean-square (RMS) thresholds ranging from -4.5 to -3.5 effectively detected strong spiking activity well above the noise floor. Notably, combining spike band power with threshold crossings was found to improve RNN decoding performance. Regarding coverage depth, the arrays were implanted intracortically, targeting

[Figure 4]

- Figure 4: Schematic illustration of a practical selection heuristic for intracranial recording modalities. MacroECoG/SEEG prioritize coverage and deployment practicality, µECoG prioritizes cortical spatial detail, and intracortical MEAs prioritize maximal local information density and high-rate decoding at higher implantation/maintenance complexity.

superficial cortical layers in area 6v. Although their cortical coverage was narrow, this was offset by the high neural information content per channel. In terms of decoding performance, intracortical MEAs paired with RNN decoders achieved a high decoding speed of 62 words per minute, which is 3.4 times faster than previous BCI speech decoding approaches [1]. WERs were reported as 9.1% on a 50-word vocabulary and 23.8% on a 125,000-word vocabulary, with error rates decreasing log-linearly as the electrode count increased. Specifically, doubling the number of electrodes nearly halved the error rate [1].

In considering the matching of task to recording modality, high-resolution MEAs are recommended for precise speech reconstruction at the phoneme and word levels, particularly when the goal is rapid and unconstrained communication with large vocabularies. In contrast, the study predicts that SEEG or macro-ECoG may be more suitable for clinical communication interfaces with simpler vocabularies, while MEAs are best suited for supporting high-fidelity speech synthesis or restoration. Comparisons to other modalities highlighted that ECoG grids reportedly show broader somatotopy but lower spatial resolution than MEAs. However, MEAs have notable constraints: they require surgical implantation, have limited spatial coverage, and their long-term stability and clinical viability need further validation. Additionally, training data requirements are high, with 260–440 sentences needed per day, though decoding still performs reasonably with reduced retraining [1]. The study also noted that Brodmann area 44, when sampled with intracortical electrodes, contained little to no useful speech-related information, emphasizing the importance of precise targeting for optimal performance.

A structured and decision-relevant synthesis of these modality trade-offs is provided in Table 4, which integrates measurement scale, signal type, implantation pathway, chronic evidence, and deployment constraints for real-world speech neuroprostheses. A practical selection heuristic, shown in Fig. 4, is as follows: choose macro-ECoG or SEEG when coverage, clinical workflow familiarity, and lower deployment complexity dominate; choose µECoG when cortical spatial detail is a key bottleneck; and choose penetrating intracortical MEAs when the target application demands maximal local information density and high-rate decoding despite higher implantation and maintenance complexity [19, 20, 7, 1, 10, 112, 51].

- Table 4: Quantitative decision matrix for intracranial language BCI recording modalities. Values represent typical ranges and reported practice patterns rather than absolute limits.

Dimension MEA (intracortical) ECoG (µECoG/macro-ECoG)

SEEG (depth electrodes)

Spatial resolution / sampling scale

Surface sampling from sub-millimeter µECoG to millimeter-scale macro contacts; strong cortical field-potential specificity [49, 7].

Sub-millimeter local sampling with highest unit-level specificity in small cortical patches [1, 112].

Millimeter-scale contacts along depth shafts; sparse per contact but distributed 3D sampling across deep and surface targets [51, 32].

Dominant speech-relevant signals

Depth LFP and high-gamma/BHA features with access to deeper structures and distributed language networks [51, 34].

Broadband high activity (BHA/high-gamma) plus lower-frequency LFP phase/amplitude features [7, 73].

Spikes, threshold crossings, spike-band power, and local field potentials (LFP) [1].

Coverage footprint Limited cortical territory (high information density per channel, low areal coverage) [1].

Broad peri-Sylvian cortical coverage for speech motor-auditory mapping [20, 7].

Broad network reach (bilateral/deep) with clinically constrained but flexible trajectories [32, 51].

Implant pathway (research vs. routine)

Penetrating cortical implantation via craniotomy; currently mostly investigational BCI use [10].

Stereotactic depth implantation with mature clinical workflow in epilepsy monitoring [32].

Subdural/epidural cortical placement with clinically established neurosurgical workflows (primarily epilepsy mapping) [19, 20].

Chronic stability evidence

Multi-month speech performance reported, but frequent recalibration remains common [10, 1].

3-month no-recalibration ALS use and one-year signal stability analyses reported [21, 114].

Increasing speech-decoding evidence, but chronic unattended home-use evidence is still limited [51, 43].

##### Home-use feasibility Currently limited by

Promising with fully implanted wireless trajectories, but speech-specific home validation is early [32, 43].

Strongest published home-use evidence in ALS language BCI so far [21, 22].

percutaneous connectors and setup/maintenance burden in most reports [1, 10].

Training data and calibration burden

High in current high-performance pipelines (e.g., 260–440 sentences/day in one paradigm) [1].

Moderate in many pipelines; selected users showed low recalibration burden over months [21, 22].

Often moderate-high because sparse heterogeneous placement increases transfer/adaptation difficulty [51, 32].

Typical reported latency

Near-real-time components reported in recent systems (∼25 ms audio delay to ≤80 ms/phoneme decoding) [37, 112, 10].

End-to-end home ALS latency around 1.24 s has been reported; online word-level synthesis is feasible [21, 22].

Latency evidence remains less standardized and often task/pipeline dependent in current speech studies [51].

Regulatory and device maturity

High procedural clinical maturity for diagnostic use; chronic speech-prosthetic translation still emerging [32, 43].

Electrode modality/procedures are clinically mature for mapping; chronic communication indication remains investigational [19, 43].

Predominantly investigational for communication neuroprostheses (Investigational Device Exemption (IDE)-stage evidence) [10, 43].

### 3.3 Chronic Implant Stability and Clinical Deployment Constraints

Current literature indicates that multi-month stability is achievable in selected chronic implants, but generalizable long-horizon robustness across users and settings remains uncertain. Positive reports include 3-month no-recalibration ECoG control in ALS [21], online speech synthesis across sessions separated by months [22], 8.4-month intracortical speech decoding with high session-level accuracy [10], and one-year analyses linking performance to high-gamma stability [114].

Countervailing evidence shows that the adaptation burden has not disappeared: rapid in-session retraining was required in >400-day cursor-control experiments [113], occasional recalibration remained necessary in long-running speech use [10], and daily retraining has been used in high-performance pipelines to track neural drift [1]. Earlier and intermediate language BCI reports established feasibility but provide limited evidence for unattended home deployment over long horizons [111, 19, 20]. Safety results are encouraging but still based on small cohorts. Recent chronic reports noted no device-related serious adverse events in the analyzed participants [21, 10]; however, broader risk quantification across centers remains to be established.

Overall, existing data suggest that stability depends on both hardware durability and adaptive decoding strategies for non-stationary neural signals [43, 113]. For home use, percutaneous hardware, setup assistance, and residual recalibration requirements continue to limit full autonomy [37, 10]. For deployment decisions, these constraints should be treated as explicit optimization variables rather than secondary discussion points. A practical, bounded deployment utility can be written as

5

U = wAA˜ + wRR˜ −

λkC˜k, (1)

k=1

where A˜ denotes a normalized communication-accuracy score (larger is better), R˜ denotes a normalized responsiveness score derived from end-to-end latency (larger is better), and C˜k are normalized clinical deployment-burden scores (larger is worse). All components are mapped to [0,1] to make U dimensionless and bounded (avoiding scale dependence on units such as ms vs. s), and weights are nonnegative and optionally normalized for interpretability (e.g., wA + wR + 5k=1 λk = 1).

With this convention, U can be read as a single “deployment score”: values closer to the upper end of its range indicate a configuration that is simultaneously accurate, responsive, and low-burden (a plausible path to largely autonomous home use); intermediate values indicate that communication performance is acceptable but practical frictions (e.g., frequent recalibration, nontrivial caregiver/setup time, or limited robustness) still meaningfully constrain daily adoption; and low values indicate that deployment burdens dominate (e.g., high infection/maintenance risk, tight power/thermal margins, fragile packaging, or substantial home-environment degradation), making the system unsuitable for routine home autonomy despite possibly high laboratory accuracy. In practice, U can be computed per candidate system configuration (hardware + decoder + workflow) to rank alternatives or to guide multi-objective optimization under scenario-specific weight settings. Concretely, A˜ can be instantiated using task-appropriate accuracy metrics mapped to [0,1] (e.g., 1 − WER for text output), and R˜ can be instantiated by mapping latency into [0,1] via a pre-registered monotone transformation over an acceptable latency range. Accordingly, the deployment-burden vector is taken as

C˜ = [C˜infection,C˜power,C˜packaging,C˜care,C˜home], (2) with the following operational interpretations:

- • C˜infection (percutaneous-interface risk): transcutaneous connectors increase infection risk; quantify using infection events per implant-day together with intervention burden (e.g., clinic visits, antibiotics, revisions), mapped to [0,1].
- • C˜power (battery–wireless budget): wireless bandwidth for high-rate neural streams must be balanced against battery life and tissue heating constraints; quantify using average power draw, wireless duty-cycle, and thermal margin, mapped to [0,1].
- • C˜packaging (long-term encapsulation): hermetic sealing quality, corrosion resistance, and impedance drift determine effective service lifetime; quantify using impedance drift, failure-rate proxies, or predicted service lifetime, mapped to [0,1].
- • C˜care (patient adherence and maintainability): daily setup time, caregiver workload, and recalibration frequency directly affect sustained home adoption; quantify using minutes/day, caregiver involvement, and recalibration events per week, mapped to [0,1].
- • C˜home (domestic robustness): system performance under household acoustic noise, motion artifacts, and electromagnetic interference must be prospectively stress-tested; quantify using performance degradation under stress (e.g., ∆WER, dropout rate, latency inflation), mapped to [0,1].

## 4 Algorithmic Advances in Generalization and Interpretability

In the hardware–software co-design view of Fig. 2, algorithmic choices determine how effectively recorded neural information is converted into robust linguistic outputs under fixed recording constraints. Beyond subject-specific

[Figure 5]

- Figure 5: Conceptual landscape of language BCI decoding models. Decoding approaches are positioned qualitatively along two axes: biological interpretability and population-level generalization. Direct acoustic models typically offer limited interpretability and cross-subject robustness, whereas articulatory intermediates and topology-agnostic transformers occupy the high-generalization regime. Dual-path frameworks integrate acoustic and linguistic representations, and language-prior–assisted models improve large-vocabulary performance but may introduce bias. Positions reflect conceptual trends rather than quantitative benchmarking.

laboratory demonstrations, clinically viable language BCIs require decoders that generalize across participants, heterogeneous electrode layouts, sessions, and speech modes, while remaining interpretable enough to support mechanism validation and user-centered safeguards. This section reviews recent advances spanning topology-agnostic sequence and transformer architectures, biologically grounded articulatory intermediates, language-prior assistance, dual-path and multi-modal decoding frameworks, and interpretable models for linking performance gains back to neural mechanisms.

### 4.1 Cross-Subject Generalization via Sequence and Transformer Architectures

This section addresses the software-design side of Fig. 2: decoder architecture, intermediate representations, and adaptation strategies largely determine how efficiently neural features (e.g., high-gamma, low-frequency, or crossfrequency coupling (CFC) features) are converted into robust outputs under a fixed recording setup. Fig. 1 outlines this hardware–software co-design perspective by organizing representative intracranial speech-decoding frameworks into three thematic lanes, with compact technical tags that make cross-task design choices visually comparable. To synthesize the trade-space discussed in this section, Fig. 5 further provides a conceptual map of major decoding paradigms along two axes: biological grounding and population-level generalization. This framing helps explain why the following subsections emphasize topology-agnostic transformers and articulatory intermediate targets as promising routes for scalable and interpretable decoding, while also highlighting where language-prior assistance and direct acoustic decoding introduce distinct strengths and risks.

Cross-subject generalization in language BCIs has been significantly advanced through the application of sequence and transformer architectures, which address the challenges of variable electrode placements and sparse cortical coverage. Sequence-to-sequence models have demonstrated robust performance in decoding speech-related neural signals across participants. Singh et al. (2025) [52] employed a sequence-to-sequence model with LSTM layers to decode variable-length phonemic sequences, developing a cross-subject transfer learning framework that isolates shared latent manifolds. Their group-derived decoder outperformed models trained on individual data alone, with transfer learning involving pre-training a core RNN encoder and affine layers on a single subject, then freezing these components while fine-tuning a subject-specific 1D convolutional layer to accommodate variable electrode configurations; this approach resulted in no significant difference in PER when transferred to unseen participants. Similarly, Makin et al. (2020) [9] implemented a sequence-to-sequence encoder-decoder architecture with RNN-LSTM cells to decode

ECoG signals into written sentences, achieving mean WERs as low as 3% for individual participants. Transfer learning further improved cross-subject generalization, with networks pretrained on one participant and fine-tuned on limited data from another reducing WER by up to 36%, even with ECoG arrays in different hemispheres. For SEEG data, Wu et al. (2024) [51] showed that both RNN-based and transformer-based sequence-to-sequence models outperformed linear regression baselines in mel-spectrogram reconstruction accuracy, with comparable results achievable using only a few electrodes, highlighting the robustness of these architectures to electrode sparsity.

Transformer-based decoders have further enhanced cross-subject generalization by leveraging anatomical information and shared neural representations. Défossez et al. (2023) [40] introduced a shared deep convolutional architecture with a participant-specific layer, trained on non-invasive MEG/EEG data using contrastive learning aligned to pretrained speech representations (wav2vec 2.0). This group-derived model outperformed individual-specific decoders, achieving up to 70.7% top-10 segment-level accuracy in MEG datasets and generalizing to unseen participants and vocabulary. A notable advancement is the SwinTW transformer, proposed by Chen et al. (2024) [39], which uniquely handles arbitrarily positioned electrodes by leveraging their 3D anatomical locations (MNI coordinates and brain region embeddings) instead of 2D grid indices. SwinTW generates tokens from each electrode individually and applies temporal window attention, enabling multi-subject training without subject-specific layers. Multi-subject SwinTW models achieved decoding performance comparable to subject-specific models on training participants (e.g., PCC of 0.837 vs. 0.831) and generalized to unseen participants with an average PCC of 0.765 in leave-one-out cross-validation, outperforming grid-based models like ResNet and 3D Swin Transformer. This is why topology-agnostic transformer families are placed near the high-generalization region in Fig. 5: their architectural inductive bias is designed around anatomical variability rather than fixed electrode grids, which directly targets the central barrier to cross-subject transfer.

Collectively, these sequence and transformer approaches suggest that explicitly modeling shared structure—via latent articulatory manifolds or anatomy-aware tokenization—is central to cross-subject transfer. Group-derived models consistently outperform individual models by learning shared latent articulatory information. Singh et al. [52] demonstrated that multi-subject models, which concatenate subject-specific features and learn shared recurrent layers, reduced PER and were robust to regional electrode occlusion (REO), particularly showing resilience in sensorimotor and temporal lobe electrode removal, whereas single-subject models were significantly affected by removal of key speech production regions. Défossez et al. [40] similarly found that decoding accuracy increased with more training participants, indicating the model learned common neural representations across individuals. Chen et al. [39] showed that SwinTW’s use of anatomical positional bias enabled learning of shared latent representations across diverse electrode layouts, improving cross-subject robustness. Despite these advancements, challenges in achieving consistent cross-subject performance remain. Singh et al. [52] noted that group model accuracy plateaus at 3-4 subjects, and transfer learning performance improves with increased similarity of electrode coverage patterns between training and inference subjects. Wu et al. [51] highlighted electrode contribution variability across subjects: some participants exhibit critical electrodes whose removal causes significant performance degradation, while others show distributed information, complicating generalization; additionally, SEEG’s sparse, clinically constrained coverage limits consistent performance. Makin et al. [9] pointed to limited training data per participant as a barrier to scaling to larger vocabularies and unconstrained language. Chen et al. [39] acknowledged that while SwinTW generalizes well to unseen participants, achieving consistently high accuracy for subjects outside training cohorts remains a challenge, motivating future research into larger datasets and subject-specific refinements.

### 4.2 Biologically Articulatory Representations for Cross-Speaker Transfer

Biologically grounded articulatory representations, which encode the coordinated kinematic trajectories of vocaltract movements, have emerged as effective intermediate targets in language BCIs, offering distinct advantages in cross-speaker generalization, data efficiency, and zero-shot voice conversion. These representations leverage the low-dimensional, somatotopic encoding of articulatory gestures in the sensorimotor cortex, where neural activity reflects the physical shaping of the vocal tract to produce speech sounds. Studies have demonstrated that such articulatory features are highly conserved across speakers, with state-space trajectories of decoded articulation showing high similarity (r > 0.8) between participants, suggesting a shared neural representation of articulatory kinematics that facilitates cross-speaker transfer. For instance, the Speech Articulatory Coding (SPARC) framework proposes a universal articulatory space, where a single-speaker electromagnetic articulography (EMA) template can be adapted to multiple speakers via linear affine transformations to compensate for anatomical differences, enabling speaker-agnostic acoustic-to-articulatory inversion with performance comparable to multi-speaker systems [53]. Accordingly, Fig. 5 positions articulatory-intermediate paradigms toward the biologically grounded and high-generalization end of the landscape: the representation itself remains interpretable in terms of speech motor control while also supporting transfer across speakers and recording configurations.

In terms of data efficiency, articulatory intermediates have shown robust performance with limited training data. Anumanchipalli et al. [28] found that decoding articulatory kinematics first, then transforming to acoustics, achieved reliable speech synthesis with as little as 25 minutes of speech data, outperforming direct acoustic decoding. This efficiency is attributed to the low-dimensional manifold of articulatory kinematics, which constrains the high-dimensionality of acoustic signals, making the neural mapping more learnable. Additionally, articulatory coding supports zero-shot voice conversion by disentangling speaker-specific voice texture from articulatory features. SPARC, for example, uses a speaker identity encoder to separate articulation from voice characteristics, enabling accent-preserving zero-shot conversion by switching speaker embeddings while maintaining articulatory trajectories.

Compared to acoustic or text-based targets, articulatory frameworks have demonstrated improved synthesized speech quality. Silva et al. [8] noted that decoding articulatory features before transforming to acoustics yields higher quality than decoding acoustics directly from neural data. Furthermore, these frameworks support large-vocabulary decoding at natural speaking rates, with Chartier et al. [8] achieving 78 words per minute (WPM) using CTC loss to map sensorimotor cortex activity to sentences during silent speech. Clinically, such systems have restored naturalistic speech in individuals with paralysis, as shown by Wood et al. [112], where a BCI decoded neural activity from MEAs to generate speech resembling the participant’s pre-ALS voice, with real-time feedback and paralinguistic features like intonation.

However, trade-offs exist between biological interpretability and decoding accuracy. While articulatory representations offer direct insights into the neurophysiological basis of speech motor control, some degradation in naturalness has been observed in zero-shot voice conversion, particularly for rare combinations of accent and voice. This suggests that while the low-dimensional, biologically grounded nature of articulatory features enhances generalization and interpretability, optimizing for maximum accuracy may require balancing these constraints against the complexity of acoustic outputs.

### 4.3 Large Language Models (LLMs) as Language Priors: Utility and Risks

In BCI pipelines, linguistic priors (from n-gram to neural language models) have been associated with lower decoding error or improved output coherence in continuous decoding and large-vocabulary settings [47, 111, 1, 10]. A dual-path framework further reported improved intelligibility when acoustic and linguistic pathways were fused [36]. Outside BCI, wav2vec/HuBERT-style fusion and transformer language models report consistent WER reductions, supporting the plausibility of this mechanism [116, 117, 118]. From a computational-neuroscience perspective, LLM-based components also provide a useful bridge between linguistic theory and neural data, and model-brain alignment analyses can help evaluate whether language-prior representations are biologically plausible rather than only performanceimproving [119, 120]. In Fig. 5, these language-prior–assisted approaches are placed as a high-utility route for improving large-vocabulary decoding, but not at the most biologically grounded end, because gains often arise from external linguistic regularization rather than directly interpretable neural-to-speech mappings.

However, risk evidence is also multi-source. In brain-to-voice settings, generative linguistic pathways can bias outputs toward probable text patterns, potentially shifting away from intended content [36]. Ethical analyses and design recommendations further indicate agency and ownership risks when model priors dominate user intent unless start/stop, confirmation, and veto controls are explicit [121, 122, 46, 120]. At a representation level, dataset-derived bias and incomplete brain-alignment of current LLM features indicate unresolved attribution and reliability issues [123, 124, 86], while semantic reconstruction studies further foreground privacy risks around high-level language content extraction from neural signals [125]. This risk profile is also reflected in Fig. 5, where the benefit of language-prior assistance is shown alongside a potential bias cost: better lexical coverage and fluency may come at the expense of faithful intent expression if priors are insufficiently constrained. Accordingly, current evidence suggests that LLM priors can improve fluency and error rates in constrained or assisted settings [36, 46, 88], while real-world risk rates (intent drift, bias harms, latency penalties) remain to be established through prospective multi-user evaluations [8, 43, 121, 122, 46].

### 4.4 Dual-Path and Multi-Modal Decoding Frameworks

Dual-path decoding frameworks are designed to address the traditional trade-off between acoustic naturalness and linguistic intelligibility by concurrently reconstructing acoustic and linguistic features from neural signals. An early example of such an approach is the Brain-to-Text system developed by Herff et al. [47], which integrates acoustic and linguistic representations to decode continuously spoken speech from intracranial ECoG recordings. The acoustic pathway models broadband gamma power from ECoG as context-independent Gaussian phone models, capturing neural activity across time intervals with feature stacking to integrate temporal context (±200 ms), while the linguistic pathway employs statistical language models (n-gram) and a pronunciation dictionary. By combining these via Viterbi decoding to find the most likely word sequence, the system balances neural signal decoding with lexically and syntactically informed prediction, preserving lexical content and intelligibility, as evidenced by WERs as low as 25% and phone

error rates below 50% [47]. In the conceptual landscape (Fig. 5), dual-path frameworks are therefore placed between purely acoustic decoding and language-prior–dominated approaches, because they explicitly combine signal-faithful acoustic reconstruction with linguistic structure rather than relying on either pathway alone.

A more recent explicit dual-path framework, proposed by Li et al. [36], further advances this paradigm by separately decoding acoustic and linguistic representations and fusing their outputs. The acoustic pathway utilizes a bidirectional LSTM decoder and a pre-trained high-fidelity generative adversarial network (HiFi-GAN) to reconstruct detailed spectrotemporal speech features, capturing speaker-specific timbre and prosody with data efficiency (requiring only 20 minutes of neural recordings per subject). In contrast, the linguistic pathway employs a Transformer-based adaptor to extract high-level discrete word tokens, which are synthesized into speech via a text-to-speech (TTS) generator (Parler-TTS) to capture syntactic and semantic information. Fusion is achieved through voice cloning (CosyVoice 2.0), which uses the acoustic output as a voice reference and the linguistic output as text input, resulting in synthesized speech with high MOSs ( 4.0/5), mel-spectrogram correlation around 0.824, and WERs ( 18.9%) comparable to noisy speech conditions (-5dB SNR) [36]. Ablation studies confirm that integrating both pathways delivers substantial improvements over acoustic-only or linguistic-only reconstructions, with significant reductions in WERs and PERs while maintaining high acoustic fidelity.

Architectural advances, such as the Transformer model introduced by Vaswani et al. [126], provide a foundation for dual-path decoding through multi-head self-attention mechanisms. Multi-head attention allows the model to jointly attend to information from different representation subspaces, supporting simultaneous processing of acoustic-like temporal patterns and linguistic structural information, which can be interpreted as a dual-path strategy balancing naturalness and intelligibility. Encoder-decoder attention layers further enable integration of multiple data modalities, while positional encoding injects sequence order information crucial for preserving prosody and lexical content in the output. Although originally designed for machine translation, these principles are directly applicable to speech decoding frameworks aiming to reconstruct acoustic and linguistic features concurrently.

Additionally, CTC, proposed by Graves et al. [108], offers an implicit approach to balancing acoustic and linguistic aspects. CTC decodes unsegmented sequences by computing a conditional probability distribution over all possible label sequences, implicitly modeling label dependencies without explicit segmentation. By decoupling acoustic timing from label sequence prediction through its probabilistic path summation approach, CTC can be viewed as reconstructing both acoustic (timing, blanks) and linguistic (label identity) aspects simultaneously, contributing to robustness in speech sequence decoding.

Multi-modal integration enhances decoding robustness across speech types by combining complementary information from different pathways. For instance, the fusion of neural decoding and conventional language modeling in Herff et al.’s system [47] enables robust word and phone decoding performance across multiple subjects and sessions with varying electrode placements and task conditions. Similarly, the dual-path framework by Li et al. [36] overcomes the limitations of acoustic-only or linguistic-only decoding, demonstrating enhanced robustness across diverse speech types through the synergistic combination of acoustic naturalness and lexical content.

### 4.5 Interpretable Decoding Models for Neural Mechanism Validation

Interpretable decoding models are critical for validating neural mechanisms underlying speech by establishing links between neural activity and articulatory or linguistic components, thereby advancing both scientific understanding and clinical BCI optimization. Singh et al. (2025) [52] developed a sequence-to-sequence (Seq2Seq) model that integrates temporal convolutional networks, recurrent neural networks, and a linear readout layer to isolate phoneme identity probabilities, enabling interpretable mapping from neural data to phonemic sequences. This model outperformed linear baselines in phoneme prediction across patients and, through REO analysis, identified critical roles of ventral sensorimotor cortex, posterior superior temporal gyrus, and superior temporal sulcus in phonological processing—establishing region-to-phoneme mappings aligned with known neuroanatomical contributions to speech. Transfer learning with a shared recurrent layer further encoded subject-invariant articulatory information, producing latent feature embeddings that facilitated decoding in patients with variable electrode coverage and validated distributed neural mechanisms underlying speech. The use of PER provided an interpretable metric to quantify decoding precision at the phonemic level, bridging neural activity to articulatory and linguistic units.

Linear models have served as interpretable baselines for validating neural patterns, complementing more complex architectures. Luo et al. (2022) [7] noted that phoneme decoding studies using linear classifiers achieved accuracies ranging from 20% to over 70% with intracranial recordings, directly mapping neural features to articulatory or linguistic components. Beyond linear approaches, deep learning models such as convolutional neural networks (CNNs) mapped high gamma activity to speech features like mel-spectrograms, while recurrent neural networks and encoder-decoder frameworks improved word and sentence decoding accuracy. Speech synthesis approaches, which first map neural

[Figure 6]

- Figure 6: Design principles for generalizable language BCI experiments. Large cohorts, diverse tasks, multi-language coverage, rich annotations, anatomical metadata, standardization/open sharing, and longitudinal collection jointly support cross-subject generalization and more robust performance of neural-to-language decoding.

activity to intermediary representations (e.g., spectrotemporal features or vocal tract trajectories) before acoustic reconstruction via vocoders like WaveNet, enhance interpretability by elucidating neural contributions to speech production mechanisms and supporting clinical BCI optimization.

For covert speech, interpretable models have revealed discriminative neural features through visualization. Jiang et al. [127] used FAST-generated activation maps to identify distinct spatiotemporal speech-neural patterns in frontal and temporal regions during covert word production. Left hemisphere electrodes corresponding to Broca’s area and premotor regions showed pronounced activation, consistent with roles in speech motor planning and phonological processing, while right hemisphere frontal activations suggested involvement in prosodic or cognitive control mechanisms. Perutterance saliency maps further demonstrated reduced activation intensity with repeated covert rehearsal, indicating decreased cognitive and articulatory effort. Through spatial-temporal tokenization and transformer encoding, the model linked neural signals to articulatory components, supporting scientific understanding of covert speech neural dynamics and targeted clinical BCI optimization.

These interpretable decoding models—ranging from Seq2Seq architectures and linear baselines to visualization-driven frameworks—validate neural mechanisms by mapping neural features to articulatory and linguistic components, advancing both scientific knowledge and clinical translation of language BCIs. To synthesize these cross-cutting developments, Fig. 1 places representative frameworks by publication year within three lanes and annotates each with method tags (e.g., sequence/transformer decoders, CTC/LM assistance, streaming synthesis, or transfer-learning strategies), highlighting how design priorities have evolved across the field.

## 5 Unified Evaluation Framework for Speech Neuroprostheses

### 5.1 Experiment Design Protocol for Generalizable Language BCI Development

- As illustrated in Fig. 6, developing generalizable language BCIs, dataset design must prioritize critical characteristics that address the bottleneck of poor cross-subject generalization. A large cohort size is foundational, as demonstrated by studies involving 52 native English-speaking participants and 10 subjects in the Brain Treebank, which enable multisubject training and evaluation on unseen individuals. For instance, a multi-subject model trained on 15 participants generalized well to 43 unseen participants with a mean Pearson Correlation Coefficient (PCC) of 0.765 [39], highlighting that large cohorts mitigate data scarcity limitations of subject-specific models. Even smaller cohorts, such as the 4

participants in a Mandarin Chinese BCI study [35], contribute by focusing on language-specific linguistic structures, though larger cohorts remain critical for broader generalization.

Diverse speech tasks are essential to capture varied neural responses across different speech contexts. Datasets have included tasks like Auditory Repetition, Auditory Naming, Sentence Completion, Visual Reading, and Picture Naming, with 400 trials per participant [39], as well as reading monosyllabic characters (covering all Pinyin syllables) and variedlength sentences. Naturalistic paradigms, such as watching Hollywood movies to capture over 38,000 sentences [128], further enhance diversity by reflecting real-world language use, supporting models in generalizing beyond controlled laboratory tasks.

Multi-language coverage addresses linguistic variability, with datasets currently focusing on English and Mandarin Chinese, and plans to expand to Spanish. This diversity ensures models can adapt to distinct phonetic, syntactic, and semantic features across languages, a key step toward global BCI accessibility.

Rich linguistic annotations provide structured supervised signals to handle data variability. For example, 18 speech parameters (e.g., pitch, formants, loudness) extracted from spectrograms guide decoder training, while Mandarin BCI systems model initials, tones, and finals to decode syllables. The Brain Treebank enhances annotations with part-of-speech tags, dependency parses, word onsets/offsets, and scene labels [128], enabling fine-grained neural analysis of language processing.

To account for individual differences, datasets incorporate anatomical electrode metadata, such as MNI coordinates and brain region indices, allowing models to accommodate heterogeneous electrode layouts without subject-specific layers. Studies also report performance metrics per participant and annotate electrode locations using common brain atlases, ensuring robustness to variability in electrode placement and neural signal characteristics. Collectively, these dataset features—large cohorts, diverse tasks, multi-language coverage, rich annotations, and anatomical metadata—directly address generalization bottlenecks, paving the way for clinical translation of language BCIs.

In addition to these design principles, standardized data formats and open sharing practices are crucial for fostering collaboration and accelerating progress in the field. Adopting common data structures (e.g., Brain Imaging Data Structure (BIDS) for neuroimaging) and providing comprehensive documentation facilitate reproducibility and enable researchers to build upon existing datasets effectively. Moreover, incorporating longitudinal data collection can help capture neural signal variability over time, informing the development of adaptive decoding algorithms that maintain performance in real-world settings.

### 5.2 Limitations of Conventional Metrics and Role of Perceptual Evaluation

In the co-design view of Fig. 2, evaluation strategy is part of the software stack rather than a post hoc reporting detail: it determines whether improvements in decoder architecture or adaptation are detectable, comparable, and clinically meaningful.

Conventional objective metrics in speech neuroprosthesis evaluation, such as correlation coefficient (CC) and mel cepstral distortion (MCD), suffer from significant limitations and inconsistent usage, hindering meaningful cross-task comparisons [41]. Correlation coefficient, widely relied upon in many studies, is sensitive to analysis parameters like window size and focuses on co-variation rather than absolute signal differences, failing to capture perceptual intelligibility or naturalness. Similarly, MCD, which operates on mel-frequency cepstral coefficients (MFCCs) and is preferred over correlation-based metrics for weighting perceptually relevant features, ignores temporal alignment and can unfairly penalize perceptually good reconstructions with constant spectral offsets, thus not fully reflecting speech intelligibility. The inconsistent application of these metrics, coupled with variations in parameters and experimental conditions, leads to non-comparable evaluation results across different studies and datasets.

To address these limitations, perceptual evaluation metrics are essential as they anchor assessments to human auditory perception. Perceptual metrics include human-transcribed WER, character error rate (CER), PER, and mean opinion scores (MOS), which directly gauge intelligibility and naturalness. For instance, crowd-sourced human transcription tasks have been used to quantify perceptual WER and CER, which improve with decreased vocabulary size and correlate with MCD, providing a more accurate measure of true speech intelligibility beyond objective acoustic features [50]. In aphasic speech assessment, non-expert human evaluators using a 4-point Likert scale to rate clarity, fluidity, and prosody have yielded close-to-expert performance, addressing the unreliability of traditional objective measures like WER for irregular speech patterns [129]. MOS, as the subjective perceptual ground truth, is indispensable despite being time-consuming, as it reflects user experience and overcomes the limitations of purely objective metrics [41].

Perceptual evaluation metrics mitigate non-comparable results by aligning with human perception and enabling standardized benchmarking. By complementing objective metrics with human listener judgments—such as transcript matching, open transcription without vocabulary constraints, or Likert scale ratings—researchers can better contextualize

objective results with perceptual relevance and clinical translatability [37]. For example, combining objective metrics (e.g., MCD) with human-intelligibility scores has been shown to promote standardized assessment, ensuring that evaluation outcomes are clinically meaningful and user-centered. This integrated approach, which includes both objective and perceptual metrics, forms a critical part of establishing a unified evaluation framework for speech neuroprostheses [8].

### 5.3 Standardized Benchmark for Cross-Task and Cross-Language Comparison

The variability and lack of standardization in evaluation metrics across speech neuroprosthesis studies, particularly for continuous speech decoding, have hindered cross-task and cross-language comparisons [43]. While discrete speech decoding benefits from well-established metrics such as WER and PER that directly relate to semantic content, continuous voice synthesis lacks standardized metrics, with objective measures (e.g., mel-cepstral distortion, frequency band power correlation) often poorly corresponding to speech intelligibility, and subjective perceptual scores varying across studies. To address this, we propose a cross-language, cross-task standardized benchmark and define it explicitly as a direction-normalized, weighted composite score. Let xℓ,t,i,m denote the raw value of metric m for language ℓ, task t, and sample/session/participant index i; let [am,bm] be the pre-registered reference range for metric m, and let dm ∈ {+1,−1} indicate whether larger values are better (+1) or worse (−1). The normalized metric score zℓ,t,i,m ∈ [0,1] is

 

xℓ,t,i,m − am bm − am

min 1,max 0,

, dm = +1, min 1,max 0,

(3)

zℓ,t,i,m =

bm − xℓ,t,i,m bm − am



, dm = −1.

For metrics that must be mapped to perceptual quality (e.g., objective acoustic features to MOS), a calibrated model fθ is used to generate a perceptual proxy pˆℓ,t,i = fθ(xℓ,t,i,M

), which is then normalized using the same rule to obtain zℓ,t,i(p) . The task-language benchmark score is defined as

obj

Nℓ,t

Nℓ,t

1 Nℓ,t

1 Nℓ,t

zℓ,t,i,m, z¯ℓ,t(p) =

zℓ,t,i(p) , Bℓ,t =

wmz¯ℓ,t,m + wpz¯ℓ,t(p), (4)

z¯ℓ,t,m =

m∈Mt

i=1

i=1

where Nℓ,t is the number of evaluated samples/sessions, z¯ℓ,t(p) is the averaged normalized perceptual proxy (or observed MOS when available), and m∈M

wm + wp = 1. The global cross-language, cross-task (CLT) benchmark is then

t

βtBℓ,t, (5)

BCLT =

αℓ

t∈T

ℓ∈L

where ℓ∈L αℓ = 1 and t∈T βt = 1. In practice, the benchmark process therefore comprises (i) standardized data collection protocols, (ii) standardized task design, (iii) pre-registered metric ranges/weights, and (iv) an integrated

perceptual mapping model to ensure cross-task comparability.

Table 5 gives a default pre-registered benchmark template for representative task classes, explicitly specifying Mt, [am,bm], direction dm, and weights (objective wm and perceptual wp). These values should be fixed a priori and reported unchanged for cross-task comparison. Short-Time Objective Intelligibility (STOI) is included in the synthesis-task defaults. To make the default weights transparent and reproducible, we compute them using a structured swingweighting [130] rationale: for each task t, a “swing” for metric m is defined as improving it from the worst admissible level to the best admissible level within the pre-registered range [am,bm] (accounting for direction dm), while holding all other metrics at their worst levels. We then assign each metric an a priori swing-importance score sm that reflects its relative contribution to the task goal (content fidelity vs. usability vs. perceptual quality), and obtain the reported weights by normalization.

A key component of this benchmark is the adoption of uniform intermediate speech representations. For instance, Angrick et al. [131] demonstrated that segmenting neural data into spatial-temporal feature matrices and decoding onto standardized spectral features (logarithmic mel-scaled spectrograms) provides a consistent intermediate step, facilitating cross-task and cross-language comparisons. By combining this with a Wavenet vocoder trained independently on large external phonetic datasets (e.g., LJ-Speech corpus), synthesis quality is normalized, reducing variability introduced by individual neural data idiosyncrasies and enabling more reliable cross-task evaluations.

Table 5: Default parameterization template for the proposed cross-language, cross-task benchmark. For each task t, the listed weights satisfy m∈M

wm + wp = 1.

t

Task t Default Mt Metric m [am, bm] dm Weight

tdisc (copy/spelling) {WER, PER, Lon, Rcomm} WER [0, 1] −1 0.35 PER [0, 1] −1 0.20 Lon [0, 3] s −1 0.15 Rcomm [0, 30] wpm +1 0.10 p [1, 5] +1 wp = 0.20

tsynth (cont. synth.) {STOI, MCD, Rmel2 , Lon} STOI [0, 1] +1 0.25 MCD [0, 10] dB −1 0.20 Rmel2 [0, 1] +1 0.15 Lon [0, 3] s −1 0.10 p (MOS) [1, 5] +1 wp = 0.30

texpr (prosody) {Rf0, Reng, F1inton, ∆tsync} Rf0 [0, 1] +1 0.20 Reng [0, 1] +1 0.10 F1inton [0, 1] +1 0.20 ∆tsync [0, 0.5] s −1 0.15 p (MOS) [1, 5] +1 wp = 0.35

tconv (interactive) {WER, Lon, Sturn, Ustable} WER [0, 1] −1 0.20 Lon [0, 3] s −1 0.20 Sturn [0, 1] +1 0.25 Ustable [0, 1] +1 0.15 p (utility) [1, 5] +1 wp = 0.20

Notes: tdisc denotes discrete text-output tasks such as copy-typing, spelling, or prompted word/sentence transcription (closed or open vocabulary); tsynth denotes continuous speech synthesis/reconstruction tasks where the output is a waveform or acoustic features (e.g., mel-spectrogram) rendered to audio; texpr denotes expressivity/prosody tasks focusing on pitch, energy, intonation category, emphasis, and timing synchrony; tconv denotes interactive conversational tasks evaluated in turn-taking settings (participant-paced dialogue), emphasizing latency, turn success, and stability over time.

To solve the problem of non-comparable metrics, the benchmark integrates objective and subjective measures. Objective metrics such as Pearson correlation coefficients for spectrogram reconstruction and STOI scores can quantify technical performance, as shown by Angrick et al. [131] where these metrics demonstrated significantly better-than-chance performance across participants. For discrete outputs, PER and WER remain valuable, as evidenced by Card et al. [10] who reported mean WER as low as 2.5% in copy tasks and 3.7% in conversational mode, with these objective metrics showing correspondence to participant-reported perceptual accuracy (e.g., correct, mostly correct, incorrect). Importantly, such integrated approaches, which relate objective decoding metrics to perceptual intelligibility and communication efficacy, have been validated in speech synthesis and automatic speech recognition research, supporting their feasibility in speech neuroprosthetics.

The benchmark process should also standardize task design, including both controlled tasks (e.g., instructed-delay copy tasks) and ecologically valid scenarios (e.g., participant-paced conversational modes), as implemented in Card et al. [10] to enable cross-task evaluation. Additionally, leveraging advances in automated speech recognition to transcribe synthesized speech and compare with ground truth, alongside developing metrics for paralinguistic features like intonation, could further enhance benchmark comprehensiveness. By establishing such a framework, the field can objectively track progress, compare decoding algorithms across languages and tasks, and accelerate clinical translation.

### 5.4 Metrics for Naturalistic Expressivity and Conversational Utility

Naturalistic expressivity and conversational utility in speech neuroprostheses demand metrics that extend beyond basic intelligibility, capturing prosodic nuances, temporal dynamics, and expressive features critical for real-world communication.

Prosodic accuracy, which includes elements like pitch, loudness, intonation, and timbre, is vital for conveying emotional tone and speaker identity. Objective metrics for prosodic accuracy include mel-spectrogram correlation (R²), which quantifies fine-grained time-frequency alignment with ground truth speech; a dual-pathway decoding framework achieved a high mel-spectrogram R² of 0.824 ± 0.029, comparable to speech degraded by 0dB additive noise, indicating strong preservation of prosodic details such as pitch and timbre [36]. Source features like pitch (f0) and loudness, encoded within frameworks such as SPARC, directly represent prosodic elements critical for expressive speech [53]. Subjective evaluation via MOS further assesses human perception of expressiveness, with one system achieving a MOS of 3.956 ± 0.173 on a 5-point scale, rated near "excellent" for expressivity [36]. Additionally, decoding paralinguistic features such as statement versus question intonation and word emphasis has been demonstrated, enabling naturalistic prosodic variation in synthesized speech.

Conversational latency, defined as the time from speech intent to audible output, is crucial for maintaining natural conversation flow, as delays longer than a few seconds can disrupt interaction and cause frustration. Key latency metrics include the onset delay between speech attempt and decoding output, processing chunk size, and inference latency. For example, a system using recurrent neural network transducer (RNN-T) models achieved latencies as low as 1.12 s for speech synthesis and 1.01 s for text decoding, with 80-ms processing chunks and median inference latency of 12 ms, enabling seamless incremental speech production [46]. Another system demonstrated near-instantaneous latency of 25 ms, similar to the delay of an able-bodied speaker hearing their own voice, highlighting progress toward real-time conversational dynamics [112]. However, some frameworks still operate at 2-3x real-time latency, necessitating engineering focus to reduce latency for improved conversational utility.

Expressive feature decoding encompasses the extraction of semantic, syntactic, and speaker-specific features enabling nuanced communication. Semantic decoding, for instance, has been achieved with multivariate pattern analysis, reaching an average accuracy of 21% across participants for word-level semantic features (chance level 10%), demonstrating the ability to capture meaning beyond lexical content [34]. Bimodal decoding models, such as those enabling simultaneous streaming speech synthesis and text decoding, have shown tight temporal synchrony (median absolute timing difference 170-185 ms between text and speech onset), enhancing expressivity through synchronized multimodal outputs [46]. Frameworks like SPARC incorporate speaker identity embedding, disentangled from articulatory features, allowing control of voice texture and accent preservation, vital for naturalistic expressivity. Standard linguistic metrics like PER and WER further quantify expressive feature decoding accuracy, with one system reporting WER of 18.9% ± 3.3% and PER of 12.0% ± 2.5%, reflecting advances in semantic and syntactic precision [36]. Collectively, these metrics—prosodic accuracy via acoustic correlation and MOS, conversational latency via onset delay and processing speed, and expressive feature decoding via semantic accuracy and bimodal synchrony—comprehensively capture real-world communication utility beyond basic intelligibility.

### 5.5 Long-Term Performance and Stability Evaluation Protocols

Evaluating long-term decoding stability requires protocols that jointly report signal retention, performance drift, and adaptation burden. Current evidence includes both encouraging longitudinal stability and persistent recalibration requirements.

Positive studies report multi-month operation in selected participants, including 3-month ECoG use without retraining [21], online synthesis with session gaps of months [22], 8.4-month intracortical speech decoding with high accuracy over repeated sessions [10], and one-year signal-stability analyses in chronic ECoG language BCI [114]. Extended cursor-control results (>400 days) further indicate that stable use is possible under structured follow-up [113].

Counter-evidence indicates that non-stationarity remains operationally significant: >400-day cursor studies relied on frequent retraining during calibration blocks [113], long-duration speech use still required periodic recalibration [10], and earlier speech-BCI reports and reviews caution that across-session robustness cannot be assumed [111, 19, 20, 43]. Home-use demonstrations are promising [21, 37], but unattended operation without specialist support remains to be established.

Overall, current longitudinal studies indicate partial clinical readiness rather than definitive stability, supporting adaptive closed-loop protocols while highlighting remaining translational uncertainty.

## 6 Translational Pathways and Ethical Design for Clinical Speech Neuroprostheses

- As summarized in Fig. 7, this section frames clinical translation as a gated process in which user agency, verifiable metrics, MVP definition, ethical shared control, multimodal utility, and regulatory validation must advance together for deployment readiness.

### 6.1 Operationalizing User Agency Through Designable Functions

User agency in clinical speech neuroprostheses can be operationalized through specific designable functions that address ethical concerns about automated output shaping by centering user volitional control. As the first translational gate in Fig. 7, these functions include decoder start-stop control, message confirmation, and expressive style modulation, each contributing to ensuring users retain authority over their communication.

Decoder start-stop control ensures users govern when decoding initiates and terminates, preventing unintended output. This is achieved via speech-detection mechanisms: explicit modules trained to identify volitional speech attempts [122] or implicit detection within decoding models, such as the RNN-T architecture, which enables continuous operation with implicit start-stop detection from neural signals. In addition, decoder gating can be augmented with peripheral

[Figure 7]

- Figure 7: Translational gate framework of language BCIs for clinical speech neuroprostheses. The funnel depicts sequential gates from laboratory innovation to clinical deployment, spanning user agency, verifiable real-world metrics, MVP readiness, ethical shared control, multimodal utility, and regulatory validation. The roadmap highlights aligned future directions, emphasizing that clinical adoption requires progress across all gates, not optimization of a single metric.

biosignals such as electromyography (EMG), for example using a deliberate EMG switch or push-to-talk gesture as an explicit user-controlled start signal and a rapid veto/kill-switch to halt synthesis [132, 133]. Such hybrid gating or switching schemes can reduce false positives by requiring concordant volitional evidence (e.g., neural intent plus EMG activation) before allowing output, and by supporting reliable transitions between control modes [134]. Advances in EMG classification further support robust detection of user-triggered control signals for start/stop gating [135, 136]. Such systems distinguish intended speech from internal monologue by gating decoding through speech-detection algorithms, aligning with executory control (go-command) and veto control to avoid unintentional speech and halt production if needed [121]. For example, one system demonstrated minimal false-positive synthesis (3 out of 100 non-speech attempts) and no premature decoding before user-initiated “GO” cues, confirming respect for user-driven initiation [46].

Message confirmation mechanisms allow users to verify outputs before or during synthesis, mitigating errors and enhancing ownership. Real-time visual display of decoded text enables users to read and confirm accuracy, as implemented in a system with incremental text-to-speech synthesis where decoded text is confirmed before speech generation. Additionally, simultaneous brain-to-text decoding facilitates verification of synthesized speech accuracy, providing a form of implicit message confirmation.

Expressive style modulation empowers users to shape communicative nuances, aligning outputs with personal identity. This includes customization of speech synthesizer voice (e.g., using pre-ALS voice clips) and modulation of paralinguistic features like intonation (e.g., rising pitch for questions), word emphasis, and even melody [112]. For instance, a brain-to-voice neuroprosthesis implemented parallel binary classifiers to decode user intent for pitch or emphasis modulation, enabling closed-loop control over expressive features [37]. Beyond vocal features, facial animation can accompany speech synthesis to express non-verbal gestures, further enhancing expressive capacity [8]. Customization of avatars or communication parameters (e.g., language model adaptivity) also contributes to user agency by aligning the system with individual preferences.

### 6.2 Translational Priorities with Verifiable Performance Metrics

Translational priorities for clinical speech neuroprostheses necessitate verifiable performance metrics to address bottlenecks of insufficient real-world utility, with key focuses on closed-loop audio feedback latency, long-term stability,

and interoperability with personal computer systems. This corresponds to the verifiable real-world metrics gate in Fig. 7. For long-term stability, evidence is mixed rather than uniformly positive. Positive reports include 3-month ECoG operation without retraining [21], online synthesis using months-old training data with session-wise recalibration [22], 8.4-month high-accuracy intracortical use [10], and one-year high-gamma stability analyses in chronic language BCI [114]. In contrast, other reports indicate continuing adaptation burdens, including frequent retraining or calibration to track neural drift [113, 1, 43]. Thus, existing data indicate feasibility of sustained operation in selected users, while routine no-recalibration deployment across diverse users remains to be established.

Closed-loop audio feedback latency is essential for natural communication, and advancements in this area are notable. While in 2023, Luo et al. [21] reported a median system latency of 1.24 seconds between speech offset and decoding registration, more recent progress has achieved lower latencies: in 2024, Card et al. [10] noted that their intracortical neuroprosthesis operated in real time with decoding latency at or below 80 ms per phoneme, supporting near-real-time feedback. Additionally, in 2024, Angrick et al. [22] implemented a closed-loop architecture with latency compatible with online synthesis and playback, using delayed auditory feedback after each word to avoid interference, which was deemed acceptable for the participant with ALS.

Interoperability with personal computer control systems is vital for integrating language BCIs into daily life. In 2023, Luo et al. [21] showed that their ECoG-based system could control various computer applications and external devices in real time, while in 2015, Herff et al. [47] noted that their Brain-to-Text approach, though evaluated offline, is well-suited for real-time online application on desktop computers. In 2024, Angrick et al. [22] demonstrated interoperability through communication board control, and in 2024, Card et al. [10] integrated their neuroprosthesis with personal computers via Bluetooth keyboard functionality, enabling activities like email writing and integration with eye tracking for user confirmation.

To ensure consistent evaluation of these metrics, in 2025, Wu et al. [41] proposed a unified metric using a Random Forest regressor that combines STOI and MCD to predict human-rated MOS, addressing the limitations of individual objective metrics. This validated model provides a verifiable performance metric that correlates with subjective perception, enabling standardized cross-task benchmarking and addressing bottlenecks in real-world utility by facilitating reliable assessment of language BCI waveform reconstruction quality.

### 6.3 MVP Profiles for Early Clinical Deployment

Because communication reliability and speech naturalness place different demands on hardware and algorithms, an actionable translational strategy is to define use-case-specific MVP stacks rather than seeking a single universal architecture. This operationalizes the MVP readiness gate in Fig. 7 and is also consistent with the organizing logic of Fig. 1, whose lane structure emphasizes that clinically relevant progress depends on jointly improving decoding performance, robustness, calibration burden, and deployment feasibility rather than optimizing a single benchmark metric.

- • ALS home communication (reliability-first MVP): prioritize ECoG or SEEG pathways with clinically routine implantation routes and lower day-to-day recalibration burden. Use explicit start/stop gating, confirmation or veto control, and a simplified high-frequency lexicon or phrase bank to reduce unintended output and caregiver load [21, 22, 122, 37]. Practical endpoints should include stable multi-week operation, predictable latency, and low maintenance overhead.
- • High-naturalness conversational speech (fidelity-first MVP): prioritize MEA or high-density µECoG when the target is rich prosody, voice identity preservation, and low-latency synthesis. A recommended chain is neural decoding to articulatory intermediate to acoustic synthesis (vocoder/voice model), accepting higher channel density and calibration requirements [1, 112, 28, 53, 36]. Practical endpoints should include near-real-time feedback and robust control of expressive features (intonation/emphasis).

This two-profile framing clarifies that clinical deployment decisions should be benchmarked against scenario-specific success criteria, not only pooled average decoding metrics.

### 6.4 Ethical Considerations in Shared Control and Output Ownership

Shared control between users and automated decoding systems in language BCIs introduces nuanced ethical dynamics, as demonstrated by systems where automated suggestions are paired with user oversight. This directly maps to the ethical shared-control gate in Fig. 7. In 2023, Willett et al. [1] described a framework where neurally decoded words appear in real time as the language model’s best guess, with the user retaining control to finalize outputs via a button press. This interactive process embodies shared control, balancing the efficiency of automated decoding (e.g., neural

RNNs and language models) with user agency in confirming or rejecting suggestions. Similarly, in 2023, Metzger et al. [50] highlighted that their multimodal neuroprosthesis, which decodes neural activity into text, speech, and avatar animations, relies on the participant’s active silent speech attempts to drive decoding, ensuring outputs reflect intended communicative goals. Such designs underscore the ethical imperative to prioritize user control alongside system efficiency, as over-automation diminish user autonomy, while overly restrictive user oversight could hinder communication speed.

The distinction between user ownership of synthetic speech and moral responsibility for outputs hinges on clarifying which elements of the output stem from user intent versus automated processing. In 2024, Cho et al. [53] addressed this through the SPARC framework, which disentangles speaker-agnostic articulatory features (controlled by the user’s neural intent) from speaker-specific voice texture (handled by automated encoders). This separation enables clear attribution: users retain ownership of content via interpretable articulatory commands, while moral responsibility for outputs is linked to these intentional articulatory features rather than automated synthesis components. 2023, Metzger et al. [50] further emphasized ownership by personalizing synthetic speech to the participant’s pre-injury voice and animating facial avatars to reflect intended emotional expressions, grounding outputs in the user’s identity.

Design strategies to balance efficiency and user control must address both technical and ethical dimensions. In 2023, Willett et al. [1] noted that retraining decoders daily improves adaptation to neural changes, but unsupervised adaptation could reduce user burden, suggesting that adaptive algorithms should prioritize user convenience without sacrificing control. In 2023, Metzger et al. [50] introduced complementary output modalities (text, speech, avatar) and early stopping for silence detection, allowing users to select context-appropriate outputs and maintain control over communication flow. In 2024, Cho et al. [53] emphasized the role of interpretable articulatory features in shared control, making the decoding process transparent and modifiable, thereby empowering users to correct automated errors. Additionally, in 2025, Li et al. [36] highlighted risks of generative model biases (e.g., Parler-TTS favoring linguistically probable outputs), advocating for dual-pathway architectures that integrate acoustic and linguistic decoding to mitigate such biases while preserving user-specific vocal identity.

While some studies focus primarily on technical performance—such as Feng et al. [35], who developed a Mandarin brain-to-sentence decoder without explicit ethical analysis—these examples collectively underscore that ethical design in shared control requires intentional integration of user agency, transparent decoding mechanisms, and personalized output to ensure synthetic speech remains an extension of the user’s intent and identity.

### 6.5 Multi-Modal BCI Integration for Comprehensive Communication

Combining speech decoding with cursor control and other BCI modalities addresses critical limitations of single-modal systems by leveraging the complementary strengths of each approach, thereby enhancing real-world utility. In Fig. 7, this corresponds to the multimodal utility gate required for broader clinical communication tasks. Traditional non-language BCIs, such as those using P300, motor imagery, or steady-state visually evoked potential, cannot match the speed and flexibility of spoken communication. Language BCIs, by contrast, offer a more efficient and expressive channel through real-time synthesis, while the integration of cursor control provides an additional means of precise computer interaction or device manipulation. This multi-modal approach not only expands the range of communication and control capabilities but also accommodates varied user needs in dynamic environments.

Evidence for shared cortical substrates supporting multi-modal BCI functions is increasingly robust, with studies demonstrating that overlapping neural regions can support both speech decoding and motor control. For instance, an individual with tetraplegia successfully used ECoG signals recorded from the left sensorimotor cortex to operate 3D cursor movement by associating attempted movements (e.g., thumb, elbow, wrist flexion/extension) with cursor directions, while the same neural signals simultaneously supported speech movements [137]. Similarly, recent research has shown that speech can be decoded from microelectrode Utah arrays implanted in dorsal motor areas, indicating that these regions may subserve multiple BCI modalities [7]. High-density recordings from peri-Sylvian cortices, including vSMC and STG, have further revealed that these areas, which are associated with speech production and auditory feedback, can support accurate decoding of complex speech sequences. This finding points to their potential as shared substrates for speech and other control functions, such as cursor movement [9].

The modular nature of BCI systems facilitates multi-modal integration. A typical synthesis-based language BCI comprises stages of neural signal recording, feature extraction, speech decoding, and audio synthesis, a framework that can be extended to incorporate additional modalities such as cursor control by integrating parallel decoding pathways. Advanced computational approaches, such as transfer learning across participants and sentence sets, enhance adaptability by enabling networks pretrained on one task (e.g., speech decoding) to improve performance on another (e.g., cursor control), reflecting multi-task learning capacities. Furthermore, decoding lexical semantic information—such as word meanings—from neural activity, as demonstrated using SEEG recordings with 21% accuracy (vs. 10% chance) during

spontaneous conversation, offers opportunities to combine semantic decoding with phoneme-focused speech models, potentially producing smoother and more accurate communication [34].

The translational benefits of multi-modal functionality are substantial. First, shared cortical recording sites reduce the need for extensive implantations, enhancing safety and feasibility for clinical translation. This is supported by evidence that ECoG implants in individuals with late-stage ALS remain stable and maintain high performance over long periods, further reinforcing the clinical viability of multi-modal systems. Second, multi-modal BCIs address real-world usability by providing redundant or complementary communication channels: speech synthesis enables rapid expressive communication, while cursor control offers precise manipulation for tasks requiring fine motor coordination. Finally, integrating diverse modalities—such as speech, cursor movement, and semantic decoding—enhances overall system robustness and user satisfaction, both critical for successful clinical adoption. Collectively, these advances position multi-modal BCI integration as a key pathway toward comprehensive communication restoration for individuals with speech impairments.

### 6.6 Clinical Trial Design for Speech Neuroprosthesis Validation

Participant selection criteria for speech neuroprosthesis clinical trials must balance clinical relevance and feasibility, focusing on individuals with speech impairment while ensuring safety and meaningful outcomes. This subsection addresses the regulatory validation gate in Fig. 7, where study design determines whether promising prototypes can generate approval-relevant evidence. For example, a study included a person with bulbar-onset ALS who retained limited orofacial movement and vocalization ability despite being unable to speak intelligibly, highlighting the importance of recruiting participants with residual speech-related motor function [1]. Similarly, the BrainGate2 pilot clinical trial enrolled participants with tetraplegia and residual speech ability to safely explore neural decoding performance [55], while another BrainGate2 participant with severe motor impairment (tetraplegic with dysarthria) demonstrated feasibility in a highly impaired population [113]. Surveys of potential users, including those with ALS and spinal cord injury, highlight that willingness to undergo implantation depends on the system meeting priorities like restoring communication with sufficient accuracy (>90%) [43].

Outcome measures in such trials prioritize user experience by focusing on metrics that reflect real-world communication efficacy and user preferences. Performance evaluations have included both vocalized and silent (mouthing) speech attempts, with participants reporting preferences for silent speech due to reduced fatigue. Phoneme classification accuracy (e.g., 33.9% across 39 phonemes, chance 6%) [55] and broader metrics like WER, PER, and communication rate (words per minute) are critical, as they directly relate to the user’s ability to communicate effectively.

Long-term safety monitoring and decoder stability are essential for regulatory approval, addressing neural nonstationarities and device longevity. Strategies include using RNN architectures with day-specific input layers and rolling feature adaptation to handle across-day and within-day neural changes. Implanted sensors like Utah arrays and ECoG grids have demonstrated stable recordings for months to years (e.g., up to 7 years for Utah arrays, 3 years for ECoG), supported by adaptive algorithms that maintain performance without frequent recalibration. Clinical trials such as BrainGate2 operate under U.S. Food and Drug Administration (FDA) IDE and institutional review board (IRB) approvals, with monitoring extending to home environments to assess real-world reliability.

These design elements directly address barriers to regulatory approval by demonstrating safety, efficacy, and user-centric outcomes. For example, the use of IDE-approved protocols ensures compliance with regulatory standards, while evidence of stable decoding performance, implant safety, and meaningful communication output helps meet regulatory expectations of efficacy. Ongoing trials, including BrainGate2, implement these principles by exploring suboptimal cortical areas to de-risk future trials targeting ventral speech cortex, demonstrating multi-modal control (speech and cursor) from a single implant, and planning commercial trials with fully wireless sensors. Despite promising results, further validation in larger cohorts remains necessary to establish clinical viability.

## 7 Future Directions

- As summarized in Fig. 8, future research in intracranial language BCIs should prioritize a coordinated roadmap that links hardware and algorithmic progress to real-world clinical deployment. A foundational systems priority is recording-hardware and implant co-design. Beyond improving acute signal quality, future electrode development should target coverage–resolution co-optimization (e.g., hybrid macro+µECoG and surface+depth strategies), chronic biocompatibility and low-impedance interface stability, fully implanted wireless architectures with onboard preprocessing, and high-channel-count active multiplexed arrays that preserve bandwidth within thermal and power limits. Platforms that support both decoding and causal stimulation/functional mapping may also enable adaptive closed-loop speech systems.

[Figure 8]

- Figure 8: Future directions for intracranial language BCIs. A coordinated roadmap highlighting six interdependent priorities: hardware and implant co-design, representative multilingual datasets, adaptive/interpretable decoding, standardized clinical evaluation, multicenter validation and deployment, and open data/standards for reproducible progress.

These hardware advances should be evaluated with deployment-relevant endpoints such as infection risk, packaging durability, setup burden, and home-environment robustness.

On the data side, a foundational priority is the development of larger, multi-language, and clinically representative datasets to improve generalization across populations and linguistic contexts [138, 139]. Current evidence is dominated by English-speaking participants and highly controlled tasks, which limits external validity [140]. Expanding data collection to include tonal and morphologically diverse languages, broader age ranges, and heterogeneous etiologies of speech impairment will enhance both scientific rigor and translational relevance [141].

- At the model-development level, adaptive and interpretable decoding approaches remain a central priority. Although deep learning approaches have substantially improved decoding performance, black-box behavior can undermine user trust, calibration transparency, and ethical accountability. Future systems should therefore combine high performance with interpretable intermediate representations (e.g., articulatory or phonological features), user-correctable outputs, richer control of prosody/paralinguistic expression (including tonal cues where relevant), and longitudinal adaptation strategies that reduce daily recalibration burden while preserving user agency [142]. Improving reliable covert/imaginedspeech decoding under weaker and less time-locked neural signals is another important frontier for clinically flexible communication [99].

Beyond model optimization, the field would benefit from broader adoption of standardized evaluation frameworks that capture clinically meaningful outcomes rather than isolated model metrics. In addition to accuracy or WER, studies should report latency, calibration time, robustness across sessions, failure modes, user workload, and communication utility in ecologically valid tasks [139]. Cross-language and cross-task benchmarks are an important starting point, but they must be harmonized across centers to support fair comparison and cumulative progress [140].

At the translational stage, rigorous multi-center clinical validation is necessary to establish safety, efficacy, and durability. Many influential studies remain single-participant or single-center demonstrations. Larger prospective trials with standardized protocols, long-term follow-up, and diverse participant demographics will be essential for clarifying which combinations of recording modality, decoding architecture, and shared-control strategy are clinically viable and scalable for regulatory pathways [139, 99]. These trials should also evaluate multimodal use cases (e.g., speech plus cursor control or semantic assistance) and home-use performance, because real-world utility may depend on redundancy and interoperability rather than copy-task accuracy alone.

Across all of these priorities, open sharing of data is not only beneficial but necessary for the field’s progress. Intracranial language BCI research is highly interdisciplinary and resource-intensive, requiring collaboration across neuroscience, engineering, clinical neurology, rehabilitation, linguistics, and ethics. Timely sharing of de-identified datasets, metadata, annotations, and benchmark splits can improve cross-task comparability and help investigators, clinicians, and institutions build on prior work more efficiently [143], including in lower-resource settings. In parallel with appropriate protections for participant privacy and sensitive neural data, greater openness in data standards, protocols, evaluation criteria, code, and reporting practices will improve reproducibility, reduce duplication of effort, and accelerate equitable clinical translation [143, 138].

By advancing these priorities in parallel, intracranial language BCI research can move beyond isolated technical milestones toward robust, reproducible, and widely accessible communication neuroprostheses for individuals with severe speech impairments.

## 8 Conclusion

This review summarizes the current trajectory of intracranial language BCIs for speech restoration across neural mechanisms, recording technologies, decoding algorithms, evaluation strategies, and translational design. Overall, the field is progressing from proof-of-concept demonstrations toward more clinically meaningful communication systems, but key bottlenecks remain. At the neural level, intracranial evidence supports a mixed organization with partially somatotopic articulatory coding, dorsal–ventral stream specialization, and frequency-specific dynamics across overt, mimed, and imagined speech. For covert and imagined speech, decoding is increasingly feasible in constrained settings, yet clinically reliable open-vocabulary decoding remains unresolved. At the systems level, recording modalities continue to present trade-offs in coverage, resolution, invasiveness, and long-term robustness. Multi-month stability has been demonstrated for both ECoG and intracortical approaches, but recalibration burden and setup dependence remain important barriers to routine longitudinal use. In parallel, advances in sequence models, transformers, and articulatory intermediates have improved decoding performance, while language priors (including LLM-based components) may enhance fluency and error correction; however, intent preservation, latency, bias, and privacy risks require continued safeguards and prospective monitoring.

Future progress will depend on standardized and longitudinal evaluation, harmonized benchmarks, explicit reporting of recalibration burden, and larger multi-center clinical cohorts. User agency, shared-control transparency, and multimodal integration should remain central translational priorities, together with prospective safety analyses for language-priorassisted decoding. In summary, clinically viable intracranial language BCIs are increasingly plausible, but broader translation will require larger and more diverse datasets, adaptive and interpretable models, rigorous cross-center validation, and transparent data-sharing and reporting practices to support reproducibility and equitable deployment. Sustained open sharing of de-identified datasets, annotations, benchmark definitions, code, and negative results will further strengthen cross-center learning and accelerate responsible clinical translation.

## Acknowledgments

This work was supported by The Hong Kong Polytechnic University Start-up Fund (Project ID: P0053210), The Hong Kong Polytechnic University Faculty Reserve Fund (Project ID: P0053738), an internal grant from The Hong Kong Polytechnic University (Project ID: P0048377), The Hong Kong Polytechnic University Departmental Collaborative Research Fund (Project ID: P0056428), The Hong Kong Polytechnic University Collaborative Research with Worldleading Research Groups Fund (Project ID: P0058097) and Research Grants Council Collaborative Research Fund (Ref: C5033-24G).

## Author Contributions

D.H. and N.W. contributed to the conceptualization of the study. D.H., W.T.S., and N.W. performed the investigation. D.H. and N.W. drafted the original manuscript. All authors (D.H., W.T.S., and N.W.) reviewed and edited the manuscript. W.T.S. and N.W. acquired funding for the study and supervised the research.

## References

- [1] Francis R Willett, Erin M Kunz, Chaofei Fan, Donald T Avansino, Guy H Wilson, Eun Young Choi, Foram Kamdar, Matthew F Glasser, Leigh R Hochberg, Shaul Druckmann, et al. A high-performance speech neuroprosthesis. Nature, 620(7976):1031–1036, 2023.

- [2] Ujwal Chaudhary, Ioannis Vlachos, Jonas B Zimmermann, Arnau Espinosa, Alessandro Tonin, Andres JaramilloGonzalez, Majid Khalili-Ardali, Helge Topka, Jens Lehmberg, Gerhard M Friehs, et al. Spelling interface using intracortical signals in a completely locked-in patient enabled via auditory neurofeedback training. Nature communications, 13(1):1236, 2022.
- [3] Pegah Masrori and Philip Van Damme. Amyotrophic lateral sclerosis: a clinical review. European journal of neurology, 27(10):1918–1929, 2020.
- [4] Piera Pasinelli and Robert H Brown. Molecular biology of amyotrophic lateral sclerosis: insights from genetics. Nature Reviews Neuroscience, 7(9):710–723, 2006.
- [5] Ezgi Tiryaki and Holli A Horak. Als and other motor neuron diseases. CONTINUUM: Lifelong Learning in Neurology, 20(5):1185–1207, 2014.
- [6] Adriano Chiò, Marco Pagani, Federica Agosta, Andrea Calvo, Angelina Cistaro, and Massimo Filippi. Neuroimaging in amyotrophic lateral sclerosis: insights into structural and functional changes. The Lancet Neurology, 13(12):1228–1240, 2014.
- [7] Shiyu Luo, Qinwan Rabbani, and Nathan E Crone. Brain-computer interface: applications to speech decoding and synthesis to augment communication. Neurotherapeutics, 19(1):263–273, 2022.
- [8] Alexander B Silva, Kaylo T Littlejohn, Jessie R Liu, David A Moses, and Edward F Chang. The speech neuroprosthesis. Nature Reviews Neuroscience, 25(7):473–492, 2024.
- [9] Joseph G Makin, David A Moses, and Edward F Chang. Machine translation of cortical activity to text with an encoder–decoder framework. Nature neuroscience, 23(4):575–582, 2020.
- [10] Nicholas S Card, Maitreyee Wairagkar, Carrina Iacobacci, Xianda Hou, Tyler Singer-Clark, Francis R Willett, Erin M Kunz, Chaofei Fan, Maryam Vahdati Nia, Darrel R Deo, et al. An accurate and rapidly calibrating speech neuroprosthesis. New England Journal of Medicine, 391(7):609–618, 2024.
- [11] Stéphane d’Ascoli, Corentin Bel, Jérémy Rapin, Hubert Banville, Yohann Benchetrit, Christophe Pallier, and JeanRémi King. Towards decoding individual words from non-invasive brain recordings. Nature Communications, 16(1):10521, 2025.
- [12] Yun Zhao, Bin Jiang, Yanying Yan, Dongyi He, Xiaoling Zhang, Shuaidong Zou, Yijie Zhu, Xiyue Hu, and Guanghui Xie. Rgftslanet: A cross-subject classification model for decoding eeg-based motor imagery tasks. In 2025 Cross Strait Radio Science and Wireless Technology Conference (CSRSWTC), pages 1–4. IEEE, 2025.
- [13] Jiahao Lu, Hongjie Yan, Chunqi Chang, and Nizhuan Wang. Comparison of machine learning and deep learning approaches for decoding brain computer interface: an fnirs study. In International Conference on Intelligent Information Processing, pages 192–201. Springer, 2020.
- [14] Bin Jiang, Xiangkai Wang, Dongyi He, Siyu Cheng, Maoyu Liao, Duoqian Miao, Qingling Xia, Yun Zhao, and Gen Li. A comprehensive review of deep learning for motor imagery eeg: From healthy subjects to patients. Biomedical Signal Processing and Control, 117:109680, 2026.
- [15] Yueyang Li, Weiming Zeng, Wenhao Dong, Di Han, Lei Chen, Hongyu Chen, Zijian Kang, Shengyu Gong, Hongjie Yan, Wai Ting Siok, et al. A tale of single-channel electroencephalogram: Devices, datasets, signal processing, applications, and future directions. IEEE Transactions on Instrumentation and Measurement, 2025.
- [16] Dongyi He, Shiyang Li, Bin Jiang, and He Yan. Spec2volcamu-net: a spectrogram-to-volume model for eeg-tofmri reconstruction based on multi-directional time–frequency convolutional attention encoder and vision-mamba u-net. Journal of Neural Engineering, 22(5):056042, 2025.
- [17] Dongyi He, Bin Jiang, Kecheng Feng, Luyin Zhang, Ling Liu, Yuxuan Li, Yun Zhao, and He Yan. Non-invasive reconstruction of intracranial eeg across the deep temporal lobe from scalp eeg based on conditional normalizing flow. arXiv preprint arXiv:2603.03354, 2026.
- [18] Miao Cao, Daniel Galvis, Simon J Vogrin, William P Woods, Sara Vogrin, Fan Wang, Wessel Woldman, John R Terry, Andre Peterson, Chris Plummer, et al. Virtual intracranial eeg signals reconstructed from meg with potential for epilepsy surgery. Nature communications, 13(1):994, 2022.
- [19] Eric C Leuthardt, Gerwin Schalk, Jonathan R Wolpaw, Jeffrey G Ojemann, and Daniel W Moran. A brain– computer interface using electrocorticographic signals in humans. Journal of neural engineering, 1(2):63, 2004.
- [20] Eric C Leuthardt, Charles Gaona, Mohit Sharma, Nicholas Szrama, Jarod Roland, Zac Freudenberg, Jamie Solis, Jonathan Breshears, and Gerwin Schalk. Using the electrocorticographic speech network to control a brain–computer interface in humans. Journal of neural engineering, 8(3):036004, 2011.

- [21] Shiyu Luo, Miguel Angrick, Christopher Coogan, Daniel N Candrea, Kimberley Wyse-Sookoo, Samyak Shah, Qinwan Rabbani, Griffin W Milsap, Alexander R Weiss, William S Anderson, et al. Stable decoding from a speech bci enables control for an individual with als without recalibration for 3 months. Advanced Science, 10(35):2304853, 2023.
- [22] Miguel Angrick, Shiyu Luo, Qinwan Rabbani, Daniel N Candrea, Samyak Shah, Griffin W Milsap, William S Anderson, Chad R Gordon, Kathryn R Rosenblatt, Lora Clawson, et al. Online speech synthesis using a chronically implanted brain–computer interface in an individual with als. Scientific reports, 14(1):9617, 2024.
- [23] Kathrin Müsch, Kevin Himberger, Kean Ming Tan, Taufik A Valiante, and Christopher J Honey. Transformation of speech sequences in human sensorimotor circuits. Proceedings of the National Academy of Sciences, 117(6):3203–3213, 2020.
- [24] Gregg A Castellucci, Christopher K Kovach, Matthew A Howard III, Jeremy DW Greenlee, and Michael A Long. A speech planning network for interactive language use. Nature, 602(7895):117–122, 2022.
- [25] Ran Wang, Xupeng Chen, Amirhossein Khalilian-Gourtani, Leyao Yu, Patricia Dugan, Daniel Friedman, Werner Doyle, Orrin Devinsky, Yao Wang, and Adeen Flinker. Distributed feedforward and feedback cortical processing supports human speech production. Proceedings of the National Academy of Sciences, 120(42):e2300255120, 2023.
- [26] Timothée Proix, Jaime Delgado Saa, Andy Christen, Stephanie Martin, Brian N Pasley, Robert T Knight, Xing Tian, David Poeppel, Werner K Doyle, Orrin Devinsky, et al. Imagined speech can be decoded from low-and cross-frequency intracranial eeg features. Nature communications, 13(1):48, 2022.
- [27] Aurélie de Borman, Benjamin Wittevrongel, Ine Dauwe, Evelien Carrette, Alfred Meurs, Dirk Van Roost, Paul Boon, and Marc M Van Hulle. Imagined speech event detection from electrocorticography and its transfer between speech modes and subjects. communications biology, 7(1):818, 2024.
- [28] Gopala K Anumanchipalli, Josh Chartier, and Edward F Chang. Speech synthesis from neural decoding of spoken sentences. Nature, 568(7753):493–498, 2019.
- [29] Josh Chartier, Gopala K Anumanchipalli, Keith Johnson, and Edward F Chang. Encoding of articulatory kinematic trajectories in human speech sensorimotor cortex. Neuron, 98(5):1042–1054, 2018.
- [30] Kristofer E Bouchard, Nima Mesgarani, Keith Johnson, and Edward F Chang. Functional organization of human sensorimotor cortex for speech articulation. Nature, 495(7441):327–332, 2013.
- [31] Sergey D Stavisky, Francis R Willett, Guy H Wilson, Brian A Murphy, Paymon Rezaii, Donald T Avansino, William D Memberg, Jonathan P Miller, Robert F Kirsch, Leigh R Hochberg, et al. Neural ensemble dynamics in dorsal motor cortex during speech in people with paralysis. Elife, 8:e46015, 2019.
- [32] Xupeng Chen, Ran Wang, Amirhossein Khalilian-Gourtani, Leyao Yu, Patricia Dugan, Daniel Friedman, Werner Doyle, Orrin Devinsky, Yao Wang, and Adeen Flinker. A neural speech decoding framework leveraging deep learning and speech synthesis. Nature Machine Intelligence, 6(4):467–480, 2024.
- [33] Maxime Verwoert, Maarten C Ottenhoff, Sophocles Goulis, Albert J Colon, Louis Wagner, Simon Tousseyn, Johannes P Van Dijk, Pieter L Kubben, and Christian Herff. Dataset of speech production in intracranial electroencephalography. Scientific data, 9(1):434, 2022.
- [34] Camille RC Pescatore, Haoyu Zhang, Alex E Hadjinicolaou, Angelique C Paulk, John D Rolston, R Mark Richardson, Ziv M Williams, Jing Cai, and Sydney S Cash. Decoding semantics from natural speech using human intracranial eeg. bioRxiv, 2025.
- [35] Chen Feng, Lu Cao, Di Wu, En Zhang, Ting Wang, Xiaowei Jiang, Jinbo Chen, Hui Wu, Siyu Lin, Qiming Hou, et al. Acoustic inspired brain-to-sentence decoder for logosyllabic language. Cyborg and Bionic Systems, 6:0257, 2025.
- [36] Jiawei Li, Chunxu Guo, Chao Zhang, Edward F Chang, and Yuanning Li. High-fidelity neural speech reconstruction through an efficient acoustic-linguistic dual-pathway framework. bioRxiv, pages 2025–09, 2025.
- [37] Maitreyee Wairagkar, Nicholas S Card, Tyler Singer-Clark, Xianda Hou, Carrina Iacobacci, Lee M Miller, Leigh R Hochberg, David M Brandman, and Sergey D Stavisky. An instantaneous voice-synthesis neuroprosthesis. Nature, pages 1–8, 2025.
- [38] Soufiane Jhilal, Silvia Marchesotti, Bertrand Thirion, Brigitte Soudrie, Anne-Lise Giraud, and Emmanuel Mandonnet. Implantable neural speech decoders: Recent advances, future challenges. Neurorehabilitation and Neural Repair, page 15459683251369468, 2025.
- [39] Junbo Chen, Xupeng Chen, Ran Wang, Chenqian Le, Amirhossein Khalilian-Gourtani, Erika Jensen, Patricia Dugan, Werner Doyle, Orrin Devinsky, Daniel Friedman, et al. Transformer-based neural speech decoding from surface and depth electrode signals. Journal of Neural Engineering, 22(1):016017, 2025.

- [40] Alexandre Défossez, Charlotte Caucheteux, Jérémy Rapin, Ori Kabeli, and Jean-Rémi King. Decoding speech perception from non-invasive brain recordings. Nature Machine Intelligence, 5(10):1097–1107, 2023.
- [41] Xiaolong Wu, Kejia Hu, Zhichun Fu, and Dingguo Zhang. Improved evaluation of waveform reconstruction in speech decoding based on invasive brain-computer interfaces. Imaging Neuroscience, 3:IMAG–a, 2025.
- [42] Xupeng Chen. Neural Speech Decoding and Understanding Leveraging Deep Learning and Speech Synthesis. PhD thesis, New York University Tandon School of Engineering, 2025.
- [43] Sergey D Stavisky. Restoring speech using brain–computer interfaces. Annual Review of Biomedical Engineering, 27, 2025.
- [44] Denis Burnham, Eric Vatikiotis-Bateson, Adriano Vilela Barbosa, João Vítor Menezes, Hani C Yehia, Rua Haszard Morris, Guillaume Vignali, and Jessica Reynolds. Seeing lexical tone: Head and face motion in production and perception of cantonese lexical tones. Speech Communication, 141:40–55, 2022.
- [45] Yuan Chen. Is cantonese lexical tone information important for sentence recognition accuracy in quiet and in noise? Plos one, 17(10):e0276254, 2022.
- [46] Kaylo T Littlejohn, Cheol Jun Cho, Jessie R Liu, Alexander B Silva, Bohan Yu, Vanessa R Anderson, Cady M Kurtz-Miott, Samantha Brosler, Anshul P Kashyap, Irina P Hallinan, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nature neuroscience, pages 1–11, 2025.
- [47] Christian Herff, Dominic Heger, Adriana De Pesters, Dominic Telaar, Peter Brunner, Gerwin Schalk, and Tanja Schultz. Brain-to-text: decoding spoken phrases from phone representations in the brain. Frontiers in neuroscience, 8:141498, 2015.
- [48] Hassan Akbari, Bahar Khalighinejad, Jose L Herrero, Ashesh D Mehta, and Nima Mesgarani. Towards reconstructing intelligible speech from the human auditory cortex. Scientific reports, 9(1):874, 2019.
- [49] Suseendrakumar Duraivel, Shervin Rahimpour, Chia-Han Chiang, Michael Trumpis, Charles Wang, Katrina Barth, Stephen C Harward, Shivanand P Lad, Allan H Friedman, Derek G Southwell, et al. High-resolution neural recordings improve the accuracy of speech decoding. Nature communications, 14(1):6938, 2023.
- [50] Sean L Metzger, Kaylo T Littlejohn, Alexander B Silva, David A Moses, Margaret P Seaton, Ran Wang, Maximilian E Dougherty, Jessie R Liu, Peter Wu, Michael A Berger, et al. A high-performance neuroprosthesis for speech decoding and avatar control. Nature, 620(7976):1037–1046, 2023.
- [51] Xiaolong Wu, Scott Wellington, Zhichun Fu, and Dingguo Zhang. Speech decoding from stereoelectroencephalography (seeg) signals using advanced deep learning methods. Journal of Neural Engineering, 21(3):036055, 2024.
- [52] Aditya Singh, Tessy Thomas, Jinlong Li, Greg Hickok, Xaq Pitkow, and Nitin Tandon. Transfer learning via distributed brain recordings enables reliable speech decoding. Nature communications, 16(1):8749, 2025.
- [53] Cheol Jun Cho, Peter Wu, Tejas S Prabhune, Dhruv Agarwal, and Gopala K Anumanchipalli. Coding speech through vocal tract kinematics. IEEE Journal of Selected Topics in Signal Processing, 2024.
- [54] Patrick W Hullett, Matthew K Leonard, Maria Luisa Gorno-Tempini, Maria Luisa Mandelli, and Edward F Chang. Parallel encoding of speech in human frontal and temporal lobes. Nature Communications, 2025.
- [55] Guy H Wilson, Sergey D Stavisky, Francis R Willett, Donald T Avansino, Jessica N Kelemen, Leigh R Hochberg, Jaimie M Henderson, Shaul Druckmann, and Krishna V Shenoy. Decoding spoken english from intracortical electrode arrays in dorsal precentral gyrus. Journal of neural engineering, 17(6):066007, 2020.
- [56] Matthew K Leonard, Laura Gwilliams, Kristin K Sellers, Jason E Chung, Duo Xu, Gavin Mischler, Nima Mesgarani, Marleen Welkenhuysen, Barundeb Dutta, and Edward F Chang. Large-scale single-neuron speech sound encoding across the depth of human cortex. Nature, 626(7999):593–602, 2024.
- [57] Arjun R Khanna, William Muñoz, Young Joon Kim, Yoav Kfir, Angelique C Paulk, Mohsen Jamali, Jing Cai, Martina L Mustroph, Irene Caprara, Richard Hardstone, et al. Single-neuronal elements of speech production in humans. Nature, 626(7999):603–610, 2024.
- [58] Friedemann Pulvermüller, Martina Huss, Ferath Kherif, Fermin Moscoso del Prado Martin, Olaf Hauk, and Yury Shtyrov. Motor cortex maps articulatory features of speech sounds. Proceedings of the National Academy of Sciences, 103(20):7865–7870, 2006.
- [59] Shreya Chakrabarti, Hilary M Sandberg, Jonathan S Brumberg, and Dean J Krusienski. Progress in speech decoding from the electrocorticogram. Biomedical Engineering Letters, 5(1):10–21, 2015.
- [60] Harshavardhana T Gowda and Lee M Miller. emg2speech: synthesizing speech from electromyography using self-supervised speech models. arXiv preprint arXiv:2510.23969, 2025.

- [61] Elisa Golfinopoulos, Jason A Tourville, and Frank H Guenther. The integration of large-scale neural network modeling and functional brain imaging in speech motor control. Neuroimage, 52(3):862–874, 2010.
- [62] Frigyes Viktor Arthur and Tamás Gábor Csapó. Speech synthesis from intracranial stereotactic electroencephalography using a neural vocoder. Infocommunications Journal, 16(1), 2024.
- [63] Kevin Meng, Farhad Goodarzy, EuiYoung Kim, Ye Jin Park, June Sic Kim, Mark J Cook, Chun Kee Chung, and David B Grayden. Continuous synthesis of artificial speech sounds from human cortical surface recordings during silent speech production. Journal of Neural Engineering, 20(4):046019, 2023.
- [64] Connie Cheung, Liberty S Hamilton, Keith Johnson, and Edward F Chang. The auditory representation of speech sounds in human motor cortex. elife, 5:e12577, 2016.
- [65] Jerrin Thomas Panachakel and Angarai Ganesan Ramakrishnan. Decoding covert speech from eeg-a comprehensive review. Frontiers in neuroscience, 15:642251, 2021.
- [66] Julius Fridriksson, Grigori Yourganov, Leonardo Bonilha, Alexandra Basilakos, Dirk-Bart Den Ouden, and Christopher Rorden. Revealing the dual streams of speech processing. Proceedings of the National Academy of Sciences, 113(52):15108–15113, 2016.
- [67] Stephanie Martin, José del R Millán, Robert T Knight, and Brian N Pasley. The use of intracranial recordings to decode human language: Challenges and opportunities. Brain and language, 193:73–83, 2019.
- [68] Yingyi Qiu, Han Liu, and Mengyuan Zhao. A review of brain–computer interface-based language decoding: From signal interpretation to intelligent communication. Applied Sciences, 15(1):392, 2025.
- [69] Gerwin Schalk, Jan Kubanek, Kai J Miller, NR Anderson, Eric C Leuthardt, Jeffrey G Ojemann, Dave Limbrick, Daniel Moran, Lester A Gerhardt, and Jonathan R Wolpaw. Decoding two-dimensional movement trajectories using electrocorticographic signals in humans. Journal of neural engineering, 4(3):264, 2007.
- [70] Martin Schrimpf, Idan Asher Blank, Greta Tuckute, Carina Kauf, Eghbal A Hosseini, Nancy Kanwisher, Joshua B Tenenbaum, and Evelina Fedorenko. The neural architecture of language: Integrative modeling converges on predictive processing. Proceedings of the National Academy of Sciences, 118(45):e2105646118, 2021.
- [71] Jason K Hsieh, Prashanth R Prakash, Robert D Flint, Zachary Fitzgerald, Emily Mugler, Yujing Wang, Nathan E Crone, Jessica W Templer, Joshua M Rosenow, Matthew C Tate, et al. Cortical sites critical to language function act as connectors between language subnetworks. Nature communications, 15(1):7897, 2024.
- [72] Kirill V Nourski, Richard A Reale, Hiroyuki Oya, Hiroto Kawasaki, Christopher K Kovach, Haiming Chen, Matthew A Howard, and John F Brugge. Temporal envelope of time-compressed speech represented in the human auditory cortex. Journal of Neuroscience, 29(49):15564–15574, 2009.
- [73] Elana M Zion Golumbic, Nai Ding, Stephan Bickel, Peter Lakatos, Catherine A Schevon, Guy M McKhann, Robert R Goodman, Ronald Emerson, Ashesh D Mehta, Jonathan Z Simon, et al. Mechanisms underlying selective neuronal tracking of attended speech at a “cocktail party”. Neuron, 77(5):980–991, 2013.
- [74] Darius Ivucic, Tamari Bayer, Gabriel Ivucic, Stephanie Ries, Jerry Shih, Dean J Krusienski, and Tanja Schultz. Speech envelope reconstruction from stereo eeg in a speech production task. In 2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 1–5. IEEE, 2025.
- [75] Liberty S Hamilton, Erik Edwards, and Edward F Chang. A spatial map of onset and sustained responses to speech in the human superior temporal gyrus. Current Biology, 28(12):1860–1871, 2018.
- [76] Nima Mesgarani, Connie Cheung, Keith Johnson, and Edward F Chang. Phonetic feature encoding in human superior temporal gyrus. Science, 343(6174):1006–1010, 2014.
- [77] David A Moses, Matthew K Leonard, Joseph G Makin, and Edward F Chang. Real-time decoding of questionand-answer speech dialogue using human cortical activity. Nature communications, 10(1):3096, 2019.
- [78] Spencer Kellis, Kai Miller, Kyle Thomson, Richard Brown, Paul House, and Bradley Greger. Decoding spoken words using local field potentials recorded from the cortical surface. Journal of neural engineering, 7(5):056007, 2010.
- [79] Faxin Zhou, Siyuan Zhou, Yuhang Long, Adeen Flinker, and Chunming Lu. Hierarchical linguistic predictions and cross-level information updating during narrative comprehension. Communications Biology, 2025.
- [80] Micha Heilbron, Kristijan Armeni, Jan-Mathijs Schoffelen, Peter Hagoort, and Floris P De Lange. A hierarchy of linguistic predictions during natural language comprehension. Proceedings of the National Academy of Sciences, 119(32):e2201968119, 2022.
- [81] Stephanie K Ries, Nina F Dronkers, and Robert T Knight. Choosing words: left hemisphere, right hemisphere, or both? perspective on the lateralization of word retrieval. Annals of the New York Academy of Sciences, 1369(1):111–131, 2016.

- [82] Han Gyol Yi, Matthew K Leonard, and Edward F Chang. The encoding of speech sounds in the superior temporal gyrus. Neuron, 102(6):1096–1110, 2019.
- [83] Nathan E Crone, Dana Boatman, Barry Gordon, and Lei Hao. Induced electrocorticographic gamma activity during auditory perception. Clinical neurophysiology, 112(4):565–582, 2001.
- [84] Daohan Zhang, Zhenjie Wang, Youkun Qian, Zehao Zhao, Yan Liu, Xiaotao Hao, Wanxin Li, Shuo Lu, Honglin Zhu, Luyao Chen, et al. A brain-to-text framework for decoding natural tonal sentences. Cell Reports, 43(11), 2024.
- [85] A Schippers, MJ Vansteensel, ZV Freudenburg, and NF Ramsey. Don’t put words in my mouth: Speech perception can generate false positive activation of a speech bci. medRxiv, 2024.
- [86] Ariel Goldstein, Eric Ham, Mariano Schain, Samuel A Nastase, Bobbi Aubrey, Zaid Zada, Avigail GrinsteinDabush, Harshvardhan Gazula, Amir Feder, Werner Doyle, et al. Temporal structure of natural language processing in the human brain corresponds to layered hierarchy of large language models. Nature communications, 16(1):10529, 2025.
- [87] Laura Gwilliams, Alec Marantz, David Poeppel, and Jean-Remi King. Hierarchical dynamic coding coordinates speech comprehension in the human brain. Proceedings of the National Academy of Sciences, 122(42):e2422097122, 2025.
- [88] Yu Wang, Heyang Liu, Yuhao Wang, Chuan Xuan, Yixuan Hou, Sheng Feng, Hongcheng Liu, Yusheng Liao, and Yanfeng Wang. Progress, challenges and future of linguistic neural decoding with deep learning. Communications Biology, 8(1):1350, 2025.
- [89] Jonathan S Brumberg, Dean J Krusienski, Shreya Chakrabarti, Aysegul Gunduz, Peter Brunner, Anthony L Ritaccio, and Gerwin Schalk. Spatio-temporal progression of cortical activity related to continuous overt and covert speech production in a reading task. PloS one, 11(11):e0166872, 2016.
- [90] Amirhossein Khalilian-Gourtani, Ran Wang, Xupeng Chen, Leyao Yu, Patricia Dugan, Daniel Friedman, Werner Doyle, Orrin Devinsky, Yao Wang, and Adeen Flinker. A corollary discharge circuit in human speech. Proceedings of the National Academy of Sciences, 121(50):e2404121121, 2024.
- [91] Muge Ozker, Leyao Yu, Patricia Dugan, Werner Doyle, Daniel Friedman, Orrin Devinsky, and Adeen Flinker. Speech-induced suppression and vocal feedback sensitivity in human cortex. Elife, 13:RP94198, 2024.
- [92] Debadatta Dash, Paul Ferrari, and Jun Wang. Decoding imagined and spoken phrases from non-invasive neural (meg) signals. Frontiers in neuroscience, 14:290, 2020.
- [93] Ke Su and Liang Tian. Systematic review: progress in eeg-based speech imagery brain-computer interface decoding and encoding research. PeerJ Computer Science, 11:e2938, 2025.
- [94] Sarah K Wandelt, David A Bjånes, Kelsie Pejsa, Brian Lee, Charles Liu, and Richard A Andersen. Representation of internal speech by single neurons in human supramarginal gyrus. Nature human behaviour, 8(6):1136–1149,

- 2024.

[95] Mohammed Salah Al-Radhi, Géza Németh, and Branislav Gerazov. Mistr: multi-modal ieeg-to-speech synthesis with transformer-based prosody prediction and neural phase reconstruction. arXiv preprint arXiv:2508.03166,

- 2025.

- [96] Lee M Miller, Monty A Escabí, Heather L Read, and Christoph E Schreiner. Spectrotemporal receptive fields in the lemniscal auditory thalamus and cortex. Journal of neurophysiology, 87(1):516–527, 2002.
- [97] Christian Herff, Garett Johnson, Lorenz Diener, Jerry Shih, Dean Krusienski, and Tanja Schultz. Towards direct speech synthesis from ecog: A pilot study. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 1540–1543. IEEE, 2016.
- [98] Stephanie Martin, Peter Brunner, Iñaki Iturrate, José del R Millán, Gerwin Schalk, Robert T Knight, and Brian N Pasley. Word pair classification during imagined speech using direct brain recordings. Scientific reports, 6(1):25803, 2016.
- [99] Erin M Kunz, Benyamin Abramovich Krasa, Foram Kamdar, Donald T Avansino, Nick Hahn, Seonghyun Yoon, Akansha Singh, Samuel R Nason-Tomaszewski, Nicholas S Card, Justin J Jude, et al. Inner speech in motor cortex and implications for speech neuroprostheses. Cell, 188(17):4658–4673, 2025.
- [100] Tianyu He, Mingyi Wei, Ruicong Wang, Renzhi Wang, Shiwei Du, Siqi Cai, Wei Tao, and Haizhou Li. Vocalmind: a stereotactic eeg dataset for vocalized, mimed, and imagined speech in tonal language. Scientific Data, 12(1):657, 2025.

- [101] Ran Zhao, Yanru Bai, Shuming Zhang, Jianing Zhu, Hongxing Liu, and Guangjian Ni. An open dataset of multidimensional signals based on different speech patterns in pragmatic mandarin. Scientific Data, 12(1):1934, 2025.
- [102] Pedram Z Soroush, Christian Herff, Stephanie K Ries, Jerry J Shih, Tanja Schultz, and Dean J Krusienski. The nested hierarchy of overt, mouthed, and imagined speech activity evident in intracranial recordings. NeuroImage, 269:119913, 2023.
- [103] Stéphanie Martin, Peter Brunner, Chris Holdgraf, Hans-Jochen Heinze, Nathan E Crone, Jochem Rieger, Gerwin Schalk, Robert T Knight, and Brian N Pasley. Decoding spectrotemporal features of overt and covert speech from the human cortex. Frontiers in neuroengineering, 7:14, 2014.
- [104] Jesse A Livezey, Kristofer E Bouchard, and Edward F Chang. Deep learning as a tool for neural data analysis: speech classification and cross-frequency coupling in human sensorimotor cortex. PLoS computational biology, 15(9):e1007091, 2019.
- [105] Ciaran Cooney, Raffaella Folli, and Damien Coyle. Neurolinguistics research advancing development of a direct-speech brain-computer interface. IScience, 8:103–125, 2018.
- [106] Kristofer E Bouchard and Edward F Chang. Control of spoken vowel acoustics and the influence of phonetic context in human speech sensorimotor cortex. Journal of Neuroscience, 34(38):12662–12677, 2014.
- [107] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural computation, 9(8):1735–1780, 1997.
- [108] Alex Graves, Santiago Fernández, Faustino Gomez, and Jürgen Schmidhuber. Connectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks. In Proceedings of the 23rd international conference on Machine learning, pages 369–376, 2006.
- [109] Christopher Heelan, Jihun Lee, Ronan O’Shea, Laurie Lynch, David M Brandman, Wilson Truccolo, and Arto V Nurmikko. Decoding speech from spike-based neural population recordings in secondary auditory cortex of non-human primates. Communications biology, 2(1):466, 2019.
- [110] Maxime Verwoert, Joaquín Amigó-Vega, Yingming Gao, Maarten C Ottenhoff, Pieter L Kubben, and Christian Herff. Whole-brain dynamics of articulatory, acoustic and semantic speech representations. Communications Biology, 8(1):432, 2025.
- [111] David A Moses, Sean L Metzger, Jessie R Liu, Gopala K Anumanchipalli, Joseph G Makin, Pengfei F Sun, Josh Chartier, Maximilian E Dougherty, Patricia M Liu, Gary M Abrams, et al. Neuroprosthesis for decoding speech in a paralyzed person with anarthria. New England Journal of Medicine, 385(3):217–227, 2021.
- [112] Heather Wood. Brain–computer interface restores naturalistic speech to a man with als: Motor neuron disease. Nature Reviews Neurology, 21(8):409–409, 2025.
- [113] Tyler Singer-Clark, Xianda Hou, Nicholas S Card, Maitreyee Wairagkar, Carrina Iacobacci, Hamza Peracha, Leigh R Hochberg, Sergey D Stavisky, and David M Brandman. Speech motor cortex enables bci cursor control and click. Journal of Neural Engineering, 22(3):036015, 2025.
- [114] Kimberley Wyse-Sookoo, Shiyu Luo, Daniel Candrea, Anouck Schippers, Donna C Tippett, Brock Wester, Matthew Fifer, Mariska J Vansteensel, Nick F Ramsey, and Nathan E Crone. Stability of ecog high gamma signals during speech and implications for a speech bci system in an individual with als: a year-long longitudinal study. Journal of neural engineering, 21(4):046016, 2024.
- [115] Duo Xu, Juyeong Hong, Huilin Zhao, Sojeong Pak, Jejung Kim, Anh Tuan Hoang, Kyungtai Park, Beom Jin Kim, Seunghyeon Ji, Jonggyu Choi, et al. Two-dimensional semiconductor-based active array for high-fidelity spatiotemporal monitoring of neural activities. Nature materials, pages 1–12, 2025.
- [116] Alexei Baevski, Yuhao Zhou, Abdelrahman Mohamed, and Michael Auli. wav2vec 2.0: A framework for self-supervised learning of speech representations. Advances in neural information processing systems, 33:12449– 12460, 2020.
- [117] Wei-Ning Hsu, Benjamin Bolte, Yao-Hung Hubert Tsai, Kushal Lakhotia, Ruslan Salakhutdinov, and Abdelrahman Mohamed. Hubert: Self-supervised speech representation learning by masked prediction of hidden units. IEEE/ACM transactions on audio, speech, and language processing, 29:3451–3460, 2021.
- [118] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers), pages 4171–4186, 2019.

- [119] Fudong Zhang, Bo Chai, Yujie Wu, Wai Ting Siok, and Nizhuan Wang. Linguistics and human brain: A perspective of computational neuroscience. arXiv preprint arXiv:2602.08275, 2026.
- [120] Yi Guo, Guanhua Ren, Shiqiang Ma, Jun Zhou, Hasan Al Nashash, Alireza Jolfaei, Zhiguo Zhang, Guanglin Li, Ye Li, Yong Hu, et al. Generative ai for brain-computer interfaces decoding: Advances, challenges and future. The Innovation Medicine, pages 100193–1, 2026.
- [121] Hannah Maslen and Stephen Rainey. Control and ownership of neuroprosthetic speech. Philosophy & Technology, 34(3):425–445, 2021.
- [122] Narayan Sankaran, David Moses, Winston Chiong, and Edward F Chang. Recommendations for promoting user agency in the design of speech neuroprostheses. Frontiers in Human Neuroscience, 17:1298129, 2023.
- [123] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
- [124] Charlotte Caucheteux, Alexandre Gramfort, and Jean-Rémi King. Deep language algorithms predict semantic comprehension from brain activity. Scientific reports, 12(1):16327, 2022.
- [125] Jerry Tang, Amanda LeBel, Shailee Jain, and Alexander G Huth. Semantic reconstruction of continuous language from non-invasive brain recordings. Nature Neuroscience, 26(5):858–866, 2023.
- [126] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.
- [127] Muyun Jiang, Wei Zhang, Yi Ding, Kok Ann Colin Teo, LaiGuan Fong, Shuailei Zhang, Zhiwei Guo, Chenyu Liu, Raghavan Bhuvanakantham, Wei Khang Jeremy Sim, et al. Decoding covert speech from eeg by functional areas spatio-temporal transformer. IEEE Journal of Biomedical and Health Informatics, 2026.
- [128] Christopher Wang, Adam Yaari, Aaditya Singh, Vighnesh Subramaniam, Dana Rosenfarb, Jan DeWitt, Pranav Misra, Joseph Madsen, Scellig Stone, Gabriel Kreiman, et al. Brain treebank: Large-scale intracranial recordings from naturalistic language stimuli. Advances in Neural Information Processing Systems, 37:96505–96540, 2024.
- [129] Duc Le, Keli Licata, Carol Persad, and Emily Mower Provost. Automatic assessment of speech intelligibility for individuals with aphasia. IEEE/ACM transactions on audio, speech, and language processing, 24(11):2187–2199, 2016.
- [130] Gregory S Parnell and Timothy E Trainor. 2.3. 1 using the swing weight matrix to weight multiple objectives. In INCOSE International Symposium, volume 19, pages 283–298. Wiley Online Library, 2009.
- [131] Miguel Angrick, Christian Herff, Emily Mugler, Matthew C Tate, Marc W Slutzky, Dean J Krusienski, and Tanja Schultz. Speech synthesis from ecog using densely connected 3d convolutional neural networks. Journal of neural engineering, 16(3):036019, 2019.
- [132] Simon Judge. Exploring electromyography for assistive technology: feasibility, usability and performance of a dry sensor emg switch. Disability and Rehabilitation: Assistive Technology, 20(7):2315–2326, 2025.
- [133] Joan Lobo-Prat, Peter N Kooren, Arno HA Stienen, Just L Herder, Bart FJM Koopman, and Peter H Veltink. Non-invasive control interfaces for intention detection in active movement-assistive devices. Journal of neuroengineering and rehabilitation, 11(1):168, 2014.
- [134] Alex Kreilinger, Vera Kaiser, Christian Breitwieser, John Williamson, Christa Neuper, and Gernot R Müller-Putz. Switching between manual control and brain-computer interface using long term and short term quality measures. Frontiers in neuroscience, 5:147, 2012.
- [135] Dongyi He, Wei Liu, Xiangkai Wang, He Yan, Yun Zhao, and Bin Jiang. Dsranet: A lightweight depthwise separable residual attention network for semg gesture recognition. Biomedical Signal Processing and Control, 113:108845, 2026.
- [136] Dongyi He, Wei Liu, He Yan, Yun Zhao, and Bin Jiang. A multi-scale dual-stream fusion network for highaccuracy semg-based gesture classification. Scientific Reports, 2026.
- [137] Wei Wang, Jennifer L Collinger, Alan D Degenhart, Elizabeth C Tyler-Kabara, Andrew B Schwartz, Daniel W Moran, Douglas J Weber, Brian Wodlinger, Ramana K Vinjamuri, Robin C Ashmore, et al. An electrocorticographic brain interface in an individual with tetraplegia. PloS one, 8(2):e55344, 2013.
- [138] Chaoqi Yang, M Westover, and Jimeng Sun. Biot: Biosignal transformer for cross-data learning in the wild. Advances in Neural Information Processing Systems, 36:78240–78260, 2023.
- [139] Alisa D Levin, Donald T Avansino, Foram B Kamdar, Nicholas S Card, Maitreyee Wairagkar, Brandon G Jacques, Justin J Jude, Carrina Iacobacci, Bayardo E Lacayo, Payton H Bechefsky, et al. Cross-brain transfer of high-performance intracortical speech and handwriting bcis. bioRxiv, pages 2026–01, 2026.

- [140] Jerry Tang and Alexander G Huth. Semantic language decoding across participants and stimulus modalities. Current Biology, 35(5):1023–1032, 2025.
- [141] Mohsen Jamali, Benjamin Grannan, Jing Cai, Arjun R Khanna, William Muñoz, Irene Caprara, Angelique C Paulk, Sydney S Cash, Evelina Fedorenko, and Ziv M Williams. Semantic encoding during language comprehension at single-cell resolution. Nature, 631(8021):610–616, 2024.
- [142] Francisco Pereira, Bin Lou, Brianna Pritchett, Samuel Ritter, Samuel J Gershman, Nancy Kanwisher, Matthew Botvinick, and Evelina Fedorenko. Toward a universal decoder of linguistic meaning from brain activation. Nature communications, 9(1):963, 2018.
- [143] Maël Donoso. A new strategy for artificial intelligence: Training foundation models directly on human brain data. arXiv preprint arXiv:2601.12053, 2026.

