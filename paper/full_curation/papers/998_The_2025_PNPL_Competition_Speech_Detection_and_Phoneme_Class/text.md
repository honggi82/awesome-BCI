arXiv:2506.10165v1[cs.LG]11Jun2025

# The 2025 PNPL Competition: Speech Detection and Phoneme Classification in the LibriBrain Dataset

Gilad Landau1,N Miran Özdogan1,N Gereon Elvers1,N Francesco Mantegna1,N Pratik Somaiya1,N Dulhan Jayalath1,N Luisa Kurth1,N Teyun Kwon1,N Brendan Shillingford2 Greg Farquhar2 Minqi Jiang3 Karim Jerbi4,5 Hamza Abdelhedi4,5 Yorguin Mantilla Ramos4,5 Caglar Gulcehre6 Mark Woolrich7,8,N Natalie Voets8,N Oiwi Parker Jones1,N

[Figure 1]

1PNPL 2Google DeepMind 3MetaAI 4Mila 5Université de Montréal 6EPFL 7OHBA 8WIN NUniversity of Oxford

{gilad, oiwi}@robots.ox.ac.uk

## Abstract

The advance of speech decoding from non-invasive brain data holds the potential for profound societal impact. Among its most promising applications is the restoration of communication to paralysed individuals affected by speech deficits such as dysarthria, without the need for high-risk surgical interventions. The ultimate aim of the 2025 PNPL competition is to produce the conditions for an “ImageNet moment” or breakthrough in non-invasive neural decoding, by harnessing the collective power of the machine learning community.

To facilitate this vision we present the largest within-subject MEG dataset recorded to date (LibriBrain) together with a user-friendly Python library (pnpl) for easy data access and integration with deep learning frameworks. For the competition we define two foundational tasks (i.e. Speech Detection and Phoneme Classification from brain data), complete with standardised data splits and evaluation metrics, illustrative benchmark models, online tutorial code, a community discussion board, and public leaderboard for submissions. To promote accessibility and participation the competition features a Standard track that emphasises algorithmic innovation, as well as an Extended track that is expected to reward larger-scale computing, accelerating progress toward a non-invasive brain-computer interface for speech.

Keywords Neural Decoding, Non-Invasive, MEG, Speech Comprehension, LibriBrain

## 1 Competition description

### 1.1 Background and impact

Until a few years ago, the idea of communicating through a neural prosthetic was confined to science fiction. Today the frontier of neuroscience and artificial intelligence (AI) holds the potential of expansive benefits for people who have lost the ability to speak because of debilitating ailments, such as traumatic brain injury and motor neurone disease. In 2021, the first brain-computer interface (BCI) capable of restoring connected-speech to a paralysed individual appeared [25]. This landmark BCI

Preprint. Under review.

[Figure 2]

Figure 1: Overview of data and labels. (A) Illustration of a non-invasive MEG scanner and corresponding sensor layout. The layout shows a 2D top-down projection of the MEG sensor positions on the scalp. (B) Schematic comparing the per-subject recording durations of comparable MEG datasets (gray) [33, 10, 16, 2] with the LibriBrain dataset (orange) [42]. LibriBrain is approximately 5× bigger than the next biggest dataset, and 25-50× bigger than typical datasets. (C) Example MEG recordings with annotations, showing aligned audio, phoneme labels, and speech/non-speech segments. These labels provide the basis for the Speech Detection and Phoneme Classification tasks.

enabled sentence decoding from surgically-implanted electrodes for a limited 50-word vocabulary, achieving a promising 25.6% word-error rate (WER).

Since then, new surgical data and AI systems have resulted in BCIs with vocabulary sizes increasing up to 125,000 words [35, 8] and reported WERs decreasing down to less than 5% [8]. This is remarkable as 10% WER is often cited as the threshold for widespread adoption of automatic speech recognition (ASR), when it reached human parity [38] on realistic conversational benchmarks [14].

Despite this rapid progress, invasive BCIs face fundamental limitations to widespread adoption. Two critical limitations are that brain surgery is inherently dangerous and that surgical data does not easily scale. By contrast, non-invasive neuroimaging offers a safe alternative that can be easily repeated in healthy participants, unlocking data collection at unprecedented scale. Amongst current technologies, magnetoencephalography (MEG) stands out for its unique strengths. It is a direct measure of neuronal activity, providing millisecond temporal resolution equivalent to intracranial recordings. In this respect, MEG is also like electroencephalography (EEG). But, whereas the spatial resolution of EEG is significantly degraded by volume conduction and electrical artefacts from the skull and scalp, the magnetic fields that MEG measures pass through biological tissue without distortion. MEG systems routinely achieve spatial localisation in the range of 5–10 mm [34], and, in some studies, resolution as precise as 2 mm has been achieved [3]. MEG recordings can therefore approach, or, under ideal conditions, even exceed the precision of invasive modalities for speech BCIs such as electrocorticography (ECoG) [25, 24].

Compared to invasive modalities, a key limitation of MEG is the greater distance between sensors and neural sources, which typically results in lower signal-to-noise ratios. Our working hypothesis is that with enough high-quality data, and with the right deep learning methods, MEG-based speech decoding should be able to compete with surgical alternatives. We are therefore proposing this competition to coincide with PNPL’s first big release of data. Prior to this, the biggest public EEG and MEG datasets have typically included tens to hundreds of participants, but only 1–2 hours per person [26, 33, 6, 10, 1, 16], resulting in data that can be characterised as broad but shallow. An

exception is a dataset including 10 hours of within-subject MEG data [2]. Empirical results show that deep data, representing big data acquired over repeated scans from the same subject, yield the largest gains in decoding performance [10]. So, it is good timing for us to be releasing the deepest within-subject, speech decoding dataset to date. In this first release of the LibriBrain dataset [42], we include over 50 hours of MEG, which is 5× the previously biggest dataset [2], and 25–50× bigger than most other MEG and EEG datasets. Given that data is king, we expect the competition to break new ground in non-invasive speech decoding (see Figure 1).

The first PNPL competition will focus on two basic but fundamental tasks, which have been influential in the development of both ASR and invasive brain-to-text (B2T). Several recent efforts to train non-invasive B2T systems with MEG or EEG have reported WERs approaching 100%, indicating uninformative or near-chance performance [19, 40, 41, 39]. Other recent non-invasive works have found success by exploring a diverse set of simpler tasks such as Segment Identification [11], Word Classification [10], and (Phonetic) Feature Classification [18]. To make the most of the available data, the 2025 PNPL competition will focus on the tasks of Speech Detection and Phoneme Classification. To illustrate the efficiency of these tasks, consider that the LibriBrain dataset includes 1,523,920 phoneme examples divided over 39 phoneme classes. Compare this to a task like Word Classification, where an order of magnitude fewer examples (466,264 words) are divided over many more classes (e.g. 16,892 distinct words). Even if one were to limit the vocabulary to the most frequent 250 words

- [10], or even to the most frequent 50 words [25], Word Classification leverages fewer examples per class. Of course, restricting the vocabulary also results in excluded data. Speech Detection is even more efficient as we make a binary prediction for every temporal sample (250 per second). Inspired by the success of ImageNet [32], our vision is to repeat the PNPL Competition over multiple years. So, as the community solves foundational tasks like Speech Detection and Phoneme Classification, and as our dataset grows ever bigger, we will host a series of future PNPL Competitions across a curriculum of increasingly difficult tasks.

To encourage both advances in the state-of-the-art and inclusion of participants in the PNPL competition, we will host two tracks for each task. In the Standard track, participants will train and test their submissions on data from the LibriBrain dataset. This track aims to make the competition relevant and accessible to all participants by levelling the playing field in terms of training data; we expect that this track will reward methodological innovations. In the Extended track, participants can train their submissions on any data they want. Recent work has shown that MEG data from multiple datasets can be effectively pooled to improve downstream decoding performance with unsupervised pre-training [18], with domain adaptation [31], and by selectively combining datasets based on a measure of their quality [17]. To enable useful comparisons, teams competing on the Extended track will evaluate their models on the standard LibriBrain holdout splits. This track is meant to encourage the use of more compute, in order to see how far teams with resources can push the state-of-the-art.

The 2025 PNPL competition is a collaborative effort by researchers from academia and industry, and from a number of places around the world. To make the competition as accessible as benchmark tasks in computer vision, like CIFAR-10 [20], we have put a lot of effort into the materials supporting the competition. Chief amongst these is a Python library, which automatically downloads the data as needed and makes it straightforward to integrate into deep learning frameworks like PyTorch [28]. To illustrate how easy it is to use, note that the library can be installed with one line on the command line (pip install pnpl). The dataset is then accessed like other popular datasets (e.g. torchvision and huggingface) in Python (e.g. from pnpl.datasets import LibriBrain). The data is structured into PyTorch-ready tensors, making it easy to integrate with existing machine learning pipelines. The library also comes with methods to generate TSV files for predictions on the competition holdout data, which in turn can be uploaded on a submission website to populate Papers-With-Code style leaderboard plots – gamifying the experience, we hope, in a fun and motivating way for participants.

1.2 Novelty

This is the first competition dedicated to language decoding from non-invasive brain data. An invasive B2T competition was run in 2024 [36] which helped to bridge the jump from a large-vocabulary WER of 23.8% [35] to less than 5% [8]. Recently, the non-invasive field has seen remarkable advances, including the availability of high-quality brain recordings and application of powerful new AI methods

- [11, 10, 18]. Yet, despite this progress, we believe that several key elements are still missing—and that addressing them will be essential to unlocking the next major breakthrough. This competition

Table 1: Overview of data splits and approximate durations. The competition holdout set consists of two disjoint subsets used for leaderboard updates and final rankings.

Competition Holdout Leaderboard Final Rankings

Train Validation Test

Data Public Public Public Public Public Labels Public Public Public Private Private Hours 51.57 0.36 0.38 Private Private

is designed to help close these gaps by focusing on: a the largest dataset of its kind; standard data splits to encourage comparable results in the literature; foundational tasks and evaluation metrics; a competition website; a Python library that allows easy downloading and streamlined integration into deep learning frameworks; tutorial code that runs in the browser with a free GPU for easy onboarding; baseline models that illustrate the viability of the tasks; interactive leaderboards for each competition track; a community Discord for discussion with the organisers and others; and incentives including at least $10,000 in prizes.

### 1.3 Data

The LibriBrain data used for the competition [42] are non-invasive MEG recordings acquired from one healthy participant listening to over 50 hours of audiobooks, all sourced from LibriVox [23]. The MEG recordings were acquired from 306 sensors covering the whole head/brain. Neural data were minimally filtered (e.g. to remove line noise and drift) and downsampled to 250 Hz (see the dataset paper for details [42]). From the perspective of the competition, the MEG data can be thought of as 2-dimensional tensors composed of sensors × temporal samples (see Figure 1C). LibriBrain comes with word- and phoneme-level alignments, as in the LibriSpeech corpus [27], itself a standard resource for automatic speech recognition (ASR). Data and labels can be easily batched using the PNPL library. In practice, one may install the PNPL library from the command line:

1 pip install pnpl

The following is a minimal example that illustrates how only a few lines of Python are required to download the data to a specified folder on the user’s computer (e.g. /data):

- 1 from pnpl.datasets import LibriBrainSpeech
- 2 _ = LibriBrainSpeech(data_path="/data")

If not already present, the dataset will be automatically downloaded to the specified directory. Alternatively, the data may be downloaded manually from Hugging Face.1 MEG data and labels are saved in HDF5 and TSV files, respectively. The full, serialised LibriBrain dataset is approximately 50 GB. The data are standardly split into train, validation, and test sets. For the competition, we include an additional competition holdout split, which includes disjoint subsets of data to be used to update the leaderboard during the competition and to decide the final ranking of submissions (see Table 1).

### 1.4 Tasks and application scenarios

The tasks in the contest are foundational to neural decoding: Speech Detection and Phoneme Classification. Both are supervised and have analogues in the acoustic domain, where early ASR systems were built around phonemes [21, 13, 30] and speech detection has long been a useful preprocessing step in the ASR pipeline [12, 4]. Although we would ultimately like to decode connected speech from the brain, early attemps in EEG and MEG have yielded weak results [40, 41, 39]. There are, however, useful application scenarios for Speech Detection and Phoneme Classification, given their roles in ASR. Historically, speech detection played a critical role in the pipeline of the first invasive speech BCI for a paralysed individual [25]: in this work the user attempted to produce isolated words, so that speech detection also functioned as word detection, and word

1https://huggingface.co/datasets/pnpl/LibriBrain

classification together with an external language model were used to produce transcriptions. Before this work on decoding full transcripts, many invasive studies focused on phoneme classification [5, 15, 22, 29, 7, 37].

When detecting speech from MEG, the input data x is a 306 sensor × T samples tensor. For each sample t ∈ {1,...,T} we have a corresponding label y, where y = 1 if speech or y = 0 if nonspeech. For the phoneme classification task, the dataloader provides fixed windows of data. Each window is an input x with an associated label y, which is one of the standard 39 phoneme classes in the CMU/ARPAbet [9]. The task for each input is to predict which class the brain data corresponds to. So rather than where, as is emphasised in the Speech Detection task, the Phoneme Classification task is primarily about what examples are.

- 1.5 Metrics The metric that we use to measure success in both tasks is the F1-macro score:

F1macro =

1 K

K

k=1

2 ·

Precisionk · Recallk Precisionk + Recallk

This is the unweighted average of per-class F1 scores, where the F1 score is the harmonic mean of Precision and Recall. Here, each class k is a phoneme for Phoneme Classification, or it is speech or non-speech for Speech Detection. For reference, Precision and Recall can be defined in terms of True Positives (TP), False Positives (FP), and False Negatives (FN), each of which is an integer count:

Precision =

TP TP + FP

, Recall =

TP TP + FN

, F1 =

2 · TP 2 · TP + FP + FN

In practice F1macro scores range from 0 to 1 and can be reported as percentages, which we prepose to do in order to communicate proportions clearly in the competition. For Speech Detection, random

guessing under balanced-class assumptions yields F1macro = 21 = 50%. It is possible, however, to do worse than this in imbalanced settings, since F1macro penalises poor performance on the minority class. For example, a naive baseline that always predicts the most frequent label in the LibriBrain

data results in a comparatively lower F1macro score of 45.3%. For Phoneme Classification with 39 balanced classes, the chance of guessing the correct label is 391 ≈ 2.56%. Higher F1macro scores are better. For the competition, a good predictive model should produce Speech Detection scores significantly greater than 50%, and Phoneme Classification scores greater than 2.56% (cf. Table 2).

- 1.6 Baselines, code, and material provided

To help participants get started easily, we have created a Starter Kit that includes a Python library for easy data access, clear tutorials on training baseline models, and baseline scores for comparison. The first component of the starter kit is the PNPL library introduced in section 1.3. It simplifies loading train, validation, and test data and integrating them into minimal training and evaluation loops (similar methods are included to load the competition holdout data and produce submission files):

- 1 from pnpl.datasets import LibriBrainSpeech
- 2 from torch.utils.data import DataLoader
- 3
- 4 train_data = LibriBrainSpeech(data_path="/data", partition="train")
- 5 train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
- 6 for x, y in train_loader: # Iterate through DataLoader as usual
- 7 pass # Perform operations using data x and labels y

- As an entry point to the library, we provide three tutorials in the form of Jupyter Notebooks, optimised for usage in Google Colab.

1. The first tutorial covers data loading and provides foundational information on the problem domain. It also contains the code for training our reference speech detection model. It is suitable for beginners with some previous familiarity in machine learning without any knowledge in the neuroscience domain.

Table 2: F1-macro scores (% ↑ higher is better) for reference models and naive baselines.

Method Speech Detection Phoneme Classification Reference Model 68.04% 60.39% Naive Baseline 45.30% 0.47%

- 2. The second tutorial covers the phoneme classification task in more detail. It assumes familiarity with the dataset and is primarily intended to provide an introduction to the second track. It also contains the code for training our reference phoneme classification model.
- 3. The third tutorial explains how to run and submit model predictions, to populate the leaderboards and participate in the competition.

The architectures of the reference models in the tutorials are designed to significantly outperform naive baselines while also being simple enough for beginners to pick up and train on limited amounts of data within the GPU compute provided. We note that the Google Colab Free Tier provides users with a free GPU to use in the browser2. The tutorial code has also been tested on Unix (e.g. Mac) and Windows machines.

For the speech detection task, we provide a fully trained reference model and report its performance using the evaluation metric (F1macro = 68.04%). To ensure meaningful evaluation, we compare the reference model to a naive strategy that always predicts the majority class (F1macro = 45.30%). We chose a majority class baseline as the evaluation data were collected using a naturalistic experimental design and contain imbalanced classes—mostly speech with short intermittent periods of non-speech. For the phoneme classification task, we provide a reference model for predicting phonemes averaged over sets of 100 samples (F1macro = 60.39%). We compare this against a naive baseline that always predicts the most likely phoneme (majority class) in the training data (F1macro = 0.47%). See Table 2 for a summary.

### 1.7 Website, tutorial and documentation

The website for the competition3 serves as a hub, aggregating a Starter Kit of code, documentation, tutorials, leaderboards for tracking submissions, and links to the submission system. To maximise ease of onboarding for participants, we have produced tutorials for all aspects of the competition in the form of interactive Colab notebooks (e.g. data exploration, task-specific models, submission). To encourage community building, participants also have access to a custom Discord server4 where official announcements will be posted and where participants will be encouraged to discuss their approaches, team up, and exchange ideas. Organisers will be available on Discord. We are also planning a series of blog posts to release at regular intervals during the competition to help advertise the competition, and to inspire dialogue within the community.

2 Organisational aspects

### 2.1 Protocol

Inclusivity is central to our competition. As such, participating is designed to be simple and accessible. For instance, we have ensured that participants can make impactful contributions without expensive hardware or significant technical barriers. To participate, one needs only to install a Python library (pip install pnpl), which, when used, automatically downloads the dataset and provides seamless integration via a standard PyTorch Data Loader. Once the data is loaded, participants are free to develop their solutions and make predictions on the competition holdout data. The PNPL library includes a straightforward method to write these predictions to a TSV file. Submissions are made by manually uploading TSV files to the EvalAI platform. Solutions will be evaluated automatically according to the metrics detailed in section 1.5. Rankings for each submission are continuously

- 2https://research.google.com/colaboratory/faq.html#gpu-availability
- 3https://neural-processing-lab.github.io/2025-libribrain-competition/
- 4https://neural-processing-lab.github.io/2025-libribrain-competition/links/

discord

updated and displayed on our leaderboard. Comprehensive details for every stage of participation, along with tutorials and Colab notebooks equipped with free GPU access, are available on the competition website.

The challenge will consist of two phases for the two tasks. In the first phase, we will release the competition holdout data for the Speech Detection task. Participants will then be able to make official submissions to “Standard” and “Extended” tracks. The second phase will commence after the Speech Detection tracks have closed. In this phase, we will release the competition holdout data for the Phoneme Classification task, and participants will be invited to make submissions to two new tracks.

### 2.2 Rules and engagement

- • This challenge encourages everyone to join and helps us bring forth the societal impact of speech decoding technologies.
- • No domain specific knowledge or specialised hardware is required (free GPU access is available through Google Colab).
- • Although our goal is to democratise the field of speech decoding, we are aware that previous breakthroughs in AI were the result of accumulating more data and computational resources. To resolve this tension, we are splitting the competition into two tracks for each task.
- • In the “Standard” tracks participants may only use the LibriBrain data in their solutions, empowering teams with fewer resources to compete by innovating on the methods side.
- • Pre-trained models may be used, provided they were publicly available and known to the community prior to the launch of the competition (e.g. described in a NeurIPS paper and downloadable from Hugging Face). The organisers reserve the right to make final decisions on any edge cases. Think of this as a hinge loss: staying away from the margin will be safer.
- • In the “Extended” tracks, there are no limits to the training data that participants can use.
- • Teams may submit to all tracks and their progress will be shared on the relevant leaderboards. However, to encourage diversity, any team will only be allowed to win prize money for one track. If the same team were to win multiple tracks, then they would still be listed on the leaderboards, but the next team in the ranking would get the smaller of the prizes.
- • The organisers strongly encourage all participants to share their code in the spirit of openscience. Similarly, participants are invited to submit pull requests to the GitHub repo for the PNPL library (e.g. to add dataloaders to new datasets and thus accelerate the community).
- • The organisers will reach out to participants on the “Standard” tracks who could win prizes to verify that their solutions are not dependent on external datasets by sharing training code, and to participants on the “Extended” tracks to query the amount of compute used. For verification, this may also require models or code by request after the relevant closing date.
- • To avoid data leakage, final ranking will be determined based on independent holdout data.
- • The top 3 confirmed submissions for each track will win, provided they beat the reference

models in Table 2 for each task (i.e. F1macro scores of 68.04% for Speech Detection and 60.39% for Phoneme Classification). In the unlikely event of a tie, the prize will be split.

To facilitate open and continuous communication between the organisers and participants, a dedicated Discord channel will be used as the primary platform for all contest-related discussions. This includes addressing specific questions, enabling real-time discussion, and providing technical support. The forum will be managed collaboratively by contest organisers to ensure comprehensive support.

### 2.3 Schedule and readiness

The organisers are ready at the time of submission with working versions of all competition materials. The proposed schedule will commence advertisement on the day that competition acceptances are announced. We will then provide a few weeks for participants to familiarise themselves with the website and with restricted beta versions of the competition materials. To promote a fair competition, the full set of materials will be released for the Speech Detection Tracks on 1 June, 2025, with 2 months allocated for submissions. The Phoneme Classification Tracks will then run for another 2 months, leaving time for the organisers to analyse the results and prepare analyses to present

at our NeurIPS session. By staggering the tasks, we hope to generate renewed excitement within the community for the Phoneme Classification Tracks when we announce results from the Speech Detection Tracks. This will also give the organisers more time to verify the Speech Detection results, establishing a protocol to turn around the Phoneme Classification results more quickly.

10 May 26 May, 2025: Acceptance notifications for competition proposals are sent out. The official contest announcement and promotion commence. Beta versions of all necessary resources will be made available through the competition website so participants can familiarise themselves with the tutorial code and set up their training environments. This time will allow participants to familiarise themselves with the materials and seek clarification from the organisers.

1 Jun – 31 Jul, 2025: Official opening of the contest to the public. Phase 1 commences with the start of the Standard and Extended Speech Detection Tracks. All relevant materials released.

1 Aug – 30 Sep, 2025: Phase 2 begins with the release of all materials for the two Phoneme Classification Tracks (Standard and Extended). During this phase, the organisers will evaluate submissions from phase 1, with contenders for prizes being asked to share system details (e.g. training code for the Standard Tracks) to ensure winners adhere to the rules of the competition.

- 1 Oct – 10 Oct, 2025: The organising committee reviews and verifies all results. Winners of the first two Speech Detection Tracks will be announced on the competition website. Contenders for prizes in the second two Phoneme Classification Tracks will be asked to share details about their submissions with the organisers. The organisers will endeavour to contact winners before the NeurIPS Early Registration Deadline (11 Oct, 2025), noting the Visa Application Deadline (16 Oct, 2025). 15 Oct – 1 Dec, 2025: Organisers conduct an in-depth analysis of contest results for the conference.
- 2 Dec – 7 Dec, 2025: The contest will culminate in a dedicated session at NeurIPS. Winners will be announced, prizes will be awarded, and select participants will be invited to present.

At the time of writing this proposal, all of the materials for the competition are ready but have not yet been made publicly available. The equivalent of $10,000 USD has been raised in GBP for prizes. Additional funds are being sought to be able to offer travel and computational support to participants.

2.4 Competition promotion and incentives

We will promote the competition vigorously through social networks, academic mailing lists, and other venues. Special attention will be taken to reach out to all listed NeurIPS affinity groups (e.g. Indigenous in AI, LatinX in AI, Black in AI, Women in ML). A dedicated website has been created, providing information, resources, and continuous updates about the competition. During the competition, the organisers plan to release a series of blog posts that go in-depth into relevant questions from what we know about the tasks, with the aim of creating discussion and further interest in the competition. Participation will be incentivised through rewards, with at least $10,000 available for prizes. To promote inclusivity, we are in ongoing discussions to raise additional funds for travel and compute, especially for participants from under-represented groups in AI and ML. We intend to invite teams with innovative solutions to participate in a joint publication.

- 3 Resources

### 3.1 Resources provided by organisers

The organisers will actively monitor and support the competition, offering technical and scientific guidance through Discord and the competition website. Tutorial code can run in the browser and provides a free GPU for participants. A Python library is available to download the data and integrate it into standard deep learning frameworks. Winners will receive prize money.

### 3.2 Support requested

The main support needed will be the provision of a video-conferencing platform/setting for presentations, and a room for in-person participant gathering and presentations. If possible, we would like to request registration be waived for up to one member apiece from the top-3 submissions in each track, as well as 3 discretionary places (e.g. from under-represented groups; so 15 participants total).

## Organising team

Our team combines AI researchers and neuroscientists, and embodies a strategic collaboration between researchs in Oxford, Montreal, Switzerland, Google, and Meta. We range in levels of seniority from research assistants and master’s students, to DPhil and PhD students, Professors and Research Scientists in Industry. In terms of diversity, our team includes members of multiple NeurIPS affinity groups (e.g. Indigenous in AI and Women in ML).

[Figure 3]

Gilad Landau is a DPhil student in Engineering and member of PNPL , supervised by Oiwi Parker Jones at the University of Oxford.

[Figure 4]

Miran Özdogan is a DPhil student in Computer Science and member of PNPL , supervised by Oiwi Parker Jones and Michael Bronstein, at the University of Oxford.

Gereon Elvers is a master’s student in Information Systems at the Technical University of Munich (TUM) and visiting researcher at PNPL .

[Figure 5]

[Figure 6]

Francesco Mantegna is a Postdoctoral Researcher in PNPL , Department of Engineering Science, University of Oxford. He received his PhD from NYU under the supervision of David Poeppel.

Pratik Somaiya is a Software Engineer at the Oxford Robotics Institute.

Dulhan Jayalath is a DPhil student in Machine Learning at the University of Oxford, supervised by Oiwi Parker Jones as part of PNPL and funded by an Amazon Web Services (AWS) studentship as part of the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems (AIMS). His research interests lie in a range of areas including brain decoding, LLMs, reasoning, and foundation models.

[Figure 7]

[Figure 8]

Luisa Kurth is a DPhil student in PNPL and the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems (AIMS), University of Oxford.

[Figure 9]

Teyun Kwon is a DPhil student in PNPL and the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems (AIMS), University of Oxford.

Brendan Shillingford is a Staff Research Scientist at Google DeepMind. Greg Farquhar is a Staff Research Scientist at Google DeepMind. Minqi Jiang is a Senior Research Scientist at Meta. He was previously a Research Scientist at Google DeepMind.

Karim Jerbi is Professor in the Psychology Department of the Université de Montréal and Associate Professor at Mila. He heads UNIQUE, the Quebec-wide Neuro-AI research center, and is also Canada Research Chair in Computational Neuroscience and Cognitive Neuroimaging.

Hamza Abdelhedi is a Biomedical Engineering PhD student at the Université de Montréal, supervised by Karim Jerbi and specialising in Neuro-AI.

Yorguin Mantilla Ramos is a master’s student at the Université de Montréal and Graduate Research Assistant at Mila.

Caglar Gulcehre is Assistant Professor at the École Polytechnique Fédérale de Lausanne (EPFL) in Switzerland. He previously worked as a Staff Research Scientist at Google DeepMind on many topics in AI, including reinforcement learning, foundation models, novel architectures and training paradigms, safety + alignment, and natural language understanding.

Mark Woolrich is Professor of Computational Neuroscience at the University of Oxford. He is Head of Analysis and Associate Director of the Oxford centre for Human Brain Activity (OHBA).

Natalie Voets is an Associate Professor at the Oxford Centre for Functional MRI of the Brain (FMRIB). She also works in the Awake Neurosurgery Service at the Oxford University Hospitals NHS Foundation Trust. Her research focuses on language mapping in surgical populations.

[Figure 10]

Oiwi Parker Jones heads the Parker Jones Neural Processing Lab (PNPL ) in the Department of Engineering Science, University of Oxford. He is also a Fellow in Computer Science at Jesus College Oxford, a Principal Investigator at the Oxford Robotics Institute, and an Honorary Fellow in the Nuffield Department of Clinical Neurosciences.

## Acknowledgments and Disclosure of Funding

The authors would first like to thank our beta testers for feedback on the website, tutorial code, submission system, and leaderboard. We also gratefully acknowledge the use of the University of Oxford Advanced Research Computing (ARC) facility in carrying out this work (http://dx.doi. org/10.5281/zenodo.22558), and NVIDIA for contributing additional GPUs used in this research. PNPL is supported by the MRC (MR/X00757X/1), Royal Society (RG\R1\241267), NSF (2314493), NFRF (NFRFT-2022-00241), and SSHRC (895-2023-1022).

## References

- [1] B. Accou et al. SparrKULee: A speech-evoked auditory response repository of the KU Leuven, containing EEG of 85 participants. bioRxiv, 2023. URL https://doi.org/10.1101/2023. 07.24.550310.

- [2] K. Armeni, U. Güçlü, M. van Gerven, and J.-M. Schoffelen. A 10-hour within-participant magnetoencephalography narrative dataset to test models of language comprehension. Scientific Data, 9:278, 2022.

- [3] E. L. Barratt, S. T. Francis, P. G. Morris, and M. J. Brookes. Mapping the topological organisation of beta oscillations in motor cortex using MEG. NeuroImage, 181:831–844, 2018. doi: 10.1016/j.neuroimage.2018.06.041. URL https://doi.org/10.1016/j.neuroimage. 2018.06.041.

- [4] J. Benesty, M. Sondhi, and Y. Huang. Speech enhancement. Springer, 2007.

- [5] T. M. Blakely, K. J. Miller, R. P. N. Rao, M. D. Holmes, and J. G. Ojemann. Localization and classification of phonemes using high spatial resolution electrocorticography (ECoG) grids. In 2008 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, pages 4964–4967. IEEE, 2008. doi: 10.1109/IEMBS.2008.4650328. URL https://doi.org/10.1109/IEMBS.2008.4650328.

- [6] M. P. Broderick, A. J. Anderson, G. M. Di Liberto, M. J. Crosse, and E. C. Lalor. Electrophysiological correlates of semantic dissimilarity reflect the comprehension of natural, narrative speech. Current Biology, 28:803–809, 2018.

- [7] J. S. Brumberg, E. J. Wright, D. S. Andreasen, F. H. Guenther, and P. R. Kennedy. Classification of intended phoneme production from chronic intracortical microelectrode recordings in speechmotor cortex. Frontiers in Neuroscience, 5:65, May 2011. doi: 10.3389/fnins.2011.00065. URL https://doi.org/10.3389/fnins.2011.00065.

- [8] N. S. Card, M. Wairagkar, C. Iacobacci, X. Hou, T. Singer-Clark, F. R. Willett, E. M. Kunz, and D. M. Brandman. An accurate and rapidly calibrating speech neuroprosthesis. New England Journal of Medicine, 391(7):609–618, 2024.

- [9] Carnegie Mellon University. The CMU pronouncing dictionary, 1993. http://www.speech. cs.cmu.edu/cgi-bin/cmudict.
- [10] S. d’Ascoli, C. Bel, J. Rapin, H. Banville, Y. Benchetrit, C. Pallier, and J.-R. King. Decoding individual words from non-invasive brain recordings across 723 participants. arXiv preprint,

2024. URL https://arxiv.org/abs/2412.17829.

- [11] A. Défossez, C. Caucheteux, J. Rapin, O. Kabeli, and J.-R. King. Decoding speech perception from non-invasive brain recordings. Nature Machine Intelligence, 5(10):1097–1107,

2023. doi: 10.1038/s42256-023-00714-5. URL https://www.nature.com/articles/ s42256-023-00714-5.

- [12] S. Furui. Speech recognition: Technology and applications. Academic Press, 2000.

- [13] J. S. Garofolo, L. F. Lamel, W. M. Fisher, J. G. Fiscus, D. S. Pallett, and N. L. Dahlgren. TIMIT acoustic-phonetic continuous speech corpus. Linguistic Data Consortium, 1993. https: //catalog.ldc.upenn.edu/LDC93S1.
- [14] J. J. Godfrey, E. C. Holliman, and J. McDaniel. Switchboard: Telephone speech corpus for research and development. In Proc. IEEE ICASSP, pages 517–520, 1992.

- [15] F. H. Guenther, J. S. Brumberg, E. J. Wright, A. Nieto-Castanon, J. A. Tourville, M. Panko, R. Law, S. A. Siebert, J. L. Bartels, D. S. Andreasen, P. Ehirim, H. Mao, and P. R. Kennedy.

- A wireless brain-machine interface for real-time speech synthesis. PLoS ONE, 4(12):e8218, Jan 2009. doi: 10.1371/journal.pone.0008218. URL https://doi.org/10.1371/journal. pone.0008218.
- [16] L. Gwilliams, G. Flick, A. Marantz, L. Pylkkanen, D. Poeppel, and J.-R. King. Introducing MEG-MASC: A high-quality magneto-encephalography dataset for evaluating natural speech processing. Scientific Data, 10(1):862, 2023. doi: 10.1038/s41597-023-02752-5. URL https://www.nature.com/articles/s41597-023-02752-5.

- [17] D. Jayalath, G. Landau, and O. Parker Jones. Unlocking non-invasive brain-to-text. arXiv preprint arXiv:2505.13446, 2025.

- [18] D. Jayalath, G. Landau, B. Shillingford, M. Woolrich, and O. Parker Jones. The Brain’s Bitter Lesson: Scaling speech decoding with self-supervised learning. Forty-second International Conference on Machine Learning, ICML, 2025.

- [19] H. Jo, Y. Yang, J. Han, Y. Duan, H. Xiong, and W. H. Lee. Are EEG-to-text models working? arXiv preprint, 2024. URL https://arxiv.org/abs/2405.06459.

- [20] A. Krizhevsky. Learning multiple layers of features from tiny images. Technical Report TR-2009, University of Toronto, 2009.
- [21] K.-F. Lee and H.-W. Hon. Speaker-independent phone recognition using hidden markov models. IEEE Transactions on Acoustics, Speech, and Signal Processing, 37(11):1641–1648, 1989.

- [22] E. C. Leuthardt, C. Gaona, M. Sharma, N. Szrama, J. Roland, Z. Freudenberg, J. Solis, J. Breshears, and G. Schalk. Using the electrocorticographic speech network to control a braincomputer interface in humans. Journal of Neural Engineering, 8(3):036004, Jun 2011. doi: 10. 1088/1741-2560/8/3/036004. URL https://doi.org/10.1088/1741-2560/8/3/036004.

- [23] LibriVox Volunteers. Librivox: Free public domain audiobooks, 2024. https://librivox. org.
- [24] S. L. Metzger, K. T. Littlejohn, A. B. Silva, D. A. Moses, M. P. Seaton, R. Wang, M. E. Dougherty, J. R. Liu, P. Wu, M. A. Berger, I. Zhuravleva, A. Tu-Chan, K. Ganguly, G. K. Anumanchipalli, and E. F. Chang. A high-performance neuroprosthesis for speech decoding and avatar control. Nature, 620:1037–1046, 2023.

- [25] D. A. Moses, S. L. Metzger, J. R. Liu, G. K. Anumanchipalli, J. G. Makin, P. F. Sun, J. Chartier, M. E. Dougherty, P. M. Liu, G. M. Abrams, A. Tu-Chan, K. Ganguly, and E. F. Chang. Neuroprosthesis for decoding speech in a paralyzed person with anarthria. New England Journal of Medicine, 385(3):217–227, 2021. doi: 10.1056/NEJMoa2027540. URL https: //doi.org/10.1056/NEJMoa2027540.

- [26] M. S. Nieuwland et al. Large-scale replication study reveals a limit on probabilistic prediction in language comprehension. eLife, Apr. 2018.

- [27] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur. Librispeech: an ASR corpus based on public domain audio books. In 2015 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 5206–5210. IEEE, 2015.

- [28] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Köpf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala. PyTorch: An imperative style, high-performance deep learning library. In Advances in Neural Information Processing Systems 32, pages 8024–8035. Curran Associates, Inc., 2019.

- [29] X. Pei, D. L. Barbour, E. C. Leuthardt, and G. Schalk. Decoding vowels and consonants in spoken and imagined words using electrocorticographic signals in humans. Journal of Neural Engineering, 8:046028, 2011.

- [30] L. R. Rabiner and B.-H. Juang. Fundamentals of Speech Recognition. Prentice-Hall, 1993.

- [31] J. Ridge and O. Parker Jones. Resolving domain shift for representations of speech in noninvasive brain recordings. arXiv preprint, 2024. URL https://arxiv.org/abs/2410. 19986.

- [32] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang, A. Karpathy, A. Khosla, M. Bernstein, A. C. Berg, and L. Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. International Journal of Computer Vision, 115(3):211–252, 2015.

- [33] J.-M. Schoffelen et al. A 204-subject multimodal neuroimaging dataset to study language processing. Scientific Data, 6:1–13, Apr. 2019.

- [34] M. W. J. van Es, C. Gohil, A. J. Quinn, and M. W. Woolrich. osl-ephys: a python toolbox for the analysis of electrophysiology data. Frontiers in Neuroscience, 19:1522675, Feb. 2025. doi: 10.3389/fnins.2025.1522675.

- [35] F. R. Willett, E. M. Kunz, C. Fan, D. T. Avansino, G. H. Wilson, E. Y. Choi, F. Kamdar, M. F. Glasser, L. R. Hochberg, S. Druckmann, K. V. Shenoy, and J. M. Henderson. A high-performance speech neuroprosthesis. Nature, 620:1031–1036, 2023. doi: 10.1038/s41586-023-06377-x.

- [36] F. R. Willett, J. Li, T. Le, C. Fan, M. Chen, E. Shlizerman, Y. Chen, X. Zheng, T. S. Okubo, T. Benster, H. D. Lee, M. Kounga, E. K. Buchanan, D. Zoltowski, S. W. Linderman, and J. M. Henderson. Brain-to-Text Benchmark ’24: Lessons learned. arXiv preprint arXiv:2412.17227,

2024. URL https://doi.org/10.48550/arXiv.2412.17227.

- [37] G. H. Wilson, S. D. Stavisky, F. R. Willett, D. T. Avansino, J. N. Kelemen, L. R. Hochberg, J. M. Henderson, S. Druckmann, and K. V. Shenoy. Decoding spoken English from intracortical electrode arrays in dorsal precentral gyrus. Journal of Neural Engineering, 17(6):066007, 2020. doi: 10.1088/1741-2552/abbfef. URL https://doi.org/10.1088/1741-2552/abbfef.

- [38] W. Xiong, J. Droppo, X. Huang, F. Seide, M. Seltzer, A. Stolcke, D. Yu, and G. Zweig. Achieving human parity in conversational speech recognition. arXiv preprint arXiv:1610.05256, 2016. URL https://arxiv.org/abs/1610.05256.

- [39] Y. Yang, Y. Duan, H. Jo, Q. Zhang, R. Xu, O. Parker Jones, X. Hu, C.-T. Lin, and H. Xiong. NeuGPT: Unified multi-modal neural GPT. arXiv preprint, 2024. URL https://arxiv.org/ abs/2410.20916.

- [40] Y. Yang, Y. Duan, Q. Zhang, R. Xu, and H. Xiong. NeuSpeech: Decode neural signal as speech. arXiv preprint, 2024. URL https://arxiv.org/abs/2403.01748.

- [41] Y. Yang, H. Jo, Y. Duan, Q. Zhang, J. Zhou, W. H. Lee, R. Xu, and H. Xiong. MAD: Multialignment MEG-to-text decoding. arXiv preprint, 2024. URL https://arxiv.org/abs/ 2406.01512.

- [42] M. Özdogan, G. Landau, G. Elvers, D. Jayalath, P. Somaiya, F. Mantegna, M. Woolrich, and O. Parker Jones. LibriBrain: Over 50 hours of within-subject MEG to improve speech decoding methods at scale. arXiv preprint, 2025. URL https://arxiv.org/abs/2506.02098.

