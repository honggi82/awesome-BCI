# arXiv:2408.12124v1[cs.LG]22Aug2024

Recording Brain Activity While Listening to Music Using Wearable EEG Devices Combined with Bidirectional Long Short-Term Memory Networks

Jingyi Wanga,∗, Zhiqun Wangb and Guiran Liuc

aSchool of Music, Jiangxi Normal University, 330027, Nanchang, China bSchool of Electronic Information, HuZhou College, 313000, HuZhou, China cSan Francisco State University, 94132, San Francisco, United Stated

#### ARTICLE INFO

#### ABSTRACT

Keywords: EEG signal processing Bi-LSTM Attention mechanisms Emotion recognition Wearable EEG devices

Electroencephalography (EEG) signals are crucial for investigating brain function and cognitive processes. This study aims to address the challenges of efficiently recording and analyzing highdimensional EEG signals while listening to music to recognize emotional states. We propose a method combining Bidirectional Long Short-Term Memory (Bi-LSTM) networks with attention mechanisms for EEG signal processing. Using wearable EEG devices, we collected brain activity data from participants listening to music. The data was preprocessed, segmented, and Differential Entropy (DE) features were extracted. We then constructed and trained a Bi-LSTM model to enhance key feature extraction and improve emotion recognition accuracy. Experiments were conducted on the SEED and DEAP datasets. The Bi-LSTM-AttGW model achieved 98.28% accuracy on the SEED dataset and 92.46% on the DEAP dataset in multi-class emotion recognition tasks, significantly outperforming traditional models such as SVM and EEG-Net. This study demonstrates the effectiveness of combining Bi-LSTM with attention mechanisms, providing robust technical support for applications in braincomputer interfaces (BCI) and affective computing. Future work will focus on improving device design, incorporating multimodal data, and further enhancing emotion recognition accuracy, aiming to achieve practical applications in real-world scenarios.

dimensionality and complexity of EEG data. By introducing a novel combination of Bi-LSTM and attention mechanisms, this research aims to overcome these challenges and provide a robust solution for real-time emotion recognition using wearable EEG devices. The significance of this study lies in its potential applications in brain-computer interfaces, music therapy, and affective computing, where accurate emotion recognition can greatly enhance user experience and therapeutic outcomes.

## 1. Introduction

The study of Electroencephalography (EEG) signals [1] has garnered significant attention in the fields of neuroscience and computer science. EEG signals, which reflect the brain’s electrophysiological activity, are crucial tools for investigating brain function and cognitive processes. The advent of deep learning and wearable technology has revolutionized the ability to record and analyze EEG signals in real-time using portable devices [2]. This advancement not only facilitates research but also expands the applications in brain-computer interfaces (BCI) and affective computing [3, 4].

Bidirectional Long Short-Term Memory (Bi-LSTM) networks [8–11], an advanced type of Recurrent Neural Network (RNN) [12–16], are well-suited for this task. Bi-LSTM networks can leverage both past and future information in time series data, making them adept at capturing long-term dependencies. Applying Bi-LSTM to EEG signal analysis enhances the modeling capabilities for complex time-series data, thereby improving the accuracy and robustness of emotion recognition [17–21]. Additionally, incorporating attention mechanisms allows Bi-LSTM to focus on critical features, further boosting model performance.

Music, as a complex auditory stimulus, profoundly influences emotional and cognitive functions of the brain [5, 6]. Research indicates that different types of music can elicit various neural responses, thereby affecting emotional states. Recording brain activity via EEG while listening to music provides deep insights into the mechanisms by which music influences emotions. This is particularly valuable for applications in music therapy and other practical uses. However, the complexity and high dimensionality of EEG signals pose challenges in efficiently extracting and analyzing useful information [7].

In this study, we utilize wearable devices to record EEG signals from participants while they listen to music. We then analyze these signals using a Bi-LSTM model to explore the impact of music on brain activity. The process involves low-pass filtering of EEG signals, feature extraction and selection, and the construction and training of the Bi-LSTM model. Our goal is to achieve efficient recording and precise prediction of brain activity. The results of this study will not only enhance the accuracy of emotion recognition but

This study addresses the critical need for advanced methods in EEG signal processing to enhance emotion recognition accuracy. Existing methods often struggle with the high

∗Corresponding author.

xiabin126@126.com (J. Wang); hgzhou2020@163.com (Z. Wang); gliu@sfsu.edu (G. Liu)

[Figure 1]

also provide substantial support for applications in BCI and affective computing.

This study addresses the critical need for advanced methods in EEG signal processing to enhance emotion recognition accuracy. Existing methods often struggle with the high dimensionality and complexity of EEG data. By introducing a novel combination of Bi-LSTM and attention mechanisms, this research aims to overcome these challenges and provide a robust solution for real-time emotion recognition using wearable EEG devices. The significance of this study lies in its potential applications in brain-computer interfaces, music therapy, and affective computing, where accurate emotion recognition can greatly enhance user experience and therapeutic outcomes.

The main contributions of our work are as follows:

∙ We propose a novel EEG signal processing method using Bi-LSTM and attention mechanisms, significantly enhancing emotion recognition accuracy.

∙ Our method enables real-time brain activity recording and analysis under music stimulation using portable EEG devices.

∙ The effectiveness of our model is validated on SEED and DEAP datasets, achieving a high accuracy of 98.28% in emotion recognition.

The remainder of this paper is structured as follows. Section 2 reviews related work on wearable EEG signal monitoring devices, EEG recording and MRI neuroimaging, applications of recurrent neural networks in EEG analysis, and auditory neural stimulation on the brain. Section 3 describes the proposed method, including EEG feature extraction, the construction of a 3D adjacency matrix of graph convolutional neural networks, and the Bi-LSTM model for EEG signal recognition. Section 4 presents relevant experimental results and analysis on the SEED and DEAP datasets. Finally, Section 5 concludes the paper with a summary and future research directions.

## 2. Related Work

### 2.1. Wearable EEG Signal Monitoring Devices

Wearable EEG signal monitoring devices have gained widespread application in neuroscience, psychology, and biomedical engineering [22, 23]. Their portability and ease of use make them essential tools in various domains, including affective computing, BCI, sleep management, emotion regulation, depression treatment, and fatigue monitoring. These devices, such as the Emotiv EPOC+ and Muse [24], enable real-time recording and analysis of an individual’s emotional state by capturing EEG signals and identifying emotional changes, facilitating emotion regulation and psychological therapy [25]. In BCI technology, EEG devices decode brain signals to help users control external devices, such as enabling individuals with disabilities to operate wheelchairs. In sleep management, these devices analyze brain activity during sleep, providing feedback on sleep

quality and promoting better sleep habits. They also aid in the long-term monitoring of emotional changes for diagnosing and treating emotional disorders, and in fatigue monitoring by providing real-time alerts during work or driving to prevent accidents.

Wearable EEG devices offer numerous advantages. Their portability and ease of use make them suitable for long-term wear and operation, meeting various application scenarios [26]. These devices provide real-time monitoring of brain signals, offering immediate feedback and monitoring results. Advanced devices like Mindeep support multiple electrode types, feature long battery life, impedance detection, and WiFi wireless transmission, and can provide high-quality raw data and multi-device synchronous data collection. However, these devices also have limitations. Despite offering higher sampling rates and data quality, many commercial devices still face constraints in sampling rate, signal resolution, and noise control. EEG signals are susceptible to artifacts from eye movements and muscle activity, necessitating complex preprocessing and signal processing algorithms, increasing data analysis complexity [27–31]. High-end devices are expensive, and cost considerations remain a factor for average users and some research institutions. Additionally, dry electrode devices may face issues with electrode contact and signal distortion, affecting data accuracy and stability [32, 33].

Using these devices, researchers can efficiently record real-time brain activity data from participants while they listen to music, allowing for accurate analysis and prediction of brain responses to musical stimuli. Bi-LSTM models [34– 38] capture long-term dependencies in EEG signals and, combined with attention mechanisms, improve the extraction of key features. This method not only enhances the accuracy of emotion recognition but also provides robust technical support for BCI and affective computing applications. Future improvements in hardware design and signal processing algorithms can address current device limitations, further enhancing EEG signal processing efficiency and accuracy, offering broader applications in neuroscience research and healthcare.

### 2.2. EEG Recording and MRI Neuroimaging

Electroencephalography (EEG) and magnetic resonance imaging (MRI) are pivotal in neuroscience and biomedical engineering, each offering unique advantages [39]. EEG involves placing electrodes on the scalp to capture the brain’s electrical activity in real-time, boasting high temporal resolution. It is extensively used in affective computing, BCI, and cognitive neuroscience. Functional MRI (fMRI) [40], which measures blood oxygen level-dependent (BOLD) signals [41], provides high spatial resolution images of brain structure and function, making it invaluable for brain function localization, disease diagnosis, and cognitive research. Combining these techniques allows for multi-faceted brain activity analysis; for example, EEG can monitor real-time emotional changes while fMRI can precisely locate emotionrelated brain activity.

Each method has distinct advantages and limitations. EEG’s high temporal resolution enables millisecond-level recording of brain activity, ideal for studying rapid neural processes. Its portability and non-invasiveness make longterm monitoring and convenient operation possible, especially with wearable devices. The relatively low cost of EEG equipment makes it suitable for large-scale and daily monitoring. However, EEG’s low spatial resolution limits its ability to reflect deep brain activity, and EEG signals are prone to artifacts, requiring complex preprocessing and signal processing algorithms. On the other hand, MRI’s high spatial resolution provides detailed images of brain structures and functions. Its multi-modal imaging capabilities, such as combining structural imaging, functional imaging, and diffusion tensor imaging (DTI) [42], offer comprehensive brain information. MRI is also non-invasive, suitable for repeated examinations. Nonetheless, MRI’s low temporal resolution makes it challenging to capture rapid neural activity changes. The high cost and operational complexity of MRI equipment, requiring professional maintenance and operation, limit its widespread use. Additionally, MRI is sensitive to motion artifacts, necessitating strict control of the experimental environment.

### 2.3. Applications of Recurrent Neural Networks in EEG Analysis

Recurrent Neural Networks (RNNs) [43], particularly Long Short-Term Memory (LSTM) and Bidirectional Long Short-Term Memory (Bi-LSTM) networks, are widely applied in EEG signal processing [44]. RNNs handle time series data, capturing temporal dependencies, making them particularly suitable for EEG signal analysis. LSTM networks address the vanishing gradient problem of traditional RNNs, making them ideal for long-sequence data analysis. Anitha and Hemanth proposed emotion recognition models based on LSTM and Gated Recurrent Unit (GRU) networks [45–47], achieving efficient emotion classification through EEG signal processing, applicable in BCI and affective computing. Hybrid models like CNN-LSTM combine convolutional neural networks (CNN) [48–52] with LSTM [53–57] to extract spatial and temporal features, enhancing emotion recognition accuracy.

RNNs and their variants [58–60] offer significant advantages and disadvantages in EEG signal processing. RNNs excel in handling dynamic time series data, making them ideal for analyzing rapidly changing EEG signals. LSTM networks effectively address the vanishing gradient problem of traditional RNNs, capturing long-term dependencies and improving the modeling of long-sequence data. Bi-LSTM networks further utilize both past and future information in sequences, enhancing the understanding of complex time series, showing excellent performance in emotion recognition and BCI systems. However, RNN models face challenges, including high computational complexity and long training times when processing large-scale data, requiring substantial computational resources. RNNs are also prone to overfitting, especially with high-dimensional data, necessitating

regularization techniques and other methods to prevent overfitting. Despite LSTM networks mitigating the vanishing gradient problem, they may still encounter challenges when dealing with extremely long time sequences.

Using wearable EEG devices to record participants’ brain activity in real-time while listening to music allows for accurate analysis and prediction of brain responses to musical stimuli. Bi-LSTM models capture long-term dependencies in EEG signals and, combined with attention mechanisms, improve the extraction of key features. This method not only enhances the accuracy of emotion recognition but also provides robust technical support for BCI and affective computing applications. Future advancements in RNN models and signal processing algorithms can better address current technical limitations, offering broader applications in neuroscience research and healthcare.

### 2.4. Auditory Neural Stimulation on the Brain

Auditory stimuli, particularly music, significantly impact the brain and are widely used in neuroscience and psychology research [61]. Music is known to activate multiple brain regions, including the auditory cortex, limbic system, and prefrontal cortex, thereby influencing emotional and cognitive functions. In affective computing, emotional responses induced by music are used to study the brain’s emotion processing mechanisms [62]. For instance, by analyzing EEG signals while listening to music, researchers can identify the emotional states elicited by different musical stimuli, which is valuable in music therapy and emotion computing. In cognitive neuroscience, music is used to study cognitive functions such as attention and memory. Additionally, auditory stimuli are applied in BCI systems to decode brain signals induced by auditory stimuli, enabling control of external devices.

Auditory stimulation offers numerous advantages in studying brain activity [63]. Music, as a complex auditory stimulus, can activate multiple brain regions, providing researchers with a comprehensive understanding of the brain’s emotional and cognitive processing mechanisms. Music stimuli are easy to control and standardize, ensuring high repeatability and reliability of experimental results. Furthermore, the effects of music on the brain are apparent and significant, allowing researchers to clearly observe changes in brain activity through EEG signals [64].

However, auditory stimulation also presents some challenges. Firstly, individual differences in emotional responses to music can significantly affect the generalizability and consistency of experimental results. Secondly, music-induced EEG signals are complex, involving multiple frequency bands and brain regions, requiring sophisticated signal processing and analysis techniques. Additionally, the effects of music on the brain are transient, posing challenges in effectively capturing and analyzing these brief changes.

By using wearable EEG devices to record brain activity while participants listen to music, researchers can monitor and analyze the brain’s response to musical stimuli in real-time. Combining these recordings with Bi-LSTM

[Figure 2]

- Fig. 1. Schematic Diagram of the Proposed Bi-LSTM Framework for Recording Brain Activity While Listening to Music. EEG Signals Are Extracted from the SEED Dataset, and ERP Signals Are Extracted from the DEAP Dataset. The Two Datasets Are Processed Independently and Do Not Interfere with Each Other.

networks allows for more accurate analysis and prediction of the brain’s emotional and cognitive responses to different musical stimuli. Bi-LSTM models capture long-term dependencies in EEG signals and, combined with attention mechanisms, improve the extraction of key features. This combined approach not only enhances emotion recognition accuracy but also provides strong technical support for BCI and affectivecomputing applications. Future research should focus on optimizing auditory stimulus control and EEG signal analysis methods to better understand and utilize the effects of auditory neural stimulation on the brain, providing broader applications in neuroscience and psychology.

## 3. Method

As shown in Figure 1, the overall experimental model involves extracting features from the EEG and ERP signals of the SEED and DEAP datasets. We processed these signals in segments before applying the Bi-LSTM model [65– 69]. The Bi-LSTM architecture comprises an enhanced BiLSTM layer, an attention weighting layer, two fully attentive layers, and a Softmax classification layer. For feature extraction of the P300 component in ERP data and general EEG signals, we performed channel selection, filtering, and segmentation. However, the extraction of P300 features from ERP data included an additional step of Independent Component Analysis (ICA) to remove prominent signal noise and artifacts.

The subsequent Bi-LSTM model incorporated our attention gate method, applying attention weighting to both types of signal features. We utilized dropout techniques in the fully connected layers to prevent overfitting. Separate experiments were conducted on the SEED and DEAP datasets. The SEED dataset experiments primarily focused on processing EEG signals, while the DEAP dataset experiments concentrated on ERP signal processing.

- 3.1. EEG Feature Extraction In the experiment, the differential entropy (DE) [70]

feature in the frequency domain is used as the input for emotion recognition. The extraction process of the differential entropy (DE) feature in the frequency domain is as follows.

Differential entropy (DE) extends the Shannon information entropy 𝐻(𝑋) = −

∑

𝑥 𝑝(𝑥)log

(𝑝(𝑥)

)

to continuous random variables, as shown in Equation 1.

𝐷𝐸 = −∫

𝑏

𝑎

𝑝(𝑥)log

(𝑝(𝑥)

)𝑑𝑥, (1)

where 𝑝(𝑥) represents the continuous probability density function, and [𝑎,𝑏] represents the interval of information extraction. For an EEG signal segment that approximately follows a Gaussian distribution 𝑁(𝜇,𝜎2), its differential entropy is equal to the logarithm of its energy spectrum in a specific frequency band, as shown in Equation 2.

𝐷𝐸 = −∫

𝑏

𝑎

1 √2𝜋𝜎2

𝑒−

(𝑥−𝜇)2

2𝜎2 log(

1 √2𝜋𝜎2

𝑒−

(𝑥−𝜇)2

2𝜎2 )𝑑𝑥

=

- 1

- 2

log(2𝜋𝑒𝜎2),

(2)

- 3.2. Construction of 3D Adjacency Matrix of Graph Convolutional Neural Networks

In EEG-based emotion recognition research utilizing graph neural networks [71–73], it is known that describing the relationships between different EEG electrode channels, i.e., constructing an adjacency matrix, is crucial for EEG emotion classification. In this section, we use the spatial distance between EEG nodes to construct the adjacency matrix representing the topology of EEG channels. The specific construction process is as follows:

The adjacency matrix A ∈ ℝ𝑛×𝑛, where 𝑛 denotes the number of channels in the EEG signals. Each entry 𝑎𝑖𝑗

is learnable and represents the connection weight between channel 𝑖 and channel 𝑗. The international 10-20 EEG electrode system provides the three-dimensional coordinates of each electrode mapped onto a unit sphere. The physical distance between two electrodes is used to measure the connection relationship in the brain space. The farther the distance,thelesstightlythechannelsareconnected.Suppose the coordinates of two points on the sphere with radius 𝑟 are (𝑥𝑖,𝑦𝑖,𝑧𝑖) and (𝑥𝑗,𝑦𝑗,𝑧𝑗), the distance 𝑑𝑖𝑗 between the two points in Cartesian space can be expressed as shown in Equation 3.

), (3)

𝑑𝑖𝑗 = arccos(

𝑥𝑖𝑥𝑗 + 𝑦𝑖𝑦𝑗 + 𝑧𝑖𝑧𝑗 𝑟2

Figure 2 below is a schematic diagram of the 3D spatial relationship of EEG channels used to construct the model’s adjacency matrix. The points in the 3D graph represent the electrode positions of the wearable EEG device used for measuring brainwave activity.

[Figure 3]

- Fig. 2. 3D location map of EEG channels and location channel connectivity map. Left: 3D location map of EEG channels; Right: Initialize the global channel connectivity graph.

In sparse fMRI networks, using about 20% of all possible connections typically maximizes the efficiency of network topology. Therefore, for each EEG channel, we retain connections to its nearest 𝐾 channels, considering them as connected. The value of 𝐾 is chosen based on the number of electrode channels used in the EEG data acquisition equipment. For devices with 62 electrode channels, the value of 𝐾 is selected as 62 × 20% ≈ 12.

The asymmetry of neural activity between the left and right hemispheres is significant in valence and arousal prediction. Therefore, we select certain electrode pairs to initialize the adjacency matrix. To leverage the asymmetry information between the left and right hemispheres, we use 9 global connection pairs and initialize the global interchannel relationships in the adjacency matrix as shown in Equation 4:

𝑎𝑖𝑗 = 𝑎𝑖𝑗 + 1, (4)

As shown in Figure 3, the global channel pairs (𝑖,𝑗) used for initialization are (FP1, FP2), (AF3, AF4), (F5, F6), (FC5,

FC6), (C5, C6), (CP5, CP6), (P5, P6), (PO5, PO6), and (O1, O2).

### 3.3. Bi-LSTM constructs EEG signal recognition

Bi-LSTM is a deep learning model based on LSTM. LSTM networks, through their unique gating mechanisms, can effectively capture and learn long-term dependencies in sequential data, addressing the issues of gradient vanishing and exploding in traditional RNNs (Recurrent Neural Networks).

As shown in Figure 3, unlike traditional unidirectional LSTM, Bi-LSTM comprises two LSTM layers: one processes the sequence forward, and the other processes it backward. This bidirectional mechanism enables Bi-LSTM to leverage both past and future information in the sequence, enhancing the model’s understanding of time-series data.

[Figure 4]

Fig. 3. Bidirectional Long Short-Term Memory Network Network

EEG (Electroencephalography) signals are complex time-series data containing rich temporal and frequency information. Due to the dynamic nature of EEG signals, traditional signal processing methods struggle to capture long-term dependencies and dynamic changes effectively. Bi-LSTM, with its bidirectional mechanism, can more accurately model the temporal information in EEG signals, improving the accuracy of emotion recognition.

In EEG signal recognition models, Bi-LSTM processes EEG signals through forward and backward LSTM layers to extract deep features from the signals. These features can be used for further classification or regression tasks, aiding in recognizing participants’ brain activity patterns in different emotional states. By incorporating attention mechanisms, the Bi-LSTM model can further focus on important moments in the signal, enhancing the model’s recognition capabilities.

In Bi-LSTM, the forward LSTM layer processes EEG samples from time index 1 to 𝑡, generating the forward hidden state sequence ℎ⃖⃖⃗𝑡, while the backward LSTM layer processes EEG samples from time index 𝑡 + 1 to the end, generating the backward hidden state output ⃖⃖⃖ℎ𝑡. This bidirectional processing mechanism allows Bi-LSTM to capture dynamic changes in EEG signals and more accurately model long-term dependencies in the signals.

[Figure 5]

Fig. 4. Single LSTM Cell Diagram. Left: Original LSTM Cell Diagram; Right: LSTM Cell Diagram with Attention Gate.

The left part of Figure 4 illustrates the original architecture of LSTM, where the cell’s output state update is related to the previous hidden layer output and the current input. At each time step 𝑡, the LSTM unit receives the current input 𝑥𝑡, the hidden state ℎ𝑡−1, and the cell state 𝑐𝑡−1 from the previous time step. The LSTM controls information storage and transfer through three gating mechanisms: the input gate, the forget gate, and the output gate. The input gate 𝑖𝑡 determines the update of the cell state by the current input, the forget gate 𝑓𝑡 decides whether to retain the previous cell state 𝑐𝑡−1, and the output gate 𝑜𝑡 decides whether to transfer the hidden state ℎ𝑡−1 to the next LSTM unit. The candidate cell state 𝑐̃𝑡 is a nonlinear transformation of the current input and the previous hidden state. The current cell state 𝑐𝑡 is updated through the forget gate and the input gate, and the current hidden state ℎ𝑡 is determined by the output gate and the nonlinear transformation of the current cell state. Here, 𝜎 represents the sigmoid activation function, tanh represents the tanh activation function, ⊙ denotes elementwise multiplication, 𝑊 and 𝑈 are weight matrices, and 𝑏 is the bias vector. The formulas for the LSTM unit are shown below:

𝑖𝑡 = 𝜎(𝑊𝑖𝑥𝑡 + 𝑈𝑖ℎ𝑡−1 + 𝑏𝑖), 𝑓𝑡 = 𝜎(𝑊𝑓𝑥𝑡 + 𝑈𝑓ℎ𝑡−1 + 𝑏𝑓), 𝑜𝑡 = 𝜎(𝑊𝑜𝑥𝑡 + 𝑈𝑜ℎ𝑡−1 + 𝑏𝑜), 𝑐̃𝑡 = tanh(𝑊𝑐𝑥𝑡 + 𝑈𝑐ℎ𝑡−1 + 𝑏𝑐), 𝑐𝑡 = 𝑓𝑡 ⊙ 𝑐𝑡−1 + 𝑖𝑡 ⊙ 𝑐̃𝑡, ℎ𝑡 = 𝑜𝑡 ⊙ tanh(𝑐𝑡),

(5)

Bi-LSTM combines the outputs of the forward and backward LSTM layers to form the final hidden state output ℎ𝑡. The forward hidden state is computed by the forward LSTM layer, and the backward hidden state is computed by the backward LSTM layer. By combining the forward and back-

- ward hidden states, Bi-LSTM can more comprehensively understand the temporal information in EEG signals, leading to higher accuracy in emotion recognition. The formulas for the Bi-LSTM unit are shown below:

ℎ⃖⃖⃗𝑡 = LSTM→(𝑥𝑡,ℎ⃖⃖⃖⃖⃖⃖⃗𝑡−1), ⃖⃖⃖ℎ𝑡 = LSTM←(𝑥𝑡,⃖⃖⃖⃖⃖⃖⃖ℎ𝑡+1), ℎ𝑡 = [ℎ⃖⃖⃗𝑡;⃖⃖⃖ℎ𝑡],

(6)

In emotion recognition models, Bi-LSTM effectively captures the temporal dynamics in EEG signals through its bidirectional mechanism. Using wearable frontal EEG signal monitoring devices, EEG signals of participants are recorded while they listen to different types of music. The device employs dry electrode technology, simplifying the signal acquisition process and making it suitable for largescale daily applications. The collected EEG signals undergo preprocessing, including denoising, filtering, and feature extraction, to ensure signal quality and analysis accuracy. The Bi-LSTM model processes the preprocessed EEG signals through forward and backward LSTM layers, extracting deep features. By incorporating attention mechanisms to focus on important moments in the signals, this study introduces an improved LSTM method, as shown on the right side of Figure 4, which incorporates the attention mechanism to capture essential historical information and update the cell state. This ultimately improves the accuracy and robustness of emotion recognition, as represented by Eq. 7:

𝑓𝑡 = 𝛿(𝑣𝑓 ∗ tanh(𝑤𝑓 ∗ 𝑐𝑡−1)). (7)

where 𝑣𝑓 and 𝑤𝑓 are the parameters of the attention mechanism. This method reduces the dimensionality of the training parameters compared to Eq. 5.

## 4. Experiment

### 4.1. Datasets

SEED dataset. The SEED dataset [74], collected by Shanghai Jiao Tong University, involves participants watching movie clips of various emotional types, with their EEG signals recorded in response to these stimuli. This dataset

SEED dataset composition.

|Number<br><br>|Name of the clip|Label|
|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>|Lost in Thailand<br><br>World Heritage in China<br><br>Aftershock<br><br>Back to 1942<br><br>Flirting Scholar<br><br>Just Another Pandora’s Box<br><br>|Vigorous Neutral Passive Passive Vigorous Vigorous|

was collected using a 62-channel EEG cap. The experiment included 15 participants, comprising 8 males and 7 females. Each participant was required to attend three identical sessions, with each session spaced 7-14 days apart. In each session, participants watched 15 movie clips, as detailed in Table 1. These 15 clips were selected from different segments of 6 movies, with each segment eliciting different emotions and affective states. During the experiment, the length of each clip was limited to approximately 4 minutes. After watching each clip, participants completed an emotional assessment and took a rest. Once the EEG data was acquired, it was downsampled and filtered for further analysis.

DEAP dataset. The DEAP dataset [75]is a multimodal dataset specifically designed for affective analysis, offering a rich collection of electroencephalogram (EEG), physiological signals, and video data. This dataset involves 32 participants who watched 40 one-minute-long music video excerpts, during which their emotional responses were recorded. The first part of the dataset comprises evaluations of the music videos by 14 to 16 participants, who rated the videos based on arousal, valence, and dominance. The second partof thedataset includesratings, physiological recordings, and facial videos from 32 volunteers while watching the aforementioned 40 music video excerpts. In addition to emotional state ratings, the physiological recordings primarily consist of EEG data. The objective of the DEAP dataset is to provide researchers with a standardized dataset for testing and validating their methods of estimating emotional states, thereby advancing research in affective computing, emotion recognition, and brain-computer interfaces.

### 4.2. Data Preprocessing and Feature Extraction EEG signals have low amplitudes and are often contam-

inated with various noise signals during acquisition. The preprocessing process aims to enhance the quality of EEG signals and reduce noise and artifacts. Common artifacts include electrooculographic (EOG) artifacts, electromyographic (EMG) artifacts, electrocardiographic (ECG) artifacts, skin conductance responses, and power line interference.

The EEG preprocessing workflow includes the following steps:

(1) Downsampling: The original EEG signals were downsampled to reduce computational complexity (SEED: 1000 Hz to 200 Hz; DEAP: 512 Hz to 128 Hz).

Table 2 The rhythm of each band of EEG signal.

|Band<br><br>|Frequency (𝐻𝑧)|Human State|
|---|---|---|
|Delta (𝛿)<br><br>|0.1-3.0<br><br>|Deep sleep, disordered, hypoxic, comatose states|
|Theta (𝜃)<br><br>|4.0-7.0|Fatigue, depression, low mood, disappointment|
|Alpha (𝛼)<br><br>|8.0-12.0|Relaxed, calm, eyes closed but awake<br><br>|
|Beta (𝛽)|12.5-28.0<br><br>|Tense, excited,happy|
|Gamma (𝛾)<br><br>|29.0-50.0|Highly aroused, excited, tense|

- (2) Bad channel detection and removal: Channels with excessive noise or artifacts were identified and removed.
- (3) Electrode re-referencing: Signals were re-referenced to a common average reference.
- (4) Bandpass filtering: A bandpass filter (0.5-50 Hz) was applied to remove irrelevant frequencies and noise.
- (5) Artifact removal using ICA: Independent Component Analysis (ICA) was performed to remove EOG, EMG, and other artifacts.

### 4.3. Emotion Evoked EEG Signal Generation and Acquisition

EEG is a method of recording the electrophysiological activity of the brain’s neural tissues on the surface of the cerebral cortex. Neuronal excitation and inhibition in the brain generate voltage fluctuations, typically measured from the scalp in the range of 10 to 100 𝜇V in adults. Information in EEG signals is primarily contained within the frequency spectrum of 0.5 to several tens of Hertz. Based on frequency differences, EEG signals can be classified into five bands: 𝛿 band (Delta, 1-4 𝐻𝑧), 𝜃 band (Theta, 4-8 𝐻𝑧), 𝛼 band (Alpha, 8-12 𝐻𝑧), 𝛽 band (Beta, 12-30 𝐻𝑧), and 𝛾 band (Gamma, > 30 Hz). The rhythmic characteristics of each band are detailed in Table 2.

EEG signal collection generally employs either dry electrode or wet electrode methods. The current predominant method for EEG data collection is the wet electrode method, which has the advantage of obtaining more distinct EEG data but is inconvenient and less suitable for practical, everyday collection. The use of dry electrodes for EEG signal collection does not require an electrolyte, allowing the electrodes to contact the scalp directly, thereby offering greater convenience. However, due to the higher impedance of the stratum corneum, the EEG signals collected in this manner tend to be weaker. Figure 5 illustrates the layout of the 130-electrode system used in this study, which is both easy to implement and ensures test reproducibility. In the second phase of the experiment, 31 EEG channels were selected (indicated by the blue electrodes in Figure 5), with 13 channels located in the prefrontal cortex and 18 channels in the occipital lobe.

EEG signals have low amplitudes and are often contaminated with various noise signals during acquisition. The

[Figure 6]

- Fig. 5. EEG electrode 130 system placement method. The blue labels indicate the 31 EEG channels selected for the second phase of the experiment, with 13 channels in the prefrontal cortex and 18 channels in the occipital lobe.

preprocessing process aims to enhance the quality of EEG signals and reduce noise and artifacts. Common artifacts include electrooculographic (EOG) artifacts, electromyographic (EMG) artifacts, electrocardiographic (ECG) artifacts, skin conductance responses, and power line interference.

EOG artifacts typically occur in the frequency range of 0-15 Hz and are common EEG artifacts usually associated with eye movements. Blinking artifacts are characterized by narrow spikes with large amplitudes. EMG artifacts generally have higher frequencies and are mixed into EEG signals due to muscle movements during EEG experiments. ECG artifacts primarily arise from the signals generated by myocardial contraction and relaxation, typically presenting as low-frequency signals (less than 5 Hz). Skin conductance responses usually appear in signals collected from the palms or fingertips. Power line interference originates from the 50 Hz mains electricity voltage.

The EEG preprocessing workflow includes downsampling, bad channel detection, electrode re-referencing, bandpass filtering, and Independent Component Analysis (ICA) [76] for artifact removal.

### 4.4. Bi-LSTM Construction and Simulation Parameters

The Bi-LSTM model employed in this study is designed to process EEG signals effectively, leveraging both past and future information to capture long-term dependencies and enhance emotion recognition accuracy. Below are the details of the model construction, hyperparameters, time settings, and experimental parameters:

Bi-LSTM Model Architecture. The Bi-LSTM architecture consists of the following components: An enhanced BiLSTM layer with 128 hidden units in each direction (forward and backward); An attention weighting layer to emphasize critical features in the EEG signals; Two fully connected layers with 64 neurons each, using ReLU activation functions; ASoftmaxclassification layer to output the probability distribution of emotional states.

Hyperparameters. The hyperparameters for the BiLSTM model were carefully selected based on empirical experiments and existing literature. The following settings were used: Learning rate: 0.001;Batch size: 64; Epochs: 100; Dropout rate: 0.5 to prevent overfitting; Optimizer: Adam.

Time Settings and Data Preprocessing. For the SEED dataset, EEG signals were recorded at a sampling rate of 1000 Hz and then downsampled to 200 Hz to reduce computational complexity. Each recording session lasted approximately 4 minutes per clip. The EEG signals were segmented into 1-second non-overlapping windows, resulting in 200 data points per segment.

For the DEAP dataset, EEG signals were recorded at a sampling rate of 512 Hz and then downsampled to 128 Hz. Each music video excerpt lasted 1 minute, and the signals were segmented into 1-second windows with 128 data points per segment.

Experimental Parameters and Settings. The experimental setup included the following key parameters: Feature extraction: Differential Entropy (DE) features were extracted from the segmented EEG signals; Model training: The BiLSTM model was trained on 80% of the data and validated on the remaining 20%; Evaluation metrics: Accuracy, precision, recall, and F1-score were used to evaluate the model’s performance.

Simulation Process.The simulation of EEG signal fluctuations was conducted as follows: The Data_preprocessed files from the DEAP dataset were fed into a linear filter to map the spectral output of the EEG signals, representing brain neural activity; A receptive field model of the linear filter was created to generate artificial neural responses; The data were downsampled along the time dimension, and the receptive field was used to create an artificial neural response by performing a dot product with the receptive field; The Bi-LSTM model was then used to simulate and predict the time-varying stimulus response of the EEG signals.

### 4.5. Results

To ensure a fair comparison between the different models, we maintained consistent experimental conditions across all tests. All models were trained and evaluated using the same datasets (SEED and DEAP) and preprocessing techniques. Additionally, we used the same training, validation, and testing splits to provide an equitable basis for performance evaluation. Hyperparameters for each model were tuned individually to achieve optimal performance, ensuring that each model was fairly optimized for comparison. We also employed standard evaluation metrics, such as accuracy, precision, recall, and F1-score, to provide a

Comparative Performance Analysis of Advanced Models on the SEED Dataset for EEG-Based Emotion Recognition.

Model Multiclass Channel Accuracy(%) SVM [77] Binary 256 82.52 EEG-Net [79] Binary 14 88.04 PMK [78] Multi(3) 32 91.45 LSTM [80] Multi(20) 64 86.75 Bi-LSTM Multi(20) 64 92.39 Bi-LSTM+AttW(1 layer and 64 hidden size) Multi(20) 64 93.42 Bi-LSTM+AttG(1 layer and 64 hidden size) Multi(20) 64 95.16 Bi-LSTM+AttWG(1 layer and 32 hidden size) Multi(20) 64 95.08 Bi-LSTM+AttWG(1 layer and 64 hidden size) Multi(20) 128 98.28 Bi-LSTM+AttWG(1 layer and 128 hidden size) Multi(20) 64 96.22

comprehensive assessment of each model’s performance. The results demonstrate the superior performance of the BiLSTM model with attention mechanisms, highlighting the effectiveness of our proposed approach in emotion recognition using EEG signals.

Results on SEED dataset. We conducted a comparative experiment using EEG-based object detection visual models on the SEED dataset. The models we employed include Support Vector Machine (SVM) [77], Pyramid Match Kernel (PMK) [78], EEG-Net [79], LSTM [80], and Bi-LSTM. SVM is a supervised learning model used for classification and regression analysis, effectively handling high-dimensional data. PMK is a kernel function used for image matching by processing image features through a pyramid structure to achieve efficient matching. EEG-Net is a deep learning model specifically designed for processing and analyzing EEG data to improve the classification and recognition performance of EEG signals. LSTM is a type of RNN model that addresses long-term dependency issues through its gating mechanism, making it suitable for handling sequential data. Bi-LSTM consists of forward and backward LSTM layers, enabling the model to utilize both past and future information in the sequence, thus enhancing its understanding of temporal data.

Our proposal and the performance comparison of these models are shown in Table 3. In addition to these advanced model algorithms, we also compared our model with the incorporation of attention gates and attention weights to explore the effectiveness of Bi-LSTM. As shown in the table, the Bi-LSTM models with attention mechanisms significantly improved accuracy. Specifically, the Bi-LSTMAttGW (1 layer and 128 hidden size) model achieved the highest accuracy of 98.28% in multiclass tasks. This demonstrates that incorporating attention mechanisms can significantly enhance the performance of models in emotion recognition using EEG signals. This method greatly improves the accuracy of capturing EEG signals.

As shown in Table 4, we compared the accuracy and standard deviation of different models in various frequency bands of the SEED dataset. Our proposed model demonstrated superior performance across all frequency bands, particularly in the 𝛾 band, where it achieved an accuracy of 98.28% with a standard deviation of 7.42. This highlights

Table 4 Comparison of Accuracy and Standard Deviation of Different Models in Different Frequency Bands of SEED Dataset.

Frequency Band

SVM [77] LSTM [80] Ours

𝛿 60.12 ± 14.11 74.45 ± 11.43 70.26 ± 15.36 𝜃 60.92 ± 10.25 71.26 ± 5.46 75.34 ± 15.16 𝛼 66.95 pm 14.85 74.31 ± 12.58 86.13 ± 14.83 𝛽 80.71± 11.16 81.25 ± 10.11 90.23 ± 9.13 𝛾 82.52 ± 9.17 86.75 ± 8.43 98.28 ± 7.42

the robustness and effectiveness of our Bi-LSTM model with attention mechanisms in capturing the complexities of EEG signals and improving emotion recognition accuracy.

To visualize the EEG signal activity of the brain, we applied a low-pass filter at 8 𝐻𝑧 to the EEG signals from the SEED dataset to remove high-frequency noise. Figure 6 shows the EEG signal fragments in the regions of interest (ROIs) using the 130-electrode system layout. Each row in thefigurerepresentsthebrainactivityrecorded fora segment from different movies, illustrating the variations in EEG signals in response to different emotional stimuli.

The first row represents the brain activity recorded for a segment from the movie Lost in Thailand, showing EEG signal snippets from 50 ms before to 130 ms after each beat mark. We performed baseline correction for each EEG signal band by subtracting the mean value calculated from the 50 ms segments between beat marks. The second row represents brain activity for a segment from the movie Back to 1942, recorded from 100 ms before to 180 ms after each beat mark, with baseline correction applied every 20 ms. The third row shows brain activity for a segment from the movie World Heritage in China, recorded from 55 ms before to 130 ms after each beat mark, with baseline correction applied every 25 ms. This detailed breakdown demonstrates the dynamic changes in brain activity elicited by different emotional stimuli across multiple time points.

When recording EEG data, the signal initially shows a negative dip at 0 ms. Any auditory processing related to the music beats occurs shortly afterward. One possible explanation is that the sudden change in the music beat causes a sudden dip in the EEG signal. However, this requires further

[Figure 7]

- Fig. 6. Dynamic Changes in EEG Signal Regions of Interest at Different Time Points Across Various Movie Scenes in the SEED Datazset. The figure illustrates how different emotional stimuli from movies affect brain activity recorded through EEG signals.

investigation.Itcouldalsobedue toinaccuracies in the wearable device used to collect the signal or the sampling rate and tracker precision. For further comparison, Figure 7 shows the EEG signal changes at the imagined time points corresponding to different movie scenes in the SEED dataset. This figure corresponds to the second row in Figure 6, showing the variations in the ROIs. The amplitude range of these EEG signal changes is relatively large, likely due to the emotional intensity provided by the movie segments. To calculate meaningful fluctuations, precise timing (e.g., sudden events) must be known. However, small changes during EEG signal recording are likely, causing some imprecision in the beat marks.

[Figure 8]

- Fig. 7. EEG Signal Variations at Time Points in the Movie Scene "Back to 1942" from the SEED Dataset.

To understand the event-related effects on EEG signals induced by auditory and visual stimuli, we used the DEAP dataset, which contains emotion-related EEG signals. We analyzed the five EEG frequency bands affected by emotional states (as shown in Table 2). We employed EventRelated Potentials (ERP) metrics to record these changes.

Table 5 Statistics on the P300 value of ERP data on the DEAP dataset.

|Emotion Change|ERP Change Period Post-Stimulus (ms)<br><br>|P|
|---|---|---|
|Happiness (mean±SD) Sadness (mean±SD) Fear (mean±SD)<br><br>|298.45±33.25 316.45±30.24 327.13±31.69|0.026 0.470 0.020<br><br>|

ERP refers to the specific potentials induced by stimuli such as auditory and visual cues, excluding spontaneous EEG signals. With its high temporal resolution, ERP can reflect changes in brain neurophysiological activities during cognitive processes, making it a widely used tool for assessing brain cognitive processing. The features commonly analyzed in ERP data are the latency and peaks of its components. The main components of ERP include P100, N100, P200, N200, and P300. Most studies focus on the P300 component of ERP data for brainwave analysis. The P300 component is a positive deflection occurring around 300 milliseconds post-stimulus. Table 5 presents the statistical results of P300 values from ERP data in the DEAP dataset. It is evident from the table that participants exhibit more intense emotional reactions to sad music scenes.

We used a Bi-LSTM model to simulate and predict EEG signal fluctuations recorded in the DEAP dataset. The Data_preprocessed files were fed into a linear filter to map the spectral output of the EEG signals, representing brain neural activity. We attempted to recreate the receptive field model of the linear filter to generate this data. The data were downsampled along the time dimension, and this receptive field was used to create an artificial neural response. This involved performing a dot product with the receptive field. As shown in Figure 8, the left side depicts the simulated neural response to EEG signals, with auditory features as input and the simulated time-varying stimulus response as output. The top right shows the receptive field generated by the stimulus signals, and the bottom right illustrates the EEG signal variation process simulated by the Bi-LSTM. The figure indicates that the EEG signals exhibit significant fluctuations in response to varying levels of musical stimuli, with the extent of fluctuations being related to the emotional intensity provided by the music.

## 5. Conclusion

This study records and analyzes brain activity while listening to music using wearable EEG devices and Bi-LSTM with attention mechanisms to identify emotional states. Data was collected using wearable EEG devices, preprocessed, and DE features were extracted. A Bi-LSTM model with attention mechanisms was then constructed, showing superior performance in emotion recognition, particularly with the SEED and DEAP datasets. The Bi-LSTM-AttGW model achieved the highest accuracy of 98.28% in multi-class tasks.

The novelty of this study lies in the integration of BiLSTM with attention mechanisms for EEG signal processing. This combination significantly improves the accuracy

[Figure 9]

Fig. 8. Neural Response Signal Changes and Bi-LSTM Simulated Signal Variation Trends in EEG Data.

of emotion recognition, outperforming traditional models like SVM, EEG-Net, and LSTM [81, 82]. The study demonstrates the potential of using advanced deep learning techniques to better capture the complexities of EEG signals and enhance emotion recognition.

Despite these achievements, there are limitations. Wearable EEG devices have relatively low sampling rates and are prone to artifacts, affecting signal quality. Future research should focus on improving device design and signal processing algorithms. Additionally, larger sample sizes and more diverse experimental conditions are needed to account for individual differences in emotional responses to music. Further integration of multimodal data and various emotional elicitation methods could enhance the accuracy and applicability of emotion recognition in BCI and affective computing.

## Author contributions

Jingyi Wang: Data Management, Methodology, Soft-

- ware, and Writing – original draft. Zhiqun Wang: Supervision, Writing – review & editing. Fanyu Kong: Methodology, Software, Writing – review & editing. Guiran Liu: Supervision, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The data that support the findings of this study are available on request from the corresponding author. The data are not publicly available due to privacy or ethical restrictions.

## References

- [1] X. Hu, S. Yuan, F. Xu, Y. Leng, K. Yuan, Q. Yuan, Scalp eeg classification using deep bi-lstm network for seizure detection, Computers in Biology and Medicine 124 (2020) 103919.
- [2] Y. Wang, S. Sun, Q. Guo, The mechanism of the impact of enterprise digital transformation on transaction performance, Journal of Xi’an University of Finance and Economics 37 (2024) 60–71.
- [3] Y. Wang, W. Song, W. Tao, A. Liotta, D. Yang, X. Li, S. Gao, Y. Sun, W. Ge, W. Zhang, et al., A systematic review on affective computing: Emotion models, databases, and recent advances, Information Fusion 83 (2022) 19–52.
- [4] K. S. Kamble, J. Sengupta, Ensemble machine learning-based affective computing for emotion recognition using dual-decomposed eeg signals, IEEE Sensors Journal 22 (2021) 2496–2507.
- [5] D. S. Naser, G. Saha, Influence of music liking on eeg based emotion recognition, Biomedical Signal Processing and Control 64 (2021) 102251.
- [6] I. Daly, Neural decoding of music from the eeg, Scientific Reports 13 (2023) 624.
- [7] M. M. Rahman, A. K. Sarkar, M. A. Hossain, M. S. Hossain, M. R. Islam, M. B. Hossain, J. M. Quinn, M. A. Moni, Recognition of human emotions using eeg signals: A review, Computers in biology and medicine 136 (2021) 104696.
- [8] X. Zheng, W. Chen, An attention-based bi-lstm method for visual object classification via eeg, Biomedical Signal Processing and Control 63 (2021) 102174.
- [9] S. Dai, K. Li, Z. Luo, P. Zhao, B. Hong, A. Zhu, J. Liu, Ai-based nlp section discusses the application and effect of bag-of-words models

- and tf-idf in nlp tasks, Journal of Artificial Intelligence General science (JAIGS) ISSN: 3006-4023 5 (2024) 13–21.
- [10] Y. Wang, M. Alangari, J. Hihath, A. K. Das, M. Anantram, A machine learning approach for accurate and real-time dna sequence identification, BMC genomics 22 (2021) 1–10.
- [11] A. Richardson, X. Wang, A. Dubey, J. Sprinkle, Reinforcement learning with communication latency with application to stop-andgo wave dissipation, in: 2024 IEEE Intelligent Vehicles Symposium (IV), IEEE, 2024, pp. 1187–1193.
- [12] G. Bouallegue, R. Djemal, S. A. Alshebeili, H. Aldhalaan, A dynamic filtering df-rnn deep-learning-based approach for eeg-based neurological disorders diagnosis, IEEE Access 8 (2020) 206992– 207007.
- [13] J. Wang, F. Li, Y. An, X. Zhang, H. Sun, Towards robust lidar-camera fusion in bev space via mutual deformable attention and temporal aggregation, IEEE Transactions on Circuits and Systems for Video Technology (2024) 1–1.
- [14] Z. Xu, D. Deng, Y. Dong, K. Shimada, Dpmpc-planner: A realtime uav trajectory planning framework for complex static environments with dynamic obstacles, in: 2022 International Conference on Robotics and Automation (ICRA), IEEE, 2022, pp. 250–256.
- [15] P. Zhao, K. Li, B. Hong, A. Zhu, J. Liu, S. Dai, Task allocation planning based on hierarchical task network for national economic mobilization, Journal of Artificial Intelligence General science (JAIGS) ISSN: 3006-4023 5 (2024) 22–31.
- [16] Y. Song, R. Fellegara, F. Iuricich, L. De Floriani, Parallel topologyaware mesh simplification on terrain trees, ACM Transactions on Spatial Algorithms and Systems 10 (2024) 1–39.
- [17] X. Geng, X. Zhang, M. Yue, W. Hu, L. Wang, X. Zhang, P. Yu, D. Long, H. Yan, A motor imagery eeg signal optimized processing algorithm, Alexandria Engineering Journal 101 (2024) 38–51.
- [18] Q. Zhang, W. Qi, H. Zheng, X. Shen, Cu-net: a u-net architecture for efficient brain-tumor segmentation on brats 2019 dataset, 2024. arXiv:2406.13113.
- [19] H. Peng, R. Ran, Y. Luo, J. Zhao, S. Huang, K. Thorat, T. Geng, C. Wang, X. Xu, W. Wen, et al., Lingcn: Structural linearized graph convolutional network for homomorphically encrypted inference, in: Thirty-seventh Conference on Neural Information Processing Systems, ????
- [20] Y. Song, R. Fellegara, F. Iuricich, L. De Floriani, Efficient topologyaware simplification of large triangulated terrains, in: Proceedings of the 29th International Conference on Advances in Geographic Information Systems, 2021, pp. 576–587.
- [21] Y. Wang, V. Khandelwal, A. K. Das, M. Anantram, Classification of dna sequences: Performance evaluation of multiple machine learning methods, in: 2022 IEEE 22nd International Conference on Nanotechnology (NANO), IEEE, 2022, pp. 333–336.
- [22] R. Zanetti, A. Arza, A. Aminifar, D. Atienza, Real-time eeg-based cognitive workload monitoring on wearable devices, IEEE transactions on biomedical engineering 69 (2021) 265–277.
- [23] P. Srinivas, M. Arulprakash, M. Vadivel, N. Anusha, G. Rajasekar, C. Srinivasan, Support vector machines based predictive seizure care using iot-wearable eeg devices for proactive intervention in epilepsy, in: 2024 2nd International Conference on Computer, Communication and Control (IC4), IEEE, 2024, pp. 1–5.
- [24] K. Kotowski, K. Stapor, J. Leski, M. Kotas, Validation of emotiv epoc+ for extracting erp correlates of emotional face processing, Biocybernetics and Biomedical Engineering 38 (2018) 773–781.
- [25] Q. Cheng, Y. Song, The impact of the digital economy on regional economic development disparities from the perspective of spatial spillovers, Journal of Xi’an University of Finance and Economics 36 (2023) 44–57.
- [26] J. H. Shin, J. Kwon, J. U. Kim, H. Ryu, J. Ok, S. Joon Kwon, H. Park, T.-i. Kim, Wearable eeg electronics for a brain–ai closedloop system to enhance autonomous machine decision-making, npj Flexible Electronics 6 (2022) 32.
- [27] T. Li, R. Zhao, Y. Liu, X. Liu, Y. Li, Effect of age on driving behavior and a neurophysiological interpretation, in: International Conference

- on Human-Computer Interaction, Springer, 2022, pp. 184–194.
- [28] A. De, H. Mohammad, Y. Wang, R. Kubendran, A. K. Das, M. Anantram, Modeling and simulation of dna origami based electronic read-only memory, in: 2022 IEEE 22nd International Conference on Nanotechnology (NANO), IEEE, 2022, pp. 385–388.
- [29] B. Hong, P. Zhao, J. Liu, A. Zhu, S. Dai, K. Li, The application of artificial intelligence technology in assembly techniques within the industrial sector, Journal of Artificial Intelligence General science (JAIGS) ISSN: 3006-4023 5 (2024) 1–12.
- [30] C. Jin, T. Huang, Y. Zhang, M. Pechenizkiy, S. Liu, S. Liu, T. Chen, Visual prompting upgrades neural network sparsification: A datamodel perspective, arXiv preprint arXiv:2312.01397 (2023).
- [31] Y. Dong, The design of autonomous uav prototypes for inspecting tunnel construction environment, arXiv preprint arXiv:2408.07286

(2024).

- [32] R. Zhao, Y. Liu, T. Li, Y. Li, A preliminary evaluation of driver’s workload in partially automated vehicles, in: International Conference on Human-Computer Interaction, Springer, 2022, pp. 448–458.
- [33] C. Jin, T. Che, H. Peng, Y. Li, M. Pavone, Learning from teaching regularization: Generalizable correlations should be easy to imitate, arXiv preprint arXiv:2402.02769 (2024).
- [34] X. Jiang, J. Yu, Z. Qin, Y. Zhuang, X. Zhang, Y. Hu, Q. Wu, Dualvd: An adaptive dual encoding model for deep visual understanding in visual dialogue, in: Proceedings of the AAAI conference on artificial intelligence, volume 34, 2020, pp. 11125–11132.
- [35] T. Li, R. Zhao, Y. Liu, Y. Li, G. Li, Evaluate the effect of age and driving experience on driving performance with automated vehicles, in: InternationalConferenceonAppliedHumanFactorsandErgonomics, Springer, 2021, pp. 155–161.
- [36] X. Xie, H. Peng, A. Hasan, S. Huang, J. Zhao, H. Fang, W. Zhang, T. Geng, O. Khan, C. Ding, Accel-gcn: High-performance gpu accelerator design for graph convolution networks, in: 2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD), IEEE, 2023, pp. 01–09.
- [37] P. Chen, Z. Zhang, Y. Dong, L. Zhou, H. Wang, Enhancing visual question answering through ranking-based hybrid training and multimodal fusion, arXiv preprint arXiv:2408.07303 (2024).
- [38] K. Li, A. Zhu, W. Zhou, P. Zhao, J. Song, J. Liu, Utilizing deep learning to optimize software development processes, arXiv preprint arXiv:2404.13630 (2024).
- [39] V. Lambrecq, A. Hanin, E. Munoz-Musat, L. Chougar, S. Gassama, C. Delorme, L. Cousyn, A. Borden, M. Damiano, V. Frazzini, et al., Association of clinical, biological, and brain magnetic resonance imaging findings with electroencephalographic findings for patients with covid-19, JAMA Network Open 4 (2021) e211489–e211489.
- [40] M. Nentwich, L. Ai, J. Madsen, Q. K. Telesford, S. Haufe, M. P. Milham, L. C. Parra, Functional connectivity of eeg is subject-specific, associated with phenotype, and different from fmri, NeuroImage 218

(2020) 117001.

- [41] J. M. Palva, S. Palva, Infra-slow fluctuations in electrophysiological recordings, blood-oxygenation-level-dependent signals, and psychophysical time series, Neuroimage 62 (2012) 2201–2211.
- [42] E. A. Wilde, N. J. Goodrich-Hunsaker, A. L. Ware, B. A. Taylor, B. D. Biekman, J. V. Hunter, R. Newman-Norlund, S. Scarneo, D. J. Casa, H. S. Levin, Diffusion tensor imaging indicators of white matter injury are correlated with a multimodal electroencephalography-based biomarker in slow recovering, concussed collegiate athletes, Journal of neurotrauma 37 (2020) 2093–2101.
- [43] S. Tortora, S. Ghidoni, C. Chisari, S. Micera, F. Artoni, Deep learning-based bci for gait decoding from eeg with lstm recurrent neural network, Journal of neural engineering 17 (2020) 046011.
- [44] S. J. Teipel, O. Pogarell, T. Meindl, O. Dietrich, D. Sydykova, U. Hunklinger, B. Georgii, C. Mulert, M. F. Reiser, H.-J. Möller, et al., Regional networks underlying interhemispheric connectivity: an eeg and dti study in healthy ageing and amnestic mild cognitive impairment, Human brain mapping 30 (2009) 2098–2119.
- [45] H. Cui, A. Liu, X. Zhang, X. Chen, J. Liu, X. Chen, Eeg-based subject-independent emotion recognition using gated recurrent unit

- and minimum class confusion, IEEE Transactions on Affective Computing 14 (2023) 2740–2750.
- [46] T. Li, G. Pang, X. Bai, J. Zheng, L. Zhou, X. Ning, Learning adversarial semantic embeddings for zero-shot recognition in open worlds, Pattern Recognition 149 (2024) 110258.
- [47] H. Ran, W. Li, L. Li, S. Tian, X. Ning, P. Tiwari, Learning optimal inter-class margin adaptively for few-shot class-incremental learning via neural collapse-based meta-learning, Information Processing & Management 61 (2024) 103664.
- [48] A. A. Ein Shoka, M. M. Dessouky, A. El-Sayed, E. El-Din Hemdan, An efficient cnn based epileptic seizures detection framework using encrypted eeg signals for secure telemedicine applications, Alexandria Engineering Journal 65 (2023) 399–412.
- [49] A. Zhu, K. Li, T. Wu, P. Zhao, W. Zhou, B. Hong, Cross-task multibranch vision transformer for facial expression and mask wearing classification, arXiv preprint arXiv:2404.14606 (2024).
- [50] K. Li, P. Xirui, J. Song, B. Hong, J. Wang, The application of augmented reality (ar) in remote work and education, arXiv preprint arXiv:2404.10579 (2024).
- [51] Z. An, X. Wang, T. T. Johnson, J. Sprinkle, M. Ma, Runtime monitoring of accidents in driving recordings with multi-type logic in empirical models, in: International Conference on Runtime Verification, Springer, 2023, pp. 376–388.
- [52] Y. Liu, R. Zhao, T. Li, Y. Li, An investigation of the impact of autonomous driving on driving behavior in traffic jam, in: IIE Annual Conference. Proceedings, Institute of Industrial and Systems Engineers (IISE), 2021, pp. 986–991.
- [53] S. Sheykhivand, Z. Mousavi, T. Y. Rezaii, A. Farzamnia, Recognizing emotions evoked by music using cnn-lstm networks on eeg signals, IEEE access 8 (2020) 139332–139345.
- [54] X. Wang, S. Onwumelu, J. Sprinkle, Using automated vehicle data as a fitness tracker for sustainability, in: 2024 Forum for Innovative Sustainable Transportation Systems (FISTS), IEEE, 2024, pp. 1–6.
- [55] R. Fellegara, F. Iuricich, Y. Song, L. D. Floriani, Terrain trees: a framework for representing, analyzing and visualizing triangulated terrains, GeoInformatica 27 (2023) 525–564.
- [56] H. Peng, S. Huang, T. Zhou, Y. Luo, C. Wang, Z. Wang, J. Zhao, X. Xie, A. Li, T. Geng, et al., Autorep: Automatic relu replacement for fast private network inference, in: 2023 IEEE/CVF International Conference on Computer Vision (ICCV), IEEE, 2023, pp. 5155– 5165.
- [57] Y. Zhuang, Y. Chen, J. Zheng, Music genre classification with transformer classifier, in: Proceedings of the 2020 4th international conference on digital signal processing, 2020, pp. 155–159.
- [58] R. Zhao, Y. Liu, Y. Li, B. Tokgoz, An investigation of resilience in manual driving and automatic driving in freight transportation system, in: IIE Annual Conference. Proceedings, Institute of Industrial and Systems Engineers (IISE), 2021, pp. 974–979.
- [59] A. De, H. Mohammad, Y. Wang, R. Kubendran, A. K. Das, M. Anantram, Performance analysis of dna crossbar arrays for highdensity memory storage applications, Scientific Reports 13 (2023) 6650.
- [60] Y. Liu, R. Zhao, Y. Li, A preliminary comparison of drivers’ overtaking behavior between partially automated vehicles and conventional vehicles, in: Proceedings of the Human Factors and Ergonomics Society Annual Meeting, volume 66, SAGE Publications Sage CA: Los Angeles, CA, 2022, pp. 913–917.
- [61] B. Somers, C. J. Long, T. Francart, Eeg-based diagnostics of the auditory system using cochlear implant electrodes as sensors, Scientific Reports 11 (2021) 5383.
- [62] D. Henao, M. Navarrete, M. Valderrama, M. Le Van Quyen, Entrainment and synchronization of brain oscillations to auditory stimulations, Neuroscience Research 156 (2020) 271–278.
- [63] M. L. Ferster, G. Da Poian, K. Menachery, S. J. Schreiner, C. Lustenberger, A. Maric, R. Huber, C. R. Baumann, W. Karlen, Benchmarking real-time algorithms for in-phase auditory stimulation of low amplitude slow waves with wearable eeg devices during sleep, IEEE Transactions on Biomedical Engineering 69 (2022) 2916–2925.

- [64] X. Geng, D. Li, H. Chen, P. Yu, H. Yan, M. Yue, An improved feature extraction algorithms of eeg signals based on motor imagery braincomputer interface, Alexandria Engineering Journal 61 (2022) 4807– 4820.
- [65] Q. Deng, Z. Fan, Z. Li, X. Pan, Q. Kang, M. Zhou, Solving the foodenergy-water nexus problem via intelligent optimization algorithms, arXiv preprint arXiv:2404.06769 (2024).
- [66] S. Patel, Y. Liu, R. Zhao, X. Liu, Y. Li, Inspection of in-vehicle touchscreen infotainment display for different screen locations, menu types, and positions, in: International conference on human-computer interaction, Springer, 2022, pp. 258–279.
- [67] J. Lee, H. Wang, K. Jang, A. Hayat, M. Bunting, A. Alanqary, W. Barbour, Z. Fu, X. Gong, G. Gunter, et al., Traffic smoothing via connected & automated vehicles: A modular, hierarchical control design deployed in a 100-cav flow smoothing experiment, IEEE Control Systems Magazine (2024).
- [68] Z. Zhu, R. Zhao, J. Ni, J. Zhang, Image and spectrum based deep feature analysis for particle matter estimation with weather informatio, in: 2019 IEEE International Conference on Image Processing (ICIP), IEEE, 2019, pp. 3427–3431.
- [69] Y. Liu, R. Zhao, T. Li, Y. Li, The impact of directional road signs combinations and language unfamiliarity on driving behavior, in: International Conference on Human-Computer Interaction, Springer, 2022, pp. 195–204.
- [70] J. Zhang, Z. Wei, J. Zou, H. Fu, Automatic epileptic eeg classification based on differential entropy and attention model, Engineering Applications of Artificial Intelligence 96 (2020) 103975.
- [71] T. Zhou, J. Zhao, Y. Luo, X. Xie, W. Wen, C. Ding, X. Xu, Adapi: Facilitating dnn model adaptivity for efficient private inference in edge computing, arXiv preprint arXiv:2407.05633 (2024).
- [72] H. Peng, X. Xie, K. Shivdikar, M. A. Hasan, J. Zhao, S. Huang, O. Khan, D. Kaeli, C. Ding, Maxk-gnn: Extremely fast gpu kernel design for accelerating graph neural networks training, in: Proceedings of the 29th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2, ASPLOS ’24, Association for Computing Machinery, New York, NY, USA, 2024, p. 683–698.
- [73] C. Jin, H. Peng, S. Zhao, Z. Wang, W. Xu, L. Han, J. Zhao, K. Zhong, S. Rajasekaran, D. N. Metaxas, Apeer: Automatic prompt engineering enhances large language model reranking, arXiv preprint arXiv:2406.14449 (2024).
- [74] Y. Cimtay, E. Ekmekcioglu, Investigating the use of pretrained convolutional neural network on cross-subject and cross-dataset eeg emotion recognition, Sensors 20 (2020) 2034.
- [75] M. Khateeb, S. M. Anwar, M. Alnowami, Multi-domain feature fusion for emotion classification using deap dataset, Ieee Access 9 (2021) 12134–12142.
- [76] M. J. Antony, B. P. Sankaralingam, R. K. Mahendran, A. A. Gardezi, M. Shafiq, J.-G. Choi, H. Hamam, Classification of eeg using adaptive svm classifier with csp and online recursive independent component analysis, Sensors 22 (2022) 7596.
- [77] J. Kang, X. Han, J. Song, Z. Niu, X. Li, The identification of children with autism spectrum disorder by svm approach on eeg and eyetrackingdata, Computersinbiology andmedicine120(2020) 103722.
- [78] F. Hou, J. Liu, Z. Bai, Z. Yang, J. Liu, Q. Gao, Y. Song, Eeg-based emotion recognition for hearing impaired and normal individuals with residual feature pyramids network based on time–frequency–spatial features, IEEE Transactions on Instrumentation and Measurement 72

(2023) 1–11.

- [79] D. Huang, X. Wang, J. Liu, J. Li, W. Tang, Virtual reality safety training using deep eeg-net and physiology data, The visual computer 38 (2022) 1195–1207.
- [80] N. Kadri, A. Ellouze, M. Ksantini, S. H. Turki, New lstm deep learning algorithm for driving behavior classification, Cybernetics and Systems 54 (2023) 387–405.
- [81] Y. Wang, B. Demir, H. Mohammad, E. E. Oren, M. Anantram, Computational study of the role of counterions and solvent dielectric in determining the conductance of b-dna, Physical Review E 107

(2023) 044404.

[82] Y. Luo, N. Xu, H. Peng, C. Wang, S. Duan, K. Mahmood, W. Wen, C. Ding, X. Xu, Aq2pnn: Enabling two-party privacy-preserving deep neural network inference with adaptive quantization, in: 2023 56th IEEE/ACM International Symposium on Microarchitecture (MICRO), IEEE, 2023, pp. 628–640.

