arXiv:2506.06353v1[eess.SP]2Jun2025

# Large Language Models for EEG: A Comprehensive Survey and Taxonomy

Naseem Babu Jimson Mathew and A. P. Vinod

Abstract—The growing convergence between Large Language Models (LLMs) and electroencephalography (EEG) research is enabling new directions in neural decoding, brain-computer interfaces (BCIs), and affective computing. This survey offers a systematic review and structured taxonomy of recent advancements that utilize LLMs for EEG-based analysis and applications. We organize the recent studies into four categories: (1) LLM-inspired foundation models for EEG analysis, (2) EEG-to-language decoding, (3) cross-modal generation including image and 3D object synthesis, and (4) clinical applications and dataset management tools. The survey highlights how transformer-based architectures adapted through fine-tuning, few-shot, and zero-shot learning have enabled EEG-based models to perform complex tasks such as natural language generation, semantic interpretation, and diagnostic assistance. By presenting a structured overview of the employed models and application domains, this survey establishes a comprehensive framework to advance neural signal analysis through the application of language models.

Index Terms—Electroencephalography (EEG), Large Language Models (LLMs), Brain-Computer Interfaces (BCIs), Neural Decoding, EEG-to-Text Translation, Foundation Models.

✦

## 1 INTRODUCTION

The growing use of language models is shaping new developments in both neuroscience and artificial intelligence. Language models such as GPT, BERT [1], [2], [3], and their multimodal variants have shown remarkable success across tasks involving natural language processing and understanding, generation, and even vision-language fusion. The transformer-based architecture enables these models to effectively process sequential data, contributing to their success across a range of domains beyond natural language processing. Alongside these developments, the field of electroencephalogram (EEG)

Department of Computer Science and Engineering, Indian Institute of Technology Patna, Bihta, Patna, India, 801106. Email: naseem 2021cs22@iitp.ac.in Department of Computer Science and Engineering, Indian Institute of Technology Patna, Bihta, Patna, India, 801106. Email: jimson@iitp.ac.in Infocomm Technology Cluster, Singapore Institute of Technology, 10 Dover Drive, Singapore 138683 Email: vinod.prasad@singaporetech.edu.sg

[4], [5] based brain signal processing has seen substantial growth, driven by its promising applications in brain-computer interfaces (BCIs) [6], [7], [8], cognitive assessment, mental health monitoring, and neurological diagnostics. The convergence of large language models and EEG signals offers a unique opportunity to bridge artificial intelligence and neuroscience. Leveraging LLMs enables the translation of brain activity into meaningful outputs such as text, images, 3D objects, and diagnostic insights [9], [10], [11], [12], as illustrated in Fig. 1. The acronyms used throughout this paper are summarized in TABLE 1.

### 1.1 EEG and Language Models

Despite recent advancements, EEG signal processing remains highly challenging due to the noisy nature of non-invasive recordings, which are often contaminated by artifacts such as eye movements, muscle activity, and external interference [13], [14], [15]. Additionally, these signals

TABLE 1 Acronyms and abbreviations used in this survey

#### Acronym Full Form

- LLM Large Language Model EEG Electroencephalography BCI Brain-Computer Interface
- MI Motor Imagery BERT Bidirectional Encoder Representations from Transformers BART Bidirectional and Auto-Regressive Transformers GPT Generative Pre-trained Transformer BELT Bridging Electroencephalogram with Language Transformers CET-MAE Contrastive EEG-Text Masked Autoencoder LLaMA Large Language Model Meta AI FLAN-T5 Fine-tuned Language Net T5 LaBraM Large Brain Model EEGPT Electroencephalography Pretrained Transformer LCM Large Cognition Model EEGFormer EEG Transformer Neuro-GPT Neurological Generative Pre-trained Transformer EEG2TEXT Electroencephalogram to Text SEE Semantically Aligned EEG-to-Text Translation EEGTrans Electroencephalogram Transformer ELM EEG-Language Model AdaCT Adapter for Converting Time Series E2T-PTR EEG-to-Text using Pretrained Transferable Representations EEG-CLIP EEG-based Contrastive Language-Image Pretraining HMLLM Hypergraph Multi-modal Large Language Model MLM Masked Language Modeling ALM Autoregressive Language Modeling NLP Natural Language Processing FCM Fuzzy C-Means FJM Fuzzy J-Means

[Figure 1]

[Figure 2]

Text

[Figure 3]

[Figure 4]

Images

3D Objects

Large Language Model (LLM)

EEG Signals

[Figure 5]

Mental Health

- Fig. 1. EEG signals are processed by a large language model that interprets the underlying neural patterns. Depending on the task, the system generates outputs such as text, images, 3D reconstructions, or diagnostic insights.

show inter-subject and intra-subject variability, complicating generalization across individuals and recording sessions [16], [17]. Lack of datasets poses a challenge for effective model training and

evaluation. As a result, many existing machine and deep learning approaches remain confined to single-task, single-dataset settings, limiting their scalability and robustness. To address these challenges, more flexible and scalable learning frameworks are needed, and language models [18], with their ability to capture complex dependencies and adapt across modalities, offer promising capabilities to overcome these limitations.

- • Self-attention for spatiotemporal modeling: The self-attention mechanism in language models enables dynamic weighting of input features and effectively captures long-range dependencies, which are essential for modeling the spatiotemporal dynamics of signals [19], [20], [21].
- • Transformer adaptability to neural signals: The flexibility of the transformer

architecture allows it to effectively handle multichannel, multi-timescale inputs by learning embedding-based representations that capture both spatial and temporal characteristics of signals [22], [23].

• Cross-modal generation capabilities: Combining EEG signals with multimodal language models enables novel applications such as EEG-to-text generation, brain-driven image synthesis, and exploratory 3D reconstruction. These advances expand the possibilities for interpreting and visualizing brain activity [10], [11], [24].

### 1.2 Scope and Contributions

This survey reviews recent advancements combining EEG signal processing and large language models (LLMs), focusing on applications such as EEG-to-text decoding, emotion recognition, multimodal generation, and mental health diagnostics.

The main contributions of this work are as follows:

- 1) Introduces a structured taxonomy covering four domains: foundation models, decoding, cross-modal generation, and clinical applications.
- 2) Summarizes recent studies through comprehensive tables detailing the tasks, datasets, methods, and model types used.
- 3) Highlights how different LLM architectures have been adapted for EEG-related tasks and outlines their roles across various applications.
- 4) Identifies key challenges in this emerging field, including data scarcity, interpretability, and real-time deployment, and outlines directions for future work.

The remainder of this paper is organized

- as follows: Section 2 provides background on electroencephalography (EEG) signals and large language models (LLMs); Section 3 presents a taxonomy of language models applications in EEG analysis; Section 4 outlines model adaptation strategies in EEG analysis; Section 5 gives

a detailed discussion on recent studies; Section 6 discusses future research directions; and Section 7 concludes the paper.

2 BACKGROUND

2.1 Electroencephalography (EEG) Signals

EEG is a non-invasive neuroimaging technique that records electrical activity in the brain with electrodes placed on the scalp [6], [7], [8]. These signals reflect the collective electrical activity of cortical neurons and are captured as voltage fluctuations over time. These signals are inherently multichannel time series, typically sampled at high frequencies (e.g., 128-1024 Hz) across arrays of electrodes arranged according to standardized systems such as the international 10-20 or 1010 montage. Each electrode provides spatially localized insight into cortical function, supporting both region-specific and network-level analyses. These signals are often decomposed into frequency bands: delta (0.5-4 Hz), theta (4-8 Hz), alpha (8-13 Hz), beta (13-30 Hz), and gamma (30-100 Hz) [7], [8], where each band is associated with different cognitive or physiological states. For example, alpha waves are linked to relaxed wakefulness, while beta waves correspond to focused attention and active mental engagement. Despite their versatility, these signals are highly susceptible to various artifacts, such as those arising from eye blinks, facial muscle movements, and environmental interference, making preprocessing and artifact rejection essential before further analysis [13], [14], [15]. EEG is widely used across various domains, including BrainComputer Interfaces (BCIs) [4], [5], [25], where it enables direct communication between the brain and external devices using mental states such as motor imagery [26], [27] or steady-state visual evoked potentials (SSVEPs) [28], [29]; clinical diagnosis of neurological conditions like epilepsy, sleep disorders, and encephalopathies; and applications in cognitive monitoring, emotion recognition, neurofeedback, and neuroergonomics, supporting real-time assessment of mental workload, attention, and affective states in both laboratory and real-world settings.

### 2.2 Large Language Models (LLMs)

LLMs are deep neural architectures designed to model and generate human-like language [18], [21], [30]. The backbone of language models is the transformer architecture, introduced by Vaswani et al. in 2017 [31]. The key innovation in transformers is the self-attention mechanism, which allows the model to assign dynamic importance to different positions in a sequence, thereby capturing both local and global dependencies. Unlike recurrent neural networks, transformers are highly parallelizable and scalable, enabling them to process longer sequences efficiently. Two major pretraining paradigms have emerged in large language models:

- 1) Masked Language Modeling (MLM): This approach involves masking a portion of the input tokens and training the model to predict the masked content using both left and right context. BERT [32], [33] is a well-known example of MLM, leveraging bidirectional modeling to learn rich contextual embeddings that are particularly effective for classification and semantic understanding tasks.
- 2) Autoregressive Language Modeling (ALM): This approach trains a model to predict the next token in a left-to-right sequence, enabling the generation of coherent long-form text. GPT [32] is a prominent example of this method, which is well-suited for applications such as dialogue systems, document completion, and EEG-to-text decoding.

With the continued progress of large language models, there has been a shift toward supporting diverse input modalities and learning objectives. These models have evolved from textonly systems to multimodal frameworks (e.g., Flamingo, LLaVA, GPT-4V) [34], [35] capable of processing combinations of text, images, and audio. Instruction-tuned variants such as FLAN-T5 and ChatGPT demonstrate how prompting can guide them to perform a wide range of tasks with little or no task-specific fine-tuning [36]. This is particularly promising for brain signal analysis, where labeled data is often limited and zero or

few-shot prompting can leverage domain-specific cues. These advancements have extended the role of LLMs beyond traditional language tasks, enabling applications in neural decoding, cognitive state modeling, and multimodal brain-machine interfaces.

## 3 A TAXONOMY OF LLM APPLICATIONS IN EEG ANALYSIS

To provide a clear and structured overview of how large language models are being used in EEG analysis, we present a taxonomy that categorizes recent studies based on their primary objective, methodology, and output modality. The surveyed works are organized into four categories:

- 1) LLM-Inspired EEG Foundation Models: This category includes approaches that adopt transformer-based architectures to learn general-purpose EEG representations that can be transferred across multiple tasks. Inspired by foundation models in natural language processing, these models aim to capture spatiotemporal features through large-scale pretraining. Two primary modeling strategies are commonly used: masked modeling and autoregressive modeling.
- 2) EEG-to-Language Decoding: This category focuses on generating natural language from brain signals. Techniques include decoder-based approaches that use neural embeddings as prompts or inputs to text decoders, semantic alignment methods that map signal representations to language embeddings in a shared space, and instruction-tuned models that leverage prompt-based learning for interpretation with minimal supervision.
- 3) Cross-Modal EEG Generation: This category explores the translation of brain activity into other modalities such as images, text, or 3D objects, enabling richer interpretations of neural signals and supporting applications like brain-to-image synthesis and brain-to-text decoding.

4) Clinical Applications and Dataset Tools: This category encompasses applications such as emotion recognition, mental health diagnostics, and motor imagery classification. It also includes efforts focused on dataset tools and report clustering for automated annotation, as well as cognitive and reading analysis that links brain signals to attention and comprehension levels.

Fig. 2 provides a visual overview of this classification, highlighting the functional contributions of language models in EEG processing and their diverse applications across related tasks. To better understand how language models are being applied to EEG analysis, Fig. 3 illustrates the distribution of existing studies, emphasizing the current focus areas within this emerging field.

## 4 LLM ADAPTATION STRATEGIES IN EEG ANALYSIS

As LLMs find growing use in EEG analysis, various strategies have emerged to adapt them for related tasks. Based on recent studies, these strategies can be categorized into three types: finetuning, few-shot learning, and zero-shot learning.

### 4.1 Fine-Tuning

Fine-tuning is a widely used method for adapting language models to domain-specific tasks. In the context of neural signal analysis, this involves retraining a pretrained LLM using labeled EEG data, enabling the model to learn domainrelevant patterns and perform specialized downstream tasks such as classification, interpretation, or generation [37]. Depending on the available resources and task requirements, fine-tuning can range from updating the entire model to using lightweight methods like prefix tuning. In some cases, only small additional modules are trained while keeping the core LLM unchanged. Despite requiring labeled data and moderate computational effort, fine-tuning remains a powerful and flexible approach for EEG applications. In Thought2Text [9] uses instruction-tuned language models such as LLaMA, Mistral, and Qwen2.5,

which are first fine-tuned on multimodal datasets (e.g., image-text pairs) and then applied to EEG embeddings for generating open-ended textual descriptions. AdaCT [38] introduces a plug-andplay approach using adapters that transform EEG signals into pseudo-text or pseudo-image formats, enabling fine-tuning with pretrained vision or language models. Similarly, BELT-2 [39] adopts prefix tuning, a parameter-efficient strategy where learnable prefix vectors are prepended to LLM layers to align EEG representations with GPT-style decoders for EEG-to-text translation. An illustrative overview of the fine-tuning process, including its integration with EEG inputs, is presented in Fig. 4.

### 4.2 Zero-Shot Learning

Zero-shot learning pushes generalization to the extreme by allowing a pretrained language model to perform tasks without being exposed to any task-specific training examples. Instead, the model is prompted using only natural language instructions or semantic cues [40], [41]. In the context of EEG analysis, this approach enables the transfer of knowledge to new tasks, patients, or datasets without the need for additional labeled data or retraining. Several EEG-based applications have explored this paradigm, like EEGCLIP [42], which aligns time-series data with clinical text reports through contrastive learning, enabling both zero-shot classification and retrieval via a shared embedding space. Similarly, the Video-SME framework [43] incorporates a Hypergraph Multimodal Large Language Model (HMLLM) to jointly interpret EEG and eye-tracking data during video viewing, using zero-shot inference to uncover semantic associations between modalities. Additionally, components of the Mental Health Classifier and Clinical Report Clustering systems [12] apply zeroshot language model reasoning to analyze patient states or group clinical documents, without requiring retraining on those specific target tasks. An overview of the zero-shot learning workflow is illustrated in Fig. 5.

Taxonomy of Large Language Model (LLM) for EEG Signal Analysis

Clinical Applications and Dataset Tools Masked Modeling

LLM-Inspired EEG Foundation Models

EEG-to-Language Decoding

Cross-Modal EEG Generation

Decoder-Based Approach

Emotion Recognition

Motor Imagery Classification

EEG-to-Image

Autoregressive Modeling

Semantic Alignment

Adapter-Based EEG-to-Text

Mental Health Diagnosis

Instruction-Tuned LLMs

Dataset Tools & Report Clustering

Cognitive/ Reading Analysis

- Fig. 2. A taxonomy of large language model applications in EEG signal analysis, organized into four categories: foundation models, language decoding, cross-modal generation, and clinical applications.

| |31<br><br>28|
|---|---|
| |25<br><br>16|
| | |
| | |

PercentageofStudies

0

10

20

30

40

LLM-Inspired EEG Foundation Models

EEG-to-Language Decoding

Cross-Modal EEG Generation

Clinical Applications and Dataset Tools

- Fig. 3. Distribution of EEG-LLM studies across four domains, reflecting current research trends and areas of emphasis in the application of language models to EEG signal analysis.
- 4.3 Few-Shot Learning

[Figure 6]

Fig. 4. Workflow illustrating the fine-tuning of a large language model for EEG analysis. A pretrained LLM is adapted using labeled data to perform domain-specific tasks.

learning has been applied to various tasks involving multimodal data. The Multimodal Mental Health Classifier [12] employs few-shot prompting to perform emotion and depression classification using EEG signals alongside facial and textual features. In this setup, models like GPT4 are prompted with carefully structured example pairs, allowing them to generalize to new, unseen inputs. Similarly, EEG Emotion Copilot [46] applies few-shot style querying during inference to generate adaptive feedback and emotion summaries based on input. Overall, few-shot

Few-shot learning leverages the ability of language models to generalize from a small number of labeled examples embedded in the prompt

- at inference time, through a process known as in-context learning. Unlike fine-tuning, few-shot learning does not involve updating the model’s parameters, making it computationally efficient and particularly suitable for low-resource environments [44], [45]. In EEG analysis, few-shot

[Figure 7]

- Fig. 5. Illustration of a zero-shot approach using a pretrained language model, where unlabeled EEG signals are provided along with a task-specific prompt (e.g., “Are the EEG signals normal or abnormal?”). The model performs inference without task-specific training or examples, directly predicting the outcome based on the prompt.

approaches are highly effective in scenarios with limited labeled data or when rapid prototyping is needed without the overhead of full model retraining. A schematic representation of the fewshot learning is provided in Fig. 6.

[Figure 8]

- Fig. 6. Illustration of few-shot learning for emotion classification using a pretrained large language model. A small support set with labeled samples from three emotion classes, positive, neutral, and negative, is included incontext prompt. The model receives unlabeled query samples and infers their emotion class by reasoning over the support set, producing a probability distribution across the three categories.

## 5 EEG LLM BASED STUDIES

To illustrate the proposed taxonomy, this section reviews recent studies that integrate LLMs into EEG signal processing across various tasks,

including emotion recognition, motor imagery, EEG-to-text translation, and clinical reporting. Despite differences in architecture and data requirements, these works demonstrate how language models enhance EEG data analysis and generation tasks. TABLE 2 provides a structured overview, summarizing each study by model or paper name, the integration of these models, their role (e.g., decoding, alignment, generation), and the broader task category. Figures 7 and 8 further visualize the models and their applications across these tasks.

5.1 LLM-Inspired Foundation Models for EEG Foundation models are trained on large-scale datasets using self-supervised learning objectives, such as masked modeling and autoregressive prediction. These models are designed to learn general-purpose, transferable representations that can support a variety of downstream tasks, including emotion recognition, abnormality detection, and cognitive state classification.

- 5.1.1 Masked Pretraining (BERT-Style)

Inspired by BERT’s masked language modeling strategy, several EEG foundation models adopt similar self-supervised approaches by learning to reconstruct masked segments of input signals. EEGFormer applies masked token prediction over spatiotemporal patches using a transformer architecture [66], while LaBraM [60] segments signals into channel-wise patches and employs a vector-quantized tokenizer to enable generalization across datasets. EEGPT [62] introduces electrode-wise masked modeling, and LCM [61] enhances this framework by incorporating both temporal and spectral attention during large-scale pretraining.

- 5.1.2 Autoregressive Pretraining (GPT-style)

Inspired by GPT’s autoregressive modeling, which involves predicting the next token in a sequence, several models have adopted next-step prediction frameworks to capture temporal dependencies in brain signals. EEGPT includes an autoregressive variant that discretizes inputs and predicts future tokenized segments sequentially

Gemma-3-1b

Mistral-7B-v0.3

BART (Decoder)

Meditron-7B

BioMistral

Mistral

BART

Meditron BioMistral

Gemma

GPT Family BERT Family

LLaMA Series

Qwen Family

Other

- LlaMA-2

- LlaMA-3

EEGUnity

GPT-o1

Qwen2.5

BERT

- GPT-3.5

- GPT-3.5 turbo

- GPT-4

- GPT-4o

Qwen2-0.5B

ClinicalBERT

- LlaMA-2-7B

- LlaMA-3.1-8B

Qwen2.5-7B

Neuro-GPT

- Fig. 7. Summary of large language models (LLMs) used in EEG studies.

[68]. Similarly, Neuro-GPT [64] combines a pretrained EEG encoder with a GPT-style decoder for masked segment reconstruction, showing strong performance in low-data scenarios such as motor imagery classification. These models are particularly effective in tasks requiring temporal reasoning, including sequence prediction and classification under limited supervision.

Generating synthetic data is increasingly used to address challenges such as data scarcity, domain generalization, and class imbalance. While GAN-based methods have been popular [98], [99], [100], they often suffer from training instability and limited temporal precision. Recent transformer-based approaches, inspired by LLMs, provide a more stable alternative [101], [102]. EEGTrans [67] applies a GPT-style transformer to generate discrete EEG sequences by first compressing raw signals with a quantized autoencoder, then learning temporal patterns autoregressively. This method produces high-fidelity synthetic EEG that preserves spectral and sequential characteristics, and has been shown to improve motor imagery classification performance while outperforming GAN-based baselines in signal quality and downstream accuracy.

### 5.2 EEG-to-Language Decoding

A particularly promising application of LLMs in EEG analysis is the decoding of brain activity into natural language. Recent models achieve this by coupling EEG encoders with pretrained language decoders such as BART and GPT, enabling both fixed and open-vocabulary text generation [49]. Notable examples include BELT-2 [39], CET-MAE [54], and Thought2Text [24], which incorporate techniques like instruction tuning and semantic alignment to enhance the fluency and contextual relevance of the generated text. These models significantly advance EEG-to-text translation and offer strong potential for real-world braincomputer interface (BCI) systems that facilitate communication through neural signals.

5.2.1 Decoder-Based Approaches

Decoder-based EEG-to-text models typically pair a neural EEG encoder with a pretrained language decoder such as BART or GPT, allowing the model to generate natural language conditioned on brain activity. This modular design leverages the linguistic strength of LLMs while grounding them in neural representations. For

EEG Foundation Model [Y. Chen et al., 2024] ⚙ EEGFormer (transformer based) 🎯Masked modeling for representation learning

Foundation Model (Autoregressive) [T Yue et al., 2024] ⚙ EEGPT: Autoregressive token prediction 🎯Sequence modeling across EEG tasks

AutoregressiveModeling

⚙ LLM used 🎯Purpose

Foundation Model for EEG [W. B. Jiang et al., 2025] ⚙ LaBraM (Large Brain Model) 🎯Cross-dataset pretraining

Developing a Foundation Model [W. Cui et al., 2023] ⚙ Neuro-GPT (GPT-style decoder) 🎯Masked reconstruction & classification

MaskedModeling

LLM-InspiredFoundation

Representation of EEG Signals [G. Wang et al., 2024] ⚙ EEGPT + Masked modeling with electrode-wise input 🎯Universal EEG encoder

EEG Synthesis Model [J. H. Lim et al., 2025] ⚙ EEGTrans (Transformer-driven generative model) 🎯Synthetic EEG generation

EEG-to-LanguageDecodingModelsforEEG ClinicalApplicationsand

EEG Foundation Model [C. S. Chen et al., 2025] ⚙ LCM (Large Cognition Model), BERT style 🎯General EEG representation learning

SEE (EEG2Text) [Y. Tao et al., 2025] ⚙ BART + cross-modal codebook 🎯Semantic alignment of EEG-text

Alignment Instruction-Tuned

Semantic

EEG-to-Language [J. Zhou et al., 2024] ⚙ BELT-2 (EEG encoder + LLM decoder) 🎯Sentence decoding from EEG

DeWave [Y. Duan et al., 2024] ⚙ BART + contrastive training 🎯EEG-to-text without markers

Decoder-Based

LLMsforEEGSignals

Approaches

CET-MAE + E2T-PTR [J. Wang et al., 2024] ⚙ Dual encoder + BART decoder 🎯Self-supervised EEG-to-text

Analysis

Thought2Text [A. Mishra et al., 2024] ⚙ LlaMA-v3 + Mistral-v0.3 + Qwen2.5 🎯Open vocabulary EEG-to-text

LLMs

Neural Decoding [D. H. Lee et al., 2024] ⚙ GPT-3.5 turbo 🎯Interpretive EEG descriptions

EEG2TEXT [H. Liu et al., 2024] ⚙ Pretrained EEG encoder + transformer 🎯Open vocabulary text decoding

EEG-to-Image [A. Liua et al., 2024] ⚙ LLaMA-2 embeddings + diffusion 🎯EEG-guided visual reconstruction

Adapter-Based

EEG-to-Text

EEG-to-Image

AdaCT [B. Wang et al., 2023] ⚙ Adapter for ViT/LLM fine-tuning 🎯EEG → pseudo-image or text representation

Cross-ModelEEG

Generation

EEG-to-3D Object [X. Deng et al., 2025] ⚙ Mistral-7B-v0.3 + 3D Gaussian generator 🎯Coarse 3D shape reconstruction from EEG

Motor Imagery Classification [D. H. Lim et al., 2024] ⚙ LLM fine-tuned (GPT-4o) on MI task 🎯EEG classification vs SVM/MLP baselines

MotorImagery

Classification Cognitiveand

PAWS [S. Yao et al., 2024] ⚙ Semi-supervised + LlaMA-2-7B 🎯Emotion classification with limited data

Reading Comprehension Decoder [Y. Zhang et al., 2024] ⚙ EEG + eye-tracking + BERT 🎯Relevance of words during reading

DatasetTools

Recognition MentalHealth

Emotion

ReadingAnalysis DatasetToolsand

EEG Emotion Copilot [H. Chen et al., 2024] ⚙ Qwen2-0.5B (local deployment) 🎯Real-time emotion classification + feedback

Semantic Relevance Decoder [Y. Zhang et al., 2023] ⚙ EEG + word relevance + GPT-3.5 & 4 + LlaMA 🎯Reading-based semantic classification

Video-SME (HMLLM) [M. Wu et al., 2024] ⚙ Hypergraph LLM 🎯EEG + eye tracking for media interpretation

Multimodal Mental Health Classifier [Y. Hu et al., 2024] ⚙ EEG + audio + visual + GPT-4o based few-shot 🎯Depression/ emotion detection

Diagnosis

Schizophrenia Detection [M. Guerra et al., 2024] ⚙ GPT-4 + GPT-o1 🎯EEG-based diagnosis

EEGUnity [C. Qin et al., 2025] ⚙ LLM-assisted parsing + harmonization 🎯EEG dataset correction + standardization

ReportClustering

Sleep-Attention Feedback Model [A. Sano et al., 2024] ⚙ GPT-3.5 turbo + GPT-4 + script generator 🎯Wellness suggestions from EEG + activity

ClinicalBERT Clustering [C. Zhao et al., 2025] ⚙ ClinicalBERT + Meditron + BioMistral 🎯Report clustering (normal/abnormal)

- Fig. 8. A hierarchical taxonomy of LLM-based EEG analysis, structured according to primary application domains. Each entry provides the model or paper name, approximate publication year, type of large language model, purpose, and task.

instance, BELT-2 [39] uses prefix tuning to connect an EEG encoder to a GPT-style decoder, aligning EEG embeddings with linguistic tokens. CETMAE [54] incorporates a dual-stream encoder and

a BART decoder trained with multi-modal selfsupervised objectives. Other approaches utilize general-purpose models like GPT-3.5 to generate interpretable descriptions of EEG activity [55].

This table provides a comprehensive overview of recent studies that integrate Large Language Models (LLMs) with Electroencephalography (EEG) signals across multiple domains. The table reports the model name, the use of LLMs and EEG data, the model’s primary role, and the broader classification of each study.

|Model Paper<br><br>|LLMs Used<br><br>|EEG Used<br><br>|LLM Purpose|Category|
|---|---|---|---|---|
|PAWS [47]|Yes<br><br>|Yes|Enhancing feature representation for semisupervised emotion recognition for EEG data<br><br>|Emotion Recognition with LLM|
|BELT-2 [39]|Yes<br><br>|Yes<br><br>|Uses prefix tuning to align EEG embeddings with GPT for EEG-to-text generation|LLM-Based EEG-to-Language Decoding|
|GPT-4o [48]<br><br>|Yes|Yes<br><br>|Fine-tunes LLM for motor imagery and compares it to traditional classifiers|Cognitive and Motor State Classification|
|BART+GPT-4 [49]<br><br>|Yes|Yes|Subject-dependent representation for openvocabulary sentence generation and refinement|EEG-to-Language Decoding with Hybrid LLM Architecture<br><br>|
|BART [50]<br><br>|Yes<br><br>|Yes|Quantized variational encoder and contrastive training to align EEG tokens with BART|EEG-to-Text Generation via Discrete Contrastive Alignment|
|Qwen2-0.5B [46]<br><br>|Yes|Yes|Real-time emotion recognition and generates diagnostic feedback with prompt tuning<br><br>|Emotion Recognition and Clinical Text Generation|
|BERT [42]|Implicit<br><br>|Yes<br><br>|Contrastive learning of shared EEG-text embeddings for few-shot and zero-shot classification|Multimodal EEG Text Alignment with Contrastive Learning<br><br>|
|EEG-GPT [51]<br><br>|Yes|Yes<br><br>|Few-shot interpretable abnormality classification|Interpretable EEG Classification|
|ELM [52]<br><br>|Yes<br><br>|Yes<br><br>|EEG+text for pathology detection with multimodals|EEG for Clinical Pathology|
|EEGUnity [53]|Yes<br><br>|Yes<br><br>|Uses an LLM Boost module for metadata harmonization, structure inference, and label standardization across EEG datasets|EEG Dataset Management and Preprocessing with LLM Assistance|
|BART [54]<br><br>|Yes|Yes<br><br>|Contrastive EEG-text learning + BART decoder|EEG-to-Language Decoding|
|GPT-3.5 [55]<br><br>|Yes|Yes<br><br>|Interpretive neural decoding using GPT<br><br>|Neural Decoding|
|GPT-3.5turbo [56]<br><br>|Yes<br><br>|Yes<br><br>|Wellness feedback, guided imagery via LLM|Behavioral Analysis|
|GPT-4o [12]<br><br>|Yes<br><br>|Yes|Multimodal Depression/emotion prediction|Mental Health Assessment|
|GPT-(4, o1) [57]<br><br>|Yes<br><br>|Yes<br><br>|Schizophrenia Detection through EEG Analysis|Mental Health Diagnosis|
|LLaMA-2 [10]<br><br>|Yes<br><br>|Yes|Visual decoding with semantic alignment<br><br>|EEG-to-Image Visual Decoding|
|BERT [58]|Yes<br><br>|Yes<br><br>|EEG+eye-tracking comprehension prediction|EEG Reading Analysis|
|HMLLM [43]<br><br>|Yes|Yes|Video content analysis with EEG + eye-tracking|Multimodal Cognitive EEG|
|GPT+LlaMA [59]|Yes<br><br>|Yes<br><br>|Word-level semantic relevance prediction during reading using EEG and eye-tracking data|LLM-Guided EEG Semantic Decoding<br><br>|
|LaBraM [60]<br><br>|LLMstyle<br><br>|Yes<br><br>|Channel-wise patches, trains a vector-quantized transformer model for cross-dataset generalization|LLM-Inspired Foundation Models for EEG|
|LCM [61]<br><br>|LLMstyle|Yes<br><br>|Spectral-temporal attention mechanisms, generalization across multiple EEG datasets and tasks|LLM-Inspired Foundation Models for EEG|
|EEGPT [62]|LLMstyle<br><br>|Yes<br><br>|Masked spatio-temporal modeling with electrodewise inputs, generalizable EEG representation<br><br>|LLM-Inspired Foundation Models for EEG|
|AdaCT [38]<br><br>|Yes|Yes<br><br>|EEG into pseudo-image or text form for fine-tuning pretrained vision and language transformers<br><br>|Adapter-Based LLM Transfer Learning for EEG|
|ClinicalBERT [63]|Yes|Text<br><br>|EEG Report clustering with clinical LLM<br><br>|EEG Report Analysis|
|Mistral-7B [11]<br><br>|Yes<br><br>|Yes<br><br>|Gaussian-based generative 3D object modeling|EEG-to-3D Object construction|
|Neuro-GPT [64]|Yes<br><br>|Yes|Masked segment reconstruction and generalization in low-data motor imagery tasks|Hybrid EEG Foundation Architectures|
|Transformer [24]|Yes<br><br>|Yes|Open vocabulary EEG-to-text via pretraining|EEG-to-Text Generation|
|BART [65]<br><br>|Yes<br><br>|Yes|Cross-modal codebook + semantic alignment|EEG-to-Text|
|Multimodals [9]<br><br>|Yes|Yes<br><br>|Instruction-tuned LLaMA, Mistral, and Qwen used|EEG-to-Text<br><br>|
|EEGFormer [66]|LLMstyle<br><br>|Yes<br><br>|Self-supervised transformer for universal EEG representations<br><br>|LLM-Inspired Foundation Models|
|EEGTrans [67]<br><br>|LLMstyle|Yes|Autoregressive EEG signal generator using transformer decoder<br><br>|LLM-Inspired Generative Models for Synthetic EEG|
|EEGPT [68]<br><br>|LLMstyle|Yes<br><br>|Next-signal prediction with 1.1B model for multitask EEG<br><br>|LLM-Style Foundation Models|

- 5.2.2 Instruction-Tuned LLMs

Instruction-tuned large language models enable open-vocabulary decoding, allowing the gen-

eration of free-form text from neural activity instead of limiting output to predefined classes. Thought2Text [9] fine-tunes instruction-

EEG Datasets used in the LLM-Based Studies

|Datasets|Papers<br><br>|Purpose / Task|
|---|---|---|
|SEED [69], SEED-IV [70]|[47] (PAWS)|Emotion recognition<br><br>|
|ZuCo [71]|[39] (BELT-2), [50] (DeWave), [54] (CET-MAE), [24] (EEG2TEXT), [65] (SEE), [9] (Thought2Text)|EEG-to-text translation, semantic relevance decoding|
|ImageNet-EEG [72], [73]|[10] (EEG-to-Image), [11] (EEGto-3D Generation)<br><br>|Cross-modal visual and 3D generation|
|LMSU ScZ [74]<br><br>|[57] (LLM for Schizophrenia Detection)<br><br>|Schizophrenia classification|
|Sleep-EDF [75]|[56] (Sleep-Attention Feedback Model), [38] (AdaCT)<br><br>|Sleep staging, EEG + activity data for wellness analysis|
|BCI competition III [76]<br><br>|[48] (Motor Imagery tasks)<br><br>|Classification of non-invasive EEG signals during Motor Imagery tasks using a Large Language Model|
|The Temple University Hospital EEG corpus (TUEG) [77]|[42] (Learning EEG representations), [51] (EEG-GPT: MODELS FOR EEG CLASSIFICATION), [66] (EEGFormer: Foundation Model)|Learning EEG representations from natural language descriptions|
|TUEG [77], TUAB [78], NMT [79], TUSZ [80]<br><br>|[52] (Learning EEG representations), [51] (EEG-Language modeling)<br><br>|EEG-language modeling for pathology detection|
|ZuCo 1.0 [81]<br><br>|[49] (EEG-to-Text), [58], [59] (Reading comprehension)<br><br>|EET-to-text and reading analysis|
|SRI-ADV [43]<br><br>|[43] (Hypergraph Multi-modal)|EEG and Eye-tracking Modalities to Evaluate Heterogeneous Responses for Video Understanding|
|TUAB, TUEV [77]|[60] (Learning generic representation)|Large Brain Model for learning generic representation with tremendous EEG data in BCI<br><br>|
|PhysioMI [82], TSU [83], SEED [69], BCIC-2A [84], BCIC-2B [85]<br><br>|[61] (EEG Foundation Model)|Large Cognition Model: Towards Pretrained Electroencephalography (EEG) Foundation Model<br><br>|
|PhysioMI [82], HGD [86], TSU [83], SEED [69], M3CV [87], BCIC-2A [84], BCIC-2B [85], Sleep-EDFx [75], KaggleERN [88], PhysioP300 [89], TUAB, TUEV [77]<br><br>|[62] (Reliable Representation of EEG signals)|Pretrained Transformer for Universal and Reliable Representation of EEG Signals|
|BCI Competition [84], HGD [86]<br><br>|[67] (Generative models for EEG synthesis)<br><br>|EEGTRANS: Transformer-driven generative models for EEG synthesis|
|DEAP [90], FACED [91], SEED-IV [70], SEED-V [92], MIBCI [93], EEGMat [94], STEW [95], HMC [96], IMG [68], SPE [97]<br><br>|[68] (Foundation model)|Unleashing the potential of EEG generalist foundation model by autoregressive pre-training|

optimized models such as LLaMA-V3, Mistral, and Qwen2.5 to produce descriptive text from EEG embeddings recorded during visual stimulus tasks. Its training pipeline involves three stages: EEG encoding, multimodal alignment using vision-language data, and EEG-to-text decoding. Similarly, EEG2TEXT [24] introduces a brainto-text framework that incorporates enhanced pretraining and a multi-view transformer to enable open-ended text generation.

5.2.3 Semantic Alignment

Recent models aim to improve EEG-to-text translation by aligning neural features with textual embeddings in a shared semantic space. DeWave [50] employs a quantized variational encoder to generate discrete codes, which are aligned with language representations through contrastive training. SEE [65] introduces a semantic matching module that maps signal features into a shared latent space with text using precomputed embeddings, while addressing false nega-

tives during training. These approaches focus on reducing the modality gap between brain signals and language by learning semantically consistent representations, thereby enhancing the coherence of the generated text.

### 5.3 Cross-Modal EEG Generation

Recent work has explored translating neural signals into other modalities such as visual scenes and 3D objects. These approaches integrate brain representations into generative pipelines, such as diffusion models and Gaussian frameworks, guided by embeddings derived from large language models (LLMs) [10], [11].

- 5.3.1 EEG-to-Image Generation

EEG-to-image generation utilizes LLaMA-2 as a semantic scaffold [10]. In this framework, brain signals are first encoded into latent features aligned with image captions. LLaMA-2 then processes these to extract high-level semantic embeddings that guide the subsequent image synthesis. These embeddings condition a pretrained diffusion model that fuses them with signal-derived visual features to synthesize images capturing both the original stimulus’s structural layout and semantic content. Similarly, EEG-to-3D object reconstruction has been achieved using language models as semantic intermediaries [11]. In this method, a neural encoder extracts spatiotemporal features, which a fine-tuned LLM interprets to produce semantic embeddings. These guide a 3D Gaussian-based generator to reconstruct object geometry and layout. Although the generated models remain coarse, they reflect the conceptual form of the perceived or imagined object.

- 5.3.2 Adapter-Based EEG-to-Text

AdaCT [38] introduces an adapter-based framework that enables flexible integration of EEG signals with both language and vision models. It features two plug-and-play modules: AdaCT-T, which converts short EEG segments into textual representations for fine-tuning language transformers; and AdaCT-I, which transforms longer sequences into 2D pseudo-images compatible

with vision transformers. This dual-pathway design allows the system to adapt large language models and vision transformers (ViTs) for EEG decoding across modalities.

### 5.4 Clinical Applications and Dataset Tools

LLMs are increasingly being explored in clinical and affective computing contexts, enabling tasks such as emotion recognition, mental health monitoring, diagnostic report generation, and decision support. These models enhance the interpretability of brain signals and support more personalized, multimodal analysis of cognitive and emotional states. In parallel, they are also applied to EEG data management and augmentation, such as generating synthetic samples to improve model generalization, parsing and organizing large-scale datasets, and assisting with data cleaning and clustering. Semantic alignment techniques have further enabled the embedding of neural signals and clinical text into a shared space, supporting zero-shot and few-shot inference.

- 5.4.1 Emotion Recognition Emotion recognition in low-resource settings remains a key challenge. To address this, [47] proposes a semi-supervised framework that combines LLM-driven feature extraction with mixupbased data augmentation to boost performance when labeled data is scarce. Another system, EEG Emotion Copilot, employs a lightweight 0.5Bparameter LLM capable of real-time classification and personalized feedback generation [46]. Designed for efficient on-device inference, it incorporates prompt learning, model pruning, and fine-tuning strategies. Beyond recognizing emotional states, the copilot also generates diagnostic summaries and treatment suggestions, supporting automated clinical documentation.
- 5.4.2 Mental Health Diagnosis Mental health is a prime concern at present, and large language models are increasingly being explored for multimodal diagnostics. One line of work focuses on classifying depression and emotional states by integrating EEG signals with additional inputs such as facial expressions, audio,

- and behavioral data [12]. These systems often employ zero-shot or few-shot prompting to generalize across mental health tasks without extensive retraining. In a related study, GPT-4 and GPT01 were applied to classify schizophrenia from EEG recordings, producing interpretable outputs that align with established clinical patterns [57]. Another model, the Sleep-Attention Feedback Model, fuses EEG and physical activity data to estimate attention states and sleep stages, using LLMs to generate personalized wellness guidance and adaptive imagery scripts [56]. While performance may be constrained by limited labeled data, these efforts highlight the potential of LLMs in supporting both clinical and non-clinical applications for cognitive and emotional health.
- 5.4.3 Motor Imagery Classification Motor imagery (MI) classification has emerged as a promising application of language models in EEG analysis. One study explores a fine-tuned LLM-based classifier that processes these signals recorded during MI tasks, demonstrating performance comparable to or exceeding traditional models such as Support Vector Machines, Random Forests, and Multi-Layer Perceptrons [48]. In a related approach, Neuro-GPT [64] introduces a hybrid framework that combines a pretrained EEG encoder with a GPT-style decoder for masked segment reconstruction. Evaluated under low-data conditions, the model shows strong potential for subject-generalization with minimal supervision, highlighting the advantages of transformer-based architectures in MI decoding.
- 5.4.4 Cognitive and Reading Analysis Analyzing cognitive states during reading and video interpretation has become a key focus in LLM-guided EEG research. The Reading Comprehension Decoder [58] combines EEG and eyetracking data using an attention-based transformer encoder guided by word-level embeddings from a pretrained BERT model. It predicts the relevance of each word to a target inference keyword, achieving over 68% accuracy across multiple subjects. Complementarily, the Semantic Relevance Decoder [59] demonstrates that EEG signals alone can classify word-level

understanding, highlighting the feasibility of decoding comprehension without additional modalities. Extending beyond reading, the Video-SME dataset [43] investigates subjective video interpretation by capturing EEG and gaze data across diverse participants. A Hypergraph Multimodal LLM (HMLLM) is used to model semantic relationships among brain signals, gaze behavior, and video content, supporting deeper insights into cognitive and perceptual processing.

5.4.5 Dataset Tools and Report Clustering

Beyond decoding and classification, LLMs are increasingly used for managing, interpreting, and standardizing EEG datasets and clinical reports crucial tasks given the field’s challenges with data heterogeneity, inconsistent formatting, and weak alignment between signals and annotations. Language models pretrained on biomedical corpora offer strong capabilities for automating the parsing, structuring, and semantic organization of such data [53], [63]. A notable example is EEGUnity, an open-source framework that streamlines preprocessing across diverse sources [53]. It features modules for raw file parsing, inconsistency correction, and batch processing, alongside an LLM Boost component that infers intelligent data structures, harmonizes metadata, and standardizes annotations. Evaluated on 25 public datasets, EEGUnity demonstrates robust performance in handling varied channel layouts, sampling rates, and labeling schemes, addressing fragmentation that often hinders large-scale analysis. Semantic clustering and joint learning approaches are reshaping how EEG reports and signals are interpreted using language models, like ClinicalBERT, Meditron-7B, and BioMistral have been used to group patients into diagnostic categories such as normal and abnormal [63], with fuzzy clustering methods (e.g., Fuzzy C-Means, Fuzzy J-Means) supporting soft label assignments to handle clinical ambiguity. For low-resource scenarios, EEGGPT [51] applies a few-shot transformer trained with just 2% labeled data, achieving performance comparable to fully supervised models while offering interpretable, step-by-step reasoning. EEGLanguage Model (ELM) [52] further advances this space by jointly learning from EEG signals

and their associated clinical reports using timeseries cropping, text segmentation, and multiple instance learning. ELM supports both classification and retrieval, enabling bidirectional querying between neural data and medical documentation.

## 6 FUTURE DIRECTIONS

While significant progress has been made in applying language models to EEG tasks, some challenges still need to be addressed to further enhance brain signal interpretation and enable real-world applications..

- • Real-Time and Low-Latency Inference: Achieving real-time performance is essential for neurofeedback and assistive communication applications. This requires exploring model compression techniquesquantization, knowledge distillation, and dynamic attention to support efficient, low-latency streaming inference.
- • Personalized and Adaptive Models: Due to the high inter-subject variability in EEG signals, personalization is essential for achieving reliable performance. Techniques such as continual learning, metalearning, and federated fine-tuning can enable models to adapt to individual users over time, thereby improving both accuracy and user trust.
- • Multilingual and Multimodal Interfaces: While EEG-based systems have traditionally focused on monolingual and unimodal processing, the emergence of multimodal large language models (LLMs) presents new opportunities to advance brain computer interaction. These include inner speech decoding from EEG, crosslingual emotion recognition, and the integration of EEG with complementary biosignals such as eye tracking, facial expressions, and audio, enabling more robust and context-aware interpretation of brain activity.
- • Interpretability and Clinical Validation: Despite the strong performance of LLMs, they function as black boxes, limiting their adoption in clinical settings. To address

this limitation, explainable AI techniques, including attention maps, saliency visualizations, and natural language rationales, should be emphasized to enhance transparency and support clinical decisionmaking.

## 7 CONCLUSION

This work presents a comprehensive survey of recent studies employing large language models (LLMs) in conjunction with EEG signal processing. The reviewed works are systematically categorized into four major domains: (1) LLMinspired foundation models for EEG analysis, (2) EEG-to-language decoding, (3) cross-modal generation, including image and 3D object synthesis, and (4) clinical applications and dataset management tools, encompassing emotion recognition, mental health analysis, and clinical report interpretation. To unify these developments, a structured taxonomy is proposed, highlighting the application areas, utilized models, and the specific roles of these models. Furthermore, various adaptation strategies are examined, including finetuning, zero-shot learning, and few-shot learning. Finally, the survey discussed current limitations and outlined future directions.

## REFERENCES

- [1] B. Ghojogh and A. Ghodsi, “Attention Mechanism, Transformers, BERT, and GPT: Tutorial and Survey,” Dec. 2020, working paper or preprint. [Online]. Available: https://hal.science/hal-04637647
- [2] M. V. Koroteev, “Bert: a review of applications in natural language processing and understanding,” arXiv preprint arXiv:2103.11943, 2021.
- [3] G. Jawahar, B. Sagot, and D. Seddah, “What does BERT learn about the structure of language?” in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, A. Korhonen, D. Traum, and L. M`arquez, Eds. Florence, Italy: Association for Computational Linguistics, Jul. 2019, pp. 3651–3657. [Online]. Available: https://aclanthology.org/P19-1356/
- [4] L. F. Nicolas-Alonso and J. Gomez-Gil, “Brain computer interfaces, a review,” Sensors, vol. 12, no. 2, pp. 1211–1279, Jan 2012.

- [5] J. Wolpaw, N. Birbaumer, W. Heetderks, D. McFarland, P. Peckham, G. Schalk, E. Donchin, L. Quatrano, C. Robinson, and T. Vaughan, “Braincomputer interface technology: a review of the first international meeting,” IEEE Transactions on Rehabilitation Engineering, vol. 8, no. 2, pp. 164–173, 2000.
- [6] D. P. Subha, P. K. Joseph, U. R. Acharya, and C. M. Lim, “Eeg signal analysis: a survey,” Journal of Medical Systems, vol. 34, no. 2, pp. 195–212, Apr 2010.
- [7] J. S. Kumar and P. Bhuvaneswari, “Analysis of electroencephalography (eeg) signals and its categorization–a study,” Procedia Engineering, vol. 38, pp. 2525–2536, 2012, iNTERNATIONAL CONFERENCE ON MODELLING OPTIMIZATION AND COMPUTING. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S1877705812022114
- [8] D. P. Subha, P. K. Joseph, R. Acharya U, and C. M. Lim, “Eeg signal analysis: a survey,” Journal of medical systems, vol. 34, pp. 195–212, 2010.
- [9] A. Mishra, S. Shukla, J. Torres, J. Gwizdka, and S. Roychowdhury, “Thought2text: Text generation from eeg signal using large language models (llms),” arXiv preprint arXiv:2410.07507, 2024.
- [10] A. Liu, H. Jing, Y. Liu, Y. Ma, and N. Zheng, “Hidden states in llms improve eeg representation learning and visual decoding,” vol. 392, pp. 2130–2137, 2024.
- [11] X. Deng, S. Chen, J. Zhou, and L. Li, “Mind2matter: Creating 3d models from eeg signals,” arXiv preprint arXiv:2504.11936, 2025.
- [12] Y. Hu, S. Zhang, T. Dang, H. Jia, F. D. Salim, W. Hu, and A. J. Quigley, “Exploring large-scale language models to evaluate eeg-based multimodal data for mental health,” in Companion of the 2024 on ACM International Joint Conference on Pervasive and Ubiquitous Computing, 2024, pp. 412–417.
- [13] J. A. Uriguen¨ and B. Garcia-Zapirain, “Eeg artifact removal—state-of-the-art and guidelines,” Journal of Neural Engineering, vol. 12, no. 3, p. 031001, apr 2015. [Online]. Available: https: //dx.doi.org/10.1088/1741-2560/12/3/031001
- [14] M. M. N. Mannan, M. A. Kamran, and M. Y. Jeong, “Identification and removal of physiological artifacts from electroencephalogram signals: A review,” IEEE Access, vol. 6, pp. 30630–30652, 2018.
- [15] X. Jiang, G.-B. Bian, and Z. Tian, “Removal of artifacts from eeg signals: A review,” Sensors, vol. 19, no. 5, 2019. [Online]. Available: https: //www.mdpi.com/1424-8220/19/5/987
- [16] G. Huang, Z. Zhao, S. Zhang, Z. Hu, J. Fan, M. Fu, J. Chen, Y. Xiao, J. Wang, and G. Dan, “Discrepancy between inter- and intra-subject variability in eeg-based motor imagery brain-computer interface: Evidence from multiple perspectives,” Frontiers in Neuroscience, vol. Volume 17 - 2023, 2023. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2023.1122661
- [17] S. Saha and M. Baumert, “Intra- and inter-subject variability in eeg-based sensorimotor brain computer interface: A review,” Frontiers in Computational Neuroscience, vol. Volume 13 - 2019,

- 2020. [Online]. Available: https://www.frontiersin. org/journals/computational-neuroscience/articles/ 10.3389/fncom.2019.00087
- [18] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi, C. Wang, Y. Wang, W. Ye, Y. Zhang, Y. Chang, P. S. Yu, Q. Yang, and X. Xie, “A survey on evaluation of large language models,” ACM Trans. Intell. Syst. Technol., vol. 15, no. 3, Mar. 2024. [Online]. Available: https://doi.org/10.1145/3641289
- [19] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” p. 6000–6010, 2017.
- [20] T. Shen, R. Jin, Y. Huang, C. Liu, W. Dong, Z. Guo, X. Wu, Y. Liu, and D. Xiong, “Large language model alignment: A survey,” arXiv preprint arXiv:2309.15025, 2023.
- [21] Y. Wang, W. Zhong, L. Li, F. Mi, X. Zeng, W. Huang, L. Shang, X. Jiang, and Q. Liu, “Aligning large language models with human: A survey,” arXiv preprint arXiv:2307.12966, 2023.
- [22] Z. Wan, M. Li, S. Liu, J. Huang, H. Tan, and W. Duan, “Eegformer: A transformer–based brain activity classification method using eeg signal,” Frontiers in Neuroscience, vol. Volume 17 - 2023, 2023. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2023.1148855
- [23] Z. Wang, Y. Wang, C. Hu, Z. Yin, and Y. Song, “Transformers for eeg-based emotion recognition: A hierarchical spatial information learning model,” IEEE Sensors Journal, vol. 22, no. 5, pp. 4359–4368, 2022.
- [24] H. Liu, D. Hajialigol, B. Antony, A. Han, and X. Wang, “Eeg2text: Open vocabulary eeg-to-text decoding with eeg pre-training and multi-view transformer,” arXiv preprint arXiv:2405.02165, 2024.
- [25] U. Chaudhary, N. Birbaumer, and A. RamosMurguialday, “Brain–computer interfaces for communication and rehabilitation,” Nature Reviews Neurology, vol. 12, no. 9, pp. 513–525, 2016.
- [26] M. Hamedi, S.-H. Salleh, and A. M. Noor, “Electroencephalographic motor imagery brain connectivity analysis for bci: A review,” Neural Computation, vol. 28, no. 6, pp. 999–1041, 06 2016. [Online]. Available: https://doi.org/10.1162/NECO a 00838

- [27] M. Ahn and S. C. Jun, “Performance variation in motor imagery brain–computer interface: A brief review,” Journal of Neuroscience Methods, vol. 243, pp. 103–110, 2015. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S0165027015000400
- [28] F.-B. Vialatte, M. Maurice, J. Dauwels, and A. Cichocki, “Steady-state visually evoked potentials: Focus on essential paradigms and future perspectives,” Progress in Neurobiology, vol. 90, no. 4, pp. 418–438, 2010. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S0301008209001853
- [29] G. R. Muller-Putz,¨ R. Scherer, C. Brauneis, and G. Pfurtscheller, “Steady-state visual evoked potential (ssvep)-based communication: impact of harmonic frequency components,”

- Journal of Neural Engineering, vol. 2, no. 4, p. 123, oct 2005. [Online]. Available: https://dx.doi.org/10.1088/1741-2560/2/4/008
- [30] Z. Liang, Y. Xu, Y. Hong, P. Shang, Q. Wang, Q. Fu, and K. Liu, “A survey of multimodel large language models,” in Proceedings of the 3rd International Conference on Computer, Artificial Intelligence and Control Engineering, ser. CAICE ’24. New York, NY, USA: Association for Computing Machinery, 2024, p. 405–409. [Online]. Available: https://doi.org/10.1145/3672758.3672824
- [31] N. Parmar, A. Vaswani, J. Uszkoreit, L. Kaiser, N. Shazeer, and A. Ku, “Image transformer,” CoRR, vol. abs/1802.05751, 2018. [Online]. Available: http://arxiv.org/abs/1802.05751
- [32] X. Han, Z. Zhang, N. Ding, Y. Gu, X. Liu, Y. Huo, J. Qiu, Y. Yao, A. Zhang, L. Zhang, W. Han, M. Huang, Q. Jin, Y. Lan, Y. Liu, Z. Liu, Z. Lu, X. Qiu, R. Song, J. Tang, J.-R. Wen, J. Yuan, W. X. Zhao, and J. Zhu, “Pre-trained models: Past, present and future,” AI Open, vol. 2, pp. 225–250, 2021. [Online]. Available: https://www.sciencedirect.com/science/ article/pii/S2666651021000231
- [33] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training of deep bidirectional transformers for language understanding,” CoRR, vol. abs/1810.04805, 2018. [Online]. Available: http://arxiv.org/abs/1810.04805
- [34] J.-B. Alayrac et al., “Flamingo: a visual language model for few-shot learning,” arXiv preprint arXiv:2204.14198, 2022.
- [35] H. Liu, C. Zhang, Z. Hu, Y. Wang, Z. Yang, J. Wang, W. Chen et al., “Visual instruction tuning,” arXiv preprint arXiv:2304.08485, 2023.
- [36] J. Wei, M. Bosma, V. Y. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le, “Finetuned language models are zero-shot learners,” arXiv preprint arXiv:2109.01652, 2021.
- [37] S. Zhang, L. Dong, X. Li, S. Zhang, X. Sun, S. Wang, J. Li, R. Hu, T. Zhang, F. Wu et al., “Instruction tuning for large language models: A survey,” arXiv preprint arXiv:2308.10792, 2023.
- [38] B. Wang, X. Fu, Y. Lan, L. Zhang, W. Zheng, and Y. Xiang, “Large transformers are better eeg learners,” arXiv preprint arXiv:2308.11654, 2023.
- [39] J. Zhou, Y. Duan, F. Chang, T. Do, Y.-K. Wang, and C.T. Lin, “Belt-2: Bootstrapping eeg-to-language representation alignment for multi-task brain decoding,” arXiv preprint arXiv:2409.00121, 2024.
- [40] W. Wang, V. W. Zheng, H. Yu, and C. Miao, “A survey of zero-shot learning: Settings, methods, and applications,” ACM Trans. Intell. Syst. Technol., vol. 10, no. 2, Jan. 2019. [Online]. Available: https://doi.org/10.1145/3293318
- [41] F. Pourpanah, M. Abdar, Y. Luo, X. Zhou, R. Wang, C. P. Lim, X.-Z. Wang, and Q. M. J. Wu, “A review of generalized zero-shot learning methods,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 45, no. 4, pp. 4051–4070, 2023.
- [42] T. C. N’dir and R. T. Schirrmeister, “Eegclip : Learning eeg representations from natural

- language descriptions,” 2025. [Online]. Available: https://arxiv.org/abs/2503.16531
- [43] M. Wu, C. Zhao, A. Su, D. Di, T. Fu, D. An, M. He, Y. Gao, M. Ma, K. Yan, and P. Wang, “Hypergraph multi-modal large language model: Exploiting eeg and eye-tracking modalities to evaluate heterogeneous responses for video understanding,” 2024. [Online]. Available: https://arxiv.org/abs/2407.08150
- [44] Y. Wang, Q. Yao, J. Kwok, and L. M. Ni, “Generalizing from a few examples: A survey on few-shot learning,” 2020. [Online]. Available: https://arxiv.org/abs/1904.05046
- [45] Y. Song, T. Wang, S. K. Mondal, and J. P. Sahoo, “A comprehensive survey of few-shot learning: Evolution, applications, challenges, and opportunities,” 2022. [Online]. Available: https: //arxiv.org/abs/2205.06743
- [46] H. Chen, W. Zeng, C. Chen, L. Cai, F. Wang, Y. Shi, L. Wang, W. Zhang, Y. Li, H. Yan, W. T. Siok, and N. Wang, “Eeg emotion copilot: Optimizing lightweight llms for emotional eeg interpretation with assisted medical record generation,” 2025. [Online]. Available: https://arxiv.org/abs/2410.00166
- [47] S. Yao, L. Liu, J. Lu, D. Wu, and Y. Li, “Advancing semi-supervised eeg emotion recognition through feature extraction with mixup and large language models,” in 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024, pp. 2772– 2779.
- [48] D.-H. Lim, M.-J. Cho, and H.-H. Kim, “Classification of non-invasive eeg signals during motor imagery tasks using a large language model,” in 2024 International Conference on Cyberworlds (CW), 2024, pp. 378– 379.
- [49] H. Amrani, D. Micucci, and P. Napoletano, “Deep representation learning for open vocabulary electroencephalography-to-text decoding,” IEEE Journal of Biomedical and Health Informatics, p. 1–12, 2024. [Online]. Available: http://dx.doi.org/10.1109/JBHI.2024.3416066
- [50] Y. Duan, J. Zhou, Z. Wang, Y.-K. Wang, and C.T. Lin, “Dewave: Discrete eeg waves encoding for brain dynamics to text translation,” arXiv preprint arXiv:2309.14030, 2023.
- [51] J. W. Kim, A. Alaa, and D. Bernardo, “Eeg-gpt: exploring capabilities of large language models for eeg classification and interpretation,” arXiv preprint arXiv:2401.18006, 2024.
- [52] S. Gijsen and K. Ritter, “Eeg-language modeling for pathology detection,” arXiv preprint arXiv:2409.07480, 2024.
- [53] C. Qin, R. Yang, W. You, Z. Chen, L. Zhu, M. Huang, and Z. Wang, “Eegunity: Open-source tool in facilitating unified eeg datasets toward large-scale eeg model,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 33, pp. 1653–1663, 2025.
- [54] J. Wang, Z. Song, Z. Ma, X. Qiu, M. Zhang, and Z. Zhang, “Enhancing eeg-to-text decoding through transferable representations from pre-trained con-

- trastive eeg-text masked autoencoder,” arXiv preprint arXiv:2402.17433, 2024.
- [55] D. H. Lee and C. K. Chung, “Enhancing neural decoding with large language models: A gpt-based approach,” in 2024 12th International Winter Conference on Brain-Computer Interface (BCI), 2024, pp. 1–4.
- [56] A. Sano, J. Amores, and M. Czerwinski, “Exploration of llms, eeg, and behavioral data to measure and support attention and sleep,” arXiv preprint arXiv:2408.07822, 2024.
- [57] M. Guerra, R. Milanese, M. Deodato, M. G. Ciobanu, and F. Fasano, “Exploring the diagnostic potential of llms in schizophrenia detection through eeg analysis,” in 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2024, pp. 6812–6819.
- [58] Y. Zhang, S. Yang, G. Cauwenberghs, and T.-P. Jung, “From word embedding to reading embedding using large language model, eeg and eye-tracking,” in 2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 2024, pp. 1–4.
- [59] Y. Zhang, Q. Li, S. Nahata, T. Jamal, S.-k. Cheng, G. Cauwenberghs, and T.-P. Jung, “Integrating llm, eeg, and eye-tracking biomarker analysis for word-level neural state classification in semantic inference reading comprehension,” arXiv preprint arXiv:2309.15714, 2023.
- [60] W.-B. Jiang, L.-M. Zhao, and B.-L. Lu, “Large brain model for learning generic representations with tremendous eeg data in bci,” arXiv preprint arXiv:2405.18765, 2024.
- [61] C.-S. Chen, Y.-J. Chen, and A. H.-W. Tsai, “Large cognition model: Towards pretrained eeg foundation model,” arXiv preprint arXiv:2502.17464, 2025.
- [62] G. Wang, W. Liu, Y. He, C. Xu, L. Ma, and H. Li, “Eegpt: Pretrained transformer for universal and reliable representation of eeg signals,” in Advances in Neural Information Processing Systems, A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, Eds., vol. 37. Curran Associates, Inc., 2024, pp. 39249–

39280. [Online]. Available: https://proceedings. neurips.cc/paper files/paper/2024/file/ 4540d267eeec4e5dbd9dae9448f0b739-Paper-Conference. pdf

- [63] C. Zhao, Z. Cook, L. Murray, J. Kesan, N. Belacel, S. Doesburg, G. Medvedev, V. Vakorin, and P. Xi, “Leveraging large language models and fuzzy clustering for eeg report analysis,” in 2024 IEEE SENSORS, 2024, pp. 1–4.
- [64] W. Cui, W. Jeong, P. Th¨olke, T. Medani, K. Jerbi, A. A. Joshi, and R. M. Leahy, “Neuro-gpt: Developing a foundation model for eeg,” arXiv preprint arXiv:2311.03764, vol. 107, 2023.
- [65] Y. Tao, Y. Liang, L. Wang, Y. Li, Q. Yang, and H. Zhang, “See: Semantically aligned eeg-to-text translation,” in ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025, pp. 1–5.
- [66] Y. Chen, K. Ren, K. Song, Y. Wang, Y. Wang, D. Li, and L. Qiu, “Eegformer: Towards transferable

- and interpretable large-scale eeg foundation model,” arXiv preprint arXiv:2401.10278, 2024.
- [67] J.-H. Lim and P.-C. Kuo, “EEGTrans: Transformerdriven generative models for EEG synthesis,” 2025. [Online]. Available: https://openreview.net/forum? id=ydw2l8zgUB
- [68] T. Yue, S. Xue, X. Gao, Y. Tang, L. Guo, J. Jiang, and J. Liu, “Eegpt: Unleashing the potential of eeg generalist foundation model by autoregressive pretraining,” arXiv preprint arXiv:2410.19779, 2024.
- [69] W.-L. Zheng and B.-L. Lu, “Investigating critical frequency bands and channels for eeg-based emotion recognition with deep neural networks,” IEEE Transactions on Autonomous Mental Development, vol. 7, no. 3, pp. 162–175, 2015.
- [70] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “Emotionmeter: A multimodal framework for recognizing human emotions,” IEEE Transactions on Cybernetics, vol. 49, no. 3, pp. 1110–1122, 2019.
- [71] N. Hollenstein, M. Troendle, C. Zhang, and N. Langer, “ZuCo 2.0: A dataset of physiological recordings during natural reading and annotation,” in Proceedings of the Twelfth Language Resources and Evaluation Conference, N. Calzolari, F. B´echet, P. Blache, K. Choukri, C. Cieri, T. Declerck, S. Goggi, H. Isahara, B. Maegaard, J. Mariani, H. Mazo, A. Moreno, J. Odijk, and S. Piperidis, Eds. Marseille, France: European Language Resources Association, May 2020, pp. 138–146. [Online]. Available: https://aclanthology.org/2020.lrec-1.18/
- [72] C. Spampinato, S. Palazzo, I. Kavasidis, D. Giordano, N. Souly, and M. Shah, “Deep learning human mind for automated visual classification,” in 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 4503–4511.
- [73] S. Palazzo, C. Spampinato, I. Kavasidis, D. Giordano, J. Schmidt, and M. Shah, “Decoding brain representations by multimodal learning of neural activity and visual features,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 43, no. 11, pp. 3833– 3849, 2021.
- [74] S. V. Borisov, A. Y. Kaplan, N. L. Gorbachevskaya, and I. A. Kozlova, “Analysis of eeg structural synchrony in adolescents with schizophrenic disorders,” Human Physiology, vol. 31, no. 3, pp. 255–261, 2005. [Online]. Available: https://doi.org/10.1007/s10747-005-0042-z
- [75] B. Kemp, A. Zwinderman, B. Tuk, H. Kamphuisen, and J. Oberye, “Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the eeg,” IEEE Transactions on Biomedical Engineering, vol. 47, no. 9, pp. 1185–1194, 2000.
- [76] B. Blankertz, K.-R. Muller, D. Krusienski, G. Schalk, J. Wolpaw, A. Schlogl, G. Pfurtscheller, J. Millan, M. Schroder, and N. Birbaumer, “The bci competition iii: validating alternative approaches to actual bci problems,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 14, no. 2, pp. 153–159, 2006.
- [77] I. Obeid and J. Picone, “The temple university hospital eeg data corpus,” Frontiers in Neuroscience,

- vol. Volume 10 - 2016, 2016. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2016.00196
- [78] S. L´opez, G. Suarez, D. Jungreis, I. Obeid, and J. Picone, “Automated identification of abnormal adult eegs,” in 2015 IEEE Signal Processing in Medicine and Biology Symposium (SPMB), 2015, p. 10.1109/SPMB.2015.7405423.
- [79] H. A. Khan, R. Ul Ain, A. M. Kamboh, H. T. Butt, S. Shafait, W. Alamgir, D. Stricker, and F. Shafait, “The nmt scalp eeg dataset: An open-source annotated dataset of healthy and pathological eeg recordings for predictive modeling,” Frontiers in Neuroscience, vol. Volume 15 - 2021, 2022. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2021.755817
- [80] V. Shah, E. von Weltin, S. Lopez, J. R. McHugh, L. Veloso, M. Golmohammadi, I. Obeid, and J. Picone, “The temple university hospital seizure detection corpus,” Frontiers in Neuroinformatics, vol. 12, p. 83, Nov 2018.
- [81] N. Hollenstein, J. Rotsztejn, M. Troendle, A. Pedroni, C. Zhang, and N. Langer, “Zuco, a simultaneous eeg and eye-tracking resource for natural sentence reading,” Scientific Data, vol. 5, p. 180291, Dec 2018.
- [82] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals,” Circulation, vol. 101, no. 23, pp. e215–e220, Jun 2000.
- [83] Y. Wang, X. Chen, X. Gao, and S. Gao, “A benchmark dataset for ssvep-based brain-computer interfaces,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 10, pp. 1746–1752, Oct 2017, epub 2016 Nov 10.
- [84] M. Tangermann, K.-R. Muller,¨ A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. J. Miller, G. Mueller-Putz, G. Nolte, G. Pfurtscheller, H. Preissl, G. Schalk, A. Schl¨ogl, C. Vidaurre, S. Waldert, and B. Blankertz, “Review of the bci competition iv,” Frontiers in Neuroscience, vol. Volume 6 - 2012, 2012. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2012.00055
- [85] D. Steyrl, R. Scherer, J. Faller, and G. R. Muller-Putz,¨ “Random forests in non-invasive sensorimotor rhythm brain-computer interfaces: a practical and convenient non-linear classifier,” Biomedical Engineering / Biomedizinische Technik, vol. 61, no. 1, pp. 77–86, 2016. [Online]. Available: https://doi.org/10.1515/bmt-2014-0117
- [86] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391–5420,

2017. [Online]. Available: https://onlinelibrary. wiley.com/doi/abs/10.1002/hbm.23730

- [87] G. Huang, Z. Hu, W. Chen, Z. Liang, L. Li,

- L. Zhang, and Z. Zhang, “M3cv:a multi-subject, multi-session, and multi-task database for eegbased biometrics challenge,” bioRxiv, 2022. [Online]. Available: https://www.biorxiv.org/content/early/ 2022/07/03/2022.06.28.497624
- [88] P. Margaux, M. Emmanuel, D. S´ebastien, B. Olivier, and M. J´er´emie, “Objective and subjective evaluation of online error correction during p300-based spelling,” Advances in HumanComputer Interaction, vol. 2012, no. 1, p. 578295,

2012. [Online]. Available: https://onlinelibrary. wiley.com/doi/abs/10.1155/2012/578295

- [89] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, physiotoolkit, and physionet,” Circulation, vol. 101, no. 23, pp. e215–e220, 2000. [Online]. Available: https://www.ahajournals.org/ doi/abs/10.1161/01.CIR.101.23.e215
- [90] S. Koelstra, C. Muhl, M. Soleymani, J.-S. Lee, A. Yazdani, T. Ebrahimi, T. Pun, A. Nijholt, and I. Patras, “Deap: A database for emotion analysis ;using physiological signals,” IEEE Transactions on Affective Computing, vol. 3, no. 1, pp. 18–31, 2012.
- [91] J. Chen, X. Wang, C. Huang, X. Hu, X. Shen, and D. Zhang, “A large finer-grained affective computing eeg dataset,” Scientific Data, vol. 10, no. 1, p. 740, 2023. [Online]. Available: https: //doi.org/10.1038/s41597-023-02650-w
- [92] W. Liu, J.-L. Qiu, W.-L. Zheng, and B.-L. Lu, “Comparing recognition performance and robustness of multimodal deep learning models for multimodal emotion recognition,” IEEE Transactions on Cognitive and Developmental Systems, vol. 14, no. 2, pp. 715–729, 2022.
- [93] H. Cho, M. Ahn, S. Ahn, M. Kwon, and S. C. Jun, “Eeg datasets for motor imagery brain–computer interface,” GigaScience, vol. 6, no. 7, p. gix034, 05 2017. [Online]. Available: https://doi.org/10.1093/gigascience/gix034
- [94] I. Zyma, S. Tukaev, I. Seleznov, K. Kiyono, A. Popov, M. Chernykh, and O. Shpenkov, “Electroencephalograms during mental arithmetic task performance,” Data, vol. 4, no. 1, 2019. [Online]. Available: https://www.mdpi.com/2306-5729/4/1/14
- [95] W. L. Lim, O. Sourina, and L. P. Wang, “Stew: Simultaneous task eeg workload data set,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 26, no. 11, pp. 2106–2114, 2018.
- [96] D. Alvarez-Estevez and R. Rijsman, “Haaglanden medisch centrum sleep staging database (version 1.1),” https://doi.org/10.13026/t79q-fr32, 2022, physioNet.
- [97] C. H. Nguyen, G. K. Karavas, and P. Artemiadis, “Inferring imagined speech using eeg signals: a new approach using riemannian manifold features,” Journal of Neural Engineering, vol. 15, no. 1, p. 016002, dec 2017. [Online]. Available: https://dx.doi.org/10.1088/1741-2552/aa8235
- [98] A. Creswell, T. White, V. Dumoulin, K. Arulkumaran, B. Sengupta, and A. A. Bharath,

- “Generative adversarial networks: An overview,” IEEE Signal Processing Magazine, vol. 35, no. 1, p. 53–65, Jan. 2018. [Online]. Available: http://dx.doi.org/10.1109/MSP.2017.2765202
- [99] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial networks,”

2014. [Online]. Available: https://arxiv.org/abs/ 1406.2661

- [100] Z. Pan, W. Yu, X. Yi, A. Khan, F. Yuan, and Y. Zheng, “Recent progress on generative adversarial networks (gans): A survey,” IEEE Access, vol. 7, pp. 36322– 36333, 2019.
- [101] A. G. Habashi, A. M. Azab, S. Eldawlatly, G. M. Aly, and A. Fahmy, “Generative adversarial networks in eeg analysis: An overview,” Journal of NeuroEngineering and Rehabilitation, vol. 20, p. 40,

2023. [Online]. Available: https://doi.org/10.1186/ s12984-023-01169-w

- [102] K. G. Hartmann, R. T. Schirrmeister, and T. Ball, “Eeg-gan: Generative adversarial networks for electroencephalograhic (eeg) brain signals,” 2018. [Online]. Available: https://arxiv.org/abs/1806.01875

