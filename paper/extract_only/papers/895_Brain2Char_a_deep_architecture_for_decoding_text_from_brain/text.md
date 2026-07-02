# arXiv:1909.01401v1[cs.LG]3Sep2019

## Brain2Char: A Deep Architecture for Decoding Text from Brain Recordings

Pengfei Sun Center for Integrative Neuroscience UCSF

Gopala K. Anumanchipalli Center for Integrative Neuroscience UCSF

Edward F. Chang Center for Integrative Neuroscience UCSF

### Abstract

Decoding language representations directly from the brain can enable new BrainComputer Interfaces (BCI) for high bandwidth human-human and human-machine communication. Clinically, such technologies can restore communication in people with neurological conditions affecting their ability to speak. In this study, we propose a novel deep network architecture Brain2Char, for directly decoding text (speciﬁcally character sequences) from direct brain recordings (called Electrocorticography, ECoG). Brain2Char framework combines state-of-the-art deep learning modules — 3D Inception layers for multiband spatiotemporal feature extraction from neural data and bidirectional recurrent layers, dilated convolution layers followed by language model weighted beam search to decode character sequences, optimizing a connectionist temporal classiﬁcation (CTC) loss. Additionally, given the highly non-linear transformations that underlie the conversion of cortical function to character sequences, we perform regularizations on the network’s latent representations motivated by insights into cortical encoding of speech production and artifactual aspects speciﬁc to ECoG data acquisition. To do this, we impose auxiliary losses on latent representations for articulatory movements, speech acoustics and session speciﬁc non-linearities. In 3 participants tested here, Brain2Char achieves 10.6%, 8.5% and 7.0% Word Error Rates (WER) respectively on vocabulary sizes ranging from 1200 to 1900 words. Brain2Char also performs well when 2 participants silently mimed sentences. These results set a new state-of-the-art on decoding text from brain and demonstrate the potential of Brain2Char as a high-performance communication BCI.

Several demonstrations in recent years have shown that it is possible to decode cognitive, linguistic and speech representations directly from the brain through machine learning on neurophysiological imaging datasets. Attempts have been successful in decoding word classes or semantic representations from fMRI data (Mitchell, et al. (2008), Wehbe, et al. (2014), Huth, et al. (2016), Pereira, et al. (2018)). However, since speech communication happens at a much faster rate, accurately decoding cortical function at the rate of ﬂuent speech requires neurophysiological imaging at higher spatial resolution (in the order of millimeters) and temporal resolution (in the order of milliseconds). Among the modalities that offer the best resolution for assaying neural function is Electrocorticography (ECoG, Sejnowski, et al. (2014), Chang, et al. (2015)). ECoG is an invasive neuroimaging technique where a ﬂexible array of electrodes (3 in × 3 in) is placed directly on the surface of the cortex as part of clinical treatment for intractable epilepsy. Each electrode records the raw voltage potentials at the cortical surface, an aggregate electrical activity of thousands of neurons underneath the contact. This setting provides a unique opportunity to create datasets of parallel neural and behavioral data as participants perform tasks such as listening or speaking naturally. Indeed, several key results have

Preprint. Under review.

been published in recent literature on inferring speech representations directly from associated ECoG activity, broadly referred to here as Neural Speech Recognition (NSR).

Prior works on speech/language decoding from ECoG used data either from the auditory or the speech motor cortices. Pasley et al. (2012) and Akbari et al. (2019) report methods for direct reconstruction of external speech stimuli from auditory cortex activations. Martin et al. (2016) use non-linear SVM to classify auditory stimuli and Moses et al. (2016) use Hidden Markov Modeling to infer continuous phoneme sequences from neural data during listening. Similarly, for neural decoding during speech production, Mugler et al. (2018) have used linear models to classify phonemes and Herff et al. (2015) use HMM/GMM based decoding to achieve a WER of 60% on a 50 vocabulary task. Recent attempts have focused on decoding audible speech directly from the sensorimotor cortex, including Angrick et al. (2019), using deep convolutional architectures (Wavenet) and Anumanchipalli et al. (2019), using recurrent architectures.

In speech processing applications like automatic speech recognition (ASR) and text-to-speech synthesis (TTS), much progress has been made to achieve near-human performance on standard benchmarks. These include the use of recurrent (Hannun et al. (2014)) and convolutional architectures (Collobert et al. (2016)) towards End-to-End speech recognition minimizing CTC loss, which remain unexplored for decoding text from brain data. Given the demonstration of naturalistic and continuous speech synthesis directly from the brain, one way to approach the Brain-to-text problem is a 2 stage model where neural data is converted to speech, which can then be converted to text using a state-of-the-art ASR system. Indeed, we propose a strong baseline for the Brain-to-text problem along these lines, that to our knowledge, already achieves the best reported performance on this task. To improve this baseline further, we propose Brain2Char, a deep network architecture that borrows ideas from speech processing, and proposes optimizations appropriate for NSR. Brain2Char implements an End-to-End network that jointly optimizes various sub-problems, like neural feature extraction, optimizing latent representations and session calibration through regularization via auxiliary loss functions. Performance of Brain2Char is quantiﬁed on 4 volunteer participants who spoke overtly or silently, and various aspects of decoder design are objectively evaluated.

### 1 Neural Speech Recognition from ECoG

Unsupervised modelling techniques have shown great promise in various speech and language applications, but these methods rely on vast amounts of training data. Since ECoG data is acquired from individual participants in clinical settings, the amount of useful training data is limited in most cases. Moreover, since individual brains differ anatomically, neural data cannot be directly pooled across participants. Hence, conventional speech recognition methods do not work right off-the-shelf for neural data without customization. Ideally, a neural speech recognizer is robust to all known aspects of neural and behavioral variability to model the conversion of one to the other. Previous insights from neurobiology have prescribed the analytic amplitude of the High Gamma frequency band (70-150 Hz) as a robust feature that correlates well with multi-unit spiking (Edwards, et al. (2005), Crone, et al. (2011)), and that there is complementary information in lower frequency ranges. Besides these features, there are aspects speciﬁc to ECoG and speech production that need to be modelled in NSR. Here are some factors that contribute to neural variance in ECoG signal, as related to speech production –

Neural Basis of Speech Production : Neural mechanisms for linguistic planning and execution occur at diverse timescales, and at diverse alignment offsets with respect to the speech signal. Also, different cortical regions encode distinct aspects of speaking. For example, the IFG is linked to motor sequence planning (Flinker et al. (2015)) and the vSMC is linked to the articulatory aspects in producing speech (Chartier, et al. (2018), Mugler, et al. (2014)). Each electrode location in the vSMC codes a unique kinematic plan, spanning multiple vocal tract articulators and timescales to orchestrate continuous speech articulation. Electrodes in the STG encode spectrotemporal aspects of speech signal (Mesgarani et al. (2014)). This diversity of cortical function and tuning properties contributes to most of the speech related variability in the ECoG signal. It is therefore important for an NSR system to model these representations, as appropriate for a given electrode location and participant behavior (e.g., whether it’s a speaking task or a listening task).

Intrinsic Neural Variability: ECoG measures the local ﬁeld potentials at the cortical surface. Since each electrode contact records from thousands of underlying neurons, the signal at each may not be entirely speciﬁc to speech production. Some cortical regions responsible for certain articulatory

phonetic sequences may not even be sampled, given a particular electrode coverage, or there may be redundancy across neighbouring electrodes. Furthermore, the intrinsic neural dynamics (Churchland, et al. (2010), Sun, et al. (2019)) mask the true signal causal to producing speech. All of these aspects contribute to a poor signal-to-noise ratio (SNR) in the neural data. It is important for NSR systems to extract meaningful features from across the diverse spatial and temporal scales of the ECoG data.

Cross-session variability: Typical ECoG data is collected in multiple, short sessions spread over a week or so, where electrode leads from the brain are manually connected to a preampliﬁer before recording neural data for each session. An artifactual aspect of neural recordings is the non-stationarity in the signal across recording sessions. This may be due to different “baseline" brain states in each session, or some electrode channels not recording (e.g., sensor losing contact with the cortical surface), or (more rarely) the entire grid slightly shifted on the cortical surface, causing differences across sessions that are unrelated to speech production process itself. An ideal NSR approach subsumes session speciﬁc corrections to improve cross session compatibility in neural data.

Since most of these issues cannot be deterministically modelled, it is necessary for neural speech recognition to be realized within an unsupervised framework, jointly optimizing neural feature extraction, latent representation learning, session calibration and text prediction, all within the same model. We now describe Brain2Char, a deep learning architecture that implements such a framework.

#### 1.1 Brain2Char Architecture

We propose a neural speech recognition framework Brain2Char with a modular architecture comprising three parts: the neural feature encoder, the text decoder and the latent representation regularizer. The modular structure is convenient for network optimization, and each sub module can be independently improved based on the general design considerations of NSR systems mentioned in the earlier section. The inference model consists of the encoder and the decoder, and the regularization networks are only used at training time. Figure1 illustrates the architecture of the Brain2Char decoder.

Inference network Regularization network

Inception Block

BiLSTM

Inception Block Bagging

Time label

| |
|---|

| | |
|---|---|
| | |

CrossEntropy

ECoG

[Figure 1]

SMC

| | |
|---|---|
| | |

[Figure 2]

LM Convolution Dilated CNN

Dilated CNN

Y

MSELoss

| | |
|---|---|
| | |

CTC Loss

X

Time

MFCC

| | |
|---|---|
| | |

[Figure 3]

[Figure 4]

X

MSELoss

Y

CTC

- Figure 1: Architecture of Brain2Char: Neural data is recorded as participants produce speech. Different ﬁlters spanning multiple space, time and frequency dimensions convert recorded potentials into appropriate feature representations. The intermediate features are fed into regularization network and the decoder network. The regularization networks impose MSE losses on regressed speech representations and session embeddings. The decoder implements a sequence learning model that dilated CNNs convert the latent representations to character sequences, using language model weighted BeamSearch.

Notation: Brain2Char optimizes a transformation Φ to map the recorded neural signals X = {x1,x2,··· ,xn|xi ∈ Rt×w×h} to character sequences Z = {z1,z2,··· ,zm|zj ∈ Rv}. Here the index t,w,h refer to time dimension, the anterior-posterior (width) and dorsal-ventral (height) axes of the ECoG grid, and v refers to the embedding dimension of text vector. In the encoding phase, encoder Φe projects neural inputs X to latent feature space F, which in turn will be translated as

the outputs Z by decoder Φd in the decoding phase. Here capital F with upper index (e.g., Fh) represents the basis, whereas with the foot index (e.g., Fh) is vector.

#### 1.2 Neural Feature Encoder Network

The goal of the encoder is to extract the speech-speciﬁc part of the neural signal, robustly accounting for the spatial, temporal and spectral variations within the neural signals. In Brain2Char, the 3dimensional ECoG signals X are fed into the encoder stacked by network modules similar to inception nets (Szegedy et al. (2017)). A single inception layer parallelly employs several sub-networks to extract features at different resolutions, by choosing a set of hyperparameters specifying the number of channels, kernel size and number of stacked layers. This design is capable of extracting features at various space-time scales within single inception module, and aggregate these multi-resolution features. Therefore, the next stage can access robust features at different resolutions simultaneously.

The neural feature encoder Φe consists of several layers of grouped convolutional neural networks (CNN). For each single layer, a set of convolutional ﬁlters {W1,W2,···} are used in multiple sub-networks, where Wi ∈ Rc

in×kt×kw×kh×cout. For the weight tensor Wi, the spatial support of each kernel ﬁlter κi is kt × kw × kh. There are cin input channels and cout output feature maps. with the input tensor Λ ∈ Rt

in×win×hin×cin, the convolution between kernel function κi and the input tensor Λ can be translated as F(κi ∗ Λ) = F(κi) F(Λ), where F represents Fourier transform, ∗ and refer to convolution and Hadamard product, respectively. By utilizing different kernel sizes

kt,kw,kh, each Wi can extract components in certain frequency bands by imposing a group of kernel ﬁlters. Additionally, to ensure the extracted features are densely sampled at diverse resolutions, each sub-networks p in jth layer may use l stacked layers that employ a series of kernels κ with different sizes. Therefore, the output of sub-networks can be written as

Λ))), (1)

F{j,p|κ} = Wi(Wq(···(

l

where F{j,p|κ} refers to the features obtained at the pth sub-networks in jth layer of encoder by using kernel set {κ}. After multi-scale feature extractor, two Bi-LSTM layers are stacked to strengthen the sequence correlation learning within the latent representations. In the proposed framework, the output of the Bi-LSTM layers are referred as the latent feature representation Fh.

#### 1.3 Regularization network

To implicitly enforce a meaningful latent representation in the neural encoder, the regularization branch performs simple feed-forward transformations of the latent features of the encoder to account for known aspects of neural signal variance discussed earlier.

Session Calibration: To reduce the variabilty of neural signals X due to session speciﬁc artifacts, calibration across sessions is done to pool sessions in terms of their relative similarity to the earlier sessions. Since changes across sessions cannot be modelled systematically, in this study we introduce an implicit calibration on the encoded feature F to reduce intrinsic session-dependent variation. In other words, each latent feature Ft,t∈T

, which are indexed by continuous valued numbers. Instead of using one-hot vector to represent ST

within the time duration Ti can be assigned session labels ST

i

i

, we learned the time embedding vector QT

i

in a skip-gram fashion (Mikolov et al. (2013)). Similar to word embedding, QT

i

describes the correlation among ST based on their temporal positions. A regression layer M(·) would map the dynamic latent sequence Fh to the embedding QT

i

, and L = M(Fh) − Qt 2 is used as the cost function of time regularization.

i

Speech-speciﬁc latent representation: The basis space Fx representing neural signals X exist in a higher dimensional space compared to the basis space Fz of text Z. In Brain2Char architecture, the encoder projects the neural data X into the reduced latent space Fh and the decoder expands the latent feature Fh to span the basis of targets Z. If trained without regularization on the output of Φe, the encoder Φe explores quite a large space searching for a manifold where Fz ⊂ Fh. To reduce the search space, the language basis Fz can be directly used as the regression target of Φe. However, limited by the data, complete basis Fz is not obtainable. As the baseline we proposed, other accessible feature representation Fz , such as MFCC, can be used as the regression targets of Φe. Directly employing Fz ⊂ Fz as the output of encoder may over penalize the ECoG basis Fx. Therefore, a more practical approach is to keep Fh as the intermediate layer and apply empirical feature space Fz as the regularization. It retrains the pattern variance of Fx, whereas utilizes MFCC

from speech acoustics or articulatory kinematic movement to inform intrinsic feature space of Fh. That is {Fz \ Fz } ⊂ Fh. Generally, the regularization features Fz can be any type of features correlated with or generated from speech or text Z associated with productions. For instance, by applying autoencoder on speech acoustics, Akbari et al. (2018) derive a low dimensional basis utilized as the regularization component in auditory speech reconstruction. Assuming a set of feature basis {Fs

,···}, we can either utilize these feature basis independently, or in a more ensemble fashion, where a joint feature basis is learned. Here the index si refers to ith category features (e.g., MFCCs). Based on the obtained feature vectors {Fs

,Fs

1

2

i}, two types of regularizations are described as: Ψ(Fh,Fs

,··· ,Fs

αi Fh − Fs

) =

1

i

i

(2)

i

,··· ,Fs

) = Fh − Ω(Fs

,··· ,Fs

Ψ(Fh,Fs

) ,

1

i

1

i

where Ω represents projection operation, and Ψ is cost function. By using Ω, a new ensemble feature basis is incorporated to modulate the latent representation. Physiologically generative representations or close features derived from speech acoustics make better targets for regularization.

#### 1.4 Text Decoder Network

At the core, translating the latent feature Fh to character sequences is a sequence decoding task. In other words, any state-of-the-art sequence translation system can be adapted to the text decoder

network. In the context of our application, different temporal scale of latent features Fh must be used as appropriate, as the relationship between text and speech is temporally imprecise. Brain2Char model employs three layers of dilated CNNs to process the long-short term correlations, which could be more resistant to noise components (in comparison to sequence to sequence decoding, that decouples the features by locally transferring the state, and obviously is more vulnerable to background noise interference). In each dilated layer, 5 sub-layers as shown in ﬁg.1 are applied to learn the sequence correlations at various scales. The layer-wise residual connections ensure the features at different scale are processed simultaneously. Since the exact alignment of latent representations is hard to obtain (i.e., onset and offset of neural data corresponding to characters), on top of the dilated CNN, CTC is incorporated with 4-gram language model as the text decoder network. Together with feature regularization and the explicit language model used for beam search, the cost function for the overall Brain2Char decoder is

, (3)

L = α0LI +

iLsi

αs

si

where the ﬁrst component LI refers to the loss of the inference networks, and the second component is the summation of the loss of regularization networks.

Implementation We implemented our method using Tensorﬂow. In terms of model training, we use a cyclic learning rate with maximal value 0.005 and minimal value 0.0001. Linear decay coefﬁcients are applied to the weight coefﬁcients of regularization components. The batch size is 50 at the sentence level for training. The feature dimension of MFCC and AKT are 26 and 33, respectively. For 3D inception module, the kernel sizes kt,kw,kh along each axle are selected from {1,3,5,7}. The dimension reduction is achieved by using 2 step strides in inception modules. For dilated CNN, the ﬁlter size is ﬁxed as 11, and the dilated ratios for ﬁve sub-layer are [1,2,4,8,16]. The convlutional layer after the dialted CNN uses kernel size 1, and the output channel is the dimension of character vocabulary. Two BiLSTM layers are set at 0.5 dropout rate, and the output of dilated CNN is set 0.15 dropout rate. To ensure robust sequence learning, the onset and offset of neural features are randomly jittered about a time window aligned to speech boundaries. A 4-gram language model incorporated with beam search is be applied to the outputs of CTC. KenLM (Heaﬁeld et al. (2013)) is used to train the word language models of the speech corpus that is used for speaking task. Additionally, the pre-trained LibriSpeech language model in DeepSpeech (Hannun et al. (2014)) is used as a baseline language model. The weighting coefﬁcient of language model is set to 1.5.

### 2 Experimental Results

Data: In this study, data from four participants P1,P2,P3, and P4 is used. These volunteer participants read prompted sentences on a screen while their speech and ECoG data were synchronously recorded. The sentences were derived from MOCHA-TIMIT corpus (a 1900 word vocabulary task of 460 independent sentences, for participants P1 and P2) and a limited domain dataset of verbal

descriptions of 3 pictures (a 400 words vocabulary on controlled description and 1200 vocabulary on free-style interview task for participants P3 and P4). The total data collected across participants varied between 120 minutes to 200 minutes. Participants P3 and P4 also silently mimed a subset of 20 sentences without overt vocalization. The recordings were made in several one hour long sessions, over a week or more while participants were implanted with grids for clinical monitoring for seizure localization. Speciﬁcally, the neural data of subject P1, P2 and P4 are recorded with 16 × 16 electrode grid covering the ventral sensorimotor cortex (vSMC), inferior frontal gyrus(IFG) and superior temporal gyrus(STG), only subject P3 was recorded with 16 × 8 electrode grid covering only the dorsal half of the vSMC. All neural data was preprocessed to reject artifacts and extract the analytic amplitude in the High Gamma frequency band(70-150Hz) and low frequency component (0-40 Hz) z-scored appropriately. For the speech data collected, acoustic-to-articulatory inversion is performed to estimate the articulatory kinematic trajectories (AKT), and Mel Frequency Cepstral Coefﬁcients (MFCC) are extracted. All data were synchronously sampled at 200 Hz.

Baseline: We designed a baseline ECoG-to-text system inspired by previous demonstrations of speech synthesis from the ECoG data (Angrick, et al. (2019) and Anumanchipalli, et al. (2019)), and off-the-shelf ASR systems. We used DeepSpeech, a pretrained state-of-the-art ASR system to decode text from the acoustic features, which in turn are estimated from ECoG features using a neural feature encoder Φe, implemented as a 2 BiLSTM layers. Since neural speech synthesis does not yield perfectly intelligible speech, directly decoding neurally synthesized MFCCs through DeepSpeech resulted in poor performance (80% WER). To improve this, the baseline neural feature encoder Φe is optimized for the DeepSpeech network. The neural feature encoder is stacked on top of a pre-trained DeepSpeech network and trained on parallel ECoG, MFCC and Text data. The joint network is optimizes a CTC loss, and an optimally weighted auxiliary mean-squared error (MSE) loss on the MFCCs. We found it beneﬁcial to ‘freeze’ the pre-trained layers of DeepSpeech, and only allowing the neural encoder layers to be learnt, while still optimizing the joint loss.

Quantitative results. We conducted a quantitative evaluation of the baselines and the proposed Brain2Char architecture. Fig2(a) compares the performance of various systems with increasing amounts of training data. Systems indexed DS0 are a 2-stage implementation of speech synthesis from the brain using neural feature encoder Φe, followed by pretrained DeepSpeech to decode text. The baseline DS1 refers to the joint network where Φe is modulated by DeepSpeech, trained jointly optimizing the CTC loss on characters and MSE loss on intermediate MFCCs. Across 3 patients, the joint optimized DS1 systems show consistent gains of around 30% in WER over DS0. This suggests that acoustic features alone are not sufﬁcient to code neural representations and customizing the intermediate representations in Φe is critical. Fig2(a) also shows the performance of the proposed Brain2Char networks (indexed B2C) against these baselines. In all cases, we see signiﬁcant gains of an additional 30% in WER, and the performance trends with time also suggests that the architecture makes optimal utilization of the available data compared to the baseline (larger slope in WER gain with more data, whereas the baselines seem to plateau).

Since the training data from each subject is not an exhaustive representation of all phonetic aspects of English language, we wanted to see how important it is to have observed similar phonetic contexts in the training data. This analysis was done by varying the number of repetitions of the same sentence in several training runs of Brain2Char networks. Fig2(b) shows the WER as a trend against the number of prior repeats of testing sentences in training data (in other trials than those in test). It is clear that having several prior example trials of the sentence helps in future decoding of the same sentence at inference time.

Fig2(c) quantiﬁes the contribution of language models towards Brain2Char Performance. For different amounts of training data and for 3 participants, 3 different language modelling conditions at inference – decoding with no language model (indexed NL), the default language model in DeepSpeech trained on librispeech, a general purpose character-level language model of English ( _L1), and a task speciﬁc language model created using all training data from the task(_L2). It can be seen that language models help improve decoding performance, and task dependent language models help further. In all, Brain2Char achieves roughly 10% to 25% WER improvement across three subjects, and the performance improvements against librispeech based language model range from 3% up to 15%. It is to be noted that the performance is still respectable in the _NL conditions, possibly due to implicit language modeling in the text decoder. This may sometimes lead to overﬁtting if the decoder is simply memorizing the task language independently of the neural data. To test this, we ran inference on trials that were randomly cut off, either at the start or the end. Fig2(d) shows the error rates as a

function of amount of signal cut off (in seconds, either at the start, or at the end of a trial, indexed _onset and _offset). The results conﬁrm that Brain2Char is sensitive to the length of the trial in time, without completely memorizing entire sentences. It also seems that onset cutoff is worse than offset cutoff.

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

- Figure 2: Performance evaluation of Brain2Char (a) WER as a function of increasing amount of training data for baselines and Brain2Char. (b) The effect on WER of sentences against the numer of trials for a given sentence provided in training. (c) Contribution of various language models. (d) Performance on partial neural data with cutoff on either onset or offset.

The offset cutoff condition in Fig2(d) also shows that Brain2Char is capable of synchronous, incremental decoding (instead of waiting for whole sentence length neural data inputs), which is a critical desirable of a real time communication BCI. Table 1 shows the performance of Brain2Char on 2 example sentences as data is provided in increments of 0.2 seconds at inference time. Note that the decoded sentences are shorter in length, as would be expected for shorter time windows of neural inputs, and the errors are typically in the last word(s) that may be cutoff midword.

Table 1: Incremental decoding demonstration if only the mother could pay attention to her children i think their water bill will be high

0.2s his in 0.4s if only to i think the

- 0.6s if only the mother a i think their water

- 0.8s if only the mother could pay atendion i think their water bill
- 1.0s if only the mother could pay attention with i think their water bill will be

- 1.2s if only the mother could pay attention to her children i think their water bill will be high

Importance of Regularization: One of the salient features of Brain2Char framework is the regularization branch that implicitly enforces a meaningful and robust latent representation in the neural encoder. To quantify the effect of various regularization factors used, we trained several systems each with different regularization strategies. Firstly, to study the effect of the session embedding regularization (calibration), we trained comparable systems where only in the calibrated condition, the latent representation Fh regresses to the attached time embedding. The imposed time constraints on Fh reduce cross-session neural variability, and the results in ﬁg.3(a) conﬁrm this trend, across increasing amounts of training data. In general, the session calibration enhanced the performance by about 4% against non-calibrated approach.

The second regularization we evaluated was that of the latent speech representation in Fh. We built variants of Brain2Char systems, where Fh was unconstrained (no regularization), and added

regularization branches from Fh to either i) acoustic features (MFCC), ii) articulatory kinematic features (AKT) and ii) MFCC + AKT. We observed improvements in all these cases compared to the case where no regularization was performed. Fig.3(b) summarizes these effects in terms of WER improvement from unregularized Brain2Char system. While, all speech representations result in positive gains, articulatory representation are signiﬁcantly better regularization factors than the spectral MFCC representations. There best improvements were obtained using both representations (MFCC+AKT achieving a 15% absolute improvement in P2), as neural signals may explain some acoustic variations, complementary to the articulatory features. These results indicate that implicitly enforcing physiological aspects in latent representations heavily contribute to explaining the neural speech variance, that cannot otherwise be learnt in an unsupervised fashion, given these smaller scale datasets. The beneﬁts of the articulatory representations are also consistent with earlier studies about neural encoding in the vSMC (Chartier, et al. (2018)).

[Figure 9]

[Figure 10]

- Figure 3: Importance of Regularization factors in Brain2Char. (a) Effect of session calibration on two subjects. (b) WER gains by imposing physiological features targets (e.g., MFCC and AKT)

One confound in neural speech recognition is the possibility of decoding from the auditory regions during the participants’ self-perception of their own speech. While, Fig.3(b) conﬁrms that articulation is the primary driver of the performance, we tested this further by running inference on trials where participants only silently mimed sentences without overtly vocalizing. The decoding performance was still acceptable, a 40% WER over 20 tested mimed trials on participant P3 and for P4, 67% WER on 20 mimed trials. These results show that the decoder is not relying on auditory feedback of hearing oneself. Some selected mimed decoding results are summarized in Table.2. Note that the errors are often phonetically close confusions (decoded "helping" as “hoping"; “sink” as “sing" etc). Performance in the silent speaking condition also shows the potential Brain2Char as a silent communication BCI.

Table 2: Mimed speech decoding Ground Truth Decoded

- P3

there is chaos in the kitchen there is chaos in the catch the stool is tipping over the stool is tipping over the and his sister is helping him steal a cookie his sister is hoping steal a cookie

- P4

the little girl is giggling little girl is giggling water is overﬂowing from the sink water is overﬂowing from the sing the woman is holding a broom the woman the room

### 3 Conclusion

We propose Brain2Char, a neural network architecture that converts Brain recordings to text. Brain2Char utilizes multi-scale grouped CNN ﬁlters to extract neural signals from ECoG data, employs physiological and artifactual regularization schemes on latent representations, and decodes character sequences optimizing a CTC loss. The jointly optimized Brain2Char model makes optimial utilization of available data and sets a new state-of-the-art performance on decoding text from ECoG recordings. This holds both in terms of vocabulary sizes and performance metrics compared to earlier studies. Furthermore, Brain2Char is amenable to incremental, real-time decoding and performs

reasonably well on decoding silently mimed speech, only using brain data. These results demonstrate that Brain2Char is a promising candidate for a communication BCI.

### References

- [1] Mitchell, T. M., Shinkareva, S. V., Carlson, A., Chang, K. M., Malave, V. L., Mason, R. A., & Just, M. A.

(2008). Predicting human brain activity associated with the meanings of nouns. science, 320(5880): 1191-1195.

- [2] Wehbe, L., Murphy, B., Talukdar, P., Fyshe, A., Ramdas, A., & Mitchell, T. (2014). Simultaneously uncovering the patterns of brain regions involved in different story reading subprocesses. PloS one, 9(11): e112575
- [3] Huth, A. G., de Heer, W. A., Grifﬁths, T. L., Theunissen, F. E., & Gallant, J. L. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex. Nature, 532(7600): 453.
- [4] Pereira, F., Lou, B., Pritchett, B., Ritter, S., Gershman, S. J., Kanwisher, N., Botvinick, M. & Fedorenko, E.

(2018). Toward a universal decoder of linguistic meaning from brain activation. Nature communications, 9(1): 963.

- [5] Sejnowski, T. J., Churchland, P. S., & Movshon, J. A. (2014). Putting big data to good use in neuroscience. Nature neuroscience, 17(11): 1440.
- [6] Chang, E. F., Rieger, J. W., Johnson, K., Berger, M. S., Barbaro, N. M., & Knight, R. T. (2010). Categorical speech representation in human superior temporal gyrus. Nature neuroscience, 13(11): 1428.
- [7] Chang, E.F. (2015). Towards large-Scale, human-Based, mesoscopic neurotechnologies. Neuron, 86: 68-78.
- [8] Pasley, B. N., David, S. V., Mesgarani, N., Flinker, A., Shamma, S. A., Crone, N. E., Knight, R. T., & Chang, E. F. (2012). Reconstructing speech from human auditory cortex. PLoS biology, 10(1): e1001251.
- [9] Akbari, H., Khalighinejad, B., Herrero, J. L., Mehta, A. D., & Mesgarani, N. (2019). Towards reconstructing intelligible speech from the human auditory cortex. Scientiﬁc reports, 9(1): 874.
- [10] Martin, S., Brunner, P., Iturrate, I., Millán, J. D. R., Schalk, G., Knight, R. T., & Pasley, B. N. (2016). Word pair classiﬁcation during imagined speech using direct brain recordings. Scientiﬁc reports, 6: 25803.
- [11] Moses, D. A., Mesgarani, N., Leonard, M. K., & Chang, E. F. (2016). Neural speech recognition: continuous phoneme decoding using spatiotemporal representations of human cortical activity. Journal of neural engineering, 13(5): 056004.
- [12] Mugler, E. M., Patton, J. L., Flint, R. D., Wright, Z. A., Schuele, S. U., Rosenow, J., Shih, J. J., Krusienski, D. J., & Slutzky, M. W. (2014). Direct classiﬁcation of all American English phonemes using signals from functional speech motor cortex. Journal of neural engineering, 11(3): 035015.
- [13] Herff, C., Heger, D., De Pesters, A., Telaar, D., Brunner, P., Schalk, G., & Schultz, T. (2015). Brain-to-text: decoding spoken phrases from phone representations in the brain. Frontiers in neuroscience, 9: 217.
- [14] Angrick, M., Herff, C. Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J. & Schultz, T. (2019). Speech synthesis from ECoG using densely connected 3D convolutional neural networks. Journal of neural engineering, 16, 036019.
- [15] Anumanchipalli, G. K., Chartier, J., & Chang, E. F. (2019). Speech synthesis from neural decoding of spoken sentences. Nature, 568: 493-498.
- [16] Hannun, A., Case, C., Casper, J., Catanzaro, B., Diamos, G., Elsen, E., Prenger, R., Satheesh, S., Sengupta, S., Coates, A., & Ng, A. Y. (2014). Deep speech: Scaling up end-to-end speech recognition. arXiv preprint arXiv:1412.5567.
- [17] Collobert, R., Puhrsch, C., & Synnaeve, G. (2016). Wav2letter: an end-to-end convnet-based speech recognition system. arXiv preprint arXiv:1609.03193.
- [18] Edwards, E., Soltani, M., Deouell, L. Y., Berger, M. S., & Knight, R. T. (2005). High gamma activity in response to deviant auditory stimuli recorded directly from human cortex. Journal of neurophysiology, 94(6): 4269-4280.
- [19] Crone, N. E., Korzeniewska, A., & Franaszczuk, P. J. (2011). Cortical gamma responses: searching high and low. International Journal of Psychophysiology, 79(1): 9-15.
- [20] Flinker, A., Korzeniewska, A., Shestyuk, A. Y., Franaszczuk, P. J., Dronkers, N. F., Knight, R. T., & Crone, N. E. (2015). Redeﬁning the role of Broca’s area in speech. Proceedings of the National Academy of Sciences, 112(9): 2871-2875.

- [21] Chartier, J., Anumanchipalli, G. K., Johnson, K., & Chang, E. F. (2018). Encoding of articulatory kinematic trajectories in human speech sensorimotor cortex. Neuron, 98(5): 1042-1054.
- [22] Mesgarani, N., Cheung, C., Johnson, K., & Chang, E. F. (2014). Phonetic feature encoding in human superior temporal gyrus. Science, 343(6174): 1006-1010.
- [23] Churchland, M. M., Byron, M. Y., Cunningham, J. P., Sugrue, L. P., Cohen, M. R., Corrado, G. S., Newsome, W. T., Clark, A. M., Hosseini, P., Scott, B. B., Bradley, D. C., Smith M. A., Kohn, A., Movshon, J. A., Armstrong, K. M., Moore, T., Chang, S. W., Snyder, L. H., Lisberger, S. G., Priebe, N. J., Finn, I. M., Ferster, D., Ryu, S. I., Sahani, M., & Shenoy, K. V. (2010). Stimulus onset quenches neural variability: a widespread cortical phenomenon. Nature neuroscience, 13(3): 369.
- [24] Sun, P., Moses, D. A., & Chang, E. F. (2019). Modeling neural dynamics during speech production using a state space variational autoencoder. arXiv:1901.04024.
- [25] Szegedy, C., Ioffe, S., Vanhoucke, V., & Alemi, A. A. (2017). Inception-v4, inception-resnet and the impact of residual connections on learning. In Thirty-First AAAI Conference on Artiﬁcial Intelligence.
- [26] Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. In Advances in neural information processing systems, 3111-3119.
- [27] Heaﬁeld, K., Pouzyrevsky, I., Clark, J. H., & Koehn, P. (2013). Scalable modiﬁed Kneser-Ney language model estimation. In Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics 2: 690-696.

