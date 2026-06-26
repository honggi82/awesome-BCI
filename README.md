# Awesome BCI

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A taxonomy-first, citation-ranked map of recent Brain-Computer Interface (BCI) research.

<p align="center">
  <a href="https://honggi82.github.io/awesome-BCI/">
    <img src="https://img.shields.io/badge/Open_Interactive_Website-honggi82.github.io%2Fawesome--BCI-0f766e?style=for-the-badge" alt="Open Interactive Website">
  </a>
</p>

> Browse the full interactive taxonomy site with period, language, keyword, chart, and paper-card filters: https://honggi82.github.io/awesome-BCI/

Generated on 2026-06-26 from free public Semantic Scholar metadata. The current edition investigates up to 500 BCI-related candidate papers per year for 2000-2026, keeps an audited candidate pool, selects the top 100 papers per year by citation count, and reorganizes the final 2,447 papers by research taxonomy.

## Project Links

- Website: https://honggi82.github.io/awesome-BCI/
- Selected dataset: `data/papers_2000_2026.csv`
- Taxonomy dataset with paper-level ideas, strengths, and limitations: `data/papers_taxonomy_2000_2026.csv`
- Precomputed period and language analysis: `data/period_analysis_2000_2026.json`
- Candidate pool: `data/candidates_top500_2000_2026.csv`
- English review draft: `paper/review_en.html`, `paper/review_en.docx`
- Korean review draft: `paper/review_ko.html`
- Curation method: `paper/curation_method.md`, `paper/curation_method.html`

## Keywords Convention

These badges define the BCI keyword tags used to read and extend this collection.

- ![invasive](https://img.shields.io/badge/keyword-invasive-2563eb) **invasive**: Implanted or intracranial neural interfaces, including ECoG and intracortical recordings.
- ![non-invasive](https://img.shields.io/badge/keyword-non--invasive-0f766e) **non-invasive**: External sensing interfaces such as EEG, MEG, fNIRS, or fMRI.
- ![human](https://img.shields.io/badge/keyword-human-f59e0b) **human**: Studies using human participants, patients, or volunteers.
- ![non-human](https://img.shields.io/badge/keyword-non--human-a855f7) **non-human**: Animal, simulation, or non-human experimental settings.
- ![SMR](https://img.shields.io/badge/keyword-SMR-dc2626) **SMR**: Sensorimotor rhythm, ERD/ERS, or motor-imagery control paradigms.
- ![SSVEP](https://img.shields.io/badge/keyword-SSVEP-7c3aed) **SSVEP**: Steady-state visual evoked potential paradigms.
- ![P300](https://img.shields.io/badge/keyword-P300-be123c) **P300**: P300 or event-related-potential speller paradigms.
- ![arm-direction](https://img.shields.io/badge/keyword-arm--direction-0891b2) **arm-direction**: Arm, hand, reach, or directional movement decoding/control.

## Taxonomy Overview

- **Total selected papers**: 2,447 papers
- **Motor Imagery and Movement Decoding**: 1050 papers
- **General BCI Methods and Systems**: 425 papers
- **SSVEP, P300, and ERP Spellers**: 391 papers
- **EEG Signal Processing and Datasets**: 265 papers
- **Invasive and Implantable Interfaces**: 135 papers
- **Rehabilitation and Neuroprosthetics**: 87 papers
- **Hybrid, Affective, and Closed-loop BCIs**: 32 papers
- **Speech, Language, and Communication BCIs**: 31 papers
- **Deep Learning and Representation Learning**: 31 papers

## Taxonomy Collections

### Motor Imagery and Movement Decoding

- Papers selected: **1050**
- Years covered: **2000-2026**
- Citation count in selected set: **130,164**
- Category Overview (main research trends):
  - The field is moving from subject-specific pipelines toward cross-subject, calibration-light, and transfer-learning decoders for EEG motor imagery.
  - Deep CNN, temporal convolution, graph, attention, and large EEG representation models are increasingly used to improve robustness under noisy and low-data conditions.
  - Application work is expanding from binary hand imagery toward gait, lower-limb control, soft robotics, virtual feedback, and rehabilitation-oriented closed-loop use.
- Limitations:
  - Cross-subject and cross-session variability still limits real-world robustness, especially when calibration time is short.
  - Many high-scoring methods remain validated on offline datasets rather than sustained closed-loop control or clinical rehabilitation outcomes.
  - Citation-ranked lists can favor mature EEG motor imagery pipelines over newer low-citation work on multimodal movement decoding.

<details>
<summary><strong>Show representative papers for Motor Imagery and Movement Decoding</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2552/aace8c">EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces</a><br><sub>Vernon J. Lawhern, Amelia J. Solon, Nicholas R. Waytowich, S. Gordon, C. Hung, Brent Lance</sub></td>
<td width="12%">2016<br>Journal of Neural Engineering<br>4,344 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Objective.</td>
<td align="right" width="8%">4,344</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1109/5.939829">Motor imagery and direct brain-computer communication</a><br><sub>G. Pfurtscheller, C. Neuper</sub></td>
<td width="12%">2001<br>Proceedings of the IEEE<br>2,002 citations</td>
<td width="12%"><img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Motor imagery and direct brain-computer communication within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">2,002</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neuroimage.2005.12.003">Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks</a><br><sub>G. Pfurtscheller, C. Brunner, A. Schlögl, F. H. L. D. Silva</sub></td>
<td width="12%">2006<br>NeuroImage<br>1,617 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Mu rhythm (de)synchronization and EEG single-trial classification of different motor imagery tasks within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">1,617</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1073/pnas.0403504101">Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans.</a><br><sub>J. Wolpaw, D. McFarland</sub></td>
<td width="12%">2004<br>Proceedings of the National Academy of Sciences of the United States of America<br>1,608 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">1,608</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2552/ab0ab5">Deep learning for electroencephalogram (EEG) classification tasks: a review</a><br><sub>Alexander Craik, Yongtian He, J. Contreras-Vidal</sub></td>
<td width="12%">2019<br>Journal of Neural Engineering<br>1,540 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Objective.</td>
<td align="right" width="8%">1,540</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.3389/fnins.2012.00039">Filter Bank Common Spatial Pattern Algorithm on BCI Competition IV Datasets 2a and 2b</a><br><sub>K. Ang, Z. Chin, C. Wang, Cuntai Guan, Haihong Zhang</sub></td>
<td width="12%">2012<br>Frontiers in Neuroscience<br>1,201 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">The Common Spatial Pattern (CSP) algorithm is an effective and popular method for classifying 2-class motor imagery electroencephalogram (EEG) data, but its effectiveness depends on the subject-specific frequency band.</td>
<td align="right" width="8%">1,201</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1101/703801">An Integrated Brain-Machine Interface Platform With Thousands of Channels</a><br><sub>E. Musk</sub></td>
<td width="12%">2019<br>bioRxiv<br>978 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Brain-machine interfaces (BMIs) hold promise for the restoration of sensory and motor function and the treatment of neurological disorders, but clinical BMIs have not yet been widely adopted, in part because modest channel counts have limited their potential.</td>
<td align="right" width="8%">978</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.3389/fnhum.2015.00003">fNIRS-based brain-computer interfaces: a review</a><br><sub>Noman Naseer, K. Hong</sub></td>
<td width="12%">2015<br>Frontiers in Human Neuroscience<br>929 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">A brain-computer interface (BCI) is a communication system that allows the use of brain activity to control computers or other external devices.</td>
<td align="right" width="8%">929</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1038/s41586-021-03506-2">High-performance brain-to-text communication via handwriting</a><br><sub>Francis R. Willett, Donald T. Avansino, L. Hochberg, J. Henderson, K. Shenoy</sub></td>
<td width="12%">2021<br>Nature<br>848 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Brain–computer interfaces (BCIs) can restore communication to people who have lost the ability to move or speak.</td>
<td align="right" width="8%">848</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2552/aaf12e">A comprehensive review of EEG-based brain–computer interface paradigms</a><br><sub>R. Abiri, Soheil Borhani, E. Sellers, Yang Jiang, Xiaopeng Zhao</sub></td>
<td width="12%">2019<br>Journal of Neural Engineering<br>836 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Advances in brain science and computer technology in the past decade have led to exciting developments in brain–computer interface (BCI), thereby making BCI a top research area in applied science.</td>
<td align="right" width="8%">836</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/14/1/016003">A novel deep learning approach for classification of EEG motor imagery signals</a><br><sub>Y. R. Tabar, U. Halici</sub></td>
<td width="12%">2017<br>Journal of Neural Engineering<br>819 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions A novel deep learning approach for classification of EEG motor imagery signals within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">819</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1038/416141a">Brain-machine interface: Instant neural control of a movement signal</a><br><sub>M. Serruya, N. Hatsopoulos, L. Paninski, M. Fellows, J. Donoghue</sub></td>
<td width="12%">2002<br>Nature<br>806 citations</td>
<td width="12%"><img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions Brain-machine interface: Instant neural control of a movement signal within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">806</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Arm or cursor decoding performance may not generalize to unconstrained daily functional movements.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1111/j.1469-8986.2006.00456.x">Breaking the silence: brain-computer interfaces (BCI) for communication and motor control.</a><br><sub>N. Birbaumer</sub></td>
<td width="12%">2006<br>Psychophysiology<br>768 citations</td>
<td width="12%"><img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Breaking the silence: brain-computer interfaces (BCI) for communication and motor control. within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">768</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.3389/fnpro.2010.00003">The Hybrid BCI</a><br><sub>G. Pfurtscheller, B. Allison, C. Brunner, G. Bauernfeind, T. Solis-Escalante, Reinhold Scherer, et al.</sub></td>
<td width="12%">2010<br>Frontiers in Neuroscience<br>755 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Nowadays, everybody knows what a hybrid car is.</td>
<td align="right" width="8%">755</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1186/1744-9081-7-30">Automatic Classification of Artifactual ICA-Components for Artifact Removal in EEG Signals</a><br><sub>I. Winkler, S. Haufe, M. Tangermann</sub></td>
<td width="12%">2011<br>Behavioral and Brain Functions<br>744 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">BackgroundArtifacts contained in EEG recordings hamper both, the visual interpretation by experts as well as the algorithmic processing and analysis (e.g.</td>
<td align="right" width="8%">744</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neuroimage.2006.11.005">Temporal classification of multichannel near-infrared spectroscopy signals of motor imagery for developing a brain-computer interface</a><br><sub>R. Sitaram, Haihong Zhang, Cuntai Guan, M. Thulasidas, Y. Hoshi, A. Ishikawa, et al.</sub></td>
<td width="12%">2007<br>NeuroImage<br>611 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">There has been an increase in research interest for brain-computer interface (BCI) technology as an alternate mode of communication and environmental control for the disabled, such as patients suffering from amyotrophic lateral sclerosis (ALS), brainstem stroke and spinal cord injury.</td>
<td align="right" width="8%">611</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1002/ana.24390">Brain–computer interface boosts motor imagery practice during stroke recovery</a><br><sub>F. Pichiorri, G. Morone, M. Petti, J. Toppi, I. Pisotta, M. Molinari, et al.</sub></td>
<td width="12%">2015<br>Annals of Neurology<br>597 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Brain–computer interface boosts motor imagery practice during stroke recovery within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">597</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1186/1743-0003-8-66">Rehabilitation of gait after stroke: a review towards a top-down approach</a><br><sub>J. Belda-Lois, S. Mena-del Horno, I. Bermejo-Bosch, J. Moreno, J. Pons, D. Farina, et al.</sub></td>
<td width="12%">2011<br>Journal of NeuroEngineering and Rehabilitation<br>578 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">This document provides a review of the techniques and therapies used in gait rehabilitation after stroke.</td>
<td align="right" width="8%">578</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1212/01.wnl.0000158616.43002.6d">Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface</a><br><sub>A. Kübler, F. Nijboer, J. Mellinger, T. M. Vaughan, H. Pawelzik, G. Schalk, et al.</sub></td>
<td width="12%">2005<br>Neurology<br>572 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">572</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1093/gigascience/giz002">EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy</a><br><sub>Min-Ho Lee, O-Yeon Kwon, Yong-Jeong Kim, Hong Kim, Young-Eun Lee, J. Williamson, et al.</sub></td>
<td width="12%">2019<br>GigaScience<br>567 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Abstract Background Electroencephalography (EEG)-based brain-computer interface (BCI) systems are mainly divided into three major paradigms: motor imagery (MI), event-related potential (ERP), and steady-state visually evoked potential (SSVEP).</td>
<td align="right" width="8%">567</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/10/4/046003">Quadcopter control in three-dimensional space using a noninvasive motor imagery based brain-computer interface</a><br><sub>K. Lafleur, K. Cassady, A. Doud, K. Shades, E. Rogin, Bin He</sub></td>
<td width="12%">2013<br>Journal of Neural Engineering<br>564 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Objective.</td>
<td align="right" width="8%">564</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1126/science.aaa5417">Decoding motor imagery from the posterior parietal cortex of a tetraplegic human</a><br><sub>T. Aflalo, S. Kellis, Christian Klaes, Brian Lee, Ying Shi, K. Pejsa, et al.</sub></td>
<td width="12%">2015<br>Science<br>556 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Brain imagination to control external devices Studies in monkeys have implicated the brain&#x27;s posterior parietal cortex in high-level coding of planned and imagined actions.</td>
<td align="right" width="8%">556</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1007/s00521-021-06352-5">Deep learning techniques for classification of electroencephalogram (EEG) motor imagery (MI) signals: a review</a><br><sub>Hamdi Altaheri, G. Muhammad, M. Alsulaiman, S. Amin, G. Altuwaijri, Wadood Abdul, et al.</sub></td>
<td width="12%">2021<br>Neural computing &amp; applications (Print)<br>551 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Deep learning techniques for classification of electroencephalogram (EEG) motor imagery (MI) signals: a review within Motor Imagery and Movement Decoding.</td>
<td align="right" width="8%">551</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1109/tnnls.2018.2789927">Learning Temporal Information for Brain-Computer Interface Using Convolutional Neural Networks</a><br><sub>Siavash Sakhavi, Cuntai Guan, Shuicheng Yan</sub></td>
<td width="12%">2018<br>IEEE Transactions on Neural Networks and Learning Systems<br>544 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Deep learning (DL) methods and architectures have been the state-of-the-art classification algorithms for computer vision and natural language processing problems.</td>
<td align="right" width="8%">544</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1038/s41467-018-04673-z">Brain-actuated functional electrical stimulation elicits lasting arm motor recovery after stroke</a><br><sub>A. Biasiucci, R. Leeb, I. Iturrate, S. Perdikis, A. Al-Khodairy, T. Corbet, et al.</sub></td>
<td width="12%">2018<br>Nature Communications<br>536 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Brain-computer interfaces (BCI) are used in stroke rehabilitation to translate brain signals into intended movements of the paralyzed limb.</td>
<td align="right" width="8%">536</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1038/nature20118">A Brain–Spinal Interface Alleviating Gait Deficits after Spinal Cord Injury in Primates</a><br><sub>M. Capogrosso, T. Milekovic, D. Borton, Fabien B. Wagner, E. Moraud, Jean-Baptiste Mignardot, et al.</sub></td>
<td width="12%">2016<br>Nature<br>526 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Spinal cord injury disrupts the communication between the brain and the spinal circuits that orchestrate movement.</td>
<td align="right" width="8%">526</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Offline benchmark performance may not transfer to real-time closed-loop use.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1155/2011/217987">Multisubject Learning for Common Spatial Patterns in Motor-Imagery BCI</a><br><sub>D. Devlaminck, B. Wyns, M. Grosse-Wentrup, G. Otte, P. Santens</sub></td>
<td width="12%">2011<br>Computational Intelligence and Neuroscience<br>524 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Motor-imagery-based brain-computer interfaces (BCIs) commonly use the common spatial pattern filter (CSP) as preprocessing step before feature extraction and classification.</td>
<td align="right" width="8%">524</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1155/2007/79642">Self-Paced (Asynchronous) BCI Control of a Wheelchair in Virtual Environments: A Case Study with a Tetraplegic</a><br><sub>R. Leeb, D. Friedman, G. Müller-Putz, Reinhold Scherer, M. Slater, G. Pfurtscheller</sub></td>
<td width="12%">2007<br>Computational Intelligence and Neuroscience<br>522 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">The aim of the present study was to demonstrate for the first time that brain waves can be used by a tetraplegic to control movements of his wheelchair in virtual reality (VR).</td>
<td align="right" width="8%">522</td>
<td width="24%">SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1007/s10548-009-0121-6">Towards a Cure for BCI Illiteracy</a><br><sub>C. Vidaurre, B. Blankertz</sub></td>
<td width="12%">2009<br>Brain Topography<br>509 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Brain–Computer Interfaces (BCIs) allow a user to control a computer application by brain activity as acquired, e.g., by EEG.</td>
<td align="right" width="8%">509</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.3390/s19061423">EEG-Based Brain-Computer Interfaces Using Motor-Imagery: Techniques and Challenges</a><br><sub>Natasha M. J. Padfield, J. Zabalza, Huimin Zhao, Valentin Masero Vargas, J. Ren</sub></td>
<td width="12%">2019<br>Italian National Conference on Sensors<br>503 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Electroencephalography (EEG)-based brain-computer interfaces (BCIs), particularly those using motor-imagery (MI) data, have the potential to become groundbreaking technologies in both clinical and entertainment settings.</td>
<td align="right" width="8%">503</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; SMR and movement decoders often need subject-specific calibration and may drift across sessions.; Offline motor-imagery accuracy may not translate to reliable continuous control or rehabilitation gains.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 1050 papers.</td>
</tr>
</tbody>
</table>

</details>

### General BCI Methods and Systems

- Papers selected: **425**
- Years covered: **2000-2026**
- Citation count in selected set: **55,190**
- Category Overview (main research trends):
  - General BCI work is consolidating definitions, system architectures, evaluation principles, and long-term challenges across invasive and non-invasive approaches.
  - Recent surveys increasingly emphasize translation, usability, ethics, safety, reproducibility, and the gap between laboratory performance and real-world use.
  - This area functions as the conceptual bridge between signal processing, neural engineering, clinical deployment, and human-centered design.
- Limitations:
  - Survey and system papers can dominate citation-ranked views while obscuring smaller empirical advances.
  - Evaluation language remains inconsistent across paradigms, making taxonomy boundaries imperfect.
  - Broad system claims often need stronger protocol-level reproducibility checks and real-world usability validation.

<details>
<summary><strong>Show representative papers for General BCI Methods and Systems</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.827072">BCI2000: a general-purpose brain-computer interface (BCI) system</a><br><sub>G. Schalk, D. McFarland, T. Hinterberger, N. Birbaumer, J. Wolpaw</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>3,136 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions BCI2000: a general-purpose brain-computer interface (BCI) system within General BCI Methods and Systems.</td>
<td align="right" width="8%">3,136</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1109/tre.2000.847807">Brain-computer interface technology: a review of the first international meeting.</a><br><sub>J. Wolpaw, N. Birbaumer, W. J. Heetderks, Dennis J. McFarland, P. Peckham, G. Schalk, et al.</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>2,282 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interface technology: a review of the first international meeting. within General BCI Methods and Systems.</td>
<td align="right" width="8%">2,282</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1016/j.tins.2006.07.004">Brain-machine interfaces: past, present and future.</a><br><sub>M. Lebedev, M. Nicolelis</sub></td>
<td width="12%">2006<br>Trends in Neurosciences<br>1,865 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-machine interfaces: past, present and future. within General BCI Methods and Systems.</td>
<td align="right" width="8%">1,865</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1109/ijcnn.2008.4634130">Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface</a><br><sub>K. Ang, Z. Y. Chin, Haihong Zhang, Cuntai Guan</sub></td>
<td width="12%">2008<br>IEEE World Congress on Computational Intelligence<br>1,456 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface within General BCI Methods and Systems.</td>
<td align="right" width="8%">1,456</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2006.875642">The BCI competition III: validating alternative approaches to actual BCI problems</a><br><sub>B. Blankertz, K. Müller, D. Krusienski, G. Schalk, J. Wolpaw, A. Schlögl, et al.</sub></td>
<td width="12%">2006<br>IEEE transactions on neural systems and rehabilitation engineering<br>934 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions The BCI competition III: validating alternative approaches to actual BCI problems within General BCI Methods and Systems.</td>
<td align="right" width="8%">934</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/955e2d6b7f237add6cde6b9786efbb7d9ef6893a">Brain-Computer Interfaces: Principles and Practice</a><br><sub>J. Wolpaw, E. Wolpaw</sub></td>
<td width="12%">2012<br>Unknown venue<br>901 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-Computer Interfaces: Principles and Practice within General BCI Methods and Systems.</td>
<td align="right" width="8%">901</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2002.803536">Design and implementation of a brain-computer interface with high transfer rates</a><br><sub>Ming Cheng, Xiaorong Gao, Shangkai Gao, D. Xu</sub></td>
<td width="12%">2002<br>IEEE Transactions on Biomedical Engineering<br>854 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Design and implementation of a brain-computer interface with high transfer rates within General BCI Methods and Systems.</td>
<td align="right" width="8%">854</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/9031aac7e9b6adae909ce22fa35fa74ec52a52ec">BCI Competition 2008 { Graz data set B</a><br><sub>R. Leeb, C. Brunner</sub></td>
<td width="12%">2008<br>Unknown venue<br>811 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions BCI Competition 2008 { Graz data set B within General BCI Methods and Systems.</td>
<td align="right" width="8%">811</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1109/86.847819">Brain-computer interfaces based on the steady-state visual-evoked response.</a><br><sub>Matthew Middendorf, G. McMillan, G. Calhoun, Keith S. Jones</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>713 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interfaces based on the steady-state visual-evoked response. within General BCI Methods and Systems.</td>
<td align="right" width="8%">713</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neuroimage.2010.03.022">Neurophysiological predictor of SMR-based BCI performance</a><br><sub>B. Blankertz, C. Sannelli, Sebastian Halder, E. Hammer, A. Kübler, K. Müller, et al.</sub></td>
<td width="12%">2010<br>NeuroImage<br>686 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Neurophysiological predictor of SMR-based BCI performance within General BCI Methods and Systems.</td>
<td align="right" width="8%">686</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1016/j.mayocp.2011.12.008">Brain-computer interfaces in medicine.</a><br><sub>J. Shih, D. Krusienski, J. Wolpaw</sub></td>
<td width="12%">2012<br>Mayo Clinic proceedings<br>647 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interfaces in medicine. within General BCI Methods and Systems.</td>
<td align="right" width="8%">647</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1109/86.847821">Current trends in Graz Brain-Computer Interface (BCI) research.</a><br><sub>G. Pfurtscheller, C. Neuper, C. Guger, W. Harkam, H. Ramoser, A. Schlögl, et al.</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>575 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Current trends in Graz Brain-Computer Interface (BCI) research. within General BCI Methods and Systems.</td>
<td align="right" width="8%">575</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2003.814449">A BCI-based environmental controller for the motion-disabled.</a><br><sub>Xiaorong Gao, D. Xu, Ming Cheng, Shangkai Gao</sub></td>
<td width="12%">2003<br>IEEE transactions on neural systems and rehabilitation engineering<br>574 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A BCI-based environmental controller for the motion-disabled. within General BCI Methods and Systems.</td>
<td align="right" width="8%">574</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1007/978-3-540-29678-2_717">Brain-Computer Interfaces</a><br><sub>Ricardo Chavarriaga, J. Millán</sub></td>
<td width="12%">2020<br>Handbook of Clinical Neurology<br>548 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-Computer Interfaces within General BCI Methods and Systems.</td>
<td align="right" width="8%">548</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.827827">Support vector channel selection in BCI</a><br><sub>T. N. Lal, M. Tangermann, T. Hinterberger, J. Weston, M. Bogdan, N. Birbaumer, et al.</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>546 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Support vector channel selection in BCI within General BCI Methods and Systems.</td>
<td align="right" width="8%">546</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1109/86.847823">Brain-computer interface research at the Wadsworth Center.</a><br><sub>J. Wolpaw, D. McFarland, T. Vaughan</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>514 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interface research at the Wadsworth Center. within General BCI Methods and Systems.</td>
<td align="right" width="8%">514</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1109/rbme.2009.2035356">Clinical Applications of Brain-Computer Interfaces: Current State and Future Prospects</a><br><sub>J. Mak, J. Wolpaw</sub></td>
<td width="12%">2009<br>IEEE Reviews in Biomedical Engineering<br>495 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Braincomputer interfaces (BCIs) allow their users to communicate or control external devices using brain signals rather than the brain&#x27;s normal output pathways of peripheral nerves and muscles.</td>
<td align="right" width="8%">495</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neucom.2016.10.024">Brain computer interface: control signals review</a><br><sub>R. Ramadan, A. Vasilakos</sub></td>
<td width="12%">2017<br>Neurocomputing<br>470 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain computer interface: control signals review within General BCI Methods and Systems.</td>
<td align="right" width="8%">470</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neuroimage.2007.03.019">An MEG-based brain-computer interface (BCI)</a><br><sub>J. Mellinger, G. Schalk, C. Braun, H. Preissl, W. Rosenstiel, N. Birbaumer, et al.</sub></td>
<td width="12%">2007<br>NeuroImage<br>466 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions An MEG-based brain-computer interface (BCI) within General BCI Methods and Systems.</td>
<td align="right" width="8%">466</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.827063">Principles of a brain-computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI)</a><br><sub>N. Weiskopf, K. Mathiak, S. Bock, F. Scharnowski, R. Veit, W. Grodd, et al.</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>450 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Principles of a brain-computer interface (BCI) based on real-time functional magnetic resonance imaging (fMRI) within General BCI Methods and Systems.</td>
<td align="right" width="8%">450</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.3109/17482961003777470">A brain-computer interface for long-term independent home use</a><br><sub>E. Sellers, T. Vaughan, J. Wolpaw</sub></td>
<td width="12%">2010<br>Amyotrophic Lateral Sclerosis<br>438 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A brain-computer interface for long-term independent home use within General BCI Methods and Systems.</td>
<td align="right" width="8%">438</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/c7a146b7317f1befab39cf432044f8f2ce01221d">Brain-computer interface technology: a review of the Second International Meeting.</a><br><sub>T. Vaughan, W. J. Heetderks, L. Trejo, W. Z. Rymer, M. Weinrich, M.M. Moore, et al.</sub></td>
<td width="12%">2003<br>IEEE transactions on neural systems and rehabilitation engineering<br>415 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interface technology: a review of the Second International Meeting. within General BCI Methods and Systems.</td>
<td align="right" width="8%">415</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jneumeth.2007.02.009">An auditory brain-computer interface (BCI).</a><br><sub>F. Nijboer, A. Furdea, I. Gunst, J. Mellinger, D. McFarland, N. Birbaumer, et al.</sub></td>
<td width="12%">2008<br>Journal of Neuroscience Methods<br>404 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions An auditory brain-computer interface (BCI). within General BCI Methods and Systems.</td>
<td align="right" width="8%">404</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.826702">BCI competition 2003-data sets Ib and IIb: feature extraction from event-related brain potentials with the continuous wavelet transform and the t-value scalogram</a><br><sub>Vladimir Bostanov</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>400 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions BCI competition 2003-data sets Ib and IIb: feature extraction from event-related brain potentials with the continuous wavelet transform and the t-value scalogram within General BCI Methods and Systems.</td>
<td align="right" width="8%">400</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1109/rbme.2011.2172408">Brain-Computer Interfaces Using Electrocorticographic Signals</a><br><sub>G. Schalk, E. Leuthardt</sub></td>
<td width="12%">2011<br>IEEE Reviews in Biomedical Engineering<br>397 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-Computer Interfaces Using Electrocorticographic Signals within General BCI Methods and Systems.</td>
<td align="right" width="8%">397</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.3389/fnins.2010.00198">The Berlin Brain–Computer Interface: Non-Medical Uses of BCI Technology</a><br><sub>B. Blankertz, M. Tangermann, C. Vidaurre, S. Fazli, C. Sannelli, S. Haufe, et al.</sub></td>
<td width="12%">2010<br>Frontiers in Neuroscience<br>395 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain–computer interfacing (BCI) is a steadily growing area of research.</td>
<td align="right" width="8%">395</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1088/0967-3334/25/4/003">On the suitability of near-infrared (NIR) systems for next-generation brain-computer interfaces.</a><br><sub>S. Coyle, T. Ward, C. Markham, G. McDarby</sub></td>
<td width="12%">2004<br>Physiological Measurement<br>394 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions On the suitability of near-infrared (NIR) systems for next-generation brain-computer interfaces. within General BCI Methods and Systems.</td>
<td align="right" width="8%">394</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1109/mc.2008.410">Brain-Computer Interfaces, Virtual Reality, and Videogames</a><br><sub>A. Lécuyer, F. Lotte, R. Reilly, R. Leeb, M. Hirose, M. Slater</sub></td>
<td width="12%">2008<br>Computer<br>390 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-Computer Interfaces, Virtual Reality, and Videogames within General BCI Methods and Systems.</td>
<td align="right" width="8%">390</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2003.814484">Linear and nonlinear methods for brain-computer interfaces</a><br><sub>K. Müller, Charles Anderson, G. Birch</sub></td>
<td width="12%">2003<br>IEEE transactions on neural systems and rehabilitation engineering<br>385 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Linear and nonlinear methods for brain-computer interfaces within General BCI Methods and Systems.</td>
<td align="right" width="8%">385</td>
<td width="24%">Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2016.2627016">Riemannian Approaches in Brain-Computer Interfaces: A Review</a><br><sub>F. Yger, Maxime Bérar, F. Lotte</sub></td>
<td width="12%">2017<br>IEEE transactions on neural systems and rehabilitation engineering<br>383 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Riemannian Approaches in Brain-Computer Interfaces: A Review within General BCI Methods and Systems.</td>
<td align="right" width="8%">383</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Broad BCI system claims often need stronger standardized evaluation across users, sessions, and devices.; Laboratory performance may not transfer to everyday usability, safety, and maintenance conditions.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 425 papers.</td>
</tr>
</tbody>
</table>

</details>

### SSVEP, P300, and ERP Spellers

- Papers selected: **391**
- Years covered: **2000-2026**
- Citation count in selected set: **52,869**
- Category Overview (main research trends):
  - Research is concentrating on high-speed, many-target communication systems with lower calibration burden and more stable target recognition.
  - Training-free and adaptive spatial filtering, task-discriminant component analysis, and deep neural decoders are prominent directions for SSVEP/P300 reliability.
  - Hybrid paradigms that combine SSVEP, P300, RSVP, EOG, or augmented/virtual reality interfaces are becoming a practical route to richer command sets.
- Limitations:
  - Visual fatigue, gaze dependence, and stimulus comfort remain practical barriers for long-duration communication use.
  - High-speed results often depend on controlled displays, known target layouts, and calibration conditions that may not transfer to daily use.
  - Hybrid paradigms improve command diversity but add setup complexity and make fair benchmarking harder.

<details>
<summary><strong>Show representative papers for SSVEP, P300, and ERP Spellers</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1109/86.847808">The mental prosthesis: assessing the speed of a P300-based brain-computer interface.</a><br><sub>E. Donchin, K. Spencer, R. Wijesinghe</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>1,299 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions The mental prosthesis: assessing the speed of a P300-based brain-computer interface. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">1,299</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2006.886577">Frequency Recognition Based on Canonical Correlation Analysis for SSVEP-Based BCIs</a><br><sub>Zhonglin Lin, Changshui Zhang, Wei Wu, Xiaorong Gao</sub></td>
<td width="12%">2006<br>IEEE Transactions on Biomedical Engineering<br>1,120 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Frequency Recognition Based on Canonical Correlation Analysis for SSVEP-Based BCIs within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">1,120</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jneumeth.2007.03.005">An efficient P300-based brain-computer interface for disabled subjects.</a><br><sub>Ulrich Hoffmann, J. Vesin, T. Ebrahimi, K. Diserens</sub></td>
<td width="12%">2008<br>Journal of Neuroscience Methods<br>944 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions An efficient P300-based brain-computer interface for disabled subjects. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">944</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2005.06.027">A P300-based brain-computer interface: initial tests by ALS patients.</a><br><sub>E. Sellers, E. Donchin</sub></td>
<td width="12%">2006<br>Clinical Neurophysiology<br>808 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A P300-based brain-computer interface: initial tests by ALS patients. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">808</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/6/4/046002">An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method</a><br><sub>Guangyu Bin, Xiaorong Gao, Zheng Yan, Bo Hong, Shangkai Gao</sub></td>
<td width="12%">2009<br>Journal of Neural Engineering<br>789 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">789</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.1109/tpami.2010.125">Convolutional Neural Networks for P300 Detection with Application to Brain-Computer Interfaces</a><br><sub>H. Cecotti, A. Gräser</sub></td>
<td width="12%">2011<br>IEEE Transactions on Pattern Analysis and Machine Intelligence<br>746 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Convolutional Neural Networks for P300 Detection with Application to Brain-Computer Interfaces within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">746</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/12/4/046008">Filter bank canonical correlation analysis for implementing a high-speed SSVEP-based brain–computer interface</a><br><sub>Xiaogang Chen, Yijun Wang, Shangkai Gao, T. Jung, Xiaorong Gao</sub></td>
<td width="12%">2015<br>Journal of Neural Engineering<br>723 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Filter bank canonical correlation analysis for implementing a high-speed SSVEP-based brain–computer interface within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">723</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2017.2694818">Enhancing Detection of SSVEPs for a High-Speed Brain Speller Using Task-Related Component Analysis</a><br><sub>M. Nakanishi, Yijun Wang, Xiaogang Chen, Yu-Te Wang, Xiaorong Gao, T. Jung</sub></td>
<td width="12%">2017<br>IEEE Transactions on Biomedical Engineering<br>691 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Objective: This study proposes and evaluates a novel data-driven spatial filtering approach for enhancing steady-state visual evoked potentials (SSVEPs) detection toward a high-speed brain-computer interface (BCI) speller.</td>
<td align="right" width="8%">691</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neulet.2009.06.045">How many people are able to control a P300-based brain-computer interface (BCI)?</a><br><sub>C. Guger, Shahab Daban, E. Sellers, C. Holzner, G. Krausz, R. Carabalona, et al.</sub></td>
<td width="12%">2009<br>Neuroscience Letters<br>688 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions How many people are able to control a P300-based brain-computer interface (BCI)? within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">688</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1155/2010/702357">A Survey of Stimulation Methods Used in SSVEP-Based BCIs</a><br><sub>Dan-hua Zhu, J. Bieger, G. G. Molina, Ronald M. Aarts</sub></td>
<td width="12%">2010<br>Computational Intelligence and Neuroscience<br>677 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Brain-computer interface (BCI) systems based on the steady-state visual evoked potential (SSVEP) provide higher information throughput and require shorter training than BCI systems using other brain signals.</td>
<td align="right" width="8%">677</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2008.03.034">A P300-based brain-computer interface for people with amyotrophic lateral sclerosis.</a><br><sub>F. Nijboer, E. Sellers, J. Mellinger, M. Jordan, Tamara Matuz, A. Furdea, et al.</sub></td>
<td width="12%">2008<br>Clinical Neurophysiology<br>666 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">666</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2007.897815">Control of an Electrical Prosthesis With an SSVEP-Based BCI</a><br><sub>G. Müller-Putz, G. Pfurtscheller</sub></td>
<td width="12%">2008<br>IEEE Transactions on Biomedical Engineering<br>610 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Control of an Electrical Prosthesis With an SSVEP-Based BCI within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">610</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2010.01.030">A novel P300-based brain-computer interface stimulus presentation paradigm: moving beyond rows and columns</a><br><sub>G. Townsend, B. LaPallo, C. Boulay, D. Krusienski, G. Frye, C. Hauser, et al.</sub></td>
<td width="12%">2010<br>Clinical Neurophysiology<br>587 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Objective An electroencephalographic brain-computer interface (BCI) can provide a non-muscular means of communication for people with amyotrophic lateral sclerosis (ALS) or other neuromuscular disorders.</td>
<td align="right" width="8%">587</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2006.889160">Multiple Channel Detection of Steady-State Visual Evoked Potentials for Brain-Computer Interfaces</a><br><sub>Ola Friman, Ivan Volosyak, A. Gräser</sub></td>
<td width="12%">2007<br>IEEE Transactions on Biomedical Engineering<br>568 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Multiple Channel Detection of Steady-State Visual Evoked Potentials for Brain-Computer Interfaces within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">568</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/2/4/008">Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components</a><br><sub>G. Müller-Putz, Reinhold Scherer, Christian Brauneis, G. Pfurtscheller</sub></td>
<td width="12%">2005<br>Journal of Neural Engineering<br>560 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">560</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1016/j.biopsycho.2006.04.007">A P300 event-related potential brain-computer interface (BCI): the effects of matrix size and inter stimulus interval on performance.</a><br><sub>E. Sellers, D. Krusienski, D. McFarland, T. Vaughan, J. Wolpaw</sub></td>
<td width="12%">2006<br>Biological Psychology<br>549 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A P300 event-related potential brain-computer interface (BCI): the effects of matrix size and inter stimulus interval on performance. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">549</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.826698">BCI competition 2003-data set IIb: support vector machines for the P300 speller paradigm</a><br><sub>M. Kaper, P. Meinicke, U. Großekathöfer, T. Lingner, H. Ritter</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>538 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions BCI competition 2003-data set IIb: support vector machines for the P300 speller paradigm within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">538</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2008.915728">BCI Competition III: Dataset II- Ensemble of SVMs for BCI P300 Speller</a><br><sub>A. Rakotomamonjy, Vincent Guigue</sub></td>
<td width="12%">2008<br>IEEE Transactions on Biomedical Engineering<br>535 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions BCI Competition III: Dataset II- Ensemble of SVMs for BCI P300 Speller within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">535</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1016/j.eij.2015.06.002">Brain computer interfacing: Applications and challenges</a><br><sub>Sarah N. Abdulkader, Ayman Atia, Mostafa-Sami M. Mostafa</sub></td>
<td width="12%">2015<br>Unknown venue<br>497 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Abstract Brain computer interface technology represents a highly growing field of research with application systems.</td>
<td align="right" width="8%">497</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2016.2627556">A Benchmark Dataset for SSVEP-Based Brain–Computer Interfaces</a><br><sub>Yijun Wang, Xiaogang Chen, Xiaorong Gao, Shangkai Gao</sub></td>
<td width="12%">2017<br>IEEE transactions on neural systems and rehabilitation engineering<br>443 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A Benchmark Dataset for SSVEP-Based Brain–Computer Interfaces within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">443</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1109/memb.2008.923958">Brain-Computer Interfaces Based on Visual Evoked Potentials</a><br><sub>Yijun Wang, Xiaorong Gao, Bo Hong, Chuan Jia, Shangkai Gao</sub></td>
<td width="12%">2008<br>IEEE Engineering in Medicine and Biology Magazine<br>428 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Brain-Computer Interfaces Based on Visual Evoked Potentials within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">428</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2004.841878">An improved P300-based brain-computer interface</a><br><sub>Hilit Serby, E. Yom-Tov, G. Inbar</sub></td>
<td width="12%">2005<br>IEEE transactions on neural systems and rehabilitation engineering<br>426 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions An improved P300-based brain-computer interface within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">426</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2013.2270283">A Hybrid BCI System Combining P300 and SSVEP and Its Application to Wheelchair Control</a><br><sub>Yuanqing Li, Jiahui Pan, Fei Wang, Z. Yu</sub></td>
<td width="12%">2013<br>IEEE Transactions on Biomedical Engineering<br>383 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A Hybrid BCI System Combining P300 and SSVEP and Its Application to Wheelchair Control within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">383</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2009.2039495">BCI Demographics: How Many (and What Kinds of) People Can Use an SSVEP BCI?</a><br><sub>B. Allison, T. Luth, Diana Valbuena, Amir Teymourian, Ivan Volosyak, A. Graser</sub></td>
<td width="12%">2010<br>IEEE transactions on neural systems and rehabilitation engineering<br>371 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions BCI Demographics: How Many (and What Kinds of) People Can Use an SSVEP BCI? within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">371</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1142/s0129065714500130">Frequency Recognition in SSVEP-Based BCI using Multiset Canonical Correlation Analysis</a><br><sub>Yu Zhang, Guoxu Zhou, Jing Jin, Xingyu Wang, A. Cichocki</sub></td>
<td width="12%">2013<br>International Journal of Neural Systems<br>362 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Canonical correlation analysis (CCA) has been one of the most popular methods for frequency recognition in steady-state visual evoked potential (SSVEP)-based brain-computer interfaces (BCIs).</td>
<td align="right" width="8%">362</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2005.07.024">P300-based brain computer interface: reliability and performance in healthy and paralysed participants.</a><br><sub>F. Piccione, F. Giorgi, Paolo Tonin, K. Priftis, S. Giove, S. Silvoni, et al.</sub></td>
<td width="12%">2006<br>Clinical Neurophysiology<br>362 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions P300-based brain computer interface: reliability and performance in healthy and paralysed participants. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">362</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2007.09.121">Towards an independent brain-computer interface using steady state visual evoked potentials.</a><br><sub>B. Allison, D. McFarland, G. Schalk, S. Zheng, M. Jackson, J. Wolpaw</sub></td>
<td width="12%">2008<br>Clinical Neurophysiology<br>353 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions Towards an independent brain-computer interface using steady state visual evoked potentials. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">353</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1371/journal.pone.0140703">A Comparison Study of Canonical Correlation Analysis Based Methods for Detecting Steady-State Visual Evoked Potentials</a><br><sub>M. Nakanishi, Yijun Wang, Yu-Te Wang, T. Jung, D. Yao</sub></td>
<td width="12%">2015<br>PLoS ONE<br>351 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Canonical correlation analysis (CCA) has been widely used in the detection of the steady-state visual evoked potentials (SSVEPs) in brain-computer interfaces (BCIs).</td>
<td align="right" width="8%">351</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1111/j.1469-8986.2008.00783.x">An auditory oddball (P300) spelling system for brain-computer interfaces.</a><br><sub>A. Furdea, Sebastian Halder, D. Krusienski, D. Bross, F. Nijboer, N. Birbaumer, et al.</sub></td>
<td width="12%">2009<br>Psychophysiology<br>345 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions An auditory oddball (P300) spelling system for brain-computer interfaces. within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">345</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1111/j.1749-6632.2008.04122.x">A Brain–Computer Interface Controlled Auditory Event‐Related Potential (P300) Spelling System for Locked‐In Patients</a><br><sub>A. Kübler, A. Furdea, Sebastian Halder, E. Hammer, F. Nijboer, B. Kotchoubey</sub></td>
<td width="12%">2009<br>Annals of the New York Academy of Sciences<br>333 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SSVEP" src="https://img.shields.io/badge/keyword-SSVEP-7c3aed"> <img alt="P300" src="https://img.shields.io/badge/keyword-P300-be123c"></td>
<td width="18%">Positions A Brain–Computer Interface Controlled Auditory Event‐Related Potential (P300) Spelling System for Locked‐In Patients within SSVEP, P300, and ERP Spellers.</td>
<td align="right" width="8%">333</td>
<td width="24%">Visual spellers can be constrained by gaze dependence, stimulus comfort, and fatigue during long sessions.; Controlled target layouts and calibration conditions may not transfer to everyday communication.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 391 papers.</td>
</tr>
</tbody>
</table>

</details>

### EEG Signal Processing and Datasets

- Papers selected: **265**
- Years covered: **2000-2026**
- Citation count in selected set: **28,640**
- Category Overview (main research trends):
  - This taxonomy emphasizes reproducible preprocessing, artifact handling, channel selection, spatial filtering, and benchmark datasets for EEG-based BCI.
  - The field is gradually shifting from isolated algorithm papers toward shared datasets, standardized evaluation, and metadata-aware comparisons.
  - Hybrid EEG/fNIRS, transfer learning, and open benchmark resources are recurring themes for improving generalization and clinical relevance.
- Limitations:
  - Benchmark datasets vary widely in task design, sensors, preprocessing, and participant populations.
  - Artifact handling, channel selection, and evaluation protocols are not standardized enough for simple leaderboard-style comparison.
  - Participant counts, trial structure, hardware, and licensing differences can limit reproducible reuse across laboratories.

<details>
<summary><strong>Show representative papers for EEG Signal Processing and Datasets</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2010.2082539">Regularizing Common Spatial Patterns to Improve BCI Designs: Unified Theory and New Algorithms</a><br><sub>F. Lotte, Cuntai Guan</sub></td>
<td width="12%">2011<br>IEEE Transactions on Biomedical Engineering<br>1,028 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">One of the most popular feature extraction algorithms for brain-computer interfaces (BCI) is common spatial patterns (CSPs).</td>
<td align="right" width="8%">1,028</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Benchmark value depends on standardized protocols, transparent splits, and external replication.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.826692">The BCI competition 2003: progress and perspectives in detection and discrimination of EEG single trials</a><br><sub>B. Blankertz, K. Müller, G. Curio, T. Vaughan, G. Schalk, J. Wolpaw, et al.</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>727 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions The BCI competition 2003: progress and perspectives in detection and discrimination of EEG single trials within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">727</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2006.10.019">EMG and EOG artifacts in brain computer interface systems: A survey.</a><br><sub>Mehrdad Fatourechi, Ali Bashashati, R. Ward, G. Birch</sub></td>
<td width="12%">2007<br>Clinical Neurophysiology<br>665 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions EMG and EOG artifacts in brain computer interface systems: A survey. within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">665</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1155/2011/130714">EEGLAB, SIFT, NFT, BCILAB, and ERICA: New Tools for Advanced EEG Processing</a><br><sub>A. Delorme, T. Mullen, C. Kothe, Z. Acar, Nima Bigdely Shamlo, A. Vankov, et al.</sub></td>
<td width="12%">2011<br>Computational Intelligence and Neuroscience<br>654 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">We describe a set of complementary EEG data collection and processing tools recently developed at the Swartz Center for Computational Neuroscience (SCCN) that connect to and extend the EEGLAB software environment, a freely available and readily extensible processing environment running under Matlab.</td>
<td align="right" width="8%">654</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/48fac6ee86f7cf8788acd2da8155a8dd47aa59fb">Enhanced performance by a hybrid NIRS – EEG brain computer interface</a><br><sub>S. Fazli, J. Mehnert, J. Steinbrink, G. Curio, A. Villringer, K. Müller, et al.</sub></td>
<td width="12%">2011<br>Unknown venue<br>584 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Enhanced performance by a hybrid NIRS – EEG brain computer interface within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">584</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2003.814481">How many people are able to operate an EEG-based brain-computer interface (BCI)?</a><br><sub>C. Guger, G. Edlinger, W. Harkam, I. Niedermayer, G. Pfurtscheller</sub></td>
<td width="12%">2003<br>IEEE transactions on neural systems and rehabilitation engineering<br>559 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions How many people are able to operate an EEG-based brain-computer interface (BCI)? within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">559</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/3/1/r02">Towards adaptive classification for BCI</a><br><sub>P. Shenoy, M. Krauledat, B. Blankertz, Rajesh P. N. Rao, K. Müller</sub></td>
<td width="12%">2006<br>Journal of Neural Engineering<br>483 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Towards adaptive classification for BCI within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">483</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neucom.2012.12.039">Classification of covariance matrices using a Riemannian-based kernel for BCI applications</a><br><sub>A. Barachant, S. Bonnet, M. Congedo, C. Jutten</sub></td>
<td width="12%">2013<br>Neurocomputing<br>482 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Classification of covariance matrices using a Riemannian-based kernel for BCI applications within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">482</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1016/s0278-2626(03)00036-8">Learning to control brain activity: a review of the production and control of EEG components for driving brain-computer interface (BCI) systems.</a><br><sub>Eleanor Curran, M. Stokes</sub></td>
<td width="12%">2003<br>Brain and Cognition<br>448 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Learning to control brain activity: a review of the production and control of EEG components for driving brain-computer interface (BCI) systems. within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">448</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2011.2131142">Optimizing the Channel Selection and Classification Accuracy in EEG-Based BCI</a><br><sub>M. Arvaneh, Cuntai Guan, K. Ang, Hiok Chai Quek</sub></td>
<td width="12%">2011<br>IEEE Transactions on Biomedical Engineering<br>435 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Optimizing the Channel Selection and Classification Accuracy in EEG-Based BCI within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">435</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.3389/fnbot.2020.00025">Current Status, Challenges, and Possible Solutions of EEG-Based Brain-Computer Interface: A Comprehensive Review</a><br><sub>M. Rashid, N. Sulaiman, A. P. Majeed, R. Musa, A. Nasir, Bifta Sama Bari, et al.</sub></td>
<td width="12%">2020<br>Frontiers in Neurorobotics<br>420 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Brain-Computer Interface (BCI), in essence, aims at controlling different assistive devices through the utilization of brain waves.</td>
<td align="right" width="8%">420</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/08f7fb99edd844aac90fccfa51f5d55cbdf15cbd">EURASIP Journal on Applied Signal Processing 2005:19, 3156–3164 c ○ 2005 Hindawi Publishing Corporation Steady-State VEP-Based Brain-Computer Interface Control in an Immersive 3D Gaming Environment</a><br><sub>Unknown authors</sub></td>
<td width="12%">2004<br>Unknown venue<br>408 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions EURASIP Journal on Applied Signal Processing 2005:19, 3156–3164 c ○ 2005 Hindawi Publishing Corporation Steady-State VEP-Based Brain-Computer Interface Control in an Immersive 3D Gaming Environment within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">408</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1109/86.895947">Real-time EEG analysis with subject-specific spatial patterns for a brain-computer interface (BCI).</a><br><sub>C. Guger, H. Ramoser, G. Pfurtscheller</sub></td>
<td width="12%">2000<br>IEEE transactions on rehabilitation engineering<br>407 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Real-time EEG analysis with subject-specific spatial patterns for a brain-computer interface (BCI). within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">407</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1080/2326263x.2017.1297192">Riemannian geometry for EEG-based brain-computer interfaces; a primer and a review</a><br><sub>M. Congedo, A. Barachant, R. Bhatia</sub></td>
<td width="12%">2017<br>Unknown venue<br>404 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Riemannian geometry for EEG-based brain-computer interfaces; a primer and a review within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">404</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1186/1743-0003-8-24">Brain-computer interfacing using modulations of alpha activity induced by covert shifts of attention</a><br><sub>M. Treder, Ali Bahramisharif, Nico M. Schmidt, Marcel A J van Gerven, B. Blankertz</sub></td>
<td width="12%">2011<br>Journal of NeuroEngineering and Rehabilitation<br>366 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">BackgroundVisual brain-computer interfaces (BCIs) often yield high performance only when targets are fixated with the eyes.</td>
<td align="right" width="8%">366</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1016/j.measurement.2007.07.007">EEG feature extraction based on wavelet packet decomposition for brain computer interface</a><br><sub>Wu Ting, Guo-zheng Yan, Banghua Yang, Sun Hong</sub></td>
<td width="12%">2008<br>Unknown venue<br>366 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions EEG feature extraction based on wavelet packet decomposition for brain computer interface within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">366</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2006.875557">The Berlin brain-computer interface: EEG-based communication without subject training</a><br><sub>B. Blankertz, G. Dornhege, M. Krauledat, K. Müller, V. Kunzmann, F. Losch, et al.</sub></td>
<td width="12%">2006<br>IEEE transactions on neural systems and rehabilitation engineering<br>361 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions The Berlin brain-computer interface: EEG-based communication without subject training within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">361</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1109/7333.918276">Rapid prototyping of an EEG-based brain-computer interface (BCI)</a><br><sub>C. Guger, A. Schlögl, C. Neuper, D. Walterspacher, Thomas Strein, G. Pfurtscheller</sub></td>
<td width="12%">2001<br>IEEE transactions on neural systems and rehabilitation engineering<br>344 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Rapid prototyping of an EEG-based brain-computer interface (BCI) within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">344</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neunet.2009.07.020">Time Domain Parameters as a feature for EEG-based Brain-Computer Interfaces</a><br><sub>C. Vidaurre, Nicole Krämer, B. Blankertz, A. Schlögl</sub></td>
<td width="12%">2009<br>Neural Networks<br>319 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Time Domain Parameters as a feature for EEG-based Brain-Computer Interfaces within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">319</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2010.2082540">Regularized Common Spatial Pattern With Aggregation for EEG Classification in Small-Sample Setting</a><br><sub>Haiping Lu, H. Eng, Cuntai Guan, K. Plataniotis, A. Venetsanopoulos</sub></td>
<td width="12%">2010<br>IEEE Transactions on Biomedical Engineering<br>315 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Common spatial pattern (CSP) is a popular algorithm for classifying electroencephalogram (EEG) signals in the context of brain-computer interfaces (BCIs).</td>
<td align="right" width="8%">315</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1016/j.bspc.2016.09.005">Trends in EEG-BCI for daily-life: Requirements for artifact removal</a><br><sub>Jesús Minguillón, M. A. Lopez-Gordo, F. Pelayo</sub></td>
<td width="12%">2017<br>Biomedical Signal Processing and Control<br>269 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Trends in EEG-BCI for daily-life: Requirements for artifact removal within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">269</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/8/2/025008">Bristle-sensors—low-cost flexible passive dry EEG electrodes for neurofeedback and BCI applications</a><br><sub>C. Grozea, C. Voinescu, S. Fazli</sub></td>
<td width="12%">2011<br>Journal of Neural Engineering<br>261 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Bristle-sensors—low-cost flexible passive dry EEG electrodes for neurofeedback and BCI applications within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">261</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1371/journal.pone.0002967">Towards Zero Training for Brain-Computer Interfacing</a><br><sub>M. Krauledat, M. Tangermann, B. Blankertz, K. Müller</sub></td>
<td width="12%">2008<br>PLoS ONE<br>255 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Electroencephalogram (EEG) signals are highly subject-specific and vary considerably even between recording sessions of the same user within the same experimental paradigm.</td>
<td align="right" width="8%">255</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1007/978-3-642-15995-4_78">Riemannian Geometry Applied to BCI Classification</a><br><sub>A. Barachant, S. Bonnet, M. Congedo, C. Jutten</sub></td>
<td width="12%">2010<br>Latent Variable Analysis and Signal Separation<br>252 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Riemannian Geometry Applied to BCI Classification within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">252</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1080/10447318.2013.780869">EEG-Based Brain-Computer Interfaces: A Thorough Literature Survey</a><br><sub>Han-Jeong Hwang, Soyoun Kim, S. Choi, C. Im</sub></td>
<td width="12%">2013<br>International journal of human computer interactions<br>249 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions EEG-Based Brain-Computer Interfaces: A Thorough Literature Survey within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">249</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2006.875637">BCI meeting 2005-workshop on BCI signal processing: feature extraction and translation</a><br><sub>D. McFarland, Charles Anderson, K. Müller, A. Schlögl, D. Krusienski</sub></td>
<td width="12%">2006<br>IEEE transactions on neural systems and rehabilitation engineering<br>242 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions BCI meeting 2005-workshop on BCI signal processing: feature extraction and translation within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">242</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1016/j.eswa.2017.12.015">Multi-kernel extreme learning machine for EEG classification in brain-computer interfaces</a><br><sub>Yu Zhang, Yu Wang, Guoxu Zhou, Jing Jin, Bei Wang, Xingyu Wang, et al.</sub></td>
<td width="12%">2018<br>Expert systems with applications<br>242 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Multi-kernel extreme learning machine for EEG classification in brain-computer interfaces within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">242</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1007/s11831-021-09684-6">Review of Machine Learning Techniques for EEG Based Brain Computer Interface</a><br><sub>Swati Aggarwal, Nupur Chugh</sub></td>
<td width="12%">2022<br>Archives of Computational Methods in Engineering<br>233 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Review of Machine Learning Techniques for EEG Based Brain Computer Interface within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">233</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1016/j.ins.2007.11.012">Classifying mental tasks based on features of higher-order statistics from EEG signals in brain-computer interface</a><br><sub>Shang-Ming Zhou, J. Q. Gan, F. Sepulveda</sub></td>
<td width="12%">2008<br>Information Sciences<br>228 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Classifying mental tasks based on features of higher-order statistics from EEG signals in brain-computer interface within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">228</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2012.2190299">Electroencephalography (EEG)-Based Brain–Computer Interface (BCI): A 2-D Virtual Wheelchair Control Based on Event-Related Desynchronization/Synchronization and State Control</a><br><sub>Dandan Huang, Kai Qian, D. Fei, Wenchuan Jia, Xuedong Chen, O. Bai</sub></td>
<td width="12%">2012<br>IEEE transactions on neural systems and rehabilitation engineering<br>224 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Electroencephalography (EEG)-Based Brain–Computer Interface (BCI): A 2-D Virtual Wheelchair Control Based on Event-Related Desynchronization/Synchronization and State Control within EEG Signal Processing and Datasets.</td>
<td align="right" width="8%">224</td>
<td width="24%">Dataset and preprocessing choices can bias comparisons across algorithms and laboratories.; Artifact robustness and sensor-setup variability need stronger external validation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 265 papers.</td>
</tr>
</tbody>
</table>

</details>

### Invasive and Implantable Interfaces

- Papers selected: **135**
- Years covered: **2003-2026**
- Citation count in selected set: **14,406**
- Category Overview (main research trends):
  - Invasive BCI research is shifting toward high-bandwidth, stable, long-term decoding for movement, communication, and sensory feedback.
  - Key engineering themes include wireless operation, power efficiency, signal longevity, surgical risk, and reliability outside tightly controlled laboratory sessions.
  - Clinical translation is increasingly tied to home use, user safety, tactile feedback, speech decoding, and realistic functional tasks.
- Limitations:
  - Surgical risk, long-term signal stability, device maintenance, and participant burden remain major translation barriers.
  - Many studies involve small cohorts or case reports, so headline performance can be difficult to generalize.
  - Home deployment, cybersecurity, informed consent, explantation, and support infrastructure remain difficult to evaluate consistently.

<details>
<summary><strong>Show representative papers for Invasive and Implantable Interfaces</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neuroimage.2007.01.051">The non-invasive Berlin Brain-Computer Interface: Fast acquisition of effective performance in untrained subjects</a><br><sub>B. Blankertz, G. Dornhege, M. Krauledat, K. Müller, G. Curio</sub></td>
<td width="12%">2007<br>NeuroImage<br>1,003 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions The non-invasive Berlin Brain-Computer Interface: Fast acquisition of effective performance in untrained subjects within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">1,003</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1016/j.clinph.2008.06.001">A brain-actuated wheelchair: asynchronous and non-invasive Brain-computer interfaces for continuous control of robots.</a><br><sub>F. Galán, F. Galán, M. Nuttin, Eileen Lew, P. Ferrez, G. Vanacker, et al.</sub></td>
<td width="12%">2008<br>Clinical Neurophysiology<br>703 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A brain-actuated wheelchair: asynchronous and non-invasive Brain-computer interfaces for continuous control of robots. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">703</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/10/6/066014">Failure mode analysis of silicon-based intracortical microelectrode arrays in non-human primates</a><br><sub>James C. Barrese, Naveen G. Rao, Kaivon Paroo, C. Triebwasser, C. Vargas-Irwin, Lachlan Franquemont, et al.</sub></td>
<td width="12%">2013<br>Journal of Neural Engineering<br>569 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"></td>
<td width="18%">Positions Failure mode analysis of silicon-based intracortical microelectrode arrays in non-human primates within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">569</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1016/s0079-6123(06)59019-3">High-frequency gamma oscillations and human brain mapping with electrocorticography.</a><br><sub>N. Crone, A. Sinai, Anna Korzeniewska</sub></td>
<td width="12%">2006<br>Progress in Brain Research<br>507 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions High-frequency gamma oscillations and human brain mapping with electrocorticography. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">507</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1056/nejmoa1608085">Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS.</a><br><sub>M. Vansteensel, Elmar G. M. Pels, M. Bleichner, M. Branco, T. Denison, Z. Freudenburg, et al.</sub></td>
<td width="12%">2016<br>New England Journal of Medicine<br>490 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Fully Implanted Brain-Computer Interface in a Locked-In Patient with ALS. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">490</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.1109/jssc.2014.2364824">A Minimally Invasive 64-Channel Wireless μECoG Implant</a><br><sub>R. Muller, Hanh-Phuc Le, Wen Li, P. Ledochowitsch, S. Gambini, T. Björninen, et al.</sub></td>
<td width="12%">2015<br>IEEE Journal of Solid-State Circuits<br>352 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Emerging applications in brain-machine interface systems require high-resolution, chronic multisite cortical recordings, which cannot be obtained with existing technologies due to high power consumption, high invasiveness, or inability to transmit data wirelessly.</td>
<td align="right" width="8%">352</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1016/j.brainresbull.2008.01.007">Non-invasive brain-computer interface system: towards its application as assistive technology.</a><br><sub>F. Cincotti, D. Mattia, F. Aloise, S. Bufalari, G. Schalk, G. Oriolo, et al.</sub></td>
<td width="12%">2008<br>Brain Research Bulletin<br>339 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Non-invasive brain-computer interface system: towards its application as assistive technology. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">339</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.3389/fnhum.2013.00568">Flaws in current human training protocols for spontaneous Brain-Computer Interfaces: lessons learned from instructional design</a><br><sub>F. Lotte, F. Larrue, C. Mühl</sub></td>
<td width="12%">2013<br>Frontiers in Human Neuroscience<br>302 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">While recent research on Brain-Computer Interfaces (BCI) has highlighted their potential for many applications, they remain barely used outside laboratories.</td>
<td align="right" width="8%">302</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.3389/fnins.2014.00208">Errare machinale est: the use of error-related potentials in brain-machine interfaces</a><br><sub>Ricardo Chavarriaga, A. Sobolewski, J. Millán</sub></td>
<td width="12%">2014<br>Frontiers in Neuroscience<br>289 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">The ability to recognize errors is crucial for efficient behavior.</td>
<td align="right" width="8%">289</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2010.2053387">Learning From EEG Error-Related Potentials in Noninvasive Brain-Computer Interfaces</a><br><sub>Ricardo Chavarriaga, J. del R. Millán</sub></td>
<td width="12%">2010<br>IEEE transactions on neural systems and rehabilitation engineering<br>275 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">We describe error-related potentials generated while a human user monitors the performance of an external agent and discuss their use for a new type of brain-computer interaction.</td>
<td align="right" width="8%">275</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1016/j.biomaterials.2013.03.007">The impact of chronic blood-brain barrier breach on intracortical electrode function.</a><br><sub>Tarun Saxena, Lohitash Karumbaiah, Eric A Gaupp, Radhika Patkar, K. Patil, Martha I. Betancur, et al.</sub></td>
<td width="12%">2013<br>Biomaterials<br>265 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions The impact of chronic blood-brain barrier breach on intracortical electrode function. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">265</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.3390/app7121239">Review and Classification of Emotion Recognition Based on EEG Brain-Computer Interface System Research: A Systematic Review</a><br><sub>Abeer Al-Nafjan, M. Hosny, Y. Al-Ohali, A. Al-Wabil</sub></td>
<td width="12%">2017<br>Unknown venue<br>260 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Recent developments and studies in brain-computer interface (BCI) technologies have facilitated emotion detection and classification.</td>
<td align="right" width="8%">260</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.7554/elife.32904">Proprioceptive and cutaneous sensations in humans elicited by intracortical microstimulation</a><br><sub>M. Armenta Salas, L. Bashford, S. Kellis, M. Jafari, HyeongChan Jo, Daniel R. Kramer, et al.</sub></td>
<td width="12%">2018<br>eLife<br>228 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Pioneering work with nonhuman primates and recent human studies established intracortical microstimulation (ICMS) in primary somatosensory cortex (S1) as a method of inducing discriminable artificial sensation.</td>
<td align="right" width="8%">228</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1152/jn.00104.2011">Neural decoding of treadmill walking from noninvasive electroencephalographic signals.</a><br><sub>A. Presacco, Ronald N. Goodman, L. Forrester, J. Contreras-Vidal</sub></td>
<td width="12%">2011<br>Journal of Neurophysiology<br>206 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Neural decoding of treadmill walking from noninvasive electroencephalographic signals. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">206</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1007/978-1-4471-6584-2_7">A Tutorial on EEG Signal Processing Techniques for Mental State Recognition in Brain-Computer Interfaces</a><br><sub>F. Lotte</sub></td>
<td width="12%">2014<br>Unknown venue<br>198 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A Tutorial on EEG Signal Processing Techniques for Mental State Recognition in Brain-Computer Interfaces within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">198</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.2307/j.ctt9qh0x7.26">Neural Dust: An Ultrasonic, Low Power Solution for Chronic Brain-Machine Interfaces</a><br><sub>D. Seo, J. Carmena, J. Rabaey, E. Alon, M. Maharbiz</sub></td>
<td width="12%">2013<br>Unknown venue<br>197 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">zJoint senior authors A major hurdle in brain-machine interfaces (BMI) is the lack of an implantable neural interface system that remains viable for a lifetime.</td>
<td align="right" width="8%">197</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/e075fb346b31e19296537664f3a137dde765eb93">Methods Towards Invasive Human Brain Computer Interfaces</a><br><sub>T. N. Lal, T. Hinterberger, G. Widman, M. Schröder, J. Hill, W. Rosenstiel, et al.</sub></td>
<td width="12%">2004<br>Neural Information Processing Systems<br>197 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Methods Towards Invasive Human Brain Computer Interfaces within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">197</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2006.875570">ECoG factors underlying multimodal control of a brain-computer interface</a><br><sub>J. A. Wilson, Elizabeth A Felton, P. C. Garell, G. Schalk, Justin C. Williams</sub></td>
<td width="12%">2006<br>IEEE transactions on neural systems and rehabilitation engineering<br>191 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions ECoG factors underlying multimodal control of a brain-computer interface within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">191</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1038/srep33526">Flexible Neural Electrode Array Based-on Porous Graphene for Cortical Microstimulation and Sensing</a><br><sub>Yichen Lu, H. Lyu, Andrew G. Richardson, T. Lucas, D. Kuzum</sub></td>
<td width="12%">2016<br>Scientific Reports<br>185 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Neural sensing and stimulation have been the backbone of neuroscience research, brain-machine interfaces and clinical neuromodulation therapies for decades.</td>
<td align="right" width="8%">185</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jphysparis.2011.08.003">Spelling with non-invasive Brain-Computer Interfaces--current and future trends.</a><br><sub>H. Cecotti</sub></td>
<td width="12%">2011<br>Journal of Physiology - Paris<br>181 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Spelling with non-invasive Brain-Computer Interfaces--current and future trends. within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">181</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/9/2/026027">A recurrent neural network for closed-loop intracortical brain–machine interface decoders</a><br><sub>David Sussillo, Paul Nuyujukian, Joline M. Fan, J. Kao, S. Stavisky, S. Ryu, et al.</sub></td>
<td width="12%">2012<br>Journal of Neural Engineering<br>176 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions A recurrent neural network for closed-loop intracortical brain–machine interface decoders within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">176</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2004.838443">Phase synchronization for the recognition of mental tasks in a brain-computer interface</a><br><sub>E. Gysels, P. Celka</sub></td>
<td width="12%">2004<br>IEEE transactions on neural systems and rehabilitation engineering<br>175 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions Phase synchronization for the recognition of mental tasks in a brain-computer interface within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">175</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1038/s41467-021-27725-3">Imagined speech can be decoded from low- and cross-frequency intracranial EEG features</a><br><sub>Timothée Proix, Jaime F. Delgado Saa, Andy Christen, Stéphanie Martin, Brian N. Pasley, R. Knight, et al.</sub></td>
<td width="12%">2022<br>Nature Communications<br>175 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Reconstructing intended speech from neural activity using brain-computer interfaces holds great promises for people with severe speech production deficits.</td>
<td align="right" width="8%">175</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/8/2/025002">Critical issues in state-of-the-art brain–computer interface signal processing</a><br><sub>D. Krusienski, M. Grosse-Wentrup, F. Galán, D. Coyle, K. Miller, E. Forney, et al.</sub></td>
<td width="12%">2011<br>Journal of Neural Engineering<br>175 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">This paper reviews several critical issues facing signal processing for brain–computer interfaces (BCIs) and suggests several recent approaches that should be further examined.</td>
<td align="right" width="8%">175</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1109/jssc.2011.2108770">A Battery-Powered Activity-Dependent Intracortical Microstimulation IC for Brain-Machine-Brain Interface</a><br><sub>M. Azin, D. Guggenmos, S. Barbay, R. Nudo, P. Mohseni</sub></td>
<td width="12%">2011<br>IEEE Journal of Solid-State Circuits<br>172 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions A Battery-Powered Activity-Dependent Intracortical Microstimulation IC for Brain-Machine-Brain Interface within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">172</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.48550/arxiv.2308.13234">Decoding Natural Images from EEG for Object Recognition</a><br><sub>Yonghao Song, Bingchuan Liu, Xiang Li, Nanlin Shi, Yijun Wang, Xiaorong Gao</sub></td>
<td width="12%">2023<br>International Conference on Learning Representations<br>147 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Electroencephalography (EEG) signals, known for convenient non-invasive acquisition but low signal-to-noise ratio, have recently gained substantial attention due to the potential to decode natural images.</td>
<td align="right" width="8%">147</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://arxiv.org/abs/1905.04149">A Survey on Deep Learning based Brain Computer Interface: Recent Advances and New Frontiers</a><br><sub>Xiang Zhang, Lina Yao, Xianzhi Wang, Jessica J. M. Monaghan, D. McAlpine</sub></td>
<td width="12%">2019<br>arXiv.org<br>147 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain-Computer Interface (BCI) bridges the human&#x27;s neural world and the outer physical world by decoding individuals&#x27; brain signals into commands recognizable by computer devices.</td>
<td align="right" width="8%">147</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1109/is.2018.8710576">A Study on Mental State Classification using EEG-based Brain-Machine Interface</a><br><sub>Jordan J. Bird, Luis J. Manso, E. P. Ribeiro, Anikó Ekárt, D. Faria</sub></td>
<td width="12%">2018<br>2018 International Conference on Intelligent Systems (IS)<br>143 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">This work aims to find discriminative EEG-based features and appropriate classification methods that can categorise brainwave patterns based on their level of activity or frequency for mental state recognition useful for human-machine interaction.</td>
<td align="right" width="8%">143</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/4f73e04a88b1a2093c300b071650cecd96a7954d">Playing Pinball with non-invasive BCI</a><br><sub>M. Tangermann, M. Krauledat, K. Grzeska, M. Sagebaum, B. Blankertz, C. Vidaurre, et al.</sub></td>
<td width="12%">2008<br>Neural Information Processing Systems<br>143 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Playing Pinball with non-invasive BCI within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">143</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2552/aa9ee7">Rapid calibration of an intracortical brain–computer interface for people with tetraplegia</a><br><sub>D. M. Brandman, Tommy Hosman, J. Saab, Michael C. Burkhart, Benjamin E Shanahan, John G. Ciancibello, et al.</sub></td>
<td width="12%">2018<br>Journal of Neural Engineering<br>137 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"></td>
<td width="18%">Positions Rapid calibration of an intracortical brain–computer interface for people with tetraplegia within Invasive and Implantable Interfaces.</td>
<td align="right" width="8%">137</td>
<td width="24%">Surgical risk, device durability, and long-term signal stability constrain clinical translation.; Small participant cohorts make headline decoding performance difficult to generalize.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 135 papers.</td>
</tr>
</tbody>
</table>

</details>

### Rehabilitation and Neuroprosthetics

- Papers selected: **87**
- Years covered: **2000-2026**
- Citation count in selected set: **11,970**
- Category Overview (main research trends):
  - The dominant trend is integration of BCI with robotic gloves, exoskeletons, FES, VR, and task-oriented therapy for post-stroke and motor impairment rehabilitation.
  - Studies increasingly ask whether BCI training transfers to activities of daily living rather than only improving offline decoding accuracy.
  - Recent work points toward home-use, patient-centered protocols, multimodal feedback, and combined motor-cognitive-affective rehabilitation.
- Limitations:
  - Clinical evidence is often fragmented across small cohorts, heterogeneous protocols, and short follow-up windows.
  - Improvements in decoder accuracy or therapy-session metrics do not always demonstrate transfer to activities of daily living.
  - Patient selection, therapist involvement, adverse-event reporting, and outcome measures vary enough to limit direct comparison.

<details>
<summary><strong>Show representative papers for Rehabilitation and Neuroprosthetics</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1016/s1474-4422(08)70223-0">Brain-computer interfaces in neurological rehabilitation.</a><br><sub>J. Daly, J. Wolpaw</sub></td>
<td width="12%">2008<br>Lancet Neurology<br>1,144 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-computer interfaces in neurological rehabilitation. within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">1,144</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.3390/s120201211">Brain Computer Interfaces, a Review</a><br><sub>Luis F. Nicolás-Alonso, J. G. Gil</sub></td>
<td width="12%">2012<br>Italian National Conference on Sensors<br>1,125 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">A brain-computer interface (BCI) is a hardware and software communications system that permits cerebral activity alone to control computers or external devices.</td>
<td align="right" width="8%">1,125</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1161/strokeaha.107.505313">Think to Move: a Neuromagnetic Brain-Computer Interface (BCI) System for Chronic Stroke</a><br><sub>Ethan R. Buch, Cornelia Weber, L. Cohen, C. Braun, M. Dimyan, T. Ard, et al.</sub></td>
<td width="12%">2008<br>Stroke<br>619 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Think to Move: a Neuromagnetic Brain-Computer Interface (BCI) System for Chronic Stroke within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">619</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1152/physrev.00027.2016">Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation.</a><br><sub>M. Lebedev, M. Nicolelis</sub></td>
<td width="12%">2017<br>Physiological Reviews<br>555 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Machine Interfaces: From Basic Science to Neuroprostheses and Neurorehabilitation. within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">555</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1038/srep38565">Noninvasive Electroencephalogram Based Control of a Robotic Arm for Reach and Grasp Tasks</a><br><sub>Jianjun Meng, Shuying Zhang, Angeliki Bekyo, Jaron Olsoe, Bryan S. Baxter, Bin He</sub></td>
<td width="12%">2016<br>Scientific Reports<br>447 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Brain-computer interface (BCI) technologies aim to provide a bridge between the human brain and external devices.</td>
<td align="right" width="8%">447</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.3389/fnsys.2021.578875">Progress in Brain Computer Interface: Challenges and Opportunities</a><br><sub>S. Saha, K. Mamun, K. Ahmed, R. Mostafa, G. Naik, A. Khandoker, et al.</sub></td>
<td width="12%">2019<br>Frontiers in Systems Neuroscience<br>328 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain computer interfaces (BCI) provide a direct communication link between the brain and a computer or other external devices.</td>
<td align="right" width="8%">328</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1016/j.cobme.2017.11.004">EEG-Based Brain-Computer Interfaces</a><br><sub>D. McFarland, J. Wolpaw</sub></td>
<td width="12%">2017<br>Current Opinion in Biomedical Engineering<br>317 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain-Computer Interfaces (BCIs) are real-time computer-based systems that translate brain signals into useful commands.</td>
<td align="right" width="8%">317</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Offline benchmark performance may not transfer to real-time closed-loop use.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1038/s41586-023-06377-x">A high-performance speech neuroprosthesis</a><br><sub>Francis R. Willett, Erin M. Kunz, Chaofei Fan, Donald T. Avansino, G. Wilson, Eun Young Choi, et al.</sub></td>
<td width="12%">2023<br>Nature<br>292 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Speech brain–computer interfaces (BCIs) have the potential to restore rapid communication to people with paralysis by decoding neural activity evoked by attempted speech into text^ 1 , 2 or sound^ 3 , 4 .</td>
<td align="right" width="8%">292</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1186/1743-0003-9-5">Gaming control using a wearable and wireless EEG-based brain-computer interface device with novel dry foam-based sensors</a><br><sub>Lun-De Liao, Chi-Yu Chen, I-Jan Wang, Sheng-Fu Chen, Shih-Yu Li, Bo-Wei Chen, et al.</sub></td>
<td width="12%">2012<br>Journal of NeuroEngineering and Rehabilitation<br>270 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">A brain-computer interface (BCI) is a communication system that can help users interact with the outside environment by translating brain signals into machine commands.</td>
<td align="right" width="8%">270</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1152/jn.00918.2015">Efficient neuroplasticity induction in chronic stroke patients by an associative brain-computer interface.</a><br><sub>N. Mrachacz‐Kersting, N. Jiang, A. J. T. Stevenson, I. Niazi, V. Kostic, A. Pavlovic, et al.</sub></td>
<td width="12%">2016<br>Journal of Neurophysiology<br>240 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Efficient neuroplasticity induction in chronic stroke patients by an associative brain-computer interface. within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">240</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1109/mc.2008.432">Rehabilitation with Brain-Computer Interface Systems</a><br><sub>G. Pfurtscheller, G. Müller-Putz, Reinhold Scherer, C. Neuper</sub></td>
<td width="12%">2008<br>Computer<br>235 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Rehabilitation with Brain-Computer Interface Systems within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">235</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2010.2077654">EEG Control of a Virtual Helicopter in 3-Dimensional Space Using Intelligent Control Strategies</a><br><sub>Audrey S. Royer, A. Doud, Minn L. Rose, B. He</sub></td>
<td width="12%">2010<br>IEEE transactions on neural systems and rehabilitation engineering<br>232 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Films like Firefox, Surrogates, and Avatar have explored the possibilities of using brain-computer interfaces (BCIs) to control machines and replacement bodies with only thought.</td>
<td align="right" width="8%">232</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1177/155005941104200410">Brain-Computer Interface in Stroke: A Review of Progress</a><br><sub>S. Silvoni, A. Ramos-Murguialday, M. Cavinato, C. Volpato, Giulia Cisotto, A. Turolla, et al.</sub></td>
<td width="12%">2011<br>Clinical EEG and Neuroscience<br>227 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Computer Interface in Stroke: A Review of Progress within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">227</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1109/tsmcc.2012.2226444">A New Gaze-BCI-Driven Control of an Upper Limb Exoskeleton for Rehabilitation in Real-World Tasks</a><br><sub>A. Frisoli, Claudio Loconsole, D. Leonardis, F. Banno, M. Barsotti, C. Chisari, et al.</sub></td>
<td width="12%">2012<br>IEEE Transactions on Systems Man and Cybernetics Part C (Applications and Reviews)<br>219 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions A New Gaze-BCI-Driven Control of an Upper Limb Exoskeleton for Rehabilitation in Real-World Tasks within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">219</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.5626/jcse.2013.7.2.139">Brain-Computer Interface in Stroke Rehabilitation</a><br><sub>K. Ang, Cuntai Guan</sub></td>
<td width="12%">2013<br>Journal of Computing Science and Engineering<br>217 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Computer Interface in Stroke Rehabilitation within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">217</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1177/1545968310368683">Combination of Brain-Computer Interface Training and Goal-Directed Physical Therapy in Chronic Stroke: A Case Report</a><br><sub>D. Broetz, C. Braun, Cornelia Weber, S. Soekadar, A. Caria, N. Birbaumer</sub></td>
<td width="12%">2010<br>Neurorehabilitation and Neural Repair<br>216 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Combination of Brain-Computer Interface Training and Goal-Directed Physical Therapy in Chronic Stroke: A Case Report within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">216</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1038/s41598-018-37359-z">Towards reconstructing intelligible speech from the human auditory cortex</a><br><sub>Hassan Akbari, B. Khalighinejad, J. Herrero, A. Mehta, N. Mesgarani</sub></td>
<td width="12%">2018<br>Scientific Reports<br>210 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Auditory stimulus reconstruction is a technique that finds the best approximation of the acoustic stimulus from the population of evoked neural activity.</td>
<td align="right" width="8%">210</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1109/mc.2008.409">Brain-Computer Interface Operation of Robotic and Prosthetic Devices</a><br><sub>D. McFarland, J. Wolpaw</sub></td>
<td width="12%">2008<br>Computer<br>204 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Computer Interface Operation of Robotic and Prosthetic Devices within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">204</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/3759c8b09acff0ed5ed197794a6bc1eba67e9b3e">Journal of Neuroengineering and Rehabilitation Open Access a Brain-computer Interface with Vibrotactile Biofeedback for Haptic Information</a><br><sub>A. Chatterjee, V. Aggarwal, A. Ramos, S. Acharya, N. Thakor</sub></td>
<td width="12%">2007<br>Unknown venue<br>201 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Journal of Neuroengineering and Rehabilitation Open Access a Brain-computer Interface with Vibrotactile Biofeedback for Haptic Information within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">201</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neunet.2009.05.009">Hemodynamic brain-computer interfaces for communication and rehabilitation</a><br><sub>R. Sitaram, A. Caria, N. Birbaumer</sub></td>
<td width="12%">2009<br>Neural Networks<br>185 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Hemodynamic brain-computer interfaces for communication and rehabilitation within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">185</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1016/j.artmed.2013.07.004">Hybrid brain-computer interfaces and hybrid neuroprostheses for restoration of upper limb functions in individuals with high-level spinal cord injury</a><br><sub>M. Rohm, M. Schneiders, C. Müller, A. Kreilinger, V. Kaiser, G. Müller-Putz, et al.</sub></td>
<td width="12%">2013<br>Artif. Intell. Medicine<br>182 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions Hybrid brain-computer interfaces and hybrid neuroprostheses for restoration of upper limb functions in individuals with high-level spinal cord injury within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">182</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1111/j.1469-8986.2010.01117.x">Chronic stroke recovery after combined BCI training and physiotherapy: a case report.</a><br><sub>A. Caria, Cornelia Weber, D. Brötz, A. Ramos, L. Ticini, A. Gharabaghi, et al.</sub></td>
<td width="12%">2011<br>Psychophysiology<br>182 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Chronic stroke recovery after combined BCI training and physiotherapy: a case report. within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">182</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1016/j.rehab.2014.09.016">Brain computer interfaces for neurorehabilitation – its current status as a rehabilitation strategy post-stroke.</a><br><sub>L. Dokkum, Tomas E. Ward, I. Laffont</sub></td>
<td width="12%">2015<br>Annals of Physical and Rehabilitation Medicine<br>168 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain computer interfaces for neurorehabilitation – its current status as a rehabilitation strategy post-stroke. within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">168</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1101/2023.12.26.23300110">An accurate and rapidly calibrating speech neuroprosthesis</a><br><sub>N. Card, M. Wairagkar, Carrina Iacobacci, Xianda Hou, Tyler Singer-Clark, Francis R. Willett, et al.</sub></td>
<td width="12%">2023<br>medRxiv<br>143 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain-computer interfaces (BCIs) can provide a rapid, intuitive way for people with paralysis to communicate by transforming the cortical activity associated with attempted speech into text.</td>
<td align="right" width="8%">143</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Offline benchmark performance may not transfer to real-time closed-loop use.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1126/sciadv.1600889">Implantable microcoils for intracortical magnetic stimulation</a><br><sub>Seung Woo Lee, F. Fallegger, B. Casse, S. Fried</sub></td>
<td width="12%">2016<br>Science Advances<br>139 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Magnetic stimulation from cortically implantable microcoils can activate neuronal circuits with high selectivity and reliability.</td>
<td align="right" width="8%">139</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Surgical risk, device durability, and long-term signal stability constrain clinical translation.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2006.875547">The neurochip BCI: towards a neural prosthesis for upper limb function</a><br><sub>Andrew Jackson, C. Moritz, J. Mavoori, Timothy H. Lucas, Eberhard E. Fetz</sub></td>
<td width="12%">2006<br>IEEE transactions on neural systems and rehabilitation engineering<br>135 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions The neurochip BCI: towards a neural prosthesis for upper limb function within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">135</td>
<td width="24%">Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.3109/17483107.2014.961569">Application of BCI systems in neurorehabilitation: a scoping review</a><br><sub>M. Bamdad, Homayoon Zarshenas, M. Auais</sub></td>
<td width="12%">2015<br>Disability and Rehabilitation: Assistive Technology<br>135 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Application of BCI systems in neurorehabilitation: a scoping review within Rehabilitation and Neuroprosthetics.</td>
<td align="right" width="8%">135</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1007/s12152-011-9132-6">The Asilomar Survey: Stakeholders’ Opinions on Ethical Issues Related to Brain-Computer Interfacing</a><br><sub>F. Nijboer, J. Clausen, B. Allison, Pim Haselager</sub></td>
<td width="12%">2011<br>Neuroethics<br>132 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain-Computer Interface (BCI) research and (future) applications raise important ethical issues that need to be addressed to promote societal acceptance and adequate policies.</td>
<td align="right" width="8%">132</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1152/jn.00493.2017">Stable long-term BCI-enabled communication in ALS and locked-in syndrome using LFP signals.</a><br><sub>T. Milekovic, Anish A. Sarma, D. Bacher, J. Simeral, J. Saab, C. Pandarinath, et al.</sub></td>
<td width="12%">2018<br>Journal of Neurophysiology<br>127 citations</td>
<td width="12%"><img alt="invasive" src="https://img.shields.io/badge/keyword-invasive-2563eb"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Restoring communication for people with locked-in syndrome remains a challenging clinical problem without a reliable solution.</td>
<td align="right" width="8%">127</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.3390/s140712784">Classification of EEG Signals Using a Multiple Kernel Learning Support Vector Machine</a><br><sub>Xiaoou Li, Xun Chen, Yuning Yan, Wenshi Wei, Z. J. Wang</sub></td>
<td width="12%">2014<br>Italian National Conference on Sensors<br>125 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In this study, a multiple kernel learning support vector machine algorithm is proposed for the identification of EEG signals including mental and cognitive tasks, which is a key component in EEG-based brain computer interface (BCI) systems.</td>
<td align="right" width="8%">125</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Clinical cohorts are often small and heterogeneous, making functional effect sizes difficult to compare.; Short follow-up windows can miss whether gains transfer to daily activities.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 87 papers.</td>
</tr>
</tbody>
</table>

</details>

### Hybrid, Affective, and Closed-loop BCIs

- Papers selected: **32**
- Years covered: **2001-2026**
- Citation count in selected set: **3,471**
- Category Overview (main research trends):
  - Hybrid BCI combines multiple signals or paradigms to improve reliability, command diversity, and asynchronous control.
  - Closed-loop and neurofeedback work is increasingly focused on user adaptation, mental-state awareness, fatigue, affect, and training protocols.
  - The trend is toward systems that adapt to the user over time rather than treating decoding as a one-shot offline classification problem.
- Limitations:
  - Combining paradigms can improve reliability but increases calibration, hardware, and user workload.
  - Closed-loop adaptation is hard to evaluate because user learning, fatigue, and affect change during use.
  - Longitudinal real-world studies remain scarce, so durability and user acceptance are not well captured.

<details>
<summary><strong>Show representative papers for Hybrid, Affective, and Closed-loop BCIs</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2003.814435">Asynchronous BCI and local neural classifiers: an overview of the adaptive brain interface project</a><br><sub>J. Millán, J. Mouriño</sub></td>
<td width="12%">2003<br>IEEE transactions on neural systems and rehabilitation engineering<br>319 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Asynchronous BCI and local neural classifiers: an overview of the adaptive brain interface project within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">319</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2012.2197221">A Hybrid Brain Computer Interface to Control the Direction and Speed of a Simulated or Real Wheelchair</a><br><sub>J. Long, Yuanqing Li, Hongtao Wang, Tianyou Yu, Jiahui Pan, Feng Li</sub></td>
<td width="12%">2012<br>IEEE transactions on neural systems and rehabilitation engineering<br>289 citations</td>
<td width="12%"><img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions A Hybrid Brain Computer Interface to Control the Direction and Speed of a Simulated or Real Wheelchair within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">289</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-human or simulated results require cautious translation to everyday human BCI use.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1080/2326263x.2014.912881">A survey of affective brain computer interfaces: principles, state-of-the-art, and challenges</a><br><sub>C. Mühl, B. Allison, A. Nijholt, G. Chanel</sub></td>
<td width="12%">2014<br>Unknown venue<br>279 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A survey of affective brain computer interfaces: principles, state-of-the-art, and challenges within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">279</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1162/neco_a_00089">Machine-Learning-Based Coadaptive Calibration for Brain-Computer Interfaces</a><br><sub>C. Vidaurre, C. Sannelli, K. Müller, B. Blankertz</sub></td>
<td width="12%">2011<br>Neural Computation<br>197 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Machine-Learning-Based Coadaptive Calibration for Brain-Computer Interfaces within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">197</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/8/2/025009">Co-adaptive calibration to improve BCI efficiency</a><br><sub>C. Vidaurre, C. Sannelli, K. Müller, B. Blankertz</sub></td>
<td width="12%">2011<br>Journal of Neural Engineering<br>182 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Co-adaptive calibration to improve BCI efficiency within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">182</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.1152/jn.00503.2010">A closed-loop human simulator for investigating the role of feedback control in brain-machine interfaces.</a><br><sub>J. Cunningham, Paul Nuyujukian, V. Gilja, C. Chestek, S. Ryu, K. Shenoy</sub></td>
<td width="12%">2011<br>Journal of Neurophysiology<br>176 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions A closed-loop human simulator for investigating the role of feedback control in brain-machine interfaces. within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">176</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1016/s0074-7742(09)86008-x">Neurofeedback and brain-computer interface clinical applications.</a><br><sub>N. Birbaumer, Ander Ramos Murguialday, Cornelia Weber, P. Montoya</sub></td>
<td width="12%">2009<br>International review of neurobiology<br>155 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Neurofeedback and brain-computer interface clinical applications. within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">155</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2011.2167718">Target Selection With Hybrid Feature for BCI-Based 2-D Cursor Control</a><br><sub>J. Long, Yuanqing Li, Tianyou Yu, Z. Gu</sub></td>
<td width="12%">2012<br>IEEE Transactions on Biomedical Engineering<br>135 citations</td>
<td width="12%"><img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Positions Target Selection With Hybrid Feature for BCI-Based 2-D Cursor Control within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">135</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Arm or cursor decoding performance may not generalize to unconstrained daily functional movements.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1371/journal.pone.0176674">A systematic review of hybrid brain-computer interfaces: Taxonomy and usability perspectives</a><br><sub>Inchul Choi, Ilsun Rhiu, Yushin Lee, M. Yun, C. Nam</sub></td>
<td width="12%">2017<br>PLoS ONE<br>120 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">A new Brain-Computer Interface (BCI) technique, which is called a hybrid BCI, has recently been proposed to address the limitations of conventional single BCI system.</td>
<td align="right" width="8%">120</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1038/s41598-017-02626-y">Absence Seizure Control by a Brain Computer Interface</a><br><sub>V. Maksimenko, S. van Heukelum, V. Makarov, J. Kelderhuis, A. Lüttjohann, A. Koronovskii, et al.</sub></td>
<td width="12%">2017<br>Scientific Reports<br>116 citations</td>
<td width="12%"><img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"></td>
<td width="18%">The ultimate goal of epileptology is the complete abolishment of epileptic seizures.</td>
<td align="right" width="8%">116</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jneumeth.2014.03.011">A hybrid brain computer interface system based on the neurophysiological protocol and brain-actuated switch for wheelchair control.</a><br><sub>Lei Cao, Jie Li, Hongfei Ji, Changjun Jiang</sub></td>
<td width="12%">2014<br>Journal of Neuroscience Methods<br>115 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A hybrid brain computer interface system based on the neurophysiological protocol and brain-actuated switch for wheelchair control. within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">115</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1080/2326263x.2016.1207497">Brain-computer interface-based control of closed-loop brain stimulation: attitudes and ethical considerations</a><br><sub>E. Klein, S. Goering, J. Gagne, Conor V. Shea, R. Franklin, S. Zorowitz, et al.</sub></td>
<td width="12%">2016<br>Unknown venue<br>115 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-computer interface-based control of closed-loop brain stimulation: attitudes and ethical considerations within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">115</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1109/tbme.2004.824128">Adaptive BCI based on variational Bayesian Kalman filtering: an empirical evaluation</a><br><sub>P. Sykacek, S. Roberts, Maria Stokes</sub></td>
<td width="12%">2004<br>IEEE Transactions on Biomedical Engineering<br>108 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Adaptive BCI based on variational Bayesian Kalman filtering: an empirical evaluation within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">108</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1109/tbcas.2016.2622738">Design of a Closed-Loop, Bidirectional Brain Machine Interface System With Energy Efficient Neural Feature Extraction and PID Control</a><br><sub>Xilin Liu, Milin Zhang, Andrew G. Richardson, T. Lucas, J. van der Spiegel</sub></td>
<td width="12%">2017<br>IEEE Transactions on Biomedical Circuits and Systems<br>106 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Design of a Closed-Loop, Bidirectional Brain Machine Interface System With Energy Efficient Neural Feature Extraction and PID Control within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">106</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1007/978-3-642-02091-9_4">Neurofeedback Training for BCI Control</a><br><sub>C. Neuper, G. Pfurtscheller</sub></td>
<td width="12%">2009<br>Unknown venue<br>106 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Neurofeedback Training for BCI Control within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">106</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2552/abca17">A review of user training methods in brain computer interfaces based on mental tasks</a><br><sub>A. Roc, Léa Pillette, J. Mladenović, Camille Benaroch, B. N&#x27;Kaoua, C. Jeunet, et al.</sub></td>
<td width="12%">2020<br>Journal of Neural Engineering<br>98 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Mental-tasks based brain–computer interfaces (MT-BCIs) allow their users to interact with an external device solely by using brain signals produced through mental tasks.</td>
<td align="right" width="8%">98</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1162/neco_a_00460">Design and Analysis of Closed-Loop Decoder Adaptation Algorithms for Brain-Machine Interfaces</a><br><sub>Siddharth Dangi, A. Orsborn, H. Moorman, J. Carmena</sub></td>
<td width="12%">2013<br>Neural Computation<br>93 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Design and Analysis of Closed-Loop Decoder Adaptation Algorithms for Brain-Machine Interfaces within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">93</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1007/978-3-642-02315-6_23">Affective Pacman: A Frustrating Game for Brain-Computer Interface Experiments</a><br><sub>Boris Reuderink, A. Nijholt, M. Poel</sub></td>
<td width="12%">2009<br>Intelligent Technologies for Interactive Entertainment<br>89 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Affective Pacman: A Frustrating Game for Brain-Computer Interface Experiments within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">89</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1007/978-3-642-21605-3_46">A Hybrid Brain-Computer Interface for Smart Home Control</a><br><sub>G. Edlinger, C. Holzner, C. Guger</sub></td>
<td width="12%">2011<br>Interacción<br>73 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A Hybrid Brain-Computer Interface for Smart Home Control within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">73</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1142/s0129065714500142">Evaluation and Application of a Hybrid Brain Computer Interface for Real Wheelchair Parallel Control with Multi-Degree of Freedom</a><br><sub>Jie Li, Hongfei Ji, Lei Cao, Di Zang, Rong Gu, Bin Xia, et al.</sub></td>
<td width="12%">2014<br>International Journal of Neural Systems<br>72 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Evaluation and Application of a Hybrid Brain Computer Interface for Real Wheelchair Parallel Control with Multi-Degree of Freedom within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">72</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neunet.2011.05.006">On the use of interaction error potentials for adaptive brain computer interfaces</a><br><sub>A. Llera, M. Gerven, V. Gómez, O. Jensen, H. Kappen</sub></td>
<td width="12%">2011<br>Neural Networks<br>67 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions On the use of interaction error potentials for adaptive brain computer interfaces within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">67</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1109/iembs.2007.4353015">Brain-Computer Interface Analysis using Continuous Wavelet Transform and Adaptive Neuro-Fuzzy Classifier</a><br><sub>S. Darvishi, A. Al-Ani</sub></td>
<td width="12%">2007<br>Annual International Conference of the IEEE Engineering in Medicine and Biology Society<br>62 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Brain-Computer Interface Analysis using Continuous Wavelet Transform and Adaptive Neuro-Fuzzy Classifier within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">62</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1109/acii.2009.5349456">Detecting affective covert user states with passive brain-computer interfaces</a><br><sub>T. Zander, S. Jatzev</sub></td>
<td width="12%">2009<br>2009 3rd International Conference on Affective Computing and Intelligent Interaction and Workshops<br>60 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Detecting affective covert user states with passive brain-computer interfaces within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">60</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1109/acii.2009.5349479">Affective brain-computer interfaces: Psychophysiological markers of emotion in healthy persons and in persons with amyotrophic lateral sclerosis</a><br><sub>F. Nijboer, Stefan Carmien, E. Leon, F. Morin, R. Koene, Ulrich Hoffmann</sub></td>
<td width="12%">2009<br>2009 3rd International Conference on Affective Computing and Intelligent Interaction and Workshops<br>58 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Affective brain-computer interfaces: Psychophysiological markers of emotion in healthy persons and in persons with amyotrophic lateral sclerosis within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">58</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1088/1741-2560/13/4/046003">Ensembles of adaptive spatial filters increase BCI performance: an online evaluation</a><br><sub>C. Sannelli, C. Vidaurre, K. Müller, B. Blankertz</sub></td>
<td width="12%">2016<br>Journal of Neural Engineering<br>56 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Ensembles of adaptive spatial filters increase BCI performance: an online evaluation within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">56</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1016/j.compbiomed.2012.02.004">Hangman BCI: An unsupervised adaptive self-paced Brain-Computer Interface for playing games</a><br><sub>Bashar Awwad Shiekh Hasan, J. Q. Gan</sub></td>
<td width="12%">2012<br>Comput. Biol. Medicine<br>55 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">This paper presents a novel user interface suitable for adaptive Brain Computer Interface (BCI) system.</td>
<td align="right" width="8%">55</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1016/j.medengphy.2006.01.009">Adaptive subject-based feature extraction in brain-computer interfaces using wavelet packet best basis decomposition.</a><br><sub>Banghua Yang, Guo-zheng Yan, Rongguo Yan, Ting Wu</sub></td>
<td width="12%">2007<br>Medical Engineering and Physics<br>48 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Adaptive subject-based feature extraction in brain-computer interfaces using wavelet packet best basis decomposition. within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">48</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1126/scitranslmed.abm5868">Closed-loop stimulation using a multi-region brain-machine interface has analgesic effects in rodents</a><br><sub>Guanghao Sun, Fei Zeng, Michael McCartin, Qiaosheng Zhang, Helen Y. Xu, Yaling Liu, et al.</sub></td>
<td width="12%">2022<br>Science Translational Medicine<br>48 citations</td>
<td width="12%"><img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Effective treatments for chronic pain remain limited.</td>
<td align="right" width="8%">48</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1109/icassp.2005.1416311">A hybrid genetic algorithm approach for improving the performance of the LF-ASD brain computer interface</a><br><sub>Mehrdad Fatourechi, Ali Bashashati, R. Ward, G. Birch</sub></td>
<td width="12%">2005<br>Proceedings. (ICASSP &#x27;05). IEEE International Conference on Acoustics, Speech, and Signal Processing, 2005.<br>37 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A hybrid genetic algorithm approach for improving the performance of the LF-ASD brain computer interface within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">37</td>
<td width="24%">Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/885f8291e27c0038e2039a8afe3cbddab0b07696">Designing a brain-computer interface device for neurofeedback using virtual environments</a><br><sub>N. Yan, Jue Wang, M. Liu, L. Zong, Y. Jiao, J. Yue, et al.</sub></td>
<td width="12%">2008<br>Unknown venue<br>30 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Designing a brain-computer interface device for neurofeedback using virtual environments within Hybrid, Affective, and Closed-loop BCIs.</td>
<td align="right" width="8%">30</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Hybrid and closed-loop designs make it difficult to isolate which signal or feedback component drives the benefit.; User learning, fatigue, and affect can change during closed-loop operation and confound evaluation.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 32 papers.</td>
</tr>
</tbody>
</table>

</details>

### Speech, Language, and Communication BCIs

- Papers selected: **31**
- Years covered: **2002-2024**
- Citation count in selected set: **11,096**
- Category Overview (main research trends):
  - Communication BCI is expanding from spelling paradigms toward imagined speech, decoded language, and higher-bandwidth text production.
  - Both invasive and non-invasive studies are exploring more naturalistic communication, including speech motor cortex decoding and inner-speech EEG datasets.
  - The central challenge remains preserving accuracy, latency, vocabulary size, and user autonomy in real-world assistive communication.
- Limitations:
  - Vocabulary size, latency, privacy, and user autonomy remain difficult to balance in practical assistive communication.
  - The strongest decoding results often rely on invasive recordings or carefully constrained tasks with limited participant diversity.
  - Non-invasive imagined-speech datasets are still comparatively small and hard to evaluate consistently.

<details>
<summary><strong>Show representative papers for Speech, Language, and Communication BCIs</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1016/s1388-2457(02)00057-3">Brain-computer interfaces for communication and control.</a><br><sub>J. Wolpaw, N. Birbaumer, D. McFarland, Gert Pfurtscheller, T. Vaughan</sub></td>
<td width="12%">2002<br>Clinical Neurophysiology<br>5,454 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-computer interfaces for communication and control. within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">5,454</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1145/1941487.1941506">Brain-Computer Interfaces for Communication and Control</a><br><sub>D. McFarland, J. Wolpaw</sub></td>
<td width="12%">2011<br>Communications of the ACM<br>2,866 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">The brain&#x27;s electrical signals enable people without muscle control to physically interact with the world.</td>
<td align="right" width="8%">2,866</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://doi.org/10.1016/j.tics.2021.04.003">Interface, interaction, and intelligence in generalized brain-computer interfaces.</a><br><sub>Xiaorong Gao, Yijun Wang, Xiaogang Chen, Shangkai Gao</sub></td>
<td width="12%">2021<br>Trends in Cognitive Sciences<br>263 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">A brain-computer interface (BCI) establishes a direct communication channel between a brain and an external device.</td>
<td align="right" width="8%">263</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.1007/s11042-006-0094-3">The Berlin Brain-Computer Interface (BBCI) – towards a new communication channel for online control in gaming applications</a><br><sub>R. Krepki, B. Blankertz, G. Curio, K. Müller</sub></td>
<td width="12%">2007<br>Multimedia tools and applications<br>243 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions The Berlin Brain-Computer Interface (BBCI) – towards a new communication channel for online control in gaming applications within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">243</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.3390/brainsci11010043">Summary of over Fifty Years with Brain-Computer Interfaces—A Review</a><br><sub>Aleksandra Kawala-Sterniuk, Natalia Browarska, Amir F. Al-Bakri, Mariusz Pelc, J. Zygarlicki, Michaela Sidikova, et al.</sub></td>
<td width="12%">2021<br>Brain Science<br>236 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Over the last few decades, the Brain-Computer Interfaces have been gradually making their way to the epicenter of scientific interest.</td>
<td align="right" width="8%">236</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.3389/fnins.2016.00530">The Berlin Brain-Computer Interface: Progress Beyond Communication and Control</a><br><sub>B. Blankertz, L. Acqualagna, Sven Dähne, S. Haufe, M. Schultze-Kraft, I. Sturm, et al.</sub></td>
<td width="12%">2016<br>Frontiers in Neuroscience<br>210 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">The combined effect of fundamental results about neurocognitive processes and advancements in decoding mental states from ongoing brain signals has brought forth a whole range of potential neurotechnological applications.</td>
<td align="right" width="8%">210</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1016/s0079-6123(06)59028-4">Future prospects of ERD/ERS in the context of brain-computer interface (BCI) developments.</a><br><sub>G. Pfurtscheller, C. Neuper</sub></td>
<td width="12%">2006<br>Progress in Brain Research<br>205 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="SMR" src="https://img.shields.io/badge/keyword-SMR-dc2626"></td>
<td width="18%">Positions Future prospects of ERD/ERS in the context of brain-computer interface (BCI) developments. within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">205</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1186/s12910-017-0220-y">Ethical aspects of brain computer interfaces: a scoping review</a><br><sub>Sasha Burwell, M. Sample, E. Racine</sub></td>
<td width="12%">2017<br>BMC Medical Ethics<br>182 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">BackgroundBrain-Computer Interface (BCI) is a set of technologies that are of increasing interest to researchers.</td>
<td align="right" width="8%">182</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1109/msp.2003.1166626">Brain-computer interface in multimedia communication</a><br><sub>T. Ebrahimi, J. Vesin, G. G. Molina</sub></td>
<td width="12%">2003<br>IEEE Signal Processing Magazine<br>152 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-computer interface in multimedia communication within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">152</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.1145/1296843.1296845">Brain-computer interfaces (BCIs) for communication and control</a><br><sub>J. Wolpaw</sub></td>
<td width="12%">2007<br>International ACM SIGACCESS Conference on Computers and Accessibility<br>134 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-computer interfaces (BCIs) for communication and control within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">134</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1016/j.inat.2020.100694">Brain computer interface advancement in neurosciences: Applications and issues</a><br><sub>S. Mudgal, S. Sharma, Jitender Chaturvedi, A. Sharma</sub></td>
<td width="12%">2020<br>Interdisciplinary Neurosurgery<br>117 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Abstract Neurosciences and Neuro-technology are continuously advancing and so individuals, society and healthcare professionals have to up date themselves with advancement.</td>
<td align="right" width="8%">117</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/410ba0d4fe4244c3097af17f1100bef17533c312">Brain Computer Interface for Communication and Control</a><br><sub>Rehab Ashary</sub></td>
<td width="12%">2008<br>Unknown venue<br>97 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain Computer Interface for Communication and Control within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">97</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1007/s13311-022-01190-2">Brain-Computer Interface: Applications to Speech Decoding and Synthesis to Augment Communication</a><br><sub>S. Luo, Q. Rabbani, N. Crone</sub></td>
<td width="12%">2022<br>Neurotherapeutics<br>97 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Computer Interface: Applications to Speech Decoding and Synthesis to Augment Communication within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">97</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jneumeth.2020.108918">A comprehensive assessment of Brain Computer Interfaces: Recent trends and challenges.</a><br><sub>Drishti Yadav, S. Yadav, K. Veer</sub></td>
<td width="12%">2020<br>Journal of Neuroscience Methods<br>89 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">BACKGROUND An uninterrupted channel of communication and control between the human brain and electronic processing units has led to an increased use of Brain Computer Interfaces (BCIs).</td>
<td align="right" width="8%">89</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1016/j.isci.2018.09.016">Neurolinguistics Research Advancing Development of a Direct-Speech Brain-Computer Interface</a><br><sub>Ciaran Cooney, R. Folli, D. Coyle</sub></td>
<td width="12%">2018<br>iScience<br>81 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">A direct-speech brain-computer interface (DS-BCI) acquires neural signals corresponding to imagined speech, then processes and decodes these signals to produce a linguistic output in the form of phonemes, words, or sentences.</td>
<td align="right" width="8%">81</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1145/2556288.2557339">FOCUS: enhancing children&#x27;s engagement in reading by using contextual BCI training sessions</a><br><sub>Jin Huang, Chun Yu, Yuntao Wang, Yuhang Zhao, Siqi Liu, Chou Mo, et al.</sub></td>
<td width="12%">2014<br>International Conference on Human Factors in Computing Systems<br>80 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions FOCUS: enhancing children&#x27;s engagement in reading by using contextual BCI training sessions within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">80</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1109/iccsp60870.2024.10543610">IoT in Brain-Computer Interfaces for Enabling Communication and Control for the Disabled</a><br><sub>Dr. S. Rajarajan, P. M. Suresh, Dr. T. Kowsalya, Nukala Sujata, Gupta, S. Murugan</sub></td>
<td width="12%">2024<br>International Conference on Cryptography, Security and Privacy<br>76 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">The proposed system integrates Internet of Things (IoT) technologies with Brain-computer interfaces to improve disability-related communication and control.</td>
<td align="right" width="8%">76</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1044/2017_ajslp-16-0244">Brain-Computer Interfaces for Augmentative and Alternative Communication: A Tutorial.</a><br><sub>J. Brumberg, Kevin M. Pitt, Alana Mantie-Kozlowski, Jeremy D. Burnison</sub></td>
<td width="12%">2018<br>American Journal of Speech-Language Pathology<br>75 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-Computer Interfaces for Augmentative and Alternative Communication: A Tutorial. within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">75</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1016/j.ijhcs.2006.11.010">Berlin Brain-Computer Interface - The HCI communication channel for discovery</a><br><sub>R. Krepki, G. Curio, B. Blankertz, K. Müller</sub></td>
<td width="12%">2007<br>Int. J. Hum. Comput. Stud.<br>69 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Berlin Brain-Computer Interface - The HCI communication channel for discovery within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">69</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.5539/mas.v16n3p34">The Importance of the Application of the Metaverse in Education</a><br><sub>G. S. Contreras, Aurora Hernández González, Martin Fernandez, C. M. Cepa, J. C. Escobar</sub></td>
<td width="12%">2022<br>Modern Applied Science<br>68 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In the early 90&#x27;s, and especially in some American universities, with the emergence of virtual reality, virtual environments and their manipulation began to be implemented, achieving important advances that have led to improvements in research through changes in the perception of the subject, modeling, communication processes and the development of 3D virtua</td>
<td align="right" width="8%">68</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jphysparis.2017.07.002">Key considerations in designing a speech brain-computer interface.</a><br><sub>Florent Bocquelet, Thomas Hueber, Laurent Girin, S. Chabardès, B. Yvert</sub></td>
<td width="12%">2016<br>Journal of Physiology - Paris<br>63 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Restoring communication in case of aphasia is a key challenge for neurotechnologies.</td>
<td align="right" width="8%">63</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/97cbf8583591f03332f6134bb8a07e185d9370da">Brain-computer interfaces (BCIs) for communication and control: a mini-review.</a><br><sub>J. Wolpaw</sub></td>
<td width="12%">2004<br>Supplements to Clinical Neurophysiology<br>57 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Brain-computer interfaces (BCIs) for communication and control: a mini-review. within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">57</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1177/1545968321989331">Brain-Computer Interfaces for communication: preferences of individuals with locked-in syndrome</a><br><sub>M. Branco, Elmar G. M. Pels, Ruben H. Sars, E. Aarnoutse, N. Ramsey, M. Vansteensel, et al.</sub></td>
<td width="12%">2021<br>Neurorehabilitation and Neural Repair<br>50 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">Background Brain-computer interfaces (BCIs) have been proposed as an assistive technology (AT) allowing people with locked-in syndrome (LIS) to use neural signals to communicate.</td>
<td align="right" width="8%">50</td>
<td width="24%">Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.1109/comst.2024.3387124">A Human-Centric Metaverse Enabled by Brain-Computer Interface: A Survey</a><br><sub>Howe Yuan Zhu, Nguyen Quang Hieu, D. Hoang, Diep N. Nguyen, Chin-Teng Lin</sub></td>
<td width="12%">2023<br>IEEE Communications Surveys and Tutorials<br>48 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"> <img alt="arm-direction" src="https://img.shields.io/badge/keyword-arm--direction-0891b2"></td>
<td width="18%">The growing interest in the Metaverse has generated momentum for members of academia and industry to innovate toward realizing the Metaverse world.</td>
<td align="right" width="8%">48</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1155/2007/94397">A Semisupervised Support Vector Machines Algorithm for BCI Systems</a><br><sub>Jianzhao Qin, Yuanqing Li, Wei Sun</sub></td>
<td width="12%">2007<br>Computational Intelligence and Neuroscience<br>32 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">As an emerging technology, brain-computer interfaces (BCIs) bring us new communication interfaces which translate brain activities into control signals for devices like computers, robots, and so forth.</td>
<td align="right" width="8%">32</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/f07e080a347f7c1a35ca1950c889b56e55d46b03">The Berlin Brain-Computer Interface ( BBCI ) towards a new communication channel for online control of multimedia applications and computer games</a><br><sub>R. Krepki, B. Blankertz, G. Curio, K. Müller</sub></td>
<td width="12%">2003<br>Unknown venue<br>22 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions The Berlin Brain-Computer Interface ( BBCI ) towards a new communication channel for online control of multimedia applications and computer games within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">22</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://www.semanticscholar.org/paper/5b42a80bf1dd810dbf8a79fe028bd1b7e2001c4a">Communication speed enhancement for visual based Brain Computer Interfaces</a><br><sub>S. Sami, K. D. Nielsen</sub></td>
<td width="12%">2004<br>Unknown venue<br>10 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Communication speed enhancement for visual based Brain Computer Interfaces within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">10</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.1109/iembs.2006.260238">Autoregressive spectral analysis in Brain Computer Interface context</a><br><sub>S. Bufalari, D. Mattia, F. Babiloni, M. Mattiocco, M. Marciani, F. Cincotti</sub></td>
<td width="12%">2006<br>Annual International Conference of the IEEE Engineering in Medicine and Biology Society<br>10 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Autoregressive spectral analysis in Brain Computer Interface context within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">10</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1142/9789812561763_0039">BRAIN-COMPUTER INTERFACES FOR VERBAL COMMUNICATION</a><br><sub>N. Birbaumer, U. Strehl, T. Hinterberger</sub></td>
<td width="12%">2004<br>Unknown venue<br>10 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions BRAIN-COMPUTER INTERFACES FOR VERBAL COMMUNICATION within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">10</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1055/s-2003-816484">Lateralisiertes Bereitschaftspotenzial und Ereignis-korrelierte Desynchronisation perizentraler my/beta-Rhythmen bei rasch repetierten Fingerbewegungen im Kontext des Berlin Brain-Computer Interface (BBCI)</a><br><sub>F. Losch, B. Blankertz, K. Müller, G. Curio</sub></td>
<td width="12%">2003<br>Unknown venue<br>0 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Positions Lateralisiertes Bereitschaftspotenzial und Ereignis-korrelierte Desynchronisation perizentraler my/beta-Rhythmen bei rasch repetierten Fingerbewegungen im Kontext des Berlin Brain-Computer Interface (BBCI) within Speech, Language, and Communication BCIs.</td>
<td align="right" width="8%">0</td>
<td width="24%">Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Many decoding results rely on constrained tasks or limited participant diversity.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 31 papers.</td>
</tr>
</tbody>
</table>

</details>

### Deep Learning and Representation Learning

- Papers selected: **31**
- Years covered: **2015-2026**
- Citation count in selected set: **3,158**
- Category Overview (main research trends):
  - Deep learning work is moving beyond single-dataset CNN classifiers toward temporal, spectral, graph, transformer, and attention-based architectures.
  - A major trend is representation learning that can transfer across users, sessions, headsets, and BCI paradigms with less subject-specific calibration.
  - Interpretability, uncertainty, robustness to artifacts, and benchmark comparability are becoming as important as peak classification accuracy.
- Limitations:
  - Performance can be inflated by dataset leakage, weak cross-subject splits, or inconsistent preprocessing across benchmarks.
  - Large models often improve accuracy while reducing interpretability, uncertainty awareness, and clinical trust.
  - Low-data and noisy-session robustness remains unresolved for many architectures outside curated datasets.

<details>
<summary><strong>Show representative papers for Deep Learning and Representation Learning</strong></summary>

<table width="100%">
<colgroup>
<col width="5%">
<col width="21%">
<col width="12%">
<col width="12%">
<col width="18%">
<col width="8%">
<col width="24%">
</colgroup>
<thead>
<tr>
<th align="right">Rank</th>
<th>Paper</th>
<th>Meta</th>
<th>Keywords</th>
<th>Key idea</th>
<th>Strengths<br><sub>(high citation signal)</sub></th>
<th>Limitations</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right" width="5%">1</td>
<td width="21%"><a href="https://doi.org/10.1109/tcbb.2021.3052811">EEG-Based Brain-Computer Interfaces (BCIs): A Survey of Recent Studies on Signal Sensing Technologies and Computational Intelligence Approaches and Their Applications</a><br><sub>Xiaotong Gu, Zehong Cao, A. Jolfaei, Peng Xu, Dongrui Wu, T. Jung, et al.</sub></td>
<td width="12%">2020<br>IEEE/ACM Transactions on Computational Biology &amp; Bioinformatics<br>322 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Brain-Computer interfaces (BCIs) enhance the capability of human brain activities to interact with the environment.</td>
<td align="right" width="8%">322</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">2</td>
<td width="21%"><a href="https://doi.org/10.1016/j.neunet.2019.12.006">A novel multi-modal machine learning based approach for automatic classification of EEG recordings in dementia</a><br><sub>C. Ieracitano, N. Mammone, A. Hussain, F. Morabito</sub></td>
<td width="12%">2019<br>Neural Networks<br>283 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Electroencephalographic (EEG) recordings generate an electrical map of the human brain that are useful for clinical inspection of patients and in biomedical smart Internet-of-Things (IoT) and Brain-Computer Interface (BCI) applications.</td>
<td align="right" width="8%">283</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Clinical impact needs stronger longitudinal evidence on daily function, adherence, and adverse events.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.</td>
</tr>
<tr>
<td align="right" width="5%">3</td>
<td width="21%"><a href="https://arxiv.org/abs/2106.11170">Transformer-based Spatial-Temporal Feature Learning for EEG Decoding</a><br><sub>Yonghao Song, Xueyu Jia, Lie Yang, Longhan Xie</sub></td>
<td width="12%">2021<br>arXiv.org<br>219 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">At present, people usually use some methods based on convolutional neural networks (CNNs) for Electroencephalograph (EEG) decoding.</td>
<td align="right" width="8%">219</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">4</td>
<td width="21%"><a href="https://doi.org/10.3390/brainsci9050115">Epilepsy Detection by Using Scalogram Based Convolutional Neural Network from EEG Signals</a><br><sub>Ömer Türk, M. S. Özerdem</sub></td>
<td width="12%">2019<br>Brain Science<br>183 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">The studies implemented with Electroencephalogram (EEG) signals are progressing very rapidly and brain computer interfaces (BCI) and disease determinations are carried out at certain success rates thanks to new methods developed in this field.</td>
<td align="right" width="8%">183</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">5</td>
<td width="21%"><a href="https://doi.org/10.52202/079017-1239">EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals</a><br><sub>Guangyu Wang, Wenchao Liu, Yuhong He, Cong Xu, Lin Ma, Haifeng Li</sub></td>
<td width="12%">2024<br>Neural Information Processing Systems<br>174 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Electroencephalography (EEG) is crucial for recording brain activity, with applications in medicine, neuroscience, and brain-computer interfaces (BCI).</td>
<td align="right" width="8%">174</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">6</td>
<td width="21%"><a href="https://doi.org/10.1155/2015/129021">Deep Extreme Learning Machine and Its Application in EEG Classification</a><br><sub>Shifei Ding, Nan Zhang, Xinzheng Xu, Lili Guo, Jian Zhang</sub></td>
<td width="12%">2015<br>Unknown venue<br>169 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Recently, deep learning has aroused wide interest in machine learning fields.</td>
<td align="right" width="8%">169</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">7</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2020.2985996">Manifold Embedded Knowledge Transfer for Brain-Computer Interfaces</a><br><sub>Wen Zhang, Dongrui Wu</sub></td>
<td width="12%">2019<br>IEEE transactions on neural systems and rehabilitation engineering<br>167 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Transfer learning makes use of data or knowledge in one problem to help solve a different, yet related, problem.</td>
<td align="right" width="8%">167</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">8</td>
<td width="21%"><a href="https://doi.org/10.1016/j.engappai.2022.105347">Adaptive transfer learning-based multiscale feature fused deep convolutional neural network for EEG MI multiclassification in brain-computer interface</a><br><sub>Anisha Roy</sub></td>
<td width="12%">2022<br>Engineering applications of artificial intelligence<br>158 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Adaptive transfer learning-based multiscale feature fused deep convolutional neural network for EEG MI multiclassification in brain-computer interface within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">158</td>
<td width="24%">Offline benchmark performance may not transfer to real-time closed-loop use.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">9</td>
<td width="21%"><a href="https://doi.org/10.1109/tbdata.2017.2769670">Optimized Deep Learning for EEG Big Data and Seizure Prediction BCI via Internet of Things</a><br><sub>M. Hosseini, D. Pompili, K. Elisevich, H. Soltanian-Zadeh</sub></td>
<td width="12%">2017<br>IEEE Transactions on Big Data<br>151 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Optimized Deep Learning for EEG Big Data and Seizure Prediction BCI via Internet of Things within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">151</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">10</td>
<td width="21%"><a href="https://doi.org/10.3389/fnhum.2020.00103">Cross-Dataset Variability Problem in EEG Decoding With Deep Learning</a><br><sub>Lichao Xu, Minpeng Xu, Yufeng Ke, X. An, Shuang Liu, Dong Ming</sub></td>
<td width="12%">2020<br>Frontiers in Human Neuroscience<br>129 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Cross-subject variability problems hinder practical usages of Brain-Computer Interfaces.</td>
<td align="right" width="8%">129</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">11</td>
<td width="21%"><a href="https://doi.org/10.1109/mci.2021.3061875">Multi-Scale Neural Network for EEG Representation Learning in BCI</a><br><sub>Wonjun Ko, Eunjin Jeon, Seungwoo Jeong, Heung-Il Suk</sub></td>
<td width="12%">2020<br>IEEE Computational Intelligence Magazine<br>102 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Recent advances in deep learning have had a methodological and practical impact on brain-computer interface (BCI) research.</td>
<td align="right" width="8%">102</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">12</td>
<td width="21%"><a href="https://doi.org/10.1109/tnnls.2021.3100583">Mutual Information-Driven Subject-Invariant and Class-Relevant Deep Representation Learning in BCI</a><br><sub>Eunjin Jeon, Wonjun Ko, Jee Seok Yoon, Heung-Il Suk</sub></td>
<td width="12%">2019<br>IEEE Transactions on Neural Networks and Learning Systems<br>100 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In recent years, deep learning-based feature representation methods have shown a promising impact on electroencephalography (EEG)-based brain–computer interface (BCI).</td>
<td align="right" width="8%">100</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">13</td>
<td width="21%"><a href="https://doi.org/10.1109/tnsre.2019.2908955">On the Vulnerability of CNN Classifiers in EEG-Based BCIs</a><br><sub>Xiao Zhang, Dongrui Wu</sub></td>
<td width="12%">2019<br>IEEE transactions on neural systems and rehabilitation engineering<br>98 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Deep learning has been successfully used in numerous applications because of its outstanding performance and the ability to avoid manual feature engineering.</td>
<td align="right" width="8%">98</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">14</td>
<td width="21%"><a href="https://doi.org/10.1109/jbhi.2024.3504604">EEG-Deformer: A Dense Convolutional Transformer for Brain-Computer Interfaces</a><br><sub>Yi Ding, Yong Li, Hao Sun, Rui Liu, Chengxuan Tong, Chenyu Liu, et al.</sub></td>
<td width="12%">2024<br>IEEE journal of biomedical and health informatics<br>91 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Effectively learning the temporal dynamics in electroencephalogram (EEG) signals is challenging yet essential for decoding brain activities using brain-computer interfaces (BCIs).</td>
<td align="right" width="8%">91</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">15</td>
<td width="21%"><a href="https://doi.org/10.1109/access.2019.2942838">Enhanced Drowsiness Detection Using Deep Learning: An fNIRS Study</a><br><sub>M. Tanveer, M. J. Khan, M. Qureshi, Noman Naseer, K. Hong</sub></td>
<td width="12%">2019<br>IEEE Access<br>81 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In this paper, a deep-learning-based driver-drowsiness detection for brain-computer interface (BCI) using functional near-infrared spectroscopy (fNIRS) is investigated.</td>
<td align="right" width="8%">81</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">16</td>
<td width="21%"><a href="https://doi.org/10.1109/smc.2019.8914246">Optimizing Layers Improves CNN Generalization and Transfer Learning for Imagined Speech Decoding from EEG</a><br><sub>Ciaran Cooney, R. Folli, D. Coyle</sub></td>
<td width="12%">2019<br>IEEE International Conference on Systems, Man and Cybernetics<br>79 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">A brain-computer interface (BCI) that employs imagined speech as the mode of determining user intent requires strong generalizability for a feasible system to be realized.</td>
<td align="right" width="8%">79</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.</td>
</tr>
<tr>
<td align="right" width="5%">17</td>
<td width="21%"><a href="https://doi.org/10.1016/j.compbiomed.2022.106248">EEGDnet: Fusing Non-Local and Local Self-Similarity for 1-D EEG Signal Denoising with 2-D Transformer</a><br><sub>X. Pu, Peng Yi, Kecheng Chen, Zhaoqi Ma, Di Zhao, Yazhou Ren</sub></td>
<td width="12%">2021<br>Comput. Biol. Medicine<br>79 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Electroencephalogram (EEG) has shown a useful approach to produce a brain-computer interface (BCI).</td>
<td align="right" width="8%">79</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">18</td>
<td width="21%"><a href="https://doi.org/10.1109/smc.2017.8122608">Deep learning-based classification for brain-computer interfaces</a><br><sub>J. Thomas, Tomasz Maszczyk, N. Sinha, T. Kluge, J. Dauwels</sub></td>
<td width="12%">2017<br>IEEE International Conference on Systems, Man and Cybernetics<br>74 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Deep learning-based classification for brain-computer interfaces within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">74</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">19</td>
<td width="21%"><a href="https://doi.org/10.1016/j.jneumeth.2016.11.002">The extraction of motion-onset VEP BCI features based on deep learning and compressed sensing.</a><br><sub>Teng Ma, Hui Li, Hao Yang, Xulin Lv, Peiyang Li, Tiejun Liu, et al.</sub></td>
<td width="12%">2017<br>Journal of Neuroscience Methods<br>74 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions The extraction of motion-onset VEP BCI features based on deep learning and compressed sensing. within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">74</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">20</td>
<td width="21%"><a href="https://doi.org/10.1007/s00521-021-06038-y">Vehicle driver drowsiness detection method using wearable EEG based on convolution neural network</a><br><sub>Miankuan Zhu, Jiangfan Chen, Haobo Li, Fujian Liang, Lei Han, Zutao Zhang</sub></td>
<td width="12%">2021<br>Neural computing &amp; applications (Print)<br>69 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="non-human" src="https://img.shields.io/badge/keyword-non--human-a855f7"></td>
<td width="18%">Vehicle drivers driving cars under the situation of drowsiness can cause serious traffic accidents.</td>
<td align="right" width="8%">69</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">21</td>
<td width="21%"><a href="https://doi.org/10.1016/j.engappai.2023.106205">On The Effects Of Data Normalisation For Domain Adaptation On EEG Data</a><br><sub>Andrea Apicella, F. Isgrò, A. Pollastro, R. Prevete</sub></td>
<td width="12%">2022<br>Engineering applications of artificial intelligence<br>69 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In the Machine Learning (ML) literature, a well-known problem is the Dataset Shift problem where, differently from the ML standard hypothesis, the data in the training and test sets can follow different probability distributions, leading ML systems toward poor generalisation performances.</td>
<td align="right" width="8%">69</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">22</td>
<td width="21%"><a href="https://doi.org/10.1109/embc.2015.7318984">Investigating deep learning for fNIRS based BCI</a><br><sub>Johannes Hennrich, Christian Herff, D. Heger, Tanja Schultz</sub></td>
<td width="12%">2015<br>Annual International Conference of the IEEE Engineering in Medicine and Biology Society<br>68 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Investigating deep learning for fNIRS based BCI within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">68</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">23</td>
<td width="21%"><a href="https://doi.org/10.1109/icassp49357.2023.10096587">EEG2IMAGE: Image Reconstruction from EEG Brain Signals</a><br><sub>Prajwal Singh, Pankaja Pandey, K. Miyapuram, S. Raman</sub></td>
<td width="12%">2023<br>IEEE International Conference on Acoustics, Speech, and Signal Processing<br>66 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Reconstructing images using brain signals of imagined visuals may provide an augmented vision to the disabled, leading to the advancement of Brain-Computer Interface (BCI) technology.</td>
<td align="right" width="8%">66</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.</td>
</tr>
<tr>
<td align="right" width="5%">24</td>
<td width="21%"><a href="https://doi.org/10.3389/fnrgo.2021.805573">Denoising EEG Signals for Real-World BCI Applications Using GANs</a><br><sub>Eoin Brophy, P. Redmond, Andrew Fleury, M. de Vos, G. Boylan, Tomás Ward</sub></td>
<td width="12%">2022<br>Frontiers in Neuroergonomics<br>52 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">As a measure of the brain&#x27;s electrical activity, electroencephalography (EEG) is the primary signal of interest for brain-computer-interfaces (BCI).</td>
<td align="right" width="8%">52</td>
<td width="24%">Benchmark value depends on standardized protocols, transparent splits, and external replication.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.</td>
</tr>
<tr>
<td align="right" width="5%">25</td>
<td width="21%"><a href="https://doi.org/10.1093/pnasnexus/pgae076">Transfer learning promotes acquisition of individual BCI skills</a><br><sub>Satyam Kumar, Hussein Alawieh, F. S. Racz, R. Fakhreddine, J. D. R. Millán</sub></td>
<td width="12%">2024<br>PNAS Nexus<br>39 citations</td>
<td width="12%"><img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">Abstract Subject training is crucial for acquiring brain–computer interface (BCI) control.</td>
<td align="right" width="8%">39</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Participant variability can limit generalization across age, ability, disease status, and training experience.</td>
</tr>
<tr>
<td align="right" width="5%">26</td>
<td width="21%"><a href="https://doi.org/10.1016/j.prime.2024.100448">Evaluating Deep Learning with different feature scaling techniques for EEG-based Music Entrainment Brain Computer Interface</a><br><sub>R. C R, D. C P</sub></td>
<td width="12%">2024<br>e-Prime<br>21 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Evaluating Deep Learning with different feature scaling techniques for EEG-based Music Entrainment Brain Computer Interface within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">21</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">27</td>
<td width="21%"><a href="https://doi.org/10.1016/j.eswa.2024.126081">A bidirectional cross-modal transformer representation learning model for EEG-fNIRS multimodal affective BCI</a><br><sub>Xiaopeng Si, Shuai Zhang, Zhuobin Yang, Jiayue Yu, Dong Ming</sub></td>
<td width="12%">2024<br>Expert systems with applications<br>21 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions A bidirectional cross-modal transformer representation learning model for EEG-fNIRS multimodal affective BCI within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">21</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">28</td>
<td width="21%"><a href="https://doi.org/10.48550/arxiv.2502.02830">Multimodal Brain-Computer Interfaces: AI-powered Decoding Methodologies</a><br><sub>Siyang Li, Hongbin Wang, Xiaoqing Chen, Dongrui Wu</sub></td>
<td width="12%">2025<br>arXiv.org<br>15 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Brain-computer interfaces (BCIs) enable direct communication between the brain and external devices.</td>
<td align="right" width="8%">15</td>
<td width="24%">Review-level synthesis cannot resolve study quality differences, protocol bias, or reproducibility gaps.; Communication systems must still balance accuracy, latency, vocabulary size, privacy, and user autonomy.; Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.</td>
</tr>
<tr>
<td align="right" width="5%">29</td>
<td width="21%"><a href="https://doi.org/10.1016/j.hest.2026.01.002">Neural Decoding for EEG-BCI: From Conventional Machine Learning to Deep Learning Models</a><br><sub>Yibo Ding, Xinyu Ma, Ping Zhang, Yingxin Tang, Zhixian Zhao, Danyang Chen, et al.</sub></td>
<td width="12%">2026<br>Brain Hemorrhages<br>2 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"></td>
<td width="18%">Positions Neural Decoding for EEG-BCI: From Conventional Machine Learning to Deep Learning Models within Deep Learning and Representation Learning.</td>
<td align="right" width="8%">2</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td align="right" width="5%">30</td>
<td width="21%"><a href="https://doi.org/10.1109/ojsp.2026.3664271">Alternatives to Sine Carrier in Auditory BCI: Exploring Machine Learning Strategies for Assessing Modulation Detectability in EEG</a><br><sub>Lenaïg Guého, Henrique Lefundes da Silva, Cyril Plapous, L. Bougrain, Patrick Hénaff, Rozenn Nicol</sub></td>
<td width="12%">2026<br>IEEE Open Journal of Signal Processing<br>2 citations</td>
<td width="12%"><img alt="non-invasive" src="https://img.shields.io/badge/keyword-non--invasive-0f766e"> <img alt="human" src="https://img.shields.io/badge/keyword-human-f59e0b"></td>
<td width="18%">In this paper, the use of non-sinusoidal amplitude-modulated stimuli is assessed for Brain-Computer Interfaces (BCIs) based on Steady-State Auditory Evoked Potentials (SSAEPs).</td>
<td align="right" width="8%">2</td>
<td width="24%">Deep models can overfit small EEG datasets without rigorous cross-subject and cross-device validation.; Model interpretability and uncertainty estimates are often insufficient for clinical trust.; Non-invasive signals are vulnerable to low signal-to-noise ratio, artifacts, and electrode setup variability.</td>
</tr>
<tr>
<td colspan="7">See the website and taxonomy CSV for all 31 papers.</td>
</tr>
</tbody>
</table>

</details>

## Yearly Coverage

| Year | Selected papers | Citation count | Top paper |
| ---: | ---: | ---: | --- |
| 2000 | 20 | 6,492 | [Brain-computer interface technology: a review of the first international meeting.](https://doi.org/10.1109/tre.2000.847807) |
| 2001 | 14 | 3,007 | [Motor imagery and direct brain-computer communication](https://doi.org/10.1109/5.939829) |
| 2002 | 24 | 7,864 | [Brain-computer interfaces for communication and control.](https://doi.org/10.1016/s1388-2457(02)00057-3) |
| 2003 | 89 | 7,102 | [A BCI-based environmental controller for the motion-disabled.](https://doi.org/10.1109/tnsre.2003.814449) |
| 2004 | 100 | 14,605 | [BCI2000: a general-purpose brain-computer interface (BCI) system](https://doi.org/10.1109/tbme.2004.827072) |
| 2005 | 100 | 6,627 | [Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface](https://doi.org/10.1212/01.wnl.0000158616.43002.6d) |
| 2006 | 100 | 17,128 | [Brain-machine interfaces: past, present and future.](https://doi.org/10.1016/j.tins.2006.07.004) |
| 2007 | 100 | 10,574 | [The non-invasive Berlin Brain-Computer Interface: Fast acquisition of effective performance in untrained subjects](https://doi.org/10.1016/j.neuroimage.2007.01.051) |
| 2008 | 100 | 18,705 | [Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface](https://doi.org/10.1109/ijcnn.2008.4634130) |
| 2009 | 100 | 13,728 | [An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method](https://doi.org/10.1088/1741-2560/6/4/046002) |
| 2010 | 100 | 17,519 | [The Hybrid BCI](https://doi.org/10.3389/fnpro.2010.00003) |
| 2011 | 100 | 20,824 | [Brain-Computer Interfaces for Communication and Control](https://doi.org/10.1145/1941487.1941506) |
| 2012 | 100 | 15,347 | [Filter Bank Common Spatial Pattern Algorithm on BCI Competition IV Datasets 2a and 2b](https://doi.org/10.3389/fnins.2012.00039) |
| 2013 | 100 | 15,830 | [Failure mode analysis of silicon-based intracortical microelectrode arrays in non-human primates](https://doi.org/10.1088/1741-2560/10/6/066014) |
| 2014 | 100 | 12,955 | [Brain-Computer Interfaces Using Sensorimotor Rhythms: Current State and Future Perspectives](https://doi.org/10.1109/tbme.2014.2312397) |
| 2015 | 100 | 16,376 | [fNIRS-based brain-computer interfaces: a review](https://doi.org/10.3389/fnhum.2015.00003) |
| 2016 | 100 | 15,478 | [EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces](https://doi.org/10.1088/1741-2552/aace8c) |
| 2017 | 100 | 15,668 | [A novel deep learning approach for classification of EEG motor imagery signals](https://doi.org/10.1088/1741-2560/14/1/016003) |
| 2018 | 100 | 13,140 | [Learning Temporal Information for Brain-Computer Interface Using Convolutional Neural Networks](https://doi.org/10.1109/tnnls.2018.2789927) |
| 2019 | 100 | 16,909 | [Deep learning for electroencephalogram (EEG) classification tasks: a review](https://doi.org/10.1088/1741-2552/ab0ab5) |
| 2020 | 100 | 13,125 | [Brain-Computer Interfaces](https://doi.org/10.1007/978-3-540-29678-2_717) |
| 2021 | 100 | 11,412 | [High-performance brain-to-text communication via handwriting](https://doi.org/10.1038/s41586-021-03506-2) |
| 2022 | 100 | 7,455 | [Past, Present, and Future of EEG-Based BCI Applications](https://doi.org/10.3390/s22093331) |
| 2023 | 100 | 6,906 | [Physics-Informed Attention Temporal Convolutional Network for EEG-Based Motor Imagery Classification](https://doi.org/10.1109/tii.2022.3197419) |
| 2024 | 100 | 4,231 | [Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://doi.org/10.48550/arxiv.2405.18765) |
| 2025 | 100 | 1,787 | [Recent applications of EEG-based brain-computer-interface in the medical field](https://doi.org/10.1186/s40779-025-00598-z) |
| 2026 | 100 | 170 | [EEG Foundation Models: Progresses, Benchmarking, and Open Problems](https://doi.org/10.48550/arxiv.2601.17883) |
## Method

The collection uses Semantic Scholar's Academic Graph paper search. Queries combine broad BCI terms and common subfields, results are filtered to the target publication year, relevance-filtered by BCI terms in title/abstract, deduplicated by DOI/arXiv/PubMed/CorpusId/paperId, and reduced to a maximum of 500 candidates per year. Importance scoring is retained for candidate auditing and combines log-scaled citation count, log-scaled influential citation count, recognized venue signals, BCI relevance-term density, and bonuses for reviews/surveys, datasets/benchmarks, clinical or rehabilitation relevance, invasive/high-bandwidth interfaces, and modern ML methods. The final awesome list selects the top 100 papers per year by citation count from the audited candidate pool.

## Caveats

- Citation counts favor older papers and may under-rank recent 2026 work.
- Metadata search is not equivalent to a full systematic review of PDFs.
- Some venues and publication dates are missing in upstream metadata.

## Acknowledgements

This repository and interactive site were created with appreciation for [jehyunlee/paper-curation](https://github.com/jehyunlee/paper-curation). Its paper-curation workflow and repository organization informed the approach used here for a taxonomy-first, citation-ranked research map.
