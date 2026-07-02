- [6] T. Deliagina, “Vestibular compensation in lampreys: impairment and recoveryofequilibrium control during locomotion,” J. Exp.Biol., vol. 200, pp. 1459–1471, 1997.
- [7] C. Rovainen, “Electrophysiology of vestibulospinal and vestibuloreticulospinal systems in lampreys,” J. Neurophysiol., vol. 42, pp. 745–766, 1979.
- [8] S. Alford, I. Zompa, and R. Dubuc, “Long-term potentiation of glutamatergic pathways in the lamprey brainstem,” J. Neurosci., vol. 15, pp. 7528–7538, 1995.
- [9] K. M. Fleming, B. D. Reger, V. Sanguineti, S. Alford, and F. A. MussaIvaldi, “Connecting brains to robots: an artificial animal for the study of learning in vertebrate nervous system,” in Proceedings of the VI International Conference on Simulation of Adaptive Systems. Cambridge, MA: MIT Press, 2000.
- [10] H. Abarbanel, Analysis of Observed Chaotic Data. New York: Springer-Verlag, 1996.
- [11] A. Karniel, K. Fleming, V. Sanguineti, S. Alford, and F. Mussa-Ivaldi, “Dynamic properties of the Lamprey’s neuronal curcuits as it drives a two-wheeled robot,” in Proceedings of the SAB’2002 Workshop on Motor Control in Humans and Robots: On the Interplay of Real Brains and Artificial Devices, J. M. Carmena and G. Maistros, Eds. Edinburgh, Scotland, 2002, pp. 29–36.
- [12] M. Takahashi and S. Alford, “The requirement of presynaptic metabotropic glutamate receptors for the maintenance of locomotion,” J. Neurosci., vol. 22, pp. 3692–3699, 2002.
- [13] N. Scwartz and S. Alford, “Physiological activation of presynaptic metabotropic glutamate receptors increases intracellular calcium and glutamate release,” J. Neurophysiol., vol. 84, pp. 415–427, 2000.

# Asynchronous BCI and Local Neural Classifiers: An Overview of the Adaptive Brain Interface Project

José del R. Millán and Josep Mouriño

Abstract—In this communication, we give an overview of our work on an asynchronous brain–computer interface (where the subject makes selfpaced decisions on when to switch from one mental task to the next) that responds every 0.5 s. A local neural classifier tries to recognize three different mental tasks; it may also respond “unknown” for uncertain samples

- as the classifier has incorporated statistical rejection criteria. We report our experience with 15 subjects. We also briefly describe two brain-actuated applications we have developed: a virtual keyboard and a mobile robot (emulating a motorized wheelchair).

Index Terms—Asynchronous protocol, brain-actuated applications, brain–computer interfaces (BCIs), electroencephalogram (EEG), local-neural classifier.

I. INTRODUCTION

Over the last seven years, our brain–computer interface (BCI) laboratory, in cooperation with the Institute Santa Lucia, Rome, Italy, and

Manuscript received July 19, 2002; revised April 2, 2003. This work was supported in part by the European ESPRIT Program under LTR Project 28193-ABI. The work of J. d. R. Millán was supported by the Swiss National Science Foundation through the National Centre of Competence in Research (NCCR) on “Interactive Multimodal Information Management (IM2).”

J. d. R. Millán was with the Joint Research Centre, European Commission, I-21020 Ispra (VA), Italy. He is now with the Dalle Molle Institute for Perceptual Artificial Intelligence, CH-1920 Martigny, Switzerland (e-mail: jose.millan@idiap.ch).

J. Mouriño was with the Joint Research Centre, European Commission, I-21020 Ispra (VA), Italy. He is now with the Centre de Recerca en Enginyeria Biomédica, Universitat Politècnica de Catalunya, E-08028 Barcelona, Spain (e-mail: jmourino@eic.ictnet.es).

Digital Object Identifier 10.1109/TNSRE.2003.814435

the Computational Engineering Laboratory of the Helsinki University of Technology, Finland, has developed a portable BCI, called Adaptive Brain Interface (ABI), based on the on-line analysis of spontaneous electroencephalogram (EEG) signals measured with eight scalp electrodes and able to recognize three mental tasks. Our approach relies on an asynchronous protocol where the subject decides voluntarily when to switch between mental tasks and uses a simple local neural classifier to recognize, every 0.5 s, the mental task on which the subject is concentrating [1]. ABI is being used to operate two brain-actuated devices: a virtual keyboard and a mobile robot (emulating a motorized wheelchair) [2]–[4].

Like some of the other BCIs reported in the literature, our BCI is based on the analysis of EEG signals associated with spontaneous mental activity. In particular, we look at local variations of EEG over several cortical areas related to different cognitive mental tasks such as imagination of movements, arithmetic operations, or language. The approach aims at discovering EEG patterns embedded in the continuous EEG signal and associated with different mental states [1], [5], [6]. It applies machine-learning techniques to train the classifier and follows a mutual learning process where the user and the brain interface are coupled and adapt to each other [1], [6], [7]. This accelerates the training process. In the presence of feedback, our subjects achieve good performance in just a few hours of training. Analysis of learned EEG patterns confirms that for a subject to operate satisfactorily his/her personal BCI, the personal BCI must fit the individual features of the subject [1], [8].

Most BCIs are based on synchronous protocols where the subject must follow a fixed repetitive scheme to switch from one mental task to the next [7], [9], [10]. In these synchronous BCI systems, the EEG phenomena to be recognized are time-locked to a cue, and a trial typically lasts from 4 to 10 s or longer. In contrast, ABI and a few other systems rely on asynchronous protocols in which the subject makes voluntary, self-paced decisions on when to stop performing a mental task and when to start the next one [1], [11]. This makes the system very flexible and natural to operate and yields rapid response times (e.g., 0.5 s in our case).

Typically, EEG-based BCIs make binary decisions as they seek to recognize two different mental states and reach accuracy levels that, in general, are around 90%. ABI achieves error rates below 5% for three mental tasks, while correct recognition is 70% (or higher). In the remaining cases (around 20%–25%), the classifier doesn’t respond, since it considers the EEG samples as uncertain. The incorporation of rejection criteria to avoid making risky decisions is an important concern in BCI. From a practical point of view, a low classification error is a critical performance criterion for a BCI; otherwise users can become frustrated and stop utilizing the interface. The system of Roberts and Penny [6] applies Bayesian techniques for rejection purposes.

The classification rates of our system, together with the number of recognizable tasks (3) and the 0.5-s response times, yields a theoretical maximum transmission rate of approximately 2.0 b/s for our system. However, as will be discussed in the following, this bit rate was rarely achieved in practice for long periods.

The use of statistical rejection criteria also helps to deal with an important aspect of a BCI, namely “idle” states where the user is not involved in any particular mental task. In an asynchronous protocol, idle states appear during the operation of a brain-actuated device, while the subject does not want the BCI to carry out any action. Although the neural classifier is not explicitly trained to recognize those idle states, the BCI can process them adequately by giving no response.

1534-4320/03$17.00 © 2003 IEEE

160 IEEE TRANSACTIONS ON NEURAL SYSTEMS AND REHABILITATION ENGINEERING, VOL. 11, NO. 2, JUNE 2003

II. EXPERIMENTAL PROTOCOL

After a short evaluation, every user selects the three mental tasks that he/she finds easier out of the following choices: “relax;” imagination of “left” and “right” hand (or arm) movements; “cube rotation;” “subtraction;” or “word association.” More specifically, the tasks consist of getting relaxed, imagining repetitive self-paced movements of the limb, visualizing a spinning cube, performing successive elementary subtractions by a fixed number (e.g., , , etc.), and concatenating related words. “Relax” is done with eyes closed; the other tasks are performed with eyes open.1

In a given training session, a subject participates in several consecutive training trials (normally four), each lasting approximately 5 min, and separated by breaks of 5–10 min. The subject is seated and performs the selected task during 10–15 s. Then, one of two protocols is followed. In one, the subject voluntarily chooses when to stop performing the first task and decides the next to be undertaken. In this case, the subject verbally informs the operator which task he/she is ready to perform next so that data can be labeled for the training and testing of the neural classifiers. In the other protocol, the operator indicates the next mental task randomly. (The latter option is the acquisition protocol we are following now.) With either protocol, the nature of the acquisition is such that there is a time-shift between the moment the subject actually starts performing a task and the moment the operator introduces the label for the subsequent period. Thus, the acquired EEG data is not time-locked to any kind of event in accordance with the principle of asynchronous BCI. While operating a brain-actuated application, the subject does essentially the same as during the training trial, the only difference being that now he/she switches to the next mental task as soon as the desired action has been carried out.

During the training trials, users receive feedback through three buttons on the computer screen, each of a different color and associated to one of the mental tasks to be recognized. A button lights up when an arriving EEG sample is classified as belonging to the corresponding mental task.

EEG potentials are recorded at the eight standard fronto-centro-parietal locations: , , , , , , , and . The sampling rate is 128 Hz. The raw EEG potentials are first transformed by means of a surface Laplacian (SL) computed globally by means of a spherical spline of order 2 [12], [13].2 Mouriñoet al.[15] comparedifferent ways to compute the SL with a few electrodes. We then use the Welch periodogram algorithm to estimate the power spectrum of each SL-transformed channel over the last second. We average three 0.5-s segments with 50% overlap, which gives a frequency resolution of 2 Hz. The values in the frequency band 8–30 Hz are normalized according to the total energy in that band. Thus, an EEG sample has 96 features (8 channels times 12 components each). The periodogram, and, hence, an EEG sample, is computed every 62.5 ms (i.e., 16 times per second).

An important question in any BCI system is to rule out the possibility that subjects may use electrooculogram (EOG) and electromyogram (EMG) activity as the control signals. Most EOG activity occurs in the delta frequency range (0–4 Hz) [16] (cited in [17]), and so EOG activity should be nearly absent from the band 8–30 Hz we use for analysis. It is still possible that EOG and facial EMG activity is present in this band, but, if so, these artifacts should be more prominent in anterior electrodes than in posterior ones. In fact, we have found that this is not

- 1Note that the recognition of the task “relax” is not based on the detection of

eye movements. Also, as shown in [1], the learned prototypes for this task are not simply based on alpha activity (8–12 Hz) which should increase when the eyes are closed.

- 2Normally, the SL is estimated with a high number of electrodes. However,

- [14] has shown that, for the operation of a BCI, SL waveforms with either a low or a high number of electrodes give statistically similar classification results.

the case for any of our subjects. In particular, we have calculated the proportion of energy between the frontal and posterior locations

This expression gives a real value between 1 (all the energy lies in the posterior sites) and 1 (all the energy is located in the anterior electrodes). This value is always negative (or close to zero) for all mental tasks chosen by the subjects. For instance, in the case of one subject who has extensively operated the virtual keyboard described in Section III, the proportions are 0.63, 0.30, and 0.23 for the mental tasks “relax,” “cube,” and “left,” respectively. In addition, if we apply machine-learning techniques for the selection of those relevant features that best differentiate the mental tasks, we find that the classifier performance improves with only a small proportion of features, which are not grouped in a cluster [8]. This suggests that subjects are not using EMG activity, which is broadband. This supports the fact that only EEG signals account for the control achieved.

III. EXPERIMENTAL RESULTS

ABI has a simple local neural classifier where every unit represents a prototype of one of the mental tasks to be recognized [1]. This local network performs better than more sophisticated approaches such as support vector machines and temporal-processing neural networks (TDNN and Elman-like) [18]. This performance is achieved by simply averaging the outputs of the network for eight consecutive EEG samples (and still yielding a global response every 0.5 s). Once trained, the response of the network for the arriving EEG sample is the task with the highest posterior probability, provided that it is above a given probability confidence threshold (otherwise the response is classified as “unknown”). The posterior probability distribution is based on the Mahalanobis distance from the EEG sample to the different prototypes.

Typically, subjects reach the aforementioned level of performance at the end of a few days of moderate training (around 0.5 h daily). Some subjects have achieved this level in a single day of intensive training. One of the latter subjects is a physically impaired person suffering from spinal muscular atrophy. In total, we have worked with around 15 different subjects in a variety of conditions.

We have developed several demonstrators that illustrate the wide range of systems that can be linked to ABI. Thus, the brain interface can be used to select letters from a virtual keyboard on a computer screen and to write a message. Initially, the whole keyboard (26 English letters plus the space to separate words, for a total of 27 symbols organized in a matrix of three rows by nine columns) is divided in three blocks, each associated to one of the mental tasks. The association between blocks and mental tasks is indicated by the same colors as during the training phase. Each block contains an equal number of symbols, namely nine at this first level (three rows by three columns). Then, once the neural classifier recognizes the block on which the subject is concentrating, this block is split in three smaller blocks, each having three symbols this time (one row). As one of these second-level blocks is selected (the neural classifier recognizes the corresponding mental task), it is again split in three parts. At this third and final level, each block contains one single symbol. Finally, to select the desired symbol, the user concentrates in its associated mental task as indicated by the color of the symbol. This symbol goes to the message and the whole process starts over again. Thus, the process of writing a single letter requires three decision steps.

The actual selection of a block incorporates some additional reliability measures (in addition to the statistical rejection criteria). In par-

ticular, a part of the keyboard is selected only when the corresponding mental task is recognized three times in a row. Also, in the case of an eventual wrong selection, the user can undo it by concentrating immediately on one of the mental tasks of his/her choice. Thus, the system waits a short time after every selection (3.5 s) before going down to next level. The mental task used to undo selection is that for which the user exhibits the best performance. For our trained subjects, it takes 22.0 s on average to select a letter. This time includes recovering from eventual errors [3]. Thus, the actual bit rate in this particular implementation is about 0.22 b/s, far less than the maximum theoretical bit rate of 2.0 b/s. This discrepancy is due to the additional reliability measures we have incorporated to increase the likelihood of correct functioning. In preliminary work where those reliability measures were relaxed (requiring that two consecutive responses were the same and eliminating the waiting period, but adding an additional symbol for undoing the last selection), one subject could write letters at an average speed of 7.0 s. This translates to a bit rate of 0.69 b/s.

ABI also makes possible the continuous control of a mobile robot (emulating a motorized wheelchair) generating nontrivial trajectories among different rooms in a house-like environment. The key idea here is that the user’s mental states are associated with high-level commands (e.g., “turn right at the next occasion”) and that the robot executes these commands autonomously using the readings of its on-board sensors. Another critical feature is that a subject can issue high-level commands

- at any moment. This is possible because the operation of the BCI is asynchronous and, unlike synchronous approaches, does not require waiting for external cues. The robot relies on a behavior-based controller to implement the high-level commands to guarantees obstacle avoidance and smooth turns. In this kind of controller, on-board sensors are read constantly and determine the next action to take.

The mapping from the user’s mental states is not the only input to determine the robot’s behavior. In order to achieve more flexible control of the robot, the mental states are just one of the inputs for a finite state automaton with 6 states (or behaviors). The transitions between behaviors are determined by the three mental states (#1, #2, #3) of the user, supplemented by six perceptual states of the environment determined from the robot’s sensory readings (left wall, right wall, wall or obstacle in front, left obstacle, right obstacle, and free space.) The robot’s interpretation of a particular mental state depends on the perceptual state of the robot. Thus, in an open space, mental state #2 means “left turn;” on the other hand, if a wall is detected on the left-hand side, mental state #2 is interpreted as “follow left wall.” Similarly, depending on the perceptual state of the robot, mental state #3 can mean “right turn” or “follow right wall.” However, mental state #1 always means “move forward.” The robot continues executing a particular behavior until the next mental state is received. Using this system, two subjects have succeeded in mentally driving the robot along nontrivial trajectories in an office environment visiting three or four rooms in the desired order. Furthermore, experimental results [4] show that mental control of the robot is only marginally worse than manual control for the same trajectories.

IV. DISCUSSION AND CONCLUSION

A key concern for BCI technology to move beyond demonstrations is to keep the brain interface constantly tuned to its owner. This requirement arises because, as subjects gain experience, they develop new capabilities and change their EEG patterns. In addition, brain activity changes naturally over time. In particular, this is the case from one session (with which data the classifier is trained) to the next (where the classifier is applied). The challenge is to adapt online the classi-

fier while the subject operates a brain-actuated device. In this respect, local neural classifiers are better suited for online learning than other methods due to their robustness against catastrophic interference and their simple learning rules. Furthermore, online adaptation should be ongoing even when the subject’s intention is not known instant by instant. To address this issue, we could resort to reinforcement learning techniques [19], especially if the subject is controlling robotic devices, a task in which these machine-learning techniques have been demonstrated to be particularly effective [20].

REFERENCES

- [1] J. d. R. Millán, J. Mouriño, M. Franzé, F. Cincotti, M. Varsta, J. Heikkonen, and F. Babiloni, “A local neural classifier for the recognition of EEG patterns associated to mental tasks,” IEEE Trans. Neural Networks, vol. 13, pp. 678–686, May 2002.
- [2] J. d. R. Millán, “Brain-computer interfaces,” in Handbook of Brain Theory and Neural Networks, 2nd ed, M. A. Arbib, Ed. Cambridge, MA: MIT Press, 2002.
- [3] , “Adaptive brain interfaces,” Commun. ACM, vol. 46, pp. 74–80, 2003.

- [4] J. d. R. Millián, F. Renkens, J. Mouriño, and W. Gerstner, “Non-invasive brain-actuated control of a mobile robot,” in Proc. 18th Int. Joint Conf. Artificial Intelligence, Acapulco, Mexico, 2003.
- [5] C. W. Anderson, “Effects of variations in neural network topology and output averaging on the discrimination of mental tasks from spontaneous EEG,” J. Int. Syst., vol. 7, pp. 165–190, 1997.
- [6] S. J. Roberts and W. D. Penny, “Real-time brain-computer interfacing: A preliminary study using Bayesian learning,” Med. Biol. Eng. Comput., vol. 38, pp. 56–61, 2000.
- [7] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proc. IEEE, vol. 89, pp. 1123–1134, July 2001.
- [8] J. d. R. Millán, M. Franzé, J. Mouriño, F. Cincotti, and F. Babiloni, “Relevant EEG features for the classification of spontaneous motor-related tasks,” Biol. Cybern., vol. 86, pp. 89–95, 2002.
- [9] J. R. Wolpaw and D. J. McFarland, “Multichannel EEG-based brain-computer communication,” Electroencephalogr. Clin. Neurophysiol., vol. 90, pp. 444–449, 1994.
- [10] N. Birbaumer, N. Ghanayim, T. Hinterberger, I. Iversen, B. Kotchoubey, A. Kübler, J. Perelmouter, E. Taub, and H. Flor, “A spelling device for the paralyzed,” Nature, vol. 398, pp. 297–298, 1999.
- [11] G. E. Birch and S. G. Mason, “Brain computer interface research at the neil squire foundation,” IEEE Trans. Rehab. Eng., vol. 8, pp. 193–195, June 2000.
- [12] F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier, “Spherical spline for potential and current density mapping,” Electroencephalogr. Clin. Neurophysiol., vol. 72, pp. 184–187, 1989.
- [13] , “Corrigendum EEG 02274,” Electroencephalogr. Clin. Neurophysiol., vol. 76, p. 565, 1990.

- [14] F. Babiloni, F. Cincotti, L. Bianchi, G. Pirri, J. d. R. Millán, J. Mouriño, S. Salinari, and M. G. Marciani, “Recognition of imagined hand movements with low resolution surface Laplacian and linear classifiers,” Med. Eng. Phys., vol. 23, pp. 323–328, 2001.
- [15] J. Mouriño, J. d. R. Millán, F. Cincotti, S. Chiappa, R. Jané, and F. Babiloni, “Spatial filtering in the training process of a brain computer interface,” in Proc. 23rd Annu. Int. Conf. Engineering in Medicine and Biology Soc., Istambul, Turkey, 2001, pp. 639–642.
- [16] P. Berg, “Comments on EOG correction methods,” J. Psychophysiol., vol. 3, pp. 41–44, 1989.
- [17] R. J. Croft and R. J. Barry, “EOG correction: A new perspective,” Electroencephalogr. Clin. Neurophysiol., vol. 107, pp. 387–394, 1998.
- [18] A. Hauser, P.-E. Sottas, and J. d. R. Millán, “Temporal processing of brain activity for the recognition of EEG patterns,” in Proc. Int. Conf. Artificial Neural Networks, Madrid, Spain, 2002, pp. 1125–1130.
- [19] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. Cambridge, MA: MIT Press, 1998.
- [20] J. d. R. Millán, “Rapid, safe, and incremental learning of navigation strategies,” IEEE Trans. Syst. Man Cybern. B, vol. 26, pp. 408–420, June 1996.

