## Integrating Biological and Machine Intelligence: Attention Mechanisms in Brain-Computer Interfaces

Jiyuan Wanga,b,1, Weishan Yea,b,1, Jialin Hea,b, Li Zhanga,b, Gan Huanga,b, Zhuliang Yuc,d, and Zhen Lianga,b,*

aThe School of Biomedical Engineering, Medical School, Shenzhen University, Shenzhen, China bThe Guangdong Provincial Key Laboratory of Biomedical Measurements and Ultrasound Imaging, Shenzhen, China cShien-Ming Wu School of Intelligent Engineering, South China University of Technology, Guangdong, China dInstitute for Super Robotics, Guangdong, China

arXiv:2502.19281v2[eess.SP]7Jul2025

### Abstract

With the rapid advancement of deep learning, attention mechanisms have become indispensable in electroencephalography (EEG) signal analysis, significantly enhancing Brain-Computer Interface (BCI) applications. This paper presents a comprehensive review of traditional and Transformerbased attention mechanisms, their embedding strategies, and their applications in EEG-based BCI, with a particular emphasis on multimodal data fusion. By capturing EEG variations across time, frequency, and spatial channels, attention mechanisms improve feature extraction, representation learning, and model robustness. These methods can be broadly categorized into traditional attention mechanisms, which typically integrate with convolutional and recurrent networks, and Transformer-based multi-head self-attention, which excels in capturing long-range dependencies. Beyond single-modality analysis, attention mechanisms also enhance multimodal EEG applications, facilitating effective fusion between EEG and other physiological or sensory data. Finally, we discuss existing challenges and emerging trends in attention-based EEG modeling, highlighting future directions for advancing BCI technology. This review aims to provide valuable insights for researchers seeking to leverage attention mechanisms for improved EEG interpretation and application.

Keywords: EEG, Brain-Computer Interface, Attention Mechanism, Transformer, Multimodal Data Fusion

### 1. Introduction

Research in brain-computer interfaces (BCIs) has long been challenged by the need to process large, complex datasets of brain signals [1]. The primary difficulty arises from the diverse and complicated nature of electroencephalography (EEG) signals, which requires efficient and effective strategies for signal analysis and modeling [2]. Attention mechanism-based models have shown exceptional promise in tackling the complexities of EEG signal processing [3]. By selectively focusing on critical information within extensive brain signal datasets, Attention models help to minimize irrelevant noise, thereby significantly improving data processing efficiency [4]. Attention mechanisms not only enhances the effectiveness of BCI research but also introduces greater flexibility and intelligence in the development of models tailored for BCI applications [5].

- 1 Equal contributions.

Preprint submitted to Nuclear Physics B July 8, 2025

|Stimulus Acquisition Electroencephalography<br><br>[Figure 1]<br><br>[Figure 2]<br><br>[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>|
|---|

Figure 1: The interaction between BCI and attention mechanisms

Attention mechanisms draw inspiration from biological visual and auditory processes, as well as cognitive processes in psychology [6]. Research has demonstrated that during visual and auditory recognition tasks, humans naturally focus on key elements while suppressing irrelevant information, thereby enhancing the accuracy and efficiency of recognition and decision-making [7]. Leveraging this principle, attention mechanisms in models, commonly referred to as attention models, are designed to assign flexible weights to different features [8]. This enables the model to concentrate on critical information pertinent to the target task while filtering out extraneous data [9]. Attention models also enhance the understanding of the relationships between input and output data, which in turn improves the model’s interpretability [10]. This enhancement not only maximizes the effective utilization of data but also reduces the impact of data variability caused by individual differences, as the model can learn to prioritize more representative features. In BCI research, these capabilities are particularly valuable, as they help enhance the accuracy of neural decoding, improve the robustness of brain modeling, and enable more adaptive and personalized brain-computer interaction [11]. Furthermore, attention models are well-suited for multimodal BCI applications, where they facilitate the efficient fusion of features extracted from different modalities [12]. As a result, the use of attention models in BCI-related research tasks holds significant potential and offers promising avenues for further exploration.

Attention models have been initially applied extensively in computer vision and natural language processing (NLP) domains, typically integrated as modules within the backbone frameworks of convolutional neural networks (CNNs) and recurrent neural networks (RNNs) [13]. In 2014, Mnih et al. [14] and Bahdanau et al. [15] introduced attention mechanisms in RNNs for image classification and machine translation tasks in NLP, respectively. The introduction of a novel self-attention mechanism by Vaswani et al. [16] in 2017, through the ”Transformer” model architecture for machine translation tasks, further propelled the use of attention models. Since then, Transformer models and their variants have been applied across various tasks [17]. For example, Dosovitskiy et al. proposed the Vision Transformer [18], demonstrating that a pure Transformer architecture could be effective for computer vision tasks without relying on CNN modules. Additionally, Liu et al. introduced the Swin Transformer [19], which utilizes a windowed self-attention mechanism to reduce the computational complexity of Transformer models. Nowadays, attention mechanisms are foundational to modern deep learning, with their flexibility and efficacy continuing to revolutionize artificial intelligence research and applications.

Building on significant breakthroughs in computer vision and NLP, attention models have also attracted substantial interest in the BCI field, catalyzing rapid progress in integrating EEG signal processing with attention mechanisms. To assess the growing interest in this area, we conduct a literature search using Google Scholar to track the number of publications since 2019. The search is performed using two keyword combinations: (1) ”attention”+”EEG”+”deep

| |
|---|

| |
|---|

Figure 2: The number of papers retrieved from Google Scholar for the two keyword combinations.

learning”, and (2) ”attention”+”EEG”+”Transformer” +”deep learning”.The searching results are presented in Fig. 2, showing the number of papers retrieved from Google Scholar for each of the two keyword combinations. In the BCI domain, attention mechanism modeling generally falls into two categories. (1) Traditional Attention Mechanism-Based Modeling. It calculates attention weights for various types of information in EEG signals, such as spatial, temporal, and spectral features, prioritizing those most relevant to the task. (2) TransformerBased Multi-Head Self-Attention Modeling. It employs multiple attention heads to simultaneously focus on different parts of the EEG data, enabling the model to capture both global and local relationships across various dimensions [20]. Furthermore, extending these two modeling strategies to multimodal applications significantly enhances the model’s ability to process and integrate information from different modalities [21]. Such integration is particularly critical for developing efficient and accurate BCI systems, as it allows for a more comprehensive understanding of the user’s intentions and mental state.

The following sections provide a comprehensive exploration of the applications of attention models in BCIs, focusing on their role in enhancing the understanding of EEG signals and advancing BCI technology. Section 2 introduces the concept of traditional attention mechanisms and categorizes their specific applications in EEG signal modeling. Section 3 details EEG signal modeling methods based on Transformer multi-head self-attention mechanisms. Given the growing popularity of multimodal models, Section 4 discusses the application of attention models in multimodal contexts. Finally, Section 5 summarizes the key points of this work and provides future perspectives on the use of attention mechanisms in EEG signal modeling.

### 2. Traditional Attention Mechanisms in EEG

Traditional attention mechanism-based modeling enhances performance and generalization by efficiently selecting features through adaptive weighting and combining different types of

information. Given input data, attention modeling dynamically computes feature weights based on prior knowledge or task-specific requirements. Depending on how these weights are applied, attention mechanisms can be broadly categorized into soft and hard attention. In the soft attention mechanism, each feature is assigned a weight that is continuously distributed between 0 and 1. These weights are differentiable, which allows them to be optimized through continuous learning within the network model [22] Compared to hard attention, where features are either entirely selected or ignored, soft attention provides a more refined weighting approach, enabling the model to learn the relative importance of features more effectively. This leads to smoother gradient flow during backpropagation, contributing to more stable and efficient training [23]. In contrast, hard attention assigns non-differentiable weights, which cannot be optimized through conventional deep learning techniques [24] Due to these limitations, hard attention is challenging to integrate directly with traditional deep learning models. Therefore, this paper will not cover or summarize research work related to hard attention mechanisms.

Building on this foundational understanding of attention mechanisms, it is crucial to explore their implementation in practical scenarios, particularly with EEG data. Attention modules can vary significantly depending on their scope and integration into the model, and analyzing these variations provides a more comprehensive understanding of their impact. To do so, we will focus on two critical aspects of attention module implementation: the specific types of attention modules used and their methods of embedding within broader model architectures.

- 2.1. Types of Attention Modules In brain modeling tasks, attention mechanisms enhance feature extraction from EEG signals

across channel, temporal, and frequency dimensions by assigning weights to highlight the most relevant information, as shown in Fig. 3.

|[Figure 8]<br><br>|[Figure 9]<br><br>[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]|
|---|---|

Figure 3: Types of attention modules in traditional attention mechanism-based modeling. The attention weights are defined as Wc = Fc(fc(Xc)) for channel attention, Wt = Ft(ft(Xt)) for temporal attention, and Wf = Ff(ff(Xf)) for frequency attention. Here, f(·) represents a transformation applied by the model to the input, and Fn(·) denotes a normalization function, commonly implemented as the softmax function in practical applications.

### (1) Channel Attention Module.

The channel attention module is designed to assess and adaptively weight the importance of individual EEG channel. The brain, as a complex biological system, relies on specialized brain regions that fulfill distinct roles while maintaining inter-regional interactions to adapt to diverse real world tasks[25]. Extensive research from neuroscience and computational studies indicates that different brain areas contribute unequally to specific cognitive functions. In BCI applications, channel attention module effectively identifies and emphasizes the most informative brain regions for tasks such as motor imagery, emotion recognition, and visual perception[26, 27, 28, 29, 30, 31, 32]. By assigning weights to EEG channels based on their task relevance, it allows models to focus on salient signals from informative channels and suppress noises from less informative channels. The most straightforward approach to implement the traditional attention mechanism to the channel dimension of electroencephalography (EEG) signals is to initialize trainable weight parameters for each channel. These weights are multiplied with the corresponding EEG input features and dynamically updated during model training, Higher weights signify greater channel importance for the task. For example, Huang et al. introduced a channel attention layer within a CNN-Bi-LSTM architecture to balance contributions of EEG channels in emotion recognition[33]. Su et al. designed a soft attention mechanism that generates channel masks by optimizing task objectives for auditory attention detection in multi-speaker scenarios[34]. Hsu et al. proposed the Deep EEG-Channel-Attention (DEC) module, which adaptively adjusts channel weights in motor imagery classification[35]. Similar efforts by Wimpff et al. and Zhang et al. further validate the utility of channel attention mechanism[36, 37]. Mathematically, given a multi-channel EEG input Xc ∈ RC×T(C denotes the number of channels and T is the number of time points), a trainable attention weight vector Wc ∈ R1×C is introduced. The weighted output Xˆc is computed as:

Xˆc = σ(Xc ⊙ Wc) (1)

where σ denotes an activation function (e.g., Sigmoid or Softmax), and ⊙ denotes element-wise multiplication.

To capture the spatial dependencies between EEG electrodes, channel attention can be integrated with Graph Neural Networks (GNNs) [38]. GNNs are particularly well-suited for EEG data due to their ability to model non-Euclidean structures, such as the irregular spatial layout of scalp electrodes. They represent EEG channels as nodes and their spatial relationships as edges in a graph. For example, Lin et al. demonstrated that retaining only 20% of EEG channels via attention-based selection within a GNN architecture yielded over 90% accuracy on the DEAP and SEED datasets. Even when limited to the top 12 channels, performance declined by only 1.3% on SEED [39]. Additional channel-specific weighting modules can be introduced prior to GNN input, further enhancing flexibility and performance[40]. The general formulation for channel attention in GNNs is as follows:

H(x) = σ(A˜ F(X ⊙ Wc)WG) (2)

Here, σ represents an activation function (e.g. sigmoid or softmax), A˜ is the adjacency matrix, F(.) is a mapping function (e.g., convolutional or fully connected layer), and Wc is a learnable GNN parameter, and the rest are as previously defined.

Recent advances in channel-specific attention mechanisms for EEG have focused on enhancing spatial modeling without relying on temporal or spectral features. By concentrating on channels associated with key brain functions, these mechanisms improve feature extraction and boost the performance of brain-computer interface systems and other neural decoding applications. A notable innovation is the use of dynamic, data-driven channel connectivity, where traditional fixed adjacency matrices based on anatomical electrode positions are replaced by adaptive graph

structures learned directly from data. This flexibility allows the model to assign edge weights via attention scores that reflect task-specific functional relevance. For example, it emphasizes frontal-parietal connections during emotional processing, which could capture context-dependent neural couplings unique to each individual or task. Another promising direction involves sparse and interpretable channel weighting through regularization techniques such as L1-norm, which encourage the selection of a minimal subset of critical channels. This reduces redundancy while aligning with established neurophysiological insights, enhancing model transparency. Hierarchical channel grouping provides further refinement by organizing electrodes into brain regions and applying attention at both inter-regional and intra-regional levels, effectively capturing multiscale spatial dependencies in neural activity. To address inter-subject variability, cross-subject adaptive attention mechanisms incorporate meta-learning or transfer learning strategies to personalize channel weighting for new individuals, leveraging common neural topologies while accommodating unique signal characteristics. Finally, lightweight attention architectures have been developed to ensure computational efficiency in real-time applications by incorporating compact modules such as bottleneck layers that select essential channels with minimal latency. Collectively, these innovations significantly advance the modeling of EEG spatial dynamics, enabling more adaptive, interpretable, and efficient neural systems.

### (2) Temporal Attention Module.

The temporal attention module is designed to effectively capture the dynamic fluctuations in brain activity over time, acknowledging that EEG signals reflect temporally varying neural states depending on the nature of the task. During task execution, cognitive processes unfold across multiple phases, with certain moments carrying higher relevance while others contribute less informative or even distracting signals. For example, in emotion recognition tasks, the onset, peak, and offset of emotional responses are distributed across distinct time points, reflecting task-specific temporal patterns[41, 42]. Findings in neuroscience and cognitive science have consistently demonstrated that different time steps in EEG signals contribute unevenly to cognitive function processing[43, 44, 45]. By assigning higher attention weights to task-relevant time intervals and suppressing irrelevant fluctuations, the temporal attention module enhances the model’s capacity to extract discriminative temporal features. It ultimately improves the robustness and precision of brain activity analysis in time-series modeling.

Due to the inherently non-stationary nature of EEG signals, two fundamental challenges arise when applying temporal attention: determining the appropriate duration of each time window and defining the optimal number of segments necessary to isolate meaningful neural responses. These parameters often vary across tasks and recording conditions, making them more complex to optimize than the fixed and predefined spatial structure seen in channel attention mechanisms. To address these issues, researchers have proposed various solutions. Jiang et al. introduced a dynamic weighting strategy for identifying key temporal fragments, demonstrating that task performance, such as emotion recognition, can be significantly influenced by the selected window length[46]. Their work suggested that optimal segment durations should be adapted based on task characteristics, such as distinguishing between structured emotional induction and natural conversation. Yang et al. developed a Gated Temporal-Separable Attention Network that leverages causal and dilated convolutions to extract multi-scale temporal features, subsequently assigning attention weights to relevant segments [47]. Beyond these examples, temporal attention has been widely applied in diverse BCI contexts, including cognitive and emotional state monitoring[48, 49] as well as motor imagery classification [50, 51]. A general representation of temporal attention in this context can be formalized as follows. Given an EEG signal vector Xt ∈ R1×T (T is the length of the temporal sequence), an attention weight vector Wt ∈ R1×(n·t) is initialized. Here, n denotes the number of time windows, and t is the length

of each window, with n · t = T. These parameters can either be fixed as hyperparameters or learned dynamically. The weighted output Xˆt is computed as:

Xˆt = σ(Xt ⊙ Wt) (3)

where σ is an activation function, and ⊙ denotes element-wise multiplication. This formulation enables the model to focus on critical time segments that are aligned with cognitive task demands. Furthermore, research in temporal attention for EEG is increasingly oriented toward dynamic, neuroscience-inspired adaptability and data-efficient unsupervised learning. One promising direction involves drawing from neural coding principles, such as the variable temporal resolution observed in biological spiking neural networks, to enable models to adjust temporal granularity in a task-sensitive manner, eliminating the need for heuristic fixed windows. Additionally, unsupervised learning approaches such as contrastive learning or masked segment prediction offer a pathway for discovering generalizable temporal patterns from large volumes of unlabeled EEG data. These methods help mitigate the limitations of scarce annotated datasets while extracting meaningful representations from latent brain dynamics. To further enhance interpretability, generative models can be used to visualize attention-aligned neural features, and causal inference techniques may uncover how specific time segments contribute to cognitive or behavioral outcomes. Together, these innovations offer a pathway toward more adaptive, efficient, and explainable EEG-based systems, with broad implications for clinical neuroscience and nextgeneration brain-computer interfaces.

### (3) Frequency Attention Module.

The frequency attention mechanism is designed to capture and enhance the spectral characteristics of EEG signals, which reflect brain activity across different cognitive and behavioral states. Frequency-domain analysis has long been recognized as a powerful approach in neuroscience and signal processing. Decades of research in neuroscience and signal processing have shown that specific frequency bands, namely δ (0.5-4 Hz), θ (4 - 8 Hz), α (8 - 12 Hz), β (13 - 30 Hz), and γ (> 30 Hz), are closely associated with distinct brain functions. In practical BCI applications, this predefined division of frequency bands is often used as prior knowledge to guide the analysis of task-related EEG features. The frequency attention module builds on this foundation by learning to adaptively assign higher weights to the most informative spectral components, such as power spectral density (PSD) or differential entropy (DE), thereby improving the extraction of features that are most relevant to tasks like auditory attention detection, motor imagery, and emotional state classification[52, 53].

In practical use, the frequency attention mechanism is typically implemented by first decomposing EEG signals into multiple sub-bands based on prior neuroscience knowledge, and then applying attention weights to each band. For example, Cai. et al. decomposed EEG into five classical frequency bands and applied dynamic weighting to identify those most relevant to auditory attention tasks[52]. This method improved detection accuracy compared to models using fixed frequency bands. Similarly, Xie et al. developed a neural model that calculates the importance scores of these frequency bands using convolutional and fully connected layers, offering an efficient solution for real-time decoding with short time windows [54]. Other studies, such as that by Chen et al. [55], extracted DE features from the five standard bands through manual preprocessing and matched them with attention weights to improve classification performance. A generalized formulation of frequency attention mechanism can be expressed as follows. Given a frequency vector XF ∈ R1×F, the signal is divided into five frequency band subsets Fδ,Fθ,Fα,Fβ,Fγ, with each processed into a common feature dimension fi, using a neural network or entropy function:

fi = function(Fi) i ∈ {δ,θ,α,β,γ} (4)

[Figure 15]

Embedding

Methods

[Figure 16]

Figure 4: Embedding Methods of Attention Modules

The resulting band-wise features are stacked into a matrix Xf ∈ R5×f, followed by the initialization of an attention weight vector Wf(f ∈ δ,θ,α,β,γ). The final frequency-aware feature representation is obtained via:

Xˆf = σ(Xf ⊙ Wf) (5)

This process ensures that the model selectively emphasizes the most relevant spectral components, enhancing its ability to extract robust and discriminative features from EEG data.

Future developments of frequency attention mechanisms may focus on improving adaptability, efficiency, and interpretability. One promising direction is to move beyond static, predefined frequency bands by incorporating data-driven frequency decomposition methods that allow the model to discover meaningful spectral patterns tailored to specific individuals or tasks. Additionally, self-supervised learning techniques such as masked frequency modeling or contrastive learning could enable the model to extract useful frequency features from unlabeled EEG data, thus addressing the common challenge of limited annotations. To enhance interpretability, future work may also integrate generative models that visualize the relationship between attention weights and neurophysiological signals, providing clearer insights into the model’s decisionmaking process. These advancements are expected to improve the flexibility and transparency of EEG analysis, reinforcing the role of frequency attention as a critical component in advanced BCI systems.

The aforementioned mentioned attention modules, including channel, temporal, and frequency, can be used individually or in combination based on the specific demands of the task. The selection and integration of these attention modules are determined by the unique characteristics of the problem being addressed. By strategically choosing the appropriate combination of attention mechanisms, researchers can effectively customize EEG signal processing and model design, providing a more adaptable and efficient solution tailored to the task’s requirements.

- 2.2. Embedding Methods of Attention Modules

In embedding attention modules, two primary approaches are employed: single attention module embedding and multi-attention module integration. The single attention module

approach thoroughly explores the internal dynamics, efficacy, and performance of a particular attention module across diverse application scenarios, providing insights into how it influences model learning and performance [8]. This allows researchers to tailor optimization strategies for specific tasks and datasets. In contrast, the multi-attention module approach integrates multiple attention modules, leveraging their complementary strengths to handle complex data more effectively [6]. This integration enhances the model’s generalization capabilities and facilitates a deeper understanding of how different attention mechanisms interact and contribute to information extraction, as illustrated in Fig. 4.

(1) Single Attention Module Embedding. In BCI modeling, embedding a single attention mechanism is widely used approach to enhance a model’s ability to focus on critical features. The key idea is to emphasize specific information dimensions (channel or temporal or frequency) by leveraging a particular type of attention mechanism, thereby improving feature extraction and recognition efficiency.

For example, embedding a channel attention module specifically enhances the model’s ability to capture important features at the channel level. Du et al. proposed the ATDD-LSTM model, which combined a channel attention module with a long short-term memory (LSTM) network. In this approach, the channel attention module was applied to feature vectors extracted by the LSTM layers, allowing the model to concentrate on channels most relevant to specific emotions while downplaying less relevant ones, which improved the accuracy of emotion recognition [56]. Although channel-level attention mechanisms in EEG analysis have shown promising results, conventional methods often flatten all channels into a uniform space when estimating their importance, disregarding the inherent spatial structure among electrodes, which may introduce bias. To overcome this limitation, Xu et al. integrated channel attention into a graph convolutional network (GCN), taking into account the spatial relationships between EEG recording electrodes [57]. Beyond channel attention, some studies focus on embedding temporal attention module to emphasize the temporal dynamics of EEG signals. Zhang et al. proposed a convolutional recurrent attention model that used CNNs to encode high-level representations and combined them with recurrent attention mechanisms (including LSTM networks and temporal attention modules). This method calculated attention weights on dynamic temporal features, allowed the model to focus on the most informative time periods, and extracted more valuable temporal information [58]. Traditional temporal attention modules typically rely on a purely data-driven learning paradigm, where the model autonomously identifies significant temporal segments. However, incorporating prior knowledge to guide the learning process can help the model identify key temporal patterns more efficiently. For example, inspired by the psychological peak-end rule, Kim et al. developed a model that integrated a bidirectional LSTM network with a temporal attention module. It assigned greater weight to emotional states occurring at key moments, capturing the dynamic variability of emotions over time and enhancing the model’s interpretability [59]. For frequency-domain features, frequency attention is rarely modeled in isolation. Instead, it is typically integrated with spatial and temporal features to enhance EEG signal representation.

While embedding a single attention module can effectively improve performance in specific tasks, several challenges remain. Choosing the right attention module is crucial. Determining how to integrate it optimally into the model framework for different scenarios is also important. Additionally, understanding how the placement of the attention layer affects model performance requires further exploration. Researchers need to carefully assess both the model architecture and the task requirements to design an optimal embedding strategy.

(2) Multi-Attention Module Integration. Embedding multiple attention modules helps overcome the limitations of single attention module embedding by enabling the model to

simultaneously capture various aspects of different feature dimensions. This approach enhances the model’s capacity to learn diverse and informative features, thereby improving its robustness and generalization capabilities. Consequently, transitioning from single to multiple attention embedding is a natural step to better manage the complexity of real-world EEG data.

For example, Tao et al. proposed a deep learning model that incorporated both channel attention and inter-sample attention mechanisms. Since the samples were segmented based on time, the inter-sample attention effectively functioned as temporal attention. This approach enabled the model to effectively prioritize significant information across different channels and temporal segments for feature extraction [28]. Besides of the aforementioned method, Cai et al. introduced a dynamic attention mechanism that assigned different weights to different frequency sub-bands and channels of EEG signals [52]. This dynamic approach optimized feature representation and was applied within an adaptive decoding framework for complex downstream tasks. Additionally, to better capture the spatial relationships among EEG electrode channels, Jia et al. ’s GraphSleepNet [60] and Zhang et al. ’s hierarchical attention network based on graph structures [61] both utilized GCNs to model the spatial relationships of EEG electrodes. These approaches leveraged attention mechanisms across both time and space, significantly enhancing performance in tasks such as sleep stage classification and movement intention prediction. To extract information from EEG signals in a more comprehensive manner, a number of studies have implemented attention mechanisms across all three dimensions (channel, temporal and frequency). However, expanding attention to multiple dimensions requires careful architectural design to ensure a balanced and effective focus across them. Extending beyond channel and temporal information, Jia et al. introduced a spatio-temporal-spectral attention dense network that simultaneously considered temporal, frequency, and spatial features. This model adaptively captured crucial information across brain regions (spatial, i.e., channels), frequency bands (spectral), and time, providing a comprehensive feature extraction framework [49]. Xiao et al. extended Jia et al.’s model by proposing a neural network based on 4D attention [53]. In this approach, the channel dimension of the input samples is transformed into a two-dimensional feature to preserve the spatial positional information of the EEG signal electrodes, while also incorporating the time and frequency dimensions. It computed spatial attention (addressing the spatial positional relationships between channels) and frequency attention (applied to power spectral density and differential entropy features). These attention weights were then applied to refine the input, resulting in enhanced output features. Jia et al. ’s and Xiao et al. ’s models both leveraged temporal, frequency, and spatial characteristics of EEG channels, calculating attention weights across these dimensions to enhance the model’s focus on information pertinent to specific tasks. The main difference between their approaches lies in how they calculated attention weights and structured their models. Jia et al. computed attention separately across the frequency and time dimensions in parallel, and then merged these features for classification. In contrast, Xiao et al. integrated all dimensions into a unified 4D representation before computing attention, providing a different approach to capture feature interdependencies. While Jia et al. ’s dual-stream framework excels in modular feature extraction, it may miss cross-dimensional dependencies. In comparison, Xiao et al. ’s integrated 4D strategy enables holistic feature learning but introduces greater model complexity. The choice between these approaches depends on the dependency structure of the task: Jia et al. ’s method is more suited for problems where temporal and spectral features are relatively independent, whereas Xiao et al. ’s model is preferable when multi-dimensional interactions are crucial.

A crucial aspect of applying attention mechanisms is defining the shape and dimensions of the input feature matrix. In previous research, attention weight computations have predominantly relied on the strict Euclidean geometric space of the feature matrix. However, given the

Table 1: Embedding methods of attention modules in the literature.

Ref Year Embedding style Backbone Task Dataset

- [61] 2019 Channel, Temporal CNN, GCN Movement decoding PhysioNet

- [58] 2019 Temporal CNN, LSTM Movement intention recognition BCI IV-2A

- [56] 2020 Channel LSTM Emotion recognition DEAP, SEED, CMEED [60] 2020 Channel, Temporal GCN Sleep stage recognition MASS-SS [28] 2020 Channel, Temporal RNN Emotion recognition DEAP, DREAMER

[59] 2020 Temporal LSTM, CNN Emotion recognition DEAP [49] 2020 Channel, Temporal, Frequency CNN Emotion recognition SEED, SEEDIV

[62] 2020 Temporal, Frequency LSTM,CNN Emotion recognition

SEED-VIG, SEED, BCI IV-2A, BCI IV-2B

- [34] 2021 Channel CNN Auditory attention detection KUL

- [52] 2021 Channel, Frequency CNN Auditory attention detection KUL, DTU [27] 2021 Channel, Frequency CNN Motor imagery BCI IV-2A, BCI IV-2B, HGD
- [53] 2022 Channel, Temporal, Frequency LSTM, CNN Emotion recognition DEAP, SEED, SEEDIV [26] 2023 Channel, Temporal CNN Motor imagery BCI IV-2A, Custom

[57] 2023 Channel GCN Emotion recognition SEED, SEEDIV

- [35] 2023 Channel CNN Motor imagery BCI IV-2A,BCI IV-2B, 2020BCI Track#1

- [63] 2024 Channel CNN Motor imagery BCI IV-2A, BCI IV-2B, HGD, BCI III-4A
- [64] 2024 Channel, Temporal CNN RSVP Tsinghua RSVP
- [65] 2025 Channel CNN Motor imagery BCI IV-2A, BCI IV-2B, HGD
- [66] 2025 Temporal CNN Motor imagery BCI IV-2A, BCI IV-2B

Table 2: Transformer-based embedding methods in the literature.

Ref Year Embedding style Backbone Task Dataset

- [67] 2020 Temporal Transformer Sleep stage recognition MASS, Sleep-EDF
- [68] 2021 Temporal, Channel Transformer Motor imagery BCI IV-2A, BCI IV-2B
- [69] 2022 Frequncy, Temporal Transformer Seizure prediction CHB-MIT, Kaggle datasets
- [70] 2022 Channel Transformer Emotion recognition SEED
- [71] 2022 Temporal, Channel Transformer Visual discomfort induces Private datasets
- [72] 2022 Temporal, Channel Transformer Motor imagery PhysioNet
- [73] 2024 Channel, Temporal Transformer Emotion recognition DEAP, SEED, THU-EP
- [74] 2024 Channel, Frequncy Transformer Emotion recognition Private datasets, SEED, SEED-IV
- [75] 2024 Temporal, Channel, Frequncy Transformer Emotion recognition, Motor imagery BCI IV-2A, BCI IV-2B, SEED
- [76] 2025 Temporal, Channel Transformer Cognitive attention classification A publicly accessible EEG dataset
- [77] 2025 Temporal Transformer EEG event recognition, epilepsy seizure detection TUEV, TUAB, IIIC Seizure, CHB-MIT

brain’s complex topological structure, using Euclidean space alone may not accurately capture its underlying properties. Consequently, several studies have sought to align feature matrix definitions more precisely with the brain’s physiological structure by incorporating non-Euclidean space representations within attention mechanisms. For example, Zhang et al. introduced the concept of manifolds, proposing a time-frequency domain feature learning model that integrated both Riemannian manifold and Euclidean space representations. Their work demonstrated the effectiveness of attention mechanisms in synthesizing feature information across different mathematical domains [62].

These studies collectively highlight the crucial role of attention mechanisms in enhancing the performance of EEG signal processing models, especially in terms of accuracy and efficiency of feature extraction. By calculating attention weights across multiple dimensions, such as channel, temporal, and frequency, and either integrating or applying them independently, these models offer more refined and effective solutions to address the complexities of EEG signal processing.The relevant literature we have reviewed is summarized in Table 1.

### 3. Transformer-based Multi-Head Self-Attention Mechanisms in EEG

The Transformer model, first proposed by Vaswani et al. in 2017 [16], introduced a selfattention mechanism that revolutionized machine translation tasks. The Transformer architecture is composed of encoder and decoder modules, which are built by stacking multiple sub-layers, including self-attention, feed-forward neural networks, residual connections, and normalization layers [16, 78]. This composition enables the model to effectively encode input

sequences and generate outputs, with the self-attention mechanism at its core enhancing the ability to capture contextual and temporal relationships [79].

Since then, the Transformer and its variants have seen widespread application across fields such as natural language processing, and computer vision [80]. The core strength of the Transformer lies in its capacity to capture long-range dependencies and interactions among input features, making it particularly effective for time series modeling and also achieving significant advancements in temporal signal processing task. Table 2 summarizes a survey of studies that employ the transformer architecture. For example, AST [81] utilized a generative adversarial encoder-decoder framework to train a sparse Transformer model for time series prediction. It demonstrates that adversarial training can enhance time series prediction by directly shaping the network’s output distribution to mitigate error accumulation during one-step-ahead inference. FEDformer [82] applied attention mechanisms in the frequency domain using Fourier and wavelet transforms, achieving linear complexity by randomly selecting a fixed-size subset of frequencies. It is noted that FEDformer’s success has spurred increased interest in exploring the self-attention mechanism in the frequency domain for time series modeling [83].

- 3.1. Multi-Head Self-Attention Mechanisms

The self-attention mechanism, also known as ”Scaled Dot-Product Attention” [84], offers a significant advantage over traditional attention models. It captures contextual relationships effectively, especially in long sequences. This helps overcome challenges like information loss and long-term dependencies. Self-attention analyzes correlations between positions in the input sequence, making it more efficient than CNNs and RNNs for sequence modeling.

In the Transformer model, self-attention is implemented using three matrices: Query (Q), Key (K), and Value (V ). These matrices are derived from the input feature matrix I ∈ RL×D, where L is the sequence length and D is the feature dimension. The matrices Q, K, and V are obtained by applying linear transformations to I:

Q = I ⊗ WQ, (6) K = I ⊗ WK, (7) V = I ⊗ WV , (8)

where WQ ∈ RD×D

#### , WK ∈ RD×D

#### , and WV ∈ RD×D

are trainable weight matrices. The self-attention layer then calculates attention weights and the output:

v

k

k

QKT √Dk

A = softmax(

). (9)

Attention(Q,K,V ) = AV. (10) To allow multiple self-attention processes to run in parallel, the multi-head attention

mechanisms is suggested. For H self-attention heads, the output of the multi-head attention is: MultiHeadAttn(Q,K,V ) = Concat(head1,...,headH)WO, (11)

where WO is a trainable weight matrix. This ensures the output size matches the input. The multi-head approach allows the model to focus on different parts of the sequence simultaneously. This enriches the representation and improves model performance.

| | |
|---|---|
| | |

| |
|---|

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |

Figure 5: Multi-Head Self-Attention Module

- 3.2. Strategies for Applying Transformers

In practical applications, the complete Transformer architecture is not always necessary for every task. Many models modify specific Transformer components or integrate elements into existing frameworks. Broadly, Transformer applications can be categorized into three main strategies [80].

(1) Encoder-Decoder Combination. This strategy suits sequence-to-sequence tasks, where the input sequence is processed by an encoder and then decoded into a target sequence. This approach addresses long-range dependencies by fully leveraging contextual information. While this method increases model complexity and requires more parameters, longer training times, and larger datasets, it generally yields improved performance.

- (2) Encoder Only. Used for non-sequence-to-sequence tasks, this strategy employs only

the encoder to convert the input sequence into a specialized representation for subsequent processing. By simplifying the model structure and reducing parameters and training time, it provides a more efficient approach. However, the encoded representation may lack the depth of contextual information needed for complex sequence generation tasks.

- (3) Decoder Only. Typically paired with a pre-trained encoder module, this strategy is

ideal for generative tasks. The decoder, utilizing self-attention, generates the target sequence based on the representations from upstream tasks. This setup captures comprehensive contextual information, though it may increase time complexity.

In BCI applications, the core benefit of Transformers lies in the self-attention mechanism, essential for capturing temporal correlations and performing effective feature encoding. Consequently, BCI applications frequently implement either the encoder or encoder-decoder strategy, with self-attention as a pivotal component for handling EEG-based tasks.

- 3.3. Practical Applications of Transformer Models in EEG Analysis

The use of Transformer-based self-attention mechanisms shows great potential for enhancing EEG modeling. These mechanisms help capture relevant information from complex, non-

stationary EEG signals. We introduce EEG modeling with Transformers in three areas: temporal, spatial, and combined temporal-spatial.

- (1) Application in Temporal Dimension. In the temporal domain, researchers have increasingly adopted hybrid models such as CNN-Transformer and LSTM-Transformer to extract informative temporal representations from EEG signals [85]. Enhancements to the self-attention mechanism have significantly improved the models’ ability to capture evolving neural patterns and temporal dynamics. Qu et al. [67] proposed a residual-based attention model for sleep staging, treating 30-second EEG epochs as fundamental processing units. The model’s decoder utilized a multi-head self-attention mechanism, enriched with sinusoidal positional encoding, to retain the sequential structure of sleep transitions. By embedding residual blocks within the encoder for feature extraction and adopting parallelizable self-attention operations, the model effectively captured inter-epoch dependencies (e.g., sleep stage shifts) while mitigating the sequential processing limitations inherent in LSTM architectures. This design achieved a 12× acceleration in training speed, enabling efficient large-scale sleep data processing. Additionally, the model performed multi-scale frequency decomposition using Hilbert-transform-inspired pooling, and directly operated on raw EEG inputs in an end-to-end architecture, thus eliminating reliance on handcrafted preprocessing. Complementing this work, Li et al. [69] introduced the Transformer-guided CNN (TGCNN) for epilepsy prediction, featuring a novel squeezed multihead self-attention (SMHSA) module. Unlike standard Transformer attention, SMHSA applied depth-wise convolutions to downsample the Key and Value matrices, reducing computational cost by a factor of four, while incorporating learnable bias terms to improve positional encoding. The model employed an alternating CNN-Transformer structure, in which CNN layers first extracted local time-frequency patterns from STFT-based spectrograms, followed by SMHSA modeling of long-range temporal dependencies. This allowed the model to capture both fine-grained waveform details (e.g., seizure spikes) and broader temporal trends (e.g., pre-ictal changes), achieving a robust balance between local feature resolution and global contextual awareness. While Qu et al. focused on optimizing training efficiency and temporal transition modeling for regular and stable sleep stages, Li et al. targeted computational scalability and feature complementarity to detect rare, transient epileptic events. However, each approach has its trade-offs: Qu’s reliance on fixed-length epochs may limit modeling of ultra-long temporal dependencies, whereas Li’s use of STFT preprocessing could result in loss of raw phase information. Together, these studies underscore the importance of task-specific adaptations of self-attention (such as residualenhanced encoding in Qu’s model and compressed attention in Li’s architecture) in optimizing EEG temporal modeling. Future research directions may include the integration of adaptive temporal windows, multi-resolution temporal attention, or self-supervised pretraining to improve generalization across diverse EEG analysis tasks.
- (2) Application in Spatial Dimension. Inspired by the Vision Transformer (ViT) model for image processing, researchers have developed innovative neural network models tailored for spatial feature analysis in EEG signals. For example, Guo et al. proposed a model called the Deep Convolutional and Transformer Network (DCoT) [70], focusing on the importance of each EEG channel in emotion recognition and visualizing these features. Based on the extracted differential entropy features, EEG signals were formed in a three-dimensional representation (Time × Channel × Frequency), which is similar to RGB representation in image. Inspired from ViT structure, DCoT was designed to analyze correlations between EEG electrodes, with each Transformer token representing a specific EEG electrode channel. The model applied positional encoding to the input tokens (i.e., EEG channels) and introduced an additional token dedicated to classification. After processing the encoded signals through the Transformer encoder module, a fully connected layer generated the final classification results. Furthermore, Zheng et al.

proposed a Copula-Based Transformer model (CBT) [71], designed to learn spatial dependencies between EEG channels while optimizing classification performance. By reducing the size of the attention matrix, CBT lowered dependency on large datasets, improving computational efficiency. The CBT model excelled in an EEG-based visual discomfort assessment task, pioneering the revelation of temporal characteristics in EEG signals linked to visual discomfort. These studies underscore that Transformer-based self-attention mechanisms effectively capture the spatial dynamics of EEG signal sequences, enhancing spatial information processing and optimizing model training efficiency and accuracy. These studies illustrate two complementary strategies for integrating spatial information into Transformer-based EEG models. DCoT adopts a data-driven self-attention paradigm, enabling the dynamic discovery of inter-channel correlations, and is particularly well-suited to applications demanding interpretability, such as emotion recognition with spatial brain mapping. In contrast, CBT leverages structured priors via copula functions to explicitly encode electrode positioning, which is advantageous in scenarios characterized by limited data availability and region-specific neural responses, such as visual discomfort detection. While both approaches validate the effectiveness of self-attention for spatial feature modeling, future research could explore hybrid frameworks that combine physiological priors (e.g., brain connectivity graphs, cortical maps) with adaptive attention mechanisms. Such integration may further enhance the generalization capability of EEG-based models across diverse cognitive and clinical tasks, especially when spatial specificity is critical.

### (3) Application in Combined Temporal and Spatial Dimensions.

Researchers have leveraged the powerful capabilities of the Transformer self-attention mechanism to simultaneously capture both the temporal and spatial dimensions of EEG signals, enabling the extraction of highly discriminative features. For example, Song et al. [68] developed an EEG decoding model that primarily relies on the Transformer’s self-attention layers to enhance feature representations in both dimensions. In the spatial transformation component, the self-attention mechanism weighted each channel, emphasizing signals with higher relevance. Meanwhile, the temporal transformation component employed convolutional layers to encode temporal features, with channel compression and sample segmentation steps to reduce computational load. Finally, global average pooling and fully connected layers were combined to classify EEG signals effectively. Similarly, Du et al. proposed an EEG spatio-temporal Transformer network [72], which introduced Temporal Transformer Encoder (TTE) and Spatial Transformer Encoder (STE) modules to independently capture temporal and spatial features. In the TTE, temporal attention mechanisms calculated correlations among sampling points within each sample, extracting temporal features. Since channel correlations are often unique to individuals, the STE calculated spatial attention among channels and applies positional encoding to retain spatial location information. This allows the model to capture inter-channel relationships more accurately, improving its ability to identify individuals based on unique EEG patterns. Additionally, Si et al. [73] proposed integrating the Selective Kernel (SK) attention mechanism with the Transformer self-attention mechanism to identify and select the channels most relevant to the current task. This approach enables the model to filter out noise and irrelevant signals, simplifying the processing of complex temporal information. Once the SK attention mechanism isolated key channels, the Transformer encoder module deeply extracted temporal features from these selected channels. This approach’s strength lies in its ability to focus on the most informative parts of the data while preserving sensitivity to temporal dependencies, a critical factor for managing complex tasks in BCIs. These studies demonstrate that an incorporation of both temporal and spatial information can significantly enhance the accuracy and efficiency of EEG signal analysis. A critical factor for managing the variability and complexity of real-world BCI scenarios. Together, these studies illustrate the advantages of

incorporating both temporal and spatial information within Transformer-based EEG models. Each approach presents task-specific strengths. Si et al. enable robust emotion recognition via hierarchical attention. Song et al. achieve efficient motor imagery decoding with lightweight slice-based self-attention. Du et al. enhance person identification using spatio-temporal encoders and positional encoding. These works highlight the growing trend of leveraging modular attention architectures to tailor EEG decoding strategies for diverse BCI applications.

### 4. Attention Models for Multimodal Applications

To improve the accuracy of EEG signal recognition, recent studies have gradually introduced multimodal data (such as speech, images, text, etc.) to be jointly trained with EEG signals (as shown in Fig. 6). By leveraging traditional attention mechanism modeling strategies or Transformer-based multi-head self-attention mechanism modeling strategies, these approaches achieve effective fusion of signals from different modalities, enhancing the accuracy and stability of recognition. As multimodal applications in brain modeling continue to expand, the ability to efficiently utilize information from each modality becomes increasingly critical.

At the current stage, multimodal tasks face two core challenges: (1) effectively fusing multimodal data and (2) facilitating better interaction between different modalities. The key to the first challenge lies in assessing the importance of each modality for a given task and assigning appropriate weights to generate a unified feature representation for downstream processing. The selection of these weights significantly impacts model performance. Traditionally, this process relies on manual tuning, which is both time-consuming and suboptimal. In contrast, automated weight optimization not only improves efficiency but also enhances model performance. This is typically achieved by incorporating attention models that introduce an attention parameter matrix to dynamically adjust weight distribution. Attention modeling can be broadly categorized into traditional attention mechanisms and Transformer-based self-attention strategies. The latter emphasizes capturing complementary and shared information between modalities, ensuring that the information from one modality is reflected in another. For example, in cross-modal generation tasks using diffusion models, cross-attention mechanisms are often employed to facilitate information exchange and allocate importance between modalities.

|[Figure 17]<br><br>[Figure 18]<br><br>Multim|[Figure 19]<br><br>odal|
|---|---|
|[Figure 20]<br><br>Applic|[Figure 21]<br><br>ations|

Figure 6: Attention Modules for Multimodal Applications

The second challenge focuses on improving interactions between different modalities, ensuring seamless information exchange across data sources. A major difficulty arises from the heterogeneous nature of multimodal data, where differences in feature distributions, temporal alignment, and semantic relevance must be addressed. To tackle this, recent studies have introduced contrastive learning [86], cross-modal attention [87], and graph-based approaches [88] to establish meaningful associations between modalities. These methods enhance feature complementarity and reduce modality gaps, ultimately improving model robustness and generalization. Furthermore, explicit modeling of inter-modality dependencies through techniques such as mutual information maximization [89] and self-supervised learning strengthens interactions [90], allowing each modality to contribute more effectively to the overall task performance.

- 4.1. Application of Attention Mechanisms in the Fusion of EEG Signals with Multimodal Data In multimodal emotion recognition tasks, Liu et al. employed two modality fusion strategies:

a basic weighted fusion method and an attention-based fusion method [91]. In the basic weighted fusion approach, the weight coefficients for each modality were manually adjusted, and the weighted sum of data from different modalities was computed to generate a fused output. The fusion process was represented as:

O = α1O1 + α2O2. (12)

Here, α1 and α2 represented the weight coefficients assigned to different modalities, satisfying α1 + α2 = 1. The model’s performance was thoroughly evaluated by manually testing various combinations of α1 and α2. In the attention-based fusion method, although a weighted summation formula was still used to obtain the fused feature O, in solving for α1 and α2, the authors first initialized an attention layer, which was then optimized through the network. The final attention weights, α1 and α2, were derived from the softmax function applied to the attention layer’s output. This approach allows the model to adaptively adjust the attention weights, dynamically learning an optimal set of weight parameters. This work attempts to enhance multimodal fusion by incorporating adaptive weight coefficients. It systematically compares traditional manual weighting with an attention-based dynamic adjustment strategy, ultimately demonstrating improvements in both performance and robustness for multimodal emotion recognition. These findings further support the application potential of multimodal analysis in BCI systems. However, the model architecture was restricted to the fusion of only two modalities, and the employed attention mechanism was relatively simple in design. On the other hand, Qiu et al. designed a more complex attention structure. They developed a correlation attention network that effectively integrated eye movement and EEG signals for fusion analysis. The unique aspect of the correlation attention network is that it not only computed attention weights for the two modalities but also adopted the canonical correlation analysis (CCA) method from statistics. This analysis method generated a cross-correlation coefficient matrix C by calculating the cross-correlation between outputs of each recurrent unit in the bidirectional gated recurrent unit (GRU) layer. Utilizing this matrix along with the average features extracted by the bidirectional GRU, the fusion feature matrix F was constructed to determine the attention weights. The computation followed a structured process. The attention score uit at each time step was derived as

uit = tanh(Ww1fit + Ww2cit + bw) (13) The attention weights for each time point were obtained by normalizing the attention scores using the softmax function αit, as

exp(uTit) t exp(uTit)

αit =

(14)

The final attention-weighted output si was computed as follows: si =

αithit (15)

t

Here, fit and cit represented elements from the fusion feature matrix F and the cross-correlation coefficient matrix C, respectively. Ww1, Ww2, and bw were trainable weight parameters. This approach effectively combined the complementarity of multimodal data with statistical correlation analysis, introducing an innovative attention mechanism for multimodal tasks. This not only enhances the model’s efficiency in understanding and utilizing multimodal data features but also demonstrates how traditional attention mechanisms can be extended and improved through statistical analysis methods.

Recent studies have pointed out that traditional multimodal fusion approaches tend to focus solely on integrating various types of physiological signal features. A novel and increasingly promising direction involves combining human statistical data (such as demographic information) with physiological signals from the brain. This integration provides a richer and more holistic understanding of brain activity and is expected to significantly advance the performance and applicability of BCI systems. Zhang et al. proposed a multimodal neural network model for integrating demographic data and EEG signals [92]. This model incorporated an attention mechanism to effectively combine the two data types, aiming to uncover complex relationships between EEG signals and demographic factors. Such integration is particularly valuable for applications like depression detection, where demographic information can provide crucial contextual insights. The model first used a one-dimensional CNN to process EEG signals, resulting in a feature matrix Z ∈ RC

out×m, while demographic data were encoded as a feature vector S ∈ Rd. The two data types were fused through an attention mechanism, with the calculation as follows:

A = tanh((WfeZ + bfe) ⊕ (WdeS + bde)). (16)

Here, Wfe and bfe were trainable weights and biases related to EEG signal features. Wde and bde were weights and biases related to demographic features. The symbol ⊕ represented the fusion operation between the two modalities. This approach enhances the integration of demographic data and EEG signals by leveraging attention mechanisms, helping to mitigate the impact of individual differences on model performance. By dynamically adjusting the influence of demographic information, the model achieves a more effective and personalized feature representation, improving the accuracy of multimodal analysis.

Furthermore, Choi et al. proposed a multimodal attention network to explore the fusion of facial video and EEG signals [93]. Unlike traditional methods that rely on a single fusion layer, this network utilized multimodal fusion layers incorporating bilinear and trilinear pooling to extract and integrate deep features. This approach not only enhances the integration of features from both modalities but also improves model performance by dynamically allocating attention weights, enabling more effective cross-modal information exchange.

Recently, Transformer-based multi-head self-attention mechanisms have become a prevalent approach in multimodal data fusion, enabling efficient processing and integration of features from diverse modalities. In the model framework, each token received by the Transformer encoder corresponds to a specific modality, allowing the model to effectively capture and integrate information at the feature level. By leveraging complex inter-modal interactions, the self-attention mechanism uncovers intrinsic relationships and complementary information between modalities, dynamically refining feature representations. A well-known example is the MMASleepNet model [94], which not only incorporated the concept of the Squeeze-and-Excitation (SE) module from SENet [95] but also integrated the advantages of the Transformer encoder

module. To enhance the utilization of multimodal collaborative information, researchers typically employ a two-stage attention mechanism: first, applying attention modules to extract modalityspecific features from individual modalities, followed by integrating cross-modal information through another layer of attention during fusion. This strategy, which combines hierarchical attention mechanisms, has demonstrated remarkable effectiveness in BCI tasks. For instance, He et al. proposed the EEG-EMG FAConformer framework[96], which leverages self-attention modules to hierarchically extract critical features from EEG and EMG(electromyography) signals. By further incorporating cross-modal attention for fusion, this approach achieves robust performance and enhanced classification accuracy, as evidenced by its superior stability and generalization capabilities in experimental evaluations. Another interesting research work by Wang et al. proposed a cross-modal fusion model to combine EEG signals with textual data for enhancing emotion detection in English writing[97]. The model utilizes the self-attention mechanism of the Transformer architecture to dynamically fuse EEG signals and textual features, addressing the limitations of traditional methods in leveraging the complementary information between textual and physiological signals.

- 4.2. Application of Attention Mechanisms in Information Interaction Between EEG Signals and Multimodal Data

Compared to self-attention, cross-attention extends its functionality by integrating information from multiple modalities, enabling more precise modeling of inter-modal associations [98]. When the query (Q) matrix and the key (K) and value (V) matrices originate from different modalities, the computation shifts from capturing intra-modal correlations to establishing inter-modal relationships, effectively transforming self-attention into cross-attention [99]. Also referred to as cross-modal attention, this mechanism introduces additional input sequences from distinct modalities, enhancing information fusion and improving the overall representation of multimodal data [100][101].

In EEG-related research, visual reconstruction from EEG signals is a particularly challenging yet rapidly evolving field. The objective is to decode the information embedded in EEG signals and use it to reconstruct corresponding visual stimuli. This process requires capturing the intricate relationships between EEG and visual modalities, often achieved through crossattention mechanisms. By computing the relevance between EEG segments and visual data, EEG signals serve as conditioning inputs to guide the generation of visual stimuli. A wellknown example is the DreamDiffusion model [102], which employed an EEG encoder trained on large-scale EEG data using a masking strategy to enhance feature extraction. The extracted EEG features then conditioned the Stable Diffusion model to generate images. Within Stable Diffusion, the cross-attention mechanism computes correlations between EEG-derived and image-derived features, enabling coherent information exchange between the two modalities. The cross-attention mechanism employed in Stable Diffusion model has been widely adopted in EEG-to-image guided reconstruction tasks, such as in works like[103, 104]. The mathematical formulation of cross-attention can be expressed as follows:

Q = WQ(i) · φi (zt),K = WK(i) · τθ(y),V = WV(i) · τθ(y). (17) Here, φi (zt) ∈ RN×die is the output of the noise prediction model Unet, and τθ(y) ∈ RM×d

is the encoded representation obtained by projecting the EEG features output from the EEG encoder through an additional layer. WV(i) ∈ Rd×diϵ,WQ(i) ∈ Rd×d

τ

#### ,and,WK(i) ∈ Rd×d

are learnable parameters. In this setup, the Q matrix is derived from image data, while the K and V matrices are derived from EEG signals. By substituting these Q, K, and V matrices into the self-attention computation formula, the attention score matrix is obtained, leading to the output of the

τ

τ

cross-attention mechanism. This process facilitates effective information interaction between EEG and image modalities, enabling more precise multimodal feature integration.

- 4.3. Comparison of Transformer-Based Cross-Attention and Traditional Attention in EEG Multimodal Applications

Traditional attention mechanisms and Transformer-based cross-attention have both been applied in EEG multimodal fusion tasks. In recent years, Transformer-based approaches have increasingly become the mainstream. Traditional attention retains limited advantages in computational efficiency and parameter compactness, often using fewer parameters, which suits real-time BCI and low-resource clinical applications[105]. However, Transformer-based models demonstrate superior overall performance. For example, the Dual-Branch Transformer with Cross-Attention (DTCA) achieves state-of-the-art results on SEED and SEED-IV datasets by encoding EEG and eye movement data with sophisticated query-key-value relationships[106]. In more complex scenarios involving a greater number of modalities, Transformer-based crossattention mechanisms also demonstrate strong performance. For example, Ying et al. developed a method that integrates EEG, audio, and video, advancing the incorporation of EEG into more complex multimodal systems[107]. Notably, researchers are actively exploring lightweight Transformer architectures. In the future, significant improvements in the computational efficiency of Transformer-based cross-attention mechanisms are expected to further reduce the reliance on traditional attention in multimodal EEG systems.

- 5. Conclusion and Future Works

This paper presents a systematic and comprehensive review of recent advancements in attention mechanisms integrated into EEG-based BCI systems. We structure the review around three conceptually related categories of attention mechanisms: traditional attention methods, Transformer-based multi-head self-attention architectures, and multimodal attention fusion strategies. First, we introduce traditional attention mechanisms, including channel-specific, temporal-specific, and frequency-specific modules. These approaches enhance EEG signal decoding by adaptively emphasizing salient features, which could improve model accuracy and robustness against noise and inter-subject variability. We then explore Transformer-based architectures that utilize multi-head self-attention mechanisms to capture complex temporal and spatial dependencies within EEG data. These methods enable more expressive and flexible feature representations, addressing limitations of earlier approaches. We then review multimodal attention fusion strategies, which incorporate EEG signals with additional physiological and sensory modalities. This integration enhances system interpretability and adaptability, supporting more effective performance in complex and dynamic environments. Together, these three categories form a coherent taxonomy that reflects the methodological evolution of attentionbased techniques in neural decoding and offers a comparative understanding of their respective advantages, limitations, and suitable application contexts. Through this structured overview, we aim to provide researchers with a practical reference for selecting attention mechanisms that best address specific challenges in BCI design.

Despite the progress outlined in this review, several important challenges remain. Current attention mechanisms often suffer from limited generalizability, as their performance tends to be constrained by dataset-specific and subject-specific characteristics. In addition, the high computational complexity of models such as Transformers can hinder their application in realtime and resource-limited scenarios. To address these issues, future research should focus on the development of lightweight, energy-efficient, and EEG-specific attention models that are better aligned with the physiological properties of neural signals. Advancing in this direction will help

unlock the broader potential of attention-based BCIs, enabling their practical use across a range of domains including clinical diagnosis, neurorehabilitation, education, and human–machine interaction.

To establish a stronger foundation for future advancements, it is essential to examine the current landscape of attention-based BCI applications across various domains. In clinical neuroscience, attention mechanisms have significantly enhanced diagnostic accuracy in EEGbased emotion recognition and the detection of neurological disorders such as epilepsy and Parkinson’s disease. However, these clinical systems continue to face challenges, particularly with inter-subject variability and the need for extensive calibration, which hinder widespread clinical deployment. In motor rehabilitation, attention mechanisms optimized for specific EEG channels and temporal dynamics have improved the decoding of motor imagery. Nonetheless, achieving robust, low-latency performance suitable for real-time application in diverse operational environments remains a key challenge. In educational technology, attention-based BCIs have made substantial progress in enabling personalized learning, particularly for students with learning disabilities. However, the scalability of such systems and their integration into formal educational settings still require significant development. In safety-critical industries, such as aviation and maritime operations, EEG-driven attention monitoring has shown promise in managing fatigue and cognitive workload. Despite this potential, ensuring system reliability and generalizability under dynamic, high-stress conditions remains a critical concern.

Building upon these practical experiences and the challenges identified above, future research in attention-based deep learning for BCIs is well-positioned to address current limitations and expand into broader domains with increased precision and robustness. Specifically, attentionenhanced models have the potential to reshape several application areas by leveraging the temporal-spatial sensitivity of EEG signals and the interpretability of attention mechanisms. In clinical neuroscience, attention-guided BCI frameworks can be utilized to develop early diagnostic tools for conditions such as epilepsy, Parkinson’s disease, and Alzheimer’s disease. By dynamically attending to frequency bands and electrode regions associated with preictal states, attention-based models can facilitate real-time seizure prediction with fewer false alarms. In assistive technologies, attention mechanisms can enhance brain-controlled exoskeletons and spelling interfaces for individuals with severe motor impairments. Through adaptively focusing on high-informative EEG segments, such as event-related desynchronization (ERD) windows, the system could improve command accuracy under non-stationary conditions. Coupling these models with transfer learning and few-shot adaptation methods may reduce calibration time and personalize device control for locked-in syndrome patients. In mental health monitoring, attention-based emotion recognition systems can be fine-tuned to identify neural signatures of chronic stress, anxiety, or depression. Temporal attention can be applied to isolate emotionally salient EEG segments during resting-state or affective stimulation, facilitating early intervention via wearable neurofeedback devices or closed-loop neuromodulation. In educational neuroscience, future BCI systems can employ attention modules to track cognitive workload in real time, enabling adaptive learning platforms that adjust content difficulty or presentation speed based on attention levels and fatigue. These systems could be particularly beneficial for students with ADHD, where continuous monitoring of frontoparietal EEG activity might allow for real-time feedback or stimulus modulation to improve engagement and learning outcomes. In maritime and aerospace environments, attention-informed BCIs can support neuroergonomic monitoring by detecting shifts in vigilance, workload, or mental fatigue during prolonged or high-stakes operations. By focusing on alpha and theta band dynamics in frontal and parietal regions, these systems can be trained to issue cognitive alerts or task reallocations in response to declining neural performance. Furthermore, embedding these models in low-power wearable headsets with

[Figure 22]

Aerospace Systems

Emotion Recognition

[Figure 23]

[Figure 24]

[Figure 25]

BCI IN

Disability Support

[Figure 26]

# FUTURE

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

Education

[Figure 31]

Clinical Applications Maritime Safety

[Figure 32]

Figure 7: Future works of attention modules in BCI.

real-time edge inference capabilities is essential for deployment in dynamic, mobility-constrained settings.

Furthermore, future research on attention-based BCI systems should prioritize the development of specialized model architectures that are explicitly aligned with the unique physiological and temporal characteristics of EEG signals. At present, many BCI models are adapted from computer vision and natural language processing, relying on transformations that convert EEG signals into images or sequences. While these approaches have shown promise, they often fail to fully capture the dynamic and non-stationary nature of neural activity. Designing models specifically tailored to EEG data could lead to substantial improvements in clinical neurotechnologies, such as real-time seizure prediction and continuous brain-state monitoring. In addition, it is critical to address the computational inefficiencies and convergence challenges commonly associated with Transformer-based attention mechanisms. These limitations are particularly relevant for mobile neurodiagnostic tools, wearable assistive technologies, and real-time neuroergonomic monitoring systems, where energy efficiency, low latency, and portability are essential. Developing lightweight and optimized attention models will be vital not only for enhancing user experience but also for ensuring reliable real-time inference in resource-constrained environments.

### 6. Acknowledgments

This work was supported by the National Natural Science Foundation of China (62276169), Medical-Engineering Interdisciplinary Research Foundation of Shenzhen University (2023YG004), Shenzhen University Lingnan University Joint Research Programme, Shenzhen-Hong Kong Institute of Brain Science-Shenzhen Fundamental Research Institutions (2023SHIBS0003), the STI 2030-Major Projects (2021ZD0200500), the Open Research Fund of the State Key Laboratory

of Brain-Machine Intelligence, Zhejiang University (Grant No. BMI2400008), and the Shenzhen Science and Technology Program (No. JCYJ20241202124222027 and JCYJ20241202124209011).

### References

- [1] Dan Chen, Yangyang Hu, Chang Cai, Ke Zeng, and Xiaoli Li. Brain big data processing with massively parallel computing technology: challenges and opportunities. Software: Practice and Experience, 47(3):405–420, 2017.
- [2] D Puthankattil Subha, Paul K Joseph, Rajendra Acharya U, and Choo Min Lim. EEG signal analysis: a survey. Journal of medical systems, 34:195–212, 2010.
- [3] Berdakh Abibullaev, Aigerim Keutayeva, and Amin Zollanvari. Deep learning in EEGbased BCIs: a comprehensive review of transformer models, advantages, challenges, and applications. IEEE Access, 2023.
- [4] Alana de Santana Correia and Esther Luna Colombini. Attention, please! a survey of neural attention models in deep learning. Artificial Intelligence Review, 55(8):6037–6124, 2022.
- [5] Aigerim Keutayeva and Berdakh Abibullaev. Exploring the potential of attention mechanism-based deep learning for robust subject-independent motor-imagery based BCIs. IEEE Access, 2023.
- [6] Hiroshi Fukui, Tsubasa Hirakawa, Takayoshi Yamashita, and Hironobu Fujiyoshi. Attention branch network: Learning of attention mechanism for visual explanation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 10705–10714, 2019.
- [7] Derya Soydaner. Attention mechanism in neural networks: where it comes and where it goes. Neural Computing and Applications, 34(16):13371–13385, 2022.
- [8] Haixin Lv, Jinglong Chen, Tongyang Pan, Tianci Zhang, Yong Feng, and Shen Liu. Attention mechanism in intelligent fault diagnosis of machinery: A review of technique and application. Measurement, 199:111594, 2022.
- [9] Zhaoyang Niu, Guoqiang Zhong, and Hui Yu. A review on the attention mechanism of deep learning. Neurocomputing, 452:48–62, 2021.
- [10] Yuan Gao and Yingjun Ruan. Interpretable deep learning model for building energy consumption prediction based on attention mechanism. Energy and Buildings, 252:111379, 2021.
- [11] Pengpai Wang, Zhongnian Li, Peiliang Gong, Yueying Zhou, Fang Chen, and Daoqiang Zhang. Mtrt: Motion trajectory reconstruction transformer for EEG-based BCI decoding. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:2349–2358, 2023.
- [12] Junwei Duan, Jiaqi Xiong, Yinghui Li, and Weiping Ding. Deep learning based multimodal biomedical data fusion: An overview and comparative review. Information Fusion, 112:102536, 2024.

- [13] Yutong Xie, Bing Yang, Qingbiao Guan, Jianpeng Zhang, Qi Wu, and Yong Xia. Attention mechanisms in medical image segmentation: A survey. arXiv preprint arXiv:2305.17937, 2023.
- [14] Volodymyr Mnih, Nicolas Heess, Alex Graves, et al. Recurrent models of visual attention. Advances in neural information processing systems, 27, 2014.
- [15] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473, 2014.
- [16] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,  Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.
- [17] Saidul Islam, Hanae Elmekki, Ahmed Elsebai, Jamal Bentahar, Nagat Drawel, Gaith Rjoub, and Witold Pedrycz. A comprehensive survey on applications of transformers for deep learning tasks. Expert Systems with Applications, page 122666, 2023.
- [18] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929, 2020.
- [19] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin, and Baining Guo. Swin transformer: Hierarchical vision transformer using shifted windows. In Proceedings of the IEEE/CVF international conference on computer vision, pages 10012–10022, 2021.
- [20] Tao Chen, Yanrong Guo, Shijie Hao, and Richang Hong. Exploring self-attention graph pooling with EEG-based topological structure and soft label for depression detection. IEEE transactions on affective computing, 13(4):2106–2118, 2022.
- [21] Lisa-Marie Vortmann, Simon Ceh, and Felix Putze. Multimodal EEG and eye tracking feature fusion approaches for attention classification in hybrid BCIs. Frontiers in Computer Science, 4:780580, 2022.
- [22] Tao Shen, Tianyi Zhou, Guodong Long, Jing Jiang, Sen Wang, and Chengqi Zhang. Reinforced self-attention network: a hybrid of hard and soft attention for sequence modeling. arXiv preprint arXiv:1801.10296, 2018.
- [23] Siyu Lu, Mingzhe Liu, Lirong Yin, Zhengtong Yin, Xuan Liu, and Wenfeng Zheng. The multi-modal fusion in visual question answering: a review of attention mechanisms. PeerJ Computer Science, 9:e1400, 2023.
- [24] Kaixuan Chen, Dalin Zhang, Lina Yao, Bin Guo, Zhiwen Yu, and Yunhao Liu. Deep learning for sensor-based human activity recognition: Overview, challenges, and opportunities. ACM Computing Surveys (CSUR), 54(4):1–40, 2021.
- [25] Hilary Toulmin, Christian F Beckmann, Jonathan O’Muircheartaigh, Gareth Ball, Pum Za Nongena, Antonios Makropoulos, Ashraf Ederies, Serena J Counsell, Nigel Kennea, Tomoki Arichi, et al. Specialization and integration of functional thalamocortical connectivity in the human infant. Proceedings of the National Academy of Sciences, 112(25):7858–7863, 2015.

- [26] Runze Wu, Jing Jin, Ian Daly, Xingyu Wang, and Andrzej Cichocki. Classification of motor imagery based on multi-scale feature extraction and the channeltemporal attention module. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2023.
- [27] Peiyin Chen, Zhongke Gao, Miaomiao Yin, Jialing Wu, Kai Ma, and Celso Grebogi. Multiattention adaptation network for motor imagery recognition. IEEE Transactions on Systems, Man, and Cybernetics: Systems, 52(8):5127–5139, 2021.
- [28] Wei Tao, Chang Li, Rencheng Song, Juan Cheng, Yu Liu, Feng Wan, and Xun Chen. EEG-based emotion recognition via channel-wise attention and self attention. IEEE Transactions on Affective Computing, 2020.
- [29] Shuaiqi Liu, Xu Wang, Ling Zhao, Bing Li, Weiming Hu, Jie Yu, and Yu-Dong Zhang. 3dcann: A spatio-temporal convolution attention neural network for EEG emotion recognition. IEEE Journal of Biomedical and Health Informatics, 26(11):5321–5331, 2021.
- [30] Cunbo Li, Peiyang Li, Yangsong Zhang, Ning Li, Yajing Si, Fali Li, Zehong Cao, Huafu Chen, Badong Chen, Dezhong Yao, and Peng Xu. Effective emotion recognition by learning discriminative graph topologies in EEG brain networks. IEEE Transactions on Neural Networks and Learning Systems, 34(12):7247–7259, 2023.
- [31] Aarthy Nagarajan, Neethu Robinson, and Cun Tai Guan. Relevance-based channel selection in motor imagery brain-computer interface. Journal of Neural Engineering, 20(6):066014, 2023.
- [32] Kenneth E Hild, Santosh Mathan, Yonghong Huang, Deniz Erdogmus, and Misha Pavel. Optimal set of EEG electrodes for rapid serial visual presentation. In 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, pages 4335–4338. IEEE, 2010.
- [33] Zhentao Huang, Yahong Ma, Rongrong Wang, Wei Su Li, and Yongsheng Dai. A model for EEG-based emotion recognition: Cnn-bi-lstm with attention mechanism. Electronics, 12(14):3188, 2023.
- [34] Enze Su, Siqi Cai, Peiwen Li, Long Han Xie, and Haizhou Li. Auditory attention detection with EEG channel attention. In 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), page 9630508. IEEE, 2021.
- [35] Wei-Yen Hsu and Ya-Wen Cheng. EEG-channel-temporal-spectral-attention correlation for motor imagery EEG classification. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:1659–1669, 2023.
- [36] Martin Wimpff, Leonardo Gizzi, Jan Zerfowski, and Bin Yang. EEG motor imagery decoding: A framework for comparative analysis with channel attention mechanisms. arXiv preprint arXiv:2310.11198, 2023.
- [37] Yunxia Zhang, Xin Li, Changming Zhao, Wenyin Zheng, Manqing Wang, Yongqing Zhang, Hong Jiang Ma, and Dongrui Gao. Affective EEG-based person identification using channel attention convolutional neural dense connection network. Scientific Programming, 2021:7568460, 2021.

- [38] Franco Scarselli, Marco Gori, Allan C Tsoi, Markus Hagenbuchner, and Giovanni Monfardini. The graph neural network model. IEEE Transactions on Neural Networks, 20(1):61–80, 2009.
- [39] Xuefen Lin, Jielin Chen, Weifeng Ma, Wei Tang, and Yuchen Wang. EEG emotion recognition using improved graph neural network with channel selection. Computer Methods and Programs in Biomedicine, 231:107380, 2023.
- [40] Tian Chen, Lubao Li, and Xiaohui Yuan. A graph neural network with spatial attention for emotion analysis. Cognitive Computation, 17(1):1–12, 2025.
- [41] Chuan Lin Zhu, Weiqi He, Zhengyang Qi, Lili Wang, Dongqing Song, Lei Zhan, Shengnan Yi, Yuejia Luo, and Wenbo Luo. The time course of emotional picture processing: An event-related potential study using a rapid serial visual presentation paradigm. Frontiers in Psychology, 6:954, 2015.
- [42] Ravi Thiruchselvam, Jens Blechert, Gal Sheppes, Anders Rydstr¨om, and James J Gross. The temporal dynamics of emotion regulation: An EEG study of distraction and reappraisal. Biological Psychology, 87(1):84–92, 2011.
- [43] Maitreyee Wai Rag Kar, Yoshikatsu Hayashi, and Slawomir J Nasuto. Dynamics of long-range temporal correlations in broadband EEG during different motor execution and imagery tasks. Frontiers in Neuroscience, 15:660032, 2021.
- [44] Alessandro Angrilli, Thomas Elbert, Stefano Cusumano, Luciano Stegagno, and Brigitte Rockstroh. Temporal dynamics of linguistic processes are reorganized in aphasics’ cortex: an EEG mapping study. NeuroImage, 20(1):494–505, 2003.
- [45] Shuyu Yu, Lianghao Tian, Guohua Wang, and Shengxin Nie. Which ERP components are effective in measuring cognitive load in multimedia learning? a meta-analysis based on relevant studies. Frontiers in Psychology, 15:1401005, 2024.
- [46] Lei Jiang, Panote Siria Raya, Dongeun Choi, Fang Meng Zeng, and Noriaki Kuwahara. Electroencephalogram signals emotion recognition based on convolutional neural networkrecurrent neural network framework with channel-temporal attention mechanism for older adults. Frontiers in Aging Neuroscience, 14:945024, 2022.
- [47] Lijun Yang, Yixin Wang, Xiangru Zhu, and Xiaohui Yang. A gated temporal-separable attention network for EEG-based depression recognition. Computers in Biology and Medicine, 157:106782, 2023.
- [48] Yuzhe Zhang, Huan Liu, Dalin Zhang, Xuxu Chen, Tao Qin, and Qinghua Zheng. EEGbased emotion recognition with emotion localization via hierarchical self-attention. IEEE Transactions on Affective Computing, 2022.
- [49] Ziyu Jia, Youfang Lin, Xiyang Cai, Haobin Chen, Haijun Gou, and Jing Wang. Sstemotionnet: Spatial-spectral-temporal based attention 3d dense network for EEG emotion recognition. In Proceedings of the 28th ACM international conference on multimedia, pages 2909–2917, 2020.
- [50] Dalin Zhang, Kaixuan Chen, Debao Jian, and Lina Yao. Motor imagery classification via temporal attention cues of graph embedded EEG signals. IEEE journal of biomedical and health informatics, 24(9):2570–2579, 2020.

- [51] Xuelin Ma, Shuang Qiu, and Huiguang He. Time-distributed attention network for EEGbased motor imagery decoding from the same limb. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 30:496–508, 2022.
- [52] Siqi Cai, Enze Su, Longhan Xie, and Haizhou Li. EEG-based auditory attention detection via frequency and channel neural attention. IEEE Transactions on Human-Machine Systems, 52(2):256–266, 2021.
- [53] Guowen Xiao, Meng Shi, Mengwen Ye, Bowen Xu, Zhendi Chen, and Quansheng Ren. 4d attention-based neural network for EEG emotion recognition. Cognitive Neurodynamics, pages 1–14, 2022.
- [54] Zhuang Xie, Jianguo Wei, Wenhuan Lu, ZhongJie Li, Chunli Wang, and Gaoyan Zhang. EEG-based fast auditory attention detection in real-life scenarios using time-frequency attention mechanism. In ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1741–1745. IEEE, 2024.
- [55] Wei Chen, Yuan Liao, Rui Dai, Yuanlin Dong, and Liya Huang. EEG-based emotion recognition using graph convolutional neural network with dual attention mechanism. Frontiers in Computational Neuroscience, 18:1416494, 2024.
- [56] Xiaobing Du, Cuixia Ma, Guanhua Zhang, Jinyao Li, Yu-Kun Lai, Guozhen Zhao, Xiaoming Deng, Yong-Jin Liu, and Hongan Wang. An efficient lstm network for emotion recognition from multichannel EEG signals. IEEE Transactions on Affective Computing, 13(3):1528–1540, 2020.
- [57] Tao Xu, Wang Dang, Jiabao Wang, and Yun Zhou. Dagam: a domain adversarial graph attention model for subject-independent EEG-based emotion recognition. Journal of Neural Engineering, 20(1):016022, 2023.
- [58] Dalin Zhang, Lina Yao, Kaixuan Chen, and Jessica Monaghan. A convolutional recurrent attention model for subject-independent EEG signal analysis. IEEE Signal Processing Letters, 26(5):715–719, 2019.
- [59] Youmin Kim and Ahyoung Choi. EEG-based emotion classification using long short-term memory network with attention mechanism. Sensors, 20(23):6727, 2020.
- [60] Ziyu Jia, Youfang Lin, Jing Wang, Ronghao Zhou, Xiaojun Ning, Yuanlai He, and Yaoshuai Zhao. Graphsleepnet: Adaptive spatial-temporal graph convolutional networks for sleep stage classification. In IJCAI, volume 2021, pages 1324–1330, 2020.
- [61] Dalin Zhang, Lina Yao, Kaixuan Chen, Sen Wang, Pari Delir Haghighi, and Caley Sullivan. A graph-based hierarchical attention model for movement intention detection from EEG signals. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 27(11):2247–2253, 2019.
- [62] Guangyi Zhang and Ali Etemad. Spatio-temporal EEG representation learning on riemannian manifold and euclidean space. arXiv preprint arXiv:2008.08633, 2020.
- [63] Martin Wimpff, Leonardo Gizzi, Jan Zerfowski, and Bin Yang. EEG motor imagery decoding: A framework for comparative analysis with channel attention mechanisms. Journal of neural engineering, 21(3):036020, 2024.

- [64] Zijian Yuan, Qian Zhou, Baozeng Wang, Qi Zhang, Yang Yang, Yuwei Zhao, Yong Guo, Jin Zhou, and Changyong Wang. PsaEEGnet: pyramid squeeze attention mechanism-based cnn for single-trial EEG classification in RSVP task. Frontiers in Human Neuroscience, 18:1385360, 2024.
- [65] Xuejian Wu, Yaqi Chu, Qing Li, Yang Luo, Yiwen Zhao, and Xingang Zhao. AmEEGnet: attention-based multiscale EEGnet for effective motor imagery EEG decoding. Frontiers in Neurorobotics, 19:1540033, 2025.
- [66] Wenzhe Liao, Zipeng Miao, Shuaibo Liang, Linyan Zhang, and Chen Li. A composite improved attention convolutional network for motor imagery EEG classification. Frontiers in Neuroscience, 19:1543508, 2025.
- [67] Wei Qu, Zhiyong Wang, Hong Hong, Zheru Chi, David Dagan Feng, Ron Grunstein, and Christopher Gordon. A residual based attention model for EEG based sleep staging. IEEE journal of biomedical and health informatics, 24(10):2833–2843, 2020.
- [68] Yonghao Song, Xueyu Jia, Lie Yang, and Longhan Xie. Transformer-based spatial-temporal feature learning for EEG decoding. arXiv preprint arXiv:2106.11170, 2021.
- [69] Chang Li, Xiaoyang Huang, Rencheng Song, Ruobing Qian, Xiang Liu, and Xun Chen. EEG-based seizure prediction via transformer guided cnn. Measurement, 203:111948, 2022.
- [70] Jia-Yi Guo, Qing Cai, Jian-Peng An, Pei-Yin Chen, Chao Ma, Jun-He Wan, and Zhong-Ke Gao. A transformer based neural network for emotion recognition and visualizations of crucial EEG channels. Physica A: Statistical Mechanics and its Applications, 603:127700, 2022.
- [71] Yawen Zheng, Xiaojie Zhao, and Li Yao. Copula-based transformer in EEG to assess visual discomfort induced by stereoscopic 3d. Biomedical Signal Processing and Control, 77:103803, 2022.
- [72] Yang Du, Yongling Xu, Xiaoan Wang, Li Liu, and Pengcheng Ma. EEG temporal–spatial transformer for person identification. Scientific Reports, 12(1):14378, 2022.
- [73] Xiaopeng Si, Dong Huang, Zhen Liang, Yulin Sun, He Huang, Qile Liu, Zhuobin Yang, and Dong Ming. Temporal aware mixed attention-based convolution and transformer network for cross-subject EEG emotion recognition. Computers in Biology and Medicine, 181:108973, 2024.
- [74] Yue Pan, Qile Liu, Qing Liu, Li Zhang, Gan Huang, Xin Chen, Fali Li, Peng Xu, and Zhen Liang. Dua: Dual attentive transformer in long-term continuous EEG emotion analysis. arXiv preprint arXiv:2407.20519, 2024.
- [75] Hongqi Li, Haodong Zhang, and Yitong Chen. Dual-tsst: A dual-branch temporalspectral-spatial transformer model for eeg decoding. arXiv preprint arXiv:2409.03251, 2024.
- [76] Yi Ding, Joon Hei Lee, Shuailei Zhang, Tianze Luo, and Cuntai Guan. Decoding human attentive states from spatial-temporal EEG patches using transformers. arXiv preprint arXiv:2502.03736, 2025.

- [77] Jathurshan Pradeepkumar, Xihao Piao, Zheng Chen, and Jimeng Sun. Single-channel EEG tokenization through time-frequency modeling. arXiv preprint arXiv:2502.16060, 2025.
- [78] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pretraining of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.
- [79] Goro Kobayashi, Tatsuki Kuribayashi, Sho Yokoi, and Kentaro Inui. Attention is not only a weight: Analyzing transformers with vector norms. arXiv preprint arXiv:2004.10102, 2020.
- [80] Tianyang Lin, Yuxin Wang, Xiangyang Liu, and Xipeng Qiu. A survey of transformers. AI Open, 2022.
- [81] Sifan Wu, Xi Xiao, Qianggang Ding, Peilin Zhao, Ying Wei, and Junzhou Huang. Adversarial sparse transformer for time series forecasting. Advances in neural information processing systems, 33:17105–17115, 2020.
- [82] Tian Zhou, Ziqing Ma, Qingsong Wen, Xue Wang, Liang Sun, and Rong Jin. Fedformer: Frequency enhanced decomposed transformer for long-term series forecasting. In International conference on machine learning, pages 27268–27286. PMLR, 2022.
- [83] Qingsong Wen, Tian Zhou, Chaoli Zhang, Weiqi Chen, Ziqing Ma, Junchi Yan, and Liang Sun. Transformers in time series: A survey. arXiv preprint arXiv:2202.07125, 2022.
- [84] Peng Xu, Xiatian Zhu, and David A Clifton. Multimodal learning with transformers: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023.
- [85] Jin Xie, Jie Zhang, Jiayao Sun, Zheng Ma, Liuni Qin, Guanglin Li, Huihui Zhou, and Yang Zhan. A transformer-based approach combining deep learning network and spatialtemporal information for raw EEG classification. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 30:2126–2136, 2022.
- [86] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from natural language supervision. In International conference on machine learning, pages 8748–8763. PMLR, 2021.
- [87] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Bjo¨rn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 10684–10695,

- 2022.

[88] Chaoyue Ding, Shiliang Sun, and Jing Zhao. Mst-gat: A multimodal spatial–temporal graph attention network for time series anomaly detection. Information Fusion, 89:527–536,

- 2023.

- [89] Bing Cao, Yinan Xia, Yi Ding, Changqing Zhang, and Qinghua Hu. Predictive dynamic fusion. arXiv preprint arXiv:2406.04802, 2024.

- [90] Wei Wei, Chao Huang, Lianghao Xia, and Chuxu Zhang. Multi-modal self-supervised learning for recommendation. In Proceedings of the ACM Web Conference 2023, pages 790–800, 2023.
- [91] Wei Liu, Jie-Lin Qiu, Wei-Long Zheng, and Bao-Liang Lu. Comparing recognition performance and robustness of multimodal deep learning models for multimodal emotion recognition. IEEE Transactions on Cognitive and Developmental Systems, 14(2):715–729, 2021.
- [92] Xiaowei Zhang, Junlei Li, Kechen Hou, Bin Hu, Jian Shen, and Jing Pan. EEG-based depression detection using convolutional neural network with demographic attention mechanism. In 2020 42nd annual international conference of the ieee engineering in medicine & biology society (embc), pages 128–133. IEEE, 2020.
- [93] Dong Yoon Choi, Deok-Hwan Kim, and Byung Cheol Song. Multimodal attention network for continuous-time emotion recognition using video and EEG signals. IEEE Access, 8:203814–203826, 2020.
- [94] Zheng Yubo, Luo Yingying, Zou Bing, Zhang Lin, and Li Lei. Mmasleepnet: A multimodal attention network based on electrophysiological signals for automatic sleep staging. Frontiers in Neuroscience, 16:973761, 2022.
- [95] Jie Hu, Li Shen, and Gang Sun. Squeeze-and-excitation networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 7132–7141, 2018.
- [96] ZhengXiao He, Minghong Cai, Letian Li, Siyuan Tian, and Ren-Jie Dai. EEG-EMG faconformer: Frequency aware conv-transformer for the fusion of EEG and EMG. In 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), pages 3258–3261. IEEE, 2024.
- [97] Jing Wang and Ci Zhang. Cross-modality fusion with EEG and text for enhanced emotion detection in english writing. Frontiers in Neurorobotics, 18:1529880, 2025.
- [98] Songtao Li and Hao Tang. Multimodal alignment and fusion: A survey. arXiv preprint arXiv:2411.17040, 2024.
- [99] Wei-Yu Lee, Ljubomir Jovanov, and Wilfried Philips. Cross-modality attention and multimodal fusion transformer for pedestrian detection. In European Conference on Computer Vision, pages 608–623. Springer, 2022.
- [100] Hao Wang, Mingchuan Yang, Zheng Li, Zhenhua Liu, Jie Hu, Ziwang Fu, and Feng Liu. Scanet: Improving multimodal representation and fusion with sparse-and crossattention for multimodal sentiment analysis. Computer Animation and Virtual Worlds, 33(3-4):e2090, 2022.
- [101] Fei Zhao, Chengcui Zhang, and Baocheng Geng. Deep multimodal data fusion. ACM Computing Surveys, 56(9):1–36, 2024.
- [102] Yunpeng Bai, Xintao Wang, Yan-pei Cao, Yixiao Ge, Chun Yuan, and Ying Shan. Dreamdiffusion: Generating high-quality images from brain EEG signals. arXiv preprint arXiv:2306.16934, 2023.

- [103] Dongyang Li, Haoyang Qin, Mingyang Wu, Yuang Cao, Chen Wei, and Quanying Liu. Realmind: Zero-shot EEG-based visual decoding and captioning using multi-modal models. arXiv e-prints, pages arXiv–2410, 2024.
- [104] Dongyang Li, Chen Wei, Shiying Li, Jiachen Zou, Haoyang Qin, and Quanying Liu. Visual decoding and reconstruction via EEG embeddings with guided diffusion. arXiv preprint arXiv:2403.07721, 2024.
- [105] Elnaz Vafaei and Mohammad Hosseini. Transformers in EEG analysis: A review of architectures and applications in motor imagery, seizure, and emotion classification. Sensors, 25(5), 2025.
- [106] Xiaoshan Zhang, Enze Shi, Sigang Yu, and Shu Zhang. Dtca: Dual-branch transformer with cross-attention for EEG and eye movement data fusion. In Marius George Linguraru, Qi Dou, Aasa Feragen, Stamatia Giannarou, Ben Glocker, Karim Lekadir, and Julia A. Schnabel, editors, Medical Image Computing and Computer Assisted Intervention

– MICCAI 2024, pages 141–151, Cham, 2024. Springer Nature Switzerland.

- [107] Kang Yin, Hye-Bin Shin, Dan Li, and Seong-Whan Lee. EEG-based multimodal representation learning for emotion recognition. In 2025 13th International Conference on Brain-Computer Interface (BCI), pages 1–4. IEEE, 2025.

