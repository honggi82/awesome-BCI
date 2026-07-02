[Figure 1]

J. Integr. Neurosci. 2024; 23(7): 125 https://doi.org/10.31083/j.jin2307125

Review

# Review on the Use of Brain Computer Interface Rehabilitation Methods for Treating Mental and Neurological Conditions

Vladimir Khorev1,2, Semen Kurkin2,*, Artem Badarin1, Vladimir Antipov1, Elena Pitsik2, Andrey Andreev2, Vadim Grubov2, Oxana Drapkina1, Anton Kiselev1, Alexander Hramov2

1Coordinating Center for Fundamental Research, National Medical Research Center for Therapy and Preventive Medicine, 101990 Moscow, Russia 2Baltic Center for Neurotechnology and Artificial Intelligence, Immanuel Kant Baltic Federal University, 236016 Kaliningrad, Russia

*Correspondence: kurkinsa@gmail.com (Semen Kurkin) Academic Editor: Imran Khan Niazi Submitted: 25 November 2023 Revised: 10 January 2024 Accepted: 31 January 2024 Published: 5 July 2024

#### Abstract

This review provides a comprehensive examination of recent developments in both neurofeedback and brain-computer interface (BCI) within the medical field and rehabilitation. By analyzing and comparing results obtained with various tools and techniques, we aim to offer a systematic understanding of BCI applications concerning different modalities of neurofeedback and input data utilized. Our primary objective is to address the existing gap in the area of meta-reviews, which provides a more comprehensive outlook on the field, allowing for the assessment of the current landscape and developments within the scope of BCI. Our main methodologies include meta-analysis, search queries employing relevant keywords, and a network-based approach. We are dedicated to delivering an unbiased evaluation of BCI studies, elucidating the primary vectors of research development in this field. Our review encompasses a diverse range of applications, incorporating the use of brain-computer interfaces for rehabilitation and the treatment of various diagnoses, including those related to affective spectrum disorders. By encompassing a wide variety of use cases, we aim to offer a more comprehensive perspective on the utilization of neurofeedback treatments across different contexts. The structured and organized presentation of information, complemented by accompanying visualizations and diagrams, renders this review a valuable resource for scientists and researchers engaged in the domains of biofeedback and brain-computer interfaces.

Keywords: BCI; neurofeedback; review; classification; modality; biofeedback; meta-analysis

## 1. Introduction

The study of brain-computer interface (BCI) has been gaining significance over the past few decades, with a multitude of scientists from various parts of the world contributing to this domain by creating numerous tools and techniques for brain signal acquisition and processing. This progress is largely attributed to advancements in cuttingedge technology, which provide researchers with access to crucial data: recordings of neural activity. These recordings enable scientists to carry out in-depth and productive research in the field of brain-computer interfaces, allowing them to gain insights into the workings of the brain.

The use of BCI mainly categorizes into the following target populations: patients who lack any motor control (can barely move), patients with little voluntary movement, and patients with significant neuromuscular control [1]. BCIs are also used for people with psychiatric disorders such as attention deficit hyperactivity disorder (ADHD), neurodegenerative diseases, schizophrenia, and depression [2–6]. Significant advances in electroencephalography (EEG)-based BCI provide acceptable signal quality, combine low cost and easy-to-use equipment, allowing its users new means of communication and control without interference from peripheral nerves and muscles [7]. Moreover, neuromarketing and the video game industry are in-

creasingly using BCIs to extract affective information from healthy individuals, bypassing physical interaction, and developing new levels of control [8]. BCIs help users to be more relaxed and focused, and make life easier for the end user if they are able to control the BCI [9,10].

There is an increasing use of BCIs for addressing issues in the fields of psychology and psychiatry, suggesting a trend towards more widespread adoption of this technology in mental health care. Recently, there has been a demand for more diagnostic tools for the objective detection and monitoring of mental disorders [11–21]. One of the recentreviewsfocusesontheautomateddetectionofthesedevelopmental and mental disorders using physiological signals [11]. Another review provides an introduction to various emotion models, stimuli used for emotion elicitation, and the background of existing automated emotion recognition systems [12]. Cho and his co-authors [22] undertook a wide-ranging review of the machine learning algorithms that have been utilized in the field of mental health, utilizing speech, neuroimaging, physiological data, and diverse types of patient information for diagnostic purposes. By examining the uses of BCIs in the treatment of various mental disorders, it is possible to provide insight into the potential benefits and limitations of this technology and its usefulness for improving clinical outcomes.

Copyright: © 2024 The Author(s). Published by IMR Press. This is an open access article under the CC BY 4.0 license.

[Figure 2]

Publisher’s Note: IMR Press stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Currently, a majority of systematic reviews on BCIs tend to have a specific and limited focus, either on solving a particular issue or addressing a specific problem [23–25], a specific application [11–13], or solely on the physical principles of BCIs [7]. While these reviews offer the benefit of providing detailed and focused information, they often lack a broader perspective on the overall use and application of BCIs in the medical field [1,23–31]. In light of the aforementioned context, it becomes evident that a gap persists in the area of meta-reviews, which provide a more comprehensive perspective on the field, enabling the consideration of overall trends in research and development of BCIs for rehabilitation and the treatment of mental and neurological conditions [32].

In this meta-review, our aim is to explore the utilization of BCIs in medicine from a data science perspective. We identify and compare BCI technologies for different data and neurofeedback modalities employed by researchers in various branches of medicine. We conducted our analysis using data obtained from the PubMed database, employing meticulously constructed search queries based on keywords to obtain the most conclusive results with each query.

## 2. Materials and Methods

- As part of the methodology implementation, pub-

lished articles were retrieved from scientific databases using the PubMed search engine (https://pubmed.ncbi.nlm.ni h.gov, accessed on 15 October 2023). At the present moment, a keyword search for BCI yields roughly 6.9 thousand results. In our investigation, we chose not to restrict our scope of research to a specific time window. Instead, we conducted searches through a variety of sources and studies without a specific limit regarding date. The following terms were used in the construction of search queries to perform an analytical review of the current scientific and technical, regulatory, and methodological literature addressingthescientificandtechnicalproblem of biofeedback BCI for rehabilitation, as well as the prevention of cognitive disorders and the diagnosis of patients with motor or cognitive disorders within the framework of rehabilitation medicine: “brain-computer interface” or “BCI” keywords were a mandatory part of the query, while terms for the data (by data, we refer to the type of recorded signal received from the test subject, e.g., “EEG”), modality (by modality we refer to a specific type of input or output mechanism, used to communicate with BCI, e.g., “VR” or “Virtual reality”), and application (e.g., “stroke”) were combined pairwise as shown in Table 1. The query construction scheme is shown in Fig. 1.

- At the initial stage of our review, we identified and

highlighted the following key issues that we wish to address:

– Which types of BCIs are the most frequently utilized in medicine? Are there varying preferences for them in dif-

[Figure 3]

Fig. 1. The query construction scheme for the keywords. Unique identification numbers were assigned to the specific areas of focus. BCI, Brain-computer interface.

ferent areas of medicine? If so, what are the reasons behind these discrepancies?

- – Which data types are the most commonly employed in medicine for BCI? How are the various data types processed and utilized in different applications?
- – Which types of modalities correspond to which fields of application?

In the search phase, papers were considered relevant for review if they contained one of the search terms or an equivalent restatement in their title, abstract, or keywords. The papers with paper types “Book”, “Chapter”, and “Monography” were excluded from the final sample using PubMed search filters. After collecting the number of papers found with each query, we selected the most prominent results and features, and conducted a more detailed review to establish the causes for these features based on specific cases.

We created a keyword co-occurrence network which utilized information gathered from around 2000 papers found in PubMed by using a search query consisting of keywords “BCI” or “Brain-Computer Interface” using VOSviewer version 1.6.19 (Center for Science and Technology Studies, Leiden University, Leiden, The Netherlands) [33]. This network allows us to visualize how often certain terms appear together in the analyzed studies, providing a better understanding of the underlying trends and connections within the field. Through the use of network visualization, we identified clusters, or communities, within the keyword co-occurrence network by color-coding the items according to the cluster to which they belong. We utilized the VOSviewer algorithm in our research, which employs a modularity function to detect these groups [34]. The resulting clusters provide further information and insights into keyword relationships within the field of interest.

#### Table 1. Table of the used keywords.

Data type Modality Application EEG; Audio; limb rehabilitation; EMG; visual; stroke; MEG; vibrotactile; neurodegenerative diseases; NIRS; electrotactile; add or adhd or attention deficit disorder or attention

deficit hyperactivity disorder; fMRI; TES or Transcranial electric stimulation; autistic; ECoG. TMS or Transcranial magnetic stimilation; depression;

VR or virtual reality; anxiety; AR or augmented reality; substances addiction; RHI or rubber hand illusion; coma; XR or extended reality. persistent postural-perceptual dizziness or PPPD;

chronic neuropathic pain; post-traumatic stress disorder or PTSD; schizophrenia.

EEG, Electroencephalography; EMG, Electromyography; MEG, Magnetoencephalography; NIRS, Nearinfrared spectroscopy; fMRI, Functional magnetic resonance imaging; ECoG, Electrocorticography.

## 3. Review

- 3.1 Fundamentals of Brain-Computer Interface (BCI)

By BCI, we refer to a system that allows a user to interact with computers and electronic devices using brain activity. BCIs primarily facilitate communication for people with severe motor impairments [30,32,35–53] who cannot communicate otherwise, but they can also provide useful communication and rehabilitation of various disorders for healthy people or people with less critical motor impairments. BCI research can leverage advances in cognitive neuroscience in addressing learning, feedback analysis, accessibility, concentration, exhaustion, stimulation, stress, and cognitive and psychiatric disorders [1–6,26–29,31,54– 83].

Biofeedback is the primary method of rehabilitation BCI, and it serves as a treatment and research technology based on the patient’s or research participant’s ability to self-regulate. Biofeedback involves learning to voluntarily change a measurable biological parameter that is normally not regulated consciously but can become controllable through exercise. A target signal (e.g., related to a symptom of a disorder) is measured and then fed back to the participant, allowing them to find their own strategy to control that signal and subsequently adjust that strategy to master self-regulation, which can then be extended to daily life. In this way, biofeedback and neurofeedback (biofeedback directed at brain signals) can be used as treatments or as research approaches aimed at testing hypotheses about causal relationships between localized neural activity and symptoms [30].

Biofeedback has been utilized in rehabilitation for over half a century to help establish normal motor patterns following injury, highlighting the significance of analyzing recent progress in this field. It is a technique of providing real-time biological information to patients that would

otherwise be unknown. This information is sometimes referred to as augmented or external feedback, namely, feedback that provides the user with additional information beyond what is available to them naturally, as opposed to sensory (or internal) feedback, which provides the user with information obtained directly from various internal sensory receptors [30]. Biological feedback typically involves measuring a target biomedical variable and transmitting it to the user using one of two strategies: direct, such as in the case of heart rate or respiration mapping [84], and indirect, where the signal undergoes pre-processing, as seen in the case of brain electrical activity signals [54].

Neuronal loss due to stroke leads to 80% of patients undergoing motor rehabilitation, for which brain-computer interfaces and neurofeedback are utilized. During rehabilitation, when patients attempt or imagine performing a movement, the BCI/neurofeedback system provides them with synchronized sensory (e.g., tactile) feedback based on sensorimotor brain activity with the aim of promoting brain plasticity and motor recovery. The combined activation of ascending (i.e., somatosensory) and descending (i.e., motor) networks enables significant functional improvement in motor skills as well as neurophysiologic changes related to sensorimotor skills. Somatosensory abilities are necessary for patients to perceive the feedback provided by the BCI system. Consequently, somatosensory impairments can significantly reduce the effectiveness of BCI-based motor rehabilitation [54].

If feedback is explicitly presented, as is common in most clinical applications, such learning should be referred to as model-based, where the participant intentionally seeks reward, leading to a predominance of top-down regulation involving attention focus and working memory content. In cases of implicit feedback, model-free learning occurs, characterized by a predominance of bottom-up processes

[40]. Dual process theory suggests that conscious and unconscious learning processes (top-down and bottom-up) occur simultaneously. As a result, the learner acquires both some overt strategies and a hidden “intuition” that cannot be explicitly articulated. In the first stage, conscious connections prevail, and as the skill is generally learned, unconscious learning becomes a major contributor to its adaptation.

BCIs can employ various approaches, but one of the most common techniques for limb rehabilitation is known as motor imagination. Motor imagination is a process used in BCI systems where users control devices by imagining themselves moving a limb or part of their body. The user’s imagined movements are detected by the BCI system using a suitable neural sensor. This process generates specific patterns of brain activity, which can then be recognized and transformed into control commands for the associated device or computer. Motor imagination is applicable in a wide range of fields: for the development of BCI, rehabilitation tasks, prediction and prevention of neurodegenerative diseases, psychosis research and diagnosis, and sports. Regarding the general mechanism, biofeedback and neurofeedback are often considered to be based on operant conditioning, meaning that learning to control some biological signal occurs by repeatedly testing and adjusting behavior to achieve more frequent reinforcement (positive feedback) [85]. Biological feedback relies on two basic cognitive skills: the ability to identify the state for which a reward is given (internal feedback) and the ability to adjust the current state towards the desired direction. Therefore, biofeedback can be understood as providing missing information about the performance or outcome of cognitive effort and aiding in fine-tuning internal feedback.

- 3.2 Types of Brain-Computer Interface (BCI)

BCI modality refers to a specific type of input or output mechanism used to communicate with a BCI. Regarding the type of BCI modality, respiratory [84], audio [86], and visual approaches [87,88], vibrotactile [23,37,89–96], electrotactile [97–100], imagined motion approach [30,32, 35–53,101], virtual reality [8,24,88,102–118], transcranial magnetic stimulation [47,48,119–121], and direct transcranial electrical stimulation [66,111,122–125] are commonly recognized (see Fig. 2).

A general operational scheme for the BCI systems is presented in Fig. 3. In a BCI system, data is collected from the user’s brain activity. After that, relevant features are extracted from the data and used to create a control signal. This control signal influences both active external systems and simulated sensory input, which then impacts the user’s performance or experience. This feedback loop provides the basis for real-time interaction between the user and the BCI system. Since we are constantly receiving multiple information inputs simultaneously and from many different sources, a BCI system that can handle and communicate in

[Figure 6]

- Fig. 2. Classification of modalities most commonly used in BCI.

a multi-modal way is particularly suitable for this situation. In view of this, testing an approach that incorporates multisensory feedback in the context of BCI represents a promising direction [126]. It can be posited that multimodal feedback such as visual-tactile or audio-tactile feedback will be more effective than simple unimodal feedback.

[Figure 7]

- Fig. 3. General scheme of implementation of biofeedback system in BCI.

To clarify: modality refers to the ways in which information is presented to the user, while biofeedback techniques involve measuring brain activity and using this data to generate a control signal. These techniques can be implemented using different modalities. The following types of biofeedback can be distinguished according to the methods of application (Fig. 4).

Motor imagery biofeedback. In this variant, the user is asked to imagine moving a specific body part, and the BCI detects and translates brain signals into movements in a virtual environment. The user receives feedback on their performance and over time can learn to control the imagined movements with greater accuracy. Real-time measurements and monitoring of physiological responses such as muscle activity and EEG take place. This method has been proven effective in improving motor function and reducing symptoms in various neurological diseases, including stroke, Parkinson’s disease, and spinal cord injury [30,32,35–53].

Steady State Visual Evoked Potential (SSVEP) stands for Steady State Visual Evoked Potential. This refers to the

[Figure 9]

- Fig. 4. Types of biofeedback distinguished according to the techniques of application. SSVEP, Steady State Visual Evoked Potential.

pattern of brain activity elicited by visual stimulation, such

- as from a computer screen or monitor, displaying a constantly changing pattern of light or color. The specific patterns of brain activity associated with the SSVEP stimulus can be extracted from the measurements and used to control a BCI device. In this variant, the user is presented with a grid of options and asked to focus on the desired outcome. This type of BCI utilizes the potential, which is specific and arises in response to a visual stimulus.

P300 stands for the positive component occurring 300 milliseconds after the onset of a target stimulus. In the P300 neurofeedback system, the user is presented with a series of stimuli and asked to focus on a specific stimulus that will elicit the greatest P300 response. When the user focuses their attention on the target stimulus, they receive a positive reinforcement cue, such as a sound or visual cue. Over time, the user learns to produce larger and more consistent P300 responses to the target stimulus. The BCI detects and decodes the brain signals associated with the response and displays them on a screen. The user receives feedback on their accuracy and can learn to manipulate the brain signals to enhance control speed. The P300 is used to treat a variety of conditions, including ADHD, depression, and anxiety. It is a non-invasive and safe technique that has been demonstrated to be effective in improving attention, cognition, and emotional regulation [58,61,93,94].

Biofeedback Self-Paced Therapy. In this variant, the user is asked to perform movements, such as turning a doorknob, picking up an object, or squeezing a ball. The BCI detects and translates brain signals into movements in a virtual environment, providing feedback on the user’s progress and results. As the user gains skill in managing their brain activity, they are encouraged to increase the difficulty of the tasks. The BCI provides real-time feedback on the user’s performance and adapts the parameters of the training program accordingly. Self-learning therapy can help people with neurological conditions, such as stroke, to improve upper extremity function [127,128].

Biofeedback with real-time translation. In this system, the user wears an BCI device that reads brain signals and

translates them into speech, which can be synthesized and delivered either through a speaker or a headset. The user can communicate by thinking of the words they want to say [129–131]. Biofeedback with real-time translation is not always limited to the use of speech; nonverbal communication techniques, such as blinking, facial expressions, and hand gestures, or motor signals, like muscle contractions and eye movements, can also be utilized. The technology is based on the concept of neuroplasticity—the ability of the nervous system to adapt to changes in the environment or injury. By providing real-time feedback to the user’s brain signals, the BCI can train the user’s brain to produce the brain patterns necessary for speech production. This option is also promising for self-learning foreign languages. In this variant, the user is asked to listen to spoken words and translate them into another language. The BCI detects and translates their brain signals into the desired language, providing real-time feedback. This option can help people learning a new language and people with speech impairments [100,132–134].

3.3 Results and Findings

The VOSviewer analysis identified seven large clusters (each with more than five items), which can be interpreted based on the keywords they contain (Fig. 5, Ref. [135]). First, a signal processing cluster (red lines) includes modalities such as auditory, visual, and P300. Second, is a psychology-related cluster (green lines) which includes visual feedback, transcranial magnetic stimulation, mood and anxiety disorders, depression, and similar applications. The third cluster (blue lines) includes conditions connected with consciousness (coma, wakefulness, locked-in syndrome) as well as functional near-infrared spectroscopy and ECoG methods. Fourth cluster (yellow) is connected with learning approaches, e.g., neural networks, artificial intelligence, virtual reality, with primary applications including autism disorders. The fifth cluster (purple) is the attention cluster consisting of ADHD/ADD (attention deficit disorder ), cognition, pediatrics, and similar keywords. The sixth (cyan) is a neurology cluster focused on neuropathic pains, paralysis, cord and brain injuries, and functional electric stimulation as the main method. Finally, the seventh cluster (orange) is connectedwithstrokerehabilitation, includinghemiparesis, motor recovery, and neurorehabilitation, with transcranial direct current stimulation also included.

Looking at the current trends in the field, as presented in Fig. 6, we can see that clusters 2, 4, and 6, which are associated with cutting-edge strategies such as artificial intelligence and relatively modern applications, exhibit the highest level of activity. Conversely, clusters 1 and 3, representing ideas with a lesser degree of novelty or a narrower focus on specific topics, have experienced a decrease in activity in recent years, potentially due to the lack of innovation or their specialization.

[Figure 11]

- Fig. 5. The co-occurrence network constructed using VOSviewer. The size of the nodes is determined by the weight of the corresponding item, indicating the importance of the item, and the color is determined by the cluster to which the item belongs. The methodology of the VOSviewer visualization technique is detailed in [135].

[Figure 12]

- Fig. 6. The co-occurrence network constructed using VOSviewer. The size of the nodes is determined by the weight of the corresponding item, indicating the importance of the item, and the color is determined by the publishing activity per year (blue color denotes nodes with the majority of publications in 2016 year, and yellow denotes nodes where corresponding publications are from 2022–2023).

Main tables for the various keyword combinations are shown in Figs. 7,8,9. As a first interesting observation from our review, we note the varying popularity of different data types used in BCIs for medical purposes. Some data types seem to be more widely utilized in certain applications, while others are primarily favored in others. We will further

explore the topic of data types and their utilization throughout our review.

3.3.1 Electroencephalography (EEG)

EEG is by far the most popular data acquisition method for BCI applications. This is due to its safety, flex-

[Figure 14]

- Fig. 7. Amount of publications by Application/Data keywords. Box-whiskers plots denote median (red line), standard deviation (whiskers) and quartile range (box) of the corresponding data row or column. PTSD, Post-traumatic stress disorder.

ibility, ease of use, frequency resolution, and affordability. EEG is a quick and easy data gathering method that can be used in practically any environment. In addition, the data can be sampled at high frequency (around 200 Hz or more) which allows for higher resolution and more accurate data collection. The main disadvantage of EEG is low spatial resolution [136–138]. EEG studies are well suited to characterize developing attention disorders such as ADHD (attention deficit hyperactivity disorder) [58–60], and can reliably measure brain function across a wide age range, even in infants, and during wakefulness and sleep. A wide variety of biofeedback applications have used EEG-based BCI systems to improve healthy individuals’ cognitive abilities, speech skills, affect, and pain management, as well as to treat attention deficit, learning disabilities, depression, and autistic disorders [10].

- 3.3.2 Magnetoencephalography (MEG)

While similar to EEG technology, the magnetoencephalography (MEG) technique offers several advantages, including less signal interference, superior temporal resolution, and higher spatial resolution compared to EEG. This makes MEG a crucial tool for classifying epilepsy patients and assisting with surgical planning. Despite its numerous

benefits, MEG also has drawbacks. Firstly, it can only measure magnetic fields oriented parallel to the neural surface, which restricts its access to deep-lying areas. Secondly, it’s an exceptionally pricey technology. Additionally, MEG is prone to external noise interference, which makes it less popular for BCI use [139]. As evident from Figs. 7,8, the number of studies dedicated to MEG is sparse; however, the field of research appears to have potential that remains unexplored. Despite the limited amount of studies concerning the application of MEG, there are promising results for rehabilitation after a stroke and tetraplegia that suggest the field is worth further exploration [140–142].

3.3.3 Functional Magnetic Resonance Imaging (fMRI)

The prevalence of neurofeedback BCIs based on functional magnetic resonance imaging (fMRI) processing in studies on cognitive distortions and disorders is noteworthy [4,29,31,55,68,69,81]. This phenomenon is explained by the combination of low speed of data acquisition and high accuracy offered by fMRI technology. For motor rehabilitation, speed and rapidity are important to ensure comfortable limb control, which requires minimal latency. Delays for fMRI acquisition are typically within seconds, and the machines for acquiring such signals are bulky. However, in

[Figure 16]

##### Fig. 8. Amount of publications by Modality/Data keywords. Box-whiskers plots denote median (red line), standard deviation (whiskers) and quartile range (box) of the corresponding data row or column.

[Figure 17]

#### Fig. 9. Amount of publications by Application/Modality keywords. PPPD, Persistent postural-perceptual dizziness.

the case of cognitive distortions, this delay does not play a major role, as more time is required to think about a task or to elicit a complex psycho-emotional response. In addition, fMRI can more accurately identify the areas responsible for realizing a specific response [143].

So far, fMRI BCI has successfully utilized a variety of mental activities that can be classified into four categories: higher-order cognitive tasks (e.g., mental calculation), covert language-related tasks (e.g., mental speech and mental singing), imagination-related tasks (motor, visual, auditory, tactile, and emotional imagination), and selective attention tasks (visual, auditory, and tactile attention). Although the finite spatial and temporal resolution of fMRI is limited by the physiological properties of the hemodynamic response, technical and analytical advances have led to significantly improved solutions with a more natural character during stimulations [87].

- 3.3.4 Functional Near-Infrared Spectroscopy (fNIRS)

Functional near-infrared spectroscopy (fNIRS) measures the blood flow changes in the local capillary network caused by neuronal activations [144,145]. fNIRS’s main advantages are its relatively low cost, portability, safety, low noise (compared to fMRI), and ease of use. Unlike EEG and MEG, its signals are not as susceptible to electrical noise, since it is an optical imaging modality. The most common brain areas in fNIRS BCI are the primary motor and the prefrontal cortices. In relation to the motor cortex, motor imagery tasks were preferred to motor execution tasks since possible proprioceptive feedback could be avoided. In relation to the prefrontal cortex, fNIRS showed a significant advantage due to diminished hair influence in detecting cognitive tasks like mental arithmetic, music imagery, and emotion induction [108,144,146].

Despite holding immense promise and showcasing impressive results when applied in BCI initiatives, the fNIRS-based approach still has two prominent limitations. The first is the low data transfer rate, and the second is the relatively high level of error in the recognition systems. Both of these limitations hinder real-world applications, although extensive research efforts are underway to address these drawbacks [144,147,148].

- 3.3.5 Electrocorticography (ECoG)

Electrocorticography (ECoG) is a neurosurgical procedure that involves placing electrodes directly on the surface of the brain to record electrical activity. As a result, it is mainly used to treat severe epilepsy and brain tumor cases, where the surgery is already necessary and the benefits outweigh the risks. Additionally, there are no cases of application for psychiatric tasks. The limited use of ECoG in mental health conditions may be due to the invasive nature of the procedure, as well as the lack of clear guidelines for its use in this field [149–151]. While the number of studies on ECoG applications is still confined, there is a flourish-

ing evolution of decoding algorithms happening in recent years [125,152–154]. Various strategies are being considered, such as the use of switching models and the adaptation of algorithms. Furthermore, a thorough examination of the ECoG approaches can be found in the study by Volkova and her co-authors [155].

3.3.6 Comparison

While the limited use of ECoG for the most severe cases, such as stroke, can be explained by the danger of complications and the complexity of the procedure, and there are no cases of application for psychiatric tasks, the low popularity of relatively safe fNIRS and MEG is disappointing (see Fig. 7). The lack of popularity of fNIRS and MEG is likely due to their high cost, limited availability, and relatively complex equipment configurations. Additionally, research groups in these fields often have limited funding, leading to a lack of resources necessary for widespread adoption [156–158]. Despite these limitations, both fNIRS and MEG have the potential to provide valuable insight into the brain’s functions and might be useful in diagnosing and treating certain mental health conditions [159].

The limited use of EEG-based BCI in psychiatric tasks can be attributed to the difficulty of interpreting the data and the potential for false positives. Additionally, the risk of side effects from the procedure, such as psychogenic dizziness or seizures, makes it unsuitable for psychiatric applications [160,161]. This is in contrast to the more widely used functional magnetic resonance imaging (MRI), which boasts a higher degree of accuracy and precision in identifying neural activity associated with mental disorders [162– 164].

When making a comparison between different types of data, the visual data type is seen to be the predominant one. This is not surprising due to its availability, although research using virtual realit (VR), extended reality (XR), and augmented reality (AR) has been steadily increasing in popularity. The most common combination is EEG plus visual neurofeedback. As an alternative variant, fMRI plus VR is quite popular (see Fig. 8).

When analyzing the popularity of queries specifying both application and modality areas of interest, we can see in Fig. 9 that the most common keyword lines are “stroke” and “limb rehabilitation”. In a similar manner to our analysis of queries specifying data and modality pairs, the most commonly searched-for modalities are those related to visual and VR. However, if we disregard the most popular use cases, it is interesting to note that the next most common application and modality categories are related to the treatment of neurodegenerative diseases and attention deficit hyperactivity disorder. In both of the cases we have mentioned regarding neurodegenerative diseases and ADD/ADHD, the most favored modalities of treatment are still visual and VR, followed by transcranial magnetic

stimilation (TMS). On the flip side, the least often-selected modality is electrotactile stimulation. Electrotactile stimulation is the least popular modality for BCI researchers for a few reasons. Compared to the more traditional haptic and tactile systems, the subject’s ability to enumerate electrotactile stimuli decreased with increasing the number of active electrodes [165]. Additionally, although it can still provide useful information, it requires a more complicated setup with multiple electrodes, making this modality much less popular for research and application. It just fails to provide the level of accuracy and convenience as traditional haptic and tactile feedbacks.

## 4. Discussion

The field of rehabilitation BCI seems to have its own research traditions that define its strengths and weaknesses. Specifically, the procedure’s description is one of its strengths, offering a clear understanding of the process and providing important insights into its inner workings. Many studies, even those with somewhat flawed methodology, contain an in-depth description of their procedure or

- at least cite a previously published protocol in reference to their own methods.

This level of transparency and dedication to the description of the procedures used in research provides clarity and a better understanding of the study for readers. On the other hand, the tendency to study the effect of combined treatments, e.g., BCI with biofeedback plus relaxation training, should be noted, as it is the intervention using biofeedback alone that should be investigated more thoroughly. Most studies also contain a sufficient description of the sample and (to a lesser extent) all necessary information about statistical treatment. From a methodological point of view, most controlled studies randomize participants [2,3,5,6,82,83].

However, some studies show difficulties in rehabilitation in cases where somatosensory imagery included only two contralateral body parts that are relatively far apart in physical and somatotopic space and whose representations are on contralateral sides of the body. The classification obtained by the BCI may have been based solely on less specific images associated with a side of the body. However, the fact that classification success was highest in primary somatosensory cortex and related to the degree of somatotopy in discriminative weighting maps indicates that subjects used a limb-specific somatosensory imagery strategy rather than a body-side-related strategy [166].

In addition, several clinical studies have reported that repeated use of BCI systems after stroke can induce neurologic recovery, but the clinical efficacy and effect size of repeated BCI-based neurorehabilitation training were previously unknown. At the same time, the effect of BCI-based neurorehabilitation on upper limb motor function in studies where effect size was indicated was larger than with other traditional treatments. In addition to motor outcomes, sev-

eral studies also reported BCI-induced functional and structural neuroplasticity at the subclinical level, some of which also correlated with improved motor outcomes. Additional studies with larger sample sizes are needed to improve the reliability of these results.

In motor rehabilitation after stroke, research shows that BCI combined with functional electrical stimulation induces significant, clinically meaningful, and long-lasting recovery of motor function in chronic stroke survivors more effectively than sham electrical stimulation. Such recovery is associated with quantitative evidence of functional neuroplasticity. Patients with BCI demonstrate significant functional recovery after intervention, which persists 6–12 months after the end of therapy. Electroencephalography analysis reveals significant differences in favor of the BCI groups, mainly consisting of an increase in functional connectivity between motor areas in the affected hemisphere. This increase correlates significantly with functional improvement. The results show how therapy can promote significant functional recovery and goal-directed plasticity through conditioned activation of the body’s natural efferent and afferent pathways [112,117,120].

BCI is being used in a variety of mental health applications, including the monitoring of stress and mood [167,168], the detection of abnormal thoughts and emotions [56,62], and the delivery of cognitive-behavioral therapies [55]. OneofthemainwaysBCIisbeingusedtotreatmental conditions is through the implementation of brain-computer interfaces for neuromodulation [169–171]. These devices use brain activity as input to deliver targeted stimulation to specific areas in the brain, which can be used to modulate brain activity and improve symptoms for a range of mental disorders and neuropsychiatric conditions. Additionally, biofeedback allows patients to learn how to control and improve their mood and cognitive condition.

It is worth noting the success of training incorporating biofeedback to reduce clinically assessed depression, as measured by Montgomery-Asberg Depression Rating Scale (MADRS) [172] and Hamilton Depression Rating Scale (HAM-D) [173], and changes in frontal and central theta and alpha bands. In a group of drug addicts convicted of robbery, some improvement in the HAM-D scale was shown after infra-low frequency (0.01–0.02 Hz) neurofeedback with simultaneous suppression of a number of frequency bands between 1–40 Hz [174]. Neurofeedback improves impulsivity and clinical symptoms of anxiety and depression in long-term abstainers from cocaine and heroin better than placebo [54].

Let’s delve into further advances in the perspective of tactile BCIs for rehabilitation tasks. A neuromorphic artificial sense of touch should be highlighted as one of the promising directions in the development of tactile paradigms. This system enables the encoding of tactile information using a sequence of spikes, closely mimicking the neural dynamics of human mechanoreceptors. The neu-

romorphic fingertip demonstrated the capability to encode naturalistic textures with a remarkably high degree of discriminability, achieving up to 97% accuracy at a 10% probability level, as detailed in the work of Rongala et al. [175].

However, the literature on interoceptive processes [176] suggests that an individual’s psychophysiological control potentially influences components of embodiment, such as body ownership. It is hypothesized that breathing biofeedback techniques [177], similar to those employed in contemplative mental training and biofeedback, may exert aninfluenceontheembodimentprocessrelatedtolimbcontrol. A study conducted by Barresi et al. [84] presents preliminary results indicating how self-regulation techniques, particularly via breath control, can enhance the processes of limb mastery underlying virtual right-hand embodiment.

We examined BCIs for rehabilitation and treatment in the review, but there are numerous other equally important applications, including Locked-In Syndrome (LiS) and Amyotrophic Lateral Sclerosis (ALS), which require further development to facilitate communication with the user [131,178]. The general principles of BCI usage in support of individuals with LiS were rigorously examined in a study by Kübler [129]. Another study on LiS BCI by Branco et al. [130] demonstrated that individuals with LiS consider both direct and indirect communication, general computer use, and environmental control to be essential features of a BCI. Additionally, they showed that attempted speech and movement as control strategies are preferred over reactive strategies such as P300 and SSVEPs.

Newer reviews on ALS indicate that the most prominent applications for machine learning methods in BCI involve diagnosis (72.22%), communication (22.22%), and survival prediction (5.56%) [179,180]. Invasive speechbased BCI platforms are known to face certain challenges, including the need for retraining and recalibration of the decoding algorithm over a prolonged timeframe [181]. However, recent advances in the development of speechBCIsdemonstratethatachronically implantedECoG-based speech BCI can reliably control assistive devices over extended periods with only initial model training and calibration [181].

The field of BCIs is replete with numerous challenges and potential outlooks for the future [11,27,40,136,137]. These challenges encompass various areas, including the improvement of decoding algorithms, the enhancement of neural signal processing, and the development of technologies and designs that are more user-friendly and costeffective. One of the major issues in this field is explainability and uncertainty quantification: BCI systems generate predictions that inherently possess a degree of uncertainty [182]. There is a pressing need to devise methods for quantifying and evaluating this uncertainty in a transparent manner for users to interpret meaningfully. These advancements are closely linked to explainability, which pertains to the capacity to elucidate the workings of a complex black-

box system, such as BCIs, to users. Providing comprehensible explanations for BCI system predictions is crucial for fostering adoption [183].

The mostprevalenttermsthat have gained prominence overthepasttwoyears, someofwhichareoutlinedinFig.6, include depression, mood disorders, artificial intelligence, neuroimaging, ADHD, and functional electrical stimulation. It is logical to expect more research and work related to BCI in these areas in the near future.

As for the instrumental challenges, we can highlight several directions. The first direction includes engineering problems associated with cumbersome EEG systems. These challenges are being addressed through the development of more compact and affordable EEG devices, as well as dry EEG technology, which offers increased comfort for the user [184–186].

The second challenge pertains to the usage of passive BCIs. Effortsare being made to develop personalized applications of this technology, including fatigue monitoring and personalized medicine. A systematic review of BCI studies for mental fatigue detection using artificial intelligence (AI) techniques was conducted by Yaacob et al. [187]. Although the field of passive BCIs is not widely discussed, a few concise reviews, especially those focused on personalized medicine, have been published in the last three years [188–190].

A major weakness in the field of research in the area of BCI is the prevalence of a large number of pilot studies. While these studies play an essential role in laying the groundwork for future research, the vast majority of data from such studies cannot be replicated or confirmed, leading to an overall decrease in the quality of research in the field. Small-scale studies are beneficial in the early stages of developing a technology or protocol as they provide important insights and data that can be used to fine-tune the overall design. It is understandable that these types of studies are limited in number, especially when the protocols are only described in one or two previous papers. However, the lack of a control group makes it impossible to account for any influence factors unrelated to treatment, such as spontaneous seasonal variations in depression severity.

A second weakness is the absence of rigorous repeated studies. Independent replicated studies are particularly needed in the field of BCI using fMRI biofeedback, which may currently be hindered by the complexity of the technology and the limited number of research groups conducting studies in parallel to EEG biofeedback protocols, such as frontal alpha asymmetry, environmental rhythm variability regulation, and training [174].

It is important to highlight that our research has certain limitations. Firstly, we acknowledge that we were unable to conduct a rigorous examination of every paper for compliance with its respective field of interest. Given that we utilized a large sample of papers obtained from the PubMed database, it was not feasible to manually review each one.

We attempted to address this limitation by implementing various filters and inclusion criteria to generate appropriate keywords for selection. However, it is important to note that using this methodology does not guarantee the exclusion of unsuitable papers from the final sample, as there is always the possibility of some irrelevant articles being included. Nevertheless, we can assert that the number of such papers is relatively small and did not significantly impact

- our results due to the thorough screening process and the utilization of appropriate filters and inclusion criteria.

5. Conclusions

BCIs have been used for many years to assist patients and clinicians during rehabilitation. This paper reviews the applications of BCIs with various types of input data and modalities currently utilized in rehabilitation and categorizes different biofeedback techniques. We identify clusters of methods and applications that show a rapid increase in publications, reflecting changing trends in the field. There is an increasing focus on AI and newer applications related to ADHD and anxiety disorders.

While exploring the advantages and drawbacks of the various data types and modalities for BCIs, it becomes evident that each has its unique strengths and weaknesses. This discussion emphasizes the necessity for a comprehensive understanding of each method so that engineers can properly design and build BCI systems, optimizing the use of these distinct options.

The information presented in this meta-review is organized and compiled in an easy-to-digest manner, making it particularly useful for specialists working in the field of biofeedback, brain-computer interfaces, and related medical disciplines. By providing a clear overview of the vari-

- ous options and their associated benefits and limitations, the paper serves as a valuable guide and reference material for professionals seeking to apply and utilize different methods and approaches in their work.

## Availability of Data and Materials

The data presented in this study are available on request from the corresponding author.

## Author Contributions

SK, AB, OD, and AH designed the study. VK, VA, and AK collected the data. VK, SK, EP, AA, and VG analyzed the data. VK, SK, and AB drafted the manuscript. OD, AK, and AH edited and approved the manuscript. All authors contributed to editorial changes in the manuscript. All authors read and approved the final manuscript. All authors have participated sufficiently in the work and agreed to be accountable for all aspects of the work.

## Ethics Approval and Consent to Participate

Not applicable.

## Acknowledgment

Not applicable.

## Funding

This work was supported by the Russian Ministry of Healthaspartofthescientificwork“Developmentofamultimodal biofeedback-based hardware and software system for rehabilitation of patients with cognitive and motor disorders of different nature”, No. 123020600127-4, performed at the National Medical Research Center for Therapy and Preventive Medicine in 2023-2025.

## Conflict of Interest

The authors declare no conflict of interest.

## References

- [1] Papanastasiou G, Drigas A, Skianis C, Lytras M. Brain computer interface based applications for training and rehabilitation of students with neurodevelopmental disorders. A literature review. Heliyon. 2020; 6: e04250.
- [2] Zotev V, Mayeli A, Misaki M, Bodurka J. Emotion selfregulation training in major depressive disorder using simultaneous real-time fMRI and EEG neurofeedback. NeuroImage: Clinical. 2020; 27: 102331.
- [3] Takamura M, Okamoto Y, Shibasaki C, Yoshino A, Okada G, Ichikawa N, et al. Antidepressive effect of left dorsolateral prefrontal cortex neurofeedback in patients with major depressive disorder: A preliminary report. Journal of Affective Disorders. 2020; 271: 224–227.
- [4] Herwig U, Lutz J, Scherpiet S, Scheerer H, Kohlberg J, Opialla S, et al. Training emotion regulation through real-time fMRI neurofeedback of amygdala activity. NeuroImage. 2019; 184: 687–696.
- [5] Mennen AC, Norman KA, Turk-Browne NB. Attentional bias in depression: understanding mechanisms to improve training and treatment. Current Opinion in Psychology. 2019; 29: 266–273.
- [6] Zotev V, Bodurka J. Effects of simultaneous real-time fMRI and EEG neurofeedback in major depressive disorder evaluated with brain electromagnetic tomography. NeuroImage: Clinical. 2020; 28: 102459.
- [7] Hramov AE, Maksimenko VA, Pisarchik AN. Physical principles of brain–computer interfaces and their applications for rehabilitation, robotics and control of human brain states. Physics Reports. 2021; 918: 1–133.
- [8] Wen D, Liang B, Zhou Y, Chen H, Jung TP. The Current Research of Combining Multi-Modal Brain-Computer Interfaces With Virtual Reality. IEEE Journal of Biomedical and Health Informatics. 2021; 25: 3278–3287.
- [9] Venkatesan M, Mohan H, Ryan JR, Schürch CM, Nolan GP, Frakes DH, et al. Virtual and augmented reality for biomedical applications. Cell Reports. Medicine. 2021; 2: 100348.
- [10] LaMarca K, Gevirtz R, Lincoln AJ, Pineda JA. Brain-Computer Interface Training of mu EEG Rhythms in Intellectually Impaired Children with Autism: A Feasibility Case Series. Applied Psychophysiology and Biofeedback. 2023; 48: 229–245.
- [11] Khare SK, March S, Barua PD, Gadre VM, Acharya UR. Application of data fusion for automated detection of children with developmental and mental disorders: A systematic review of the last decade. Information Fusion. 2023; 99: 101898.
- [12] Khare SK, Blanes-Vidal V, Nadimi ES, Acharya UR. Emotion recognition and artificial intelligence: A systematic review

- (2014–2023) and research recommendations. Information Fusion. 2024; 102: 102019.
- [13] Khare SK, Acharya UR. Adazd-Net: Automated adaptive and explainable Alzheimer’s disease detection system using EEG signals. Knowledge-Based Systems. 2023; 278: 110858.
- [14] Khare SK, Gadre VM, Acharya R. ECGPsychNet: an optimized hybrid ensemble model for automatic detection of psychiatric disorders using ECG signals. Physiological Measurement. 2023; 44: 115004.
- [15] Aydemir E, Baygin M, Dogan S, Tuncer T, Barua PD, Chakraborty S, et al. Mental performance classification using fused multilevel feature generation with EEG signals. International Journal of Healthcare Management. 2023; 16: 574–587.
- [16] Loh HW, Ooi CP, Oh SL, Barua PD, Tan YR, Molinari F, et al. Deep neural network technique for automated detection of ADHD and CD using ECG signal. Computer Methods and Programs in Biomedicine. 2023; 241: 107775.
- [17] Loh HW, Ooi CP, Oh SL, Barua PD, Tan YR, Acharya UR, et al. Adhd/cd-net: automated eeg-based characterization of adhd and cd using explainable deep neural network technique. Cognitive Neurodynamics. 2023; 1–17.
- [18] Stoyanov D, Kandilarova S, Kherif F. Toward Methodology for Strategic Innovations in Translational and Computational Neuroscience in Psychiatry. Computational Neuroscience. Springer US: New York, NY. 2023.
- [19] Stoyanov D, Kandilarova S, Aryutova K, Paunova R, TodevaRadneva A, Latypova A, et al. Multivariate Analysis of Structural and Functional Neuroimaging Can Inform Psychiatric Differential Diagnosis. Diagnostics. 2020; 11: 19.
- [20] Stojanov D, Korf J, de Jonge P, Popov G. The possibility of evidence-based psychiatry: depression as a case. Clinical Epigenetics. 2011; 2: 7–15.
- [21] Stoyanov D. Methodological challenges before translation from psychopathology to neuroscience: top-down or bottom-up models? Dialogues in Philosophy, Mental & Neuro Sciences. 2020; 13.
- [22] Cho G, Yim J, Choi Y, Ko J, Lee SH. Review of Machine Learning Algorithms for Diagnosing Mental Illness. Psychiatry Investigation. 2019; 16: 262–269.
- [23] Huang X, Liang S, Li Z, Lai CYY, Choi KS. EEG-based vibrotactile evoked brain-computer interfaces system: A systematic review. PLoS ONE. 2022; 17: e0269001.
- [24] Said RR, Heyat MBB, Song K, Tian C, Wu Z. A Systematic Review of Virtual Reality and Robot Therapy as Recent Rehabilitation Technologies Using EEG-Brain-Computer Interface Based on Movement-Related Cortical Potentials. Biosensors. 2022; 12: 1134.
- [25] Hu Z, Lin L, Lin W, Xu Y, Xia X, Peng Z, et al. Machine Learning for Tactile Perception: Advancements, Challenges, and Opportunities. Advanced Intelligent Systems. 2023; 5: 2200371.
- [26] Thabrew H, Ruppeldt P, Sollers JJ, 3rd. Systematic Review of Biofeedback Interventions for Addressing Anxiety and Depression in Children and Adolescents with Long-Term Physical Conditions. Applied Psychophysiology and Biofeedback. 2018; 43: 179–192.
- [27] Paret C, Goldway N, Zich C, Keynan JN, Hendler T, Linden D, et al. Current progress in real-time functional magnetic resonance-based neurofeedback: Methodological challenges and achievements. NeuroImage. 2019; 202: 116107.
- [28] Kadosh KC, Staunton G. A systematic review of the psychological factors that influence neurofeedback learning outcomes. NeuroImage. 2019; 185: 545–555.
- [29] Fede SJ, Dean SF, Manuweera T, Momenan R. A Guide to Literature Informed Decisions in the Design of Real Time fMRI Neurofeedback Studies: A Systematic Review. Frontiers in Human Neuroscience. 2020; 14: 60.

- [30] Ladda AM, Lebon F, Lotze M. Using motor imagery practice for improving motor performance - A review. Brain and Cognition. 2021; 150: 105705.
- [31] Linhartová P, Látalová A, Kóša B, Kašpárek T, Schmahl C, Paret C. fMRI neurofeedback in emotion regulation: A literature review. NeuroImage. 2019; 193: 75–92.
- [32] Pillette L, Lotte F, N’Kaoua B, Joseph PA, Jeunet C, Glize B. Why we should systematically assess, control and report somatosensory impairments in BCI-based motor rehabilitation after stroke studies. NeuroImage: Clinical. 2020; 28: 102417.
- [33] Waltman L, van Eck NJ, Noyons ECM. A unified approach to mapping and clustering of bibliometric networks. Journal of Informetrics. 2010; 4: 629–635.
- [34] Waltman L, Van Eck NJ. A smart local moving algorithm for large-scale modularity-based community detection. The European Physical Journal B. 2013; 86: 1–14.
- [35] Frolov NS, Pitsik EN, Maksimenko VA, Grubov VV, Kiselev AR, Wang Z, et al. Age-related slowing down in the motor initiation in elderly adults. PLoS ONE. 2020; 15: e0233942.
- [36] Hramov AE, Grubov V, Badarin A, Maksimenko VA, Pisarchik AN. Functional Near-Infrared Spectroscopy for the Classification of Motor-Related Brain Activity on the Sensor-Level. Sensors. 2020; 20: 2362.
- [37] Grigorev NA, Savosenkov AO, Lukoyanov MV, Udoratina A, Shusharina NN, Kaplan AY, et al. A BCI-Based Vibrotactile Neurofeedback Training Improves Motor Cortical Excitability During Motor Imagery. IEEE Transactions on Neural Systems and Rehabilitation Engineering. 2021; 29: 1583–1592.
- [38] Abidi M, de Marco G, Grami F, Termoz N, Couillandre A, Querin G, et al. Neural Correlates of Motor Imagery of Gait in Amyotrophic Lateral Sclerosis. Journal of Magnetic Resonance Imaging. 2021; 53: 223–233.
- [39] Wang L, Zhang Y, Zhang J, Sang L, Li P, Yan R, et al. Aging Changes Effective Connectivity of Motor Networks During Motor Execution and Motor Imagery. Frontiers in Aging Neuroscience. 2019; 11: 312.
- [40] Yazmir B, Reiner M. Neural Correlates of User-initiated Motor Success and Failure - A Brain-Computer Interface Perspective. Neuroscience. 2018; 378: 100–112.
- [41] Wright DJ, Wood G, Eaves DL, Bruton AM, Frank C, Franklin ZC. Corticospinal excitability is facilitated by combined action observation and motor imagery of a basketball free throw. Psychology of Sport and Exercise. 2018; 39: 114–121.
- [42] Yoxon E, Welsh TN. Motor system activation during motor imagery is positively related to the magnitude of cortical plastic changes following motor imagery training. Behavioural Brain Research. 2020; 390: 112685.
- [43] Yoxon E, Welsh TN. Rapid motor cortical plasticity can be induced by motor imagery training. Neuropsychologia. 2019; 134: 107206.
- [44] Ruffino C, Gaveau J, Papaxanthis C, Lebon F. An acute session of motor imagery training induces use-dependent plasticity. Scientific Reports. 2019; 9: 20002.
- [45] Bruno V, Fossataro C, Garbarini F. Inhibition or facilitation? Modulation of corticospinal excitability during motor imagery. Neuropsychologia. 2018; 111: 360–368.
- [46] Kraeutner SN, El-Serafi M, Lee J, Boe SG. Disruption of motor imagery performance following inhibition of the left inferior parietal lobe. Neuropsychologia. 2019; 127: 106–112.
- [47] Kang JH, Kim MW, Park KH, Choi YA. The effects of additional electrical stimulation combined with repetitive transcranial magnetic stimulation and motor imagery on upper extremity motor recovery in the subacute period after stroke: A preliminary study. Medicine. 2021; 100: e27170.
- [48] Pan W, Wang P, Song X, Sun X, Xie Q. The Effects of Combined Low Frequency Repetitive Transcranial Magnetic Stimu-

- lation and Motor Imagery on Upper Extremity Motor Recovery Following Stroke. Frontiers in Neurology. 2019; 10: 96.
- [49] Chholak P, Niso G, Maksimenko VA, Kurkin SA, Frolov NS, Pitsik EN, et al. Visual and kinesthetic modes affect motor imagery classification in untrained subjects. Scientific Reports. 2019; 9: 9838.
- [50] Krüger B, Hettwer M, Zabicki A, de Haas B, Munzert J, Zentgraf K. Practice modality of motor sequences impacts the neural signature of motor imagery. Scientific Reports. 2020; 10: 19176.
- [51] Jia T, Mo L, Li C, Liu A, Li Z, Ji L. 5 Hz rTMS improves motorimagery based BCI classification performance. Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference. 2021; 2021: 6116–6120.
- [52] Décombe A, Brunel L, Murday V, Osiurak F, Capdevielle D, Raffard S. Getting a tool gives wings even in schizophrenia: underestimation of tool-related effort in a motor imagery task. NPJ Schizophrenia. 2021; 7: 45.
- [53] Ravindran A, Rieke JD, Zapata JDA, White KD, Matarasso A, Yusufali MM, et al. Four methods of brain pattern analyses of fMRI signals associated with wrist extension versus wrist flexion studied for potential use in future motor learning BCI. PLoS ONE. 2021; 16: e0254338.
- [54] Corominas-Roso M, Ibern I, Capdevila M, Ramon R, Roncero C, Ramos-Quiroga JA. Benefits of EEG-Neurofeedback on the Modulation of Impulsivity in a Sample of Cocaine and Heroin Long-Term Abstinent Inmates: A Pilot Study. International Journal of Offender Therapy and Comparative Criminology. 2020; 64: 1275–1298.
- [55] MacDuffie KE, MacInnes J, Dickerson KC, Eddington KM, Strauman TJ, Adcock RA. Single session real-time fMRI neurofeedback has a lasting impact on cognitive behavioral therapy strategies. NeuroImage: Clinical. 2018; 19: 868–875.
- [56] Mehler DMA, Sokunbi MO, Habes I, Barawi K, Subramanian L, Range M, et al. Targeting the affective brain-a randomized controlled trial of real-time fMRI neurofeedback in patients with depression. Neuropsychopharmacology. 2018; 43: 2578–2585.
- [57] Elbogen EB, Alsobrooks A, Battles S, Molloy K, Dennis PA, Beckham JC, et al. Mobile Neurofeedback for Pain Management in Veterans with TBI and PTSD. Pain Medicine. 2021; 22: 329– 337.
- [58] Thibault RT, Veissière S, Olson JA, Raz A. Treating ADHD With Suggestion: Neurofeedback and Placebo Therapeutics. Journal of Attention Disorders. 2018; 22: 707–711.
- [59] Pigott HE, Cannon R, Trullinger M. The Fallacy of ShamControlled Neurofeedback Trials: A Reply to Thibault and Colleagues (2018). Journal of Attention Disorders. 2021; 25: 448– 457.
- [60] Ros T, Enriquez-Geppert S, Zotev V, Young KD, Wood G, Whitfield-Gabrieli S, et al. Consensus on the reporting and experimental design of clinical and cognitive-behavioural neurofeedback studies (CRED-nf checklist). Brain. 2020; 143: 1674– 1685.
- [61] Lin IM, Fan SY, Yen CF, Yeh YC, Tang TC, Huang MF, et al. Heart Rate Variability Biofeedback Increased Autonomic Activation and Improved Symptoms of Depression and Insomnia among Patients with Major Depression Disorder. Clinical Psychopharmacology and Neuroscience. 2019; 17: 222–232.
- [62] Zhao G, Zhang Y, Ge Y. Frontal EEG Asymmetry and Middle Line Power Difference in Discrete Emotions. Frontiers in Behavioral Neuroscience. 2018; 12: 225.
- [63] Yu SH, Tseng CY, Lin WL. A Neurofeedback Protocol for Executive Function to Reduce Depression and Rumination: A Controlled Study. Clinical Psychopharmacology and Neuroscience. 2020; 18: 375–385.
- [64] Tschiesner R. Infra-Low-Frequency Neurofeedback Treatment

- in Dysthymia: A Case Study. Behavioral Sciences. 2023; 13: 711.
- [65] Dobrushina OR, Dobrynina LA, Arina GA, Kremneva EI, Novikova ES, Gubanova MV, et al. Enhancing Brain Connectivity With Infra-Low Frequency Neurofeedback During Aging: A Pilot Study. Frontiers in Human Neuroscience. 2022; 16: 891547.
- [66] Guleken Z, Eskikurt G, Karamürsel S. Investigation of the effects of transcranial direct current stimulation and neurofeedback by continuous performance test. Neuroscience Letters. 2020; 716: 134648.
- [67] Bostanov V, Ohlrogge L, Britz R, Hautzinger M, Kotchoubey B. Measuring Mindfulness: A Psychophysiological Approach. Frontiers in Human Neuroscience. 2018; 12: 249.
- [68] Barreiros AR, Almeida I, Baía BC, Castelo-Branco M. Amygdala Modulation During Emotion Regulation Training With fMRI-Based Neurofeedback. Frontiers in Human Neuroscience. 2019; 13: 89.
- [69] Lorenzetti V, Melo B, Basílio R, Suo C, Yücel M, Tierra-Criollo CJ, et al. Emotion Regulation Using Virtual Environments and Real-Time fMRI Neurofeedback. Frontiers in Neurology. 2018; 9: 390.
- [70] De Filippi E, Wolter M, Melo BRP, Tierra-Criollo CJ, Bortolini T, Deco G, et al. Classification of Complex Emotions Using EEG and Virtual Environment: Proof of Concept and Therapeutic Implication. Frontiers in Human Neuroscience. 2021; 15: 711279.
- [71] Quevedo K, Liu G, Teoh JY, Ghosh S, Zeffiro T, Ahrweiler N, et al. Neurofeedback and neuroplasticity of visual self-processing in depressed and healthy adolescents: A preliminary study. Developmental Cognitive Neuroscience. 2019; 40: 100707.
- [72] Ahrweiler N, Santana-Gonzalez C, Zhang N, Quandt G, Ashtiani N, Liu G, et al. Neural Activity Associated with Symptoms Change in Depressed Adolescents following Self-Processing Neurofeedback. Brain Sciences. 2022; 12: 1128.
- [73] Berger CC, Coppi S, Ehrsson HH. Synchronous motor imagery and visual feedback of finger movement elicit the moving rubber hand illusion, at least in illusion-susceptible individuals. Experimental Brain Research. 2023; 241: 1021–1039.
- [74] Lio G, Fadda R, Doneddu G, Duhamel JR, Sirigu A. Digittracking as a new tactile interface for visual perception analysis. Nature Communications. 2019; 10: 5392.
- [75] Sarkheil P, Klasen M, Schneider F, Goebel R, Mathiak K. Amygdala response and functional connectivity during cognitive emotion regulation of aversive image sequences. European Archives of Psychiatry and Clinical Neuroscience. 2019; 269: 803–811.
- [76] Zhao Z, Yao S, Li K, Sindermann C, Zhou F, Zhao W, et al. Real-Time Functional Connectivity-Informed Neurofeedback of Amygdala-Frontal Pathways Reduces Anxiety. Psychotherapy and Psychosomatics. 2019; 88: 5–15.
- [77] Tsuchiyagaito A, Misaki M, Zoubi OA, Tulsa 1000 Investigators, Paulus M, Bodurka J. Prevent breaking bad: A proof of concept study of rebalancing the brain’s rumination circuit with real-time fMRI functional connectivity neurofeedback. Human Brain Mapping. 2021; 42: 922–940.
- [78] Lubianiker N, Goldway N, Fruchtman-Steinbok T, Paret C, Keynan JN, Singer N, et al. Process-based framework for precise neuromodulation. Nature Human Behaviour. 2019; 3: 436–445.
- [79] Keynan JN, Cohen A, Jackont G, Green N, Goldway N, Davidov A, et al. Electrical fingerprint of the amygdala guides neurofeedback training for stress resilience. Nature Human Behaviour. 2019; 3: 63–73.
- [80] Skottnik L, Linden DEJ. Mental Imagery and Brain RegulationNew Links Between Psychotherapy and Neuroscience. Frontiers in Psychiatry. 2019; 10: 779.

- [81] Hellrung L, Dietrich A, Hollmann M, Pleger B, Kalberlah C, Roggenhofer E, et al. Intermittent compared to continuous realtime fMRI neurofeedback boosts control over amygdala activation. NeuroImage. 2018; 166: 198–208.
- [82] Quevedo K, Yuan Teoh J, Engstrom M, Wedan R, SantanaGonzalez C, Zewde B, et al. Amygdala Circuitry During Neurofeedback Training and Symptoms’ Change in Adolescents With Varying Depression. Frontiers in Behavioral Neuroscience. 2020; 14: 110.
- [83] Young KD, Siegle GJ, Misaki M, Zotev V, Phillips R, Drevets WC, et al. Altered task-based and resting-state amygdala functional connectivity following real-time fMRI amygdala neurofeedback training in major depressive disorder. NeuroImage. Clinical. 2017; 17: 691–703.
- [84] Barresi G, Marinelli A, Caserta G, de Zambotti M, Tessadori J, Angioletti L, et al. Exploring the Embodiment of a Virtual Hand in a Spatially Augmented Respiratory Biofeedback Setting. Frontiers in Neurorobotics. 2021; 15: 683653.
- [85] Lehrer P, Kaur K, Sharma A, Shah K, Huseby R, Bhavsar J, et al. Heart Rate Variability Biofeedback Improves Emotional and Physical Health and Performance: A Systematic Review and Meta Analysis. Applied Psychophysiology and Biofeedback. 2020; 45: 109–129.
- [86] Zhang B, Zhou Z, Jiang J. A 36-Class Bimodal ERP BrainComputer Interface Using Location-Congruent Auditory-Tactile Stimuli. Brain Sciences. 2020; 10: 524.
- [87] Sorger B, Goebel R. Real-time fMRI for brain-computer interfacing. Handbook of Clinical Neurology. 2020; 168: 289–302.
- [88] Huggins JE, Guger C, Aarnoutse E, Allison B, Anderson CW, Bedrick S, et al. Workshops of the Seventh International BrainComputer Interface Meeting: Not Getting Lost in Translation. Brain Computer Interfaces. 2019; 6: 71–101.
- [89] Eidel M, Kübler A. Identifying potential training factors in a vibrotactile P300-BCI. Scientific Reports. 2022; 12: 14006.
- [90] Hehenberger L, Sburlea AI, Müller-Putz GR. Assessing the impact of vibrotactile kinaesthetic feedback on electroencephalographic signals in a center-out task. Journal of Neural Engineering. 2020; 17: 056032.
- [91] Spataro R, Xu Y, Xu R, Mandalà G, Allison BZ, Ortner R, et al. How brain-computer interface technology may improve the diagnosis of the disorders of consciousness: A comparative study. Frontiers in Neuroscience. 2022; 16: 959339.
- [92] Batistić L, Sušanj D, Pinčić D, Ljubic S. Motor Imagery Classification Based on EEG Sensing with Visual and Vibrotactile Guidance. Sensors. 2023; 23: 5064.
- [93] Jin J, Chen Z, Xu R, Miao Y, Wang X, Jung TP. Developing a Novel Tactile P300 Brain-Computer Interface With a CheeksStimParadigm.IEEETransactionsonBio-MedicalEngineering. 2020; 67: 2585–2593.
- [94] Guger C, Spataro R, Pellas F, Allison BZ, Heilinger A, Ortner R, et al. Assessing Command-Following and Communication With Vibro-Tactile P300 Brain-Computer Interface Tools in Patients With Unresponsive Wakefulness Syndrome. Frontiers in Neuroscience. 2018; 12: 423.
- [95] Murovec N, Heilinger A, Xu R, Ortner R, Spataro R, La Bella V, et al. Effects of a Vibro-Tactile P300 Based Brain-Computer Interface on the Coma Recovery Scale-Revised in Patients With Disorders of Consciousness. Frontiers in Neuroscience. 2020; 14: 294.
- [96] Candreia C, Rust HM, Honegger F, Allum JHJ. The Effects of Vibro-Tactile Biofeedback Balance Training on Balance Control and Dizziness in Patients with Persistent Postural-Perceptual Dizziness (PPPD). Brain Sciences. 2023; 13: 782.
- [97] Novičić M, Savić AM. Somatosensory Event-Related Potential as an Electrophysiological Correlate of Endogenous Spatial Tactile Attention: Prospects for Electrotactile Brain-Computer In-

- terface for Sensory Training. Brain Sciences. 2023; 13: 766.
- [98] Savić AM, Novičić M, Ðorđević O, Konstantinović L, MilerJerković V. Novel electrotactile brain-computer interface with somatosensory event-related potential based control. Frontiers in Human Neuroscience. 2023; 17: 1096814.
- [99] Xu R, Dosen S, Jiang N, Yao L, Farooq A, Jochumsen M, et al. Continuous 2D control via state-machine triggered by endogenous sensory discrimination and a fast brain switch. Journal of Neural Engineering. 2019; 16: 056001.
- [100] Hsu HT, Shyu KK, Hsu CC, Lee LH, Lee PL. PhaseApproaching Stimulation Sequence for SSVEP-Based BCI: A Practical Use in VR/AR HMD. IEEE Transactions on Neural Systems and Rehabilitation Engineering. 2021; 29: 2754–2764.
- [101] Chancel M, Ehrsson HH. Proprioceptive uncertainty promotes the rubber hand illusion. Cortex. 2023; 165: 70–85.
- [102] Mahmood M, Kim N, Mahmood M, Kim H, Kim H, Rodeheaver N, et al. VR-enabled portable brain-computer interfaces via wireless soft bioelectronics. Biosensors & Bioelectronics. 2022; 210: 114333.
- [103] Sánchez-Cuesta FJ, Arroyo-Ferrer A, González-Zamorano Y, Vourvopoulos A, Badia SBI, Figuereido P, et al. Clinical Effects of Immersive Multimodal BCI-VR Training after Bilateral Neuromodulation with rTMS on Upper Limb Motor Recovery after Stroke. A Study Protocol for a Randomized Controlled Trial. Medicina. 2021; 57: 736.
- [104] Wen D, Fan Y, Hsu SH, Xu J, Zhou Y, Tao J, et al. Combining brain-computer interface and virtual reality for rehabilitation in neurological diseases: A narrative review. Annals of Physical and Rehabilitation Medicine. 2021; 64: 101404.
- [105] Kim S, Lee S, Kang H, Kim S, Ahn M. P300 Brain-Computer Interface-Based Drone Control in Virtual and Augmented Reality. Sensors. 2021; 21: 5765.
- [106] Gehrke L, Lopes P, Klug M, Akman S, Gramann K. Neural sources of prediction errors detect unrealistic VR interactions. Journal of Neural Engineering. 2022; 19: 036002.
- [107] Vourvopoulos A, Jorge C, Abreu R, Figueiredo P, Fernandes JC, Bermúdez I Badia S. Efficacy and Brain Imaging Correlates of an Immersive Motor Imagery BCI-Driven VR System for Upper Limb Motor Rehabilitation: A Clinical Case Report. Frontiers in Human Neuroscience. 2019; 13: 244.
- [108] Zapała D, Augustynowicz P, Tokovarov M. Recognition of Attentional States in VR Environment: An fNIRS Study. Sensors. 2022; 22: 3133.
- [109] Chin ZY, Zhang Z, Wang C, Ang KK. An Affective Interaction System using Virtual Reality and Brain-Computer Interface. Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference. 2021; 2021: 6183–6186.
- [110] Ren S, Wang W, Hou ZG, Liang X, Wang J, Shi W. Enhanced Motor Imagery Based Brain- Computer Interface via FES and VR for Lower Limbs. IEEE Transactions on Neural Systems and Rehabilitation Engineering. 2020; 28: 1846–1855.
- [111] Montag M, Paschall C, Ojemann J, Rao R, Herron J. A Platform for Virtual Reality Task Design with Intracranial Electrodes. Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference. 2021; 2021: 6659–6662.
- [112] Vourvopoulos A, Pardo OM, Lefebvre S, Neureither M, Saldana D, Jahng E, et al. Effects of a Brain-Computer Interface With Virtual Reality (VR) Neurofeedback: A Pilot Study in Chronic Stroke Patients. Frontiers in Human Neuroscience. 2019; 13: 210.
- [113] Marin-Pardo O, Laine CM, Rennie M, Ito KL, Finley J, Liew SL. A Virtual Reality Muscle-Computer Interface for Neurore-

- habilitation in Chronic Stroke: A Pilot Study. Sensors. 2020; 20: 3754.
- [114] Nunes JD, Vourvopoulos A, Blanco-Mora DA, Jorge C, Fernandes JC, Bermudez I Badia S, et al. Brain activation by a VR-based motor imagery and observation task: An fMRI study. PLoS ONE. 2023; 18: e0291528.
- [115] Ferrero L, Quiles V, Ortiz M, Iáñez E, Gil-Agudo Á, Azorín JM. Brain-computer interface enhanced by virtual reality training for controlling a lower limb exoskeleton. iScience. 2023; 26: 106675.
- [116] Lapborisuth P, Koorathota S, Wang Q, Sajda P. Integrating neural and ocular attention reorienting signals in virtual reality. Journal of Neural Engineering. 2022; 18: 066052.
- [117] McDermott EJ, Metsomaa J, Belardinelli P, Grosse-Wentrup M, Ziemann U, Zrenner C. Predicting motor behavior: an efficient EEG signal processing pipeline to detect brain states with potential therapeutic relevance for VR-based neurorehabilitation. Virtual Reality. 2023; 27: 347–369.
- [118] Sciaraffa N, Di Flumeri G, Germano D, Giorgi A, Di Florio A, Borghini G, et al. Evaluation of a New Lightweight EEG Technology for Translational Applications of Passive BrainComputer Interfaces. Frontiers in Human Neuroscience. 2022; 16: 901387.
- [119] Wang H, Zheng H, Wu H, Long J. Behavior-Dependent Corticocortical Contributions to Imagined Grasping: a BCI-triggered TMS study. IEEE Transactions on Neural Systems and Rehabilitation Engineering. 2022; 31: 519–529.
- [120] Liang WD, Xu Y, Schmidt J, Zhang LX, Ruddy KL. Upregulating excitability of corticospinal pathways in stroke patients using TMS neurofeedback; A pilot study. NeuroImage: Clinical. 2020; 28: 102465.
- [121] Carino-Escobar RI, Rodríguez-García ME, Ramirez-Nava AG, Quinzaños-Fresnedo J, Ortega-Robles E, Arias-Carrion O, et al. A case report: Upper limb recovery from stroke related to SARS-CoV-2 infection during an intervention with a braincomputer interface. Frontiers in Neurology. 2022; 13: 1010328.
- [122] Won K, Kim H, Gwon D, Ahn M, Nam CS, Jun SC. Can vibrotactile stimulation and tDCS help inefficient BCI users? Journal of Neuroengineering and Rehabilitation. 2023; 20: 60.
- [123] Xie J, Peng M, Lu J, Xiao C, Zong X, Wang M, et al. Enhancement of Event-Related Desynchronization in Motor Imagery Based on Transcranial Electrical Stimulation. Frontiers in Human Neuroscience. 2021; 15: 635351.
- [124] Chew E, Teo WP, Tang N, Ang KK, Ng YS, Zhou JH, et al. Using Transcranial Direct Current Stimulation to Augment the Effect of Motor Imagery-Assisted Brain-Computer Interface Training in Chronic Stroke Patients-Cortical Reorganization Considerations. Frontiers in Neurology. 2020; 11: 948.
- [125] Caldwell DJ, Ojemann JG, Rao RPN. Direct Electrical Stimulation in Electrocorticographic Brain-Computer Interfaces: Enabling Technologies for Input to Cortex. Frontiers in Neuroscience. 2019; 13: 804.
- [126] Kawala-Sterniuk A, Browarska N, Al-Bakri A, Pelc M, Zygarlicki J, Sidikova M, et al. Summary of over Fifty Years with Brain-Computer Interfaces-A Review. Brain Sciences. 2021; 11: 43.
- [127] Mitsopoulos K, Fiska V, Tagaras K, Papias A, Antoniou P, Nizamis K, et al. NeuroSuitUp: System Architecture and Validation of a Motor Rehabilitation Wearable Robotics and Serious Game Platform. Sensors. 2023; 23: 3281.
- [128] Pimentel RE, Feldman JN, Lewek MD, Franz JR. Quantifying mechanical and metabolic interdependence between speed and propulsive force during walking. Frontiers in Sports and Active Living. 2022; 4: 942498.
- [129] Kübler A. The history of BCI: From a vision for the future to real support for personhood in people with locked-in syndrome.

- Neuroethics. 2020; 13: 163–180.
- [130] Branco MP, Pels EGM, Sars RH, Aarnoutse EJ, Ramsey NF, Vansteensel MJ, et al. Brain-Computer Interfaces for Communication: Preferences of Individuals With Locked-in Syndrome. Neurorehabilitation and Neural Repair. 2021; 35: 267–279.
- [131] Milekovic T, Sarma AA, Bacher D, Simeral JD, Saab J, Pandarinath C, et al. Stable long-term BCI-enabled communication in ALS and locked-in syndrome using LFP signals. Journal of Neurophysiology. 2018; 120: 343–360.
- [132] Pitt KM, Brumberg JS. Evaluating the perspectives of those with severe physical impairments while learning BCI control of a commercial augmentative and alternative communication paradigm. Assistive Technology. 2023; 35: 74–82.
- [133] Shah U, Alzubaidi M, Mohsen F, Abd-Alrazaq A, Alam T, Househ M. The Role of Artificial Intelligence in Decoding Speech from EEG Signals: A Scoping Review. Sensors. 2022; 22: 6975.
- [134] Pan H, Li Z, Tian C, Wang L, Fu Y, Qin X, et al. The LightGBM-based classification algorithm for Chinese characters speech imagery BCI system. Cognitive Neurodynamics. 2023; 17: 373–384.
- [135] Van Eck NJ, Waltman L. Visualizing bibliometric networks. Measuring scholarly impact: Methods and practice (pp. 285– 320). Springer: Berlin, Germany. 2014.
- [136] Värbu K, Muhammad N, Muhammad Y. Past, Present, and Future of EEG-Based BCI Applications. Sensors. 2022; 22: 3331.
- [137] Alsharif A, Salleh N, Baharun R, Safaei M. Neuromarketing approach: An overview and future research directions. Journal of Theoretical and Applied Information Technology. 2020; 98: 991–1001.
- [138] Liao JJ, Luo JJ, Yang T, So RQY, Chua MCH. Effects of local and global spatial patterns in EEG motor-imagery classification using convolutional neural network. Brain-Computer Interfaces. 2020; 7: 47–56.
- [139] Abdulwahab SS, Khleaf HK, Jassim MH, Abdulwahab S. A systematic review of brain-computer interface based eeg. Iraqi Journal for Electrical and Electronic Engineering. 2020; 16: 81– 90.
- [140] Bai Z, Fong KNK, Zhang JJ, Chan J, Ting KH. Immediate and long-term effects of BCI-based rehabilitation of the upper extremity after stroke: a systematic review and meta-analysis. Journal of Neuroengineering and Rehabilitation. 2020; 17: 57.
- [141] Foldes ST, Boninger ML, Weber DJ, Collinger JL. Effects of MEG-based neurofeedback for hand rehabilitation after tetraplegia: preliminary findings in cortical modulations and grip strength. Journal of Neural Engineering. 2020; 17: 026019.
- [142] Miao Y, Chen S, Zhang X, Jin J, Xu R, Daly I, et al. BCI-Based Rehabilitation on the Stroke in Sequela Stage. Neural Plasticity. 2020; 2020: e8882764.
- [143] Valente G, Kaas AL, Formisano E, Goebel R. Optimizing fMRI experimental design for MVPA-based BCI control: Combining the strengths of block and event-related designs. NeuroImage. 2019; 186: 369–381.
- [144] Naseer N, Hong KS. fNIRS-based brain-computer interfaces: a review. Frontiers in Human Neuroscience. 2015; 9: 3.
- [145] Rieke JD, Matarasso AK, Yusufali MM, Ravindran A, Alcantara J, White KD, et al. Development of a combined, sequential real-time fMRI and fNIRS neurofeedback system to enhance motor learning after stroke. Journal of Neuroscience Methods. 2020; 341: 108719.
- [146] Zheng Y, Tian B, Zhuang Z, Zhang Y, Wang D. fNIRS-based adaptive visuomotor task improves sensorimotor cortical activation. Journal of Neural Engineering. 2022; 19: 046023.
- [147] Nazeer H, Naseer N, Khan RA, Noori FM, Qureshi NK, Khan US, et al. Enhancing classification accuracy of fNIRS-BCI using features acquired from vector-based phase analysis. Journal of

- Neural Engineering. 2020; 17: 056025.
- [148] Ahn S, Jun SC. Multi-Modal Integration of EEG-fNIRS for Brain-Computer Interfaces – Current Limitations and Future Directions. Frontiers in Human Neuroscience. 2017; 11: 503.
- [149] Saez I, Gu X. Invasive Computational Psychiatry. Biological Psychiatry. 2023; 93: 661–670.
- [150] Śliwowski M, Martin M, Souloumiac A, Blanchart P, Aksenova T. Impact of dataset size and long-term ECoG-based BCI usage on deep learning decoders performance. Frontiers in Human Neuroscience. 2023; 17: 1111645.
- [151] Freudenburg ZV, Branco MP, Leinders S, van der Vijgh BH, Pels EGM, Denison T, et al. Sensorimotor ECoG Signal Features for BCI Control: A Comparison Between People With Locked-In Syndrome and Able-Bodied Controls. Frontiers in Neuroscience. 2019; 13: 1058.
- [152] Miller KJ, Hermes D, Staff NP. The current state of electrocorticography-based brain-computer interfaces. Neurosurgical Focus. 2020; 49: E2.
- [153] Rabbani Q, Milsap G, Crone NE. The Potential for a Speech Brain-Computer Interface Using Chronic Electrocorticography. Neurotherapeutics. 2019; 16: 144–165.
- [154] Branco MP, Geukes SH, Aarnoutse EJ, Ramsey NF, Vansteensel MJ. Nine decades of electrocorticography: A comparison between epidural and subdural recordings. The European Journal of Neuroscience. 2023; 57: 1260–1288.
- [155] Volkova K, Lebedev MA, Kaplan A, Ossadtchi A. Decoding Movement From Electrocorticographic Activity: A Review. Frontiers in Neuroinformatics. 2019; 13: 74.
- [156] Duez L, Beniczky S, Tankisi H, Hansen PO, Sidenius P, Sabers A, et al. Added diagnostic value of magnetoencephalography (MEG) in patients suspected for epilepsy, where previous, extensive EEG workup was unrevealing. Clinical Neurophysiology. 2016; 127: 3301–3305.
- [157] Cargnelutti E, Tomasino B. Pre-Operative Functional Mapping in Patients with Brain Tumors by fMRI and MEG: Advantages and Disadvantages in the Use of One Technique over the Other. Life. 2023; 13: 609.
- [158] Thomas RJ, Morrison PJ. Mapping proprioceptive function using corticokinematic coherence in ataxias. Neurology. 2019; 93: 49–50.
- [159] Hakim U, De Felice S, Pinti P, Zhang X, Noah JA, Ono Y, et al. Quantification of inter-brain coupling: A review of current methods used in haemodynamic and electrophysiological hyperscanning studies. NeuroImage. 2023; 280: 120354.
- [160] Angus-Leppan H. Seizures and adverse events during routine scalp electroencephalography: a clinical and EEG analysis of 1000 records. Clinical Neurophysiology. 2007; 118: 22–30.
- [161] Kane N, Grocott L, Kandler R, Lawrence S, Pang C. Hyperventilation during electroencephalography: safety and efficacy. Seizure. 2014; 23: 129–134.
- [162] Siddiqi SH, Kandala S, Hacker CD, Bouchard H, Leuthardt EC, Corbetta M, et al. Precision functional MRI mapping reveals distinct connectivity patterns for depression associated with traumatic brain injury. Science Translational Medicine. 2023; 15: eabn0441.
- [163] Rao P, Morandini H. Functional magnetic resonance imaging in child and adolescent psychiatry: What is it and where are we headed? Annals of Indian Psychiatry. 2023; 7: 89–91.
- [164] Nielsen AN, Graham AM, Sylvester CM. Baby Brains at Work: How Task-Based Functional Magnetic Resonance Imaging Can Illuminate the Early Emergence of Psychiatric Risk. Biological Psychiatry. 2023; 93: 880–892.
- [165] Nataletti S, Leo F, Seminara L, Trompetto C, Valle M, Dosen S, et al. Temporal Asynchrony but Not Total Energy Nor Duration Improves the Judgment of Numerosity in Electrotactile Stimulation. Frontiers in Bioengineering and Biotechnology. 2020; 8:

- 555.
- [166] Kaas A, Goebel R, Valente G, Sorger B. Topographic Somatosensory Imagery for Real-Time fMRI Brain-Computer Interfacing. Frontiers in Human Neuroscience. 2019; 13: 427.
- [167] Huang W, Wu W, Lucas MV, Huang H, Wen Z, Li Y. Neurofeedback training with an electroencephalogram-based braincomputer interface enhances emotion regulation. IEEE Transactions on Affective Computing. 2021.
- [168] Shanechi MM. Brain-machine interfaces from motor to mood. Nature Neuroscience. 2019; 22: 1554–1564.
- [169] Fang H, Yang Y. Predictive neuromodulation of cingulo-frontal neural dynamics in major depressive disorder using a braincomputer interface system: A simulation study. Frontiers in Computational Neuroscience. 2023; 17: 1119685.
- [170] Belkacem AN, Jamil N, Khalid S, Alnajjar F. On closed-loop brain stimulation systems for improving the quality of life of patients with neurological disorders. Frontiers in Human Neuroscience. 2023; 17: 1085173.
- [171] Provenza NR, Matteson ER, Allawala AB, Barrios-Anderson A, Sheth SA, Viswanathan A, et al. The Case for Adaptive Neuromodulation to Treat Severe Intractable Mental Disorders. Frontiers in Neuroscience. 2019; 13: 152.
- [172] Montgomery SA, Asberg M. A new depression scale designed to be sensitive to change. The British Journal of Psychiatry. 1979; 134: 382–389.
- [173] Carrozzino D, Patierno C, Fava GA, Guidi J. The Hamilton Rating Scales for Depression: A Critical Review of Clinimetric Properties of Different Versions. Psychotherapy and Psychosomatics. 2020; 89: 133–150.
- [174] Melnikov MY. The Current Evidence Levels for Biofeedback and Neurofeedback Interventions in Treating Depression: A Narrative Review. Neural Plasticity. 2021; 2021: 8878857.
- [175] Rongala U, Mazzoni A, Camboni D, Carrozza MC, Oddo CM. Neuromorphic Artificial Sense of Touch: Bridging Robotics and Neuroscience. Robotics Research: Volume 2. 2018; 617–630.
- [176] Zaidel A, Salomon R. Multisensory decisions from self to world. Philosophical Transactions of the Royal Society of London. 2023; 378: 20220335.
- [177] Czub M, Kowal M. Respiration Entrainment in Virtual Reality by Using a Breathing Avatar. Cyberpsychology, Behavior and Social Networking. 2019; 22: 494–499.
- [178] Marchetti M, Priftis K. Brain-computer interfaces in amyotrophic lateral sclerosis: A metanalysis. Clinical Neurophysiology. 2015; 126: 1255–1263.
- [179] Neto LL, Constantini AC, Chun RYS. Communication vulnerable in patients with Amyotrophic Lateral Sclerosis: A systematic review. NeuroRehabilitation. 2017; 40: 561–568.
- [180] Fernandes F, Barbalho I, Barros D, Valentim R, Teixeira C, Henriques J, et al. Biomedical signals and machine learning in amyotrophic lateral sclerosis: a systematic review. Biomedical Engineering Online. 2021; 20: 61.
- [181] Luo S, Angrick M, Coogan C, Candrea DN, Wyse-Sookoo K, Shah S, et al. Stable Decoding from a Speech BCI Enables Control for an Individual with ALS without Recalibration for 3 Months. Advanced Science. 2023; 10: e2304853.
- [182] El-Dahshan ESA, Bassiouni MM, Khare SK, Tan RS, Rajendra Acharya UR. ExHyptNet: An explainable diagnosis of hypertension using EfficientNet with PPG signals. Expert Systems with Applications. 2024; 239: 122388.
- [183] Gu X, Cao Z, Jolfaei A, Xu P, Wu D, Jung TP, et al. EEG-Based Brain-Computer Interfaces (BCIs): A Survey of Recent Studies on Signal Sensing Technologies and Computational Intelligence Approaches and Their Applications. IEEE/ACM Transactions on Computational Biology and Bioinformatics. 2021; 18: 1645– 1666.
- [184] Yang L, Liu Q, Zhang Z, Gan L, Zhang Y, Wu J. Materials for

- dry electrodes for the electroencephalography: advances, challenges, perspectives. Advanced Materials Technologies. 2022; 7: 2100612.
- [185] Hinrichs H, Scholz M, Baum AK, Kam JWY, Knight RT, Heinze HJ. Comparison between a wireless dry electrode EEG system with a conventional wired wet electrode EEG system for clinical applications. Scientific Reports. 2020; 10: 5218.
- [186] Di Flumeri G, Aricò P, Borghini G, Sciaraffa N, Di Florio A, Babiloni F. The Dry Revolution: Evaluation of Three Different EEG Dry Electrode Types in Terms of Signal Spectral Features, Mental States Classification and Usability. Sensors. 2019; 19: 1365.
- [187] Yaacob H, Hossain F, Shari S, Khare SK, Ooi CP, Acharya UR. Application of artificial intelligence techniques for braincomputer interface in mental fatigue detection: a systematic re-

- view (2011-2022). IEEE Access. 2023; 11: 74736–74758.
- [188] He C, Chen YY, Phang CR, Stevenson C, Chen IP, Jung TP, et al. Diversity and Suitability of the State-of-the-Art Wearable and Wireless EEG Systems Review. IEEE Journal of Biomedical and Health Informatics. 2023; 27: 3830–3843.
- [189] Haider A. A brief review of signal processing for eeg-based bci: Approaches and opportunities. In 2021 IEEE International Conference on Electro Information Technology (EIT). IEEE. 2021; 2021: 389–394.
- [190] di Biase L, Tinkhauser G, Martin Moraud E, Caminiti ML, Pecoraro PM, Di Lazzaro V. Adaptive, personalized closed-loop therapy for Parkinson’s disease: biochemical, neurophysiological, and wearable sensing systems. Expert Review of Neurotherapeutics. 2021; 21: 1371–1388.

