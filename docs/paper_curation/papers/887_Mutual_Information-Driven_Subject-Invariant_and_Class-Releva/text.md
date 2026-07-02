## Mutual Information-driven Subject-invariant and Class-relevant Deep Representation Learning in BCI

Eunjin Jeon, Wonjun Ko, Jee Seok Yoon, and Heung-Il Suk, Member, IEEE

### arXiv:1910.07747v4[cs.LG]21Aug2020

Abstract—In recent years, deep learning-based feature representation methods have shown a promising impact in electroencephalography (EEG)-based brain-computer interface (BCI). Nonetheless, owing to high intra- and inter-subject variabilities, many studies on decoding EEG were designed in a subject-speciﬁc manner by using calibration samples, with no concern of its practical use, hampered by time-consuming steps and a large data requirement. To this end, recent studies adopted a transfer learning strategy, especially domain adaptation techniques. Among those, to our knowledge, an adversarial learning has shown its potential in BCIs. In the meantime, it is known that adversarial learning-based domain adaptation methods are prone to negative transfer that disrupts learning generalized feature representations, applicable to diverse domains, e.g., subjects or sessions in BCIs. In this paper, we propose a novel framework that learns class-relevant and subject-invariant feature representations in an information-theoretic manner, without using adversarial learning. To be speciﬁc, we devise two operational components in a deep network that explicitly estimate mutual information between feature representations; (1) to decompose features in an intermediate layer into class-relevant and class-irrelevant ones, (2) to enrich class-discriminative feature representation. On two large EEG datasets, we validated the effectiveness of our proposed framework by comparing with several comparative methods in performance. Further, we conducted rigorous analyses by performing an ablation study in regard to the components in our network, explaining our model’s decision on input EEG signals via layer-wise relevance propagation, and visualizing the distribution of learned features via t-SNE.

Index Terms—Brain-Computer Interface; Deep Learning; Electroencephalogram; Motor Imagery; Mutual Information; Transfer Learning; Domain Adaptation; Subject-Independent

I. INTRODUCTION

# B

RAIN–computer interface (BCI) allows users to directly communicate or control external devices based on

thoughts, typically measured through electroencephalography (EEG) [1]. EEG signals that measure the electrical activity of the brain are usually categorized into two types, namely, evoked and spontaneous, depending on their inducing manner in non-invasive BCIs. Evoked EEGs, e.g., steady-state visually

This work was supported by Institute for Information & Communications Technology Promotion (IITP) grant funded by the Korea government (No. 2017-0-00451, Development of BCI based Brain and Cognitive Computing Technology for Recognizing User’s Intentions using Deep Learning). Additional support was provided by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) (No. 2019-0-00079, Department of Artiﬁcial Intelligence (Korea University)). (Corresponding author: Heung-Il Suk)

E. Jeon, W. Ko, and J.S. Yoon are with the Department of Brain and Cognitive Engineering, Korea University, Seoul 02841, Korea (e-mail: eunjinjeon@korea.ac.kr; wjko@korea.ac.kr; wltjr1007@korea.ac.kr). H.-I. Suk is with the Department of Artiﬁcial Intelligence and the Department of Brain and Cognitive Engineering, Korea University, Seoul 02841 Korea (e-mail: hisuk@korea.ac.kr).

[Figure 1]

Fig. 1. (Left) Power spectral density (PSD) curve of subject 45; (Right) PSD curve of subject 14 in GIST-motor imagery dataset [10]. By taking the average of the trials, we denote the solid line and the area of shaded region as the mean and standard deviation of PSD. Both subjects show different patterns in PSD, which can be regarded as a domain shift.

evoked potentials, steady-state somatosensory evoked potentials, and event-related potentials, are derived from immediate automatic responses to an external stimulus regardless of a user’s will. In contrast, spontaneous EEGs induce activation of event-related (de)synchronization (ERD/ERS) when carrying out mental tasks at a user’s will. Of the various types of EEG signals, we focused on motor imagery signals showing ERD/ERS induced by simply imagining body movements.

By taking advantage of the controlling system without explicit commands, many studies have focused on decoding motor imagery through machine learning. One of the most popular methods is common spatial pattern (CSP) [2]. CSP and its variants [3], [4] were employed to design discriminative spatial ﬁlters by maximizing differences in their variances between different motor imagery classes to extract features. After conducting CSP or its variants, the extracted features were applied to a linear classiﬁer, e.g., linear discriminative analysis (LDA) [5]. Recently, deep learning-based methods have drawn increasing attention in BCI researchers by virtue of the possibility to learn features from data automatically [6], [7]. Especially, convolutional neural networks (CNNs) have been well utilized to decode temporal and spatial information of EEG signals and showed remarkable performances [7]–[9].

However, the motor imagery EEG shows high variability among subjects (inter-subject) and sessions for the same subject (intra-subject) [11] on account of inherent background neural activities, fatigue, concentration levels, etc. Fig. 1 presents the power spectral density (PSD) curves of motor imagery EEG signals obtained from two subjects. Both curves are plotted using all motor imagery EEG samples over the sensorimotor area. In Fig. 1, the right panel presents a clear peak in the mu-band with relatively small variations (blue shading) among samples, whereas the left panel shows large variations

without any clear pattern. Because of those unpredictable high variations and less clearly observable patterns inherent in EEG signals, it is challenging to train a subject-invariant model, which is applicable to different datasets or subjects. In this regard, an EEG decoding model trained on one subject causes performance degradation when applied to other subjects [12]– [14]. Therefore, training a model for each subject is a typical approach to decode brain signals despite time-consuming and amount of data-requirable process [15]. In order to address the limitation, previous studies exploited multiple subjects and/or sessions data simultaneously to train their respective models through transfer learning [11], [15].

We focus on, in this work, boosting model generalization among subjects in the transfer learning manner [11], [16], by considering a subject as a domain [12]. Owing to the unfavorable property of motor imagery EEG, i.e., high interand intra-subject variabilities [11], a large distributional discrepancy was observed on a feature space among different subjects or sessions, referred to as a domain shift [13], [14]. Hence, mitigating the domain shift is one of the important objectives in the transfer learning for BCI tasks [14], [16], [17].

Regarding the domain shift problem, numerous studies on machine learning, referring to domain adaptation, have been conducted [18]–[20]. Particularly, most methods tried to tackle the problem by introducing a domain discriminator in their framework to discover features indistinguishable among domains via adversarial training like a generative adversarial network [18]. In the same line of work, [16], [17] proposed a domain adversarial network to learn a subject-invariant representation for motor imagery classiﬁcation in BCIs, which is applicable for more than two subjects by devising a subject or domain discriminator.

However, recent studies have pointed two major limitations of those approaches: First, an adversarial learning, which induces to alleviate a domain shift, is likely to disrupt feature representation learning, due to restraint of domain-speciﬁc variations, while not considering class-related distribution across domains [21]. Second, most domain adaptation methods may not only improve the feature representation of a target domain, but also corrupt it. This corrupting phenomenon is called negative transfer [22]. In this regard, Peng et al. [22] proposed a framework, where the source domain was sorted as domain-invariant, domain-speciﬁc, and class-irrelevant to alleviate the effect of negative transfer. To this end, it is of great importance to differentiate positive and negative transferable factors from data of various domains.

In this work, we propose a novel framework to learn subjectinvariant feature representations for motor imagery EEG signals classiﬁcation in an information-theoretic manner, instead of using the adversarial learning strategy, towards subjecttransferable learning and ultimately subject-independent BCIs. Concisely, we introduce a specially designed network component that decomposes feature maps of an intermediate layer in a feature extractor into class-irrelevant and class-relevant ones via mutual information estimation. Further, owing to the possibility of having subject-related information remained in the class-relevant features that could be negative transfer, even

after the decomposition, we further devise a regularization mechanism that imposes the extracted class-relevant (regarded as ‘local’) features and the next-level of abstract (regarded as ‘global’) features to have maximal mutual information. The rationale of imposing this regularization of maximal mutual information between local and global features is as follows. As the global feature representation layer is closer to a classiﬁer, it is more likely to receive class-discriminative information in backpropagation from the classiﬁcation loss. By imposing such information to be reﬂected in the local features by means of mutual-information maximization, it is expected to discard the remaining subject-related information in the local features, but to keep the class-relevant features only. Thus, it is expected to lessen the effect of negative transfer and to enhance the discriminative power of learned feature representations. In other words, to jointly consider domain shifts between multiple domains (i.e., subjects) and to estimate mutual information from them, we devise a novel network architecture to estimate mutual information in high- and low-level representations in a subject-independent manner. As a result, our trained model can be subject-invariant and suitable for applying to new subjects in a way of zero training, i.e., no subject-dependent adaptation or calibration is required.

Compared to the existing domain-adaptation work in BCIs [16], [17], our method is less concerned on the negative transfer thanks to the mutual information-driven learning. In addition, unlike those existing works that use a domain discriminator that identiﬁes a subject’s id with regard to an input EEG signals, our framework does not use a subject’s id during training. In the circumstance of incrementally adding samples of new training subjects, their architectures need to accommodate the increasing number of domains, i.e., training subjects, and modify their classiﬁer accordingly. However, since our proposed method does not use the information of subjects’ id, there is no need to revise or modify our network, thus being scalable to domains or training subjects.

We evaluated our proposed framework on GIST [10] and KU [23] motor imagery datasets. Our experimental results demonstrated that (i) the feature decomposition into classrelevant and class-irrelevant helped enhance the performance by diminishing distributional difference in features among subjects and (ii) maximizing mutual information between high- and low-level representations encouraged to enrich classdiscriminative features and to boost the performance. Our results showed promising performance compared to the competing methods trained with data from multiple subjects. The main contributions of our work are three-fold:

- • First, we propose a novel deep-learning framework that learns subject-invariant and class-relevant feature representations in an information-theoretic and end-to-end manner.
- • Our proposed components of feature decomposition and feature enrichment can be naturally plugged into the existing network architectures, e.g., EEGNet [6] and Deep ConvNet [9].
- • On two large motor imagery EEG datasets, our method achieved the best performance in both cross-subject learning and zero-training scenarios.

II. RELATED WORK

- A. Transfer Learning in BCI

In general, many methods for decoding EEGs are devised for individual use with independent training per subject; this is because of high inter- and intra-subject variabilities. However, the calibration and training of the decoding model requires plenty of data and is time-consuming [11], [15]. To cope with the aforementioned limitation, various studies have focused on training the decoding model with multiple subjects and/or sessions with the objective of learning a subject-invariant representation. These approaches are divided into two: (i) zeroor few-shot learning for decoding training data of unseen subject [17], [24], [25] and (ii) performance improvement by incorporating data of other subjects [14], [15], [26]. In particular, deep learning-based methods [13], [14], [16], [17] utilize a domain adaptation approach to deal with these issues. They all constrain the distributional discrepancy between subjects by minimizing the maximum mean discrepancy in the latent space [13] or making the encoder to confuse the domain [14], [16], [17]. Among those studies, two proposed methods were fundamentally devised for only two subjects [13], [14] and did not utilize diverse subjects. In [17], a classiﬁer was trained from the pre-trained subject-invariant representation, and hence, confusing the domain and identifying the class were not trained in an end-to-end manner. Although [16] proposed a method to extract a subject-invariant and classdiscriminative features among multiple subjects in an end-toend manner, there still remain some challenges. Since [16] trains a domain discriminator by explicitly using subjects’ id (or domain labels), when samples of new training subjects are added incrementally, it is required to modify the classiﬁer architecture, thus to increase tunable parameters. However, our proposed network achieves domain adaptation among multiple subjects and classiﬁcation in an end-to-end manner by estimating mutual information, without explicitly using subjects’ id. In this regard, our proposed network is scalable to domains. Further, as no adversarial learning mechanism is involved, it does not have a risk of experiencing negative transfer to deteriorate the performance, caused by the adversarial learning. [21].

- B. Transfer Learning in Machine Learning

Various studies have been done to mitigate differences between source and target domains in domain adaptation, i.e., a case of transfer learning. In [19], the domain adaptation was categorized into one- and multi-step approaches depending on the presence of an intermediate domain, decreases the gap between source and target domains. The one-step domain adaptation was achieved by means of a domain discriminator, which guides its features to become indistinguishable between domains by reversing its gradient during training through the adversarial learning [18], [20]. However, Liu et al. [21] showed that adversarial feature learning can potentially damage their original feature representation from a viewpoint of transfer learning. In this paper, we take a different strategy and propose a novel framework to learn domain adaptation by means of mutual information estimation to lessen the distributional

discrepancy among domains. For this, we assume that a latent space maximized via the mutual information between multiple domains can be viewed as a commonly shared space among those domains. In addition, recently, studies have focused on disentangled representation learning in terms of transfer learning to prevent negative transfer [22], [27]. Peng et al. [22] divided a latent representation into domain-invariant, domainspeciﬁc, and class-irrelevant features by minimizing mutual information among them for domain-agnostic learning. Similar to those approaches, we decompose our feature representations into class-relevant and class-irrelevant features and then boost the class-relevant feature to contain more domain-invariant (i.e., subject-invariant) information. In particular, we utilize mutual information between two feature representations to ensure decomposition.

III. METHODS

In this work, we regard each subject as one domain. Thus, we assume that for S subjects, Ds = {(x(si),ys(i))}n

i=1 with ns labeled samples, where s ∈ {1...,S}. Let x(si) ∈ Rn

s

c×nt denote a raw EEG trial including spatio-temporal information, where nc and nt are the number of electrode channels and timepoints, respectively. We also deﬁne ys(i) ∈ {0,1}2 as the corresponding class label, i.e., left- and right-hand. Hereafter, for uncluttered, we omit the superscripts (s and i) without loss of generality.

The goal of this work is to build a deep neural network robustly applicable for multiple subjects. In other words, we develop an intention identiﬁcation system that can be generally applicable for all subjects. Further, our trained model can be applied to a new subject’s data without any further calibration and/or training steps, thus towards zero-training.

An overall framework of our proposed method is shown in Fig. 2. Our network ﬁrst discovers a feature representation including spatio-temporal information through existing CNNbased networks. However, to ﬁlter out class-irrelevant representation, we utilize an intermediate feature representation, i.e., an output of a local encoder El (local feature fl). After the local feature fl is decomposed into class-relevant feature fre and class-irrelevant feature fir, only class-relevant feature fre passes through the following layers of a global encoder fg) and a classiﬁer C to identify the corresponding class of an input x. To help our network diminish dependency between two characteristics in features, i.e., class-relevant feature and classirrelevant feature, we leverage a neural mutual information estimator M (green box in Fig. 2). In the meantime, another two mutual information estimators (Tl and Tg) are utilized to learn more subject-invariant and class-discriminative feature representation by maximizing mutual information between the class-relevant feature and the global feature among multiple subjects (blue box in Fig. 2).

A. Class-relevant Feature Decomposition

As aforementioned, all feature representations are not necessarily useful for classiﬁcation in terms of transfer learning [22]. Hence, we assume that a feature representation can be decomposed into class-relevant and class-irrelevant factors

| |
|---|
| |
| |

| |
|---|

Channel

Time

Subject 1 Subject 2 Subject S

Class-relevant Feature Decomposition

| |
|---|

| || |
|---|
<br><br>| |
|---|
<br><br>|
|---|---|
| | |

Enriched Feature Representation Learning

- Fig. 2. Overview of the proposed network. We randomly select trials regardless of the subjects for a mini-batch. After mapping an input x to a local feature fl by a local encoder El, a point-wise convolutional layer V embeds it into a class-relevant feature fre and a class-irrelevant feature fir with the help of mutual information estimator M. Subsequently, a global encoder Eg operates on top of the class-relevant feature, and then extracts global feature fg. A classiﬁer C takes the global feature fg to identify the class label of an input EEG. Furthermore, to enhance the representational power of the global feature, we maximize mutual information between two features of fre and fg by using two networks, i.e., Tl and Tg.

and then introduce a method to separate a class-relevant feature out by minimizing mutual information between two factors.

First, our encoder E is comprised of the local encoder and the global encoder. The local encoder, El, maps input x onto the local feature fl = El(x) ∈ Rh

1×w1×d1, where h1, w1, and d1 represent the height, width, and depth of the feature, respectively. The global encoder Eg computes the global feature fg that is fed into a classiﬁer C. In other words, if the local encoder embeds the local feature, the remaining layers are regarded as the global encoder. The encoder E is structured such that it produces an intermediate local feature and then the global feature.

Before feature decomposition in the local feature fl, we apply a point-wise convolution V to the local feature considering cross-feature map correlation [28] to alleviate unexpected information loss. Subsequently, we obtain two features; one is related to class-relevant feature fre among subjects and the other one is related to class-irrelevant feature fir that can be regarded as subject-speciﬁc factors regardless of the classiﬁcation, where fre,fir ∈ Rh

1×w1×d1. The global encoder Eg takes only the class-relevant feature as an input and then outputs a global feature fg. The classiﬁer C is trained by minimizing the softmax cross-entropy loss:

N

Lcls = −

i=1

y(i) log(C(Eg(fre(i)))) (1)

where y(i) denotes a one-hot label vector for an input x(i) and N is the number of samples in a mini-batch. The class-relevant factors are sufﬁcient for the ﬁnal classiﬁcation task after embedding to the global feature through the global encoder.

In order to better decompose local feature fl into two factors, i.e., fre and fir, we exploit mutual information between them, which is deﬁned in a form of the Kullback-Leibler (KL) divergence between the their joint distribution J and the

product of marginals of them M. Recently, mutual information neural estimation (MINE) [29] showed that mutual information is estimated based on deep learning by reformulating it as the Donsker-Varadhan representation [30]:

IΘ(X;Y ) = DKL(J||M)

EJ[Tθ(x,y)] − log(EM[eT

θ(x,y)]) (2)

= sup

θ∈Θ

where T is a neural network parameterized by θ. Here, the product of marginal distributions M is induced by shufﬂing the samples from the joint distribution along the batch axis. MINE [29] achieves the estimation of mutual information between continuous random variables by maximizing Eq. (2).

However, as we only focus on maximizing the mutual information, the exact value of mutual information in terms of training the neural network is not required. In this regard, Deep infomax (DIM) [31] takes advantage of the Jenshen-Shannon (JS) divergence as an alternative of Eq. (2) by following [32]. Thus, Eq. (2) can be rewritten as follows:

#### IΘ(X;Y ) = EJ[−sp(−Tθ(x,y))] − EM[sp(Tθ(x,y))] (3) where sp(z) = log(1 + ez) is a softplus function.

From the viewpoint of the feature decomposition, we make use of mutual information between fir and fre. In other words, by introducing a network M to estimate mutual information between fir and fre and penalizing a large mutual information value of M, we make the two factors of fir and fre to be decomposed with minimal information overlap. Hence, the neural estimator M is trained with the the local encoder El and the point-wise convolutional layer V based on the output of a neural estimator M, i.e., Id(fre(i);fir(i)), which deﬁnes the decomposition loss Ldec:

N

Id(fre(i);fir(i)). (4)

Ldec = min El,V

max

M

i=1

In [29], the parameters of MINE [29] are trained by gradient ascent owing to the use of the Donsker-Varadhan representation [30]. However, in our case, as we want to minimize the mutual information between fre and fir, we apply a gradient reversal layer (GRL) [18]. The GRL passes features innate to M in forward propagation, but reverses the gradients in backpropagation, i.e., reversed gradients, during training.

B. Enriched Feature Representation Learning

Meanwhile, in order to generalize our proposed method in the subject-independent manner, it is of great importance to learn a subject-invariant and class-discriminative feature. However, although we separate the class-relevant feature and the class-irrelevant feature by the means of MINE M [29], the class-relevant feature can potentially lose much of the classrelated information or still contain subject-speciﬁc information.

In this regard, we further introduce another mutualinformation-oriented mechanism that helps enrich the discriminative power of the feature representation fg, which is fed into a classiﬁer. Speciﬁcally, based on deep infomax (DIM) [31], we devise two sub-networks, denoted as Tl and Tg in Fig. 2, to maximize the mutual information between two features of the class-relevant feature fre and the global feature fg. While the two networks Tl and Tg take the same inputs of fre and fg, they consider different levels of information in mutual information estimation. The network Tl estimates the mutual information in a ﬁne-grained local level for each one of the patches1 in the feature fre with respect to the global feature fg as follows:

h1×w1

N

1 h1 × w1

Il(fg(i);fre(i,j)) (5)

max

El,Eg,V,Tl

i=1

j=1

where fre(i,j) denotes a j-th local patch of the class-relevant feature fre(i). In the meantime, the network Tg estimates in a coarse global level by jointly considering all patches in the feature fre as follows:

max

El,Eg,V,Tg

N

Ig(fg(i);fre(i)) (6)

i=1

After calculating the mutual information between the global feature fg(i) and each of the local patches fre(i,j) in the classrelevant feature fre in Eq. (5), their averaged values is used to update the parameters of the local encoder El, the global encoder Eg, the point-wise convolutional layer V , and the Tl. As a result, the global feature fg includes more information with regards to the local regions of the input; thus, it enriches the representation in terms of data quality [31]. Note that we randomly select trials from a number of subjects and use them for a mini-batch during training. Thus, the networks of Tl and Tg share the same information from multiple subjects within a mini-batch. As a result, owing to the maximization of the mutual information between the class-relevant feature and the global feature among multiple subjects in two different ways, the calculated global feature fg(i) becomes more

1Here, one patch denotes a depth-wise vector in a tensor.

subject-invariant and contain enriched feature representation for classiﬁcation.

C. Objective Function

All three objectives can be jointly used to train all components in an end-to-end manner. Our overall objective function J is deﬁned as follows:

#### J = αLcls + βLdec + γLDIM (7)

where LDIM is a sum of Eq. (5) and Eq. (6). α, β, and γ are hyper-parameters to control the balance among three loss terms.

IV. EXPERIMENTS & RESULTS

We expect that our proposed network can be generalized for multiple subjects by learning subject-invariant and classrelevant representations. In this regard, we validated our methods by considering the following two scenarios (or applications): (i) a possibility of learning generalizable representation across sessions or subjects and (ii) a feasibility of zero-training approach of an unseen subject. We evaluated the proposed method over two public large datasets: e.g., GIST [10] and KU [23] motor imagery datasets. The codes are available at https://github.com/eunjin93/SICR BCI.

A. Data & Preprocessing

- 1) GIST dataset [10]: This2 is a big dataset of 52 subjects

and comprises EEG signals related to two different motor imagery tasks of the left- and right-hands. All EEG signals were recorded from 64 Ag/AgCl electrodes according to the 10-20 system and sampled at 512 Hz. Each class of a subject comprises 100 or 120 trials acquired from four sessions. All subjects were asked to take a rest for 2 s and then imagine the hand movement for 3 s by following the instruction given on the monitor. Since two subjects (subjects 29 and 34) had a high correlation with electromyography (EMG), they were termed as bad subjects and their data was not considered in the analysis [10]. Thus, we conducted experiments using the data of the remaining 50 subjects.

- 2) KU dataset [23]: This3 dataset contains EEG signals of

54 subjects for two motor imagery tasks, i.e., of the left- and right-hands, recorded from 62 Ag/AgCl electrodes according to the 10-20 system and sampled at 1k Hz. All EEG signals are acquired from two sessions. Unlike the GIST-motor imagery dataset [10], the KU dataset is divided into training and test phases for each session. In each session, each subject undergoes 100 trials per class regardless of the phase. All subjects took a rest of 3 s, and then performed the imagery task of hand movement for 4 s by following the given instruction in the monitor. For the low computational cost, we downsampled EEG signals to 500 Hz.

- 2Available at http://gigadb.org/dataset/100295
- 3Available at http://gigadb.org/dataset/10054

3) Preprocessing: For both datasets, the signals were preprocessed using a large Laplacian ﬁlter to reduce noise and a bandpass ﬁlter in the range of 4−40 Hz related to sensorimotor rhythms. After segmenting the signals to a baseline and task, we discarded the ﬁrst and last 0.5 seconds of the segmented task signal. Next, we subtracted the mean of the baseline to each task signal for baseline correction.

- B. Experimental Settings

Although each subject in both GIST [10] and KU [23] datasets performed motor imagery tasks over different sessions, we simply combined samples across sessions into one. To verify the generalization of the network, we conducted experiments considering the following two scenarios:

- • Scenario I (cross-subject learning): In this scenario, we considered the use of all available samples from other subjects as well as a target subject. The underlying assumption behind this scenario is that it could be possible to learn better feature representations based on diverse EEG signals. In order for performance evaluation, we divided the samples of each subject into 5 folds by assigning an equal number of samples to each fold, and used samples of 4 folds for training and samples of one remaining fold for test. The training samples of 4 folds were further randomly partitioned into a pure training set and an independent validation set at a ratio of 7 : 1. We trained and selected models with combined training and validation samples of all subjects, respectively, and then tested on the testing samples of each subject. That is, a single subject-independent model was built and tested on all subjects. The processes were repeated 5 times and their average performance was reported for evaluation.
- • Scenario II (zero-training): This is designed for a zerotraining application, i.e., no sample of a target subject is used to tune model parameters. That is, we ﬁrst trained a model based on solely samples of non-target subjects, and then tested the trained model on the samples of a new (unseen) target subject. For this, we have exploited a leave-one-subject-out validation scheme.

- C. Model Implementation

1) Architecture: To demonstrate that our method can be independent of the architecture of the feature extractor, we utilized two deep learning-based motor imagery decoding models as our encoder.

- • Deep ConvNet [9]: This is composed of four convolutionpool blocks capturing spatio-temporal information of raw EEG signals and a fully-connected layer. In the ﬁrst block, an input EEG is convolved with kernels of [1×10]

temporally and then convolved with kernels of [nc×1] to integrate spatial information. The remaining three blocks consist of temporal convolution with [1×10] kernels and max-pooling as [1×3], respectively. For fair comparison, we did not use the “cropped-training” strategy which was considered in the original work [9].

• EEGNet [6]: This exploits depthwise and separable convolutions [28] to encode EEG signals for reduction of the number of parameters. In detail, EEGNet [6] consists of three convolutional layers: (i) the ﬁrst convolutional layer has ﬁlters of [1 × fs/2], where fs denotes the sampling rate of the data and then encodes the temporal information of the inputs, (ii) the second convolutional layer convolves kernels of [nc×1] to the output of the ﬁrst layer in a depth-wise manner [28], and (iii) the separable convolution [28] is utilized as the last layer to summarize the temporal information of each feature map.

Since both Deep ConvNet [9] and EEGNet [6] include several convolutional layers, we set the last layer as our global encoder and the previous layers as our local encoder. Note that we modiﬁed the spatial ﬁlter size as the number of electrode channels in each dataset. After obtaining the local feature, we conducted a point-wise convolution to expand the depth dimension double. We split the embedded local feature along the depth-axis to divide it into the class-relevant feature and the class-irrelevant feature.

In the Tg, after embedding the class-relevant feature through another convolutional layer which has same architecture with the global encoder, the feature was concatenated with the global feature along the depth-axis. Then, the concatenated feature was taken as the input of a fully-connected layer that outputs 1 unit. We used the concat-and-convolve architecture for the Tl in accordance with [31]. In the Tl, the global feature was replicated to be the same dimension with the class-relevant feature and then concatenated with the class-relevant feature at every location. Subsequently, the concatenated feature were passed to the pointwise convolutional layer and then became same height and width of the class-relevant feature. After attaining scores corresponding the joint distribution and the product of marginals between the class-relevant feature and the global feature, we calculated their average to use in Eq. (5). The classiﬁer C was composed of a fully-connected layer with the number of classes units. More details can be found in Supplementary A.

2) Training Settings: Exponential linear units (ELU) were used as a nonlinear function in our network. In addition to the two networks, i.e., Tg and Tl, we applied a batch normalization [33]. Furthermore, we applied an l2-regularization with a coefﬁcient of 0.1 and a dropout [34] with a rate of 0.5 to prevent over-ﬁtting. We trained models by using a RAdam [35] with a learning rate of 10−3 by exponentially decreasing 0.99 per epoch, where the dimension of a mini-batch size was 40. Regarding the hyper-parameters α, β and γ in Eq. (7), we chose {α,β,γ} as {0.5,0.3,0.5} for all cases.

D. Competing Methods

For evaluation, we compared our proposed method with the following various methods using the same architecture of the feature extractor:

• Pooled learning: In order to see the effectiveness of a transfer learning approach, we ﬁrst considered the most straightforward way of using all available samples from many subjects by pooling them into a single large dataset,

as a baseline. In this case, we did not explicitly model subject-invariance or class-relevance of features, but took advantage of all available samples in feature representation and classiﬁer learning. We implemented conventional machine learning-based models (e.g., CSP [2] and FBCSP [3]) as well as deep learning-based models.

- • Subject-to-Subject transfer learning: Various forms of regularized CSPs (RCSPs) [36], which exploit covariance matrices derived from other subjects’ EEG signals for better generalization in a way of regularization, have been studied and presented reasonable performance in subjectto-subject transfer [36], [37]. Among those, we implemented Lotte et al.’s Weighted Tikhonov Regularization method (WTRCSP) because of its superiority to its counterpart methods in performance [36]. Subsequently, we used LDA based classiﬁer by taking the WTRCSP features as input.
- • Domain adversarial neural network for motor imagery signals (DANN-MI) [16]: Inspired by DANN [18], Ozdenizci¨ et al. [16] introduced a deep EEG feature representation learning robust across intra- and intersubject variability via adversarial inference. DANN-MI composed of three modules, i.e., a feature extractor, a classiﬁer, and an adversary, and trained by two loss terms, i.e., a classiﬁcation loss and a subject discrimination loss. Speciﬁcally, based on the adversarial learning between the adversary and the feature extractor, their feature extractor learned class-discriminative and subject-invariant feature representation. [16] also set the hyper-parameter to tune the importance between two losses. We chose λ as 0.03 for EEGNet [6] and 0.05 for Deep ConvNet [9] according to the original work [16].
- • Deep adversarial disentangled autoencoder (DADA) [22]: Because of the philosophical similarity to our method, we also compared with DADA, which was also inspired by DANN [18] and devised to tackle a domain adaptation issue in computer vision. DADA disentangles the domaininvariant features from both domain-speciﬁc and classirrelevant features simultaneously to prevent negative transfer [22].

E. Ablation study

In addition, to validate the effectiveness of each component in our model, we performed three different ablations under Scenario I. First, we trained our proposed method by considering only the class decomposition step, referred as Model I. In other words, Model I was trained by using the composite of a classiﬁcation loss in Eq. (1) and a decomposition loss in Eq. (4). We developed Model II composed of encoders (El,Eg and V ), Tg, and C and trained it by jointly minimizing the classiﬁcation loss in Eq. (1), the decomposition loss in Eq. (4) and the global MINE loss in Eq. (6). Regarding Model III, we removed the Tg in our complete network, denoted as as Model IV. Concisely, Model III was trained without the global MINE loss in Eq. (7).

TABLE I

- AVERAGED PERFORMANCE [%] UNDER SCENARIO I. (∗: p < 0.05, †: NO STATISTICAL DIFFERENCE)

(a) Comparison with linear methods in pooled or transfer learning and deep-learning methods in pooled learning.

GIST dataset [10] KU dataset [23] CSP [2] (Pooled learning) 41.53 ± 8.40∗ 56.83 ± 7.72∗

FBCSP [3] (Pooled learning) 46.24 ± 6.84∗ 44.67 ± 7.10∗ WTRCSP [36] (Transfer learning) 55.84 ± 10.25∗ 55.10 ± 8.98∗ Deep ConvNet [9] (Pooled learning) 54.77 ± 8.54∗ 58.45 ± 11.64∗ EEGNet [6] (Pooled learning) 55.38 ± 9.55∗ 64.67 ± 13.24∗ Ours (with Deep ConvNet [9]) 74.15 ± 12.64 76.67 ± 13.01

Ours (with EEGNet [6]) 76.60 ± 12.48 74.48 ± 13.84

(b) Comparison with methods of deep learning-based transfer learning on GIST dataset [10].

Deep ConvNet [9] EEGNet [6]

- DANN-MI [16] 73.17 ± 12.81† 74.92 ± 12.44∗ DADA [4] 50.26 ± 2.76∗ 72.12 ± 13.31∗

Ours 74.15 ± 12.64 76.60 ± 12.48 (c) Comparison with methods of deep learning-based transfer learning on KU dataset [23].

Deep ConvNet [9] EEGNet [6]

- DANN-MI [16] 74.96 ± 13.15∗ 72.43 ± 13.90∗ DADA [22] 50.93 ± 2.66∗ 68.43 ± 13.75∗

Ours 76.67 ± 13.01 74.48 ± 13.84

TABLE II

- AVERAGED PERFORMANCE [%] UNDER SCENARIO II. (∗: p < 0.05, †: NO STATISTICAL DIFFERENCE)

(a) GIST dataset [10] Deep ConvNet [9] EEGNet [6] DANN-MI [16] 69.64 ± 12.93† 72.56 ± 13.61†

Ours 70.54 ± 12.84 73.73 ± 13.75 (b) KU dataset [23] Deep ConvNet [9] EEGNet [6]

DANN-MI [16] 69.41 ± 13.17∗ 72.08 ± 14.29∗ Ours 73.32 ± 13.55 72.22 ± 13.51

F. Results

- 1) Scenario I: We trained the comparative methods with

all the subjects of each dataset in a subject-independent way, and tested them with the test samples of each subject. The averaged performance for all the subjects in two datasets is summarized in TABLE I. Our model showed the accuracy of 74.15% (with Deep ConvNet [9]) and 76.60% (with EEGNet [6]) on the GIST dataset [10] and achieved the averaged accuracy of 76.67% (with Deep ConvNet [9]) and 74.48% (with EEGNet [6]) on the KU dataset [23]. Notably, our method outperformed all the competing methods of the pooled learning, DANN-MI [16], and DADA [22] with high statistical signiﬁcance (p-value<0.05), except the case of DANN-MI with Deep ConvNet on the GIST dataset [10].

- 2) Scenario II: TABLE II summarizes the results of

DANN-MI [16] and our method in Scenario II. Again, our proposed method showed its superiority to DANN-MI [16] in all cases by moderate margin, depicting its generalization

Subject 23

Scenario I

Scenario II

Subject 43

Scenario I

Scenario II

Ours DANN-MI

Ours DANN-MI

Ours DANN-MI

Ours DANN-MI

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

R

R

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

L

L

[Figure 22]

(a) Deep ConvNet [9] trained on GIST dataset [10] (b) EEGNet [6] trained on GIST dataset [10]

Subject 33 Scenario I

Scenario I

Scenario II

Subject 36

Scenario II

Ours DANN-MI

Ours DANN-MI

Ours DANN-MI

Ours DANN-MI

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

R

R

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

L

L

(c) Deep ConvNet [9] trained on KU dataset [23] (d) EEGNet [6] trained on KU dataset [23]

- Fig. 3. Illustrative comparison of PSD maps and decision-relevance heatmaps [38] of input EEG signals from randomly selected subjects. We normalized each visualized topoplot in a range between 0 and 1. (L: left-hand, R: right-hand)

TABLE III PERFORMANCE COMPARISON IN AN ABLATION STUDY OF DIFFERENT COMPONENTS IN OUR PROPOSED FRAMEWORK UNDER SCENARIO I. (∗: p < 0.05, †: NO STATISTICAL DIFFERENCE)

(a) GIST dataset [10] Deep ConvNet [9] EEGNet [6]

- Model I 73.31 ± 12.68† 74.48 ± 12.87∗
- Model II 73.68 ± 12.05† 75.94 ± 13.20†
- Model III 73.34 ± 12.44† 75.44 ± 12.93∗
- Model IV 74.15 ± 12.64 76.60 ± 12.48 (b) KU dataset [23]

Deep ConvNet [9] EEGNet [6]

- Model I 75.22 ± 13.42∗ 73.26 ± 14.12∗
- Model II 75.70 ± 13.30∗ 74.06 ± 13.49†
- Model III 75.45 ± 13.20∗ 73.41 ± 13.85∗
- Model IV 76.67 ± 13.01 74.48 ± 13.84

power to samples of new (unseen) subjects. In other words, this supports our hypothesis that the feature representation learning in our framework is effective to be applicable for new subjects in a way of zero training, i.e., no subject-dependent adaptation or calibration is required.

3) Ablation Study: Table III summarizes the performance differences according to the changes of involving different components in our proposed framework. Although the performance improvement with each individual component was

moderate, the joint work of all components showed best performance overall. It is noteworthy that the performance improvements with our proposed full network (Model IV) was statistically signiﬁcant compared to the counterpart models in several cases. Based on those results, we believe that our feature decomposition and enriched representation learning simultaneously encourage to enhance the performance. For individual performances, refer to Supplementary B.

V. ANALYSES & DISCUSSION

This section presents the analyses of our proposed network from two aspects: neurophysiological explanation and feature decomposition. First, we performed layer-wise relevance propagation (LRP) [38] to obtain an insight into the neurophysiological explanation. Next, from the viewpoint of feature decomposition, we plotted the learned feature by using t-distributed stochastic neighbor embedding (t-SNE) [39] to determine how the class-relevant and class-irrelevant features are distributed.

A. Neurophysiological Explanation

LRP [38] has been used in several studies in BCI to interpret their results neurophysiologically [16]. We also applied LRP to explain which channels of an input EEG contribute to the decision in our proposed network. We implemented LRPs by following -rule to calculate relevance scores [40] and then compared them to the PSD of raw motor imagery EEGs

[Figure 43]

- (a) Subject 5 of GIST dataset [10]

[Figure 44]

- (b) Subject 21 of KU dataset [23]

- Fig. 4. t-SNE [39] of the class-irrelevant, class-relevant, and global features in Scenario I and II. We visualized all features trained using Deep ConvNet

- [9].

by using each subject’s test samples for both Scenario I and Scenario II. First, we computed the PSD by conducting Welch’s method [41]. In an attempt to exploit spatial properties of EEG, we averaged the PSD and relevance scores in the frequency and time axis, respectively. Fig. 3 plots PSD maps and relevance heatmaps of randomly selected subjects for each class in a topological manner. Notably, in both PSD maps and relevance heatmaps, it is clearly observable the contra-lateral patterns. That is, when imagining left-/right-hand movements, the right/left motor-related areas showed noticeable activation patterns (red color), respectively. Those activated areas were highly contributed to making a decision by our method, as illustrated in the respective relevance heatmaps. Although our proposed method removed partial information considered as the class-irrelevant representation, both feature extractors (EEGNet [6] and Deep ConvNet [9]) could still learn a spatiospectral pattern inherent in motor imagery EEGs. With regard to the relevance heatmaps obtained in Scenario II, even though our network did not leverage the target subject’s samples, it could detect patterns from motor-related areas that served to identify the class of input EEGs. As a result, we believe our model well learned and utilized the neurophysiological characteristics related to motor imagery, by learning subjectinvariant and class-relevant feature representations.

B. Feature Decomposition

We used t-SNE [39] to visualize the class-irrelevant, classrelevant, and global features of subject 5 of GIST dataset [10]

and subject 21 of KU dataset [23] under both Scenario I and Scenario II as shown in Fig. 4. We observed that compared with the class-irrelevant features, the class-relevant features and the global features were separable between two classes, i.e., for the left- and right-hands. Note that in comparison between distributions of class-relevant and global features, that of global features enriched by means of local-global mutualinformation maximization was better separable showing relatively large between-class distance. In addition, although we did not exploit a target subject’s data for training, the target subject’s samples were also highly distinguishable between two classes in Scenario II. Hence, we argue that our proposed method could ﬁnd class-relevant and subject-invariant features, and successfully used to classify samples of unseen subjects.

VI. CONCLUSION

In this work, we proposed a deep neural network that learns subject-invariant and class-relevant representations via mutual information estimation among features in different levels for BCI tasks in an end-to-end manner. The subject-invariant and class-relevant feature space can be deployed for decoding a new subject and mitigate negative transfer. Notably, we showed our proposed method is independent of the feature representation, thus, we can utilize any existing decoding models as our feature extractor. We evaluated our proposed method using two large motor imagery EEG datasets. In addition, we analyzed our results to provide neurophysiological explanation and explicate the results from the viewpoint of transfer learning. Further, we expect that our proposed method could be applied to other types of EEG signals.

REFERENCES

- [1] B. Graimann, B. Allison, and G. Pfurtscheller, “Brain–computer interfaces: A gentle introduction,” in Brain-Computer Interfaces. Springer, 2009, pp. 1–27.
- [2] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial ﬁltering of single trial EEG during imagined hand movement,” IEEE Transactions on Rehabilitation Engineering, vol. 8, no. 4, pp. 441–446, 2000.
- [3] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common spatial pattern (FBCSP) in brain-computer interface,” in IEEE International Joint Conference on Neural Networks, 2008, pp. 2390–2397.
- [4] H.-I. Suk and S.-W. Lee, “A novel bayesian framework for discriminative feature extraction in brain-computer interfaces,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 35, no. 2, pp. 286–299, 2012.
- [5] C. Vidaurre, M. Kawanabe, P. von B¨unau, B. Blankertz, and K.-R. M¨uller, “Toward unsupervised adaptation of LDA for brain–computer interfaces,” IEEE Transactions on Biomedical Engineering, vol. 58, no. 3, pp. 587–597, 2010.
- [6] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for EEG-based brain–computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
- [7] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE transactions on neural networks and learning systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [8] W. Ko, J. Yoon, E. Kang, E. Jun, J.-S. Choi, and H.-I. Suk, “Deep recurrent spatio-temporal neural network for motor imagery based BCI,” in 2018 6th International Conference on Brain-Computer Interface (BCI). IEEE, 2018, pp. 1–3.
- [9] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.

- [10] H. Cho, M. Ahn, S. Ahn, M. Kwon, and S. C. Jun, “EEG datasets for motor imagery brain–computer interface,” GigaScience, vol. 6, no. 7, p. gix034, 2017.
- [11] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. GrosseWentrup, “Transfer learning in brain-computer interfaces,” IEEE Computational Intelligence Magazine, vol. 11, no. 1, pp. 20–31, 2016.
- [12] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Transactions on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345– 1359, 2009.
- [13] X. Chai, Q. Wang, Y. Zhao, X. Liu, O. Bai, and Y. Li, “Unsupervised domain adaptation techniques based on auto-encoder for non-stationary EEG-based emotion recognition,” Computers in Biology and Medicine, vol. 79, pp. 205–214, 2016.
- [14] E. Jeon, W. Ko, and H.-I. Suk, “Domain adaptation with source selection for motor-imagery based BCI,” in 2019 7th International Winter Conference on Brain-Computer Interface (BCI). IEEE, 2019, pp. 1–4.
- [15] Y.-P. Lin and T.-P. Jung, “Improving EEG-based emotion classiﬁcation using conditional transfer learning,” Frontiers in Human Neuroscience, vol. 11, p. 334, 2017.
- [16] O. Ozdenizci,¨ Y. Wang, T. Koike-Akino, and D. Erdo˘gmu¸s, “Learning invariant representations from EEG via adversarial inference,” IEEE Access, vol. 8, pp. 27074–27085, 2020.
- [17] ——, “Transfer learning in brain-computer interfaces with adversarial variational autoencoders,” in 2019 9th International IEEE/EMBS Conference on Neural Engineering (NER). IEEE, 2019, pp. 207–210.
- [18] Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. Marchand, and V. Lempitsky, “Domain-adversarial training of neural networks,” The Journal of Machine Learning Research, vol. 17, no. 1, pp. 2096–2030, 2016.
- [19] M. Wang and W. Deng, “Deep visual domain adaptation: A survey,” Neurocomputing, vol. 312, pp. 135–153, 2018.
- [20] E. Tzeng, J. Hoffman, K. Saenko, and T. Darrell, “Adversarial discriminative domain adaptation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 7167–7176.
- [21] H. Liu, M. Long, J. Wang, and M. Jordan, “Transferable adversarial training: A general approach to adapting deep classiﬁers,” in International Conference on Machine Learning, 2019, pp. 4013–4022.
- [22] X. Peng, Z. Huang, X. Sun, and K. Saenko, “Domain agnostic learning with disentangled representations,” in International Conference on Machine Learning, 2019, pp. 5102–5112.
- [23] M.-H. Lee, O.-Y. Kwon, Y.-J. Kim, H.-K. Kim, Y.-E. Lee, J. Williamson, S. Fazli, and S.-W. Lee, “EEG dataset and openbmi toolbox for three BCI paradigms: An investigation into BCI illiteracy,” GigaScience, vol. 8, no. 5, p. giz002, 2019.
- [24] P.-J. Kindermans, M. Tangermann, K.-R. M¨uller, and B. Schrauwen, “Integrating dynamic stopping, transfer learning and language models in an adaptive zero-training ERP speller,” Journal of Neural Engineering, vol. 11, no. 3, p. 035005, 2014.
- [25] A. M. Azab, L. Mihaylova, K. K. Ang, and M. Arvaneh, “Weighted transfer learning for improving motor imagery-based brain–computer interface,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 7, pp. 1352–1359, 2019.
- [26] C.-S. Wei, Y.-P. Lin, Y.-T. Wang, C.-T. Lin, and T.-P. Jung, “A subjecttransfer framework for obviating inter-and intra-subject variability in EEG-based drowsiness detection,” NeuroImage, vol. 174, pp. 407–419, 2018.
- [27] X. Wang, L. Li, W. Ye, M. Long, and J. Wang, “Transferable attention for domain adaptation,” in AAAI Conference on Artiﬁcial Intelligence (AAAI), 2019.
- [28] F. Chollet, “Xception: Deep learning with depthwise separable convolutions,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 1251–1258.
- [29] M. I. Belghazi, A. Baratin, S. Rajeshwar, S. Ozair, Y. Bengio, D. Hjelm, and A. Courville, “Mutual information neural estimation,” in International Conference on Machine Learning, 2018, pp. 530–539.
- [30] M. D. Donsker and S. S. Varadhan, “Asymptotic evaluation of certain markov process expectations for large time. iv,” Communications on Pure and Applied Mathematics, vol. 36, no. 2, pp. 183–212, 1983.
- [31] R. D. Hjelm, A. Fedorov, S. Lavoie-Marchildon, K. Grewal, P. Bachman, A. Trischler, and Y. Bengio, “Learning deep representations by mutual information estimation and maximization,” in International Conference on Learning Representations, 2019.
- [32] S. Nowozin, B. Cseke, and R. Tomioka, “f-gan: Training generative neural samplers using variational divergence minimization,” in Advances in Neural Information Processing Systems, 2016, pp. 271–279.

- [33] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” arXiv preprint arXiv:1502.03167, 2015.
- [34] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout: A simple way to prevent neural networks from overﬁtting,” The Journal of Machine Learning Research, vol. 15, no. 1, pp. 1929–1958, 2014.
- [35] L. Liu, H. Jiang, P. He, W. Chen, X. Liu, J. Gao, and J. Han, “On the variance of the adaptive learning rate and beyond,” in Proceedings of the Eighth International Conference on Learning Representations (ICLR 2020), April 2020.
- [36] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve BCI designs: uniﬁed theory and new algorithms,” IEEE Transactions on biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2010.
- [37] H. Kang, Y. Nam, and S. Choi, “Composite common spatial pattern for subject-to-subject transfer,” IEEE Signal Processing Letters, vol. 16, no. 8, pp. 683–686, 2009.
- [38] G. Montavon, S. Lapuschkin, A. Binder, W. Samek, and K.-R. M¨uller, “Explaining nonlinear classiﬁcation decisions with deep taylor decomposition,” Pattern Recognition, pp. 211–222, 2017.
- [39] L. v. d. Maaten and G. Hinton, “Visualizing data using t-SNE,” Journal of Machine Learning Research, vol. 9, no. Nov, pp. 2579–2605, 2008.
- [40] S. Bach, A. Binder, G. Montavon, F. Klauschen, K.-R. M¨uller, and W. Samek, “On pixel-wise explanations for non-linear classiﬁer decisions by layer-wise relevance propagation,” PloS One, vol. 10, no. 7, 2015.
- [41] P. Welch, “The use of fast fourier transform for the estimation of power spectra: a method based on time averaging over short, modiﬁed periodograms,” IEEE Transactions on audio and electroacoustics, vol. 15, no. 2, pp. 70–73, 1967.

