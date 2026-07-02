# Multimodal Brain-Computer Interfaces: AI-powered Decoding Methodologies

Siyang Li, Hongbin Wang, Xiaoqing Chen, and Dongrui Wu, Fellow, IEEE

arXiv:2502.02830v1[cs.HC]5Feb2025

Abstract—Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices. This review highlights the core decoding algorithms that enable multimodal BCIs, including a dissection of the elements, a uniﬁed view of diversiﬁed approaches, and a comprehensive analysis of the present state of the ﬁeld. We emphasize algorithmic advancements in cross-modality mapping, sequential modeling, besides classic multi-modality fusion, illustrating how these novel AI approaches enhance decoding of brain data. The current literature of BCI applications on visual, speech, and affective decoding are comprehensively explored. Looking forward, we draw attention on the impact of emerging architectures like multimodal Transformers, and discuss challenges such as brain data heterogeneity and common errors. This review also serves as a bridge in this interdisciplinary ﬁeld for experts with neuroscience background and experts that study AI, aiming to provide a comprehensive understanding for AI-powered multimodal BCIs.

Index Terms—AI, Brain-computer interface, brain signal decoding, multimodal learning

I. INTRODUCTION

Perception is the process by which sensory information is interpreted to comprehend the surrounding environment [1]. A modality, therefore, not only refers to how something occurs but also to the way it is experienced or perceived [2]. Perception involves the transmission of signals through the nervous system, which are triggered by physical or chemical stimulation of the sensory system. For instance, visual signals from the retina allow us to see a puppy scampering across the lawn; auditory nerves process sound waves to let us hear a baby’s cry; and olfactory receptors detect odor molecules, enabling us to smell the aroma of roasted chicken. Understanding the brain, therefore, is as crucial as understanding these individual modalities, as it serves as the foundation for our interaction with the environment.

The brain’s ability to interpret and integrate sensory information not only shapes our immediate experiences but also inﬂuences our memories, decisions, and emotions. By decoding the brain, we can build brain-computer interface (BCI) technologies that offer unprecedented opportunities to

This research was supported by the Open Foundation of Henan Key Laboratory of Brain Science and Brain-Computer Interface Technology under grant HNBBL230204.

S. Li, H. Wang, X. Chen, and D. Wu are with the Ministry of Education Key Laboratory of Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China. S. Li is also with the Henan Key Laboratory of Brain Science and Brain Computer Interface Technology, School of Electrical and Information Engineering, Zhengzhou University.

Corresponding Authors: Dongrui Wu (drwu09@gmail.com).

bridge the gap between human cognitive functions and machines, potentially revolutionizing how we interact with and manipulate our environment.

This review emphasizes the signiﬁcance of decoding approaches in multimodal BCIs, speciﬁcally focusing on the algorithmic perspective enabled by the rapid advancements in artiﬁcial intelligence (AI). The seminal work by Gu¨rko¨k and Nijholt [3] established foundational principles for multimodal BCIs. With over a decade of advancement in AI, however, an updated analysis of current methodologies and applications is necessary.

Recent breakthroughs in AI decoding algorithms make BCIs highly effective tools for interpreting human cognitive states and intentions. The applications of these technologies span a broad spectrum, including, but not limited to, visual, speech, and affective decoding. By leveraging AI’s unique capabilities, these systems can create intuitive interfaces that improve the quality and accessibility of human-machine interactions. Their societal impact is particularly profound in areas such as healthcare and rehabilitation, offering new possibilities for enhancing human capabilities.

To emphasize, the classic deﬁnition of multimodality has primarily focused on multiple types of inputs, with fusion tasks being the central problem addressed. This review, however, extends the scope to include additional perspectives beyond multimodal fusion. Speciﬁcally, we cover instance-wise crossmodality mapping and sequential cross-modality translation tasks. The goal is to provide a deeper and more comprehensive understanding of the interaction between modalities, with a particular focus on decoding algorithms in the context of multimodal BCIs.

The rest of this paper is organized as follows: Section II reviews related work and the background of BCIs. Section II details the components of BCIs, categorizes multimodal tasks, and describes the types of brain data. Section IV presents representative multimodal BCI applications, corresponding public datasets, and their core decoding algorithms. Section V discusses future research prospects and common pitfalls. Finally, Section VI concludes the review. An outline of the paper is shown in Fig. 1.

II. ELEMENTS OF MULTIMODAL BCIS A. Components of BCIs

Multimodal BCIs include four primary components: input elicitation, brain data acquisition, neuromechanism interpretation, and output interaction. Each component plays a critical role in evoking, capturing, and translating neural activity into

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

- Fig. 1. The outline of this review.

functional outputs, bridging human cognition and external devices.

Input Elicitation Stimuli are used to elicit speciﬁc neural responses from the user. These stimuli can be visual, auditory, or sensory, designed to provoke brain activity that the BCI system can detect and interpret. Stimulus design must prioritize speciﬁcity to reduce user confusion, ensure user comfort and safety by avoiding sensory overload or fatigue, and adapt to individual differences in sensory perception and cognitive processing.

Brain Data Acquisition (also known as brain signal acquisition or brain imaging) At the core of any BCI system is its capacity to accurately capture brain activity. This involves measuring electrical activity, magnetic ﬁelds, or blood ﬂow changes associated with neural activity using specialized devices. The choice of acquisition method directly impacts the resolution, precision, and potential applications of the BCI, ranging from basic communication aids to complex prosthetic control systems.

Neuromechanism Interpretation Decoding neural activity is essential for effective BCI functionality. This step involves interpreting the brain’s responses to stimuli and understanding

the neuromechanisms behind them, considering various factors in the processing techniques. Decoding algorithms are further inﬂuenced by speciﬁc neuro mechanistic characteristics, such as the latency of task-related responses, the temporal window of interest, and the frequency bands retained for analysis. The effectiveness thus highly depends on the precision of algorithms that decode neural recordings.

Output Interaction The ﬁnal component involves translating interpreted brain signals into actionable outputs. While passive BCIs may not include this step, active BCIs utilize it to enable functions such as synthesizing speech, executing physical commands, or interacting with virtual environments.

These components form the foundation of BCI systems. In the following sections, we explore how AI-powered decoding distinguishes multimodal BCIs from classical designs, enabling sophisticated integration across multiple modalities.

B. Categorization of Multimodal BCIs

Multimodal learning has become a prominent research area in AI [2]. With the development of advanced methodologies such as contrastive learning, generative modeling, sequential modeling, multimodal Transformers, etc., the categorization of

multimodal BCIs has evolved beyond classic feature/decisionlevel fusion tasks. This subsection offers a brief peak of the core mechanisms of multimodal interactions, grounded in the classical categorization of BCIs.

There are various categorizations for BCIs. Based on where the input signal is collected, BCIs can be categorized into non-invasive/invasive/partially invasive [4]. As illustrated in Fig. 2, we propose a novel algorithmic categorization that distinguishes BCIs into three types. This categorization integrates the classic reactive/active/passive BCI categorization [3], [5]:

- • Reactive BCIs use unintended changes in cognition by voluntarily focussing on outside stimuli. It is composed of input elicitation, brain signal acquisition, and neuromechanism interpretation.
- • Active BCIs utilize brain activity that directly correlates with intended actions. It is composed of brain signal acquisition, neuromechanism interpretation, and output interaction.
- • Passive BCIs monitor in the background to detect states based on natural or spontaneous brain activities. It is composed of input elicitation, signal acquisition and neuromechanism interpretation.

The algorithmic categorization of multimodal BCIs is detailed below:

Instance-wise Cross-Modality Mapping This task focuses on mapping an entity from one modality to a corresponding entity in another. For example, reactive BCIs decode brain activity to reconstruct input stimuli, such as visual experiences.

Algorithmically, the mapping function fmapping(·) transforms a sample from modality xA into an entity in modality xB:

xB = fmapping(xA). (1)

Sequential Cross-Modality Translation Sequential communication requires the continuous translation of input modality sequences into target modality sequences while preserving context, coherence, and integrity. Active BCIs are particularly suited for tasks like speech decoding, enabling ﬂuent communication.

Algorithmically, the translation function ftranslation(·) con-

verts sequential inputs from one modality (xA1 ,xA2 ,...,xAT ) into another modality:

(xB1 ,xB2 ,...,xBT ) = ftranslation (xA1 ,xA2 ,...,xAT ) . (2)

Multi-Modality Fusion This classic topic involves combining information from multiple modalities to achieve an integrated decoding result. Passive BCIs utilize this approach by fusing multiple modalities, such as EEG and video data, to improve decoding accuracy.

Algorithmically, the fusion function ffusion(·,·) integrates samples from two or more modalities, xA and xB, into a single output label y:

y = ffusion(xA,xB), (3)

It is also viable to build a sequential fusion function that further considers temporal information:

yt = fseqfusion (xA1 ,xA2 ,...,xAT );(xB1 ,xB2 ,...,xBT ) , (4)

Remark Observe that the technical problems involved in the tasks for the three types of multimodal BCIs are very distinct. Each task presents unique challenges and opportunities, demanding tailored AI algorithms. Addressing these distinctions has catalyzed the development of novel applications in BCIs.

C. Types of Brain Data

Brain data collection is integral to the functionality and applications of BCIs. While various BCI-related surveys provide detailed descriptions, this subsection offers a concise overview of the most widely used brain data collection methods and their characteristics, summarized in Table I. These methodologies can be broadly categorized into invasive and non-invasive techniques, each with distinct advantages and limitations that inﬂuence their suitability for speciﬁc BCI applications.

Invasive BCIs Invasive techniques require surgical implantation of electrodes directly into the brain, offering highresolution signals essential for precise monitoring and intervention. These methods are predominantly used in clinical and research settings for applications such as disease localization and advanced neural interfacing.

- • Electrocorticography (ECoG) Electrodes are placed directly on the exposed brain surface, providing broad area coverage without deep penetration [6]. ECoG is used for motor cortex mapping and tasks requiring precise, localized monitoring of brain activity.
- • Stereoelectroencephalography (SEEG) Electrodes are implanted into the brain through small burr holes, enabling the recording of electrical activity from deep brain structures [7]. SEEG is widely used for epilepsy diagnosis and pre-surgical planning.
- • Microelectrode Arrays (MEA) Arrays of silicon-based electrodes penetrate brain tissue, capturing single-neuron activity with exceptional spatial and temporal resolution. MEAs are instrumental in detailed neural mapping. For example, the Utah array, the ﬁrst invasive neural interface approved by the U.S. FDA, has evolved to record from over a thousand electrodes in a compact area [8].
- • Flexible Electrodes Fabricated using soft polymers or advanced techniques [9]–[16], these electrodes conform to the brain’s surface or penetrate tissue with minimal damage. They offer high biocompatibility, scalability, and long-term stability, reducing chronic immune responses [17].

They are also loosely referred to as intracranial electroencephalography [18].

Non-invasive BCIs Non-invasive techniques [19] are safer and more accessible, eliminating the need for surgical procedures. They rely on external sensors or imaging devices, making them suitable for a broader range of users, including consumer and clinical applications.

• Electroencephalography (EEG) EEG [20], [21] is one of the most popular non-invasive methods due to its affordability and ease of use. It measures electrical activity through scalp electrodes, supporting applications from medical diagnostics to user interface control. Dry electrodes offer quick setups but may be noisier, while

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

- Fig. 2. Three types of multimodal BCIs and their representative applications. Reactive BCIs involve brain activities stimulated by designed inputs, such as visual decoding, where perceived images are decoded instance-wise. Active BCIs facilitate user-driven communication in sequential forms, such as speech decoding. Passive BCIs record brain activities using various sensors for tasks like affective BCIs. The core mechanisms involved are very distinct in the aspect of AI decoding algorithms for such three types.

TABLE I SUMMARY OF BRAIN DATA COLLECTION DEVICES AND THEIR DATA CHARACTERISTICS.

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

Category Name Spatial Resolution Temporal Resolution Cost Universality Inplant Duration / Time for Setup

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

ECoG High High Expensive Low Short-term SEEG High High Expensive Low Short-term MEA Very High Very High Very Expensive Low Medium-term

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

Invasive

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

Flexible Electrodes High / Very High High / Very High Very Expensive Low Long-term

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

EEG Low High Cheap High Quick (Dry) / Moderate (Wet) Setup MEG Moderate High Very Expensive Low Moderate Setup fMRI High Low Very Expensive Moderate Moderate Setup fNIRS Moderate Moderate Moderate Moderate Quick Setup

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

Non-Invasive

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

wet electrodes provide better signal quality at the expense of longer preparation times. However, EEG signals are limited to low-frequency bands due to attenuation by the skull and scalp [22].

- • Magnetoencephalography (MEG) MEG [23] records magnetic ﬁelds generated by neural activity, offering a balance of high temporal and moderate spatial resolution. It is predominantly used in research for time-sensitive brain activity analysis.
- • Functional Magnetic Resonance Imaging (fMRI) fMRI [24], [25] detects blood ﬂow changes associated with brain activity, offering excellent spatial resolution. It is invaluable for mapping neural activity across the entire brain but has limited temporal resolution and high operational costs.
- • Functional Near-Infrared Spectroscopy (fNIRS) Using light to measure blood oxygenation, fNIRS [26] provides moderate spatial and temporal resolution. It is portable, less affected by electrical interference, and suitable for practical and research applications.

The choice between invasive and non-invasive methods depends on the application’s requirements, including resolution,

invasiveness, and cost. Invasive methods are preferred for highprecision clinical or research tasks, while non-invasive approaches dominate consumer and general clinical applications due to their safety and convenience.

III. DECODING ALGORITHMS FOR MULTIMODAL LEARNING

This section introduces key AI techniques fundamental to multimodal BCIs. A. Cross-Modality Contrastive Learning

Cross-modality contrastive learning focuses on classiﬁcation and retrieval tasks by aligning paired samples in the feature space while separating unpaired ones. This approach is particularly effective for instance-wise cross-modality mapping, enabling the alignment of representations from two modalities that share identical semantics1. For example, brain data representations corresponding to viewing a cat can be aligned with

1For readers unfamiliar with such terminologies, it is safe to comprehend “representation” as “feature extracted by trained neural networks” [27], in the form of a vector. The term “semantics” refers to “meaning/class”, e.g., a cat image, text of “cat”, and the brain data of a subject viewing a cat, has identical semantics.

those of a cat image. This is achieved through the learning objective detailed below.

InfoNCE Objective The InfoNCE objective [28], [29] (NCE stands for noise contrastive estimation) takes a symmetrical form. Denote feature extractors for the two modalities

- A and B as fθ(·) and fφ(·), parameterized by trainable neural networks for better feature learning with parameters θ and φ, respectively. Cross-modality contrastive learning aims to optimize their parameters θ and φ with paired inputs

{(xAi ,xBi )}ni=1 from two modalities A and B through the following objective:

LInfoNCEA→B (xA,xB);fθ;fφ = −

1 n

[Figure 113]

n

i=1

log

exp fθ(xAi ) · fφ(xBi )/τ

[Figure 114]

n j=1 exp fθ(xAi ) · fφ(xBj )/τ

, (5)

where exp(·) calculates the exponential (taking the logarithm after summing exponentiated logits computes log probabilities more accurately while ensuring numerical stability), and τ is a temperature hyperparameter that controls the density of the learned representation (a lower value of τ makes the model more sensitive to differences between the more similar and dissimilar pairs [30]), the dot product is a similarity calculation between two samples and can practically also be replaced with other functions like cosine similarity.

For alignment of two modalities, the complete objective combines bidirectional alignment that LInfoNCEA+B = LInfoNCEA→B + LInfoNCEB→A . This objective pulls anchor-positive pairs closer and pushes anchor-negative pairs farther in the feature space. For cross-modality mapping tasks, the anchor fθ(xAi ) corresponds to modality A, with fφ(xBi ) as the positive pair and fφ(xBj ) as the negative pair.

Zero-Shot Classiﬁcation A notable advantage of crossmodality contrastive learning is its capacity for zero-shot classiﬁcation [31], [32], which eliminates the dependence on predeﬁned class labels. As illustrated in Fig. 3, zero-shot classiﬁcation replaces traditional classiﬁcation with a retrieval objective, enabling the system to generalize to unseen classes during testing.

This is achieved by the InfoNCE objective. It produces feature extractors that generate correlated representations, effectively constructing a mapping function that class prediction can be determined with similarity metrics that

xB = fmapping(xA) = arg max

xBi

fθ(xA) · fφ(xBi ) τ

[Figure 115]

. (6)

Extensions and Alternatives Beyond classic contrastive learning, cross-modality alignment can also incorporate label information [33], [34]. Additionally, this framework can be extended to multiple modalities [35], [36] or replaced with direct alignment techniques [37], [38], though these approaches are less common in practice.

- B. Cross-Modality Generative Modeling

Generative modeling has become a cornerstone of contemporary AI systems, particularly in enabling cross-modality

mapping as summarized in this subsection. Variational generative models, such as variational autoencoders (VAEs) [39], generative adversarial networks (GANs) [40], and diffusion models [41], achieve this by learning either a joint latent space or a conditional latent space that correlates two modalities. These latent spaces are typically regularized to align with a prior distribution (commonly Gaussian) to facilitate meaningful sampling, interpolation, and generalization. Figure 4 illustrates these two paradigms.

Joint Latent Space In joint latent space cross-modality mapping, separate encoders fθ(·) and fφ(·) project two modalities into a common space z with reduced dimensionality such that fθ(xA),fφ(xB) ∈ Rd. Separate decoders fθ′(·) and fφ′(·) reconstruct the respective modalities from latent space back to their original forms. The training process typically employs a Gaussian distribution for regularization:

Lshared (xA,xB);fθ;fθ′;fφ;fφ′ = Eq

φ(z|xB) log pφ′(xB|z) − DKL qθ(z|xA) p(z) − DKL qφ(z|xB) p(z) , (7)

θ(z|xA) log pθ′(xA|z) + Eq

where q(z|x) denotes the approximate posterior distributions of encoders, p(x|z) the prior likelihood distributions of decoders, p(z) The prior distribution over the latent space which is often assumed to be a standard Gaussian distribution (i.e., N(0,I)), DKL(q p) the Kullback-Leibler (KL) divergence which measures the extent of distribution gap (how much the approximate posterior q diverges from the prior p) and regularizes the latent distribution in VAEs.

After training, data from one modality can be mapped to another by encoding it into the shared latent space and decoding it with the target modality’s decoder that xB = fφ′ fθ(xA) or xA = fθ′ fφ(xB) .

Conditional Latent Space In conditional latent space mapping, the representation is explicitly conditioned on the source modality. An encoder fθ(·) projects input from one modality to a latent space z, and a decoder fφ′(·) maps the latent representation to the target modality:

Lconditional (xA,xB);fθ,fφ′ = Eq

θ(z|xA) log pφ′(xB|z) − DKL qθ(z|xA) p(z) , (8)

where regularization may involve KL divergence (e.g., in VAEs), progressive diffusion processes (e.g., in diffusion models), or implicit regularization through adversarial training (e.g., in GANs).

Cross-modality mapping in this case follows xB = fφ′ fθ(xA) . Note that such a model is now an asymmetrical, one-way mapping instead.

C. Sequential Modeling

Sequential modeling has become a fundamental paradigm for analyzing chronologically ordered data, including text, speech, and time series. The aforementioned algorithms only considered learning instance-wise functions across modalities, whereas the sequential nature of such data was ignored.

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

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

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

(a) (b)

- Fig. 3. Zero-shot classiﬁcation under cross-modality contrastive learning, using visual decoding as an example. (a) Training stage, where feature extractors for image and brain signal pairings are learned in the latent space using cross-modality contrastive learning. (b) Test stage, where novel classes that were not present in the training set require classiﬁcation. Retrieval could be performed using similarity metrics in the latent space.

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

(a) (b)

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

- Fig. 4. Two types of cross-modality generative modeling, using two modalities of image and brain signal as an example. (a) Joint latent space, where separate encoders project two modalities into a shared latent space, and separate decoders reconstruct the respective inputs; (b) Conditional latent space, where an asymmetrical encoder and decoder projects inputs from a modality to a latent space and then to another modality.

Sequential modeling of brain signal data on the temporal dimension is a more appealing direction compared to instancewise analysis. Three pipelines for decoding brain data into speech are illustrated in Fig. 5.

Speciﬁcally, there are two types of sequential modeling for cross-modality translation. One type focuses on reorganizing the target modality entities to maintain temporal coherence, while the other type considers both the source and target modality entities to improve both temporal coherence and inter-modality alignment.

1) Target-Centric Sequential Modeling: Assuming that a prebuilt cross-modality mapping function fmapping has already predicted the output probabilities for the target modality B, these methods focus on improving ﬂuency, coherence, and sequential consistency of the target modality.

Viterbi Algorithm The Viterbi algorithm ﬁnds the most probable sequence of entities in target modality xB = (xB1 ,xB2 ,...,xBT ) by maximizing the joint probability of

emissions and transitions:

T

xB = argmax

xBt

t=1

P(xBt |xAt ) · P(xBt |xBt−1) , (9)

where P(xBt |xAt ) is the emission probability from predictions by fmapping, and P(xBt |xBt−1) is the transition probability between target entities (predeﬁned or learned).

N-gram The n-gram model predicts the most probable se-

quence of target entities xB = (xB1 ,xB2 ,...,xBT ) by modeling the conditional probability of each target entity given both the

corresponding source entity xAt and the previous n − 1 target entities:

xB = argmax

xBt

T

P(xBt |xAt ,xBt−n+1,...,xBt−1), (10)

t=1

where P(xBt |xAt ,xBt−n+1,...,xBt−1) represents the probability of the current target entity xBt , conditioned on the corresponding source entity xAt and the preceding n − 1 entities in the

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

| |
|---|

| |
|---|

| |
|---|

| |
|---|

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

- Fig. 5. Three pipelines for decoding brain recordings into speech and their respective sequential modeling components. The majority of works decode brain data into sentences, either through direct sequence-to-sequence neural networks, or ﬁrst map to discrete entities of language and then reorganize them. An alternative pipeline directly synthesizes speech waveform, through ﬁrst mapping to mel-spectrogram, then using vocoder for audio generation.

target sequence (n is predeﬁned as for the naming n-gram as a context length).

Sequence-to-sequence neural network models [42] ensure that both temporal coherence and inter-modality alignment are achieved.

Decoder-only Transformers The decoder-only Transformers are also commonly referred to as architectures that are generative pre-trained Transformer (GPT)-like. These models predict the sequence xB = (xB1 ,xB2 ,...,xBT ) by iteratively generating each token xBt based on all previously generated tokens xB1:t−1:

Recurrent Neural Networks (RNNs) RNNs and their variants, including gated recurrent units (GRUs), and long short-term memory networks (LSTMs), are commonly used for sequence-to-sequence modeling. For cross-modality translation, the process involves encoding the source modality sequence into a latent representation and then decoding it into the target modality sequence.

T

xB = argmax

P(xBt |xB1:t−1), (11)

xB

- • Encoder: The encoder processes the source modality

sequence (xA1 ,xA2 ,...,xAT ) to generate a sequence of hidden states (hA1 ,hA2 ,...,hAT ):

hAt = fRNN(xAt ,hAt−1), (12)

where fRNN(·,·) is the recurrent cell function (e.g., slight variations for vanilla RNNs and GRUs/LSTMs).

- • Decoder: The decoder generates the target modality

t=1

where P(xBt |xB1:t−1) represents the probability of the t-th token in the target modality conditioned on its previous tokens, modeled by masked self-attention, which ensures each token in the sequence can only attend to itself and its preceding tokens.

Comparing Viterbi, n-gram, and decoder-only Transformers, the size of the context used for predicting the next token increases progressively (1 for Viterbi, n for n-gram, and Transformers can go very long to thousands of tokens).

sequence (xB1 ,xB2 ,...,xBT ) from the encoder’s hidden states. Note that the ﬁnal hidden state hAT will be treated as a context vector and used to initialize the decoder, i.e., hB0 = hAT . At each time step t, the decoder hidden state hBt is updated as:

Still, these methods have a major drawback in that sequential modeling is only considered for the target modality, which is better addressed by end-to-end sequence-to-sequence neural network models.

hBt = fRNN(xBt−1,hBt−1), (13)

2) Sequence-to-Sequence Cross-Modality Modeling: In this type of modeling, the source and target modalities are jointly considered, and the cross-modality mapping function is integrated with sequential modeling into a uniﬁed framework.

where xBt−1 is the previous target modality prediction (teacher-forced during training).

- A classiﬁer can then follow the target modality’s hidden

states (or the ﬁnal hidden state) for classiﬁcation or regression tasks. The model is trained by minimizing the cross-entropy loss between the predicted and ground truth class labels. When the input and output sequences have different lengths, connectionist temporal classiﬁcation (CTC) loss objective [43] would replace the standard cross-entropy loss to marginalize all possible alignments of the input sequence to the output sequence.

Sequence-to-Sequence Transformers The sequence-tosequence Transformer predicts the most probable target sequence xB = (xB1 ,xB2 ,...,xBT ) given the source sequence xA, as follows:

T

xB = argmax

xB

t=1

P(xBt |xB1:t−1,hA), (14)

where hA represents the contextualized representation of the source sequence modeled by self-attention and cross-attention, P(xBt |xB1:t−1,hA) is the conditional probability of the t-th token in the target sequence, predicted by the decoder.

These approaches merge cross-modality mapping and sequential modeling, ensuring both temporal coherence and inter-modality alignment.

D. Multimodal Transformers

Transformer architectures have emerged as the dominant neural network framework, offering outstanding performance across diverse domains. Their advantages are rooted in three main characteristics:

- • Input Tokenization Transformers are suitable for modeling discrete sequence data of text as a notable advantage over RNNs and their variants, which suffer from vanishing gradient issues, limited memory capacity, and incapability of parallel computation across time steps [44].
- • Attention Mechanism Transformers intrinsically have a more general and ﬂexible modeling space as a notable advantage over CNNs, which are restricted in the aligned grid spaces/matrics [45].
- • Parallel Computing The inherent parallelism of Transformer computation, driven by matrix operations, ensures scalability for large-scale datasets with faster training speeds.

Multimodal Transformers [45] extend the vanilla architecture to process and fuse information from multiple modalities. We summarize the core mechanisms that make them capable and effective for taking inputs from multiple modalities for fusion tasks. Note that such architectures are different from the decoder-only or the sequence-to-sequence variations described in the previous subsection.

Token Fusion Token fusion approaches include token summation and token concatenation, integrating features from different modalities at the input stage. Token summation considers modality-speciﬁc token representations that are summed element-wise, maintaining computational simplicity but limiting modality-speciﬁc distinctions. Token concatenation, on the other hand, combines token embeddings into a longer

sequence, preserving modality-speciﬁc information but increasing computational complexity.

Hierarchical Fusion Hierarchical fusion utilizes attention mechanisms to reﬁne the fusion process by structuring interactions across multiple layers. Multi-stream-to-one-stream hierarchy processes each modality independently before integrating them. It is also viable to adopt a one-stream-tomulti-stream hierarchy that jointly processes inputs and then separates them for ﬁne-tuned representations.

Cross-Attention Fusion Cross-attention extends the vanilla self-attention mechanism by modeling dependencies between tokens from different modalities. Queries from one modality attend to keys and values from another, enabling targeted information exchange. Cross-attention enhances inter-modality interactions while preserving modality-speciﬁc features. It is also viable to concatenate two streams of cross-attention and process them by another Transformer to model the global context.

For clarity and to accommodate the wide variations in practical implementations, Fig. 6 provides visual illustrations of such concepts mimicking that of the survey by Xu et al. [45], with exact mathematical formulations omitted for simplicity.

IV. APPLICATIONS AND DATASETS

This section reviews the current literature on representative multimodal BCI applications of visual, speech, and affective decoding.

A. Visual Decoding

The human visual system has been extensively studied using neurophysiological measurements [46], [47]. Early BCI research focused primarily on decoding visual stimuli using paradigms such as P300 potentials [48] and steady-state visually evoked potentials [49].

This review, however, emphasizes the direct estimation of viewed object categories from recorded brain activity, moving beyond articulately designed visual stimuli. Although this has long been an aspirational objective [50], notable progress has only recently been achieved due to advancements in AI. Recent reviews [51], [52] provide a brief overview and feasibility analysis of this ﬁeld of visual decoding. In contrast, this subsection delivers an analysis from the algorithmic perspective, covering publicly available datasets, core decoding algorithms, and tasks of interest.

The statistics of publicly available visual decoding datasets are summarized in Table II. The datasets reviewed include those containing public brain data (e.g., EEG or fMRI recorded while subjects viewed images). Whether the input elicitation materials (e.g., ImageNet images or video clips) were publicly available was not considered a criterion for dataset inclusion.

Classiﬁcation Objective Early studies approached visual decoding as a classiﬁcation task, training classiﬁers with brain signals as input and image classes as labels.

Haxby et al. [50] extracted voxel activity patterns from fMRI for viewing 8 object classes. They used within-category correlations in comparison to between-category correlations

(a) (b) (c)

- Fig. 6. Variants of multimodal Transformers mechanisms that enable multimodal fusion. (a) Token summation and token concatenation; (b) Multi-streamto-one-stream hierarchy and one-stream-to-multi-stream hierarchy; and (c) Cross-attention and cross-attention to concatenation. Q, K, and V stand for query, key, and value of attention mechanism. Blue and red blocks stand for tokens for two input modalities.

TABLE II STATISTICS OF PUBLIC VISUAL DECODING DATASETS.

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

Download Data Type Data Type Electrodes Length Trials Materials Link

Brain Stimulation

# Sensors / Stimulus # Total # Stimulation

Dataset

# Subjects

# Classes

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

Kaneshiro2015 [53] EEG Image 10 124 0.5s 43,206 72 72 / 6 SDR

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

GOD [54] fMRI Image 5 - - 14,750 1,250 200 FigShare Video-fMRI [55] fMRI Video 3 - 8mins - 972 15 PU

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

Shen2019 [56] fMRI Image 3 - - 21,600 1,250 200 OpenNeuro BOLD5000 [57] fMRI Image 4 - 1s 5,254 4,916 250 / 2000 / 1916 FigShare

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

[Figure 286]

Grootswagers2019 [58] EEG Image 16 63 0.2s 256,000 200 200 / 50 / 10 / 2 OSF

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

NSD [59] fMRI Image 8 - 1s 213,000 10,000 - NSD THINGS-EEG [60] EEG Image 50 64 0.05s 1,312,400 22,248 1,854 / 27 OSF

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

ThingsEEG [61] EEG Image 10 64 0.1s 821,600 16,740 1,854 / 27 OSF THINGS-data-fMRI [62] fMRI Image 3 - 4.5s 26,220 8740 720 OpenNeuro THINGS-data-MEG [62] MEG Image 4 272 1.5±0.2s 89,792 22,448 1,854 / 27 OpenNeuro

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

SEED-DV [63] EEG Video 20 62 5mins - 1,400 40 / 9 SJTU

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

fMRI-Shape [64] fMRI 3D Object 14 - 8s - 1,624 55 HuggingFace fMRI-Objaverse [64] fMRI 3D Object 5 - 6.4s - 3,142 117 HuggingFace

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

for classiﬁcation. Using 10 object classes, Cox and Savoy [65] proposed two feature selection approaches for fMRI, selecting voxels with minimum amount of variations across classes, or identifying voxels by comparing responses to whole objects and scrambled images. Cichy et al. [66] studied both MEG and fMRI responses to 92 object classes. Voxel values from the region of interest were extracted from fMRI as features. For MEG, each time point of the 306-channel MEG was used as feature and analyzed separately. They proposed a binary pairwise classiﬁcation approach, where the classiﬁer only learns to determine from two available options each time, to differentiate between the real stimuli class from one of the remaining classes.

End-to-end neural networks can be used to directly classify raw EEG signals. Bagchi et al. [67] proposed a CNN+Transformer network. They use multi-headed selfattention and temporal convolution to enhance architecture over classic CNN architectures. Similarly, Luo et al. [68] proposed a dual-branch spatio-temporal-spectral Transformer feature fusion network. They utilized channel attention and

graph convolutions for better performance.

Besides explicit classiﬁcation for objects, human perception can also be analyzed for decoding other kinds of mental states. Haynes and Rees [69] studied orientations, using only two object classes as a stimulus of contrast-reversing gratings with orthogonal orientation. With simple voxel values under feature selection and classic classiﬁers, they showed that fMRI-based decoding can obtain a direct measure of orientation-selective processing. Kamitani and Tong [47] studied 8 stimulus orientations with a similar approach.

Retrieval Objective Cross-modality learning transforms classiﬁcation tasks into retrieval objectives, aligning representations across modalities. This would require using representations of the stimulus materials, which can usually be from models pre-trained on large-scale image datasets or image-text datasets such as CLIP (which stands for contrastive languageimage pre-training) [29] model.

Horikawa and Kamitani [54] proposed to use a linear regression function that transformed fMRI patterns into CNN features of the viewed images. The novel image categories can

be estimated by comparing the correlation coefﬁcients between the predicted image features and the category-average visual features of various categories. Chen et al. [70] proposed to cast the mapping problem as an optimal transport problem. They introduced a graph matching framework for the alignment of fMRI and image representations. Song et al. [71] adopted the InfoNCE objective, and further utilized self-attention and graph attention to enhance existing architectures using EEG or MEG. Gong et al. [72] extracted voxel features based on discrete Fourier transform, and further aligns with image representations with InfoNCE objective and diffusion model. Zhou et al. [73] introduced representational similarity analysis for modality alignment. Representations of blood-oxygenlevel dependent of fMRI across subjects were extracted by Transformer model, to align with image representation in the space of pretrained image model [29].

Generative Mapping in a Joint Latent Space Du et al. [74] proposed a deep generative multiview model for joint latent space modeling. The reconstruction of the perceived image was cast as the problem of Bayesian inference of the missing modality. Each modality can also be modeled through different types of models, where neural networks can be used for images, and a sparse Bayesian linear generative model for fMRI [75]. Han et al. [76] utilized a VAE for joint latent space construction. The VAE maps the image to the latent space, whereas a linear regression model maps fMRI responses to the VAE’s latent variables, aligning the two modalities into a uniﬁed representation for decoding and reconstruction. Cheng et al. [77] used a generator in the form of GAN or diffusion model for joint latent space alignment. Beyond natural images, they also studied the stimulus of illusory lines and neon color spreading to understand the subjective experience of visual perception. Qian et al. [78] used ridge regression to constrain the learning space for joint latent space modeling. To learn a better global representation of fMRI, they also used masked autoencoder [79] that is able to reconstruct from only the class token.

Generative Mapping in a Conditional Latent Space Zeng et al. [80] utilized diffusion model for conditional latent space construction. The fMRI signals act as conditioning inputs to the latent diffusion model and directly guide the image generation process in terms of both semantics and spatial structure. The latent diffusion model generates images by explicitly conditioning the denoising process on the extracted fMRI features. Qian et al. [81] proposed to use the diffusion model with CNN+Transformer architecture for conditional latent space modeling. Scotti et al. [82] used InfoNCE objective with mixup data augmentation [83] for image reconstruction with fMRI. The objective was then further softened with knowledge distillation and regularized with diffusion prior. Benchetrit et al. [84] used the InfoNCE objective to align MEG and image representations. They also used the diffusion model to convert the latent representation back to the stimulus image object class. Li et al. [85] also proposed to directly reconstruct viewed image from brain data, using InfoNCE loss and diffusion model, veriﬁed for EEG, MEG, and fMRI, respectively. Chen et al. [86] used an autoencoder with masked signal modeling as a pretext task to learn fMRI representations.

The trained fMRI encoder is then integrated with a latent diffusion model through cross-attention and time-step conditioning for conditional latent space modeling.

Text Caption-aided Visual Decoding Text captions can be generated for the images of stimulus materials, using pretrained vision-language models [87]. Being an alternative option other than images, such texts’ representations can further help establish a better cross-modality mapping function.

The integration of text captions into visual decoding frameworks leverages the powerful capabilities of pre-trained visionlanguage models [87] to enrich the cross-modal mapping process. By incorporating textual descriptions associated with visual stimuli, these approaches provide an additional modality that bridges the gap between brain signals and visual content, enabling more robust and interpretable decoding.

Du et al. [88] proposed a VAE-based model that works in two collaborative parts, i.e., multi-modality joint modeling and mutual information regularization, to learn the relationship between brain activities, visual stimuli, and Wikipedia descriptions of classes. Then, a support vector machine is used to perform the classiﬁcation task with the learned latent representation. Similarly, Liu et al. [89] also adopted the InfoNCE objective for fMRI-to-image or fMRI-to-text retrieval. Xie et al. [90] projected the fMRI data into image and text latent spaces using a diffusion prior, maintaining brainvisual-linguistic consistency. Xia et al. [91] utilized InfoNCE objective with mixup data augmentation to learn fMRI-imagetext shared representations.

Takagi and Nishimoto [92] used linear regression to map brain activity to image and text latent spaces, with early visual cortex signals providing low-level structural details and higher visual cortex signals offering semantic context. The latent diffusion model then reﬁned noisy latent into coherent images, conditioned on both structural and semantic features, enabling conditional latent space generative reconstruction.

Not speciﬁcally aiming for decoding the visual stimulus, Wang et al. [93] investigated the ability of multimodal representations from pre trained vision-language models to predict high-level visual cortex responses in the human brain. They found that the inclusion of text feedback alongside diverse and large-scale datasets allows better comprehension of brain data, which aligns well with neural representations in highlevel brain areas.

Beyond Image Decoding Decoding visual experiences from brain data extends beyond static images to include dynamic stimuli such as videos and 3D objects. This extension broadens the scope of applications, allowing researchers to decode and reconstruct richer visual experiences that align more closely with real-world perception.

Li et al. [94] proposed reconstructing video stimulus from fMRI data, aligning functional and anatomical brain activity into a uniﬁed space. In contrast to traditional fMRI decoding methods that ﬂatten each frame of fMRI into a 1D signal and select subject-speciﬁc activated voxels, their approach transformed fMRI into a uniﬁed representation across subjects into the latent space of the pre-trained vision-language model. The fMRI embedding was utilized as input to the cross-

attention module of the diffusion model for conditional latent space modeling.

Lu et al. [95] also proposed reconstructing video stimulus from fMRI data. Semantic, structural, and motion information features are projected into the latent space using InfoNCE objective, vector quantized VAE, and a Transformer model, respectively. A latent diffusion model then reconstructs video stimulus from such three features from the conditional latent space. Liu et al. [63] proposed to reconstruct dynamic videos from EEG signals. Utilizing the much higher temporal resolution of EEG signals (compared to fMRI), a sequenceto-sequence Transformer model aligned the EEG and video representations. Text captions and their representations were generated for video frames using a pre-trained vision-language model [29], [96], and then aligned with EEG representations. Reconstruction was then reﬁned with a diffusion model to ensure consistency across generated video frames.

Gao et al. [64], [97] proposed to reconstruct 3D objects as stimuli from fMRI. They proposed to align the representations of fMRI and video frames of 3D objects in the latent space of pre-trained vision-language model [29]. The fMRI feature was then used to condition the diffusion model. Finally, a vector quantized decoder converts the latent vector back into 3D mesh representation. Guo et al. [98] considered 3D object reconstruction from EEG of 72 classes to recover both the shape and color of 3D objects. They utilized InfoNCE objective, dynamic-static EEG-fusion encoder, and a colored point cloud decoder.

Application Value Despite the signiﬁcant progress in decoding visual stimuli from brain data, the real-world applications of such technologies remain relatively under-explored. Unlike paradigms like P300 or SSVEP, which are wellestablished for use in spellers or other practical BCIs, visual decoding primarily serves as a tool for understanding neuromechanisms rather than addressing immediate functional needs.

One potential avenue lies in developing assistive technologies for individuals with visual or cognitive impairments. By decoding their internal visual experiences, these systems could facilitate communication or enhance accessibility [99]. Another promising direction is in immersive entertainment and virtual reality, where brain-driven visual decoding could provide personalized and adaptive experiences [100].

However, challenges remain in bridging the gap between research and application. The high computational demands, reliance on specialized equipment, and lack of accuracy limit the widespread adoption of visual decoding technologies. Continued explorations in decoding algorithms and practical applications are crucial to unlocking the full potential of visual decoding-based BCIs.

- B. Speech Decoding

Language is the primary medium through which humans communicate complex ideas, emotions, and intentions. Understanding how the brain encodes and processes language is a central question in neuroscience, with profound implications for BCIs. A prominent application is speech neuroprostheses

[101], which aims to restore communication by decoding neural activity into intelligible speech or text. Unlike other BCI tasks, speech decoding must address the sequential and dynamic nature of linguistic information, where components like phonemes and words unfold over time.

A recent review by Silva et al. [102] provides a comprehensive overview of speech neuroprostheses, primarily on the used features and practices, while this review focuses on the AI algorithms that enable sequential cross-modality translation. Sequential modeling approaches, which are only brieﬂy discussed in Mathis et al. [103], are examined. This review also extends beyond speech neuroprostheses to general linguistic tasks, such as reading and listening. Table III summarizes the statistics of publicly available speech decoding datasets.

Instance-wise Classiﬁcation Preliminary research on speech decoding primarily established the feasibility of mapping brain data to language elements, either by demonstrating correlations [116]–[119] or by employing rudimentary classiﬁcation methods for mapping brain recordings to phonemes and words.

Angrick et al. [120] studied speech onset detection using ECoG from an ALS participant with dysarthria under attempted speech task in English. A binary LSTM model was used for direct binary classiﬁcation. Mugler et al. [121] used ECoG and corresponding time-frequency features with classic classiﬁers for decoding into phonemes under reading task in English. Lee et al. [122] used EEG for decoding into 12-word vocabulary under imaged speech task in English. Common spatial pattern feature and classic classiﬁer was used. Luo et al. [123] decoded ECoG of an ALS patient under reading and miming task in English. CNN was used to classify ECoG into 6 words of directional commands. Wandelt et al. [124] decoded MEA under internal speech and reading task for six-word and two-pseudoword vocabulary in English. Neural ﬁring rates were used as features under classic classiﬁers. Tan et al. [125] proposed a hyperbolic neural network for direct classiﬁcation into phonemes using MEA recorded with 96channel Utah arrays under Mandarin Chinese reading task. They used a hierarchical clustering loss objective to guide the representation learning. Liu et al. [126] used ECoG to classify 8 tonal syllables under Mandarin Chinese reading task. CNNs were used to decode lexical tones and base syllables independently.

Instance-wise Retrieval Recent advances leverage crossmodality contrastive learning and generative modeling to expand the label space and accommodate novel classes in retrieval task. These approaches use instance-wise mapping functions to align neural and linguistic representations.

De´fossez et al. [127] utilized cross-modality contrastive learning using MEG and EEG data under listening task in English or Dutch. Under the InfoNCE objective, neural activity representations were aligned with deep speech representations, obtained from a pre-trained speech model. Duan et al. [128] integrated discrete encoding sequences into open-vocabulary EEG-to-text translation with pre-trained language models under reading task in English. Using both word-level features and raw EEG signals, they applied a combination of the InfoNCE objective and self-reconstruction loss objective to improve

TABLE III STATISTICS OF PUBLIC SPEECH DECODING DATASETS.

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

Brain Data

# Sensors /

Download /

Dataset

# Subjects

Language Duration Task Type Disease

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

Type Electrodes Request Link ZuCo [104] EEG 12 128 English 60h Reading None OSF

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

Broderick2018 [105] EEG 19 128 English 19h Listening None Dryad

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

Brennan-Hale2019 [106] EEG 33 60 English 6.8h Listening None UMich MOUS-MEG [107] MEG 204 275 Dutch - Reading / Listening None RU MOUS-fMRI [107] fMRI 204 - Dutch - Reading / Listening None RU

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

ZuCo 2.0 [108] EEG 18 105 English 42h Reading None OSF Verwoert2022 [109] SEEG 10 54-127 Dutch 33min Reading Epilepsy OSF MEG-MASC [110] MEG 27 208 English 56.2h Listening None OSF

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

Willett2023 [111] MEA 1 128 English 54h Attempted Speech Amyotrophic Lateral Sclerosis Dryad Metzger2023 [112] ECoG 1 253 English 22.4h Attempted Speech Anarthria & Quadriplegia Zenodo

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

Chisco [113] EEG 3 125 Mandarin Chinese 45h Imagined Speech None OpenNeuro ChineseEEG [114] EEG 10 128 Mandarin Chinese 110h Silently Reading None OpenNeuro

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

[Figure 481]

Du-IN [115] SEEG 12 72-158 Mandarin Chinese 36h Reading Epilepsy HuggingFace

[Figure 482]

alignment between EEG and text representations.

Zheng et al. [115] proposed a discrete codex-guided mask modeling framework for instance-wise decoding 61 words from SEEG under reading task in Mandarin Chinese. Using a conditional latent space, the model employs Transformer model under temporal modeling and mask modeling tasks for pre-training. Ma et al. [129] proposed a multi-scale cycleconsistent dual generative adversarial network for EEG/SEEGto-speech translation under listening task in English. For crossmodality mapping in a conditional latent space, their model employed a cycle-consistency loss objective, aligning the temporal and spectral representations of EEG/SEEG signals and speech waveforms.

Target-Centric Sequential Modeling via Classic Language Models As a fundamental element of language, coherence across phonemes and words is the core requirement to form concrete communication. Sequential modeling is thus a must-have for better-performing speech decoding, considering contextual dependencies and allowing the decoded output to align more closely with natural language patterns.

Herff et al. [130] used Viterbi algorithm on language models to improve the coherence of sequences of phonemes, using ECoG data under reading task in English. Their model showed high error rates under increased vocabulary sizes. Sun et al. [131] proposed a character-level decoding approach from ECoG under reading task in English. Their model took ECoG signals as input, using 3D inception layers for multiband spatiotemporal feature extraction, dilated CNNs (a method to extend CNNs for sequential correlations like RNNs) for sequence learning, and a CTC objective optimized for character decoding. For sequential modeling, they incorporated a language model in the form of either n-gram or RNN to evaluate the likelihood of speciﬁc character sequences with an over 1,000-word vocabulary. Moses et al. [132] used longterm ECoG of a paralyzed individual with anarthria to decode words and sentences under attempted speech task of 50-word vocabulary in English. They used an LSTM-based speech detection model to identify speech onset, a bidirectional GRUbased word classiﬁcation model to classify 50 words, and an n-gram language model combined with a Viterbi decoder for sentence reconstruction. Zhang et al. [133] proposed a modular neural network framework using ECoG under reading task in Mandarin Chinese. The framework combined three

components of speech onset detection, tone (four tones in Mandarin Chinese) decoding, and syllable decoding modules, integrated post-hoc using a Viterbi-based Bayesian language model for sequential modeling.

Language Modeling via Large Language Models Large Language Models (LLMs) have become the standard in language modeling due to its unprecedented performance in all language tasks [134], [135]. The decoder-only GPT-like LLMs thus replace n-gram or Viterbi in language-wise sequential modeling. Additionally, they are also capable for handling much more complicated cases such as multi-lingual decoding.

Mischler et al. [136] used intracranial EEG data collected under listening task in English. They applied ridge regression to align representations of neural responses to corresponding text data, obtained with open-source LLMs’ representations. They demonstrated that higher-performance LLMs align more closely with brain-like hierarchical feature extraction pathways, particularly beneﬁting from contextual information.

- Tang et al. [137] proposed to decode fMRI to language

under perceived or imagined speech task in English. They used a multivariate Gaussian distribution modeling for conditional latent space cross-modality instance-wise generative modeling. Then, they used a ﬁne-tuned LLM to predict coherent sequences, additionally leveraging beam search to optimize candidate sequences for vocabulary consisting of thousands of words.

- Tang et al. [138] used ECoG from stroke patients with

dysarthria under silently attempted speech task in English. Brain data were segmented into tokens, where a 1D-CNN directly classiﬁed each segment into a corresponding language token. For sequential modeling, a pre-trained LLM then reﬁned sentences by incorporating contextual and emotional cues.

Silva et al. [139] decoded ECoG data from a participant with anarthria and paralysis into sentences under bilingual attempted speech in English and Spanish. They employed a bidirectional GRU for word classiﬁcation using ECoG signals. For sequential modeling, they used language-speciﬁc n-gram and a bilingual large language model, followed by a bilingual beam search to reﬁne word sequences and ﬂexibly infer the intended language.

Direct Sequence-to-Sequence Translation Sequence-tosequence modeling has emerged as a powerful framework for speech decoding. It involves transforming a temporal sequence

of neural signals into another sequential representation, such as phonemes, words, or sentences, by leveraging encoderdecoder architectures of RNNs/GRUs/LSTMs or encoderdecoder Transformers. The encoder processes raw brain signal data, extracting meaningful high-dimensional representations, while the decoder generates structured output sequences by maintaining temporal coherence and contextual relevance. These models can handle the inherent temporal dynamics of neural activity, accommodating the sequential unfolding of linguistic information over time.

Makin et al. [140] developed an encoder-decoder framework for word-level cross-modality translation using ECoG under reading task in English. High-gamma features of ECoG signals were processed with temporal convolutions, encoded into high-dimensional representations by an RNN. For sequential modeling, another decoder RNN used this representation to generate words of a sentence, maintaining coherence between successive predictions. Duraivel et al. [141] decoded ECoG to phoneme sequences under speech repetition tasks in English. A sequence-to-sequence RNN was used to map ECoG features to phoneme sequences, one phoneme at a time, using the encoder’s output.

Willett et al. [111] and Card et al. [142] both studied MEA for text decoding for a (different) participant with ALS under attempted speech task in English. Willett et al. [111] used a GRU to map spike features to phoneme probabilities, leveraging CTC objective to align neural inputs and phoneme sequences. Decoded phonemes were sequentially modeled with an n-gram language model via Viterbi search to infer ﬂuent word sequences. In Card et al. [142], neural signals were processed to extract spike-band power and threshold crossings. A bidirectional GRU was used under CTC objective in an identical purpose. The outputs were integrated with a ngram language model, followed by multi-stage rescoring, to construct ﬂuent word sequences. Both systems were evaluated for both 50-word and 125,000-word vocabulary and achieved low error rates.

Acoustic Speech Waveform Generation Direct acoustic speech waveform conversion bypasses intermediate linguistic representations like phonemes or words by translating brain signals to continuous acoustic representations. Melspectrograms, which capture the spectral characteristics of speech in a time-frequency domain, are commonly used as intermediary representations. Each temporal segment of neural activity is mapped to and aligned with corresponding frames in the mel-spectrogram. Vocoders, short for voice coders, then convert the mel-spectrogram into raw audio/speech waveforms. Articulatory kinematics and linear predictive coefﬁcients are also frequently employed as intermediate representations. The vocoders are usually in the architecture of sequenceto-sequence RNNs, such as WaveNet [143] and its variants.

Angrick et al. [144] used ECoG data for speech synthesis under reading task in English. They employed densely connected 3D CNN [145] to map spatiotemporal feature of broadband gamma power of ECoG onto logMel spectrograms, which provide a compressed acoustic representation of speech.

- A pre-trained WaveNet vocoder conditioned on logMel features [146] then reconstructed speech waveforms.

Anumanchipalli et al. [147] used ECoG data for speech synthesis under reading and miming task in English. They utilized a bidirectional LSTM model to decode articulatory kinematics from neural signals, followed by a second LSTM to convert kinematics into acoustic features for synthesizing speech waveform.

Metzger et al. [112] decoded ECoG of a participant with severe limb and vocal paralysis under attempted speech task in English. Three output modalities: text, synthesized speech, and facial avatar animations, were considered. Signals were mapped into phonemes through a bidirectional GRU, n-gram model and beam search were then used to reﬁne the phoneme predictions for sequential modeling. The phonemes were then converted into discrete speech units from mel-spectrograms of speech-sound features, and the speech waveform was further synthesized using a unit-to-speech pre-trained vocoder [148]. Articulatory gestures, which were converted using an encapsulated model for animating live speech, were then used to animate synchronized facial movements of an avatar in realtime.

Angrick et al. [149] used ECoG from an ALS participant for decoding a closed 6-word vocabulary under attempted speech task in English. The decoding pipeline included three RNNs: a one-directional one to identify speech segments, a bidirectional one to map signals onto linear predictive coefﬁcients, and a pre-trained vocoder [150] to reconstruct acoustic waveforms.

Wairagkar et al. [151] used MEA from a participant with ALS and dysarthria under attempted speech task in English. Acoustic features were extracted using a Transformer model. These features included vocal tract, tone, and voicing characteristics, which were converted into continuous speech by a pre-trained vocoder [150].

Chen et al. [152] used ECoG data from epilepsy participants for speech synthesis under a series of speech tasks in English. ECoG signals were mapped into acoustic speech parameters through an ECoG encoder with 3D ResNet, 3D Swin Transformer [153], or LSTM architectures. A differentiable speech synthesizer then converted these parameters into a spectrogram, which was subsequently transformed into speech waveforms.

Application Broadness Speech neuroprosthesis has transformative potential for individuals with severe speech impairments, offering a pathway to regain communication capabilities. These technologies can bridge the gap for patients with conditions like ALS, anarthria, or stroke-induced paralysis, providing them with a means to express themselves and interact with the world. The societal implications of restoring speech extend beyond basic communication, encompassing emotional expression, social engagement, and improved quality of life.

Despite their promise, the applicability of speech neuroprostheses remains limited. Current methods heavily rely on invasive brain-recording techniques, such as ECoG or MEA, which require surgical implantation and long-term use to collect subject-speciﬁc training data [154]. This restricts accessibility to individuals who meet strict medical criteria. Additionally, decoding performance often diminishes for less invasive methods like EEG, due to lower signal resolution and

susceptibility to noise. The lack of scalable, non-invasive solutions hinders broader adoption. Additionally, the performance of direct waveform conversion pipelines, particularly those using mel-spectrograms, also remains underwhelming, limiting the naturalness and intelligibility of synthesized speech. Continued research in decoding accuracy, model generalization, and minimum calibration strategies are essential for enabling the widespread adoption of speech decoding-based BCIs.

- C. Affect Decoding

Affect decoding is becoming increasingly signiﬁcant due to its essential role in human cognition, communication, and decision-making processes [155], as well as its critical importance for intelligent systems [156]. An affective BCI is deﬁned as a system that monitors and/or regulates the emotional states of the brain [157]. While our prior review comprehensively addressed the purpose, datasets, and machine learning components of affective BCIs, this review focuses speciﬁcally on fusion methods that leverage contemporary AI models under multimodal inputs. The publicly available datasets are omitted in this review as they were summarized in [157], including information on the speciﬁc modalities.

Feature- or Decision-Level Fusion Feature- and decisionlevel fusion methods represent classic approaches for integrating multiple modalities. Feature-level fusion typically involves concatenating features extracted from different modalities into a uniﬁed representation, which is then used for subsequent classiﬁer training. In contrast, decision-level fusion independently trains classiﬁers for each modality, with predictions aggregated through ensemble strategies based on prediction scores.

For feature-level fusion, Wu et al. [158] concatenated features from four physiological signals (EEG, electrocardiogram, skin conductance level, and respiration) for arousal classiﬁcation. Zheng and Lu et al. [159] concatenated EEG and electrooculography features for vigilance regression. Soleymani et al. [160] combined EEG signals, eye gaze data, and pupillary responses to classify emotions. Beyond feature-level fusion, they also explored decision-level fusion where classiﬁcations from each modality are combined based on their conﬁdence (prediction probability) scores.

Chen et al. [161] introduced a framework for integrating multimodal and multiset neurophysiological data. They used complementary modalities of EEG, fMRI, electromyography, and kinematic data to enhance brain function analysis. They introduced a joint blind source separation approach that achieves multimodal fusion by recovering ensembles of independent sources while exploiting shared statistical dependencies across datasets. This fusion methodology addresses the limitations of single-modality analyses by maximizing the correlation or independence across modalities through advanced optimization techniques like canonical correlation analysis and its variants.

Gong et al. [162] integrated EEG and eye movement modalities for emotion classiﬁcation. They used a non-neural network approach called completeness modality representation learning to capture both modality-independent and modalityrelevant features. Additionally, they used a weighted represen-

tation distribution alignment to align marginal and conditional distributions across subjects.

For a comprehensive survey of these methods, Poria et al. provided a detailed review that highlights their applications in affective computing.

Representation Fusion Representation fusion leverages neural networks to integrate feature extraction and fusion processes, enabling the automatic learning of multimodal representations and fusion of multiple modalities simultaneously.

Han et al. [163] integrated fMRI-based brain responses and low-level audio-visual features for arousal classiﬁcation. Multimodal fusion was achieved using a multimodal deep Boltzmann machine, which learns a joint probabilistic representation of the modalities. The model captured the complementary features of fMRI-derived functional connectivity matrices and audio-visual characteristics, enabling effective classiﬁcation while allowing inference of joint representations from audio-visual features alone during testing.

Du et al. [164] utilized EEG and eye movement signals for emotion classiﬁcation. The fusion of modalities is achieved through a multi-view variational autoencoder framework that models the statistical relationships between modalities in a joint latent space. A non-uniformly weighted Gaussian mixture posterior approximates the latent space, allowing dynamic weighting of each modality based on its importance, which facilitates robust semi-supervised classiﬁcation and imputation of missing data. This approach leverages both labeled and unlabeled data to improve performance on incomplete multimodal datasets with missing modalities.

Zheng et al. [165] integrated EEG and eye movement data for emotion classiﬁcation. A bimodal autoencoder extracted shared high-level representations from both modalities. The framework ﬁrst trained individual restricted Boltzmann machines for EEG and eye movement features, then combined them into a shared representation through stacking and ﬁnetuning.

Yan et al. [166] used EEG and eye movement data for emotion classiﬁcation. The fusion was achieved with a bimodal autoencoder for conditioning on a joint latent space. Thus representation of the missing modality could be synthesized using a conditional GAN from single-modality eye movement data, reducing reliance on EEG.

Fusion via Multimodal Transformers Multimodal Transformers have emerged as powerful tools for integrating information across diverse modalities, due to advantages detailed in Section III-D.

Jiang et al. [167] proposed a multimodal Transformer for emotion classiﬁcation using EEG and eye movement modalities. They used multi-stream to one-stream hierarchical attention, where EEG and eye movement features are processed independently within their respective streams using self-attention, followed by a fusion mechanism that integrates the outputs of these streams into a uniﬁed representation. Adversarial training is further applied to improve cross-subject generalization by reducing domain-speciﬁc discrepancies between subjects.

Li et al. [168] integrated acoustic, textual, and EEG modalities for spoken language intent recognition, using intent

categories (e.g., query, irony, praise) as the task labels. To model inter-modal dependencies, multi-head cross-attention of multimodal Transformers dynamically adjusted the weight of acoustic-textual joint features using EEG-based brain representations. Additionally, the framework employed a joint multitask learning approach, optimizing intent recognition as the primary task and emotion recognition as an auxiliary task to enhance performance. This multimodal strategy enabled the interpretation of the speaker’s true intent.

Yin et al. [169] used EEG and electrooculography modalities for emotion classiﬁcation. The fusion was achieved through multimodal Transformers with hierarchical attention. Intra-modal channel attention focused on extracting dependencies and assigning weights across different EEG and electrooculography channels within each modality, while crossmodal temporal attention captured global dependencies across the temporal features of EEG and electrooculography signals, allowing for the integration of information across modalities.

Sequential Fusion Sequential fusion methods focus on leveraging temporal correlations to enhance multimodal analysis. Such modes attempt to integrate representation learning, sequential modeling, and multimodal fusion in a uniﬁed framework. Sequential neural network models and Multimodal Transformers are widely adopted for this purpose.

Zhu et al. [170] integrated EEG and facial expression data for valence and arousal classiﬁcation. They proposed a self-attention-based multi-channel LSTM for temporal feature alignment and a conﬁdence regression network to estimate the reliability of each modality. The fusion process dynamically weighted modalities based on their conﬁdence levels and combined them using a weighted concatenation strategy.

Zhang et al. [171] utilized blood volume pulse and electrodermal activity signals for stress recognition, with binary and multi-class stress labels. 1D-CNNs and LSTMs were used to model these two modalities, respectively. The fusion was achieved using a cross-attention that aligned and fused the two modalities to learn joint representations under temporal slices, while self-attention reduced noise.

Koorathota et al. [172] employed EEG, photoplethysmography, and electrodermal activity data for valence and arousal classiﬁcation. Multimodal Transformers used cross-attention to align and integrate features across modalities, while selfattention was used to reﬁne temporal and intra-modal features, leveraging long-range interactions to enhance emotion recognition performance.

Zhang et al. [173] used multimodal Transformers for integrating EEG and peripheral physiological signals for valence and arousal classiﬁcation tasks. The fusion methodology employed an intra-modality self-attention to enhance modalityspeciﬁc features, followed by an inter-modality cross-attention to model correlations between modalities. A credibility fusion module then evaluated the sequential pattern consistency of modalities using dynamic time warping, assigning weights to ensure credible fusion.

Zhu et al. [174] employed EEG and eye-tracking data for mild depression detection. The fusion was achieved through multimodal Transformers under hierarchical attention to model temporal dependencies and inter-modal interactions.

The model combined intra-modal feature extraction with intermodal dependencies in a structured intermediate fusion framework.

Challenges in Emotion Labeling and Elicitation The future of building effective affect decoding systems lies in addressing fundamental limitations in current datasets. One critical issue is the labeling process of emotions, which is a comparatively more serious problem for brain data which is hard to annotate directly by human evaluators. Emotion labeling also involves subjectivity and cultural diversity involved in its deﬁnition and expression. Current datasets often rely on self-reported labels or annotations from multiple experts, while future efforts could also leverage AI techniques such as selfsupervised and semi-supervised learning to reduce the reliance on labels beyond incorporating multiple modalities for better performance.

Another signiﬁcant challenge is the reliance on video stimuli for emotion elicitation, which may fail to accurately reﬂect real-world emotional experiences. Videos often evoke only superﬁcial emotional responses or limited classes of labels. Moving forward, affective BCIs would beneﬁt from the development of more intuitive, naturalistic, and interactive emotionelicitation paradigms.

V. PROGRESS, PROSPECTS, AND PITFALLS A. Multimodal Big Data

The advancement of multimodal BCIs depends on the availability of large-scale, high-quality datasets. AI-driven decoding methodologies have signiﬁcantly expanded the scope of insights extractable from such data. For multimodal BCIs, such data must not only be extensive but also meticulously structured to suit speciﬁc algorithmic tasks.

Importance of Big Data AI techniques thrive on large datasets to uncover complex, non-linear relationships within and across modalities for training heavily parameterized neural network models. For instance, sequential models like Transformers or recurrent neural networks require extensive temporal data to learn long-range dependencies, while generative models depend on substantial datasets to accurately align and reconstruct multimodal representations. Consequently, the size of multimodal datasets must scale to ensure models are adequately trained and generalizable.

Large-scale initiatives like the Human Connectome Project [175], [176] exemplify the importance of comprehensive datasets, offering thousands of fMRI scans enriched with supplementary information such as behavioral and genetic data. However, the scale of data required for multimodal BCIs often extends beyond the capabilities of such traditional repositories, necessitating new approaches to data acquisition, annotation, and integration.

Data that are Paired and Aligned Mapping or translation tasks involve converting data from one modality to another. For mapping tasks, datasets must consist of paired data from two modalities, where each instance in one modality directly corresponds to an instance in another. For sequential translation tasks, the alignment must also be temporally correlated. Pairing and alignment are the core requirements for such settings that enable AI algorithms to function effectively [177].

Data of Complementary Modalities Fusion tasks aim to integrate data from multiple modalities to enhance decoding accuracy or robustness. Unlike mapping/translation tasks, fusion tasks focus on combining complementary information from different sensors. For such tasks, simultaneous data collection is crucial to ensure that signals across modalities reﬂect the same underlying cognitive or physiological state. Note that complementarity of sensor modalities is the key to fusion. Modalities should provide distinct but related perspectives of the same phenomenon. For instance, EEG offers high temporal resolution, while fMRI provides detailed spatial information. AI-driven fusion models rely on the availability of synchronized datasets to effectively combine these diverse perspectives.

- B. Brain Data Heterogeneity

A signiﬁcant obstacle in brain data decoding is the limited dataset size available for machine learning. Instead of laboriously collecting new data, a promising alternative enabled by AI algorithms is transfer learning [178], [179]. Transfer learning leverages auxiliary labeled data previously collected, presumably from additional subjects acquired with the same or even a different brain data collection device, thereby improving the decoding accuracy for the target subject [180], [181]. Most studies focus on auxiliary data from subjects under identical collection devices and tasks. However, cross-device and cross-task transfers, where brain data are gathered using different devices or under varying tasks, remain underexplored. Fig. 7 summarizes the possible types of auxiliary data, along with their relationships to the test data, from a transfer learning perspective.

Inter-Subject Discrepancy Brain data (and physiological data in general) varies signiﬁcantly across subjects/users [180]. Without speciﬁc adaptation strategies, training AI algorithms with auxiliary subject data often yields poor or even negative results for the target subject [182]. These variations can be interpreted as distribution shifts in a probabilistic sense [178], [179], including marginal distribution shifts, conditional distribution shifts, and label shifts, which may occur independently or simultaneously, necessitating distinct mitigation strategies.

The literature provides abundant solutions to address these challenges. Data normalization is the primary method for handling marginal distribution shifts [183], with data alignment techniques offering effective solutions [181], [184], [185]. More complex issues like conditional distribution or label shifts demand ﬁne-grained approaches [186], [187]. Recent works have explored sophisticated and robust learning objectives to mitigate these impacts particularly for neural network models [188]–[191]. Additionally, studies consistently report that brain data shifts not only exist across subjects but also occur within the same subject across different collection sessions [181], [188].

Heterogeneity in Collection Devices Unlike image or text data, which can be easily aggregated for deep learning, brain data such as EEG or other intracranial multi-electrode electrical signals are complex, multivariate time-series data. These signals are collected using varying numbers of electrodes, electrode placements, and trial durations. Most existing algorithms

rely on single-channel feature extraction or neural networks designed for ﬁxed input dimensions. Aligning heterogeneous EEG data from diverse devices is challenging but essential for building large-scale datasets and enabling advanced AI applications.

Device heterogeneity has been addressed in limited studies. Some approaches utilize a common subset of channels across training and testing datasets [192], [193]. Nakanishi et al. [194] proposed mitigating device discrepancies using spatial ﬁlters computed via channel averaging. However, such methods often result in information loss by failing to utilize the full electrode set.

Liu et al. [195] proposed a co-training approach utilizing hand-designed network architectures to facilitate feature space alignment for motor imagery EEG classiﬁcation. Such an approach requires speciﬁcally designed ﬁlters for each device. Li et al. [196] proposed a uniﬁed framework of heterogeneous supervised domain adaptation to address feature space discrepancies along with marginal and conditional distribution shifts simultaneously. Their approach uses symmetric heterogeneous channel alignment to align channels across devices. Additionally, they introduced a distance metric-based feature learning objective and a model inversion-based gradient regularization strategy to enhance class discriminability while preserving transferability.

An alternative to symmetric alignment is an asymmetric, one-way mapping function from source to target devices. Liu et al. [197] proposed a knowledge distillation-based approach for motor imagery EEG classiﬁcation, ensuring information transfer from full channels of the source device to the common subset of channels shared by both the source and target device. Wang et al. [198] proposed to further transfer across species (canines and humans) for EEG-based epileptic seizure detection, using knowledge distillation to match source and target channels in the representation space.

Different Task Transfer Labeled data from similar or related tasks can also facilitate the decoding of a new task [180]. For instance, motor imagery EEG data for foot movement can aid the classiﬁcation of left- and right-hand movements, a scenario referred to as different task transfer [199]. In such cases, the source and target domains have different label spaces (tasks). A transformation matrix, constructed using a small amount of labeled target data, can project and align the target distribution with the source distribution for the most relevant class. Such utilization of auxiliary data from different tasks has also demonstrated effectiveness in practice [200].

Challenges for Transfer Learning Despite its promise, transfer learning remains constrained by the limitations of classic deep learning, including:

- • Dependence on Distribution Estimation: Transfer learning performance often relies on the availability of source and target domain data, with signiﬁcant degradation observed when such data are limited, inaccessible, or under poor quality.
- • Limited Generalization: Current methods struggle to adapt across diverse paradigms, reducing their applicability in real-world settings.

[Figure 483]

[Figure 484]

|[Figure 485]<br><br>[Figure 486]|[Figure 487]<br><br>[Figure 488]<br><br>[Figure 489]|[Figure 490]<br><br>[Figure 491]<br><br>[Figure 492]<br><br>[Figure 493]<br><br>[Figure 494]<br><br>[Figure 495]<br><br>[Figure 496]|[Figure 497]<br><br>[Figure 498]<br><br>[Figure 499]<br><br>[Figure 500]|[Figure 501]<br><br>[Figure 502]<br><br>[Figure 503]<br><br>[Figure 504]|[Figure 505]<br><br>[Figure 506]<br><br>[Figure 507]<br><br>[Figure 508]|
|---|---|---|---|---|---|
| | | | | | |
|[Figure 509]| | | | | |
|[Figure 510]| | | | | |
|[Figure 511]| | | | | |
|[Figure 512]| | | | | |
|[Figure 513]| | | | | |
| | | | | | |
| | | | | | |

[Figure 514]

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

- Fig. 7. Available types of auxiliary data that could beneﬁt target classiﬁcation, along with their types of shifts, general quantity, and availability, from a TL perspective.

• Single-Modality Focus: Most transfer learning frameworks are extensively theorized, studied, and validated within a single modality, limiting their applicability in multimodal contexts.

enabling the aggregation of diverse datasets. The objective is to learn generalized features from brain data that can be universally applied to various downstream tasks.

Tokenization for Embedding Tokenization is a crucial challenge in applying Transformer models to multivariate time-series analysis. For brain signal modeling, tokenization can be implemented in multiple ways, such as using single channels [210], [211], patches of time windows [212], [213], combinations of channel subsets and time windows [214], or frequency-domain representations [93]. In multimodal learning, tokenization becomes even more complex, requiring a uniﬁed strategy to accommodate multiple modalities within a single framework.

The emerging paradigm of the brain foundation model, discussed in the next subsection, offers a potential revolutionary alternative to address these issues, representing a promising direction for future research.

- C. Brain Foundation Model

The trend toward building larger and deeper models is evident across ﬁelds, from natural language processing [134] to computer vision [29], and is now extending to general timeseries data [201]. Developing large brain foundation models has gained signiﬁcant interest in the research community.

In the context of multimodal applications, research interest has also focused on generative brain models [215] and aligning brain data with other modalities [216]. However, the development of multimodal brain foundation models remains an open challenge, with key questions yet to be resolved.

Large-scale Transformers In the context of brain data, the advantages of Transformer architectures are being increasingly recognized. Architectures that integrate CNN-based feature extraction with Transformer encoders have demonstrated superior performance in brain data decoding when compared to traditional CNN- or RNN-only models [202]–[208]. These hybrid designs, when properly optimized, offer notable improvements in decoding accuracy.

D. Common Errors

Physiological signals often exhibit temporal correlations within both short and long ranges during experimental sessions, as demonstrated in EEG [217] and fMRI [218]. These temporal patterns indicate the presence of a background hidden state unique to each session or block of data collection. Such hidden states, although generally unrelated to the task stimuli, are inherent in data collection processes. Consequently, machine learning algorithms should not rely on these hidden states as proxies for task-related classes or exploit future hidden states to predict past outcomes. Due to the

Training Strategies Fit for Foundation Models Scaling both model size and data volume is necessary but insufﬁcient for building effective foundation models. Tailored training strategies that leverage large datasets are critical. A key component of these strategies is representation learning, often achieved through self-supervised learning [209]. This approach eliminates the dependence on labels or task-speciﬁc settings,

interdisciplinary nature of brain signal decoding, these issues might not always be evident to researchers, particularly those in the machine-learning community focused on multimodal applications. Below, we examine some of the most notable problems in this context.

Block Design A recent study [219] highlights errors in certain data collection protocols, such as those reported in [220], and subsequent works [221]–[226]. These errors stem from block-wise temporal correlations inherent in brain signals, leading to unintended biases. The study illustrates how block design ﬂaws, as shown in Fig. 8, can cause classiﬁcation algorithms to rely on block-speciﬁc hidden states rather than task-relevant patterns. This issue arises when training and test splits fail to ensure temporal independence. As a result, regardless of whether the classiﬁer is feature-based or neuralnetwork-based, its predictions are inadvertently guided by block-speciﬁc temporal artifacts rather than stimulus-related activity. Consequently, performance metrics appear artiﬁcially inﬂated and fail to reﬂect real-world applicability. Speciﬁcally, “The block design leads to the classiﬁcation of arbitrary brain states based on block-level temporal correlations that are known to exist in all EEG data, rather than stimulus-related activity. Because every trial in their test sets comes from the same block as many trials in the corresponding training sets, their block design thus leads to classifying arbitrary temporal artifacts of the data instead of stimulus-related activity.”

Temporal Normalization Brain-state monitoring spans durations from seconds to months, depending on the clinical context or task stimuli [227]. For brain signals with low signalto-noise ratios and susceptibility to motion artifacts, normalization techniques are essential. These approaches, commonly considered preprocessing steps in machine learning, are increasingly recognized in brain-signal analysis. Temporal normalization addresses marginal distribution shifts [180], [183] by reducing noise and variability, enhancing decoding performance. However, when applied without caution, especially in the presence of block design ﬂaws, normalization can introduce temporal leakage, compromising model validity.

For instance, the SEED dataset [228], widely used in affective BCIs, applies differential entropy features normalized via linear dynamical systems [229]. In this context, users’ emotional states are analyzed based on brain signal recordings elicited by movie clips. During analysis, each multi-minute recording block is typically split into smaller trials. Normalization is applied to these trials using statistics from preceding trials within the same block. As illustrated in Fig. 9, this leads to block-speciﬁc feature distributions. When training and test sets are drawn from the same block (thus containing highly similar normalized features of the identical class), classiﬁers exploit these distributions, resulting in inﬂated performance metrics. Proper segregation of training and test samples across blocks is crucial to avoid this issue.

Avoiding Temporal Leakage To highlight these issues, we emphasize the following:

• Data Split Protocol: Temporal leakage occurs when training and test sets include trials from the same block, and classiﬁers rely on brain states instead of task-related components for classiﬁcation.

- • Classiﬁer Independence: The core issue stems from improper data splits combined with ﬂawed experimental protocols. Temporal leakage is independent of the classiﬁer type.
- • Impact on Experimental Conclusions: Temporal leakage, of false data split under such methods, invalidates experimental conclusions for decoding. However, it does not necessarily falsify the classiﬁcation algorithm (neural network architecture or feature extraction method) or the normalization method itself.

Researchers can adopt the following practices to avoid temporal leakage:

- • Adopt Standard Experimental Designs: Ensure experimental conditions are randomly distributed across multiple blocks, intertwining task stimuli with block-speciﬁc hidden states.
- • Avoid Random Data Splits: Random splits of brain data within a block into training and test sets are impractical and incur temporal leakage, compromising real-world applicability [230].
- • Focus on Cross-Subject Generalization: Test trials should ideally come from entirely separate blocks or subjects to ensure robust model evaluation, regardless of whether it is feature-based models, neural network models, or foundation models.
- • Use Proper Preprocessing: While preprocessing steps (e.g., bandpass, notch ﬁltering) cannot entirely eliminate the impact of ﬂawed experimental designs, they can mitigate issues or reveal underlying problems [219].

E. Security and Privacy

The security and privacy of BCIs have long been major concerns [231]. As multimodal techniques and large models continue to advance, the signiﬁcance of BCI security and privacy will only increase [232], [233].

Security Issues BCI outputs are susceptible to manipulation via adversarial attacks [234]. Zhang and Wu [235] were the ﬁrst to demonstrate that adversarial samples could signiﬁcantly degrade the decoding accuracy of EEG-based BCIs. Liu et al. [153] and Jung et al. [236] developed universal adversarial perturbations, simplifying the implementation of such attacks. Wang et al. [237] explored physically constrained attacks, while Gunawardena et al. [238] showed that attacking a single sensor could manipulate the outputs of smart headsets for behavioral biometrics. Liang et al. [239] discovered that backdoors could be embedded in multimodal models, allowing for manipulation of their outputs. These adversarial attacks raise signiﬁcant safety concerns, making adversarial robustness a critical issue for BCIs.

Both active and reactive defense strategies are essential for enhancing BCI security [238]. Active defense can be integrated at various stages of the BCI decoding pipeline, with approaches such as standardized data processing, effective data augmentation, rational model architectures, and generalizable training algorithms contributing to BCI models that are more resilient to adversarial attacks [240], [241]. Reactive defense focuses on detecting and rejecting inputs that have been

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

[Figure 529]

[Figure 530]

[Figure 531]

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

[Figure 540]

[Figure 541]

[Figure 542]

[Figure 543]

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

(a) (b)

- Fig. 8. Common error of block design on brain signal classiﬁcation experiments. (a) Incorrect experiment protocol, where each block contains only one class of stimuli. Classiﬁers can rely solely on the block-speciﬁc brain states to differentiate between task-related classes, irrespective of the actual stimulus-related brain patterns. This limitation persists regardless of the random or sequential division between training and test sets. (b) The correct experiment protocol, where each block would contain all classes of stimuli and the stimuli would be preferably presented in random order. During analysis, training and test samples are segregated to not overlap by block. It ensures that classiﬁers do not learn to discriminate based merely on block-speciﬁc temporal patterns.

[Figure 553]

|[Figure 554]|
|---|

| |
|---|

- Fig. 9. Common error of normalization on block-based brain signal classiﬁcation under machine learning. t-SNE visualization of EEG data from SEED dataset shows that normalization produces high within-block feature similarity while maintaining distinct distributions across blocks. Improper data splits involving the same block in training and test sets lead to misleading performance metrics.

the development of more accurate and secure BCI models.

Privacy Issues Several regulations, such as the European Union’s General Data Protection Regulation and China’s Personal Information Protection Law, have been introduced to safeguard user privacy. Regardless of the paradigm, brain data inherently contain sensitive personal information [243]. For example, Martinovic et al. [244] showed that EEG signals can reveal private details, including credit card numbers, personal identiﬁcation numbers, contacts, and addresses. Ienca et al. [231] highlighted the ethical and privacy issues associated with consumer neurotechnology. Landau et al. [245] demonstrated that even resting-state EEG data can disclose personal characteristics such as personality traits and cognitive abilities.

Various methods can be employed to protect the privacy of brain data, including privacy-preserving machine learning, synthetic data generation, data perturbation, and federated learning [243], [246]. Privacy-preserving machine learning avoids using raw brain data or model parameters directly. Synthetic data generation leverages generative models to produce data that retains essential information for BCI tasks. Data perturbation adds noise to the original data to protect private information, while maintaining the data’s utility for downstream tasks [246]. Federated learning trains a global model without sharing brain data between the server and the clients, or among the clients, protecting user privacy by preventing other devices from accessing raw data stored on the local client, thus avoiding the privacy risks of centralized datasets [195], [247].

tampered with. Combining both defense strategies can improve the overall security of BCIs [238].

As multimodal techniques and large models evolve, new security challenges must be addressed. For example, the integration of multimodal, cross-paradigm brain signals may inﬂuence the vulnerability of BCIs, an area yet to be explored [239]. This could lead to the emergence of new methods to enhance BCI security, such as improved data alignment in multimodal models and more effective multi-dataset fusion in large models, which may help create more secure and accurate BCI models. Consequently, adversarial robustness could also serve as an evaluation metric for BCI models [242], facilitating

As more brain signals are incorporated into multimodal and large BCI decoding models, ensuring privacy will present greater challenges. Future research must focus on understand-

ing the privacy risks in larger datasets and protecting user information.

VI. CONCLUSIONS

This review explored the landscape of AI-powered decoding methodologies for multimodal BCIs, addressing their elements, decoding algorithms, applications, and challenges. By emphasizing advancements in cross-modality mapping, sequential modeling, and multimodal fusion, this work highlighted the pivotal role of AI decoding algorithms in enabling more accurate BCIs. From decoding brain signals for visual, speech, and affective BCI applications to discussing the transformative potential of large-scale brain foundation models, we showcased the profound impact of AI methodologies for this interdisciplinary ﬁeld.

The prospects for AI-powered multimodal BCIs are vast, extending into healthcare, neurorehabilitation, immersive virtual reality, and beyond. With continued advancements in decoding algorithms and the integration of large-scale brain data, these systems are poised to transform human-computer interaction and neurotechnology. By addressing the outlined challenges and leveraging emerging AI paradigms, the ﬁeld is well-positioned to unlock the full potential of BCIs. Fundings also support the development of BCIs [248], [249], paving the way for a future where seamless brain-machine integration enhances human capabilities and quality of life.

REFERENCES

- [1] D. L. Schacter, D. T. Gilbert, and D. M. Wegner, Psychology. Macmillan, 2009.
- [2] T. Baltrusˇaitis, C. Ahuja, and L.-P. Morency, “Multimodal machine learning: A survey and taxonomy,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 41, no. 2, pp. 423–443, 2019.
- [3] H. Gu¨rko¨k and A. Nijholt, “Brain–computer interfaces for multimodal interaction: a survey and principles,” Int’l Journal of Human-Computer Interaction, vol. 28, no. 5, pp. 292–307, 2012.
- [4] R. P. Rao, Brain-Computer Interfacing: an Introduction. Cambridge University Press, 2013.
- [5] T. O. Zander, C. Kothe, S. Welke, and M. Ro¨tting, “Utilizing secondary input from passive brain-computer interfaces for enhancing human-machine interaction,” in Proc. Int’l Conf. Foundations of Augmented Cognition. Neuroergonomics and Operational Neuroscience, San Diego, CA, Jul. 2009, pp. 759–771.
- [6] E. C. Leuthardt, G. Schalk, J. R. Wolpaw, J. G. Ojemann, and D. W. Moran, “A brain-computer interface using electrocorticographic signals in humans,” Journal of Neural Engineering, vol. 1, no. 2, pp. 63–71, 2004.
- [7] J. Talairach and J. Bancaud, “Lesion, “irritative” zone and epileptogenic focus,” Conﬁnia Neurologica, vol. 27, no. 1, pp. 91–94, 1966.
- [8] A. B. Schwartz, “Cortical neural prosthetics,” Annual Review of Neuroscience, vol. 27, pp. 487–507, 2004.
- [9] E. Musk and Neuralink, “An integrated brain-machine interface platform with thousands of channels,” Journal of Medical Internet Research, vol. 21, no. 10, p. e16194, 2019.
- [10] Y. Jiang, Z. Zhang, Y.-X. Wang, D. Li, C.-T. Coen, E. Hwaun, G. Chen, H.-C. Wu, D. Zhong, S. Niu et al., “Topological supramolecular network enabled high-conductivity, stretchable organic bioelectronics,” Science, vol. 375, no. 6587, pp. 1411–1417, 2022.
- [11] X. Tang, H. Shen, S. Zhao, N. Li, and J. Liu, “Flexible brain–computer interfaces,” Nature Electronics, vol. 6, no. 2, pp. 109–118, 2023.
- [12] J. Wang, T. Wang, H. Liu, K. Wang, K. Moses, Z. Feng, P. Li, and W. Huang, “Flexible electrodes for brain–computer interface system,” Advanced Materials, vol. 35, no. 47, p. 2211012, 2023.
- [13] S. Zhao, X. Tang, W. Tian, S. Partarrieu, R. Liu, H. Shen, J. Lee, S. Guo, Z. Lin, and J. Liu, “Tracking neural activity from the same cells during the entire adult life of mice,” Nature Neuroscience, vol. 26, no. 4, pp. 696–710, 2023.

- [14] A. Zhang, E. T. Mandeville, L. Xu, C. M. Stary, E. H. Lo, and C. M. Lieber, “Ultraﬂexible endovascular probes for brain recording through micrometer-scale vasculature,” Science, vol. 381, no. 6655, pp. 306– 312, 2023.
- [15] C. Dong, A. Carnicer-Lombarte, F. Bonafe, B. Huang, S. Middya, A. Jin, X. Tao, S. Han, M. Bance, D. G. Barone et al., “Electrochemically actuated microelectrodes for minimally invasive peripheral nerve interfaces,” Nature Materials, vol. 23, pp. 969–976, 2024.
- [16] P. Le Floch, S. Zhao, R. Liu, N. Molinari, E. Medina, H. Shen, Z. Wang, J. Kim, H. Sheng, S. Partarrieu et al., “3D spatiotemporally scalable in vivo neural probes based on ﬂuorinated elastomers,” Nature Nanotechnology, vol. 19, no. 3, pp. 319–329, 2024.
- [17] S. H. Lee, M. Thunemann, K. Lee, D. R. Cleary, K. J. Tonsfeldt, H. Oh, F. Azzazy, Y. Tchoe, A. M. Bourhis, L. Hossain et al., “Scalable thousand channel penetrating microneedle arrays on ﬂex for multimodal and large area coverage brainmachine interfaces,” Advanced Functional Materials, vol. 32, no. 25, p. 2112045, 2022.
- [18] J. Parvizi and S. Kastner, “Promises and limitations of human intracranial electroencephalography,” Nature Neuroscience, vol. 21, no. 4, pp. 474–483, 2018.
- [19] B. J. Edelman, S. Zhang, G. Schalk, P. Brunner, G. Mu¨ller-Putz, C. Guan, and B. He, “Non-invasive brain-computer interfaces: State of the art and trends,” IEEE Reviews in Biomedical Engineering, pp. 1–25, early access, 2024.
- [20] Y. Roy, H. Banville, I. Albuquerque, A. Gramfort, T. H. Falk, and J. Faubert, “Deep learning-based electroencephalography analysis: a systematic review,” Journal of Neural Engineering, vol. 16, no. 5, p. 051001, 2019.
- [21] X. Gu, Z. Cao, A. Jolfaei, P. Xu, D. Wu, T.-P. Jung, and C.-T. Lin, “EEG-based brain-computer interfaces (BCIs): A survey of recent studies on signal sensing technologies and computational intelligence approaches and their applications,” IEEE/ACM Trans. Computational Biology and Bioinformatics, vol. 18, no. 5, pp. 1645–1666, 2021.
- [22] L. F. Nicolas-Alonso and J. Gomez-Gil, “Brain computer interfaces, a review,” Sensors, vol. 12, no. 2, pp. 1211–1279, 2012.
- [23] D. Cohen, “Magnetoencephalography: detection of the brain’s electrical activity with a superconducting magnetometer,” Science, vol. 175, no. 4022, pp. 664–666, 1972.
- [24] R. Sitaram, N. Weiskopf, A. Caria, R. Veit, M. Erb, and N. Birbaumer, “fMRI brain-computer interfaces,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 95–106, 2008.
- [25] B. Du, X. Cheng, Y. Duan, and H. Ning, “fMRI brain decoding and its applications in brain–computer interface: A survey,” Brain Sciences, vol. 12, no. 2, p. 228, 2022.
- [26] F. F. Jo¨bsis, “Noninvasive, infrared monitoring of cerebral and myocardial oxygen sufﬁciency and circulatory parameters,” Science, vol. 198, no. 4323, pp. 1264–1267, 1977.
- [27] Y. Bengio, A. Courville, and P. Vincent, “Representation learning: A review and new perspectives,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 35, no. 8, pp. 1798–1828, 2013.
- [28] A. v. d. Oord, Y. Li, and O. Vinyals, “Representation learning with contrastive predictive coding,” arXiv preprint arXiv:1807.03748, 2018.
- [29] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark et al., “Learning transferable visual models from natural language supervision,” in Proc. Int’l Conf. Machine Learning, Vienna, Austria, Jul. 2021, pp. 8748–8763.
- [30] F. Wang and H. Liu, “Understanding the behaviour of contrastive loss,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Nashville, TN, Jun. 2021, pp. 2495–2504.
- [31] C. H. Lampert, H. Nickisch, and S. Harmeling, “Learning to detect unseen object classes by between-class attribute transfer,” in IEEE Conf. Computer Vision and Pattern Recognition, Miami, FL, Jun. 2009, pp. 951–958.
- [32] R. Socher, M. Ganjoo, C. D. Manning, and A. Ng, “Zero-shot learning through cross-modal transfer,” in Proc. Advances in Neural Information Processing Systems, Lake Tahoe, NV, Dec. 2013.
- [33] J. Yang, C. Li, P. Zhang, B. Xiao, C. Liu, L. Yuan, and J. Gao, “Uniﬁed contrastive learning in image-text-label space,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, New Orleans, LA, Jun. 2022, pp. 19 163–19 173.
- [34] P. Khosla, P. Teterwak, C. Wang, A. Sarna, Y. Tian, P. Isola, A. Maschinot, C. Liu, and D. Krishnan, “Supervised contrastive learning,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2020, pp. 18 661–18 673.
- [35] S. Mai, Y. Zeng, S. Zheng, and H. Hu, “Hybrid contrastive learning of tri-modal representation for multimodal sentiment analysis,” IEEE Trans. Affective Computing, vol. 14, no. 3, pp. 2276–2289, 2022.

- [36] R. Lin and H. Hu, “Multimodal contrastive learning via uni-modal coding and cross-modal prediction for multimodal sentiment analysis,” in Findings of the Association for Computational Linguistics: EMNLP, 2022, pp. 511–523.
- [37] Z.-Y. Dou, A. Kamath, Z. Gan, P. Zhang, J. Wang, L. Li, Z. Liu, C. Liu, Y. LeCun, N. Peng et al., “Coarse-to-ﬁne vision-language pre-training with fusion in the backbone,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Nov. 2022, pp. 32 942–32 956.
- [38] H. Bao, W. Wang, L. Dong, Q. Liu, O. K. Mohammed, K. Aggarwal, S. Som, S. Piao, and F. Wei, “VLMO: Uniﬁed vision-language pre-training with mixture-of-modality-experts,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Nov. 2022, pp. 32897–32 912.
- [39] D. P. Kingma, “Auto-encoding variational bayes,” arXiv preprint arXiv:1312.6114, 2013.
- [40] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,” in Proc. Advances in Neural Information Processing Systems, Montreal, Canada, Dec. 2014.
- [41] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2020, pp. 6840–6851.
- [42] I. Sutskever, O. Vinyals, and Q. V. Le, “Sequence to sequence learning with neural networks,” in Proc. Advances in Neural Information Processing Systems, Montreal, Canada, Dec. 2014.
- [43] A. Graves, S. Ferna´ndez, F. Gomez, and J. Schmidhuber, “Connectionist temporal classiﬁcation: labelling unsegmented sequence data with recurrent neural networks,” in Proc. Int’l Conf. Machine learning, Pittsburgh, PA, Jun. 2006, pp. 369–376.
- [44] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. u. Kaiser, and I. Polosukhin, “Attention is all you need,” in Proc. Advances in Neural Information Processing Systems, Long Beach, CA, Dec. 2017.
- [45] P. Xu, X. Zhu, and D. A. Clifton, “Multimodal learning with transformers: A survey,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 45, no. 10, pp. 12113–12 132, 2023.
- [46] S. Thorpe, D. Fize, and C. Marlot, “Speed of processing in the human visual system,” Nature, vol. 381, no. 6582, pp. 520–522, 1996.
- [47] Y. Kamitani and F. Tong, “Decoding the visual and subjective contents of the human brain,” Nature Neuroscience, vol. 8, no. 5, pp. 679–685, 2005.
- [48] S. Sutton, M. Braren, J. Zubin, and E. John, “Evoked-potential correlates of stimulus uncertainty,” Science, vol. 150, no. 3700, pp. 1187– 1188, 1965.
- [49] O. Friman, I. Volosyak, and A. Graser, “Multiple channel detection of steady-state visual evoked potentials for brain-computer interfaces,” IEEE Trans. Biomedical Engineering, vol. 54, no. 4, pp. 742–750, 2007.
- [50] J. V. Haxby, M. I. Gobbini, M. L. Furey, A. Ishai, J. L. Schouten, and P. Pietrini, “Distributed and overlapping representations of faces and objects in ventral temporal cortex,” Science, vol. 293, no. 5539, pp. 2425–2430, 2001.
- [51] Y.-J. Zhang, Z.-F. Yu, J. K. Liu, and T.-J. Huang, “Neural decoding of visual information across different neural recording modalities and approaches,” Machine Intelligence Research, vol. 19, no. 5, pp. 350– 365, 2022.
- [52] H. Wilson, X. Chen, M. Golbabaee, M. J. Proulx, and E. O’Neill, “Feasibility of decoding visual information from EEG,” Brain-Computer Interfaces, vol. 11, no. 1-2, pp. 33–60, 2024.
- [53] B. Kaneshiro, M. Perreau Guimaraes, H.-S. Kim, A. M. Norcia, and P. Suppes, “A representational similarity analysis of the dynamics of object processing using single-trial EEG classiﬁcation,” PLOS One, vol. 10, no. 8, p. e0135697, 2015.
- [54] T. Horikawa and Y. Kamitani, “Generic decoding of seen and imagined objects using hierarchical visual features,” Nature Communications, vol. 8, no. 1, p. 15037, 2017.
- [55] H. Wen, J. Shi, Y. Zhang, K.-H. Lu, J. Cao, and Z. Liu, “Neural encoding and decoding with deep learning for dynamic natural vision,” Cerebral Cortex, vol. 28, no. 12, pp. 4136–4160, 2018.
- [56] G. Shen, T. Horikawa, K. Majima, and Y. Kamitani, “Deep image reconstruction from human brain activity,” PLOS Computational Biology, vol. 15, no. 1, p. e1006633, 2019.
- [57] N. Chang, J. A. Pyles, A. Marcus, A. Gupta, M. J. Tarr, and E. M. Aminoff, “BOLD5000, a public fMRI dataset while viewing 5000 visual images,” Scientiﬁc Data, vol. 6, no. 1, p. 49, 2019.

- [58] T. Grootswagers, A. K. Robinson, and T. A. Carlson, “The representational dynamics of visual objects in rapid serial visual processing streams,” NeuroImage, vol. 188, pp. 668–679, 2019.
- [59] E. J. Allen, G. St-Yves, Y. Wu, J. L. Breedlove, J. S. Prince, L. T. Dowdle, M. Nau, B. Caron, F. Pestilli, I. Charest et al., “A massive 7T fMRI dataset to bridge cognitive neuroscience and artiﬁcial intelligence,” Nature Neuroscience, vol. 25, no. 1, pp. 116–126, 2022.
- [60] T. Grootswagers, I. Zhou, A. K. Robinson, M. N. Hebart, and T. A. Carlson, “Human EEG recordings for 1,854 concepts presented in rapid serial visual presentation streams,” Scientiﬁc Data, vol. 9, no. 1, p. 3, 2022.
- [61] A. T. Gifford, K. Dwivedi, G. Roig, and R. M. Cichy, “A large and rich EEG dataset for modeling human visual object recognition,” NeuroImage, vol. 264, p. 119754, 2022.
- [62] M. N. Hebart, O. Contier, L. Teichmann, A. H. Rockter, C. Y. Zheng, A. Kidder, A. Corriveau, M. Vaziri-Pashkam, and C. I. Baker, “THINGS-data, a multimodal collection of large-scale datasets for investigating object representations in human brain and behavior,” eLife, vol. 12, p. e82580, 2023.
- [63] X. Liu, Y.-K. Liu, Y. Wang, K. Ren, H. Shi, Z. Wang, D. Li, B.-l. Lu, and W.-L. Zheng, “EEG2Video: Towards decoding dynamic visual perception from EEG signals,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2024.
- [64] J. Gao, Y. Fu, Y. Wang, X. Qian, J. Feng, and Y. Fu, “MinD3D: Reconstruct high-quality 3D objects in human brain,” in Proc. European Conf. Computer Vision, Milan, Italy, Sep. 2024, pp. 312– 329.
- [65] D. D. Cox and R. L. Savoy, “Functional magnetic resonance imaging (fMRI) “brain reading”: detecting and classifying distributed patterns of fMRI activity in human visual cortex,” Neuroimage, vol. 19, no. 2, pp. 261–270, 2003.
- [66] R. M. Cichy, D. Pantazis, and A. Oliva, “Resolving human object recognition in space and time,” Nature Neuroscience, vol. 17, no. 3, pp. 455–462, 2014.
- [67] S. Bagchi and D. R. Bathula, “EEG-ConvTransformer for single-trial EEG-based visual stimulus classiﬁcation,” Pattern Recognition, vol. 129, p. 108757, 2022.
- [68] J. Luo, W. Cui, S. Xu, L. Wang, X. Li, X. Liao, and Y. Li, “A dualbranch spatio-temporal-spectral transformer feature fusion network for EEG-based visual recognition,” IEEE Trans. Industrial Informatics, vol. 20, no. 2, pp. 1721–1731, 2024.
- [69] J.-D. Haynes and G. Rees, “Predicting the orientation of invisible stimuli from activity in human primary visual cortex,” Nature Neuroscience, vol. 8, no. 5, pp. 686–691, 2005.
- [70] J. Chen, Y. Qi, Y. Wang, and G. Pan, “Mind artist: Creating artistic snapshots with human thought,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Seattle, WA, Jun. 2024, pp. 27207– 27 217.
- [71] Y. Song, B. Liu, X. Li, N. Shi, Y. Wang, and X. Gao, “Decoding natural images from EEG for object recognition,” in Int’l Conf. Learning Representations, Vienna, Austria, May. 2024.
- [72] Z. Gong, Q. Zhang, G. Bao, L. Zhu, Y. Zhang, K. Liu, L. Hu, and D. Miao, “Lite-Mind: Towards efﬁcient and robust brain representation learning,” in Proc. ACM Int’l Conf. Multimedia, Melbourne, Australia, Oct. 2024.
- [73] Q. Zhou, C. Du, S. Wang, and H. He, “CLIP-MUSED: CLIP-guided multi-subject visual neural information semantic decoding,” in Int’l Conf. Learning Representations, Vienna, Austria, May. 2024.
- [74] C. Du, C. Du, and H. He, “Sharing deep generative representation for perceived image reconstruction from human brain activity,” in Proc. Int’l Joint Conf. Neural Networks, Anchorage, AK, May. 2017, pp. 1049–1056.
- [75] C. Du, C. Du, L. Huang, and H. He, “Reconstructing perceived images from human brain activities with bayesian deep multiview learning,” IEEE Trans. Neural Networks and Learning Systems, vol. 30, no. 8, pp. 2310–2323, 2019.
- [76] K. Han, H. Wen, J. Shi, K.-H. Lu, Y. Zhang, D. Fu, and Z. Liu, “Variational autoencoder: An unsupervised model for encoding and decoding fMRI activity in visual cortex,” NeuroImage, vol. 198, pp. 125–136, 2019.
- [77] F. L. Cheng, T. Horikawa, K. Majima, M. Tanaka, M. Abdelhack, S. C. Aoki, J. Hirano, and Y. Kamitani, “Reconstructing visual illusory experiences from human brain activity,” Science Advances, vol. 9, no. 46, p. eadj3906, 2023.
- [78] X. Qian, Y. Wang, X. Sun, Y. Fu, and J. Feng, “LEA: Learning latent embedding alignment model for fMRI decoding and encoding,” Trans. on Machine Learning Research, 2024.

- [79] K. He, X. Chen, S. Xie, Y. Li, P. Dolla´r, and R. Girshick, “Masked autoencoders are scalable vision learners,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, New Orleans, LA, Jun. 2022, pp. 16 000–16 009.
- [80] B. Zeng, S. Li, X. Liu, S. Gao, X. Jiang, X. Tang, Y. Hu, J. Liu, and B. Zhang, “Controllable mind visual diffusion model,” in Proc. AAAI Conf. Artiﬁcial Intelligence, vol. 38, no. 7, Vancouver, Canada, Feb. 2024, pp. 6935–6943.
- [81] D. Qian, H. Zeng, W. Cheng, Y. Liu, T. Bikki, and J. Pan, “NeuroDM: Decoding and visualizing human brain activity with EEG-guided diffusion model,” Computer Methods and Programs in Biomedicine, vol. 251, p. 108213, 2024.
- [82] P. Scotti, A. Banerjee, J. Goode, S. Shabalin, A. Nguyen, A. Dempster, N. Verlinde, E. Yundler, D. Weisberg, K. Norman et al., “Reconstructing the mind’s eye: fMRI-to-image with contrastive learning and diffusion priors,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Dec. 2023.
- [83] H. Zhang, M. Cisse, Y. N. Dauphin, and D. Lopez-Paz, “Mixup: Beyond empirical risk minimization,” in Int’l Conf. Learning Representations, Vancouver, Canada, Apr. 2018.
- [84] Y. Benchetrit, H. Banville, and J.-R. King, “Brain decoding: toward real-time reconstruction of visual perception,” in Int’l Conf. Learning Representations, Vienna, Austria, May. 2024.
- [85] D. Li, C. Wei, S. Li, J. Zou, H. Qin, and Q. Liu, “Visual decoding and reconstruction via EEG embeddings with guided diffusion,” arXiv preprint arXiv:2403.07721, 2024.
- [86] Z. Chen, J. Qing, T. Xiang, W. L. Yue, and J. H. Zhou, “Seeing beyond the brain: Conditional diffusion model with sparse masked modeling for vision decoding,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Vancouver, Canada, Jun. 2023, pp. 22 710–22 720.
- [87] J. Zhang, J. Huang, S. Jin, and S. Lu, “Vision-language models for vision tasks: A survey,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 46, no. 8, pp. 5625–5644, 2024.
- [88] C. Du, K. Fu, J. Li, and H. He, “Decoding visual neural representations by multimodal learning of brain-visual-linguistic features,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 45, no. 9, pp. 10760– 10 777, 2023.
- [89] Y. Liu, Y. Ma, W. Zhou, G. Zhu, and N. Zheng, “BrainCLIP: Bridging brain and visual-linguistic representation via CLIP for generic natural visual stimulus decoding from fMRI,” arXiv preprint arXiv:2302.12971, 2023.
- [90] D. Xie, P. Zhao, J. Zhang, K. Wei, X. Ni, and J. Xia, “BrainRAM: Cross-modality retrieval-augmented image reconstruction from human brain activity,” in Proc. ACM Int’l Conf. Multimedia, New York, NY, Oct. 2024, p. 3994–4003.
- [91] W. Xia, R. de Charette, C. Oztireli, and J.-H. Xue, “DREAM: Visual decoding from reversing human visual system,” in Proc. IEEE/CVF Winter Conf. Applications of Computer Vision, Waikoloa, HI, Jan. 2024, pp. 8226–8235.
- [92] Y. Takagi and S. Nishimoto, “High-resolution image reconstruction with latent diffusion models from human brain activity,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Vancouver, Canada, Jun. 2023, pp. 14 453–14 463.
- [93] C. Wang, V. Subramaniam, A. U. Yaari, G. Kreiman, B. Katz, I. Cases, and A. Barbu, “BrainBERT: Self-supervised representation learning for intracranial recordings,” in Int’l Conf. Learning Representations, Kigali, Rwanda, May 2023.
- [94] C. Li, X. Qian, Y. Wang, J. Huo, X. Xue, Y. Fu, and J. Feng, “Enhancing cross-subject fMRI-to-Video decoding with global-local functional alignment,” in Proc. European Conf. Computer Vision, Milan, Italy, Sep. 2024, pp. 353–369.
- [95] Y. Lu, C. Du, C. Wang, X. Zhu, L. Jiang, and H. He, “Animate your thoughts: Decoupled reconstruction of dynamic natural vision from slow brain activity,” arXiv preprint arXiv:2405.03280, 2024.
- [96] J. Li, D. Li, C. Xiong, and S. Hoi, “BLIP: Bootstrapping languageimage pre-training for uniﬁed vision-language understanding and generation,” in Proc. Int’l Conf. Machine Learning, Baltimore, MD, Jul. 2022, pp. 12 888–12 900.
- [97] J. Gao, Y. Fu, Y. Wang, X. Qian, J. Feng, and Y. Fu, “fMRI-3D: A comprehensive dataset for enhancing fMRI-based 3D reconstruction,” arXiv preprint arXiv:2409.11315, 2024.
- [98] Z. Guo, J. Wu, Y. Song, W. Mai, Q. Zheng, W. Ouyang, and C. Song, “Neuro-3D: Towards 3D visual decoding from EEG signals,” arXiv preprint arXiv:2411.12248, 2024.
- [99] M. S. Beauchamp, D. Oswalt, P. Sun, B. L. Foster, J. F. Magnotti, S. Niketeghad, N. Pouratian, W. H. Bosking, and D. Yoshor, “Dynamic

- stimulation of visual cortex produces form vision in sighted and blind humans,” Cell, vol. 181, no. 4, pp. 774–783, 2020.
- [100] M. Ferrante, T. Boccato, S. Bargione, and N. Toschi, “Decoding visual brain representations from electroencephalography through knowledge distillation and latent diffusion models,” Computers in Biology and Medicine, p. 108701, 2024.
- [101] E. F. Chang, “Brain–computer interfaces for restoring communication,” New England Journal of Medicine, vol. 391, no. 7, pp. 654–657, 2024.
- [102] A. B. Silva, K. T. Littlejohn, J. R. Liu, D. A. Moses, and E. F. Chang, “The speech neuroprosthesis,” Nature Reviews Neuroscience, vol. 25, p. 473–492, 2024.
- [103] M. W. Mathis, A. P. Rotondo, E. F. Chang, A. S. Tolias, and A. Mathis, “Decoding the brain: From neural representations to mechanistic models,” Cell, vol. 187, no. 21, pp. 5814–5832, 2024.
- [104] N. Hollenstein, J. Rotsztejn, M. Troendle, A. Pedroni, C. Zhang, and N. Langer, “ZuCo, a simultaneous EEG and eye-tracking resource for natural sentence reading,” Scientiﬁc Data, vol. 5, no. 1, pp. 1–13, 2018.
- [105] M. P. Broderick, A. J. Anderson, G. M. Di Liberto, M. J. Crosse, and E. C. Lalor, “Electrophysiological correlates of semantic dissimilarity reﬂect the comprehension of natural, narrative speech,” Current Biology, vol. 28, no. 5, pp. 803–809, 2018.
- [106] J. R. Brennan and J. T. Hale, “Hierarchical structure guides rapid linguistic predictions during naturalistic listening,” PLOS One, vol. 14, no. 1, p. e0207741, 2019.
- [107] J.-M. Schoffelen, R. Oostenveld, N. H. Lam, J. Udde´n, A. Hulte´n, and P. Hagoort, “A 204-subject multimodal neuroimaging dataset to study language processing,” Scientiﬁc Data, vol. 6, no. 1, p. 17, 2019.
- [108] N. Hollenstein, M. Troendle, C. Zhang, and N. Langer, “ZuCo 2.0: A dataset of physiological recordings during natural reading and annotation,” in Proc. Conf. Language Resources and Evaluation, 2020, pp. 138–146.
- [109] M. Verwoert, M. C. Ottenhoff, S. Goulis, A. J. Colon, L. Wagner, S. Tousseyn, J. P. Van Dijk, P. L. Kubben, and C. Herff, “Dataset of speech production in intracranial electroencephalography,” Scientiﬁc Data, vol. 9, no. 1, p. 434, 2022.
- [110] L. Gwilliams, G. Flick, A. Marantz, L. Pylkka¨nen, D. Poeppel, and J.-R. King, “Introducing MEG-MASC a high-quality magnetoencephalography dataset for evaluating natural speech processing,” Scientiﬁc Data, vol. 10, no. 1, p. 862, 2023.
- [111] F. R. Willett, E. M. Kunz, C. Fan, D. T. Avansino, G. H. Wilson, E. Y. Choi, F. Kamdar, M. F. Glasser, L. R. Hochberg, S. Druckmann et al., “A high-performance speech neuroprosthesis,” Nature, vol. 620, no. 7976, pp. 1031–1036, 2023.
- [112] S. L. Metzger, K. T. Littlejohn, A. B. Silva, D. A. Moses, M. P. Seaton, R. Wang, M. E. Dougherty, J. R. Liu, P. Wu, M. A. Berger et al., “A high-performance neuroprosthesis for speech decoding and avatar control,” Nature, vol. 620, no. 7976, pp. 1037–1046, 2023.
- [113] Z. Zhang, X. Ding, Y. Bao, Y. Zhao, X. Liang, B. Qin, and T. Liu, “Chisco: An EEG-based BCI dataset for decoding of imagined speech,” Scientiﬁc Data, vol. 11, no. 1, p. 1265, 2024.
- [114] X. Mou, C. He, L. Tan, J. Yu, H. Liang, J. Zhang, Y. Tian, Y.-F. Yang, T. Xu, Q. Wang et al., “ChineseEEG: A Chinese linguistic corpora EEG dataset for semantic alignment and neural decoding,” Scientiﬁc Data, vol. 11, no. 1, p. 550, 2024.
- [115] H. Zheng, H.-T. Wang, W.-B. Jiang, Z.-T. Chen, L. He, P.-Y. Lin, P.-H. Wei, G.-G. Zhao, and Y.-Z. Liu, “Du-IN: Discrete units-guided mask modeling for decoding speech from intracranial neural signals,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2024.
- [116] K. E. Bouchard, N. Mesgarani, K. Johnson, and E. F. Chang, “Functional organization of human sensorimotor cortex for speech articulation,” Nature, vol. 495, no. 7441, pp. 327–332, 2013.
- [117] J. Chartier, G. K. Anumanchipalli, K. Johnson, and E. F. Chang, “Encoding of articulatory kinematic trajectories in human speech sensorimotor cortex,” Neuron, vol. 98, no. 5, pp. 1042–1054, 2018.
- [118] B. K. Dichter, J. D. Breshears, M. K. Leonard, and E. F. Chang, “The control of vocal pitch in human laryngeal motor cortex,” Cell, vol. 174, no. 1, pp. 21–31, 2018.
- [119] M. K. Leonard, L. Gwilliams, K. K. Sellers, J. E. Chung, D. Xu, G. Mischler, N. Mesgarani, M. Welkenhuysen, B. Dutta, and E. F. Chang, “Large-scale single-neuron speech sound encoding across the depth of human cortex,” Nature, vol. 626, no. 7999, pp. 593–602, 2024.
- [120] M. Angrick, S. Luo, Q. Rabbani, S. Joshi, D. N. Candrea, G. W. Milsap, C. R. Gordon, K. Rosenblatt, L. Clawson, N. Maragakis et al., “Realtime detection of spoken speech from unlabeled ECoG signals: A pilot study with an ALS participant,” medRxiv, 2024.

- [121] E. M. Mugler, J. L. Patton, R. D. Flint, Z. A. Wright, S. U. Schuele, J. Rosenow, J. J. Shih, D. J. Krusienski, and M. W. Slutzky, “Direct classiﬁcation of all American English phonemes using signals from functional speech motor cortex,” Journal of Neural Engineering, vol. 11, no. 3, p. 035015, 2014.
- [122] S.-H. Lee, M. Lee, and S.-W. Lee, “Neural decoding of imagined speech and visual imagery as intuitive paradigms for BCI communication,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 28, no. 12, pp. 2647–2659, 2020.
- [123] S. Luo, M. Angrick, C. Coogan, D. N. Candrea, K. Wyse-Sookoo, S. Shah, Q. Rabbani, G. W. Milsap, A. R. Weiss, W. S. Anderson et al., “Stable decoding from a speech BCI enables control for an individual with ALS without recalibration for 3 months,” Advanced Science, vol. 10, no. 35, p. 2304853, 2023.
- [124] S. K. Wandelt, D. A. Bja˚nes, K. Pejsa, B. Lee, C. Liu, and R. A. Andersen, “Representation of internal speech by single neurons in human supramarginal gyrus,” Nature Human Behaviour, vol. 8, pp. 1136–1149, 2024.
- [125] X. Tan, Q. Lian, J. Zhu, J. Zhang, Y. Wang, and Y. Qi, “Effective phoneme decoding with hyperbolic neural networks for highperformance speech BCIs,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 32, pp. 3432–3441, 2024.
- [126] Y. Liu, Z. Zhao, M. Xu, H. Yu, Y. Zhu, J. Zhang, L. Bu, X. Zhang, J. Lu, Y. Li, D. Ming, and J. Wu, “Decoding and synthesizing tonal language speech from brain activity,” Science Advances, vol. 9, no. 23, p. eadh0478, 2023.
- [127] A. De´fossez, C. Caucheteux, J. Rapin, O. Kabeli, and J.-R. King, “Decoding speech perception from non-invasive brain recordings,” Nature Machine Intelligence, vol. 5, no. 10, pp. 1097–1107, 2023.
- [128] Y. Duan, J. Zhou, Z. Wang, Y.-K. Wang, and C.-T. Lin, “DeWave: discrete EEG waves encoding for brain dynamics to text translation,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Dec. 2023.
- [129] C. Ma, Y. Zhang, Y. Guo, X. Liu, H. Shangguan, J. Wang, and L. Zhao, “Fully end-to-end EEG to speech translation using multi-scale optimized dual generative adversarial network with cycle-consistency loss,” Neurocomputing, vol. 616, p. 128916, 2025.
- [130] C. Herff, D. Heger, A. De Pesters, D. Telaar, P. Brunner, G. Schalk, and T. Schultz, “Brain-to-text: decoding spoken phrases from phone representations in the brain,” Frontiers in Neuroscience, vol. 9, p. 217, 2015.
- [131] P. Sun, G. K. Anumanchipalli, and E. F. Chang, “Brain2Char: a deep architecture for decoding text from brain recordings,” Journal of Neural Engineering, vol. 17, no. 6, p. 066015, 2020.
- [132] D. A. Moses, S. L. Metzger, J. R. Liu, G. K. Anumanchipalli, J. G. Makin, P. F. Sun, J. Chartier, M. E. Dougherty, P. M. Liu, G. M. Abrams et al., “Neuroprosthesis for decoding speech in a paralyzed person with anarthria,” New England Journal of Medicine, vol. 385, no. 3, pp. 217–227, 2021.
- [133] D. Zhang, Z. Wang, Y. Qian, Z. Zhao, Y. Liu, X. Hao, W. Li, S. Lu, H. Zhu, L. Chen, K. Xu, Y. Li, and J. Lu, “A brain-to-text framework for decoding natural tonal sentences,” Cell Reports, vol. 43, no. 11, p. 114924, 2024.
- [134] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford,

I. Sutskever, and D. Amodei, “Language models are few-shot learners,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2020, pp. 1877–1901.

- [135] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang, J. Zhang, Z. Dong et al., “A survey of large language models,” arXiv preprint arXiv:2303.18223, 2023.
- [136] G. Mischler, Y. A. Li, S. Bickel, A. D. Mehta, and N. Mesgarani, “Contextual feature extraction hierarchies converge in large language models and the brain,” Nature Machine Intelligence, vol. 6, p. 1467–1477, 2024.
- [137] J. Tang, A. LeBel, S. Jain, and A. G. Huth, “Semantic reconstruction of continuous language from non-invasive brain recordings,” Nature Neuroscience, vol. 26, no. 5, pp. 858–866, 2023.
- [138] C. Tang, S. Gao, C. Li, W. Yi, Y. Jin, X. Zhai, S. Lei, H. Meng, Z. Zhang, M. Xu et al., “Wearable intelligent throat enables natural speech in stroke patients with dysarthria,” arXiv preprint arXiv:2411.18266, 2024.
- [139] A. B. Silva, J. R. Liu, S. L. Metzger, I. Bhaya-Grossman, M. E. Dougherty, M. P. Seaton, K. T. Littlejohn, A. Tu-Chan, K. Ganguly,

- D. A. Moses et al., “A bilingual speech neuroprosthesis driven by cortical articulatory representations shared between languages,” Nature Biomedical Engineering, vol. 8, p. 977–991, 2024.
- [140] J. G. Makin, D. A. Moses, and E. F. Chang, “Machine translation of cortical activity to text with an encoder–decoder framework,” Nature Neuroscience, vol. 23, no. 4, pp. 575–582, 2020.
- [141] S. Duraivel, S. Rahimpour, C.-H. Chiang, M. Trumpis, C. Wang, K. Barth, S. C. Harward, S. P. Lad, A. H. Friedman, D. G. Southwell et al., “High-resolution neural recordings improve the accuracy of speech decoding,” Nature Communications, vol. 14, no. 1, p. 6938, 2023.
- [142] N. S. Card, M. Wairagkar, C. Iacobacci, X. Hou, T. Singer-Clark, F. R. Willett, E. M. Kunz, C. Fan, M. Vahdati Nia, D. R. Deo et al., “An accurate and rapidly calibrating speech neuroprosthesis,” New England Journal of Medicine, vol. 391, no. 7, pp. 609–618, 2024.
- [143] A. Van Den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, K. Kavukcuoglu et al., “WaveNet: A generative model for raw audio,” arXiv preprint arXiv:1609.03499.
- [144] M. Angrick, C. Herff, E. Mugler, M. C. Tate, M. W. Slutzky, D. J. Krusienski, and T. Schultz, “Speech synthesis from ECoG using densely connected 3D convolutional neural networks,” Journal of Neural Engineering, vol. 16, no. 3, p. 036019, 2019.
- [145] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, “Densely connected convolutional networks,” in Proc. IEEE Conf. Computer Vision and Pattern Recognition, Honolulu, HI, Jul. 2017, pp. 4700– 4708.
- [146] J. Shen, R. Pang, R. J. Weiss, M. Schuster, N. Jaitly, Z. Yang, Z. Chen, Y. Zhang, Y. Wang, R. Skerrv-Ryan, R. A. Saurous, Y. Agiomvrgiannakis, and Y. Wu, “Natural TTS synthesis by conditioning Wavenet on Mel spectrogram predictions,” in IEEE Int’l Conf. Acoustics, Speech and Signal Processing, Calgary, Canada, Apr. 2018, pp. 4779–4783.
- [147] G. K. Anumanchipalli, J. Chartier, and E. F. Chang, “Speech synthesis from neural decoding of spoken sentences,” Nature, vol. 568, no. 7753, pp. 493–498, 2019.
- [148] A. Lee, P.-J. Chen, C. Wang, J. Gu, S. Popuri, X. Ma, A. Polyak, Y. Adi, Q. He, Y. Tang et al., “Direct speech-to-speech translation with discrete units,” in Proc. Annual Meeting Association for Computational Linguistics, Dublin, Ireland, May 2022, pp. 3327–3339.
- [149] M. Angrick, S. Luo, Q. Rabbani, D. N. Candrea, S. Shah, G. W. Milsap, W. S. Anderson, C. R. Gordon, K. R. Rosenblatt, L. Clawson et al., “Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS,” Scientiﬁc Reports, vol. 14, no. 1, p. 9617, 2024.
- [150] J.-M. Valin and J. Skoglund, “LPCNet: Improving neural speech synthesis through linear prediction,” in IEEE Int’l Conf. Acoustics, Speech and Signal Processing, Brighton, United Kingdom, May 2019, pp. 5891–5895.
- [151] M. Wairagkar, N. S. Card, T. Singer-Clark, X. Hou, C. Iacobacci, L. R. Hochberg, D. M. Brandman, and S. D. Stavisky, “An instantaneous voice synthesis neuroprosthesis,” bioRxiv, 2024.
- [152] H. Chen, L. He, Y. Liu, and L. Yang, “Visual neural decoding via improved visual-EEG semantic consistency,” arXiv preprint arXiv:2408.06788, 2024.
- [153] Z. Liu, L. Meng, X. Zhang, W. Fang, and D. Wu, “Universal adversarial perturbations for CNN classiﬁers in EEG-based BCIs,” Journal of Neural Engineering, vol. 18, no. 4, p. 0460a4, 2021.
- [154] M. J. Vansteensel, S. Leinders, M. P. Branco, N. E. Crone, T. Denison, Z. V. Freudenburg, S. H. Geukes, P. H. Gosselaar, M. Raemaekers, A. Schippers et al., “Longevity of a brain–computer interface for amyotrophic lateral sclerosis,” New England Journal of Medicine, vol. 391, no. 7, pp. 619–626, 2024.
- [155] J. S. Lerner, Y. Li, P. Valdesolo, and K. S. Kassam, “Emotion and decision making,” Annual Review of Psychology, vol. 66, no. 1, pp. 799–823, 2015.
- [156] M. Minsky, Society of Mind. Simon and Schuster, 1988.
- [157] D. Wu, B.-L. Lu, B. Hu, and Z. Zeng, “Affective brain-computer interfaces (aBCIs): A tutorial,” Proc. of the IEEE, vol. 11, no. 10, pp. 1314–1332, 2023.
- [158] D. Wu, C. G. Courtney, B. J. Lance, S. S. Narayanan, M. E. Dawson, K. S. Oie, and T. D. Parsons, “Optimal arousal identiﬁcation and classiﬁcation for affective computing using physiological signals: Virtual reality stroop task,” IEEE Trans. Affective Computing, vol. 1, no. 2, pp. 109–118, 2010.
- [159] W.-L. Zheng and B.-L. Lu, “A multimodal approach to estimating vigilance using EEG and forehead EOG,” Journal of Neural Engineering, vol. 14, no. 2, p. 026017, 2017.

- [160] M. Soleymani, M. Pantic, and T. Pun, “Multimodal emotion recognition in response to videos,” IEEE Trans. Affective Computing, vol. 3, no. 2, pp. 211–223, 2012.
- [161] X. Chen, Z. J. Wang, and M. McKeown, “Joint blind source separation for neurophysiological data analysis: Multiset and multimodal methods,” IEEE Signal Processing Magazine, vol. 33, no. 3, pp. 86–107, 2016.
- [162] X. Gong, C. L. P. Chen, B. Hu, and T. Zhang, “CiABL: Completenessinduced adaptative broad learning for cross-subject emotion recognition with EEG and eye movement signals,” IEEE Trans. Affective Computing, vol. 15, no. 4, pp. 1970–1984, 2024.
- [163] J. Han, X. Ji, X. Hu, L. Guo, and T. Liu, “Arousal recognition using audio-visual features and fMRI-based brain response,” IEEE Trans. Affective Computing, vol. 6, no. 4, pp. 337–347, 2015.
- [164] C. Du, C. Du, H. Wang, J. Li, W.-L. Zheng, B.-L. Lu, and H. He, “Semi-supervised deep generative modelling of incomplete multimodality emotional data,” in Proc. ACM Int’l Conf. Multimedia, Seoul, South Korea, Oct. 2018, pp. 108–116.
- [165] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “EmotionMeter: A multimodal framework for recognizing human emotions,” IEEE Trans. Cybernetics, vol. 49, no. 3, pp. 1110–1122, 2019.
- [166] X. Yan, L.-M. Zhao, and B.-L. Lu, “Simplifying multimodal emotion recognition with single eye movement modality,” in Proc. ACM Int’l Conf. Multimedia, Virtual, Oct. 2021, pp. 1057–1063.
- [167] W.-B. Jiang, X.-H. Liu, W.-L. Zheng, and B.-L. Lu, “Multimodal adaptive emotion transformer with ﬂexible modality inputs on a novel dataset with continuous labels,” in Proc. ACM Int’l Conf. Multimedia, Ottawa, Canada, Oct. 2023, pp. 5975–5984.
- [168] Z. Li, G. Zhang, S. Okada, L. Wang, B. Zhao, and J. Dang, “MBCFNet: A multimodal brain–computer fusion network for human intention recognition,” Knowledge-Based Systems, vol. 296, p. 111826, 2024.
- [169] J. Yin, M. Wu, Y. Yang, P. Li, F. Li, W. Liang, and Z. Lv, “Research on multimodal emotion recognition based on fusion of electroencephalogram and electrooculography,” IEEE Trans. Instrumentation and Measurement, vol. 73, pp. 1–12, 2024.
- [170] Q. Zhu, C. Zheng, Z. Zhang, W. Shao, and D. Zhang, “Dynamic conﬁdence-aware multi-modal emotion recognition,” IEEE Trans. Affective Computing, vol. 15, no. 3, pp. 1358–1370, 2024.
- [171] X. Zhang, X. Wei, Z. Zhou, Q. Zhao, S. Zhang, Y. Yang, R. Li, and B. Hu, “Dynamic alignment and fusion of multimodal physiological patterns for stress recognition,” IEEE Trans. Affective Computing, vol. 15, no. 2, pp. 685–696, 2024.
- [172] S. Koorathota, Z. Khan, P. Lapborisuth, and P. Sajda, “Multimodal neurophysiological transformer for emotion recognition,” in Proc. Int’l Conf. IEEE Engineering Medicine Biology Society, Glasgow, United Kingdom, Jul. 2022, pp. 3563–3567.
- [173] Y. Zhang, H. Liu, D. Wang, D. Zhang, T. Lou, Q. Zheng, and C. Quek, “Cross-modal credibility modelling for EEG-based multimodal emotion recognition,” Journal of Neural Engineering, vol. 21, no. 2, p. 026040, 2024.
- [174] F. Zhu, J. Zhang, R. Dang, B. Hu, and Q. Wang, “MTNet: Multimodal transformer network for mild depression detection through fusion of EEG and eye tracking,” Biomedical Signal Processing and Control, vol. 100, p. 106996, 2025.
- [175] D. C. Van Essen, K. Ugurbil, E. Auerbach, D. Barch, T. E. Behrens, R. Bucholz, A. Chang, L. Chen, M. Corbetta, S. W. Curtiss et al., “The human connectome project: a data acquisition perspective,” Neuroimage, vol. 62, no. 4, pp. 2222–2231, 2012.
- [176] M. F. Glasser, S. N. Sotiropoulos, J. A. Wilson, T. S. Coalson, B. Fischl, J. L. Andersson, J. Xu, S. Jbabdi, M. Webster, J. R. Polimeni et al., “The minimal preprocessing pipelines for the human connectome project,” Neuroimage, vol. 80, pp. 105–124, 2013.
- [177] M. Sato, K. Tomeoka, I. Horiguchi, K. Arulkumaran, R. Kanai, and S. Sasai, “Scaling law in neural data: Non-invasive speech decoding with 175 hours of EEG data,” arXiv preprint arXiv:2407.07595, 2024.
- [178] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans. Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345–1359, 2010.
- [179] F. Zhuang, Z. Qi, K. Duan, D. Xi, Y. Zhu, H. Zhu, H. Xiong, and Q. He, “A comprehensive survey on transfer learning,” Proc. of the IEEE, vol. 109, no. 1, pp. 43–76, 2021.
- [180] D. Wu, Y. Xu, and B.-L. Lu, “Transfer learning for EEG-based brain–computer interfaces: A review of progress made since 2016,” IEEE Trans. Cognitive and Developmental Systems, vol. 14, no. 1, pp. 4–19, 2022.

- [181] D. Wu, X. Jiang, and R. Peng, “Transfer learning for motor imagery based brain-computer interfaces: A tutorial,” Neural Networks, vol. 153, pp. 235–253, 2022.
- [182] W. Zhang, L. Deng, L. Zhang, and D. Wu, “A survey on negative transfer,” IEEE/CAA Journal of Automatica Sinica, vol. 10, no. 2, pp. 305–329, 2023.
- [183] A. Apicella, F. Isgro`, A. Pollastro, and R. Prevete, “On the effects of data normalization for domain adaptation on EEG data,” Engineering Applications of Artiﬁcial Intelligence, vol. 123, p. 106205, 2023.
- [184] P. Zanini, M. Congedo, C. Jutten, S. Said, and Y. Berthoumieu, “Transfer learning: A Riemannian geometry framework with applications to brain–computer interfaces,” IEEE Trans. Biomedical Engineering, vol. 65, no. 5, pp. 1107–1116, 2018.
- [185] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A Euclidean space data alignment approach,” IEEE Trans. Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [186] C. M. Wong, Z. Wang, B. Wang, K. F. Lao, A. Rosa, P. Xu, T.-P. Jung, C. L. P. Chen, and F. Wan, “Inter- and intra-subject transfer reduces calibration effort for high-speed SSVEP-based BCIs,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 28, no. 10, pp. 2123–2135, 2020.
- [187] W. Zhang and D. Wu, “Manifold embedded knowledge transfer for brain-computer interfaces,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 28, no. 5, pp. 1117–1127, 2020.
- [188] S. Li, Z. Wang, H. Luo, L. Ding, and D. Wu, “T-TIME: Test-time information maximization ensemble for plug-and-play BCIs,” IEEE Trans. Biomedical Engineering, vol. 71, no. 2, pp. 423–432, 2024.
- [189] Y. Wang, S. Qiu, D. Li, C. Du, B.-L. Lu, and H. He, “Multi-modal domain adaptation variational autoencoder for EEG-based emotion recognition,” IEEE/CAA Journal of Automatica Sinica, vol. 9, no. 9, pp. 1612–1626, 2022.
- [190] J. Li, S. Qiu, C. Du, Y. Wang, and H. He, “Domain adaptation for EEG emotion recognition based on latent representation similarity,” IEEE Trans. Cognitive and Developmental Systems, vol. 12, no. 2, pp. 344–353, 2020.
- [191] Z. Wang, W. Zhang, S. Li, X. Chen, and D. Wu, “Unsupervised domain adaptation for cross-patient seizure classiﬁcation,” Journal of Neural Engineering, vol. 20, no. 6, p. 066002, 2023.
- [192] L. Xu, M. Xu, Y. Ke, X. An, S. Liu, and D. Ming, “Cross-dataset variability problem in EEG decoding with deep learning,” Frontiers in Human Neuroscience, vol. 14, p. 103, 2020.
- [193] Y. Xie, K. Wang, J. Meng, J. Yue, L. Meng, W. Yi, T.-P. Jung, M. Xu, and D. Ming, “Cross-dataset transfer learning for motor imagery signal classiﬁcation via multi-task learning and pre-training,” Journal of Neural Engineering, vol. 20, no. 5, p. 056037, 2023.
- [194] M. Nakanishi, Y.-T. Wang, C.-S. Wei, K.-J. Chiang, and T.-P. Jung, “Facilitating calibration in high-speed BCI spellers via leveraging crossdevice shared latent responses,” IEEE Trans. Biomedical Engineering, vol. 67, no. 4, pp. 1105–1113, 2020.
- [195] R. Liu, Y. Chen, A. Li, Y. Ding, H. Yu, and C. Guan, “Aggregating intrinsic information to enhance BCI performance through federated learning,” Neural Networks, vol. 172, p. 106100, 2024.
- [196] S. Li, Z. Wang, S. Zheng, and D. Wu, “Heterogeneous supervised domain adaptation (HSDA) for cross-device EEG classiﬁcation,” IEEE Trans. Pattern Analysis and Machine Intelligence, under review. 2025.
- [197] D. Liu, S. Li, Z. Wang, W. Li, and D. Wu, “Spatial distillation based distribution alignment (SDDA) for cross-headset EEG classiﬁcation,” IEEE Trans. Neural Systems and Rehabilitation Engineering, under review. 2025.
- [198] Z. Wang, S. Li, and D. Wu, “Cross-species and cross-modality framework for epileptic seizure detection via multi-space alignment,” National Science Review, under review. 2025.
- [199] H. He and D. Wu, “Different set domain adaptation for brain-computer interfaces: A label alignment approach,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 28, no. 5, pp. 1091–1108, 2020.
- [200] M. Vishwanath, N. Dutt, A. M. Rahmani, M. M. Lim, and H. Cao, “Label alignment improves EEG-based machine learning-based classiﬁcation of traumatic brain injury,” in Int’l Conf. IEEE Engineering in Medicine & Biology Society, Glasgow, United Kingdom, Jul. 2022, pp. 3546–3549.
- [201] Y. Wang, H. Wu, J. Dong, Y. Liu, M. Long, and J. Wang, “Deep time series models: A comprehensive survey and benchmark,” arXiv preprint arXiv:2407.13278, 2024.
- [202] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding

- and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [203] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
- [204] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE Trans. Neural Networks and Learning Systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [205] T. Song, W. Zheng, P. Song, and Z. Cui, “EEG emotion recognition using dynamical graph convolutional neural networks,” IEEE Trans. Affective Computing, vol. 11, no. 3, pp. 532–541, 2020.
- [206] Y. Ding, N. Robinson, S. Zhang, Q. Zeng, and C. Guan, “TSception: Capturing temporal dynamics and spatial asymmetry from EEG for emotion recognition,” IEEE Trans. Affective Computing, vol. 14, no. 3, pp. 2238–2250, 2023.
- [207] Y. Ding, Y. Li, H. Sun, R. Liu, C. Tong, C. Liu, X. Zhou, and C. Guan, “EEG-Deformer: A dense convolutional transformer for brain-computer interfaces,” IEEE Journal of Biomedical and Health Informatics, pp. 1–10, early access, 2024.
- [208] Y. Ding, N. Robinson, C. Tong, Q. Zeng, and C. Guan, “LGGNet: Learning from local-global-graph representations for brain–computer interface,” IEEE Trans. Neural Networks and Learning Systems, vol. 35, no. 7, pp. 9773–9786, 2024.
- [209] X. Liu, F. Zhang, Z. Hou, L. Mian, Z. Wang, J. Zhang, and J. Tang, “Self-supervised learning: Generative or contrastive,” IEEE Trans. Knowledge and Data Engineering, vol. 35, no. 1, pp. 857–876, 2023.
- [210] X. Zhang, Z. Zhao, T. Tsiligkaridis, and M. Zitnik, “Self-supervised contrastive pre-training for time series via time-frequency consistency,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Nov. 2022, pp. 3988–4003.
- [211] C. Yang, M. Westover, and J. Sun, “BIOT: Biosignal transformer for cross-data learning in the wild,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Dec. 2023.
- [212] D. Zhang, Z. Yuan, Y. Yang, J. Chen, J. Wang, and Y. Li, “Brant: Foundation model for intracranial neural signal,” in Proc. Advances in Neural Information Processing Systems, New Orleans, LA, Dec. 2023.
- [213] G. Wang, W. Liu, Y. He, C. Xu, L. Ma, and H. Li, “EEGPT: Pretrained transformer for universal and reliable representation of EEG signals,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2024.
- [214] W. Jiang, L. Zhao, and B.-L. Lu, “Large brain model for learning generic representations with tremendous EEG data in BCI,” in Int’l Conf. Learning Representations, Vienna, Austria, May. 2024.
- [215] W. Mai, J. Zhang, P. Fang, and Z. Zhang, “Brain-conditional multimodal synthesis: A survey and taxonomy,” IEEE Trans. Artiﬁcial Intelligence, pp. 1–20, early access. 2024.
- [216] W. Xia, R. de Charette, C. Oztireli, and J.-H. Xue, “UMBRAE: Uniﬁed multimodal brain decoding,” in Proc. European Conf. Computer Vision, Milan, Italy, Sep. 2024, pp. 242–259.
- [217] K. Linkenkaer-Hansen, V. V. Nikouline, J. M. Palva, and R. J. Ilmoniemi, “Long-range temporal correlations and scaling behavior in human brain oscillations,” Journal of Neuroscience, vol. 21, no. 4, pp. 1370–1377, 2001.
- [218] E. Bullmore, C. Long, J. Suckling, J. Fadili, G. Calvert, F. Zelaya, T. A. Carpenter, and M. Brammer, “Colored noise and computational inference in neurophysiological (fMRI) time series analysis: resampling methods in time and wavelet domains,” Human Brain Mapping, vol. 12, no. 2, pp. 61–78, 2001.
- [219] R. Li, J. S. Johansen, H. Ahmed, T. V. Ilyevsky, R. B. Wilbur, H. M. Bharadwaj, and J. M. Siskind, “The perils and pitfalls of block design for EEG classiﬁcation experiments,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 43, no. 1, pp. 316–333, 2021.
- [220] C. Spampinato, S. Palazzo, I. Kavasidis, D. Giordano, N. Souly, and M. Shah, “Deep learning human mind for automated visual classiﬁcation,” in Proc. IEEE Conf. Computer Vision and Pattern Recognition, Honolulu, HI, Jul. 2017, pp. 6809–6817.
- [221] S. Palazzo, C. Spampinato, I. Kavasidis, D. Giordano, and M. Shah, “Generative adversarial networks conditioned by brain signals,” in Proc. IEEE Int’l Conf. Computer Vision, Venice, Italy, Oct. 2017, pp. 3410–3418.
- [222] I. Kavasidis, S. Palazzo, C. Spampinato, D. Giordano, and M. Shah, “Brain2Image: Converting brain signals into images,” in Proc. ACM Int’l Conf. Multimedia, Mountain View, CA, Oct. 2017, pp. 1809–1817.
- [223] C. Du, C. Du, X. Xie, C. Zhang, and H. Wang, “Multi-view adversarially learned inference for cross-domain joint distribution matching,” in

- Proc. ACM SIGKDD Int’l Conf. Knowledge Discovery & Data Mining, London, United Kingdom, Aug. 2018, pp. 1348–1357.
- [224] P. Kumar, R. Saini, P. P. Roy, P. K. Sahu, and D. P. Dogra, “Envisioned speech recognition using EEG sensors,” Personal and Ubiquitous Computing, vol. 22, pp. 185–199, 2018.
- [225] P. Tirupattur, Y. S. Rawat, C. Spampinato, and M. Shah, “ThoughtViz: Visualizing human thoughts using generative adversarial network,” in Proc. ACM Int’l Conf. Multimedia, Seoul, South Korea, Oct. 2018, pp. 950–958.
- [226] S. Palazzo, C. Spampinato, I. Kavasidis, D. Giordano, J. Schmidt, and M. Shah, “Decoding brain representations by multimodal learning of neural activity and visual features,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 43, no. 11, pp. 3833–3849, 2021.
- [227] R. Gilron, S. Little, R. Perrone, R. Wilt, C. de Hemptinne, M. S. Yaroshinsky, C. A. Racine, S. S. Wang, J. L. Ostrem, P. S. Larson et al., “Long-term wireless streaming of neural recordings for circuit discovery and adaptive stimulation in individuals with Parkinson’s disease,” Nature Biotechnology, vol. 39, no. 9, pp. 1078–1085, 2021.
- [228] W.-L. Zheng and B.-L. Lu, “Investigating critical frequency bands and channels for EEG-based emotion recognition with deep neural networks,” IEEE Trans. Autonomous Mental Development, vol. 7, no. 3, pp. 162–175, 2015.
- [229] L.-C. Shi and B.-L. Lu, “Off-line and on-line vigilance estimation based on linear dynamical system and manifold learning,” in Int’l Conf. IEEE Engineering in Medicine and Biology, Buenos Aires, Argentina, Aug. 2010, pp. 6587–6590.
- [230] S. Kapoor and A. Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science,” Patterns, vol. 4, no. 9, 2023.
- [231] M. Ienca, P. Haselager, and E. J. Emanuel, “Brain leaks and consumer neurotechnology,” Nature Biotechnology, vol. 36, no. 9, pp. 805–810, 2018.
- [232] L. Turchet, B. O’Sullivan, R. Ortner, and C. Guger, “Emotion recognition of playing musicians from EEG, ECG, and acoustic signals,” IEEE Trans. Human-Machine Systems, vol. 54, no. 5, pp. 619–629, 2024.
- [233] P. Magee, M. Ienca, and N. Farahany, “Beyond neural data: Cognitive biometrics and mental privacy,” Neuron, vol. 112, no. 18, pp. 3017– 3028, 2024.
- [234] X. Zhang, D. Wu, L. Ding, H. Luo, C.-T. Lin, T.-P. Jung, and R. Chavarriaga, “Tiny noise, big mistakes: Adversarial perturbations induce errors in brain-computer interface spellers,” National Science Review, vol. 8, no. 4, p. nwaa233, 2021.
- [235] X. Zhang and D. Wu, “On the vulnerability of CNN classiﬁers in EEG-based BCIs,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 27, no. 5, pp. 814–825, 2019.
- [236] J. Jung, H. Moon, G. Yu, and H. Hwang, “Generative perturbation network for universal adversarial attacks on brain-computer interfaces,” IEEE Journal of Biomedical and Health Informatics, vol. 27, no. 11, pp. 5622–5633, 2023.
- [237] X. Wang, R. O. S. Quintanilla, M. Hersche, L. Benini, and G. Singh, “Physically-constrained adversarial attacks on brain-machine interfaces,” in Proc. Advances in Neural Information Processing Systems Workshop on Trustworthy and Socially Responsible Machine Learning, New Orleans, LA, Nov. 2022.
- [238] R. Gunawardena, S. Jayawardena, S. Seneviratne, R. Masood, and S. S. Kanhere, “Single-sensor sparse adversarial perturbation attacks against behavioural biometrics,” IEEE Internet of Things Journal, vol. 11, no. 16, pp. 27303–27 321, 2024.
- [239] S. Liang, M. Zhu, A. Liu, B. Wu, X. Cao, and E.-C. Chang, “BadCLIP: Dual-embedding guided backdoor attack on multimodal contrastive learning,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Seattle, WA, Jun. 2024, pp. 24645–24 654.
- [240] X. Chen, Z. Wang, and D. Wu, “Alignment-based adversarial training (ABAT) for improving the robustness and accuracy of EEG-based BCIs,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 32, pp. 1703–1714, 2024.
- [241] F. Croce, M. Andriushchenko, V. Sehwag, E. Debenedetti, N. Flammarion, M. Chiang, P. Mittal, and M. Hein, “RobustBench: a standardized adversarial robustness benchmark,” in Proc. Neural Information Processing Systems Track on Datasets and Benchmarks, Virtual, Dec. 2021.
- [242] L. Meng, X. Jiang, and D. Wu, “Adversarial robustness benchmark for EEG-based brain–computer interfaces,” Future Generation Computer Systems, vol. 143, pp. 231–247, 2023.
- [243] K. Xia, W. Duch, Y. Sun, K. Xu, W. Fang, H. Luo, Y. Zhang, D. Sang, X. Xu, F.-Y. Wang, and D. Wu, “Privacy-preserving brain-computer interfaces: A systematic review,” IEEE Trans. Computational Social Systems, vol. 10, no. 5, pp. 2312–2324, 2023.

- [244] I. Martinovic, D. Davies, M. Frank, D. Perito, T. Ros, and D. Song, “On the feasibility of side-channel attacks with brain-computer interfaces,” in Proc. 21st USENIX Security Symposium, Bellevue, WA, Aug. 2012, pp. 143–158.
- [245] O. Landau, A. Cohen, S. Gordon, and N. Nissim, “Mind your privacy: Privacy leakage through BCI applications using machine learning methods,” Knowledge-Based Systems, vol. 198, p. 105932, 2020.
- [246] X. Chen, S. Li, Y. Tu, Z. Wang, and D. Wu, “User-wise perturbations for user identity protection in EEG-based BCIs,” Journal of Neural Engineering, 2024, in press.
- [247] T. Jia, L. Meng, S. Li, J. Liu, and D. Wu, “Federated motor imagery classiﬁcation for privacy-preserving brain-computer interfaces,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 32, pp. 3442–3451, 2024.
- [248] L. Wang, “Mu-ming poo: China brain project and the future of chinese neuroscience,” National Science Review, vol. 4, no. 2, pp. 258–263, 2017.
- [249] C. T. Miller, X. Chen, Z. R. Donaldson, B. J. Marlin, D. Y. Tsao, Z. M. Williams, M. Zelikowsky, H. Zeng, and W. Hong, “The BRAIN Initiative: a pioneering program on the precipice,” Nature Neuroscience, vol. 27, p. 2264–2266, 2024.

