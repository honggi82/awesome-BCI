# arXiv:2602.01019v1[q-bio.NC]1Feb2026

## Inter- and Intra-Subject Variability in EEG: A Systematic Survey

Xuan-The Tran1, Thien-Nhan Vo2, Son-Tung Vu2,3, Thoa-Thi Tran2,4, Manh-Dat Nguyen5, Thomas Do5, and Chin-Teng Lin5 1Vietnam Maritime University, Haiphong, Vietnam 2HAI-Smartlink Research Lab, Anchi STE Company, Vietnam 3Hanoi Architectural University, Hanoi, Vietnam 4Greenwich Vietnam, FPT University, Hanoi, Vietnam 5Computational Intelligence and Brain Computer Interface Lab, School of Computer Science, Australian AI Institute, Faculty of Engineering and Information Technology, University of Technology Sydney ∗

### Abstract

Electroencephalography (EEG) underpins neuroscience, clinical neurophysiology, and brain– computer interfaces (BCIs), yet pronounced interand intra-subject variability limits reliability, reproducibility, and translation. This systematic review studies that quantified or modeled EEG variability across resting-state, event-related potentials (ERPs), and task-related/BCI paradigms (including motor imagery and SSVEP) in healthy and clinical cohorts. Across paradigms, inter-subject differences are typically larger than within-subject fluctuations, but both affect inference and model generalization. Stability is feature-dependent: alpha-band measures and individual alpha peak frequency are often relatively reliable, whereas higher-frequency and many connectivity-derived metrics show more heterogeneous reliability; ERP reliability varies by component, with P300 measures frequently showing moderate-to-good stability. We summarize major sources of variability (biological, state-related, technical, and analytical), review common quantification and modeling approaches (e.g., ICC, CV, SNR, generalizability theory, and multivariate/learning-based methods), and provide recommendations for study design, reporting, and harmonization. Overall, EEG variability should be treated as both a practical constraint to manage and a meaningful signal to leverage for precision neuroscience and robust neurotechnology.

### 1 Introduction

Electroencephalography (EEG) is widely used for studying brain dynamics and for building applied neurotechnologies because it provides high temporal resolution and can be collected repeatedly across tasks and contexts. However, EEG measurements are strongly shaped by systems, subjects, and

∗Preprint notice: This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.

sessions, and substantial variability is consistently observed both between individuals (inter-subject) and within the same individual across trials, days, and tasks (intra-subject) Melnik et al. [2017]; Saha and Baumert [2020]. In practical decoding settings, this variability manifests as distribution shift across subjects, sessions, and datasets, directly degrading generalization and inflating performance estimates when evaluation protocols are not carefully designed Huang et al.

- [2023]; Kamrud et al. [2021]; Xu et al. [2020]. Importantly, variability is multi-determined: it can reflect meaningful traitlike differences and state dynamics, but it is also amplified by technical and analytical factors (e.g., electrode placement variability, source/connectivity pipeline choices) Scrivener and Reader [2022]; Allouch et al. [2023].

Variability matters for at least four reasons. First, it is central to reliability and reproducibility: test–retest datasets and longitudinal designs show that EEG features can be stable in some conditions yet change markedly with state and time, motivating explicit quantification of within- and acrosssession consistency Wang et al. [2022]; Meghdadi et al.

- [2024]. Second, variability constrains biomarker development and interpretation. Quantitative EEG (qEEG) biosignatures and effect-size interpretation depend on how inter- and intra-subject variability interact across frequencies and features, with implications for longitudinal change detection and clinical inference Meghdadi et al. [2024]; Liu et al. [2024]; Nahmias et al. [2019]. Third, variability is a primary driver of BCI performance limitations: cross-session drift and crosssubject heterogeneity reduce decoding robustness, motivate recalibration, and shape the design of adaptation and transfer strategies; large multi-day and multi-session datasets have been introduced specifically to benchmark these effects Ma et al. [2022]; Huang et al. [2023]; Maswanganyi et al. [2022]. Related work also links performance variation to physiological and state-related factors (e.g., pre-task and task-stage band power, stress), highlighting that variability can be partly predictable rather than purely random Zhou et al. [2021]; Zhang et al. [2020]; Borgheai et al. [2024]. Finally, variability is also an opportunity for precision neuroscience: several studies indicate that individual signatures can be detectable and reproducible over time (e.g., trial-by-trial variability magni-

tudes; microstate and spectral “fingerprints”), suggesting a trait-like component alongside state dependence Arazi et al. [2017]; Liu et al. [2020]; Croce et al. [2020]; Zulliger et al. [2022].

In this review, we use inter-subject variability to denote between-person differences in EEG features under comparable experimental contexts, and intra-subject variability to denote within-person fluctuations across trials, sessions, or tasks Saha and Baumert [2020]; Huang et al. [2023]. We distinguish variability from reliability, which concerns the consistency of measurements across repeated observations and is commonly assessed with test–retest designs and reliability metrics in qEEG and cognitive/rest datasets Wang et al.

- [2022]; Meghdadi et al. [2024]; Nahmias et al. [2019]. A feature may show large absolute fluctuations yet remain informative if individual structure is preserved; conversely, analytic flexibility can substantially alter outcomes (notably for connectivity), emphasizing the need to interpret variability estimates in light of pipeline choices Allouch et al. [2023].

We synthesize evidence from 93 empirical studies selected because they explicitly quantified or modeled EEG inter- and/or intra-subject variability across paradigms including resting-state, event-related potentials (ERPs), motor imagery (MI), steady-state visual evoked potentials (SSVEP), and other task-based protocols. The reviewed work spans diverse feature families (spectral power, ERP components, ERD/ERS indices, functional connectivity measures, microstate parameters, spatial patterns) and populations ranging from healthy cohorts to clinical groups, including studies explicitly targeting component- and paradigm-dependent data quality/variability in ERP measurements Wang et al. [2022]; Zhang and Luck [2023]; Eyamu et al. [2024]. We also include evidence from multi-subject, multi-session resources intended to characterize commonality and variability across tasks and days, supporting realistic generalization and benchmarking Huang et al. [2022]; Ma et al. [2022].

The primary aims of this review are to:

- 1. Establish a conceptual framework that organizes EEG variability by type, temporal scale, and plausible sources;
- 2. synthesize empirical evidence on the magnitude and structure of variability across paradigms and feature families;
- 3. Review and compare metrics and modeling approaches for quantifying variability and reliability;
- 4. Examine practical strategies to manage, reduce, or exploit variability in experimental design and downstream modeling;
- 5. Discuss implications for key application domains, including BCI, clinical biomarker development, and cognitive neuroscience; and
- 6. Provide evidence-informed recommendations to improve reproducibility and translation of EEG-based findings.

### 2 Methodology

This review followed a structured search and screening workflow to identify empirical studies in which inter-subject and/or intra-subject variability in EEG was a primary object of analysis. The goal of the search was to capture research that either (i) directly quantified variability and reliability (e.g., test–retest stability, cross-session drift, cross-subject heterogeneity), or (ii) evaluated methodological strategies designed to manage, reduce, or exploit variability (e.g., normalization, harmonization, adaptation, calibration-efficient decoding).

Searches were conducted across major scholarly databases and digital libraries commonly used for EEG and neurotechnology research (e.g., Web of Science, PubMed, IEEE Xplore, ScienceDirect, SpringerLink, and Scopus), supplemented by backward and forward citation screening of key papers. The query design combined terms for EEG with terms for variability and reliability, together with paradigm-specific terms to ensure coverage across resting-state, ERP, oscillatory, and BCI contexts. Representative keyword groups included: “EEG” OR “electroencephalography” AND (“variability” OR “inter-subject” OR “intra-subject” OR “withinsubject” OR “between-subject” OR “test–retest” OR “reliability” OR “repeatability” OR “reproducibility” OR “nonstationarity” OR “session-to-session” OR “domain shift” OR “generalization”) with optional paradigm terms (e.g., “resting-state”, “ERP”, “P300”, “motor imagery”, “SMR”, “SSVEP”, “BCI”).

#### 2.1 Inclusion and Exclusion Criteria

As summarized in Fig. 1, records were identified through database search and then screened in multiple stages. An initial corpus of 312 records was assembled, duplicates were removed, and the remaining records were screened by title and abstract for relevance to the review questions. Full texts were then assessed for eligibility, yielding 93 studies included in the final synthesis. Included studies either (i) explicitly targeted EEG variability and/or reliability as a primary research question, or (ii) reported quantitative analyses of variability patterns (e.g., test–retest reliability, cross-session drift, crosssubject heterogeneity, cross-domain generalization) that were central to interpretation.

Eligibility criteria. Studies were included if they met one or more of the following criteria: they explicitly examined inter-subject and/or intra-subject variability in EEG (within-session, across-session, or across contexts); they reported quantitative estimates of variability or reliability (e.g., ICC, coefficient of variation, SNR-based metrics, pattern similarity, or performance generalization across subjects/sessions); they evaluated factors that modulate EEG variability (e.g., task, age, clinical status, recording protocol, montage/reference); or they proposed and empirically evaluated methodological approaches intended to manage, reduce, or exploit variability (e.g., harmonization, normalization, adaptation, calibration strategies). Records were excluded when they focused exclusively on artifact detection or generic signal-processing methodology without explicit variability analysis, addressed non-EEG modalities without di-

[Figure 1]

Figure 1: PRISMA-style flow diagram summarizing study identification, screening, eligibility assessment, and inclusion for the EEG variability literature review.

rect EEG variability evaluation, or presented purely conceptual/methodological arguments without empirical variability or reliability outcomes.

Temporal distribution of the evidence base. The included studies span more than five decades (1972–2024) and show a pronounced increase in publication volume in the last decade. The distribution across time periods was: 1970s– 1990s (6 studies), 2000–2010 (8 studies), 2011–2015 (5 studies), 2016–2020 (32 studies), and 2021–2024 (43 studies). This growth is consistent with (i) increased emphasis on reproducibility and reliability reporting, (ii) expanding use of EEG for individualized prediction and biomarker development, and (iii) practical demand for robust, calibrationefficient BCIs and generalizable machine learning models. Recent studies more frequently evaluate variability under ecologically realistic conditions (multi-session, multi-site, cross-dataset) and increasingly frame variability as a domainshift problem rather than solely measurement noise.

#### 2.2 Screening and Classification Process

Screening proceeded in three stages aligned with PRISMA reporting: (1) title/abstract screening to remove clearly irrelevant records; (2) full-text eligibility assessment against inclusion/exclusion criteria; and (3) structured data extrac-

tion and coding of the included studies. For each included study, we extracted and coded (at minimum) population characteristics, paradigm/task, recording context (single-session vs. multi-session; single-site vs. multi-site), feature family (spectral/ERP/connectivity/microstates/BCI decoding), variability targets (inter-subject, intra-subject, or both), and the reported variability/reliability metrics (e.g., ICC specification when applicable, CV, correlation-based stability, variance components, or generalization performance). Studies were then grouped for descriptive synthesis by paradigm and feature family to enable comparison of reliability ranges under broadly similar methodological conditions, and to support later sections that discuss how variability sources and mitigation strategies differ across application domains.

### 3 Conceptual Framework of EEG Variability

#### 3.1 Sources of Variability

EEG variability arises from a complex interplay of biological, psychological, technical, and analytical factors. Disentangling these sources is essential for interpreting observed effects, designing reproducible experiments, and developing models that are robust to non-stationarity and domain shift Huang et al. [2023]; Melnik et al. [2017]. Importantly, the same observed variability can have different origins de-

pending on the context: for example, changes across sessions may reflect genuine neurophysiological dynamics, but may also be driven by electrode placement differences, impedance fluctuations, or preprocessing choices. Below we organize major sources of variability into four broad categories and highlight their typical manifestations.

Biological sources. Anatomy and head–brain structure. Individual differences in skull thickness, scalp-to-cortex distance, tissue conductivity, and cortical folding influence both the amplitude and spatial distribution of scalp-recorded potentials Scrivener and Reader [2022]; Bodmer et al. [2017]. These factors systematically contribute to inter-subject differences in feature magnitude and topography, and they can also modulate how sensitive a given montage is to specific cortical generators Scrivener and Reader [2022]. Forward modeling and simulation studies indicate that realistic variation in head geometry and conductivity can yield substantial differences in recorded amplitudes and spatial patterns even when underlying neural sources are identical Bodmer et al. [2017]; Scrivener and Reader [2022]. Such effects are especially relevant when comparing topographic biomarkers, source-localized estimates, or connectivity measures that depend on spatial covariance structure.

Neural generators and functional organization. Individuals differ in the organization and dynamics of functional brain networks, including the coupling strength and configuration of large-scale interactions Pani et al. [2019]; Nakuci et al. [2022]. These differences contribute to inter-subject variability in EEG connectivity and graph-theoretic measures Allouch et al. [2023]. Resting-state network properties can exhibit person-specific structure that is partly stable over time, consistent with the notion that some connectivity signatures behave as trait-like markers Nakuci et al. [2022].

Genetic influences. Twin and family studies support a substantial heritable component in several EEG features, including alpha peak frequency, band-limited power, and selected ERP measures. Reported heritability estimates vary by feature and paradigm but can be sizable, implying that inter-subject variability includes stable biological contributions beyond measurement noise. Candidate genetic variants, particularly those related to neurotransmitter systems, have been associated with variability in oscillatory and evoked responses, although effect sizes and reproducibility can differ across cohorts and analytic choices.

Age, development, and aging. Developmental processes and aging-related neurophysiological changes are major drivers of both inter- and intra-subject variability Dong et al. [2024]; Magnuson et al. [2020]. Across the lifespan, EEG spectral profiles and evoked responses show systematic shifts in frequency, power, and topography Milne [2011]; Bodmer et al. [2017]. For example, alpha peak frequency tends to increase through childhood and adolescence and may decrease in older adulthood, while ERP component amplitudes and latencies change with maturation and cognitive aging Bodmer et al. [2017]; Magnuson et al. [2020]. These effects underscore the importance of age matching, age-stratified analyses, and developmental considerations in biomarker and BCI studies.

Pathology and clinical status. Neurological and psychiatric disorders can alter mean EEG features and often increase within-group heterogeneity Liu et al. [2024]; Eyamu et al. [2024]. Elevated variability in clinical cohorts may reflect heterogeneity in disease mechanisms, stage, symptom severity, medication status, and compensatory strategies Milne [2011]; Magnuson et al. [2020]. Consequently, variability itself can be informative (e.g., indicating subtypes), but it can also dilute group-level contrasts if not modeled appropriately.

Cognitive and psychological state sources. Attention and arousal. Moment-to-moment fluctuations in attention and arousal are key drivers of within-session variability Arazi et al. [2017, 2016]. Lapses in attention can change ongoing oscillatory activity and modulate evoked response amplitudes and latencies, influencing both spectral features and ERP measures Arazi et al. [2017]. Pre-stimulus markers (e.g., alpha power) often correlate with subsequent perceptual performance and the magnitude of stimulus-evoked responses, linking intra-subject variability to latent state dynamics Arazi

- et al. [2016]. Fatigue and mental workload. Prolonged tasks and sus-

tained interaction with BCI systems can induce fatigue that systematically shifts EEG characteristics over time Hwang et al. [2021]. Fatigue-related changes are frequently reflected in increased low-frequency power (e.g., theta), altered alpha dynamics, and reduced amplitudes of cognitive ERP components, which may degrade decoding performance and confound longitudinal comparisons Hwang et al. [2021].

Learning, practice, and strategy adaptation. Repeated exposure to tasks can elicit learning-dependent changes in EEG patterns across sessions Huang et al. [2023]. In BCI paradigms, improvements in control can correspond to the acquisition of stable neural strategies, representing intra-subject variability that is meaningful rather than undesirable Huang et al. [2023]. However, learning trajectories differ substantially across individuals, thereby contributing to inter-subject variability in calibration requirements and achievable performance Saha et al. [2023].

Mood and affective state. Variations in mood and emotion can influence EEG, particularly measures involving frontal activity and asymmetry indices. Day-to-day changes in affect may contribute to test–retest variability and can confound longitudinal designs unless measured and modeled as covariates.

Technical and acquisition sources. Hardware and recording systems. EEG systems differ in channel count, electrode type (wet, dry, active), amplifier characteristics, dynamic range, sampling rate, and shielding, leading to cross-system variability even when measuring identical tasks Melnik et al. [2017]. Such differences contribute to cross-lab and cross-dataset heterogeneity and can interact with preprocessing choices (e.g., filtering) Melnik

- et al. [2017]. Even within a fixed system, impedance fluctuations and subtle placement differences can induce substantial variability in recorded amplitude and noise characteristics Scrivener and Reader [2022].

Electrode placement and referencing. Small deviations in electrode placement across sessions—despite standard-

ized layouts such as the 10–20 system—can change the spatial sampling of cortical sources and alter feature estimates Scrivener and Reader [2022]. Reference choice (e.g., average reference, linked mastoids, Cz, REST) can substantially reshape scalp topographies and influence connectivity measures via changes in covariance structure Allouch et al.

- [2023]. Inconsistent referencing across studies is therefore a major contributor to cross-dataset variability and complicates meta-analytic synthesis Allouch et al. [2023].

Environmental conditions. Ambient electrical noise (e.g., mains interference), temperature, humidity, and local electromagnetic environments influence recording quality and artifact prevalence. Additionally, time of day and circadian rhythms can modulate EEG dynamics, including systematic variations in alpha frequency and power, thereby contributing to within- and across-session variability when protocols are not time-controlled.

Analytical and modeling sources. Preprocessing pipelines. Filtering choices, artifact handling (manual rejection, ICA-based correction, automated pipelines), rereferencing, and segmentation parameters can substantially alter derived EEG measures Allouch et al. [2023]; Zhang and Luck [2023]. Differences in pipelines across groups constitute a major source of cross-lab heterogeneity, and some evidence suggests that preprocessing decisions can affect not only mean feature values but also reliability estimates and apparent stability across sessions Zhang and Luck [2023]. For variability-focused studies, it is therefore important to report preprocessing details comprehensively and, where feasible, evaluate sensitivity to plausible pipeline variants.

Feature definitions and extraction. The choice of feature family (e.g., band power vs. phase-based metrics vs. connectivity), frequency band boundaries, time windows, spatial filtering (e.g., CSP, beamformers), and normalization strategies shapes both the magnitude of observed variability and the resulting reliability Zhang and Luck [2023]. For example, individualized frequency definitions (e.g., using individual alpha frequency) may reduce spurious inter-subject variance while preserving meaningful differences, though such normalization can also change interpretability and comparability across studies.

Model architecture, training, and evaluation. In learning-based pipelines, model class, hyperparameter selection, optimization stochasticity, and data augmentation can produce variability in performance metrics that is distinct from neurophysiological variability Kamrud et al. [2021]. Evaluation protocols also matter: cross-validation design, train–test splitting strategy, and leakage control can inflate or deflate apparent generalization and thereby alter conclusions about inter- and intra-subject robustness Kamrud et al.

- [2021]. Variability-aware reporting should therefore separate (i) variability intrinsic to EEG generation and measurement from (ii) variability induced by modeling and evaluation procedures.

#### 3.2 Relationship to Reliability and Test–Retest

Variability and reliability are closely related but conceptually distinct. Variability describes the magnitude and struc-

ture of dispersion (within a person, between people, across contexts), whereas reliability concerns the repeatability of a measurement—that is, the extent to which observed differences are reproducible under repeated assessment Meghdadi et al. [2024]. Clarifying this distinction is essential for interpreting EEG findings, selecting features for biomarkers or BCI control, and designing studies that can separate true neurophysiological change from measurement noise.

Distinguishing variability from reliability. High variability does not necessarily imply low reliability. For example, an EEG feature may exhibit large inter-subject differences (high between-person variance) yet remain highly reliable if individuals maintain a consistent rank ordering across sessions Arazi et al. [2017]. Conversely, a feature may show low apparent variability at the group level but still be unreliable if repeated measurements fluctuate unpredictably within individuals or are strongly affected by uncontrolled state or technical factors Liu et al. [2024]. In practice, reliability depends on the relative contributions of between-subject variance, within-subject variance, and measurement error; thus, the same absolute variability can correspond to different reliability profiles depending on the study design and the population sampled.

### 4 Methods to Quantify and Model EEG Variability

A rigorous understanding of inter- and intra-subject variability in EEG depends on methodological choices that determine what is treated as signal, how variability is quantified, and which sources of variation are modeled explicitly versus absorbed into error. This section reviews common approaches used in the included literature to quantify variability and reliability, and to formalize variability structure in ways that support study design, longitudinal inference, and robust decoding.

#### 4.1 Classical Reliability Metrics

Classical reliability metrics remain widely used because they provide interpretable summaries of stability across repeated measurements Meghdadi et al. [2024]. However, each metric captures a distinct aspect of variability, and none is sufficient on its own for characterizing the full spatiotemporal and contextual complexity of EEG. Accordingly, variabilityfocused EEG studies increasingly report multiple indices and pair them with explicit modeling of design factors (e.g., session interval, trial count, montage, preprocessing pipeline) Maswanganyi et al. [2022] Wang et al. [2022].

Intraclass correlation coefficient (ICC). The intraclass correlation coefficient is the most commonly used statistic for quantifying test–retest reliability in EEG research Meghdadi et al. [2024]. Conceptually, ICC expresses the fraction of total observed variance attributable to stable betweensubject differences relative to within-subject variance (including measurement error and state-driven fluctuation). In a simplified two-level setting, ICC can be expressed as:

ICC =

σbetween2 σbetween2 + σwithin2

, (1)

Table 1: Summary of Methods to Quantify and Model EEG Variability

Category Method Study (examples) Key Concept / Formula Application Limitations

- 1.Classical Reliability

ICC Maswanganyi et al. [2022]; Ma et al. [2022]; Meghdadi et al. [2024]; Saha and Baumert [2020]

Ratio: σ

2 between

σ2 total

Test–retest reliability quantification.

Sensitive to sample homogeneity & ICC model choice.

Coefficient of Variation (CV)

Meghdadi et al. [2024]; Wang et al. [2022]; Maswanganyi et al. [2022]; Saha and Baumert [2020]

σ µ × 100% Comparing dispersion

across measures/scales.

Dispersion, not reproducibility; unstable when µ ≈ 0.

Signal-to-Noise Ratio (SNR)

Zhang and Luck [2023]; Wang et al. [2022]

Ratio: Psignal/Pnoise ERP/spectral data quality assessment.

High SNR ⇏ high reliability (e.g., systematic shifts).

Generalizability Theory (G-Theory)

Maswanganyi et al. [2022]; Eckert [1974]

Variance decomposition across facets (subj, sess, item,

...)

Designing studies (e.g., trial/session counts) and partitioning sources.

Needs sufficient/structured data; can be complex to implement/interpret.

Test–retest correlation Wang et al. [2022]; Meghdadi et al. [2024]; Nahmias et al. [2019]

Pearson/Spearman r across sessions Rank-order stability check. Ignores mean shifts/absolute agreement; outlier sensitive.

- 2.Pattern Approaches

Pattern similarity Wang et al. [2022]; Maswanganyi et al. [2022]; Zhang and Luck [2023]

Correlation of vectors/waveforms/maps across time Stability of spatial patterns or ERP morphology/timing.

Affected by electrode shifts, referencing, and latency jitter.

Distance metrics Wang et al. [2022]; Huang et al. [2023]

Euclidean/Mahalanobis (feature-space distance) Drift detection; crosssession feature stability in decoding.

Depends on feature scaling/preprocessing; metric choice matters.

Microstate dynamics Saha and Baumert [2020]; Zanesco et al. [2019]; Liu et al. [2020]

Stability of microstate parameters / transition structure Whole-brain state sequence characterization.

Temporal parameters can be less stable than spatial topographies.

Network/connectivity stability

Saha and Baumert [2020]; Pani et al. [2019]; Nakuci et al. [2023]; Allouch et al. [2023]

Reproducibility of graph edges/metrics/modules Functional connectivity organization across sessions/subjects.

Single edges often noisy; pipeline choices can dominate outcomes.

- 3.ML Perspectives Cross-validation (WS/CS/CV)

Ma et al. [2022]; Kamrud et al. [2021]

Performance under within-session vs. crosssession/subject splits

Operationalizing variability as generalization gap.

Sensitive to partitioning; improper splits can inflate accuracy.

Domain shift quantification

Huang et al. [2023]; Xu et al. [2020]

Distribution mismatch (e.g., MMD, classifier-based distances)

Measuring train–test mismatch across sessions/datasets.

Requires careful estimation; depends on feature representation.

- 4.Explicit Modeling Mixed-effects models Eckert [1974]; Dong et al. [2024]

Fixed (population) + random (subject/session) effects Unbalanced longitudinal data; individual trajectories.

Complexity grows with interactions; modeling assumptions matter.

Trait–state decomposition Saha and Baumert [2020]; Zanesco et al. [2019]

Y = Trait + State + Error Separating stable traits from

Requires repeated measures and state/context annotation.

fluctuating states.

Domain adaptation / transfer learning

Huang et al. [2023]; Xu et al. [2020]

Aligning source/target feature distributions Mitigating crosssession/cross-subject performance drops.

May require target calibration data; risk of negative transfer.

Bayesian hierarchical models

Wang et al. [2022]; Nakuci et al. [2023]

Probabilistic multi-level modeling with uncertainty Variance partitioning and uncertainty-aware inference.

Computationally intensive; requires careful priors/diagnostics.

[Figure 2]

Figure 2: Sources of EEG Variability

where σbetween2 is between-subject variance and σwithin2 is within-subject variance across repeated assessments.

Interpretation. Conventional heuristic thresholds are often used to describe ICC magnitudes (e.g., poor, fair, good, excellent), such as:

- • ICC < 0.25: poor,
- • 0.25 ≤ ICC < 0.50: fair,
- • 0.50 ≤ ICC < 0.75: good,
- • ICC ≥ 0.75: excellent Meghdadi et al. [2024].

These thresholds should be interpreted in context because acceptable reliability depends on the intended application (e.g., group-level inference vs. individual-level clinical decisions vs. longitudinal change detection) and on the costs of misclassification or measurement error Meghdadi et al. [2024].

ICC variants and design dependence. Multiple ICC formulations exist, reflecting whether raters/sessions are treated

- as random or fixed effects and whether single measurements or averages are considered. Common forms include ICC(1,1), ICC(2,1), and ICC(3,1) . In many test–retest EEG contexts, ICC(2,1) or ICC(3,1) are used depending on whether the specific sessions/raters are considered a random sample from a larger universe (random effects) or are the only conditions of interest (fixed effects) Meghdadi et al. [2024] Maswanganyi et al. [2022]. Because ICC estimates can differ meaningfully across formulations, variability-focused work should report the exact ICC model, the unit of analysis (single trial, condition average, session average), and confidence intervals where possible.

Limitations. ICC is informative but has important caveats:

- • Dependence on between-subject variance: low ICC can arise either from high within-subject variability or from low between-subject heterogeneity (e.g., a homogeneous sample), even when measurement error is small Wang et al. [2022]; Ma et al. [2022]; Saha and Baumert [2020].
- • Model assumptions: standard ICC formulations assume linear relationships and homoscedasticity, which may be violated for EEG features with non-Gaussian distributions or state-dependent variance Maswanganyi et al. [2022]; Ma et al. [2022].

• Sample size sensitivity: ICC can be unstable in small samples, especially when estimating multiple variance components or when outliers are present Maswanganyi et al. [2022]; Wang et al. [2022].

Coefficient of variation (CV). The coefficient of variation expresses variability relative to the mean:

CV =

σ µ × 100%, (2)

where σ is the standard deviation and µ is the mean of the measure.

Applications. CV is frequently used to:

- • compare relative dispersion of measures expressed on different scales Maswanganyi et al. [2022],
- • summarize measurement precision and heteroscedasticity patterns Maswanganyi et al. [2022]; Ma et al. [2022],
- • flag unusually variable or potentially artifactual measurements Ma et al. [2022]; Saha and Baumert [2020].

Limitations. CV does not directly quantify reliability because it does not assess whether individual differences are reproducible across sessions. A high CV may reflect unstable measurement, genuine heterogeneity across individuals, or a combination of both; thus, CV should be interpreted alongside reliability indices such as ICC, test–retest correlation, or variance-component/trait–state frameworks Meghdadi et al. [2024]; Wang et al. [2022]; Maswanganyi et al. [2022]; Saha and Baumert [2020].

Signal-to-noise ratio (SNR). SNR compares the magnitude of a signal of interest to background noise. In power terms:

Psignal Pnoise

, (3) and in decibels:

SNR =

SNRdB = 10log10

Psignal Pnoise

. (4)

Applications in EEG. SNR is used across multiple EEG domains:

[Figure 3]

Figure 3: Methodological Overview

- • ERP research: SNR may be quantified as the ratio of averaged ERP amplitude to baseline variability (or other noise estimates), and is closely tied to single-trial variability and measurement error considerations Zhang and Luck [2023]; Milne [2011]; Magnuson et al. [2020]; Ganin et al. [2023].
- • Spectral analysis: SNR can be defined as power in a target band relative to adjacent bands or noise floors, often used for oscillatory peaks and band-limited contrasts Saha and Baumert [2020]; Meghdadi et al. [2024]; Zhou et al. [2021].
- • BCI: feature-level SNR (e.g., discriminative bandpower contrasts or ERD/ERS strength) is often predictive of decoding performance and can be used as a proxy for expected classifier separability and user “BCI efficiency” Zhou et al. [2021]; Huang et al. [2023]; Zhang et al. [2020].

Relationship to reliability. Higher SNR often, though not invariably, corresponds to improved reliability because noise-driven fluctuations contribute less to the measured feature Zhang and Luck [2023]; Meghdadi et al. [2024]; Wang

- et al. [2022]. However, reliability can still be low when systematic shifts occur across sessions (e.g., electrode placement changes, state drift, learning effects), even if within-session SNR is high Wang et al. [2022]; Ma et al. [2022]; Scrivener and Reader [2022]; Ribeiro and Castelo-Branco [2021]. Consequently, SNR is best interpreted as a necessary but not sufficient condition for reliability.

Generalizability theory (G-theory). Generalizability theory extends classical reliability by decomposing variability into multiple facets (e.g., subject, session, item/stimulus,

rater, and their interactions) Maswanganyi et al. [2022]; Eckert [1974]. A generic variance decomposition can be written as:

σtotal2 = σsubjects2 +σsessions2 +σitems2 +σinteractions2 +σerror2 .

(5) Advantages. G-theory provides:

- • simultaneous estimation of multiple sources of variability, rather than collapsing them into a single error term Maswanganyi et al. [2022]; Eckert [1974];
- • a principled way to optimize design (e.g., how many trials or sessions are needed to achieve a target reliability), closely related to work emphasizing trial counts, measurement error, and data quality in ERP/EEG Zhang and Luck [2023]; Wang et al. [2022];
- • generalizability coefficients that are conceptually analogous to reliability coefficients but explicitly designdependent Maswanganyi et al. [2022].

EEG applications. In the included literature, G-theory has been used to motivate variance partitioning across subjects, sessions, and task/stimulus facets when interpreting stability and reproducibility of EEG-derived measures Maswanganyi et al. [2022]; Wang et al. [2022]; Zhang and Luck [2023]. Related multi-facet perspectives also arise in work emphasizing that systems, subjects, and sessions jointly shape EEG outcomes and apparent reliability Melnik et al. [2017].

Limitations. G-theory can require balanced or wellstructured designs and becomes computationally and statistically complex when many facets are included or when data are highly unbalanced (common in real-world EEG due to artifact-related trial loss) Maswanganyi et al. [2022]; Zhang and Luck [2023].

Test–retest correlation. Simple Pearson or Spearman correlations between measurements at two time points provide an intuitive assessment of rank-order stability:

r = corr(XTime1,XTime2). (6)

Advantages. Correlation is easy to compute and interpret and directly assesses whether individuals maintain relative ordering across sessions Wang et al. [2022]; Meghdadi et al.

- [2024]; Nahmias et al. [2019]. Limitations. Correlation-based indices have several draw-

backs:

- • they do not account for systematic mean shifts across sessions (e.g., practice effects, habituation), and thus can indicate high stability even when absolute agreement is poor Wang et al. [2022]; Meghdadi et al. [2024];
- • they can be sensitive to outliers, especially in small samples and in the presence of data-quality heterogeneity across participants Maswanganyi et al. [2022]; Zhang and Luck [2023]; Wang et al. [2022];
- • they do not explicitly separate between-subject from within-subject variance components, limiting interpretability when the goal is to model sources of variability (e.g., subject vs session vs trial factors) Maswanganyi et al. [2022]; Eckert [1974]; Melnik et al. [2017].

For these reasons, test–retest correlations are often best reported alongside ICC and/or variance-component approaches, particularly in studies aiming to support individuallevel inference or longitudinal change detection Meghdadi et al. [2024]; Maswanganyi et al. [2022].

#### 4.2 Multivariate and Pattern-Based Approaches

Classical reliability statistics (e.g., ICC, test–retest correlation) are typically computed on scalar features such as band power at a given electrode or ERP amplitude in a fixed time window. However, many modern EEG analyses and BCI pipelines rely on multivariate representations (topographies, spatial filters, covariance matrices, time–frequency maps, connectivity graphs), where the object of interest is the pattern rather than any single element Saha and Baumert [2020]; Melnik et al. [2017]; Pani et al. [2019]; Nakuci et al. [2023]. Pattern-based approaches therefore quantify stability by measuring similarity (or dissimilarity) between highdimensional representations obtained from different trials, sessions, or datasets Wang et al. [2022]; Saha and Baumert

- [2020]; Maswanganyi et al. [2022]; Huang et al. [2023]; Xu et al. [2020].

Pattern similarity metrics. Spatial pattern correlation. For scalp topographies, spatial filters (e.g., CSP weights), or source maps, a common approach is to compute correlation between vectors representing the pattern across electrodes:

###### rspatial = corr p(1), p(2) , (7)

where p(1) and p(2) denote the spatial patterns from session 1 and session 2, respectively. High spatial correlations are commonly interpreted as evidence of stable topography Wang et al. [2022]; Maswanganyi et al. [2022].

This strategy has been used in reliability-oriented analyses to assess stability of ERP-related spatial patterns across sessions Wang et al. [2022]; Zhang and Luck [2023], the consistency of component/scalp-pattern decompositions (including sign/scale ambiguities) Maswanganyi et al. [2022]; Croce et al. [2020]; Zulliger et al. [2022], and agreement of localization- or map-like outcomes when analyses are repeated across time or conditions Saha and Baumert [2020]; Melnik et al. [2017]. In practice, spatial correlation should be interpreted alongside sign/scale ambiguities (e.g., ICA sign flips) and should control for referencing differences when comparing across sessions or datasets Maswanganyi et al.

- [2022]. Moreover, apparent spatial-pattern differences can be amplified by session-to-session changes in electrode placement and the underlying brain regions sampled by nominally identical sensors Scrivener and Reader [2022]; Melnik et al. [2017].

Temporal pattern similarity. For ERP waveforms and other time-series representations, similarity can be quantified via cross-correlation, waveform correlation within defined windows, or measures that explicitly accommodate latency jitter. These approaches are particularly relevant when intrasubject variability expresses itself as latency shifts (e.g., P300 latency drift) rather than simple amplitude rescaling Saha and Baumert [2020]; Wang et al. [2022]; Ganin et al. [2023]. More generally, reliability work highlights that temporalpattern stability is sensitive to preprocessing choices, artifact handling, scoring procedures, and state fluctuations, which can introduce structured session-to-session differences even when within-session SNR is high Wang et al. [2022]; Maswanganyi et al. [2022]; Zhang and Luck [2023]; Ribeiro and Castelo-Branco [2021].

Distance-based metrics. Similarity can also be defined in terms of distance between multivariate feature vectors. For example, Euclidean distance between feature vectors x(1) and x(2) is:

dEuc =

i

x(1)i − x(2)i

2

, (8)

where smaller distances indicate greater similarity. Mahalanobis distance generalizes this by incorporating feature covariance, which can be important when features have different scales or are correlated Maswanganyi et al.

- [2022]. Distance-based approaches have been used to quantify session-to-session stability in BCI feature spaces and to characterize distributional shifts across datasets as a proxy for cross-dataset variability Wang et al. [2022]; Huang et al.
- [2023]; Xu et al. [2020]. A key advantage of distance measures is that they can be applied directly to multivariate feature embeddings learned by models, enabling comparisons even when features are not easily interpretable Huang et al.

- [2023]; Ma et al. [2022]; Sartzetaki et al. [2023]. In practice, however, distance estimates can be strongly affected by analysis/feature choices (“analytical variability”), motivating sensitivity analyses and transparent reporting of pipelines Allouch et al. [2023]; Maswanganyi et al. [2022].

Microstate transition analysis. In microstate research, beyond assessing stability of microstate topographies, investigators often quantify stability of microstate dynamics. Tran-

sition matrices summarize the probability of moving from one microstate class to another, and their stability can be assessed using correlation between transition probability matrices across sessions, entropy measures that summarize the regularity or complexity of transitions, or graphtheoretic descriptors of microstate transition networks Saha and Baumert [2020]; Maswanganyi et al. [2022]; Zanesco et

- al. [2019]. The broader variability literature commonly reports that microstate-like spatial patterns can be relatively stable, whereas temporal dynamics and transition structure tend to be more state-dependent and therefore less reliable across sessions Saha and Baumert [2020]; Croce et al. [2020]; Liu et
- al. [2020]; Zulliger et al. [2022]; Zanesco et al. [2019]. Because transition estimates depend on recording duration and segmentation choices, studies should report data length, number of states, and clustering/labeling procedures when interpreting reliability Maswanganyi et al. [2022]; Zanesco et al.

- [2019].

Network-level stability in connectivity analyses. Connectivity-based variability can be evaluated at multiple organizational levels Saha and Baumert [2020]; Pani et al. [2019]; Allouch et al. [2023]; Nakuci et al. [2023]:

Edge-level stability. The stability of individual connections (edges) can be assessed via test–retest correlation or ICC computed per edge across sessions Nakuci et al. [2023, 2022]; Pani et al. [2019]. Edge-level reliability is often limited by estimator variance and analysis choices (e.g., inverse solutions, connectivity metrics, number of electrodes), and is particularly sensitive to within-subject state changes across sessions Saha and Baumert [2020]; Maswanganyi et

- al. [2022]; Allouch et al. [2023].

Module-level stability. Community structure (network modular organization) can be compared across sessions using partition-similarity views to test whether large-scale organization is preserved even when individual edges fluctuate Pani et al. [2019]; Nakuci et al. [2023, 2022]. Such analyses align with the broader observation that multivariate organization may be more stable than element-wise estimates in high-dimensional EEG representations Maswanganyi et al.

- [2022]; Nakuci et al. [2023].

Global network metrics. Graph-theoretic summaries such as clustering coefficient, characteristic path length, synchronizability, and centrality can be evaluated for reliability across sessions Pani et al. [2019]; Nakuci et al. [2023, 2022]. A recurring observation is that global metrics and/or appropriately pooled summaries may show better stability than individual edge weights, suggesting that network organization can be more robust than specific pairwise connections when appropriately aggregated Saha and Baumert [2020]; Nakuci et al. [2023]. This pattern is consistent with the idea that high-dimensional connectivity estimates are noisy

- at the edge level but can yield more stable low-dimensional summaries when appropriately pooled, while remaining sensitive to methodological degrees of freedom that should be explicitly reported Maswanganyi et al. [2022]; Allouch et al.

- [2023].

#### 4.3 Machine Learning Perspectives

Machine learning (ML) provides complementary frameworks for assessing and modeling EEG variability by treating variability as a generalization problem: how performance and representation structure change when moving across trials, sessions, subjects, or datasets. In this view, variability is reflected in distribution shift between training and deployment conditions, and robustness is evaluated via explicit validation schemes and domain shift metrics Huang et al. [2023]; Xu et

- al. [2020]; Kamrud et al. [2021].

Cross-validation schemes as probes of variability. Different validation protocols isolate different sources and time scales of variability:

Within-subject cross-validation. Training and testing on different trials or runs from the same subject (often within the same session) primarily probes trial-to-trial variability and estimation noise. This scheme typically yields the highest decoding accuracy and is most representative of single-session BCI use cases where calibration and testing occur under similar conditions Ma et al. [2022]; Kamrud et al. [2021].

Cross-session validation. Training on one session and testing on another session from the same subject probes intra-subject variability across time. Performance degradation under this scheme reflects non-stationarity, state drift, and session-level technical differences (e.g., electrode placement), and is central for evaluating long-term BCI viability Ma et al. [2022]; Wang et al. [2022]; Zhou et al. [2021].

Cross-subject validation (e.g., leave-one-subject-out). Training on a cohort of subjects and testing on a held-out subject probes inter-subject variability and is relevant to zerocalibration or low-calibration BCI aspirations. This setting typically yields the lowest accuracy because the model must generalize across large differences in spatial patterns, frequency profiles, and baseline characteristics Huang et al. [2023]; Kamrud et al. [2021]; Golz et al. [2019].

Cross-dataset validation. Training on one dataset and testing on another evaluates a compounded form of variability that includes inter-subject heterogeneity, cross-session drift, and methodological differences across labs (hardware, protocol, preprocessing). This scheme often exposes substantial limitations in generalization and is increasingly used as a benchmark for robustness and domain adaptation methods Xu et al. [2020]; Sartzetaki et al. [2023]; Allouch et al. [2023]; Ahuis et al. [2024].

Performance degradation as an operational measure of variability. Many BCI studies quantify the impact of variability via performance drops between validation regimes. A simple operational definition is:

∆var = Accwithin − Acccross, (9)

where Accwithin denotes within-subject (or within-session) accuracy and Acccross denotes accuracy under cross-session, cross-subject, or cross-dataset testing. Larger drops indicate stronger variability effects Huang et al. [2023]; Ma et al. [2022]; Xu et al. [2020]. Reported comparisons often show systematic degradations when moving from withinsubject to cross-session testing Ma et al. [2022]; Zhou et

- al. [2021], larger drops when moving from within-subject

to cross-subject testing Huang et al. [2023]; Kamrud et al.

- [2021]; Golz et al. [2019], and the largest reductions under cross-dataset transfer, reflecting compounded domain shift Xu et al. [2020]; Sartzetaki et al. [2023]. These figures are highly dependent on dataset, preprocessing, class balance, and model choice, and should be reported with confidence intervals and consistent evaluation protocols to avoid overcomparison across studies Kamrud et al. [2021]; Allouch et

- al. [2023].

Quantifying domain shift. Domain adaptation research provides explicit measures of distributional difference between domains (subjects, sessions, datasets), enabling variability to be quantified beyond performance outcomes Huang

- et al. [2023]; Xu et al. [2020]. Maximum mean discrepancy (MMD). MMD measures

the distance between two distributions P and Q in a reproducing kernel Hilbert space:

MMD(P,Q) = Ex∼P ϕ(x) − Ey∼Q ϕ(y) , (10)

where ϕ(·) is a feature mapping (often implicit via a kernel) Xu et al. [2020]; Huang et al. [2023]. In EEG, distribution-discrepancy views are used to characterize crosssession and cross-subject feature shifts and to evaluate whether adaptation reduces mismatch between training and target domains Huang et al. [2023]; Ma et al. [2022].

A-distance. The A-distance (often used as a proxy for domain discrepancy) can be estimated from the error ϵ of a classifier trained to discriminate samples from two domains:

dA = 2(1 − 2ϵ), (11)

where larger values indicate more separable domains and hence greater domain shift Kamrud et al. [2021]; Xu et al.

- [2020]. In BCI contexts, discriminability-based discrepancy views can help anticipate which subject pairs or sessions are difficult to transfer between and motivate source selection and partitioning practices that prevent optimistic generalization estimates Kamrud et al. [2021]; Huang et al. [2023].

Overall, ML-based perspectives treat EEG variability as a form of distribution shift that can be detected, quantified, and mitigated through careful evaluation design and explicit discrepancy measures Huang et al. [2023]; Xu et al. [2020]; Sartzetaki et al. [2023]. When combined with classical reliability statistics and variance-component models, these approaches provide a more complete methodological toolkit for understanding and managing variability in both scientific and applied EEG settings.

#### 4.4 Modeling Variability Explicitly

A growing body of work argues that EEG variability should not be treated solely as nuisance noise to be removed. Instead, variability can be conceptualized as an inherent property of the neurophysiological system (state dynamics, learning, context dependence) interacting with measurement and analysis processes Saha and Baumert [2020]; Arazi et al. [2017]; Allouch et al. [2023]. Under this view, the objective shifts from eliminating variability to explaining, partitioning, and predicting it.

Mixed-effects (multilevel) models. Mixed-effects models (also termed multilevel or hierarchical linear models) partition variability into fixed effects that describe populationlevel relationships and random effects that capture systematic subject- and session-level deviations Eckert [1974]; Dong et al. [2024]. A generic formulation can be written as:

Yijk = β0 + β1Xijk + u0j + u1jXijk + v0k + εijk,

(12) Advantages. Mixed-effects models are particularly well-

suited to EEG variability questions because they:

- • explicitly represent both between-subject and withinsubject (e.g., cross-session) variability via random effects Dong et al. [2024]; Melnik et al. [2017];
- • naturally handle unbalanced designs and missing data (common in EEG due to artifact-related trial loss and dropouts) without requiring listwise deletion Dong et al. [2024]; Zhang and Luck [2023];
- • yield subject-specific parameter estimates (e.g., individualized slopes, learning curves), supporting individualized inference and precision modeling Dong et al. [2024]; Arazi et al. [2017];
- • enable hypothesis testing about moderators of variability (e.g., whether stability differs by age group, sex/gender, task, or device/protocol) through interactions and variance-structure comparisons Zanesco et al. [2019]; Kumral et al. [2019]; Chen et al. [2024].

Applications in EEG. Mixed-effects and related multilevel models have been applied to quantify trial-level response variability and its group differences (e.g., evokedresponse latency variability) Dong et al. [2024]; Hecker et al. [2022]; Eyamu et al. [2024], to study how data quality and scoring choices impact ERP stability across participants and paradigms Zhang and Luck [2023], and to evaluate variability sources in multi-session or multi-factor settings where subject/session/task effects are jointly present Melnik et al. [2017]; Pani et al. [2019].

Latent trait–state decomposition. Trait–state frameworks aim to disentangle stable individual characteristics from timevarying fluctuations and measurement noise:

Measurementij = Traiti + Stateij + Errorij. (13)

This decomposition is attractive for EEG because many features plausibly contain both trait-like structure and state dependence Saha and Baumert [2020]; Zanesco et al. [2019]. Evidence for trait-like stability in variability-related signatures across tasks and long time spans supports the idea that some variability magnitudes are themselves stable individual characteristics Arazi et al. [2017]. In parallel, microstate and spectral work indicates that whole-brain dynamics contain both within-person fluctuations and reliable between-person differences Croce et al. [2020]; Liu et al. [2020]; Zulliger et al. [2022].

Domain adaptation and domain generalization. Machine learning frameworks frequently conceptualize data from different subjects, sessions, or recording setups as originating from different but related domains, each with its own

distribution Huang et al. [2023]; Xu et al. [2020]. Within this framing, variability is operationalized as domain shift.

Domain adaptation assumes access to (typically unlabeled) data from the target domain and aims to align source and target distributions. In EEG, the need for such alignment is motivated by clear differences between cross-subject and cross-session feature distributions and their distinct implications for training and sample selection Huang et al. [2023]; Ma et al. [2022]. Practical strategies in the literature often combine recalibration, subject-specific transformations, or robustness-oriented preprocessing choices to reduce mismatch Arevalillo-Herr´aez et al. [2019]; Ma et al. [2022]; Allouch et al. [2023].

Domain generalization aims to learn models that generalize to unseen domains without target-domain access. Multidataset benchmarking shows that naive pooling can overestimate performance when partitioning is imperfect, and that generalization gaps remain substantial when moving to unseen subjects or datasets Kamrud et al. [2021]; Xu et al. [2020]; Sartzetaki et al. [2023]. Data augmentation and diversity-enhancing strategies are frequently used to improve robustness under inter-subject or inter-patient variability Aldahr et al. [2022]; Goswami et al. [2024], and methodological choices such as channel selection or common-channel identification can also target session/subject variability in practical pipelines Fauzi et al. [2022]; Changoluisa et al. [2018].

Bayesian hierarchical models. Bayesian hierarchical models offer a principled probabilistic framework for representing EEG variability across multiple nested levels (population → subject → session → observation) and are conceptually aligned with multilevel variance modeling common in variability research Eckert [1974]; Dong et al.

- [2024]; Nakuci et al. [2023]. Such hierarchies mirror the structure of EEG datasets with repeated measures and can naturally express uncertainty in the presence of unequal trial counts and heterogeneous data quality Zhang and Luck

- [2023]; Allouch et al. [2023]. Applications in EEG. Hierarchical perspectives are par-

ticularly relevant for longitudinal and multi-session datasets and for designs that explicitly quantify within- versus between-subject reproducibility across modalities, tasks, and time Wang et al. [2022]; Nakuci et al. [2023]; Ma et al.

- [2022]. From a variability standpoint, these models are attractive because they jointly model multiple sources of variability and quantify uncertainty, rather than providing point estimates alone Dong et al. [2024]; Eckert [1974].

### 5 Variability Across Major EEG Paradigms

This section synthesizes variability and reliability findings across major EEG paradigms, with emphasis on identifying which feature families and frequency ranges tend to be more stable (and under what recording conditions) versus those that are more sensitive to state, artifacts, or methodological choices. Throughout, we distinguish (i) inter-subject variability that supports individual-differences inference when reliable, from (ii) intra-subject variability that limits longitudinal inference and cross-session generalization when not modeled or controlled.

#### 5.1 Resting-State EEG

Resting-state EEG (rsEEG) is typically recorded during quiet wakefulness with eyes closed and/or eyes open and is widely used in cognitive neuroscience and clinical contexts due to its minimal task demands and feasibility in diverse populations Wang et al. [2022]; Nahmias et al. [2019]; Melnik et al. [2017]. However, the apparent simplicity of rsEEG is accompanied by a core methodological challenge: because the paradigm imposes minimal structure, recordings are sensitive to uncontrolled mental activity and fluctuating arousal (e.g., mind wandering, drowsiness), which can introduce substantial within- and across-session variability if vigilance is not monitored or standardized Wang et al. [2022]; Ribeiro and Castelo-Branco [2021]; Parameshwaran and Thiagarajan [2023]; Zanesco et al. [2019]. Consequently, rsEEG provides a useful test case for understanding how trait-like individual signatures coexist with pronounced state dependence.

Inter-subject variability in resting-state EEG. Intersubject differences in rsEEG are often large. Large clinical and longitudinal qEEG datasets report substantial dispersion in spectral power across participants and frequency bins, reflecting both biological heterogeneity and measurement/processing influences Nahmias et al. [2019]; Van Albada et al. [2007]; Meghdadi et al. [2024]. Importantly, this variability is not solely measurement noise: stable betweenperson differences in rhythm expression and multivariate organization can support person-level phenotyping (including “fingerprint”-like identification) when measurements are sufficiently reliable and analysis choices are controlled Arazi et al. [2017]; Nakuci et al. [2023]; Pani et al. [2019].

Spectral power. Among canonical rhythms, posterior alpha activity is frequently reported to provide strong, reproducible individual differences and relatively favorable reliability compared with many other bands, motivating its use for trait-like characterization Meghdadi et al. [2024]; Croce et al. [2020]; Arazi et al. [2017]. Nonetheless, alpha expression varies markedly across individuals, with some participants showing strong, well-defined posterior alpha and others displaying weaker or broader alpha activity Croce et al. [2020]; Arazi et al. [2017]. Reported determinants of this intersubject heterogeneity include system- and acquisition-related factors (e.g., differences in montage/electrode placement and the cortical regions sampled beneath electrodes) Scrivener and Reader [2022]; Melnik et al. [2017], variability in alpharelated spectral organization and its coupling to global brainstate structure (e.g., microstate–spectral relationships) Croce et al. [2020]; Zulliger et al. [2022], recording condition (eyes open vs. eyes closed) Wang et al. [2022]; Parameshwaran and Thiagarajan [2023], and demographic/clinical factors including age and cognitive status Kumral et al. [2019]; Ribeiro and Castelo-Branco [2021]; Eyamu et al. [2024]; Meghdadi et al. [2024]. In contrast to alpha, theta, beta, and especially high-frequency activity (gamma) often show larger relative dispersion and stronger susceptibility to state and artifact contributions, complicating individual-differences interpretation without careful control and preprocessing Van Albada et al. [2007]; Golz et al. [2019]; Allouch et al. [2023].

##### Individual alpha frequency (IAF). IAF-related character-

Table 2: Variability Studies Across Major EEG Paradigms

Category Study Focus / Design Key Finding Limitation

- 1. Resting-State Wang et al. Wang et al. [2022] 60 subjects, 3 sessions (90min + 30 days)

State control critical; alpha ICC>0.8

Young adults; short-term only

Meghdadi et al. Meghdadi et al. [2024] Inter/intra frequency-specific ICC 7-9Hz most reliable (ICC>0.94)

Clinical sample limits generalization

Arazi et al. Arazi et al. [2017] Trial-by-trial reproducibility Trait-like across time/tasks Small sample; specific tasks Nakuci et al. Nakuci et al. [2023] 8 sessions, multi-modal Within¿between repro-

ducibility; alpha stable

Complex setup; small N

Scrivener & Reader Scrivener and Reader [2022] Between-subject electrode placement

3.94-7.17mm variability across axes

No test-retest design

- 2. ERPs Zhang & Luck Zhang and Luck [2023] 40 participants, component quality ERP quality varies by component/paradigm

Cross-sectional; no longitudinal

Ganin et al. Ganin et al. [2023] 19 subjects, P300 latency Latency variability impacts BCI

Small N; single paradigm

Changoluisa et al. Changoluisa et al. [2018] Cross-subject/session electrode selection

Electrode choice affects P300 stability

P300-specific; limited scope

Dong et al. Dong et al. [2024] Population heterogeneity modeling Trial-level variability in auditory ERPs

Auditory modality only

Bland & Schaefer Bland et al. [2011] Trial-to-trial mechanisms Intra-recording variability structured

No test-retest component

- 3. MI-BCI Saha & Baumert Saha and Baumert [2020] Review: inter/intra variability Both dimensions are major BCI challenges

Review; no new empirical data

Huang et al. Huang et al. [2023] Exp1 (inter) vs Exp2 (intra) comparison

Cross-subject ̸= crosssession patterns

N=10; single MI paradigm

Ma et al. Ma et al. [2022] 25 subjects, 5 days, adaptation Accuracy: 68.8→53.7%; adapt→78.9%

2-3 days interval; short-term

Zhou et al. Zhou et al. [2021] 20 subjects, 7 sessions, alpha power Alpha predicts MI across subjects/sessions

Limited time period; single center

Borgheai et al. Borgheai et al. [2024] fNIRS + EEG multimodal prediction

Predicts inter/intra performance (R²=0.942)

Requires dual modality; complexity

- 4. Advanced Huang et al. Huang et al. [2022] M³CV: 106 subjects, 95 with 2 sessions

Multi-paradigm (6) biometric stability

Max 2 sessions; longer-term unknown

Melnik et al. Melnik et al. [2017] Systems-Subjects-Sessions variance

Subjects=32%, Systems=9%, Sessions=1%

Small N=4; limited systems

Liu et al. Liu et al. [2020] 54 subjects, 2-day microstate reliability

Spatial stable; temporal moderate ICC

2-day only; short-term

Zulliger et al. Zulliger et al. [2022] Within vs between-subject alphabehavior

Associations differ by analysis level

Alpha-specific; single paradigm

Garc´ıa Alanis et al. Garc´ıa Alanis et al. [2023] Multi-dimensional variability Characterizes cognitive EEG variability

Complex; challenging interpretation

[Figure 4]

Figure 4: Variability Across Major EEG Paradigms

istics are commonly treated as relatively trait-like alpha markers, with multiple reports emphasizing substantial withinperson stability over extended intervals in healthy adults and comparatively large, stable between-person differences in alpha-related dynamics Arazi et al. [2017]; Meghdadi et al.

- [2024]; Wang et al. [2022]. At the same time, alpha-range features can still be modulated by arousal, ongoing-signal fluctuations, and recording context, reinforcing the need to interpret IAF-style metrics within a broader state/measurement framework Ribeiro and Castelo-Branco [2021]; Wang et al. [2022].

Functional connectivity. Resting-state connectivity measures (e.g., coherence, phase-synchronization indices, correlation/covariance-based connectivity, and graph measures) show substantial inter-subject variability and can exhibit subject-specific patterns that support person identification in multivariate network structure Pani et al. [2019]; Nakuci et al. [2023]; Allouch et al. [2023]. However, reliability of connectivity metrics varies strongly with the chosen estimator, frequency band, epoch length, and handling of volume conduction; analytical degrees of freedom (e.g., electrode count, source reconstruction choices, and connectivity metric selection) can substantially change both between- and within-subject similarity estimates Allouch et

- al. [2023]; Melnik et al. [2017]. In several longitudinal network analyses, alpha-band connectivity is reported as comparatively more reproducible than connectivity derived from other frequency bands, though results remain methoddependent Nakuci et al. [2023, 2022].

Intra-subject variability in resting-state EEG. Within individuals, rsEEG features vary across time scales ranging from within-session fluctuations to test–retest differences

across days or months. Multiple datasets and longitudinal analyses have explicitly quantified such within-person variability across both short-term and longer-term retest intervals Wang et al. [2022]; Meghdadi et al. [2024]; Liu et al. [2024]; Arazi et al. [2017].

Test–retest reliability of spectral power. Across studies, alpha power tends to show the most favorable test–retest profile, with good-to-excellent reliability often reported under eyes-closed conditions and at posterior electrodes in healthy cohorts Meghdadi et al. [2024]; Wang et al. [2022]. Eyesopen alpha commonly yields lower stability in many protocols, consistent with reduced alpha amplitude and increased influence of visual attention/fixation behavior and arousal variation Wang et al. [2022]; Parameshwaran and Thiagarajan [2023]. Reliability in other bands is more heterogeneous: theta and beta features can be moderately stable under controlled conditions, while very low-frequency and highfrequency ranges are often more affected by artifacts, preprocessing, and state dependence Wang et al. [2022]; Van Albada et al. [2007]; Golz et al. [2019].

Stability across time scales. Reliability can degrade as session intervals lengthen, but the relationship depends on protocol structure, familiarity/adaptation effects, and the degree to which session-to-session state drift is controlled or modeled Wang et al. [2022]; Meghdadi et al. [2024]; Arazi et al. [2017]. More generally, slow ongoing-signal fluctuations and arousal dynamics can confound apparent stability if not accounted for, motivating explicit adjustment or stratification by arousal-related markers Ribeiro and Castelo-Branco [2021].

State-related fluctuations during rest. A major contributor to intra-subject variability in rsEEG is fluctuation

in arousal and vigilance during “rest,” including transient drowsiness and mind wandering Wang et al. [2022]; Ribeiro and Castelo-Branco [2021]; Parameshwaran and Thiagarajan [2023]. Studies incorporating auxiliary state measures and/or explicit state modeling highlight that ongoing-signal dynamics can strongly modulate evoked and spontaneous EEG features, and that adjusting for these fluctuations can change conclusions about variability and stability Ribeiro and Castelo-Branco [2021]; Wang et al. [2022]. These findings motivate either (i) stricter vigilance control and standardized instructions or (ii) explicit state modeling (e.g., excluding drowsy epochs; stratifying by arousal markers) when aiming for trait-like rsEEG estimates Wang et al. [2022]; Parameshwaran and Thiagarajan [2023].

Factors influencing resting-state variability. Several methodological factors recurrently modulate rsEEG variability and reliability:

Recording duration. Longer recordings generally yield more stable spectral and multivariate estimates by reducing estimator variance and increasing the amount of artifact-free data available for averaging and robust estimation; this logic is consistent with reliability/data-quality analyses emphasizing the dependence of stability on data quantity and noise levels Zhang and Luck [2023]; Wang et al. [2022]; Meghdadi et

- al. [2024]. Eyes open versus eyes closed. Eyes-closed rsEEG typi-

cally produces stronger alpha rhythms and often higher stability for alpha power compared to eyes-open recordings Wang et al. [2022]; Meghdadi et al. [2024]. Eyes-open conditions, however, can support more standardized visual input (e.g., fixation) and may reduce certain forms of uncontrolled imagery, though they can also increase sensitivity to attentional fluctuations depending on protocol Wang et al. [2022]; Parameshwaran and Thiagarajan [2023].

Instructions and mental context. Instruction sets and compliance (e.g., relax vs. fixate, allowance of mind wandering) can alter both mean spectral profiles and within-session fluctuations. Differences in task context (rest vs. simple fixation) and uncontrolled cognitive content contribute to heterogeneity in reported variability ranges Wang et al. [2022]; Zanesco et al. [2019]; Melnik et al. [2017]. Reporting exact instructions and compliance monitoring is therefore essential in variability-focused rsEEG research Melnik et al. [2017].

Electrode density and spatial sampling. Higher-density montages can improve spatial characterization of topographies and connectivity patterns, potentially stabilizing multivariate estimates; however, greater preparation complexity can increase susceptibility to impedance variability and session-to-session placement differences. Empirical work shows that electrode count and placement variability, as well as downstream analysis choices, can meaningfully impact estimated similarity and reproducibility of connectivity and other multivariate features Scrivener and Reader [2022]; Allouch et al. [2023].

Clinical implications. Resting-state EEG is widely used within quantitative EEG (qEEG) frameworks and has been proposed as a biomarker substrate across multiple clinical contexts, supported by large clinical datasets that reveal both

robust structure and substantial heterogeneity in qEEG features Nahmias et al. [2019, 2017]. However, substantial interand intra-subject variability imposes constraints on diagnostic sensitivity and longitudinal monitoring, particularly when recordings are short, vigilance is uncontrolled, or pipelines differ across sites and laboratories Meghdadi et al. [2024]; Liu et al. [2024]; Ahuis et al. [2024]. Because normative comparisons are only as valid as the stability and harmonization of the underlying features, clinical translation requires careful attention to measurement reliability, standardized acquisition, and transparent reporting of preprocessing, referencing, and methodological choices known to induce analytical variability Allouch et al. [2023]; Scrivener and Reader

- [2022]; Ahuis et al. [2024].

5.2 Evoked Potentials and Event-Related Potentials (ERPs)

Event-related potentials (ERPs) are voltage deflections extracted from EEG by time-locking to discrete events (stimulus onset, response execution, feedback) and averaging across repeated trials. ERPs have been widely used to study perceptual and cognitive processes and are central to multiple clinical and BCI applications Saha and Baumert [2020]; Changoluisa et al. [2018]; Abu-Alqumsan et al. [2017]; Ganin et al. [2023]. Averaging improves signal-to-noise ratio by attenuating uncorrelated noise and some forms of trial-totrial variability; however, systematic variability remains and can be substantial across individuals, across sessions, and across contexts Zhang and Luck [2023]; Bland et al. [2011]; Ribeiro and Castelo-Branco [2021]. ERP variability therefore provides a useful lens for distinguishing (i) stable traitlike individual differences in cognitive processing from (ii) state-dependent fluctuations and measurement-related instability Arazi et al. [2017]; Zanesco et al. [2019].

Inter-subject variability in ERPs. Between-person variability in ERP amplitudes and latencies is widely documented and has important implications for both theory-driven cognitive neuroscience and translation-oriented biomarker research Saha and Baumert [2020]; Zhang and Luck [2023]. Inter-subject differences reflect heterogeneity in neural generators, cognitive strategy, attentional engagement, and demographic/clinical factors, as well as anatomical influences on scalp-recorded amplitude scaling.

P300/P3. The P300 elicited in oddball and related paradigms is among the most extensively studied ERP components and is foundational to several BCI pipelines Changoluisa et al. [2018]; Ganin et al. [2023]. Studies report large inter-individual dispersion in P300 amplitude and latency, and emphasize that performance and interpretation can be limited by both physiological heterogeneity and componentlevel variability (including latency variability) Ganin et al.

- [2023]; Zhang and Luck [2023]. In aging-related contexts, changes in ongoing dynamics and their modulation of evoked responses complicate between-person comparisons, reinforcing the need to control for state and arousal when attributing differences to trait or pathology Ribeiro and CasteloBranco [2021]; Kumral et al. [2019]. In clinical/biomarker contexts, intra-individual ERP variability and its asymmetry (e.g., prefrontal ERP variability) has been investigated

as a complementary marker beyond mean amplitude/latency alone Eyamu et al. [2024].

N2. Components in the N2/N200 family show notable inter-individual variability, and single-trial or intra-individual variability in these components has been highlighted in developmental and clinical cohorts, suggesting that dispersion may reflect meaningful neurocognitive instability rather than only measurement noise Magnuson et al. [2020]; Hecker et

- al. [2022]. Error-related potentials (ERN and related). Error-

related potentials can show strong between-person differences, and work on interaction error-related potentials highlights that invariance/variability has direct consequences for classification and generalization in error-monitoring settings Abu-Alqumsan et al. [2017]. These observations motivate reporting both average ERN-like effects and variabilityaware metrics when ERPs are used for individual-level inference Maswanganyi et al. [2022].

Early sensory components (P1/N1 and related). Early visual-evoked components can exhibit substantial intersubject variability, and recent large-scale modeling work emphasizes that trial-level variability in interpretable features (e.g., latency) can be a key differentiator in neurodevelopmental conditions Dong et al. [2024]. More broadly, ERP data quality varies substantially across participants and paradigms, and these differences can dominate apparent between-person variability if not explicitly quantified and controlled Zhang and Luck [2023].

Intra-subject variability in ERPs. ERP intra-subject variability manifests both as trial-to-trial fluctuation within a session and as test–retest differences across sessions. Reliability evidence is heterogeneous across components and tasks, reflecting differences in SNR, trial availability, and state dependence Saha and Baumert [2020]; Wang et al. [2022]; Zhang and Luck [2023].

Test–retest reliability. Test–retest work in resting and cognitive EEG underscores that state changes across sessions can meaningfully alter EEG features even when withinsession data quality is acceptable, motivating reliability reporting for ERP-derived features whenever longitudinal or individual-differences conclusions are drawn Wang et al.

- [2022]; Maswanganyi et al. [2022]. In practice, reliability improves when sufficient artifact-free trials are available and when quantification procedures are robust to scoring choices and latency estimation issues Zhang and Luck
- [2023]. For error-related components, variability/invariance properties directly affect classifier performance, and limited effective trial counts (e.g., few errors) can lead to unstable estimates that inflate apparent session-to-session differences Abu-Alqumsan et al. [2017]; Zhang and Luck [2023].

Trial-to-trial variability. Even when averaged ERPs appear stable, single-trial ERP amplitudes and latencies vary substantially around the mean waveform Arazi et al. [2017]; Bland et al. [2011]. Contributors include fluctuations in attention and arousal and the interaction between ongoing activity and evoked responses, which can change across time and age Ribeiro and Castelo-Branco [2021]; Parameshwaran and Thiagarajan [2023]. A growing body of work argues that

variability is structured and behaviorally relevant: trial-bytrial neural variability magnitude can be highly reproducible across tasks and over long intervals in adults, suggesting traitlike variability signatures alongside state sensitivity Arazi et al. [2017]. Increased or altered intra-individual ERP variability has also been reported in clinical and developmental contexts, including autism-related cohorts and mild cognitive impairment, supporting variability-aware ERP features as complementary markers Milne [2011]; Magnuson et al. [2020]; Hecker et al. [2022]; Eyamu et al. [2024].

Factors influencing ERP variability. Across studies, several recurring factors modulate ERP variability and reliability:

Number of trials and SNR. Increasing trial counts improves SNR and typically enhances stability of ERP estimates, but the realized benefit depends strongly on paradigm, participant-specific data quality, and scoring procedures Zhang and Luck [2023]; Bland et al. [2011]. In BCI contexts, explicitly addressing latency variability and optimizing repetitions can improve performance, illustrating how variability-aware design choices can trade off time-on-task and estimation reliability Ganin et al. [2023].

Task design parameters. Differences in cognitive demands and internal state (even within nominally similar tasks) can induce structured changes in evoked responses across sessions, complicating synthesis across studies unless task parameters and compliance are well characterized Wang et al. [2022]; Saha and Baumert [2020]; Ribeiro and CasteloBranco [2021].

Electrode and region-of-interest selection. Measurement depends strongly on spatial sampling and extraction choices. Electrode selection strategies have been explicitly proposed to mitigate inter- and intra-subject variability in ERP-based BCIs, highlighting that spatial choices can materially affect robustness Changoluisa et al. [2018]. More generally, participant- and paradigm-dependent variation in data quality implies that fixed ROI/electrode choices can differentially penalize some individuals unless justified or individualized Zhang and Luck [2023].

Analysis decisions. Peak vs. mean amplitude, timewindow definitions, baseline correction, and scoring/latency estimation procedures can materially influence ERP estimates and their apparent stability. Systematic comparisons show that both paradigm and scoring procedure substantially affect ERP data quality, motivating sensitivity analyses and transparent reporting in variability-focused ERP work Zhang and Luck [2023]; Maswanganyi et al. [2022].

Implications for cognitive and clinical studies. ERP variability has direct consequences for inference and translation.

Statistical power and reproducibility. High dispersion and imperfect reliability attenuate observable effects and increase sample size needs, especially when participant-level data quality and scoring procedures introduce additional variance Zhang and Luck [2023]; Maswanganyi et al. [2022].

Biomarker development. Variability-aware ERP features (e.g., trial-level latency variability or prefrontal ERP variability measures) have been explored as potential complementary biomarkers in neurodevelopmental and cognitive-impairment

contexts, but their usefulness depends on robust estimation under realistic noise and trial constraints Dong et al. [2024]; Eyamu et al. [2024].

Longitudinal inference. Longitudinal or intervention studies require components and quantification pipelines with sufficiently high stability to distinguish true within-person change from measurement error and state-driven fluctuations. Evidence that ongoing-state fluctuations can modulate evoked responses, and that cognitive-state differences can emerge across sessions, reinforces the importance of protocol standardization and state monitoring Wang et al. [2022]; Ribeiro and Castelo-Branco [2021]; Maswanganyi et

- al. [2022].

#### 5.3 Oscillatory Task-Related EEG and BCI Paradigms

Task-related oscillatory EEG activity is a central signal source for non-invasive BCI, particularly in motor imagery (MI) and sensorimotor rhythm (SMR) paradigms Saha and Baumert [2020]; Saha et al. [2018]. These paradigms typically exploit event-related desynchronization (ERD; taskrelated power decrease) and event-related synchronization (ERS; power increase, often post-movement) in mu/alpha and beta ranges over sensorimotor cortices Saha and Baumert [2020]; Saha et al. [2018]; Rimbert et al. [2022]. Although oscillatory features can be robust within well-controlled sessions, MI/SMR-BCI is widely recognized as strongly impacted by both inter- and intra-subject variability, which limits generalization and affects user experience in practice Saha and Baumert [2020]; Huang et al. [2023]; Maswanganyi et al.

- [2022].

Inter-subject variability in motor imagery and BCI. Inter-subject variability is a defining challenge for MI-BCI and is a major reason why many systems require subjectspecific calibration and have difficulty achieving “plug-andplay” operation Saha and Baumert [2020]; Huang et al.

- [2023]; Xu et al. [2020]. Canonical ERD/ERS responses include mu/alpha (8–13 Hz) and beta (13–30 Hz) ERD over sensorimotor cortex during imagery or movement, with beta rebound (ERS) often observed after movement cessation Saha et al. [2018]; Saha and Baumert [2020]. However, the magnitude, spatial distribution, temporal dynamics, and frequency specificity of these responses vary substantially across individuals Saha and Baumert [2020]; Huang et al. [2023]; Wriessnegger et al. [2020]. Consequently, discriminative features can differ in optimal frequency band, electrode location, and spatial-filter subspace from one user to another, even under identical task instructions Maswanganyi et al. [2022]; Zhou et al. [2021].

Several sources contribute to inter-subject variability in MI/SMR paradigms:

- • Anatomical and electrode-location factors. Betweenperson differences in head/brain geometry and the practical variability of electrode placement relative to underlying cortex can alter the apparent amplitude and topography of sensorimotor rhythms at the scalp Scrivener and Reader [2022]; Maswanganyi et al. [2022].

- • Functional organization. Individuals differ in how motor imagery recruits sensorimotor networks and in the degree of lateralization during unilateral imagery, yielding strongly lateralized ERD in some users and more bilateral/diffuse modulation in others Saha and Baumert [2020]; Wriessnegger et al. [2020].
- • Cognitive strategies and compliance. Different imagery strategies (e.g., kinesthetic vs. visual imagery), vividness, and timing can lead to distinct oscillatory signatures and different levels of trial-to-trial consistency Saha and Baumert [2020]; Zhou et al. [2021].
- • Baseline neurophysiological traits. Baseline rhythm strength and relative power in relevant bands/stages can influence the magnitude and detectability of ERD/ERS and can correlate with MI decoding performance across subjects and across time Zhou et al. [2021]; Rimbert et al. [2022].

A practical manifestation of strong inter-subject heterogeneity is the existence of a non-trivial subset of users who fail to achieve adequate control under standard MI protocols, reflecting a mismatch between canonical feature assumptions and the individual’s true oscillatory patterns Saha and Baumert [2020]; Huang et al. [2023]; Borgheai et al. [2024]. Importantly, recent evidence suggests that poor performance is not necessarily due to an inability to generate ERD/ERS, but can reflect how cross-subject feature distributions differ from within-subject consistency and how conventional pipelines fail to capture subject-specific discriminative structure Huang et al. [2023]; Maswanganyi et al. [2022]. This motivates individualized band/channel selection and alternative representations designed to be more robust to intersubject differences Fauzi et al. [2022]; Saha et al. [2023].

Inter-subject variability is also reflected in generalization performance. Cross-subject decoding typically underperforms within-subject decoding, mirroring distributional mismatch across participants Huang et al. [2023]; Saha and Baumert [2020]. More broadly, cross-participant and crossdataset EEG modeling can be severely biased by partitioning choices and dataset shift, leading to overestimated performance when evaluation protocols are not designed for true generalization Kamrud et al. [2021]; Xu et al. [2020]; Sartzetaki et al. [2023].

Intra-subject variability in motor imagery and BCI. Within a given user, MI/SMR features often drift over time, and cross-session variability is a critical limitation for practical BCI deployment Saha and Baumert [2020]; Maswanganyi et al. [2022]; Ma et al. [2022]. A common observation is that a classifier trained on one session performs worse on later sessions from the same user even when tasks and equipment are nominally unchanged, consistent with non-stationarity and distribution shift in oscillatory features Huang et al. [2023]; Ma et al. [2022]. Large multi-day datasets and benchmarks further demonstrate that cross-session performance can degrade substantially, and that adaptation can recover performance, highlighting the practical importance of modeling cross-session drift Ma et al. [2022].

This drift can be decomposed into multiple contributors:

- • Electrode placement and contact variability. Sessionto-session differences in cap placement and electrode contact alter spatial covariance structure and can impact spatial filtering and band-power features Scrivener and Reader [2022]; Maswanganyi et al. [2022].
- • State changes (fatigue/drowsiness/stress). Attention, motivation, fatigue, and arousal-related fluctuations modulate oscillatory dynamics and can induce withinperson variability that is not captured by stationary models Chin-Teng Lin et al. [2008]; Golz et al. [2019]; Hwang et al. [2021].
- • Learning and adaptation. Practice effects can improve MI control, but learning trajectories are heterogeneous and can interact with non-stationarity, producing nonmonotonic changes across sessions Saha and Baumert

- [2020]; Ma et al. [2022].

• Non-stationarity and feature drift. Even withinsession EEG statistics can evolve, and these dynamics can accumulate into cross-session shifts that degrade decoders trained under stationarity assumptions Huang et al. [2023]; Maswanganyi et al. [2022]; Kamrud et al.

- [2021].

In addition to cross-session effects, substantial trial-to-trial variability exists within sessions for MI-related ERD/ERS patterns Saha et al. [2018]; Wriessnegger et al. [2020]. Such variability reflects fluctuations in imagery vividness and timing and broader state dynamics, and can be behaviorally meaningful rather than purely noise Arazi et al. [2017]; Garc´ıa Alanis et al. [2023]. Consequently, single-trial decoding is typically more sensitive to short-term variability than block-averaged analyses, reinforcing the need for robustness in real-time control Do et al. [2020]; Saha and Baumert [2020]; Huang et al. [2023]; Do et al. [2021].

Strategies to address variability in BCI. Given the magnitude of inter- and intra-subject variability, the MI-BCI literature has developed multiple strategies to improve robustness:

Calibration and adaptation. Most systems rely on an initial calibration session to fit subject-specific spatial filters and classifiers Saha and Baumert [2020]. To reduce repeated recalibration, adaptive approaches update model parameters online or incrementally to track drift and compensate for within-user non-stationarity; cross-session benchmarks show that adaptation can substantially improve performance relative to naive cross-session transfer Ma et al. [2022]; Huang et

- al. [2023]. Transfer learning and evaluation rigor. Transfer and do-

main adaptation aim to reduce distribution mismatch across subjects/sessions; however, reliable conclusions require careful dataset partitioning and cross-dataset evaluation to avoid inflated accuracy estimates Kamrud et al. [2021]; Xu et al. [2020]; Sartzetaki et al. [2023].

Robust feature engineering and selection. Stability can be improved through individualized frequency-band/channel selection and methods that explicitly target inter-session and inter-subject common channels or robust discriminative subspaces Fauzi et al. [2022]; Maswanganyi et al. [2022]. Analytical choices can also materially affect derived metrics

(especially for connectivity-style features), motivating transparency and sensitivity analyses when robustness is a central goal Allouch et al. [2023].

Comparison with other BCI paradigms. SSVEP-based BCI. Relative to MI-BCI, SSVEP often yields strong stimulus-locked responses and high inter-trial reproducibility; group-level component methods have been proposed to explicitly maximize inter-trial reproducibility and intersubject similarity in SSVEP data Tanaka [2020]. Nevertheless, SSVEP performance can still vary with user state (e.g., stress/fatigue) and other context factors that influence attention and visual processing Zhang et al. [2020].

Hybrid BCIs. Hybrid systems may improve robustness by combining complementary control signals, but can also inherit variability sources from each component paradigm and increase calibration/workload complexity Saha and Baumert [2020]; Maswanganyi et al. [2022].

#### 5.4 Advanced Paradigms

Beyond conventional resting-state, ERP, and canonical oscillatory BCI paradigms, several advanced experimental and analytical approaches have been developed to better characterize EEG dynamics under realistic conditions and to explicitly probe sources of inter- and intra-subject variability Melnik et al. [2017]; Garc´ıa Alanis et al. [2023]. These approaches are particularly valuable because they (i) increase ecological validity by sampling broader contexts (multiple tasks, multiple days, multiple sites), and (ii) provide richer structure for decomposing variance into trait-like and state-like components Wang et al. [2022]; Huang et al. [2022].

Multi-task and multi-session datasets. A notable recent trend is the development of large-scale datasets that deliberately incorporate multiple tasks and repeated sessions per participant, enabling systematic quantification of within-person drift and between-person heterogeneity under a unified protocol Huang et al. [2022]; Wang et al. [2022]. Such resources support design-aware reliability estimation (e.g., how stability changes with session spacing or trial count) and facilitate benchmarking of generalization methods (transfer learning, domain adaptation, meta-learning) under standardized evaluation conditions Ma et al. [2022]; Kamrud et al. [2021]; Sartzetaki et al. [2023].

For example, multi-session datasets in MI and related BCI settings demonstrate that (i) cross-session variability is a robust phenomenon, (ii) the magnitude and structure of variability can be paradigm- and feature-dependent, and (iii) individuals differ substantially in their learning and stability trajectories over repeated sessions Ma et al. [2022]; Maswanganyi et al. [2022]; Huang et al. [2023]. More broadly, largecohort datasets with dozens to hundreds of participants enable population-level characterization of performance variability and the study of correlates of BCI aptitude and stability, including user-profile information and state-related factors Dreyer Pauline et al. [2023]; Saha et al. [2023]; Borgheai et al. [2024]. Importantly, these datasets shift the focus from demonstrating performance within carefully curated sessions to quantifying robustness across realistic deployment conditions, where session-to-session drift and user-state fluctu-

ations are unavoidable Melnik et al. [2017]; Wang et al. [2022].

Cross-dataset generalization and “dataset shift”. Crossdataset generalization studies—training on one dataset and evaluating on another—provide a stringent test of whether models capture invariant neurophysiological structure or instead overfit dataset-specific characteristics Xu et al. [2020]; Sartzetaki et al. [2023]; Kamrud et al. [2021]. Even for nominally similar paradigms, cross-dataset performance can degrade substantially, reflecting compounded sources of variability including (i) hardware and montage differences, (ii) protocol and instruction differences, (iii) population differences, and (iv) preprocessing and feature-extraction choices Xu et al. [2020]; Kamrud et al. [2021]; Allouch et

- al. [2023]. From a variability perspective, cross-dataset studies emphasize that “robustness” is not solely an intra-subject non-stationarity problem; it is also a domain shift problem that spans acquisition systems and analysis pipelines Melnik et al. [2017]; Xu et al. [2020]; Allouch et al. [2023]. Consequently, variability-aware benchmarking benefits from explicit reporting of dataset-level factors, careful partitioning/evaluation design, and sensitivity analyses that quantify how much variance is attributable to key pipeline decisions Kamrud et al. [2021]; Allouch et al. [2023].

Microstate analysis. Microstate analysis characterizes EEG as a sequence of quasi-stable global scalp topographies that persist for tens to hundreds of milliseconds, providing a compact description of large-scale spatiotemporal dynamics Zanesco et al. [2019]; Liu et al. [2020]. Microstates are increasingly used in both basic and clinical EEG research because they summarize complex multichannel activity into interpretable temporal parameters and can be related to spectral and network-level properties Croce et al. [2020]; Zulliger et al. [2022].

Inter-subject variability. While canonical microstate classes can show broadly consistent topographies across individuals, microstate temporal parameters frequently vary across participants. Reported sources of inter-subject variability include differences in average microstate duration, coverage (fraction of time occupied by each class), and the temporal dynamics of occurrence and sequencing Zanesco et al. [2019]; Liu et al. [2020]; Zulliger et al. [2022]. Such variability may reflect stable differences in large-scale dynamics, but it is also influenced by recording context and methodological decisions Laganaro [2017]; Liu et al. [2020].

Intra-subject variability and reliability. Across-session assessments generally suggest that microstate topographies can be relatively stable, whereas temporal parameters (e.g., duration, coverage, occurrence rate) show more moderate reliability and can vary with state and recording conditions Liu et al. [2020]; Zanesco et al. [2019]. Microstate parameters are also systematically related to band-limited spectral features (especially alpha), highlighting that fluctuations in oscillatory state can covary with microstate dynamics within and across individuals Croce et al. [2020]; Zulliger et al. [2022]. These findings motivate detailed reporting of microstate pipeline decisions (e.g., number of states, clustering strategy, template use) and, when possible, sensitivity analy-

ses, because methodological choices can meaningfully affect inferred stability Liu et al. [2020]; Laganaro [2017].

Clinical relevance. Microstate features have been explored as candidate markers in clinical EEG research; however, moderate reliability of some temporal parameters and large inter-subject dispersion present challenges for individual-level inference, underscoring the need for standardized protocols, robust estimation, and validation in independent cohorts Liu et al. [2020]; Laganaro [2017].

### 6 Discussion

This review highlights that inter- and intra-subject EEG variability is not a single phenomenon but the observable outcome of interacting biological, psychological/state, technical, and analytical factors. Across paradigms, variability limits reproducibility and cross-domain generalization, yet it also contains stable, person-specific structure that can be leveraged for individual-differences neuroscience and precision neurotechnology Saha and Baumert [2020]; Huang et al. [2023]; Arazi et al. [2017]; Liu et al. [2020]. A key implication is that variability should be treated as a design variable: what a study can reliably infer depends on how recordings are repeated, how data are partitioned for evaluation, and how analytic choices are controlled and documented Kamrud et al. [2021]; Allouch et al. [2023].

#### 6.1 Interpretation of variability across paradigms and features

The literature consistently indicates that cross-session and cross-subject shifts are major sources of performance degradation for EEG decoding, particularly in motor imagery BCIs, where distribution changes across days and across users remain a central barrier to robust deployment Huang et al. [2023]; Ma et al. [2022]; Maswanganyi et al. [2022]. At the same time, trait-like components are repeatedly observed: trial-by-trial neural variability magnitudes can be stable over long intervals and across tasks Arazi et al. [2017], and microstate parameters and related spectral expressions exhibit reproducible within- and between-subject structure that supports the idea of individual “fingerprints” alongside state dependence Croce et al. [2020]; Liu et al. [2020]; Zulliger et al. [2022]. These findings reinforce a dual perspective: variability is problematic when the goal is estimating small group effects under heterogeneous states, but it is informative when the goal is characterizing stable individual organization or state dynamics.

#### 6.2 Methodological contributors and the need for transparency

A recurring theme is that a non-trivial fraction of observed variability is methodological. Electrode placement can vary meaningfully even with fixed caps, altering the cortical regions sampled and thereby contributing to between-subject and between-session differences Scrivener and Reader [2022]. Likewise, results from EEG source connectivity and network analyses can change substantially with pipeline decisions (e.g., sensor density, inverse solution, connectivity metric), producing analytical variability that directly

impacts between- and within-subject similarity and grouplevel consistency Allouch et al. [2023]. For cross-participant deep learning models, improper dataset partitioning can lead to severe overestimation of accuracy, underscoring that evaluation protocols are inseparable from claims about generalization under variability Kamrud et al. [2021]; Xu et al. [2020]. These observations motivate a stronger norm: studies should treat analysis pipelines and validation strategies as first-class methodological objects to be justified, documented, and sensitivity-tested.

#### 6.3 Recommendations for study design, reporting, and analysis

To support cumulative science and translation, EEG variability studies should treat design, reporting, and analysis as an integrated system rather than independent choices.

Repeated-measures designs. Separating trait-like subject effects from state fluctuations and measurement noise requires repeated recordings. Public resources illustrate how multi-session designs enable quantification of both short- and longer-term stability across resting and cognitive states Wang et al. [2022]. In BCI contexts, multi-day datasets show that cross-session classification can degrade markedly relative to within-session evaluation, but that adaptation strategies and training over session diversity can improve robustness, making repeated measures essential for realistic benchmarking Ma et al. [2022]; Huang et al. [2023]. When feasible, multi-task and multi-session collections can further characterize how task-switching compares to session effects and subject-specific structure Huang et al. [2022]; Pani et al. [2019].

Standardization and metadata for controllable sources of variance. Avoidable variability should be reduced through procedural standardization and explicit metadata capture. In addition to conventional reporting of montage and preprocessing, studies should record electrode placement/fit information when possible, given demonstrated placement variability and its potential impact on sampled brain regions Scrivener and Reader [2022]. For multi-laboratory or multi-site settings, evidence from coordinated preclinical work shows that harmonization of protocols and centralized analysis can reduce between-laboratory variance, supporting investment in standardized procedures, training, and centralized QC Ahuis et al. [2024]. Rich subject- and state-level profiling is also valuable for interpreting performance variation and enabling covariate modeling; datasets with behavioral/psychological measures and subject-driven states provide a template for this approach Wang et al. [2022].

Reliability reporting and uncertainty. Reliability should be reported whenever EEG measures are used for longitudinal inference, individual differences, biomarker development, or patient-level interpretation. Large clinical datasets demonstrate that quantitative EEG feature consistency can be characterized at scale, providing benchmarks for what is stable in realistic settings Nahmias et al. [2019]. For longitudinal effect interpretation, recent work emphasizes that inter- and intra-subject variability can meaningfully alter normalized effect-size estimates across frequencies, implying that both

population variability and change-score variability should be considered when interpreting intervention effects Meghdadi et al. [2024]; Liu et al. [2024]. More broadly, component- and procedure-dependent ERP data quality varies strongly across paradigms and participants, implying that reliability and measurement error should be routinely quantified and discussed rather than assumed Zhang and Luck [2023].

Evaluation under realistic domain shifts. Given the prevalence of cross-session and cross-dataset degradation, claims about generalization should be anchored in evaluations that explicitly test shifts across sessions, subjects, and datasets. Cross-dataset variability is a documented failure mode for deep learning decoding, and cross-participant evaluation can be misleading without strict separation of subjects across data splits Xu et al. [2020]; Kamrud et al. [2021]. Therefore, studies proposing “general” models should report leave-one-subject-out or equivalent subject-independent testing, and where possible include cross-session and crossdataset transfer as primary (not secondary) outcomes Golz et al. [2019]; Sartzetaki et al. [2023].

#### 6.4 Future directions

Large, repeated, and diverse datasets. A central constraint in the variability literature is the limited availability of large, multi-session datasets with rich phenotyping. Emerging multi-subject/multi-session resources for MI and broader multi-task databases provide important building blocks for robust variance decomposition and benchmarking Ma et al. [2022]; Huang et al. [2022]. Extending this direction to multi-site collections, and pairing them with harmonized acquisition and centralized QC, is likely to be pivotal for quantifying site effects and enabling reproducible cross-domain generalization Ahuis et al. [2024]. Such datasets should also include detailed device/protocol metadata and, when feasible, measures that index subject state (sleep, fatigue, stress) given evidence that these factors relate to performance variation Zhou et al. [2021]; Zhang et al. [2020]; Borgheai et al. [2024].

From paradigm-specific engineering to representation learning. The variability challenge can be reframed as a representation problem: models should learn features that preserve neurophysiological invariants while discounting nuisance variation. Evidence of predictable performance variability (e.g., links with spectral state markers) suggests that part of the “noise” may be modeled explicitly or used for adaptive control policies Zhou et al. [2021]; Borgheai et al. [2024]. In addition, multi-dataset fine-tuning studies indicate both the promise and pitfalls of transfer, motivating benchmarks that quantify gains under realistic shifts rather than within-dataset tuning alone Sartzetaki et al. [2023]. Progress here will depend on transparent cross-session and crossdataset evaluations and on reporting practices that prevent inadvertent leakage or overestimation Kamrud et al. [2021].

Edge computing for more reproducible EEG pipelines. A practical future direction to reduce system-induced variability is to move parts of the EEG processing and inference pipeline from heterogeneous host computers to standardized

embedded/edge platforms. By keeping acquisition interfacing, preprocessing (e.g., filtering/re-referencing), feature extraction, and decoding within a fixed hardware/software stack, edge deployment can improve run-to-run determinism (timing, latency, and numerical consistency) and reduce variability introduced by differences in operating systems, drivers, compute loads, and network connectivity. While edge computing cannot remove physiological sources of variability (state fluctuations, learning, fatigue), it may meaningfully reduce avoidable engineering variability and thereby support more reliable longitudinal measurements and realworld BCI use. Recent overviews of Edge AI for BCIs and fully embedded SSVEP platforms highlight the feasibility and emerging design patterns for on-device processing in low-power real-time settings Nguyen et al. [2025, 2026].

Variability as a clinical and cognitive signal. Finally, variability itself may serve as a target phenotype. Work on autism and cognitive impairment illustrates that intraindividual ERP variability can differ systematically between groups and may provide biomarker-relevant information beyond mean amplitudes/latencies Magnuson et al. [2020]; Eyamu et al. [2024]; Dong et al. [2024]. Similarly, dynamic variability metrics (e.g., high-variability periods; microstate dynamics) can distinguish cognitive brain states and link to individual differences, encouraging a shift from viewing variability only as error toward treating it as a mechanistic object of study Parameshwaran and Thiagarajan [2023]; Zanesco et al. [2019].

#### 6.5 Limitations of the present review

Several limitations should be considered. First, the included literature spans heterogeneous paradigms, devices, preprocessing pipelines, and variability metrics, which complicates direct quantitative comparison and may itself reflect analytical variability in the field. Second, variability estimates depend on design choices such as retest interval and task structure; therefore, conclusions about “stability” should be interpreted as conditional on those contexts. Third, because many studies focus on specific applications (e.g., MI-BCI), the evidence base is uneven across paradigms; broader multi-task resources help address this gap but remain relatively scarce. These limitations reinforce the need for harmonized benchmarks, richer metadata, and sensitivity analyses as standard practice.

### 7 Conclusion

This review synthesized evidence from 61 studies examining inter- and intra-subject EEG variability across paradigms, populations, and feature families. A consistent message emerges: variability is pervasive, structured, and consequential. Most EEG measures show substantial differences between individuals as well as meaningful within-individual fluctuations across time and context, and the balance between these sources depends on the paradigm, feature definition, and recording conditions. Reliability is similarly featureand task-dependent, with some measures exhibiting stable individual signatures and others showing pronounced nonstationarity that limits interpretability.

These findings have direct implications for neuroscience and translation. In cognitive and systems neuroscience, variability can attenuate effect sizes and undermine replication unless designs explicitly incorporate repeated measurements and reliability assessment. In neurotechnology and BCI development, variability is a primary driver of calibration burden and performance drift across sessions and users. In clinical applications, variability and moderate reliability constrain individual-level decision making, emphasizing the need for careful measurement design, standardized pipelines, and uncertainty-aware interpretation.

Looking forward, progress will depend on routine reporting of reliability and variance components, stronger harmonization of acquisition and analysis practices, and wider availability of large, diverse, multi-session (and ideally multisite) datasets that enable robust benchmarking under realistic domain shifts. Ultimately, treating variability as a fundamental property to be modeled—rather than residual noise to be ignored—will be central to improving reproducibility and enabling practical, trustworthy EEG-based science and applications.

### References

Mohammad Abu-Alqumsan, Christoph Kapeller, Christoph Hinterm¨uller, Christoph Guger, and Angelika Peer. Invariance and variability in interaction error-related potentials and their consequences for classification. J. Neural Eng., 14(6):066015, December 2017.

Tim P. Ahuis, Magdalena K. Smyk, Cl´ement Laloux, Katharina Aulehner, Jack Bray, Ann-Marie Waldron, Nina Miljanovic, Isabel Seiffert, Dekun Song, Bruno Boulanger, Mathias Jucker, Heidrun Potschka, Bettina Platt, Gernot Riedel, Patrizia Voehringer, Janet R. Nicholson, Wilhelmus H. I. M. Drinkenburg, Martien J. H. Kas, and Steven C. Leiser. Evaluation of variation in preclinical electroencephalographic (EEG) spectral power across multiple laboratories and experiments: An EQIPD study. PLoS ONE, 19(10):e0309521, October 2024.

Raghdah Saem Aldahr, Munid Alanazi, and Mohammad Ilyas. Addressing Inter-Patient Variability in EEG: Diversity-Enhanced Data Augmentation and Few-Shot Learning-based Epilepsy Detection. In 2022 International Conference on Healthcare Engineering (ICHE), pages 1– 7, Johor, Malaysia, September 2022. IEEE.

Sahar Allouch, Aya Kabbara, Joan Duprez, V´eronique Paban, Mohamad Khalil, Julien Modolo, and Mahmoud Hassan. Effect of analytical variability in estimating EEG-based functional connectivity, August 2023.

Ayelet Arazi, Gil Gonen-Yaacovi, and Ilan Dinstein. The magnitude of trial-by-trial neural variability is reproducible over time and across tasks in humans, December 2016.

Ayelet Arazi, Gil Gonen-Yaacovi, and Ilan Dinstein. The Magnitude of Trial-By-Trial Neural Variability Is Reproducible over Time and across Tasks in Humans. eNeuro, 4(6):ENEURO.0292–17.2017, November 2017.

Miguel Arevalillo-Herr´aez, Maximo Cobos, Sandra Roger, and Miguel Garc´ıa-Pineda. Combining Inter-Subject Modeling with a Subject-Based Data Transformation to Improve Affect Recognition from EEG Signals. Sensors, 19(13):2999, July 2019.

Amy R. Bland, Faisal Mushtaq, and David V. Smith. Exploiting Trial-to-Trial Variability in Multimodal Experiments. Front. Hum. Neurosci., 5, 2011.

Benjamin Bodmer, Moritz M¨uckschel, Veit Roessner, and Christian Beste. Neurophysiological variability masks differences in functional neuroanatomical networks and their effectiveness to modulate response inhibition between children and adults. Brain Struct Funct, December 2017.

Seyyed Bahram Borgheai, Alyssa Hillary Zisk, John McLinden, James Mcintyre, Reza Sadjadi, and Yalda Shahriari. Multimodal pre-screening can predict BCI performance variability: A novel subject-specific experimental scheme. Computers in Biology and Medicine, 168:107658, January 2024.

Vinicio Changoluisa, Pablo Varona, and Francisco B. Rodriguez. An electrode selection approach in P300-based BCIs to address inter- and intra-subject variability. In 2018 6th International Conference on Brain-Computer Interface (BCI), pages 1–4, GangWon, January 2018. IEEE.

Jun Chen, Anqi Chen, Bingkun Jiang, Mohammad S. Obaidat, Ni Li, and Xinyu Zhang. Cross-subject Brain Functional Connectivity Analysis for Multi-task Cognitive State Evaluation, 2024. Version Number: 1.

Chin-Teng Lin, Nikhil R. Pal, Chien-Yao Chuang, Tzyy-Ping Jung, Li-Wei Ko, and Sheng-Fu Liang. An EEG-based subject- and session-independent drowsiness detection. In 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence), pages 3448–3454, Hong Kong, China, June 2008. IEEE.

Pierpaolo Croce, Angelica Quercia, Sergio Costa, and Filippo Zappasodi. EEG microstates associated with intraand inter-subject alpha variability. Sci Rep, 10(1):2469, February 2020.

Tien-Thong Nguyen Do, Avinash Kumar Singh, Carlos A Tirado Cortes, and Chin-Teng Lin. Estimating the cognitive load in physical spatial navigation. In 2020 IEEE Symposium Series on Computational Intelligence (SSCI), pages 568–575. IEEE, 2020.

Tien-Thong Nguyen Do, Tzyy-Ping Jung, and Chin-Teng Lin. Retrosplenial segregation reflects the navigation load during ambulatory movement. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 29:488–496, 2021.

Mingfei Dong, Donatello Telesca, Michele Guindani, Catherine Sugar, Sara J. Webb, Shafali Jeste, Abigail Dickinson, April R. Levin, Frederick Shic, Adam Naples, Susan Faja, Geraldine Dawson, James C. McPartland, and Damla S¸ent¨urk. Modeling intra-individual inter-trial EEG

response variability in autism. Statistics in Medicine, 43(17):3239–3263, July 2024.

Dreyer Pauline, Roc Aline, Rimbert S´ebastien, Pillette L´ea, and Lotte Fabien. A large EEG database with users’ profile information for motor imagery Brain-Computer Interface research, January 2023.

Helen M. Eckert. Statistical Models for Inter- and Intraindividual Variability. Research Quarterly. American Alliance for Health, Physical Education and Recreation, 45(2):162–170, May 1974.

Joel Eyamu, Wuon-Shik Kim, Kahye Kim, Kun Ho Lee, and Jaeuk U. Kim. Prefrontal intra-individual ERP variability and its asymmetry: exploring its biomarker potential in mild cognitive impairment. Alz Res Therapy, 16(1):83, April 2024.

Hilman Fauzi, Tadayasu Komura, Masaki Kyoso, Mohd. Ibrahim Shapiai, and Yasmin Mumtaz. Defining Common Inter-Session and Inter-Subject EEG Channels Using Spatial Selection Method. Int. J. Artif. Intell. Res, 6(2), July 2022.

Ip Ganin, An Vasilyev, Td Glazova, and AYa Kaplan. Sources and impact of human brain potential variability in the brain-computer interface. BRSMU, (2023(2)), April 2023.

Jos´e C. Garc´ıa Alanis, Michael D. Nunez, Maren H. Wehrheim, Christian Fiebach, Christoph L¨offler, and Anna-Lena Schubert. The Devil’s in the Variability: A Multidimensional Analysis of EEG Signal Dynamics and Their Relation to Behaviour, November 2023.

Martin Golz, Adolf Schenka, Florian Haselbeck, and Martin Patrick Pauli. Inter-individual variability of EEG features during microsleep events. Current Directions in Biomedical Engineering, 5(1):13–16, September 2019.

Sourojit Goswami, Jacob Phelan, Sean Anderson, and Mahnaz Arvaneh. Improving Motor Imagery-Based BrainComputer Interfaces with Simple EEG Data Augmentation Algorithms: A Comparative Analysis. In 2024 IEEE International Conference on Metrology for eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE), pages 423–428, St Albans, United Kingdom, October 2024. IEEE.

Lukas Hecker, Mareike Wilson, Ludger Tebartz Van Elst, and J¨urgen Kornmeier. Altered EEG variability on different time scales in participants with autism spectrum disorder: an exploratory study. Sci Rep, 12(1):13068, July 2022.

Gan Huang, Zhenxing Hu, Weize Chen, Zhen Liang, Linling Li, Li Zhang, and Zhiguo Zhang. M3 CV:A Multisubject, Multi-session, and Multi-task database for EEGbased Biometrics Challenge, July 2022.

Gan Huang, Zhiheng Zhao, Shaorong Zhang, Zhenxing Hu, Jiaming Fan, Meisong Fu, Jiale Chen, Yaqiong Xiao, Jun Wang, and Guo Dan. Discrepancy between inter- and intrasubject variability in EEG-based motor imagery braincomputer interface: Evidence from multiple perspectives. Front. Neurosci., 17:1122661, February 2023.

Sunhee Hwang, Sungho Park, Dohyung Kim, Jewook Lee, and Hyeran Byun. Mitigating Inter-Subject Brain Signal Variability FOR EEG-Based Driver Fatigue State Classification. In ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 990–994, Toronto, ON, Canada, June 2021. IEEE.

Alexander Kamrud, Brett Borghetti, and Christine Schubert Kabban. The Effects of Individual Differences, NonStationarity, and the Importance of Data Partitioning Decisions for Training and Testing of EEG Cross-Participant Models. Sensors, 21(9):3225, May 2021.

D. Kumral, F. ¸Sansal, E. Cesnaite, K. Mahjoory, E. Al, M. Gaebler, V. V. Nikulin, and A. Villringer. BOLD and EEG Signal Variability at Rest Differently Relate to Aging in the Human Brain, May 2019.

Marina Laganaro. Inter-study and inter-Individual Consistency and Variability of EEG/ERP Microstate Sequences in Referential Word Production. Brain Topogr, 30(6):785– 796, November 2017.

Jiayi Liu, Jing Xu, Guangyuan Zou, Yong He, Qihong Zou, and Jia-Hong Gao. Reliability and Individual Specificity of EEG Microstate Characteristics. Brain Topogr, 33(4):438– 449, July 2020.

Eric Liu, Cidnee Luu, and Lyndia C. Wu. Resting State EEG Variability and Implications for Interpreting Clinical Effect Sizes. IEEE Trans. Neural Syst. Rehabil. Eng., 32:587– 596, 2024.

Jun Ma, Banghua Yang, Wenzheng Qiu, Yunzhe Li, Shouwei Gao, and Xinxing Xia. A large EEG dataset for studying cross-session variability in motor imagery brain-computer interface. Sci Data, 9(1):531, September 2022.

Justine R. Magnuson, Grace Iarocci, Sam M. Doesburg, and Sylvain Moreno. Increased Intra-Subject Variability of Reaction Times and Single-Trial Event-Related Potential Components in Children With Autism Spectrum Disorder. Autism Research, 13(2):221–229, February 2020.

Rito Clifford Maswanganyi, Chunling Tu, Pius Adewale Owolawi, and Shengzhi Du. Statistical Evaluation of Factors Influencing Inter-Session and Inter-Subject Variability in EEG-Based Brain Computer Interface. IEEE Access, 10:96821–96839, 2022.

Amir H. Meghdadi, Chris Berka, and Michael H. MalekAhmadi. Inter- and intra-subject variability of quantitative EEG biosignatures and their effect on interpretation of normalized effect size. Alzheimer’s &amp; Dementia, 20(S2):e084211, December 2024.

Andrew Melnik, Petr Legkov, Krzysztof Izdebski, Silke M. K¨archer, W. David Hairston, Daniel P. Ferris, and Peter K¨onig. Systems, Subjects, Sessions: To What Extent Do These Factors Influence EEG Data? Front. Hum. Neurosci., 11, March 2017.

Elizabeth Milne. Increased Intra-Participant Variability in Children with Autistic Spectrum Disorders: Evidence from Single-Trial Analysis of Evoked EEG. Front. Psychology, 2, 2011.

David O. Nahmias, Kimberly L. Kontson, and Eugene F. Civillico. Learning EEG: Identification of novel electroencephalogram classifications and variability of baseline features in a large clinical dataset. In 2017 International Symposium on Wearable Robotics and Rehabilitation (WeRob), pages 1–2, Houston, TX, November 2017. IEEE.

David O Nahmias, Kimberly L Kontson, David A Soltysik, and Eugene F Civillico. Consistency of quantitative electroencephalography features in a large clinical data set. J. Neural Eng., 16(6):066044, November 2019.

Johan Nakuci, Nick Wasylyshyn, Matthew Cieslak, James C. Elliot, Kanika Bansal, Barry Giesbrecht, Scott T. Grafton, Jean M. Vettel, Javier O. Garcia, and Sarah F. Muldoon. Within- and between-subject reproducibility and variability in multi-modal, longitudinal brain networks, May 2022.

Johan Nakuci, Nick Wasylyshyn, Matthew Cieslak, James C. Elliott, Kanika Bansal, Barry Giesbrecht, Scott T. Grafton, Jean M. Vettel, Javier O. Garcia, and Sarah F. Muldoon. Within-subject reproducibility varies in multi-modal, longitudinal brain networks. Sci Rep, 13(1):6699, April 2023.

Manh-Dat Nguyen, Thomas Do, Xuan-The Tran, Quoc-Toan Nguyen, and Chin-Teng Lin. Edge ai–brain-computer interfaces system: A survey. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2025.

Manh-Dat Nguyen, Thomas Do, Nguyen Thanh Trung Le, Xuan-The Tran, Fred Chang, and Chin-Teng Lin. Edgessvep: A fully embedded ssvep bci platform for low-power real-time applications. arXiv preprint arXiv:2601.01772, 2026.

Sara M. Pani, Marta Ciuffi, Matteo Demuru, Giovanni Bazzano, Ernesto D’aloja, and Matteo Fraschini. Subject, session and task effects on power, connectivity and network centrality: a source-based EEG study, June 2019.

Dhanya Parameshwaran and Tara C. Thiagarajan. High Variability Periods in the EEG Distinguish Cognitive Brain States. Brain Sciences, 13(11):1528, October 2023.

Maria J. Ribeiro and Miguel Castelo-Branco. Slow fluctuations in ongoing brain activity decrease in amplitude with ageing yet their impact on task-related evoked responses is dissociable from behaviour, November 2021.

Sebastien Rimbert, David Trocellier, and Fabien Lotte. Is Event-Related Desynchronization variability correlated with BCI performance? In 2022 IEEE International Conference on Metrology for Extended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE), pages 163–168, Rome, Italy, October 2022. IEEE.

Simanto Saha and Mathias Baumert. Intra- and Inter-subject Variability in EEG-Based Sensorimotor Brain Computer Interface: A Review. Front. Comput. Neurosci., 13:87, January 2020.

Simanto Saha, Khawza Iftekhar Uddin Ahmed, Raqibul Mostafa, Leontios Hadjileontiadis, and Ahsan Khandoker. Evidence of Variabilities in EEG Dynamics During Motor Imagery-Based Multiclass Brain–Computer Interface.

IEEE Trans. Neural Syst. Rehabil. Eng., 26(2):371–382, February 2018.

Simanto Saha, Mathias Baumert, and Alistair McEwan. Can Inter-Subject Associativity Predict Data-Driven BCI Performance? In 2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 1–4, Sydney, Australia, July 2023. IEEE.

Christina Sartzetaki, Panagiotis Antoniadis, Nick Antonopoulos, Ioannis Gkinis, Agamemnon Krasoulis, Serafeim Perdikis, and Vassilis Pitsikalis. Beyond Within-Subject Performance: A Multi-Dataset Study of Fine-Tuning in the EEG Domain. In 2023 IEEE International Conference on Systems, Man, and Cybernetics (SMC), pages 4429–4435, Honolulu, Oahu, HI, USA, October 2023. IEEE.

Catriona L. Scrivener and Arran T. Reader. Variability of EEG electrode positions and their underlying brain regions: visualizing gel artifacts from a simultaneous EEGfMRI dataset. Brain and Behavior, 12(2):e2476, February 2022.

Hirokazu Tanaka. Group task-related component analysis (gTRCA): a multivariate method for inter-trial reproducibility and inter-subject similarity maximization for EEG data analysis. Sci Rep, 10(1):84, January 2020.

Sacha J. Van Albada, Christopher J. Rennie, and Peter A. Robinson. VARIABILITY OF MODEL-FREE AND MODEL-BASED QUANTITATIVE MEASURES OF EEG. J. Integr. Neurosci., 06(02):279–307, June 2007.

Yulin Wang, Wei Duan, Debo Dong, Lihong Ding, and Xu Lei. A test-retest resting, and cognitive state EEG

dataset during multiple subject-driven states. Sci Data, 9(1):566, September 2022.

Selina C. Wriessnegger, Gernot R. M¨uller-Putz, Clemens Brunner, and Andreea I. Sburlea. Inter- and Intraindividual Variability in Brain Oscillations During Sports Motor Imagery. Front. Hum. Neurosci., 14:576241, October 2020.

Lichao Xu, Minpeng Xu, Yufeng Ke, Xingwei An, Shuang Liu, and Dong Ming. Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. Front. Hum. Neurosci., 14:103, April 2020.

Anthony P. Zanesco, Brandon G. King, Alea C. Skwara, and Clifford D. Saron. Within and Between-person Correlates of the Temporal Dynamics of Resting EEG Microstates, September 2019.

Guanghui Zhang and Steven J. Luck. Variations in ERP data quality across paradigms, participants, and scoring procedures. Psychophysiology, 60(7):e14264, July 2023.

Hao-Yan Zhang, Cory E. Stevenson, Tzyy-Ping Jung, and Li-Wei Ko. Stress-Induced Effects in Resting EEG Spectra Predict the Performance of SSVEP-Based BCI. IEEE Trans. Neural Syst. Rehabil. Eng., 28(8):1771–1780, August 2020.

Qing Zhou, Jiafan Lin, Lin Yao, Yueming Wang, Yan Han, and Kedi Xu. Relative Power Correlates With the Decoding Performance of Motor Imagery Both Across Time and Subjects. Front. Hum. Neurosci., 15:701091, August 2021.

Johannes Zulliger, Laura Diaz Hernandez, and Thomas Koenig. Within and Between Subject Spectral Fingerprints of EEG-Microstate Parameters. Brain Topogr, 35(3):277– 281, May 2022.

