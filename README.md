# Awesome BCI

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A taxonomy-first, citation-ranked map of recent Brain-Computer Interface (BCI) research.

Generated on 2026-06-25 from free public Semantic Scholar metadata. The current edition investigates up to 500 BCI-related candidate papers per year for 2020-2026, scores their importance, selects the top 100 papers per year, and reorganizes the final 700 papers by research taxonomy.

## Project Links

- Website: https://honggi82.github.io/awesome-BCI/
- Selected dataset: `data/papers_2020_2026.csv`
- Taxonomy dataset with paper-level ideas, strengths, and limitations: `data/papers_taxonomy_2020_2026.csv`
- Candidate pool: `data/candidates_top500_2020_2026.csv`
- English review draft: `paper/review_en.html`, `paper/review_en.docx`
- Korean review draft: `paper/review_ko.html`

## Taxonomy Overview

- **Motor Imagery and Movement Decoding**: 476 papers
- **SSVEP, P300, and ERP Spellers**: 99 papers
- **Invasive and Implantable Interfaces**: 39 papers
- **EEG Signal Processing and Datasets**: 29 papers
- **Rehabilitation and Neuroprosthetics**: 21 papers
- **General BCI Methods and Systems**: 14 papers
- **Deep Learning and Representation Learning**: 12 papers
- **Speech, Language, and Communication BCIs**: 7 papers
- **Hybrid, Affective, and Closed-loop BCIs**: 3 papers

## Taxonomy Collections

### Motor Imagery and Movement Decoding

- Papers selected: **476**
- Years covered: **2020-2026**
- Citation count in selected set: **24,907**
- Main research trends:
  - The field is moving from subject-specific pipelines toward cross-subject, calibration-light, and transfer-learning decoders for EEG motor imagery.
  - Deep CNN, temporal convolution, graph, attention, and large EEG representation models are increasingly used to improve robustness under noisy and low-data conditions.
  - Application work is expanding from binary hand imagery toward gait, lower-limb control, soft robotics, virtual feedback, and rehabilitation-oriented closed-loop use.

<details>
<summary>Show representative papers for Motor Imagery and Movement Decoding</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.48550/arXiv.2405.18765">Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI</a><br><sub>Wei-Bang Jiang, Li-Ming Zhao, Bao-Liang Lu</sub></td>
<td width="13%">2024<br>International Conference on Learning Representations<br>351 citations</td>
<td width="30%">The current electroencephalogram (EEG) based deep learning models are typically designed for specific datasets and applications in brain-computer interaction (BCI), limiting the scale of the models and thus diminishing their perceptual capabilities and generalizability.</td>
<td width="15%">high citation signal (351); influential citation signal (98)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1109/TII.2022.3197419">Physics-Informed Attention Temporal Convolutional Network for EEG-Based Motor Imagery Classification</a><br><sub>Hamdi Altaheri, G. Muhammad, Mansour Alsulaiman</sub></td>
<td width="13%">2023<br>IEEE Transactions on Industrial Informatics<br>370 citations</td>
<td width="30%">The brain-computer interface (BCI) is a cutting-edge technology that has the potential to change the world.</td>
<td width="15%">high citation signal (370); influential citation signal (40); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1126/science.abd0380">A brain-computer interface that evokes tactile sensations improves robotic arm control</a><br><sub>Sharlene N. Flesher, J. Downey, Jeffrey M. Weiss, Christopher L. Hughes, Angelica J. Herrera, E. Tyler-Kabara, et al.</sub></td>
<td width="13%">2021<br>Science<br>503 citations</td>
<td width="30%">A boost for brain–computer interfaces The finely controlled movement of our limbs requires two-way neuronal communication between the brain and the body periphery.</td>
<td width="15%">high citation signal (503); influential citation signal (13); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.1007/s00521-021-06352-5">Deep learning techniques for classification of electroencephalogram (EEG) motor imagery (MI) signals: a review</a><br><sub>Hamdi Altaheri, G. Muhammad, M. Alsulaiman, S. Amin, G. Altuwaijri, Wadood Abdul, et al.</sub></td>
<td width="13%">2021<br>Neural computing &amp; applications (Print)<br>551 citations</td>
<td width="30%">Positions Deep learning techniques for classification of electroencephalogram (EEG) motor imagery (MI) signals: a review within Motor Imagery and Movement Decoding.</td>
<td width="15%">high citation signal (551); influential citation signal (21)</td>
<td width="15%">abstract unavailable in metadata; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/aba162">BCI for stroke rehabilitation: motor and beyond</a><br><sub>R. Mane, Tushar Chouhan, Cuntai Guan</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>386 citations</td>
<td width="30%">Stroke is one of the leading causes of long-term disability among adults and contributes to major socio-economic burden globally.</td>
<td width="15%">high citation signal (386); influential citation signal (16); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1016/j.neunet.2020.12.013">Adaptive transfer learning for EEG motor imagery classification with deep Convolutional Neural Network</a><br><sub>Kaishuo Zhang, Neethu Robinson, Seong-Whan Lee, Cuntai Guan</sub></td>
<td width="13%">2020<br>Neural Networks<br>266 citations</td>
<td width="30%">In recent years, deep learning has emerged as a powerful tool for developing Brain-Computer Interface (BCI) systems.</td>
<td width="15%">high citation signal (266); influential citation signal (19); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bspc.2020.102172">Deep learning for motor imagery EEG-based classification: A review</a><br><sub>A. Al-Saegh, Shefa A. Dawwd, J. Abdul-Jabbar</sub></td>
<td width="13%">2021<br>Biomedical Signal Processing and Control<br>408 citations</td>
<td width="30%">Abstract Objectives The availability of large and varied Electroencephalogram (EEG) datasets, rapidly advances and inventions in deep learning techniques, and highly powerful and diversified computing systems have all permitted to easily analyzing those datasets and discovering vital information within.</td>
<td width="15%">high citation signal (408); influential citation signal (18)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://arxiv.org/abs/2104.01233">FBCNet: A Multi-view Convolutional Neural Network for Brain-Computer Interface</a><br><sub>R. Mane, E. Chew, K. Chua, K. Ang, Neethu Robinson, A. P. Vinod, et al.</sub></td>
<td width="13%">2021<br>arXiv.org<br>229 citations</td>
<td width="30%">Lack of adequate training samples and noisy high-dimensional features are key challenges faced by Motor Imagery (MI) decoding algorithms for electroencephalogram (EEG) based Brain-Computer Interface (BCI).</td>
<td width="15%">high citation signal (229); influential citation signal (35)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.1038/s41551-020-0542-9">Stabilization of a brain-computer interface via the alignment of low-dimensional spaces of neural activity</a><br><sub>A. D. Degenhart, William E. Bishop, E. Oby, E. Tyler-Kabara, S. Chase, A. Batista, et al.</sub></td>
<td width="13%">2020<br>Nature Biomedical Engineering<br>214 citations</td>
<td width="30%">The instability of neural recordings can render clinical brain–computer interfaces (BCIs) uncontrollable.</td>
<td width="15%">high citation signal (214); influential citation signal (19); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2021.3137184">MIN2Net: End-to-End Multi-Task Learning for Subject-Independent Motor Imagery EEG Classification</a><br><sub>Phairot Autthasan, Rattanaphon Chaisaen, Thapanun Sudhawiyangkul, Phurin Rangpong, Suktipol Kiatthaveephong, Nat Dilokthanakul, et al.</sub></td>
<td width="13%">2021<br>IEEE Transactions on Biomedical Engineering<br>166 citations</td>
<td width="30%">Objective: Advances in the motor imagery (MI)-based brain-computer interfaces (BCIs) allow control of several applications by decoding neurophysiological phenomena, which are usually recorded by electroencephalography (EEG) using a non-invasive technique.</td>
<td width="15%">high citation signal (166); influential citation signal (19); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1109/JBHI.2020.2967128">Motor Imagery Classification via Temporal Attention Cues of Graph Embedded EEG Signals</a><br><sub>Dalin Zhang, Kaixuan Chen, Debao Jian, Lina Yao</sub></td>
<td width="13%">2020<br>IEEE journal of biomedical and health informatics<br>172 citations</td>
<td width="30%">Motor imagery classification from EEG signals is essential for motor rehabilitation with a Brain-Computer Interface (BCI).</td>
<td width="15%">high citation signal (172); influential citation signal (23)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.1016/J.BSPC.2021.102826">Electroencephalography-based motor imagery classification using temporal convolutional network fusion</a><br><sub>Yazeed K. Musallam, Nasser I. AlFassam, Muhammad Ghulam, S. Amin, M. Alsulaiman, Wadood Abdul, et al.</sub></td>
<td width="13%">2021<br>Biomedical Signal Processing and Control<br>212 citations</td>
<td width="30%">Abstract Motor imagery electroencephalography (MI-EEG) signals are generated when a person imagines a task without actually performing it.</td>
<td width="15%">high citation signal (212); influential citation signal (15)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.3390/brainsci11111525">Neural Decoding of EEG Signals with Machine Learning: A Systematic Review</a><br><sub>Maham Saeidi, W. Karwowski, F. Farahani, K. Fiok, R. Taiar, P. Hancock, et al.</sub></td>
<td width="13%">2021<br>Brain Science<br>244 citations</td>
<td width="30%">Electroencephalography (EEG) is a non-invasive technique used to record the brain’s evoked and induced electrical activity from the scalp.</td>
<td width="15%">high citation signal (244); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/abed81">EEG-inception: an accurate and robust end-to-end neural network for EEG-based motor imagery classification</a><br><sub>Ce Zhang, Young-Keun Kim, A. Eskandarian</sub></td>
<td width="13%">2021<br>Journal of Neural Engineering<br>194 citations</td>
<td width="30%">Objective.</td>
<td width="15%">high citation signal (194); influential citation signal (11); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="22%"><a href="https://doi.org/10.1038/s41598-024-71118-7">CTNet: a convolutional transformer network for EEG-based motor imagery classification</a><br><sub>Wei Zhao, Xiaolu Jiang, Baocan Zhang, Shixiao Xiao, Sujun Weng</sub></td>
<td width="13%">2024<br>Scientific Reports<br>154 citations</td>
<td width="30%">Brain-computer interface (BCI) technology bridges the direct communication between the brain and machines, unlocking new possibilities for human interaction and rehabilitation.</td>
<td width="15%">high citation signal (154); influential citation signal (17); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="22%"><a href="https://doi.org/10.3389/fncom.2019.00087">Intra- and Inter-subject Variability in EEG-Based Sensorimotor Brain Computer Interface: A Review</a><br><sub>S. Saha, M. Baumert</sub></td>
<td width="13%">2020<br>Frontiers in Computational Neuroscience<br>275 citations</td>
<td width="30%">Brain computer interfaces (BCI) for the rehabilitation of motor impairments exploit sensorimotor rhythms (SMR) in the electroencephalogram (EEG).</td>
<td width="15%">high citation signal (275); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2021.3099908">A Temporal-Spectral-Based Squeeze-and- Excitation Feature Fusion Network for Motor Imagery EEG Decoding</a><br><sub>Yang Li, Lianghui Guo, Yu Liu, Jingyu Liu, F. Meng</sub></td>
<td width="13%">2021<br>IEEE transactions on neural systems and rehabilitation engineering<br>142 citations</td>
<td width="30%">Motor imagery (MI) electroencephalography (EEG) decoding plays an important role in brain-computer interface (BCI), which enables motor-disabled patients to communicate with the outside world via external devices.</td>
<td width="15%">high citation signal (142); influential citation signal (12); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2020.2984003">Brain-Computer Interface-Based Soft Robotic Glove Rehabilitation for Stroke</a><br><sub>Nicholas Cheng, K. Phua, H. Lai, P. K. Tam, K. Tang, K. Cheng, et al.</sub></td>
<td width="13%">2020<br>IEEE Transactions on Biomedical Engineering<br>131 citations</td>
<td width="30%">Objective: This randomized controlled feasibility study investigates the ability for clinical application of the Brain-Computer Interface-based Soft Robotic Glove (BCI-SRG) incorporating activities of daily living (ADL)-oriented tasks for stroke rehabilitation.</td>
<td width="15%">high citation signal (131); influential citation signal (16); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="22%"><a href="https://doi.org/10.1016/j.compbiomed.2020.103843">Review on motor imagery based BCI systems for upper limb post-stroke neurorehabilitation: From designing to application</a><br><sub>M. A. Khan, Rig Das, H. Iversen, S. Puthusserypady</sub></td>
<td width="13%">2020<br>Comput. Biol. Medicine<br>231 citations</td>
<td width="30%">Strokes are a growing cause of mortality and many stroke survivors suffer from motor impairment as well as other types of disabilities in their daily life activities.</td>
<td width="15%">high citation signal (231); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2022.3193277">FBMSNet: A Filter-Bank Multi-Scale Convolutional Neural Network for EEG-Based Motor Imagery Decoding</a><br><sub>Ke Liu, Mingzhao Yang, Zhuliang Yu, Guoyin Wang, Wei Wu</sub></td>
<td width="13%">2022<br>IEEE Transactions on Biomedical Engineering<br>107 citations</td>
<td width="30%">Object: Motor imagery (MI) is a mental process widely utilized as the experimental paradigm for brain-computer interfaces (BCIs) across a broad range of basic science and clinical studies.</td>
<td width="15%">high citation signal (107); influential citation signal (14); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="22%"><a href="https://doi.org/10.1109/TIM.2021.3051996">A Sliding Window Common Spatial Pattern for Enhancing Motor Imagery Classification in EEG-BCI</a><br><sub>Pramod Gaur, Harsh Gupta, Anirban Chowdhury, K. McCreadie, R. B. Pachori, Hui Wang</sub></td>
<td width="13%">2021<br>IEEE Transactions on Instrumentation and Measurement<br>219 citations</td>
<td width="30%">Accurate binary classification of electroencephalography (EEG) signals is a challenging task for the development of motor imagery (MI) brain–computer interface (BCI) systems.</td>
<td width="15%">high citation signal (219); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="22%"><a href="https://doi.org/10.1109/TNNLS.2022.3202569">GCNs-Net: A Graph Convolutional Neural Network Approach for Decoding Time-Resolved EEG Motor Imagery Signals</a><br><sub>Xiangmin Lun, Shuyue Jia, Yimin Hou, Yan Shi, Y. Li, Hanrui Yang, et al.</sub></td>
<td width="13%">2020<br>IEEE Transactions on Neural Networks and Learning Systems<br>169 citations</td>
<td width="30%">Toward the development of effective and efficient brain–computer interface (BCI) systems, precise decoding of brain activity measured by an electroencephalogram (EEG) is highly demanded.</td>
<td width="15%">high citation signal (169); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2020.3048106">EEG-Inception: A Novel Deep Convolutional Neural Network for Assistive ERP-Based Brain-Computer Interfaces</a><br><sub>E. Santamaría-Vázquez, V. Martínez-Cagigal, F. Vaquerizo-Villar, R. Hornero</sub></td>
<td width="13%">2020<br>IEEE transactions on neural systems and rehabilitation engineering<br>183 citations</td>
<td width="30%">In recent years, deep-learning models gained attention for electroencephalography (EEG) classification tasks due to their excellent performance and ability to extract complex features from raw data.</td>
<td width="15%">high citation signal (183); influential citation signal (12); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="22%"><a href="https://doi.org/10.1016/j.neuroimage.2023.120209">LMDA-Net:A lightweight multi-dimensional attention network for general EEG-based brain-computer interfaces and interpretability</a><br><sub>Zhengqing Miao, Mei-rong Zhao, Xin Zhang, Dong Ming</sub></td>
<td width="13%">2023<br>NeuroImage<br>150 citations</td>
<td width="30%">Electroencephalography (EEG)-based brain-computer interfaces (BCIs) pose a challenge for decoding due to their low spatial resolution and signal-to-noise ratio.</td>
<td width="15%">high citation signal (150); influential citation signal (12); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ab4af6">A novel approach of decoding EEG four-class motor imagery tasks via scout ESI and CNN</a><br><sub>Yimin Hou, Lu Zhou, Shuyue Jia, Xiangmin Lun</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>137 citations</td>
<td width="30%">Objective.</td>
<td width="15%">high citation signal (137); influential citation signal (14); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2022.3185262">SSVEP-Based Brain Computer Interface Controlled Soft Robotic Glove for Post-Stroke Hand Function Rehabilitation</a><br><sub>Ning Guo, Xiaojun Wang, Dehao Duanmu, Xin Huang, Xiaodong Li, Yunli Fan, et al.</sub></td>
<td width="13%">2022<br>IEEE transactions on neural systems and rehabilitation engineering<br>86 citations</td>
<td width="30%">Soft robotic glove with brain computer interfaces (BCI) control has been used for post-stroke hand function rehabilitation.</td>
<td width="15%">influential citation signal (10); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="22%"><a href="https://doi.org/10.1109/tii.2021.3132340">Attention-Inception and Long- Short-Term Memory-Based Electroencephalography Classification for Motor Imagery Tasks in Rehabilitation</a><br><sub>S. Amin, Hamdi Altaheri, G. Muhammad, Mansour Alsulaiman, A. Wadood</sub></td>
<td width="13%">2022<br>IEEE Transactions on Industrial Informatics<br>118 citations</td>
<td width="30%">In recent years, the contributions of deep learning have had a phenomenal impact on electroencephalography-based brain-computer interfaces.</td>
<td width="15%">high citation signal (118); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2021.3059166">Dynamic Joint Domain Adaptation Network for Motor Imagery Classification</a><br><sub>Xiaolin Hong, Qingqing Zheng, Luyan Liu, Peiyin Chen, Kai Ma, Zhongke Gao, et al.</sub></td>
<td width="13%">2021<br>IEEE transactions on neural systems and rehabilitation engineering<br>115 citations</td>
<td width="30%">Electroencephalogram (EEG) has been widely used in brain computer interface (BCI) due to its convenience and reliability.</td>
<td width="15%">high citation signal (115); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2020.3020975">Bispectrum-Based Channel Selection for Motor Imagery Based Brain-Computer Interfacing</a><br><sub>Jing Jin, Chang Liu, I. Daly, Yangyang Miao, Shurui Li, Xingyu Wang, et al.</sub></td>
<td width="13%">2020<br>IEEE transactions on neural systems and rehabilitation engineering<br>122 citations</td>
<td width="30%">The performance of motor imagery (MI) based Brain-computer interfacing (BCI) is easily affected by noise and redundant information that exists in the multi-channel electroencephalogram (EEG).</td>
<td width="15%">high citation signal (122); influential citation signal (10); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="22%"><a href="https://doi.org/10.1109/ACCESS.2022.3161489">EEG-ITNet: An Explainable Inception Temporal Convolutional Network for motor imagery classification</a><br><sub>Abbas Salami, Javier Andreu-Perez, H. Gillmeister</sub></td>
<td width="13%">2022<br>IEEE Access<br>117 citations</td>
<td width="30%">In recent years, neural networks and especially deep architectures have received substantial attention for EEG signal analysis in the field of brain-computer interfaces (BCIs).</td>
<td width="15%">high citation signal (117); influential citation signal (13); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td colspan="6">See the website and taxonomy CSV for all 476 papers.</td>
</tr>
</tbody>
</table>

</details>

### SSVEP, P300, and ERP Spellers

- Papers selected: **99**
- Years covered: **2020-2026**
- Citation count in selected set: **4,533**
- Main research trends:
  - Research is concentrating on high-speed, many-target communication systems with lower calibration burden and more stable target recognition.
  - Training-free and adaptive spatial filtering, task-discriminant component analysis, and deep neural decoders are prominent directions for SSVEP/P300 reliability.
  - Hybrid paradigms that combine SSVEP, P300, RSVP, EOG, or augmented/virtual reality interfaces are becoming a practical route to richer command sets.

<details>
<summary>Show representative papers for SSVEP, P300, and ERP Spellers</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2021.3114340">Improving the Performance of Individually Calibrated SSVEP-BCI by Task- Discriminant Component Analysis</a><br><sub>Bingchuan Liu, Xiaogang Chen, Nanlin Shi, Yijun Wang, Shangkai Gao, Xiaorong Gao</sub></td>
<td width="13%">2021<br>IEEE transactions on neural systems and rehabilitation engineering<br>177 citations</td>
<td width="30%">A brain-computer interface (BCI) provides a direct communication channel between a brain and an external device.</td>
<td width="15%">high citation signal (177); influential citation signal (21); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ab6a67">Comparing user-dependent and user-independent training of CNN for SSVEP BCI</a><br><sub>Aravind Ravi, Nargess Heydari Beni, J. Manuel, N. Jiang</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>143 citations</td>
<td width="30%">Objective.</td>
<td width="15%">high citation signal (143); influential citation signal (24); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2021.3110440">A Deep Neural Network for SSVEP-Based Brain-Computer Interfaces</a><br><sub>O. B. Guney, Muhtasham Oblokulov, Huseyin Ozkan</sub></td>
<td width="13%">2020<br>IEEE Transactions on Biomedical Engineering<br>102 citations</td>
<td width="30%">Objective: Target identification in brain-computer interface (BCI) spellers refers to the electroencephalogram (EEG) classification for predicting the target character that the subject intends to spell.</td>
<td width="15%">high citation signal (102); influential citation signal (20); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.48550/arXiv.2210.04172">A Transformer-based deep neural network model for SSVEP classification</a><br><sub>Jianbo Chen, Yangsong Zhang, Yudong Pan, Peng Xu, Cuntai Guan</sub></td>
<td width="13%">2022<br>Neural Networks<br>108 citations</td>
<td width="30%">Steady-state visual evoked potential (SSVEP) is one of the most commonly used control signals in the brain-computer interface (BCI) systems.</td>
<td width="15%">high citation signal (108); influential citation signal (14); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ab2373">Learning across multi-stimulus enhances target recognition methods in SSVEP-based BCIs</a><br><sub>C. Wong, Feng Wan, Boyu Wang, Z. Wang, Wenya Nan, K. Lao, et al.</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>123 citations</td>
<td width="30%">Objective.</td>
<td width="15%">high citation signal (123); influential citation signal (14); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.3390/s20185083">EEG-Based BCI Emotion Recognition: A Survey</a><br><sub>E. Torres P., E. Torres, Myriam Hernández-Álvarez, S. Yoo</sub></td>
<td width="13%">2020<br>Italian National Conference on Sensors<br>249 citations</td>
<td width="30%">Affecting computing is an artificial intelligence area of study that recognizes, interprets, processes, and simulates human affects.</td>
<td width="15%">high citation signal (249); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2020.3038718">Convolutional Correlation Analysis for Enhancing the Performance of SSVEP-Based Brain-Computer Interface</a><br><sub>Yao Li, Jiayi Xiang, T. Kesavadas</sub></td>
<td width="13%">2020<br>IEEE transactions on neural systems and rehabilitation engineering<br>76 citations</td>
<td width="30%">Currently, most of the high-performance models for frequency recognition of steady-state visual evoked potentials (SSVEPs) are linear.</td>
<td width="15%">influential citation signal (13); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2020.2975614">Implementing Over 100 Command Codes for a High-Speed Hybrid Brain-Computer Interface Using Concurrent P300 and SSVEP Features</a><br><sub>Minpeng Xu, Jin Han, Yijun Wang, T. Jung, Dong Ming</sub></td>
<td width="13%">2020<br>IEEE Transactions on Biomedical Engineering<br>139 citations</td>
<td width="30%">Objective: Recently, electroencephalography (EEG)- based brain-computer interfaces (BCIs) have made tremendous progress in increasing communication speed.</td>
<td width="15%">high citation signal (139); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.3390/s22093331">Past, Present, and Future of EEG-Based BCI Applications</a><br><sub>Kaido Värbu, M. Naveed, Yar Muhammad</sub></td>
<td width="13%">2022<br>Italian National Conference on Sensors<br>286 citations</td>
<td width="30%">An electroencephalography (EEG)-based brain–computer interface (BCI) is a system that provides a pathway between the brain and external devices by interpreting EEG.</td>
<td width="15%">high citation signal (286); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ac0bfa">Implementing a calibration-free SSVEP-based BCI system with 160 targets</a><br><sub>Yonghao Chen, Chen Yang, X. Ye, Xiaogang Chen, Yijun Wang, Xiaorong Gao</sub></td>
<td width="13%">2021<br>Journal of Neural Engineering<br>101 citations</td>
<td width="30%">Objective.</td>
<td width="15%">high citation signal (101); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2023.3237319">ST-CapsNet: Linking Spatial and Temporal Attention With Capsule Network for P300 Detection Improvement</a><br><sub>Zehui Wang, Chuangquan Chen, Junhua Li, Feng Wan, Yu Sun, Hongtao Wang</sub></td>
<td width="13%">2023<br>IEEE transactions on neural systems and rehabilitation engineering<br>64 citations</td>
<td width="30%">A brain-computer interface (BCI), which provides an advanced direct human-machine interaction, has gained substantial research interest in the last decade for its great potential in various applications including rehabilitation and communication.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2020.2975552">Spatial Filtering in SSVEP-Based BCIs: Unified Framework and New Improvements</a><br><sub>C. Wong, Boyu Wang, Z. Wang, K. Lao, Agostinho C. Rosa, Feng Wan</sub></td>
<td width="13%">2020<br>IEEE Transactions on Biomedical Engineering<br>108 citations</td>
<td width="30%">Objective: In the steady-state visual evoked potential (SSVEP)-based brain computer interfaces (BCIs), spatial filtering, which combines the multi-channel electroencephalography (EEG) signals in order to reduce the non-SSVEP-related component and thus enhance the signal-to-noise ratio (SNR), plays an important role in target recognition.</td>
<td width="15%">high citation signal (108); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ab914e">A novel training-free recognition method for SSVEP-based BCIs using dynamic window strategy</a><br><sub>Yonghao Chen, Chen Yang, Xiaogang Chen, Yijun Wang, Xiaorong Gao</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>81 citations</td>
<td width="30%">Objective.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2020.3019276">Inter- and Intra-Subject Transfer Reduces Calibration Effort for High-Speed SSVEP-Based BCIs</a><br><sub>C. Wong, Z. Wang, Boyu Wang, K. Lao, Agostinho C. Rosa, Peng Xu, et al.</sub></td>
<td width="13%">2020<br>IEEE transactions on neural systems and rehabilitation engineering<br>63 citations</td>
<td width="30%">Objective: Steady-state visual evoked potential (SSVEP)-based brain-computer interfaces (BCIs) that can deliver a high information transfer rate (ITR) usually require subject’s calibration data to learn the class- and subject-specific model parameters (e.g.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ab4dc6">An online SSVEP-BCI system in an optical see-through augmented reality environment</a><br><sub>Yufeng Ke, Pengxiao Liu, X. An, Xizi Song, Dong Ming</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>78 citations</td>
<td width="30%">Objective.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="22%"><a href="https://doi.org/10.3389/fnins.2020.568104">BCIAUT-P300: A Multi-Session and Multi-Subject Benchmark Dataset on Autism for P300-Based Brain-Computer-Interfaces</a><br><sub>M. Simões, D. Borra, Eduardo Santamaría-Vázquez, M. Bittencourt-Villalpando, D. Krzemiński, A. Miladinović, et al.</sub></td>
<td width="13%">2020<br>Frontiers in Neuroscience<br>63 citations</td>
<td width="30%">There is a lack of multi-session P300 datasets for Brain-Computer Interfaces (BCI).</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ac8dc5">An efficient CNN-LSTM network with spectral normalization and label smoothing technologies for SSVEP frequency recognition</a><br><sub>Yudong Pan, Jianbo Chen, Yangsong Zhang, Yu Zhang</sub></td>
<td width="13%">2022<br>Journal of Neural Engineering<br>73 citations</td>
<td width="30%">Objective.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2021.3133594">Online Adaptation Boosts SSVEP-Based BCI Performance</a><br><sub>C. Wong, Z. Wang, M. Nakanishi, Boyu Wang, Agostinho C. Rosa, C. L. P. Chen, et al.</sub></td>
<td width="13%">2021<br>IEEE Transactions on Biomedical Engineering<br>43 citations</td>
<td width="30%">Objective: A user-friendly steady-state visual evoked potential (SSVEP)-based brain-computer interface (BCI) prefers no calibration for its target recognition algorithm, however, the existing calibration-free schemes perform still far behind their calibration-based counterparts.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="22%"><a href="https://doi.org/10.1101/2021.04.19.440473">“Thinking out loud”: an open-access EEG-based BCI dataset for inner speech recognition</a><br><sub>Nicolás Nieto, V. Peterson, H. Rufiner, Juan Kamienkoski, Rubén D. Spies</sub></td>
<td width="13%">2021<br>bioRxiv<br>66 citations</td>
<td width="30%">Surface electroencephalography is a standard and noninvasive way to measure electrical brain activity.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="22%"><a href="https://doi.org/10.1038/s41597-022-01509-w">EEG Dataset for RSVP and P300 Speller Brain-Computer Interfaces</a><br><sub>K. Won, Moonyoung Kwon, M. Ahn, S. Jun</sub></td>
<td width="13%">2022<br>Scientific Data<br>59 citations</td>
<td width="30%">As attention to deep learning techniques has grown, many researchers have attempted to develop ready-to-go brain-computer interfaces (BCIs) that include automatic processing pipelines.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2020.2972747">A Hybrid Asynchronous Brain-Computer Interface Combining SSVEP and EOG Signals</a><br><sub>Yajun Zhou, Shenghong He, Qiyun Huang, Yuanqing Li</sub></td>
<td width="13%">2020<br>IEEE Transactions on Biomedical Engineering<br>61 citations</td>
<td width="30%">Objective: A challenging task for an electroencephalography (EEG)-based asynchronous brain-computer interface (BCI) is to effectively distinguish between the idle state and the control state while maintaining a short response time and a high accuracy when commands are issued in the control state.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="22%"><a href="https://doi.org/10.1109/TMRB.2019.2959559">MsCNN: A Deep Learning Framework for P300-Based Brain–Computer Interface Speller</a><br><sub>S. Kundu, S. Ari</sub></td>
<td width="13%">2020<br>IEEE Transactions on Medical Robotics and Bionics<br>65 citations</td>
<td width="30%">In this paper, a novel multiscale convolutional neural network (MsCNN) architecture is proposed for P300 based BCI speller.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="22%"><a href="https://doi.org/10.1109/TBME.2021.3105331">Align and Pool for EEG Headset Domain Adaptation (ALPHA) to Facilitate Dry Electrode Based SSVEP-BCI</a><br><sub>Bingchuan Liu, Xiaogang Chen, Xiang Li, Yijun Wang, Xiaorong Gao, Shangkai Gao</sub></td>
<td width="13%">2021<br>IEEE Transactions on Biomedical Engineering<br>54 citations</td>
<td width="30%">Objective: The steady-state visual evoked potential based brain-computer interface (SSVEP-BCI) implemented in dry electrodes is a promising paradigm for alternative and augmentative communication in real-world applications.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="22%"><a href="https://doi.org/10.1109/TNNLS.2021.3135696">An MVMD-CCA Recognition Algorithm in SSVEP-Based BCI and Its Application in Robot Control</a><br><sub>Kang Wang, Dihua Zhai, Y. Xiong, Leyun Hu, Yuanqing Xia</sub></td>
<td width="13%">2021<br>IEEE Transactions on Neural Networks and Learning Systems<br>47 citations</td>
<td width="30%">This article proposes a novel recognition algorithm for the steady-state visual evoked potentials (SSVEP)-based brain–computer interface (BCI) system.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="22%"><a href="https://doi.org/10.1109/TASE.2021.3054741">Transferring Subject-Specific Knowledge Across Stimulus Frequencies in SSVEP-Based BCIs</a><br><sub>C. Wong, Z. Wang, Agostinho C. Rosa, C. L. P. Chen, T. Jung, Yong Hu, et al.</sub></td>
<td width="13%">2021<br>IEEE Transactions on Automation Science and Engineering<br>51 citations</td>
<td width="30%">Learning from subject’s calibration data can significantly improve the performance of a steady-state visually evoked potential (SSVEP)-based brain–computer interface (BCI), for example, the state-of-the-art target recognition methods utilize the learned subject-specific and stimulus-specific model parameters.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="22%"><a href="https://doi.org/10.1016/j.cmpb.2020.105326">A novel hybrid BCI speller based on RSVP and SSVEP paradigm</a><br><sub>Shayan Jalilpour, Sepideh Hajipour Sardouie, A. Mijani</sub></td>
<td width="13%">2020<br>Comput. Methods Programs Biomed.<br>52 citations</td>
<td width="30%">BACKGROUND AND OBJECTIVE Steady-state visual evoked potential (SSVEP) and rapid serial visual presentation (RSVP) are useful methods in the brain-computer interface (BCI) systems.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2022.3208717">A Spectrally-Dense Encoding Method for Designing a High-Speed SSVEP-BCI With 120 Stimuli</a><br><sub>Xiaogang Chen, Bingchuan Liu, Yijun Wang, Xiaorong Gao</sub></td>
<td width="13%">2022<br>IEEE transactions on neural systems and rehabilitation engineering<br>43 citations</td>
<td width="30%">The practical functionality of a brain-computer interface (BCI) is critically affected by the number of stimuli, especially for steady-state visual evoked potential based BCI (SSVEP-BCI), which shows promise for the implementation of a multi-target system for real-world applications.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2021.3070327">Capsule Network for ERP Detection in Brain-Computer Interface</a><br><sub>Ronghua Ma, Tianyou Yu, Xiaoli Zhong, Z. Yu, Yuanqing Li, Z. Gu</sub></td>
<td width="13%">2021<br>IEEE transactions on neural systems and rehabilitation engineering<br>41 citations</td>
<td width="30%">Event-related potential (ERP) is bioelectrical activity that occurs in the brain in response to specific events or stimuli, reflecting the electrophysiological changes in the brain during cognitive processes.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="22%"><a href="https://doi.org/10.1007/s12021-020-09473-9">Review of Riemannian Distances and Divergences, Applied to SSVEP-based BCI</a><br><sub>S. Chevallier, Emmanuel K. Kalunga, Quentin Barthélemy, É. Monacelli</sub></td>
<td width="13%">2020<br>Neuroinformatics<br>60 citations</td>
<td width="30%">Positions Review of Riemannian Distances and Divergences, Applied to SSVEP-based BCI within SSVEP, P300, and ERP Spellers.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/acacca">Transfer learning of an ensemble of DNNs for SSVEP BCI spellers without user-specific training</a><br><sub>Osman Berke Guney, Huseyin Ozkan</sub></td>
<td width="13%">2022<br>Journal of Neural Engineering<br>32 citations</td>
<td width="30%">Objective.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td colspan="6">See the website and taxonomy CSV for all 99 papers.</td>
</tr>
</tbody>
</table>

</details>

### Invasive and Implantable Interfaces

- Papers selected: **39**
- Years covered: **2020-2026**
- Citation count in selected set: **1,218**
- Main research trends:
  - Invasive BCI research is shifting toward high-bandwidth, stable, long-term decoding for movement, communication, and sensory feedback.
  - Key engineering themes include wireless operation, power efficiency, signal longevity, surgical risk, and reliability outside tightly controlled laboratory sessions.
  - Clinical translation is increasingly tied to home use, user safety, tactile feedback, speech decoding, and realistic functional tasks.

<details>
<summary>Show representative papers for Invasive and Implantable Interfaces</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1038/s41551-020-0595-9">Power-saving design opportunities for wireless intracortical brain computer interfaces</a><br><sub>N. Even-Chen, D. Muratore, S. Stavisky, L. Hochberg, J. Henderson, B. Murmann, et al.</sub></td>
<td width="13%">2020<br>Nature Biomedical Engineering<br>101 citations</td>
<td width="30%">The efficacy of wireless intracortical brain–computer interfaces (iBCIs) is limited in part by the number of recording channels, which is constrained by the power budget of the implantable system.</td>
<td width="15%">high citation signal (101); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1109/RBME.2024.3449790">Non-Invasive Brain-Computer Interfaces: State of the Art and Trends</a><br><sub>B. Edelman, Shuailei Zhang, Gerwin Schalk, P. Brunner, Gernot Müller-Putz, Cuntai Guan, et al.</sub></td>
<td width="13%">2024<br>IEEE Reviews in Biomedical Engineering<br>129 citations</td>
<td width="30%">Brain-computer interface (BCI) is a rapidly evolving technology that has the potential to widely influence research, clinical and recreational use.</td>
<td width="15%">high citation signal (129); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2021.705064">Toward EEG-Based BCI Applications for Industry 4.0: Challenges and Possible Applications</a><br><sub>Khalida Douibi, S. Le Bars, A. Lemontey, Lipsa Nag, Rodrigo Balp, Gabrièle Breda</sub></td>
<td width="13%">2021<br>Frontiers in Human Neuroscience<br>76 citations</td>
<td width="30%">In the last few decades, Brain-Computer Interface (BCI) research has focused predominantly on clinical applications, notably to enable severely disabled people to interact with the environment.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.3389/fnins.2020.00123">The Potential of Stereotactic-EEG for Brain-Computer Interfaces: Current Progress and Future Directions</a><br><sub>Christian Herff, D. Krusienski, P. Kubben</sub></td>
<td width="13%">2020<br>Frontiers in Neuroscience<br>105 citations</td>
<td width="30%">Stereotactic electroencephalogaphy (sEEG) utilizes localized, penetrating depth electrodes to measure electrophysiological brain activity.</td>
<td width="15%">high citation signal (105); recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1007/s10462-023-10690-2">Role of machine learning and deep learning techniques in EEG-based BCI emotion recognition system: a review</a><br><sub>Priyadarsini Samal, M. Hashmi</sub></td>
<td width="13%">2024<br>Artificial Intelligence Review<br>107 citations</td>
<td width="30%">Emotion is a subjective psychophysiological reaction coming from external stimuli which impacts every aspect of our daily lives.</td>
<td width="15%">high citation signal (107); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1016/j.brs.2021.08.016">The sensitivity of ECG contamination to surgical implantation site in brain computer interfaces</a><br><sub>W. Neumann, Majid Memarian Sorkhabi, M. Benjaber, L. Feldmann, A. Saryyeva, J. Krauss, et al.</sub></td>
<td width="13%">2021<br>Brain Stimulation<br>73 citations</td>
<td width="30%">Background Brain sensing devices are approved today for Parkinson&#x27;s, essential tremor, and epilepsy therapies.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.3389/fnins.2021.599549">Defining Surgical Terminology and Risk for Brain Computer Interface Technologies</a><br><sub>E. Leuthardt, D. Moran, T. Mullen</sub></td>
<td width="13%">2021<br>Frontiers in Neuroscience<br>49 citations</td>
<td width="30%">With the emergence of numerous brain computer interfaces (BCI), their form factors, and clinical applications the terminology to describe their clinical deployment and the associated risk has been vague.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.1101/2023.06.30.23291352">Online speech synthesis using a chronically implanted brain-computer interface in an individual with ALS</a><br><sub>Miguel Angrick, S. Luo, Q. Rabbani, D. Candrea, Samyak Shah, G. Milsap, et al.</sub></td>
<td width="13%">2023<br>medRxiv<br>40 citations</td>
<td width="30%">Recent studies have shown that speech can be reconstructed and synthesized using only brain activity recorded with intracranial electrodes, but until now this has only been done using retrospective analyses of recordings from able-bodied patients temporarily implanted with electrodes for epilepsy surgery.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.34133/hds.0096">Recent Progress in Wearable Brain–Computer Interface (BCI) Devices Based on Electroencephalogram (EEG) for Medical Applications: A Review</a><br><sub>Jiayan Zhang, Junshi Li, Zhe Huang, Dong Huang, Huaiqiang Yu, Zhihong Li</sub></td>
<td width="13%">2023<br>Health Data Science<br>49 citations</td>
<td width="30%">Importance: Brain–computer interface (BCI) decodes and converts brain signals into machine instructions to interoperate with the external world.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1007/s11042-024-18259-z">Emotion recognition with EEG-based brain-computer interfaces: a systematic literature review</a><br><sub>Kübra Erat, Elif Bilge Şahin, Furkan Doğan, Nur Merdanoğlu, Ahmet Akcakaya, P. O. Durdu</sub></td>
<td width="13%">2024<br>Multimedia tools and applications<br>54 citations</td>
<td width="30%">Electroencephalography (EEG)-based Brain-Computer Interface (BCI) systems for emotion recognition have the potential to assist the enrichment of human–computer interaction with implicit information since they can enable understanding of the cognitive and emotional activities of humans.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/ac127e">Neuropathological effects of chronically implanted, intracortical microelectrodes in a tetraplegic patient</a><br><sub>Linda J Szymanski, S. Kellis, C. Liu, Kymry T. Jones, R. Andersen, D. Commins, et al.</sub></td>
<td width="13%">2021<br>Journal of Neural Engineering<br>41 citations</td>
<td width="30%">Objective.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2022.806517">Error-Related Potentials in Reinforcement Learning-Based Brain-Machine Interfaces</a><br><sub>Aline Xavier Fidêncio, Christian Klaes, Ioannis Iossifidis</sub></td>
<td width="13%">2022<br>Frontiers in Human Neuroscience<br>33 citations</td>
<td width="30%">The human brain has been an object of extensive investigation in different fields.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.48550/arXiv.2209.03785">A Novel Semi-supervised Meta Learning Method for Subject-transfer Brain-computer Interface</a><br><sub>Jingcong Li, Fei Wang, Haiyun Huang, Feifei Qi, Jiahui Pan</sub></td>
<td width="13%">2022<br>Neural Networks<br>42 citations</td>
<td width="30%">The brain-computer interface (BCI) provides a direct communication pathway between the human brain and external devices.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.1371/journal.pone.0275454">Public attitudes towards neurotechnology: Findings from two experiments concerning Brain Stimulation Devices (BSDs) and Brain-Computer Interfaces (BCIs)</a><br><sub>S. Sattler, Dana Pietralla</sub></td>
<td width="13%">2022<br>PLoS ONE<br>29 citations</td>
<td width="30%">This study contributes to the emerging literature on public perceptions of neurotechnological devices (NTDs) in their medical and non-medical applications, depending on their invasiveness, framing effects, and interindividual differences related to personal needs and values.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="22%"><a href="https://doi.org/10.1109/TBCAS.2023.3278531">Calibration-Free and Hardware-Efficient Neural Spike Detection for Brain Machine Interfaces</a><br><sub>Zheng Zhang, Peilong Feng, A. Oprea, T. Constandinou</sub></td>
<td width="13%">2023<br>IEEE Transactions on Biomedical Circuits and Systems<br>13 citations</td>
<td width="30%">Recent translational efforts in brain-machine interfaces (BMI) are demonstrating the potential to help people with neurological disorders.</td>
<td width="15%">recognized venue</td>
<td width="15%">limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="22%"><a href="https://doi.org/10.1021/acsnano.3c06781">Advanced Electrode Technologies for Noninvasive Brain-Computer Interfaces.</a><br><sub>Sen Lin, Jingjing Jiang, Kai Huang, Lei Li, Xian He, Peng Du, et al.</sub></td>
<td width="13%">2023<br>ACS Nano<br>41 citations</td>
<td width="30%">Brain-computer interfaces (BCIs) have garnered significant attention in recent years due to their potential applications in medical, assistive, and communication technologies.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="22%"><a href="https://doi.org/10.1038/s41467-024-53858-2">Constructing organoid-brain-computer interfaces for neurofunctional repair after brain injury</a><br><sub>Nan Hu, Jian Shi, Chonga Chen, Hai-Huan Xu, Zhennan Chang, Pengchong Hu, et al.</sub></td>
<td width="13%">2024<br>Nature Communications<br>32 citations</td>
<td width="30%">The reconstruction of damaged neural circuits is critical for neurological repair after brain injury.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="22%"><a href="https://doi.org/10.48550/arXiv.2507.09882">AdaBrain-Bench: Benchmarking Brain Foundation Models for Brain-Computer Interface Applications</a><br><sub>Jiamin Wu, Zichen Ren, Junyu Wang, Pengyu Zhu, Yonghao Song, Mianxin Liu, et al.</sub></td>
<td width="13%">2025<br>arXiv.org<br>12 citations</td>
<td width="30%">Non-invasive Brain-Computer Interfaces (BCI) offer a safe and accessible means of connecting the human brain to external devices, with broad applications in home and clinical settings to enhance human capabilities.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="22%"><a href="https://doi.org/10.1056/NEJMoa2314598">Longevity of a Brain-Computer Interface for Amyotrophic Lateral Sclerosis</a><br><sub>M. Vansteensel, S. Leinders, M. Branco, N. E. Crone, Timothy Denison, Z. Freudenburg, et al.</sub></td>
<td width="13%">2024<br>New England Journal of Medicine<br>41 citations</td>
<td width="30%">Summary The durability of communication using Brain-Computer Interfaces (BCIs) in people with progressive neurodegenerative disease has not been extensively examined.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="22%"><a href="https://doi.org/10.1186/s42490-024-00080-2">On the role of generative artificial intelligence in the development of brain-computer interfaces</a><br><sub>Seif Eldawlatly</sub></td>
<td width="13%">2024<br>BMC Biomedical Engineering<br>22 citations</td>
<td width="30%">Since their inception more than 50 years ago, Brain-Computer Interfaces (BCIs) have held promise to compensate for functions lost by people with disabilities through allowing direct communication between the brain and external devices.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="22%"><a href="https://doi.org/10.1038/s41467-024-49709-9">Low-intensity pulsed ultrasound stimulation (LIPUS) modulates microglial activation following intracortical microelectrode implantation</a><br><sub>Fan Li, Jazlyn Gallego, Natasha N Tirko, Jenna Greaser, Derek Bashe, Rudra Patel, et al.</sub></td>
<td width="13%">2024<br>Nature Communications<br>22 citations</td>
<td width="30%">Microglia are important players in surveillance and repair of the brain.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="22%"><a href="https://doi.org/10.1016/j.jneumeth.2025.110471">Advances in Endovascular Brain Computer Interface: systematic review and future implications.</a><br><sub>J. Ognard, G. El Hajj, O. Verma, S. Ghozy, R. Kadirvel, David F. Kallmes, et al.</sub></td>
<td width="13%">2025<br>Journal of Neuroscience Methods<br>9 citations</td>
<td width="30%">BACKGROUND Brain-computer interfaces (BCIs) translate neural activity into real-world commands.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="22%"><a href="https://doi.org/10.1145/3712259">Toward the Construction of Affective Brain-Computer Interface: A Systematic Review</a><br><sub>Huayu Chen, Junxiang Li, Huanhuan He, Jing Zhu, Shuting Sun, Xiaowei Li, et al.</sub></td>
<td width="13%">2025<br>ACM Computing Surveys<br>14 citations</td>
<td width="30%">Electroencephalography (EEG)-based affective computing aims to recognize the emotional state, which is the core technology of affective brain-computer interface (aBCI).</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="22%"><a href="https://doi.org/10.3390/app15073512">Usability and Acceptance Analysis of Wearable BCI Devices</a><br><sub>Ilaria Lombardi, Mario Buono, Giovanna Giugliano, V. P. Senese, S. Capece</sub></td>
<td width="13%">2025<br>Applied Sciences<br>5 citations</td>
<td width="30%">In the current scientific and technological scenario, wearable neuroimaging devices represent a revolution in neuroscience and wearable technology.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="22%"><a href="https://doi.org/10.1038/s41467-025-56979-4">Bacteria invade the brain following intracortical microelectrode implantation, inducing gut-brain axis disruption and contributing to reduced microelectrode performance</a><br><sub>George F. Hoeferlin, S. Grabinski, Lindsey N. Druschel, Jonathan L Duncan, G. Burkhart, Gwendolyn R Weagraff, et al.</sub></td>
<td width="13%">2025<br>Nature Communications<br>14 citations</td>
<td width="30%">Brain-machine interface performance can be affected by neuroinflammatory responses due to blood-brain barrier (BBB) damage following intracortical microelectrode implantation.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="22%"><a href="https://doi.org/10.1109/THMS.2025.3554449">Imagined Speech–EEG Detection Using Multivariate Swarm Sparse Decomposition-Based Joint Time–Frequency Analysis for Intuitive BCI</a><br><sub>S. Bhalerao, R. B. Pachori</sub></td>
<td width="13%">2025<br>IEEE Transactions on Human-Machine Systems<br>14 citations</td>
<td width="30%">In brain–computer interface (BCI) applications, imagined speech (IMS) decoding based on electroencephalogram (EEG) has established a new neuro-paradigm that offers an intuitive communication tool for physically impaired patients.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="22%"><a href="https://doi.org/10.7717/peerj-cs.2649">Improved BCI calibration in multimodal emotion recognition using heterogeneous adversarial transfer learning</a><br><sub>M. Sarikaya, Gökhan Ince</sub></td>
<td width="13%">2025<br>PeerJ Computer Science<br>6 citations</td>
<td width="30%">The use of brain-computer interface (BCI) technology to identify emotional states has gained significant interest, especially with the rise of virtual reality (VR) applications.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="22%"><a href="https://doi.org/10.1016/j.medntd.2025.100353">The history, current state and future possibilities of the non-invasive brain computer interfaces</a><br><sub>Frederico Caiado, Arkadiy Ukolov</sub></td>
<td width="13%">2025<br>Medicine in Novel Technology and Devices<br>18 citations</td>
<td width="30%">Positions The history, current state and future possibilities of the non-invasive brain computer interfaces within Invasive and Implantable Interfaces.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="22%"><a href="https://doi.org/10.1021/acssensors.4c02461">Brain-Computer Interface and Electrochemical Sensor Based on Boron-Nitrogen Co-Doped Graphene-Diamond Microelectrode for EEG and Dopamine Detection.</a><br><sub>Shiming Chen, Daolian Jiang, Mingji Li, Xiuwei Xuan, Hongji Li</sub></td>
<td width="13%">2025<br>ACS Sensors<br>17 citations</td>
<td width="30%">The simultaneous detection of electroencephalography (EEG) signals and neurotransmitter levels plays an important role as biomarkers for the assessment and monitoring of emotions and cognition.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="22%"><a href="https://doi.org/10.1038/s44385-025-00029-7">Flexible brain electronic sensors advance wearable brain-computer interface</a><br><sub>Jia Li, Guo Chen, Gang Li, Lujia Xiao, Ruonan Jia, Kun Zhang</sub></td>
<td width="13%">2025<br>npj Biomedical Innovations<br>5 citations</td>
<td width="30%">The emerging field of wearable brain-computer interface (BCI) strives to achieve both high spatial and temporal resolution.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td colspan="6">See the website and taxonomy CSV for all 39 papers.</td>
</tr>
</tbody>
</table>

</details>

### EEG Signal Processing and Datasets

- Papers selected: **29**
- Years covered: **2020-2026**
- Citation count in selected set: **1,908**
- Main research trends:
  - This taxonomy emphasizes reproducible preprocessing, artifact handling, channel selection, spatial filtering, and benchmark datasets for EEG-based BCI.
  - The field is gradually shifting from isolated algorithm papers toward shared datasets, standardized evaluation, and metadata-aware comparisons.
  - Hybrid EEG/fNIRS, transfer learning, and open benchmark resources are recurring themes for improving generalization and clinical relevance.

<details>
<summary>Show representative papers for EEG Signal Processing and Datasets</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.3389/fnbot.2020.00025">Current Status, Challenges, and Possible Solutions of EEG-Based Brain-Computer Interface: A Comprehensive Review</a><br><sub>M. Rashid, N. Sulaiman, A. P. Majeed, R. Musa, A. Nasir, Bifta Sama Bari, et al.</sub></td>
<td width="13%">2020<br>Frontiers in Neurorobotics<br>420 citations</td>
<td width="30%">Brain-Computer Interface (BCI), in essence, aims at controlling different assistive devices through the utilization of brain waves.</td>
<td width="15%">high citation signal (420); influential citation signal (18); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2020.3040289">Neural Decoding of Imagined Speech and Visual Imagery as Intuitive Paradigms for BCI Communication</a><br><sub>Seo-Hyun Lee, Minji Lee, Seong-Whan Lee</sub></td>
<td width="13%">2020<br>IEEE transactions on neural systems and rehabilitation engineering<br>133 citations</td>
<td width="30%">Brain-computer interface (BCI) is oriented toward intuitive systems that users can easily operate.</td>
<td width="15%">high citation signal (133); influential citation signal (10); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1007/s11831-021-09684-6">Review of Machine Learning Techniques for EEG Based Brain Computer Interface</a><br><sub>Swati Aggarwal, Nupur Chugh</sub></td>
<td width="13%">2022<br>Archives of Computational Methods in Engineering<br>233 citations</td>
<td width="30%">Positions Review of Machine Learning Techniques for EEG Based Brain Computer Interface within EEG Signal Processing and Datasets.</td>
<td width="15%">high citation signal (233)</td>
<td width="15%">abstract unavailable in metadata; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.3390/s21175746">Brain-Computer Interface: Advancement and Challenges</a><br><sub>M. F. Mridha, S. Das, Muhammad Mohsin Kabir, Aklima Akter Lima, Md. Rashedul Islam, Yutaka Watanobe</sub></td>
<td width="13%">2021<br>Italian National Conference on Sensors<br>213 citations</td>
<td width="30%">Brain-Computer Interface (BCI) is an advanced and multidisciplinary active research domain based on neuroscience, signal processing, biomedical sensors, hardware, etc.</td>
<td width="15%">high citation signal (213); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1016/J.BSPC.2021.102595">A systematic review on hybrid EEG/fNIRS in brain-computer interface</a><br><sub>Ziming Liu, J. Shore, Miao Wang, Fengpei Yuan, Aaron T. Buss, Xiaopeng Zhao</sub></td>
<td width="13%">2021<br>Biomedical Signal Processing and Control<br>130 citations</td>
<td width="30%">Abstract As a relatively new field of neurology and computer science, brain computer interface (BCI) has many established and burgeoning applications across scientific disciplines.</td>
<td width="15%">high citation signal (130)</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1109/TNSRE.2021.3096874">Decoding Imagined Speech Based on Deep Metric Learning for Intuitive BCI Communication</a><br><sub>Dong-Yeon Lee, Minji Lee, Seong-Whan Lee</sub></td>
<td width="13%">2021<br>IEEE transactions on neural systems and rehabilitation engineering<br>55 citations</td>
<td width="30%">Imagined speech is a highly promising paradigm due to its intuitive application and multiclass scalability in the field of brain-computer interfaces.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.1109/TAFFC.2021.3134183">Neurofeedback Training With an Electroencephalogram-Based Brain-Computer Interface Enhances Emotion Regulation</a><br><sub>Weichen Huang, Wei Wu, Molly V. Lucas, Haiyun Huang, Zhenfu Wen, Yuanqing Li</sub></td>
<td width="13%">2023<br>IEEE Transactions on Affective Computing<br>45 citations</td>
<td width="30%">Emotion regulation plays a vital role in human beings daily lives by helping them deal with social problems and protects mental and physical health.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.3390/s20216321">Application of Transfer Learning in EEG Decoding Based on Brain-Computer Interfaces: A Review</a><br><sub>Kai Zhang, Guanghua Xu, Xiaowei Zheng, Huanzhong Li, Sicong Zhang, Yunhui Yu, et al.</sub></td>
<td width="13%">2020<br>Italian National Conference on Sensors<br>60 citations</td>
<td width="30%">The algorithms of electroencephalography (EEG) decoding are mainly based on machine learning in current research.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.3390/s23136001">State-of-the-Art on Brain-Computer Interface Technology</a><br><sub>Jānis Pekša, D. Mamchur</sub></td>
<td width="13%">2023<br>Italian National Conference on Sensors<br>119 citations</td>
<td width="30%">This paper provides a comprehensive overview of the state-of-the-art in brain–computer interfaces (BCI).</td>
<td width="15%">high citation signal (119); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2024.1429130">Comprehensive evaluation methods for translating BCI into practical applications: usability, user satisfaction and usage of online BCI systems</a><br><sub>He Pan, Peng Ding, Fan Wang, Tianwen Li, Lei Zhao, Wenya Nan, et al.</sub></td>
<td width="13%">2024<br>Frontiers in Human Neuroscience<br>35 citations</td>
<td width="30%">Although brain-computer interface (BCI) is considered a revolutionary advancement in human-computer interaction and has achieved significant progress, a considerable gap remains between the current technological capabilities and their practical applications.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1038/s41597-022-01898-y">Open multi-session and multi-task EEG cognitive Dataset for passive brain-computer Interface Applications</a><br><sub>Marcel F. Hinss, E. Jahanpour, B. Somon, Lou Pluchon, F. Dehais, R. Roy</sub></td>
<td width="13%">2023<br>Scientific Data<br>51 citations</td>
<td width="30%">Brain-Computer Interfaces and especially passive Brain-Computer interfaces (pBCI), with their ability to estimate and monitor user mental states, are receiving increasing attention from both the fundamental research and the applied research and development communities.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bspc.2022.103526">Machine-learning-enabled adaptive signal decomposition for a brain-computer interface using EEG</a><br><sub>Ashwin Kamble, P. Ghare, Vinay P. Kumar</sub></td>
<td width="13%">2022<br>Biomedical Signal Processing and Control<br>55 citations</td>
<td width="30%">Positions Machine-learning-enabled adaptive signal decomposition for a brain-computer interface using EEG within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2022.901387">Evaluation of a New Lightweight EEG Technology for Translational Applications of Passive Brain-Computer Interfaces</a><br><sub>Nicolina Sciaraffa, G. di Flumeri, D. Germano, Andrea Giorgi, Antonio Di Florio, G. Borghini, et al.</sub></td>
<td width="13%">2022<br>Frontiers in Human Neuroscience<br>44 citations</td>
<td width="30%">Technologies like passive brain-computer interfaces (BCI) can enhance human-machine interaction.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.19101/ijatee.2021.874883">EEG artifacts detection and removal techniques for brain computer interface applications: a systematic review</a><br><sub>Unknown authors</sub></td>
<td width="13%">2022<br>International Journal of Advanced Technology and Engineering Exploration<br>37 citations</td>
<td width="30%">Positions EEG artifacts detection and removal techniques for brain computer interface applications: a systematic review within EEG Signal Processing and Datasets.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="22%"><a href="https://doi.org/10.1007/s11042-022-12795-2">Automatic EEG channel selection for multiclass brain-computer interface classification using multiobjective improved firefly algorithm</a><br><sub>Anurag Tiwari, Amrita Chaturvedi</sub></td>
<td width="13%">2022<br>Multimedia tools and applications<br>38 citations</td>
<td width="30%">Positions Automatic EEG channel selection for multiclass brain-computer interface classification using multiobjective improved firefly algorithm within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bbe.2023.05.001">Hybrid EEG-fNIRS brain-computer interface based on the non-linear features extraction and stacking ensemble learning</a><br><sub>Asmaa Maher, Saeed Mian Qaisar, N. Salankar, Feng Jiang, R. Tadeusiewicz, Paweł Pławiak, et al.</sub></td>
<td width="13%">2023<br>Biocybernetics and Biomedical Engineering<br>41 citations</td>
<td width="30%">Positions Hybrid EEG-fNIRS brain-computer interface based on the non-linear features extraction and stacking ensemble learning within EEG Signal Processing and Datasets.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="22%"><a href="https://doi.org/10.1016/j.future.2023.01.028">Adversarial robustness benchmark for EEG-based brain-computer interfaces</a><br><sub>Lubin Meng, Xue Jiang, Dongrui Wu</sub></td>
<td width="13%">2023<br>Future generations computer systems<br>24 citations</td>
<td width="30%">Positions Adversarial robustness benchmark for EEG-based brain-computer interfaces within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="22%"><a href="https://doi.org/10.1109/TIM.2024.3417598">Instrumentation, Measurement, and Signal Processing in Electroencephalography-Based Brain-Computer Interfaces: Situations and Prospects</a><br><sub>Zifan Xue, Yunfan Zhang, Hui Li, Hongbin Chen, Shengnan Shen, Hejun Du</sub></td>
<td width="13%">2024<br>IEEE Transactions on Instrumentation and Measurement<br>27 citations</td>
<td width="30%">Proper signal measurement and processing are crucial in electroencephalography (EEG)-based brain-computer interfaces (BCIs), as they form the basis of brain insight and precise BCI control.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2024.1416683">Enhancing learning experiences: EEG-based passive BCI system adapts learning speed to cognitive load in real-time, with motivation as catalyst</a><br><sub>Noémie Beauchemin, Patrick Charland, A. Karran, Jared Boasen, Bella Tadson, S. Sénécal, et al.</sub></td>
<td width="13%">2024<br>Frontiers in Human Neuroscience<br>31 citations</td>
<td width="30%">Computer-based learning has gained popularity in recent years, providing learners greater flexibility and freedom.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="22%"><a href="https://doi.org/10.1038/s41597-024-03398-7">ChineseEEG: A Chinese Linguistic Corpora EEG Dataset for Semantic Alignment and Neural Decoding</a><br><sub>Xinyu Mou, Cuilin He, Liwei Tan, Junjie Yu, Huadong Liang, Jianyu Zhang, et al.</sub></td>
<td width="13%">2024<br>bioRxiv<br>18 citations</td>
<td width="30%">An Electroencephalography (EEG) dataset utilizing rich text stimuli can advance the understanding of how the brain encodes semantic information and contribute to semantic decoding in brain-computer interface (BCI).</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="22%"><a href="https://doi.org/10.1109/COMST.2024.3396847">A Survey on Brain-Computer Interface-Inspired Communications: Opportunities and Challenges</a><br><sub>Honglin Hu, Zhenyu Wang, Xi Zhao, Ruxue Li, Ang Li, Yuan Si, et al.</sub></td>
<td width="13%">2025<br>IEEE Communications Surveys and Tutorials<br>29 citations</td>
<td width="30%">Brain-computer interfaces (BCIs) aim to directly bridge the human brain and the outside world through acquiring and processing the brain signals in real time.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="22%"><a href="https://doi.org/10.1186/s40708-025-00290-x">Beyond the lab: real-world benchmarking of wearable EEGs for passive brain-computer interfaces</a><br><sub>V. Ronca, Marianna Cecchetti, R. Capotorto, G. D. Flumeri, A. Giorgi, D. Germano, et al.</sub></td>
<td width="13%">2025<br>Brain Informatics<br>10 citations</td>
<td width="30%">Wearable EEG systems are increasingly used for brain–computer interface (BCI) applications beyond controlled laboratory environments.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="22%"><a href="https://doi.org/10.1145/3746027.3754810">Pretraining Large Brain Language Model for Active BCI: Silent Speech</a><br><sub>Jinzhao Zhou, Zehong Cao, Yiqun Duan, Connor Barkley, Daniel Leong, Xiaowei Jiang, et al.</sub></td>
<td width="13%">2025<br>ACM Multimedia<br>9 citations</td>
<td width="30%">This paper explores silent speech decoding in active brain-computer interface (BCI) systems, which offer more natural and flexible communication than traditional BCI applications.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="22%"><a href="https://doi.org/10.1016/j.knosys.2025.113074">Time-frequency transform based EEG data augmentation for brain-computer interfaces</a><br><sub>Ziwei Wang, Siyang Li, Xiaoqing Chen, Dongrui Wu</sub></td>
<td width="13%">2025<br>Knowledge-Based Systems<br>22 citations</td>
<td width="30%">Positions Time-frequency transform based EEG data augmentation for brain-computer interfaces within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bspc.2024.106943">E-FNet: A EEG-fNIRS dual-stream model for Brain-Computer Interfaces</a><br><sub>Binlong Yu, Lei Cao, Jie Jia, Chunjiang Fan, Yilin Dong, Changming Zhu</sub></td>
<td width="13%">2025<br>Biomedical Signal Processing and Control<br>20 citations</td>
<td width="30%">Positions E-FNet: A EEG-fNIRS dual-stream model for Brain-Computer Interfaces within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="22%"><a href="https://doi.org/10.1109/TETCI.2025.3619564">Multi-Scale Shapley Adaptation Pruning: Realizing Backdoor Defense in Brain-Computer Interface With Shapley-Value-Based Neural Network Pruning</a><br><sub>Fumin Li, Rui Yang, Hanjing Cheng, Mengjie Huang, Fan Zhang, Fuad E. Alsaadi, et al.</sub></td>
<td width="13%">2026<br>IEEE Transactions on Emerging Topics in Computational Intelligence<br>7 citations</td>
<td width="30%">In the recent years, researchers made significant progress in electroencephalogram (EEG) classification tasks using deep neural networks, especially in brain-computer interface (BCI) systems.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="22%"><a href="https://doi.org/10.31435/ijitss.2(50).2026.5446">BROAD APPLICATIONS OF CONSUMER-GRADE EEG DEVICES: FROM CLINICAL DIAGNOSTICS TO BRAIN-COMPUTER INTERFACES AND SOCIAL SCIENCES – LITERATURE REVIEW</a><br><sub>K. Borzęcka, Agnieszka Szwed, A. Sołtys, Daria Aleksandra Warzocha-Żurek, Ewa Maria Polewczak-Karp, Katarzyna Wawrzonek, et al.</sub></td>
<td width="13%">2026<br>International Journal of Innovative Technologies in Social Science<br>0 citations</td>
<td width="30%">Research Objective: This review article aims to assess the rapidly growing market for commercial electroencephalography (EEG) devices and analyze their transition from sterile laboratory conditions to a variety of real-world applications.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="22%"><a href="https://doi.org/10.1016/j.csi.2026.104155">Adversarial attacks and defenses in EEG based Brain Computer Interfaces: A comprehensive survey and future directions</a><br><sub>Nour El-Houda Sayah Ben Aissa, Kerrache Chaker Abdelaziz, C. Calafate</sub></td>
<td width="13%">2026<br>Comput. Stand. Interfaces<br>1 citations</td>
<td width="30%">Positions Adversarial attacks and defenses in EEG based Brain Computer Interfaces: A comprehensive survey and future directions within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="22%"><a href="https://doi.org/10.1080/10447318.2025.2602691">A Systematic Review of Techniques, Artifacts, Challenges and Future Directions on Signal Acquisition and Preprocessing in Brain-Computer Interfaces (BCIs)</a><br><sub>Samriti Thakur, S. Thakur, Aryan Rana, Pankaj Kumar, Ashok Kumar Das</sub></td>
<td width="13%">2026<br>International Journal of Human-Computer Interaction<br>1 citations</td>
<td width="30%">Positions A Systematic Review of Techniques, Artifacts, Challenges and Future Directions on Signal Acquisition and Preprocessing in Brain-Computer Interfaces (BCIs) within EEG Signal Processing and Datasets.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
</tbody>
</table>

</details>

### Rehabilitation and Neuroprosthetics

- Papers selected: **21**
- Years covered: **2020-2026**
- Citation count in selected set: **513**
- Main research trends:
  - The dominant trend is integration of BCI with robotic gloves, exoskeletons, FES, VR, and task-oriented therapy for post-stroke and motor impairment rehabilitation.
  - Studies increasingly ask whether BCI training transfers to activities of daily living rather than only improving offline decoding accuracy.
  - Recent work points toward home-use, patient-centered protocols, multimodal feedback, and combined motor-cognitive-affective rehabilitation.

<details>
<summary>Show representative papers for Rehabilitation and Neuroprosthetics</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1016/j.heliyon.2020.e04250">Brain computer interface based applications for training and rehabilitation of students with neurodevelopmental disorders. A literature review</a><br><sub>George P Papanastasiou, A. Drigas, C. Skianis, Miltiadis Demetrios Lytras</sub></td>
<td width="13%">2020<br>Heliyon<br>125 citations</td>
<td width="30%">The aim of this article is to explore a paradigm shift on Brain Computer Interface (BCI) research, as well as on intervention best practices for training and rehabilitation of students with neurodevelopmental disorders.</td>
<td width="15%">high citation signal (125); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1109/TIM.2022.3216673">Deep-Learning-Based BCI for Automatic Imagined Speech Recognition Using SPWVD</a><br><sub>Ashwin Kamble, P. Ghare, Vinay P. Kumar</sub></td>
<td width="13%">2023<br>IEEE Transactions on Instrumentation and Measurement<br>64 citations</td>
<td width="30%">The electroencephalogram (EEG)-based brain–computer interface (BCI) has potential applications in neuroscience and rehabilitation.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.3389/fnins.2021.728178">Signal Generation, Acquisition, and Processing in Brain Machine Interfaces: A Unified Review</a><br><sub>Usman Salahuddin, P. Gao</sub></td>
<td width="13%">2021<br>Frontiers in Neuroscience<br>36 citations</td>
<td width="30%">Brain machine interfaces (BMIs), or brain computer interfaces (BCIs), are devices that act as a medium for communications between the brain and the computer.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.64719/pb.4281">Effectiveness of a brain-computer interface based programme for the treatment of ADHD: a pilot study.</a><br><sub>C. Lim, Tih-Shih Lee, Cuntai Guan, Daniel Shuen Sheng Fung, Y. Cheung, S. Teng, et al.</sub></td>
<td width="13%">2025<br>Psychopharmacology bulletin<br>72 citations</td>
<td width="30%">Majority of children with attention deficit hyperactivity disorder (ADHD) have significant inattentive symptoms.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.3390/ijms24065182">Sensing and Stimulation Applications of Carbon Nanomaterials in Implantable Brain-Computer Interface</a><br><sub>Jinning Li, Yuhang Cheng, Minling Gu, Zhensheng Yang, Lisi Zhan, Zhanhong Du</sub></td>
<td width="13%">2023<br>International Journal of Molecular Sciences<br>28 citations</td>
<td width="30%">Implantable brain–computer interfaces (BCIs) are crucial tools for translating basic neuroscience concepts into clinical disease diagnosis and therapy.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1038/s44222-024-00177-2">Brain-computer interfaces for neuropsychiatric disorders</a><br><sub>Lucine L. Oganesian, Maryam Shanechi</sub></td>
<td width="13%">2024<br>Nature Reviews Bioengineering<br>28 citations</td>
<td width="30%">Neuropsychiatric disorders such as major depression are a leading cause of disability worldwide with standard treatments, including psychotherapy or medication, failing many patients.</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.31083/j.jin2307125">Review on the Use of Brain Computer Interface Rehabilitation Methods for Treating Mental and Neurological Conditions.</a><br><sub>V. Khorev, S. Kurkin, A. Badarin, Vladimir M. Antipov, E. Pitsik, A. Andreev, et al.</sub></td>
<td width="13%">2024<br>Journal of Integrative Neuroscience<br>35 citations</td>
<td width="30%">This review provides a comprehensive examination of recent developments in both neurofeedback and brain-computer interface (BCI) within the medical field and rehabilitation.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.1155/2023/2793211">Identifying Thematics in a Brain-Computer Interface Research</a><br><sub>H. Alharbi</sub></td>
<td width="13%">2023<br>Computational Intelligence and Neuroscience<br>12 citations</td>
<td width="30%">This umbrella review is motivated to understand the shift in research themes on brain-computer interfacing (BCI) and it determined that a shift away from themes that focus on medical advancement and system development to applications that included education, marketing, gaming, safety, and security has occurred.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.1039/d4cs01074d">Implantable hydrogels as pioneering materials for next-generation brain-computer interfaces.</a><br><sub>Wasid Ullah Khan, Zhenzhen Shen, Samuel M. Mugo, Hongda Wang, Qiang Zhang</sub></td>
<td width="13%">2025<br>Chemical Society Reviews<br>29 citations</td>
<td width="30%">Use of brain-computer interfaces (BCIs) is rapidly becoming a transformative approach for diagnosing and treating various brain disorders.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bioactmat.2024.08.034">Enhancing biocompatibility of the brain-machine interface: A review</a><br><sub>Jordan Villa, Joaquin Cury, Lexie Kessler, Xiaodong Tan, Claus-Peter Richter</sub></td>
<td width="13%">2024<br>Bioactive Materials<br>28 citations</td>
<td width="30%">In vivo implantation of microelectrodes opens the door to studying neural circuits and restoring damaged neural pathways through direct electrical stimulation and recording.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1126/sciadv.adz9968">Real-time decoding of full-spectrum Chinese using brain-computer interface</a><br><sub>Youkun Qian, Changjiang Liu, Peixi Yu, Xingchen Ran, Shurui Li, Qinrong Yang, et al.</sub></td>
<td width="13%">2025<br>Science Advances<br>11 citations</td>
<td width="30%">Speech brain-computer interfaces (BCIs) offer a promising means to provide functional communication capacity for patients with anarthria caused by neurological conditions such as amyotrophic lateral sclerosis (ALS) or brainstem stroke.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.3389/fhumd.2025.1553905">Neuralink’s brain-computer interfaces: medical innovations and ethical challenges</a><br><sub>A. Lavazza, M. Balconi, Marcello Ienca, Francesca Minerva, F. Pizzetti, M. Reichlin, et al.</sub></td>
<td width="13%">2025<br>Frontiers in Human Dynamics<br>20 citations</td>
<td width="30%">Neuralink’s advancements in brain-computer interface (BCI) technology have positioned the company as a leader in this emerging field.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.1016/j.brainresbull.2025.111354">Advances in Brain-Computer Interface Controlled Functional Electrical Stimulation for Upper Limb Recovery After Stroke.</a><br><sub>Yidan Zhang, Yuling Gao, Jia-qi Zhou, Zhenni Zhang, M. Feng, Yong Liu</sub></td>
<td width="13%">2025<br>Brain Research Bulletin<br>12 citations</td>
<td width="30%">Stroke often results in varying degrees of functional impairment, significantly affecting patients&#x27; quality of daily life.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.1371/journal.pdig.0000524">Community perspectives regarding brain-computer interfaces: A cross-sectional study of community-dwelling adults in the UK</a><br><sub>A. El‐Osta, Mahmoud Al Ammouri, Shujhat Khan, Sami Altalib, M. Karki, Eva Riboli-Sasco, et al.</sub></td>
<td width="13%">2025<br>PLOS Digital Health<br>6 citations</td>
<td width="30%">Background Brain-computer interfaces (BCIs) represent a ground-breaking advancement in neuroscience, facilitating direct communication between the brain and external devices.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="22%"><a href="https://doi.org/10.1007/s40820-025-02042-2">Non-Invasive Brain-Computer Interfaces: Converging Frontiers in Neural Signal Decoding and Flexible Bioelectronics Integration</a><br><sub>Sheng Wang, Xiaobin Song, Xiaopan Song, Yang Gu, Zhuangzhuang Cong, Yi Shen, et al.</sub></td>
<td width="13%">2026<br>Nano-Micro Letters<br>4 citations</td>
<td width="30%">The latest advancements in neural signal decoding and the integration of flexible bioelectronics for non-invasive brain-computer interfaces are reviewed.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="22%"><a href="https://doi.org/10.64898/2026.02.19.26346583">Restoring brain-to-text communication in a person with dysarthria from pontine stroke using an intracortical brain-computer interface</a><br><sub>S. R. Nason-Tomaszewski, P. Deevi, Q. Rabbani, B. Jacques, A. L. Pritchard, L. Wimalasena, et al.</sub></td>
<td width="13%">2026<br>medRxiv<br>1 citations</td>
<td width="30%">Positions Restoring brain-to-text communication in a person with dysarthria from pontine stroke using an intracortical brain-computer interface within Rehabilitation and Neuroprosthetics.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="22%"><a href="https://doi.org/10.1109/TCE.2025.3650654">Generative AI Empowers Brain-Computer Interfaces: A Review-Perspective on Technical Realities and Future Visions</a><br><sub>Shuqiang Wang, Yi Guo, Yihang Dong, Yanyan Shen, Zhiguo Zhang, Albert C. Cheung, et al.</sub></td>
<td width="13%">2026<br>IEEE transactions on consumer electronics<br>1 citations</td>
<td width="30%">Generative artificial intelligence (AI) has recently emerged as a transformative paradigm for brain-computer interfaces (BCIs), with impact spanning hardware, data, algorithms and applications.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="22%"><a href="https://doi.org/10.1016/j.neuroscience.2026.03.010">A neurofeedback-guided EEG and BCI framework for personalized attention rehabilitation in ADHD.</a><br><sub>Wenyang Yang, Jing Yuan, Lin Ding, Steven Kwok Keung Chow</sub></td>
<td width="13%">2026<br>Neuroscience<br>1 citations</td>
<td width="30%">The integration of game-based cognitive training with electroencephalography (EEG)-based brain-computer interaction (BCI) has demonstrated potential for enhancing attention among individuals with attention-deficit hyperactivity disorder (ADHD).</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="22%"><a href="https://doi.org/10.2147/EB.S561691">Brain-Computer Interfaces for Vision Recovery in Precortical Vision Loss</a><br><sub>Christopher D. Yang, A. Guo, Ken Y Lin</sub></td>
<td width="13%">2026<br>Eye and Brain<br>0 citations</td>
<td width="30%">Introduction Precortical vision loss remains a major global health challenge.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="22%"><a href="https://doi.org/10.1016/j.ibneur.2026.04.011">Mapping knowledge structure and emerging trends in non-invasive brain-computer interface for stroke rehabilitation</a><br><sub>Ying Li, Jiaying Chen, Yu Wang, Jinghui Huang, Fanfu Fang</sub></td>
<td width="13%">2026<br>IBRO Neuroscience Reports<br>0 citations</td>
<td width="30%">Objective To explore the current research landscape and emerging frontiers in the application of non‑invasive brain–computer interface (BCI) technology in the field of stroke.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="22%"><a href="https://doi.org/10.12659/MSM.951399">Application and Research Progress of Brain-Computer Interface for Post-Stroke Psychiatric Disorders: A Narrative Review</a><br><sub>Zekai Hu, Jinyan Wang, Kun Zhou, Sicong Ma, Jun Hu</sub></td>
<td width="13%">2026<br>Medical Science Monitor<br>0 citations</td>
<td width="30%">Post-stroke psychiatric disorders (PSPD), including depression, anxiety, and cognitive impairment, significantly hinder stroke survivors’ rehabilitation and quality of life, with traditional interventions often showing limited efficacy.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
</tbody>
</table>

</details>

### General BCI Methods and Systems

- Papers selected: **14**
- Years covered: **2020-2026**
- Citation count in selected set: **953**
- Main research trends:
  - General BCI work is consolidating definitions, system architectures, evaluation principles, and long-term challenges across invasive and non-invasive approaches.
  - Recent surveys increasingly emphasize translation, usability, ethics, safety, reproducibility, and the gap between laboratory performance and real-world use.
  - This area functions as the conceptual bridge between signal processing, neural engineering, clinical deployment, and human-centered design.

<details>
<summary>Show representative papers for General BCI Methods and Systems</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1007/978-3-540-29678-2_717">Brain-Computer Interfaces</a><br><sub>Ricardo Chavarriaga, J. Millán</sub></td>
<td width="13%">2020<br>Handbook of Clinical Neurology<br>548 citations</td>
<td width="30%">Positions Brain-Computer Interfaces within General BCI Methods and Systems.</td>
<td width="15%">high citation signal (548); influential citation signal (36); open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1016/j.matt.2022.01.012">Bioadhesive and conductive hydrogel-integrated brain-machine interfaces for conformal and immune-evasive contact with brain tissue</a><br><sub>Xiao Wang, Xiaotong Sun, Donglin Gan, M. Soubrier, H. Chiang, Liwei Yan, et al.</sub></td>
<td width="13%">2022<br>Matter<br>159 citations</td>
<td width="30%">Positions Bioadhesive and conductive hydrogel-integrated brain-machine interfaces for conformal and immune-evasive contact with brain tissue within General BCI Methods and Systems.</td>
<td width="15%">high citation signal (159); open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1109/TBCAS.2022.3175926">A Power-Efficient Brain-Machine Interface System With a Sub-mw Feature Extraction and Decoding ASIC Demonstrated in Nonhuman Primates</a><br><sub>Hyochan An, S. R. Nason-Tomaszewski, Jongyup Lim, Kyumin Kwon, Matthew S. Willsey, Parag G. Patil, et al.</sub></td>
<td width="13%">2022<br>IEEE Transactions on Biomedical Circuits and Systems<br>28 citations</td>
<td width="30%">Positions A Power-Efficient Brain-Machine Interface System With a Sub-mw Feature Extraction and Decoding ASIC Demonstrated in Nonhuman Primates within General BCI Methods and Systems.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.30574/ijsra.2024.11.1.0111">Neural interfaces and human-computer interaction: A U.S. review: Delving into the developments, ethical considerations, and future prospects of brain-computer interfaces</a><br><sub>Sedat Sonko, Adefunke Fabuyide, Kenneth Ifeanyi Ibekwe, Emmanuel Augustine Etukudoh, Valentine Ikenna Ilojianya</sub></td>
<td width="13%">2024<br>International Journal of Science and Research Archive<br>16 citations</td>
<td width="30%">This study provides a comprehensive analysis of the developments, ethical considerations, and future prospects of brain-computer interfaces (BCIs) in the United States.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1007/s11042-023-15653-x">Electroencephalogram based brain-computer interface: Applications, challenges, and opportunities</a><br><sub>Hitesh Yadav, S. Maini</sub></td>
<td width="13%">2023<br>Multimedia tools and applications<br>44 citations</td>
<td width="30%">Brain-Computer Interfaces (BCI) is an exciting and emerging research area for researchers and scientists.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1016/j.measen.2023.100823">Machine learning techniques for electroencephalogram based brain-computer interface: A systematic literature review</a><br><sub>Pawan, R. Dhiman</sub></td>
<td width="13%">2023<br>Measurement: Sensors<br>44 citations</td>
<td width="30%">Positions Machine learning techniques for electroencephalogram based brain-computer interface: A systematic literature review within General BCI Methods and Systems.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.7759/cureus.58243">Understanding the Ethical Issues of Brain-Computer Interfaces (BCIs): A Blessing or the Beginning of a Dystopian Future?</a><br><sub>Efstratios Livanis, P. Voultsos, Konstantinos Vadikolias, Panagiotis Pantazakos, Alexandra K. Tsaroucha</sub></td>
<td width="13%">2024<br>Cureus<br>30 citations</td>
<td width="30%">In recent years, scientific discoveries in the field of neuroscience combined with developments in the field of artificial intelligence have led to the development of a range of neurotechnologies.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.1016/j.asoc.2024.111648">Development of real-time brain-computer interface control system for robot</a><br><sub>Yang An, J. Wong, Sai-Ho Ling</sub></td>
<td width="13%">2024<br>Applied Soft Computing<br>41 citations</td>
<td width="30%">Positions Development of real-time brain-computer interface control system for robot within General BCI Methods and Systems.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.3389/fnins.2023.1345961">Brain-computer interface paradigms and neural coding</a><br><sub>Pengrui Tai, Peng Ding, Fan Wang, Anmin Gong, Tianwen Li, Lei Zhao, et al.</sub></td>
<td width="13%">2024<br>Frontiers in Neuroscience<br>27 citations</td>
<td width="30%">Brain signal patterns generated in the central nervous system of brain-computer interface (BCI) users are closely related to BCI paradigms and neural coding.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1016/j.hest.2025.09.002">Application and future directions of brain-computer interfaces in neurological disorders: Technological advances, clinical practices, and challenges</a><br><sub>Qiao Deng, Zhuang Fu, Nai Ma, Boding Wang</sub></td>
<td width="13%">2025<br>Brain Hemorrhages<br>10 citations</td>
<td width="30%">Positions Application and future directions of brain-computer interfaces in neurological disorders: Technological advances, clinical practices, and challenges within General BCI Methods and Systems.</td>
<td width="15%">recognized venue</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bspc.2025.108904">Brain-computer interfaces for memory enhancement: Scientometric analysis and future directions</a><br><sub>M. Kapsetaki</sub></td>
<td width="13%">2026<br>Biomedical Signal Processing and Control<br>2 citations</td>
<td width="30%">Positions Brain-computer interfaces for memory enhancement: Scientometric analysis and future directions within General BCI Methods and Systems.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.1016/j.bspc.2025.109025">Recursive sample weighted - N-way partial least squares for brain-computer interface decoder online learning with class imbalance</a><br><sub>Rémi Souriau, Félix Martel, T. Aksenova</sub></td>
<td width="13%">2026<br>Biomedical Signal Processing and Control<br>3 citations</td>
<td width="30%">Positions Recursive sample weighted - N-way partial least squares for brain-computer interface decoder online learning with class imbalance within General BCI Methods and Systems.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2026.1777024">Brain-computer interface: an update for the clinicians</a><br><sub>Agam Jain, Sreelakshmi Raveendran, K. P. S. Nair, S. Ramakrishnan</sub></td>
<td width="13%">2026<br>Frontiers in Human Neuroscience<br>0 citations</td>
<td width="30%">This narrative review critically examines the fundamental principles and clinical applications of Brain-Computer Interfaces (BCIs) in neuroscience and mental health.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="22%"><a href="https://doi.org/10.3390/proceedings2026137124">A Systematic Review of Neuroplasticity Induced by Brain–Computer Interface Combined with Virtual Reality (BCI-VR)</a><br><sub>Maria F. C. Goulart, Victor I. Maciel, Isabele C. Mortari, Sávio C. Souza, Rafaela T. Cruvinel, R. Bernardes, et al.</sub></td>
<td width="13%">2026<br>The 6th International Congress on Health Innovation&amp;amp;mdash;INOVATEC 2025<br>1 citations</td>
<td width="30%">Positions A Systematic Review of Neuroplasticity Induced by Brain–Computer Interface Combined with Virtual Reality (BCI-VR) within General BCI Methods and Systems.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
</tbody>
</table>

</details>

### Deep Learning and Representation Learning

- Papers selected: **12**
- Years covered: **2020-2026**
- Citation count in selected set: **828**
- Main research trends:
  - Deep learning work is moving beyond single-dataset CNN classifiers toward temporal, spectral, graph, transformer, and attention-based architectures.
  - A major trend is representation learning that can transfer across users, sessions, headsets, and BCI paradigms with less subject-specific calibration.
  - Interpretability, uncertainty, robustness to artifacts, and benchmark comparability are becoming as important as peak classification accuracy.

<details>
<summary>Show representative papers for Deep Learning and Representation Learning</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1109/TCBB.2021.3052811">EEG-Based Brain-Computer Interfaces (BCIs): A Survey of Recent Studies on Signal Sensing Technologies and Computational Intelligence Approaches and Their Applications</a><br><sub>Xiaotong Gu, Zehong Cao, A. Jolfaei, Peng Xu, Dongrui Wu, T. Jung, et al.</sub></td>
<td width="13%">2020<br>IEEE/ACM Transactions on Computational Biology &amp; Bioinformatics<br>322 citations</td>
<td width="30%">Brain-Computer interfaces (BCIs) enhance the capability of human brain activities to interact with the environment.</td>
<td width="15%">high citation signal (322); influential citation signal (11); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1109/MCI.2021.3061875">Multi-Scale Neural Network for EEG Representation Learning in BCI</a><br><sub>Wonjun Ko, Eunjin Jeon, Seungwoo Jeong, Heung-Il Suk</sub></td>
<td width="13%">2020<br>IEEE Computational Intelligence Magazine<br>102 citations</td>
<td width="30%">Recent advances in deep learning have had a methodological and practical impact on brain-computer interface (BCI) research.</td>
<td width="15%">high citation signal (102); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1109/JBHI.2024.3504604">EEG-Deformer: A Dense Convolutional Transformer for Brain-Computer Interfaces</a><br><sub>Yi Ding, Yong Li, Hao Sun, Rui Liu, Chengxuan Tong, Chenyu Liu, et al.</sub></td>
<td width="13%">2024<br>IEEE journal of biomedical and health informatics<br>91 citations</td>
<td width="30%">Effectively learning the temporal dynamics in electroencephalogram (EEG) signals is challenging yet essential for decoding brain activities using brain-computer interfaces (BCIs).</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.1016/j.engappai.2022.105347">Adaptive transfer learning-based multiscale feature fused deep convolutional neural network for EEG MI multiclassification in brain-computer interface</a><br><sub>Anisha Roy</sub></td>
<td width="13%">2022<br>Engineering applications of artificial intelligence<br>158 citations</td>
<td width="30%">Positions Adaptive transfer learning-based multiscale feature fused deep convolutional neural network for EEG MI multiclassification in brain-computer interface within Deep Learning and Representation Learning.</td>
<td width="15%">high citation signal (158)</td>
<td width="15%">abstract unavailable in metadata; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.3389/fnrgo.2021.805573">Denoising EEG Signals for Real-World BCI Applications Using GANs</a><br><sub>Eoin Brophy, P. Redmond, Andrew Fleury, M. de Vos, G. Boylan, Tomás Ward</sub></td>
<td width="13%">2022<br>Frontiers in Neuroergonomics<br>52 citations</td>
<td width="30%">As a measure of the brain&#x27;s electrical activity, electroencephalography (EEG) is the primary signal of interest for brain-computer-interfaces (BCI).</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.3389/fnrgo.2022.838342">Retrospective on the First Passive Brain-Computer Interface Competition on Cross-Session Workload Estimation</a><br><sub>R. Roy, Marcel F. Hinss, L. Darmet, S. Ladouce, E. Jahanpour, B. Somon, et al.</sub></td>
<td width="13%">2022<br>Frontiers in Neuroergonomics<br>36 citations</td>
<td width="30%">As is the case in several research domains, data sharing is still scarce in the field of Brain-Computer Interfaces (BCI), and particularly in that of passive BCIs—i.e., systems that enable implicit interaction or task adaptation based on a user&#x27;s mental state(s) estimated from brain measures.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.1093/pnasnexus/pgae076">Transfer learning promotes acquisition of individual BCI skills</a><br><sub>Satyam Kumar, Hussein Alawieh, F. S. Racz, R. Fakhreddine, J. D. R. Millán</sub></td>
<td width="13%">2024<br>PNAS Nexus<br>39 citations</td>
<td width="30%">Abstract Subject training is crucial for acquiring brain–computer interface (BCI) control.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="22%"><a href="https://doi.org/10.48550/arXiv.2502.02830">Multimodal Brain-Computer Interfaces: AI-powered Decoding Methodologies</a><br><sub>Siyang Li, Hongbin Wang, Xiaoqing Chen, Dongrui Wu</sub></td>
<td width="13%">2025<br>arXiv.org<br>15 citations</td>
<td width="30%">Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="22%"><a href="https://doi.org/10.1016/j.neuroimage.2025.121123">Augmenting brain-computer interfaces with ART: An artifact removal transformer for reconstructing multichannel EEG signals</a><br><sub>Chun-Hsiang Chuang, Kong-Yi Chang, Chih-Sheng Huang, Anne-Mei Bessas</sub></td>
<td width="13%">2025<br>NeuroImage<br>8 citations</td>
<td width="30%">Artifact removal in electroencephalography (EEG) is a longstanding challenge that significantly impacts neuroscientific analysis and brain-computer interface (BCI) performance.</td>
<td width="15%">recognized venue</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="22%"><a href="https://doi.org/10.1016/j.hest.2026.01.002">Neural Decoding for EEG-BCI: From Conventional Machine Learning to Deep Learning Models</a><br><sub>Yibo Ding, Xinyu Ma, Ping Zhang, Yingxin Tang, Zhixian Zhao, Danyang Chen, et al.</sub></td>
<td width="13%">2026<br>Brain Hemorrhages<br>2 citations</td>
<td width="30%">Positions Neural Decoding for EEG-BCI: From Conventional Machine Learning to Deep Learning Models within Deep Learning and Representation Learning.</td>
<td width="15%">recognized venue</td>
<td width="15%">abstract unavailable in metadata; recent work may be under-cited; limited citation history</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="22%"><a href="https://doi.org/10.59717/j.xinn-life.2026.100198">Advancing brain-computer interfaces with generative AI: A review of state-of-the-art and future outlook</a><br><sub>Su Han, Shanshan Feng, Fan Li</sub></td>
<td width="13%">2026<br>The Innovation Life<br>1 citations</td>
<td width="30%">Brain-Computer Interface (BCI) technology is rapidly emerging as a promising tool to empower individuals with severe disabilities and enhance their independence by translating brain neural signals into actionable commands.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="22%"><a href="https://doi.org/10.1109/OJSP.2026.3664271">Alternatives to Sine Carrier in Auditory BCI: Exploring Machine Learning Strategies for Assessing Modulation Detectability in EEG</a><br><sub>Lenaïg Guého, Henrique Lefundes da Silva, Cyril Plapous, L. Bougrain, Patrick Hénaff, Rozenn Nicol</sub></td>
<td width="13%">2026<br>IEEE Open Journal of Signal Processing<br>2 citations</td>
<td width="30%">In this paper, the use of non-sinusoidal amplitude-modulated stimuli is assessed for Brain-Computer Interfaces (BCIs) based on Steady-State Auditory Evoked Potentials (SSAEPs).</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">recent work may be under-cited; limited citation history; PDF link not available from metadata</td>
</tr>
</tbody>
</table>

</details>

### Speech, Language, and Communication BCIs

- Papers selected: **7**
- Years covered: **2020-2024**
- Citation count in selected set: **926**
- Main research trends:
  - Communication BCI is expanding from spelling paradigms toward imagined speech, decoded language, and higher-bandwidth text production.
  - Both invasive and non-invasive studies are exploring more naturalistic communication, including speech motor cortex decoding and inner-speech EEG datasets.
  - The central challenge remains preserving accuracy, latency, vocabulary size, and user autonomy in real-world assistive communication.

<details>
<summary>Show representative papers for Speech, Language, and Communication BCIs</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.3390/brainsci11010043">Summary of over Fifty Years with Brain-Computer Interfaces—A Review</a><br><sub>Aleksandra Kawala-Sterniuk, Natalia Browarska, Amir F. Al-Bakri, Mariusz Pelc, J. Zygarlicki, Michaela Sidikova, et al.</sub></td>
<td width="13%">2021<br>Brain Science<br>236 citations</td>
<td width="30%">Over the last few decades, the Brain-Computer Interfaces have been gradually making their way to the epicenter of scientific interest.</td>
<td width="15%">high citation signal (236); influential citation signal (10); recognized venue</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.1016/j.tics.2021.04.003">Interface, interaction, and intelligence in generalized brain-computer interfaces.</a><br><sub>Xiaorong Gao, Yijun Wang, Xiaogang Chen, Shangkai Gao</sub></td>
<td width="13%">2021<br>Trends in Cognitive Sciences<br>263 citations</td>
<td width="30%">A brain-computer interface (BCI) establishes a direct communication channel between a brain and an external device.</td>
<td width="15%">high citation signal (263); recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1016/j.inat.2020.100694">Brain computer interface advancement in neurosciences: Applications and issues</a><br><sub>S. Mudgal, S. Sharma, Jitender Chaturvedi, A. Sharma</sub></td>
<td width="13%">2020<br>Interdisciplinary Neurosurgery<br>117 citations</td>
<td width="30%">Abstract Neurosciences and Neuro-technology are continuously advancing and so individuals, society and healthcare professionals have to up date themselves with advancement.</td>
<td width="15%">high citation signal (117); open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="22%"><a href="https://doi.org/10.1016/j.jneumeth.2020.108918">A comprehensive assessment of Brain Computer Interfaces: Recent trends and challenges.</a><br><sub>Drishti Yadav, S. Yadav, K. Veer</sub></td>
<td width="13%">2020<br>Journal of Neuroscience Methods<br>89 citations</td>
<td width="30%">BACKGROUND An uninterrupted channel of communication and control between the human brain and electronic processing units has led to an increased use of Brain Computer Interfaces (BCIs).</td>
<td width="15%">recognized venue</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="22%"><a href="https://doi.org/10.1007/s13311-022-01190-2">Brain-Computer Interface: Applications to Speech Decoding and Synthesis to Augment Communication</a><br><sub>S. Luo, Q. Rabbani, N. Crone</sub></td>
<td width="13%">2022<br>Neurotherapeutics<br>97 citations</td>
<td width="30%">Positions Brain-Computer Interface: Applications to Speech Decoding and Synthesis to Augment Communication within Speech, Language, and Communication BCIs.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">abstract unavailable in metadata</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="22%"><a href="https://doi.org/10.1109/COMST.2024.3387124">A Human-Centric Metaverse Enabled by Brain-Computer Interface: A Survey</a><br><sub>Howe Yuan Zhu, Nguyen Quang Hieu, D. Hoang, Diep N. Nguyen, Chin-Teng Lin</sub></td>
<td width="13%">2023<br>IEEE Communications Surveys and Tutorials<br>48 citations</td>
<td width="30%">The growing interest in the Metaverse has generated momentum for members of academia and industry to innovate toward realizing the Metaverse world.</td>
<td width="15%">open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="22%"><a href="https://doi.org/10.1109/ICCSP60870.2024.10543610">IoT in Brain-Computer Interfaces for Enabling Communication and Control for the Disabled</a><br><sub>Dr. S. Rajarajan, P. M. Suresh, Dr. T. Kowsalya, Nukala Sujata, Gupta, S. Murugan</sub></td>
<td width="13%">2024<br>International Conference on Cryptography, Security and Privacy<br>76 citations</td>
<td width="30%">The proposed system integrates Internet of Things (IoT) technologies with Brain-computer interfaces to improve disability-related communication and control.</td>
<td width="15%">selected from the top-scored BCI candidate pool</td>
<td width="15%">PDF link not available from metadata</td>
</tr>
</tbody>
</table>

</details>

### Hybrid, Affective, and Closed-loop BCIs

- Papers selected: **3**
- Years covered: **2020-2022**
- Citation count in selected set: **174**
- Main research trends:
  - Hybrid BCI combines multiple signals or paradigms to improve reliability, command diversity, and asynchronous control.
  - Closed-loop and neurofeedback work is increasingly focused on user adaptation, mental-state awareness, fatigue, affect, and training protocols.
  - The trend is toward systems that adapt to the user over time rather than treating decoding as a one-shot offline classification problem.

<details>
<summary>Show representative papers for Hybrid, Affective, and Closed-loop BCIs</summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="22%">
<col width="13%">
<col width="30%">
<col width="15%">
<col width="15%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Key idea</th>
<th>Strengths</th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="22%"><a href="https://doi.org/10.1088/1741-2552/abca17">A review of user training methods in brain computer interfaces based on mental tasks</a><br><sub>A. Roc, Léa Pillette, J. Mladenović, Camille Benaroch, B. N&#x27;Kaoua, C. Jeunet, et al.</sub></td>
<td width="13%">2020<br>Journal of Neural Engineering<br>98 citations</td>
<td width="30%">Mental-tasks based brain–computer interfaces (MT-BCIs) allow their users to interact with an external device solely by using brain signals produced through mental tasks.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="22%"><a href="https://doi.org/10.3389/fnhum.2021.635777">Long-Term Mutual Training for the CYBATHLON BCI Race With a Tetraplegic Pilot: A Case Study on Inter-Session Transfer and Intra-Session Adaptation</a><br><sub>Lea Hehenberger, Reinmar J. Kobler, Catarina Lopes-Dias, Nitikorn Srisrisawang, P. Tumfart, J. B. Uroko, et al.</sub></td>
<td width="13%">2021<br>Frontiers in Human Neuroscience<br>28 citations</td>
<td width="30%">CYBATHLON is an international championship where people with severe physical disabilities compete with the aid of state-of-the-art assistive technology.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="22%"><a href="https://doi.org/10.1126/scitranslmed.abm5868">Closed-loop stimulation using a multi-region brain-machine interface has analgesic effects in rodents</a><br><sub>Guanghao Sun, Fei Zeng, Michael McCartin, Qiaosheng Zhang, Helen Y. Xu, Yaling Liu, et al.</sub></td>
<td width="13%">2022<br>Science Translational Medicine<br>48 citations</td>
<td width="30%">Effective treatments for chronic pain remain limited.</td>
<td width="15%">recognized venue; open-access PDF metadata</td>
<td width="15%">metadata-level appraisal; full PDF review still needed</td>
</tr>
</tbody>
</table>

</details>

## Yearly Coverage

| Year | Selected papers | Citation count | Top paper |
| ---: | ---: | ---: | --- |
| 2020 | 100 | 10,957 | [Current Status, Challenges, and Possible Solutions of EEG-Based Brain-Computer Interface: A Comprehensive Review](https://doi.org/10.3389/fnbot.2020.00025) |
| 2021 | 100 | 8,999 | [A brain-computer interface that evokes tactile sensations improves robotic arm control](https://doi.org/10.1126/science.abd0380) |
| 2022 | 100 | 6,112 | [FBMSNet: A Filter-Bank Multi-Scale Convolutional Neural Network for EEG-Based Motor Imagery Decoding](https://doi.org/10.1109/TBME.2022.3193277) |
| 2023 | 100 | 4,932 | [Physics-Informed Attention Temporal Convolutional Network for EEG-Based Motor Imagery Classification](https://doi.org/10.1109/TII.2022.3197419) |
| 2024 | 100 | 3,461 | [Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://doi.org/10.48550/arXiv.2405.18765) |
| 2025 | 100 | 1,397 | [EEG-based brain-computer interface enables real-time robotic hand control at individual finger level](https://doi.org/10.1038/s41467-025-61064-x) |
| 2026 | 100 | 102 | [Toward Robust, Reproducible, and Widely Accessible Intracranial Language Brain-Computer Interfaces: A Comprehensive Review of Neural Mechanisms, Hardware, Algorithms, Evaluation, Clinical Pathways and Future Directions](https://arxiv.org/abs/2603.12279) |
## Method

The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and reduced to a maximum of 500 candidates per year. Importance scoring combines log-scaled citation count, log-scaled influential citation count, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive/high-bandwidth interfaces, and modern ML methods. The final awesome list uses the top 100 scored papers per year.

## Caveats

- Citation counts favor older papers and may under-rank recent 2026 work.
- Metadata search is not equivalent to a full systematic review of PDFs.
- Some venues and publication dates are missing in upstream metadata.
