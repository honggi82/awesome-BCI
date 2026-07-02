# arXiv:2502.17464v1[eess.SP]11Feb2025

## Large Cognition Model: Towards Pretrained Electroencephalography (EEG) Foundation Model

Chi-Sheng Chen

Neuro Industry, Inc. Boston, Massachusetts, USA michael@neuro-industry.com m50816m50816@gmail.com

Ying-Jung Chen

Georgia Institute of Technology Atlanta, Georgia, USA yingjungcd@gmail.com

Aidan Hung-Wen Tsai

Neuro Industry, Inc. Boston, Massachusetts, USA aidan@neuro-industry.com

### Abstract

Electroencephalography (EEG) provides a non-invasive window into brain activity, offering valuable insights for neurological research, brain-computer interfaces (BCIs), and clinical diagnostics. However, the development of robust machine learning models for EEG analysis is hindered by the scarcity of large-scale, wellannotated datasets and the inherent variability of EEG signals across subjects and recording conditions. Inspired by the success of foundation models in natural language processing (NLP) and computer vision, we propose the Large Cognition Model (LCM)—a transformer-based foundation model designed to generalize across diverse EEG datasets and downstream tasks. Unlike traditional approaches, our proposed transformer-based architecture demonstrates strong generalization capabilities across datasets and tasks, even without pretraining, surpassing some existing EEG universal models on specific downstream applications. LCM leverages large-scale self-supervised learning techniques to capture universal EEG representations, enabling efficient fine-tuning for applications such as cognitive state decoding, disease classification, and neurofeedback systems. We introduce a novel architecture that integrates temporal and spectral attention mechanisms, optimizing the model’s ability to extract meaningful features from raw EEG signals. Extensive evaluations demonstrate that LCM outperforms stateof-the-art approaches across multiple EEG benchmarks, exhibiting strong cross-subject and cross-task generalization. Our findings highlight the potential of pretrained EEG foundation models to accelerate advancements in neuroscience, personalized medicine, and BCI technology.

### Keywords

Electroencephalography, EEG, Deep Learning, Foundation Model, Brain-Computer Interface, Biosignal processing, Transformer, Contrastive Learning

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

Conference’17, Washington, DC, USA © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-XXXX-X/2018/06 https://doi.org/10.1145/nnnnnnn.nnnnnnn

#### ACM Reference Format:

Chi-Sheng Chen, Ying-Jung Chen, and Aidan Hung-Wen Tsai. 2025. Large Cognition Model: Towards Pretrained Electroencephalography (EEG) Foundation Model. In . ACM, New York, NY, USA, 6 pages. https://doi.org/10. 1145/nnnnnnn.nnnnnnn

### 1 Introduction

Electroencephalography (EEG) has witnessed significant advancements in recent years, finding applications in psychiatric diagnostics [12], multimodal learning [5], brain-computer interface (BCI)based robotic control [4], generative tasks [1], and even quantum computing [2, 3]. Despite these developments, the large-scale adoption of EEG models has remained limited due to the inherent complexity of EEG signals. Unlike image or text data, EEG exhibits a low signal-to-noise ratio (SNR) and high inter-subject variability, with differences in montage configurations, channel placements, and recording formats further complicating data standardization. These challenges have hindered the development of foundation models that, similar to large language models (LLMs), could provide pretrained weights for efficient adaptation to various downstream tasks.

Several studies have already explored the development of universal EEG representations. For example, BENDR [10] takes a different approach by incorporating self-supervised learning with masked autoencoders and contrastive learning to improve EEG representation learning. This method effectively addresses the challenges posed by multi-task and multi-paradigm EEG data, enhancing model generalizability. BENDR utilizes a convolutional encoder to extract features from local time windows, applies masking to certain features, and then reconstructs the missing information using a transformer decoder. Similarly, EEG2VEC [19] introduces a self-supervised learning framework that captures EEG representations through contrastive and reconstruction losses. The pretrained model functions as a feature extractor for downstream applications. Both EEG2VEC and BENDR integrate convolutional neural networks with transformer architectures to learn both local and global representations. EEG2VEC has been validated in EEG matchmismatch and EEG regression tasks within the auditory EEG challenge. Another significant development, the Biosignal Transformer (BIOT) [17], tackles the challenges of cross-data learning, including mismatched channels, variable sequence lengths, and missing values in biosignals such as EEG, ECG, and human activity recognition signals. BIOT processes each channel separately, tokenizing signals into fixed-length segments that capture local signal features before rearranging them into a longer "sentence." In the CHB-MIT seizure

detection task, the pretrained BIOT model demonstrated a 4% improvement over existing methods. The Large Brain Model (LaBraM) [8] further extends the capabilities of EEG-based deep learning models by enabling cross-dataset learning. It partitions EEG signals into channel-specific patches and employs vector-quantized neural spectrum prediction to train a neural tokenizer. This tokenizer encodes raw EEG segments into neural codes, which are then used to pretrain transformers, allowing them to predict the original neural codes for masked segments. LaBraM surpasses state-of-the-art methods in various EEG-related tasks, including abnormal event detection, event classification, emotion recognition, and gait prediction. UM-EEG [11] is a semantically rich, continuous EEG representation that advances classification and outcome prediction beyond traditional discrete state classification. However, the model uses only four EEG channels, which may lose spatial resolution for localized patterns (e.g., lateralized discharges). UniEEG [9] is an electrode-based time-frequency pretraining model designed to address challenges in EEG research, including data scarcity, crossdevice incompatibility, and low signal-to-noise ratio. The model adopts an encoder-decoder architecture with an electrode-wise modeling approach to enhance compatibility across different devices and tasks. It leverages Masked Signal Modeling (MSM) to learn a universal EEG representation. While the electrode-wise strategy helps standardize data across different acquisition systems, it may overlook spatial information across electrodes, which could impact tasks that heavily rely on brain region distributions, such as motor imagery and cognitive load analysis. EEGPT [15] does not directly learn from raw EEG waveforms but instead leverages highSNR feature representations for self-supervised learning. Through masking and spatio-temporal alignment methods, EEGPT enhances feature interpretability and reduces noise interference. EEGPT also utilizes a local spatio-temporal embedding method to map electrode channels into learned universal representations, ensuring model compatibility across different EEG devices and reducing the impact of electrode position variations on feature extraction.

Despite these advancements, a major challenge remains in designing EEG foundation models that generalize across datasets, recording conditions, and application domains. Existing models such as BENDR, EEG2VEC, and BIOT primarily focus on leveraging self-supervised learning to improve EEG representation learning, but they often suffer from domain-specific constraints, limited scalability across heterogeneous datasets, and difficulties in capturing both temporal and spatial EEG dependencies simultaneously. While UM-EEG introduces a low-dimensional embedding space for EEG classification and prognostication, its reliance on only four EEG channels limits spatial resolution for applications requiring finegrained topographical information. Similarly, LaBraM and UniEEG offer promising cross-dataset generalization capabilities, but the former depends on vector-quantized neural codes, which may not fully capture the continuous nature of EEG dynamics, while the latter’s electrode-wise strategy trades off spatial coherence for device compatibility.

Moreover, existing EEG foundation models have yet to fully integrate advanced position encoding mechanisms, hierarchical feature fusion, and robust contrastive learning strategies to maximize feature generalizability across tasks and domains. Current approaches primarily rely on CNN-based or hybrid architectures,

which may not fully exploit the sequential dependencies inherent in EEG signals, limiting their ability to model long-range relationships in neural activity. Furthermore, while models like EEGPT emphasize spatio-temporal embedding to mitigate noise sensitivity and electrode variability, they do not explicitly address inter-subject variability or cross-device robustness, which are crucial factors for large-scale EEG deployment.

To address these issues, this paper presents the Large Cognition Model (LCM), a transformer-based EEG foundation model designed to learn robust and transferable representations from diverse EEG datasets. Building upon the foundational aspects of our Large Cognition Model (LCM), we have integrated advanced techniques to enhance its performance in EEG representation learning. One such technique used for handling cross-montage EEG data is the learnable channel mapping approach, which aligns different EEG electrode configurations into a common representation space. This method introduces a trainable transformation matrix that maps raw EEG signals from different montages into a unified latent space, ensuring consistent feature extraction across datasets. By incorporating a learnable channel embedding, the model can adapt to varying electrode placements while preserving the spatial structure of the EEG signals. This approach enhances the model’s robustness to montage variability, improving generalization across different experimental setups and recording conditions. Additionally, we employ a masked token strategy from [7] during the training phase. This approach involves masking a subset of the input data and tasking the model with predicting the missing components based on the surrounding context. Such a strategy compels the model to develop a deeper understanding of the underlying structures and dependencies within the data. In the context of EEG data, this method aids in capturing the complex temporal and spatial relationships present in neural signals.

Our contributions are threefold:

- • We introduce a novel contrastive learning framework tailored for EEG foundation models, enabling self-supervised learning of generalizable EEG representations across different tasks and domains;
- • We propose a new EEG encoder, LCM, which encodes EEG signals into both temporal and spatial tokens, facilitating effective information integration across time and electrode locations; and
- • We demonstrate that our model achieves strong generalization across datasets and tasks, even without extensive pretraining, surpassing some existing universal EEG models in specific applications.

### 2 Methodology

We propose Large Cognition Model (LCM), a self-supervised contrastive learning framework designed for EEG representation learning. The model consists of an online encoder 𝑓𝜃 and a momentumupdatedtargetencoder 𝑓𝜉. Thelearningprocessinvolvescontrastive loss for representation alignment, masked feature reconstruction loss, and an adaptive optimization schedule to balance feature learning stability. The whole flow is shown in Figure 1.

[Figure 1]

Figure 1: Overview of the LCM Training Flow. The EEG signals are first segmented into spatio-temporal patches. Each patch is then assigned a channel embedding to encode electrode-specific information. A subset of the patches is masked for selfsupervised learning. The masked and unmasked patches are processed through the Latent Contrastive Masking (LCM) module, which consists of a convolutional block followed by transformer layers to extract hierarchical spatio-temporal representations. Finally, contrastive learning is applied to align learned EEG representations, improving the robustness and generalizability of the model.

### 2.1 Feature Extraction and Cross-Montage Encoding

Given an EEG input matrix 𝑥 ∈ R𝑀×𝑇 with 𝑀 channels and 𝑇 time steps, our model first applies a learnable channel mapping 𝜙 : R𝑀×𝑇 → R𝑀′×𝑇 to align different EEG montages into a common latent space:

𝑥˜ = 𝑊𝑐𝑥 +𝐶 (1)

where 𝑊𝑐 ∈ R𝑀′×𝑀 is a trainable transformation matrix ensuring channel consistency across different EEG datasets, and 𝐶 is a learnable channel embedding matrix𝐶 ∈ R𝑀×𝑑 encoding electrodespecific properties.

Next, the transformed EEG signal is segmented into spatiotemporal patches:

{𝑝𝑖,𝑗} = Patching(𝑥˜) (2)

where each patch 𝑝𝑖,𝑗 ∈ R𝑝×𝑝 corresponds to a local segment of the EEG signal.

The encoder network 𝑓𝜃 projects these patches into latent embeddings:

𝑧 = 𝑓𝜃 (𝑥,𝑐˜ ) (3)

where 𝑐 is the channel embedding vector used to ensure robustness across different montages.

For contrastive learning, we maintain a momentum-updated target encoder 𝑓𝜉 that learns a stable representation of the EEG signal:

ℎ = 𝑓𝜉 (𝑥,𝑐˜ ) (4)

where 𝑓𝜉 shares the same architecture as 𝑓𝜃 but updates its parameters through an exponential moving average (EMA) of the online encoder:

𝜉 ← 𝑚𝜉 + (1 −𝑚)𝜃, 𝑚 ∈ [0.996, 1.0] (5)

This ensures smooth adaptation of representations across different datasets and EEG montages, improving generalization across subjects and experimental setups.

### 2.2 Spatio-Temporal Contrastive Alignment

To enforce feature consistency between 𝑧 and ℎ, we define a spatiotemporal alignment loss using Mean Squared Error (MSE) loss:

∑︁𝑁

1 𝑁

∥LN(ℎ𝑖) − LN(𝑧𝑖)∥22 (6)

L𝐴 =

𝑖=1

where LN(·) applies layer normalization to mitigate covariate shift.

### 2.3 Mask-Based Reconstruction

To enhance EEG feature completeness, we employ a masked reconstruction loss, where patches of the input EEG are randomly masked before being passed to the encoder:

𝑥˜ = 𝑥 ⊙ 𝑀, 𝑀𝑖,𝑗 ∼ Bernoulli(𝑝mask) (7) where 𝑝mask is the masking probability.

The masked embeddings are reconstructed via:

𝑥ˆ = REC(𝑧) (8) where REC(·) is the reconstructor module. The reconstruction loss is defined as:

∑︁

1 |𝑀|

∥𝑥ˆ𝑖,𝑗 − 𝑥𝑖,𝑗 ∥22 (9)

L𝑅 =

(𝑖,𝑗)∈𝑀

### 2.4 Optimization and Learning Rate Scheduling

The optimization process is handled using the AdamW optimizer with a weight decay strategy. The learning rate follows a OneCycleLR policy:

𝑝

𝑡 𝑇

(10)

𝜆𝑡 = 𝜆max × 1 −

where 𝜆max is the peak learning rate, 𝑝 is a decay exponent, and𝑇 is the total training steps.

To ensure smooth model convergence, we introduce cosine weight decay (CWD):

- 1

- 2 (𝑤final − 𝑤init) 1 + cos

𝑡𝜋 𝑇

(11)

𝑤𝑡 = 𝑤init +

### 2.5 Training Process and Gradient Updates At each training step:

- (1) Compute feature embeddings from the online encoder 𝑧 and the target encoder ℎ.
- (2) Compute contrastive alignment loss L𝐴 and masked reconstruction loss L𝑅.
- (3) Perform gradient updates using AdamW optimizer.
- (4) Update the target encoder using EMA. The final self-supervised training loss is:

L = L𝐴 + 𝜆L𝑅 (12) where 𝜆 is a trade-off hyperparameter.

### 2.6 Gradient Logging and Adaptation

To track gradient stability, we compute the first and last layer gradient statistics:

∥∇𝜃𝑖 L∥ (13) We log:

𝑔min = min

∥∇𝜃𝑖 L∥, 𝑔max = max

𝑖

𝑖

E[𝑔first layer], E[𝑔last layer], 𝑔min, 𝑔max (14) to ensure gradient propagation stability.

Table 1: Datasets for pretraining and downstream tasks

Datasets Paradigms Subjects Targets Pretraining Datasets

PhysioMI MI&ME 109 5 TSU SSVEP 35 40 SEED EMO 15 3

Downstream Datasets

- BCIC-2A MI 10 4
- BCIC-2B MI 10 2

3 Experiments and Results

- 3.1 Dataset and Preprocessing

We compiled a collection of publicly available EEG datasets covering various paradigms for model pretraining, as detailed in Table 1. These include motor imagery (MI) and execution (ME) datasets such as PhysioMI [6], steady-state visual evoked potential (SSVEP) dataset TSU [16], and emotional classification dataset SEED [18]. To evaluate the effectiveness of the learned representations in downstream tasks, we curated a selection of datasets listed in Table 1. This includes MI datasets BCIC-2A [14] and BCIC-2B [13]. To comprehensively evaluate the proposed LCM model across different tasks, each dataset underwent a combination of standardized and task-specific preprocessing steps. These steps included segmenting the data into 4-second segments, applying average re-referencing, selecting relevant channels, scaling the signals in millivolts, and resampling at 256 Hz. Additionally, MI datasets used for downstream tasks were filtered using a 0-38 Hz bandpass filter.

- 3.2 Experiment Details

We trained the Large Cognition Model (LCM) using a transformerbased architecture tailored for EEG representation learning. The training procedure was optimized to ensure stable convergence and efficient learning through careful selection of hyperparameters, model architecture, and learning rate scheduling.

The model was trained for 200 epochs with a batch size of 1024 in training and 100 epochs for downstream task fine-tuning, utilizing AdamW as the optimizer with an initial learning rate of 1.5e-4 and a weight decay of 0.05 to prevent overfitting. To facilitate stable convergence, we employed a 10-epoch warmup phase, gradually increasing the learning rate before applying a cosine annealing learning rate schedule for the remaining 90 epochs.

We utilized AdamW optimization with betas (0.9, 0.95) to control moment estimates, ensuring robust weight updates. The learning rate scheduling followed a cosine annealing decay, where the initial learning rate of 1.5e-4 increased progressively from 0 to 1.5e-4 during the first 10 epochs (warmup phase) and then gradually decayed to 1e-6 over the remaining 90 epochs.

This training setup ensures that LCM efficiently captures meaningful EEG representations, leveraging both spatial and temporal structures within the data while maintaining robust optimization dynamics.

Table 2: The results of universal EEG models on various datasets.

Datasets Methods Size Pretrained Balanced Accuracy Cohen’s Kappa Weighted F1 / AUROC

- BCIC-2A BIOT 3.2M Y 0.4590±0.0196 0.2787±0.0261 0.4282±0.0289 BENDR - Y 0.4899±0.0070 0.3199±0.0094 0.4836±0.0076 LCM (Ours) 33.9M N 0.5263±0.0027 0.3682±0.0361 0.5256±0.0267 LaBraM 5.8M Y 0.5613±0.0052 0.4151±0.0069 0.5520±0.0052 EEGPT 25M Y 0.5846±0.0070 0.4462±0.0094 0.5715±0.0051 LCM (Ours) 33.9M Y 0.6166±0.0083 0.4619±0.0241 0.5932±0.0121

- BCIC-2B BIOT 3.2M Y 0.6409±0.0118 0.2817±0.0236 0.7095±0.0141 LCM (Ours) 33.9M N 0.6825±0.1024 0.3651±0.2047 0.6766±0.1079 LaBraM 5.8M Y 0.6851±0.0063 0.3703±0.0125 0.7576±0.0067 BENDR - Y 0.7067±0.0011 0.4131±0.0022 0.7854±0.0029 EEGPT 25M Y 0.7212±0.0019 0.4426±0.0037 0.8059±0.0032 LCM (Ours) 33.9M Y 0.7523±0.0097 0.4731±0.0082 0.8244±0.0026

### 3.3 Results

The experiment result as shown in Table 2. It presents the results of different universal EEG models on the BCIC-2A and BCIC-2B datasets. Our proposed LCM model achieves the highest performance across all evaluation metrics, demonstrating its effectiveness in EEG representation learning.

Compared to previous state-of-the-art models, LCM shows significant improvements in Balanced Accuracy, Cohen’s Kappa, and Weighted F1 / AUROC. In terms of Balanced Accuracy, LCM outperforms EEGPT by 3.2% on BCIC-2A and 3.11% on BCIC-2B. The improvements over the best non-EEGPT baseline, LaBraM, are 5.53% and 6.72%, respectively. For Cohen’s Kappa, LCM achieves the most substantial gains, surpassing EEGPT by 3.52% on BCIC2A and 6.89% on BCIC-2B, while the improvements over LaBraM reach 11.28% and 27.78%. In Weighted F1 / AUROC, LCM surpasses EEGPT by 2.17% on BCIC-2A and 1.85% on BCIC-2B, with larger improvements over LaBraM at 4.12% and 6.68%, respectively.

Notably, even without pretraining, LCM surpasses several pretrained models on the BCIC datasets, highlighting its strong intrinsic generalization capability. This suggests that LCM’s architecture and learning strategy effectively capture meaningful EEG representations, reducing reliance on extensive pretraining while maintaining superior performance.

LCM demonstrates particularly strong improvements in Cohen’s Kappa, with relative gains of up to 67.98% over the weakest baseline, BIOT, highlighting its superior model consistency. The performance increase in Weighted F1 / AUROC indicates that LCM effectively reduces misclassification bias across multiple classes. The results confirm that LCM generalizes well across both datasets, validating its ability to learn robust EEG representations.

LCM significantly outperforms all baseline models, including BIOT, BENDR, LaBraM, and EEGPT, across all evaluation metrics. The improvements in Cohen’s Kappa suggest that LCM provides more reliable predictions, while gains in Balanced Accuracy and Weighted F1 / AUROC confirm its ability to capture meaningful EEG features. These findings establish LCM as a strong universal

EEG model for motor imagery classification and related EEG-based tasks.

### 4 Conclusions

In this work, we introduced the Large Cognition Model (LCM), a transformer-based EEG foundation model designed to handle diverse datasets and tasks. By combining contrastive learning, masked feature reconstruction, and cross-montage encoding, LCM learns robust EEG representations that generalize well across subjects and recording conditions. Our results show that LCM outperforms state-of-the-art models in multiple EEG benchmarks, proving its effectiveness in capturing meaningful brain signal patterns.

One of the biggest strengths of LCM is its ability to adapt to different datasets and tasks without heavy fine-tuning. This makes it a powerful tool for applications like cognitive state decoding, disease classification, and brain-computer interfaces (BCIs). It brings us a step closer to having a universal EEG model that can be easily applied to a wide range of real-world scenarios.

Of course, there’s still room for improvement. Future work could focus on refining the way the model handles spatial and temporal EEG features to make it even more interpretable. Exploring multimodal approaches—like integrating EEG with other biosignals—might also enhance its performance. Lastly, larger and more diverse pretraining datasets will be key to further boosting its generalization ability.

### References

- [1] Chi-Sheng Chen. 2024. NECOMIMI: Neural-Cognitive Multimodal EEG-informed Image Generation with Diffusion Models. arXiv preprint arXiv:2410.00712 (2024).
- [2] Chi-Sheng Chen, Samuel Yen-Chi Chen, Aidan Hung-Wen Tsai, and Chun-Shu Wei. 2024. Qeegnet: Quantum machine learning for enhanced electroencephalography encoding. In 2024 IEEE Workshop on Signal Processing Systems (SiPS). IEEE, 153–158.
- [3] Chi-Sheng Chen, Aidan Hung-Wen Tsai, and Sheng-Chieh Huang. 2024. Quantum multimodal contrastive learning framework. arXiv preprint arXiv:2408.13919

(2024).

- [4] Chi-Sheng Chen and Wei-Sheng Wang. 2024. Psycho Gundam: Electroencephalography based real-time robotic control system with deep learning. arXiv preprint arXiv:2411.06414 (2024).

- [5] Chi-Sheng Chen and Chun-Shu Wei. 2024. Mind’s Eye: Image Recognition by EEG via Multimodal Similarity-Keeping Contrastive Learning. arXiv preprint arXiv:2406.16910 (2024).
- [6] Ary L Goldberger, Luis AN Amaral, Leon Glass, Jeffrey M Hausdorff, Plamen Ch Ivanov, Roger G Mark, Joseph E Mietus, George B Moody, Chung-Kang Peng, and H Eugene Stanley. 2000. PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals. circulation 101, 23

(2000), e215–e220.

- [7] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick.

2022. Masked autoencoders are scalable vision learners. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 16000–16009.

- [8] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. 2024. Large brain model for learning generic representations with tremendous EEG data in BCI. arXiv preprint arXiv:2405.18765 (2024).
- [9] Bu Jin, Shuning Xue, Jie Jiang, Longteng Guo, Xinxin Zhu, Jin Zhou, Jing Liu, et al.

2025. UniEEG: Advancing Universal EEG Representation with Electrode-Wise Time-Frequency Pretraining. (2025).

- [10] Demetres Kostas, Stephane Aroca-Ouellette, and Frank Rudzicz. 2021. BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data. Frontiers in Human Neuroscience 15 (2021), 653659.
- [11] Laura Marie Krumm, Dominik Kranz, Mustafa Halimeh, Alexander Nelde, Edilberto Amorim, Jin Jing, Sahar Zafar, Robert Thomas, Brandon Westover, and Christian Meisel. 2024. Towards a Universal Map of EEG: A semantic, lowdimensional manifold for EEG Classification, Clustering and Prognostication. medRxiv (2024), 2024–10.
- [12] Cheng-Ta Li, Chi-Sheng Chen, Chih-Ming Cheng, Chung-Ping Chen, Jen-Ping Chen, Mu-Hong Chen, Ya-Mei Bai, and Shih-Jen Tsai. 2023. Prediction of antidepressant responses to non-invasive brain stimulation using frontal electroencephalogram signals: Cross-dataset comparisons and validation. Journal of Affective Disorders 343 (2023), 86–95.

- [13] David Steyrl, Reinhold Scherer, Josef Faller, and Gernot R Müller-Putz. 2016. Random forests in non-invasive sensorimotor rhythm brain-computer interfaces: a practical and convenient non-linear classifier. Biomedical Engineering/Biomedizinische Technik 61, 1 (2016), 77–86.
- [14] Michael Tangermann, Klaus-Robert Müller, Ad Aertsen, Niels Birbaumer, Christoph Braun, Clemens Brunner, Robert Leeb, Carsten Mehring, Kai J Miller, Gernot R Müller-Putz, et al. 2012. Review of the BCI competition IV. Frontiers in neuroscience 6 (2012), 55.
- [15] Guangyu Wang, Wenchao Liu, Yuhong He, Cong Xu, Lin Ma, and Haifeng Li.

2024. EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. In The Thirty-eighth Annual Conference on Neural Information Processing Systems.

- [16] Yijun Wang, Xiaogang Chen, Xiaorong Gao, and Shangkai Gao. 2016. A benchmark dataset for SSVEP-based brain–computer interfaces. IEEE Transactions on Neural Systems and Rehabilitation Engineering 25, 10 (2016), 1746–1752.
- [17] Chaoqi Yang, M Brandon Westover, and Jimeng Sun. 2023. BIOT: Cross-data biosignal learning in the wild. arXiv preprint arXiv:2305.10351 (2023).
- [18] Wei-Long Zheng and Bao-Liang Lu. 2015. Investigating critical frequency bands and channels for EEG-based emotion recognition with deep neural networks. IEEE Transactions on autonomous mental development 7, 3 (2015), 162–175.
- [19] Qiushi Zhu, Xiaoying Zhao, Jie Zhang, Yu Gu, Chao Weng, and Yuchen Hu.

2023. Eeg2vec: Self-Supervised Electroencephalographic Representation Learning. arXiv preprint arXiv:2305.13957 (2023).

Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009

