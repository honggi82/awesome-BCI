# arXiv:2601.19269v1[cs.HC]27Jan2026

## A Personalized and Adaptable User Interface for a Speech and Cursor Brain-Computer Interface

HAMZA PERACHA, Department of Neurological Surgery, University of California, Davis, USA CARRINA IACOBACCI, Department of Neurological Surgery, University of California, Davis, USA TYLER SINGER-CLARK, Department of Neurological Surgery, University of California, Davis, USA and Biomedical Engineering Graduate Group, University of California, Davis, USA

LEIGH R. HOCHBERG, School of Engineering and Carney Institute for Brain Sciences, Brown University, USA, VA RR&D Center for Neurorestoration and Neurotechnology, VA Providence Healthcare, USA, and Center for Neurotechnology and Neurorecovery, Department of Neurology, Massachusetts General Hospital, Harvard Medical School, USA

SERGEY D. STAVISKY, Department of Neurological Surgery, University of California, Davis, USA DAVID M. BRANDMAN, Department of Neurological Surgery, University of California, Davis, USA NICHOLAS S. CARD, Department of Neurological Surgery, University of California, Davis, USA

Communication and computer interaction are important for autonomy in modern life. Unfortunately, these capabilities can be limited or inaccessible for the millions of people living with paralysis. While implantable brain-computer interfaces (BCIs) show promise for restoring these capabilities, little has been explored on designing BCI user interfaces (UIs) for sustained daily use. Here, we present a personalized UI for an intracortical BCI system that enables users with severe paralysis to communicate and interact with their computers independently. Through a 22-month longitudinal deployment with one participant, we used iterative co-design to develop a system for everyday at-home use and documented how it evolved to meet changing needs. Our findings highlight how personalization and adaptability enabled independence in daily life and provide design implications for developing future BCI assistive technologies.

### 1 Introduction

For people living with severe paralysis, the loss of voluntary motor control can have a profound impact on daily life by limiting movement, speech, and digital access. In the United States alone, about 5 million individuals live with paralysis [11]. For these individuals, maintaining the ability to interact with a computer can help them engage with work, entertainment, social connections, and other activities which promote independence and a higher quality of life [9, 31, 45].

For many people living with paralysis, current solutions that enable communication and computer access are limited to alternative and augmentative communication (AAC) devices. AACs can range from low-tech options such as pictureand gaze-boards [3, 9], to higher-tech options such as gyroscopic head mice or eye tracker based devices [5, 37, 39].

Authors’ Contact Information: Hamza Peracha, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA, hperacha@health. ucdavis.edu; Carrina Iacobacci, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA, ciacobacci@health.ucdavis.edu; Tyler Singer-Clark, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA and Biomedical Engineering Graduate Group, University of California, Davis, Davis, CA, USA, tsingerclark@health.ucdavis.edu; Leigh R. Hochberg, School of Engineering and Carney Institute for Brain Sciences, Brown University, Providence, RI, USA and VA RR&D Center for Neurorestoration and Neurotechnology, VA Providence Healthcare, Providence, RI, USA and Center for Neurotechnology and Neurorecovery, Department of Neurology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA, leigh_hochberg@brown.edu; Sergey D. Stavisky, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA, sstavisky@health.ucdavis.edu; David M. Brandman, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA, dmbrandman@health.ucdavis.edu; Nicholas S. Card, Department of Neurological Surgery, University of California, Davis, Davis, CA, USA, nscard@health.ucdavis.edu.

1

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

Fig. 1. (A) Intracortical brain computer interface system schematic. Microelectrode arrays are surgically placed into the speech motor cortex. Neural information is transmitted through percutaneous wires to a computer system that decodes the neural data into words on a screen. (B) Participant T15 using the BCI system. T15’s personal computer monitors are pictured at the bottom, with the BCI systems monitor positioned on top, displaying the most recent decoded sentence.

However, existing AAC devices face challenges such as slow typing speeds, user fatigue, and difficulty in use due to the decline or loss of ocular motor function [17, 25, 53, 58].

Recent advances have demonstrated that brain-computer interfaces (BCIs) may be a viable AAC option. BCIs enable users to control devices by decoding intended movement from the brain, bypassing downstream injuries [67, 80]. Implantable BCIs, such as those using intracortical microelectrode arrays, are surgically implanted and can directly record neural signals from within the brain, offering signals that are highly informative about a user’s movement intent. In previous work, implantable BCIs have been used to decode intended speech and cursor movements with high fidelity from individuals with severe paralysis, offering a new avenue for assistive technology and AACs [10, 15, 20, 66, 77]. Previous work has also shown efforts to use this technology for computer interaction, including a cursor BCI for at home use [63, 75]. Implantable BCIs have been studied for over two decades in a variety of first-in-human clinical trials (e.g., [6, 7, 10, 22, 28, 38, 54, 72], see [55] for a more comprehensive list), and thanks to these proof-of-concept studies, there are now multiple neurotechnology companies seeking to create and validate medical-grade BCIs for people with paralysis [70, 78].

While academic engineering labs have largely focused on developing new end-effectors and decoding algorithms for BCIs, relatively little has been explored about how users can best interact with these devices during daily use. This raises important questions on designing effective UIs that leverage this research to support BCI use for computer interaction and communication. In this work, we demonstrate a UI for a multimodal BCI system that enables real-time communication and full-featured control over a computer. BCI use is highly individualized as users vary in terms of abilities, preferences, and interaction methods. Our goal was to design a system that can be tailored to each user’s specific needs while remaining adaptable across a broader user base.

We propose the following two contributions:

(1) The design of a personalized BCI interface through a long-term co-design process with one user, demonstrating transferable design implications for an adaptable interface.

(2) A flexible system architecture with a shared backend and an adaptable user interface that allows for the system’s easy adaptation for different BCI users with diverse needs.

2 Related Work

- 2.1 Eye Gaze AAC Systems

Eye gaze control is a popular interaction method for AAC and computer access [5, 37, 39], with commercial gaze systems such as the Tobii Dynavox (Sweden) becoming a common choice for users with paralysis [34]. Eye tracking technologies remain a viable choice for users with a wide range of neurological diseases, including late-stage amyotrophic lateral sclerosis (ALS), since ocular movements are often still intact despite limb and facial paralysis [58]. These systems enable users to spell out words and control their personal computer using a cursor. Recent advances in gaze typing have significantly increased interaction speed by eliminating the need to dwell over each key [42], addressing one of the limitations of dwell-based systems.

However, eye gaze systems still face significant limitations for computer use. Communication with these systems is slow [25, 53]. Precise control over a computer cursor is also challenging, making navigation of interfaces with small buttons difficult, although there have been developments in design techniques to remedy this [12, 56]. Some users also face difficulties operating these systems due to irregularities in ocular movement, lack of reliability in outdoor environments, and requiring a direct line of sight [17, 26, 58].

- 2.2 Switch-Based Systems

Switch-based systems are another well-established access method. In switch-based systems, items are highlighted sequentially until the user activates a switch to select, allowing text entry and navigation. Although slower than direct selection methods and often more cognitively demanding [64], switch-based systems remain a robust interaction method that can be found in consumer devices and some BCI systems [1, 18].

- 2.3 Non-Implantable BCI Systems

Given the limitations of eye gaze devices, non-implantable BCIs using electroencephalography (EEG) have been explored as an alternative control method [27, 47]. EEG-based BCIs remain relatively accessible and safe for anyone to use, and research has demonstrated their feasibility for basic computer control tasks and communication. P300-based spellers and steady-state visually evoked potential (SSVEP) systems have shown promise [14, 51]. Recent studies have demonstrated systems that are accurate and achieve communication rates upwards of 60 characters per minute in healthy subjects [21, 49], while research has also been focused on the usability of these systems [36, 43].

Non-implantable BCIs face technical limitations. The resolution and signal-to-noise ratio of neural signals recorded by non-implantable BCIs are insufficient for high-fidelity control, limiting users to basic click or switch-based interfaces and selection tasks [59]. Although EEG-based BCIs remain promising as widely accessible AAC devices, they lack the signal-to-noise ratio required for the highest speed and accuracy in communication and computer use.

- 2.4 Implantable BCI Systems

Implantable BCIs have demonstrated a significant improvement in control and performance over non-implantable options. These systems can typically decode neural signals from within the skull with much higher resolutions and signal-to-noise ratios, enabling control modalities such as cursor control [13, 16, 24, 52, 66, 75], robot arm control

[29, 33], typing and handwriting interfaces [41, 61, 76], and more recently, speech decoding [20, 44, 46, 48, 62, 68, 73, 77]. Previous work has described designing a user interface for at-home BCI systems but they lack a focus on the design process [23, 63].

Implantable BCIs face the obvious barrier of being less accessible due to the need for surgical implantation of the neural recording device, limiting their availability to participants in clinical trials until these devices are approved for broader use.

### 2.5 User-Centered BCI Design

BCIs benefit substantially from user-centered design. This requires a shift from focusing solely on metrics such as decoding performance towards the overall user experience through iterative design with end-users [43, 60]. Recent work in communication-based BCIs has shown success in adopting participatory methods, using design-test-refine cycles while involving the end-users and domain experts [32]. However, these studies primarily focus on selection-based non-implantable BCI systems. To our knowledge, no prior work reports on long-term, iterative co-design with an implanted BCI system, and we build on these user-centered design practices to address our unique challenges.

### 2.6 Speech Interfaces

While prior work on speech BCIs has primarily focused on decoding accuracy, there is limited work on interface design. Commercial speech recognition software such as Dragon NaturallySpeaking offers relevant precedents for a speech BCI [2], particularly regarding how users make corrections to errors in decoded sentences. Other work has explored error correction in speech recognition interfaces and how users can combine speech with other modalities to make corrections [69]. These systems, however, require precise physical movements to use the software and make corrections, which are not possible by people with paralysis.

### 3 Methods

Design of new assistive technology presents unique challenges because user requirements cannot be easily determined through traditional methods [50, 79]. Additionally, Phillips and Zhao [57] emphasized that assistive technology may be abandoned if users’ opinions are not considered during the design process. For emerging technologies such as implantable BCIs, these challenges are compounded as the technology’s capabilities and user control methods are still being explored.

We adopted an iterative co-design approach [30], using our ongoing prototype as a technology probe [40]. This allowed us to engage in participatory design, working collaboratively with the participant during the design process, while working versions of our prototype were deployed in the participant’s home over an extended period of time. This approach allowed us to discover design requirements and feedback through continuous interaction that would not have been possible through traditional methods alone, such as larger-scale usability testing [50]. We also applied Wobbrock et al.’s ability-based design principles [79], which focus on designing systems that adapt to users’ diverse abilities rather than requiring users to adapt to the system.

3.1 Research Questions In this work, we address the following research questions:

- RQ1: How does a user with tetraplegia and severe dysarthria due to ALS integrate a speech and cursor BCI into daily life over an extended period of time?
- RQ2: What challenges arise during the implementation of the system, and how can iterative design address them?
- RQ3: What design implications emerge that can inform the design of future BCI systems?

### 3.2 Participant

A 45-year-old man (T15) with tetraplegia and severe dysarthria due to ALS was enrolled in the BrainGate2 clinical trial (ClinicalTrials.gov number, NCT00912041) in 2023. T15 has four 64-microelectrode arrays placed in his left precentral gyrus, which is the part of the brain responsible for controlling the muscles involved in speech. Use of the system requires assistance from a member of the scientific team or a care partner to set up and remove the equipment.

Author D.M.B. is a board-certified neurosurgeon and is the site-responsible investigator for the BrainGate2 clinical trial at the University of California, Davis. He obtained informed consent, performed the operations, and continues to provide clinical care with participants while they are enrolled in the clinical trial.

### 3.3 Study Design

We evaluated the system through a 22-month-long longitudinal study with participant T15. Our approach combined continuous at-home deployment of new features along with periodic assessment of the BCI system, drawing from technology probe approaches that focus on real-world deployment and iterative design improvements [40].

We administered three surveys every six months: an assistive technology assessment evaluating the BCI’s overall effectiveness, a personal use task evaluation focused on an everyday computer task (we evaluated email composition), and a user-centered design questionnaire assessing the interface design and layout [35, 65]. The user-centered design questionnaire was only administered at the second and third sessions. Initially, all interaction with T15 was done through a gyroscopic head mouse or via a skilled interpreter. Shortly after beginning this design process, all communication transitioned to being done through the BCI.

### 3.4 Co-Design Process

The co-design process involved continuous collaboration with T15 over 22 months through multiple channels. We conducted regular check-ins twice weekly, where T15 could provide brief feedback and discuss system usage. Additional focused design sessions were held periodically to review features and gather more detailed input. Between sessions, regular communication was maintained via text messages and shared documents, along with formal surveys run every 6 months.

Features were developed through ongoing collaboration with T15, including informal interactions, rapid prototype testing, and immediate deployment for real-world validation. T15 identified needs based on daily system usage, and the research team suggested new options when possible. Design decisions prioritized T15’s preferences and usage requirements.

### 3.5 System Architecture

Intracortical neural signals are transmitted to and decoded by a system of computers (Figure 1A) [19, 20, 66]. The computers run the BRAND software platform, which allows multiple Linux processes (“nodes”) across a distributed network optimized for real-time BCI control [8]. This distributed system enables rapid development with standardized frameworks for measuring system latency and jitter.

The user interface consists of two nodes: one for logic and one for graphics display. The logic node is implemented as a finite state machine (FSM) (Figure 2), responsible for handling the different task states, such as idle, speaking, and so on (Figure 3), as well as receiving decoded neural signals in the form of text, cursor movements, or gestures. The graphics node uses Python 3.8 with the pyglet library (v2.0.12) [4], which is made for designing visually-rich applications. Using this library, we created a node to allow users to interact with the BCI system. The graphics node consists of multiple "screens" (here we use the term “screen” to mean a visual configuration of user interface elements, as in “home screen”, and not to mean a physical display), with each screen corresponding to a different task state in the logic node. This system decoupling facilitates adding new features based on user feedback. The Python-based user interface is also ideal for development in a research environment, since most researchers are familiar with the language.

Users can control the interface using their preferred interaction method. Available input modalities include decoded speech, neural cursor control, decoded gestures, and eye gaze tracking. Decoded speech allows sentence formation for in-person communication or typing on a personal computer. Speech decoding uses a transformer-based decoder to convert neural signals to phoneme probabilities [19]. An n-gram language model then generates the most likely word sequences from these phonemes, which are fed to a large language model (OPT 6.7b) for additional rescoring in a fully local pipeline [19]. Neural cursor control enables BCI users to directly translate neural activity associated with attempted motor movements into precise cursor movements [38, 52, 66]. In our study, a time series of neural data is streamed into a cursor decoder and a click decoder [19, 66]. The cursor decoder is a linear model that maps neural signals to 2-D cursor velocities. The click decoder is a linear classifier that maps neural signals to probabilities of two discrete classes: "no action" vs "click". In our system, this enables pointer control on both the system’s interface and the user’s personal computer. Decoded gestures can be calibrated and mapped to cursor clicks or other discrete actions, such as scrolling. Eye gaze tracking provides an alternative means of interacting with the system’s interface. Together, these input modalities form the user-facing side of our BCI system, and users can recalibrate any input modality at any time via the menu.

For interfacing with the user’s personal computer, we developed a desktop app that programmatically controls the keyboard and cursor. Users can paste decoded sentences into applications (Figure 3A) or enable neural cursor control to move and click the mouse on their personal computer.

4 System Design This section outlines the design process of the BCI.

### 4.1 T15 User Interface

We report on the near-daily use of the BCI system by T15. T15 has used the system for over 4000 hours, for up to 19 hours per day, communicating up to 60 words per minute [19]. Using the system, T15 has maintained full-time employment, and is able to have conversations with his young child, despite being paralyzed [71]. Over the course of 22 months, T15 has used the system through attempted speech, cursor control, gestures, and gaze tracking.

Given T15’s control methods, we were able to design a corresponding user interface as seen in Figure 3 and Figure 4. T15 typically uses the system sitting in his wheelchair, facing his personal desk in his bedroom. The interface is displayed on a 23.8” 1920x1080 resolution monitor mounted on an articulating arm, often positioned above T15’s personal computer monitors (Figure 1B).

The system begins in the “Idle” state (Figure 3A), displaying the most recently decoded sentence with quick actions such as play via text-to-speech, type to personal computer, and switch to spelling mode. When T15 begins speaking, the

Fig. 2. Finite state machine of the BCI interface for participant T15. It depicts different states and how the user navigates between them.

BCI automatically detects the attempted speech and transitions to the “Speaking” state (Figure 3B) [20], displaying the decoded words in real time. When done speaking, T15 either selects the “Done” button or waits for a 6-second timeout.

The system then transitions to the “Sentence rating” state (Figure 3C), where T15 marks the correctness by selecting one of the four options: “Correct”, “One word wrong”, “Mostly correct”, and “Incorrect” which return T15 to the “Idle” state while communicating to the system and to others the correctness of the sentence. If corrections are needed, T15 can select the “Make corrections” button. Here, T15 is first presented with candidate sentences generated by the language model pipeline (Figure 3D). If the correct sentence is not among the candidates, T15 can select a specific word to view alternative word suggestions generated by ModernBERT (Figure 3E) [74], add or delete words, refresh the suggestions, or manually type out corrections using an on-screen keyboard. Once corrections are complete, T15 returns to the “Sentence rating” state (Figure 3F) to mark the corrected sentence’s accuracy before returning to “Idle”. This gives the user the option to spend more time to ensure the sentence is fully correct if they choose to do so. In conversational exchanges, full sentence correctness is often not necessary to convey the user’s intended message, which is where having the option to rate the sentence as mostly correct is useful. In contrast, a fully correct sentence may be desired when writing a report or typing a message.

The menu (Figure 3G) contains many additional features, including speech calibration (Figure 3I, Figure 3J), cursor calibration (Figure 4G, Figure 4H), eye tracker calibration, privacy mode (data is not saved while active), sentence history (Figure 3H displays the last 5 spoken sentences), additional personal computer controls (Figure 4F such as tab, enter, space, etc.), and language filtering (censors adult language). The on-screen keyboard can also be used to compose text directly without the use of the speech BCI, which is useful when constructing character strings that may not appear in a typical corpus, such as passwords and proper nouns. A list of select features and their deployment dates can be found in Table 1.

Fig. 3. Speech-related user interface for T15. Subfigures (A)-(F) show a workflow of T15 speaking a sentence and making a correction. A gaze cursor pointer is shown interacting with the buttons on the screen. The following screens are shown: (A) idle (B) speaking (C) sentence rating (D) sentence correction (E) word correction with the selected word highlighted (F) sentence rating with the new corrected sentence. Subfigures (G) and (H) show how T15 can access the sentence history (H) through the menu (G). Subfigures (I) and (J) show accessing speech calibration (J) through the speech menu (I).

T15 can interact with the BCI interface and his personal computer via neural cursor or eye tracking. From the menu (Figure 4A), T15 can choose to control the BCI interface with neural cursor control (Figure 4B) or gaze control (Figure 4C). For personal computer control, T15 can choose to control the computer’s cursor with neural cursor (4E) or gaze control (4F) through the menu (4D).

[Figure 8]

[Figure 9]

- Fig. 4. Cursor-related user interface for T15. Subfigures (A)-(C) show how T15 can switch between neural cursor control (B) and gaze control (C) for the BCI interface from the menu (A). Subfigures (D)-(F) show how T15 can use neural cursor (E) or gaze (F) to control his personal computer by selecting options from the menu (D). Subfigures (G) and (H) show accessing neural cursor calibration (H) through the cursor menu (G).

### 4.2 Adapting to Other Platforms

By supporting multiple platforms, the system enables BCI use across a range of devices and in different environments, increasing flexibility and accessibility. Given the FSM-based design of our system, with one logic node and one graphics node, it is possible to swap out the graphics node to instead run the user interface on other devices. With this in mind, we designed versions of the BCI user interface for iPad (Figure 5A) and MacOS (Figure 5F). The same core functionality is displayed on these platforms, such as an idle screen, menu, sentence rating, and sentence correction. As long as the device is connected to the same local network that the BCI system is running on (via Ethernet, Bluetooth, or WiFi), it can read the task states and relevant information and display it accordingly. Cursor and keyboard control on the iPad is done through a Bluetooth device.

Table 1. Features in T15’s BCI user interface

Post-implant day Feature name Feature description 147 Bluetooth keyboard Allows the user to type decoded sentences on their personal computer. 227 Sentence correction Displays candidate sentences for a decoded sentence.

232 Eye tracker button magnetization Automatically guides the eye tracker cursor to the center of a button when the gaze enters a specific proximity, making dwell-based selection easier.

358 Neural cursor control for personal computer The user can control personal computer cursor via neural cursor control. 364 Eye tracker calibration The user can recalibrate the eye tracker through

a menu option. 462 Word-based correction Candidate words are now shown for each word. 462 Privacy mode Does not save data while active. 484 Miscellaneous updates Language filter, sound effects, option to toggle

features on and off, updates to UI. 486 Neural cursor control in BCI The user can control the BCI interface via neural cursor control. 491 Refresh word suggestions Refresh word suggestions and get new candidates. 505 Word insertion and deletion Insert and delete words in the word correction state. 563 External cursor control Allow a care partner to select buttons on the UI with a physical mouse. 565 On-screen keyboard On-screen keyboard that can be controlled with

gaze or neural cursor. 588 Aesthetic user interface changes Redesign of the user interface. 616 Updated word correction screen UI Redesign of the sentence and word correction

screens. 654 Sentence history Display the last 5 decoded sentences. 668 Gaze-based cursor control panel Control the personal computer cursor with

gaze.

5 Evaluation 5.1 Co-Design Insights

A significant insight was the importance of sentence correction capabilities, as the speech decoder did not always produce a fully accurate output. Initial designs required users to respeak entire sentences if any words were decoded incorrectly, which proved to be impractical. Through continuous feedback, we developed three major iterations. The first presented full candidate sentence alternatives but lacked flexibility for performing single-word corrections. The second iteration provided candidate sentences and words on separate screens, which T15 found to be highly effective but revealed the need for a refined UI and supporting features. The final iteration presents sentence and word candidates on the same screen, with options to add or delete words, refresh suggestions, and manually type out words via an on-screen keyboard (Figure 3D, Figure 3E). While time spent in making corrections per trial increased from 19 to 34 to

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

- Fig. 5. Participant T15 using the BCI on other platforms. (A) T15 using the BCI on an iPad. (E) T15 using the BCI on his iMac with a floating desktop application. Despite the differing form factor and operating systems, the applications follow the same structure as the original user interface. We show the following screens (B)(F) idle (C)(G) menu (D)(H) sentence correction.

62 seconds across iterations, the percentage of sentences marked as fully correct after making corrections increased substantially from 40% and 41% for the first two iterations to 59% for the final iteration. This suggests that the iterative co-design process resulted in a corrections screen that T15 found worthwhile, prioritizing accuracy over speed when choosing to make corrections.

Additional adaptations from the co-design process included implementing dual control modalities (neural cursor and eye tracking), developing a layout optimized for eye tracking with large circular buttons and magnetization, integrating recalibration options for all input methods to ensure stable control over the system without external assistance, and adding a horn button to catch others’ attention. T15’s control method varied by context. Eye tracking may be preferable in appropriately-lit indoor environments with direct line of sight, while neural cursor control worked better in suboptimal lighting or viewing angles. This multimodal approach allowed T15 to leverage the strengths of eye tracking for interface navigation when conditions were favorable, while maintaining access to neural cursor control when needed, demonstrating that context-based control modality selection can address the limitations noted in prior work.

The multimodal interaction methods and flexible sentence correction options together are another key insight derived from this process. A user’s control over a BCI system will be highly dependent on their condition, the BCI hardware, and the decoding accuracy. This can vary not only from user to user but also for a single user due to factors such as day-to-day variability or disease progression. Control mode redundancies are important for enabling user independence and making the system more generalizable to other users with different needs [79].

### 5.2 System Assessment

T15 used the BCI consistently in his own home over 22 months, averaging 10 hours per day. The system supported a diverse number of daily activities, including communication with family, friends, and coworkers, email and text composition, phone and video calls, work-related tasks such as report writing, and leisure activities such as browsing the web and watching videos.

Fig. 6. User interview data collected with participant T15 3 times over the course of one year.

We administered three surveys at six-month intervals. Each survey consisted of Likert-scale questions with optional comment fields after each question. The personal use task evaluation focused on email composition, asking questions such as “Rate how frustrating it is to use email using your assistive technology system”. The assistive technology assessment survey evaluated the overall system as an assistive technology with questions such as “Rate how difficult it is to use your speech BCI system overall” and “Rate how independent you are when using your speech BCI system”. The user-centered design questionnaire (administered at sessions 2 and 3) assessed the interface design with questions including “Do you feel like your feedback impacts new system features?” and “Is the layout intuitive?”.

Survey results remained consistently positive throughout (Figure 6). T15 rated independence while using the system at a 5 and 4 (out of 5), with lower scores on independence during setup (Figure 6B), indicating high autonomy once started. Sustained satisfaction occurred despite the system evolving substantially between surveys, suggesting the co-design approach maintained user satisfaction while meeting changing needs. T15’s comments further supported independence as a key takeaway. T15 emphasized he could perform all computer tasks independently once the system is set up by a care partner, stating “[I] use it for hours myself” and “can do it all by myself”. This finding aligns with work from Phillips and Zhao [57], showing independence as a key predictor of assistive technology adoption.

5.3 Longitudinal Usage Patterns System logs from T15’s 22-month use reveal insights into preferences and usage patterns over time.

T15 used two pointer control methods depending on the context. Eye tracking was preferred for the BCI interface, which was designed with large circular buttons and magnetization, making interaction more intuitive with gaze. Therefore, all interaction with the BCI system was done with eye tracking. The neural cursor offered more precision and was used for personal computer control, accounting for 11.5% of the 4000+ hours of total system use time. The neural cursor was necessary for personal computer use as standard interface elements are not optimized for gaze and require finer control than eye tracking could provide.

Sentence and word correction played a key role in T15’s usage. T15 used word-level correction (Figure 3E) for 91.2% of successfully corrected sentences, indicating its utility. A successfully corrected sentence is one that is marked as “correct” after entering the corrections screen. Sentence correction (Figure 3D) accounted for the other 8.8%, and served as a faster option for shorter sentences, averaging 18 seconds in the corrections screen versus 46 seconds for word

correction. Average sentence length was 9 words for sentence correction and 18 words for word correction. T15’s preference for word correction suggests that sentence-level alternatives, although faster, were often not sufficient, requiring more granular editing to achieve a fully correct sentence.

Within word correction, T15 had access to four editing features (Figure 3E): type word, delete word, add word before, and add word after. The delete function was used most often, while manually typing the word replacement out via an on-screen keyboard resulted in the highest correction accuracy (76% of sentences were marked as fully correct when using this feature). Alternative editing options (adding words, deleting words, and refreshing candidate word suggestions) resulted in 65% of sentences marked as fully correct. T15 may also choose not to fully correct a sentence to reduce the time spent making corrections.

- 6 Discussion

- 6.1 Independence Through Personalization

A key outcome of our longitudinal design process was that T15 remained satisfied with the system and was able to independently complete a wide variety of tasks, such as social interactions, leisure, and work, after initial system setup. We believe that these outcomes were a result of personalization of the system rather than just BCI decoding performance.

This process also enabled us to design for the changing needs of users. ALS is a progressive disease, and users’ needs and control modalities may change over time. Therefore, the system should adapt accordingly. Examples of this flexibility in our system include T15 having the ability to control his BCI via neural cursor control or eye tracking. This adaptive capability is vital for maintaining long-term usability as the disease progresses and supports the user’s abilities [79].

### 6.2 Limitations and Future Considerations

A clear limitation of our work is that the system has not been tested with a large number of users. Clinical trial inclusion criteria and the requirement of a surgically implanted BCI sensor result in a very limited user base. Due to this and the relatively recent emergence of intracranial neural speech decoding, large-scale testing is not yet feasible. Currently, this technology remains largely inaccessible outside of academic clinical trials, though recent efforts towards implanted BCI commercialization suggest that many more individuals may use such systems in the coming years.

Despite these limitations, this work provides value by addressing design questions that will become increasingly relevant as this technology becomes more widely available. The feedback collected can be carried forward to develop similar features for other users. Though the co-design process may not be feasible for large-scale studies or widespread deployment, here it proved to be a well-suited approach given the early stage of this field and the small, specialized user base. With this, we were able to apply 4 out of the 7 ability-based design principles outlined by Wobbrock at al. [79]: ability, accountability, adaptation, and transparency (Table 2).

This approach has broader implications for developing adaptable user interfaces, especially in the field of assistive technology. Our findings suggest that multimodal redundancy supports independence despite variable BCI performance, correction options should be flexible depending on context of use, transparent control through calibration options and features such as sentence history maintain users’ autonomy, and a shared backend architecture streamlines adaptation across users with different needs.

Table 2. Revisiting ability-based design principles.

Principle Applied Details

Ability Yes The system focuses on what users can do by providing multiple control modalities tailored to users’ capabilities. This principle motivated integrating neural cursor control when eye tracking proved context-dependent.

Accountability Yes When speech decoding is inaccurate, the system accommodates this through sentence corrections. Users can recalibrate at any time without external intervention. This principle drove the shift from external to user-initiated recalibration.

Adaptation Yes The system adapts to users through multiple control modalities, alternative candidate sentences and words, and calibration options. This principle guided the three correction interface iterations, responding to limitations identified through T15’s daily use.

Transparency Yes Users maintain visibility and control over the system through features such as calibration, sentence history, and sentence rating and corrections.

Performance No While the system logs usage data, it does not actively adapt to the user performance.

Context No Users are able to manually change options such as control modalities, but the system does not proactively sense the context on its own.

Commodity No This system requires a surgically implanted BCI sensor and specialized hardware and software to process the signals.

### 7 Conclusion

We report a highly personalized and adaptable user interface that enables users with paralysis to communicate and interact with a computer using an intracortical BCI, independently and in their own homes. We used an iterative co-design process with participant T15 that supported long-term daily use across communication, leisure, and work. This provides a step forward in BCI-based AAC solutions for communication and personal computer control that are both personalized and generalizable, offering a model for future user-centered BCI assistive technology development.

Acknowledgments We would like to thank participant T15 and his care partners.

This work was supported by A.P. Giannini Foundation (https://ror.org/01e3cnp62), NIH-NIDCD (U01DC017844), VA RR&D (A2295-R), ALS Association (24-AT-732), Neuralstorm NRT (2152260), ARCS Foundation, DP2 from the NIH Office of the Director and managed by NIDCD (1DP2DC021055), The Office of the Assistant Secretary of Defense for Health Affairs through the Amyotrophic Lateral Sclerosis Research Program (AL220043), Searle Scholars Program, and the Burroughs Wellcome Fund (https://ror.org/01d35cw23).

### References

- [1] [n.d.]. Apple Switch Control. Retrieved September 1, 2025 from https://support.apple.com/en-us/119835
- [2] [n.d.]. Dragon NaturallySpeaking. Retrieved September 1, 2025 from https://www.nuance.com/dragon.html

- [3] [n.d.]. Eye Gaze Board. Retrieved September 1, 2025 from https://www.als.org/sites/default/files/2020-04/Medical-Information-PacketEyeGazeBoard.pdf
- [4] [n.d.]. pyglet: The cross-platform windowing and multimedia library for Python. https://pyglet.org/
- [5] 2025. Proceedings of the 2025 ACM Symposium on Eye Tracking Research & Applications (ETRA). ACM, Tokyo, Japan.
- [6] Tyson Aflalo, Spencer Kellis, Christian Klaes, Brian Lee, Ying Shi, Kelsie Pejsa, Kathleen Shanfield, Stephanie Hayes-Jackson, Mindy Aisen, Christi Heck, et al. 2015. Decoding motor imagery from the posterior parietal cortex of a tetraplegic human. Science 348, 6237 (2015), 906–910.
- [7] A Bolu Ajiboye, Francis R Willett, Daniel R Young, William D Memberg, Brian A Murphy, Jonathan P Miller, Benjamin L Walter, Jennifer A Sweet, Harry A Hoyen, Michael W Keith, et al. 2017. Restoration of reaching and grasping movements through brain-controlled muscle stimulation in a person with tetraplegia: a proof-of-concept demonstration. The Lancet 389, 10081 (2017), 1821–1830.
- [8] Yahia H Ali, Kevin Bodkin, Mattia Rigotti-Thompson, Kushant Patel, Nicholas S Card, Bareesh Bhaduri, Samuel R Nason-Tomaszewski, Domenick M Mifsud, Xianda Hou, Claire Nicolas, et al. 2024. BRAND: a platform for closed-loop experiments with deep network models. Journal of Neural Engineering 21, 2 (2024), 026046.
- [9] MD Antonino Naro, Placido Bramanti, MD Simona Portaro, and Rocco Salvatore Calabrò. 2019. Augmentative and alternative communication improves quality of life in the early stages of amyotrophic lateral sclerosis. Functional neurology 34, 1 (2019), 35–43.
- [10] Gopala K Anumanchipalli, Josh Chartier, and Edward F Chang. 2019. Speech synthesis from neural decoding of spoken sentences. Nature 568, 7753

(2019), 493–498.

- [11] Brian S Armour, Elizabeth A Courtney-Long, Michael H Fox, Heidi Fredine, and Anthony Cahill. 2016. Prevalence and causes of paralysis—United States, 2013. American journal of public health 106, 10 (2016), 1855–1857.
- [12] Michael Ashmore, Andrew T Duchowski, and Garth Shoemaker. 2005. Efficient eye pointing with a fisheye lens. In Proceedings of Graphics interface

2005. 203–210.

- [13] Daniel Bacher, Beata Jarosiewicz, Nicolas Y Masse, Sergey D Stavisky, John D Simeral, Katherine Newell, Erin M Oakley, Sydney S Cash, Gerhard Friehs, and Leigh R Hochberg. 2015. Neural point-and-click communication by a person with incomplete locked-in syndrome. Neurorehabilitation and neural repair 29, 5 (2015), 462–471.
- [14] Guangyu Bin, Xiaorong Gao, Zheng Yan, Bo Hong, and Shangkai Gao. 2009. An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method. Journal of neural engineering 6, 4 (2009), 046002.
- [15] David M Brandman, Michael C Burkhart, Jessica Kelemen, Brian Franco, Matthew T Harrison, and Leigh R Hochberg. 2018. Robust closed-loop control of a cursor in a person with tetraplegia using Gaussian process regression. Neural computation 30, 11 (2018), 2986–3008.
- [16] David M Brandman, Tommy Hosman, Jad Saab, Michael C Burkhart, Benjamin E Shanahan, John G Ciancibello, Anish A Sarma, Daniel J Milstein, Carlos E Vargas-Irwin, Brian Franco, et al. 2018. Rapid calibration of an intracortical brain–computer interface for people with tetraplegia. Journal of neural engineering 15, 2 (2018), 026007.
- [17] Marco Caligari, Marco Godi, Simone Guglielmetti, Franco Franchignoni, and Antonio Nardone. 2013. Eye tracking communication devices in amyotrophic lateral sclerosis: impact on disability and quality of life. Amyotrophic Lateral Sclerosis and Frontotemporal Degeneration 14, 7-8 (2013), 546–552.
- [18] Daniel N Candrea, Samyak Shah, Shiyu Luo, Miguel Angrick, Qinwan Rabbani, Christopher Coogan, Griffin W Milsap, Kevin C Nathan, Brock A Wester, William S Anderson, et al. 2024. A click-based electrocorticographic brain-computer interface enables long-term high-performance switch scan spelling. Communications medicine 4, 1 (2024), 207.
- [19] Nicholas S Card, Tyler Singer-Clark, Hamza Peracha, Carrina Iacobacci, Xianda Hou, Maitreyee Wairagkar, Zachery Fogg, Elena Offenberg, Leigh R Hochberg, David M Brandman, et al. 2025. Long-term independent use of an intracortical brain-computer interface for speech and cursor control. bioRxiv (2025), 2025–06.
- [20] Nicholas S Card, Maitreyee Wairagkar, Carrina Iacobacci, Xianda Hou, Tyler Singer-Clark, Francis R Willett, Erin M Kunz, Chaofei Fan, Maryam Vahdati Nia, Darrel R Deo, et al. 2024. An accurate and rapidly calibrating speech neuroprosthesis. New England Journal of Medicine 391, 7 (2024), 609–618.
- [21] Xiaogang Chen, Yijun Wang, Masaki Nakanishi, Xiaorong Gao, Tzyy-Ping Jung, and Shangkai Gao. 2015. High-speed spelling with a noninvasive brain–computer interface. Proceedings of the national academy of sciences 112, 44 (2015), E6058–E6067.
- [22] Jennifer L Collinger, Brian Wodlinger, John E Downey, Wei Wang, Elizabeth C Tyler-Kabara, Douglas J Weber, Angus JC McMorland, Meel Velliste, Michael L Boninger, and Andrew B Schwartz. 2013. High-performance neuroprosthetic control by an individual with tetraplegia. The Lancet 381, 9866 (2013), 557–564.
- [23] Kevin C Davis, Benyamin Meschede-Krasa, Iahn Cajigas, Noeline W Prins, Charles Alver, Sebastian Gallo, Shovan Bhatia, John H Abel, Jasim A Naeem, Letitia Fisher, et al. 2022. Design-development of an at-home modular brain–computer interface (BCI) platform in a case study of cervical spinal cord injury. Journal of neuroengineering and rehabilitation 19, 1 (2022), 53.
- [24] Brian M Dekleva, Jeffrey M Weiss, Michael L Boninger, and Jennifer L Collinger. 2021. Generalizable cursor click decoding using grasp-related neural transients. Journal of neural engineering 18, 4 (2021), 0460e9.
- [25] Hilary O Edughele, Yinghui Zhang, Firdaus Muhammad-Sukki, Quoc-Tuan Vien, Haley Morris-Cafiero, and Michael Opoku Agyeman. 2022. Eye-tracking assistive technologies for individuals with amyotrophic lateral sclerosis. IEEE Access 10 (2022), 41952–41972.
- [26] Karen M Evans, John A Tarduno, Robert A Jacobs, and Jeff B Pelz. 2012. Collecting and analyzing eye-tracking data in outdoor environments. Journal of Eye Movement Research 5, 2 (2012), 11.

- [27] Lawrence Ashley Farwell and Emanuel Donchin. 1988. Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalography and clinical Neurophysiology 70, 6 (1988), 510–523.
- [28] Sharlene N Flesher, Jennifer L Collinger, Stephen T Foldes, Jeffrey M Weiss, John E Downey, Elizabeth C Tyler-Kabara, Sliman J Bensmaia, Andrew B Schwartz, Michael L Boninger, and Robert A Gaunt. 2016. Intracortical microstimulation of human somatosensory cortex. Science translational medicine 8, 361 (2016), 361ra141–361ra141.
- [29] Sharlene N Flesher, John E Downey, Jeffrey M Weiss, Christopher L Hughes, Angelica J Herrera, Elizabeth C Tyler-Kabara, Michael L Boninger, Jennifer L Collinger, and Robert A Gaunt. 2021. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science 372, 6544 (2021), 831–836.
- [30] Ellen Fraser-Barbour, Sally Robinson, Sandra Gendera, I Burton-Clark, Karen R Fisher, June Alexander, and Kellie Howe. 2025. Shifting power to people with disability in co-designed research. Disability & Society 40, 2 (2025), 259–280.
- [31] Melanie Fried-Oken, Lynn Fox, Marie T Rau, Jill Tullman, Glory Baker, Mary Hindal, Nancy Wile, and Jau-Shin Lou. 2006. Purposes of AAC device use for persons with ALS as reported by caregivers. Augmentative and Alternative Communication 22, 3 (2006), 209–221.
- [32] Cristina Gena, Dize Hilviu, Giovanni Chiarion, Silvestro Roatta, Francesca M Bosco, Andrea Calvo, Claudio Mattutino, and Stefano Vincenzi. 2023. The BciAi4SLA project: towards a user-centered BCI. Electronics 12, 5 (2023), 1234.
- [33] Jacob A George, David T Kluger, Tyler S Davis, Suzanne M Wendelken, EV Okorokova, Q He, Christopher C Duncan, Douglas T Hutchinson, Zachary C Thumser, DT Beckler, et al. 2019. Biomimetic sensory feedback through peripheral nerve stimulation improves dexterous use of a bionic hand. Science Robotics 4, 32 (2019), eaax2352.
- [34] Tobii Dynavox Global. 2025. Tobii Dynavox Global. https://tobiidynavox.com/
- [35] Ronnie Gross-Lewis, Tyler Singer-Clark, Tommy Hosman, Rekha Crawford, Anastasia Kapitonava, John D Simeral, and Leigh R Hochberg. 2022. Engaging individuals with tetraplegia in the user-centered design of a home intracortical BCI. In Society for Neuroscience, 2022. SfN.
- [36] Violaine Guy, Marie-Helene Soriani, Mariane Bruno, Theodore Papadopoulo, Claude Desnuelle, and Maureen Clerc. 2018. Brain computer interface with the P300 speller: Usability for disabled people with amyotrophic lateral sclerosis. Annals of physical and rehabilitation medicine 61, 1 (2018), 5–11.
- [37] Aleesha Hamid and Per Ola Kristensson. 2024. 40 years of eye typing: Challenges, gaps, and emergent strategies. Proceedings of the ACM on Human-Computer Interaction 8, ETRA (2024), 1–19.
- [38] Leigh R Hochberg, Mijail D Serruya, Gerhard M Friehs, Jon A Mukand, Maryam Saleh, Abraham H Caplan, Almut Branner, David Chen, Richard D Penn, and John P Donoghue. 2006. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442, 7099 (2006), 164–171.
- [39] Baosheng James Hou, Joshua Newn, Ludwig Sidenmark, Anam Ahmad Khan, and Hans Gellersen. 2024. Gazeswitch: Automatic eye-head mode switching for optimised hands-free pointing. Proceedings of the ACM on Human-Computer Interaction 8, ETRA (2024), 1–20.
- [40] Hilary Hutchinson, Wendy Mackay, Bo Westerlund, Benjamin B Bederson, Allison Druin, Catherine Plaisant, Michel Beaudouin-Lafon, Stéphane Conversy, Helen Evans, Heiko Hansen, et al. 2003. Technology probes: inspiring design for and with families. In Proceedings of the SIGCHI conference on Human factors in computing systems. 17–24.
- [41] Justin J Jude, Hadar Levi-Aharoni, Alexander J Acosta, Shane B Allcroft, Claire Nicolas, Bayardo E Lacayo, Nicholas S Card, Maitreyee Wairagkar, David M Brandman, Sergey D Stavisky, et al. 2025. An intuitive, bimanual, high-throughput QWERTY touch typing neuroprosthesis for people with tetraplegia. medRxiv (2025), 2025–04.
- [42] Per Ola Kristensson and Keith Vertanen. 2012. The potential of dwell-free eye-typing for fast assistive gaze communication. In Proceedings of the symposium on eye tracking research and applications. 241–244.
- [43] Andrea Kübler, Elisa M Holz, Angela Riccio, Claudia Zickler, Tobias Kaufmann, Sonja C Kleih, Pit Staiger-Sälzer, Lorenzo Desideri, Evert-Jan Hoogerwerf, and Donatella Mattia. 2014. The user-centered design as novel perspective for evaluating the usability of BCI-controlled applications. PloS one 9, 12 (2014), e112392.
- [44] Kaylo T Littlejohn, Cheol Jun Cho, Jessie R Liu, Alexander B Silva, Bohan Yu, Vanessa R Anderson, Cady M Kurtz-Miott, Samantha Brosler, Anshul P Kashyap, Irina P Hallinan, et al. 2025. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nature neuroscience (2025), 1–11.
- [45] Ana Londral. 2022. Assistive technologies for communication empower patients with ALS to generate and self-report health data. Frontiers in Neurology 13 (2022), 867567.
- [46] Sean L Metzger, Kaylo T Littlejohn, Alexander B Silva, David A Moses, Margaret P Seaton, Ran Wang, Maximilian E Dougherty, Jessie R Liu, Peter Wu, Michael A Berger, et al. 2023. A high-performance neuroprosthesis for speech decoding and avatar control. Nature 620, 7976 (2023), 1037–1046.
- [47] Matthew Middendorf, Grant McMillan, Gloria Calhoun, and Keith S Jones. 2000. Brain-computer interfaces based on the steady-state visual-evoked response. IEEE transactions on rehabilitation engineering 8, 2 (2000), 211–214.
- [48] David A Moses, Sean L Metzger, Jessie R Liu, Gopala K Anumanchipalli, Joseph G Makin, Pengfei F Sun, Josh Chartier, Maximilian E Dougherty, Patricia M Liu, Gary M Abrams, et al. 2021. Neuroprosthesis for decoding speech in a paralyzed person with anarthria. New England Journal of Medicine 385, 3 (2021), 217–227.
- [49] Masaki Nakanishi, Yijun Wang, Yu-Te Wang, Yasue Mitsukura, and Tzyy-Ping Jung. 2014. A high-speed brain speller using steady-state visual evoked potentials. International journal of neural systems 24, 06 (2014), 1450019.
- [50] Alan F Newell and Peter Gregor. 2000. “User sensitive inclusive design”—in search of a new paradigm. In Proceedings on the 2000 conference on Universal Usability. 39–44.

- [51] Umut Orhan, Kenneth E Hild, Deniz Erdogmus, Brian Roark, Barry Oken, and Melanie Fried-Oken. 2012. RSVP keyboard: An EEG based typing interface. In 2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 645–648.
- [52] Chethan Pandarinath, Paul Nuyujukian, Christine H Blabe, Brittany L Sorice, Jad Saab, Francis R Willett, Leigh R Hochberg, Krishna V Shenoy, and Jaimie M Henderson. 2017. High performance communication by people with paralysis using an intracortical brain-computer interface. elife 6

(2017), e18554.

- [53] Sebastian Pannasch, Jens R Helmert, Susann Malischke, Alexander Storch, and Boris M Velichkovsky. 2008. Eye typing in application: A comparison of two systems with ALS patients. Journal of Eye Movement Research 2, 4 (2008).
- [54] Brian N Pasley, Stephen V David, Nima Mesgarani, Adeen Flinker, Shihab A Shamma, Nathan E Crone, Robert T Knight, and Edward F Chang. 2012. Reconstructing speech from human auditory cortex. PLoS biology 10, 1 (2012), e1001251.
- [55] K Michelle Patrick-Krueger, Ian Burkhart, and Jose L Contreras-Vidal. 2025. The state of clinical trials of implantable brain–computer interfaces. Nature reviews bioengineering 3, 1 (2025), 50–67.
- [56] Abdul Moiz Penkar, Christof Lutteroth, and Gerald Weber. 2012. Designing for the eye: design parameters for dwell in gaze interaction. In Proceedings of the 24th australian computer-human interaction conference. 479–488.
- [57] Betsy Phillips and Hongxin Zhao. 1993. Predictors of assistive technology abandonment. Assistive technology 5, 1 (1993), 36–45.
- [58] Malcolm Proudfoot, Ricarda AL Menke, Rakesh Sharma, Claire M Berna, Stephen L Hicks, Christopher Kennard, Kevin Talbot, and Martin R Turner. 2016. Eye-tracking in amyotrophic lateral sclerosis: a longitudinal study of saccadic and cognitive tasks. Amyotrophic Lateral Sclerosis and Frontotemporal Degeneration 17, 1-2 (2016), 101–111.
- [59] Mamunur Rashid, Norizam Sulaiman, Anwar PP Abdul Majeed, Rabiu Muazu Musa, Ahmad Fakhri Ab. Nasir, Bifta Sama Bari, and Sabira Khatun.

2020. Current status, challenges, and possible solutions of EEG-based brain-computer interface: a comprehensive review. Frontiers in neurorobotics 14 (2020), 25.

- [60] Martijn Schreuder, Angela Riccio, Monica Risetti, Sven Dähne, Andrew Ramsay, John Williamson, Donatella Mattia, and Michael Tangermann. 2013. User-centered design in brain–computer interfaces—A case study. Artificial intelligence in medicine 59, 2 (2013), 71–80.
- [61] Nishal P Shah, Matthew S Willsey, Nick Hahn, Foram Kamdar, Donald T Avansino, Chaofei Fan, Leigh R Hochberg, Francis R Willett, and Jaimie M Henderson. 2024. A flexible intracortical brain-computer interface for typing using finger movements. bioRxiv (2024).
- [62] Alexander B Silva, Kaylo T Littlejohn, Jessie R Liu, David A Moses, and Edward F Chang. 2024. The speech neuroprosthesis. Nature Reviews Neuroscience 25, 7 (2024), 473–492.
- [63] John D Simeral, Thomas Hosman, Jad Saab, Sharlene N Flesher, Marco Vilela, Brian Franco, Jessica N Kelemen, David M Brandman, John G Ciancibello, Paymon G Rezaii, et al. 2021. Home use of a percutaneous wireless intracortical brain-computer interface by individuals with tetraplegia. IEEE Transactions on Biomedical Engineering 68, 7 (2021), 2313–2325.
- [64] Richard C Simpson and Heidi Horstmann Koester. 1999. Adaptive one-switch row-column scanning. IEEE Transactions on Rehabilitation Engineering 7, 4 (1999), 464–473.
- [65] Tyler Singer-Clark, Ronnie Gross-Lewis, Tommy Hosman, Anastasia Kapitonava, John D Simeral, and Leigh R Hochberg. 2021. Enabling a high quality user experience during independent home use of an iBCI by an individual with tetraplegia. In Society for Neuroscience, 2021. SfN.
- [66] Tyler Singer-Clark, Xianda Hou, Nicholas S Card, Maitreyee Wairagkar, Carrina Iacobacci, Hamza Peracha, Leigh R Hochberg, Sergey D Stavisky, and David M Brandman. 2025. Speech motor cortex enables BCI cursor control and click. Journal of Neural Engineering 22, 3 (2025), 036015.
- [67] Marc W Slutzky. 2019. Brain-machine interfaces: powerful tools for clinical treatment and neuroscientific investigations. The Neuroscientist 25, 2

(2019), 139–154.

- [68] Sergey D Stavisky. 2025. Restoring Speech Using Brain–Computer Interfaces. Annual Review of Biomedical Engineering 27 (2025).
- [69] Bernhard Suhm, Brad Myers, and Alex Waibel. 2001. Multimodal error correction for speech user interfaces. ACM transactions on computer-human interaction (TOCHI) 8, 1 (2001), 60–98.
- [70] Ike Swetlitz. 2025. Neuralink Sees $1 Billion of Revenue by 2031 in Vast Expansion. https://www.bloomberg.com/news/articles/2025-07-23/neuralinksees-1-billion-of-revenue-by-2031-in-vast-expansion?embedded-checkout=true
- [71] UC Davis Health. 2024. New Brain-Computer Interface (BCI) Allows Man with ALS to “Speak” Again Using Brain Implant and AI. https://www. youtube.com/watch?v=thPhBDVSxz0
- [72] Mariska J Vansteensel, Elmar GM Pels, Martin G Bleichner, Mariana P Branco, Timothy Denison, Zachary V Freudenburg, Peter Gosselaar, Sacha Leinders, Thomas H Ottens, Max A Van Den Boom, et al. 2016. Fully implanted brain–computer interface in a locked-in patient with ALS. New England Journal of Medicine 375, 21 (2016), 2060–2066.
- [73] Maitreyee Wairagkar, Nicholas S Card, Tyler Singer-Clark, Xianda Hou, Carrina Iacobacci, Lee M Miller, Leigh R Hochberg, David M Brandman, and Sergey D Stavisky. 2025. An instantaneous voice-synthesis neuroprosthesis. Nature (2025), 1–8.
- [74] Benjamin Warner, Antoine Chaffin, Benjamin Clavié, Orion Weller, Oskar Hallström, Said Taghadouini, Alexis Gallagher, Raja Biswas, Faisal Ladhak, Tom Aarsen, Nathan Cooper, Griffin Adams, Jeremy Howard, and Iacopo Poli. 2024. Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference. arXiv:2412.13663 [cs.CL] https://arxiv.org/abs/2412.13663
- [75] Jeffrey M Weiss, Robert A Gaunt, Robert Franklin, Michael L Boninger, and Jennifer L Collinger. 2019. Demonstration of a portable intracortical brain-computer interface. Brain-Computer Interfaces 6, 4 (2019), 106–117.
- [76] Francis R Willett, Donald T Avansino, Leigh R Hochberg, Jaimie M Henderson, and Krishna V Shenoy. 2021. High-performance brain-to-text communication via handwriting. Nature 593, 7858 (2021), 249–254.

- [77] Francis R Willett, Erin M Kunz, Chaofei Fan, Donald T Avansino, Guy H Wilson, Eun Young Choi, Foram Kamdar, Matthew F Glasser, Leigh R Hochberg, Shaul Druckmann, et al. 2023. A high-performance speech neuroprosthesis. Nature 620, 7976 (2023), 1031–1036.
- [78] Rolfe Winkler. 2025. Exclusive | Apple to Support Brain-Implant Control of Its Devices. https://www.wsj.com/tech/apple-brain-computer-interface9ec69919
- [79] Jacob O Wobbrock, Shaun K Kane, Krzysztof Z Gajos, Susumu Harada, and Jon Froehlich. 2011. Ability-based design: Concept, principles and examples. ACM Transactions on Accessible Computing (TACCESS) 3, 3 (2011), 1–27.
- [80] Han Yuan and Bin He. 2014. Brain–computer interfaces using sensorimotor rhythms: current state and future perspectives. IEEE Transactions on Biomedical Engineering 61, 5 (2014), 1425–1435.

