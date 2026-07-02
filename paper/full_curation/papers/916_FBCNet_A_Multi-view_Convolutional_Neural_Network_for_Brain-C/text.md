i

# FBCNet: A Multi-view Convolutional Neural Network for Brain-Computer Interface

Ravikiran Mane Member, IEEE, Efﬁe Chew, Karen Chua, Kai Keng Ang Senior Member, IEEE, Neethu Robinson Member, IEEE, A. P. Vinod Senior Member, IEEE, Seong-Whan Lee Fellow, IEEE, and Cuntai Guan Fellow, IEEE

## arXiv:2104.01233v1[cs.OH]17Mar2021

Abstract—Lack of adequate training samples and noisy highdimensional features are key challenges faced by Motor Imagery (MI) decoding algorithms for electroencephalogram (EEG) based Brain-Computer Interface (BCI). To address these challenges, inspired from neuro-physiological signatures of MI, this paper proposes a novel Filter-Bank Convolutional Network (FBCNet) for MI classiﬁcation. FBCNet employs a multi-view data representation followed by spatial ﬁltering to extract spectro-spatially discriminative features. This multistage approach enables efﬁcient training of the network even when limited training data is available. More signiﬁcantly, in FBCNet, we propose a novel Variance layer that effectively aggregates the EEG time-domain information. With this design, we compare FBCNet with stateof-the-art (SOTA) BCI algorithm on four MI datasets: The BCI competition IV dataset 2a (BCIC-IV-2a), the OpenBMI dataset, and two large datasets from chronic stroke patients. The results show that, by achieving 76.20% 4-class classiﬁcation accuracy, FBCNet sets a new SOTA for BCIC-IV-2a dataset. On the other three datasets, FBCNet yields up to 8% higher binary classiﬁcation accuracies. Additionally, using explainable AI techniques we present one of the ﬁrst reports about the differences in discriminative EEG features between healthy subjects and stroke patients. Also, the FBCNet source code is available at https://github.com/ravikiran-mane/FBCNet.

Index Terms—Brain Computer Interface, Stroke Rehabilitation, Deep Learning, Motor Imagery Classiﬁcation

I. INTRODUCTION

In recent years, the technology of Brain-Computer Interface (BCI) has emerged as a powerful means of communication and control for severely paralyzed patients [1], [2]. BCI systems capture real-time brain activity and try to decode users’ intentions from the observed neuronal activations [1]. The decoded state is then used to control external devices [3], [4] or for communication [5]. In BCI systems, electroencephalography (EEG) is the most widely used signal acquisition modality and Motor-Imagery (MI) based EEG-BCI, wherein participant performs mental rehearsal of a particular motor movement is one

Ravikiran Mane, Kai Keng Ang, Neethu Robinson, Cuntai Guan are with the Nanyang Technological University, 50 Nanyang Avenue, Singapore (ravikian001@e.ntu.edu.sg, kkang@ntu.edu.sg, nrobinson@ntu.edu.sg, ctguan@ntu.edu.sg).

Efﬁe Chew is with National University Hospital, Singapore. (efﬁe_chew@nuhs.edu.sg)

Karen Chua is with Tan Tock Seng Hospital, Singapore. (karen_chua@ttsh.com.sg)

Kai Keng Ang is with Institute for Infocomm Research, Agency for Science, Technology and Research (A*STAR), Singapore. (kkang@i2r.a-star.edu.sg)

A. P. Vinod is with Indian Institute of Technology, Palakkad, India. (vinod@iitpkd.ac.in)

S. -W. Lee is with the Department of Artiﬁcial Intelligence, Korea University, Seoul 02841, South Korea (sw.lee@korea.ac.kr)

Corresponding author: Cuntai Guan

of the frequently investigated protocols. Furthermore, by BCImonitored repetitive MI training, MI-BCI systems have also shown promising results in post-stroke motor rehabilitation [2], [4]. Therefore, owing to its high clinical relevance, EEGBCI literature contains many reports on decoding techniques to classify various MI classes with high accuracy. Classical machine learning techniques like linear and non-linear classiﬁers, nearest-neighbour classiﬁers as well as more data-driven techniques like neural networks and deep learning have been explored for this task of MI classiﬁcation [6]–[10].

Noisy and high dimensional data, high inter-trial variance, and scarcity of training data are among the key challenges faced by the EEG-BCI classiﬁers [11]. Furthermore, the intrinsic nature of MI and high intra-class variability in MI signature make the task of MI classiﬁcation even more difﬁcult. Owing to all these issues, the MI classiﬁcation is considered to be among the most challenging tasks in the BCI domain [12], [13]. The existing works on MI classiﬁcation can be grouped into two approaches; the classical machine learning approaches, and deep learning based approaches.

The classical machine learning approaches have commonly focused on the extraction of neuro-physiologically sound features from EEG data to achieve higher classiﬁcation accuracies. These algorithms generally employ a multistage approach wherein the EEG data is ﬁrst preprocessed to reduce the noise and then neurophysiologically sound features are extracted from the data to enhance SNR and reduce dimensionality. Neuroscientiﬁc studies have documented that MI elicits characteristic EEG activation patterns known as sensory-motor rhythms (SMR). SMRs are generally observed at the contralateral and ipsilateral sensory-motor regions in the form of a time-locked, event-related desynchronization/ synchronization (ERD/ERS) [1]. It is also known that different classes of MI differ in the spectro-spatial distribution of SMRs [1]. By extracting these features, algorithms like Filter Bank Common Spatial Patterns (FBCSP) [6], as well as Riemannian geometry based methods [14] have achieved high accuracies in this scenario of limited and noisy EEG training data. However, they still suffer from the high susceptibility to intra-trial variance and have a high dependence on handcrafted features.

In recent years, deep learning, which is an extensively data-driven approach to classiﬁcation has shown very promising results in the EEG classiﬁcation domain. Deep learning methods offer unique advantage of end-to-end processing capability and they eliminate the need for handcrafted feature extraction. Therefore, deep learning architectures, particularly based on Convolutional Neural Network (CNN), have gained

ii

popularity in the BCI domain due to their ability of effectively learning the local connectivity patterns from the given data [7]–[10]. These architectures have outperformed the classical machine learning techniques, but improvements achieved are still marginal [7]–[10]. These marginal improvements can be attributed to the scarcity of training data and the high feature dimensionality of the MI signals which together result in heavy overﬁtting of deep learning models and create unique challenges for adaptation of these methods in the BCI ﬁeld [13]. Considering these advantages and limitations of deep learning and classical machine learning methods, hybrid methods may hold the potential to achieve the best classiﬁcation accuracies in the MI-BCI ﬁeld.

Furthermore, although stroke patients are among the mostimportant target population, exploration of deep learning techniques for MI classiﬁcation is still largely limited to the data from healthy people. Alteration of brain dynamics, changes in EEG brain rhythms, and modiﬁcations in motor function control are some of the known effects following stroke [15]– [17]. Furthermore, it has been documented that close to 13% stroke patients can not control the MI-BCI using classical machine learning techniques [18]. Therefore, it is necessary to investigate how deep learning architectures perform in the stroke population and if they can extend the technology of MI-BCI to more patients by achieving better classiﬁcation accuracy. One initial report indicates that deep learning architectures may perform worse than classical machine learning techniques in stroke patients, but this result needs further veriﬁcation with data from a large stroke population [19].

Lastly, the use of deep learning in patient population also greatly necessitates interpretability of the classiﬁcation decisions. In stroke patients, since the aim is to restore brain activation to a healthy state, it is important to evaluate the information encoded by the neural network. Therefore ease of decision explanation is another important parameter when it comes to patients’ data.

Considering all the above challenges, in this paper, we propose Filter-Bank Convolutional Network (FBCNet), which is a novel end-to-end CNN architecture for subject-speciﬁc MI classiﬁcation. In FBCNet architecture we take a hybrid approach; we leverage the recent advances in deep learning technologies and mitigate their shortcomings by encoding the neurophysiological priors of MI in the architecture design. FBCNet encodes spectro-spatial discriminative information associated with the MI with the help of spectral ﬁltering of the EEG and CNN based spatial ﬁltering. Next, we propose a novel Variance layer for effective extraction of distinct MI signatures encoded by the temporal ﬂuctuations and dimensionality reduction, which results in extremely compact architecture. While being simple and interpretable, FBCNet also offers signiﬁcantly higher classiﬁcation results. The preliminary results of MI classiﬁcation using this network are presented in [20]. In this paper, we further investigate the classiﬁcation superiority of FBCNet over other deep learning architectures and FBCSP with the help of two publicly available datasets of MI classiﬁcation. The analysis is further extended to two MI datasets covering a total of 71 chronic stroke patients. In addition, using explainable AI techniques, we discuss the

difference between the data from healthy and stroke patients in the context of MI classiﬁcation. Following are the main contributions of this paper:

- • A compact and neurophysiologically inspired CNN architecture named FBCNet is proposed for MI classiﬁcation.
- • A novel Variance layer is proposed for effective extraction of EEG temporal information and parameter reduction.
- • We present one of the ﬁrst reports on the comparison between classical machine learning algorithms and deep learning architectures for MI decoding in a large population of chronic-stroke patients.
- • We present one of the ﬁrst reports on the effectiveness of deep learning architectures for MI decoding in a large population of chronic-stroke patients.
- • We show that, for stroke patients, classical machine learning approaches may outperform the general-purpose deep learning architectures and careful fusion of deep learning methods and neurophysiological knowledge of MI, as done in FBCNet, can achieve the best classiﬁcation accuracies for both healthy subjects and stroke patients.

The PyTorch implementation of the FBCNet is available at https://github.com/ravikiran-mane/FBCNet.

II. RELATED WORKS

Many classical machine learning techniques have been proposed for EEG-MI classiﬁcation and an extensive summary of them can be found in [12]. Among them, FBCSP is one of the most successful algorithms [6] and it shares a similar design philosophy as that of FBCNet. Therefore, we directly compare the results of FBCNet with FBCSP.

In recent years, many deep learning architectures have also been proposed for use in the EEG-BCI domain [7]–[10], [21]. Among them, Deep ConvNet [7] and EEGNet [9] are two architectures that have seen widespread adaptation in the EEG community and have provided open-source code implementations. Therefore, we use these two architectures to compare against the FBCNet in all the evaluation datasets. Lastly, we compare the performance of FBCNet against many recent architectures based on their reported accuracies on the BCI competition IV-2a dataset.

III. METHODOLOGY A. Proposed Architecture : Filter-bank Convolutional Net

FBCNet is designed with the aim of effectively extracting the spectro-spatial discriminative information, which is the signature of MI while avoiding the problem of overﬁtting in the presence of small datasets. At its core, FBCNet architecture is composed of the following four stages:

- 1) Multi-view data representation: The multi-view representation of the EEG data is obtained by spectrally ﬁltering the raw EEG with multiple narrow-band ﬁlters.
- 2) Spatial transformation learning: The spatial discriminative patterns for every view are then learned using a Depthwise Convolution layer.
- 3) Temporal feature extraction: Following spatial transformation, a novel Variance layer is used to effectively extract the temporal information.

iii

[Figure 1]

- Fig. 1. Proposed network architecture: FBCNet. (C: number of EEG channels, T: number of time points, Nb: number of frequency bands, m: number of convolution ﬁlters per frequency band, Nc: number of output classes)

4) Classiﬁcation: A fully connected (FC) layer ﬁnally classiﬁes features from the Variance layer into given classes.

The multi-view EEG representation followed by the spatial ﬁltering allows extraction of spectro-spatial discriminative features and the Variance layer provides a compact representation of the temporal information. With this brief design philosophy, this sub-section provides details of the FBCNet architecture which is presented in Fig. 1 and summarized in supplementary material Table S1.

1) Spectral Localization by Multi-view Data Representation: Consider a single-trial raw EEG data represented as x ∈ RC×T and its corresponding label y ∈ {0,1,..,Nc − 1}, where C represents number of EEG channels, T represents time points and Nc is total number of distinct classes.

It is known that MI related information in EEG data is spectrally localized with most information being present in the mu (8-12 Hz), and beta (12-32Hz) bands [1]. Therefore, to localize this discriminative information, in its ﬁrst stage, FBCNet creates a multi-view representation of the broad-band EEG data wherein each view represents a narrow-band localized EEG. The multi-view representation, xFB ∈ RNb×C×T, is generated by spectrally ﬁltering the raw EEG x with a ﬁlter bank F = {fi}Ni=b1 consisting of Nb number of narrow-band temporal ﬁlters. Following the ﬁltering operation, the timeseries along the third dimension of xFB becomes spectrally localized. Therefore,

xFB = F ⊗x ∈ RNb×C×T (1) Where, ⊗ indicates bandpass ﬁltering operation.

The ﬁlter bank F can consist of any number of ﬁlters with varying cut-off frequencies. In this particular work, the ﬁlter bank is constructed using Nb = 9 ﬁlters with non-overlapping frequency bands, each of 4Hz bandwidth, spanning from 4 to 40 Hz (4-8, 8-12, ..., 36-40 Hz). The ﬁltering is done using the Chebyshev Type II ﬁlter with a transition bandwidth of 2Hz and a stopband ripple of -30dB. This selection of ﬁlter bank was motivated by the traditional division of EEG in neurologically signiﬁcant spectral bands that was proposed in the FBCSP algorithm and it has been shown to achieve good classiﬁcation accuracies across multiple works [3], [6], [22].

2) Spatial Localization by CNN: Following the deterministic spectral localization, spatial localization of EEG discriminative features is achieved by a Spatial Convolution Block

(SCB) comprising of a Convolution layer, a Batch Normalization layer [23] and a Swish nonlinearity [24]. FBCNet uses a Depthwise Convolution layer [25] of kernel size = (C,1) for learning spatially discriminative patterns. Also, the use of Depthwise Convolutions results in each of these ﬁlters being associated with EEG from only one frequency band and, the depth parameter, m, controls the number of spatial ﬁlters per frequency band. Also, the Convolution kernel that is sized to span across all the channels effectively acts as a spatial ﬁlter. Following the CNN layer, we apply Batch-normalization along the feature map dimension before applying the Swish nonlinearity. We also regularize each convolutional kernel by using a maximum norm constraint of 2 on its weights; ||w||2 < 2 (weight-normalization). Effectively, SCB outputs m × Nb time-series xSCB ∈ R(m×Nb)×1×T which are spectrospatially localized. In the default FBCNet structure, we set the value m to be equal to be 32. We also evaluate the effect of different values of m on model performance in ablation analysis.

3) Temporal Feature Extraction by Variance Layer: The raw EEG data generally contains a large number of features along the time dimension and these features present the most amount of intra-class variance and high noise content. Therefore, to avoid overﬁtting of classiﬁcation models, it is necessary to reduce the time dimensional features by effective extraction of the most relevant temporal information. Max or Average Pooling strategies are the most commonly employed techniques for this purpose of reduction in feature dimensions [7], [9], [21]. However, considering that various classes of MI differ in their spectral power (ERD/ERS), a variance operation, which represents the spectral power in the given time series becomes a more suitable option for EEG temporal characterization. Therefore, for effective extraction of temporally discriminative information, we propose a novel Variance layer that characterizes a time series by computing its variance. So, in the forward pass, for any time-varying signal, g(t), the output of the Variance layer is given by,

1 T

v = Var(g(t)) =

T−1

#### ∑

(g(t)−µ)2 (2)

t=0

where, T is total number of time-points and µ is the mean of g(t).

iv

The effect of the Variance layer is yet more signiﬁcant for the EEG data during the learning phase (backpropagation) of the neural network using gradient descent optimization. In the backpropagation phase, the learnable parameters of the network are updated based on the gradient of the loss function.

So, for any network, if Lv = ∂∂Lv is the incoming loss at the variance layer then the backpropagated loss from this layer

with respect to the input g(t), Lg(t), is given by,

∂L ∂g(t)

∂L ∂v ·

∂v ∂g(t)

2 T

(g(t)−µ) (3) ∴ Lg(t) ∝ g(t)−µ

Lg(t) =

= Lv

=

As it can be observed from (3), the backpropagated loss from the Variance layer is proportional to the deviation of g(t) from the mean of the signal. Therefore, the Variance layer provides more importance to the signal points which are away from the mean by assigning a higher proportion of the incoming gradient to these points. This also aligns with the characteristics of EEG wherein the deviation from the mean, in a form of ERD or ERS is a distinct signature of MI.

Considering the suitability of the proposed Variance layer for EEG data, it was used for effective temporal features extraction in FBCNet. The output of SCB is passed to a Variance layer and it computes the temporal variance of the individual time-series in non-overlapping windows of size w, as given by (4) in the forward pass.

(k+1)∗w−1

1 w

#### ∑

(xSCB(i, j,t)−µ(i, j,k))2 (4)

xV(i, j,k) =

t=w∗k

where, µ(i, j,k) is the temporal mean of xSCB(i, j,t) within the kth window.

As it can be observed, the application of Variance layer across the entire time-duration reduces the number of features from (m×Nb×T) to (m×Nb×T/w) resulting in a high degree of feature reduction. In this work, the window length, w, was set to be 1s. Furthermore, the effect of different values of w on model performance was evaluated in ablation analysis.

4) Classiﬁcation: Finally, the features extracted by the Variance Layer are passed through a log activation and are then provided to an FC layer with linear activation. The output of the FC is then passed to the softmax layer to get the output probabilities of each class. The FC layer weights are also regularized by using a maximum norm constraint of 0.5; ||w||2 < 0.5 (Weight-normalization).

B. Evaluation Datasets

In the BCI domain, extreme inter-subject variability is observed in the classiﬁcation performance of different algorithms. Therefore, for robust comparison of the performance, we tested the FBCNet on the following four diverse EEG-MI datasets:

- 1) BCIC-IV-2A Data: A 4 class MI data from BCI Competition IV Dataset 2A [26].
- 2) OpenMBI Data: A 2 class MI data from Korea University EEG dataset [27].
- 3) Stroke Data: A: A 2 class MI vs rest dataset [4].

4) Stroke Data: B: A 2 class MI vs rest dataset [28].

Among these datasets, the BCIC-IV-2A Data [26] and the OpenMBI Data [27] contain the EEG data collected from healthy people. Moreover, these two datasets are publicly available and many state-of-the-art classiﬁcation algorithms have used these datasets as a benchmark. Since application to post-stroke motor rehabilitation is also the focus of this paper, we include two big datasets, Stroke Data: A and Stroke Data: B, containing the MI data from chronic-stroke patients in the analysis. The Stroke Data: A is collected as a part of a clinical trial that investigated the combined effect of BCI-mediated rehabilitation and transcranial Direct Current Stimulation (tDCS) in chronic stroke patients [4]. The Stroke Data: B is collected as a part of another clinical trial investigating the efﬁcacy of BCI-mediated upper extremity motor rehabilitation in chronic stroke patients [28]. Altogether, the proposed architecture was evaluated on MI-EEG data from 63 healthy people and 71 stroke patients. All the analyses in this work were performed on 0-4 seconds post-cue data.

The most important dataset characteristics are summarized in Table I and more detailed data description is provided in supplementary material section S2.

C. Experiments

To evaluate the performance of FBCNet a Cross-Validation (CV) and a Hold Out (HO) analyses were conducted.

The CV analysis was conducted in a 10 fold setting, with the 9 folds being used for training and 1 fold for testing. The folds were constructed by a sequential, class-balanced allocation of trials and this allocation was maintained constant for the entire analysis. The complete data from Stroke Data: A and Stroke Data: B datasets, and session 1 data from BCICIV-2A and OpenBMI datasets were used in CV analyses. We did not use the inter-session data in the CV analysis to avoid the confounding inﬂuence of inter-session variability which is a known problem in the BCI domain.

To understand the effect of inter-session variability on the classiﬁcation performance we conducted a subject-speciﬁc, inter-session, HO analysis for the BCIC-IV-2A Data and OpenBMI Data. In HO analysis, the complete data from session 1 for the given subject was used for the training purpose, and the resulting model was tested on the session 2 data. This analysis provides information about algorithms’ capabilities in extracting highly generalizable discriminative features which remain valid during inter-session classiﬁcation.

In this manner, the performance of FBCNet was compared with one classical machine learning algorithm of FBCSP-SVM [6], and two state-of-the-art CNN architectures namely, Deep ConvNet [7], and EEGNet-8,2 [9]. All the methods were used in the most optimal settings as recommended by the respective authors, and the detailed settings for each of these algorithms are provided in the supplementary material section S3.

D. Training Procedure

The same training procedure was followed for FBCNet, Deep ConvNet, and EEGNet-8,2. Architectures were trained using Adam optimizer at default settings (learning rate =

v

TABLE I DESCRIPTION OF EVALUATION DATASETS

Dataset Subject Type # of Subjects # of Sessions # Trials/Session # of Classes # of Channels # Time-points Analysis BCIC-IV-2A Data Healthy Subjects 9 2 288 4 22 1000 CV, HO OpenMBI Data Healthy Subjects 54 2 200 2 20 1000 CV, HO

- Stroke Data: A Stroke Patients 37 1 160 2 27 1000 CV
- Stroke Data: B Stroke Patients 34 1 160 2 27 1000 CV

CV: 10-fold Cross Validation on session 1 data, HO: Hold Out - training with session 1 data and test with session 2 data.

0.001, betas = 0.9,0.999 ) [29]. The log-cross-entropy loss was used for gradient updates. As proposed in [7], a two-stage training strategy was used wherein the training data was further divided into a training set and a validation set. In the ﬁrst stage, the model was trained using only the training set with the early stopping criteria whereby the validation set accuracy was monitored and training was stopped if there was no increase in the validation set accuracy for consecutive 200 epochs. After reaching the stopping criteria, network parameters with the best validation set accuracy were restored [7]. Starting from this model, the training procedure was continued in the second stage wherein the model was trained with the complete training data (train + validation set). The second stage training was stopped when the validation set loss reduced below the stage 1 training set loss. Lastly, to avoid the case of inﬁnite training in the situation of non-convergence, the maximum number of training epochs were limited to 1500 and 600 for training stage 1 and 2 respectively. In the CV analysis, the data from 1 among the 9 training folds was separated as a validation set. In the HO analysis, 20% of the training data was set aside as a validation set. In both the CV and HO analysis the test fold/set was never used in any of the training steps.

E. Interpretability and Visualizations

The adaption of deep learning in the medical domain necessitates some form of explanation for models’ decisions. Therefore, to understand the EEG features which the FBCNet learned to pay attention to, and to explore the difference between the data from healthy subjects and stroke patients, a method of DeepLift with the Rescale rule [30], [31] was employed. The DeepLift algorithm calculates the relevance of every input feature on the resulting classiﬁcation decision for each trial. In this analysis, from the training data, we used an average of all trials belonging to one class as a reference to the DeepLIFT algorithm and computed the singletrial relevance for every trial from the other class. Next, the subject-level relevance of input signals was calculated by averaging the normalized absolute per-trial relevance over all the trials. The extracted relevance was then used to infer the importance given by the trained model to a particular set of EEG channels and frequency bands. Finally, to summarize the properties of data from stroke patients and healthy subjects, a dataset-level relevance analysis was conducted. Here, the trained FBCNet models form the subjects with classiﬁcation accuracy > 70% from the OpenBMI Data and Stroke Data:

- A and Stroke Data: B (combined together as Stroke Data) were analyzed. We present the relevance scores from subjects

with classiﬁcation accuracy > 70% because they represent robustly trained models which have encoded the information that generalizes on the test data. Moreover, a small percentage of subjects are known to be BCI-illiterate, that is, these subjects can not generate class discriminative MI-EEG patterns and this is another reason for the exclusion of subjects with accuracy <70% for the interpretability analysis [27].

F. Statistical Analysis

The statistical signiﬁcance of differences in classiﬁcation accuracy achieved by different algorithms was assessed using a Wilcoxon signed-rank test for BCIC-IV-2A Data (small sample size) and paired t-test for the remaining three datasets. Furthermore, to control the family-wise error rate, p-values were corrected with Bonferroni correction for multiple comparisons.

IV. RESULTS A. Classiﬁcation accuracy

Result I: FBCNet achieved signiﬁcantly better classiﬁcation accuracies compared to baseline methods

Table II presents complete classiﬁcation results for all datasets using all the methods. From Table II, it can be observed that FBCNet achieved the best classiﬁcation performance across all datasets in both CV and HO analysis. The maximum accuracy improvement of 10% was observed between FBCNet and FBCSP-SVM for CV analysis on the OpenBMI dataset. Furthermore, the FBCNet achieved a new SOTA of 76.20% 4 class classiﬁcation accuracy on the BCICIV-2A Data in the HO settings. Also, in most datasets, the improvement in accuracy achieved by FBCNet over baseline methods was statistically signiﬁcant (Table II). More detailed classiﬁcation results are presented in the supplementary material section S4.

Result II: FBCNet matched the performance of best performing baseline method for most subjects

Following the analysis of classiﬁcation accuracies averaged over all subjects, the performance of all algorithms for every subject was investigated. As an example, Fig. 2 presents the 10-fold CV accuracies for all subjects in OpenBMI Data. Here, a signiﬁcant difference was observed in the classiﬁcation accuracies achieved by different algorithms for each subject. In particular, both baseline deep learning methods, Deep ConvNet, and EEGNet-8,2, resulted in similar accuracies, which were signiﬁcantly different from the accuracies achieved by the classical machine learning approach of FBCSP-SVM (paired t-test, p < 0.05). Moreover, it was observed that deep learning architectures performed far better than the classical

vi

TABLE II AVERAGE SUBJECT-SPECIFIC CLASSIFICATION ACCURACY

Dataset Test Conﬁguration FBCSP-SVM Deep ConvNet EEGNet-8,2 FBCNet

BCIC-IV-2A Data 10-fold cross validation 75.89 72.20 73.13 79.03 OpenBMI Data 10-fold cross validation 64.61** 68.33** 70.89 74.70 Stroke Data: A 10-fold cross validation 71.37** 68.81** 69.15** 79.16 Stroke Data: B 10-fold cross validation 74.14** 71.11** 73.47** 81.11 BCIC-IV-2A Data Hold out test set 68.06* 72.22 73.15 76.20 OpenBMI Data Hold out test set 60.36** 60.77** 63.63 67.19

The best performing method for each analysis is highlighted in boldface. The *, and ** represent that the classiﬁcation performance of FBCNet is signiﬁcantly better than the given baseline method with *: pcorrected < 0.05 and, **:pcorrected < 0.01.

[Figure 2]

- Fig. 2. Classiﬁcation accuracy for each subject from OpenBMI Data in 10-fold cross-validation settings (sorted by FBCSP-SVM acc.). It can be observed that deep learning architectures (Deep ConvNet, EEGNet-8,2) performed far better than FBCSP-SVM, the classical approach, for subjects with FBCSP-SVM accuracy <70%. On the other end of the spectrum, the performance of deep learning architectures was far worse than that of FBCSP-SVM in subjects with FBCSP-SVM accuracy >70%. Here, in contrast, FBCNet matched the performance of the best performing method for most of the subjects resulting in the best subject averaged classiﬁcation accuracy. A similar trend was observed in other datasets as well.

TABLE III AVERAGE CLASSIFICATION ACCURACIES FOR 25% SUBJECTS WITH HIGHEST AND LOWEST CROSS VALIDATION ACCURACY IN EACH DATASET

Top 25% Bottom 25%

Dataset

FBCSP-SVM Deep ConvNet EEGNet-8,2 FBCNet FBCSP-SVM Deep ConvNet EEGNet-8,2 FBCNet OpenBMI Data 90.11 84.79 87.43 93.75 48.00 54.50 54.61 57.60

- Stroke Data: A 90.46 83.71 84.96 95.06 53.23 53.74 52.28 59.52
- Stroke Data: B 89.53 82.05 84.21 93.14 53.55 61.88 65.00 67.22

approach, for subjects with FBCSP-SVM accuracy <70%. Conversely, the performance of deep learning architectures was worse than that of FBCSP-SVM in subjects with FBCSPSVM accuracy >70%. In contrast to all baselines, as can be observed from Fig. 2, FBCNet matched the performance of the best performing method for most subjects resulting in the best average classiﬁcation accuracy. A similar but statistically insigniﬁcant trend was observed in other datasets as well.

To quantitatively investigate this pattern, we analyzed the average classiﬁcation accuracy for 25% subjects with the highest and lowest CV accuracy in each dataset (Table III). Here, the average classiﬁcation accuracies of top 25% subjects for FBCSP-SVM were observed to be signiﬁcantly higher than that of Deep ConvNet, and EEGNet-8,2 (t-test, all p < 0.05 except pFBCSP−EEGNet for OpenBMI Data) and the accuracy for FBCNet was even better than that of FBCSP-SVM. For the

bottom 25% subjects, FBCSP-SVM was observed to perform worse than deep learning algorithms (all p < 0.01 except Stroke Data A) and the FBCNet achieved the highest average accuracy for this class of subjects as well.

Result III: Highest number of subjects achieved >70% accuracy with FBCNet

In the BCI ﬁeld, a system with > 70% 2-class classiﬁcation accuracy is generally considered to be usable by healthy subjects and stroke patients [32]. Therefore, the number of subjects for whom the classiﬁcation algorithm managed to achieve at least 70% CV accuracy were analyzed and the results are presented in Table IV. Among baseline methods, EEGNet-8,2 resulted in the most number of subjects being able to achieve >70% accuracy for OpenBMI Data. Contrarily, for both stroke datasets, FBCSP-SVM resulted in the most number of subjects with >70% accuracy. Better than all baseline

vii

TABLE IV NUMBER OF SUBJECTS WITH CV CLASSIFICATION ACCURACY > 70%

Total Subjects

Deep ConvNet

FBCNet

FBCSPSVM

EEGNet8,2

Dataset

OpenBMI Data 54 17 21 27 33

- Stroke Data: A 37 20 18 19 28
- Stroke Data: B 34 23 16 22 27 Stroke Data (A+B) 71 43 34 41 55

[Figure 3]

- Fig. 3. The sensitivity of classiﬁcation algorithms to small training sets. Here, the effect of a small amount of data on the test accuracy is evaluated using the BCIC-IV-2A Data for various algorithms. A fraction of the training data (xaxis) is used to train a model, which is tested on data from an independent test session. It can be observed that the baseline deep learning architectures (Deep ConvNet and EEGNet-8,2) are highly sensitive to the small training sets, whereas the classical approach of FBCSP-SVM is relatively less susceptible. The proposed method (FBCNet) matches the accuracy achieved by deep learning methods in the presence of ample training data while retaining relatively better performance even when the training set is small. The error bars represent a standard mean error.

methods, for all datasets, FBCNet was able to achieve >70% accuracy for the most number of subjects. Compared to the best baseline method (FBCSP-SVM), FBCNet resulted in 28% more stroke patients (Stroke Data: A+B) with >70% accuracy.

Result IV: FBCNet was least affected by datasets with fewer training samples

The sensitivity of the classiﬁcation algorithm to fewer training samples was evaluated using the separate test session data from BCIC-IV-2A Data in the HO analysis. Here, all the algorithms were trained using various fractions of the training dataset ranging from 20% to 100% in steps of 10%. Trained models were then tested on a separate session 2 data and the test accuracy was analyzed as a function of training data percentage. Results of this analysis are presented in Fig. 3. Here, both baseline deep learning architectures were observed to be highly sensitive to small training sets with an accuracy drop of almost 35% when the number of training trials was reduced to 20%. Contrarily, FBCSP-SVM was least affected by a reduction in the training set. In fact, the drop in accuracy using FBCSP-SVM only became statistically signiﬁcant when the portion of training samples was reduced to 30%. Fur-

[Figure 4]

Fig. 4. FBCNet cross validation classiﬁcation accuracies with different temporal feature extraction layers (mean±std). Temporal feature extraction using Variance layer resulted in best classiﬁcation accuracies across all datasets.

thermore, compared to both Deep ConvNet and EEGNet-8,2, better classiﬁcation accuracies achieved by FBCSP-SVM were statistically signiﬁcant when training data was reduced below 50%. However, the maximum accuracy achieved by FBCSPSVM, when using the complete training data was much lower compared to these baseline deep learning methods (Table II). Different from FBCSP-SVM, at 100% of the training data, the best accuracy was achieved by FBCNet. Moreover, the accuracy curve of FBCNet closely followed the characteristics of FBCSP-SVM with a similar sensitivity to the reduced training set as that of FBCSP-SVM.

Result V: Temporal feature extraction using Variance layer resulted in signiﬁcantly better classiﬁcation accuracies

To analyze the contribution of the novel Variance layer in the improved results achieved by FBCNet, we investigated the effect of different temporal feature extraction layers on classiﬁcation accuracies and Fig. 4 presents these results. Among all the temporal feature extraction layers, FBCNet with the Variance layer achieved the highest classiﬁcation accuracies in all analyses. Feature extraction using the Average and Max layer resulted in consistently worse accuracies across all datasets, and compared to the Variance layer, these differences were statistically signiﬁcant (all p < 0.05 expect for BCICIV-2A Data).

Result VI: Increasing the number of spatial ﬁlters and reducing the window size in FBCNet architecture resulted in marginally improved classiﬁcation results

The average classiﬁcation accuracy achieved by FBCNet on the Stroke Data: A with a different number of spatial ﬁlters and window lengths is presented in Fig. 5. In this analysis, increasing the number of spatial ﬁlters and decreasing the window size initially produced increased accuracy. However, too many spatial ﬁlters and too small window sizes resulted in reduced classiﬁcation accuracy. Also, the computational complexity of FBCNet was linearly proportional to the number of spatial ﬁlters and inversely proportional to the window size. Therefore, changes in these parameters resulted in FBCNet with more learnable parameters and longer training times.

viii

[Figure 5]

- Fig. 5. FBCNet cross-validation classiﬁcation accuracies with different number of spatial ﬁlters per frequency band (m) and variance window length (w).

TABLE V COMPARISON OF FBCNET WITH EXISTING METHODS FOR THE BCIC-IV-2A DATA (4-CLASS CLASSIFICATION %ACC. (KAPPA VALUE)).

Algorithm CV Test session

FBCSP [3] 74.72 (0.663) 67.75 (0.569) C2CM [8] 78.78 74.46 (0.659) Deep ConvNet [7] - 70.90 EEGNet [9] 70.00 RFNet [14] - 75.51 (0.673) MI-EEGNet [33] 77.49 74.61

FBCNet (proposed) 79.03 (0.720) 76.20 (0.683)

- B. Interpretability and visualizations

Result VII: Greater inter-subject variability in the relevance patterns was observed for stroke patients

To understand general trends in the relevance patterns learned by the FBCNet model across subjects and to explore if the data from stroke patients is any different from healthy subjects, a group-level relevance analysis we performed and its results are presented in Fig. 6.

First, subject-averaged relevance patterns (Fig. 6 (a)) at all frequency bands and EEG channels for stroke patients’ and healthy subjects’ data were inspected. For healthy subjects, the 12-16Hz and 8-12Hz were observed to be the two most relevant frequency bands and they constituted 34% of the total input relevance averaged across all subjects. Also, the channel relevance in these two frequency bands was most concentrated at the left and right motor areas of the brain (C3, C4). All these characteristics were closely associated with the known MI signatures. In stroke patients, the averaged relevance patterns were observed to be more diffused and all the frequency bands in the 4-24Hz range resulted in similar input relevance. Moreover, the channel relevance patterns in these frequency bands were also much more diffused and many channels received similar total relevance scores. Yet, the C4, CP4 and, P4 channels in the 8-12Hz range, C3, C4, and CP4 channels in the 12-16Hz range, and F7 and F8 channels in the 4-8Hz range, were observed to have slightly higher relevance

than other channels.

Next, the channel-frequency band relevance patterns for each healthy and stroke subject were visually inspected. Here, for most healthy subjects, the 8-12 Hz frequency band was observed to be highly relevant whereas the most relevant frequency range largely differed across stroke patients. To concisely visualize this difference, a heat-map of ﬁlter band relevance for healthy and stroke subjects was plotted and it is presented in 6 (b). From the heatmap, as well as the normalized histogram, the 12-16Hz was observed to be the frequency band with the highest relevance in half of the healthy subjects. Contrarily, for stroke patients, no single highly relevant frequency band could be identiﬁed, and the most relevant frequency band was highly subject-speciﬁc. Moreover, for each stroke patient, the input relevance was distributed across multiple frequency bands, and the difference in the relevance of the ﬁrst and the second most relevant frequency band was quite low. Furthermore, this difference was signiﬁcantly different from healthy subjects’ data (independent samples t-test, p < 0.05).

V. DISCUSSION

In this paper, we proposed FBCNet, a novel, neurophysiologically inspired, end-to-end CNN architecture for MI classiﬁcation that can learn generalizable discriminative features in the presence of limited data and produce better classiﬁcation accuracies. We evaluated FBCNet against the state-of-the-art classical machine learning and deep learning approaches using EEG-MI data from a large corpus of healthy subjects (n = 54 + 9 = 63), and chronic stroke patients (n = 37 + 34 = 71). To the best of our knowledge, this is the ﬁrst work that compares the performance of deep learning approaches with classical machine learning methods for such a large population of healthy and stroke subjects. Besides the differences in the classiﬁcation accuracies, using interpretability analysis, this work also presented some of the key differences in stroke patients and healthy subjects data from the perspective of MI classiﬁcation. Next, we showed that the use of a hybrid approach, as done in FBCNet, which leverages the complex feature learning capabilities of deep learning methods and mitigates their sensitivity to small datasets by incorporating the neurophysiological priors for MI classiﬁcation in the architecture design may lead to signiﬁcant improvements in MI-BCI classiﬁcation accuracies. We contemplate that, the three-stage approach of the spectral, spatial, and temporal localization of EEG features in FBCNet, has resulted in an architecture that is constrained enough that it effectively focuses on neurophysiological signatures of MI even in the absence of large training data while being ﬂexible enough to efﬁciently handle the intra-class variability in EEG trials. Therefore, striking a balance between model complexity (more trainable parameters to extract deeper encoded generalizable patterns) and constraints (neurophysiologically reasonable patterns) can be the way to successfully adapt deep learning methods into the BCI domain.

ix

[Figure 6]

- Fig. 6. Group level relevance analysis for healthy subjects and stroke patients. Part (a) presents the subject-averaged channel-frequency input relevance patterns for healthy subjects and stroke patients. The number in the title is the percentage relevance for the given frequency band. The input relevance is highly concentrated in the 8-16Hz frequency range at the C3 and C4 channels for healthy subjects whereas the relevance patterns for stroke subjects are highly diffused. Investigating more on the subject-averaged relevance, Part (b) presents the heatmap of frequency band relevance for each subject. Also, the histogram in the center presents a normalized count of subjects for whom the given frequency band has the highest relevance. For healthy subjects, the 8-16 Hz frequency range has consistently high relevance whereas the most relevant frequency range largely differed across stroke patients.

A. Performance of classical machine learning methods and state-of-the-art deep learning architectures

In our experiments, there was no statistically signiﬁcant difference between the subject-averaged classiﬁcation accuracy achieved by FBCSP (classical machine learning method) and Deep ConvNet, EEGNet-8,2 (deep learning methods) for all but one analysis and these results are in line with the previous literature [7], [9], [19], indicating that the deep learning architectures are yet to present substantial improvements in the EEG domain. Furthermore, although statistically insigniﬁcant, FBCSP was observed to be the best performing baseline method for both stroke subjects’ datasets and a reversed trend was observed for the healthy subjects’ data from the OpenBMI dataset. These results may have been caused by different amounts of training data present across these datasets. Both stroke datasets had 20% fewer training trials as compared to the OpenBMI dataset (160 vs 200 trials/subject) and this reduction in training data may have affected the performance of deep learning architectures on a larger scale as compared to its impact on the FBCSP. This hypothesis was also further supported by the results of variable training data analysis performed on the BCIC-IV-2A Data (Fig. 3) wherein, compared to FBCSP, the accuracy of existing deep learning methods dropped signiﬁcantly when trained with the reduced amount of data. This indicates that in the absence of adequate training data, the general-purpose deep learning architectures may result in worse classiﬁcation accuracies.

Furthermore, although, the difference in the amount of training data can account for dataset-level differences in classiﬁcation accuracies of the baseline architectures, it can not explain

the large differences in classiﬁcation performance of these algorithms for individual subjects. As observed from Fig. 2, for most subjects, the classiﬁcation accuracy differed signiﬁcantly between FBCSP and baseline deep learning methods. Here, we observed a general pattern that FBCSP resulted in extreme (very high or low) classiﬁcation accuracies for most subjects, and contrarily, average classiﬁcation accuracies were achieved by most subjects using Deep ConvNet and EEGNet-8,2. Intersubject variability in the EEG data distributions can be one possible explanation for these observed differences. It is probable that the neurophysiologically constrained model of FBCSP is inadequate for subjects with high intra-class variability and non-standard MI-EEG patterns, and more complex deep learning models may achieve relatively better accuracy for these subjects by learning some of those complex patterns. However, this additional ﬂexibility in the deep learning architectures may also be detrimental to their performance in subjects with better class discriminative features. In this case, particularly with the limited and noisy training data, deep learning architectures may end-up learning non-generalizable patterns leading to poor test set performance. This indicates that striking a balance between model complexity and constraints may beneﬁt all BCI users.

B. Classiﬁcation performance of FBCNet

FBCNet was designed to strike the balance between model capacity and complexity by incorporation of neurophysiological knowledge within the deep learning framework and this principle was hypothesized to results in a model that has optimal learning capacity while being less susceptible

x

to relatively small and noisy EEG data. The results using FBCNet strongly support this hypothesis wherein the FBCNet has resulted in best classiﬁcation accuracy across all datasets and this improvement in accuracy by FBCNet over baseline methods is statistically signiﬁcant for most datasets (Table II). Furthermore, in the analysis of individual subject classiﬁcation accuracies, we observed that FBCNet closely matched the performance of the best performing classiﬁcation algorithm for most subjects in the datasets (Fig. 2). Due to this, the average classiﬁcation accuracy of 25% best performing subjects by FBCNet was even better than that of FBCSP (Table III). Furthermore, the FBCNet achieved the best average classiﬁcation accuracy for worst performing 25% subjects (Table. III), and this consequently resulted in the most number of subjects being able to control the BCI with >70% classiﬁcation accuracy using FBCNet (Table IV). Furthermore, we observed that the FBCNet is much less susceptible than baseline deep learning architectures to small training sets (Fig. 3) indicating that the neurophysiologically constrained architecture of FBCNet can more effectively learn the generalizable class-discriminative patterns and avoid overﬁtting in cases of limited training data. Moreover, unlike FBCSP, in the presence of ample training data, the FBCNet accuracies improved continuously indicating that FBCNet can also effectively utilize a higher amount of training data when it is available. All these results indicate that the incorporation of neurophysiological knowledge within the deep learning framework, as done in FBCNet, may lead to better MI classiﬁcation accuracies. Furthermore, a similar observation can be made from the existing literature wherein RFNet [14], which fuses Riemannian geometry with deep learning methods, held the record for best accuracy on the BCIC-IV-2A to date.

- C. Role of Variance Layer

The Variance layer for temporal feature extraction is another important contribution of this paper. The use of variance operation along the temporal dimension was motivated by the fact that variance of a ﬁltered signal represents the spectral power in the time-series, and spatio-temporal differences in EEG spectral power are known class-discriminative features of MI. Therefore, we hypothesized that variance may be a more suitable operation for temporal consolidation of EEG signals and this hypothesis was conﬁrmed by experimental results. In the ablation analysis of temporal feature extraction layer, we observed that FBCNet with Variance layer resulted in signiﬁcantly better performance than Average and Max layer which are the two most widely used feature reduction strategies in the deep learning ﬁeld (Fig. 4). Hence Variance layer might be better suited for temporal feature consolidation in deep learning networks designed for MI classiﬁcation.

- D. Effect of hyperparameter selection

The number of spatial ﬁlters per frequency band (m) and length of the variance window (w) are the two most important hyperparameters in the FBCNet architecture. These two parameters respectively control the spatial and temporal feature representation capacity of FBCNet, and together they set the

computational complexity and model capacity of FBCNet. Therefore, it is important to properly set the values of these parameters. Here, we observed that the m between 16 and 32 and w between 0.5s and 1s led to optimal performance on most datasets. Also, it was observed that more complex tasks like 4 class classiﬁcation in BCIC-IV-2A Data, beneﬁt from larger m values, indicating that such tasks need a higher model capacity to correctly learn the more complex data and FBCNet can easily accommodate this requirement. The observed optimal value of w between 0.5s and 1s is also neurophysiologically sound wherein the ERD/ERS patterns associated with MI are known to have a duration of 0.5s to 1s.

E. Interpretability Analysis

Interpretability of the knowledge learned by the neural network architecture is a necessity when used in clinical settings. In this work, we observed the FBCNet models learned to assign relevance to the EEG channels in the motor region of the brain (C3 and C4) in the 8-16Hz and 24-32Hz frequency range for healthy subjects (Fig. 6). This indicates that FBCNet could successfully focus on the neurophysiologically sound features because spectro-spatially discriminative patterns at the primary motor cortex in the alpha (8-12Hz) and high beta bands (23-30Hz) of EEG are well-known signatures of left vs right-hand MI [1]. Moreover, we observed that by encapsulating the true signatures of MI, these features also generalized well on the unseen test data which explained the higher classiﬁcation accuracies achieved by FBCNet.

In the interpretability analysis, we also investigated the possible differences in the class discriminative patterns between healthy subjects and stroke patients. Here, we observed consistent relevance patterns across multiple subjects with the highest relevance in the 8-16Hz and 24-32Hz frequency range at the motor region of the brain (C3, C4 channels) for healthy subjects data. These relevance patterns are in-line with the neurophysiological signatures of MI [1]. However, for stroke patients, these patterns showed large inter-subject variability, and they were also much more spatially and spectrally diffused for individual patients. These spectro-spatially spread relevance patterns in stroke patients may indicate that the damage in the brain caused by stroke may have resulted in compensatory recruitment of non-motor areas by the brain [34]. However, to further investigate this phenomenon, more data with distinct MI tasks from stroke patients is needed. Yet, the large inter-subject differences between the stroke patients’ relevance pattern can be attributed to stroke-induced subject-speciﬁc modiﬁcation in the brain, and therefore, the compensatory recruitment of non-motor areas is a plausible explanation for the spectro-spatially spread relevance patterns in stroke patients.

VI. CONCLUSION

This paper proposed a neurophysiologically motivated endto-end CNN architecture named FBCNet for subject-speciﬁc MI classiﬁcation that can learn generalizable discriminative features in the presence of limited data and produce better classiﬁcation accuracies. In this architecture, we proposed a

xi

hybrid approach for the task of MI classiﬁcation in which we leveraged the complex feature learning capabilities of deep learning methods and mitigated their sensitivity to small datasets by incorporating the neurophysiological priors of MI in the architecture design. This proposed approach achieved signiﬁcantly better classiﬁcation accuracies across four motor imagery datasets among which two were collected from chronic stroke patients. Moreover, with interpretability analysis, we demonstrated that improved performance by FBCNet was driven by the effective learning of neurophysiologically relevant EEG features. Furthermore, we showed that there are differences in the MI data between healthy subjects and stroke patients, and FBCNet can perform well on both healthy and patient data. Overall, the results indicate that inclusion of neurophysiological priors while designing deep learning architectures, as done in this work, will result in an architecture that is constrained enough that it can effectively focus on neurophysiological signatures even in the absence of large training datasets while being complex enough to effectively utilize a higher amount of training data when it is available, and such an approach may lead to better classiﬁcation results in the ﬁeld of MI-BCI.

ACKNOWLEDGMENT

This work was partially supported by the RIE2020 AME Programmatic Fund, Singapore (No. A20G8b0102), and the Institute of Information & Communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (No. 2017-0-00451, and No. 2019-0-00079). The computational work for this article was partially performed on resources of the National Supercomputing Centre, Singapore.

REFERENCES

- [1] G. Pfurtscheller, C. Brunner et al., “Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of different motor imagery tasks,” Neuroimage, vol. 31, no. 1, pp. 153–159, May 2006.
- [2] R. Mane, T. Chouhan, and C. Guan, “Bci for stroke rehabilitation: motor and beyond,” Journal of Neural Engineering, vol. 17, no. 4, p. 041001, 2020.
- [3] K. K. Ang, Z. Y. Chin et al., “Filter bank common spatial pattern algorithm on BCI competition IV datasets 2a and 2b,” Front. Neurosci., vol. 6, p. 39, Mar. 2012.
- [4] K. K. Ang, C. Guan et al., “Facilitating effects of transcranial direct current stimulation on motor imagery brain-computer interface with robotic feedback for stroke rehabilitation,” Arch. Phys. Med. Rehabil., vol. 96, no. 3, pp. S79–S87, 2015.
- [5] Y. Li, J. Long et al., “An EEG-Based BCI System for 2-D Cursor Control by Combining Mu/Beta Rhythm and P300 Potential,” IEEE Trans. Biomed. Eng., vol. 57, no. 10, pp. 2495–2505, Oct. 2010.
- [6] K. K. Ang, Z. Y. Chin et al., “Filter Bank Common Spatial Pattern (FBCSP),” 2008 Int. Jt. Conf. Neural Networks (IJCNN 2008), pp. 2391– 2398, 2008.
- [7] R. T. Schirrmeister, J. T. Springenberg et al., “Deep learning with convolutional neural networks for EEG decoding and visualization,” Hum. Brain Mapp., vol. 38, no. 11, pp. 5391–5420, 2017.
- [8] S. Sakhavi, C. Guan, and S. Yan, “Learning Temporal Information for Brain-Computer Interface Using Convolutional Neural Networks,” IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 11, pp. 5619–5629, Nov. 2018.
- [9] V. J. Lawhern, A. J. Solon et al., “EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces,” J. Neural Eng., vol. 15, no. 5, pp. 1–30, 2018.
- [10] O.-y. Kwon, M.-H. Lee et al., “Subject-Independent Brain-Computer Interfaces Based on Deep Convolutional Neural Networks,” IEEE Trans. Neural Netw. Learn. Syst., pp. 1–14, 2019.

- [11] R. P. N. Rao, Brain-Computer Interfacing: An Introduction. Cambridge University Press, 2013.
- [12] F. Lotte, L. Bougrain et al., “A review of classiﬁcation algorithms for EEG-based brain–computer interfaces: a 10 year update,” J. Neural Eng., vol. 15, no. 3, 2018.
- [13] Y. Roy, H. Banville et al., “Deep learning-based electroencephalography analysis: a systematic review,” J. Neural Eng., vol. 16, no. 5, Jan. 2019.
- [14] G. Zhang and A. Etemad, “RFNet: Riemannian Fusion Network for EEG-based Brain-Computer Interfaces,” arXiv, pp. 1–12, aug 2020.
- [15] L. A. Boyd, K. S. Hayward et al., “Biomarkers of stroke recovery: Consensus-based core recommendations from the Stroke Recovery and Rehabilitation Roundtable,” International Journal of Stroke, vol. 12, no. 5, pp. 480–493, Jul. 2017.
- [16] R. Mane, E. Chew et al., “Prognostic and Monitory EEG-Biomarkers for BCI Upper-Limb Stroke Rehabilitation,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 27, no. 8, pp. 1654–1664, Aug. 2019.
- [17] ——, “Quantitative eeg as biomarkers for the monitoring of post-stroke motor recovery in bci and tdcs rehabilitation,” in 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). IEEE, 2018, pp. 3610–3613.
- [18] K. K. Ang, C. Guan et al., “A Large Clinical Study on the Ability of Stroke Patients to Use an EEG-Based Motor Imagery Brain-Computer Interface,” Clin. EEG Neurosci., vol. 42, no. 4, pp. 253–258, Oct. 2011.
- [19] H. Raza, A. Chowdhury, and S. Bhattacharyya, “Deep Learning based Prediction of EEG Motor Imagery of Stroke Patients’ for NeuroRehabilitation Application,” in International Joint Conference on Neural Networks (IJCNN 2020), Glasgow, 2020.
- [20] R. Mane, N. Robinson et al., “A Multi-view CNN with Novel Variance Layer for Motor Imagery Brain Computer Interface,” in 42th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). IEEE, 2020.
- [21] N. Robinson, S.-w. Lee, and C. Guan, “EEG Representation in Deep Convolutional Neural Networks for Classiﬁcation of Motor Imagery,” in 2019 IEEE International Conference on Systems, Man and Cybernetics (SMC), Oct. 2019, pp. 1322–1326.
- [22] K. K. Ang, Z. Y. Chin et al., “Mutual information-based selection of optimal spatial-temporal patterns for single-trial EEG-based BCIs,” Pattern Recognit., vol. 45, no. 6, pp. 2137–2144, 2012.
- [23] S. Ioffe and C. Szegedy, “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift,” 32nd International Conference on Machine Learning, ICML 2015, vol. 1, pp. 448–456, Feb. 2015.
- [24] P. Ramachandran, B. Zoph, and Q. V. Le, “Searching for activation functions,” arXiv preprint arXiv:1710.05941, 2017.
- [25] F. Chollet, “Xception: Deep Learning with Depthwise Separable Convolutions,” Proceedings of 30th IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2017, pp. 1251–1258, 2017.
- [26] M. Tangermann, K. R. Müller et al., “Review of the BCI competition IV,” Front. Neurosci., vol. 6, pp. 1–31, 2012.
- [27] M. H. Lee, O. Y. Kwon et al., “EEG dataset and OpenBMI toolbox for three BCI paradigms: An investigation into BCI illiteracy,” GigaScience, vol. 8, no. 5, pp. 1–16, 2019.
- [28] K. K. Ang, C. Guan et al., “Brain-computer interface-based robotic end effector system for wrist and hand rehabilitation: results of a three-armed randomized controlled trial for chronic stroke,” Front. Neuroeng., vol. 7, p. 30, Jul. 2014.
- [29] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” arXiv preprint arXiv:1412.6980, 2014.
- [30] A. Shrikumar, P. Greenside, and A. Kundaje, “Learning important features through propagating activation differences,” 34th International Conference on Machine Learning, ICML 2017, vol. 7, pp. 4844–4866, 2017.
- [31] N. Kokhlikyan, V. Miglani et al., “PyTorch Captum,” https://github.com/pytorch/captum, 2019.
- [32] X. Shu, S. Chen et al., “Fast recognition of BCI-inefﬁcient users using physiological features from EEG signals: A screening study of stroke patients,” Front. Neurosci., vol. 12, p. 93, 2018.
- [33] M. Riyad, M. Khalil, and A. Adib, “MI-EEGNET: A novel convolutional neural network for motor imagery classiﬁcation,” Journal of Neuroscience Methods, vol. 353, apr 2021.
- [34] S. C. Cramer, “Repairing the human brain after stroke: I. Mechanisms of spontaneous recovery,” Ann. Neurol., vol. 63, no. 3, pp. 272–287, Mar. 2008.

### arXiv:2104.01233v1[cs.OH]17Mar2021

##### Supplementary material: FBCNet: A Multi-view Convolutional Neural Network for Brain-Computer Interface

Ravikiran Mane1 Efﬁe Chew2 Karen Chua3 Kai Keng Ang1,4 Neethu Robinson1 A. P. Vinod5 Seong-Whan Lee6 Cuntai Guan1

- 1Nanyang Technological University,Singapore
- 2National University Hospital, Singapore 3Tan Tock Seng Hospital, Singapore

4Institute for Infocomm Research, Agency for Science, Technology and Research (A*STAR), Singapore 5 Indian Institute of Technology, Palakkad, India 6 Korea University, Seoul, South Korea

Corresponding author: Cuntai Guan - ctguan@ntu.edu.sg

###### S1 FBCNet architecture

The design philosophy of FBCNet is explained in the main manuscript section II. Here, we provide implementation level details of FBCNet in Table S1.

Table S1: FBCNet architecture

Block Layer # Kernels Kernel Size # Parameters Output Options Spectral Filtering Input (1, C, T)

Filter-Bank (Nb, C, T)

Spatial Convolution Depthwise Conv2D m∗Nb (C, 1) m∗Nb*C + m∗Nb (m∗Nb, 1, T) depth = m, max L2 weightnorm = 2 BatchNorm 2*m∗Nb (m∗Nb, 1, T) Activation - ELU (m∗Nb, 1, T) ELU, ReLU, Leaky-ReLU

Temporal Feature Extraction

Variance Layer (1, w) (m∗Nb, 1, T/w) Variance, Average, Max

Classiﬁer Flatten m∗Nb ∗T/w Fully connected Layer Nc m∗Nb ∗T/w∗Nc +Nc Nc max L2 weightnorm = 0.5 Log-Softmax Nc

C: number of EEG channels, T: number of time points, Nb: number of frequency bands, m: number of convolution ﬁlters per frequency band, Nc: number of output classes, w: temporal window length

###### S2 Details of Evaluation Datasets The performance of FBCNet was tested on following four diverse datasets:

- 1. BCIC-IV-2A Data: A 4 class MI data from BCI Competition IV Dataset 2A [1].
- 2. OpenBMI Data: A 2 class MI data from OpenBMI dataset [2].
- 3. Stroke Data: A: A 2 class MI vs rest dataset [3].
- 4. Stroke Data: B: A 2 class MI vs rest dataset [4].

Further details of these datasets are as follows:

###### S2.1 BCIC-IV-2A Data

The BCIC-IV-2A Data consists of EEG data from 9 subjects collected over 2 sessions. The data contains 4 classes; MI of left, and right hands, feet, and tongue. The EEG data has been recorded using 22 electrodes with a sampling frequency of 250 Hz. There are 72 trials of every class in each session and every trial is of 4s duration. In our analysis, we used all the 22 channels the entire 4 seconds data.

###### S2.2 OpenBMI Data

OpenBMI Data contains 2 sessions of 2-class EEG-MI data from 54 healthy subjects [2]. The MI of left and right hand are the two classes in the data and there are in total 100 trials of each class per session and each trial is 4s in length. The EEG data has been originally recorded at 1000Hz using 62 electrodes. In this analysis, as it is done in the original work [2], we have selected 20 channels in the motor region for the classiﬁcation task (FC-5/3/1/2/4/6, C-5/3/1/z/2/4/6, and CP-5/3/1/z/2/4/6). Moreover, one of the baseline architectures, the Deep ConvNet is designed for the EEG data sampled at 250 Hz. Therefore, to maintain the compatibility and fairness of comparison, we down-sampled the data by a factor of 4 to have a sampling frequency of 250 Hz. Moreover, this analysis setting results in approximately similar EEG trial dimensions (channels × time) across all the datasets.

###### S2.3 Stroke Data: A

- Stroke Data: A is part of post-stroke BCI motor rehabilitation trial wherein 37 stroke patients are screened for their ability to control MI-BCI [3]. The MI of stroke-paralyzed hand and rest are the two classes in the data and there are in total 80 trials of each class for every patient. Every trial is of 4 seconds duration and the EEG data is collected using 27 channels sampled at 250Hz with a hardware bandpass ﬁltering from 0.5 -40Hz. In the present analysis, we use the entire 27 channel, 4s data for classiﬁcation.

S2.4 Stroke Data: B

- Stroke Data: B is also a part of post-stroke BCI motor rehabilitation trial and similar to Stroke Data: A, contains a 2-class data with MI of stroke-paralyzed hand being one class and rest being the other class [4]. This dataset comprises of data from 34 stroke patients with 160 trials per patient. The data collection protocol is the same as that of the Stroke Data: A with the 4s of EEG data collected per trial using 27 channels sampled at 250 Hz. For this dataset as well, we use the entire 27 channel, 4s data for classiﬁcation.

i

###### S3 Implementation of Baseline Classiﬁcation methods

- S3.1 The Traditional Approach: FBCSP-SVM

We implemented the FBCSP-SVM algorithm as per its authors’ recommendations in [5]. As done in the original work [5], we decomposed the raw EEG data using 9 narrow-band bandpass Chebyshev Type II ﬁlters, each of 4Hz bandwidth, spanning from 4 to 40 Hz (4-8, 8-12, ..., 36-40 Hz) with transition bandwidth of 2Hz and stopband ripple of 30dB. The narrow-band EEG was then spatially ﬁltered using CSP algorithm and 4 most discriminative CSP ﬁlters from each band where extracted. The log-variance of the EEG data ﬁltered using CSP ﬁlters was extracted as a feature. From these 36 features (9 frequency bands × 4 features per band) best 8 features were selected using the MIBIFPW algorithm [6]. An SVM classiﬁer was then trained using the selected features to classify the trial into one of the two classes. An epsilon - support vector regression with a radial basis function kernel ﬂavour of SVM was used for the classiﬁcation.

The CSP algorithm is designed for a binary classiﬁcation problem. Therefore, to classify the 4 class BCIC-IV-2A Data we used a One-Verses-Rest (OVR) strategy wherein 4 binary classiﬁers were trained to classify one class from the remaining 3 classes. Then each trial was assigned to the class for which it received the maximum SVR score among all 4 classiﬁers. Due to this approach, for BCIC-IV-2A Data, in total 16 CSP ﬁlters were extracted for each band (4 OVR-models × 4 ﬁlters per model).

Lastly, since both the FBCSP and FBCNet use the multi-view ﬁltered EEG representation, we used the same ﬁlter bank in both of these algorithms for fairness in comparison.

- S3.2 Existing CNN architectures : Deep ConvNet and EEGNet

We implemented the Deep ConvNet [7] and EEGNet-8,2 [8] following the descriptions found in the respective papers. One major modiﬁcation was done to the EEGNet-8,2 architecture due to the difference in the sampling frequencies of the data. The original EEGNet was proposed for the data with 128 Hz sampling frequency. However, all 4 datasets in this work have a sampling frequency of 250Hz. Therefore we multiply the lengths of temporal kernels and temporal pooling layers in their architectures by 2 to correspond approximately to the sampling rate in our model. Deep ConvNet and EEGNet-8,2 were trained in the exact same manner as that of the FBCNet. The exact implementations of these architectures used in this work are available at https://github.com/ravikiran-mane/FBCNet.

###### S4 Single subject classiﬁcation accuracies

The detailed results of classiﬁcation accuracies achieved by baseline methods and FBCNet along with the statistical signiﬁcance are provided in Table S2. Moreover, for the purpose of reproducibility and future comparisons, the single subject MI classiﬁcation accuracies for all analyses are presented in Table S3, S4, and S5.

Table S2: Subject-speciﬁc classiﬁcation accuracy: All analyses (mean±std) Dataset Analysis FBCSP-SVM+ Deep Convnet∗ EEGNet-8,2× FBCNet† BCIC-IV-2A Data CV 75.89±13.87 72.20±12.12† 73.13±8.52 79.03±13.17∗ OpenBMI Data CV 64.61±17.07×† 68.33±12.34×† 70.89±13.01+∗† 74.70±13.95+∗×

- Stroke Data: A CV 71.37±14.52† 68.81±12.02† 69.15±12.94† 79.16±14.06+∗×
- Stroke Data: B CV 74.14±14.35† 71.11±8.79×† 73.48±8.05∗† 81.11±10.44+∗× BCIC-IV-2A Data HO 68.06±14.11† 72.22±14.35 73.15±9.29 76.20±11.97+ Korea Uni. Data HO 60.36±14.97† 60.77±11.42×† 63.63±11.08∗ 67.19±14.38+∗

The best performing method for each analysis is highlighted in boldface. To indicate statistically signiﬁcant difference (p < 0.05) between any two methods we have marked every method (column) with a call-sign (+, ∗, ×, †, ‡). The presence of any method’s call-sign in any other method’s column represents a statistically signiﬁcant difference in classiﬁcation accuracies between those two methods. CV: 10-fold cross validation, HO: Hold out analysis with separate test session.

Table S3: Classiﬁcation accuracies for each subject in BCIC-IV-2A Dataset.

10-fold cross validation Hold Out FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet

Subject No.

- 1 85.31 71.03 72.86 85.76 77.78 78.13 79.51 85.42
- 2 64.51 52.05 56.25 61.07 55.56 45.14 61.11 60.42
- 3 90.00 82.41 83.39 94.51 79.51 85.42 88.54 90.63
- 4 64.02 58.93 67.54 68.84 63.19 67.01 71.53 76.39
- 5 73.66 73.57 76.38 82.54 53.47 77.43 71.18 74.31
- 6 52.72 62.50 67.05 58.71 46.88 53.13 59.03 53.82
- 7 92.10 79.33 73.53 93.08 86.81 86.46 71.53 84.38
- 8 88.62 82.41 80.27 86.21 81.25 78.13 80.56 79.51
- 9 72.10 87.59 80.94 80.54 68.06 79.17 75.35 80.90

Avg 75.89 72.20 73.13 79.03 68.06 72.22 73.15 76.20 Std 13.87 12.12 8.52 13.17 14.11 14.35 9.29 11.97

ii

Table S4: Classiﬁcation accuracies for each subject in OpenBMI Dataset.

10-fold cross validation Hold out FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet

Subject No.

- 1 64.00 53.00 56.00 72.50 69.50 56.50 56.00 69.50
- 2 99.00 73.50 73.00 97.50 63.00 62.50 70.50 73.50
- 3 91.00 65.50 78.50 94.00 92.00 65.00 75.00 92.50
- 4 52.50 79.50 78.00 78.00 46.50 65.50 72.50 75.50
- 5 90.50 78.50 79.00 81.50 69.00 54.00 61.50 67.00
- 6 68.00 89.00 89.00 89.00 68.50 92.00 91.50 87.00
- 7 63.00 78.00 84.00 73.50 56.50 49.50 61.50 51.00
- 8 56.50 81.50 83.00 76.00 51.50 63.00 66.50 68.00
- 9 52.00 51.50 49.00 71.00 48.00 53.00 49.50 64.00
- 10 51.00 55.50 56.50 64.00 52.00 53.50 53.00 62.00
- 11 53.50 57.00 65.50 60.00 52.00 56.50 50.00 50.50
- 12 62.50 81.50 81.50 79.00 52.00 58.50 62.50 57.50
- 13 67.00 71.00 68.50 66.00 47.50 54.50 55.50 50.50
- 14 48.00 63.00 64.00 58.50 50.50 57.00 58.50 53.00
- 15 52.50 91.50 97.00 89.50 48.00 68.50 67.00 61.50
- 16 59.00 62.00 71.50 73.00 52.00 76.00 86.00 77.00
- 17 54.50 59.50 64.00 67.50 49.50 52.50 56.00 60.50
- 18 89.00 49.50 55.50 92.50 76.50 45.00 57.00 81.00
- 19 80.00 61.00 69.00 77.00 64.50 53.00 66.50 57.50
- 20 41.50 62.00 60.50 60.00 43.50 56.50 60.00 60.50
- 21 93.50 56.00 69.50 97.00 92.00 52.00 65.00 99.00
- 22 80.00 58.50 52.50 82.00 57.50 55.50 53.00 72.00
- 23 54.00 55.00 46.50 57.00 61.50 46.50 48.00 60.50
- 24 49.00 50.00 53.50 49.50 56.00 46.50 50.50 52.50
- 25 50.00 67.00 70.50 58.00 53.50 85.00 81.00 54.50
- 26 50.00 79.50 78.50 70.00 52.50 72.50 77.00 71.00
- 27 50.00 77.50 80.50 69.50 54.00 73.50 76.50 66.00
- 28 97.00 95.50 95.00 93.00 90.50 60.50 67.50 72.50
- 29 89.50 83.50 81.50 90.00 97.00 93.50 66.50 95.00
- 30 73.00 72.50 74.00 78.00 60.50 58.00 59.00 61.50
- 31 57.00 83.00 84.00 77.00 51.50 71.50 71.00 56.50
- 32 72.50 58.50 57.50 79.50 69.50 54.50 56.00 73.50
- 33 87.50 75.50 75.50 96.00 72.00 65.50 61.50 90.50
- 34 49.00 63.00 64.00 56.00 45.50 58.50 58.00 54.00
- 35 63.00 100.00 100.00 100.00 54.50 87.00 90.00 86.50
- 36 97.50 73.00 95.50 98.00 97.50 77.00 90.00 99.00
- 37 89.50 43.00 47.00 91.00 89.00 50.00 49.50 87.50
- 38 57.50 66.50 67.50 63.50 50.50 52.00 72.00 49.50
- 39 57.00 68.50 69.50 67.50 49.50 53.00 62.00 66.00
- 40 46.50 61.50 62.00 60.50 51.00 70.00 64.00 61.00
- 41 57.00 59.00 57.00 60.00 49.00 48.50 53.50 48.50
- 42 50.50 66.50 69.00 59.00 52.00 68.00 68.00 67.50
- 43 80.50 81.00 86.50 80.00 68.50 51.50 50.50 50.00
- 44 92.50 75.50 83.00 97.50 94.50 59.50 78.00 99.00
- 45 84.50 63.00 65.00 87.50 70.50 50.00 55.50 78.50
- 46 47.50 69.00 70.50 70.00 54.00 66.00 58.00 72.50
- 47 49.50 66.00 73.00 72.50 49.00 69.00 71.00 71.00
- 48 48.00 85.00 83.50 81.50 45.00 55.50 59.50 57.00
- 49 58.00 63.00 66.00 66.00 49.00 50.50 49.00 50.50
- 50 47.50 57.00 55.50 57.00 55.00 54.50 53.00 51.00
- 51 53.00 70.00 74.00 67.50 51.50 59.50 61.50 63.00
- 52 63.00 63.00 75.50 75.00 61.50 67.00 68.00 62.50
- 53 45.00 61.50 66.50 55.00 52.00 58.50 63.00 54.00
- 54 54.50 59.50 55.50 52.50 50.00 48.50 53.00 55.50

Avg 64.61 68.33 70.89 74.70 60.36 60.77 63.63 67.19 Std 17.07 12.34 13.01 13.95 14.97 11.42 11.08 14.38

iii

Table S5: Classiﬁcation accuracies for stroke patients from both stroke datasets.

Stroke Data: A Stroke Data: B FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet FBCSP-SVM Deep Convnet EEGNet-8,2 FBCNet

Subject No.

- 1 74.23 68.65 73.82 73.64 73.75 66.88 68.66 70.80
- 2 51.70 49.11 45.54 49.29 78.54 65.79 71.42 76.58
- 3 96.79 95.36 94.73 97.32 59.55 68.93 71.79 77.86
- 4 49.55 47.95 43.75 50.54 46.21 61.42 65.79 64.92
- 5 77.41 77.68 78.48 91.61 84.79 73.92 80.29 88.58
- 6 96.88 80.64 80.73 96.16 82.14 90.98 88.48 88.39
- 7 67.32 73.04 70.80 74.29 82.29 77.79 79.67 82.13
- 8 90.45 83.13 87.59 93.48 55.08 50.00 56.46 59.04
- 9 77.14 56.16 58.57 77.32 82.95 77.23 81.61 86.70
- 10 78.75 71.79 79.55 90.27 53.04 72.83 65.79 66.92
- 11 86.43 76.70 70.18 96.79 73.66 69.02 69.55 79.20
- 12 56.07 60.63 59.29 69.38 86.08 67.79 72.25 86.08
- 13 53.52 58.17 48.09 58.17 91.16 78.66 76.70 92.50
- 14 61.95 60.21 64.58 76.63 53.92 73.50 74.67 74.13
- 15 96.13 81.42 83.92 97.42 80.63 65.45 68.93 88.57
- 16 62.75 60.13 61.01 69.84 65.79 65.08 70.71 65.17
- 17 43.76 57.05 51.12 50.28 53.83 72.75 70.79 67.75
- 18 64.14 67.85 69.36 77.70 73.21 61.88 67.59 83.30
- 19 79.84 75.26 77.48 82.25 90.00 70.00 73.39 92.50
- 20 60.88 78.38 77.04 71.92 72.05 67.86 65.89 84.29
- 21 71.14 63.15 59.80 79.61 57.14 62.32 67.95 68.04
- 22 77.46 86.63 84.75 93.08 86.67 72.75 77.17 79.08
- 23 73.54 67.21 72.33 87.04 78.42 68.92 72.21 84.08
- 24 62.23 80.18 74.29 82.68 81.34 72.23 81.88 92.41
- 25 71.46 72.18 81.76 86.57 53.13 67.08 70.96 72.75
- 26 67.68 62.68 61.61 75.36 91.96 78.30 79.91 94.02
- 27 91.61 87.78 87.07 96.25 83.75 72.77 67.86 88.66
- 28 56.88 53.30 56.34 66.70 87.95 71.70 74.11 92.50
- 29 79.57 74.48 69.94 90.50 66.92 66.92 72.00 75.17
- 30 92.95 79.89 84.52 93.44 81.52 67.14 61.43 80.18
- 31 81.25 78.04 78.66 86.88 97.50 81.13 82.25 99.33
- 32 60.98 61.61 61.52 70.98 50.08 58.13 66.25 69.67
- 33 60.67 58.38 54.88 61.00 75.98 94.46 94.64 91.52
- 34 71.84 47.32 53.02 78.99 89.64 85.98 89.20 94.82
- 35 67.96 62.29 67.92 85.46
- 36 46.07 56.25 59.20 60.54
- 37 81.71 75.47 75.51 89.65

Avg 71.37 68.81 69.15 79.16 74.14 71.11 73.48 81.11 Std 14.52 12.02 12.94 14.06 14.35 8.79 8.05 10.44

###### References

- [1] M. Tangermann, K. R. Müller et al., “Review of the BCI competition IV,” Front. Neurosci., vol. 6, pp. 1–31, 2012.
- [2] M. H. Lee, O. Y. Kwon et al., “EEG dataset and OpenBMI toolbox for three BCI paradigms: An investigation into BCI illiteracy,” GigaScience, vol. 8, no. 5, pp. 1–16, 2019.
- [3] K. K. Ang, C. Guan et al., “Facilitating effects of transcranial direct current stimulation on motor imagery braincomputer interface with robotic feedback for stroke rehabilitation,” Arch. Phys. Med. Rehabil., vol. 96, no. 3, pp. S79–S87, 2015.
- [4] ——, “Brain-computer interface-based robotic end effector system for wrist and hand rehabilitation: results of a three-armed randomized controlled trial for chronic stroke,” Front. Neuroeng., vol. 7, p. 30, Jul. 2014.
- [5] K. K. Ang, Z. Y. Chin et al., “Filter Bank Common Spatial Pattern (FBCSP),” 2008 Int. Jt. Conf. Neural Networks (IJCNN 2008), pp. 2391–2398, 2008.
- [6] ——, “Mutual information-based selection of optimal spatial-temporal patterns for single-trial EEG-based BCIs,” Pattern Recognit., vol. 45, no. 6, pp. 2137–2144, 2012.
- [7] R. T. Schirrmeister, J. T. Springenberg et al., “Deep learning with convolutional neural networks for EEG decoding and visualization,” Hum. Brain Mapp., vol. 38, no. 11, pp. 5391–5420, 2017.
- [8] V. J. Lawhern, A. J. Solon et al., “EEGNet: A compact convolutional neural network for EEG-based braincomputer interfaces,” J. Neural Eng., vol. 15, no. 5, pp. 1–30, 2018.

iv

