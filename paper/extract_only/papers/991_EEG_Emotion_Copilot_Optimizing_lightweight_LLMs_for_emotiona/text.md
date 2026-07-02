# arXiv:2410.00166v3[cs.CV]15Jul2025

## EEG Emotion Copilot: Optimizing Lightweight LLMs for Emotional EEG Interpretation with Assisted Medical Record Generation

Hongyu Chena, Weiming Zenga,∗, Chengcheng Chena, Luhui Caia, Fei Wanga, Yuhu Shia, Lei Wanga, Wei Zhanga, Yueyang Lia, Hongjie Yanb, Wai Ting Siokc and Nizhuan Wangc,∗

aLaboratory of Digital Image and Intelligent Computation, Shanghai Maritime University, Shanghai 201306, China bDepartment of Neurology, Affiliated Lianyungang Hospital of Xuzhou Medical University, Lianyungang 222002, China cDepartment of Chinese and Bilingual Studies, The Hong Kong Polytechnic University, Hong Kong, SAR, China

###### ARTICLE INFO

###### ABSTRACT

Keywords: Lightweight LLM Model pruning Model fine-tuning Emotion recognition Assisted electronic medical record

In the fields of affective computing (AC) and brain-computer interface (BCI), the analysis of physiological and behavioral signals to discern individual emotional states has emerged as a critical research frontier. While deep learning-based approaches have made notable strides in EEG emotion recognition, particularly in feature extraction and pattern recognition, significant challenges persist in achieving end-to-end emotion computation, including rapid processing, individual adaptation, and seamless user interaction. This paper presents the EEG Emotion Copilot, a system optimizing a lightweight large language model (LLM) with 0.5B parameters operating in a local setting, which first recognizes emotional states directly from EEG signals, subsequently generates personalized diagnostic and treatment suggestions, and finally supports the automation of assisted electronic medical records. Specifically, we demonstrate the critical techniques in the novel data structure of prompt, model pruning and fine-tuning training, and deployment strategies aiming at improving performance and computational efficiency. Extensive experiments show that our optimized lightweight LLM-based copilot achieves an enhanced intuitive interface for participant interaction, superior accuracy of emotion recognition and assisted electronic medical records generation, in comparison to such models with similar scale parameters or large-scale parameters such as 1.5B, 1.8B, 3B and 7B. In summary, through these efforts, the proposed copilot is expected to advance the application of AC in the medical domain, offering innovative solution to mental health monitoring. The codes will be released at https://github.com/NZWANG/EEG_Emotion_Copilot.

chitecture [19] have demonstrated strong contextual understanding [20]. Models such as EEG-GPT [21] and ChatGPTBCI [22] focus primarily on brain state identification but haveyettoeffectivelyaddressdiverse, human-centeredtasks. The integration of LLMs with EEG signals to generate personalized diagnoses, treatment plans, and assisted electronic medical records remains an urgent and complex challenge with the following limitations.

### 1. Introduction

The application of affective computing (AC) in braincomputerinterfaces(BCI)isemergingasakeyresearchfrontier. Affective computing [1] seeks to identify emotional statesbyanalyzingphysiologicalandbehavioralsignals, such as electroencephalograms (EEG) [2] [3], heart rate [4], facial expressions [5], voice [6], etc. Advances in this field have expanded the possibilities for BCI technology, particularly in enhancing human-machine interaction [7], [8], and increasing its potential for practical applications in rehabilitation [9], [10] and other areas [11].

Firstly, building a suitable human-based multimodal corpus from diverse databases for LLMs is a challenging task. While public datasets like Wikitext [26] and Common Crawl [27], along with specialized datasets like SEED [28] and FACED [29], offer substantial prior knowledge, this information remains fragmented. The challenge lies in linking these datasets to create a unified data structure that facilitates language model development and enables accurate responses through appropriate prompts.

Thepowerfulcapabilitiesofdeepneuralnetworks(DNNs)

have driven rapid advancements in AC for emotion recognition via EEG signals [12], [13], with numerous deep learning approaches proposed [14], [15], [16]. Recently, large language models (LLMs) [17], [18] built on Transformer ar-

Secondly, EEG signals can be viewed as a form of long text data [30], yet the signal sequences from a single channel often exhibit significant redundancy for machine learning approaches [31], [32] [33], [34]. LLMs require a considerable number of tokens [19] to process this redundancy, resulting in unnecessary computational overhead. Additionally, many affective computing tasks rely on EEG data from 32, 64, or more channels, which further diminishes computational efficiency and poses challenges for rapid processing. Therefore, effective data compression is critical to optimizing lightweight LLMs for efficient and responsive deploy-

⋆Corresponding author: Weiming Zeng, and Nizhuan Wang.

hongychen676@gmail.com (H. Chen); zengwm86@163.com or wmzeng@shmtu.edu.cn (W. Zeng); shmtu_ccc@163.com (C. Chen); clh0x123@126.com (L. Cai); shine_wxf@163.com (F. Wang); syhustb2011@163.com (Y. Shi); sayhiwl@163.com (L. Wang); zhangw99591@163.com (W. Zhang); lyy20010615@163.com (Y. Li); yanhjns@gmail.com (H. Yan); wai-ting.siok@polyu.edu.hk (W. Siok); wangnizhuan1120@gmail.com or nizhuan.wang@polyu.edu.hk (N. Wang)

[Figure 1]

ORCID(s): 0009-0004-2934-3135 (H. Chen); 0000-0002-9035-8078 (W. Zeng); 0000-0002-6014-5135 (C. Chen); 0009-0002-3150-6664 (L. Cai); 0009-0005-3061-0496 (F. Wang); 0000-0002-4009-2849 (Y. Shi); 0000-0003-0111-4328 (L. Wang); 0009-0002-3088-1390 (W. Zhang); 0009-0008-5310-124X (Y. Li); 0009-0000-2553-2183 (H. Yan); 0000-0002-2154-5996 (W. Siok); 0000-0002-9701-2918 (N. Wang)

[Figure 2]

- Figure 1: Flowchart of EEG Emotion Copilot. The original EEG signal is preprocessed and transformed via wavelet to shorten the signal length. The final prompt is constructed using the initialized prompt, demographic data, emotional label, and treatment as training data. Using the Qwen2-0.5B-pretrained model [23] as an example, we prune it with the radio of 50% and fine-tuning the pruned model directly with specific dataset. During the Model Fine-tuning stage, a warm-up phase gradually increases the learning rate, and LoRA [24] is used for fine-tuning. Finally, the model is deployed, utilizing the RAG (Retriever-Reader-Generator) technique [25] to enhance retrieval performance, and a dialogue deployment of the graphical interface to improve interactivity.

ment.

Finally, lightweight LLMs are optimally run locally to safeguard participant privacy and data security. While tasks based on public LLMs, such as EEG-GPT [21], appear feasible, many industry models necessitate powerful machines. For specific local tasks, complex DNNs are often excessively redundant. Therefore, effective model pruning is essential to achieve a lightweight language model suitable for local execution.

Therefore, we propose EEG Emotion Copilot, an intelligent system based on a lightweight, locally-running language model that utilizes EEG signals to first perform emotion recognition, subsequently generate corresponding diagnosis and treatment plans, and finally create assisted electronic medical records, as illustrated in Fig. 1.

### 2. RELATED WORK

The integration of large language models with EEG signals has opened new avenues for affective computing and clinicaldiagnostics, particularlyinemotionrecognition, mental health assessment, and neurological disorder diagnosis. This section provides a comprehensive review of current researchonLLM-basedEEG-assisteddiagnosticsolutions, summarizes the state of the field, and highlights specific gaps addressed by the proposed EEG Emotion Copilot.

- 2.1. LLM-Based EEG-Assisted Diagnosis Recent studies have leveraged LLMs to process EEG sig-

nals for diagnostic purposes, capitalizing on their ability to

interpret complex data and generate natural language output. In emotion recognition, EEG-GPT [21] demonstrates the potential of LLMs to classify emotional states and motor imagery from raw EEG, though its reliance on large models limits practical deployment. Similarly, NeuroLM [35] integrates EEG and language in a multitask foundation model, improving emotion classification and diagnostic text generation but requiring significant computational resources. Text generation from EEG signals [36] has also been explored, with fine-tuned LLMs producing emotional state descriptions for visual stimuli, yet cross-subject variability remains a challenge.

Beyond emotion, LLMs are applied to mental health and neurological diagnostics. A review by Shang et al. [37] highlights the role of AI in EEG-based diagnosis of epilepsy, Alzheimer’s, and depression, with LLMs generating interpretive reports, although data heterogeneity and constraints on rapid inference still persist. Automated schizophrenia diagnosis using EEG and LLMs for multimodal data fusion shows promise but lacks clinical validation [38]. Specialized LLMs [39] have outperformed neurologists in complex diagnostic tasks, but their EEG integration is limited to textual case processing. Foundation models like LaBraM [40] enable cross-dataset EEG learning for tasks like seizure detection and emotion recognition, yet are not optimized for resource-constrained environments.

Despite these advancements, LLM-based EEG diagnostics face significant hurdles:

• Computational Cost: Large models (e.g., 14B) require

high-end GPUs, hindering clinical deployment.

- 2.4. Assisted Electronic Medical Records Electronicmedicalrecords(EMRs)datebacktothe1960s

[63]. With advancements in computer science and artificial intelligence (AI), EMRs have evolved from merely storing and managing patient information to incorporating more complex functionalities. Currently AI models are increasingly integrated into diagnosing mental illnesses and detecting internal organ pathologies, enhancing the capabilities of assisted EMRs. The sample of "assisted electronic medical record" is shown in Fig. 2, where the intelligent copilot can process the multimodal diagnostic data and produce accurate results. In this study, we developed a new EEG Emotion Copilot that leverages a lightweight local LLM to perform emotion recognition based on EEG signals, and to further generate the corresponding assisted EMR.

- 3. METHOD

- • Generalization: EEG variability across subjects, devices, and sessions limits model robustness [15].
- • Privacy: Cloud-based LLMs risk patient data exposure, necessitating local solutions.
- • ClinicalValidation: Lackofhuman-in-the-loopmechanisms and rigorous trials reduces trust in LLM output.

#### 2.2. Lengthy EEG Signal Embedded in Prompt For specific tasks in LLM prompt engineering, tailored

prompts are essential to obtain reasonable answers [41]. Although datasets like Wikitext [26] and Common Crawl [27] contain extensive knowledge, constructing specific datasets is necessary for optimal performance in particular tasks. In moststudiesonAC,researchersfocusondistinguishingemotions using convolutional neural networks (CNNs) or recurrent neural networks (RNNs) [42], with EEG signals primarily used to assess model quality [43], [44]. Recently, LLMs have been required to split EEG sequences into tokens for processing, with computational and memory demands increasing exponentially with input length [45]. This poses significant challenges for LLM deployment, particularly on low-resource devices or in latency-sensitive scenarios. Although data chunking strategies [46] can split long sequences for training and deployment, the EEG data length significantlyimpactsreasoningeffectiveness[47], [48]. Therefore, a reasonable data compression method is necessary to LLMs.

#### 3.1. Data Structures of Prompt in EEG Emotion Copilot

Fine-tuned LLMs often excel in generating end-to-end outputs, particularly for straightforward classification tasks. Forexample, determiningwhetherasubject’semotionalstate is positive or negative based on EEG data is relatively simple. However, distinguishing more nuanced emotions—such as the nine-class emotional categories in the FACED dataset [29]—or accurately recognizing emotions in real-world scenarios remains a formidable challenge. In datasets like Wikitext and similar corpora, the content primarily consists of declarative sentences (left part of Fig. 3). In contrast, tasks requiring logical reasoning typically store data as questionanswer pairs, as illustrated in the middle part of Fig. 3. Despite these advancements, existing data structures face significant limitations when applied to EEG-based emotion diagnosis and treatment planning, particularly in integrating multimodal data and addressing task-specific requirements. To bridge these gaps, we propose a novel data structure that leverages a question-answer system specifically designed for EEG-related tasks, enhancing both interpretability and applicability in clinical and affective computing domains.

##### 2.3. Model Pruning in Deep Learning The Frankle and Carbin’s lottery ticket hypothesis [49]

posits that small subnetworks, when trained from scratch, can achieve comparable performance. Based on it, model pruning [50] has been widely applied in DNNs to reduce computationalcomplexityandmitigatemodelhallucinations [51]. For instance, Li et al. [52] and Han et al. [53] introduced filter and weight pruning techniques, while Michel et al. [54] explored attention head pruning in Transformer models. Zhuang et al. [55] employed gradient-based structuredpruning, andLiuetal. [56]proposedMetaPrune, which combines pruning with neural architecture search (NAS). Guo et al. [57] focused on channel pruning for efficient inference. Comprehensive surveys by Blalock et al. [58] and He et al. [59] have highlighted the effectiveness of various pruning techniques and outlined future research directions. In the context of LLMs, methods such as SparseGPT [60] and LLM-Pruner [61], primarily based on the LLaMA model [62], have demonstrated promising results on public datasets and claim faster performance on local machines. However, the hardware used for inference, such as RTX 4090 GPUs, significantly outperforms standard PCs, leaving the inference cost still relatively high. Thus, for local computations with limited resources, there remains a need for more efficient and feasible pruning methods to further reduce computational costs.

In the data structure of the proposed EEG Emotion Copilot, we initialize the system with the prompt showed in the right part of Fig. 3: "You are an EEG emotion analyzer. I will input the patient’s personal information and EEG signals from specific electrode positions. Please infer the patient’s current emotional state and provide a detailed diagnosis along with personalized treatments based on your knowledge base." Following initialization, we input the subject’s demographic data, including gender, age, and facial features, to assess their emotional state. Next, the acquired EEG signals are processed. As illustrated in Fig. 1, preprocessing steps such as artifact removal and re-referencing are applied to the signals, followed by wavelet transformation for signal compression. These processed signals are then used as input. Specifically, compressed signals are combined with channel information (e.g., Fp1, Cz) into a unified prompt for text input, standardizing the model’s input format. Finally,

the structural dependencies between layers: 

[Figure 3]

(𝑓𝑖−,𝑓𝑗+) = 

(𝑓𝑗+,𝑓𝑖−)

1, if 𝑓𝑖− ↔ 𝑓𝑗+ or (𝑖 = 𝑗 and sch

= ⎧ ⎨ ⎪ ⎩

(2)

= sch(𝑓𝑗+)), 0, otherwise.

(𝑓𝑖−)

where ↔ denotes that two feature maps are directly related and sch(𝑝) operation is used to determine which parameters in the parameter group 𝑝 need to be retained. Formula 2 re-

turns a boolean value, where sch(𝑓𝑖+) = sch(𝑓𝑗−) indicates that the two parameter groups are subject to the same prun-

ing scheme.

In addition, we use the 2 norm to calculate the importance of the parameter group corresponding to each layer [64]. Based on the Qwen2 architecture, we calculate the importance  of the Embedding layer, Self-Attention layer, MLP layer, and Linear layer in turn as follows:

(embed_tokens) = ∑

‖𝑤‖22, (3)

𝑤∈embed_tokens

(𝑠𝑖) = ∑ 𝑤∈𝑠𝑖 ‖𝑤‖22,

⎧ ⎨ ⎪ ⎩

(4)

𝑆 = {𝑞proj,𝑘proj,𝑣proj,𝑜proj}.

- Figure 2: Schematic diagram of the assisted electronic medical record generated by intelligent copilot. It can include Basic Information, Medical History, Physical Examination Records, Diagnosis Information, Treatment Plan, Laboratory Results, Follow-up Records, and Medical Expenses.

(𝑚𝑖) = ∑ 𝑤∈𝑚𝑖 ‖𝑤‖22,

⎧ ⎨ ⎪ ⎩

(5)

𝑀 = {𝑔𝑎𝑡𝑒proj,𝑢𝑝proj,𝑑𝑜𝑤𝑛proj}.

(lm_head) = ∑

‖𝑤‖22. (6)

𝑤∈lm_head

the structure is completed by adding emotion labels provided by origin dataset and corresponding treatment plans in the second and third sections, respectively.

where embed_tokens denotes the input embedding matrix of the Qwen2 model, where each row corresponds to the embedding vector of a token in the vocabulary. This matrix transforms discrete token indices into dense vector representations. 𝑠𝑖 represents the 𝑖-th projection matrix within the self-attention module of each Transformer block. Specifically, 𝑠𝑖 belongs to the set 𝑆 = {𝑞proj,𝑘proj,𝑣proj,𝑜proj}, corresponding to the linear projections of query, key, value, and output in multi-head attention. 𝑚𝑖 is the 𝑖-th projection component of the multi-layer perceptron (MLP) block, including the gate, up, and down projections. lm_head refers to the final output linear transformation layer, also known as the language modeling head, which projects the hidden state outputs of the Transformer into vocabulary logits for nexttoken prediction.

- 3.2. Model Pruning in EEG Emotion Copilot In this study, for the flexibility and versatility, we applied

the torch pruning [64] to perform the model pruning task with the pruning_ratio equal to 0.5, and the detailed process is showed in Fig. 4.

Firstly, basedonthearchitectureoftheQwen2-0.5Bmodel, the total number of layers 𝐿 is determined as follows:

 = 𝑁𝑢𝑚(𝑄𝑤𝑒𝑛2_𝑙𝑎𝑦𝑒𝑟) = 𝑁𝑢𝑚(𝐸𝑚𝑏𝑒𝑑𝑑𝑖𝑛𝑔_𝑙𝑎𝑦𝑒𝑟)

+ 𝑁𝑢𝑚(𝑄𝑤𝑒𝑛2𝐷𝑒𝑐𝑜𝑑𝑒𝑟_𝑙𝑎𝑦𝑒𝑟) + 𝑁𝑢𝑚(𝐿𝑚_ℎ𝑒𝑎𝑑) = 25, (1)

where 𝑁𝑢𝑚(∗) denotes the number of respective components: embedding layer, decoder layer, and language modeling head. The input and output of each layer are denoted

Based on the above formula, we first group the parameters  to get set ′, as shown in Algorithm 1. Then, we proceed to prune the model, as shown in Algorithm 2.

as 𝑓𝑖− and 𝑓𝑗+, respectively, where 𝑖,𝑗 ∈ {1,…,}. The superscripts “−” and “+” indicate input and output features,

respectively.

#### 3.3. Model Fine-tuning in EEG Emotion Copilot

Next, we construct a layer dependency graph  according to [64]. This is a 2×2 symmetric matrix that reflects

To restore the performance of the pruned model ′, we explored two fine-tuning strategies after applying torchpruning [64], as illustrated in Fig. 5. Strategy 1 is only training the pruned model on the specific EEG dataset to focus

[Figure 4]

- Figure 3: Comparison of three data structures as to prompt in LLMs: the general data structure (left), the question-answering system data structure (middle), and the data structure used in the proposed EEG Emotion Copilot (right).

[Figure 5]

- Figure 4: Flowchart of model pruning in EEG Emotion Copilot: The upper left presents a rough framework diagram, while the right side illustrates torch pruning with a 0.5 pruning ratio. In this process, the input_feature and out_feature of Qwen2SdpaAttention and Qwen2MLP are halved compared to the original model. The final output of lm_head remains unchanged, as it is directly tied to the vocabulary size. The lower left depicts a simplified torch pruning process.

the model on task-relevant features with Low-Rank Adaptation (LoRA) [24]. Strategy 2 firstly involves full fine-tuning the pruned model on public datasets Wikitext [26] and Common Crawl [27], to leverage their diverse categories to establish generalized features, and subsequently fine-tuning on the specific EEG dataset with LoRA. Moreover, a warm-up strategy is applied at the beginning of training to facilitate convergence and improve overall model performance.

To straightforwardly illustrate the fine-tuning process, we take the FACED dataset [29] as a representative example, as shown in Fig. 6. The training procedure is divided into five sequential stages, each consisting of three epochs. In Stages 1 to 4, we employed 250 Hz EEG recordings from

55 subjects in FACED. Interestingly, the model exhibited better performance in Stage 3 than in Stage 4, despite minimal differences in training loss, indicating that extended training may be unnecessary, and potentially harmful—for lightweight architectures. In Stage 5, 1000 Hz EEG data from an additional 68 FACED subjects were incorporated, with the model initialized from the Stage 4 checkpoint. This resulted in richer task-specific responses, further validating the model’s capacity to capture the underlying structure of EEG signals and generalize across varying sampling rates.

- Algorithm 1 Parameter Grouping

Input: Dependency graph , parameter group set  Output: Group set ′

- 1: Initialize ′ ← ∅
- 2: for 𝑖 ∈  do
- 3: Create new group 𝑝 ← {𝑘}
- 4: Expand group 𝑝:
- 5: while there exists an unvisited node 𝑗 such that (𝑓𝑖−,𝑓𝑗+) = 1 do
- 6: 𝑝 ← 𝑝 ∪ {𝑗}
- 7: Mark 𝑗 as visited
- 8: end while
- 9: ′ ← ′ ∪ 𝑝
- 10: end for
- 11: return ′

- Algorithm 2 Pruning Process

[Figure 6]

Figure 5: Two fine-tuning strategies. Strategy 1 involves initially training the model on a specific EEG dataset tailored to the current task. Strategy 2 begins with training the model on public datasets, and subsequently fine-tuning it on a specific EEG dataset.

### 4. EXPERIMENTS

#### 4.1. Implementation Details

Input: Initial model , Parameter group set ′, importance func-

Dataset: During pruning, the Wikitext dataset is used to optimize language capabilities. For training validation, we utilize the FACED dataset [30], which contains EEG recordings from 123 subjects (75 females, mean age 23.2) with 32 channels, collected via a NeuSen.W32 system at 250 or 1000 Hz. Participants watched 28 affective video clips (30 seconds each) designed to evoke nine emotions: anger, disgust, fear, sadness, neutral, amusement, inspiration, joy, and tenderness. Each positive and negative emotion is represented by three clips, and neutral by four, ensuring balanced coverage.

tion , contraction strength 𝛼 Output: Pruned model ′

- 1: Calculate group importance:
- 2: for 𝑝′ ∈ ′ do
- 3: (𝑝′) ←

∑

𝑤∈′ ‖𝑤‖22 (See Formula 3, 4, 5, 6)

- 4: end for
- 5: ′′ ← sort(′,by )
- 6: Select groups for pruning based on importance:
- 7: for 𝑝′′ ∈ ′′ do
- 8: if (𝑝′′) ≤ 𝜃 is satisfied. (𝜃 is the threshold) then
- 9: ′′ ← ′′ ⧵ 𝑝′′
- 10: end if
- 11: end for
- 12: return ′

We further adopted the SEED [31, 28] and SEED-IV [65] datasets, released by Shanghai Jiao Tong University, to validate the proposed method. Both datasets contain EEG recordings from 15 healthy subjects across three sessions on different days, acquired using a 62-channel ESI NeuroScan system (originally sampled at 1000 Hz and downsampled to 200 Hz). In SEED, participants viewed 15 film clips designedtoelicitpositive, neutral, ornegativeemotions. SEEDIV extends the emotion categories to happiness, sadness, fear, and neutral, and additionally provides eye-tracking data recorded via SMI eye-tracking glasses. Each trial includes a 5-second cue, 4-minute clip, 45-second self-assessment, and 15-second rest.

- 3.4. Model Deployment in EEG Emotion Copilot Given the diverse range of model deployment tools, such

as llama.cpp, which enables model quantization based on specific scenarios and conversion into the GGUF format, the model can be seamlessly utilized via Ollama, LLM Studio, Gradio, or other platforms. When deployed with Gradio, this process culminates in the model deployment framework illustrated in Fig. 1.

- 3.5. Generation of Assisted Electronic Medical Records

Training Details: In the model pruning phase, we set the pruning ratio to 0.5 with Wikitext dataset used to optimize language capabilities and then trained on the public datasets with a learning rate of 1e-5, incorporating L1 and L2 regularization terms.The training was conducted for 40 Epoches. During the LoRA fine-tuning phase, we maintained a learning rate of 1e-5, applied weight decay and gradient decay, and set LoRA𝑟 to 8, LoRA𝛼 to 32, and LoRA𝑑𝑟𝑜𝑝𝑜𝑢𝑡 to 0.5. The fine-tuning process spanned 15 epochs, dividing into 5 steps. The training epochs of the compared models were set to 15. Unlike prior work requiring high-end GPUs (e.g., RTX 4090) fordeployment, our0.5B model runs on standard hardware, though training multiple models (0.5B to 7B) necessitated A800 and RTX 4090 GPUs for memory-intensive computations. Besides, all other models were trained for 15 epochs to ensure fairness and comparability.

Given that the proposed copilot is designed to handle a range of critical tasks—including emotion recognition, diagnosis, and treatment plan formulation—it is imperative to integrate demographic data from diverse cases across various emotional states, alongside their corresponding compressed EEG signals, into the training dataset. In downstream applications, participant data can be structured and fed into the fine-tuned model, enabling the generation of precise diagnostic insights and personalized treatment plans, as illustrated in Fig. 7.

[Figure 7]

- Figure 6: Model’s fine-tuning process on the specific EEG dataset. This fine-tuning process is divided into five steps, each consisting of three epochs. The first four steps utilize 250 Hz data from 55 subjects. Comparing the model’s answers in steps

- 3 and 4 reveals that the answer in step 3 is richer in content, with no significant difference in training loss between the two steps. This suggests that overtraining lightweight models may be redundant or even detrimental. In step 5, 1000 Hz data from 68 subjects is used for training, employing the pre-trained model from step 4.

#### 4.2. Performance Validation of Varied EEG Signal Length

Regarding the effect of the compressed signal length, we first extracted the EEG signal in the FACED data and the corresponding demography according to the Data Structure in Fig. 1. We implemented two compression methods and an original control group. The question-answering process and the corresponding results are shown in Fig. 10. Although the euclidean distance and cosine similarity of Ans1 and Ans2 are similar to the baseline for the same question, Ans2 is more consistent with the baseline than Ans1, as Ans1 differs from the baseline in terms of emotion recognition. Therefore, with limited resources, it is often more effective to compress the signal to a fixed length using wavelet transforms rather than a segmented approach.

#### 4.3. Training details of different pruning ratio

Weinvestigatedtheparameterdistributionsofthepruned models under various pruning ratios, as illustrated in Table 1 and Fig. 8. Pruning effectively reduces the dimensionality of key components, including the MLP layers (gate_proj, up_proj, down_proj)andtheattentionmodules(q_proj, k_proj,

v_proj, o_proj), resulting in smaller matrix operations duringbothforwardandbackwardpasses. Thesestructuralchanges significantly reduce the number of floating-point operations and inference time.

In addition, we explored high pruning ratios of 0.9, 0.8, 0.7, and 0.6 for the Qwen2-0.5B model. However, training under pruning ratios of 0.9 and 0.8 consistently failed to converge, as shown in Fig. 9, likely due to excessive removal of critical parameters. While models with pruning ratios of 0.7 and 0.6 exhibited more stable convergence, their improvements remained marginal after repeated training attempts. We attribute this to the relatively higher proportion of retained parameters, which preserved a basic level of representational capacity. Nevertheless, the aggressive pruning still disrupted essential pathways, limiting the model’s ability to recover, as reflected in the flattened learning curves.

#### 4.4. Performance Comparison with Lightweight Models

To rigorously validate our experimental hypothesis, we integrate the strategies illustrated in Fig. 6 and Fig. 10. The training process is structured based on data derived from

[Figure 8]

- Figure 7: Flowchart of assisted electronic medical record generation implemented in EEG Emotion Copilot.

Table 1 Changes in Model Parameter Dimensions at Different Pruning Ratio

Pruning Ratio

GPU memory usage while pruning (MB) Full 896 896 128 4864 896 24 1e-6 498,431,872 1628 -

Embed Dim Q Proj K/V Proj MLP Gate/Up

MLP Down Layers Norm Eps Total Params

GPU memory usage for loading (MB)

- 0.1 804 804 134 4376 804 24 1e-6 411,738,852 2546 2837
- 0.2 716 710 142 3888 716 24 1e-6 338,560,828 1406 1731
- 0.3 624 624 156 3404 624 24 1e-6 271,158,576 1242 2543
- 0.4 536 536 134 2916 536 24 1e-6 211,255,288 1090 2271
- 0.5 448 444 148 2432 448 24 1e-6 159,284,000 868 2451
- 0.6 356 356 178 1944 356 24 1e-6 113,233,828 832 2903
- 0.7 268 268 134 1456 268 24 1e-6 74,699,660 866 1731
- 0.8 176 168 24 972 176 24 1e-6 41,563,888 704 2291
- 0.9 88 84 12 484 88 24 1e-6 17,283,320 586 2273

compression method 1, divided into five sequential steps, with each step trained for three epochs. At each checkpoint (i.e., checkpoint1–n), we conduct classification on content generation for the nine emotion categories described in 3.1, followedbyabroaderclassificationintothreesentimentgroups (positive, negative, and neutral). For comparative analysis, we adopt Qwen2-0.5B as the baseline model, training it for six epochs under identical experimental conditions to obtain base_model-1, which is then evaluated for classification performance, as summarized in Table 2.

Next, we fine-tuned the models based on the data derived from compression method 2. Specifically, we fine-tuned the pruned model in 5 steps, with 3 epochs respectively, and perform classification for both the nine emotions and the three emotions. For consistency, Qwen2-0.5B is also trained for

15 epochs to obtain base_model-2, after which the corresponding classification experiment is conducted, as shown in Table 2.

Additionally, we include opt-350m [66], LiteLlama, and gpt-sw3-356mandrecentlyreleasedqwen3-0.6B[67]asbaseline references. Indeed, the checkpoint1-n model of Model 1 did not achieve ideal results on both tasks compared to the base_model-1. However, considering the F1 scores across multiple epochs of training, the model’s performance on this task gradually improved. In Model 2, the performance of checkpoint2-2andcheckpoint2-3showedsignificantimprovement compared to models with the similar parameter size, and they also consumed less average response time.

###### Performance Comparison Of Competing Light-Weight Models On FACED

Compression

Nine Emotion Recognition Three Emotion Recognition Method F1 Avg. RT (s) F1 Avg. RT (s)

Model Parameters Storage_size Precision Epoch

Our Model 1

- checkpoint1-1 0.15B 0.294G bf16 3 0.080 0.430 0.216 0.420

- checkpoint1-2 0.15B 0.294G bf16 3 0.096 0.510 0.324 0.510

- checkpoint1-3 0.15B 0.294G bf16 3 0.100 0.540 0.376 0.540

- checkpoint1-4 0.15B 0.294G bf16 3 0.093 0.600 0.359 0.610

- checkpoint1-5 0.15B 0.294G bf16 3 0.103 0.610 0.340 0.580

W→S

base_model-1 [23] 0.50B 0.920G bf16 15 0.188 2.100 0.331 1.200 opt-350m-1 [66] 0.35B 0.647G bf16 15 0.036 3.240 0.037 3.180

LiteLlama 0.46B 0.901G bf16 15 0.041 1.910 0.057 1.900 gpt-sw3-356m 0.47B 1.580G bf16 15 0.035 1.160 0.035 1.180

qwen3-0.6B [67] 0.6B 1.500G bf16 15 0.113 9.660 0.367 9.880 Random-guess - - - 0.111 - 0.333 -

Our Model 2

- checkpoint2-1 0.15B 0.294G bf16 3 0.118 0.580 0.432 0.590

- checkpoint2-2 0.15B 0.294G bf16 3 0.346 0.590 0.980 0.590

- checkpoint2-3 0.15B 0.294G bf16 3 0.339 0.550 0.960 0.540

- checkpoint2-4 0.15B 0.294G bf16 3 0.346 0.860 0.990 0.550

- checkpoint2-5 0.15B 0.294G bf16 3 0.351 0.900 0.991 0.570

W

base_model-2 [23] 0.50B 0.920G bf16 15 0.120 1.504 0.970 1.811 opt-350m [66] 0.35B 0.647G bf16 15 0.037 3.960 0.038 4.090

LiteLlama 0.46B 0.901G bf16 15 0.036 2.120 0.036 2.120 gpt-sw3-356m 0.47B 1.580G bf16 15 0.036 1.070 0.036 1.260

qwen3-0.6B [67] 0.6B 1.500G bf16 15 0.111 9.870 0.980 7.860 Random-guess - - - - 0.111 - 0.333 -

Note: W→S and W denote the compression method described in Fig. 10, respectively. checkpoint1-n (n∈{1,2,3,4,5}) denotes the model trained in different training step of Model 1, checkpoint2-n’ (n’∈{1,2,3}) denotes the model trained in different training step of Model 2.

[Figure 9]

- Figure 8: Module parameter trends across different pruning ratios.

#### 4.5. Performance Comparison with Heavyweight Models

In Table 3, we present the results of emotion recognition for Qwen2-1.5B [23], InternLM2.5-1.8B [68], Qwen2.5-3B [69], and Qwen2.5-7B [69], and Internlm2.5-7B [68] and DeepSeek-R1-Distill-Qwen-1.5B [70]. Surprisingly, the results were not as impressive as expected. The reason for this is that the default setting for top-k is 50. But even if top-k is set to 1, the results are still not ideal. For the heavyweight models, their responses are more flexible due to their larger

[Figure 10]

Figure 9: The training loss of different pruning ratio (0.9, 0.8, 0.7, 0.6).

knowledge storage, allowing them to generate a wider range of answers. This also indicates that, despite the very low loss during training, which might suggest model fitting, the actual responses in specific scenarios are dissatisfactory.

Meanwhile, wealsoconductedexperimentsontheSEED and SEED-IV datasets using Compression Method 2. As

###### Performance comparison Of Heavy-Weight Models On FACED

Compression

Nine Emotion Recognition Three Emotion Recognition Method F1 (Top-K=50) Avg. RT (s) F1 (Top-K=50) Avg. RT (s)

Model Parameters Storage Size Precision Epoch

qwen2-1.5B-1 [23] 1.5B 3.091G bf16 15 0.113 3.15 0.987 3.26 Internlm2.5-1.8B-1 [68] 1.8B 3.780G bf16 15 0.111 4.26 0.931 4.95

qwen2.5-3b-1 [69] 3B 6.170G bf16 15 0.272 5.17 0.935 5.15 DS-R1-Dis-Qwen-1.5B-1 [70] 1.5B 3.55G bf16 15 0.143 15.28 0.950 14.87 qwen2.5-7b-1 [69] 7B 15.230G bf16 15 0.238 6.30 0.945 6.18 Internlm2.5-7B-1 [68] 7B 14.200G bf16 15 0.106 14.89 0.978 15.29

W→S

qwen2-1.5B-2 [23] 1.5B 3.091G bf16 15 0.117 3.48 0.993 3.03 Internlm2.5-1.8B-2 [68] 1.8B 3.780G bf16 15 0.110 15.42 0.970 4.89

qwen2.5-3b-2 [69] 3B 6.170G bf16 15 0.201 10.24 0.932 5.15 DS-R1-Dis-Qwen-1.5B-2 [70] 1.5B 3.55G bf16 15 0.156 14.28 0.970 14.43 qwen2.5-7b-2 [69] 7B 15.230G bf16 15 0.179 5.05 0.990 6.10 Internlm2.5-7B-2 [68] 7B 14.200G bf16 15 0.169 14.89 0.962 14.92

W

Random-guess - - - - 0.111 - 0.333 Compression

Nine Emotion Recognition Three Emotion Recognition Method F1 (Top-K=1) Avg. RT (s) F1 (Top-K=1) Avg. RT (s)

Model Parameters Storage Size Precision Epoch

qwen2-1.5B-1 [23] 1.5B 3.091G bf16 15 0.160 2.97 0.997 3.25 Internlm2.5-1.8B-1 [68] 1.8B 3.780G bf16 15 0.104 6.44 0.960 4.95

qwen2.5-3b-1 [69] 3B 6.170G bf16 15 0.153 5.34 0.822 5.28 DS-R1-Dis-Qwen-1.5B-1 [70] 1.5B 3.55G bf16 15 0.140 9.10 0.970 5.80

W→S

qwen2.5-7b-1 [69] 7B 15.230G bf16 15 0.226 6.24 0.960 6.14 Internlm2.5-7B-1 [68] 7B 14.200G bf16 15 0.106 14.88 0.967 15.25

Random-guess - - - - 0.111 - 0.333 -

qwen2-1.5B-2 [23] 1.5B 3.091G bf16 15 0.093 3.45 0.994 3.13 Internlm2.5-1.8B-2 [68] 1.8B 3.780G bf16 15 0.112 6.09 0.956 4.90

qwen2.5-3b-2 [69] 3B 6.170G bf16 15 0.178 9.80 0.844 5.03 DS-R1-Dis-Qwen-1.5B-2 [70] 1.5B 3.55G bf16 15 0.146 8.48 0.989 8.34

W

qwen2.5-7b-2 [69] 7B 15.230G bf16 15 0.153 6.53 0.970 6.17 Internlm2.5-7B-2 [68] 7B 14.200G bf16 15 0.168 14.95 0.967 7.46

Random-guess - - - - 0.111 - 0.333 -

Note: DS-R1-Dis-Qwen-1.5B denotes DeepSeek-R1-Distill-Qwen-1.5B.

shown in Table 4 and Table 5, this method achieves consistent performance gains under both intra-subject and crosssubject settings. Compared with unpruned models and other baselines, the proposed pruning strategy effectively reduces model size and inference latency while preserving or even improvingclassificationaccuracyonemotionrecognitiontasks. Furthermore, we use the pre-trained all-MiniLM-L6-v2 model for text representation on FACED. Specifically, we combine the “prompt” and “treatment” from each record into a single string and generate the corresponding embedding vectors. These embeddings are then subjected to K-Means clusteringandspectralclustering[72]forunsupervisedlearning, with the number of clusters set to 9. The t-SNE [71] is applied to reduce the dimensionality of the embedding and visualize the results, as shown in Fig. 11.

In addition, we investigate the clustering performance for data of compression method 1 and 2 respectively in Fig. 10 by applying the same procedure to a range of models included in Table 2 and 3. We convert the text into the appropriate input format using the tokenizer, extract the hidden states from the final layer, and apply average pooling to generate fixed-length text embedding vectors. These em-

beddings are clustered using K-Means, and dimensionality reduction is performed using the t-SNE for visualization, as shown in Fig. 12. Indeed, as illustrated in Fig. 11 and 12, the visualization suggests that corpora of two different lengths are not easily clustered. Specifically, compared to the data of Model 1, the data of Model 2 exhibits a higher degree of aggregation, which directly corresponds to a reduction in computational load.

#### 4.6. Model Fine-tuning Strategy Comparison After Pruning

To rigorously assess the effectiveness of the two finetuning strategies illustrated in Fig. 5, we employed compression method 2, as depicted in Fig. 10, as a basis for comparison. As evidenced by the results in Table 2 and Fig. 13, Strategy 1 exhibited superior performance over Strategy 2 in Table 2, particularly in the fine-tuning process of lightweight models, underscoring its efficacy in optimizing model adaptation. Besides, Additionally, we visualize the training time and GPU memory usage of various models under the two compression methods presented in Tables 2 and 3, as illustrated in Fig. 14. Building upon Compression Method 2,

Performance Comparison Of Competing Light-Weight Models and Heavy-Weight Models On SEED

Compression

Three Emotion Recognition Method F1 (Top-K=50) Avg. RT (s) F1 (Top-K=1) Avg. RT (s)

Model Parameters Storage_size Precision Epoch

Our Model

- checkpoint1 0.15B 0.294G bf16 15 0.570 0.74 0.607 0.75

- checkpoint2 0.15B 0.294G bf16 15 0.630 1.13 0.640 1.26

- checkpoint3 0.15B 0.294G bf16 15 0.710 1.10 0.720 1.03

- checkpoint4 0.15B 0.294G bf16 15 0.768 1.25 0.772 1.05

- checkpoint5 0.15B 0.294G bf16 15 0.821 1.12 0.835 0.95

W

|base_model [23] 0.50B 0.920G bf16 15 0.574 2.17 opt-350m [66] 0.35B 0.647G bf16 15 0.169 0.98 LiteLlama 0.46B 0.901G bf16 15 0.628 1.12<br><br>gpt-sw3-356m 0.47B 1.580G bf16 15 0.315 0.84 qwen3-0.6B [67] 0.6B 1.5G bf16 15 0.597 33.20<br><br>|0.537 1.65 0.193 0.95 0.640 1.16 0.337 0.81 0.601 31.73<br><br>|
|---|---|
|W<br><br>qwen2-1.5B [23] 1.5B 3.091G bf16 15 0.533 2.25 Internlm2.5-1.8B [68] 1.8B 3.780G bf16 15 0.635 3.12 qwen2.5-3b [69] 3B 6.170G bf16 15 0.573 3.67<br><br>DS-R1-Dis-Qwen-1.5B [70] 0.6B 3.55G bf16 15 0.566 38.19 qwen2.5-7b [69] 7B 15.230G bf16 15 0.581 4.42 Internlm2.5-7B [68] 7B 14.200G bf16 15 0.633 11.46<br><br>|0.521 2.12 0.640 3.23 0.605 3.07 0.571 36.17 0.596 5.22 0.637 11.63<br><br>|

Random-guess - - - - 0.333 - 0.333 -

Note: W denote the compression method described in Fig. 10, respectively. checkpointn (n∈{1,2,3,4,5}) denotes the model trained in different training step of the Our Model. DS-R1-Dis-Qwen-1.5B Denotes DeepSeek-R1-Distill-Qwen-1.5B.

Table 5 Performance Comparison Of Competing Light-Weight Models and Heavy-Weight Models On SEED-IV

Compression

Three Emotion Recognition Method F1 (Top-K=50) Avg. RT (s) F1 (Top-K=1) Avg. RT (s)

Model Parameters Storage_size Precision Epoch

Our Model

- checkpoint1 0.15B 0.294G bf16 15 0.870 1.05 0.860 1.15

- checkpoint2 0.15B 0.294G bf16 15 0.980 1.03 0.990 1.08

- checkpoint3 0.15B 0.294G bf16 15 0.990 1.02 0.995 1.12

- checkpoint4 0.15B 0.294G bf16 15 0.970 1.13 0.974 1.02

- checkpoint5 0.15B 0.294G bf16 15 0.975 1.17 0.989 1.14

W

|base_model [23] 0.50B 0.920G bf16 15 0.995 2.01 opt-350m [66] 0.35B 0.647G bf16 15 0.287 0.77 LiteLlama 0.46B 0.901G bf16 15 0.920 1.02<br><br>gpt-sw3-356m 0.47B 1.580G bf16 15 0.819 0.87 qwen3-0.6B [67] 0.6B 1.5G bf16 15 0.269 60.26|0.995 1.72 0.246 1.24 0.921 1.14 0.755 0.85 0.273 69.83<br><br>|
|---|---|
|W<br><br>qwen2-1.5B [23] 1.5B 3.091G bf16 15 0.972 2.17 Internlm2.5-1.8B [68] 1.8B 3.780G bf16 15 0.940 6.96 qwen2.5-3b [69] 3B 6.170G bf16 15 0.981 3.56<br><br>DS-R1-Dis-Qwen-1.5B [70] 0.6B 3.55G bf16 15 0.454 66.35 qwen2.5-7B [69] 7B 15.230G bf16 15 0.986 4.85 Internlm2.5-7B [68] 7B 14.200G bf16 15 0.972 12.50|0.990 2.07<br><br>0.945 7.09<br><br>0.991 3.15<br><br>0.437 45.86<br><br>0.995 4.83<br><br>0.976 12.63|

Random-guess - - - - 0.250 - 0.250 -

Note: W denote the compression method described in Fig. 10, respectively. checkpointn (n∈{1,2,3,4,5}) denotes the model trained in different training step of the Our Model. DS-R1-Dis-Qwen-1.5B Denotes DeepSeek-R1-Distill-Qwen-1.5B.

and as illustrated in Tables 2 and 3, we further evaluated the feasibility of deploying various models on edge devices. While Tables 2 and 3 report the average runtime (Avg. RT) on an NVIDIA A800 GPU, practical deployment scenarios often involve resource-constrained environments where in-

ference must be performed on CPUs alone. To this end, we deployed all models on a standard consumer-grade CPU (Intel i5-11400, 16GB RAM). The corresponding inference time and memory usage results are summarized in Table 6.

[Figure 11]

- Figure 10: Two demos of paired question and answer with EEG signal lengths of 500 time points derived from compression method 1 (W→S)) and 50 time points derived from compression method 2 (W). The doctor first asks a question to the trained model based on W→S or W. For W→S, the wavelet transform initially compresses the original signal of each channel into 500 points, then divides the compressed channel signal into 10 segments. These ten sequential group data serve as training data for W→S. For W, the wavelet transform compresses the original signal of each channel into 50 points as training data. Ans1 and Ans2 are the answers from W→S and W, respectively, while the baseline represents the real answer to the question.

[Figure 12]

- Figure 11: t-SNE [71] visualization of K-Means (A-B) and spectral clustering (C-D) results of embeddings based on the EEG signal length=500 (compression method 1) and EEG signal length=50 (compression method 2) in Fig. 10, respectively.

this, we endeavor to explore the performance of lightweight models in this context. In particular, we apply structured pruning (with a pruning ratio of 0.5) to the Qwen3-0.6B model to reduce complexity while preserving inference quality. We conduct extensive training for 25 epochs on the mental_health_counseling_conversations_sharegptdataset-MHCCS,

with 20% of the data for evaluation. Comparative experimentsinvolvingQwen3-0.6B(prunedandunpruned), Qwen31.7B, and Qwen3-4B are conducted, with performance results illustrated in Fig. 16.

### 5. Discussion and Future Work

- 5.1. Data Structure of Prompt We developed a comprehensive human-centered dataset

that integrates both public knowledge bases and specialized emotion datasets, establishing a robust data foundation for LLMdevelopment. Byleveragingeffectivepromptingstrategies, we enhanced the model’s ability to generate contextually relevant responses. While the overall model performance may not be exceptionally high, as shown in Tables 2 and 3, unsupervised clustering of language remains inherently more challenging than other data types [76]. Nevertheless, by employing a pretrained sentence transformer of an appropriate size, the model can still capture underlying emotional features to some extent, as demonstrated by the spectral clustering results in Fig. 11, despite potential feature imbalance.

- 5.2. Data Redundancy in EEG Signal Processing To address the issue of data redundancy inherent in EEG

#### 4.7. Assisted Electronic Medical Record Generation with Our Copilot

Fig. 15 presents a representative example of how our EEGEmotionCopilotcanassistingeneratingelectronicmedical records. The process begins with an initial prompt containing a starting sentence, followed by the integration of demographic information such as the subject’s age, gender, and salient facial features. Subsequently, the preprocessed and compressed EEG signals are appended to complete the prompt, which is then fed into the EEG Emotion Copilot. The model first performs multimodal analysis to generate an appropriate response, which is subsequently structured into a standardized medical record through format conversion. To further enhance clinical decision support, we leverage recent advances in inference models such as DeepSeek and Qwen3 [73, 74, 75], which have demonstrated strong performance across several reasoning tasks. Building upon

signalprocessing, weemploywavelet-basedcompressiontechniques to optimize the handling of long EEG sequences, significantly improving computational efficiency and enabling rapid emotion recognition. However, direct signal compression remains computationally intensive in many scenarios, particularly when complex affective states require informa-

[Figure 13]

- Figure 12: Clustering results of data for compression method 1 and 2 described in Fig. 10 using various models mentioned in Table 2 and 3 with K-Means clustering and t-SNE [71] visualization of the text embeddings.

[Figure 14]

- Figure 13: Performance comparison as to F1 and Avg. RT of nine and three emotion classification across steps of two finetuning strategies.

[Figure 15]

Figure 14: Comparison of Training Time and GPU Memory Usage Across Two Methods (W→S and W).

- 5.3. Patient Privacy and Model Efficiency We emphasized the importance of patient privacy by en-

suring that our model can run locally. We explored model pruning strategies to create a lightweight version of the language model, making it feasible to deploy in environments with limited computational resources while maintaining performance.

- 5.4. Performance of Lightweight Models We performed model pruning and compared the perfor-

tion from more EEG channels. To this end, recent advances suggest that large language models (LLMs) can be leveraged to generate dense, high-fidelity EEG signals from a limited number of input channels, thereby enabling efficient downstream emotion analysis [77], [78]. Furthermore, by integrating channel-aware prompts, this approach mitigates inter-subject and temporal variability in EEG data, ensuring robust and generalizable emotion recognition across diverse clinical contexts.

mance of the models obtained through the two fine-tuning methods illustrated in Fig. 5. It was found that the results obtained using Strategy 1 for fine-tuning were superior. Furthermore, as shown in Table 2 and 3, the lightweight pruned model achieved through multi-step fine-tuning demonstrated better performance compared to other models with larger pa-

[Figure 16]

Figure 15: An example using our EEG Emotion Copilot to create the assisted electronic medical record. Initially, the prompt is provided as the starting sentence, followed by the addition of the subject’s demographic information, including gender, age, and certain facial features (female, 23 years old, negative). Finally, the preprocessed and compressed EEG signal is incorporated to complete the prompt, which is then input into EEG Emotion Copilot.

###### Table 6

Comparison of inference time and memory usage among different models. Inference time is reported for both Top-𝑘 = 50 and Top-𝑘 = 1 decoding.

Model Inference Time Memory Used

Top-𝑘 = 50 Top-𝑘 = 1 (MB) ours 26.002s 60.629s 308.912

qwen2_0.5B 51.362s 132.187s 959.074 opt-350m 123.165s 173.729s 647.707 LiteLlama 74.044s 74.533s 888.567

gpt-sw3-356m 128.207s 186.361s 813.613

qwen3-0.6B 125s 437.262s 1156.125 qwen2-1.5B 155.559s 123.165s 2979.620

Internlm2.5-1.8B 434.379s 420.147s 3633.197 qwen2.5-3B 317.598s 258.132s 5943.055 DS-R1-Dis-Qwen-1.5B 322.975s 294.173s 3424.745

qwen2.5-7B 1004.48s 3283.745s 14602.636 Internlm2.5-7B 16475s 5143.517s 14830.516

rameter sizes.

- 5.5. Hallucination of Heavyweight Models While a low training loss suggests a good fit to the train-

ing data, it does not necessarily reflect the model’s true performance, as the generated responses may still fail to meet expectations or even diverge significantly [79]. This issue is particularly evident in 7B and larger models, where the

[Figure 17]

Figure 16: BLEU of Various Models on MHCCS.

hallucination problem becomes more pronounced in specialized domains. Heavyweight models, despite their extensive pre-training on general datasets like Wikitext [26] and Common Crawl [27], often struggle to adapt to the nuanced patterns of compressed EEG signals and the integration of demographic data required for accurate emotion classification and electronic medical record (EMR) generation. This is evident in their lower F1 scores for nine-emotion recognition (e.g., 0.169–0.179 for Qwen2.5-7B and Internlm2.5-7B, Table 3), which are only marginally above the random-guess baseline of 0.111. The hallucination problem is exacerbated by the models’ tendency to overfit to general language patterns, leading to outputs that are less precise in specialized contexts. For example, qualitative analysis of EMRs generated by Qwen2.5-7B revealed occasional inclusion of irrelevant treatment suggestions, such as generic recommendations not aligned with the inferred emotional state, whereas our model produced more concise and task-relevant outputs. These findings also suggest that lightweight models may be better suited for such domain-specific generation tasks.

- 5.6. Future Work Future work will focus on advancing the system’s clin-

ical applicability and accuracy. First, we plan to integrate lightweight LLMs with multimodal data, such as facial expressions, speech, and gestures, to improve the robustness and effectiveness of affective computing. Second, to streamline clinical workflows, we will develop a module to interface with hospital EMR databases or patient ID systems, automatically retrieving demographic information (e.g., gender, age) to eliminate redundant user input. Finally, to ensure clinical trustworthiness, we will implement a human-in-theloop interface for physicians to review and refine diagnostic suggestions, incorporating patient symptoms and clinical expertise, and conduct a clinical validation study to evaluate diagnostic accuracy in real-world settings. These enhancements will solidify the EEG Emotion Copilot’s role as a reliable assistive tool in medical practice.

- 6. Conclusion

In this paper, we introduce EEG Emotion Copilot, a light weight, locally-executableLLMdesignedforemotionrecognition from EEG signals and the generation of corresponding treatment plans to assist in electronic medical record management. Our findings suggest that EEG Emotion Copilot holds transformative potential in advancing emotion recognition and treatment in clinical settings, ultimately enhanc-

ing human-computer interaction and improving patient outcomes. Futureworkwillexploretheintegrationoflightweight LLMs with multimodal data, including facial expressions, speech, and gestures, to further elevate the accuracy and effectiveness of affective computing.

- review on the use of visual data in affective computing. Comput. Sci. Rev., 48:100545, 2023.
- [6] Florian Eyben, Klaus R Scherer, Björn W Schuller, Johan Sundberg, Elisabeth André, Carlos Busso, Laurence Y Devillers, Julien Epps, Petri Laukka, Shrikanth S Narayanan, et al. The geneva minimalistic acoustic parameter set (gemaps) for voice research and affective computing. IEEE Trans. Affect. Comput., 7(2):190–202, 2015.
- [7] Maja Pantic, Nicu Sebe, Jeffrey F Cohn, and Thomas Huang. Affective multimodal human-computer interaction. In Proc. Int. Conf. on Multimedia, pages 669–676, 2005.
- [8] Hamdi Altaheri, Ghulam Muhammad, and Mansour Alsulaiman. Physics-informed attention temporal convolutional network for eegbased motor imagery classification. IEEE Trans. Industr. Inform., 19(2):2249–2258, 2022.
- [9] Jesús Joel Rivas, Maria del Carmen Lara, Luis Castrejon, Jorge Hernandez-Franco, Felipe Orihuela-Espina, Lorena Palafox, Amanda Williams, Nadia Bianchi-Berthouze, and Luis Enrique Sucar. Multilabel and multimodal classifier for affective states recognition in virtual rehabilitation. IEEE Trans. Affect. Comput., 13(3):1183–1194, 2021.
- [10] Syed Umar Amin, Hamdi Altaheri, Ghulam Muhammad, Wadood Abdul, and Mansour Alsulaiman. Attention-inception and long-shortterm memory-based electroencephalography classification for motor imagery tasks in rehabilitation. IEEE Trans. Industr. Inform., 18(8):5412–5421, 2021.
- [11] Shalom Greene, Himanshu Thapliyal, and Allison Caban-Holt. A survey of affective computing for stress detection: Evaluating technologies in stress detection for better health. IEEE Consum. Electr. M., 5(4):44–56, 2016.
- [12] Soraia M Alarcao and Manuel J Fonseca. Emotions recognition using eeg signals: A survey. IEEE Trans. Affect. Comput., 10(3):374–393, 2017.
- [13] Jie Luo, Weigang Cui, Song Xu, Lina Wang, Xiao Li, Xiaofeng Liao, and Yang Li. A dual-branch spatio-temporal-spectral transformer feature fusion network for eeg-based visual recognition. IEEE Trans. Industr. Inform., 20(2):1721–1731, 2023.
- [14] Mahboobeh Jafari, Afshin Shoeibi, Marjane Khodatars, Sara Bagherzadeh, Ahmad Shalbaf, David López García, Juan M Gorriz, and U Rajendra Acharya. Emotion recognition in eeg signals using deep learning methods: A review. Comput Biol. Med., page 107450, 2023.
- [15] V Padhmashree and Abhijit Bhattacharyya. Human emotion recognition based on time–frequency analysis of multivariate eeg signal. Knowl. Based Syst., 238:107867, 2022.
- [16] Yanling An, Shaohai Hu, Shuaiqi Liu, Zeyao Wang, Xinrui Wang, and Xiaole Ma. Cross-subject eeg emotion recognition based on interconnected dynamic domain adaptation. In IEEE Int. Conf. Acoust. Speech Signal Process., pages 12981–12985, 2024.
- [17] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, et al. A survey on evaluation of large language models. ACM Trans. Intell. Syst. Technol., 15(3):1–45, 2024.
- [18] Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, Laura Gutierrez, Ting Fang Tan, and Daniel Shu Wei Ting. Large language models in medicine. Nat. Med., 29(8):1930–1940, 2023.
- [19] A Vaswani. Attention is all you need. Adv. Neural Inf. Process. Syst., 2017.
- [20] Wrick Talukdar and Anjanava Biswas. Improving large language model (llm) fidelity through context-aware grounding: A systematic approach to reliability and veracity. arXiv preprint arXiv:2408.04023, 2024.
- [21] Jonathan W Kim, Ahmed Alaa, and Danilo Bernardo. Eeg-gpt: exploring capabilities of large language models for eeg classification and interpretation. arXiv preprint arXiv:2401.18006, 2024.
- [22] YuhongZhang, QinLi, SujalNahata, TasniaJamal, Shih-kuenCheng, Gert Cauwenberghs, and Tzyy-Ping Jung. Integrating llm, eeg, and eye-tracking biomarker analysis for word-level neural state classifi-

### CRediT authorship contribution statement

Hongyu Chen: Writing–original draft, Methodology, Formalanalysis, Conceptualization, Software. WeimingZeng: Writing–review & editing, Supervision, Project administration, Fundingacquisition. ChengchengChen: Writing–review &editing. LuhuiCai: Writing–review&editing. FeiWang: Writing–review & editing. Yuhu Shi: Writing–review & editing. Lei Wang: Writing–review & editing. Wei Zhang: Writing–review & editing. Yueyang Li: Writing–review & editing. Hongjie Yan: Writing–review & editing. Wai Ting Siok: Writing–review & editing. Nizhuan Wang: Writing–review & editing, Supervision, Project administration, Funding acquisition.

### Declaration of competing interest

The authors declare that they have no competing interests.

### Data availability

The datasets are publicly available.

### Code availability

The Code will be released at https://github.com/NZWANG/EEG_Emotion_Copilot.

### Acknowledgments

This work was supported by The Hong Kong Polytechnic University Start-up Fund [Project ID: P0053210], The Hong Kong Polytechnic University Faculty Reserve Fund [Project ID: P0053738], an internal grant from The Hong Kong Polytechnic University (Project ID: P0048377), The Hong Kong Polytechnic University Departmental CollaborativeResearchFund(ProjectID:P0056428), TheHongKong Polytechnic University Collaborative Research with Worldleading Research Groups Fund (Project ID: P0058097) and theNationalNaturalScienceFoundationofChina[grantnumber: 31870979].

### References

- [1] Rosalind W Picard. Affective computing. MIT press, 2000.
- [2] Xin Hu, Jingjing Chen, Fei Wang, and Dan Zhang. Ten challenges for eeg-based affective computing. Brain sci. adv., 5(1):1–20, 2019.
- [3] Yan Wang, Wei Song, Wei Tao, Antonio Liotta, Dawei Yang, Xinlei Li, Shuyong Gao, Yixuan Sun, Weifeng Ge, Wei Zhang, et al. A systematic review on affective computing: Emotion models, databases, and recent advances. Inf. Fusion, 83:19–52, 2022.
- [4] Mimma Nardelli, Gaetano Valenza, Alberto Greco, Antonio Lanata, and Enzo Pasquale Scilingo. Recognizing emotions induced by affective sounds through heart rate variability. IEEE Trans. Affect. Comput., 6(4):385–394, 2015.
- [5] Sze Chit Leong, Yuk Ming Tang, Chung Hin Lai, and CKM Lee. Facialexpressionandbodygestureemotionrecognition: Asystematic

- cation in semantic inference reading comprehension. arXiv preprint arXiv:2309.15714, 2023.
- [23] An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2024.
- [24] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685, 2021.
- [25] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, and Haofen Wang. Retrieval-augmented generation for large language models: A survey. arXiv preprint arXiv:2312.10997, 2023.
- [26] Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. Pointer sentinel mixture models, 2016.
- [27] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. arXiv e-prints, 2019.
- [28] Ruo-Nan Duan, Jia-Yi Zhu, and Bao-Liang Lu. Differential entropy feature for EEG-based emotion classification. In Proc. 6th Int. IEEE/EMBS Conf. Neural Eng. (NER), pages 81–84. IEEE, 2013.
- [29] Jingjing Chen, Xiaobin Wang, Chen Huang, Xin Hu, Xinke Shen, and DanZhang. Alarge finer-grainedaffectivecomputingeeg dataset. Sci. Data., 10(1):740, 2023.
- [30] V Michel, L Mazzola, M Lemesle, and L Vercueil. Long-term eeg in adults: sleep-deprived eeg (sde), ambulatory eeg (amb-eeg) and long-term video-eeg recording (ltver). Neurophysiol Clin., 45(1):47– 64, 2015.
- [31] Wei-Long Zheng and Bao-Liang Lu. Investigating critical frequency bands and channels for eeg-based emotion recognition with deep neural networks. IEEE Trans. Auton. Ment. Dev., 7(3):162–175, 2015.
- [32] Irene Sturm, Sebastian Lapuschkin, Wojciech Samek, and KlausRobert Müller. Interpretable deep neural networks for single-trial eeg classification. J. Neurosci. Methods., 274:141–145, 2016.
- [33] Sana Yasin, Alice Othmani, Imran Raza, and Syed Asad Hussain. Machine learning based approaches for clinical and non-clinical depression recognition and depression relapse prediction using audiovisual and eeg modalities: A comprehensive review. Comput. Biol. Med., 159:106741, 2023.
- [34] Fatima Hassan, Syed Fawad Hussain, and Saeed Mian Qaisar. Fusion of multivariate eeg signals for schizophrenia detection using cnn and machine learning techniques. Inf. Fusion, 92:466–478, 2023.
- [35] Wei-Bang Jiang, Yansen Wang, Bao-Liang Lu, and Dongsheng Li. Neurolm: A universal multi-task foundation model for bridging the gap between language and eeg signals. arXiv preprint

- arXiv:2409.00101, 2024.

[36] Abhijit Mishra, Shreya Shukla, Jose Torres, Jacek Gwizdka, and Shounak Roychowdhury. Thought2text: Text generation from eeg signal using large language models (llms). arXiv preprint

- arXiv:2410.07507, 2024.

- [37] Shunuo Shang, Yingqian Shi, Yajie Zhang, Mengxue Liu, Hong Zhang, Ping Wang, and Liujing Zhuang. Artificial intelligence for brain disease diagnosis using electroencephalogram signals. J ZHEJIANG UNIV-SC B, 25(10):914–940, 2024.
- [38] Jagdeep Rahul, Diksha Sharma, Lakhan Dev Sharma, Umakanta Nanda, and Achintya Kumar Sarkar. A systematic review of eeg based automated schizophrenia classification through machine learning and deep learning. Front. Hum. Neurosci., 18:1347082, 2024.
- [39] Sami Barrit, Nathan Torcida, Aurelien Mazeraud, Sebastien Boulogne, Jeanne Benoit, Timothée Carette, Thibault Carron, Bertil Delsaut, Eva Diab, Hugo Kermorvant, et al. Specialized large language model outperforms neurologists at complex diagnosis in blinded case-based evaluation. BRAIN SCI, 15(4):347, 2025.
- [40] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large brain model for learning generic representations with tremendous eeg data in bci. arXiv preprint arXiv:2405.18765, 2024.
- [41] Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster,

- Silviu Pitis, Harris Chan, and Jimmy Ba. Large language models are human-level prompt engineers. arXiv preprint arXiv:2211.01910, 2022.
- [42] Abhishek Iyer, Srimit Sritik Das, Reva Teotia, Shishir Maheshwari, and Rishi Raj Sharma. Cnn and lstm based ensemble learning for human emotion recognition using eeg recordings. Multimed. Tools Appl., 82(4):4883–4896, 2023.
- [43] Heung-Il Suk and Seong-Whan Lee. A novel bayesian framework for discriminative feature extraction in brain-computer interfaces. IEEE Trans. Pattern Anal. Mach. Intell., 35(2):286–299, 2012.
- [44] Ren Li, Jared S Johansen, Hamad Ahmed, Thomas V Ilyevsky, Ronnie B Wilbur, Hari M Bharadwaj, and Jeffrey Mark Siskind. The perils and pitfalls of block design for eeg classification experiments. IEEE Trans. Pattern Anal. Mach. Intell., 43(1):316–333, 2020.
- [45] Bingxin Wang, Xiaowen Fu, Yuan Lan, Luchan Zhang, Wei Zheng, and Yang Xiang. Large transformers are better eeg learners. arXiv preprint arXiv:2308.11654, 2023.
- [46] Pavan Ramkumar, Daniel E Acuna, Max Berniker, Scott T Grafton, Robert S Turner, and Konrad P Kording. Chunking as the result of an efficiency computation trade-off. Nat. Commun., 7(1):12176, 2016.
- [47] Zangwei Zheng, Xiaozhe Ren, Fuzhao Xue, Yang Luo, Xin Jiang, and Yang You. Response length perception and sequence scheduling: An llm-empowered llm inference pipeline. Adv. Neural Inf. Process. Syst., 36, 2024.
- [48] Xuezhe Ma, Xiaomeng Yang, Wenhan Xiong, Beidi Chen, Lili Yu, Hao Zhang, Jonathan May, Luke Zettlemoyer, Omer Levy, and Chunting Zhou. Megalodon: Efficient llm pretraining and inference with unlimited context length. arXiv preprint arXiv:2404.08801, 2024.
- [49] Jonathan Frankle and Michael Carbin. The lottery ticket hypothesis: Finding sparse, trainable neural networks. arXiv preprint arXiv:1803.03635, 2018.
- [50] Zhuang Liu, Mingjie Sun, Tinghui Zhou, Gao Huang, and Trevor Darrell. Rethinking the value of network pruning. arXiv preprint arXiv:1810.05270, 2018.
- [51] Nicola Jones. Bigger ai chatbots more inclined to spew nonsense-and people don’t always realize. Nature, 2024.
- [52] Hao Li, Asim Kadav, Igor Durdanovic, Hanan Samet, and Hans Peter Graf. Pruning filters for efficient convnets. arXiv preprint arXiv:1608.08710, 2016.
- [53] Song Han, Huizi Mao, and William J Dally. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. arXiv preprint arXiv:1510.00149, 2015.
- [54] Paul Michel, Omer Levy, and Graham Neubig. Are sixteen heads really better than one? Adv. Neural Inf. Process. Syst., 32, 2019.
- [55] Ziheng Wang, Jeremy Wohlwend, and Tao Lei. Structured pruning of large language models. arXiv preprint arXiv:1910.04732, 2019.
- [56] Zechun Liu, Haoyuan Mu, Xiangyu Zhang, Zichao Guo, Xin Yang, Kwang-Ting Cheng, and Jian Sun. Metapruning: Meta learning for automatic neural network channel pruning. In Proc. IEEE Conf. Comput. Vis. Pattern Recog., pages 3296–3305, 2019.
- [57] Jinyang Guo, Weichen Zhang, Wanli Ouyang, and Dong Xu. Model compression using progressive channel pruning. IEEE Trans. Circuits Syst. Video Technol., 31(3):1114–1124, 2020.
- [58] Davis Blalock, Jose Javier Gonzalez Ortiz, Jonathan Frankle, and John Guttag. What is the state of neural network pruning? Proc. Int. Conf. Mach. Learn., 2:129–146, 2020.
- [59] Yang He and Lingao Xiao. Structured pruning for deep convolutional neural networks: A survey. IEEE Trans. Pattern Anal. Mach. Intell., 2023.
- [60] Elias Frantar and Dan Alistarh. Sparsegpt: Massive language models can be accurately pruned in one-shot. In Proc. Int. Conf. Mach. Learn., pages 10323–10337. PMLR, 2023.
- [61] Xinyin Ma, Gongfan Fang, and Xinchao Wang. Llm-pruner: On the structural pruning of large language models. Proc. Adv. Neural Inf. Process. Syst., 36:21702–21720, 2023.
- [62] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient

- foundation language models. arXiv preprint arXiv:2302.13971, 2023.
- [63] Edward H Shortliffe. The evolution of electronic medical records. Acad. Med., 74(4):414–9, 1999.
- [64] Gongfan Fang, Xinyin Ma, Mingli Song, Michael Bi Mi, and Xinchao Wang. Depgraph: Towards any structural pruning. In Proc. IEEE Conf. Comput. Vis. Pattern Recognit., pages 16091–16101, 2023.
- [65] Wei-Long Zheng, Wei Liu, Yifei Lu, Bao-Liang Lu, and Andrzej Cichocki. Emotionmeter: A multimodal framework for recognizing human emotions. IEEE Trans. Cybern., 49(3):1110–1122, 2019.
- [66] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, Todor Mihaylov, Myle Ott, Sam Shleifer, Kurt Shuster, Daniel Simig, Punit Singh Koura, Anjali Sridhar, Tianlu Wang, and Luke Zettlemoyer. Opt: Open pre-trained transformer language models, 2022.
- [67] Qwen Team. Qwen3 technical report, 2025.
- [68] Z. Cai et al. Internlm2 technical report, 2024.
- [69] Qwen Team. Qwen2.5: A party of foundation models, September 2024.
- [70] DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025.
- [71] Laurens Van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. J. Mach. Learn. Res., 9(11), 2008.
- [72] Ulrike Von Luxburg. A tutorial on spectral clustering. Stat. Comput., 17:395–416, 2007.
- [73] Sarah Sandmann, Stefan Hegselmann, Michael Fujarski, Lucas Bickmann, Benjamin Wild, Roland Eils, and Julian Varghese. Benchmark evaluation of deepseek large language models in clinical decisionmaking. Nat. Med., pages 1–11, 2025.
- [74] Mickael Tordjman, Zelong Liu, Murat Yuce, Valentin Fauveau, Yunhao Mei, Jerome Hadjadj, Ian Bolger, Haidara Almansour, Carolyn Horst, Ashwin Singh Parihar, et al. Comparative benchmarking of the deepseek large language model on medical tasks and clinical reasoning. Nat. Med., pages 1–36, 2025.
- [75] Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu, Qihui Zhang, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, et al. Trustllm: Trustworthiness in large language models. arXiv preprint arXiv:2401.05561, 3, 2024.
- [76] Vijay Viswanathan, Kiril Gashteovski, Kiril Gashteovski, Carolin Lawrence, Tongshuang Wu, and Graham Neubig. Large language models enable few-shot clustering. Trans. Assoc. Comput. Linguist, 12:321–333, 2024.
- [77] Hongyu Chen, Weiming Zeng, Luhui Cai, Yueyang Li, Lei Wang, Jia Lu, Hongjie Yan, Wai Ting Siok, and Nizhuan Wang. You only acquire sparse-channel (yoas): A unified framework for dense-channel eeg generation. arXiv preprint arXiv:2406.15269, 2024.
- [78] Yueyang Li, Weiming Zeng, Wenhao Dong, Di Han, Lei Chen, Hongyu Chen, Hongjie Yan, Wai Ting Siok, and Nizhuan Wang. A tale of single-channel electroencephalogram: Devices, datasets, signal processing, applications, and future directions. arXiv preprint arXiv:2407.14850, 2024.
- [79] Lexin Zhou, Wout Schellaert, Fernando Martínez-Plumed, Yael Moros-Daval, Cèsar Ferri, and José Hernández-Orallo. Larger and more instructable language models become less reliable. Nature, pages 1–8, 2024.

