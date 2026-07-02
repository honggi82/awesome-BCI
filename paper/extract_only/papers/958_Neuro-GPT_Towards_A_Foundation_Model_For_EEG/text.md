# arXiv:2311.03764v4[cs.LG]2Mar2024

NEURO-GPT: TOWARDS A FOUNDATION MODEL FOR EEG Wenhui Cui1, Woojae Jeong1, Philipp Th¨olke2, Takfarinas Medani1, Karim Jerbi2,3,4, Anand A. Joshi1, Richard M. Leahy1 1 Ming Hsieh Department of Electrical and Computer Engineering, University of Southern California, Los Angeles, CA, USA 2 Psychology Department, Universit´e de Montr´eal, Montreal, QC, Canada

- 3 Mila (Quebec AI research institute), Montreal, QC, Canada,
- 4 UNIQUE (Quebec Neuro-AI research center), QC, Canada

## ABSTRACT

To handle the scarcity and heterogeneity of electroencephalography (EEG) data for Brain-Computer Interface (BCI) tasks, and to harness the power of large publicly available data sets, we propose Neuro-GPT, a foundation model consisting of an EEG encoder and a GPT model. The foundation model is pre-trained on a large-scale data set using a self-supervised task that learns how to reconstruct masked EEG segments. We then fine-tune the model on a motor imagery classification task to validate its performance in a low-data regime (9 subjects). Our experiments demonstrate that applying a foundation model can significantly improve classification performance compared to a model trained from scratch, which provides evidence for the generalizability of the foundation model and its ability to address challenges of data scarcity and heterogeneity in EEG. The code is publicly available at https://github.com/wenhui0206/NeuroGPT.

Index Terms— Foundation Model, EEG, GPT, Encoder

## 1. INTRODUCTION

The limited scale of training data for electroencephalography (EEG) based Brain-Computer Interface (BCI) classification tasks poses challenges to applying deep learning models. These models require a large amount of training data to converge and generalize to unseen testing data. However, individual differences can lead to heterogeneous feature representations across subjects [1], which makes it difficult to generalize the model across subjects. EEG’s high-dimensional nature and limited availability for specific tasks create additional barriers to the convergence of these models.

One common approach is to learn generalizable features from large amounts of data using self-supervised learning and then transfer to the task of interest [2]. Here, we address the question of whether we can train a model on large-scale EEG datasets using a self-supervised task and then transfer the pretrained knowledge to enhance performance on a downstream

task. Large language models (LLMs) in natural language processing (NLP) tasks have proven extraordinarily successful using this approach. Similar models have also shown remarkable performance in other tasks including image and video generation [3], medical question answering [4], and neural activity analysis [5, 6, 7]. Despite the popularity of LLMs, there have been relatively few attempts to adapt them to EEG data. The work in [8] employed a BERT-inspired [9] approach to pre-train a transformer model on massive EEG data using a contrastive self-supervised task. However, it exhibited limited generalizability to downstream tasks.

Here we aim to lay the groundwork for developing foundation models for EEG. We employ a Generative Pre-trained Transformer (GPT) model [10], which uses a decoder-only transformer architecture and is trained to predict the next masked token given a sequence of tokens as input (autoregressive training). In text-based tasks, a sentence is broken down into tokens as input units to the model. A token can be a few characters or a word, depending on the language and context. To adapt the GPT model to EEG data, we split the whole time series into fixed-length “chunks”, treating each chunk as a token. An EEG encoder is incorporated to extract representative features from raw EEG data. NeuroGPT is a foundation model consisting of an EEG encoder to extract spatio-temporal features from EEG data, and a GPT model that uses self-supervision to predict the masked chunks. The foundation model is pre-trained on the TUH EEG dataset [11]. We fine-tune the model on a motor imagery classification task where only 9 subjects are available. Experiments showed that the EEG encoder learns meaningful features that are generalizable to the downstream task.

## 2. METHODS

In this section we introduce the architecture of Neuro-GPT, the pre-training details, and the fine-tuning strategies. We divide the raw EEG data into fixed-length chunks from which we generate a sequence of tokens corresponding to contigu-

ous data chunks. The GPT model then learns to predict masked tokens. Employing chunks of raw EEG signals directly as input tokens to the GPT model would be problematic. Given the high dimensionality and low signal-to-noise ratio of EEG data [12], predicting raw signals is particularly challenging for the GPT model, and it may not learn meaningful features given the presence of noise. Thus, we introduce an EEG encoder [13] comprising convolutional and transformer layers to extract spatio-temporal features from the raw EEG. We input chunks of EEG into the encoder to generate the embeddings. These embeddings serve as a lower-dimensional and denoised representation of the raw EEG signals, not only simplifying the prediction of the masked chunk for the GPT model but also enhancing its ability to capture informative temporal correlations and patterns. The overall Neuro-GPT pipeline is illustrated in Figure 1.

[Figure 1]

Fig. 1. Neuro-GPT Pipeline: the EEG encoder takes chunks of EEG data as input and generates embeddings as tokens for the GPT model. The last embedded chunk in the sequence is masked. The GPT model then predicts the masked chunk and a reconstruction loss is computed between the prediction and the original embedding token.

## 2.1. Neuro-GPT Pipeline

EEG Encoder We adopt an encoder architecture incorporating both convolutional and self-attention modules. This arrangement has achieved state-of-the-art performance in BCI classification tasks [13]. We split the raw EEG signals into N chunks, each of time length T. This results in a sequence of chunks denoted {D1,D2,··· ,DN}. Each chunk is of dimension C × T, where C is the number of channels. Each chunk is treated as an individual training sample in the encoder. In the convolutional module, we apply a temporal convolution filter to the time series and a spatial convolution filter to the electrodes of the EEG. Then after average pooling, the extracted local features are fed into the self-attention layers to incorporate temporal dependencies within a chunk. The self-attention mechanism combined with convolution will encode the spatio-temporal features of each chunk. The outputs of the encoder are the embedded chunks or tokens: {H(D1),H(D2),··· ,H(DN)}, where H denotes the map-

[Figure 2]

Fig. 2. Causal masking: consider a sequence with four tokens (chunks). We duplicate the sequence three times and progressively mask (represented in orange) one token within each duplicated sequence.

ping learned by the EEG encoder from raw EEG signals to embeddings.

Causal Masking We apply a novel causal masking scheme to the tokens generated by the embedding module. As illustrated in Fig. 2, we first duplicate the sequence of tokens. Starting from the second token, one token is masked and subsequent tokens are zeroed-out in each duplicated sequence. The masked token is replaced with a learnable token M of the same dimension. So, after causal masking, the input sequence to the GPT model is

{H(D1),M,0,··· ,0}, {H(D1),H(D2),M,0,··· ,0}, ··· , {H(D1),H(D2),H(D3),··· ,M}

(1)

The pre-training of Neuro-GPT utilizes a self-supervised task, where the GPT model predicts every masked token in each sequence. We use a causal reconstruction loss defined in Eq. 2 as the self-supervised pre-training objective.

N

1 N − 1

∥Yˆi − H(Di)∥22

L =

(2)

i=2

where Yˆi = G[M|H(Di−1),H(Di−2),··· ,H(D1)]

where G denotes the GPT model. We aggregate the reconstruction losses of masked tokens at each position. The predicted token Yˆi produced by the GPT model is inferred based on the preceding tokens. By predicting the masked token separately from 1, 2, and 3 preceding tokens the model gains insight into the underlying temporal correlations in brain activity across different time scales. Thus the GPT model is potentially able to capture the dynamic evolution of brain activity more accurately.

GPT Model The GPT model employs a decoder-only transformer architecture consisting of a multi-layered stack of self-attention and feed-forward modules, enabling it to capture the global dependencies between tokens. Unlike BERT [9], which randomly masks some tokens in a sequence and the model predicts the masked tokens at random

positions, GPT always predicts the next masked token given preceding tokens, also known as auto-regressive training [14]. This guarantees that the prediction of EEG embeddings considers the causal temporal relationship between tokens, thus improving our model of the underlying brain activity patterns.

## 2.2. Pre-training

Pre-training Dataset: The large-scale public dataset, Temple University Hospital (TUH) EEG corpus, is used as the pre-training dataset. TUH EEG corpus comprises a diverse archive of clinical EEG recordings from 14,987 subjects with multiple sessions. The archive has over 40 different channel configurations and varying duration of recordings [11]. The sample frequency ranges from 250 - 1024 Hz, with the majority of recordings sampled at 250 Hz.

Preprocessing: We preprocessed the TUH EEG dataset using the Brainstorm software [15] in MATLAB (Mathworks, Inc.). Based on the channel labels, we selected 22 channels corresponding to the extended international 10-20 system (Fp1, Fp2, F7, F3, Fz, F4, F8, T1, T3, C3, Cz, C4, T4, T2, T5, P3, Pz, P4, T6, O1, Oz, O2). Channels with zero or missing signals throughout the recording sessions were marked as bad channels. The signals of the bad channels were interpolated by a weighted average of all neighboring channels with a maximal distance of 5cm between neighbors. EEG recordings were re-referenced to the average of 22 channels. We removed power line noise (60 Hz) using a notch filter and bandpass-filtered the data (0.5-100 Hz). All recordings were re-sampled to 250 Hz. We performed a DC offset correction and removed linear trends from the data. A z-transform was applied along the time dimension within each recording to normalize the data.

Implementation Details: During the pre-training phase, we simultaneously pre-train the entire Neuro-GPT model. After experimenting with various input configurations, we set the standard input as: 32 chunks, each with a length of 2 seconds and a 10% (0.2 second) overlap. We randomly select a starting point for each EEG recording and then sample 32 contiguous chunks. If the total length of the EEG recording is shorter than the length to be sampled (57.8 seconds), we apply zero-padding to the end of the sequence. The attention weights are set to zero for the zero-padded part. In each training batch, one sampled sequence is considered as a single training sample. The EEG encoder consists of two convolutional layers followed by six self-attention layers, with an embedding dimension of 1,080. The first convolutional layer has a kernel size of (1,25), while the second has a kernel size of (C,1), with C being the number of channels [13].

We employ the open-source GPT-2 [10] model provided by Hugging Face [16], which has an embedding dimension of 1024. We specify 6 transformer decoder layers in the GPT2 model. A linear layer is added before the GPT-2 model to project the embedding dimension from 1080 to 1024. We pre-

processed 20,000 EEG recordings from the TUH EEG dataset with a total duration of 5656 hours. We train the model on 19,000 EEG recordings for 135 epochs. The remaining 1000 EEG recordings were used as a hold-out validation set.

## 2.3. Downstream Fine-tuning

Downstream Dataset: We define the downstream task as motor imagery classification, using the BCI Competition IV Dataset 2a provided by Graz University of Technology [17]. The BCI 2a dataset consists of nine subjects performing four motor imagery tasks: imagining left hand, right hand, feet, and tongue movement. Two sessions were collected on different days for each subject, using 22 Ag/AgCl electrodes at a sampling frequency of 250 Hz. Each recording has 72 trials per task, yielding a total of 288 trials. All trials from both sessions were used as training or testing samples - importantly, no subjects in the training data were included in the testing. Data was bandpass-filtered between 0.5 Hz and 100 Hz and normalized across time for each trial. We extract the sequence from t = 2s to t = 6s for each trial, which corresponds to the period when the cue and motor imagery tasks are performed.

Channel resampling: The downstream dataset has a different subset of 22 channel locations on the scalp from the pre-training dataset. To match the channel configuration between the two datasets, we resampled the downstream data to the pre-training dataset channel configuration using a 22×22 transformation matrix. The transformation matrix was computed by solving the forward and the inverse problem for the source localization, mapping from one sensor configuration to the cerebral cortex and then back to the second configuration [18, 19].

Fine-tuning Details: We fine-tune the pre-trained model on the BCI 2a dataset for the 4-class motor imagery classification task. To fully explore the potential of the foundation model, we designed three fine-tuning strategies:

- 1. Encoder-only: Remove the GPT model and fine-tune the pre-trained EEG encoder only. (Note that in this case the model still benefits from including GPT in pre-training through the self-supervised training of the encoder in combination with the GPT model.)
- 2. Encoder+GPT: Fine-tune the entire Neuro-GPT model.
- 3. Linear: Remove the GPT model, fix the EEG encoder and fine-tune only the linear head (3 linear layers).

All strategies use the same pre-trained model and involve adding a linear head consisting of 3 linear layers to the end of the model for classification. For the Encoder+GPT strategy, we maintain the same number of chunks, the same chunk length, and the same overlapping ratio as used in the pretraining stage. Since only a 4-seconds sequence is extracted from each EEG recording in the BCI 2a dataset, we apply zero-padding to the end of the sequence. In the Encoderonly strategy, we feed the model with two non-overlapping 2-second chunks, and no zero-padding is applied. For the

Linear strategy, all the pre-trained parameters from the EEG encoder are frozen during fine-tuning. We only fine-tune the linear head, which takes the output features of the EEG encoder as input. No masking is applied during fine-tuning.

## 3. EXPERIMENTS AND RESULTS

Fine-tuning Classification Performance: Unlike previous studies which only focused on within-subject classification [20, 13], we performed leave-one-subject-out crossvalidation, which is more challenging due to the high intersubject variance. We compute the average classification accuracy across subjects. To explore the benefits of applying a pre-trained foundation model, we compare the classification performance of a model trained from scratch (w/o pre-training) to that of the same model fine-tuned on the pre-trained foundation model (w/ pre-training). In addition, we compare the proposed Neuro-GPT with BENDR [8], a BERT-inspired transformer model trained on TUH EEG data using contrastive self-supervised learning and then fine-tuned on the BCI classification data. As shown in Table 1, NeuroGPT significantly improved the classification performance compared with the best performance of BENDR, and outperforms other methods for motor imagery classification using leave-one-subject-out cross-validation.

The performance of models with pre-training surpassed that of models without pre-training for both Linear and Encoder-only fine-tuning strategies, highlighting that applying a foundation model to a downstream task can lead to effective feature learning and, consequently, improved performance. Among the fine-tuning strategies, Encoder-only achieved the best performance, indicating that the encoder learned expressive and generalizable features during pretraining, thus facilitating the learning of distinguishable features for downstream tasks. The Encoder+GPT yielded worse performance, possibly because the GPT model only serves as

|Method<br><br>|w/o Pre-train w/ Pre-train|
|---|---|
|Linear Encoder-only Encoder+GPT|0.398 ± 0.054 0.443 ± 0.051<br><br>0.606 ± 0.098 0.645 ± 0.104<br><br>0.596 ± 0.090 0.586 ± 0.098<br><br>|
|BENDR [8] SVM [21] EEGNet [22] CTCNN [23] CCNN [24] NG-CRAM [25]<br><br>|/ 0.426<br><br>0.361 ± 0.082 / 0.513 ± 0.052 / 0.477 ± 0.151 / 0.553 ± 0.101 / 0.601 ± 0.102 /|

Table 1. A comparison of means and stds of four-class classification accuracy among different methods. The first three rows are three fine-tuning strategies of Neuro-GPT, accuracies reported in other work are shown in the bottom rows.

an auxiliary component to assist the EEG encoder in encoding meaningful features from raw EEG data. The GPT model has more trainable parameters than the encoder. Fine-tuning a large model on a small data-set can lead to over-fitting. To examine whether the features learned by the foundation model are linearly separable, we input the features generated by the EEG encoder to the linear head for classification. The classification accuracy achieved by fine-tuning only the linear head is 0.443 vs. 0.398 with out pre-training, indicating that the EEG encoder can encode meaningful features through pre-training.

Hyper-parameter Evaluation in Pre-training: To explore the optimal input configurations for the foundation model during pre-training, we conducted experiments with varying numbers of chunks (4, 8, 16, 32), chunk lengths (1s, 2s, 4s), and overlapping ratios (10%, 50%). Different model architectures were also investigated. Key findings include:

- • Chunks with a 1-second length are more straightforward to predict (as embedded tokens) but led to poorer downstream performance.
- • Chunks with longer lengths are more challenging to predict but enhance downstream performance.
- • Increasing the number of chunks is beneficial. Training with 32 and 16 chunks yielded better downstream results than training with 8 or 4 chunks.
- • Increasing the overlapping ratio to 50% improved reconstruction, but degraded the downstream performance.
- • Increasing the embedding dimension of GPT-2 model (768 → 1024) improved downstream performance.
- • Reducing the number of self-attention layers in the encoder (6 → 4,2) degraded downstream performance.
- • Adding more GPT decoder layers (6 → 8,10) did not improve downstream performance.

## 4. DISCUSSION

We have demonstrated that pre-training a foundation model on a large-scale EEG dataset boosts downstream task performance. Through exploring different fine-tuning strategies, we discovered that the pre-trained EEG encoder captures inherent and fundamental features of EEG that are generalizable across datasets, leading to significant improvements in classification performance.

## 5. ACKNOWLEDGMENT

This project is sponsored in part by the NIH under grant R01 EB026299 and in part by the Defense Advanced Research Projects Agency (DARPA) under cooperative agreement No. N660012324006. The content of the information does not necessarily reflect the position or the policy of the Government, and no official endorsement should be inferred.

## 6. REFERENCES

- [1] Y. Du et al., “Eeg temporal–spatial transformer for person identification,” Scientific Reports, vol. 12, no. 1, pp. 14378, 2022.
- [2] C. J. Reed et al., “Self-supervised pretraining improves self-supervised pretraining,” in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, 2022, pp. 2584–2594.
- [3] L. Yu et al., “Language model beats diffusion – tokenizer is key to visual generation,” 2023.
- [4] K. Singhal et al., “Towards expert-level medical question answering with large language models,” 2023.
- [5] A. Thomas et al., “Self-supervised learning of brain dynamics from broad neuroimaging data,” Advances in Neural Information Processing Systems, vol. 35, pp. 21255–21269, 2022.
- [6] J. Ortega Caro et al., “Brainlm: A foundation model for brain activity recordings,” bioRxiv, pp. 2023–09, 2023.
- [7] M. Azabou et al., “A unified, scalable framework for neural population decoding,” 2023.
- [8] D. Kostas, S. Aroca-Ouellette, and F. Rudzicz, “Bendr: using transformers and a contrastive self-supervised learning task to learn from massive amounts of eeg data,” 2021.
- [9] J. Devlin et al., “Bert: Pre-training of deep bidirectional transformers for language understanding,” arXiv preprint arXiv:1810.04805, 2018.
- [10] A. Radford et al., “Language models are unsupervised multitask learners,” OpenAI blog, vol. 1, no. 8, pp. 9, 2019.
- [11] I. Obeid and J. Picone, “The temple university hospital eeg data corpus,” Frontiers in neuroscience, vol. 10, pp. 196, 2016.
- [12] C. Q. Lai et al., “Artifacts and noise removal for electroencephalogram (eeg): A literature review,” in 2018 IEEE Symposium on Computer Applications & Industrial Electronics (ISCAIE). IEEE, 2018, pp. 326–332.
- [13] Y. Song et al., “EEG Conformer: Convolutional Transformer for EEG Decoding and Visualization,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 710–719, 2023.
- [14] T. B. Brown et al., “Language models are few-shot learners,” 2020.

- [15] F. Tadel et al., “Brainstorm: a user-friendly application for meg/eeg analysis,” Computational intelligence and neuroscience, vol. 2011, pp. 1–13, 2011.
- [16] T. Wolf et al., “Huggingface’s transformers: State-ofthe-art natural language processing,” 2020.
- [17] C. Brunner et al., “Bci competition 2008–graz data set a,” Institute for Knowledge Discovery (Laboratory of Brain-Computer Interfaces), Graz University of Technology, vol. 16, pp. 1–6, 2008.
- [18] J. C. Mosher et al., “Eeg and meg: forward solutions for inverse methods,” IEEE Transactions on biomedical engineering, vol. 46, no. 3, pp. 245–259, 1999.
- [19] S. Baillet et al., “Electromagnetic brain mapping,” IEEE Signal processing magazine, vol. 18, no. 6, pp. 14–30, 2001.
- [20] C. Zhang et al., “Eeg-inception: an accurate and robust end-to-end neural network for eeg-based motor imagery classification,” Journal of Neural Engineering, vol. 18, no. 4, pp. 046014, 2021.
- [21] V. P. Oikonomou et al., “A comparison study on eeg signal processing techniques using motor imagery eeg data,” in 2017 IEEE 30th international symposium on computer-based medical systems (CBMS). IEEE, 2017, pp. 781–786.
- [22] V. J. Lawhern et al., “Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, pp. 056013, 2018.
- [23] R. T. Schirrmeister et al., “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391–5420, 2017.
- [24] S. U. Amin et al., “Deep learning for eeg motor imagery classification based on multi-layer cnns feature fusion,” Future Generation computer systems, vol. 101, pp. 542– 554, 2019.
- [25] D. Zhang et al., “Motor imagery classification via temporal attention cues of graph embedded eeg signals,” IEEE journal of biomedical and health informatics, vol. 24, no. 9, pp. 2570–2579, 2020.

