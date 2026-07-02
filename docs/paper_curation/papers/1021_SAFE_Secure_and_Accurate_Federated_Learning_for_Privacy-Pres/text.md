# SAFE: Secure and Accurate Federated Learning for Privacy-Preserving Brain-Computer Interfaces

Tianwang Jia, Xiaoqing Chen and Dongrui Wu

## arXiv:2601.05789v1[cs.HC]9Jan2026

Abstract—Electroencephalogram (EEG)-based brain-computer interfaces (BCIs) are widely adopted due to their efficiency and portability; however, their decoding algorithms still face multiple challenges, including inadequate generalization, adversarial vulnerability, and privacy leakage. This paper proposes Secure and Accurate FEderated learning (SAFE), a federated learning-based approach that protects user privacy by keeping data local during model training. SAFE employs local batch-specific normalization to mitigate cross-subject feature distribution shifts and hence improves model generalization. It further enhances adversarial robustness by introducing perturbations in both the input space and the parameter space through federated adversarial training and adversarial weight perturbation. Experiments on five EEG datasets from motor imagery (MI) and event-related potential (ERP) BCI paradigms demonstrated that SAFE consistently outperformed 14 state-of-the-art approaches in both decoding accuracy and adversarial robustness, while ensuring privacy protection. Notably, it even outperformed centralized training approaches that do not consider privacy protection at all. To our knowledge, SAFE is the first algorithm to simultaneously achieve high decoding accuracy, strong adversarial robustness, and reliable privacy protection without using any calibration data from the target subject, making it highly desirable for real-world BCIs.

Index Terms—Brain-computer interface, federated learning, domain generalization, adversarial defense, privacy protection

I. INTRODUCTION

A brain-computer interface (BCI) [1] enables direct communication between the brain and external devices, offering applications in neurological rehabilitation [2], robot control [3], text input [4], [5], speech synthesis [6], affect recognition and regularization [7], and so on. Electroencephalography (EEG), due to its efficiency and portability, is one of the most commonly used non-invasive BCI inputs. Among various EEG-based BCI paradigms, motor imagery (MI) [8], eventrelated potentials (ERPs) [9], and steady-state visual evoked potentials (SSVEPs) [10], are widely adopted.

Despite the advantages of EEG-based BCIs, they also face multiple challenges in real-world applications, including:

1) Inadequate generalization. A well-generalizable EEG classifier is critical for real-world BCIs, especially for

T. Jia, X. Chen and D. Wu are with the Key Laboratory of the Ministry of Education for Image Processing and Intelligent Control, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China. X. Chen and D. Wu are also with Zhongguancun Academy, Beijing, 100084 China. Email: {twjia, xqchen914, drwu}@hust.edu.cn.

This research was supported by Open Research Fund of the State Key Laboratory of Brain-Machine Intelligence, Zhejiang University (Grant No. BMI2400015).

Dongrui Wu is the corresponding author. Email: drwu09@gmail.com.

new users with little or no calibration data. However, conventional EEG classifiers trained for individual subjects or on limited datasets often generalize poorly across users, due to the inherently low signal-to-noise ratio of EEG signals and substantial inter-subject variations [11].

2) Adversarial vulnerability. BCI systems exhibit serious vulnerabilities to adversarial attacks, where malicious small perturbations are injected into EEG data to induce erroneous classification outputs, as illustrated in Fig. 1. Recent studies have demonstrated that even tiny adversarial perturbations can significantly compromise the decoding performance [12]–[15]. Adversarial attacks pose significant risks in critical BCI applications, as they may result in incorrect clinical decisions in healthcare, and dangerous operations in military operations [16].

[Figure 1]

Fig. 1. Adversarial attacks on BCIs.

3) Privacy leakage. Regulations such as European Union’s General Data Protection Regulation and China’s Personal Information Protection Law enforce strict protocols for collecting, storing and utilizing personal sensitive data. Previous studies have shown that EEGs can expose user privacies like mental diseases and cognitive states [17]. Thus, privacy-preserving BCIs become a necessity.

Substantial progresses have been made to address each individual challenge of the above, including decoding accuracy enhancement [11], [18], [19], adversarial robustness [20]– [22], and privacy protection [23]–[25]. Several studies have attempted to tackle two of the three challenges simultaneously.

For instance, Zhang et al. [26] considered simultaneously the decoding accuracy and privacy protection, and Chen et al. [27] enhanced both the decoding accuracy and adversarial robustness.

To our knowledge, Chen et al. [28] were the first to demonstrate the feasibility of addressing all three challenges simultaneously. However, their approach needs to make use of some target domain calibration data. This paper proposes Secure and Accurate FEderated learning (SAFE), which is completely calibration-free for the new subject. It builds upon a federated learning (FL) [29] architecture, as shown in Fig. 2. Each client retains its own EEG data, trains a local copy of the classifier, and uploads the model parameters to the central server. The central server then aggregates the model parameters from all clients and publishes them to the clients again for updates. In this way, a global EEG classifier can be trained without exposing any client’s EEG data to any other clients or the test user, ensuring strong privacy protection.

[Figure 2]

Fig. 2. SAFE for BCIs. Training users are clients, and a trusted third-party institution (e.g., a hospital) is the server; only model parameters, instead of EEG data, are exchanged, protecting client user privacy.

We conducted experiments on five EEG datasets from MI and ERP paradigms to compare SAFE with 14 state-of-theart approaches, including seven FL methods with privacy protection and seven centralized training (CT) methods without any privacy protection. We evaluated SAFE on benign data and adversarial examples generated by five representative black-box/white-box adversarial attack approaches. The results demonstrated that SAFE significantly improved the decoding accuracy and adversarial robustness while ensuring privacy protection.

The remainder of this paper is organized as follows. Section II reviews related work in domain generalization, adversarial defense, and privacy-preserving machine learning. Section III proposes SAFE. Section IV describes the experiment setup. Section V presents the experimental results on five datasets. Finally, Section VI draws conclusions.

II. RELATED WORK

This section reviews related work addressing three key challenges in machine learning: inadequate generalization, adversarial vulnerability, and privacy leakage. Specifically, we focus on studies in domain generalization, adversarial defense, and privacy-preserving machine learning.

- A. Domain Generalization

Domain generalization, also known as out-of-distribution generalization, addresses the challenge of learning a model from one or multiple related source domains that can generalize effectively to unseen target domains [30]. Over the years, significant progress has been made in domain generalization research. Existing approaches can be broadly categorized into three groups: data manipulation, representation learning, and learning strategy [31].

Data manipulation aims to improve generalization by transforming the model inputs, primarily through data augmentation [32] and data generation [33].

Representation learning is a commonly used approach in domain generalization, achieved by extracting domain-invariant features across different domains [34], [35], or decomposing features into domain-shared and domain-specific components to enhance generalization [36].

Learning strategy refers to the utilization of general learning strategies, such as meta-learning [37], gradient manipulation [38], distributionally robust optimization [39], and selfsupervised learning [40], to improve generalization.

- B. Adversarial Defense

Adversarial defenses have been extensively explored in both image and natural language processing domains to enhance model robustness against adversarial attacks. One of the most prevalent approaches is adversarial training (AT) [41], which augments the benign training data with adversarial samples. Other commonly adopted methods include model-level [42], [43] and data-level [44], [45] defenses.

Zhang et al. [12] first discovered that adversarial samples significantly reduce the decoding accuracy of EEG-based BCIs. Subsequently, multiple adversarial defense approaches for BCIs have been proposed. Meng et al. [20] systematically evaluated the advantages and limitations of various defense strategies in BCI applications. Gunawardena et al. [46] combined AT with adversarial detection, effectively enhancing the robustness of BCIs against black-box attacks. Chen et al. [27] proposed ABAT, which performs AT on the aligned EEG data to improve the decoding accuracies on both benign and adversarial samples.

- C. Privacy-preserving Machine Learning

Privacy-preserving machine learning avoids using the raw data directly, protecting their privacy. Key methodologies include source-free domain adaptation and FL.

Source-free domain adaptation protects data privacy by transferring knowledge from the source domain to the target

domain without accessing the source domain data. For example, SHOT [47] utilizes only the source model and unlabeled target data in pseudo-label-based self-supervised adaptation.

FL establishes a privacy-preserving distributed learning framework, where clients collaboratively train models without sharing raw data. FedAvg [48], the most prevalent FL approach, reduces communication overhead by conducting multiple local stochastic gradient descent updates per client before server-side model aggregation. Many studies have improved FedAvg to address various challenges, such as enhancing adversarial robustness [49], mitigating client data drift [50]– [52], and improving model generalization [53], [54].

Privacy protection is particularly critical for BCI applications, since commercial BCI systems often require crossinstitutional collaboration (e.g., hospitals, universities, and companies), and EEG data inherently contain sensitive private information. Different approaches for privacy-preserving BCIs have been proposed. Xia et al. [55] proposed augmentationbased source-free domain adaptation for cross-subject MI classification. Zhang et al. proposed lightweight source-free transfer [26] and multi-source decentralized transfer [56]. FLbased solutions include Ju et al.’s [57] federated transfer learning framework for extracting shared EEG features, and Liu et al.’s [58] split-classifier architecture combining globallocal knowledge. FedBS [59] improves both privacy protection and the decoding accuracy, without considering adversarial robustness.

III. SECURE AND ACCURATE FEDERATED LEARNING (SAFE)

This section introduces the details of our proposed SAFE approach.

- A. Problem Statement

Assume there are K subjects S = {Sk}Kk=1, each as a client participating in the training. For the k-th client, there are nk labeled EEG samples Sk = {(Xk,i,yk,i)}n

k

i=1 and a classifier with parameters θrk, where Xk,i ∈ Rc×t is the ith EEG trial, yk,i ∈ {1,··· ,L} is the corresponding label, and r ∈ {1,··· ,R} is the index of communication rounds, in which c, t, L and R represent the number of channels, time domain samples, classes, and maximum communication rounds, respectively. The goal of SAFE is to train a wellgeneralizable EEG classifier without any calibration data from test subjects.

- B. Overview

Fig. 3 illustrates the complete workflow of SAFE, which consists of one central server and multiple clients.

Each client holds EEG data from an individual subject for localized model training, while the central server communicates with the clients and aggregates their uploaded model parameters into a final global model. We utilize local batchspecific normalization (LBSN) to keep BN layers localized to each client without parameter sharing during training, enhancing privacy protection and mitigating inter-subject distribution

[Figure 3]

- (a) Server-side operations in SAFE.

[Figure 4]

- (b) Client-side operations in SAFE.

Fig. 3. Flowchart of the proposed SAFE. (a) Server-side operations; and, (b) client-side operations.

discrepancies in both training and testing phases. Furthermore, we introduce a dual-defense mechanism into client-side training, i.e., federated adversarial training (FAT) in the input space and adversarial weight perturbation (AWP) in the parameter space, to collaboratively defend against adversarial attacks.

Algorithm 1 gives the pseudo-code of SAFE. The source code will be made available after this paper is accepted.

C. LBSN

Following FedBS [59], LBSN computes batch-specific statistics for the BN layers, instead of conventional global statistics.

The standard BN layer maintains four sets of parameters: statistical parameters µ (mean) and σ (standard deviation) dynamically computed during forward propagation, and learnable parameters γ (scaling factor) and β (bias) optimized through backpropagation.

Different from traditional approaches that compute and fix statistical parameters across the entire training process, LBSN dynamically computes batch-wise statistical parameters µ and σ to alleviate the non-stationary nature of EEG signals and inter-subject distribution discrepancies. Specifically, given a training/test batch B = {(Xi,yi)}Bi=1 with batch size B, LBSN computes:

1 B

µB =

1 B

σB2 =

B

Xi, (1)

i=1

B

(Xi − µB)2. (2)

i=1

Algorithm 1: Secure and Accurate FEderated learning (SAFE).

Input: K, number of clients; Sk, labeled dataset of the k-th client; R, maximum communication rounds; η, learning rate; m, number of selected clients per round; B, batch size; E, local optimization epochs per client; α, FAT adversarial example magnitude in (4); ξ, perturbation scale for AWP in (6).

Output: θ, model parameters with BN layers. Server executes: Initialize θ′0, model parameters without BN layers; for r = 1,...,R do

Cr ← Set of m randomly selected clients; for client k ∈ Cr do

θ′rk ← ClientUpdate(k,θ′r−1);

end Nr ← k∈Cr nk; θ′r ← k∈Cr

nk Nr θ′rk;

end ClientUpdate(k,θ′): θ ← θ′ + local BN parameters; B ← Split Sk into batches of size B; for epoch = 1,...,E do

for batch B ∈ B do Calculate δ on B by (4); Generate adversarial examples from B:

B′ = {Xi + δ,yi}Bi=1;

Calculate µB′ on B′ by (1); Calculate σB′ on B′ by (2); Update θ with (µB′,σB′) on B′ by (6) and (7);

### end

end θ′ ← θ − local BN parameters; return θ′

Furthermore, LBSN localizes the BN learnable parameters γ and β to each client during federated training, and aggregates them at the server to form a complete model for testing.

LBSN offers three advantages:

- 1) Isolation of BN parameter interference across clients during training, enabling better feature alignment across distributions.
- 2) Rapid adaptation to new subject’s data during testing.
- 3) Mitigation of privacy leakage risks caused by transmitting the statistical parameters, effectively defending against attacks that attempt to reverse-engineer raw data through BN parameters.

D. FAT

AT enhances model robustness against adversarial attacks by incorporating adversarial examples during training. It solves

the following min-max optimization problem:

L(θ,X + δ,y) , (3)

E(X,y)∼D max

min

θ

∥δ∥p≤ϵ

where θ denotes model parameters, D the training set, L the loss function, and δ the adversarial perturbation constrained within an ϵ-bounded ℓp-norm ball. The input X + δ is the adversarial counterpart of Xadv. The inner maximization generates worst-case perturbations, and the outer minimization optimizes model parameters against them.

FAT extends classical AT to the FL framework through three key steps: 1) generating adversarial examples from local client data during training; 2) performing local AT using the adversarial samples; and, 3) aggregating the client model parameters at the central server. It imposes ℓ∞-norm constraints on adversarial perturbations as ∥δ∥∞ ≤ ϵ.

To address the limited computational resources on clients in federated systems, FAT employs the Fast Gradient Sign Method (FGSM) [60] for efficient perturbation generation:

δ = α · sign(∇XL(θ,X,y)), (4)

where α ≤ ϵ controls the perturbation magnitude, under the ℓ∞-norm constraint. This single-step computation enables efficient gradient acquisition through backpropagation, making FAT particularly suitable for distributed learning scenarios with resource-constrained clients.

E. AWP

FAT enhances model robustness by introducing perturbations in the input space to smooth the loss landscape. AWP [61] is further introduced into the client-side training of FL, to regularize the flatness of the weight loss landscape through parameter space perturbations, and hence to strengthen the adversarial robustness.

AWP solves a min-max optimization problem:

{L(θ) + max

[L(θ + ν) − L(θ)]}

min

θ

∥νl∥≤ξ∥θl∥

(5)

L(θ + ν),

=min

max

θ

∥νl∥≤ξ∥θl∥

where L(θ) (a simplified notation for L(θ,X,y)) represents the original training loss, L(θ + ν) − L(θ) characterizes the flatness of the weight loss landscape, ν is the weight perturbation, and ∥νl∥ ≤ ξ∥θl∥ is the constraint on the perturbation magnitude (proportional to layer-wise weights θl), with ξ controlling the perturbation scale.

To accommodate the limited computational capacity of FL clients, we adopt a simplified one-step approximation to compute ν:

ν ← ξ ∇νL(θ + ν)

∥θ∥, (6) and then update the model weights by:

∥∇νL(θ + ν)∥

θ ← (θ + ν) − η∇θ+νL(θ + ν) − ν, (7)

where η is the learning rate, and the parameters are reset to their original values after each perturbation step.

IV. EXPERIMENT SETTINGS

This section introduces our experiment settings, including datasets, preprocessing, threat models, baseline algorithms, evaluation metrics, and hyperparameters.

- A. Datasets and Preprocessing

Three MI and two ERP datasets, summarized in Table I, were used in our experiments.

TABLE I SUMMARY OF THE FIVE DATASETS.

Dataset # Subjects # Classes # Channels

# Trials per Subjects

ClassImbalance

MI1 [62] 10 6 60 480 MI2 [63] 9 4 22 576 MI3 [64] 14 2 15 160

- ERP1 [65] 10 2 16 1728

- ERP2 [66] 8 2 8 4200

- MI1 [62] includes six classes (left hand, right hand, both feet, both hands, left hand combined with right foot, and right hand combined with left foot), each with 80 trials. 60-channel EEG signals from 10 healthy subjects were recorded at 200 Hz. We resampled the signals to 250 Hz, extracted data from [0,4] seconds following task stimulation, and applied a [8–30] Hz band-pass filter.
- MI2 [63] was originally released as BCI Competition IV dataset 2a. It includes four classes (left hand, right hand, both feet, and tongue), each with 144 trials. 22-channel EEG signals from 9 healthy subjects were recorded at 250 Hz. We extracted data from [0,4] seconds following task stimulation and applied a [8–30] Hz band-pass filter.
- MI3 [64] includes two classes (left hand versus right hand), each with 80 trials. 15-channel EEG signals from 14 subjects were sampled at 512 Hz. We downsampled the signals to 250 Hz, extracted data from [0,5] seconds following task stimulation, and applied a [8–30] Hz band-pass filter.

- ERP1 [65] includes two classes (non-target and target)

with a 5:1 ratio, with 1,440 non-target trials and 288 target trials. 16-channel EEG signals from 10 healthy subjects were recorded at 256 Hz. We downsampled the signals to 250 Hz, extracted data from [0,0.8] seconds following event stimulation, and applied a [0.1,20] Hz band-pass filter.

- ERP2 [66] includes two classes (non-target and target) with

a 5:1 ratio, with 3500 non-target trials and 700 target trials. 8-channel EEG signals from 8 amyotrophic lateral sclerosis patients were recorded at 256 Hz. We downsampled the signals to 250 Hz, extracted data from [0,1] seconds following event stimulation, and applied a [0.1,30] Hz band-pass filter.

- B. Threat Models We considered three white-box adversarial attacks:

- 1) FGSM [60], which computes the gradient of the loss with respect to the input and applies a small perturbation along the direction of the sign of the loss gradient:

Xadv = X + α · sign(∇XL(θ,X,y)). (8)

- 2) Projected gradient descent (PGD) [41], which iteratively improves FGSM. Starting from an initial perturbation (often randomized) applied to the input X, the adversarial example is updated iteratively:

Xtadv+1 = ProjX,ϵ Xtadv + α · sign(∇XL(θ,Xtadv,y)) , (9)

where Xtadv denotes the adversarial example in iteration t, α controls the step size, and ProjX,ϵ(·) projects the perturbation within the ℓ∞-norm ball of radius ϵ centered at X. This multi-step exploration results in stronger attacks than the single-step FGSM.

- 3) AutoAttack (AA) [67], a parameter-free ensemble evaluation method combining four complementary attack strategies: Auto-PGD with cross-entropy loss, AutoPGD with difference of logits ratio loss, Fast Adaptive Boundary attack, and Square attack [68]. This combination ensures robustness across diverse scenarios by leveraging both white-box gradient information and black-box query strategies.

and two black-box adversarial attacks:

- 1) RayS [69], an efficient hard-label attack that replaces

continuous optimization with discrete search over ℓ∞norm vertices δ ∈ {−1,1}d, where d denotes the input dimensionality. It seeks minimal perturbation radius via greedy dimension-wise adjustments with early direction pruning to reduce the number of queries, and hierarchical coarse-to-fine search to leverage the spatial correlations.

- 2) Square attack [68], a score-based black-box adversarial

attack method applicable to the ℓ∞ norm. It employs a randomized search strategy, selecting localized squareshaped updates at random positions, ensuring that the perturbation at each iteration is approximately situated at the boundary of the feasible set. Square attack demonstrates high query efficiency and attack accuracy, particularly in untargeted attacks.

All attacks adopt the ℓ∞ untargeted setting, aiming to induce misclassification rather than targeting specific classes. Given the characteristics of EEG signals, we set the perturbation magnitude as ϵ times the signal standard deviation [27]. For the three white-box attacks, we selected ϵ ∈ {0.01,0.03,0.05}. For the two black-box attacks, which have limited access to model information, we chose ϵ ∈ {0.01,0.05,0.1}.

C. Baseline Algorithms

We compared SAFE with 14 state-of-the-art CT and FL approaches, covering a wide range of methods designed to enhance adversarial robustness and generalization. All approaches employed EEGNet [70] as the backbone architecture.

CT approaches merge data from K subjects for joint training, without considering any privacy protection. The seven CT baselines include:

1) Normal Training (NT), which applies standard empirical risk minimization to the pooled training data from all subjects.

- 2) AT, which enhances adversarial robustness by augmenting the training data with FGSM-generated adversarial examples.
- 3) Five domain generalization approaches, including DANN [34] based on domain adversarial learning, IRM [35] based on invariant risk minimization, GroupDRO [39] based on distributionally robust optimization, MLDG [37] based on meta-learning, and RSC [38] based on gradient manipulation.

FL treats each training subject as a separate client for privacy protection. The seven FL baselines include:

- 1) FedAvg [48], the most widely used FL algorithm, where each client performs multiple stochastic gradient descent update steps in a single communication round to balance communication cost and accuracy.
- 2) FAL [49], which uses PGD-generated adversarial samples for adversarial learning in a federated environment, enhancing robustness against adversarial attacks.
- 3) Three approaches focusing on mitigating client data drift, including FedProx [50], which introduces a proximal term in client objectives to reduce the discrepancy between local and global models; SCAFFOLD [51], which employs control variables to correct client drift during local updates; and MOON [52], which leverages model representation similarity during optimization.
- 4) Two methods focusing on improving model generalization, including FedFA [53], which performs federated feature augmentation to enhance generalization, and GA [54], which incorporates domain generalization through fairness objectives and requires all clients to participate in every communication round.

- D. Evaluation Metrics

We employed balanced classification accuracy (BCA) to assess the model performance on both benign and adversarial samples, because the conventional raw classification accuracy becomes unreliable for highly imbalanced datasets like ERP1 and ERP2.

The BCA is computed as:

BCA =

1 L

1 Nl

L

l=1

Nl

i=1

1(ˆyi = yi), (10)

where L denotes the total number of classes, Nl the number of test samples in class l, yˆi the predicted label of the i-th test sample, yi the true label, and 1(·) the indicator function.

- E. Additional Settings and Hyperparameters

Leave-one-subject-out cross-validation was adopted. Specifically, each subject in the corresponding dataset was treated as an unknown test subject once, while the remaining subjects served as training data. In the CT setting, data from all training subjects were aggregated for model training. In the FL setting, each client represented one training subject, i.e., the number of clients equaled the total number of subjects minus one. Five repeats with different random seeds were performed, and the average results are reported.

Euclidean alignment (EA) [18] was applied individually to each subject for all approaches.

To mitigate class imbalance in ERP1 and ERP2, we implemented a mix-based data augmentation strategy [22] for all approaches within each subject. Specifically, two EEG trials X1 and X2 were randomly selected, and their arithmetic mean was computed as the augmented sample X′:

- 1

- 2

X′ =

(X1 + X2). (11)

X′ was labeled as the target class if at least one of X1 or X2 belonged to the target class, and as non-target class otherwise.

Stochastic gradient descent optimizer was employed with a learning rate of 0.005, weight decay of 1e-4, and momentum of 0.9. For CT, models were trained for 100 epochs with varying batch sizes: 64 for MI, and 256/512 for ERP1/ERP2, respectively. In FL, we conducted 100 global communication rounds where half of the clients were randomly selected per round to reduce the communication overhead, and each client performed two local training epochs with reduced batch sizes (32 for MI, and 128/256 for ERP1/ERP2) to accommodate limited client-side samples. During testing phases for both benign and adversarial samples, a fixed batch size of 8 was used across all experiments to ensure consistency.

For SAFE, the perturbation magnitude α in FAT was set to 0.03 times the signal’s standard deviation. The perturbation scale for AWP was set to ξ = 0.01. For AT, FGSM generated adversarial examples with a perturbation magnitude of 0.03 times the signal’s standard deviation. Hyperparameters of other baselines were set according to the recommendations in their original publications and further fine-tuned slightly.

V. EXPERIMENTAL RESULTS

This section presents experimental results to demonstrate the effectiveness of SAFE.

A. BCAs on Benign Samples

Tables II-VI present the cross-subject BCAs for benign samples on the five datasets. The best performance in each column is marked in bold, and the second-best underlined.

Observe that:

- 1) In the CT setting, NT achieved the best average accuracy, outperforming domain generalization methods, indicating the limitations of existing domain generalization approaches in addressing cross-subject EEG distribution discrepancies.
- 2) Since the primary goal of both AT and FAL is to enhance the model robustness to adversarial samples instead of the decoding accuracy on the benign samples, employing either AT or FAL alone led to decreased classification accuracy on the benign samples.
- 3) All FL methods, except SAFE, underperformed CT, indicating that client data heterogeneity caused performance degradation and exposed the conflict between privacy protection and decoding accuracy.
- 4) SAFE achieved the best average performance across all five datasets, achieving both accurate decoding and privacy protection.

TABLE II CROSS-SUBJECT BCAS (%) FOR BENIGN SAMPLES ON MI1. THE BEST ACCURACY IN EACH COLUMN IS MARKED IN BOLD, AND THE SECOND BEST UNDERLINED.

Setting Approach S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 Avg.

NT 35.17 37.38 32.13 24.58 34.79 52.67 42.67 46.92 58.33 23.83 38.85 AT 23.04 30.75 25.92 20.25 26.71 36.90 36.04 33.83 41.75 17.50 29.27

DANN 26.08 33.42 26.92 24.33 29.54 45.05 38.00 40.71 47.96 23.17 33.52 IRM 34.04 36.58 29.08 23.83 30.42 47.67 41.04 39.42 49.67 22.38 35.41 GroupDro 37.25 34.58 31.29 24.96 30.46 50.00 38.42 44.21 53.58 23.50 36.83 MLDG 26.08 28.04 24.33 19.13 25.08 26.52 37.00 37.25 44.38 20.25 28.81 RSC 32.25 35.04 32.00 22.17 29.54 49.71 42.29 39.42 54.00 22.58 35.90

CT

.

FedAvg 29.71 39.46 27.75 25.33 26.21 51.57 37.67 46.33 51.71 19.54 35.53 FAL 19.25 31.63 25.00 20.38 20.88 37.67 32.50 27.29 28.58 16.17 25.93 FedProx 30.54 36.92 29.92 25.04 25.25 47.29 37.42 41.04 53.71 17.88 34.50

FL

SCAFFOLD 17.71 16.21 17.42 15.88 18.04 17.76 18.08 18.00 20.63 16.67 17.64 MOON 33.96 38.21 32.75 25.63 33.71 50.00 41.21 45.04 53.00 20.46 37.40 FedFA 29.88 31.58 26.79 24.00 20.79 42.81 27.63 31.25 38.87 18.04 29.16

GA 30.71 35.38 27.54 24.33 26.42 46.05 31.21 40.58 50.33 19.83 33.24 SAFE 39.42 45.38 36.04 23.83 34.83 52.62 40.63 58.25 57.75 29.88 41.86

TABLE III CROSS-SUBJECT BCAS (%) FOR BENIGN SAMPLES ON MI2. THE BEST ACCURACY IN EACH COLUMN IS MARKED IN BOLD, AND THE SECOND BEST UNDERLINED.

Setting Approach S1 S2 S3 S4 S5 S6 S7 S8 S9 Avg.

NT 69.17 32.78 68.92 41.25 34.58 41.81 42.40 65.73 60.97 50.84 AT 62.19 32.26 73.44 40.00 33.58 36.84 51.77 66.18 64.13 51.15

DANN 57.36 31.28 55.56 37.88 31.11 38.99 38.78 53.44 55.83 44.47 IRM 62.15 30.80 62.26 40.69 31.81 38.54 36.98 55.10 54.48 45.87 GroupDro 62.50 33.13 59.38 41.49 35.52 39.86 33.92 54.06 51.42 45.70 MLDG 53.68 28.19 60.97 27.29 32.53 28.99 40.69 48.13 53.37 41.54 RSC 66.88 30.94 71.08 38.85 32.74 37.33 40.31 60.94 58.19 48.58

CT

.

FedAvg 60.59 29.93 54.97 37.40 31.15 39.06 36.60 46.94 52.15 43.20 FAL 54.90 30.56 55.17 36.88 31.35 37.12 36.04 52.57 58.96 43.73 FedProx 53.33 28.61 54.24 35.42 29.38 37.40 38.26 45.00 42.60 40.47

FL

SCAFFOLD 41.22 26.81 39.17 29.27 27.60 29.06 27.15 31.91 40.10 32.48 MOON 64.24 30.80 68.26 37.67 34.31 38.47 43.65 58.40 54.13 47.77 FedFA 59.55 33.61 56.32 39.62 30.90 38.06 40.03 46.88 53.65 44.29

GA 45.59 27.01 48.19 36.32 31.81 39.76 32.15 32.50 44.76 37.57 SAFE 65.80 30.63 72.53 41.91 36.67 38.06 62.99 66.08 66.56 53.47

TABLE IV CROSS-SUBJECT BCAS (%) FOR BENIGN SAMPLES ON MI3. THE BEST ACCURACY IN EACH COLUMN IS MARKED IN BOLD, AND THE SECOND BEST UNDERLINED.

Setting Approach S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 Avg.

NT 68.25 84.75 90.13 87.63 76.75 70.25 94.00 72.50 93.50 68.25 85.25 79.88 63.00 50.38 77.46 AT 62.50 83.50 81.00 77.88 80.63 76.38 93.13 66.63 92.00 68.50 81.50 76.00 58.88 50.13 74.90

DANN 64.63 82.63 93.88 82.25 65.63 66.13 91.63 71.00 93.75 63.00 74.75 71.13 63.13 54.88 74.17 IRM 65.13 83.38 87.63 83.50 74.50 72.50 91.13 69.50 93.50 68.00 80.13 79.63 60.13 50.25 75.63 GroupDro 64.38 82.38 71.00 81.50 71.00 68.25 89.50 60.50 92.88 65.75 82.50 70.88 59.38 48.13 72.00 MLDG 58.38 61.63 64.75 63.63 66.88 55.50 77.50 50.88 91.38 57.50 71.13 60.00 51.63 50.25 62.93 RSC 70.13 85.25 91.00 84.38 76.88 73.75 94.50 67.88 93.50 67.12 84.25 83.63 61.50 48.25 77.29

CT

.

FedAvg 58.50 83.88 55.75 83.25 82.13 69.50 91.00 52.88 95.13 64.75 79.25 66.25 58.88 49.75 70.78 FAL 55.25 74.63 57.00 65.25 76.25 62.75 84.38 55.88 93.63 65.13 75.75 61.38 57.25 49.25 66.70 FedProx 57.25 82.38 56.38 73.25 80.63 65.00 86.88 51.63 95.50 65.25 80.13 68.00 59.88 49.88 69.43

FL

SCAFFOLD 67.13 82.13 61.50 74.25 68.88 70.38 90.00 62.38 94.38 66.63 74.50 56.00 59.63 52.25 70.00 MOON 61.38 85.63 66.75 85.50 73.13 71.88 93.63 54.63 95.38 66.63 83.88 81.50 60.63 49.38 73.56 FedFA 60.75 79.88 59.13 80.13 79.00 68.13 87.38 59.13 94.88 65.38 81.00 71.38 60.00 48.63 71.05

GA 54.25 81.38 52.00 79.38 74.13 62.38 87.13 52.50 95.13 62.63 74.63 57.88 58.25 50.50 67.29 SAFE 71.50 82.38 94.75 81.38 80.63 75.50 91.25 80.75 93.38 68.50 82.13 82.63 60.50 47.50 78.05

TABLE V

- CROSS-SUBJECT BCAS (%) FOR BENIGN SAMPLES ON ERP1. THE BEST ACCURACY IN EACH COLUMN IS MARKED IN BOLD, AND THE SECOND BEST UNDERLINED.

.

Setting Approach S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 Avg.

CT

NT 74.56 86.97 77.88 81.99 83.35 79.09 79.77 73.78 85.97 84.35 80.77 AT 74.47 82.08 74.45 82.47 81.72 80.07 79.63 72.34 83.71 81.01 79.19

DANN 73.85 86.24 77.69 81.81 83.43 78.76 77.10 72.34 84.54 84.24 80.00 IRM 73.64 85.81 78.01 83.62 85.44 78.26 78.77 73.96 86.23 85.12 80.88 GroupDro 69.26 85.03 76.68 83.19 84.19 78.28 77.14 73.54 83.69 84.10 79.51 MLDG 64.25 67.43 63.08 65.33 66.50 68.54 60.78 58.44 59.86 63.20 63.74 RSC 73.41 85.95 78.46 83.55 86.34 79.24 78.38 74.64 86.17 84.77 81.09

FL

FedAvg 70.54 79.15 75.15 80.93 87.28 75.51 66.63 70.19 80.24 85.92 77.15 FAL 73.94 82.35 76.30 81.74 88.65 79.58 70.10 72.89 83.74 83.49 79.28 FedProx 71.99 82.06 76.77 81.30 87.95 78.94 71.49 72.79 84.34 85.92 79.36

SCAFFOLD 63.93 79.69 74.52 76.36 82.22 77.96 76.17 70.37 80.70 78.91 76.08 MOON 72.23 83.49 76.40 81.48 87.30 78.79 74.36 74.12 84.98 82.94 79.61 FedFA 73.42 84.16 78.06 81.90 87.77 78.41 74.13 74.11 86.59 84.22 80.28

GA 68.49 78.81 75.63 82.32 84.67 74.42 67.53 70.87 80.40 84.46 76.76 SAFE 75.71 84.28 77.42 83.05 87.94 81.35 80.09 75.63 86.58 84.13 81.62

TABLE VI

- CROSS-SUBJECT BCAS (%) FOR BENIGN SAMPLES ON ERP2. THE BEST ACCURACY IN EACH COLUMN IS MARKED IN BOLD, AND THE SECOND BEST UNDERLINED.

Setting Approach S1 S2 S3 S4 S5 S6 S7 S8 Avg.

NT 71.46 67.54 73.04 68.71 71.97 70.44 71.95 71.60 70.84 AT 70.03 66.35 70.46 67.57 70.11 69.40 72.30 70.23 69.55

DANN 70.83 66.70 72.90 67.75 70.21 68.77 70.51 70.70 69.80 IRM 71.95 68.55 74.07 69.02 73.07 70.43 72.07 70.41 71.20 GroupDro 71.25 69.20 74.41 68.83 71.89 69.24 71.53 68.09 70.55 MLDG 54.64 50.43 53.25 52.20 51.81 51.80 51.85 50.09 52.01 RSC 71.98 67.68 74.03 69.30 72.45 70.65 71.72 71.05 71.11

CT

FedAvg 70.74 66.52 75.04 70.26 72.08 68.62 70.23 72.77 70.78 FAL 69.83 66.05 74.44 70.81 70.95 68.66 71.25 72.40 70.55 FedProx 71.13 65.52 74.99 70.28 72.25 68.12 70.91 71.31 70.57

FL

SCAFFOLD 66.27 61.76 66.73 65.39 65.07 65.61 66.05 66.75 65.45 MOON 70.79 65.66 74.52 70.07 71.93 68.25 69.27 71.28 70.22 FedFA 72.17 66.23 75.05 69.81 71.88 69.34 70.09 73.37 70.99

GA 67.89 64.72 73.52 69.44 71.14 69.06 70.20 74.14 70.01 SAFE 70.83 68.60 74.73 70.81 72.03 70.01 71.59 72.99 71.45

B. BCAs on Adversarial Samples

Figs. 4-7 respectively show the average BCAs on adversarial samples under three white-box attacks and two black-box attacks across the five datasets, with varying attack magnitude (ϵ = 0 corresponds to the benign samples).

Observe that:

- 1) In general, methods without adversarial defense mechanisms exhibited significant performance degradation on adversarial samples, particularly in white-box attacks.
- 2) Compared to CT, FL approaches had some ability to resist adversarial attacks (e.g., FedAvg outperformed NT under strong attacks), likely due to the inherent disturbance from client distribution heterogeneity in FL training.
- 3) Under white-box attacks, AT, FAL, and SAFE methods equipped with adversarial defense mechanisms demonstrated robust resilience against adversarial attacks, subject to only minor performance degradation.
- 4) Under black-box attacks, SAFE demonstrated negligible performance degradation as the attack intensity increased. This is significant in real-world applications,

where attackers seldom have complete access to the model.

5) Overall, SAFE achieved the highest classification accuracy across diverse datasets, attack types, and intensity levels, demonstrating its effectiveness in defending against adversarial attacks while protecting EEG data privacy.

C. Ablation Studies

Ablation studies were conducted to check if each strategy used in SAFE was effective and necessary.

Table VII presents the average BCAs for benign samples, white-box adversarial samples, and black-box adversarial samples on MI1 and ERP1. While LBSN achieved competitive accuracy on benign samples, it showed severe vulnerability to white-box attacks. FAT or AWP alone significantly compromised the accuracy on benign samples. While using all three strategies may lead to a slight decrease in the accuracy on benign samples, it significantly enhanced the adversarial robustness. Overall, each strategy was effective, and using all three of them together resulted in the optimal performance.

ϵ = 0 ϵ = 0.01 ϵ = 0.03 ϵ = 0.05

CT FL

40

30

BCA(%)

20

10

0

NT AT

GA

FAL

IRM

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(a) MI1

CT FL

50

40

30

BCA(%)

20

10

0

NT AT

GA

FAL

IRM

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(b) MI2

CT FL

80

70

60

BCA(%)

50

40

30

20

NT AT

GA

IRM

FAL

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(c) MI3

Fig. 4. Average BCAs on the adversarial samples under three white-box attacks with different magnitudes ϵ ∈ {0, 0.01, 0.03, 0.05} on the three MI datasets. (a) MI1; (b) MI2; and, (c) MI3.

ϵ = 0 ϵ = 0.01 ϵ = 0.05 ϵ = 0.1

CT FL

40

35

30

BCA(%)

25

20

15

NT AT

GA

FAL

IRM

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(a) MI1

CT FL

55

50

45

40

BCA(%)

35

30

25

NT AT

GA

FAL

IRM

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(b) MI2

CT FL

75

70

65

BCA(%)

60

55

50

45

NT AT

GA

IRM

FAL

RSC

SAFE

FedFA

DANN

MLDG

MOON

FedAvg

FedProx

GroupDro

SCAFFOLD

(c) MI3

Fig. 5. Average BCAs on the adversarial samples under two black-box attacks with different magnitudes ϵ ∈ {0, 0.01, 0.05, 0.1} on the three MI datasets. (a) MI1; (b) MI2; and, (c) MI3.

D. Impact of Client Selection and Local Optimization on FL Performance

In practice, the configuration of FL requires careful consideration, particularly with respect to the number of selected clients per round (m) and the number of local optimization epochs (E).

Figs. 8 and 9 respectively illustrate the average BCAs of SAFE under various values of m and E on MI1, for benign samples, white-box adversarial samples, and black-box adversarial samples. The performance of SAFE converged very

fast for both m and E, which is desirable in real-world BCIs. VI. CONCLUSIONS

This paper has proposed SAFE to address three challenges in EEG-based BCIs: inadequate generalization, adversarial vulnerability, and privacy leakage. SAFE utilizes FL to protect user EEG data privacy, and LBSN to adapt to client data distribution shifts and improve generalization. Additionally, it adopts a dual-defense mechanism to defend against adversarial attacks. Experiments on five EEG datasets from MI

ϵ = 0 ϵ = 0.01 ϵ = 0.03 ϵ = 0.05

CT FL

CT FL

80

70

75

65

70

BCA(%)

BCA(%)

60

65

55

60

50

55

NT AT

NT AT

GA

GA

IRM

IRM

FAL

FAL

RSC

RSC

SAFE

SAFE

FedFA

FedFA

DANN

DANN

MLDG

MLDG

MOON

MOON

FedAvg

FedAvg

FedProx

FedProx

GroupDro

GroupDro

SCAFFOLD

SCAFFOLD

(a) ERP1

(b) ERP2

- Fig. 6. Average BCAs on the adversarial samples under three white-box attacks with different magnitudes ϵ ∈ {0, 0.01, 0.03, 0.05} on the two ERP datasets. (a) ERP1; and, (b) ERP2.

ϵ = 0 ϵ = 0.01 ϵ = 0.05 ϵ = 0.1

NT AT

DANN

IRM

GroupDro

MLDG

RSC

FedAvg

FAL

FedProx

SCAFFOLD

MOON

FedFA

GA

SAFE

55

60

65

70

75

80

BCA(%)

CT FL

(a) ERP1

NT AT

DANN

IRM

GroupDro

MLDG

RSC

FedAvg

FAL

FedProx

SCAFFOLD

MOON

FedFA

GA

SAFE

50

55

60

65

70

BCA(%)

CT FL

(b) ERP2

- Fig. 7. Average BCAs on the adversarial samples under two black-box attacks with different magnitudes ϵ ∈ {0, 0.01, 0.05, 0.1} on the two ERP datasets. (a) ERP1; and, (b) ERP2.

[Figure 5]

- Fig. 8. Average cross-subject BCAs for benign samples, white-box adversarial samples, and black-box adversarial samples under various values of m (number of selected clients per round) on MI1.

[Figure 6]

Fig. 9. Average cross-subject BCAs for benign samples, white-box adversarial samples, and black-box adversarial samples under various values of E (number of local optimization epochs) on MI1.

TABLE VII AVERAGE BCAS (%) FOR BENIGN SAMPLES, WHITE-BOX ADVERSARIAL SAMPLES AND BLACK-BOX ADVERSARIAL SAMPLES IN ABLATION STUDIES ON MI1 AND ERP1. THE BEST ACCURACY IN EACH COLUMN FOR EACH DATASET IS MARKED IN BOLD.

Strategy Samples

Dataset

Avg. LBSN FAT AWP Benign White Black

35.53 10.28 26.20 24.00 42.27 12.94 40.85 32.02 26.11 20.27 25.51 23.96 35.59 13.95 26.60 25.38

MI1

- 40.71 25.04 40.09 35.28

- 41.89 15.64 40.59 32.71

25.63 20.21 25.00 23.61 41.86 27.75 41.32 36.98

77.15 67.04 69.60 71.26 81.23 70.95 79.47 77.22

- 79.19 72.62 73.88 75.23

- 80.16 70.43 71.96 74.18

- 80.44 73.78 79.62 77.95

- 81.66 71.47 79.87 77.66

79.93 73.53 74.72 76.06

- 81.62 75.11 80.44 79.06

ERP1

and ERP paradigms demonstrated that SAFE outperformed 14 state-of-the-art approaches in terms of decoding accuracy and adversarial robustness, including CT methods that do not consider privacy protection at all. To our knowledge, SAFE is the first algorithm to simultaneously achieve high decoding accuracy, strong adversarial robustness, and reliable privacy protection, without using any calibration data from the target subject. These characteristics make it very desirable for realworld BCIs.

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain–computer interfaces for communication and control,” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.
- [2] H. Lorach, A. Galvez, V. Spagnolo, F. Martel, S. Karakas, N. Intering, M. Vat, O. Faivre, C. Harte, S. Komi et al., “Walking naturally after spinal cord injury using a brain-spine interface,” Nature, vol. 618, no. 7963, pp. 126–133, 2023.
- [3] L. R. Hochberg, D. Bacher, B. Jarosiewicz, N. Y. Masse, J. D. Simeral, J. Vogel, S. Haddadin, J. Liu, S. S. Cash, P. Van Der Smagt et al., “Reach and grasp by people with tetraplegia using a neurally controlled robotic arm,” Nature, vol. 485, no. 7398, pp. 372–375, 2012.
- [4] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao, “High-speed spelling with a noninvasive brain-computer interface,” Proc. National Academy of Sciences, vol. 112, no. 44, pp. E6058–E6067, 2015.
- [5] F. R. Willett, D. T. Avansino, L. R. Hochberg, J. M. Henderson, and K. V. Shenoy, “High-performance brain-to-text communication via handwriting,” Nature, vol. 593, pp. 249–254, 2021.
- [6] S. L. Metzger, K. T. Littlejohn, A. B. Silva, D. A. Moses, M. P. Seaton, R. Wang, M. E. Dougherty, J. R. Liu, P. Wu, M. A. Berger et al., “A high-performance neuroprosthesis for speech decoding and avatar control,” Nature, vol. 620, no. 7976, pp. 1037–1046, 2023.
- [7] D. Wu, B.-L. Lu, B. Hu, and Z. Zeng, “Affective Brain-Computer Interfaces (aBCIs): A Tutorial,” Proc. of the IEEE, vol. 11, no. 10, pp. 1314–1332, 2023.
- [8] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proceedings of the IEEE, vol. 89, no. 7, pp. 1123–1134, 2001.
- [9] U. Hoffmann, J.-M. Vesin, T. Ebrahimi, and K. Diserens, “An efficient P300-based brain–computer interface for disabled subjects,” Journal of Neuroscience Methods, vol. 167, no. 1, pp. 115–125, 2008.

- [10] O. Friman, I. Volosyak, and A. Graser, “Multiple channel detection of steady-state visual evoked potentials for brain-computer interfaces,” IEEE Trans. on Biomedical Engineering, vol. 54, no. 4, pp. 742–750, 2007.
- [11] D. Wu, X. Jiang, and R. Peng, “Transfer learning for motor imagery based brain-computer interfaces: A tutorial,” Neural Networks, vol. 153, pp. 235–253, 2022.
- [12] X. Zhang and D. Wu, “On the vulnerability of CNN classifiers in EEG-based BCIs,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 27, no. 5, pp. 814–825, 2019.
- [13] X. Zhang, D. Wu, L. Ding, H. Luo, C.-T. Lin, T.-P. Jung, and R. Chavarriaga, “Tiny noise, big mistakes: adversarial perturbations induce errors in brain–computer interface spellers,” National Science Review, vol. 8, no. 4, p. nwaa233, 2021.
- [14] J. Jung, H. Moon, G. Yu, and H. Hwang, “Generative perturbation network for universal adversarial attacks on brain-computer interfaces,” IEEE Journal of Biomedical and Health Informatics, vol. 27, no. 11, pp. 5622–5633, 2023.
- [15] L. Meng, X. Jiang, X. Chen, W. Liu, H. Luo, and D. Wu, “Adversarial filtering based evasion and backdoor attacks to EEG-based braincomputer interfaces,” Information Fusion, vol. 107, p. 102316, 2024.
- [16] A. Binnendijk, T. Marler, and E. M. Bartels, Brain-Computer Interfaces: U.S. Military Applications and Implications, An Initial Assessment. Santa Monica, CA: RAND Corporation, 2020.
- [17] K. Xia, W. Duch, Y. Sun, K. Xu, W. Fang, H. Luo, Y. Zhang, D. Sang, X. Xu, F.-Y. Wang, and D. Wu, “Privacy-Preserving Brain-Computer Interfaces: A Systematic Review,” IEEE Trans. on Computational Social Systems, vol. 10, no. 5, pp. 2312–2324, 2023.
- [18] H. He and D. Wu, “Transfer Learning for Brain-Computer Interfaces: A Euclidean Space Data Alignment Approach,” IEEE Trans. on Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [19] D. Wu, “Revisiting Euclidean alignment for transfer learning in EEGbased brain–computer interfaces,” Journal of Neural Engineering, vol. 22, no. 3, p. 031005, 2025.
- [20] L. Meng, X. Jiang, and D. Wu, “Adversarial robustness benchmark for EEG-based brain–computer interfaces,” Future Generation Computer Systems, vol. 143, pp. 231–247, 2023.
- [21] X. Chen, L. Meng, Y. Xu, and D. Wu, “Adversarial artifact detection in EEG-based brain–computer interfaces,” Journal of Neural Engineering, vol. 21, no. 5, p. 056043, 2024.
- [22] X. Chen, T. Jia, and D. Wu, “Data alignment based adversarial defense benchmark for EEG-based BCIs,” Neural Networks, vol. 188, p. 107516, 2025.
- [23] L. Meng, X. Jiang, J. Huang, W. Li, H. Luo, and D. Wu, “User Identity Protection in EEG-Based Brain–Computer Interfaces,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 3576–3586, 2023.
- [24] C. Shao, C. Li, R. Song, X. Liu, R. Qian, and X. Chen, “Machine Unlearning for Seizure Prediction,” IEEE Trans. on Cognitive and Developmental Systems, vol. 16, no. 6, pp. 1969–1981, 2024.
- [25] X. Chen, S. Li, Y. Tu, Z. Wang, and D. Wu, “User-wise perturbations for user identity protection in EEG-based BCIs,” Journal of Neural Engineering, vol. 22, no. 1, p. 016040, 2025.
- [26] W. Zhang and D. Wu, “Lightweight Source-Free Transfer for PrivacyPreserving Motor Imagery Classification,” IEEE Trans. on Cognitive and Developmental Systems, vol. 15, no. 2, pp. 938–949, 2023.
- [27] X. Chen, Z. Wang, and D. Wu, “Alignment-Based Adversarial Training (ABAT) for Improving the Robustness and Accuracy of EEG-Based BCIs,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 1703–1714, 2024.
- [28] X. Chen, T. Jia, and D. Wu, “Accurate, Robust and Privacy-Preserving Brain-Computer Interface Decoding,” arXiv preprint arXiv:2412.11390, 2024.
- [29] Q. Yang, Y. Liu, T. Chen, and Y. Tong, “Federated machine learning: Concept and applications,” ACM Trans. on Intelligent Systems and Technology, vol. 10, no. 2, pp. 1–19, 2019.
- [30] K. Zhou, Z. Liu, Y. Qiao, T. Xiang, and C. C. Loy, “Domain generalization: A survey,” IEEE Trans. on Pattern Analysis and Machine Intelligence, vol. 45, no. 4, pp. 4396–4415, 2022.
- [31] J. Wang, C. Lan, C. Liu, Y. Ouyang, T. Qin, W. Lu, Y. Chen, W. Zeng, and P. S. Yu, “Generalizing to unseen domains: A survey on domain generalization,” IEEE Trans. on Knowledge and Data Engineering, vol. 35, no. 8, pp. 8052–8072, 2022.
- [32] C. Shorten and T. M. Khoshgoftaar, “A survey on image data augmentation for deep learning,” Journal of Big Data, vol. 6, no. 1, pp. 1–48, 2019.

- [33] K. Zhou, Y. Yang, T. Hospedales, and T. Xiang, “Learning to Generate Novel Domains for Domain Generalization,” in Proc. of European Conf. on Computer Vision. Online: Springer International Publishing, Aug. 2020, pp. 561–578.
- [34] Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. March, and V. Lempitsky, “Domain-adversarial training of neural networks,” Journal of Machine Learning Research, vol. 17, no. 59, pp. 1–35, 2016.
- [35] M. Arjovsky, L. Bottou, I. Gulrajani, and D. Lopez-Paz, “Invariant risk minimization,” arXiv preprint arXiv:1907.02893, 2019.
- [36] Z. Ding and Y. Fu, “Deep domain generalization with structured lowrank constraint,” IEEE Trans. on Image Processing, vol. 27, no. 1, pp. 304–313, 2017.
- [37] D. Li, Y. Yang, Y.-Z. Song, and T. Hospedales, “Learning to Generalize: Meta-Learning for Domain Generalization,” in Proc. of the AAAI Conf. on Artificial Intelligence, vol. 32, no. 1, New Orleans, Louisiana, USA, Feb. 2018.
- [38] Z. Huang, H. Wang, E. P. Xing, and D. Huang, “Self-challenging improves cross-domain generalization,” in Proc. of European Conf. on Computer Vision. Online: Springer, Aug. 2020, pp. 124–140.
- [39] S. Sagawa, P. W. Koh, T. B. Hashimoto, and P. Liang, “Distributionally Robust Neural Networks,” in Proc. of Int’l Conf. on Learning Representations, Online, Apr. 2020.
- [40] F. M. Carlucci, A. D’Innocente, S. Bucci, B. Caputo, and T. Tommasi, “Domain generalization by solving jigsaw puzzles,” in Proc. of the IEEE/CVF Conf. on Computer Vision and Pattern Recognition, Long Beach, California, USA, Jun. 2019, pp. 2229–2238.
- [41] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards Deep Learning Models Resistant to Adversarial Attacks,” in Proc. of Int’l Conf. on Learning Representations, Vancouver, BC, Canada, Apr. 2018.
- [42] S. Addepalli, V. B.S., A. Baburaj, G. Sriramanan, and R. V. Babu, “Towards Achieving Adversarial Robustness by Enforcing Feature Consistency Across Bit Planes,” in Proc. of the IEEE/CVF Conf. on Computer Vision and Pattern Recognition, Seattle, CA, USA, June 2020, pp. 14–19.
- [43] J. Folz, S. Palacio, J. Hees, and A. Dengel, “Adversarial Defense based on Structure-to-Signal Autoencoders,” in Proc. of IEEE Winter Conference on Applications of Computer Vision, Snowmass, CO, USA, Mar. 2020, pp. 3568–3577.
- [44] C. Guo, M. Rana, M. Cisse, and L. van der Maaten, “Countering Adversarial Images using Input Transformations,” in Proc. of Int’l Conf. on Learning Representations, Vancouver, BC, Canada, Apr. 2018.
- [45] X. Jia, X. Wei, X. Cao, and H. Foroosh, “Comdefend: An efficient image compression model to defend adversarial examples,” in Proc. of the IEEE/CVF Conf. on Computer Vision and Pattern Recognition, Long Beach, CA, USA, Jun. 2019, pp. 6084–6092.
- [46] R. Gunawardena, S. Jayawardena, S. Seneviratne, R. Masood, and S. S. Kanhere, “Single-Sensor Sparse Adversarial Perturbation Attacks Against Behavioral Biometrics,” IEEE Internet of Things Journal, vol. 11, no. 16, pp. 27303–27321, 2024.
- [47] J. Liang, D. Hu, and J. Feng, “Do We Really Need to Access the Source Data? Source Hypothesis Transfer for Unsupervised Domain Adaptation,” in Proc. of Int’l Conf. on Machine Learning, vol. 119. Online: PMLR, Jul. 2020, pp. 6028–6039.
- [48] B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. Arcas, “Communication-Efficient Learning of Deep Networks from Decentralized Data,” in Proc. of Int’l Conf. on Artificial Intelligence and Statistics, vol. 54, Ft. Lauderdale, FL, Apr. 2017, pp. 1273–1282.
- [49] X. Li, Z. Song, and J. Yang, “Federated Adversarial Learning: A Framework with Convergence Analysis,” in Proc. of Int’l Conf. on Machine Learning, vol. 202. PMLR, Jul. 2023, pp. 19932–19959.
- [50] T. Li, A. K. Sahu, M. Zaheer, M. Sanjabi, A. Talwalkar, and V. Smith, “Federated Optimization in Heterogeneous Networks,” in Proc. of Machine Learning and Systems, vol. 2, Austin, TX, Mar. 2020, pp. 429–450.
- [51] S. P. Karimireddy, S. Kale, M. Mohri, S. Reddi, S. Stich, and A. T. Suresh, “Scaffold: Stochastic controlled averaging for federated learning,” in Proc. of Int’l Conf. on Machine Learning, Online, Jul. 2020, pp. 5132–5143.
- [52] Q. Li, B. He, and D. Song, “Model-Contrastive Federated Learning,” in Proc. of the IEEE/CVF Conf. on Computer Vision and Pattern Recognition, Online, Jun. 2021.
- [53] T. Zhou and E. Konukoglu, “FedFA: Federated Feature Augmentation,” in Proc. of Int’l Conf. on Learning Representations, Kigali, Rwanda, May 2023.
- [54] R. Zhang, Q. Xu, J. Yao, Y. Zhang, Q. Tian, and Y. Wang, “Federated domain generalization with generalization adjustment,” in Proc. of

- the IEEE/CVF Conf. on Computer Vision and Pattern Recognition, Vancouver, Canada, Jun. 2023, pp. 3954–3963.
- [55] K. Xia, L. Deng, W. Duch, and D. Wu, “Privacy-Preserving Domain Adaptation for Motor Imagery-Based Brain-Computer Interfaces,” IEEE Trans. on Biomedical Engineering, vol. 69, no. 11, pp. 3365–3376, 2022.
- [56] W. Zhang, Z. Wang, and D. Wu, “Multi-Source Decentralized Transfer for Privacy-Preserving BCIs,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 2710–2720, 2022.
- [57] C. Ju, D. Gao, R. Mane, B. Tan, Y. Liu, and C. Guan, “Federated Transfer Learning for EEG Signal Classification,” in Proc. of Int’l Conf. of the IEEE Engineering in Medicine & Biology Society, Online, Jul. 2020, pp. 3040–3045.
- [58] R. Liu, Y. Chen, A. Li, Y. Ding, H. Yu, and C. Guan, “Aggregating intrinsic information to enhance BCI performance through federated learning,” Neural Networks, vol. 172, p. 106100, 2024.
- [59] T. Jia, L. Meng, S. Li, J. Liu, and D. Wu, “Federated Motor Imagery Classification for Privacy-Preserving Brain-Computer Interfaces,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 3442–3451, 2024.
- [60] I. J. Goodfellow, J. Shlens, and C. Szegedy, “Explaining and Harnessing Adversarial Examples,” in Proc. of Int’l Conf. on Learning Representations, San Diego, CA, USA, May 2015.
- [61] D. Wu, S.-T. Xia, and Y. Wang, “Adversarial Weight Perturbation Helps Robust Generalization,” in Proc. of Int’l Conf. on Neural Information Processing Systems, vol. 33. Vancouver, BC, Canada: Curran Associates, Inc., Dec. 2020, pp. 2958–2969.
- [62] W. Yi, S. Qiu, K. Wang, H. Qi, L. Zhang, P. Zhou, F. He, and D. Ming, “Evaluation of EEG oscillatory patterns and cognitive process during simple and compound limb motor imagery,” PloS one, vol. 9, no. 12, p. e114853, 2014.
- [63] M. Tangermann, K.-R. M¨uller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. Miller, G. Mueller-Putz, G. Nolte, G. Pfurtscheller, H. Preissl, G. Schalk, A. Schl¨ogl, C. Vidaurre, S. Waldert, and B. Blankertz, “Review of the BCI Competition IV,” Frontiers in Neuroscience, vol. 6, p. 55, 2012.
- [64] D. Steyrl, R. Scherer, J. Faller, and G. R. M¨uller-Putz, “Random forests in non-invasive sensorimotor rhythm brain-computer interfaces: a practical and convenient non-linear classifier,” Biomedical Engineering / Biomedizinische Technik, vol. 61, no. 1, pp. 77–86, 2016.
- [65] P. Aric`o, F. Aloise, F. Schettini, S. Salinari, D. Mattia, and F. Cincotti, “Influence of P300 latency jitter on event related potential-based brain–computer interface performance,” Journal of Neural Engineering, vol. 11, no. 3, p. 035008, 2014.
- [66] A. Riccio, L. Simione, F. Schettini, A. Pizzimenti, M. Inghilleri, M. O. Belardinelli, D. Mattia, and F. Cincotti, “Attention and P300-based BCI performance in people with amyotrophic lateral sclerosis,” Frontiers in Human Neuroscience, vol. 7, p. 732, 2013.
- [67] F. Croce and M. Hein, “Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks,” in Proc. of Int’l Conf. on Machine Learning, vol. 119. Online: PMLR, Jul. 2020, pp. 2206–2216.
- [68] M. Andriushchenko, F. Croce, N. Flammarion, and M. Hein, “Square Attack: A Query-Efficient Black-Box Adversarial Attack via Random Search,” in Proc. of European Conf. on Computer Vision. Online: Springer International Publishing, Aug. 2020, pp. 484–501.
- [69] J. Chen and Q. Gu, “RayS: A Ray Searching Method for Hard-label Adversarial Attack,” in Proc. of ACM SIGKDD Int’l Conf. on Knowledge Discovery & Data Mining. New York, NY, USA: Association for Computing Machinery, Aug. 2020, pp. 1739–1747.
- [70] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.

