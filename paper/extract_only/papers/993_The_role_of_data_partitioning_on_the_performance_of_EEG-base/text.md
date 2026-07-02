arXiv:2505.13021v1[eess.SP]19May2025

The role of data partitioning on the performance of EEG-based deep learning models in supervised cross-subject analysis: a preliminary study⋆

Federico Del Pupa,b,c,∗, Andrea Zanolab,c, Louis Fabrice Tshimangab,c, Alessandra Bertoldoa,c, Livio Finosc,d,e and Manfredo Atzorib,c,f

aDepartment of Information Engineering, University of Padua, Padua, 35131, Italy bDepartment of Neuroscience, University of Padua, Padua, 35121, Italy cPadova Neuroscience Center, University of Padua, Padua, 35129, Italy dDepartment of Statistical Sciences, University of Padua, Padua, 35121, Italy eDepartment of Developmental and Social Psychology, University of Padua, Padua, 35131, Italy fInformation Systems Institute, University of Applied Sciences Western Switzerland (HES-SO Valais), Sierre, 3960, Switzerland

###### ARTICLE INFO

###### ABSTRACT

Keywords: EEG Deep Learning Cross-Validation Data Leakage Leave-One-Subject-Out Nested-Leave-One-Subject-Out Disease classification Brain-Computer Interfaces

Deep learning is significantly advancing the analysis of electroencephalography (EEG) data by effectively discovering highly nonlinear patterns within the signals.

Data partitioning and cross-validation are crucial for assessing model performance and ensuring study comparability, as they can produce varied results and data leakage due to specific signal properties (e.g., biometric). Such variability in model evaluation leads to incomparable studies and, increasingly, overestimated performance claims, which are detrimental to the field. Nevertheless, no comprehensive guidelines for proper data partitioning and cross-validation exist in the domain, nor is there a quantitative evaluation of the impact of different approaches on model accuracy, reliability, and generalizability.

To assist researchers in identifying optimal experimental strategies, this paper thoroughly investigates the role of data partitioning and cross-validation in evaluating EEG deep learning models.

Five cross-validation settings are compared across three supervised cross-subject classification tasks (brain-computer interfaces, Parkinson’s, and Alzheimer’s disease classification) and four established architectures of increasing complexity (ShallowConvNet, EEGNet, DeepConvNet, and Temporal-based ResNet).

The comparison of over 100,000 trained models underscores, first, the importance of using subjectbased cross-validation strategies for evaluating EEG deep learning architectures, except when withinsubject analyses are acceptable (e.g., BCI). Second, it highlights the greater reliability of nested approaches (e.g., N-LNSO) compared to non-nested counterparts, which are prone to data leakage and favor larger models overfitting to validation data.

In conclusion, this work provides EEG deep learning researchers with an analysis of data partitioning and cross-validation and offers guidelines to avoid data leakage, currently undermining the domain with potentially overestimated performance claims.

a variety of applications, including Brain-Computer Interfaces (BCI) [1], emotion recognition [2], sleep staging [3], and the characterization of neurological disorders such as Parkinson’s [4], Alzheimer’s [5], and epilepsy [6]. This success stems from the ability of deep neural networks to extract complex nonlinear patterns that reflect the brain neural activity. However, the potential of deep learning is significantly hindered by its sensitivity to minimal variations in the experimental setting. For instance, the use of extensive preprocessing pipelines—though supported by literature due to the low signal-to-noise ratio of EEG signals—can lead to significant performance drops of over 10% compared to models trained with minimally filtered data [7]. Similarly, the methodology used to partition data into training, validation, and test sets can strongly influence the final results, leading to unrealistic estimates of performance metrics and a lack of comparability across studies.

#### 1. Introduction

Over the past decade, Deep Learning (DL) has dramatically transformed the analysis of electroencephalographic (EEG) data, achieving state-of-the-art performance across

⋆This document is the results of the research project funded in part by the European Union’s Horizon Europe research and innovation programme under Grant agreement no 101137074 - HEREDITARY, in part by the STARS@UNIPD funding program of the University of Padua, Italy, project: MEDMAX.

∗Corresponding author

federico.delpup@studenti.unipd.it (F. Del Pup); andrea.zanola@phd.unipd.it (A. Zanola); louisfabrice.tshimanga@unipd.it (L. Tshimanga); alessandra.bertoldo@unipd.it (A. Bertoldo); livio.finos@unipd.it (L. Finos); manfredo.atzori@unipd.it (M. Atzori)

[Figure 1]

ORCID(s): 0009-0004-0698-962X (F. Del Pup); 0000-0001-6973-8634 (A. Zanola); 0009-0002-1240-4830 (L. Tshimanga); 0000-0002-6262-6354 (A. Bertoldo); 0000-0003-3181-8078 (L. Finos); 0000-0001-5397-2063 (M. Atzori)

In EEG analysis, the limited availability of datasets with more than a few dozen or, at most, a hundred subjects,

constrains the creation of sufficiently large and representative training, validation, and test sets. Consequently, it has become best practice to assess model accuracy using CrossValidation (CV) procedures, which yield more reliable performance estimates, particularly when working with small datasets. Over the years, researchers have adopted various cross-validation strategies that operate both at the sample and the subject level [8]. Sample-level CVs allow segments of the same EEGrecording to beassigned in both the training and the validation set, while subject-level CVs ensure that data from individual subjects are not mixed between sets.

both sample-based and subject-based strategies. The comparison is conducted across three supervised cross-subject classification tasks (brain-computer interface, Parkinson’s disease, and Alzheimer’s disease classification) using four established EEG-DL architectures of increasing complexity (ShallowConvNet, EEGNet, DeepConvNet, and Temporalbased 1D ResNet). Initially, traditional sample-based and subject-based CVs are compared to determine the extent to which model inference is affected by subject-specific characteristics, potentially introducing bias. Subsequently, traditional and nested subject-based CVs are compared to evaluate the consequences of lacking independent validation and test sets. Finally, variations in accuracies derived from nested and non-nested subject-based cross-validation strategies are analyzed in relation to model complexity, assessing whether certain approaches potentially favor more complex models.

Asnotedin[9,10],biosignalslikeEEGarecharacterized by strong subject-specific characteristics that can be learned during training and exploited by the model during inference. This can lead to overfitting and unrealistic performance estimates on unseen subjects. However, sample-based methods remain common in deep learning-based EEG data analysis. According to Brookshire et al. [11], who reviewed a total of 63 deep learning studies on translational EEG, only a small percentage (27.0%) unambiguously avoided this type of data leakage. Consequently, there has been a growing emphasis on subject-based cross-validation methods, such as the Leave-N-Subjects-Out (LNSO) or the Leave-One-SubjectOut (LOSO), which aim to develop generalizable models that are less sensitive to the high inter-subject variability.

Paper structure: The outline of this paper is as follows. Section 2 describes in detail the experimental setting. Section 3 presents the results, which are discussed with their limitations in section 4. Finally, a conclusion is drawn in section 5.

#### 2. Methods

This section describes in detail important methodological aspects. It follows the checklist provided in [18], which lists all the features a research work should report to improve result reproducibility without affecting readability. These include: dataset selection, data preprocessing, models’ architecture, data partitioning and cross-validation schemes, training hyperparameters, and model evaluation. Additional details can be found within the supplementary materials and the openly available source code repository.

Quantitative analyses have been conducted to evaluate differences between traditional sample-based and subjectbased cross-validation methods, underscoring the importance of using the latter in EEG deep learning studies [12, 13]. Nonetheless, even standard subject-based CV methods do not align well with DL paradigms. To avoid overfitting on the training data, EEG-DL models necessitate a separate independent set for early stopping purposes. This is crucial for estimating the generalization error during training and halting the process if improvement does not occur over a specified number of epochs. Unfortunately, this process is frequently conducted on the validation set, which is subsequently used to evaluate the model, leading to data leakage and reinforcing overfitting tendencies [14, 15, 16]. To address this issue, [17] proposed a nested subject-based CV approach, characterized by separate validation and test sets. This methodology, formalized in [7] as Nested-LeaveN-Subjects-Out (N-LNSO), allowed to move to a trainvalidation-test framework, which is more suited for EEG-DL applications, albeit with increased computational costs.

##### 2.1. Dataset selection

The analysis was conducted on four different opensource datasets. Each of them was selected from OpenNeuro1 [19], an established open platform used by neuroscientists to share neuroimaging data associated to published research studies, with a digital object identifier. This platform was selected because it specifically requires data to be organized in BIDS format, a standardized data structure format for neuroimaging data [20]. Such feature facilitates the exploitation of automated preprocessing and harmonization tools such as [21], enhancing study reproducibility. Furthermore, all selected datasets include raw EEG data recorded at least with the minimum number of channels suggested in the American Clinical Neurophysiology Society (ACNS) guidelines [22], i.e., 19 plus 2 for contralateral referencing.

The variety of possible cross validation variants leads to inconsistencies in results, complicating comparisons across studies and causing uncertainty on the selection of an optimal approach. Despite this, a comprehensive evaluation of the precise impact of this important aspect is still missing.

Selected data were used to construct three different and widely investigated classification tasks, namely:

Contributions: This work aims at thoroughly investigating the role of data partition on the performance assessment of EEG-DL models through cross-validation analysis. The investigation involves a comparison of five distinct cross-validation settings from three main categories, as described in subsection 2.3. These categories encompass

• Parkinson: a binary pathology classification task. It aims to distinguish between Parkinson’s off-medication and healthy subjects. EEG has been investigated as a noninvasive, low-cost technique to be used in Parkinson’s

1[Online] Available: https://openneuro.org/

- Table 1 Dataset description.

number of classes

number of windows

number of subjects

original sampling rate [Hz]

number of channels

task description

task acronym

dataset ID

original reference

Motor/Imagery left vs right fist

ds004362 A1-A2 64 160 109∗ 9495 4

BCI ds002778 CMS-DRL 41 512 31

Control vs Parkinson’s off-medication

Parkinson

8608 2

ds003490 CPZ 64 500 50 ds004504 A1-A2 19 500 88 17252 3

Control vs Alzheimer vs FT-dementia

Alzheimer

*three subjects were excluded from the analysis due to inconsistent sampling rate and trial length

clinical diagnosis, with deep learning applications producing promising results [4].

- • Alzheimer: a three-classes pathology classification task. It aims to distinguish between control, Alzheimer’s, and Frontotemporal Dementia subjects. Similar to Parkinson’s applications, deep learning has been recently investigated as a promising tools for analyzing the nonlinear dynamics of EEGs that characterize neurological disorders [5].
- • BCI: a non-clinical four-classes classification task. It aims to distinguish between left/right imagined/executed fist’s movements. BCI is a widely studied EEG application that found potential usages both in industry (e.g., operative security in critical conditions) and in medicine (e.g., stroke rehabilitation) [23, 24].

A preliminary analysis with two additional tasks is provided in the Supplementary Material (Section A.7). Further acquisition details for each dataset are summarized in Table 1. The next sub-paragraphs concisely describe them.

###### 2.1.1. Parkinson’s 1 - ds002778

- This dataset [25] collects resting-state eyes open EEG

recordings (duration 195.7 ± 18.8 seconds) from 15 Parkinson’s patients and 16 age matched healthy controls (respectively 63.3 ± 8.2 years, 63.5 ± 9.7 years). Healthy subjects have only one session, while Parkinson’s have two: the first contains records from Parkinson’s patients who discontinued medication for at least 12 hours before the session (sesoff), while the second include records of the same patients under medication (ses-on). For the following analysis, only the off-medication session was included. In addition, since the number of subjects is too low to perform proper data partition strategies, this dataset is used together with the Parkinson’s 2 dataset (ds003490), described below.

2.1.2. Parkinson’s 2 - ds003490

- This dataset [26] contains resting-state eyes open/closed

and auditory oddball EEG recordings (duration 595.9±74.0 seconds) from 25 Parkinson’s patients and 25 age matched healthy controls (respectively 69.7 ± 8.7 years, 69.3 ± 9.6 years). Similarly to the previous dataset, healthy subjects have only one session, while Parkinson’s patients have offmedication (at least 15 hours) and on-medication recordings.

- 2.1.3. Alzheimer’s - ds004504 This dataset [27] collects resting-state eyes closed EEG

recordings (duration 802.2±140.3 seconds) from 23 subjects diagnosed with frontotemporal dementia, 36 Alzheimer’s patients, and 29 age matched healthy controls (respectively 63.7 ± 8.2 years, 66.4 ± 7.9 years, and 67.9 ± 5.4 years). All the subjects have only one session, which was used in this work.

- 2.1.4. BCI - ds004362 This dataset contains resting-state, motor movement, and

motor imagery records of 109 adult healthy subjects (age 39 ± 11 years). All subjects have multiple records acquired during a single session (duration 114.5 ± 22.0 seconds). In particular, there are two resting-state eyes open/closed EEG acquisition and three repetitions of four different trial-based tasks, namely:

- Task 1. Open and close left or right fist.
- Task 2. Imagine opening and closing left or right fist.
- Task 3. Open and close both fists or feet.
- Task 4. Imagine opening and closing both fists or feet.

Trials from tasks 1 and 2 were considered to perform the ‘BCI’ task. Furthermore, subjects with ID 88, 92 and 100, have been excluded due to inconsistent sampling rate and trial length, as already done in other works [28, 29].

##### 2.2. Data preprocessing

All the selected recordings were preprocessed with taskspecific pipelines. Each of them reflects the best possible configuration according to a recent analysis on the role of preprocessing in EEG-DL applications [7]. Pipelines are composed by common steps adopted by both clinicians [30] and deep learning practitioners [31], and are summarized in Table 2. Preprocessing was done with BIDSAlign2 [21] (v1.0.0), with the sole exception for the final standardization, downsampling, and windows extraction steps, which were performed online within the Python environment as part of the data loading operations during model training. A detailed description of each step and relative parameters is provided below, sorted by their order of execution.

2https://github.com/MedMaxLab/BIDSAlign

other. If the calculated probability falls within a predefined range set by the user, the IC is rejected. For this study, the rejection thresholds were set as follows: [90%, 100%] for noisy classes and [0%, 10%] for the brain category. These values were selected to ensure the rejection of both predefined and other artifacts without excessive removal of brain activity. The number of rejected components may vary depending on the quality of the EEG signal.

- Table 2 Preprocessing pipelines for each task.

preprocessing step BCI Parkinson Alzheimer non-EEG channels removal

✓ ✓ ✓

time segments removal ✓ ✓ DC component removal ✓ ✓ ✓

∙ bad-channel removal: flat or extremely noisy channels are removed using the ‘clean_rawdata’ plugin (a BIDSAlign dependency) with default parameters.

resampling ✓ ✓

filtering ✓ ✓ ✓ automatic independent component rejection

∙ bad-time windows correction: the Artifact Subspace Reconstruction (ASR) algorithm [34] with default parameters was used to detect and correct bad-time windows, i.e. particularly noisy portions of the signal.

✓ ✓ bad-channel removal ✓

bad-time windows correction with ASR

✓ spherical interpolation of removed bad-channels

∙ spherical interpolation: previously removed bad channels are interpolated with the spherical method [35].

✓ re-reference ✓ ✓ ✓

∙ re-reference: EEG recordings are re-referenced to the common average.

template alignment ✓ ✓ trials extraction ✓ standardization ✓ ✓ ✓

∙ template alignment: EEG signals collected in the Parkinson’s 1 dataset have a lower channel count compared to the Parkinson’s 2. For this reason, only channels in common were selected. In addition, data for the ‘BCI’ task were aligned to the International Federation of Clinical Neurophysiology (IFCN) 10-10 standard containing 61 channel, thus removing 3 channels.

downsampling ✓ ✓ ✓ windows extraction ✓ ✓

∙ non-EEG channels removal: other biosignals stored together with the EEG and usually included as extra channels have been removed.

∙ trials extraction: BCI trials were extracted using the event files provided by original authors. Whenever possible, if the trial was few samples shorter, a piece of the next adjacent resting-state part of the EEG signal (rest portion between trials) was included to make the trial long 4.1 seconds, which is the intended length.

∙ time segments removal: the first and last 8 seconds of each recording have been removed to exclude potential divergences in the signal caused, for example, by the instrumentation. This step makes more accurate the subsequent artifact handling operations, which can potentially remove important parts of the brain activity when the input signal is very noisy.

∙ downsampling: During the import of preprocessed files within the Python environment, data were further downsampled to 125 Hz to improve computation and reduce the GPU’s memory occupation. BCI trials, which have an original sampling rate that is not multiple of 125Hz, have been resampled with the windowed sinc interpolation method, Von Han window, provided by the ‘torchaudio’ library [36].

∙ DC component removal: The channel-wise direct current (DC) voltage was subtracted from each EEG. More formally, denoting the original EEG signal by a matrix 𝐗 ∈ ℝ𝐶×𝑇, where C represents the number of channels and T the sequence length, the new DC-subtracted signal 𝐗′ ∈ ℝ𝐶×𝑇 can be defined as:

∙ standardization: a final z-score operator was applied along the EEG channel dimension. This step transforms each EEG channel into a signal with 𝜇=0 and 𝜎=1.

𝐗′ = 𝐗 − 𝐱̄𝑐diag(𝐈𝑇 ) (1) with 𝐱̄𝑐 ∈ ℝ𝐶×1 the vector of means of the channels.

∙ windows extraction: EEG data for the Parkinson’s and Alzheimer’s tasks were partitioned into non-overlapping 4s windows. This step was not applied to BCI data due to the trial extraction step.

∙ resampling: EEG records with a sampling rate higher than 250Hz were resampled to 250Hz.

∙ filtering: EEG signals were filtered with a pass-band Hamming windowed sinc FIR filter between 1Hz and 45Hz.

##### 2.3. Cross-validation strategies

∙ automatic independent component rejection: Independent Components (IC) were extracted using the ‘runica’ algorithm [32], with no limit on their number; then, components were automatically rejected using IClabel [33], a deep learning classifier commonly used in state-of-the-art EEGpreprocessingpipelines.ICLabelcalculatestheprobability of each IC belonging to one of seven categories: brain, muscle, eye, heart, line noise, channel noise, or

To evaluate the effects of the data partition on the performance of EEG-DL classifiers, 5 different cross-validation strategies were investigated. They differentiate for the number of folds, the number of independent sets, and the way EEG windows are distributed across them. CVs can be grouped in three main categories, schematized in Figure 1, and concisely described below.

|[Figure 2]<br><br>S1 S2 S3 S4 S5 S6<br><br>|[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>|
|---|
<br><br>Metrics<br><br>Validation sample<br><br>fold<br><br>Train sample<br><br>fold<br><br>|[Figure 8]<br><br>[Figure 9]<br><br>[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>|
|---|
<br><br>|[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>[Figure 17]<br><br>|
|---|
<br><br>|[Figure 18]<br><br>[Figure 19]<br><br>[Figure 20]<br><br>[Figure 21]<br><br>[Figure 22]<br><br>|
|---|
<br><br>|[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]<br><br>[Figure 26]<br><br>[Figure 27]<br><br>|
|---|
<br><br>|[Figure 28]<br><br>[Figure 29]<br><br>[Figure 30]<br><br>[Figure 31]<br><br>[Figure 32]<br><br>|
|---|
<br><br>|[Figure 33]<br><br>[Figure 34]<br><br>[Figure 35]<br><br>[Figure 36]<br><br>[Figure 37]<br><br>|
|---|
<br><br>|[Figure 38]<br><br>[Figure 39]<br><br>[Figure 40]<br><br>[Figure 41]<br><br>[Figure 42]<br><br>|
|---|
<br><br>|[Figure 43]<br><br>[Figure 44]<br><br>[Figure 45]<br><br>[Figure 46]<br><br>[Figure 47]<br><br>|
|---|
<br><br>|[Figure 48]|
|---|
<br><br>|[Figure 49]|
|---|
<br><br>(A) Sample-based K-Fold Cross Validation|[Figure 50]<br><br>S1 S2 S3 S4 S5 S6<br><br>S1 S2 S3 S4 S5 S6<br><br>S1 S2 S3 S4 S5 S6<br><br>OuterFolds<br><br>InnerFolds<br><br>[Figure 51]<br><br>[Figure 52]<br><br>[Figure 53]<br><br>[Figure 54]<br><br>[Figure 55]<br><br>[Figure 56]<br><br>windows 4 [s]<br><br>Metrics<br><br>Test<br><br>subject<br><br>outer fold<br><br>Train + Val<br><br>subject outer fold<br><br>Train<br><br>subject inner fold<br><br>Validation<br><br>subject inner fold<br><br>(C) Nested-Leave-N-Subject-Out Cross Validation|
|---|---|
|[Figure 57]<br><br>S1 S2 S3 S4 S5 S6<br><br>S1 S2 S3 S4 S5 S6<br><br>S1 S2 S3 S4 S5 S6<br><br>Metrics<br><br>Validation<br><br>subject fold<br><br>Train subject<br><br>fold<br><br>(B) Leave-N-Subject-Out Cross Validation| |

InnerFolds

OuterFolds

Metrics

Metrics

- Figure 1: Schematic representation of the three categories of cross-validation investigated in this work, inspired by [7]. (a) Sample-based K-Fold (K-Fold) randomly assigns windows of the same EEG both in the training and in the validation set, ignoring the subject; (b) Leave-N-Subjects-Out (LNSO or LOSO if N=1) randomly assigns windows of the same subject either in the training or in the validation set (not in both); (c) Nested-Leave-N-Subjects-Out (N-LNSO or N-LOSO) introduces a nested level for the creation of multiple train-validation splits for each test split. Models are trained on the training set, and evaluated on test set, if available; otherwise, the validation set is used. This procedure generates an ensemble of performances, which is used for the subsequent cross-validation comparisons. The training is controlled using early stopping criteria on the validation set. Note that for (a) and (b), the usage of the validation set to both monitor the training and evaluate the model introduces data leakage, which is, however, considered in the following analysis.

- • Sample-basedK-Fold:astandardK-Foldcross-validation, where windows of the same EEG recording can appear both in the training and in the validation set. While still used in recent applications [37], this approach has the disadvantage of not providing accuracy estimates on unseen subjects. However, EEG signals are characterized by strong subject-specific characteristic, which can be learned during the training and leveraged by the models during inference, potentially generating optimistic results [9]. This study considers a 10-Fold sample-based crossvalidation, which will be referred to as K-Fold.
- • Leave-N-Subjects-Out: also called subject-based crossvalidation. It is a variant of the sample-based K-Fold cross-validation where folds are created by randomly assigning EEG windows of the same subject either in the training or in the validation set; hence, it allows to validate the model only on samples from unseen subjects, providing more realistic accuracy estimates. However, this approach does not consider separate validation and test

sets to respectively control the training and evaluate the model, which is crucial to train EEG-DL models that are notably known to be very susceptible to overfitting. Several papers have used the validation set to both monitor the training and evaluate the model; yet, this approach is not appropriate since it introduce data leakage, as described in [17]. This study considers a 10-Fold subject-based crossvalidation, which will be referred from here as LNSO, and a Leave-One-Subject-Out cross-validation, where each fold is composed by the records of only one subject. From here, the Leave-One-Subject-Out cross-validation will be referred to as LOSO.

• Nested-Leave-N-Subjects-Out: as proposed in [7, 17], introduces a nested level for the creation of multiple trainvalidation-test splits. Each triplet is created by concatenating two different subject-based cross-validation (LOSO or LNSO). The first determines the subjects to use as test set, called outer folds in Figure 1, while the second further partition the remaining subjects to create the training and

validation sets (inner folds). In this way, a model can be trained, monitored, and evaluated on independent sets, removing any form of data leakage. However, the addition of a nested level increases the total number of training and computational time. Nested approaches result in a total of 𝑁𝑜𝑢𝑡𝑒𝑟 × 𝑁𝑖𝑛𝑛𝑒𝑟 training, which can reach the limit value of 𝑁𝑠𝑢𝑏𝑗 × (𝑁𝑠𝑢𝑏𝑗 − 1) in case of a fully Nested-LeaveOne-Subject-Out cross-validation. This study considers a 10-outer/10-inner nested subject-based cross-validation (100 partitions),whichwill be referred to as N-LNSO, and a fully Nested-Leave-One-Subject-Out cross-validation, characterized by the concatenation of two LOSO, which will be referred to as N-LOSO. Test sets defined by outer folds perfectly overlap validation sets of standard subjectbased CVs (LNSO or LOSO), which is crucial for the comparative analysis presented in subsections 3.2 and 3.3.

Department of Neuroscience computing node, composed of three NVIDIA A30 GPU devices (CUDA 12.2). Further details not reported in the following sub-paragraphs can be found in the supplementary materials and in the openly available source code.

- 2.4.1. EEG Architectures Four established EEG-DL models with increasing com-

plexity (in terms of model size and framework, see [40]) have been selected for analysis: EEGNet, ShallowConvNet, DeepConvNet, and Temporal-based 1D ResNet [41, 42, 43].

EEGNet is a compact deep neural model widely used for the tasks being investigated. It consists of a series of convolutional layers that perform operations on either the temporal (sample) or spatial (channel) dimensions. ShallowConvNet and DeepConvNet are two other architectures related to the EEGNet family [28]. ShallowConvNet is a more compact version of EEGNet, while DeepConvNet includes additional convolutional layers in its encoder block. Similarly, ResNet is a deeper architecture recently employed in several EEG-based classification tasks, thanks to recent advances in unsupervised pretraining strategies such as selfsupervised learning [44, 45]. Numerous variants of EEGbased ResNet models exist in the literature, primarily differing in the number of stacked residual blocks and the combination of temporal and spatial layers within those blocks [46]. This study will use a variant of the ResNet34 model characterized by only temporal (horizontal) kernels, as proposed in [43]. From this point forward, this model will be referred to as T-ResNet.

Model complexity was evaluated considering several factors, including the number of layers (architecture depth), thenumberoflearnableparameters, andtherequired computationalresourcesintermsoftrainingtimeandGPUmemory allocation. Consequently, the number of parameters ranges from less than 100000 in ShallowConvNet configurations to more than a 1000000 in T-ResNet ones. A schematic representation of each model can be found in the supplementary materials, with further implementation details within the openly available source code.

- 2.4.2. Training Hyperparameters To ensure consistent results in this study, a custom seed

To summarize, Figure 1 illustrates three main categories of cross-validation, which differ in terms of the number of independent sets (nested vs. non-nested) and the distribution of the EEG windows (sample-based vs subject-based). Furthermore, the number of left-out subjects (N) is also an important cross-validation parameter. When N is set to 1, two additional settings emerge: Leave-One-Subject-Out (LOSO) and the Nested-Leave-One-Subject-Out (N-LOSO). In EEG deep learning studies, the Leave-One-Subject-Out approach is frequently used to assess the performance of deep neural models. Thus, it is crucial to consider it separately to evaluate its reliability. The same consideration applies for the Nested-Leave-One-Subject-Out method, which is considered separately from the Nested-Leave-N-Subjects-Out (N-LNSO).

Considering this, a total of CV five settings based on the

- 3 categories described above was used for the comparisons presented in Section 3. Each of these settings has been assigned a unique acronym, which is summarized below:

- • Sample-based K-Fold, called K-Fold.
- • Leave-N-Subjects-Out, called LNSO.
- • Leave-One-Subject-Out, called LOSO.
- • Nested-Leave-N-Subjects-Out, called N-LNSO.
- • Nested-Leave-One-Subject-Out, called N-LOSO.

(83136297) was randomly selected and fixed. This approach minimizes randomness in the code and enhances the reproducibility of results, as suggested in [18]. Fixing the random seed affects the initialization of model weights and the creation of mini-batches. It also affects the subject assignment in the LNSO and N-LNSO cross-validation settings (LOSO and N-LOSO remain deterministic since each fold consists of a single subject). Given the high variability of the results presented in Section 3, an analysis of the effect of the random seed on cross-validation accuracy estimation is provided in Section A.2 of the Supplementary Materials. This analysis aims to confirm the consistency of the findings of this study.

##### 2.4. Implementation details

The remaining steps of the experiment were implemented within a Python environment. In particular, models were trained using SelfEEG3 [38] (v0.2.0) and figures were generated with Seaborn [39] using the Wong’s colorblind palette. Experiments were conducted mainly on the Padova Neuroscience Center computing node composed of two NVIDIA Tesla V100 GPU devices (CUDA 12.1), to speed up the entire process by running multiple training sessions in parallel. The maximum GPU memory allocation was 8.01 GB. Additionally, the large number of training instances of the N-LOSO (see Section A.1 of the Supplementary Materials) was completed with the addition of the

Models were initialized using Pytorch’s [47] default settings, which varies according to the specific type of layer.

3https://github.com/MedMaxLab/selfEEG

with TP𝑖 and FN𝑖 being respectively the true positives and the false negatives for class 𝑖. Model performance against other metrics, such as the weighted F1-score, can be found in Section A.3 of the Supplementary Material, as well as in the openly available source code.

- Table 3 Learning rate grid.

Model BCI Parkinson Alzheimer ShallowConvNet 7.5 ⋅ 10−4 2.5 ⋅ 10−4 5.0 ⋅ 10−5

EEGNet 1.0 ⋅ 10−3 1.0 ⋅ 10−4 7.5 ⋅ 10−4 DeepConvNet 7.5 ⋅ 10−4 2.5 ⋅ 10−4 7.5 ⋅ 10−4

#### 3. Results

The analysis highlighted differences not only between sample-based and subject-based CV approaches, but also between nested and non-nested ones. To organize the large volume of information gathered from the thousands of trained models, several figures are presented and described in three separate sub-paragraphs. Each sub-paragraph compares two cross-validation approaches, namely:

T-ResNet 5.0 ⋅ 10−4 1.0 ⋅ 10−5 5.0 ⋅ 10−5

Models were trained with Adam optimizer (𝛽1 = 0.9, 𝛽2 = 0.999,no weightdecay)[48], using batchsizeof64andcross entropy as loss function. The maximum number of epochs was set to 100. In addition, an early stopping was used to control the training and restore the model’s best weights in case the validation loss did not improve for 15 epochs. It is worth recalling that this approach produces biased results in standard cross-validation strategies, because they do not have separate validation and test sets. Using the same set to both stop the training and evaluate the model put the parameter’s optimization search in an optimistic environment, introducing a minor but still relevant form of data leakage. This is a known but often ignored issue and it was purposely kept in the following analysis to evaluate its effect. Further details on this matter are discussed in Section 4. Following the strategy described in [7], a custom learning rate was selected for each combination of task and model, as summarized in Table 3. Learning rates were determined by evaluating the balanced accuracy of validation sets (considering both median and inter-quartile range) for a subset of models trained using the N-LNSO cross-validation scheme (see Figure 1). This evaluation involved searching over a non-uniform discrete grid of 13 potential values: 1.0 ⋅ 10−3, 7.5 ⋅ 10−4, 5.0 ⋅ 10−4, 2.5 ⋅ 10−4, 1.0 ⋅ 10−5, 7.5 ⋅ 10−5, 5.0 ⋅ 10−5, 2.5 ⋅ 10−5, 1.0 ⋅ 10−6. This procedure provides a good compromise between computational efficiency and the quality of the selected hyperparameters. It also avoids bad practices, such as cross-validating the entire dataset, and minimizes potential selection bias caused by the high inter-subject variability, which can lead to suboptimal values when the process is conducted on a single hold-out data partition. Furthermore, it does not favor any of the investigated cross-validation settings, as the N-LNSO validation accuracies are not considered in the comparative analysis. Lastly, learning rates slightly decrease during training following an exponential scheduler with 𝛾 = 0.995.

- • LNSO vs. K-Fold (subject-based vs Sample-based CV)
- • LNSO vs. N-LNSO
- • LOSO vs. N-LOSO and aims at answering the following questions:
- • Are there differences between sample-based and subjectbased CVs?
- • Are there differences between nested and non-nested subject-based CVs?
- • Are variations in the accuracies between nested and nonnested subject-based CV strategies influenced by model complexity?

The third question is particularly relevant, because it addresses the current trend of developing larger and deeper EEG-DL models without increasing the amount of data on which they are trained (e.g., [50]). In supervised deep learning, overparameterization has been found to improve the optimization landscape of a problem, often with minimal impact on generalization [51]. However, the effects on generalizability may be more pronounced when dealing with highly complex and noisy data, like EEG signals. Additionally, the limitations of traditional cross-validation methods may obscure these effects, leading to an overestimation of model generalizability and potentially favoring overparameterized models over shallow models. Therefore, this study aims to investigate whether EEG-DL models take advantage of limitations of non-nested cross-validation methods—such as data leakage and improper usage of the validation set—to the same extent.

##### 3.1. Sample-based vs subject-based cross-validation

- 2.4.3. Performance Evaluation The performance of each model was evaluated using

Figure 2 presents a comparative analysis of LNSO and sample-based K-Fold results. Regardless of the model, KFold results consistently outperform those of the LNSO, particularly in pathologic tasks, where balanced accuracies of ShallowConvNet (Panel A), EEGNet (Panel B), and DeepConvNet (Panel C) almost reach 100%. Furthermore, the variance of results shows significant divergence between the two cross-validation methods. In particular, differences between the minimum and maximum balanced

the balanced accuracy, which can be defined as the macro average of recall scores per class [49]. Hence, for a multiclass classification problem, with 𝐾 classes:

TP𝑖 TP𝑖 + FN𝑖

∑𝐾

1 𝐾

(2)

AccuracyBalanced =

𝑖=1

## Sample-based K-Fold vs. Leave-N-Subjects-Out

Model: ShallowConvNet

Model: EEGNet

100

100

(A)

(B)

90

90

BalancedAccuracy%

80

80

70

70

60

60

50

50

40

40

Sample-based K-Fold

Sample-based K-Fold

30

30

Leave-N-Subjects-Out

Leave-N-Subjects-Out

Parkinson Alzheimer BCI

Parkinson Alzheimer BCI

Model: DeepConvNet

Model: T-ResNet

100

100

(C)

(D)

90

90

BalancedAccuracy%

80

80

70

70

60

60

50

50

40

40

Sample-based K-Fold

Sample-based K-Fold

30

30

Leave-N-Subjects-Out

Leave-N-Subjects-Out

Parkinson Alzheimer BCI

Parkinson Alzheimer BCI

Task

Task

- Figure 2: Balanced accuracy comparison between Sample-based (K-Fold, in blue) and subject-based (LNSO, in orange) 10-Fold cross-validations. The sub-figures display results for different deep learning architectures: ShallowConvNet (Panel A), EEGNet (Panel B), DeepConvNet (Panel C), and T-ResNet (Panel D). Results are shown across all tasks. Independently from the model, there is a performance drop and an increased variance when switching to subject-based cross-validation methods, particularly in pathology classification tasks. Additionally, ShallowConvNet, the smallest model, achieved the highest median accuracies, highlighting a potential drawback in the usage of more complex models.

accuracies often exceed 30% across all the four models, particularly in the Parkinson’s and Alzheimer’s disease classification tasks. Similar trends are observed in the BCI results both in terms of performance bias and variance, albeit to a much lower degree. Smaller architectures yield higher performances in subject-based cross-validation. Specifically, ShallowConvNet achieves median balanced accuracies of 85.4% for Parkinson’s task, 58.1% for Alzheimer’s, and 54.7% for BCI. In contrast, worst performances are registered by DeepConvNet for Parkinson (53.3%), and by TResNet (Panel D) in both Alzheimer’s (43.2%) and BCI (47.6%) tasks. These results suggest potential limitations associated with deploying larger, non-pretrained deep learning models.

##### 3.2. Leave-N-Subjects-Out vs Nested-Leave-N-Subjects-Out

Figure 3 illustrates the results of the N-LNSO in relation to those from the LNSO. As noted in subsection 2.3, this comparison is enabled by the complete overlap between the test sets of the N-LNSO and the validation sets of the LNSO. In particular, each set of N-LNSO accuracies (column of points) having the same x-axis value—which is equal to the LNSO accuracy calculated from the partition using as validation set the identical group of subjects used as test set in the N-LNSO—highlights how model performance is influenced by the definition of the validation set. Focusing on the model architecture, a relationship emerges between the variability of N-LNSO results and model complexity.

### Leave-N-Subjects-Out (LNSO) vs. Nested-Leave-N-Subjects-Out (N-LNSO)

Model: ShallowConvNet

Model: EEGNet

100

100

(A)

(B)

N-LNSOBalancedAccuracy%

90

90

80

80

70

70

60

60

50

50

40

40

Parkinson Alzheimer BCI

Parkinson Alzheimer BCI

30

30

20

20

20 30 40 50 60 70 80 90 100

20 30 40 50 60 70 80 90 100

Model: DeepConvNet

Model: T-ResNet

100

100

(C)

(D)

N-LNSOBalancedAccuracy%

90

90

80

80

70

70

60

60

50

50

40

40

Parkinson Alzheimer BCI

Parkinson Alzheimer BCI

30

30

20

20

20 30 40 50 60 70 80 90 100

20 30 40 50 60 70 80 90 100

LNSO Balanced Accuracy %

LNSO Balanced Accuracy %

- Figure 3: Comparison of balanced accuracy between Nested-Leave-N-Subjects-Out (N-LNSO) and Leave-N-Subjects-Out (LNSO). The sub-figures display results for different deep learning architectures: ShallowConvNet (Panel A), EEGNet (Panel B), DeepConvNet (Panel C), and T-ResNet (Panel D). Results are shown across all tasks, with light blue representing Parkinson’s, green for Alzheimer’s, and yellow for BCI. Each column of points shows N-LNSO results for architectures trained on different train/validation partitions (inner folds) but evaluated on the same test set (outer fold), as a function of LNSO accuracies. Notably, performance differences between the two CVs increase with higher LNSO fold accuracies. The regression lines’ slopes (in red), always less than 1, further highlight this trend. Additionally, more complex models exhibit greater result variance.

ShallowConvNet (Panel A) appears less sensitive to changes in the training/validation partition (inner folds), resulting in differences between the minimum and maximum balanced accuracies that typically remain below 20%. The same can be observed in EEGNet (Panel B) for the Alzheimer’s task. In contrast, both DeepConvNet (Panel C) and T-ResNet (Panel D) exhibit greater performance variability, with TResNet displaying accuracy differences exceeding 40% in the Parkinson’s task. Furthermore, median N-LNSO test accuracies derived from groups of partitions sharing the

same test set (i.e., all inner folds corresponding to a specific outer fold, as shown in Figure 1-C) often fall below the bisector. This observation might support the hypothesis that traditional subject-based cross-validations tend to produce inflated results due to the lack of independent validation and test sets, as noted in [17]. Specifically, since N-LNSO combines two 10-Fold subject-based CVs, we can identify 30 groups (10 for each task) of 10 accuracies derived from the same test set, indicated by the columns of points in Figure 3). Among those 30 groups, only 5, 4, 9, and 8,

exhibit median balanced accuracies exceeding those of the LNSO for EEGNet, ShallowConvNet, DeepConvNet, and TResNet, respectively. Additionally, differences in balanced accuracy tend to increase with higher LNSO accuracies, a trend supported by the slope of the regression lines showed in the same figure. However, ShallowConvNet, being the simplest model, appears less affected by this trend, as con-

#### 4. Discussion

Developing deep learning pipelines for EEG applications is a complex task. Minimal variations in the experimental setup can lead to significant variations in the results, with data partitioning being particularly influential. In this field, the presence of datasets containing only a few dozen subjects does not allow the use of hold-out strategies, as model performance is highly dependent to the composition of the test set. For instance, the test set accuracies derived from individual splits of the N-LNSO, illustrated in figure 3, demonstrate how specific partitions can favor one architecture over another. Therefore, it is crucial to assess model performance using cross-validation strategies. However, even cross-validation procedures must address the high inter-subject variability inherent in EEG signals, as ignoring this can lead to unrealistic performance evaluations.

firmed by its regression slope of 0.83 (𝑅2adj = 0.91), which is the closest to 1.

##### 3.3. Leave-One-Subject-Out vs Nested-Leave-One-Subject-Out

Figures 5, 6, and 7 provide a comparative analysis of the results obtained from LOSO and N-LOSO results. As highlighted in the previous comparison, the absence of independent validation and test sets might explain the noticeable increase in the LOSO performance metrics. Specifically, Table 4 summarizes the proportion of subjects for which the median N-LOSO test accuracy outperform that of the LOSO. This proportion remains below 10% for all the models in pathologic tasks and below 36% for the BCI task, although in the latter scenario, this increase may be attributed to the inherent characteristic of the task, as noted in subsection 3.1and elaboratedin section 4. Moreover, table

The comparative analysis in subsection 3.1 highlights that sample-based methods, which allow windows of the same EEG signal to appear both in the training and validation sets, do not satisfy this requirement. Sample-based methods fail to evaluate the model’s ability to generalize to entirely unseen subjects and overlook potential relationships between consecutive windows, even when they are temporally separated, potentially inflating performance results. Consequently, it is not surprising to observe significant drops in performance during the transition to subject-based methods, particularly in applications where each subject has a unique label reflecting their health status. The results in Subsection 3.1 offer a new perspective on the exceptionally high performance reported in recent scientific papers applying deep learning to EEG data. They suggest that such performances might stem more from the propensity of deep neural networks to overfit due to the inherent characteristics of EEG signals. These characteristics include subject dependence induced by biometric properties of the signal [52], inter-correlation of consecutive samples [11], and other factors such as non-stationarity [10]. The nearly perfect accuracies reported in many studies of the domain, such as [37, 53, 54, 55, 56], may not necessarily demonstrate that such deep learning models effectively capture the representative features of the condition under investigation. Instead, these accuracies may better reflect the models’ ability to recognize individual subjects by their EEG signals [52, 11].

- 4 compares median performance metrics alongside their interquartile ranges. Notably, LOSO results suggest a superiority of DeepConvNet in pathology classification tasks (ShallowConvNet exhibit comparable performance in BCI), with a median balanced accuracy of respectively 100.00% in Parkinson’s task and 90.62% in Alzheimer’s. However, when the evaluation is shifted to a nested scenario, it is ShallowConvNet, the smallest architecture, that achieves the highest performance, with a lower but still remarkable percentage change of median values.

Figures 5, 6, and 7 also highlight the dramatic subjectwise variability observed in N-LOSO results, despite training sets across inner folds differing by only a single left-out subject used for validation purposes. In the BCI task, the range between minimum and maximum balanced accuracies fluctuates between 20% and 30%; however, for the pathological tasks, these values exhibit a remarkable increase, sometimes encompassing the entirety of the accuracy spectrum.

Figure 4 further investigates possible relations between model complexity and performance declines in N-LOSO, presenting the subject-wise distributions of performance bias between LOSO and N-LOSO (Panel A), calculated as the median accuracy across all inner folds, alongside the interquartile ranges of N-LOSO (Panel B). Even in this case, no notable differences can be found when looking at BCI results. However, inboth clinical applications, T-ResNet (the largest model) distributions are centered at higher values compared to ShallowConvNet (the simplest model). Furthermore, the distributions of DeepConvNet showed greater variability, particularly for the Parkinson’s task, with upper whiskers reaching higher values.

Creating subject-specific representations is not equivalent to creating label-specific representations. If a model is overfitted to specific subjects, it will likely assign labels based on similarity to those seen during the training phase. Thus, the performance of the model is closely related to the degree of similarity between the training, validation and test sets, or more specifically, to how similar subjects with the same label (or health status) are to each other. This interpretation not only explains the observed variability in the folds of the LNSO but also clarifies why performance in the NLOSO setting can be closed to zero in some cases (Figures

###### 5 and 6). Performance metrics close to zero indicate that the model predictions are consistently incorrect. This situation is different from that of a random classifier, as it suggests that a

- Table 4 Comparative analysis between LOSO and N-LOSO balanced accuracies. The percentage changes indicate the amount of increase or decrease the N-LOSO balanced accuracy median and IQR values have relatively to the LOSO metrics, in percentage.

Balanced Accuracy Percentage Change N-LOSO vs LOSO

Balanced Accuracy Median [25𝑡ℎ−75𝑡ℎ]

Number of subjects

Task Model

LOSO N-LOSO Median IQR N-LOSO > LOSO

99.38 [80.95 − 100.00]

88.37 [50.00 − 100.00]

-11.08 +162.50 0/81

ShallowNet

97.83 [82.61 − 100.00]

76.68 [42.97 − 97.81]

###### -21.62 +215.36 2/81 DeepConvNet

EEGNet

Parkinson

100.00 [89.63 − 100.00]

81.67 [10.80 − 100.00]

###### -18.33 +760.51 1/81 T-ResNet

91.36 [75.00 − 97.67]

70.19 [35.71 − 91.50]

-23.17 +146.04 2/81

88.19 [48.64 − 97.34]

63.05 [10.58 − 91.54]

-28.51 +66.23 4/88

ShallowNet

94.42 [48.36 − 98.53]

59.95 [3.65 − 94.8]

###### -36.51 +81.70 9/88 DeepConvNet

EEGNet

Alzheimer

90.62 [36.19 − 99.00]

52.44 [5.44 − 93.12]

###### -42.13 +39.59 6/88 T-ResNet

73.94 [32.43 − 93.67]

45.15 [14.40 − 77.85]

-38.94 +3.62 7/88

58.97 [50.83 − 68.96]

53.56 [46.58 − 62.25]

-9.18 -13.54 14/106

ShallowNet

54.09 [47.48 − 63.18]

52.28 [45.24 − 60.16]

###### -3.34 +5.00 39/106 DeepConvNet

EEGNet

BCI

58.90 [48.04 − 67.28]

52.38 [44.57 − 62.04]

###### -11.06 -9.19 19/106 T-ResNet

48.85 [42.29 − 56.46]

46.00 [39.97 − 53.06]

###### -5.84 -7.59 31/106

Accuracy difference between LOSO and median N-LOSO. Distribution across subjects

(B) N-LOSODistributioninterquartileacrossrangesubjects(IQR).

(A)

100

90

Subject-wise[LOSOmed(N-LOSO)]AccAcc

ShallowConvNet

ShallowConvNet

EEGNet DeepConvNet

EEGNet DeepConvNet

80

90

| |
|---|

| |
|---|

70

80

T-ResNet

T-ResNet

Subject-wiseIQRN-LOSO

60

70

50

60

40

50

30

40

20

30

10

20

0

10

10

0

Parkinson Alzheimer BCI

Parkinson Alzheimer BCI

Task

Task

###### Figure 4: Subject-wise analysis of Nested-Leave-One-Subject-Out (N-LOSO) results. On the left, the distribution of differences across all subjects between the Leave-One-Subject-Out (LOSO) balanced accuracies and the median N-LOSO is evaluated for each model architecture and classification task. On the right, the interquartile range distribution of N-LOSO results for each subject is evaluated for the same architectures and classification tasks. Both figures highlight minimal differences in the BCI task, but reveal higher performance drops in pathologic tasks for more complex models such as T-ResNet.

decision rule has been learned, but it is ineffective for solving the task. This result raises fundamental concerns about the features learned by EEG deep learning models, underscoring the need to improve their interpretability in this domain.

enhances methodological rigor by ensuring that the left-out subjects remain unseen during training and are used solely to evaluate the trained model. However, it does not address how the selection of data for this additional set can influence model performance, potentially introducing a subtler form of result manipulation. Figures 5, 6, and 7 illustrate that specific training/validation/test partitions can yield higher performance than those from traditional subject-based crossvalidations. This finding reveals that it is possible to identify an optimal training/validation partition (inner fold) for each left-out subject (outer fold), resulting in a performance that exceeds that of a LOSO in terms of median value and interquartile range. Following this strategy, DeepConvNet would achieve median balanced accuracies of 100% (IQR: 0.6), 99% (IQR: 30), and 64% (IQR: 17) for the Parkinson’s, Alzheimer’s, and BCI tasks, respectively.

The dominance of subject-specific characteristics in the learned embeddings may also explain why performance on the BCI task is generally lower and with less variance. In the BCI task, each subject participated in trials of every possible motor/imagery movement, preventing the model from exploiting subject-specific characteristics as shortcuts to minimize the training loss. This may explain why reported performances, even in sample-based cross-validation methods, are relatively low, despite being above the baseline of random guessing classifiers (25% accuracy for a four-class classification problem). In addition, the selected dataset does not provide any information about the participants’ level of preparation for executing the trials, especially those involving motor imagery. The absence of such information complicates the identification of bad-trials to discard, contributing to another source of under-performance to consider during the analysis of the results. While this study focuses on cross-subject prediction, the BCI fieldand related EEG domains—includes real-world applications where it is acceptable to perform within-subject EEG data analysis by training subject-specific models. However, it is necessary to acknowledge the limitations posed by the high inter-subject variability and the properties of the learned embeddings, which may focus on dominant subject-specific features that are not necessarily representative of the task of interest in general. Understanding these limitations can lead to different interpretations of study results and promote research in critical areas such as model interpretability and generalizability. Enhancing model interpretability is crucial for understanding the features learned by EEG deep learning models, while improving model generalizability is essential for creating robust models applicable to real-world scenarios. This approach can help make models less vulnerable to performance drops that may arise from changes in the subject’s health or psychological state, which may alter their normal brain activity.

These results highlight the importance of using nested approaches in deep learning-based EEG data analysis to prevent overestimating model accuracy, which could otherwise occur under the guise of addressing the previously described issues. They also emphasize the need for developing novel software tools to standardize EEG data and create large-scale multicenter datasets. Such efforts could help mitigate the discrepancies between model complexity and the amount of training data. Given that the number of subjects is a primary source of variability, the release of large-scale datasets could significantly improve model generalizability and reduce the overfitting problems described above. Increasing the number of large-scale datasets would facilitate the effective exploration of promising DL architectures, such as transformers.

Nested methods provide more realistic accuracy estimates that address the aforementioned data leakage issues, though they require greater computational resources. This is important in deep learning-based EEG data analysis, where overparameterization can increase overfitting tendencies and early stopping serves as a key regularization technique (see Section A.6 of the Supplementary Materials).

##### 4.1. Guidelines for proper EEG model evaluation

This study highlights the relationship between data partitioning in deep learning and EEG, emphasizing the importance of selecting the appropriate partitioning strategy based on the specific research task. While data partitioning is a general concept in machine learning, its impact is especially pronounced in EEG due to the specific characteristics of the signals, such as their biometric features, the inter-correlation of consecutive samples, and factors like non-stationarity. These properties can cause the learning phase to focus on extracting features that are useful for minimizing the loss but not relevant to the task at hand.

An important issue identified in this study is the lack of independent validation and test sets in traditional subjectbased approaches (LNSO and LOSO). This absence can lead to data leakage or overfitting. To address this problem, the literature proposed two approaches. The first one involves using the validation set to both monitor training and evaluate the model, rather than creating a third independent set from a subset of training samples (e.g., [14, 15, 16]). This method is incorrect because training stops when the model parameters reach the highest possible validation accuracy. Data leakage occurs because validation data (which are also used to evaluate the model) are considered during training. Consequently, the model tends to overfit on the validation set, since it is used by the early stopping callback.

For research tasks targeting within-subject analysis via sample-based approaches, such as BCI experiments, models might be tailored to specific subject to enhance humanmachine interaction for the potential end user. Still, it is crucial to interpret the results carefully to avoid overstating claims. In contrast, research tasks like disease prediction require cross-subject analyses, as sample-based methods

The second approach consists in creating a third independent set from a subset of training data to monitor model performance during training (e.g., [57]). This method

heavily overestimate model generalizability, as discussed in subsection 3.1. Choosing an inappropriate model evaluation approach may result in inflated and unrealistic performance estimates, which can limit the usefulness of the results in real-world scenarios.

as the number of folds increases. This overlap can lead to gross underestimation of the variance in the cross-validation estimator and increase the risk of Type I errors. Although previous studies [58, 59] have proposed modified versions of the t-test for single or repeated cross-validations that yield more conservative inferences, these tests still assume that accuracies from the folds follow a Gaussian distribution. Furthermore,t-testsforcross-validationare intendedtocompare different classifiers within the same cross-validation, rather than comparing two cross-validations on the same classifier. The use of non-parametric tests is also inappropriate, as both the independence of observations within the same CV and the lack of fully paired observations are violated. Therefore, it is more rigorous to provide a thorough quantitative and objective assessment of the results rather than overlook these violations just to produce optimistic and worthless p-values.

Given the computational burden and the number of training instances, we suggest the following potential guidelines for selecting the most appropriate combination of outer and inner folds:

- 1. Datasets with 20 or fewer subjects: full N-LOSO (𝑁𝑠𝑢𝑏𝑗×(𝑁𝑠𝑢𝑏𝑗−1) training instances, maximum 380).
- 2. Datasets with up to 50 subjects: LOSO-outer/10-inner

nested CV (𝑁𝑠𝑢𝑏𝑗 × 10 training instances, maximum 500). In this case, each outer fold used as a test set will consist of a single left-out subject, while the inner folds will create validation sets comprising 10% of the remaining subjects.

- 3. Datasets with more than 50 subjects: 10-outer/10inner N-LNSO (always 100 training instances).

These recommendations balance computational costs with the effects of the number of folds in terms of the biasvariance trade-off. In point 1, the small number of subjects allows for computational feasibility with N-LOSO, and the increased variance in the results is justified by the improved performance estimation given the limited amount of data. In point 2, while the number of subjects is still insufficient to produce representative test sets for conducting an N-LNSO, it is too large for a N-LOSO. A practical solution is to reduce the number of training instances by replacing the inner LOSO with a 10-fold LNSO. The recommendation against reversing the order (using 10 outer folds and LOSO inner) is based on the importance of early stopping as a key regularization technique in EEG deep learning applications. It is preferable to select the best weights based on a group of subjects to foster generalization to new subjects, rather than relying on a single subject that may be overfitted during training. In point 3, the number of subjects becomes too large to justify the computational burden of running an NLOSO cross-validation. In contrast, the N-LNSO provides an optimal compromise in terms of the bias-variance tradeoff. The choice of ten for both inner and outer folds aligns with commonpracticesandhelps assess the model’s stability against variation in the validation set.

- 4.2. Limitations and future work Although the figures and tables strongly support the

Secondly, while the analysis reveals strong differences among various cross-validation methods, it does not clarify whether these differences result from an overestimation of thegeneralizationerrorbyonemethodoranunderestimation by another. This question can be further investigated by considering the following point. Throughout the discussion, it has been repeatedly emphasized how traditional crossvalidation methods, when applied to EEG data, can introduce data leakage due to correlations between windows from the same signal and the manner in which training is monitored. As a result, these procedures are naturally inclined to provide optimistic results. To investigate and validate this hypothesis, a possible strategy may consist in adding a further nesting level to each of the investigated cross-validation methods in order to provide repeated measurements of the bias in the estimation of the generalization error. However, this proposal is computational demanding and still affected by the high inter-subject variability of EEG data that can heavily affect each measurements. Nevertheless, a preliminary analysis for the K-Fold vs LNSO and LNSO vs NLNSO scenarios, with further details on its implementation, is provided in section A.4 of the Supplementary Materials. This analysis confirms that both traditional cross-validation approaches tend to underestimate the generalization error and provide optimistic accuracies.

This study offers a rigorous analysis to the issues of overfitting and performance variability caused by data partitioning in EEG-based deep learning applications. However, future research should validate its findings in different experimental contexts. EEG data analysis using deep learning has a wide range of applications, including event-related potentials (ERPs), emotion and attention recognition, and sleep staging, to name a few. It also involves various training paradigms (e.g., transfer, learning, few-shot learning, selfsupervised learning), and levels of analysis (e.g., within, session, multi-center) that were not addressed in this study. Moreover, the variability in performance of EEG deep learning systems is influenced by several factors beyond data partitioning, such as data harmonization, preprocessing strategies [7], and random seed control. These factors deserve dedicated investigation in future works.

argumentpreviouslypresented,itisessentialtoacknowledge two main limitations of the study.

First, no statistical tests have been used to analyze the results. This decision is based on the violation of the assumptions required by both parametric and non-parametric statistic tests, specifically concerning the normality of the distribution of results and the independence of observations in this study. The violation of sample independence is particularly relevant, as different partitions of the same cross-validation share overlapping training sets, especially

(A) Model: ShallowConvNet - Task: Alzheimer

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85

(B) Model: EEGNet - Task: Alzheimer

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85

(C) Model: DeepConvNet - Task: Alzheimer

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85

(D) Model: T-ResNet - Task: Alzheimer

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85

Subject ID

###### Figure 5: Balanced accuracy comparison between Nested-Leave-One-Subject-Out (N-LOSO) and Leave-One-Subject-Out (LOSO) for the Alzheimer’s task. Each blue dot reports the subject-wise LOSO balanced accuracy resulted from a model trained on all the

(A) Model: ShallowConvNet - Task: Parkinson

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80

(B) Model: EEGNet - Task: Parkinson

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80

(C) Model: DeepConvNet - Task: Parkinson

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80

(D) Model: T-ResNet - Task: Parkinson

100

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

90

BalancedAccuracy%

80

70

60

50

40

30

20

10

0

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80

Subject ID

###### Figure 6: Balanced accuracy comparison between Nested-Leave-One-Subject-Out (N-LOSO) and Leave-One-Subject-Out (LOSO) for the Parkinson’s task. Each blue dot reports the subject-wise LOSO balanced accuracy resulted from a model trained on all the

Leave-One-Subject-Out (blue dots) vs. Nested-Leave-One-Subjects-Out (orange boxes)

(A) Model: ShallowConvNet - Task: BCI

90

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

BalancedAccuracy%

80

70

60

50

40

30

20

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105

(B) Model: EEGNet - Task: BCI

90

| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | |

BalancedAccuracy%

80

70

60

50

40

30

20

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105

(C) Model: DeepConvNet - Task: BCI

90

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

BalancedAccuracy%

80

70

60

50

40

30

20

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105

(D) Model: T-ResNet - Task: BCI

90

| | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | |

BalancedAccuracy%

80

70

60

50

40

30

20

5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105

Subject ID

- Figure 7: Balanced accuracy comparison between Nested-Leave-One-Subject-Out (N-LOSO) and Leave-One-Subject-Out (LOSO) for the BCI task. Each blue dot reports the subject-wise LOSO balanced accuracy resulted from a model trained on all the subjects except one left-out used as validation set. Each boxplot gathers all the balanced accuracies of models evaluated on the same left-out subject, but trained on different train/validation partitions following a LOSO scheme. In other words, each model was trained on all except two subjects, monitored on another changed every training, and evaluated on the same left-out subject.

#### 5. Conclusion

This study investigated the impact of data partition on the performance assessment of EEG-DL models. Five distinct cross-validation strategies that operate either at the sample or at subject level are compared across three representative clinical and non-clinical classification tasks, using four established deep learning architectures with increased complexity. The analysis of more than 100000 different trained models revealed strong differences between sample-based and subject-based approaches (e.g., LeaveN-Subjects-Out), highlighting how subject-specific characteristics can be learned and leveraged during inference to inflate performance estimates. Such findings confirm the necessity of using subject-based strategies, particularly in clinical applications, where subject IDs and health status are uniquely identified.

Additionally, the analysis stressed the importance of maintaining independent validation and test sets to respectively monitor the training and evaluating the model. Consequently, Nested-Leave-N-Subjects-Out (N-LNSO) was found to be sole method capable of preventing data leakage and providing more accurate estimation of model performance while accounting for the high inter-subject variability inherent to EEG signals. In particular, a comparative evaluation of the Nested-Leave-One-Subject-Out (N-LOSO) and the Leave-One-Subject-Out (LOSO) cross-validation techniques demonstrated that traditional approaches tend to yield optimistic results. Furthermore, it revealed that larger models exhibit higher performance drops as well as higher variance of results. In summary, this study is the first to provide a comprehensive comparative analysis of different cross-validation methods for evaluating EEG deep learning models. It is the first to provide an analysis that goes beyond the sample-based vs. subject-based strategies (subsection 3.1), clearly assessing the limitations of commonly used approaches, such as LNSO (subsection 3.2) or LOSO (subsection 3.3), and highlighting the importance of using nested strategies to provide more reliable performance estimates.

#### CRediT authorship contribution statement

Federico Del Pup: Conceptualization, Methodology, Software, Visualization, Writing – original draft . Andrea Zanola: Methodology, Writing - review and editing . Louis Fabrice Tshimanga: Methodology, Writing - review and editing . Alessandra Bertoldo: Writing - review and editing. Livio Finos: Methodology, Writing - review and editing . Manfredo Atzori: Supervision, Funding acquisition, Project administration, Writing - review and editing.

#### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

#### Code and data availability

The code used to produce both results and figures is openly available at https://github.com/MedMaxLab/eegpartition. All data that support the findings of this study are openly available within the OpenNeuro platform.

#### acknowledgment

FDP would like to thank the Padova Neuroscience Center and its members for the support provided during the realization of this study.

#### References

- [1] Z. Khademi, F. Ebrahimi, H. M. Kordy, A review of critical challenges in MI-BCI: From conventional to deep learning methods, J. Neurosci. Methods 383 (2023) 109736. doi:10.1016/j.jneumeth. 2022.109736.
- [2] J. Zhang, Z. Yin, P. Chen, S. Nichele, Emotion recognition using multi-modal data and machine learning techniques: A tutorial and review, Inform. Fusion 59 (2020) 103–126. doi:10.1016/j. inffus.2020.01.011.
- [3] H. W. Loh, C. P. Ooi, J. Vicnesh, S. L. Oh, O. Faust, A. Gertych, U. R. Acharya, Automated detection of sleep stages using deep learning techniques: A systematic review of the last decade (2010–2020), Appl. Sci. 10 (24) (2020). doi:10.3390/app10248963.
- [4] A. M. Maitin, J. P. Romero Muñoz, Á. J. García-Tejedor, Survey of machine learning techniques in the analysis of EEG signals for Parkinson’s disease: A systematic review, Appl. Sci. 12 (14) (2022)

6967. doi:10.3390/app12146967.

- [5] K. D. Tzimourta, V. Christou, A. T. Tzallas, N. Giannakeas, L. G. Astrakas, P. Angelidis, D. Tsalikakis, M. G. Tsipouras, Machine learning algorithms and statistical approaches for Alzheimer’s disease analysis based on resting-state EEG recordings: A systematic review, Int. J. Neural Syst. 31 (05) (2021) 2130002. doi:10.1142/ S0129065721300023.
- [6] K. Rasheed, A. Qayyum, J. Qadir, S. Sivathamboo, P. Kwan, L. Kuhlmann, T. O’Brien, A. Razi, Machine learning for predicting epileptic seizures using EEG signals: A review, IEEE Rev. Biomed. Eng. 14 (2020) 139–155. doi:10.1109/RBME.2020. 3008792.
- [7] F. Del Pup, A. Zanola, L. Fabrice Tshimanga, A. Bertoldo, M. Atzori, The more, the better? Evaluating the role of EEG preprocessing for deep learning applications, IEEE Transactions on Neural Systems and Rehabilitation Engineering 33 (2025) 1061–1070. doi:10.1109/ TNSRE.2025.3547616.
- [8] D. Gholamiangonabadi, N. Kiselov, K. Grolinger, Deep neural networks for human activity recognition with wearable sensors: LeaveOne-Subject-Out cross-validation for model selection, IEEE Access 8 (2020) 133982–133994. doi:10.1109/ACCESS.2020. 3010715.
- [9] J. Y. Cheng, H. Goh, K. Dogrusoz, O. Tuzel, E. Azemi, Subjectaware contrastive learning for biosignals (2020). doi:10.48550/ arXiv.2007.04871.
- [10] A. Kamrud, B. Borghetti, C. Schubert Kabban, The effects of individual differences, non-stationarity, and the importance of data partitioning decisions for training and testing of EEG cross-participant models, Sensors 21 (9) (2021). doi:10.3390/s21093225.
- [11] G. Brookshire, J. Kasper, N. M. Blauch, Y. C. Wu, R. Glatt, D. A. Merrill, S. Gerrol, K. J. Yoder, C. Quirk, C. Lucero, Data leakage in deep learning studies of translational EEG, Front. Neurosci. 18

(2024). doi:10.3389/fnins.2024.1373515.

- [12] S. Kunjan, T. S. Grummett, K. J. Pope, D. M. Powers, S. P. Fitzgibbon, T. Bastiampillai, M. Battersby, T. W. Lewis, The necessity of leave one subject out (LOSO) cross validation for EEG disease diagnosis, in: Brain Informatics: 14th International Conference, BI 2021, Virtual

- Event, September 17–19, 2021, Proceedings 14, Springer, 2021, pp. 558–567. doi:10.1007/978-3-030-86993-9_50.
- [13] H.-T. Lee, H.-R. Cheon, S.-H. Lee, M. Shim, H.-J. Hwang, Risk of data leakage in estimating the diagnostic performance of a deep-learning-based computer-aided system for psychiatric disorders, Sci. Rep. 13 (1) (2023) 16633. doi:10.1038/ s41598-023-43542-8.
- [14] L. Dubreuil-Vall, G. Ruffini, J. A. Camprodon, Deep learning convolutional neural networks discriminate adult ADHD from healthy individuals on the basis of event-related spectral EEG, Frontiers in Neuroscience 14 (2020). doi:10.3389/fnins.2020.00251.
- [15] J. L. Hagad, K. Fukui, M. Numao, Deep visual models for EEG of mindfulness meditation in a workplace setting, in: Precision Health and Medicine: A Digital Revolution in Healthcare, Springer, 2020, pp. 129–137. doi:10.1007/978-3-030-24409-5_12.
- [16] H. Albaqami, G. M. Hassan, A. Datta, MP-SeizNet: A multi-path CNN Bi-LSTM network for seizure-type classification using EEG, Biomed. Signal Process. Control 84 (2023) 104780. doi:https: //doi.org/10.1016/j.bspc.2023.104780.
- [17] J. Kim, D.-U. Hwang, E. J. Son, S. H. Oh, W. Kim, Y. Kim, G. Kwon, Emotion recognition while applying cosmetic cream using deep learning from EEG data; cross-subject analysis, PLOS ONE 17 (11) (2022) 1–26. doi:10.1371/journal.pone.0274203.
- [18] F. Del Pup, M. Atzori, Toward improving reproducibility in neuroimaging deep learning studies, Front. Neurosc. 18 (2024). doi: 10.3389/fnins.2024.1509358.
- [19] C. J. Markiewicz, K. J. Gorgolewski, F. Feingold, R. Blair, Y. O. Halchenko, E. Miller, N. Hardcastle, J. Wexler, O. Esteban, M. Goncavles, A. Jwa, R. Poldrack, The OpenNeuro resource for sharing of neuroscience data, eLife 10 (2021) e71774. doi:10. 7554/eLife.71774.
- [20] C. R. Pernet, S. Appelhoff, K. J. Gorgolewski, G. Flandin, C. Phillips, A. Delorme, R. Oostenveld, EEG-BIDS, an extension to the brain imaging data structure for electroencephalography, Sci. Data 6 (1)

(2019) 103. doi:10.1038/s41597-019-0104-8.

- [21] A. Zanola, F. Del Pup, C. Porcaro, M. Atzori, BIDSAlign: a library for automatic merging and preprocessing of multiple EEG repositories, J. Neural Eng. 21 (4) (2024) 046050. doi:10.1088/1741-2552/ ad6a8c.
- [22] S. R. Sinha, L. Sullivan, D. Sabau, D. San-Juan, K. E. Dombrowski, J. J. Halford, A. J. Hani, F. W. Drislane, M. M. Stecker, American clinical neurophysiology society guideline 1: minimum technical requirements for performing clinical electroencephalography, J. Clin. Neurophysiol. 33 (4) (2016) 303–307. doi:10.1097/WNP. 0000000000000308.
- [23] K. Douibi, S. Le Bars, A. Lemontey, L. Nag, R. Balp, G. Breda, Toward eeg-based bci applications for industry 4.0: Challenges and possible applications, Front. Hum. Neurosci. 15 (2021). doi:10. 3389/fnhum.2021.705064.
- [24] T. Karácsony, J. P. Hansen, H. K. Iversen, S. Puthusserypady, Brain computer interface for neuro-rehabilitation with deep learning classification and virtual reality feedback, in: Proceedings of the 10th Augmented Human International Conference 2019, AH2019, Association for Computing Machinery, New York, NY, USA, 2019, p. 8. doi:10.1145/3311823.3311864.
- [25] A. P. Rockhill, N. Jackson, J. George, A. Aron, N. C. Swann, UC San Diego resting state EEG data from patients with Parkinson’s disease

(2021). doi:10.18112/openneuro.ds002778.v1.0.5.

- [26] J. F. Cavanagh, Eeg: 3-stim auditory oddball and rest in parkinson’s

(2021). doi:10.18112/openneuro.ds003490.v1.1.0.

- [27] A. Miltiadous, K. D. Tzimourta, T. Afrantou, P. Ioannidis, N. Grigoriadis, D. G. Tsalikakis, P. Angelidis, M. G. Tsipouras, E. Glavas, N. Giannakeas, A. T. Tzallas, A dataset of EEG recordings from: Alzheimer’s disease, frontotemporal dementia and healthy subjects

(2023). doi:10.18112/openneuro.ds004504.v1.0.6.

- [28] C. M. Köllőd, A. Adolf, K. Iván, G. Márton, I. Ulbert, Deep comparisons of neural networks from the EEGNet family, Electronics 12 (12)

(2023). doi:10.3390/electronics12122743.

- [29] G. Zoumpourlis, I. Patras, Motor imagery decoding using ensemble curriculum learning and collaborative training, in: 2024 12th International Winter Conference on Brain-Computer Interface (BCI), 2024, pp. 1–8. doi:10.1109/BCI60775.2024.10480476.
- [30] L. J. Gabard-Durnam, A. S. Mendez Leal, C. L. Wilkinson, A. R. Levin, The harvard automated processing pipeline for electroencephalography (HAPPE): standardized processing software for developmental and high-artifact data, Front. Neurosci. 12 (2018) 316496. doi:10.3389/fnins.2018.00097.
- [31] Y. Roy, H. Banville, I. Albuquerque, A. Gramfort, T. H. Falk, J. Faubert, Deep learning-based electroencephalography analysis: a systematic review, J. Neural Eng. 16 (5) (2019) 051001. doi: 10.1088/1741-2552/ab260c.
- [32] A. J. Bell, T. J. Sejnowski, An Information-Maximization Approach to Blind Separation and Blind Deconvolution, Neural Comput. 7 (6)

(1995) 1129–1159. doi:10.1162/neco.1995.7.6.1129.

- [33] L. Pion-Tonachini, K. Kreutz-Delgado, S. Makeig, ICLabel: An automated electroencephalographic independent component classifier, dataset, and website, NeuroImage 198 (2019) 181–197. doi:10. 1016/j.neuroimage.2019.05.026.
- [34] T. R. Mullen, C. A. E. Kothe, Y. M. Chi, A. Ojeda, T. Kerth, S.Makeig,T.-P.Jung,G.Cauwenberghs,Real-timeneuroimagingand cognitive monitoring using wearable dry EEG, IEEE Trans. Biomed. Eng. 62 (11) (2015) 2553–2567. doi:10.1109/TBME.2015. 2481482.
- [35] S. S. Kang, T. J. Lano, S. R. Sponheim, Distortions in EEG interregional phase synchrony by spherical spline interpolation: causes and remedies, Neuropsychiatr. Electrophysiol. 1 (2015) 1–17. doi: 10.1186/s40810-015-0009-5.
- [36] Y.-Y. Yang, M. Hira, Z. Ni, A. Astafurov, C. Chen, C. Puhrsch, D. Pollack, D. Genzel, D. Greenberg, E. Z. Yang, et al., Torchaudio: Building blocks for audio and speech processing, in: ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE, 2022, pp. 6982–6986. doi: 10.1109/ICASSP43922.2022.9747236.
- [37] S. K. Khare, V. Bajaj, U. R. Acharya, PDCNNet: An automatic framework for the detection of Parkinson’s disease using EEG signals, IEEE Sens. J. 21 (15) (2021) 17017–17024. doi:10.1109/JSEN. 2021.3080135.
- [38] F. Del Pup, A. Zanola, L. F. Tshimanga, P. E. Mazzon, M. Atzori, SelfEEG: A Python library for self-supervised learning in electroencephalography, J. Open Source Softw. 9 (95) (2024) 6224. doi: 10.21105/joss.06224.
- [39] M. L. Waskom, seaborn: statistical data visualization, J. Open Source Softw. 6 (60) (2021) 3021. doi:10.21105/joss.03021.
- [40] X. Hu, L. Chu, J. Pei, W. Liu, J. Bian, Model complexity of deep learning: A survey, Knowl. Inf. Syst. 63 (2021) 2585–2619. doi: 10.1007/s10115-021-01605-0.
- [41] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, B. J. Lance, EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces, J. neural eng. 15 (5) (2018)

056013. doi:10.1088/1741-2552/aace8c.

- [42] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, T. Ball, Deep learning with convolutional neural networks for EEG decoding and visualization, Hum. brain mapp. 38 (11) (2017) 5391–5420. doi:10.1002/hbm.23730.
- [43] Y. Zheng, Z. Liu, R. Mo, Z. Chen, W.-s. Zheng, R. Wang, Taskoriented self-supervised learning for anomaly detection in electroencephalography, in: International Conference on Medical Image Computing and Computer-Assisted Intervention, Springer, 2022, pp. 193–

203. doi:10.1007/978-3-031-16452-1_19.

- [44] M. H. Rafiei, L. V. Gauthier, H. Adeli, D. Takabi, Self-supervised learning for electroencephalography, IEEE Trans. Neural Netw. Learn. Syst. 35 (2) (2024) 1457–1471. doi:10.1109/TNNLS. 2022.3190448.
- [45] X. Jiang, J. Zhao, B. Du, Z. Yuan, Self-supervised contrastive learning for EEG-based sleep staging, in: 2021 International Joint Conference

- on Neural Networks (IJCNN), 2021, pp. 1–8. doi:10.1109/ IJCNN52387.2021.9533305.
- [46] K. H. Cheah, H. Nisar, V. V. Yap, C.-Y. Lee, G. Sinha, Optimizing residual networks and VGG for classification of EEG signals: Identifying ideal channels for emotion recognition, J. Healthc. Eng. 2021 (1)

(2021) 5599615. doi:10.1155/2021/5599615.

- [47] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, et al., Pytorch: An imperative style, high-performance deep learning library, Adv. Neural Inf. Process. sSyst. 32 (2019). doi:10.48550/arXiv.1912. 01703.
- [48] D. Kingma, J. Ba, Adam: A method for stochastic optimization, in: 3rd international conference on learning representations (ICLR), San Diega, CA, USA, 2015, p. 13. doi:10.48550/arXiv.1412. 6980.
- [49] M. Grandini, E. Bagli, G. Visani, Metrics for multi-class classification: an overview, arXiv (2020). doi:10.48550/arXiv.2008. 05756.
- [50] A. Miltiadous, E. Gionanidis, K. D. Tzimourta, N. Giannakeas, A. T. Tzallas, DICE-net: a novel convolution-transformer architecture for Alzheimer detection in EEG signals, IEEE Access (2023). doi: 10.1109/ACCESS.2023.3294618.
- [51] R.-D. Buhai, Y. Halpern, Y. Kim, A. Risteski, D. Sontag, Empirical study of the benefits of overparameterization in learning latent variable models, in: Proceedings of the 37th International Conference on Machine Learning, Vol. 119 of Proceedings of Machine Learning Research, PMLR, 2020, pp. 1211–1219.
- [52] A. B. Tatar, Biometric identification system using eeg signals, Neural Comput. Appl. 35 (1) (2023) 1009–1023. doi:10.1007/ s00521-022-07795-0.
- [53] S. L. Oh, Y. Hagiwara, U. Raghavendra, R. Yuvaraj, N. Arunkumar, M. Murugappan, U. R. Acharya, A deep learning approach for Parkinson’s disease diagnosis from EEG signals, Neural Comput. Appl. 32

(2020) 10927–10933. doi:10.1007/s00521-018-3689-5.

- [54] M. Shaban, Automated screening of parkinson’s disease using deep learning based electroencephalography, in: 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER), 2021, pp. 158–161. doi:10.1109/NER49283.2021.9441065.
- [55] C. J. Huggins, J. Escudero, M. A. Parra, B. Scally, R. Anghinah, A. Vitória Lacerda De Araújo, L. F. Basile, D. Abasolo, Deep learning of resting-state electroencephalogram signals for three-class classification of Alzheimer’s disease, mild cognitive impairment and healthy ageing, Journal of Neural Engineering 18 (4) (2021) 046087. doi:10.1088/1741-2552/ac05d8.
- [56] M. Bakhtyari, S. Mirzaei, ADHD detection using dynamic connectivity patterns of EEG data and ConvLSTM with attention framework, Biomedical Signal Processing and Control 76 (2022) 103708. doi: 10.1016/j.bspc.2022.103708.
- [57] Y. Cimtay, E. Ekmekcioglu, Investigating the use of pretrained convolutional neural network on cross-subject and cross-dataset EEG emotion recognition, Sensors 20 (7) (2020). doi:10.3390/ s20072034.
- [58] T. G. Dietterich, Approximate statistical tests for comparing supervised classification learning algorithms, Neural Comput. 10 (7)

(1998) 1895–1923. doi:10.1162/089976698300017197.

- [59] C. Nadeau, Y. Bengio, Inference for the generalization error, Mach. Learn. 52 (3) (2003) 239–281. doi:doi.org/10.1023/A: 1024068626366.

#### A. Supplementary Materials

The following subsections provides supplementary materials for the research study “Rethinking how to evaluate model performance in deep learning-based cross-subject electroencephalogram analysis".

- A.1. How many training instances? To produce the results presented in this study, a total

of more than 100000 different models were trained. This value includes not only the models trained on the five crossvalidation settings selected for this study, but also additional experiments that were performed to prepare some sections of the Supplementary Materials. Furthermore, more than 80% of the training instances originate from the full N-LOSO CV discussed in Section 3.3 of the paper. This is also the reason why a full N-LOSO strategy is recommended only for datasets with at most 20 subjects. The total number of instances for each cross-validation method and classification task is reported below:

K-Fold = 𝑁𝐹 LNSO = 𝑁𝐹 LOSO = 𝑁𝑆

N-LNSO = 𝑁𝑂 ⋅ 𝑁𝐼 N-LOSO = 𝑁𝑆 ⋅ (𝑁𝑆 − 1)

N-Kfold = 𝑁𝑂 ⋅ 𝑁𝐹 N-NLNSO = 𝑁𝑅 ⋅ 𝑁𝑂 ⋅ 𝑁𝐼

with 𝑁𝐹 the number of folds (10), 𝑁𝑆 the number of subjects (see Table 1 in the main body), 𝑁𝑂 the number of outer folds in nested cross-validations (10), 𝑁𝐼 the number of inner folds in nested cross-validations (10), and 𝑁𝑅 the number of times a cross-validation is repeated (10). N-Kfold and N-NLNSO refer to the additional cross-validation settings explained in section A.4, which were used to provide a preliminary analysis of the generalization error underestimation with traditional cross-validation methods. Performance metrics for each trained models are shared within the openly available GitHub repository associated with this study.

- A.2. Random seed influence To produce the results of this study, a custom random

seed (83136297) was randomly selected and fixed. This approach minimizes randomness in the code and improves the reproducibility of results. While different random seeds may affect the reported accuracy scores, it can be assumed that this factor cannot alter the conclusions drawn in this research, especially given the relevant differences between the cross-validation methods. To validate this, the LNSO and N-LNSO training instances for the ShallowNet and DeepConvNet models were repeated using 4 additional random seeds: 0, 42, 1234, and 3407. Using a different random seed primarily impacts the following steps:

• Subject assignment in the LNSO and N-LNSO crossvalidation procedures.

Table 1 Balanced Accuracy median and [25𝑡ℎ−75𝑡ℎ] percentiles for different random seeds.

Task Seed LNSO N-LNSO ShallowConvNet

0 82.85 [75.02 − 89.99] 75.78 [66.44 − 84.86]

42 85.02 [81.80 − 88.65] 80.48 [74.51 − 86.30] 1234 82.24 [75.79 − 87.02] 75.89 [70.73 − 81.81] 3407 82.80 [75.20 − 93.05] 76.30 [69.70 − 89.00]

Parkinson

83136297 85.38 [71.77 − 88.91] 77.10 [67.79 − 82.95]

0 54.20 [52.53 − 62.47] 53.01 [49.19 − 57.09]

Alzheimer

42 62.41 [51.01 − 63.70] 55.87 [50.42 − 61.43] 1234 56.38 [49.53 − 65.83] 54.07 [46.04 − 60.95] 3407 59.41 [56.66 − 66.65] 55.12 [44.80 − 61.89]

83136297 58.09 [50.38 − 65.80] 57.12 [48.73 − 62.86]

0 55.49 [53.31 − 58.35] 54.19 [51.12 − 56.02]

42 56.61 [52.66 − 58.37] 54.06 [51.79 − 56.13] 1234 54.49 [52.27 − 57.75] 53.91 [51.67 − 56.87] 3407 56.07 [54.19 − 57.09] 54.46 [52.13 − 56.36]

BCI

83136297 54.72 [53.39 − 58.91] 53.41 [50.91 − 56.20] DeepConvNet

0 61.97 [51.26 − 83.32] 54.72 [51.44 − 66.39]

42 74.16 [66.34 − 82.88] 65.12 [52.17 − 73.34] 1234 70.81 [54.05 − 80.09] 61.15 [51.36 − 72.40] 3407 63.52 [50.57 − 72.76] 56.26 [50.57 − 70.98]

Parkinson

83136297 53.35 [51.81 − 81.40] 53.28 [50.77 − 68.15]

0 56.98 [51.94 − 62.05] 52.51 [46.36 − 56.90]

42 57.10 [47.17 − 60.28] 51.68 [46.19 − 56.31] 1234 53.15 [43.54 − 61.53] 53.23 [43.26 − 58.16] 3407 50.17 [44.97 − 57.11] 52.00 [43.36 − 56.98]

Alzheimer

83136297 58.78 [52.01 − 61.68] 54.38 [48.08 − 59.69]

0 53.59 [51.07 − 58.61] 53.79 [51.66 − 56.01]

42 54.34 [50.53 − 55.99] 53.09 [50.53 − 55.44] 1234 55.35 [52.98 − 57.24] 53.12 [51.46 − 55.09] 3407 54.86 [52.88 − 57.04] 54.19 [51.56 − 55.87]

BCI

83136297 56.25 [54.27 − 59.03] 54.18 [51.90 − 56.31]

- • Creation of the data loader sampler iterator for mini-batch construction.
- • Initialization of model weights.

N-LOSO cross-validation was not included in this additional analysis due to the computational impracticality of rerunning this setting multiple times. Moreover, considering the high variability among subjects, it can be inferred that the subject assignment step has the most significant impact on model accuracy. This step is deterministic in N-LOSO since it evaluates every possible partition that assigns one subject to the validation set and another to the test set. Table 1 illustrates that changing the custom random seed does

- Table 2 Median and [25𝑡ℎ − 75𝑡ℎ] percentiles of F1-score and Cohen’s Kappa for each model, task, and cross-validation setting.

K-Fold LNSO N-LNSO F1-score 𝜅 F1-Score 𝜅 F1-Score 𝜅

Task Model

0.51 [0.37 − 0.64] EEGNet

1.00 [1.00 − 1.00]

1.00 [1.00 − 1.00]

0.85 [0.75 − 0.89]

0.70 [0.44 − 0.77]

0.76 [0.70 − 0.83]

ShallowConvNet

Parkinson

0.42 [0.31 − 0.58] DeepConvNet

0.99 [0.99 − 0.99]

0.99 [0.98 − 0.99]

0.79 [0.70 − 0.87]

0.54 [0.40 − 0.72]

0.72 [0.67 − 0.80]

0.07 [0.01 − 0.35] T-ResNet

1.00 [1.00 − 1.00]

1.00 [1.00 − 1.00]

0.52 [0.29 − 0.81]

0.05 [0.04 − 0.62]

0.52 [0.36 − 0.67]

0.85 [0.83 − 0.86]

0.70 [0.66 − 0.71]

0.76 [0.61 − 0.80]

0.49 [0.25 − 0.59]

0.65 [0.58 − 0.73]

0.28 [0.17 − 0.44]

0.38 [0.27 − 0.51] EEGNet

1.00 [0.99 − 1.00]

0.99 [0.99 − 1.00]

0.59 [0.53 − 0.68]

0.39 [0.31 − 0.55]

0.57 [0.50 − 0.65]

ShallowConvNet

Alzheimer

0.27 [0.18 − 0.50] DeepConvNet

0.98 [0.97 − 0.98]

0.96 [0.95 − 0.98]

0.55 [0.47 − 0.67]

0.35 [0.23 − 0.57]

0.50 [0.44 − 0.60]

0.32 [0.21 − 0.42] T-ResNet

1.00 [0.99 − 1.00]

0.99 [0.99 − 1.00]

0.55 [0.51 − 0.63]

0.39 [0.28 − 0.44]

0.53 [0.44 − 0.61]

0.78 [0.77 − 0.81]

0.66 [0.65 − 0.71]

0.45 [0.38 − 0.56]

0.16 [0.08 − 0.34]

0.44 [0.36 − 0.50]

0.15 [0.03 − 0.24]

0.38 [0.35 − 0.42] EEGNet

0.64 [0.63 − 0.66]

0.52 [0.51 − 0.55]

0.54 [0.53 − 0.59]

0.40 [0.38 − 0.45]

0.53 [0.51 − 0.56]

ShallowConvNet

0.39 [0.35 − 0.43] DeepConvNet

0.57 [0.56 − 0.59]

0.43 [0.41 − 0.45]

0.55 [0.54 − 0.56]

0.40 [0.39 − 0.42]

0.54 [0.51 − 0.57]

BCI

0.39 [0.36 − 0.42] T-ResNet

0.65 [0.64 − 0.66]

0.54 [0.52 − 0.55]

0.56 [0.54 − 0.59]

0.42 [0.39 − 0.45]

0.54 [0.52 − 0.56]

0.48 [0.47 − 0.50]

0.31 [0.30 − 0.34]

0.47 [0.43 − 0.49]

0.30 [0.26 − 0.32]

0.45 [0.43 − 0.47]

0.28 [0.25 − 0.30]

not affect the conclusions of this study. The median values remain within the range of variability observed across different seeds for each model and task analyzed. Additionally, pairwise comparisons of the median, 25𝑡ℎ percentile, and 75𝑡ℎ percentile balanced accuracies indicate that the metrics are higher in the LNSO cross-validation compared to the NLNSO.

- A.3. Summary results with other metrics This section summarizes the results of the sample-based

K-Fold, Leave-N-Subjects-Out (LNSO), and Nested-LeaveN-Subjects-Out (N-LNSO) cross-validations using further performance metrics. In particular, Table 2 reports median and [25𝑡ℎ − 75𝑡ℎ] percentiles for the F1-score and Cohen’s Kappa. Median values decreased when transitioning from the sample-based K-Fold method to LNSO, and further from LNSO to N-LNSO. Additionally, the interquartile range increases when comparing sample-based approaches to subject-based ones. These performance variations reinforce the conclusions of this study and highlight the importance of employing nested approaches for evaluating EEG deep learning models. For further insights, additional performance metrics, including Precision, Sensitivity, and the Area Under the Receiver Operating Characteristic Curve (ROC AUC), can be found in the tabular (.csv) file uploaded in the publicly accessible GitHub repository associated with this study.

##### A.4. Generalization error underestimation with traditional cross-validation methods

To investigate whether significant differences among various cross-validation methods result from an overestimation of the generalization error by one approach or an underestimation by another, it is necessary to add an additional nesting level for each CV. This involves repeating each crossvalidation multiple times, with each run excluding a different group of subjects (10% of the total) to use to measure the bias generalization error estimations. During each run, the balanced accuracy is calculated for both the left-out group and the relevant CV evaluation split (i.e., the validation set for traditional CV and the test for nested approaches) for each trained model. Subsequently, the mean difference is calculated. In this preliminary analysis, ten repetitions of each CV have been performed, except for the LOSO vs N-LOSO scenario due to its substantial computational demands, as detailed in subsection A.1.

In comparing the K-Fold with the LNSO, it is interesting to note that adding a nested level in traditional crossvalidation methods is equivalent to run a nested crossvalidation analysis, which supports the validity of the proposed method. Furthermore, figure 1 illustrates how samplebased methods tend to produce significant positive biases, resulting in underestimation of the generalization error.

In the N-LNSO versus LNSO comparison, the high variability and the limited number of bias estimations confirm

# Accuracy Estimation Bias - Sample-based K-Fold vs LNSO

Model: ShallowConvNet

Model: EEGNet

80

80 (B)

(A)

70

70

BiasAccuracyBalanced

60

60

50

50

40

40

30

30

20

20

10

10

0

0

10

10

Sample-based K-Fold

Sample-based K-Fold

20

20

Leave-N-Subjects-Out

Leave-N-Subjects-Out

30

30

Alzheimer BCI Parkinson

Alzheimer BCI Parkinson

Model: DeepConvNet

Model: T-ResNet

80

80 (D)

(C)

70

70

BiasAccuracyBalanced

60

60

50

50

40

40

30

30

20

20

10

10

0

0

10

10

Sample-based K-Fold

Sample-based K-Fold

20

20

Leave-N-Subjects-Out

Leave-N-Subjects-Out

30

30

Alzheimer BCI Parkinson

Alzheimer BCI Parkinson

Task

Task

Figure 1: Balanced accuracy estimation bias comparison between Sample-based (K-Fold) and subject-based (LNSO) 10-Fold cross-validations. The sub-figures display results for different deep learning architectures: ShallowConvNet (Panel A), EEGNet (Panel B), DeepConvNet (Panel C), and T-ResNet (Panel D). Sample-based approaches produce strong positive biases, particularly in pathology classification tasks, indicating the tendency of this method to produce optimistic results and underestimating the generalization error.

the limitations of this preliminary approach. Nevertheless, the mean and standard deviation of biases presented in Table 3 reveals to be generally slightly lower in the N-LNSO scenario. Future analyses with more rigorously designed methodologies will offer further evidence and insights into the significant differences between the CV methods discussed in Section 3 and further elaborated in Section 4 of the paper.

##### A.5. Additional Details on Model architectures This section offers detailed information about the deep

learning models selected for this study. A summary table is provided for each model, as indicated below: Table 4 for

EEGNet, Table 5 for DeepConvNet, Table 6 for ShallowConvNet, and Table 7 for T-ResNet. Each table outlines important characteristics, including input shape, output shape, kernel size, number of convolutional groups, and the number of parameters for each layer in the network. Additionally, activation functions and dimensional operations (such as flattening and unsqueezing) are included for thoroughness. The input and output sizes correspond to the Alzheimer’s task. Specifically, the models accept EEG trial windows consisting of 19 channels and 500 samples (equivalent to 4 seconds) and output probabilities for a three-class classification problem. The variable N denotes the batch size, which was set to 64 for this study. For clarity, skip connections in the Residual Blocks of T-ResNet are not illustrated. The

- Table 3 Mean and standard deviation of the absolute balanced accuracy estimation bias for each task and model.

Task Model LNSO N-LNSO

ShallowConvNet 8.25 ± 6.56 8.11 ± 5.35

Parkinson

EEGNet 6.99 ± 4.38 5.35 ± 3.31 DeepConvNet 7.17 ± 6.15 5.46 ± 3.91

T-ResNet 8.03 ± 6.35 6.54 ± 3.91

ShallowConvNet 9.72 ± 6.80 9.26 ± 6.46

Alzheimer

EEGNet 10.64 ± 4.60 9.49 ± 5.25 DeepConvNet 9.02 ± 5.47 6.62 ± 4.71

T-ResNet 7.52 ± 5.25 5.42 ± 3.86

ShallowConvNet 3.71 ± 2.21 3.43 ± 2.22

EEGNet 3.94 ± 2.57 3.17 ± 2.49 DeepConvNet 3.00 ± 2.30 3.04 ± 3.86

BCI

T-ResNet 1.88 ± 1.74 1.92 ± 1.38

tables also facilitate a comparison of model complexity, with ShallowConvNet (Table 6) being the simplest model and T-ResNet (Table 7) being the most complex. A complete implementation of each deep learning model is accessible in the openly available SelfEEG library’s code base (version 0.2.0). Additionally, the GitHub repository associated with this study contains models exported in the Open Neural Network eXchange (ONNX) format. These ONNX files can be imported into the Netron open platform (https://netron.app/), allowing users to visualize how mini-batches pass through the layers of the network.

- Table 4 Summary Table: EEGNet. Input size reflects the Alzheimer’s task.

Layer(type) Input Shape Output Shape Kernel Shape Groups Param#

EEGNet [N,19,500] [N,3] – – – +EEGNetEncoder [N,19,500] [N,240] – – – | +Unsqueeze [N,19,500] [N,1,19,500] – – – | +Conv2d [N,1,19,500] [N,8,19,500] [1,64] 1 512 | +BatchNorm2d [N,8,19,500] [N,8,19,500] – – 16 | +DepthwiseConv2d [N,8,19,500] [N,16,1,500] [19,1] 8 304 | +BatchNorm2d [N,16,1,500] [N,16,1,500] – – 32 | +ELU [N,16,1,500] [N,16,1,500] – – – | +AvgPool2d [N,16,1,500] [N,16,1,125] [1,4] – – | +Dropout [N,16,1,125] [N,16,1,125] – – – | +SeparableConv2d [N,16,1,125] [N,16,1,125] – – – | | +DepthwiseConv2d [N,16,1,125] [N,16,1,125] [1,16] 16 256 | | +ConstrainedConv2d [N,16,1,125] [N,16,1,125] [1,1] 1 256 | +BatchNorm2d [N,16,1,125] [N,16,1,125] – – 32 | +ELU [N,16,1,125] [N,16,1,125] – – – | +AvgPool2d [N,16,1,125] [N,16,1,15] [1,8] – – | +Dropout [N,16,1,15] [N,16,1,15] – – – | +Flatten [N,16,1,15] [N,240] – – – +ConstrainedDense [N,240] [N,3] – – 723

- Table 5 Summary Table: DeepConvNet. Input size reflects the Alzheimer’s task.

Layer(type) InputShape OutputShape KernelShape Groups Param#

DeepConvNet [N,19,500] [N,3] – – – +DeepConvNetEncoder [N,19,500] [N,200] – – – | +Unsqueeze [N,19,500] [N,1,19,500] – – – | +ConstrainedConv2d [N,1,19,500] [N,25,19,491] [1,10] 1 275 | +ConstrainedConv2d [N,25,19,491] [N,25,1,491] [19,1] 1 11,900 | +BatchNorm2d [N,25,1,491] [N,25,1,491] – – 50 | +ELU [N,25,1,491] [N,25,1,491] – – – | +MaxPool2d [N,25,1,491] [N,25,1,163] [1,3] – – | +Dropout [N,25,1,163] [N,25,1,163] – – – | +ConstrainedConv2d [N,25,1,163] [N,50,1,154] [1,10] 1 12,550 | +BatchNorm2d [N,50,1,154] [N,50,1,154] – – 100 | +ELU [N,50,1,154] [N,50,1,154] – – – | +MaxPool2d [N,50,1,154] [N,50,1,51] [1,3] – – | +Dropout [N,50,1,51] [N,50,1,51] – – – | +ConstrainedConv2d [N,50,1,51] [N,100,1,42] [1,10] 1 50,100 | +BatchNorm2d [N,100,1,42] [N,100,1,42] – – 200 | +ELU [N,100,1,42] [N,100,1,42] – – – | +MaxPool2d [N,100,1,42] [N,100,1,14] [1,3] – – | +Dropout [N,100,1,14] [N,100,1,14] – – – | +ConstrainedConv2d [N,100,1,14] [N,200,1,5] [1,10] 1 200,200 | +BatchNorm2d [N,200,1,5] [N,200,1,5] – – 400 | +ELU [N,200,1,5] [N,200,1,5] – – – | +MaxPool2d [N,200,1,5] [N,200,1,1] [1,3] – – | +Dropout [N,200,1,1] [N,200,1,1] – – – | +Flatten [N,200,1,1] [N,200] – – – +ConstrainedDense [N,200] [N,3] – – 603

Summary Table: ShallowConvNet. Input size reflects the Alzheimer’s task. Layer(type) Input Shape Output Shape Kernel Shape Groups Param#

ShallowNet [N,19,500] [N,3] – – – +ShallowNetEncoder [N,19,500] [N,1080] – – – | +Unsqueeze [N,19,500] [N,1,19,500] – – – | +Conv2d [N,1,19,500] [N,40,19,476] [1,25] 1 1,040 | +Conv2d [N,40,19,476] [N,40,1,476] [19,1] 1 30,440 | +BatchNorm2d [N,40,1,476] [N,40,1,476] – – 80 | +Square [N,40,1,476] [N,40,1,476] – – 80 | +AvgPool2d [N,40,1,476] [N,40,1,27] [1,75] – – | +Log [N,40,1,27] [N,40,1,27] – – – | +Dropout [N,40,1,27] [N,40,1,27] – – – | +Flatten [N,40,1,27] [N,1080] – – – +Linear [N,1080] [N,3] – – 3,243

Table 7 Summary Table: T-ResNet. Input size reflects the Alzheimer’s task. Resnet blocks include a skip connection.

Layer(type) Input Shape Output Shape Kernel Shape Groups Param#

T-ResNet [N,19,500] [N,3] – – – +T-ResNetEncoder [N,19,500] [N,304] – – – | +Unsqueeze [N,19,500] [N,1,19,500] – – – | +Sequential [N,1,19,500] [N,16,19,250] – – – | | +Conv2d [N,1,19,500] [N,16,19,250] [1,7] 1 112 | | +BatchNorm2d [N,16,19,250] [N,16,19,250] – – 32 | | +ReLU [N,16,19,250] [N,16,19,250] – – – | +Sequential [N,16,19,250] [N,16,19,250] – – – | | +ResBlock [N,16,19,250] [N,16,19,250] – – – | | | +Conv2d [N,16,19,250] [N,16,19,250] [1,7] 1 1,792 | | | +BatchNorm2d [N,16,19,250] [N,16,19,250] – – 32 | | | +ReLU [N,16,19,250] [N,16,19,250] – – – | | | +Conv2d [N,16,19,250] [N,16,19,250] [1,7] 1 1,792 | | | +BatchNorm2d [N,16,19,250] [N,16,19,250] – – 32 | | | +ReLU [N,16,19,250] [N,16,19,250] – – – | | +ResBlock [N,16,19,250] [N,16,19,250] – – 3,648 | | +ResBlock [N,16,19,250] [N,16,19,250] – – 3,648 | +Sequential [N,16,19,250] [N,32,19,125] – – – | | +ResBlock [N,16,19,250] [N,32,19,125] – – 14,528 | | +ResBlock [N,32,19,125] [N,32,19,125] – – 14,464 | | +ResBlock [N,32,19,125] [N,32,19,125] – – 14,464 | | +ResBlock [N,32,19,125] [N,32,19,125] – – 14,464 | +Sequential [N,32,19,125] [N,64,19,63] – – – | | +ResBlock [N,32,19,125] [N,64,19,63] – – 57,728 | | +ResBlock [N,64,19,63] [N,64,19,63] – – 57,600 | | +ResBlock [N,64,19,63] [N,64,19,63] – – 57,600 | | +ResBlock [N,64,19,63] [N,64,19,63] – – 57,600 | | +ResBlock [N,64,19,63] [N,64,19,63] – – 57,600 | | +ResBlock [N,64,19,63] [N,64,19,63] – – 57,600 | +Sequential [N,64,19,63] [N,128,19,32] – – – | | +ResBlock [N,64,19,63] [N,128,19,32] – – 230,144 | | +ResBlock [N,128,19,32] [N,128,19,32] – – 229,888 | | +ResBlock [N,128,19,32] [N,128,19,32] – – 229,888 | +Sequential [N,128,19,32] [N,16,19,1] – – – | | +Conv2d [N,128,19,32] [N,16,19,26] [1,7] 1 14,336 | | +AdaptiveAvgPool2d [N,16,19,26] [N,16,19,1] – – –

+Linear [N,304] [N,3] – – 912

of the validation set in the nested level differs significantly between the two. In classical machine learning, validation sets are not used for early stopping but are instead used for hyperparameter tuning. Only the final model, retrained using the optimal hyperparameters on the entire training set (without a validation set), contributes to the final cross-validation performance estimate. In deep learning, validation sets are integral for regularization through early stopping, and their creation can heavily influence test set accuracy. Thus, accuracies from the complete ensemble of trained models are vital for determining final cross-validation performance estimates.

##### A.6. Nested cross-validation usage: differences between Machine Learning and Deep Learning

The analysis provided in this study supports the use of subject-based nested cross-validation methods to obtain more reliable performance estimates for EEG deep learning models.Althoughthisstudyprimarilyfocusesondeeplearning application, the validity of this approach can also be expanded to classical machine learning algorithms. However, the differences between the training paradigms betweem classical machine learning models and deep learning models lead to distinct motivations for using nested methods.

In classical machine learning, the validation set is not directly used during training for early stopping purposes. Instead, the validation set plays a crucial role in the model’s hyperparametertuning.Whenarepresentative testsetcannot be created (like in EEG data analysis), the recommended approach for evaluating model performance through crossvalidation is to use nested approaches. The nested level should be used for the hyperparameter tuning, while the outer level should be used to train a new model with the optimal hyperparameters using the entire training data. Additionally, classical machine learning models rely on handcrafted features and typically have a lower number of parameters compared to the training set size, which means they are not overparameterized. While overfitting can still occur, especially if sample-based partition methods are applied, it does not impact the quality of the learned features, as these are hand-crafted. Furthermore, the selection of the validation set has minimal influence on the final crossvalidation accuracy estimate, since regularization does not depend on monitoring validation error during training and the hyperparameters tuning considers the whole set of nested training instances. However, the way folds are created (i.e., train/test splits) can still affect the final accuracy due to significant inter-subject variability.

##### A.7. Preliminary analysis with additional tasks

This section provides a preliminary analysis for the LNSO vs. K-Fold (Subsection 3.1) and the LNSO vs. NLNSO (Subsection 3.1) comparisons with two additional tasks, namely:

- • Sleep deprivation: a binary classification task. It aims to distinguish between subjects in normal or sleep deprived states. Sleep deprived EEGs are widely used for investigation of patients who have seizures or blackouts, representing an important tool for the diagnosis of this neurological disease.
- • Steady State Visually Evoked Potential (SSVEP): a fourclass classification task. It aims to discriminate between responses to different stimuli at specific frequencies (5.45, 6.67, 8.57, and 12 Hz) that were presented in four positions (down, right, left, and up, respectively). SSVEP EEGs are used in a variety of settings, including braincomputer interface applications (e.g., wheelchair control systems) and clinical applications in neuroscience.

The following sections briefly describe the data sets used to construct these tasks.

###### A.7.1. ds004902 - Sleep Deprivation

In contrast, deep learning models used for EEG data analysis actively uses the validation set during training to restore the best weights when updates no longer yield an improvement in the validation loss (early stopping). Unlike classical machine learning, deep learning does not use the nested level for hyperparameter tuning; rather, it assesses how the choice of validation set impacts test accuracy. This is crucial in deep learning because the model automatically extracts features necessary for the task at hand through its encoder block. Deep learning models are often overparameterized, which increases the risk of overfitting. Combined with high inter-subject variability, this can significantly affect the quality of the learned features. In this context, early stopping serves as a key regularization technique. It is essential to have a validation set during training, and the effects of its selection must be carefully evaluated through nested approaches. Therefore, accuracies from the entire ensemble of trained models should contribute the final evaluation process.

- This dataset4, selected from the OpenNeuro platform,

contains resting-state eyes open/closed EEG recordings from 71 healthy subjects (age 20.0 ± 1.4 years). All the subjects underwent two recording sessions (duration 4.9 ± 0.4 minutes). One in a sleep deprived state and the other in normal sleep state. Not all subjects have eyes closed recordings, so only eyes open recordings were used. Raw data were acquired with a 61 channel system (10/10 template, reference on FCZ) at 500 Hz. Preprocessing was performed with the same steps as for the Parkinson’s datasets (see Table 2 in section 2.2). The total number of samples is 9914.

A.7.2. SSVEP

- This dataset5, selected from the GigaDB platform, con-

tains steady-state visually evoked potential EEG data from

- 4D. Salisbury, D. Seebold, and B. Coffman, “EEG: First episode psychosis vs. control resting task 2,” 2022. doi:10.18112/openneuro.ds003947.v1.0.1.
- 5M.-H. Lee, O.-Y. Kwon, Y.-J. Kim, H.-K. Kim, Y.-E. Lee, J. Williamson, S. Fazli, S.-W. Lee, EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy, GigaScience 8 (5) (2019) giz002. doi:10.1093/gigascience/giz002.

In summary, while the concept of using a nested method is valid in both machine learning and deep learning, the role

Median and [25𝑡ℎ − 75𝑡ℎ] percentiles of Balanced accuracy and F1-score for the additional tasks (Sleep Deprivation and SSVEP). Results are reported for each model and cross-validation setting investigated.

K-Fold LNSO N-LNSO Bal. Acc. F1-score Bal. Acc. F1-score Bal. Acc. F1-score

Task Model

0.65 [0.59 − 0.72] EEGNet

99.90 [99.84 − 100.00]

1.00 [1.00 − 1.00]

68.63 [58.80 − 74.47]

0.69 [0.59 − 0.74]

65.68 [58.73 − 73.08]

ShallowConvNet

SleepDeprivation

0.58 [0.51 − 0.64] DeepConvNet

99.95 [99.90 − 100.00]

1.00 [1.00 − 1.00]

62.94 [53.86 − 65.97]

0.59 [0.53 − 0.66]

59.71 [52.50 − 65.16]

0.57 [0.48 − 0.66] T-ResNet

100.00 [99.92 − 100.00]

1.00 [1.00 − 1.00]

67.36 [56.74 − 69.59]

0.67 [0.53 − 0.70]

60.18 [55.19 − 66.03]

75.77 [75.17 − 77.33]

0.76 [0.75 − 0.77]

63.06 [59.39 − 66.10]

0.63 [0.59 − 0.66]

59.57 [56.32 − 62.71]

0.59 [0.55 − 0.63]

0.93 [0.90 − 0.95] EEGNet

95.88 [95.66 − 96.15]

0.96 [0.96 − 0.96]

94.28 [92.99 − 95.84]

0.94 [0.93 − 0.96]

92.64 [89.90 − 94.60]

ShallowConvNet

0.97 [0.95 − 0.98] DeepConvNet

97.62 [97.25 − 97.89]

0.98 [0.97 − 0.98]

97.75 [96.59 − 98.44]

0.98 [0.97 − 0.98]

97.18 [95.34 − 98.05]

SSVEP

0.97 [0.94 − 0.97] T-ResNet

97.43 [97.00 − 97.88]

0.97 [0.97 − 0.98]

97.38 [96.36 − 98.22]

0.97 [0.96 − 0.98]

96.52 [94.07 − 97.47]

95.49 [95.23 − 95.59]

0.95 [0.95 − 0.96]

97.42 [93.69 − 97.79]

0.97 [0.94 − 0.98]

96.45 [93.05 − 97.25]

0.96 [0.93 − 0.97]

Table 9 Learning rate grid for the additional tasks.

Sleep Deprivation

Model

SSVEP

ShallowConvNet 5.0 ⋅ 10−5 7.5 ⋅ 10−4 EEGNet 1.0 ⋅ 10−3 7.5 ⋅ 10−4 DeepConvNet 2.5 ⋅ 10−4 1.0 ⋅ 10−3 T-ResNet 5.0 ⋅ 10−5 1.0 ⋅ 10−3

54 healthy subjects (age 24.2 ± 3.0 years). All the subjects underwent two recording sessions divided in two separate phases. Each phase contained 100 trials, 25 per class, associated with the response to different stimuli at specific frequencies (5.45, 6.67, 8.57, and 12 Hz) that were presented in four positions (down, right, left, and up, respectively). Each trial lasted 4 seconds. Raw data were acquired with a 62 channel system (10/10 Template, nasion-referenced and grounded to electrode AFz) at 1000 Hz. Preprocessing was performed with the same steps as for the BCI datasets (see Table 2 in section 2.2). The total number of samples is 21600.

Learning rates were selected using the same procedure described in subsection 2.4.1 and are listed in Table 9. Other values of the training hyperparameters (e.g., seed, batch size, optimizer) were left unchanged.

Table 8 reports accuracy and F1-score metrics. Sleep deprivation results further support the conclusions of this study. The median values decrease when moving from the sample-based K-fold method to LNSO, and further from LNSO to N-LNSO. In addition, the interquartile range increases when sample-based approaches are compared to

subject-based approaches. The SSVEP task appears to produce very high cross-subject accuracy and F1 scores, making it difficult to compare cross-validation methods. Nevertheless, this preliminary analysis reinforces the conclusions of this study and highlights the importance of using nested approaches to evaluate EEG deep learning models.

