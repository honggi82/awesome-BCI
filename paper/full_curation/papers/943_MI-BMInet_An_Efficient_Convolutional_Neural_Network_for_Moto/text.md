1
MI-BMInet: An Efficient Convolutional Neural
Network for Motor Imagery Brain–Machine
Interfaces with EEG Channel Selection
Xiaying Wang, Member, IEEE, Michael Hersche, Student Member, IEEE, Michele Magno, Senior Member, IEEE,
Luca Benini, Fellow, IEEE
Abstract—A brain–machine interface (BMI) based on motor
imagery (MI) enables the control of devices using brain signals
while the subject imagines performing a movement. It plays
a vital role in prosthesis control and motor rehabilitation. To
improve user comfort, preserve data privacy, and reduce the
system’s latency, a new trend in wearable BMIs is to execute al-
gorithms on low-power microcontroller units (MCUs) embedded
on edge devices to process the electroencephalographic (EEG)
data in real-time close to the sensors. However, most of the
classification models present in the literature are too resource-
demanding, making them unfit for low-power MCUs. This paper
proposes an efficient convolutional neural network (CNN) for
EEG-based MI classification that achieves comparable accuracy
while being orders of magnitude less resource-demanding and
significantly more energy-efficient than state-of-the-art (SoA)
models for a long-lifetime battery operation. To further reduce
the model complexity, we propose an automatic channel selection
method based on spatial filters and quantize both weights and
activations to 8-bit precision with negligible accuracy loss. Finally,
we implement and evaluate the proposed models on leading-
edge parallel ultra-low-power (PULP) MCUs. The final 2-class
solution consumes as little as 30 µJ/inference with a runtime of
2.95 ms/inference and an accuracy of 82.51% while using 6.4ˆ
fewer EEG channels, becoming the new SoA for embedded MI-
BMI and defining a new Pareto frontier in the three-way trade-off
among accuracy, resource cost, and power usage.
Index Terms—brain-machine interfaces, internet of minds,
convolutional neural networks, feature extraction, embedded
systems, edge computing, machine learning, tinyML
I. INTRODUCTION
A brain–machine interface (BMI) aims to translate brain
activities into actionable information to control external de-
vices, such as a wheelchair [1] or a prosthesis [2]. Besides
clinical relevance for patients to regain lost abilities [3], recent
developments in wearable technologies have pushed the field
of BMI towards everyday life tasks in consumer products [4],
[5], for example, to control robots [6] or drones [7], yielding
improved user experience also for healthy subjects [8]. Motor
Manuscript received November 07, 2019; revised January 16, 2020; ac-
cepted February 10, 2020.
X. Wang, M. Hersche, and L. Benini are with the Integrated Systems
Laboratory, ETH Z¨urich, Switzerland (e-mail: xiaywang@iis.ee.ethz.ch). M.
Magno is with the Center for Project-Based Learning D-ITET, ETH Z¨urich,
Switzerland. M. Hersche is also with Cloud and AI Systems Research, IBM
Research, Z¨urich, Switzerland. L. Benini is also with the Department of
Electrical, Electronic and Information Engineering, University of Bologna,
Italy.
This project was supported by the Swiss Data Science Center PhD Fellow-
ship under grant ID P18-04.
imagery (MI) is of great interest among the current BMI
paradigms because it does not strictly depend on external
stimuli; hence, it can be independently and asynchronously
self-paced [9]. The MI-BMI decodes the user’s intention by
analyzing the brain activities while the subject thinks of a
movement of a body part without actually performing it [10].
A recent work by Zhuang et al. [11] has demonstrated
the successful usage of MI-BMI in controlling ground vehi-
cles using a wireless wearable device based on non-invasive
electroencephalograms (EEGs). The data processing and the
classification are executed on a remote engine, which leads to
potential privacy concerns, a longer latency, and higher power
consumption due to the data transmission. Recent achieve-
ments in low-power processing platforms and miniaturization
enable the sensor data processing directly at the edge [12],
[13]. By embedding algorithms at the sensor node, the data
is analyzed locally, preserving privacy, reducing the energy
consumption for a longer battery lifetime, and minimizing
the system’s latency [14]. The decoded information can be
directly sent to the controlled devices without any intermediate
apparatus between the brain and the machines, empowering the
future Internet of Minds (IoM) [15].
To achieve this goal, a smart wearable BMI has to satisfy
a three-way trade-off among a) algorithmic performance: the
embedded algorithm has to be able to complete the targeted
task accurately; b) computational and storage parsimony: the
complexity of the deployed algorithm has to meet the resource
constraints of the edge platform in terms of memory footprint
and runtime for a real-time application scenario; c) power:
the power consumption must be low to guarantee a long-term
continuous operation with long battery lifetime [14]. The low
signal-to-noise ratio of the EEG data and the inter-session and
inter-subject variability pose enormous challenges to obtaining
high classification accuracy. Several machine learning (ML)
and deep learning (DL) models have been proposed in the
literature, achieving remarkable algorithmic performance [16],
[17], [18]. However, the majority of them target only accuracy
as a key metric while ignoring the resources required by the
model, making them unfit for low-power microcontroller units
(MCUs). For example, the Mr. Wolf processor [19] from the
parallel ultra-low power (PULP) platform, a leading-edge ex-
ample of high-performance and low-power MCU, has less than
600 kB of on-chip fast memory and can deliver up to 16.4 Giga
operations per second (GOPS) of computational capability. It
has been embedded in a wearable BMI device, called Biowolf,
©2024 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including
reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any
copyrighted component of this work in other works. Published version: DOI: 10.1109/JSEN.2024.3353146
arXiv:2203.14592v5  [eess.SP]  19 Sep 2024

2
Resource-aware
model design
Dimensionality
reduction
Deployment on
low-power MCU
Channel selection
Efficient hardware
usage
Quantization
Smart wearable BMI with
long battery lifetime
Near-sensor
processing
Imagined
movement
Fig. 1: Overview of the proposed methods for a smart wearable
MI-BMI with embedded near-sensor processing.
with the minimal form factor of 40 mmˆ20 mmˆ2 mm and
consuming less than 10 mW [12]. When considering very low-
power MCUs in the sub-100-milliwatt power range, almost
all the state-of-the-art (SoA) networks cannot be deployed on-
board without additional expensive off-chip memory, yielding
increased power consumption and longer execution latency.
In full-precision representation, even the most compact EEG-
Net [20] is out-of-reach by requiring more than 1 MB for
storing the two biggest consecutive feature maps with the
standard layer-by-layer execution during inference, making the
deployment more challenging [21], [13]. In contrast, edge
devices with more resources are too power-hungry and do
not meet the specifications for long-term usage. Therefore,
resource-friendly models that at the same time maintain high
accuracy are desirable.
Besides considering the resource usage already during
the model design, additional methods to reduce the model
complexity are essential. In EEG applications, an important
topic is the channel selection, where the EEG channels with
more relevant features are selected for the final classification
stage [22], [23]. In this work, we emphasize the importance
of this technique not only for selecting the most significant
features to improve accuracy but also for its advantages
of reducing memory usage and computational complexity.
Moreover, the reduction of EEG channels lowers the system’s
power consumption since fewer analog front-end circuits are
necessary for data acquisition, and it is fundamental for im-
proving user comfort and achieving optimal device wearability.
Another effective method to reduce the resource requirements
is quantization, e.g., using 8 bits to represent numbers instead
of 32 bits [24], [25]. It yields a significant reduction in memory
usage and allows the use of efficient hardware units. Worth
to be noted that both channel reduction and quantization
pose challenges to the classification task and can lead to
accuracy degradation due to the reduced number of inputs
and numerical precision [21]. Hence, sophisticated algorithms
are demanded to guarantee comparable accuracy while using
minimal resources.
In this paper, we propose an end-to-end workflow for the
realization of an energy-efficient wearable MI-BMI enabled
with smart near-sensor computing, as shown in Fig. 1. We
select MCUs based on PULP platforms [19], [26], because
they have been demonstrated to outperform other families of
low-power MCUs thanks to the parallel cores and the custom
hardware extensions for digital signal processing (DSP) [27],
[28], [13], [29]. Our main contributions are as follows:
‚ We co-design a compact yet accurate convolutional neural
network (CNN) for MI-BMI classification constrained
to minimal hardware resources. It meets the tight re-
source limitations of ultra-low-power MCUs while being
as accurate as the resource-demanding SoA algorithms.
We evaluate the performance in both inter-session and
inter-subject challenges using two publicly available MI
datasets, namely the BCI Competition IV-2a and the
Physionet EEG Motor Movement/Imagery (MM/MI), and
achieve respectively 76.03%, 65.62% accuracy on the 4-
class task and 86.32%, 82.79% on the 2-class task.
‚ We reduce the input dimensions by automatically se-
lecting the most relevant EEG channels to limit further
the model complexity and the memory footprint while
maintaining similar classification accuracy (82.79% vs.
82.51% for the 2-class task of the MM/MI dataset) or
even improving the accuracy by up to 1.33% in the case
of the subject-specific models of the IV-2a dataset.
‚ We quantize both model weights and activations to 8-bit
precision with negligible effect on the classification ac-
curacy to further reduce the memory usage and optimally
exploit the hardware extensions. We efficiently deploy the
quantized models on ultra-low-power MCUs, achieving
an energy consumption of merely 30 µJ per inference and
real-time execution of 2.95 ms. With a 6.4ˆ reduction of
EEG channels, the battery operation time can be increased
from 3.8 up to 22 hours.
This work successfully satisfies the three-way trade-off among
performance, cost, and power [14] by maximizing the al-
gorithmic accuracy, minimizing the computational cost, and
minimizing the power consumption for a real-time smart
wearable MI-BMI with an extended battery lifetime, paving
the way to the future IoM1.
II. RELATED WORKS
We discuss the related works based on the popular BCI
Competition IV-2a dataset [30], [31] and the Physionet EEG
MM/MI dataset [32], [33]. The former is the most represen-
tative for subject-specific models and inter-session challenges,
whereas the latter includes a remarkable number of subjects
and is often used to tackle the inter-subject variability. We
select only the works that follow the competition rules for
the IV-2a dataset or train a global model validated on unseen
subjects for the MM/MI dataset for a correct and fair com-
parison. As this paper covers the full flow of model design,
channel selection, and embedded implementation, we divide
the discussion of the related works accordingly.
A. Classification Models
Traditional ML-based approaches require manual feature
extraction, based on which a classifier is trained to solve
the task. The most common and effective methods to extract
discriminative features in MI-BMIs are based on the Com-
mon Spatial Patterns (CSP) [34], [35] and the Riemannian
1Open-source code: https://github.com/pulp-platform/MI-BMInet.

3
geometry [36]. The authors in [22] and [37] propose spa-
tial or temporal filtering based on CSP, reaching a 2-class
classification accuracy of 80.56% and 79.6% on the IV-2a
dataset, respectively. The work in [38] compares the CSP
and Riemannian methods and demonstrates that Multiscale
Riemannian Classifier (MRC) achieves the best 4-class classi-
fication accuracy of 75.47% using multiple time windows with
a support vector machine (SVM). A more recent work [29]
based on MRC reduces the number of features and achieves a
4-class accuracy of 76.4% using different classifiers for each
subject. By combining Filter-Bank Common Spatial Patterns
(CSP), autoregressive models, and feature selection with mu-
tual information, the work in [39] achieves the highest 2-class
accuracy of 86.01%. The authors generalize the methods to
the 4-class task obtaining a Cohen’s kappa coefficient of 0.61.
Similar techniques of feature extraction are used in [40] with
Adaptive Boosting classifier, resulting in an improved kappa
value of 0.646.
In another vein, DL methods enable the classification of
BMI tasks without handcrafted features. Many works have
demonstrated the effectiveness of CNNs in learning temporal
and spatial features obtaining accuracy values ranging from
79.9% up to 86.96% for 2-class tasks [16], [18] and 74.31%
to 77.35% for 4-class tasks [17], [41], [42], [13], [43]. With
additional hyperparameters tuning specific to each subject,
the accuracy can be improved up to 83.84% on the 4-class
task [42]. For the inter-subject cases on MM/MI dataset, the
2- and 4-class accuracy values range from 80.38% to 83.26%
and 58.58% and 65.07%, respectively [44], [21], [23]. One
major drawback of the DL approach is that the models tend
to grow in size, increasing the demand for computational
and storage resources. FB3DCNN achieves the SoA accuracy
(86.96%) in the 2-class task of the IV-2a dataset, but it requires
storage for 46 million parameters [18], [42]. EEG-TCNet and
EEG-ITNet perform best in the 4-class task (77.35% and
76.74%, respectively) and have significantly fewer parameters
(below 5 k) [42], [43]. However, when considering the standard
layer-by-layer computation schedule, the additional memory
footprint required during the execution time is up to two
orders of magnitude more than the number of parameters,
making them significantly more challenging for very low-
power MCUs. In this paper, we propose a more compact
CNN with less than 50 k parameters and features to be stored
during the inference time. The resource requirement is orders
of magnitude lower than recent related works [17], [41], [42],
[18] while achieving similar classification accuracy.
B. Channel Selection
It is beneficial to reduce the number of EEG channels for
improved user comfort, a reduced setup time, a lower power
consumption, and a decreased model complexity. The authors
in [22] have proven that input EEG channels can be effectively
reduced subject-specifically from 22 to an average of 8.11
while improving the 2-class accuracy on the IV-2a dataset
by around 3% using CSP-based methods. A more recent
work [45] uses a fixed number of 15 channels for all subjects
reaching an accuracy of 79.19%. It is 4.42% less than [22],
demonstrating that selecting a variable number of channels for
each subject is beneficial. The authors in [46] combine CSP
with Riemannian distances obtaining an SoA classification
accuracy of 77.82% and a kappa value of 0.71 with an average
of 15.2 selected channels over the nine subjects of the IV-2a
dataset for the 4-class MI task. CNN-based channel reduction
approaches are also found in the literature [44], [23]. Dose
et al. [44] manually select subsets of EEG channels to com-
pare with related works and demonstrate that their proposed
architecture based on the shallow ConvNet [16] outperforms
most other models. More recent work by Tokovarov et al. [23]
applies an automatic channel selection method based on CNN
feature maps obtaining 82.34% accuracy with only 14 instead
of 64 channels on the 2-class MI task of the MM/MI dataset
outperforming the manual selection of [44]. Given the many
advantages of channel selection, in this work, we propose an
automatic method based on the spatial filters of the proposed
CNN. It can effectively reduce the number of channels from
64 to 10 for the MM/MI dataset, with the advantage of 1.3ˆ
fewer parameters, 3.1ˆ less memory footprint, and 1.4ˆ lower
computational complexity while having a negligible accuracy
drop of 0.28% for the 2-class inter-subject task. The inter-
session accuracy of the subject-specific models for the IV-2a
dataset is increased by up to 1.33%, with an average channel
reduction of 60% for the 2-class task.
C. Embedded Implementation
Over the recent years, increasing attention has been gained
by the embedded deployment of ML and DL models on
low-power edge devices, nourishing the fast-growing field of
TinyML [47] and giving birth to notable projects such as
TensorFlow Lite [48]. Some initial efforts can be also found
in the BMI literature. Belwafi et al. [49] propose a CSP-
based approach implemented in 16-bit precision on a Stratix-
IV field-programmable gate array (FPGA) board with a power
consumption of 700 mW. It achieves a 2-class accuracy of
78.85% on the IV-2a dataset with an inference time of 430 ms
and energy consumption of 301,000 µJ. Another embedded
implementation based on CSP can be found in [50]. The
accuracy on the IV-2a dataset is 80.55% and 67.21% for 2-
and 4-class tasks, respectively. The methods are implemented
in 20-bit precision on a Virtex-6 FPGA consuming 83.90 mW
and taking up to 11.66 ms (i.e., 978 µJ).
Two other works have implemented DL-based approaches
for MI-BMI on embedded devices [21], [13]. The authors
in [21] deploy an EEGNet-based CNN on two STMicro-
electronics MCUs featuring ARM Cortex-M4 and M7. The
model requires too much memory for the selected low-power
MCUs based on the X-CUBE-AI deployment tool provided by
the manufacturer. Hence, the input signals are downsampled,
shortened in time, and 38 manually selected EEG channels
are used. The 4-class accuracy on the MM/MI dataset drops
by 2.56% on the Cortex-M4 due to the limited hardware
resources. The embedded model with the highest accuracy
(64.76%) could be implemented only on the Cortex-M7, which
provides more resources but consumes one order of magni-
tude more power than the Cortex-M4. The model with the

4
highest accuracy takes 43.81 ms and consumes 18,100 µJ per
inference. A more energy-efficient implementation is proposed
in [13], outperforming all previous solutions based on FPGAs
and Cortex-M MCUs. The model is first quantized to 8-bit
fixed-point representation with negligible loss in accuracy and
implemented on Mr. Wolf, consuming only 11.75 mW. The
average quantized accuracy over the nine subjects of the IV-
2a dataset is 70.9% for the 4-class MI task. The energy
consumption is 337 µJ, and the inference time is 28.67 ms.
However, the classification accuracy is relatively low, and
the proposed solution is not flexible because it is designed
specifically for EEGNet and it abandons the common layer-by-
layer paradigm adopted by most deployment frameworks [47].
A very recent work [29] proposes an MRC implementation
with a combination of 8-, 16-, and 32-bit fixed-point and 32-bit
floating-point representations on the new PULP MCU called
Vega [26]. It is currently the SoA in terms of accuracy and
energy efficiency (74.1% 4-class quantized accuracy, 16.9 ms
inference time, and 198 µJ energy consumption).
In this work, we quantize the proposed CNN to 8 bits
achieving a 4-class quantized accuracy of 75.63%. The full-
channel implementations for the IV-2a dataset take 11.37 ms
and 5.10 ms and consume 114 µJ and 60.5 µJ on Mr. Wolf and
Vega, respectively. It is 4.7% and 1.5% more accurate than [13]
and the SoA [29]. The inference execution is 2.5ˆ and 3.3ˆ
faster, and it consumes 3ˆ and 3.3ˆ less on the same MCUs,
respectively. The energy consumption is further lowered by
reducing the number of EEG channels without significantly
affecting the accuracy.
III. METHODS
The workflow proposed in this paper is as follows: first, an
accurate classification model is designed by taking into consid-
eration hardware constraints; second, EEG channel selection
is performed to reduce the input dimensionality yielding
more energy-efficient models; third, the model is quantized to
minimize further the resource usage and is efficiently deployed
on the selected MCUs by exploiting the hardware extensions.
A. Network Architecture and Resource Requirements
As motivated in the introduction, our target is low-power
MI-BMIs, meaning that the classification model has to re-
spect strict resource availability. Hence, while designing the
network, we also assess the memory footprint and the compu-
tational complexity. Additionally, unlike most previous works,
which consider only the number of parameters, we propose
a more accurate estimation of the memory usage based on
the standard layer-by-layer computation schedule. This is
especially crucial for embedded deployment [51].
Fig. 2 depicts the proposed model named MI-BMInet. The
input array is arranged such that each row represents the EEG
signals from the electrodes, and each column is the sample at
every time point. The dimension is Nch ˆNs, with Nch being
the number of EEG channels and Ns the number of samples.
Many works in literature have demonstrated that temporal and
spatial features most successfully decode the EEG signals,
as they represent the temporal and spatial summation of
brain activities [16], [20], [41], [42], [43]. In all previous
works, the extraction of the temporal information causes
a significant increase in memory usage and computations,
leading to deployment difficulties [21], [13]. In our proposed
CNN, we also extract temporal and spatial features, as this is
currently the most effective approach for EEG signals, but, in
contrast to previous works, we reduce the dimensionality by
first extracting the spatial features, followed by the extraction
of the temporal information. This way, the memory and the
computation overhead are effectively reduced.
More precisely, the input is passed to a first depthwise
convolutional layer with Nk one-dimensional kernels of size
Nch ˆ 1 to find spatial correlations among the EEG channels,
followed by a batch normalization layer. This spatial convolu-
tion outputs Nk feature maps of dimension 1 ˆ Ns. These
are subsequently filtered using another layer of depthwise
convolution with Nk kernels of dimension 1 ˆ Nf applied
along the temporal dimension to learn temporal information.
The number of parameters in a depthwise convolutional layer
can be calculated as Nk ¨ pkH ¨ kW q, with kH and kW being
the height and width of the kernels, reported in brackets
in Fig. 2. Additionally, each batch normalization layer has
4 ¨ f parameters, with f being the number of feature maps,
which corresponds to the number of filters Nk in the case
of depthwise convolutions. Afterward, a separable convolu-
tion, i.e., a depthwise convolution followed by a pointwise
convolution, is applied to extract additional spatio-temporal
features using Nk filters of size 1 ˆ 16. This amounts to
Nk¨p1¨16q`Nk¨Nk parameters. Rectified Linear Unit (ReLU)
is chosen as activation since it is the most hardware-friendly
non-linear activation function. Additionally, average pooling
layers with a kernel size of 8ˆ1 are applied in the time domain
to reduce the dimensions of the feature maps. Finally, a fully
connected layer computes the classification output. It presents
pNin ` 1q ¨ Nout parameters, with Nin being the number of
input nodes and Nout the output nodes, i.e., Ncl.
Besides the network weights, the input and the output fea-
ture maps need to be stored during the computation of a layer.
As an example, the size of the input and the output feature
maps of the first convolutional layer is Nch¨Ns`Nk¨Ns, which
has to be stored contemporaneously in the memory during the
computation time. Note that this memory can be reused for
the next layer once the computation of the previous one is
completed. Hence, the biggest sum of two consecutive feature
maps dictates the required memory footprint.
We further estimate the complexity of the model as the sum
of the number of multiply-and-accumulate (MACC) operations
in the convolutional and fully connected layers. The number of
operations in each depthwise convolutional layer is pkH ¨kW q¨
pHout ¨Woutq¨Nk, with Hout and Wout being respectively the
height and the width of the output feature maps. While for the
separable convolution, we estimate pHout¨Woutq¨pp1¨16q`Nkq
MACC operations. Finally, the fully connected layer requires
Nin ¨ Nout operations.
B. EEG Channel Selection
We propose an automatic channel selection method based on
the spatial filters of MI-BMInet to reduce further the resource

5
Ns{{8
Nk
Ns{{8{{8 ¨ Nk
Ncl
Ns
Nch
Nk
Nf
16
Spatial conv. Φ1
Separable conv. Φ3
Fully conn. Φ4
Ns{{8{{8
Temporal conv. Φ2
...
Ns
DepthConv2D (same, Nch ˆ 1)
BatchNorm2D
Quantization
DepthConv2D (valid, 1 ˆ Nf)
BatchNorm2D
ReLU
AvgPool2D (valid, 1 ˆ 8)
Quantization
DepthConv2D (same, 1 ˆ 16)
Quantization
Conv2D (1 ˆ 1)
BatchNorm2D
ReLU
AvgPool2D (valid, 1 ˆ 8)
Quantization
Dense
Nk
Fig. 2: Architecture of MI-BMInet. Ns is the number of input samples in the time domain, Nch the number of EEG channels,
Ncl the number of classes, Nf the filter size of the temporal filter, and Nk is the number of filters. The padding strategy and
the kernel size are reported in brackets. The addition of the quantization layers is highlighted in italic.
requirements. Given a pretrained model on all Nch EEG
channels and WS, the weights of the first spatial convolutional
layer with dimension Nch ˆ Nk, we compute the ℓ2-norm for
each EEG channel ich “ 1, 2, ..., Nch as
∥wS∥2pichq “
břNk
n“1|wSpich, nq|2,
(1)
which gives the vector’s magnitude of the weights corre-
sponding to each EEG channel. We subsequently select ¯Nch
channels with the biggest ∥wS∥2 amplitudes, with ¯Nch being
the desired number of EEG electrodes. Algorithm 1 shows the
pseudo-code of the proposed method.
For comparison, we implement two additional manual chan-
nel selection methods: one based on the whole scalp as
in [21]; the other one targets the specific brain region of
the sensorimotor cortex such that the EEG electrodes can
be embedded into smart wearable headphones, e.g., Versus
headset [52] or Melomind [53], for better user acceptance.
Fig. 1 in the Appendix shows the positions of the 64 electrodes
for the MM/MI dataset and the 22 channels filled with yellow
used in the IV-2a dataset. We select three configurations
that are evenly distributed over the entire scalp to directly
compare with [21] on the MM/MI dataset: a) 19 electrodes
Algorithm 1: Pseudo-code for automatic EEG channel
selection based on spatial filters of the proposed CNN.
Data: Pretrained model on all Nch channels.
Result: Indexes of ¯Nch selected channels.
begin
Load the pretrained model;
Extract WS, the weights of the spatial convolution;
for each EEG channel ich from 0 to Nch ´ 1 do
Calculate the ℓ2 norm
∥wS∥2pichq “
břNk
n“1|wSpich, nq|2
Find the indices that sort ∥wS∥2pichq in
descending order;
Take the first ¯Nch indices;
based on the international 10-20 system (excluding A1 and
A2), encircled with green dashed lines; b) 38 electrodes by
adding intermediate positions, encircled with solid blue lines;
c) 8 electrodes based on Bitbrain headset, encircled with
dash-dotted red lines. The distributed configurations are not
evaluated on the IV-2a dataset because of the reduced number
of available electrodes.
Furthermore, we manually select the EEG channels covering
the sensorimotor cortex, where most of the brain’s activations
during motor movement (MM) and MI are identified, espe-
cially around C3 and C4 [10]. This region is also physically
covered by the users’ audio headphones that are commonly
accepted and worn nowadays for extended time periods. This
means we can embed the EEG electrodes on a wearable device
already widely used in daily life. This setup is much less
obtrusive and aesthetically more acceptable than traditional
EEG caps. Hence, we select subsets of electrodes from the
central line covering the C3 and C4 electrodes, as highlighted
in Fig. 1 in the Appendix with the red-shaded background. In
addition, we separately and incrementally include subsets of
adjacent electrodes towards the front and the back of the head,
respectively shaded with the green and blue background color.
Table I in the Appendix reports all the configurations with the
selected subsets of channels over the sensorimotor cortex for
the MM/MI dataset. The same is done for the IV-2a dataset
with the available electrodes.
Additional comparisons with CSP- and Riemannian-based
methods are discussed in Sec. IV.
C. Embedded Implementation
To optimally deploy MI-BMInet on low-power MCUs,
we first quantize the models to 8-bit representations using
quantization-aware training to reduce further the memory
footprint and to exploit the hardware extensions. Subsequently,
we deploy the quantized networks on the selected MCUs and
measure the inference runtime and the power consumption.
1) Quantization: We quantize both weights and activa-
tions of MI-BMInet, including the input signals, from 32-bit
floating-point to 8-bit fixed-point values. To preserve the clas-
sification accuracy, we perform quantization-aware training.

6
The addition of the quantization layers is shown in Fig. 2.
The quantization procedure is as follows:
‚ The network is trained in full precision until epoch ta;
‚ At epoch ta, the quantization of the activations starts
using the straight-through estimator (STE) [54]. The
network is readjusted on the quantized activations until
epoch tw;
‚ From epoch tw until epoch tend, the weights are in-
creasingly quantized using Random Partition Relaxation
(RPR) [25] at a step size of 10.
2) Network Deployment: We implement the 8-bit quan-
tized networks on RISC-V-based PULP Mr. Wolf [19] and
Vega [26]. The former has been embedded into Biowolf, the
SoA BMI system in terms of power consumption, compu-
tational capability, and form factor [12]. While the latter is a
more recent microprocessor with improved design and technol-
ogy, presenting the SoA energy efficiency. They both feature a
System-on-Chip (SoC) domain with a single core for handling
peripherals and simple computations and a cluster domain with
eight and nine parallel cores for more compute-intensive tasks.
The cluster cores are based on RV32IMCF Instruction Set
Architecture (ISA) with additional custom extensions for DSP
applications, including hardware loops, post-incremental load
and store instructions, and support for two-way and four-way
Single Instruction, Multiple Data (SIMD) operations.
We propose a manual implementation of the quantized
models, as currently, no deployment tools directly support the
selected MCUs. However, we follow the same layer-by-layer
schedule to better demonstrate the deployment feasibility of
our models. We take inspiration from [13] and merge the con-
version factor of the quantization with the bias and the scaling
factor of the batch normalization layers and reorder the batch
normalization, the ReLU, and the pooling layers to reduce
the number of divisions since they are expensive operations
requiring many computational cycles and introduce rounding
errors. Moreover, we implement a concurrent computation of
the feature maps using the parallel cores and exploit the four-
way SIMD for executing four MACC operations on the 8-bit
quantized numbers in a single cycle. We export the network
weights in the reversed order with respect to convolutions to
use the optimized 1-D cross-correlation functions from the
PULP-DSP library [55]. We implement the data handling and
the computation of each layer such that the data locality is
preserved and the custom ISA extensions are effectively used.
IV. EXPERIMENTS AND RESULTS
We use Keras with TensorFlow v1.11 backend to train full-
precision models. We apply our methods to two SoA datasets
to tackle both inter-session and inter-subject variability.
a) BCI Competition IV-2a [30], [31]: Four MI tasks are
recorded from 9 subjects using 22 EEG channels, namely
the imagined movements of the left hand (L), right hand
(R), both feet (F), and tongue (T). The data is collected on
two days (i.e., sessions) at 250 Hz sampling frequency and
provided after a bandpass filter between 0.5 Hz and 100 Hz.
Each recording session contains 288 trials, of which 9.41%
are marked by an expert as artifacts and are removed. We
perform 2-, 3-, and 4-class classification using L/R, L/R/F, and
L/R/F/T MI tasks, respectively, and consider a time window
of 3 s starting from the appearance of the MI cue. We conduct
subject-specific validation using the EEG data of the first
session for training and the second for testing, as stated
in the competition rules. The models are trained with the
Adam optimizer for 500 epochs with a batch size of 32, a
fixed learning rate of 0.001, and 1e-7 as the default epsilon
value for numerical stability. The cross-entropy loss is used.
We repeat the experiments 25 times and report the average
results to consider the training variability. We calculate both
classification accuracy and Cohen’s kappa score as it is often
done with this dataset.
b) Physionet EEG MM/MI [32], [33]:
The data is
recorded at 160 Hz using 64 electrodes. 105 subjects are effec-
tively considered from this dataset. Every subject performed a
total of six MI runs: three runs of the left fist (L) against the
right fist (R) and three runs of both fists (B) against both feet
(F). We additionally extract windows of 3 s from the baseline
runs with eyes open to obtain trials with resting EEG data (0).
In total, we have 21 trials per class per subject. As in [44],
we perform 2-, 3-, and 4-class MI classification using L/R,
L/R/0, and L/R/0/F MI tasks, respectively, and consider a time
window of 3 s starting from the appearance of the cue. We use
5-fold cross-validation (CV) across the subjects, i.e., the model
is trained on the data from a subset of subjects and is validated
on the data from the remaining unseen subjects. The models
are trained with Adam optimizer for 100 epochs with a batch
size of 16. A fixed learning rate scheduler reaches the best
performance; more precisely, the learning rate is set to 0.01,
0.001, and 0.0001 at epochs 0, 40, and 80, respectively. Cross-
entropy loss is used. Similar to the IV-2a dataset, we repeat the
5-fold CV procedure five times and obtain an average accuracy
over 25 experiments to account for the training variability.
A. Network Architecture
Based on the performance achieved with hyperparameters
tuning, we choose the filter size Nf to be 64 and 128 and
the number of filters Nk to be 32 and 16 for the IV-2a
and the MM/MI dataset, respectively. As reported in Table I,
our model requires around 6.1 k and 4.2 k parameters in full-
channel configuration. The two biggest consecutive feature
maps contain 40.5 k and 38.4 k feature values for the IV-2a
TABLE I: Resource estimation considering all EEG channels
and the 4-class task. The two biggest consecutive feature maps
are marked in italic and the total resource requirements in bold.
BCI Comp. IV-2a
Physionet MM/MI
Nch=22, Ns=750, Nk=32, Nf =64
Nch=64, Ns=480, Nk=16, Nf =128
Layer
#params #features
#MACC
#params #features
#MACC
Input
16,500
30,720
Φ1
704+128
24,000
528,000 1,024+64
7,680
491,520
Φ2
2,048+128
3,000 1,536,000 2,048+64
960
983,040
Φ3
1,536+128
176
96,000
512+64
112
30,720
Φ4
1,412
4
704
484
4
448
Tot.
6,084
40,500 2,209,408
4,228
38,400
1,505,728

7
TABLE II: Comparison of accuracy and kappa values (κ) in
full-channel, full-precision configuration. The publication year
follows the apostrophe. The total number of parameters, the
maximum number of consecutive features, and the number
of MACC operations are estimated on the 4-class task when
available, otherwise on the 2-class task. The proposed solution
is highlighted in bold.
Accuracy [%] / κ
Tot. #
params
Max. #
cons. f.
Tot. #
MACC
2-
4-class
BCI Comp. IV-2a
CSP’15 [22]
80.56 / -
- / -
-
-
MRC’18 [38]
- / -
75.47 / -
-
-
-
FBCSP’20 [40]
- / -
- / 0.65
-
-
-
JSTFD+LDA’20 [37]
79.6 / -
- / -
-
-
-
MI-TS’20 [39]
86.01 / -
- / 0.61
-
-
-
MRC’21 [56], [29]:
- / -
75.10 / -
-
-
-
S. ConvNet’17 [16]||
79.90 / - 74.31 / 0.66
47.3 k
1,013 k
63.0 M
EEGNet’18 [20]||
- / -
71.30 / -
2.63 k
223 k 12.98 M
MSFBCNN’19 [17]
- / -
75.80 / -
155 k
5,775 k
202 M
MCNN’19 [41]
- / -
75.7 / -
14 M
574 k
103 M
EEG-TCNet’20 [42];
- / - 77.35 / 0.70
4.27 k
396 k
6.8 M
FB3DCNN’21 [18]
86.96 / -
- / -
46 M
472.1 k
62.3 M
EEG-ITNet’22 [43]
- / -
76.74 / -
5.2 k
74.3 k
7.36 M
MI-BMInet˚
86.32 / 0.73 76.03 / 0.68
6.08 k
40.5 k
2.21 M
Physionet MM/MI
S. ConvNet’18 [44]
80.38/ -
58.58/ -
203 k
1,260 k 86.12 M
EEGNet’20 [21]§
82.43 / -
65.07 / -
3.2 k 277.56 k 31.98 M
CNN’20 [23]
83.26 / -
- / -
235 k 122.88 k 33.61 M
MI-BMInet˚
82.79 / -
65.62 / -
4.23 k
38.40 k
1.51 M
: Improved to 76.4% using different classifiers for each subject.
; Improved to 83.84% / 0.78 using subject-specific hyperparameters.
|| Adapted and reproduced in [18], [42], [13].
§ Based on [20].
˚ Respectively 80.37% / 0.71 and 74.92% for 3-class task.
and the MM/MI datasets. This means that the execution of
MI-BMInet requires the memory storage for only 46.6 k and
42.6 k values, comprehensive of both model parameters and
the maximum number of features during inference. It is at
least 1.7ˆ [43] and up to two orders of magnitude [17], [41],
[18] less than the related works reported in Table II.
When comparing the computational complexity, MI-BMInet
requires the least number of MACC operations, i.e., down to
2.21 million for the IV-2a dataset and 1.51 million for the
MM/MI dataset. In contrast to the most compute-intensive
related works [17], [44], our models require 91ˆ and 57ˆ
fewer computations while being 0.23% and 7.04% more ac-
curate on the IV-2a and MM/MI datasets, respectively. More
recent works have reduced the computational complexity [42],
[18], [43]; however, our model still requires at least 3ˆ fewer
computations. This directly correlates with the computational
latency during inference time, as shown in Sec. IV-C.
Despite the significantly fewer resource requirements, the
accuracy of MI-BMInet is overall comparable to recent SoA
models. More specifically, the accuracy values are 86.32%,
80.37%, 76.03% (IV-2a), and 82.79%, 74.92%, 65.62%
(MM/MI), respectively for 2-, 3-, 4-class tasks. The highest
4-class accuracy on the IV-2a dataset following the compe-
tition rules is around 77% without additional subject-specific
hyperparameters tunings [42]. The authors have improved the
accuracy to about 84% with variable networks. As more details
are needed to understand the reason behind this accuracy
2
4
6
8
10
12
14
16
18
20
52
56
60
64
68
72
76
80
84
88
Number of channels
Accuracy [%]
BCI Comp. IV-2a
Center
Center+Front
Center+Back
Auto
2 classes
3 classes
4 classes
2
4
6
8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
44
48
52
56
60
64
68
72
76
80
84
Physionet MM/MI
Distributed
Center
Center+Front
Center+Back
Auto
2 classes
3 classes
4 classes
Number of channels
Accuracy [%]
Fig. 3: Channel selection accuracy averaged over subjects for
the IV-2a dataset (top) and over CV folds for the MM/MI
dataset (bottom). The solid lines indicate the full-channel
accuracy and the circles mark the optimal number of channels.
increase, we discuss this comparison separately in Sec. V.
More recent works achieve 86.96% and 76.74% 2- and 4-
class accuracy values (less than 0.71% difference from ours)
but demand significantly more resources, i.e., 997.3ˆ and
1.7ˆ more parameters and features, and 28.2ˆ and 3.3ˆ more
MACCs [18], [43].
B. EEG Channel Selection
As shown in Fig. 3, our automatic method consistently
outperforms the manual selection methods. It can reduce, on
average, the number of channels down to 9, 11, and 14 across
the 9 subjects of the IV-2a dataset while retaining similar
average accuracy (86.21%, 79.91%, 75.84%) as the baseline,
represented with solid lines (86.32%, 80.37%, 76.03%), re-
spectively for the 2-, 3-, and 4-class tasks. In some cases,
slightly better accuracy is achieved compared to the full-
channel baseline thanks to the subject-specific methodology.
We report the best accuracy for each subject with the cor-
responding number of channels in Table III. The average
accuracy is improved by up to 1.33%. The best performing

8
TABLE III: Classification accuracy (%) / kappa score with all channels and the best accuracy / kappa score for each subject
with the corresponding number of selected channels (in brackets) on the IV-2a dataset and comparison with related works. The
best accuracy values are highlighted in bold. The publication year is indicated with the apostrophe.
2-class
3-class
4-class
MI-BMInet
CSP’15 [22]
M-CSP’19 [45]
MI-BMInet
MI-BMInet
CSP+Riem.’20 [46]
S.
all ch.
sel. ch.
all ch.
sel. ch.
sel. ch.
all ch.
sel. ch.
all ch.
sel. ch.
sel. ch.
1
84.03 / 0.68
86.98 / 0.74 (4) 90.78 / -
83.36 / - (9) 90.78 / - (15) 89.43 / 0.84
91.18 / 0.87 (14) 83.10 / 0.78
84.41 / 0.80 (20)
87.51 / 0.81 (14)
2
71.15 / 0.42
72.65 / 0.45 (20) 59.85 / -
71.83 / - (11) 57.75 / - (15) 65.74 / 0.49
68.76 / 0.53 (16) 59.27 / 0.46
60.49 / 0.47 (18)
58.32 / 0.44 (18)
3
94.95 / 0.90
94.95 / 0.90 (22) 97.81 / -
98.54 / - (13) 97.08 / - (15) 91.67 / 0.88
92.18 / 0.88 (18) 90.64 / 0.88
90.97 / 0.88 (18)
89.01 / 0.86 (14)
4
74.38 / 0.49
76.66 / 0.53 (9) 68.10 / -
74.13 / - (3) 70.69 / - (15) 75.66 / 0.64
76.00 / 0.64 (14) 69.77 / 0.60
70.63 / 0.61 (18)
71.12 / 0.63 (15)
5
92.00 / 0.84
93.84 / 0.88 (4) 68.88 / -
71.11 / - (4) 61.48 / - (15) 79.17 / 0.70
80.33 / 0.71 (18) 71.83 / 0.62
73.61 / 0.65 (19)
63.44 / 0.49 (19)
6
79.48 / 0.59
81.11 / 0.62 (20) 66.67 / -
73.14 / - (8) 70.37 / - (15) 63.48 / 0.45
65.56 / 0.49 (20) 58.10 / 0.44
59.91 / 0.47 (11)
60.16 / 0.53 (11)
7
90.51 / 0.81
91.17 / 0.82 (20) 82.14 / -
83.57 / - (6) 72.14 / - (15) 88.49 / 0.83
88.97 / 0.84 (18) 84.71 / 0.80
85.76 / 0.81 (19)
93.14 / 0.92 (15)
8
98.06 / 0.96
98.27 / 0.97 (6) 97.01 / -
96.26 / - (14) 97.76 / - (15) 88.18 / 0.82
88.63 / 0.83 (19) 84.55 / 0.80
86.48 / 0.82 (18)
90.43 / 0.86 (17)
9
92.31 / 0.85
93.26 / 0.87 (14) 93.84 / -
94.61 / - (5) 94.62 / - (15) 81.53 / 0.72
82.05 / 0.73 (20) 82.33 / 0.76
82.36 / 0.77 (18)
87.21 / 0.83 (14)
Avg. 86.32 / 0.73 87.65 / 0.75 (13.2) 80.56 / - 83.61 / - (8.1) 79.19 / - (15) 80.37 / 0.71 81.52 / 0.72 (17.4) 76.03 / 0.68 77.18 / 0.70 (17.7) 77.82 / 0.71 (15.2)
Std.
8.96 / 0.18
8.42 / 0.17 (7.1) 14.85 / -
11.35 / - (4)
15.85 / - (-)
9.78 / 0.15
9.21 / 0.14 (2.2) 11.11 / 0.15
10.86 / 0.15 (2.5)
13.52 / 0.17 (2.3)
Avg.˚
87.24 / 0.75 (8.9)
81.09 / 0.72 (13.7)
76.62 / 0.69 (14.2)
Std.˚
8.40 / 0.17 (6)
9.23 / 0.14 (3.9)
10.95 / 0.15 (4.3)
˚ Taking the minimum number of channels while allowing a maximum accuracy degradation of 1%. See Appendix for the subject-specific values.
S1: 83.10%
S2: 59.27%
S3: 90.64%
S4: 69.77%
S5: 71.83%
S6: 58.10%
S7: 84.71%
S8: 84.55%
S9: 82.33%
Fig. 4: Heatmaps of ∥wS∥2pichq on the IV-2a dataset averaged over 25 repetitions with 4-class full-channel accuracy. Darker
red color represents higher values, meaning that the networks have learned stronger spatial weights.
(a) 2-class
(b) 3-class
(c) 4-class
Fig. 5: Heatmaps of ∥wS∥2pichq on the MM/MI dataset aver-
aged over 5-fold CV and 5 repetitions. Darker color indicates
regions corresponding to stronger learned spatial weights.
subjects for 2-, 3-, and 4-class tasks are S8, S3, and S3,
reaching up to 98.27%, 92.18%, and 90.97% with 6, 18, and
18 electrodes, respectively. Compared to the related works on
this dataset, our subject-specific models achieve 4.04% and
8.46% better accuracy than [22] and [45] for the 2-class task,
respectively, and 0.64% less accuracy than [46] for the 4-class
task. The number of selected channels corresponding to the
highest accuracy is vastly dependent on the subject, meaning
that the trade-off between accuracy and resource usage has to
be specifically assessed. An example is reported at the bottom
of Table III, where we select the minimum number of channels
for each subject while accepting an accuracy degradation of
1% at most. The average number of channels is further reduced
while maintaining similar accuracy values.
The results on the MM/MI dataset confirm that the auto-
matic method outperforms the manual methods. In general,
the simpler the task (i.e., 2-class), the less drop in accuracy.
More precisely, we achieve almost the same accuracy as the
baseline (82.79% and 74.92%) down to 10 and 20 channels
(82.51% and 74.21%) for the 2- and 3-class classification,
respectively. For the 4-class task, the accuracy drop is more
significant, i.e., 1.69%, when reducing the number of channels
to 18. Table IV reports the comparison with the related works.
The full-channel model by [23] achieves 0.47% better accuracy
than ours, at the cost of two orders of magnitude more memory
requirement and 22ˆ more complexity. Whereas our channel
selection method yields less accuracy drop (-0.15%) than [23]
(-0.92%) using 14 EEG channels. The authors did not further
reduce the number of channels. Compared to [44], [21], our
method consistently achieves better accuracy at lower resource
requirements. More specifically, a 14-channel configuration
achieves 5.98% better accuracy with 38.5ˆ fewer parameters,
19.1ˆ smaller feature map size, and 16.9ˆ less computation
than [44]. Compared to the method based on Granger causality
proposed in [57], our solution is overall comparable, with
slightly better accuracy when fewer channels are selected.
With our method based on the spatial filters, we can decrease
the number of EEG channels down to 10, i.e., by a factor
of 6.4ˆ, and still achieve comparable accuracy to the SoA
with full-channel configuration, proving the effectiveness of
our methods in extracting relevant features for the underlying
task. Compared to the baseline MI-BMInet with 64 channels,
using only 10 channels brings the advantage of 1.3ˆ fewer

9
parameters, 3.1ˆ less memory requirement, and 1.4ˆ less
complexity in terms of MACCs, while retaining a similar
classification accuracy of 82.51%.
We inspect the spatial filters of the trained models to gain
insights into the brain activations. The average ℓ2-norm values
of the spatial filters’ weights are depicted in Fig. 4 and
Fig. 5. Each subject of the IV-2a dataset presents a different
distribution over the scalp. Overall, the higher values are
near the electrodes C3, C4 over the sensorimotor cortex and
from the Cz to POz over the temporal lobe, indicating that
the networks have learned stronger spatial weights for these
regions. The analysis on the MM/MI dataset provides subject-
independent, global information on the relevant brain regions.
When considering the left- and right-hand tasks, the regions
under the C3 and C4 have higher values. The addition of the
‘rest’ class introduces stronger learned weights around Iz over
the occipital lobe, related to the visual cortex. The ‘feet’ class
induces activations around Cz over the sensorimotor cortex.
These findings are confirmed in the literature [10], [58]. We
additionally observe activations near the electrodes F7 and F8.
This is likely due to the presentation of the visual cues. We
discuss possible lines of investigation in Sec. V.
C. Embedded Implementation
TABLE IV: Comparison of accuracy and resource require-
ments with channel selection on the MM/MI dataset. The
estimated resources are calculated for the 4-class task when
available, otherwise for the 2-class task. The proposed solu-
tions are highlighted in bold.
# ch
Tot. #
params
Max. #
cons. f.
Tot. #
MACC
Accuracy
2-
3- 4-class
S.ConvNet’18 [44]
64
203 k
1,260 k 86.12 M 80.38 69.82
58.58
CNN’20 [23]
64
235 k 122.88 k 33.61 M 83.26
-
-
EEGNet’20 [21]§
64
3.17 k 276.48 k 48.17 M 82.29 74.46
64.85
MI-BMInet
64
4.23 k
38.40 k
1.51 M 82.79 74.92
65.62
EEGNet’20 [21]§
38
2.76 k 164.16 k 24.81 M 81.86 74.12
64.65
MI-BMInet
38
3.81 k
25.92 k
1.31 M 82.76 74.93
64.91
CNN’20 [23]
32
232 k
61.44 k 15.82 M 82.90
-
-
MI-BMInet
32
3.49 k
24.11 k
1.26 M 82.82 74.42
64.38
EEGNet’20 [21]§
19
2.35 k
82.08 k 11.02 M 81.95 72.41
62.55
MI-BMInet
19
3.51 k
16.8 k
1.16 M 82.78 74.02
63.69
S.ConvNet’18 [44]
16
126 k 314.88 k
21.6 M 78.03
-
-
MI-BMInet
16
3.23 k
15.36 k
1.14 M 82.63 73.47
63.47
S.ConvNet’18 [44]
14
123 k 275.52 k 18.92 M 76.66
-
-
CNN’20 [23]
14
231 k
26.88 k
6.68 M 82.34
-
-
GCCS’21 [57]
14
-
-
- 83.63
-
-
MI-BMInet
14
3.20 k
14.40 k
1.12 M 82.64 72.89
63.30
MI-BMInet
10
3.14 k
12.48 k
1.09 M 82.51 71.55
61.94
S.ConvNet’18 [44]
9
115 k 177.12 k 12.20 M 75.85
-
-
GCCS’21 [57]
9
-
-
- 81.26
-
-
MI-BMInet
9
3.12 k
12.00 k
1.08 M 82.06 71.24
61.44
EEGNet’20 [21]§
8
2.28 k
34.56 k
4.30 M 78.07 68.99
58.55
MI-BMInet
8
3.33 k
11.52 k
1.08 M 81.60 70.28
60.71
S.ConvNet’18 [44]
3
106 k
59.04 k
4.13 M 73.20
-
-
MI-BMInet
3
3.03 k
9.12 k
1.04 M 77.42 61.66
50.12
§ Based on [20]. The reported accuracy is reproduced by averaging over
five training/validation repetitions.
We use the PyTorch-based Quantlab framework [24] to
quantize the models before the embedded deployment. As de-
scribed in Sec. III-C, we perform quantization-aware training
with STE and RPR algorithms. For the IV-2a dataset, ta=450,
tw=550, and tend=650 yield the best results. We use the cross-
entropy loss and the Adam optimizer with a fixed learning
rate of 0.001 and eps=1e-7. For the MM/MI dataset, we have
ta=60, tw=160, and tend=260. For the 3- and 4-class tasks, a
fixed learning rate of 0.001 and eps=1e-9 yield the best results.
Whereas for the 2-class task, the same learning rate scheduler
as for the full-precision models is used with eps=1e-9.
The experimental results show that the quantized accuracy
values are similar to the full-precision ones, with a maximum
accuracy loss of 0.4%. More precisely, the values for 2-,
3-, 4-class tasks are 86.52%, 80.05%, 75.63% (IV-2a), and
82.61%, 75.12%, 65.31% (MM/MI), respectively. The quan-
tization of both weights and activations allows 4ˆ reduction
of the total memory footprint. More specifically, the memory
requirement is reduced from around 186 kB and 171 kB when
using 32-bit representation down to roughly 47 kB and 43 kB
with 8-bit quantization for the IV-2a and MM/MI datasets,
respectively. Recall that the fast L1 memory of Mr. Wolf is
only 64 kB [19]. Hence, with a memory footprint of less than
50 kB, we effectively eliminate the data transfer between the
L1 and L2 memory during the computation of a single layer,
reducing double-buffering overheads while maintaining similar
classification accuracy. As illustrated in Fig. 6, most related
works do not fit in the fast memory of Mr. Wolf and Vega,
especially without quantization. The memory requirement of
the quantized MI-BMInet is up to four orders of magnitude
lower, and it is within the tightest memory constraint (64 kB).
It also requires the least amount of MACCs.
We measure the power consumption and the inference
runtime of the deployed models using the Keysight N6705B
power analyzer (61.44 µs sampling interval), including all op-
TABLE V: Networks deployment and measurement results.
All Mr. Wolf cores run at 50 MHz with 0.8 V power supply as
in [13]. The SoC core of Vega runs at 50 MHz and the cluster
cores at 160 MHz as in [29]. The power supply is 0.65 V.
Dataset
BCI Comp.
Physionet
Num. classes
4
2
2
4
2
2
Num. channels
22
22
6:
64
64
10;
(Q) Accuracy (%)
75.63
86.52
97.76
65.31
82.61
82.51
Est. Memory (kB)
46.58
45.88
33.37
42.63
42.40
15.62
Est. #MACCs (M)
2.21
2.21
1.82
1.51
1.51
1.09
Mr. Wolf
Time/infer. (ms)
11.37
11.30
10.57
6.21
6.21
5.53
Avg. power (mW)
10.07
10.24
9.70
9.92
10.00
9.06
Energy/infer. (µJ)
114.5
115.7
102.5
61.60
62.10
50.10
Throughput (MMACCs/s)
194.3
195.5
172.6
242.5
242.4
197.2
En. Eff. (GMACCs/s/W)
19.30
19.09
17.80
24.44
24.24
21.77
Vega
Time/infer. (ms)
5.10
4.85
4.73
3.19
3.13
2.95
Avg. power (mW)
11.87
12.07
11.52
11.40
11.28
10.17
Energy/infer. (µJ)
60.5
58.5
54.5
36.4
35.3
30.0
Throughput (MMACCs/s)
433.3
455.7
384.8
473.4
482.4
369.5
En. Eff. (GMACCs/s/W)
36.50
37.75
33.40
41.52
42.77
36.33
: Subject 8. Selected channels: CP3, P1, POz, CP4, C6, FC4.
; Fold 1. Sel. channels: AF8, F8, T8, C3, Cz, C2, CP2, CP5, F6, T9.

10
101
102
103
104
105
65
70
75
80
85
90
64 kB
512 kB
128 kB
1500 kB
1 M 50 M
100 M
200 M
MI-BMInet
MI-BMInet
MI-BMInet
Q-EEGNet’20 [13]
EEGNet’18 [20]
S. ConvNet’17 [16]
MSFBCNN’19 [17]
EEG-TCNet’20 [42]
EEG-ITNet’22 [43]
MCNN’19 [41]
FB3DCNN’21 [18]
MRC’21 [56]
Memory footprint [kB]
Accuracy [%]
2-class
3-class
4-class
better
better
better
Fig. 6: Accuracy vs. memory footprint on the IV-2a dataset.
The number of MACCs is represented as the size of the circles,
while the square indicates that it is variable. The memory
footprint includes both parameters and features (see Table II).
The precision is assumed to be 32 bits if no quantization is
proposed. The dashed and dash-dotted lines mark the L1 and
L2 memory of Mr. Wolf and Vega, respectively.
eration domains of the selected microprocessors and the cluster
startup time. We set the clock frequency of the cores to the
same values as in [13] and [29] for a fair comparison. Table V
shows the results. The measured inference runtime on Mr.
Wolf is around 11.4 ms for the IV-2a dataset in full-channel
configuration and 6.2 ms for the MM/MI dataset. The average
power consumption is roughly 10 mW, yielding an energy
consumption per inference of 115 µJ and 62 µJ, respectively.
The execution time on Vega is more than twice faster and
consumes down to 36 µJ. Fig. 7 depicts the comparison with
the related works. Our implementation is orders of magnitude
faster and less energy-hungry. Compared to the most energy-
efficient model with the same MCU configurations [29], our
solution is 3.3ˆ faster and more energy-efficient and achieves
higher classification accuracy. The channel reduction further
reduces the runtime and the energy consumption. Considering
the best performing subject (S8, 98.27% accuracy) of the IV-2a
dataset on the 2-class task, the number of EEG channels can
be decreased to 6 while keeping similar classification accuracy
(97.76%). It yields an energy reduction of approximately 10%
compared to the usage of all 22 channels. We can draw the
same conclusion for the subject-independent MM/MI dataset.
We successfully decrease the number of channels by a factor
of 6.4ˆ (from 64 to 10) without significant accuracy loss for
the 2-class task. It translates into a runtime speedup of 1.1ˆ
and an energy reduction of 15%, i.e., down to 30 µJ. Overall,
the highest achieved throughput is 482.4 MMACCs/s with an
energy efficiency of 42.77 GMACCs/s/W.
V. DISCUSSION
The proposed CNN achieves similar accuracy as the most
recent related works [42], [18], [43], [23], while being sig-
nificantly more hardware-friendly. Note that our accuracy
2.9
.3.2
4.7
.5.1
11.7 16.9
.20.4 28.7
43.8
.
30
36.4
54.5
60.5
198
337
978
8.4 k
18.1 k
301 k
CSP+SVM’19 [50]
Fixed-20, 80.6 (22)
97.8 (6)
Q-EEGNet’20 [13]
Fixed-8, 70.9 (22)
75.6 (22)
MRC’21 [29]
Mixed, 74.1 (22)
82.5 (10)
EEGNet’20 [21]
Float-32, 64.8 (38)
EEGNet’20 [21]
Float-32, 62.5 (38)
65.3 (64)
BCI Comp. IV-2a
Physionet MM/MI
2 classes
4 classes
MI-BMInet
Fixed-8
Vega
Runtime [ms]
Energy [µJ]
430
WOLACSP
’18 [49]
Fixed-16,
78.9 (22)
better
better
Fig. 7: Energy consumption vs. runtime. The numerical preci-
sion and the accuracy (%) of the embedded implementation are
reported in italic. The number of EEG channels is in brackets.
values are averaged over multiple runs to account for the
variability caused by the non-deterministic behavior of the
training algorithms for a better statistical significance. The
standard deviation among the training repetitions on the IV-2a
dataset is at least 1.3% [13]. Hence, our achieved accuracy is
comparable to the related works. The additional technique of
subject-specific hyperparameters tunings proposed in [42] has
improved the accuracy to almost 84%. This further strengthens
the evidence that subject-specific network architectures (e.g.,
variable kernel sizes, different number of filters) lead to signif-
icant accuracy gains. This technique can be easily adapted to
the proposed CNN, and similar improvements can be expected.
Notwithstanding, MI-BMInet has roughly 10ˆ less memory
footprint and 3ˆ fewer computations than [42], enabling its
deployment on ultra-low-power MCUs with real-time infer-
ence. The extraction of spatial information before the temporal
features substantially reduces resource usage. It is a universal
and effective technique that all related networks in Table II can
adopt to lower their resource demands, especially the recent
ones with multiple parallel convolutional blocks [17], [41],
[43]. Future directions can investigate subject-specific neural
architecture search while being aware of the memory and com-
putation burdens related to the order of the operations. EEG-
ITNet requires also relatively small resource usage thanks to
the downsampling of the input EEG signals [43]. It is also
an effective way to reduce the model size as demonstrated
in [21], and it can be considered as a preprocessing stage in
addition to our methods.
The proposed channel reduction algorithm further reduces
the resource requirements while retaining similar accuracy.
It additionally lowers the power consumption of the data
acquisition stage. Considering the same setup as in [12], i.e.,
0.965 mW/channel, 1.26 mW for the digital section excluding
the processing, and a 65 mAh battery, the reduction from 64
to 10 channels yields an increased battery life from 3.8 to
22 hours with the negligible consumption of 0.03 mW using

11
Vega or 0.05 mW using Mr. Wolf, assuming a continuous
classification every second.
The inspection of the spatial filters gives insights into the
relevant brain regions for MI tasks. Especially interesting are
the activations around F7 and F8 electrodes. They cover the in-
ferior frontal gyrus near the Sylvian fissure between the frontal
and temporal lobe, where the insular cortex is located [59],
[60]. This area is considered relevant in attentional elabora-
tions and working memory processing related to external stim-
uli [61], [62]. Being part of the dorsal frontoparietal network, it
has a top-down control function over motor and sensory areas
with the basic cognitive selection of sensory information and
response [63]. Moreover, a study suggests that it plays a role
in motor planning and imagery [64]. A similar line of research
on the insular cortex, saccade system, and supplementary
motor areas further confirms the involvement of this area in
motor control, attentional fixation, and responses to switching
stimuli [65], [66]. Another study suggests that the activities in
this area are due to electromyographic and electrooculographic
artifacts [44]. Depending on the acquisition setup, this is also
a valid hypothesis since the electrodes F7 and F8 are prone
to collect muscular and ocular artifacts [67]. An acquisition
procedure that eliminates the dependency on the visual cue
is helpful in future research to investigate the fundamental
nature of this activation. A possible solution is to design an
experimental paradigm combined with electromyograms [68].
Another future research direction is the detection of move-
ment intention. For a real-world IoM scenario, no visual cue
is presented to the subject marking the MI’s start. Hence,
algorithms that can autonomously detect the onset of the
MI intention are necessary for an online BMI that is asyn-
chronously self-paced.
VI. CONCLUSION
This paper proposes an energy-efficient embedded solution
for MI-BMIs. We design a tiny CNN that achieves similar SoA
accuracy but is orders of magnitude less resource-demanding.
We further propose an automatic channel reduction method
based on spatial filters and extract the most relevant EEG
channels to effectively reduce the memory requirements,
the computational complexity, and the power consumption.
We finally deploy the proposed models on ultra-low-power
MCUs and experimentally measure the runtime and the energy
consumption. The final solution consumes down to 30 µJ
and takes only 2.95 ms per inference with an accuracy of
82.51% on the 2-class MI task using only 10 instead of
64 EEG channels, yielding an operation of up to 22 hours.
By combining a model design that is aware of the resource
usage, the channel reduction and the quantization techniques,
and an embedded implementation that optimally exploits the
underlying hardware architecture, we satisfy the three-way
trade-off among accuracy performance, resource usage, and
power consumption, setting the new SoA for next-generation
wearable BMIs with smart edge computing.
REFERENCES
[1] M. Xiong, R. Hotter, D. Nadin et al., “A low-cost, semi-autonomous
wheelchair controlled by motor imagery and jaw muscle activation,” in
Proc. IEEE International Conference on Systems, Man and Cybernetics
(SMC), 2019, pp. 2180–2185.
[2] M. Vilela and L. R. Hochberg, “Chapter 8 - applications of brain-
computer interfaces to the control of robotic and prosthetic arms,” in
Brain-Computer Interfaces, ser. Handbook of Clinical Neurology, N. F.
Ramsey and J. del R. Mill´an, Eds.
Elsevier, 2020, vol. 168, pp. 87–99.
[3] U.
Chaudhary,
N.
Birbaumer,
and
A.
Ramos-Murguialday,
“Brain–computer interfaces for communication and rehabilitation,”
Nature Reviews Neurology, vol. 12, pp. 513–525, 08 2016.
[4] A. Casson, “Wearable EEG and beyond,” Biomedical Engineering
Letters, vol. 9, pp. 53–71, 01 2019.
[5] P. Aric`o, N. Sciaraffa, and F. Babiloni, “Brain–computer interfaces:
Toward a daily life employment,” Brain Sciences, vol. 10, no. 3, 03
2020.
[6] L. Shao, L. Zhang, A. N. Belkacem et al., “EEG-controlled wall-
crawling cleaning robot using SSVEP-based brain-computer interface,”
Journal of Healthcare Engineering, vol. 2020, pp. 1–11, 01 2020.
[7] N.
Kobayashi
and
K.
Ishizuka,
“LSTM-based
classification
of
multiflicker-SSVEP in single channel dry-EEG for low-power/high-
accuracy quadcopter-BMI system,” in Proc. IEEE International Con-
ference on Systems, Man and Cybernetics (SMC), 2019, pp. 2160–2165.
[8] A. N. Belkacem, N. Jamil, J. A. Palmer, S. Ouhbi, and C. Chen, “Brain
computer interfaces for improving the quality of life of older adults and
elderly patients,” Frontiers in Neuroscience, vol. 14, p. 692, 2020.
[9] D. Freer and G.-Z. Yang, “Data augmentation for self-paced motor
imagery classification with C-LSTM,” Journal of Neural Engineering,
vol. 17, no. 1, p. 016041, 01 2020.
[10] G. Pfurtscheller and F. Lopes da Silva, “Event-related EEG/MEG
synchronization and desynchronization: basic principles,” Clinical Neu-
rophysiology, vol. 110, no. 11, pp. 1842–1857, 11 1999.
[11] J.
Zhuang,
K.
Geng,
and
G.
Yin,
“Ensemble
learning
based
brain–computer interface system for ground vehicle control,” IEEE
Transactions on Systems, Man, and Cybernetics: Systems, vol. 51, no. 9,
pp. 5392–5404, 2021.
[12] V. Kartsch, G. Tagliavini, M. Guermandi et al., “BioWolf: A sub-10-
mW 8-channel advanced brain–computer interface platform with a nine-
core processor and BLE connectivity,” IEEE Transactions on Biomedical
Circuits and Systems, vol. 13, no. 5, pp. 893–906, 2019.
[13] T. Schneider, X. Wang, M. Hersche, L. Cavigelli, and L. Benini, “Q-
EEGNet: an energy-efficient 8-bit quantized parallel EEGNet implemen-
tation for edge motor-imagery brain-machine interfaces,” in Proc. IEEE
International Conference on Smart Computing (SMARTCOMP), 2020,
pp. 284–289.
[14] C. Beach, E. Balaban, and A. J. Casson, “Chapter 14 - Edge algorithms
for wearables: an overview of a truly multi-disciplinary problem,” in
Wearable Sensors, 2nd ed., E. Sazonov, Ed.
Oxford: Academic Press,
2021, pp. 379–414.
[15] E. Tunstel, M. J. Cobo, E. Herrera-Viedma et al., “Systems science and
engineering research in the context of systems, man, and cybernetics:
Recollection, trends, and future directions,” IEEE Transactions on Sys-
tems, Man, and Cybernetics: Systems, vol. 51, no. 1, pp. 5–21, 2021.
[16] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer et al., “Deep
learning with convolutional neural networks for EEG decoding and
visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391–5420,
2017.
[17] H. Wu, Y. Niu, F. Li et al., “A parallel multiscale filter bank convolu-
tional neural networks for motor imagery EEG classification,” Frontiers
in Neuroscience, vol. 13, 11 2019.
[18] J. S. Bang, M. H. Lee, S. Fazli, C. Guan, and S. W. Lee, “Spatio-
spectral feature representation for motor imagery classification using
convolutional neural networks,” IEEE Transactions on Neural Networks
and Learning Systems, pp. 1–12, 2021.
[19] A. Pullini, D. Rossi, I. Loi, G. Tagliavini, and L. Benini, “Mr.Wolf:
An energy-precision scalable parallel ultra low power SoC for IoT edge
processing,” IEEE Journal of Solid-State Circuits, vol. 54, no. 7, pp.
1970–1981, 2019.
[20] V. J. Lawhern, A. J. Solon, N. R. Waytowich et al., “EEGNet: a compact
convolutional neural network for EEG-based brain–computer interfaces,”
Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
[21] X. Wang, M. Hersche, B. T¨omekce et al., “An accurate EEGNet-based
motor-imagery brain–computer interface for low-power edge comput-
ing,” in 2020 IEEE International Symposium on Medical Measurements
and Applications (MeMeA), 2020, pp. 1–6.
[22] A. K. Das and S. Suresh, “An effect-size based channel selection
algorithm for mental task classification in brain computer interface,” in
2015 IEEE International Conference on Systems, Man, and Cybernetics,
2015, pp. 3140–3145.

12
[23] M. Tokovarov, “Convolutional neural networks with reusable full-
dimension-long layers for feature selection and classification of motor
imagery in EEG signals,” in Artificial Neural Networks and Machine
Learning - ICANN 2020.
Springer International Publishing, 2020, pp.
79–91.
[24] M. Spallanzani, L. Cavigelli, G. Leonardi, M. Bertogna, and L. Benini,
“Additive noise annealing and approximation properties of quantized
neural networks,” arXiv:1905.10452, 05 2019.
[25] L. Cavigelli and L. Benini, “RPR: Random partition relaxation for
training; binary and ternary weight neural networks,” arXiv:2001.01091,
2020.
[26] D. Rossi, F. Conti, M. Eggiman et al., “A 1.3TOPS/W @ 32GOPS
fully integrated 10-core SoC for IoT end-nodes with 1.7uW cognitive
wake-up from MRAM-based state-retentive sleep mode,” in 2021 IEEE
International Solid- State Circuits Conference (ISSCC), vol. 64, 2021,
pp. 60–62.
[27] X. Wang, M. Magno, L. Cavigelli, and L. Benini, “Fann-on-mcu: An
open-source toolkit for energy-efficient neural network inference at the
edge of the internet of things,” IEEE Internet of Things Journal, vol. 7,
no. 5, pp. 4403–4417, 2020.
[28] A. Garofalo, M. Rusci, F. Conti, D. Rossi, and L. Benini, “PULP-
NN: accelerating quantized neural networks on parallel ultra-low-power
RISC-V processors,” Phil. Trans. R. Soc. A., 12 2019.
[29] X. Wang, L. Cavigelli, T. Schneider, and L. Benini, “Sub-100 µw
multispectral riemannian classification for eeg-based brain–machine
interfaces,” IEEE Transactions on Biomedical Circuits and Systems,
vol. 15, no. 6, pp. 1149–1160, 2021.
[30] C. Brunner, R. Leeb, G. R. M¨uller-Putz, A. Schl¨ogl, and G. Pfurtscheller,
“BCI competition 2008 - Graz data set A,” doi: 10.1007/BF00994018.
[31] M. Tangermann, K.-R. M¨uller, A. Aertsen et al., “Review of the BCI
competition IV,” Frontiers in Neuroscience, vol. 6, p. 55, 2012.
[32] G. Schalk, D. McFarland, T. Hinterberger, N. Birbaumer, and J. Wolpaw,
“BCI2000: a general-purpose brain-computer interface BCI system,”
IEEE Transactions on Biomedical Engineering, vol. 51, no. 6, pp. 1034–
1043, 2004.
[33] A. L. Goldberger, L. A. N. Amaral, L. Glass et al., “PhysioBank,
PhysioToolkit, and PhysioNet: components of a new research resource
for complex physiologic signals,” circulation, vol. 101, no. 23, pp. e215–
e220, 2000.
[34] K. K. Ang, Z. Y. Chin, C. Wang, C. Guan, and H. Zhang, “Filter bank
common spatial pattern algorithm on BCI competition IV datasets 2a
and 2b,” Frontiers in Neuroscience, vol. 6, p. 39, 2012.
[35] B. Chen, Y. Li, J. Dong, N. Lu, and J. Qin, “Common spatial patterns
based on the quantized minimum error entropy criterion,” IEEE Trans-
actions on Systems, Man, and Cybernetics: Systems, vol. 50, no. 11, pp.
4557–4568, 2020.
[36] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in brain-
computer interfaces: A review,” IEEE Transactions on Neural Systems
and Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, 10
2017.
[37] A. Jiang, J. Shang, X. Liu et al., “Efficient CSP algorithm with spatio-
temporal filtering for motor imagery classification,” IEEE Transactions
on Neural Systems and Rehabilitation Engineering, vol. 28, no. 4, pp.
1006–1016, 2020.
[38] M. Hersche, T. Rellstab, P. D. Schiavone et al., “Fast and Accurate
Multiclass Inference for MI-BCIs Using Large Multiscale Temporal
and Spectral Features,” in Proc. 26th European Signal Processing
Conference (EUSIPCO).
IEEE, 9 2018, pp. 1690–1694.
[39] J. Wang, Z. Feng, X. Ren et al., “Feature subset and time segment
selection for the classification of eeg data based motor imagery,”
Biomedical Signal Processing and Control, vol. 61, p. 102026, 2020.
[40] R. Das, P. S. Lopez, M. Ahmed Khan, H. K. Iversen, and S. Puthussery-
pady, “FBCSP and adaptive boosting for multiclass motor imagery
BCI data classification: A machine learning approach,” in Proc. IEEE
International Conference on Systems, Man, and Cybernetics (SMC),
2020, pp. 1275–1279.
[41] S. U. Amin, M. Alsulaiman, G. Muhammad, M. A. Mekhtiche, and
M. Shamim Hossain, “Deep learning for EEG motor imagery classifi-
cation based on multi-layer CNNs feature fusion,” Future Generation
Computer Systems, vol. 101, pp. 542–554, 2019.
[42] T. M. Ingolfsson, M. Hersche, X. Wang et al., “EEG-TCNet: An
accurate temporal convolutional network for embedded motor-imagery
brain–machine interfaces,” in Proc. IEEE International Conference on
Systems, Man, and Cybernetics (SMC), 2020, pp. 2958–2965.
[43] A. Salami, J. Andreu-Perez, and H. Gillmeister, “EEG-ITNet: An
explainable inception temporal convolutional network for motor imagery
classification,” IEEE Access, vol. 10, pp. 36 672–36 685, 2022.
[44] H. Dose, J. S. Møller, H. K. Iversen, and S. Puthusserypady, “An end-to-
end deep learning approach to MI-EEG signal classification for BCIs,”
Expert Systems with Applications, vol. 114, pp. 532–542, 2018.
[45] P. Gaur, R. B. Pachori, H. Wang, and G. Prasad, “An automatic subject
specific intrinsic mode function selection for enhancing two-class eeg-
based motor imagery-brain computer interface,” IEEE Sensors Journal,
vol. 19, no. 16, pp. 6938–6947, 2019.
[46] S. Chen, Y. Sun, H. Wang, and Z. Pang, “Channel selection based
similarity measurement for motor imagery classification,” in Proc. IEEE
International Conference on Bioinformatics and Biomedicine (BIBM),
2020, pp. 542–548.
[47] TinyML Foundation, “tinyML®,” https://www.tinyml.org/, 2021, ac-
cessed: 2021-05-27.
[48] R. David, J. Duke, A. Jain et al., “TensorFlow Lite Micro: Embedded
machine learning on TinyML systems,” arXiv:2010.08678, 2021.
[49] K. Belwafi, O. Romain, S. Gannouni et al., “An embedded implementa-
tion based on adaptive filter bank for brain–computer interface systems,”
Journal of Neuroscience Methods, vol. 305, pp. 1–16, 2018.
[50] A. Malekmohammadi, H. Mohammadzade, A. Chamanzar, M. Shabany,
and B. Ghojogh, “An efficient hardware implementation for a motor
imagery brain computer interface system,” Scientia Iranica, vol. 26, no.
Special Issue on: Socio-Cognitive Engineering, pp. 72–94, 2019.
[51] L. Lai, N. Suda, and V. Chandra, “Not all ops are created equal!” ArXiv,
vol. abs/1801.04326, 2018.
[52] N. M. LLC, “Versus: a mobile EEG headset,” https://getversus.com/,
2021, accessed: 2021-10-11.
[53] G. Spinelli, A. Odouard, M.-C. Nierat et al., “Validation of melo-
mind™signal quality: a proof of concept resting-state and ERPs study,”
bioRxiv:2020.02.28.969808, 2020.
[54] B. Jacob, S. Kligys, B. Chen et al., “Quantization and training of neural
networks for efficient integer-arithmetic-only inference,” in Proc. IEEE
CVPR, 2018, pp. 2704–2713.
[55] X. Wang, “DSP library for PULP,” https://github.com/pulp-platform/
pulp-dsp, 2019.
[56] X. Wang, T. Schneider, M. Hersche, L. Cavigelli, and L. Benini, “Mixed-
precision quantization and parallel implementation of multispectral
riemannian classification for brain–machine interfaces,” in Proc. IEEE
International Symposium on Circuits and Systems (ISCAS), 2021, pp.
1–5.
[57] H. Varsehi and S. M. P. Firoozabadi, “An eeg channel selection method
for motor imagery based brain–computer interface and neurofeedback
using granger causality,” Neural Networks, vol. 133, pp. 193–206, 2021.
[58] M. Zhao, M. Marino, J. Samogin, S. P. Swinnen, and D. Mantini, “Hand,
foot and lip representations in primary sensorimotor cortex: a high-
density electroencephalography study,” Brain Connectivity, vol. 9, pp.
2045–2322, 2019.
[59] R. Homan, J. Herman, and P. Purdy, “Cerebral location of international
10-20 system electrode placement,” Electroencephalography and Clini-
cal Neurophysiology, vol. 66, no. 4, pp. 376–82, 1987.
[60] V. L. Towle, J. Bola˜nos, D. Suarez et al., “The spatial location of EEG
electrodes: locating the best-fitting sphere relative to cortical anatomy,”
Electroencephalography and Clinical Neurophysiology, vol. 86, no. 1,
pp. 1–6, 1993.
[61] M. Tops and M. Boksem, “A potential role of the inferior frontal gyrus
and anterior insula in cognitive control, brain rhythms, and event-related
potentials,” Frontiers in Psychology, vol. 2, p. 330, 2011.
[62] M. Corbetta, G. Patel, and G. Shulman, “The reorienting system of the
human brain: from environment to theory of mind,” Neuron, vol. 58,
no. 3, pp. 306–24, 2008.
[63] M. Corbetta and G. Shulman, “Control of goal-directed and stimulus-
driven attention in the brain,” Nature Reviews Neuroscience, vol. 3, no. 3,
pp. 201–15, 2008.
[64] R. Ptak, A. Schnider, and J. Fellrath, “The dorsal frontoparietal network:
A core system for emulated action,” Trends in Cognitive Sciences,
vol. 21, no. 8, pp. 589–599, 2017.
[65] T. J. Anderson, I. H. Jenkins, D. J. Brooks et al., “Cortical control of
saccades and fixation in man. A PET study,” Brain, vol. 117, no. 5, pp.
1073–1084, 10 1994.
[66] P. Nachev, C. Kennard, and M. Husain, “Functional role of the
supplementary and pre-supplementary motor areas,” Nature Reviews
Neuroscience, vol. 9, no. 11, pp. 856–869, 2008.
[67] M. Sazgar and M. G. Young, EEG Artifacts.
Springer International
Publishing, 2019, pp. 149–162.
[68] R. Xu, N. Jiang, N. Mrachacz-Kersting et al., “A closed-loop
brain–computer interface triggering an active ankle–foot orthosis for
inducing cortical neural plasticity,” IEEE Transactions on Biomedical
Engineering, vol. 61, no. 7, pp. 2092–2101, 2014.

13
Xiaying Wang received her B.Sc. and M.Sc. de-
grees in biomedical engineering from Politecnico di
Milano, Italy, and ETH Z¨urich, Switzerland, in 2016
and 2018, respectively. She is currently pursuing a
Ph.D. degree at the Integrated Systems Laboratory at
ETH Z¨urich. Her research interests include biosignal
processing, brain–machine interface, low power em-
bedded systems, energy-efficient smart sensors, and
machine learning on microcontrollers. She received
the excellent paper award at the IEEE Healthcom
conference in 2018 and won the Ph.D. Fellowship
funded by the Swiss Data Science Center in 2019.
Michael Hersche received his M.Sc. degree from
the Swiss Federal Institute of Technology Zurich
(ETHZ), Switzerland, where he is currently pursuing
a Ph.D. degree. Since 2019, he has been a Research
Assistant with ETHZ in the group of Prof. L. Benini
at the Integrated Systems Laboratory. His research
interests include digital signal processing, artificial
intelligence, and communications with focus on hy-
perdimensional computing. He received the 2020
IBM Ph.D. Fellowship Award.
Michele Magno received his master’s and Ph.D.
degrees in electronic engineering from the Univer-
sity of Bologna, Bologna, Italy, in 2004 and 2010,
respectively. He is currently a Senior Researcher
and lecturer with ETH Z¨urich, Switzerland. He has
authored more than 150 papers in international jour-
nals and conferences, a few of them awarded as
best papers. His current research interests include
wireless sensor networks, wearable devices, energy
harvesting, low power management techniques, and
extension of the lifetime of batteries-operating de-
vices.
Luca Benini is the Chair of Digital Circuits and
Systems at ETH Z¨urich and a Full Professor at
the University of Bologna. He has served as Chief
Architect for the Platform2012 in STMicroelectron-
ics, Grenoble. Dr. Benini’s research interests are in
energy-efficient systems and multi-core SoC design.
He is also active in the area of energy-efficient smart
sensors and sensor networks. He has published more
than 1’000 papers in peer-reviewed international
journals and conferences, four books, and several
book chapters. He is a Fellow of the ACM and the
IEEE and a member of the Academia Europaea.

14
APPENDIX
Fig. 8: Electrode configurations for manual channel selections.
TABLE VI: EEG electrodes configurations using headset-
based channel selection over sensorimotor and neighboring
areas. The regions correspond to the brain areas with color-
shaded background illustrated in Fig. 8, as well as the elec-
trodes, while Nch is the number of selected channels.
Region
Nch
Electrodes
2
C3, C4
3
C3, CZ, C4
5
C5, C3, CZ, C4, C6
7
C5, C3, C1, CZ, C2, C4, C6
9
T7,C5, C3, C1, CZ, C2, C4, C6,T8
Central (C)
11
T9,T7,C5,C3,C1,CZ,C2,C4,C6,T8,T10
4
C3, C4, FC3, FC4
6
C3, CZ, C4, FC3, FCZ, FC4
10
C5, C3, CZ, C4, C6, FC5,FC3, FCZ, FC4,FC6
14
C5, C3, C1, CZ, C2, C4, C6,
FC5, FC3, FC1, FCZ, FC2, FC4, FC6
T7,C5, C3, C1, CZ, C2, C4, C6,T8,
18
FT7, FC5, FC3, FC1, FCZ, FC2, FC4, FC6, FT8
C+Frontal
20
T9,T7,C5,C3,C1,CZ,C2,C4,C6,T8,T10,
FT7, FC5, FC3, FC1, FCZ, FC2, FC4, FC6, FT8
4
C3, C4, CP3, CP4
6
C3, CZ, C4, CP3, CPZ, CP4
10
C5, C3, CZ, C4, C6, CP5, CP3, CPZ, CP4, CP6
14
C5, C3, C1, CZ, C2, C4, C6,
CP5, CP3, CP1, CPZ, CP2, CP4, CP6
18
T7,C5, C3, C1, CZ, C2, C4, C6,T8, TP7,
TP7, CP5, CP3, CP1, CPZ, CP2, CP4, CP6, TP8
C+Parietal
20
T9,T7,C5,C3,C1,CZ,C2,C4,C6,T8,T10,
TP7, CP5, CP3, CP1, CPZ, CP2, CP4, CP6, TP8
TABLE VII: Classification accuracy (%) / kappa score of MI-BMInet with all channels and with the minimum number of
selected channels (in brackets) when allowing a maximum accuracy degradation of 1% on the IV-2a dataset.
2-class
3-class
4-class
S.
all ch.
sel. ch.
all ch.
sel. ch.
all ch.
sel. ch.
1
84.03 / 0.68
86.98 / 0.74 (4) 89.43 / 0.84
91.03 / 0.87 (6) 83.10 / 0.78
83.89 / 0.79 (14)
2
71.15 / 0.42 72.03 / 0.44 (16) 65.74 / 0.49
68.76 / 0.53 (16) 59.27 / 0.46
59.52 / 0.46 (16)
3
94.95 / 0.90
94.10 / 0.88 (4) 91.67 / 0.88
91.65 / 0.88 (16) 90.64 / 0.88
90.97 / 0.88 (18)
4
74.38 / 0.49
76.07 / 0.52 (4) 75.66 / 0.64
76.00 / 0.64 (14) 69.77 / 0.60
70.63 / 0.61 (18)
5
92.00 / 0.84
93.84 / 0.88 (4) 79.17 / 0.70
79.54 / 0.69 (10) 71.83 / 0.62
72.64 / 0.64 (10)
6
79.48 / 0.59 81.11 / 0.62 (20) 63.48 / 0.45
64.69 / 0.47 (16) 58.10 / 0.44
59.42 / 0.46 (4)
7
90.51 / 0.81 90.63 / 0.81 (14) 88.49 / 0.83
88.57 / 0.83 (16) 84.71 / 0.80
84.90 / 0.80 (16)
8
98.06 / 0.96
97.76 / 0.96 (4) 88.18 / 0.82
88.26 / 0.82 (10) 84.55 / 0.80
85.93 / 0.81 (16)
9
92.31 / 0.85 92.62 / 0.85 (10) 81.53 / 0.72
81.33 / 0.72 (19) 82.33 / 0.76
81.67 / 0.76 (16)
Avg. 86.32 / 0.73 87.24 / 0.75 (8.9) 80.37 / 0.71 81.09 / 0.72 (13.7) 76.03 / 0.68 76.62 / 0.69 (14.2)
Std.
8.96 / 0.18
8.40 / 0.17 (6)
9.78 / 0.15
9.23 / 0.14 (3.9) 11.11 / 0.15
10.95 / 0.15 (4.3)
