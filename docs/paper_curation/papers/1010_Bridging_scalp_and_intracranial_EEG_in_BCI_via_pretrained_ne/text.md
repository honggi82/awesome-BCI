# arXiv:2604.14202v1[q-bio.NC]3Apr2026

## Bridging scalp and intracranial EEG in BCI via pretrained neural representations and geometric constraint embedding

##### Yihang Dong1,2, Changhong Jing1, Shuqiang Wang1,2*

1Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen, China. 2University of Chinese Academy of Sciences, Beijing, China.

*Corresponding author(s). E-mail(s): sq.wang@siat.ac.cn;

Abstract Electroencephalography (EEG) has become one of the key modalities underpinning brain–computer interfaces (BCIs) due to its high temporal resolution, rapid responsiveness, non-invasiveness, low cost, and portability. However, EEG signals are substantially inferior to intracranial EEG (iEEG) in signal-to-noise ratio and local spatial resolution, whereas iEEG suffers from extremely limited clinical accessibility owing to its invasive nature, hindering widespread application. To address this challenge, this study proposes a unified data- and prior knowledge–driven framework for EEG–iEEG representational enhancement. Guided by the principle that “geometric structure dictates function” , the framework maps static cortical anatomy onto dynamic constraints governing neural signal propagation and integrates general-purpose neural representations extracted by a pre-trained large EEG model to explicitly model signal transmission through the brain. Enhanced EEG signals are then synthesized via a multidimensional representation diffusion process. Numerous experimental results demonstrate that the generated enhanced EEG signals effectively recover the neural activity patterns lost during propagation through the brain. This finding indicates that the performance ceiling of BCIs is constrained not only by acquisition hardware but also by the depth to which the generative model resolves the mechanisms of neural signal propagation. Collectively, the proposed framework provides a viable pathway toward acquiring high-fidelity neural signals at low cost.

In recent years, BCI technologies have demonstrated substantial application potential in neurorehabilitation, human–machine interaction, and defense domains, a potential that hinges critically on accurate decoding of neural activity [1–5]. Multiple neuroimaging modalities including functional magnetic resonance imaging (fMRI), functional ultrasound (fUS), and functional near-infrared spectroscopy (fNIRS) have been employed for BCI decoding [6, 7]; however, these modalities generally suffer from insuﬀicient temporal resolution, slow response latency, high instrumentation costs, and stringent acquisition environments, rendering them ill-suited for real-time, dynamic neural decoding. In contrast, EEG has emerged as the preferred signal source for non-invasive BCI

owing to its millisecond-scale temporal resolution, rapid responsiveness, non-invasiveness, low cost, and high portability [8–10]. Intracranial EEG (iEEG) encompassing electrocorticography (ECoG), multielectrode arrays, and stereoelectroencephalography (sEEG) is regarded as the cornerstone modality for invasive BCI due to its direct recording of cortical electrical activity and exceptional signal-to-noise ratio [11, 12]. Nevertheless, EEG signals are inherently limited by volume conduction and skull attenuation, and are highly susceptible to artifacts from multiple sources. Conversely, iEEG requires craniotomy, resulting in extremely limited clinical accessibility [13]. These constraints severely impede the advancement of non-invasive and invasive BCI in terms of signal fidelity and

widespread applicability, respectively. Consequently, enhancing non-invasive EEG signals to approximate the neural activity representational capacity of iEEG, thereby yielding enhanced EEG signals, constitutes a pivotal step toward realizing high-performance, non-invasive, lowcost, and portable BCI systems.

However, the key of EEG signal enhancement does not lie in investigating the neural sources or their activation states, but rather in learning the neural activity representations lost during signal propagation. The former, which aims to localize the origin of neural electrical activity, generally falls under EEG source imaging and fundamentally addresses the question “where is the neural activity generated?” [14, 15]. In contrast, this study aims to generate high-fidelity enhanced EEG signals to improve performance on downstream BCI tasks. Recently, Bahman Abdi-Sargezeh and colleagues attempted to map EEG directly to iEEG using deep neural networks in an endto-end manner [16–18]. Although these studies preliminarily demonstrate the potential of datadriven approaches in modeling complex nonlinear mappings, their task formulation is inherently limited to signal-level fitting and cannot achieve generalizable EEG signal enhancement. On the other hand, Miao Cao and colleagues proposed reconstructing iEEG from magnetoencephalography (MEG) signals using an LCMV beamformer [19]. However, this approach remains constrained by linear assumptions and simplified brain models, yielding reconstructions insuﬀicient for high-precision BCI applications. More critically, MEG systems are prohibitively expensive, require stringent magnetically shielded environments, and are impractical for bedside or long-term monitoring scenarios. In comparison, EEG offers superior portability, broad accessibility, and low cost, making it a more viable modality for real-world BCI deployment [20].

Unlocking this modality’s potential requires overcoming limitations in modeling physical constraints. The brain exhibits intrinsic structure-function coupling, with cortical geometry as the scaffold shaping neural activity and encoding biophysical boundary conditions governing signal generation, propagation, and integration [21, 22]. Geometric modal decomposition maps static anatomy into dynamic functional priors, revealing embedded spectral properties and establishing a principled pathway for structure-guided signal enhancement [23,

24]. Incorporating geometric priors compensates for information loss in non-invasive recordings, shifting reconstruction from data-driven toward a structure–function coupled paradigm and laying a theoretical foundation for next-generation high-fidelity EEG enhancement.

To address these challenges, we propose a unified EEG–iEEG representation enhancement framework that integrates data-driven learning with neurodynamical priors, as shown in Figure 1. The framework comprises four core components. First, a pretrained large EEG model is employed to extract generalpurpose EEG representations, thereby strengthening the modeling capacity for neural activity patterns [25, 26]. Second, explicit biophysical constraints are incorporated through joint modeling of neural mass models and neural field equations, ensuring that the enhanced signals adhere to the electrophysiological dynamics governing brain activity [27, 28]. Third, to account for the complex geometric morphology of the brain, the proposed method processes T1-weighted MRI data via geometric mode decomposition to compute structurally informed priors across frequency bands, which model the attenuation of neural signals during propagation through skull and brain tissues and thereby enable recovery of lost neural representations during enhancement [29, 30]. Fourth, a multidimensional EEG feature encoder fuses the above three elements—representations, dynamical constraints, and structural priors—to generate features that precisely capture the coupling between long-range neural synchrony and local high-frequency activity; a diffusion model then guides the generation of enhanced EEG signals to improve their intrinsic fidelity to underlying neural activity patterns.

Systematic evaluation across 14 diverse EEG datasets spanning multiple task types including emotion recognition shows that the proposed EEG–iEEG unified representational enhancement framework significantly improves the fidelity with which scalp EEG captures intracranial neural activity, without requiring invasive recordings or hardware upgrades. This work thus enables low-cost acquisition of highfidelity enhanced EEG signals and provides a new technical pathway to overcome the performance bottlenecks of current non-invasive BCI.

###### d.

a.

Data + Knowledge based Unified EEG Representation Enhancement Framework

Image Text Voice

Application

[Figure 1]

Frequency Domain Visualization(dB/Hz)

Frequency Domain Visualization(dB/Hz)

Scalp

| |[Figure 2]<br><br>Frequency/Hz| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

Decoder

| |[Figure 3]<br><br>Frequency/Hz| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

0.5

0.5

0.4

[Figure 4]

0.4

0.3

0.3

else…

Skull

0.2

0.2

BCI Decoding

0.1

0.1

0

0

10 20 30 40 50

10 20 30 40 50

0

0

[Figure 5]

Real Invasive EEG

Original EEG

[Figure 6]

Original EEG

[Figure 7]

[Figure 8]

Cerebral cortex

[Figure 9]

[Figure 10]

Proposed Model

Paired training data

Model training

Enhanced EEG

Data + Knowledge based

Assist

Trainable

Unified brain electrical signal Representation Enhancement Model

Clinical Medical Assistance

###### Test inference

Frozen

Trained Model

Enhanced EEG

Original EEG

Emotion

[Figure 11]

|b.|
|---|
|Brain Electrical Signal Representation Enhancement Model|
||Signal Trend<br><br>[Figure 12]|
|---|
<br><br>|Original EEG|
|---|
<br><br>Neurodynamics<br><br>|Time domain feature<br><br>[Figure 13]|
|---|
<br><br>Geometric Decomposition<br><br>|[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>Spectral domain feature|
|---|
<br><br>Pre-trained model<br><br>|T1 MRI|
|---|
<br><br>Generative AI Based Representation Computing Module<br><br>|Enhanced EEG|
|---|
|

c.

Enhanced EEG

Enhanced EEG Display

Language

|[Figure 17]<br><br>[Figure 18]<br><br>[Figure 19]<br><br>0 Hz 100 Hz<br><br>Real iEEG<br><br>Synthesized iEEG<br><br>Original EEG<br><br>[Figure 20]<br><br>[Figure 21]<br><br>[Figure 22]<br><br>[Figure 23]<br><br>Real iEEG<br><br>0<br><br>10 20 30 40 50<br><br>0.5<br><br>0.2<br><br>0<br><br>0.1<br><br>0.3<br><br>0.4<br><br>Frequency Domain Energy Distribution (db/Hz)<br><br>Original EEG Synthesized iEEG<br><br>Hz<br><br>[Figure 24]<br><br>[Figure 25]<br><br>-1<br><br>20 40<br><br>1<br><br>0<br><br>0<br><br>10 30 50<br><br>Frequency Domain Time Domain<br><br>Enhanced iEEG Real iEEG<br><br>[Figure 26]<br><br>[Figure 27]<br><br>[Figure 28]<br><br>0.1<br><br>0.05<br><br>[Figure 29]|
|---|

Visual

Motion

Brain Function Area Research

Structure determines function

[Figure 30]

[Figure 31]

Function reflects structure

Brain Structure-Function Coupling Mechanism Analysis

- Figure 1 Schematic of the proposed framework. a, Data- and knowledge-based unified EEG representation enhancement framework. The model is trained with scalp EEG as input and iEEG as the target; during inference, enhanced EEG signals are generated from scalp EEG alone. b, Detailed architecture of the enhancement model, integrating a data-driven module, a neurodynamical–geometric constraint module, and a generative AI–based representation module. Individualized T1-weighted MRI can be incorporated alongside EEG to further improve performance. c, Multidimensional visualization of enhanced EEG signals, including spectral power distribution, spatial maps of band-specific activity, and temporal waveform morphology, collectively demonstrating recovery of neurophysiologically relevant features. d, Applications of the proposed framework, encompassing improved BCI decoding accuracy, enhanced BCI fairness , and support for brain functional mechanism research.

### Results

#### Consistency evaluation between synthesized iEEG and ground-truth iEEG

This study aims to enhance EEG signals using the proposed framework to generate highfidelity synthesized iEEG and evaluate its consistency with real iEEG. Given that neural activity representations inherently couple temporal dynamics, spectral energy distribution, and spatial propagation characteristics, similarity along a single dimension is insuﬀicient to fully validate the physiological plausibility of the

generated signals. Therefore, this set of experiments is conducted across multiple complementary dimensions: spectral, temporal, time– frequency joint structure, and inter-channel correlation. Specifically, in the spectral domain, power spectral density similarity (PSD Sim) and spectral feature similarity (Freq Sim) are used to assess consistency in energy distribution and rhythmic structure [31]; in the temporal domain, Pearson correlation coeﬀicient (PCC) and cosine similarity (Cos Sim) quantify the alignment of waveform morphology and dynamic evolution trends [32, 33]; additional metrics include phase consistency to capture time–frequency coupling properties and Frobenius norm similarity of inter-channel correlation matrices

(CorrMat Sim) to reflect connectivity fidelity at the channel level [34, 35]. The results demonstrate that the proposed framework effectively enhances EEG signals and recovers the neural activity representations lost during signal transmission through the brain’s anatomical structure.

As shown in Figure 2a, synthesized iEEG guided by real EEG (blue) significantly outperforms the noise-guided control signal (yellow) across all six evaluation metrics. In the spectral domain, PSD Sim and Freq Sim reach 0.51 and 0.50, respectively—both consistently exceeding the physiologically meaningful threshold of 0.5 and improving by more than 0.4 over the noise-guided baseline. This result directly confirms that the framework effectively compensates for high-frequency energy loss caused by skull attenuation and reconstructs attenuated rhythmic spectral structures. Further analysis of temporal characteristics reveals a PCC of 0.38 and a Cos Sim of 0.57, indicating strong alignment between synthesized iEEG and real iEEG in waveform dynamics and instantaneous amplitude distribution. In the additional dimensions, Phase Consistency reaches 0.52, further validating the physiological plausibility of synthesized iEEG in time–frequency coupling; its phase synchrony not only markedly surpasses that of the noise-guided signal but also closely matches the neural oscillatory dynamics of real iEEG. Collectively, the coordinated improvement across multiple metrics demonstrates that the proposed framework successfully learns the high-dimensional dynamic representations lost during neural signal transmission through brain anatomy.

To assess the representational capacity of the reconstructed signals, Figure 2b presents tSNE visualizations of three signal types [36]: real EEG–guided synthesized iEEG (blue),

real iEEG (red), and noise-guided iEEG (yellow), labeled as Synthesized iEEG, Real iEEG, and Noise, respectively. In the time–frequency embedding space, synthesized iEEG clusters tightly with real iEEG, whereas the noise-guided signal is distinctly separated. This result demonstrates that the proposed framework effectively learns a general time–frequency representation distribution closely aligned with real iEEG and substantially enhances the original EEG signal, markedly outperforming the unstructured, noise-guided generation approach.

Finally, Figure 2c displays heatmaps of fullchannel correlation matrices for the three signal types, with focused comparison in five regions exhibiting prominent functional connectivity. The synthesized iEEG generated under real EEG guidance successfully reproduces the local clustered connectivity and long-range crossregional synchronization patterns observed in real iEEG. In contrast, the noise-guided signal lacks such structure, exhibiting diffuse correlations without discernible topological features. This finding provides strong evidence that the proposed enhancement framework faithfully reconstructs the inter-channel structural topology characteristic of iEEG, achieving highfidelity emulation of cortical electrophysiological activity.

#### Performance gains of enhanced EEG signals in downstream tasks

Experiments on twelve diverse BCI downstream task datasets—including motor imagery and cognitive detection—demonstrate that the proposed framework yields high-fidelity enhanced EEG signals at low cost and consistently improves task performance. Specifically, the framework was first applied to generate enhanced signals on twelve public EEG– BCI datasets, and the performance difference

Freq Sim with real iEEG

Phase Consistency with real iEEG

PSD Sim with real iEEG

- a.
- b.

c.

Real iEEG Correlation Matrix

[Figure 32]

0.8

0.8

0.8

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

| |
|---|

0.6

0.6

0.6

| |
|---|

| |
|---|

0.4

0.4

0.4

| |
|---|

| |
|---|

0.2

0.2

0.2

0.0

0.0

0.0

Synthesized iEEG

Noise

Synthesized iEEG

Synthesized iEEG

Noise

Noise

PCC with real iEEG

Matrix Sim with real iEEG

Cos Sim with real iEEG

Synthesized iEEG Correlation Matrix

0.5

0.5

0.8

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

[Figure 33]

| |
|---|

0.4

0.4

0.6

0.3

0.3

| |
|---|

| |
|---|

0.2

0.4

0.2

| |
|---|

0.1

0.2

| |
|---|

0.1

0.0

-0.1

0.0

0.0

Synthesized iEEG

Synthesized iEEG

Synthesized iEEG

Noise

Noise

Noise

[Figure 34]

[Figure 35]

Frequency domain t-SNE visualization of three signals Time domain t-SNE visualization of three signals

Noise Correlation Matrix

[Figure 36]

| |
|---|

| |
|---|

| |
|---|

| |
|---|

| |
|---|

- Figure 2 Multidimensional validation of consistency between synthesized iEEG and real iEEG. a, Across six complementary metrics—spectral (PSD Sim, Freq Sim), temporal (PCC, Cos Sim), and time–frequency coupling (Phase Consistency, CorrMat Sim)—synthesized iEEG generated from EEG (blue) significantly outperforms noise-driven controls (yellow), demonstrating effective recovery of high-dimensional neural dynamics lost to skull attenuation and volume conduction. b, t-SNE embeddings in the time–frequency domain show tight clustering of synthesized iEEG with real iEEG (red), while noise-driven signals (yellow) are distinctly separated, confirming acquisition of a physiologically plausible joint time–frequency representation. c, Heatmaps of full-channel correlation matrices reveal that synthesized iEEG recapitulates the local clustered and long-range synchronized connectivity patterns observed in real iEEG within five key functional networks, whereas noise-driven reconstructions lack such neurophysiologically specific topological structure.

between original and enhanced signals was quantified under identical experimental conditions. Second, on the SEED benchmark dataset for emotion recognition, topographic maps were used to visualize and compare activation patterns in emotion-relevant brain regions before and after enhancement, thereby validating the physiological plausibility of the enhanced signals. Finally, SHAP (SHapley Additive exPlanations) analysis was employed to examine shifts

in channel contribution rankings for the emotion classification task, providing further evidence that the enhanced signals deliver meaningful performance gains over raw EEG [37].

As shown in Figure 3a, enhanced EEG signals consistently improve downstream classification performance across all twelve multi-task EEG datasets, with gains ranging from 2.8% to 8.6%. Notably, the improvements are most pronounced in emotion and cognitive state decoding

tasks: on the DEAP dataset for emotion classification, the F1 score increases by 8.6%; in cognitive state classification, the gain reaches

- 8.5%; and on the four-class SEED-IV emotion recognition task, performance improves by 8.1%. Across all datasets, the proposed framework achieves an average performance gain of 5.2%, demonstrating its ability to effectively recover high-frequency neural activity representations lost during signal propagation through complex brain tissues, including the skull, scalp, and cerebrospinal fluid, and thereby enhance the generalization capability of the generated EEG signals in downstream tasks.

To further validate physiological plausibility, a visualization analysis was conducted on the SEED emotion recognition dataset.

- Figure 3b displays topographic maps of raw and enhanced EEG under positive, neutral, and negative emotional states. Raw EEG exhibits diffuse, shallow-red activation across the entire scalp, indicating weak and spatially disorganized neural activity in emotion-relevant regions. In contrast, enhanced EEG reveals focal, highintensity activation, manifested as concentrated deep-red clusters, in the dorsolateral prefrontal cortex and bilateral temporal lobes, areas well established in emotion processing [38–40]. This pattern aligns closely with known neurophysiological mechanisms of emotion, confirming that the proposed framework enhances EEG signals in a manner consistent with underlying brain physiology while improving downstream task performance.

Finally, SHAP was employed to quantify the contribution of each EEG channel to the emotion classification task. As shown in Figure 3c, the top five channels with highest contribution in the enhanced signal, including Fp1 and Fz, are localized within the prefrontal limbic system, matching the canonical neuroanatomical substrates of emotion processing [38–40]. In

contrast, high-contribution channels in the raw signal are scattered across non-specific regions such as the parietal Pz. The Spearman correlation coeﬀicient between channel rankings and the ground-truth emotion-related topography increases from 0.41 in raw EEG to 0.62 in enhanced EEG, directly demonstrating that the framework selectively learns task-relevant neural activity representations from physiologically meaningful regions.

#### Impact analysis of geometric constraints on iEEG signal reconstruction performance

This study processes T1-weighted MRI using a geometric modal decomposition method to obtain a set of geometric features representing cortical curvature. This geometric feature set is incorporated into the proposed enhancement framework to explicitly model the complex geometric constraints of the cerebral cortex and the associated mechanisms of electrical signal transmission, thereby enabling the framework to capture high-dimensional dynamic neural information lost during propagation of neural signals through multi-scale brain structures [29]. This experimental series systematically evaluates the impact of the T1-MRI–based geometric modal decomposition on iEEG reconstruction performance through three core analyses: first, differential decomposition of the T1-MRI signal is performed and the resulting geometric features are visualized; second, under identical experimental conditions, each derived geometric feature set is fed into the proposed framework to generate synthesized iEEG, and its consistency with real iEEG is assessed using multiple quantitative metrics; third, for each geometric feature set comprising N features, an intra-set correlation matrix is computed to quantify feature redundancy, providing a qualitative basis

###### a.

0.60

0.7

0.8

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

###### HR-EEG4EMO

0.6

0.7

0.55

###### Seed-IV

###### Deap

0.6

0.5

0.50

0.5

0.4

0.4

0.45

0.3

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

0.7

0.6

0.8

###### BCICompetitionIV-2b

###### BCICompetitionIV-2a

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

###### MULTI-CLARID

0.7

0.5

0.6

0.6

0.4

0.5

0.3

0.5

0.4

0.2

0.4

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

0.8

0.8

0.8

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

0.7

Physionet

0.7

0.7

Seed-V

0.6

Seed

0.5

0.6

0.6

0.4

0.5

0.3

0.5

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

0.60

0.60

CHB-MITEEGDatabase

0.80

0.8

0.8

FaceprocessingEEG

###### Stateclassification

0.55

0.55

0.75

###### SEED-V

###### SEED-V

0.7

0.7

0.70

0.50

0.50

0.6

0.6

0.65

0.45

0.45

0.5

0.5

0.60

0.40

0.40

0.55

0.4

0.4

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Accuracy Precision Recall F1 Score

Original EEG Enhanced EEG

Original EEG Enhanced EEG

###### b.

###### c.

Original

SEED Dataset

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

Original

MidlineFronto-Central

[Figure 42]

[Figure 43]

[Figure 44]

Occipital Temporo-Parietal

AnteriorFrontal

FrontalPole

Frontal

Fronto-Central

Temporal

Fronto-Temporal

Centro-Parietal MidlineParietal

Central

Parietal

MidlineCentral

MidlineFrontal

Enhanced

Enhanced

SEED-V Dataset

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

Original

MidlineFronto-Central

FrontalPole

Temporo-Parietal

AnteriorFrontal

Frontal

Fronto-Central

Central

MidlineFrontal

Temporal

Fronto-Temporal

MidlineParietal

Parietal

MidlineCentral

Occipital

Centro-Parietal

[Figure 49]

[Figure 50]

[Figure 51]

Enhanced

- Figure 3 Performance gains and neurophysiological validity of enhanced EEG across diverse BCI tasks. a, Across 12 EEG datasets spanning motor imagery emotion and cognitive decoding enhanced EEG boosts classification F1 scores by 2.8% to

- 8.6% (mean 5.2%) indicating recovery of high-frequency neural dynamics lost to tissue filtering. b, On SEED topographic maps show enhanced EEG yields focal high-intensity activation in dorsolateral prefrontal and bilateral temporal regions consistent with emotion circuitry whereas raw EEG shows diffuse weak activity. c, SHAP analysis reveals top channels in enhanced EEG such as Fp1 and Fz cluster in prefrontal limbic areas and their importance ranking correlates more strongly with emotion-related localization rising from 0.41 to 0.62.

for selecting the optimal value of N in geometric constraint modeling.

The incorporation of T1-weighted MRI structural information enables the proposed framework to preserve static anatomical specificity while explicitly modeling the modulatory effects of cortical curvature and topology on neural signal conduction, allowing the generated enhanced EEG signals to effectively approach the high-dimensional neural representational capacity of iEEG. This advancement further drives non-invasive BCI signal enhancement from empirical data fitting toward interpretable modeling grounded in structure–function coupling principles.

Figure 4a displays the visualization of eight geometric feature sets obtained via cortical geometric mode decomposition. Features derived at low N values (N = 2–5) exhibit coarse-grained spatial patterns, primarily capturing large-scale cortical geometry. As N increases to 20–100, the features become progressively refined, resolving gyral- and sulcal-level anatomical details.

As shown in Figure 4b, the consistency between synthesized iEEG and real iEEG exhibits a non-monotonic trend with increasing N: performance initially rises, then fluctuates, and eventually declines, peaking at N = 20, where Freq Sim reaches 0.50, PSD Sim 0.51, PCC 0.38, and Cos Sim 0.57. This set of experiments demonstrates that an optimal precision threshold exists between cortical geometric constraint modeling and the overall framework; both insuﬀicient and excessive numbers of geometric features degrade framework performance to some extent, thereby compromising the fidelity of the synthesized iEEG.

The correlation matrix heatmap in

- Figure 4c further reveals the interdependencies and structural properties among the cortical geometric modal features.. When N ≤ 10, the matrices display deep-red, block-like regions

of strong correlation, indicating high feature redundancy. At N = 20–40, the main diagonal becomes distinctly prominent while off-diagonal correlations remain moderate, reflecting a balance between structural independence and necessary physiological coupling. When N ≥ 50, the matrices exhibit highly disordered patterns with substantial noise and diminishing feature coherence, consistent with the quantitative performance decline observed in Figure 4b.

#### Contribution analysis of individual components in the enhancement framework

The effectiveness of the proposed framework stems from its systematic integration of data-driven representations, neural dynamics constraints, and geometric structural priors. To dissect the mechanistic contributions of these components to EEG signal enhancement, ablation experiments were conducted focusing on three core elements: the Pretrained EEG Representation Encoder (PERE), the Neural Dynamics Constraint (NC), and the Geometric Constraint (GC). The experimental design comprises three parts. First, on a simultaneously recorded EEG iEEG dataset, eight ablation configurations were evaluated to quantify the individual and synergistic effects of each component on multi-dimensional reconstruction metrics, including spectral and temporal domains. Second, on the SEED emotion recognition dataset, topographic maps of enhanced EEG signals generated under each ablation setting were visualized to qualitatively assess whether the activation patterns align with known emotionrelated cortical regions and to compare enhancement outcomes across configurations. Third, the impact of each ablation setup on downstream discriminative performance was evaluated on two classification tasks, MULTI-CLARID and SEED, to reveal the relative priority of each

a. b.

###### Reconstruction results under different geometric mode decompositions

- Mode 2
- Mode 3
- Mode 4
- Mode 5

[Figure 52]

0.8

0.6

###### FreqSim

0.4

[Figure 53]

0.2

0.0

0.8

[Figure 54]

0.6

###### PSDSim

0.4

[Figure 55]

0.2

0.0

Mode 10

0.6

[Figure 56]

0.4

###### PCC

Mode 20

0.2

[Figure 57]

0.0

1.0

Mode 50

[Figure 58]

0.8

CosSim

0.6

0.4

Mode 100

[Figure 59]

0.2

0.0

c.

[Figure 60]

[Figure 61]

[Figure 62]

- Figure 4 Impact of T1-MRI–derived geometric constraints on iEEG reconstruction fidelity. a, Eight geometric modal features extracted from T1 MRI show coarse large-scale patterns at low N (2–5) and progressively finer gyral-level detail as N increases to 20–100. b, Consistency between synthesized and real iEEG peaks at N = 20 (Freq Sim 0.50 PSD Sim 0.51 PCC 0.38 Cos Sim 0.57) then declines with further increases in N revealing an optimal precision threshold for geometric constraint modeling. c, Correlation matrix heatmaps illustrate feature redundancy at N ≤ 10 strong diagonal dominance with moderate off-diagonal structure at N = 20–40 indicating balanced independence and physiological coherence and increasing noise and loss of structure at N ≥ 50 consistent with performance trends in b.

component in terms of neural information recovery and task adaptation. In this notation,“Full” denotes the complete enhancement framework incorporating PERE, NC, and GC, while all other settings are labeled as“w/o X”to indicate the removal of the corresponding component.

As shown in Figure 5a, the full framework achieves superior performance across all four metrics compared to every ablation variant. Specifically, Freq Sim and PSD Sim reach 0.50 and 0.51 under the full framework, representing an improvement of over 50% relative to the backbone-only baseline; PCC and Cos Sim attain 0.38 and 0.57, respectively, also showing consistent gains. Ablation analysis reveals that removing PERE causes the largest performance drop, with reductions exceeding 0.08 in both Freq Sim and PCC, indicating that the general-purpose time–frequency representations provided by PERE form the foundational support of the framework. Removal of GC substantially degrades PSD Sim, highlighting the critical role of geometric constraint modeling in enhancing spectral fidelity. Although NC contributes relatively modestly when introduced alone, it consistently improves phase consistency in combination with other components, demonstrating its effectiveness in capturing the temporal evolution of neural electrical activity. These results confirm a nonlinear complementary relationship among the three components, where the absence of any single element leads to a marked decline in overall performance, thereby validating their irreplaceable roles within the framework.

Figure 5b displays topographic maps of enhanced EEG signals under eight ablation settings on the SEED dataset, where color intensity reflects channel activation strength. Darker red indicates higher activation and darker blue indicates lower activation. In the first four ablation conditions, activation patterns appear diffuse

and lack spatial focus. In contrast, the latter four configurations show markedly more focal activation, particularly in the left temporal lobe and temporo-occipital junction [40, 41]. Notably, the topography generated by the full framework exhibits not only concentrated high-activation regions but also clear intensity gradients that closely match the spatial patterns of genuine emotion-evoked EEG. This qualitative observation aligns precisely with the quantitative results in Figure 5c, corroborating the effectiveness of each component in EEG signal enhancement.

Figure 5c presents performance changes on two downstream classification tasks, MULTICLARID and SEED. As PERE, GC, and NC are incrementally incorporated, model accuracy increases monotonically on both datasets. The full framework achieves 0.48 on MULTICLARID and 0.60 on SEED, corresponding to improvements of 84% and 39% over the backbone-only baseline, respectively. These findings demonstrate that the proposed framework establishes a multidimensional synergistic enhancement architecture by integrating general-purpose representations, neural dynamics constraints, and geometric structure modeling, thereby achieving both higher fidelity in enhanced EEG signals and robust performance gains across diverse downstream tasks.

#### Contribution analysis of EEG signals across frequency bands to enhancement outcomes

To quantify the contribution of distinct neural oscillatory bands to EEG signal enhancement, this section systematically evaluates the reconstruction performance of the delta, theta, alpha, beta, and gamma frequency bands under the unified framework. Results reveal pronounced spectral specificity in the enhancement effect, with high-frequency components playing

###### a.

0.8

0.8

0.6

0.6

###### FreqSim

###### PSDSim

0.4

0.4

0.2

0.2

0.0

0.0

0.8

1.0

0.8

0.6

###### CosSim

0.6

###### PCC

0.4

0.4

0.2

0.2

0.0

0.0

- b.
- c.

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

Backbone-only w/o PERE & NC w/o PERE & GC w/o NC & GC w/o PERE w/o GC w/o NC Full

0.8

0.6

AcconMulti-Clarid

AcconSEED

0.6

0.4

0.4

0.2

0.2

0.0

0.0

- Figure 5 Ablation study of framework components. a, The full model (PERE + NC + GC) achieves highest fidelity across all metrics; removing PERE causes the largest drop while GC and NC provide complementary gains in spectral and phase consistency. b, Only the full model yields focal activation in emotion-relevant regions on SEED matching known neurophysiological patterns; ablated variants show diffuse activity. c, Downstream accuracy on MULTI-CLARID and SEED rises with component integration reaching 0.48 and 0.60 which are 84% and 39% above baseline confirming synergistic enhancement from data-driven representation neurodynamics and geometry.

a dominant role in recovering localized neural activity and spatial organization.

### Discussion

To address the performance ceiling of noninvasive brain–computer interfaces imposed by

the measurement-centric paradigm of traditional neural engineering, this study reframes the generation of enhanced brain signals as a Bayesian inference process and proposes a unified EEG enhancement framework that jointly integrates cortical geometry and function. By incorporating T1-weighted MRI to capture the brain’s geometric architecture and underlying physical laws, the framework establishes a structural foundation for representing functional brain patterns, enabling EEG enhancement without any modification to acquisition hardware and allowing enhanced EEG signals to approach the representational capacity of invasive recordings. This work marks a paradigm shift in BCI signal enhancement from black-box data fitting toward neural signal computation grounded in the principle that geometry shapes function.

The performance of the current framework remains constrained by several key factors. First, the scarcity of synchronized scalp EEG and iEEG paired recordings, combined with the limited scale and generalizability of existing pretrained EEG models, jointly restrict the model’ s capacity to learn complex neural propagation mechanisms and high-frequency dynamic features [25]. Second, substantial heterogeneity across studies in experimental paradigms, acquisition protocols, and task designs introduces considerable electromyographic, ocular, and environmental noise during data collection, which often obscures underlying neural activity, severely degrades EEG signal-to-noise ratio, and consequently limits both the upper bound of enhancement eﬀicacy and cross-task robustness [42]. Third, the present framework incorporates neurodynamical constraints only at the mesoscale, focusing on mean-field modeling of neural population activity; microscale singleneuron dynamics and macroscale inter-regional network coupling have not yet been integrated

due to challenges in task adaptability and computational complexity, thereby limiting its ability to fully capture multiscale neural dynamics. Collectively, these factors constrain further improvements in the fidelity of enhanced EEG signals and underscore the necessity of evolving from a “generic enhancement”paradigm toward one of “task- and subject-coordinated optimization.”

Future work could explore region-specific generative strategies targeting functionally defined brain areas, by integrating local anatomical priors with region-specific neurodynamical models to enable precise reconstruction and modulation of electrical activity in designated cortical regions [43]. This direction would shift EEG enhancement from “global signal reconstruction”toward“task-driven enhancement of specific neural activity,”thereby substantially improving the fidelity of downstream task modeling [44]. Moreover, such a strategy has the potential to significantly reduce reliance on high sensor density and large channel counts while maintaining high reconstruction fidelity, offering a critical technical foundation for nextgeneration non-invasive brain–computer interfaces that are lightweight, comfortable, and suitable for long-term wear.

Furthermore, this study proposes a threestage evolutionary paradigm as a foundational roadmap for the future development of EEG signal enhancement, illustrated in Figure 6. The lower tier, Stage 1, establishes a neural representation foundation model based on “data plus knowledge,”which learns universal principles of neural signal propagation by integrating large-scale datasets of EEG, iEEG, and MEG with neuroscientific priors to compute shared representations of neural activity patterns, thereby enabling robust cross-scenario transfer and multi-dataset generalization. The

middle tier, Stage 2, implements scenariooriented fine-tuned adaptation: the neural representation foundation model is further fine-tuned on task-specific BCI datasets—such as those for affective computing or motor imagery—to yield a scenario-specific adaptation module. Integration of this module endows the enhancement framework with strong contextual adaptability, allowing it to generate EEG enhanced signals that are better aligned with the demands of a given application domain. The upper tier, Stage 3, focuses on personalized representation enhancement. Here, subject-specific calibration data are used to perform personalized finetuning of the Stage 2 module, enabling individualized modeling across participants and producing EEG enhanced signals with maximized fidelity—critical for advanced applications such as high-precision BCI control and targeted cortical activity reconstruction. When individualized data are scarce, zero-shot learning strategies can be employed to partially compensate and improve model performance.

This three-stage paradigm not only offers a systematic solution to current bottlenecks —including data scarcity, low signal-to-noise ratio, and task heterogeneity, but also marks a paradigm shift in non-invasive brain–computer interfaces from passive signal enhancement toward active neural information reconstruction. Pursuing this trajectory, future BCI systems are expected to achieve high fidelity, task adaptability, and individual interpretability while maintaining hardware lightweightness, thereby enabling robust deployment in critical real-world applications such as neurorehabilitation, human–machine interaction, and defense.

### Methods

clinical inaccessibility of iEEG due to its invasive nature, this study proposes a unified EEG– iEEG representation enhancement framework that synergistically integrates data-driven learning with neuroscientific priors. The framework enhances raw EEG signals by jointly leveraging a pretrained large-scale EEG model, neural dynamics constraints, and brain geometric modeling. Its primary objective is to reconstruct the high-dimensional neural activity representations that are attenuated during propagation through the brain due to volume conduction and tissue filtering, thereby generating enhanced EEG signals whose fidelity approaches that of iEEG. As illustrated in Figure 1b, the pipeline comprises four coordinated stages: (i) extracting robust generic neural representations from raw EEG using a pretrained foundation model; (ii) computing constraint features over cortical regions based on neural dynamics equations; (iii) modeling the intrinsic geometric properties of the cortical surface via geometric mode decomposition; and (iv) progressively reconstructing high-fidelity enhanced EEG signals under the guidance of these three complementary feature streams, using a multi-dimensional EEG feature encoder coupled with a diffusion-based generative mechanism.

Critically, the output of this framework is neurophysiologically unified: when evaluated for iEEG reconstruction and signal fidelity, it is termed “synthesized iEEG”; when deployed in downstream BCI tasks, it is referred to as

“enhanced EEG.”These two designations share an identical generative mechanism and representational basis, with the naming distinction reflecting only the objective of the downstream application, not any divergence in the signal’s intrinsic properties.

To overcome the fundamental limitations of EEG—particularly its substantially lower signal fidelity compared to iEEG, while avoiding the

[Figure 71]

Stage 3

[Figure 72]

Personalized Representation Enhancement

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

Personalized

Sub-N Personalized fine-tuning

[Figure 79]

[Figure 80]

[Figure 81]

representation module

[Figure 82]

Zero-shot learning

[Figure 83]

Personalized calibration data

[Figure 84]

[Figure 85]

Stage 2

Scenario-Oriented Fine-Tuned Adaptation

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

Scenario-specific adaptation module

Scenario-specific fine-tuning

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

Scene related datasets

[Figure 99]

[Figure 100]

[Figure 101]

Stage 1

“Data + Knowledge” Neural Representation Foundation Model

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

Neural

Pre-training Physical information learning

[Figure 107]

representation

[Figure 108]

[Figure 109]

[Figure 110]

Large-scale EEG/iEEG/MEG dataset

Knowledge of neuroscience

foundation model

- Figure 6 A three-stage paradigm for EEG enhancement. Stage 1 builds a neural representation foundation model from multimodal data and neuroscientific priors to capture universal propagation patterns. Stage 2 adapts this model to specific BCI scenarios such as emotion or motor imagery through fine-tuning. Stage 3 personalizes the output using subject-specific calibration for high-fidelity signals; with limited data zero-shot learning provides partial adaptation.

#### Pretrained EEG Representation Encoding Module

Raw EEG signals are highly susceptible to contamination from non-neural artifacts such as electromyographic and electrooculographic activity. This results in low signal-tonoise ratio and high inter-subject variability, which impedes the reliable extraction of highdimensional neural activity patterns. Even after standard preprocessing, signal fidelity remains substantially limited, making it diﬀicult to support demanding downstream tasks such as high-precision neural decoding. A more fundamental challenge arises from the scarcity of simultaneously recorded EEG–iEEG paired data in clinical and research settings. Publicly available datasets typically involve only a small number of subjects, a narrow range of experimental paradigms, and short recording durations. Under such limited and lowquality observational conditions, reconstruction

of high-dimensional, spatiotemporally continuous neural representations is prone to overfitting subject-specific noise or task-related artifacts, significantly compromising generalization to unseen scenarios.

To address these challenges, a Pretrained EEG Representation Encoder (PERE) is constructed. PERE employs LaBraM, a large foundation model pretrained on massive-scale unpaired EEG data, as its initial network layer to extract noise-robust and cross-task generic pretrained neural representations. These representations do not require iEEG supervision yet effectively disentangle neural activity from multi-source confounding factors, thereby establishing a foundational neural representation space for subsequent multi-dimensional feature fusion. Specifically, PERE consists of three components: an EEG spatial dimension adapter, a pretrained generic neural representation extractor, and a neural representation spatial aligner.

###### EEG Spatial Dimension Adapter

Let a preprocessed EEG segment be denoted as Xi ∈ RC×T, where C is the number of channels and T is the number of time points (fixed at 250 in this study). To map these signals into the embedding space of the pre-trained model, we introduce a spatial dimension adapter, a parameter-shared single-layer linear projection applied at each channel–time position:

[Xiemb]c,t,: = Wadapter · Xi(c,t) + badapter.

Here, Xi(c,t) ∈ R denotes a scalar input, and [Xiemb]c,t,: ∈ RD

emb is the corresponding embedding vector. This operation is equivalent to generating C×T tokens on a C×T grid, with each token embedded in a Demb-dimensional feature space. The resulting tensor is given by

###### Xiemb = Adapter(Xi) ∈ RC×T×D

emb

.

###### Pretrained Generic Neural Representation Extractor

emb serves as input to LaBraM. LaBraM is a Transformer architecture pretrained on large-scale unpaired EEG data, containing 5.8 million parameters, with its self-attention mechanism computed over all C × T tokens:

The tensor Xiemb ∈ RC×T×D

QK⊤

V,

Attention(Q,K,V) = softmax

√

d

where d = Demb denotes the feature dimension. The core advantage of this mechanism lies in its ability to adaptively capture nonlinear spatiotemporal interactions prevalent in EEG, such as cross-frequency phase–amplitude coupling and event-related desynchronization/synchronization. These patterns constitute essential carriers of neural information encoding and cannot be effectively modeled by conventional bandpass filtering or handcrafted features.

The activations from the L∗ = 12-th layer of LaBraM are selected as intermediate representations:

###### Eiraw = LaBraML∗(Xiemb) ∈ RC×T×D

emb

###### .

Empirical evaluation shows that this layer achieves an optimal trade-off between preserving fine-grained spectral details and encoding high-level neural semantics. It consistently demonstrates the strongest generalization across datasets and subjects.

###### Neural Representation Spatial Alignment Module

To align the output of LaBraM with the multi-dimensional EEG feature space required by subsequent fusion modules, a linear projection layer is applied to each token:

[Eiproj]c,t,: = Wproj · [Eiraw]c,t,: + bproj.

emb denotes the raw output of LaBraM, and Demb is its embedding dimension. The projected tensor Eiproj ∈ RC×T×D

Here, Eiraw ∈ RC×T×D

fuse is then flattened and linearly compressed into a unified sequence space:

Edata = Reshape(Eiproj) ∈ RL×D,

where L = C · T and D = Dfuse. This yields the final data-driven pretrained EEG representation Edata. The resulting representation not only suppresses non-neural artifacts in EEG signals but also encodes their underlying neural activity patterns. It thus provides a robust, generalizable foundation for integrating neural dynamics and cortical geometric constraints, enabling the reconstruction of high-dimensional dynamic neural information lost during transcranial signal propagation.

#### Neural Dynamics Constraint Computation Module

Although the data-driven representation Edata exhibits strong generalization capability, its generation process does not explicitly adhere to the fundamental physical laws of neuroelectrophysiology. This may cause the enhanced EEG signals to deviate from genuine cortical activity in temporal dynamics or spatial distribution, thereby compromising their neuroscientific plausibility and the reliability of downstream decoding tasks. To ensure interpretability and fidelity at the level of neural mechanisms, a prior model grounded in neural dynamics is introduced to impose physical constraints consistent with established neural signal propagation principles during signal generation. This module comprises three coordinated submodules: (i) head physical modeling, (ii) neural population dynamics representation, and (iii) dynamics-to-embedding mapping.

###### Head Physical Modeling Submodule

Specifically, a three-layer Boundary Element Method (BEM) head model is constructed from individual T1-weighted MRI scans, corresponding respectively to brain tissue, skull, and scalp. Within this model, the relationship between scalp potentials Φk and cortical current sources J is governed by the Poisson equation derived from the quasi-static Maxwell equations:

∇ · (σk∇Φk) = 0 in Ωk,

where Ωk denotes the k-th tissue compartment (k = 1: brain, k = 2: skull, k = 3: scalp), and the conductivity vector is σ = [0.33, 0.01, 0.33]⊤ S/m. This formulation accurately captures the strong attenuation and spatial low-pass filtering effect of the skull on

high-frequency neural activity. Such physicsmediated distortion—arising from the multilayered anatomical structure of the head—is the primary cause of the loss of fine-grained neural patterns in raw EEG.

###### Neural Population Dynamics Representation Submodule

Under this geometric constraint, the lead field matrix L ∈ RC×N is computed as:

L = GB,

where G denotes the Green’s function and B is the mapping operator; N is the number of cortical source points. Given the i-th scalp EEG segment Xi ∈ RC×T, the cortical current source estimate Jˆi ∈ RN×T is obtained by solving the sLORETA-regularized optimization problem:

Jˆi = argmin

J

W−1/2(Xi − LJ) 2F + λ∥J∥2F ,

where W ∈ RC×C is a noise-covariance-based normalization matrix, λ > 0 is the regularization parameter, and ∥·∥F denotes the Frobenius norm. This strategy ensures solution uniqueness while preserving the true spatial distribution of cortical activity, thereby providing a reliable constraint Jˆi.

To further constrain temporal dynamics, Jˆi(x,t) serves as the external input to a Neural Mass Model (NMM) that describes the mean membrane potential evolution of local excitatory (E) and inhibitory (I) neuronal populations:

 

V˙E = fE(VE,VI,Jˆ), V˙I = fI(VE,VI,Jˆ),



where fE and fI are nonlinear dynamical functions simplified from Hodgkin–Huxley theory. This model effectively captures characteristic oscillatory rhythms—such as alpha and beta bands—generated by cortical microcircuits.

Let ∆V (x,t) denote the deviation of the excitatory population’s mean membrane potential from rest at cortical location x ∈ Ω, where Ω is the subject-specific cortical surface manifold. Similarly, y ∈ Ω denotes an integration variable representing other cortical locations. The spatiotemporal evolution of ∆V (x,t) is then governed by the neural field equation:

∂∆V (x,t) ∂t

= −∆V (x,t)+

w dgeo(x,y) S ∆V (y,t) dy + Jˆ(x,t)

Ω

w(·) is a connectivity kernel based on geodesic cortical distance dgeo(x,y), quantifying structural coupling strength between regions; S(·) is a sigmoidal activation function; Jˆ(x,t) is the cortical current source estimated via sLORETA.

This equation explicitly models the diffusion and synchronization of neural activity across the cortical surface, revealing how neural signals evolve in space and time during transcranial propagation.

###### Neural Population Dynamics Representation Mapping Submodule

Finally, to interface the computed spatiotemporal neural activity dynamics with downstream deep generative modules, a lightweight multilayer perceptron (MLP) compresses the high-dimensional dynamical state ∆V (x,t) into a compact prior feature:

Eprior = MLP flatten(∆V ) ∈ RL×D,

where flatten(∆V ) reshapes the cortical field ∆V (x,t) over space x ∈ Ω and time t into a vector of length L, and D denotes the embedding dimension. This mapping preserves essential dynamic neural representations while enabling a compatible transformation from the continuous differential system to a discrete deep learning

representation. Consequently, the derived neural dynamics constraint can be effectively fused into the subsequent diffusion-based enhancement process.

#### Geometric coding of the cerebral cortex

Although the Boundary Element Method (BEM) model effectively captures the volume conduction effect from cortex to scalp, distortions in raw EEG also arise from the spatial organization of cortical neural activity on the subject-specific cortical manifold. Inter-subject variability in sulcal and gyral morphology modulates local neural synchrony and the spatial superposition of field potentials, leading to significant inter-individual differences in scalp EEG even under identical cognitive states. Such anatomy-coupled neural representations are further obscured during transcranial propagation and cannot be directly recovered from observed signals. To address this, a structural modeling pipeline is constructed, comprising three coordinated submodules: (i) cortical surface geometric decomposition, (ii) geometric mode feature computation, and (iii) weighted geometric feature mapping.

###### Cortical Surface Geometric Decomposition Submodule

To recover neural activity patterns tightly coupled with cortical geometry, a geometric mode decomposition framework is adopted. Specifically, a high-resolution cortical triangular mesh M is reconstructed from individual T1-weighted MRI using FreeSurfer, and the Laplace–Beltrami Operator (LBO) is defined on M as:

1 √detg

∂i detg gij∂jf ,

∆Mf =

where g denotes the Riemannian metric tensor induced by the mesh. Solving the eigenvalue problem:

∆Mϕk = −λkϕk, k = 0,1,2,...,

yields an orthogonal set of geometric modes {ϕk} on M, with corresponding eigenvalues λk reflecting spatial frequency (i.e., oscillation scale). These modes form an intrinsic eigenfunction basis of the cortical surface, naturally encoding geometric properties such as gyral scale, curvature variation, and topological connectivity.

###### Geometric Mode Feature Computation Submodule

To capture the multi-scale modulation of neural activity by cortical geometry, the spectral domain is partitioned into three bands: low (λk < λlow), medium (λlow ≤ λk < λhigh), and high (λk ≥ λhigh). The T1-weighted image intensity IT1(r) is then projected onto the geometric eigenbasis:

IT1(r)ϕk(r)dr.

αk = ⟨IT1,ϕk⟩M =

M

This projection is neurobiologically grounded: T1 signal intensity correlates strongly with cortical myelination, neuronal density, and microcolumnar architecture—microstructural features that govern the generation eﬀiciency and spatial coherence of local field potentials. By representing T1 MRI in the geometric eigenbasis, microscopic cytoarchitectonic information is unified with macroscopic cortical morphology within a common spectral framework, yielding a geometric–functional joint representation that is both anatomically precise and physiologically meaningful.

###### Weighted Geometric Feature Mapping Submodule

Finally, a geometric prior feature map is reconstructed via learnable band-wise weights w = [wlow,wmid,whigh]⊤:

Egeo(r) =

k

wb(λk)αk ϕk(r),

where wb(λk) equals wlow, wmid, or whigh depending on the band to which λk belongs. The weight wb reflects the detectability of each spatial frequency component in scalp EEG. This feature map explicitly encodes how individual cortical geometry influences neural signal propagation, thereby providing critical geometric guidance for the enhancement process. As a result, the generated enhanced EEG signals conform not only to neurophysiological dynamics but also to the subject’s true cortical geometry in spatial distribution.

To facilitate fusion with the data-driven representation, Egeo is resampled to match the spatiotemporal grid of Edata and mapped into the shared feature space RL×D via a lightweight projection layer, yielding Estruct. This structural feature serves as a conditional input during EEG enhancement, ensuring that neural activity patterns masked by the transcranial propagation pathway are reconstructed under explicit, individualized brain geometric constraints.

#### EEG Enhancement Signal Generation via Feature Fusion and Diffusion Modeling

###### Multi-Dimensional Data–Knowledge Feature Fusion Module

To synergistically integrate the three complementary representations—data-driven generic neural features Edata, neural dynamics constraint prior Eprior, and cortical geometric structure prior Estruct—a multi-dimensional

data–knowledge feature fusion module is designed. Its objective is to construct a conditional signal that guides the enhancement process to simultaneously satisfy statistical adaptability, neurophysiological plausibility, and anatomical specificity.

The fusion module concatenates the three feature streams Edata, Eprior, and Estruct along the sequence dimension to form a unified input, which is then processed by a shallow Transformer encoder. Cross-modal dependencies are modeled via multi-head self-attention:

Zfused = TransEncoder [Edata;Eprior;Estruct] .

This architecture dynamically weights the contribution of each feature stream in representing neural activity patterns, thereby avoiding semantic conflicts arising from rigid concatenation. The resulting fused representation Zfused preserves the flexibility of data-driven learning while embedding the rigidity of neurodynamical and geometric constraints.

###### High-Fidelity EEG Enhancement via Fusion-Guided Diffusion

The fused representation Zf serves as the global conditioning signal for a conditional diffusion model, which generates an enhanced EEG signal X ∈ RC×T with fidelity approaching that of iEEG. The enhancement process is formulated as a progressive denoising trajectory from pure Gaussian noise XT ∼ N(0,I) to the target signal X0 = X. The reverse Markov chain is defined as:

pθ(Xt−1 | Xt,Zf) = N Xt−1;µθ(Xt,t,Zf),Σθ(t) ,

where µθ is implemented by a U-Net architecture. Skip connections in the U-Net preserve fine-grained temporal details from the original EEG, while the global condition Zfused is injected

at every decoder layer via cross-attention mechanisms, ensuring consistency between the generated signal and the multi-dimensional guidance features across multiple scales.

Notably, during early diffusion steps (large t), the model prioritizes recovery of highfrequency neural patterns masked by the skull’ s low-pass filtering effect. In later steps (small t), it refines phase and amplitude to achieve precise temporal alignment with the observed EEG. This staged, multi-scale control enables the model to learn both global neural event structures and high-dimensional spatiotemporal dynamics aligned with iEEG, thereby producing high-fidelity enhanced EEG signals.

###### Composite Loss Function

The model is trained end-to-end by minimizing the variational Evidence Lower Bound (ELBO):

Ldiff = Et,X

0,ϵ

ϵ − ϵθ √αtX0 + 1 − αt2 ϵ, t, Zfused

2 2

,

where ϵ ∼ N(0,I) denotes standard Gaussian noise and Xt = √αtX0 + 1 − αt2 ϵ is the forward noising process. This objective enforces distributional consistency between the generated signal X and the three guiding feature streams, thereby ensuring generalization across diverse non-invasive BCI scenarios.

To further improve amplitude and waveform fidelity, three auxiliary supervised losses are incorporated into the training objective:

- • A weighted negative Pearson correlation loss

λ1 · − ρ(Xˆ0,X0) to enhance morphological similarity between the generated and target waveforms;

- • A mean squared error term λ2 ·∥Xˆ0 −X0∥22 to enforce precise amplitude reconstruction;
- • An L2 weight regularization term λ3 · ∥θ∥22 to mitigate overfitting.

The total loss is defined as:

Ltotal =

Ldiff+λ1 −ρ(Xˆ0,X0) +λ2∥Xˆ0−X0∥22+λ3∥θ∥22.

In this study, the hyperparameters are set to λ1 = 0.1, λ2 = 0.3, and λ3 = 0.1. This composite objective function jointly optimizes the generation process across four dimensionsdistributional consistency, amplitude accuracy, waveform morphology, and model complexityensuring that the generated enhanced EEG signal X achieves comprehensive fidelity approaching that of iEEG.

#### Downstream Task Evaluation Pipeline for EEG Datasets

To systematically evaluate the performance of enhanced EEG signals across diverse downstream tasks, a Transformer-based autoencoder module is constructed to adapt conventional EEG signals to the proposed enhancement framework, enabling spatial channel compression and subsequent reconstruction.

###### EEG Spatial Channel Compression Module

The encoder takes raw EEG signals X ∈ R64×T, recorded from standard 64-channel systems with temporal length T, as input. It models inter-channel spatial dependencies via multi-head self-attention and outputs a compressed representation Xcomp ∈ RC×T. The encoder is trained to reconstruct the subset of C scalp EEG channels that spatially correspond to the intracranial electrode locations in simultaneously recorded EEG–iEEG datasets. This ensures compatibility between the compressed signal and the input requirements of the proposed enhancement framework.

###### EEG Enhancement via Unified Framework

The compressed representation Xcomp is fed into the unified enhancement framework. Through sequential stages—including data-driven representation extraction, neurodynamical–geometric constraint fusion, and conditional diffusion-based generation—the framework produces a high-fidelity enhanced signal Xenh ∈ RC

′×T. Here, the number of output channels C′ strictly matches the count of valid iEEG channels in the corresponding simultaneous recording, ensuring dimensional alignment with ground-truth iEEG in the channel space.

###### EEG Spatial Resolution Enhancement Module

The enhanced signal Xenh is then passed to a decoder, which also adopts a Transformer architecture. During training, the decoder takes the C′ iEEG-proximal scalp channels as input and reconstructs the full 64-channel scalp EEG as the target. This enables the decoder to learn a mapping that effectively upsamples the enhanced signal back to full-brain spatial coverage, thereby completing end-to-end spatial resolution enhancement.

###### Downstream Task Experimental Protocol

To ensure an objective assessment of the proposed framework, the performance of original EEG signals and generated enhanced EEG signals is compared under strictly controlled experimental conditions. Both signal types undergo identical preprocessing pipelines, temporal windowing strategies, dataset partitioning schemes, and hyperparameter search spaces, guaranteeing a fair evaluation. Downstream decoders employ simple yet well-established baseline architectures, including multilayer perceptrons

(MLPs) and lightweight Transformers. These models possess suﬀicient representational capacity to capture fundamental neural dynamics while avoiding excessive complexity that could obscure the true impact of signal fidelity differences on task performance. Across twelve EEG datasets spanning multiple task types, systematic experiments are conducted using identical decoders for both signal variants. The consistent performance gains observed in the enhanced signals validate the effectiveness of the proposed framework in improving the fidelity of noninvasive EEG and boosting decoding accuracy in downstream BCI applications.

#### Data preprocessing

All neurophysiological and neuroimaging data underwent standardized preprocessing pipelines to ensure methodological rigor and cross-dataset comparability.

For simultaneously recorded EEG and iEEG signals, raw data were bandpass filtered between 0.5 and 150 Hz to remove baseline drift and high-frequency artifacts, followed by a 50 Hz notch filter to suppress line noise. iEEG signals were re-referenced using a bipolar montage to reduce common-mode noise, and channels with signal-to-noise ratio below 3 dB or impedance exceeding 20 kΩ were manually excluded. EEG signals were further processed using independent component analysis (ICA) combined with the automatic artifact rejection algorithm ADJUST to remove ocular, cardiac, and muscular artifacts; only channels with signal-to-noise ratio above 3 dB and impedance below 10 kΩ were retained. Both signal types were re-referenced to the common average, downsampled uniformly to 500 Hz, and segmented into non-overlapping epochs of 250 samples (corresponding to 500 ms). Each channel–epoch unit was independently z-score normalized, yielding standardized

input tensors of dimension RC×250, where C denotes the number of valid channels.

The twelve multi-task EEG datasets were processed using the same filtering pipeline, with additional ocular artifact correction via linear regression and electromyographic interference suppression through wavelet-enhanced ICA. After common average referencing, epochs exhibiting variance exceeding five times the median absolute deviation across the cohort were discarded. All signals were downsampled to 500 Hz, segmented into non-overlapping 250sample windows, and z-score normalized per channel–epoch unit to produce RC×250 tensors.

Structural MRI data were processed using FreeSurfer v7.3.0. T1-weighted images underwent motion correction, skull stripping, and N3 bias field correction, followed by intensity normalization and white matter segmentation. Cortical surface reconstruction employed deformable models expanded to the gray–white and pial boundaries, then smoothed with a 10 mm FWHM Gaussian kernel. All surface meshes were registered to the fsaverage5 standard space, and vertex-wise cortical thickness and curvature features were extracted and bilinearly interpolated onto a 642-vertex spherical grid. Quality control followed ENIGMA consortium guidelines: samples with surface overlap error greater than 0.5 mm or thickness signal-to-noise ratio below 8 dB were excluded. The resulting cortical geometric features were strictly aligned with electrophysiological data in individual anatomical space.

All preprocessing steps were implemented using MNE-Python 1.4 and FreeSurfer 7.3.0, encapsulated in containerized workflows to ensure cross-platform reproducibility. Processed datasets were partitioned into non-overlapping training and testing sets at an 8:2 ratio to prevent data leakage.

### References

- [1] Chaudhary, U., Birbaumer, N. & RamosMurguialday, A. Brain–computer interfaces for communication and rehabilitation. Nature Reviews Neurology 12, 513–525

(2016).

- [2] Schwemmer, M. A. et al. Meeting brain– computer interface user performance expectations using a deep neural network decoding framework. Nature medicine 24, 1669– 1676 (2018).
- [3] d’Ascoli, S. et al. Towards decoding individual words from non-invasive brain recordings. Nature Communications 16, 10521 (2025).
- [4] Lee, J. Y. et al. Brain–computer interface control with artificial intelligence copilots. Nature machine intelligence 7, 1510–1523

(2025).

- [5] Merk, T. et al. Invasive neurophysiology and whole brain connectomics for neural decoding in patients with brain implants. Nature Biomedical Engineering 1–18 (2025).
- [6] Rybář, M., Poli, R. & Daly, I. Simultaneous eeg and fnirs recordings for semantic decoding of imagined animals and tools. Scientific Data 12, 613 (2025).
- [7] Griggs, W. S. et al. Decoding motor plans using a closed-loop ultrasonic brain– machine interface. Nature Neuroscience 27, 196–207 (2024).
- [8] Ding, Y., Udompanyawit, C., Zhang, Y. & He, B. Eeg-based brain-computer interface enables real-time robotic hand control at individual finger level. Nature Communications 16, 1–20 (2025).

- [9] Huang, L., Varlet, M. & Grootswagers, T. Robust neural decoding with low-density eeg. Scientific Reports (2026).
- [10] Daly, I. Neural decoding of music from the eeg. Scientific Reports 13, 624 (2023).
- [11] Stolk, A. et al. Integrated analysis of anatomical and electrophysiological human intracranial data. Nature protocols 13, 1699–1723 (2018).
- [12] Dipalo, M. et al. Plasmonic meta-electrodes allow intracellular recordings at network level on high-density cmos-multi-electrode arrays. Nature nanotechnology 13, 965–971

(2018).

- [13] Parvizi, J. & Kastner, S. Human intracranial eeg: promises and limitations. Nature neuroscience 21, 474 (2018).
- [14] Michel, C. M. et al. Eeg source imaging. Clinical neurophysiology 115, 2195–2222

(2004).

- [15] Kaiboriboon, K., Lüders, H. O., Hamaneh, M., Turnbull, J. & Lhatoo, S. D. Eeg source imaging in epilepsy—practicalities and pitfalls. Nature Reviews Neurology 8, 498–507

(2012).

- [16] Abdi-Sargezeh, B., Valentin, A., Alarcon, G., Martin-Lopez, D. & Sanei, S. Higherorder tensor decomposition based scalp-tointracranial eeg projection for detection of interictal epileptiform discharges. Journal of neural engineering 18, 066039 (2021).
- [17] Abdi-Sargezeh, B., Oswal, A. & Sanei, S. Mapping scalp to intracranial eeg using generative adversarial networks for automatically detecting interictal epileptiform discharges, 710–714 (IEEE, 2023).

- [18] Abdi-Sargezeh, B., Shirani, S., Valentin, A., Alarcon, G. & Sanei, S. Eeg-to-eeg: Scalp-to-intracranial eeg translation using a combination of variational autoencoder and generative adversarial networks. Sensors 25, 494 (2025).
- [19] Cao, M. et al. Virtual intracranial eeg signals reconstructed from meg with potential for epilepsy surgery. Nature communications 13, 994 (2022).
- [20] Santhanam, G., Ryu, S. I., Yu, B. M., Afshar, A. & Shenoy, K. V. A high-performance brain–computer interface. nature 442, 195–198 (2006).
- [21] Wang, G. et al. Human-centred physical neuromorphics with visual brain-computer interfaces. Nature Communications 15, 6393 (2024).
- [22] Pun, T. K. et al. Measuring instability in chronic human intracortical neural recordings towards stable, long-term braincomputer interfaces. Communications Biology 7, 1363 (2024).
- [23] Jiang, L. et al. Gene transcription, neurotransmitter, and neurocognition signatures of brain structural-functional coupling variability. Nature Communications 16, 7623

(2025).

- [24] Zhang, Z. et al. Dynamic structure-function coupling in macroscale neonatal brain networks. Communications Biology (2025).
- [25] Jiang, W.-B., Zhao, L.-M. & Lu, B.-L. Large brain model for learning generic representations with tremendous eeg data in bci. arXiv preprint arXiv:2405.18765

(2024).

- [26] Cui, W. et al. Neuro-gpt: Towards a foundation model for eeg, 1–5 (IEEE, 2024).
- [27] Scheeringa, R. et al. Neuronal dynamics underlying high-and low-frequency eeg oscillations contribute independently to the human bold signal. Neuron 69, 572–583

(2011).

- [28] Kiebel, S. J., David, O. & Friston, K. J. Dynamic causal modelling of evoked responses in eeg/meg with lead field parameterization. NeuroImage 30, 1273–1284

(2006).

- [29] Pang, J. C. et al. Geometric constraints on human brain function. Nature 618, 566–574

(2023).

- [30] Yu, S., Ma, J. & Osher, S. Geometric mode decomposition. Inverse Problems & Imaging 12 (2018).
- [31] Youngworth, R. N., Gallagher, B. B. & Stamper, B. L. An overview of power spectral density (psd) calculations. Optical manufacturing and testing VI 5869, 206–216 (2005).
- [32] Benesty, J., Chen, J., Huang, Y. & Cohen,

I. in Pearson correlation coeﬀicient 1–4 (Springer, 2009).

- [33] Xia, P., Zhang, L. & Li, F. Learning similarity with cosine similarity ensemble. Information sciences 307, 39–52 (2015).
- [34] Thatcher, R. W., North, D. & Biver, C. Eeg and intelligence: relations between eeg coherence, eeg phase delay and power. Clinical neurophysiology 116, 2129–2141

(2005).

- [35] Schindler, K., Leung, H., Elger, C. E. & Lehnertz, K. Assessing seizure dynamics by

- analysing the correlation structure of multichannel intracranial eeg. Brain 130, 65–77 (2007).
- [36] Maaten, L. v. d. & Hinton, G. Visualizing data using t-sne. Journal of machine learning research 9, 2579–2605 (2008).
- [37] Lundberg, S. M. & Lee, S.-I. A unified approach to interpreting model predictions. Advances in neural information processing systems 30 (2017).
- [38] Kragel, P. A. & LaBar, K. S. Decoding the nature of emotion in the brain. Trends in cognitive sciences 20, 444–455 (2016).
- [39] Lindquist, K. A., Wager, T. D., Kober, H., Bliss-Moreau, E. & Barrett, L. F. The brain basis of emotion: a meta-analytic review. Behavioral and brain sciences 35, 121–143

(2012).

- [40] Dalgleish, T. The emotional brain. Nature Reviews Neuroscience 5, 583–589 (2004).
- [41] Olson, I. R., Plotzker, A. & Ezzyat, Y. The enigmatic temporal pole: a review of findings on social and emotional processing. Brain 130, 1718–1731 (2007).
- [42] Delorme, A. Eeg is better left alone. Scientific reports 13, 2372 (2023).
- [43] Zhang, Y. & Chen, Z. S. Harnessing electroencephalography connectomes for cognitive and clinical neuroscience. Nature Biomedical Engineering 9, 1186– 1201 (2025).
- [44] Olejarczyk, E., Gotman, J. & Frauscher, B. Region-specific complexity of the intracranial eeg in the sleeping human brain. Scientific reports 12, 451 (2022).

### Supplement

To quantify the contribution of distinct neural oscillatory bands to EEG signal enhancement, this experimental set systematically evaluates the spectral-specific performance of the five standard frequency bands—delta, theta, alpha, beta, and gamma—within the proposed framework, encompassing both reconstruction fidelity and latent representational structure. On two simultaneously recorded EEG–iEEG datasets (Dataset1 and Dataset2 of data availability), raw EEG signals were processed through standard bandpass filters to isolate individual sub-band components. Under identical experimental conditions, each sub-band signal was fed into the proposed framework to generate synthesized iEEG, which was then quantitatively compared against ground-truth iEEG using multiple evaluation metrics. The results are presented in extended data Fig. 1.

Reconstruction performance exhibits a monotonic increase with rising frequency. The delta and theta bands achieve the lowest scores across all metrics, with a mean PCC of 0.17 and PSD Sim of 0.18, reflecting the limited capacity of low-frequency components to recover highfidelity neural dynamics. In contrast, the gamma band yields the best performance, achieving a mean PCC of 0.47 and PSD Sim of 0.49, approaching the performance of full-band input. These findings indicate that high-frequency components carry richer reconstructible information within the current framework. Furthermore, the multi-scale feature encoding mechanism effectively compensates for the attenuation of high-dimensional neural activity representations during propagation through the brain.

Figure further evaluates the enhancement eﬀicacy at the level of spectral structure. Heatmap visualizations depict the information distribution of enhanced signals and real

- a.
- b. c.

###### delta band

###### aplha band

- 0.0
- 0.1
- 0.2
- 0.3
- 0.4 sigma band

0.4

0.6

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

0.3

0.4

0.2

0.2

0.1

0.0

0.0

PCC Cos PSD Freq

PCC Cos PSD Freq

PCC Cos PSD Freq

gamma band

0.8 beta band

###### 0.8 full band

0.8

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

0.6

0.6

0.6

0.4

0.4

0.4

0.2

0.2

0.2

0.0

0.0

PCC Cos PSD Freq

PCC Cos PSD Freq

PCC Cos PSD Freq

Synthesized iEEG Real iEEG

[Figure 111]

[Figure 112]

[Figure 113]

delta

[Figure 114]

[Figure 115]

sigma

[Figure 116]

[Figure 117]

alpha

[Figure 118]

[Figure 119]

beta

[Figure 120]

[Figure 121]

gamma

- Extended Data Fig. 1 Spectral specificity of EEG enhancement across neural oscillation bands. a, Reconstruction fidelity increases with frequency; gamma achieves highest performance with PCC 0.47 and PSD Sim 0.49 while delta and theta are lowest with PCC 0.17 and PSD Sim 0.18. b, Beta and gamma enhanced signals replicate focal iEEG-like patterns whereas delta and theta remain diffuse lacking structural specificity. c, t-SNE shows distinct band-specific clusters with adjacent bands spatially proximate; full-band embeds near beta and gamma and sigma from 13 to 15 hertz lies at the alpha–beta boundary consistent with its transitional role.

iEEG across frequency bands, where red indicates regions of high information concentration and blue indicates regions of low concentration. The results show that in the beta and gamma bands, enhanced signals exhibit localized, highintensity information clustering patterns that closely resemble those of real iEEG, demonstrating strong spatial correspondence. In contrast, in the delta and theta bands, enhanced signals display diffuse energy distributions with poorly defined boundaries, lacking the structural characteristics observed in real iEEG. This observation aligns with the quantitative trends and confirms that the proposed framework effectively reconstructs the frequency-domain organizational signatures intrinsic to iEEG in highfrequency bands, thereby preserving the spatial specificity required for physiological plausibility.

Figure 7c visualizes the latent representations of the six frequency-band signals using t-SNE dimensionality reduction, revealing their intrinsic structures in the embedding space. Feature points from distinct frequency bands form relatively independent clusters, indicating that the framework successfully preserves the spectral identity of each band during encoding. Adjacent bands—such as delta and theta, alpha and beta, and gamma and full-band—exhibit spatial proximity and partial overlap, reflecting the neurodynamical continuity and functional associations across the frequency spectrum. The representation of the full-band signal resides between multiple single-band clusters and shows substantial overlap with the gamma and beta clusters, consistent with its nature as a broadband composite signal. Additionally, the sigma component (13–15 Hz) localizes at the boundary between the alpha and beta clusters, aligning with its established physiological role as a transitional rhythm in sensorimotor processing.

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

SEED

Negative

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

Positive

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

Neutral

###### w/o PERE w/o GC w/o NC Full

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

###### SEED-V

Negative

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

Positive

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

Neutral

w/o PERE w/o GC w/o NC Full

- Extended Data Fig. 2 Topographic maps of EEG signal enhancement across model variants, illustrating the spatial specificity of neural activation patterns.Top rows show results on the SEED dataset; bottom rows show results on SEEDV. Columns correspond to three ablation settings: without the Pretrained EEG Representation Encoder (PERE), without the Neural Dynamics Constraint (NC), without the Geometric Constraint (GC), and the full model. Warm colors from red to orange indicate regions of high activation, while cool colors from blue to cyan denote low or baseline-level activity. As model components are incrementally integrated from ablated variants to the full framework, activation patterns become increasingly focal and anatomically coherent, converging on emotion-relevant cortical regions such as the prefrontal cortex, anterior cingulate, and temporal poles, while non-specific activations in sensorimotor and occipital areas are markedly suppressed. These findings demonstrate that the proposed framework enhances both the neurophysiological fidelity and functional specificity of reconstructed EEG signals.

###### Reconstruction results on paired EEG-iEEG data with T1 MRI standard template

0.5

0.4

###### PCC

0.3

0.2

0.1

Sub-01

Sub-02

Sub-03

Sub-04

Sub-05

Sub-06

Sub-07

Sub-08

Sub-09

Sub-10

Sub-11

Sub-12

Sub-13

Sub-14

Sub-15

###### Reconstruction results on paired EEG-iEEG data with T1 MRI standard template

0.8

0.6

###### CosSim

0.4

0.2

Sub-01

Sub-02

Sub-03

Sub-04

Sub-05

Sub-06

Sub-07

Sub-08

Sub-09

Sub-10

Sub-11

Sub-12

Sub-13

Sub-14

Sub-15

###### Reconstruction results on paired EEG-iEEG data with T1 MRI standard template

0.6

0.5

###### FreqSim

0.4

0.3

0.2

Sub-01

Sub-02

Sub-03

Sub-04

Sub-05

Sub-06

Sub-07

Sub-08

Sub-09

Sub-10

Sub-11

Sub-12

Sub-13

Sub-14

Sub-15

###### Reconstruction results on paired EEG-iEEG data with T1 MRI standard template

0.6

0.5

PSDSim

0.4

0.3

0.2

Sub-01

Sub-02

Sub-03

Sub-04

Sub-05

Sub-06

Sub-07

Sub-08

Sub-09

Sub-10

Sub-11

Sub-12

Sub-13

Sub-14

Sub-15

- Extended Data Fig. 3 Reconstruction performance of iEEG signals on a T1 MRI–free EEG–iEEG dataset (OpenNeuro ds004752), demonstrating the generalizability and robustness of the proposed framework. In the absence of subject-specific T1 MRI, the framework employs a standardized T1 MRI template as the anatomical prior to condition the iEEG reconstruction. Results are presented for 15 participants from dataset ds004752 (OpenNeuro, https://openneuro.org/datasets/ds004752/versions/1.0.1). Quantitative evaluation is conducted using four complementary metrics: Pearson correlation coeﬀicient (PCC), cosine similarity (Cos Sim), power spectral density similarity (PSD Sim), and frequency-domain similarity (Freq Sim). The consistent high performance across these metrics confirms that the framework maintains eﬀicacy and functional fidelity even when subject-specific structural imaging is unavailable, thereby validating its applicability in real-world clinical and research settings where high-resolution MRI may be inaccessible.

[Figure 156]

[Figure 157]

γ：9%

Sub-15

Original EEG

Increaseby7%Increaseby6%Increaseby5%Increaseby3%

0 50 100 150 200 250

[Figure 158]

Enhanced EEG

γ：16%

0 50 100 150 200 250

[Figure 159]

[Figure 160]

Sub-07

Original EEG

0 50 100 150 200 250

[Figure 161]

Enhanced EEG

- γ：14%

γ：9%

- γ：15%

0 50 100 150 200 250

[Figure 162]

[Figure 163]

γ：8%

Sub-04

Original EEG

0 50 100 150 200 250

[Figure 164]

Enhanced EEG

γ：13%

0 50 100 150 200 250

[Figure 165]

[Figure 166]

Sub-12

γ：11%

Original EEG

0 50 100 150 200 250

[Figure 167]

Enhanced EEG

0 50 100 150 200 250

- Extended Data Fig. 4 Comparative analysis of frequency distributions for original and enhanced EEG signals across representative subjects. The spectrograms demonstrate that the enhanced EEG signals exhibit a marked increase in the proportion of high-frequency bands (yellow-green hues) and a corresponding decrease in low-frequency bands (blue-purple hues) compared to the original signals. This spectral shift indicates a significant improvement in the proportion of highfrequency components, suggesting that the enhancement framework successfully and effectively recovers high-frequency information typically lost during the propagation of neural signals through brain tissue. Quantitative evaluation of the enhancement effects across different subjects reveals a widespread distribution of eﬀicacy, with the proportion of increase in the γ band following the order: Sub-15 (7%) > Sub-07 (6%) > Sub-04 (5%) > Sub-12 (3%). This hierarchical trend highlights the robustness of the method in recovering high-frequency neural dynamics across varying individual baselines.

###### modal features of different groups on sub-12

[Figure 168]

[Figure 169]

R²=0.93

R²=0.88

R²=0.82

R²=0.75

R²=0.64

R²=0.51

R²=0.31

[Figure 170]

R²=0.91

R²=0.87

R²=0.79

R²=0.71

R²=0.55

R²=0.43

R²=0.22

[Figure 171]

- Extended Data Fig. 5 Scatter points represent geometric modal feature samples for mode groups (mode-2 to mode100), color-coded with a purple→blue→green→yellow gradient reflecting the progressive diffusion stage of geometric feature decomposition. The dotted black line represents the principal regression trajectory of the Laplace–Beltrami Operator, serving as a reference axis for quantifying geometric structure deviation, with R² values measuring the goodness-of-fit between each mode group and this regression line. Results show: mode-2 to mode-10 (purple-blue) exhibit highly compact clustering along the diagonal band with strong geometric constraint but limited discriminability; mode-60 to mode-100 (green-yellow) show excessive diffusion beyond the band structure, obscuring geometric-topological relationships; mode20 to mode-50 (blue-green) maintain band-aligned structure with suﬀicient inter-sample discriminability while remaining tightly constrained around the regression line, preserving intrinsic cortical manifold geometry. These findings indicate that mode-20 to mode-50 achieve optimal balance between geometric constraint and feature expressiveness, representing the most suitable geometric feature decomposition modes for EEG enhancement tasks.

###### modal features of different groups on sub-15

[Figure 172]

[Figure 173]

R²=0.91

R²=0.89

R²=0.83

R²=0.76

R²=0.66

R²=0.50

R²=0.29

[Figure 174]

R²=0.90

R²=0.86

R²=0.81

R²=0.72

R²=0.57

R²=0.44

R²=0.24

[Figure 175]

- Extended Data Fig. 6 Scatter points represent geometric modal feature samples for mode groups (mode-2 to mode100), color-coded with a purple→blue→green→yellow gradient reflecting the progressive diffusion stage of geometric feature decomposition. The dotted black line represents the principal regression trajectory of the Laplace–Beltrami Operator, serving as a reference axis for quantifying geometric structure deviation. Results show: mode-2 to mode-10 (purple-blue) exhibit highly compact clustering along the diagonal band with strong geometric constraint but limited discriminability; mode-60 to mode-100 (green-yellow) show excessive diffusion beyond the band structure, obscuring geometric-topological relationships; mode-20 to mode-50 (blue-green) maintain band-aligned structure with suﬀicient inter-sample discriminability while remaining tightly constrained around the regression line, preserving intrinsic cortical manifold geometry. These findings indicate that mode-20 to mode-50 achieve optimal balance between geometric constraint and feature expressiveness, representing the most suitable geometric feature decomposition modes for EEG enhancement tasks.

