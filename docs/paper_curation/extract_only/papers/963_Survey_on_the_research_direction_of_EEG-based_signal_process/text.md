TYPE Review PUBLISHED July DOI   .    /fnins.    .       

OPEN ACCESS

EDITED BY

Aydin Farajidavar, New York Institute of Technology, United States

REVIEWED BY

Maryam Ravan, New York Institute of Technology, United States Mohammad Ali Ahmadi-Pajouh, Amirkabir University of Technology, Iran

*CORRESPONDENCE

Chaozhou Mou

mouchaozhou@mail.sdu.edu.cn

RECEIVED April ACCEPTED June PUBLISHED July

CITATION

Sun C and Mou C (    ) Survey on the research direction of EEG-based signal processing. Front. Neurosci.   :       . doi:   .    /fnins.    .       

COPYRIGHT

© Sun and Mou. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# Survey on the research direction of EEG-based signal processing

Congzhong Sun and Chaozhou Mou*

School of Mathematics and Statistics, Shandong University, Weihai, China

Electroencephalography (EEG) is increasingly important in Brain-Computer Interface (BCI) systems due to its portability and simplicity. In this paper, we provide a comprehensive review of research on EEG signal processing techniques since     , with a focus on preprocessing, feature extraction, and classiﬁcation methods. We analyzed research articles retrieved from academic search engines, including CNKI, PubMed, Nature, IEEE Xplore, and Science Direct. For preprocessing, we focus on innovatively proposed preprocessing methods, channel selection, and data augmentation. Data augmentation is classiﬁed into conventional methods (sliding windows, segmentation and recombination, and noise injection) and deep learning methods [Generative Adversarial Networks (GAN) and Variation AutoEncoder (VAE)]. We also pay attention to the application of deep learning, and multi-method fusion approaches, including both conventional algorithm fusion and fusion between conventional algorithms and deep learning. Our analysis identiﬁes (  . %), (  . %), and (  . %) studies in the directions of preprocessing, feature extraction, and classiﬁcation, respectively. We ﬁnd that preprocessing methods have become widely used in EEG classiﬁcation (  . % of reviewed papers) and comparative experiments have been conducted in some studies to validate preprocessing. We also discussed the adoption of channel selection and data augmentation and concluded several mentionable matters about data augmentation. Furthermore, deep learning methods have shown great promise in EEG classiﬁcation, with Convolutional Neural Networks (CNNs) being the main structure of deep neural networks (  . % of deep learning papers). We summarize and analyze several innovative neural networks, including CNNs and multi-structure fusion. However, we also identiﬁed several problems and limitations of current deep learning techniques in EEG classiﬁcation, including inappropriate input, low cross-subject accuracy, unbalanced between parameters and time costs, and a lack of interpretability. Finally, we highlight the emerging trend of multi-method fusion approaches (  . % of reviewed papers) and analyze the data and some examples. We also provide insights into some challenges of multi-method fusion. Our review lays a foundation for future studies to improve EEG classiﬁcation performance.

KEYWORDS

electroencephalography (EEG), brain-computer interface (BCI), preprocessing, feature extraction, classiﬁcation, deep learning (DL), multi-method fusion

##  . Introduction

The Brain-Computer Interface (BCI) is a communication system that allows humans to send messages and commands to the outside world without relying on peripheral nerves and muscles (Wolpaw et al., 2000). The BCI system is composed of four primary components: signal acquisition, signal processing, control equipment, and feedback link. Signal acquisition technology in BCI systems can be divided into two categories: noninvasive methods and invasive methods. While invasive methods, such as implanting

electrodes directly into the brain, have been explored in some studies, they are not commonly used due to the potential risks and complicated operations. Thus, non-invasive methods are used in many studies. Non-invasive methods include functional Magnetic Resonance Imaging (fMRI), functional Near-Infrared Spectroscopy (fNIRS), Magnetoencephalography (MEG), Electroencephalography (EEG), and Positron Emission Tomography (PET).

Among the aforementioned methods, EEG signals are commonly utilized due to their features of safety, portability, ease of use, high temporal resolution, and low cost (Singh et al., 2021). EEG signals are a useful tool for directly reﬂecting the activities of the brain, in both BCI and clinical applications (Wolpaw et al., 2000; Michel and Murray, 2012). For example, a typical application of EEG-BCI systems is to control a robot arm by brain signals, which will be greatly helpful for not only the disabled but also general people to improve their life (Jeong et al., 2020). Therefore, it is important to process and analyze EEG signals so as to ﬁt multitudes of applications in BCI. EEG signal processing typically involves three main steps: preprocessing, feature extraction, and classiﬁcation.

EEG signals are typically collected using multiple electrodes placed on the scalp, with electrodes placed on diﬀerent scalp locations to collect signals from various brain areas. The positioning or arrangement of electrodes is called the montage, and there are two broad categories of montages: bipolar and referential (Kumar and Bhuvaneswari, 2012). The former compares an electrode with its neighbors and outputs their diﬀerence as a channel, while the latter chooses one reference electrode and compares all other electrodes with this electrode (Sanei and Chambers, 2021). After acquisition, the raw EEG signals are represented as 2D tensors (multi-channel 1D sequences) with shape C × T, where C and T represent the number of channels and time samples, respectively. Many datasets adopt referential montage, and thus in those datasets, one channel corresponds to one electrode. The collected signal can be considered as complex mixtures of the activities of many brain cells, resulting in EEG signals exhibiting various rhythms that reﬂect diverse cognitive states and are associated with diﬀerent brain activities. Diﬀerent rhythms can be broadly categorized into several bands based on frequency, including delta (1–4 Hz), theta (4–8 Hz), alpha (8–12 Hz), beta (13–25 Hz), and gamma (≥25 Hz; Kumar and Bhuvaneswari, 2012; Singh et al., 2021). Additionally, EEG signals can have diﬀerent paradigms, referring to diﬀerent types of tasks or stimuli. Common paradigms include P300 (Bashashati et al., 2007), Motor Imagery (MI; Cano-Izquierdo et al., 2012), SteadyState Visual Evoked Potential (SSVEP; Wolpaw et al., 2003), etc. These paradigms often relate to speciﬁc brain activities and signal processing tasks. For example, when a person imagines his/her limb moving, some speciﬁc changes in EEG signals will occur, the paradigm of which is called MI, and this will relate to the task of controlling a device to move.

However, in order to eﬀectively process EEG signals, it is important to consider some of their inherent characteristics, including:

1. Low spatial resolution and low Signal-to-Noise Ratio (SNR). EEG signals are susceptible to interference and artifacts.

Therefore, signal processing must address the challenges of separating noise from abnormal signals and extracting meaningful features.

- 2. Dimensionality disaster. EEG signals have multiple channels during acquisition, leading to exponentially increasing computation as dimensionality increases.
- 3. Non-stationariness. The statistics of EEG signals change rapidly over time.
- 4. Lack of large labeled training samples. Due to the requirement for high participant focus during data acquisition, it is diﬃcult to obtain a large number of brain data. For example, frequent visual stimulation during Visual Evoked Potential (VEP) signals acquisition can cause visual fatigue. Consequently, many datasets have a limited number of samples.
- 5. Subject-speciﬁcity. EEG signals diﬀer signiﬁcantly among individuals, leading to poor stability and generalization. Models trained on speciﬁc subjects may not perform well on new subjects (Lashgari et al., 2020).

Furthermore, unlike image processing and natural language processing, we lack speciﬁc knowledge of the physiological activity of our brains. This means that we cannot intuitively understand EEG signals or apply our a priori knowledge to them.

The rest of this article is organized as follows: In the next part of Section 1, we introduce three steps of EEG signal processing and summarize several previous reviews. In Section 2, we summarize the relevant information for the proposed approaches and how the papers were selected and assessed. In Section 3, discussions are introduced, where speciﬁc methods are compared, including preprocessing, deep learning, and multi-method fusion. In Section 4 we show our conclusions ﬁnally.

 . . Preprocessing

After collecting EEG signals, it is necessary to preprocess the data in order to remove irrelevant noise and reduce computational complexity. In the following text, we will introduce some preprocessing methods.

 . . . Basic preprocessing methods

Basic preprocessing methods are based on some basic characteristics of EEG signals. These methods including ﬁltering, electrode positioning, deletion of useless data, baseline correction, heavy reference, downsampling, removal of artifacts, removal of bad segments, etc. These methods can be easily invoked by the EEGLAB toolbox, a useful Matlab toolbox that facilitates various preprocessing operations of EEG signals (Delorme and Makeig, 2004; Bashashati et al., 2007).

Filtering is one of the most frequently used preprocessing methods. EEG signals have low SNR and diﬀerent rhythms; thus, band-pass ﬁltering is suitable to eliminate noise that has a diﬀerent frequency from EEG signals and separate useful rhythms from the source (Saeidi et al., 2021).

 . . . Data augmentation

To address the problem of small dataset, data augmentation is an eﬀective method, which includes both non-deep learning methods like sliding windows, noise injection, and segmentation and recombination, as well as deep learning methods like Generative Adversarial Networks (GAN) and Variation AutoEncoder (VAE; Lashgari et al., 2020; He et al., 2021). Many models, especially deep learning models, require a large amount of training data to achieve high classiﬁcation accuracy and avoid overﬁtting. However, collecting a large number of EEG data is diﬃcult due to the intrinsic characteristics of EEG signals. Data augmentation can generate new data from a small dataset, providing enough training data.

Among non-deep learning methods, sliding window crops the signals into several segments by sliding a window on the signals. The length and overlap of segments depend on the window size and window step. Sliding window increases the number of training data but also eliminates long-term information. Segmentation methods can cut out speciﬁc time intervals based on the temporal characteristics of EEG signals (Lu et al., 2022). Gaussian noise injection injects a random matrix from a Gaussian distribution into the original data to achieve data augmentation (Okafor et al., 2017). These methods are intuitive and simple, but they may exacerbate the overﬁtting of models due to their similarity after augmentation.

GAN and its variants can generate artiﬁcial data by training a generative network and a discriminative network (Zhang A. et al., 2021). The generative network accepts random noise from a speciﬁc distribution (e.g., Gaussian) and attempts to generate synthetic data similar to real data, while the discriminative network is trained to classify the real and synthetic data. These two networks are adversarial, and after adequate training, the generative network will produce verisimilar signals. For VAE, like a normal autoencoder (which will be introduced below), the encoder converts the raw data into latent data, and the decoder maps the latent data back to real data. To generate new data, the VAE randomly samples points from the learned latent space, and then passes these samples through the decoder network, which reconstructs them into new samples. Both GAN and VAE generate new samples indirectly.

 . . . Channel selection

During acquisition, every electrode records a channel of data. Thus the raw EEG signals has C channels, which is known as the multi-dimensionality of EEG signals. Diﬀerent channels correspond to diﬀerent areas of the brain. For a speciﬁc task, some channels may contain task-irrelevant or redundant information (Liu et al., 2016), which increases data size and time cost, and can negatively impact the performance of BCI (Asensio-Cubero et al., 2013). Channel selection is a method to select the most salient channels of task-related regions as the optimal channels so as to improving performance and eﬃciency. However, multichannel EEG data contain complex channel correlations rather than simple adjacencies (Cona et al., 2009; Hamedi et al., 2016). Therefore, we should seek selection criteria based on the features of channels, such as correlation, electrode distance, and task characteristics, to select

the channels that preserve the signal features to the maximum extent possible.

 . . . Dimensionality reduction

EEG signals are multi-dimensional signals. Compared to traditional 1D signals, EEG signal processing has high computational complexity. Therefore, we usually need to impose corresponding constraint assumptions according to the structure of EEG signals and reduce the dimensionality to further improve the extraction eﬀect and classiﬁcation robustness of feature signals.

Many algorithms can reduce the dimension. For instance, Principle Component Analysis (PCA) can decompose the EEG signal into linearly uncorrelated components which have the maximum variance. Redundant components such as interference from eyes and muscles can be separated by PCA before reconstructing the EEG signal (Liu and Yao, 2006). Independent Component Analysis (ICA) separates artifacts from EEG signals as independent components based on data features (Saeidi et al., 2021). Geng et al. (2022) proposed that preprocessing can decompose complex mixed signals into independent signals by ICA to achieve separation of P300 signals from noise. However, because the ICA algorithm was not trained to learn the characteristics of noise signals, some valuable signals may be removed as noise, causing some brain activity information loss. By using the Wavelet Transform (WT), the feature of EEG signals can be extracted, and then by ICA-WT ﬁltering, the noise artifacts can be eﬀectively eliminated, thus eﬀectively improving the accuracy of EEG signals of diﬀerent subjects (Ayoobi and Sadeghian, 2022). Ayoobi and Sadeghian (2022) also investigated the AutoEncoder (AE) for preprocessing, where the encoder extracts the information of the input raw data into a small latent space and then decodes the latent data to reconstruct the dataset. Since the latent variables carry information of raw signals but have fewer dimensions, we can use latent variables as the input of subsequent steps.

###  . . Feature extraction

Feature extraction generally refers to the extraction of hidden brain information features from signals. Next, we will introduce some feature extraction methods, including both conventional algorithms (non-deep learning) and deep learning algorithms.

 . . . Feature extraction by conventional algorithms

The conventional algorithms adopted in feature extraction include Common Spatial Pattern (CSP), Fourier Transform (FT), Power Spectral Density (PSD), Wavelet Transform (WT), Wavelet Packet Decomposition (WPD), Empirical Mode Decomposition (EMD), Autoregression (AR), and Hjorth parameters, etc. (Wolpaw et al., 2003; Kim et al., 2018; Torres et al., 2020).

Common Spatial Pattern (CSP) is a space domain ﬁltering algorithm used for binary classiﬁcation tasks. CSP extracts the spatial distribution components of each class of the multi-channel EEG signal and seeks the best projection direction to maximize the variance of one class and minimize that of the other class (Meng

et al., 2022). Since CSP maximizes the diﬀerence among EEG signals, it is more capable of mining the features of EEG signals. However, the number of electrodes needs to be further optimized because a large number of electrodes are required for multichannel analysis of EEG signals. There are also many variants of CSP, such as Common Space Spectral Pattern (CSSP), Filter Bank CSP (FBCSP), etc. (Park et al., 2018; Maruyama et al., 2020; Kumar et al., 2021).

EEG signals exhibit various frequency bands, each associated with distinct brain activities. Therefore, analyzing EEG signals in the frequency domain and time-frequency domain is a common approach. Fourier Transform (FT), particularly Fast Fourier Transform (FFT) as a fast version, is a fundamental tool in frequency analysis. It can transform stationary signals to the frequency domain to extract frequency features. Power Spectral Density (PSD), the FT of the autocorrelation function of a signal, reveals the power (energy) distribution across diﬀerent frequencies. However, FT and PSD can only analyze the frequency content across the entire series. To analyze the frequency changes over time, time-frequency analysis methods are necessary. ShortTime Fourier Transform (STFT) segments signals into short time intervals before applying Fourier transform to analyze the frequency variance. Wavelet Transform (WT), an improved method of STFT, is suitable for analyzing non-stationary signals such as EEG signals (Al-Fahoum and Al-Fraihat, 2014). Wavelet Packet Decomposition (WPD), a modiﬁcation of WT, further decomposes the high-frequency sub-bands and provides better frequency resolution. Following the time-frequency analysis, the signal shape becomes F × T × C, where F represents the frequency resolution.

Furthermore, Autoregression (AR) is a popular approach used in time-series prediction. AR assumes that the current value of a time series depends linearly on its past values (Saeidi et al., 2021). Another technique used to analyze non-stationary EEG signals is Empirical Mode Decomposition (EMD). EMD is a non-linear method that decomposes a signal into its intrinsic modes of oscillation (El-Kafrawy et al., 2014). This method has been used to study the time-frequency characteristics of EEG signals. Finally, Hjorth parameters are statistical features used to extract information about EEG signals (Du et al., 2021). The three Hjorth parameters are Activity, Mobility, and Complexity. Activity measures the signal’s energy, Mobility measures its frequency content, and Complexity reﬂects the signal’s nonlinearity.

 . . . Automatic feature extraction by deep learning

Traditional feature extraction algorithms such as CSP and PSD have limitations. For instance, feature extraction and classiﬁcation are performed separately, and much experience or priori knowledge is manually added during feature extraction. In contrast, deep learning algorithms utilize a deep architecture consisting of many hidden layers to automatically extract spatiotemporal features of EEG signals using a large number of training parameters and data (Aellen et al., 2021). The location of discriminative patterns of deep learning in spatial detection is irrelevant, which often leads to neural networks outperforming conventional machine learning algorithms. Deep

learning algorithms are capable of learning useful features that capture the underlying structure of EEG signals, without the need for explicit feature extraction. Furthermore, deep learning methods have the potential to overcome the limitations of traditional feature extraction methods and to enable more accurate classiﬁcation of EEG signals.

###  . . Classiﬁcation algorithms

General tasks of machine learning can be sorted into two categories: regression and classiﬁcation. There are several novel papers adopting regression methods, such as Jeong et al. (2020) which adopted deep learning to track the movement of a robot arm. But among the research on EEG, most studies focused on classiﬁcation, since the labels of tasks and outputs of processing are usually categorical variables. The development of higher performance and more robust classiﬁcation algorithms is a key focus in EEG research. The selection of a classiﬁcation algorithm plays a crucial role in determining the performance of the system.

 . . . Conventional classiﬁcation algorithms

Conventional BCI classiﬁcation algorithms include Support Vector Machine (SVM; Li et al., 2018), Linear Discriminant Analysis (LDA; Vidaurre et al., 2011), and k-Nearest Neighbor (KNN; Tang et al., 2019). SVM can be used for linearly separable data by ﬁnding an optimal hyperplane through optimization algorithms. For linearly inseparable problems, a kernel function can be used to transform the data into a higher dimensional space. LDA is a simple linear classiﬁer that projects all samples onto a line to maximize the inter-class distance and minimize the intra-class variance. KNN is a method for classiﬁcation that counts the class number of the k nearest samples with the least distance to the new sample.

While SVM and LDA are popular algorithms with good performance, SVM can be computationally complex and LDA requires linear separability. KNN is simple and easy to use, but can be weak in generalization.

 . . . Deep learning algorithm

Deep learning algorithms have been shown to be eﬀective in extracting features from high-dimensional data. They are particularly useful for processing EEG signals, which are often highdimensional and complex. Deep learning methods use Artiﬁcial Neural Networks (ANN) to process data, which can automatically learn features that are relevant to the task, and can generalize well across diﬀerent tasks. The structure of ANN is shown at the top of Figure 1. Common deep learning algorithms and ANNs applied to EEG signal processing include Multilayer Perceptrons (MLP), Convolutional Neural Network (CNN; Mane et al., 2020), Recurrent Neural Network (RNN; Luo et al., 2018), etc.

The most simple deep learning algorithm is the Multilayer Perceptron (MLP). An MLP is a network constructed by Fully Connected (FC) layers (also called Dense layer or Linear layer in some papers), in which a linear transform and a subsequent

|[Figure 1]<br><br>FIGURE<br><br>The structure of artiﬁcial neural networks in deep learning. Each layer in the network can be an FC layer (left bottom), a convolutional layer of CNN (middle bottom), or a recurrent layer of RNN (right bottom).|
|---|

nonlinear activation function are used sequentially. Let x ∈ Rm be the input, the output y ∈ Rn of a single FC layer is calculated by

the features along the time dimension; if m × 1, it will seek the correlations of diﬀerent channels.

Plenty of CNN structures have been applied to EEG signal processing, such as residual network (ResNet; He et al., 2016) and ConvNet (Azizpour et al., 2016). EEG-speciﬁc neural networks have also been proposed, such as EEGNet. EEGNet is a compact CNN with only three convolutional layers, and it adopts two special structures—depthwise convolutional layers and separable convolutional layers to reduce the number of parameters and computational costs (Lawhern et al., 2018). EEGNet is proposed in 2018, and has been shown to be more robust, more compact, and less data-intensive to diﬀerent paradigms of EEG signals, and thus has widespread application in EEG signal processing.

Recurrent Neural Networks (RNN) are another type of deep learning algorithm that has been used in EEG signal processing. RNN appends a hidden state into conventional MLP and passes the hidden state into the next unit, which is ﬁt for extracting long-term relations of time series models. EEG signals, as a kind of contextsensitive sequences, are also suitable for using RNN to extract temporal features. A recurrent unit of RNN accepts a sequence

- x ∈ RT as input, and will calculate the hidden state h and output
- y by

ht = σ(W1xt + W2ht−1 + b2); yt = W3ht + b2;

(3)

y = σ(Wx + b); (1)

where W ∈ Rm×n,b ∈ Rn and σ are weight matrix, bias and activation function, respectively (Zhang A. et al., 2021). The bottom left of Figure 1 illustrates an example of the FC layer. MLP is seldom used alone now, but FC is often combined with other networks, used as the last layer to classify the features.

One deep learning algorithm that has been widely used in EEG signal processing is the Convolutional Neural Network (CNN). CNN adopts convolution operations to automatically extract features from the data. CNN consists of multiple convolutional layers, which accept a 2D image or a 3D multi-channel image as the input and apply convolution operation on it. For a given input X ∈ Rc×m×n, a convolutional layer gives the output Y ∈ Rd×m′×n′ by

δ2

δ1

Yd,i,j =

q=−δ2

p=−δ1

c

Kd,r,p,qXr,i+p,j+q; (2)

r=1

where c and d denotes the input and output channels, respectively; K ∈ Rd×c×(2δ1+1)×(2δ2+1) is the kernel and also parameters of CNN (Zhang A. et al., 2021). A graph of convolutional layers is shown at the bottom middle of Figure 1. Since c and d are decided by the layers, the shape of kernel K is often shorted to (2δ1 + 1) × (2δ2 + 1). The operation of a convolution layer is actually a spatial ﬁlter, but its parameters can be updated by the backpropagation algorithm automatically. Also, diﬀerent sizes of kernels can be used for diﬀerent tasks. When the input tensor has size C × T, like raw EEG signals, if we set the size of the kernel to 1 × n, it will extract

where W1,W2,W3 are weight matrices, b1,b2 are biases and σ is the activation function. The structure of a recurrent layer is illustrated in the bottom right of Figure 1. Long Short-Term Memory (LSTM) network (Wang et al., 2018) and Gated Recurrent Unit (GRU; Nakagome et al., 2020) are two popular variants of RNN. By appending several gate units into conventional RNN, they inherit the advantages of RNN and lead to more accurate analysis of sequence data.

Batch Normalization (BN), dropout, and attention mechanisms are also spreadly used. During the mini-batch feedforward step, the data passing BN will subtract the mean and divided by the variance, converted into zero mean and unit variance (Zhang A. et al., 2021). BN is usually used before an activation function so as to improve the distinction of the activation function. Dropout is a method that makes the unit of networks stop with a probability p to avoid overﬁtting, which is only used during training (Zhang A. et al., 2021). Attention mechanisms simulate the attention functions of our brain to make signiﬁcant information prominent. Attention mechanisms are not a single algorithm, but a set of methods including conventional methods and CNN-based methods.

In addition, the Transfer Learning (TL) algorithm supplements the limited training data with data transferred from other domains to improve the system portability and solve the problem of long training time while ensuring accuracy (Zhang et al., 2020). TL uses the similarities between two tasks, and transfers what has been learned from the source network into the target network to enhance the model. Facing a small dataset, TL has become an eﬀective method to improve performance.

 . . Research issues and contribution

 . . Reviewed papers

In previous research, Alzahab et al. (2021) provided a comprehensive summary of hybrid deep learning algorithms used in EEG-based BCI systems between 2015 and 2020 and compared their accuracy. However, they also highlighted the lack of evidence regarding the impact of preprocessing on the accuracy of EEG classiﬁcation. Vallabhaneni et al. (2021) surveyed articles that used deep learning to decode EEG signals in diﬀerent applications, and outlined some existing deep learning problems. Chen and Xie (2019) suggested that the choice of data processing methods should be based on the characteristics and size of the EEG signals. He et al. (2021) reviewed the application of data augmentation in EEG and found that it could improve classiﬁcation performance and overcome the challenges of small-scale datasets. Saeidi et al. (2021) systematically reviewed the machine learning-based EEG decoding methods in terms of diﬀerent tasks and concluded that CNN, SVM, and WT become the most eﬀective deep learning, conventional machine learning, and feature extraction methods. These studies have contributed to the advancement of BCI-EEG and highlighted the existing challenges in this ﬁeld.

In this paper, we analyze the latest studies since 2021 and compare them to the reviews and articles before 2020. We choose post-2021 articles since there have been plenty of reviews focused on the articles before 2020, and we want to summarize the latest development. Based on the articles we reviewed, we provide an overview of the research landscape in EEG-based BCI signals and the emerging trends. We focus on answering the following research questions: What are the current research topics in BCI signal processing? How can we evaluate BCI performance and improve it? What are the innovative approaches being explored in this ﬁeld? We also evaluate the strengths and limitations of diﬀerent methods. Our main contributions are as follows:

- 1. We summarize various methods of EEG-based signal processing of BCI systems and the major research trends. We also propose solutions to potential issues.
- 2. We attempt to seek valid, reasonable, and useful indicators of BCI performance.
- 3. We conﬁrm the eﬀectiveness of preprocessing on the performance.
- 4. We discuss deep learning and multi-method fusion studies in diﬀerent aspects and summarize several existing problems.

##  . Search methods and reviewed table

 . . Search methods

Research articles were selected for review on 31 June 2022. The following databases were conducted: CNKI, PubMed, Nature, IEEE Xplore, and Science Direct. The search covered studies published between 2021 and 2022. The following query terms are used: (“brain-machine interface” OR “brain-computer interface” OR “BCI”) AND (“EEG” OR “electroencephalography”) AND (“preprocessing” OR “feature extraction” OR “classiﬁcation”). This search resulted in 61 research papers, as shown in Figure 2.

By collecting and summarizing the papers on EEG-based BCI signal processing, we sort out a variety of new methods for EEG signal processing and analyze the characteristics of their performance.

Since the table of all the reviewed papers is too large, we only provide a list of the papers reviewed in this article. A detailed table with information on the directions and performance of each paper can be found in the Supplementary material. The following reviewed papers are presented in ascending order of their published date (Aellen et al., 2021; Asheri et al., 2021; Ashwini and Nagaraj, 2021; Awais et al., 2021; Cai et al., 2021; Dagdevir and Tokmakci,

- 2021; De Venuto and Mezzina, 2021; Du et al., 2021; Fan et al., 2021, 2022; Ferracuti et al., 2021; Gao N. et al., 2021; Gao Z. et al.,

- 2021; Gaur et al., 2021; Lashgari et al., 2021; Lian et al., 2021; Liu and Jin, 2021; Liu and Yang, 2021; Liu et al., 2021; Qi et al., 2021; Rashid et al., 2021; Sun et al., 2021; Varsehi and Firoozabadi, 2021; Vega et al., 2021; Vorontsova et al., 2021; Wahid and Tafreshi, 2021; Wang and Quan, 2021; Xu C. et al., 2021; Xu F. et al., 2021; Yin et al.,

- 2021; Zhang K. et al., 2021; Zhang Y. et al., 2021; Algarni et al., 2022; Ali et al., 2022; Asadzadeh et al., 2022; Ayoobi and Sadeghian, 2022; Bagchi and Bathula, 2022; Chang et al., 2022; Chen J. et al., 2022; Chen L. et al., 2022; Cui et al., 2022; Geng et al., 2022; Islam et al.,
- 2022; Jia et al., 2022; Kim et al., 2022; Ko et al., 2022; Li and Sun,

- 2022; Li H. et al., 2022; Lin et al., 2022; Li Q. et al., 2022; Lu et al.,

- 2022; Ma et al., 2022; Mattioli et al., 2022; Meng et al., 2022; Pei et al., 2022; Song et al., 2022; Suhaimi et al., 2022; Tang et al., 2022; Xu et al., 2022; Ying et al., 2022; Zhao et al., 2022).

##  . Results and discussion

The BCI system based on EEG signals analyzes the instructions issued by the human brain. The processing and classiﬁcation of EEG signals determine the performance of the BCI system. In the study of EEG signal processing, several questions arise, including:

- 1. What is the current development trend of EEG signal processing techniques?
- 2. How to select a processing method suitable for EEG signal characteristics?
- 3. How to apply deep learning algorithm properly to enhance performance?
- 4. Why do we need multi-method fusion, and are they valid?

Considering the characteristics of EEG signals, the processing of EEG signals aims to ﬁnd a feasible method to fuse the signal pattern to seek high-performance and strong applicability processing methods. Currently, many preprocessing, feature extraction, and classiﬁcation algorithms are applied to EEG signals, each with its own advantages and disadvantages. Therefore, appropriate methods should be selected according to speciﬁc situations. In this paper, we classify algorithms according to the categories introduced in Section 1. In the following, we will discuss the directions and numbers of reviewed studies.

For preprocessing, by increasing data samples and identifying valid data, it can obtain better features of signals and reduce computation costs. By studying the 61 papers, we found that the

|[Figure 2]<br><br>FIGURE<br><br>The search method for identifying studies about EEG signal processing.|
|---|

number of preprocessing studies is 35 (57.4%). This suggests that preprocessing is an important step to seek more prominent features and achieve higher performance of EEG signals. As for feature extraction, since deep learning has a strong ability in automatic feature extraction learning of EEG signals, feature extraction tends to be completed automatically by deep learning algorithms. Therefore the number of feature extraction studies is only 18 (29.5%). The number of classiﬁcation algorithms is 37 (60.7%), indicating that the innovation of classiﬁcation algorithms is still the main method to improve the performance of BCI. Thus it is the focus and hotspot of current EEG processing research. The study number of these three directions is shown in Figure 3.

 . . Indicators of EEG

Various indicators are used to measure the performance of classiﬁers in EEG classiﬁcation. Accuracy (ACC) remains the most widely used indicator across papers as it provides an intuitive measure of classiﬁcation performance. However, several other indicators, such as the confusion matrix (Algarni et al., 2022) and kappa (Lian et al., 2021), are also commonly employed. The confusion matrix compares the number of predicted and actual labels in an n × n matrix. On the other hand, kappa measures the consistency of classiﬁcation and is used in multiple studies to gauge performance improvement.

Although accuracy is the primary indicator, 16 papers also compare other factors like parameter number, Information Translating Rate (ITR), and computation time. Parameter number is used to measure the complexity of a model, especially for neural networks. ITR and computation time reﬂect the speed of classiﬁcation and are crucial factors in many studies. Notably, six

studies improve ITR, with the maximum ITR reaching 170.67 bit/min in Zhang K. et al. (2021). Seven studies achieve time cost reduction, reﬂecting the importance of computational eﬃciency.

Given the subject-speciﬁcity of EEG signals, researchers also investigate the variation between subject-dependent (withinsubject) and subject-independent (cross-subject) accuracy. Subjectindependent tasks involve testing models on new individuals whose data are not included in the training data, whereas subjectdependent tasks test on diﬀerent segments of the same individuals’ data. Singh et al. (2021) has highlighted the importance of subjectindependent tasks— they play a crucial role in designing a plugand-play calibration-free BCI device. While many studies report high within-subject accuracy, which can exceed 90% in several cases, cross-subject accuracy is still lower (mostly around 50%; Lashgari et al., 2021; Fan et al., 2022). Improving cross-subject accuracy has become a signiﬁcant direction.

 . . Preprocessing

In the 35 studies about preprocessing, innovative preprocessing methods include channel selection (10 papers, 28.6%), dimension reduction (11 papers, 31.4%), data augmentation (16 papers, 45.7%), etc., as shown in Figure 4. Dimension reduction is commonly used to reduce computation complexity, but only around half of the studies applying dimension reduction have innovative methods. While channel selection and sliding windows are also widely used, many papers proposed new channel selection or sliding window approaches.

According to Alzahab et al. (2021), among studies on hybrid Deep Learning (hDL) from 2015 to 2020, 21.28% did not

|[Figure 3]<br><br>FIGURE<br><br>Numbers of di erent directions of EEG signal processing. The numbers of preprocessing (P), feature extraction (F), and classiﬁcation algorithm (C) papers are   ,   , and   , respectively. The numbers of papers about both P and F, both P and C, and both F and C (all including two papers in the center) are  ,   , and  , respectively. There are two papers focus on all three directions.|
|---|

|[Figure 4]<br><br>FIGURE<br><br>Comparison of preprocessing methods. Blue bars denote the number of papers involving a method, and the orange bars denote modiﬁed or new methods proposed.|
|---|

apply any preprocessing step, 61.7% applied basic preprocessing such as bandpass ﬁltering, and 17.02% applied more advanced preprocessing methods such as ICA and PCA. Our study shows that since 2021, 24 (100%) and 15 (62.5%) of the studies applying hDL performed preprocessing and advanced preprocessing methods, respectively. In addition, Alzahab et al. (2021) also pointed out that since none of the papers they reviewed compared performance between the presence and the absence of preprocessing, it cannot be conﬁrmed whether preprocessing can improve accuracy.

However, we found that several papers since 2021 have conducted comparative experiments on preprocessing and have clearly concluded that appropriate preprocessing methods can improve accuracy performance. For example, Lashgari et al. (2021) showed that by selecting the optimal channel (ACC = 81.73%) compared to no channel (ACC = 71.47%), the accuracy of the hybrid CNN and GRU algorithm was improved by 10.26%. Therefore, it has been proved that appropriate preprocessing methods can improve the performance of the entire processing task.

In the following section, we will discuss several directions of preprocessing research, including innovative preprocessing methods, channel selection, and data augmentation (including sliding windows, segmentation and recombination, noise injection, GAN, and VAE).

 . . . Innovative preprocessing methods

The number of studies on improving classiﬁer performance through preprocessing has increased signiﬁcantly, with 60 (98.4%) of the 61 papers including preprocessing, and 35 (57.4%) of them improving performance through innovative preprocessing approaches.

Many innovative preprocessing methods are related to the structure of deep learning networks. For example, Liu and Yang (2021) and Bagchi and Bathula (2022) both transform raw signals into 3D tensors, as shown in Figure 5. The former simply represents the positions of electrodes in a matrix roughly and ﬁlls zeros for the cells without electrodes, while the latter applies Azimuthal Equidistant Projection (AEP, a method to project a globe onto a plane) to transform the distribution of 3D electrodes into a 2D heatmap image and keep the relative distance of electrodes. After AEP and interpolation, the EEG signals become a video-like stream with plenty of 2D thermodynamic images and can be analyzed by ConvTransformer, which will be discussed in Section 3.3.1.

Autoencoder can extract the features and reduce the dimension of raw EEG signals by transforming them into a small vector. In Ayoobi and Sadeghian (2022), an LSTM-AutoEncoder is trained unsupervisedly, and the latent variables are used as the input of feature extraction algorithms. This shows that AE can extract valid features and greatly reduce the size of input signals.

 . . . Selecting optimal channels

Among the 35 papers focused on preprocessing, 12 (34.3%) addressed channel selection, indicating that selecting optimal channels is a promising direction for improving classiﬁcation performance. In the study conducted by Liu and Jin (2021), channel selection using the proposed Bispectrum and Euclidean Distance-based Channel Selection (BECS) algorithm resulted in signiﬁcant improvements in classiﬁcation accuracy for 18 out of 35 subjects (paired t-test, p < 0.05). The accuracy and ITR increased by 7.38% and 18.4%, respectively. However, performance did not signiﬁcantly change for 10 subjects, and seven subjects experienced a decrease in accuracy. They also supposed that by ordering all the leads and fusing them with a fuzzy system, it is possible to automatically determine whether to select channels, thus avoiding performance degradation. Yin et al. (2021) using a voting approach to select optimal channels, which not only signiﬁcantly improved the classiﬁcation rate (p < 0.01) when compared with the traditional FBCSP algorithm, but also reduced computing complexity.

 . . . Data augmentation

In our study, we reviewed 22 studies that applied data augmentation techniques to enhance EEG signal processing. Among them, we found that 16 studies adopted innovative

data augmentation methods, which can be classiﬁed into several categories: sliding window (10 papers, 45.5%), segmentation and recombination (4 papers, 18.2%), Gaussian noise (one paper, 4.6%), GAN (4 papers, 18.2%), and VAE (one paper, 4.6%). Since a study may use multiple data augmentation methods, the total percentage exceeds 100%.

Many studies have adopted conventional data augmentation methods, including sliding windows and segmentation and recombination. For instance, Gaur et al. (2021) employed SWMode technology based on sliding window to reduce the diﬀerences among subjects, achieving superior performance compared to the best available technology in the dataset of stroke patients (ACC = 80%, p < 0.05). In another study by Lian et al. (2021), time windows were divided into 1 s to increase the number of training samples and satisfy the requirements of CNN, enhancing the stability and reducing the impact of individual diﬀerences (kappa = 0.78). Similarly, in a study by Islam et al. (2022), the dataset was divided into three diﬀerent short decision windows (1, 2, and 3 s). They concluded that choosing a shorter decision window can reduce computational complexity, minimize the use of additional functionality for a single decision, and make the system faster. In yet another study by Ayoobi and Sadeghian (2022), the preprocessing step involved comparing fragments of various time windows, where the authors found that by clipping into short segments to match up self-attention mechanisms, the average classiﬁcation accuracy increased by 13.9%, and computation complexity was reduced.

GAN can imitate the samples in the dataset and generate new EEG samples to improve the accuracy (Lashgari et al., 2021). However, poor training stability is a problem. For example, Song et al. (2022) used Auxiliary Classiﬁer GAN (ACGAN), a variant of GAN, to generate new data to expand the training dataset, which met the requirements of deep learning and increased the accuracy by 1.7%.

Research has also explored diﬀusion models. Diﬀusion Model (DM), as an up-to-date substitute for GAN, can generate highquality images and has a wide range of applications in AI painting. Thus, it is believed that diﬀusion models can also generate verisimilar EEG signals. For example, Duan et al. (2023) used diﬀusion to remove artifacts and improve cross-subject accuracy. However, there are few papers about the diﬀusion model in EEG signal generation, and more research is needed.

However, data augmentation also has some limitations which must be considered in its application. Here we list three main factors.

First, generating too much data through data augmentation is not appropriate. Beyond a certain amount, generating more data into the training dataset only increases the training time and will not improve the generalization of the model. For example, in the study by Lashgari et al. (2021), the model achieved the best accuracy (93.6%) after applying 15 times data augmentation on BCI Competition IV dataset 2a. If 20 times augmentation is adopted, the accuracy will decline instead.

Second, a major diﬀerence between synthetic EEG signals and images is that EEG signals cannot be directly interpreted. While GANs and other deep learning-based generators have demonstrated success in synthetic image generation, it is challenging to interpret the diﬀerences between real and synthetic

|[Figure 5]<br><br>FIGURE<br><br>Two  D representation methods of EEG signals in Liu and Yang ( ) and Bagchi and Bathula ( ), respectively. Both of them are in the shapes of width × height × time samples. The ﬁgure are partly cropped and modiﬁed from these two articles.|
|---|

EEG signals. Sliding windows and noise injection methods ensure that the augmented data are similar to real EEG signals, but GANs and Variational Autoencoders (VAEs) are less transparent, resulting in a new “black box”.

Third, selecting appropriate data augmentation methods in a given situation is crucial as diﬀerent methods have both advantages and disadvantages. For example, sliding windows and segmentation and recombination can directly augment data in the input space, which is intuitive and has a low calculation cost (He et al., 2021). However, this method also increases the similarity of training data, which may cause overﬁtting and reduce the classiﬁcation accuracy of the model.

 . . Deep learning algorithms

As is mentioned in Section 1.3.2, CNN can extract temporal and spatial kernels by setting diﬀerent sizes of kernels, and RNN can extract long-term temporal kernels. In our study, we ﬁnd that most of the papers about DL use CNN alone or with other structures to extract features and use FC as the last layer to sort extracted features into given categories. Some papers also add an RNN layer after CNN. Also, batch normalization (BN) and dropout layers are applied widely to avoid overﬁtting.

Among the papers reviewed in our study, 28 studies used DL algorithms, with the majority relying on CNNs (26 papers, 92.9%), followed by RNNs (eight papers, 28.6%) and MLP (one paper, 3.6%). Most of the CNN and RNN algorithms proposed

innovative methods. Notably, since 2021, CNN-based algorithms have accounted for 42.6% of the 61 reviewed papers, indicating that CNN is the mainstream classiﬁcation and DL approach for EEG signal processing. Out of the 28 DL papers reviewed, 20 studies used time-domain signals as input, while six studies used time-frequency domain signals. The number of diﬀerent methods or structures is depicted in Figure 6. As some studies used multiple methods, the sum of each sector may exceed the total number.

Our research indicates that the prevalence of DL and the popularity of CNNs as a classiﬁcation algorithm can be attributed to three factors:

- 1. DL can be applied to not only the spatial and time domains but also the frequency and time-frequency domains. CNNs are predominantly used to extract spatial features, while RNNs can extract longer temporal features than CNNs.
- 2. Classiﬁcation accuracy is highly dependent on the amount of training data, and limited training data often leads to low accuracy. Data augmentation and transfer learning have partially resolved this issue in recent years. Data augmentation expands the amount of data by applying various preprocessing techniques, while transfer learning leverages knowledge and experience from other ﬁelds to train a model with a smaller dataset. Transfer learning shortens the training time and is less aﬀected by individual diﬀerences.
- 3. DL algorithms reduce the computational burden and enhance BCI performance by sharing parameters or constructing a shallow neural network that is consistent with the characteristics of EEG.

|[Figure 6]<br><br>FIGURE<br><br>The number of di erent deep learning methods used in reviewed papers. The orange sector represents MLP, with one paper. Special CNN includes graph CNN, etc.|
|---|

 . . . Application and innovation in CNN

CNNs are capable of extracting both spatial and short-term temporal features using 1 × M and N × 1 kernels, respectively, when the input has the shape C × T. Research on CNNs can be classiﬁed into three categories: (1) improving proposed networks, (2) modifying networks from other domains, and (3) proposing innovative network structures.

First, to improve proposed networks. As mentioned in Section 1.3.2, EEGNet is a network designed speciﬁcally according to the characteristics of EEG signals (Lawhern et al., 2018). Various modiﬁcations have been made to EEGNet to improve performance. For example, Li H. et al. (2022) added an FC layer to concatenate the output of three convolution layers to aggregate diﬀerent features and improve the accuracy of EEGNet. Vega et al. (2021) added a Fuzzy Neural Block (FNB) after EEGNet and demonstrated that FNB can slightly enhance the accuracy of subject-dependent classiﬁcation.

Second, to adapt the networks from other realms. Researchers have applied innovative structures from the ﬁelds of imaging processing and computer vision to EEG signal processing. For instance, Bagchi and Bathula (2022) modiﬁed the ConvTransformer network, originally designed for video processing, to process EEG signals and achieve the highest accuracy among several methods. Here, the raw EEG signals

are preprocessed into a video-like stream, which serves as the input of ConvTransformer, similar to the approach used in video processing. However, the ConvTransformer model has a large computational complexity due to a large number of parameters. In addition, Lin et al. (2022) inserted the Spatial Attention Mechanism (SAM) from the ﬁeld of imaging processing into their network to extract the salient frequency of EEG signals.

Third, to propose an innovative network structure. Compared to traditional 2D-CNN, various methods of deep learning have been developed. Mattioli et al. (2022) proposed a 1D CNN, a special convolutional layer that accepts input of shape T × C and uses Q × C-shaped kernels to process the input, thereby squeezing the second dimension and outputting a tensor of shape T ×O, where O is the number of output channels. Multi 1D CNNs were constructed sequentially, which reduces computational cost while achieving high accuracy. Lashgari et al. (2021) proposed a relatively simple network that uses a shared-parameter convolutional layer as sliding windows to process signals without any conventional preprocessing methods. They then employ CNN and self-attention mechanisms to extract features and an FC layer for classiﬁcation. The network achieved the highest accuracy compared to other state-of-the-art networks, mainly because it abandoned prior methods such as preprocessing and manual hyperparameter selection, allowing all parameters to be trained and updated automatically.

There are also deep learning studies focusing on particular applications of EEG-BCI. For instance, aiming to develop a BCI for people with communication disabilities to control the movement of a device, Vorontsova et al. (2021) designed a simple network using ResNet and GRU but without the last FC layer to classify the EEG signals into correct words during silent speech. They hypothesized that a smaller dataset on one subject (i.e., subjectdependent dataset) will contribute to higher accuracy, which was demonstrated by their experiment results. Similarly, Vega et al. (2021) applied P300-based EEG signals on controlling smart appliances. They collected EEG signals from both healthy and poststroke subjects and designed the aforementioned EEGNet with FNB to classify these data. The performance of these applications has shown the eﬀectiveness and prospect of deep learning-based EEG signal processing methods and the possibility of real-life BCI devices.

 . . . Multi-network structure fusion

There exist various neural networks and structures, such as CNN, RNN, attention mechanisms, and AutoEncoder (EncoderDecoder) structures, each with diﬀerent performance in various application scenarios. The fusion of multiple structures can improve classiﬁcation accuracy by combining diﬀerent features (Singh et al., 2021). It has been observed that many studies apply dropout, BN, and attention mechanisms to deep learning algorithms. Among the 28 papers surveyed, 11 (39.3%) used dropout, 11 (39.3%) used BN, and 7 (25%) used attention mechanisms.

Lin et al. (2022) proposed Phase Learning and Frequency Attention Network (PLFA-Net), which combines a phase-learning module, SAM, feature-extracting CNN, and a fully connected layer. The phase-learning module calculates the linear combination of the real and imaginary parts of FFT outputs to learn phase information. The SAM extracts frequency features as mentioned above. The feature-extracting CNN, a conventional convolutional layer, extracts features of both time and channels. PLFA-Net performs better than CCA in high frequency but worse in low frequency, probably because it extracts low-amplitude information of high frequency well but is aﬀected by low-frequency noise.

Lian et al. (2021) combined a Shallow CNN (SCNN), BiLSTM, and attention mechanisms to improve EEG classiﬁcation. The design of SCNN is inspired by Visual Geometry Group (VGG), but SCNN uses rectangular kernels with shapes of 1 × 5 and 1 × 3 instead of square kernels to extract temporal features. Attention mechanisms are used after BiLSTM to fuse the features of SCNN and BiLSTM.

Li and Sun (2022) used modiﬁed EEGNet and ConvLSTM to process EEG signals. ConvLSTM uses convolution operations to pass the hidden state, combining both RNN and CNN. Attention mechanisms are also adopted before the input of ConvLSTM. This model achieved better results on several datasets.

 . . . Problems and future directions of deep learning

Although deep learning has been shown to be eﬀective in processing EEG signals, several notable problems still exist, which

also serve as future directions for research in EEG signal processing with deep learning. In the following sections, we highlight some of these issues and provide potential avenues for addressing them.

The ﬁrst problem is related to the shape of the input. While CNNs typically accept 2D images or 3D multi-channel images as input, EEG signals are multi-channel 1D sequences with a shape of C × T. Directly using a 2D C × T matrix as input can lead to insuﬃcient feature extraction during convolutional operations due to the electrodes being adjacent to four surrounding electrodes on a 3D sphere, as opposed to only two adjacent electrodes in the matrix. Figure 7 illustrates this issue. Some researchers ignore the input shape and properties of CNNs, using inappropriate inputs and conventional 2D convolutional layers, which can result in poor correlation extraction. For example, in Islam et al. (2022), after applying wavelet transform as a feature extraction step, the spectrograms of all channels are concatenated into a large 2D image, which may extract redundant features due to the lack of apparent relations between the border of the image. To overcome these issues, researchers have proposed innovative solutions such as considering each channel as an independent sample, transforming the signals into 3D tensors to preserve the relative positions of electrodes (Liu and Yang, 2021; Bagchi and Bathula, 2022), or using a C × 1 kernel for depthwise convolutional layers in models such as EEGNet (Lawhern et al., 2018) and EEG-TCFNet (Vega et al., 2021). In the future, further attention is needed in designing CNN structures that can accommodate the shape and characteristics of EEG signals to eﬀectively extract features.

Another problem concerns the accuracy of cross-subject tasks, where many studies have shown high accuracy in within-subject tasks but lower accuracy in cross-subject tasks. For instance, in the study of Mattioli et al. (2022), the accuracy drops sharply from 99% in within-subject tasks to approximately 50% when applying transfer learning to other subjects, indicating that the parameters overﬁt the given individuals and cannot be generalized easily to new individuals. This issue presents a bottleneck for EEG applications and BCI technology, where a universal classiﬁer for all participants is yet to be designed. In fact, Singh et al. (2021) have summarized some methods to improve subject-independent accuracy, but most of them are non-deep learning methods or fusions of non-DL and DL methods. Further research on deep learning-based EEG signal processing to address this problem and improve cross-subject accuracy is still needed.

The balance between accuracy and time cost is another challenge that requires consideration in many cases. Deeper and more complex networks often lead to higher accuracy but also longer computing time, which can be problematic in real-time EEG-based applications like BCI for controlling devices. Some studies, such as the study of Bagchi and Bathula (2022), pursue higher accuracy but achieve it with a large number of parameters and high time cost. On the other hand, some studies have used special structures like separable convolutional layers, which can maintain high accuracy without signiﬁcantly increasing computing time. In the future, achieving a balance between accuracy and computing time will remain an important consideration.

Finally, the lack of interpretability in both EEG and deep learning hinders further development. As the functions of our brains are still not fully understood, interpreting EEG signals

|[Figure 7]<br><br>FIGURE<br><br>If  D electrodes (A) are squeezed into a  D channel arrangement (B), the spatial relationship of electrodes is lost. An m × n CNN kernel cannot extract the information fully, since it only extracts n channels every time. For EEGNet (C), a C × kernel is used to extract the features from all channels. (A)  D sphere of collecting device. (B)  D representation and a normal CNN kernel. (C) C × kernel of EEGNet.|
|---|

and understanding the workings of deep learning models can be challenging. Deep learning is often considered a “black box” (Adadi and Berrada, 2018), which can make it diﬃcult to explain and understand EEG DL models. Additionally, the lack of interpretability is also a factor contributing to the low crosssubject accuracy, as we do not know the speciﬁc variations in EEG signals between diﬀerent individuals. Many papers attempt to explain the reason why their networks are eﬃcient in terms of network structure, but the existing reasons are still very subjective. Furthermore, Vallabhaneni et al. (2021) stated that pathological mechanisms are more important than classiﬁcation accuracy in medical and psychological applications of EEG and BCI. But from the papers we reviewed, researchers are still mainly paying attention to high performance, or more precisely, high accuracy. Hence in medical realms, deep learning of EEG cannot still be put into practical applications, leaving a signiﬁcant unsolved problem.

 . . Fusion of di erent methods

Currently, there exist numerous classiﬁcation algorithms. However, their performance varies signiﬁcantly across diﬀerent paradigms and application scenarios. The No Free Lunch Theorem asserts that it is impossible to ﬁnd a single algorithm that generalizes well on any distribution of data (Wolpert and Macready, 1997). Additionally, many algorithms encounter challenges during processing, such as insuﬃcient feature extraction, overlooking global network characteristics, and inability to identify the physical function of the brain. Furthermore, as preprocessing methods and deep learning algorithms develop and merge, the partitions between preprocessing, feature extraction, and classiﬁcation become blurred. In the review conducted by Saeidi et al. (2021), ICA and PCA are classiﬁed into both preprocessing and feature extraction methods. In most deep learning studies, features are considered automatically extracted by

neural networks, so there is not a single step of feature extraction. Multi-algorithm fusion, as opposed to a single algorithm, can optimize feature selection, decrease computational complexity, and improve classiﬁcation accuracy (Singh et al., 2021).

Our survey reveals that 45 studies (73.8%) employed the fusion of more than two methods for feature extraction and classiﬁcation, leading to a signiﬁcant improvement in performance. Multialgorithm fusion is becoming a new trend in EEG signal processing. Additionally, 14 papers utilized the BCI Competition IV 2a dataset for their studies, as shown in Figure 8. Liu et al. (2021) utilized the fusion of LSTM and self-attention and achieved the highest accuracy (97.7%) among 14 papers.

 . . . Multi-conventional method fusion

Despite the prevalence of deep learning, many conventional feature extraction methods are still applied to EEG signals, especially in feature extraction. In practice, when choosing a variety of conventional algorithms, it is necessary to consider the inﬂuence of various factors such as the number of samples that can be obtained, training time, and test methods. Through combination, the optimal feature-extracting ability can be obtained, and the time cost of training and classiﬁcation can be saved, along with good generalization ability. Our research shows that 16 papers (26.2%) using feature extraction algorithms involve feature extraction fusion algorithms, indicating that feature extraction algorithms also have a trend of fusion development. The accuracy and accuracy increment are shown in Figure 9. Although diﬀerent benchmarks or classiﬁcation algorithms are used among diﬀerent studies, they all achieve at least 1% accuracy increments.

For example, Sun et al. (2021) proposed the Discriminative Canonical Pattern Matching (DCPM) algorithm, which integrates DSP, CCA, and pattern matching, and achieved the best performance in various situations. Compared with LDA-related algorithms, DCPM performs better when the number of training samples is small or the number of features is too large. Compared with SVM-related

|[Figure 8]<br><br>FIGURE<br><br>Accuracy comparison of di erent methods on the BCI competition IV dataset  a. Each label on the vertical axis represents a method in a study, which is from Gaur et al. ( ), Lashgari et al. ( ), Lian et al. ( ), Liu and Yang ( ), Liu et al. ( ), Qi et al. ( ), Ali et al. ( ), Ayoobi and Sadeghian ( ), Chang et al. ( ), Chen L. et al. ( ), Ko et al. ( ), Li and Sun ( ), Li H. et al. ( ), and Tang et al. ( ), from top to bottom, respectively.|
|---|

|[Figure 9]<br><br>FIGURE<br><br>The accuracy and accuracy increment of di erent fusion methods. The benchmark algorithms are often methods in previous studies or conventional algorithms like simply CSP, whose accuracy is denoted by blue bars. The innovative methods mean new methods proposed in the papers, whose accuracy increments are denoted by orange bars. Each label on the vertical axis represents a method in a study, which is from Du et al. ( ), Gao N. et al. ( ), Qi et al. ( ), Rashid et al. ( ), Wang and Quan ( ), Xu C. et al. ( ), Yin et al. ( ), Zhang Y. et al. ( ), Algarni et al. ( ), Cui et al. ( ), Jia et al. ( ), Ma et al. ( ), Pei et al. ( ), and Tang et al. ( ), from top to bottom, respectively.|
|---|

algorithms, DCPM avoids the long-term parameter selection process during use, making the application process easier.

Ma et al. (2022) proposed the CCA-CWT-SVM fusion algorithm, which combines the features extracted by CCA with CWT, to achieve feature complementarity, and

thus signiﬁcantly improves the target accuracy within a limited time.

Yin et al. (2021) proposed a channel-based optimal sparse time-frequency block common space pattern (OCSB-CSP) feature extraction method to improve model classiﬁcation accuracy and computational eﬃciency. A channel selection method based on Pearson correlation coeﬃcients is ﬁrst invoked to reduce the redundant information between channels and to mark the best channel for subsequent processing. Then, the discriminative ability of each time-frequency block is measured by deﬁning the Fisher ratio index to sparse the time-frequency blocks, which signiﬁcantly reduces the data dimensionality, and the selected time-frequency blocks are mostly distributed in the frequency bands related to the MI task. Finally, the p-shape analysis of Lasso regression is performed to select the extracted multi-block CSP features and use SVM for classiﬁcation. The results show that the proposed OCSB-CSP algorithm achieves higher classiﬁcation accuracy while reducing the computational burden of the model.

 . . . Fusion of conventional methods and deep learning

In addition to modifying deep learning algorithms as discussed in Section 3.3.1, some studies have explored the fusion of conventional methods and deep learning. In this section, we review some innovative fusions of both conventional methods and deep learning.

Islam et al. (2022) proposed a fusion of CNN and KNN. The features extracted by CNN are treated as 1D vectors in Rm and classiﬁed by KNN using Euclidean distance.

Algarni et al. (2022) proposed a fusion of Hurst index, WPD, statistical features, Binary Gray Wolf Optimization (BGWO) algorithm, and BiLSTM. Hurst index is used to measure the long-term memory changes of time series, WPD is used to better ﬁlter the discrete-time signal, and statistical features are used to analyze time-domain features. The fusion of Hurst, WPD, and statistical features is used to extract features. BGWO is applied to select features and eliminate redundant features while retaining important information. BiLSTM is then used to extract features further, and ﬁnally, an FC layer is used for classiﬁcation.

 . . . Future directions of multi-method fusion

Multi-method fusion is a promising trend in EEG signal processing. We will attempt to give some reasons why multimethod fusion is important and summarize the tendencies of multi-method fusion in this section.

First, the characteristics of the brain have not been fully explored. EEG comes from the neural activities in our brain, and the aim of EEG signal processing is to decode and obtain information from our brain. However, nowadays there are few researchers who adopt machine learning fusion focusing on the explanations of the eﬀectiveness of algorithms, as well as associating the algorithms with cognitive mechanisms. While the eﬀectiveness of fusion methods can be indirectly demonstrated through comparing performance like accuracy, what feature each method exactly

extracts, and what the neurologic meanings of features are, are not clear, so the cognitive mechanisms behind the fusion methods are not fully understood. Thus, the optimal solutions or a general explanation of algorithm selection have not been proposed (Chen J. et al., 2022).

Second, in addition to algorithm fusion, other fusion approaches such as multi-sample fusion are also worth exploring. Fan et al. (2021) used multi-sample fusion to classify EEG signals using SVM, where multiple samples from the same experimental conditions were combined to improve classiﬁcation accuracy. This signiﬁcantly improved the accuracy of SVM classiﬁcation than that of a single sample.

Third, a single feature may not eﬀectively capture the physiological behavior of the brain. Future studies may introduce more parameters to improve classiﬁcation accuracy. However, method fusion may lead to increased time and space complexity, resulting in longer training and prediction times, which limits the practical application of the model (Lu et al., 2022). Therefore, it is important to balance the parameter number and time cost to avoid overﬁtting and excessive time and space complexity. For example, in Section 3.4.2, we discussed the study of Algarni et al. (2022) that used multi-feature extraction stages and BiLSTM to reduce the dimensionality of data and improve classiﬁcation accuracy. BiLSTM reduces the high dimensionality of data, which reduces complexity and leads to less classiﬁcation time and improved performance.

In summary, multi-method fusion is a promising direction for EEG signal processing, and more research is needed to fully explore its potential. Future studies may focus on understanding the cognitive mechanisms behind the fusion methods, exploring other fusion approaches, and reducing the limitations and complexity of the model.

##  . Conclusions

In this paper, we have reviewed 61 studies of EEG signal processing. We have discussed diﬀerent preprocessing methods and highlighted the eﬀectiveness of proper preprocessing methods to increase accuracy, which solves the problems in the review of Alzahab et al. (2021). Furthermore, we have observed the wide adoption of deep learning methods in EEG signal processing and discussed some reasons why they have become prevalent. We have also noted that many studies apply multi-method fusion, using both conventional algorithms and deep learning. This summarization can show some future directions to the researchers focusing on EEG signal processing.

Despite these advancements, we still face signiﬁcant challenges in EEG-based BCI systems and EEG signal processing due to our limited understanding of the brain. The problem of low cross-subject accuracy also remains unsolved, indicating a limited generalization ability. Designing a more robust system with stronger generalization ability and less time cost remains an open question for future research.

## Author contributions

## Conﬂict of interest

CS and CM conceived the ideas and designed the study. CS collected the relevant literature and wrote the ﬁrst draft of the manuscript. CM provided writing supervision and critical revisions and ﬁnalized the manuscript. Both authors contributed to the article and approved the submitted version.

## Funding

This work was supported by the Natural Science Foundation of Shandong Province, China (Grant No. 1090413702304).

The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their aﬃliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Acknowledgments

The authors express their gratitude to the reviewers for their valuable feedback, which greatly contributed to enhancing the quality of this review paper.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fnins.2023. 1203059/full#supplementary-material

## References

Adadi, A., and Berrada, M. (2018). Peeking inside the black-box: a survey on explainable artiﬁcial intelligence (xai). IEEE Access 6, 52138–52160. doi: 10.1109/ACCESS.2018.2870052

Aellen, F. M., Goktepe-Kavis, P., Apostolopoulos, S., and Tzovara, A. (2021). Convolutional neural networks for decoding electroencephalography responses and visualizing trial by trial changes in discriminant features. J. Neurosci. Methods 364, 109367. doi: 10.1016/j.jneumeth.2021.109367

Al-Fahoum, A. S., and Al-Fraihat, A. A. (2014). Methods of eeg signal features extraction using linear analysis in frequency and time-frequency domains. ISRN Neurosci. 2014, 730218. doi: 10.1155/2014/730218

Algarni, M., Saeed, F., Al-Hadhrami, T., Ghabban, F., and Al-Sarem, M. (2022). Deep learning-based approach for emotion recognition using electroencephalography (EEG) signals using bi-directional long short-term memory (Bi-LSTM). Sensors 22, s22082976. doi: 10.3390/s22082976

Ali, O., Saif-Ur-Rehman, M., Dyck, S., Glasmachers, T., Iossiﬁdis, I., and Klaes, C. (2022). Enhancing the decoding accuracy of eeg signals by the introduction of anchored-STFT and adversarial data augmentation method. Sci. Rep. 12, 4245. doi: 10.1038/s41598-022-07992-w

Alzahab, N. A., Apollonio, L., Di Iorio, A., Alshalak, M., Iarlori, S., Ferracuti, F., et al. (2021). Hybrid deep learning (HDL)-based brain-computer interface (BCI) systems: a systematic review. Brain Sci. 11, brainsci11010075. doi: 10.3390/brainsci11010075

Asadzadeh, S., Youseﬁ Rezaii, T., Beheshti, S., and Meshgini, S. (2022). Accurate emotion recognition using bayesian model based EEG sources as dynamic graph convolutional neural network nodes. Sci. Rep. 12, 10282. doi: 10.1038/s41598-022-14217-7

Asensio-Cubero, J., Gan, J. Q., and Palaniappan, R. (2013). Multiresolution analysis over simple graphs for brain computer interfaces. J. Neural Eng. 10, e046014. doi: 10.1088/1741-2560/10/4/046014

Asheri, B., Haratian, A., Mohamadi, M., Asadi, F., Yasini, P., Zarepak, N., et al. (2021). Enhancing detection of steady-state visual evoked potentials using frequency and harmonics of that frequency in openvibe. Biomed. Eng. Adv. 2, 100022. doi: 10.1016/j.bea.2021.100022

Ashwini S. R., and Nagaraj, H. C. (2021). Classiﬁcation of EEG signal using EACA based approach at SSVEP-BCI. IAES Int. J. Artif. Intell. 10, 726. doi: 10.11591/ijai.v10.i3.pp717-726

Awais, M. A., Yusoﬀ, M. Z., Khan, D. M., Yahya, N., Kamel, N., and Ebrahim, M. (2021). Eﬀective connectivity for decoding electroencephalographic motor imagery using a probabilistic neural network. Sensors 21, s21196570. doi: 10.3390/s21196570

Ayoobi, N., and Sadeghian, E. B. (2022). “Unsupervised motor imagery saliency detection based on self-attention mechanism,” in 2022 44th Annual International

Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE), 4817–4820. doi: 10.1109/EMBC48229.2022.9871906

Azizpour, H., Razavian, A. S., Sullivan, J., Maki, A., and Carlsson, S. (2016). Factors of transferability for a generic convnet representation. IEEE Trans. Pat. Anal. Mach. Intell. 38, 1790–802. doi: 10.1109/TPAMI.2015.2500224

Bagchi, S., and Bathula, R. D. (2022). EEG-convtransformer for singletrial EEG based visual stimulus classiﬁcation. Pat. Recogn. 129, 108757. doi: 10.1016/j.patcog.2022.108757

Bashashati, A., Fatourechi, M., Ward, R. K., and Birch, G. E. (2007). A survey of signal processing algorithms in brain-computer interfaces based on electrical brain signals. J. Neural Eng. 4, R32–R57. doi: 10.1088/1741-2560/4/2/R03

Cai, Z., Guo, M., Yang, X., Chen, X., and Xu, G. (2021). Cross-subject electroencephalogram emotion recognition based on maximum classiﬁer discrepancy. J. Biomed. Eng. 38, 455–462. doi: 10.7507/1001-5515.202012027

Cano-Izquierdo, J. M., Ibarrola, J., and Almonacid, M. (2012). Improving motor imagery classiﬁcation with a new BCI design using neuro-fuzzy S-dFasArt. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 2–7. doi: 10.1109/TNSRE.2011.2169991

Chang, Z., Zhang, C., and Li, C. (2022). Motor imagery EEG classiﬁcation based on transfer learning and multi-scale convolution network. Micromachines 13, 60927. doi: 10.3390/mi13060927

Chen, J., Min, C., Wang, C., Tang, Z., Liu, Y., and Hu, X. (2022). Electroencephalograph-based emotion recognition using brain connectivity feature and domain adaptive residual convolution model. Front. Neurosci. 16, 878146. doi: 10.3389/fnins.2022.878146

Chen, L., Gong, A., and Ding, P. (2022). EEG signal decoding of motor imagination based on euclidean space-weighted logistic regression transfer learning. J. Nanjing Univ. 58, 264–274. doi: 10.13232/j.cnki.jnju.2022.02.010

Chen, Z., and Xie, K. (2019). A Review of EEG-Based Analysis and Classiﬁcation Methods.

Cona, F., Zavaglia, M., Astolﬁ, L., Babiloni, F., and Ursino, M. (2009). Changes in EEG power spectral density and cortical connectivity in healthy and tetraplegic patients during a motor imagery task. Comput. Intell. Neurosci. 2009, 279515. doi: 10.1155/2009/279515

Cui, Y., Xie, S., Xie, X., Duan, X., and Gao, C. (2022). A spatial-temporal hybrid feature extraction method for rapid serial visual presentation of electroencephalogram signals. Chin. J. Biomed. Eng. 39, 39–46. doi: 10.7507/1001-5515.202104049

Dagdevir, E., and Tokmakci, M. (2021). Optimization of preprocessing stage in EEG based BCI systems in terms of accuracy and timing cost. Biomed. Sign. Process. Contr. 67, 102548. doi: 10.1016/j.bspc.2021.102548

De Venuto, D., and Mezzina, G. (2021). A single-trial p300 detector based on symbolized EEG and autoencoded-(1D)CNN to improve ITR performance in BCIs.

- Sensors 21, s21123961. doi: 10.3390/s21123961

Delorme, A., and Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. J. Neurosci. Methods 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

Du, Y., Liu, Z., and Fu, Z. (2021). Motion imagery classiﬁcation algorithm research based on hybrid transfer learning and application in brain-computer interface. Acta Metrol. Sin. 45, 629–637. doi: 10.3969/j.issn.1000-1158.2021.05.14

Duan, Y., Zhou, J., Wang, Z., Chang, Y.-C., Wang, Y.-K., and Lin, C.-T. (2023). Domain-speciﬁc denoising diﬀusion probabilistic models for brain dynamics. arXiv [Preprint]. arXiv: 2305.04200. Available online at: https://arxiv.org/pdf/2305.04200.pdf

El-Kafrawy, N. M., Hegazy, D., and Tolba, M. F. (2014). “Features extraction and classiﬁcation of EEG signals using empirical mode decomposition and support vector machine,” in Advanced Machine Learning Technologies and Applications, eds A. E. Hassanien, M. F. Tolba, and A. Taher Azar (Cham: Springer International Publishing), 189–198.

Fan, C., Hu, J., Huang, S., Peng, Y., and Kwong, S. (2022). EEGTNET: an end-to-end brain computer interface framework for mental workload estimation. Front. Neurosci. 16, 869522. doi: 10.3389/fnins.2022. 869522

Fan, W., Luo, S., Deng, Y., and li, Y. (2021). Support vector machine algorithm with multi-sample fusion for p300 signal classiﬁcation. J. Wuhan Inst. Technol. 43, 670–674. doi: 10.19843/j.cnki.CN42-1779/TQ.202101006

Ferracuti, F., Iarlori, S., Mansour, Z., Monteriu, A., and Porcaro, C. (2021). Comparing between diﬀerent sets of preprocessing, classiﬁers, and channels selection techniques to optimise motor imagery pattern classiﬁcation system from EEG pattern recognition. Brain Sci. 12, 10057. doi: 10.3390/brainsci120 10057

Gao, N., Gao, Z., and Zhang, H. (2021). Riemannian approach research for the feature extraction and classiﬁcation of motor imagery electroencephalogram (EEG) signals. J. Biomed. Eng. Res. 40, 246–251. doi: 10.19529/j.cnki.1672-6278.2021. 03.04

Gao, Z., Dang, W., Liu, M., Guo, W., Ma, K., and Chen, G. R. (2021). Classiﬁcation of EEG signals on VEP-based bci systems with broad learning. IEEE Trans. Syst. Man Cybernet. 51, 7143–7151. doi: 10.1109/tsmc.2020.2964684

Gaur, P., Gupta, H., Chowdhury, A., McCreadie, K., Pachori, R., and Wang, H. (2021). A sliding window common spatial pattern for enhancing motor imagery classiﬁcation in EEG-BCI. IEEE Trans. Instrument. Measur. 70, 1–9. doi: 10.1109/TIM.2021.3051996

Geng, X., Li, D., Chen, H., Yu, P., Yan, H., and Yue, M. (2022). An improved feature extraction algorithms of EEG signals based on motor imagery brain-computer interface. Alexandria Eng. J. 61, 4807–4820. doi: 10.1016/j.aej.2021.10.034

Hamedi, M., Salleh Sh, H., and Noor, A. M. (2016). Electroencephalographic motor imagery brain connectivity analysis for BCI: a review. Neural Comput. 28, 999–1041. doi: 10.1162/NECO_a_00838

He, C., Liu, J., Zhu, Y., and Du, W. (2021). Data augmentation for deep neural networks model in EEG classiﬁcation task: a review. Front. Hum. Neurosci. 15, 765525.

- doi: 10.3389/fnhum.2021.765525

He, K., Zhang, X., and Ren, S. (2016). “Deep residual learning for image recognition,” in Proceedings of 2016 IEEE Conference on Computer Vision and Pattern Recognition (Las Vegas, NV), 770–778.

Islam, M. N., Sulaiman, N., Bari, B. S., Rashid, M., and Mustafa, M. (2022). A hybrid scheme for AEP based hearing deﬁciency diagnosis: CWT and convoluted K-nearest neighbour (CKNN) pipeline. Neurosci. Informat. 2, 100037. doi: 10.1016/j.neuri.2021.100037

Jeong, J. H., Shim, K. H., Kim, D. J., and Lee, S. W. (2020). Brain-controlled robotic arm system based on multi-directional CNN-BiLSTM network using EEG signals. IEEE Trans. Neural Syst. Rehabil. Eng. 28, 1226–1238. doi: 10.1109/TNSRE.2020.2981659

Jia, T., Dong, C., and Ma, S. (2022). Brain-computer interface of motor imaging based on mutual information feature extraction. Chin. J. Med. Phys. 39, 63–68. doi: 10.3969/j.issn.1005-202X.2022.01.011

Kim, C., Sun, J., Liu, D., Wang, Q., and Paek, S. (2018). An eﬀective feature extraction method by power spectral density of EEG signal for 2-class motor imagerybased BCI. Med. Biol. Eng. Comput. 56, 1645–1658. doi: 10.1007/s11517-017-1761-4

Kim, S., Shin, D. Y., Kim, T., Lee, S., Hyun, J. K., and Park, S. M. (2022). Enhanced recognition of amputated wrist and hand movements by deep learning method using multimodal fusion of electromyography and electroencephalography.

- Sensors 22, s22020680. doi: 10.3390/s22020680

Ko, W., Jeon, E., Yoon, J. S., and Suk, H. I. (2022). Semi-supervised generative and discriminative adversarial learning for motor imagery-based brain-computer interface. Sci. Rep. 12, 4587. doi: 10.1038/s41598-022-08490-9

Kumar, J. S., and Bhuvaneswari, P. (2012). Analysis of electroencephalography (EEG) signals and its categorization–a study. Proc. Eng. 38, 2525–2536. doi: 10.1016/j.proeng.2012.06.298

Kumar, S., Tsunoda, T., and Sharma, A. (2021). Spectra: a tool for enhanced brain wave signal recognition. BMC Bioinformat. 22(Suppl.6), 195. doi: 10.1186/s12859-021-04091-x

Lashgari, E., Liang, D., and Maoz, U. (2020). Data augmentation for deeplearning-based electroencephalography. J. Neurosci. Methods 346, 108885. doi: 10.1016/j.jneumeth.2020.108885

Lashgari, E., Ott, J., Connelly, A., Baldi, P., and Maoz, U. (2021). An end-to-end CNN with attentional mechanism applied to raw EEG in a BCI classiﬁcation task. J. Neural Eng. 18, e0460e3. doi: 10.1088/1741-2552/ac1ade

Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gordon, S. M., Hung, C. P., and Lance, B. J. (2018). EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces. J.Neural Eng. 15, e056013. doi: 10.1088/1741-2552/aace8c

Li, H., Ding, M., and Zhang, R. (2022). Motor imaginative EEG classiﬁcation algorithm based on feature fusion neural network. Chin. J. Med. Phys. 39, 69–75. doi: 10.3969/j.issn.1005-202X.2022.01.012

Li, L., and Sun, N. (2022). Attention-based DSC-ConvLSTM for multiclass motor imagery classiﬁcation. Comput. Intell. Neurosci. 2022, 8187009. doi: 10.1155/2022/8187009

Li, Q., Shi, K., Gao, N., Li, J., and Bai, O. (2018). Training set extension for SVM ensemble in p300-speller with familiar face paradigm. Technol. Health Care 26, 469–482. doi: 10.3233/THC-171074

Li, Q., Wu, Y., Song, Y., Zhao, D., Sun, M., Zhang, Z., et al. (2022). A p300detection method based on logistic regression and a convolutional neural network. Front. Comput. Neurosci. 16, 909553. doi: 10.3389/fncom.2022.909553

Lian, S., Xu, J., Zuo, G., Wei, X., and Zhou, H. (2021). A novel timeincremental end-to-end shared neural network with attention-based feature fusion for multiclass motor imagery recognition. Comput. Intell. Neurosci. 2021, 6613105. doi: 10.1155/2021/6613105

Lin, Y., Zang, B., and Guo, R. (2022). A deep learning method for SSVEP classiﬁcation based on phase and frequency characteristics. J. Electr. Inform. Technol. 44, 446–454. doi: 10.11999/JEIT210816

Liu, C., and Jin, J. (2021). Ji yu shuang pu de wen tai shi jue you fa dian wei nao ji jie kou dao lian xuan ze suan fa. Ren Gong Zhi Neng, 6:52–60. doi: 10.16453/j.cnki.ISSN2096-5036

Liu, J., Ye, F., and Xiong, H. (2021). Multi-class motor imagery EEG classiﬁcation method with high accuracy and low individual diﬀerences based on hybrid neural network. J. Neural Eng. 18, ac1ed0. doi: 10.1088/1741-2552/ac1ed0

Liu, T., and Yang, D. (2021). A three-branch 3D convolutional neural network for EEG-based diﬀerent hand movement stages classiﬁcation. Sci. Rep. 11, 10758. doi: 10.1038/s41598-021-89414-x

Liu, T., and Yao, D. (2006). Removal of the ocular artifacts from EEG data using a cascaded spatio-temporal processing. Comput. Methods Progr. Biomed. 83, 95–103. doi: 10.1016/j.cmpb.2006.03.009

Liu, Y., Zhang, H., Chen, M., and Zhang, L. (2016). A boosting-based spatialspectral model for stroke patients’ EEG analysis in rehabilitation training. IEEE Trans. Neural Syst. Rehabil. Eng. 24, 169–179. doi: 10.1109/TNSRE.2015.2466079

Lu, R., Zeng, Y., Zhang, R., Yan, B., and Tong, L. (2022). SAST-GCN: segmentation adaptive spatial temporal-graph convolutional network for p3-based video target detection. Front. Neurosci., 16, 913027. doi: 10.3389/fnins.2022.913027

Luo, T. J., Zhou, C. L., and Chao, F. (2018). Exploring spatial-frequency-sequential relationships for motor imagery classiﬁcation with recurrent neural network. BMC Bioinformat. 19, 344. doi: 10.1186/s12859-018-2365-1

Ma, P., Dong, C., Lin, R., Ma, S., Jia, T., Chen, X., et al. (2022). A classiﬁcation algorithm of an SSVEP brain-computer interface based on cca fusion wavelet coeﬃcients. J. Neurosci. Methods 371, 109502. doi: 10.1016/j.jneumeth.2022.109502

Mane, R., Robinson, N., Vinod, A. P., Lee, S. W., and Guan, C. (2020). A multi-view CNN with novel variance layer for motor imagery brain computer interface. Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. 2020, 2950–2953. doi: 10.1109/EMBC44109.2020.9175874

Maruyama, Y., Ogata, Y., Martinez-Tejada, L. A., Koike, Y., and Yoshimura, N.

(2020). Independent components of EEG activity correlating with emotional state. Brain Sci. 10, brainsci10100669. doi: 10.3390/brainsci10100669

Mattioli, F., Porcaro, C., and Baldassarre, G. (2022). A 1D CNN for high accuracy classiﬁcation and transfer learning in motor imagery EEG-based brain-computer interface. J. Neural Eng. 18, doi: 10.1088/1741-2552/ac4430

Meng, M., Dong, Z., and Gao, Y. (2022). Correlation and sparse representation based channel selection of motor imagery electroencephalogram. J. Electr. Inform. Technol. 44, 477–485. doi: 10.11999/JEIT210778

Michel, C. M., and Murray, M. M. (2012). Towards the utilization of EEG as a brain imaging tool. NeuroImage 61, 371–385. doi: 10.1016/j.neuroimage.2011.12.039

Nakagome, S., Luu, T. P., He, Y., Ravindran, A. S., and Contreras-Vidal, J. L. (2020). An empirical comparison of neural networks and machine learning algorithms for EEG gait decoding. Sci. Rep. 10, 4372. doi: 10.1038/s41598-020-60932-4

Okafor, E., Smit, R., Schomaker, L., and Wiering, M. (2017). “Operational data augmentation in classifying single aerial images of animals,” in 2017 IEEE International Conference on INnovations in Intelligent SysTems and Applications (INISTA) (Gdynia), p. 354–360. doi: 10.1109/INISTA.2017.8001185

Park, S. H., Lee, D., and Lee, S. G. (2018). Filter bank regularized common spatial pattern ensemble for small sample motor imagery classiﬁcation. IEEE Trans. Neural Syst. Rehabil. Eng. 26, 498–505. doi: 10.1109/TNSRE.2017.2757519

Pei, Y., Luo, Z., Zhao, H., Xu, D., Li, W., Yan, Y., et al. (2022). A tensor-based frequency features combination method for brain-computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 30, 465–475. doi: 10.1109/TNSRE.2021.3125386

Qi, F., Wang, W., Xie, X., Gu, Z., Yu, Z. L., Wang, F., et al. (2021). Single-trial EEG classiﬁcation via orthogonal wavelet decomposition-based feature extraction. Front. Neurosci. 15, 715855. doi: 10.3389/fnins.2021.715855

Rashid, M., Bari, B. S., Hasan, M. J., Razman, M. A. M., Musa, R. M., Ab Nasir, A. F., et al. (2021). The classiﬁcation of motor imagery response: an accuracy enhancement through the ensemble of random subspace K-NN. PeerJ Comput. Sci. 7, e374. doi: 10.7717/peerj-cs.374

Saeidi, M., Karwowski, W., Farahani, F. V., Fiok, K., Taiar, R., Hancock, P. A., et al. (2021). Neural decoding of EEG signals with machine learning: a systematic review. Brain Sci. 11, brainsci11111525. doi: 10.3390/brainsci11111525

Sanei, S., and Chambers, J. A. (2021). EEG Signal Processing and Machine Learning. Hoboken, NJ: John Wiley & Sons.

Singh, A., Hussain, A. A., Lal, S., and Guesgen, H. W. (2021). A comprehensive review on critical issues and possible solutions of motor imagery based electroencephalography brain-computer interface. Sensors 21, s21062173.

- doi: 10.3390/s21062173

Song, C., Sheng, Y., and Ning, Z. (2022). Deep learning-based method for recognition of motion imagery EEG signal. Transducer Microsyst. Technol. 41, 125–133. doi: 10.13873/J.1000-9787(2022)04-0125-04

Suhaimi, N. S., Mountstephens, J., and Teo, J. (2022). A dataset for emotion recognition using virtual reality and EEG (DER-VREEG): Emotional state classiﬁcation using low-cost wearable VR-EEG headsets. Big Data Cogn. Comput. 6, bdcc6010016. doi: 10.3390/bdcc6010016

Sun, J., Jung, T. P., Xiao, X., Meng, J., Xu, M., and Ming, D. (2021). Classiﬁcation algorithms of error-related potentials in brain-computer interface. Sheng Wu Yi Xue Gong Cheng Xue Za Zhi 38, 463–472. doi: 10.7507/1001-5515.202012013

- Tang, X., Wang, T., Du, Y., and Dai, Y. (2019). Motor imagery EEG recognition with KNN-based smooth auto-encoder. Artif. Intell. Med. 101, 101747. doi: 10.1016/j.artmed.2019.101747
- Tang, Y., Zhao, Z., Zhang, S., Li, Z., Mo, Y., Guo, Y., et al. (2022). Motor imagery EEG decoding based on new spatial-frequency feature and hybrid feature selection method. Math. Probl. Eng. 2022, 1–12. doi: 10.1155/2022/2856818

Torres, P. E., Torres, E. A., Hernandez-Alvarez, M., and Yoo, S. G.

(2020). EEG-based BCI emotion recognition: a survey. Sensors 20, s20185083. doi: 10.3390/s20185083

Vallabhaneni, R. B., Sharma, P., Kumar, V., Kulshreshtha, V., Reddy, K. J., Kumar, S. S., et al. (2021). Deep learning algorithms in EEG signal decoding application: a review. IEEE Access 9, 125778–125786. doi: 10.1109/ACCESS.2021.3105917

Varsehi, H., and Firoozabadi, S. M. P. (2021). An EEG channel selection method for motor imagery based brain-computer interface and neurofeedback using granger causality. Neural Netw. 133, 193–206. doi: 10.1016/j.neunet.2020.11.002

Vega, C. F., Quevedo, J., Escandon, E., Kianic, M., Dingd, W., and AndreuPerez, J. (2021). Fuzzy temporal convolutional neural networks in p300-based braincomputer interface for smart home interaction. Appl. Soft Comput. 117, 108359. doi: 10.1016/j.asoc.2021.108359

Vidaurre, C., Kawanabe, M., von Bunau, P., Blankertz, B., and Muller, K. R. (2011). Toward unsupervised adaptation of LDA for brain-computer interfaces. IEEE Trans. Biomed. Eng. 58, 587–97. doi: 10.1109/TBME.2010.2093133

Vorontsova, D., Menshikov, I., Zubov, A., Orlov, K., Rikunov, P., Zvereva, E., et al. (2021). Silent EEG-speech recognition using convolutional and recurrent neural network with 85% accuracy of 9 words classiﬁcation. Sensors 21, s21206744. doi: 10.3390/s21206744

Wahid, M. F., and Tafreshi, R. (2021). Improved motor imagery classiﬁcation using regularized common spatial pattern with majority voting strategy. IFAC-PapersOnLine 54, 226–231. doi: 10.1016/j.ifacol.2021.11.179

- Wang, P., Jiang, A., Liu, X., Shang, J., and Zhang, L. (2018).

LSTM-based EEG classiﬁcation in motor imagery tasks. IEEE Trans. Neural Syst. Rehabil. Eng. 26, 2086–2095. doi: 10.1109/TNSRE.2018. 2876129

- Wang, Q., and Quan, H. (2021). Research on the classiﬁcation of motor imagery

EEG by optimized svm based surface-simplex swarm evolution. J. Electr. Measur. Instrument. 35, 157–163. doi: 10.13382/j.jemi.B2103989

Wolpaw, J. R., Birbaumer, N., Heetderks, W. J., McFarland, D. J., Peckham, P. H., Schalk, G., et al. (2000). Brain-computer interface technology: a review of the ﬁrst international meeting. IEEE Trans. Rehabil. Eng. 8, 164–173. doi: 10.1109/tre.2000.847807

Wolpaw, J. R., McFarland, D. J., Vaughan, T. M., and Schalk, G. (2003). The wadsworth center brain-computer interface (BCI) research and development program. IEEE Trans. Neural. Syst. Rehabil. Eng. 11, 204–7. doi: 10.1109/TNSRE.2003. 814442

Wolpert, D. H., and Macready, W. G. (1997). No free lunch theorems for optimization. IEEE Trans. Evolution. Comput. 1, 67–82.

Xu, C., Zhang, H., and Sun, L. (2021). Prediction of hand grip motion intention based on sample entropy and time-frequency analysis. J. Zhejiang Univ. 55, 2315–2322. doi: 10.3785/j.issn.1008-973X.2021.12.011

Xu, F., Miao, Y., Sun, Y., Guo, D., Xu, J., Wang, Y., et al. (2021). A transfer learning framework based on motor imagery rehabilitation for stroke. Sci. Rep. 11, 19783.

- doi: 10.1038/s41598-021-99114-1

Xu, M., Wang, D., Li, Z., and Chen, Y. (2022). Incepa-eegnet: p300 signal detection method based on fusion of inception network and attention mechanism. J. Zhejiang Univ. 56, 745–753. doi: 10.3785/j.issn.1008-973X.2022.04.014

Yin, X., Meng, M., She, Q., Gao, Y., and Luo, Z. (2021). Optimal channelbased sparse time-frequency blocks common spatial pattern feature extraction method for motor imagery classiﬁcation. Math. Biosci. Eng. 18, 4247–4263. doi: 10.3934/mbe.2021213

Ying, J., Wei, Q., and Zhou, X. (2022). Riemannian geometry-based transfer learning for reducing training time in C-VEP BCIs. Sci. Rep. 12, 9818.

- doi: 10.1038/s41598-022-14026-y

Zhang, A., Lipton, Z. C., Li, M., and Smola, A. J. (2021). Dive into deep learning. arXiv [Preprint]. arXiv: 2106.11342. Available online at: https://arxiv.org/pdf/2106. 11342.pdf

Zhang, K., Xu, G., Du, C., Wu, Y., Zheng, X., Zhang, S., et al. (2021). Weak feature extraction and strong noise suppression for SSVEP-EEG based on chaotic detection technology. IEEE Trans. Neural Syst. Rehabil. Eng. 29, 862–871. doi: 10.1109/TNSRE.2021.3073918

Zhang, K., Xu, G., Zheng, X., Li, H., Zhang, S., Yu, Y., et al. (2020). Application of transfer learning in EEG decoding based on brain-computer interfaces: a review. Sensors 20, 6321. doi: 10.3390/s20216321

Zhang, Y., Liao, Y., Zhang, Y., and Huang, L. (2021). Emergency braking intention detect system based on K-order propagation number algorithm: a network perspective. Brain Sci. 11, brainsci11111424. doi: 10.3390/brainsci 11111424

Zhao, X., Jin, J., Xu, R., Li, S., Sun, H., Wang, X., et al. (2022). A regional smoothing block sparse bayesian learning method with temporal correlation for channel selection in p300 speller. Front. Hum. Neurosci. 16, 875851. doi: 10.3389/fnhum.2022. 875851

