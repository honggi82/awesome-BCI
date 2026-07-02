# Simulating Brain Signals: Creating Synthetic EEG Data via Neural-Based Generative Models for Improved SSVEP Classiﬁcation

## arXiv:1901.07429v2[q-bio.QM]3Apr2019

Nik Khadijah Nik Aznan∗†, Amir Atapour-Abarghouei∗, Stephen Bonner∗, Jason D. Connolly‡ Noura Al Moubayed∗ and Toby P. Breckon∗† Department of {∗Computer Science, †Engineering, ‡ Psychology} Durham University, Durham, UK

Abstract—Despite signiﬁcant recent progress in the area of Brain-Computer Interface (BCI), there are numerous shortcomings associated with collecting Electroencephalography (EEG) signals in real-world environments. These include, but are not limited to, subject and session data variance, long and arduous calibration processes and predictive generalisation issues across different subjects or sessions. This implies that many downstream applications, including Steady State Visual Evoked Potential (SSVEP) based classiﬁcation systems, can suffer from a shortage of reliable data. Generating meaningful and realistic synthetic data can therefore be of signiﬁcant value in circumventing this problem. We explore the use of modern neural-based generative models trained on a limited quantity of EEG data collected from different subjects to generate supplementary synthetic EEG signal vectors, subsequently utilised to train an SSVEP classiﬁer. Extensive experimental analysis demonstrates the efﬁcacy of our generated data, leading to improvements across a variety of evaluations, with the crucial task of cross-subject generalisation improving by over 35% with the use of such synthetic data.

I. INTRODUCTION

Electroencephalography (EEG) is the most prominent signal acquisition approach employed for Brain-Computer Interface (BCI) as it has the non-invasive ability to capture electrical activity of the human cerebral cortex [1]. BCI is a system that translates such acquired signals to provide a communication and control medium between the human brain and external devices. BCI has received signiﬁcant attention within the research community for decades [2]. However, not many BCI applications are tractable for daily use in real-world scenarios, especially for important medical applications, such as assisting patients with locked-in syndrome. This is due to the numerous shortcomings and limitations within the current state of the art that lead to the low reliability and usability of BCI [3].

Deep neural networks have recently been used to improve the classiﬁcation of various aspects of EEG data [4]–[6]. While it is essential to have access to large quantities of data for training such methods, collecting high quality EEG data has proven difﬁcult [7], [8]. This can be for a variety of reasons including the requirement for careful per-subject and per-session calibration. This makes EEG BCI experiments time-consuming, expensive and difﬁcult to operate within the usually short amount of time experimental subjects can perform EEG experiments [9]. In addition to these issues,

[Figure 1]

Fig. 1: Details of the collection process for an SSVEP EEG dataset (Video-Stimuli) using a video based stimuli.

there are commonly-known limitations with EEG data in general, which can severely hinder the applicability of a system dependent on such data [7]. For instance, EEG data is known to be highly subject and session variant, which leads to a long calibration process for every individual experiment [2], [3]. This further impacts any machine learning based models which are trained upon this data, as they often demonstrate poor generalisation performance across different subjects or experiential data collecting sessions [3], [6].

In machine learning, generative models have long been used to generate entirely new and realistic data points which match the distribution of a given target dataset [10]. Recent work on neural-based models such as Generative Adversarial Networks (GAN) and Variational Auto-Encoders (VAE) have demonstrated that these are highly capable at capturing key elements from a diverse range of datasets to generate realistic samples [11]. Increasingly, there is evidence that using synthetic data, taken from a generative model, can be used as a form of data augmentation to help improve the performance of any downstream data classiﬁcation task [12].

In this paper, we detail the generation of new synthetic EEG data using a selection of customised neural-based generative models and explore applications of such data including using it to boost classiﬁcation accuracy on real datasets. Uniquely,

we speciﬁcally focus on dry-EEG data containing Steady State Visual Evoked Potential (SSVEP) signals. Dry-EEG requires no conductive gel which improves its usability within a BCI context, eliminating major limitations of the wet EEG systems [13]–[15]. However, dry-EEG results in high impedance values that cause more noise and artefacts in the data, leading to more challenging signal decoding and classiﬁcation [13].

SSVEP is a type of evoked potential stimuli generated by having repeated ﬂashes at certain frequencies presented to subjects (the ﬂashing can occur in a video as seen in Figure 1) [1]. The frequency of the ﬂashing is present in the EEG signals recorded from the subjects and can be extracted via a variety of competing signal processing techniques [16]. SSVEP has many important applications in BCI, for example it can be utilised to allow people with severe physical disabilities to control or communicate with external devices just by having them ﬁxate on a ﬂickering stimuli [17], controlling an exoskeleton [4] or navigating a humanoid robot [18]. To the best of our knowledge, this is the ﬁrst work in the literature to explore the use of neural-based generative models to create dry-EEG data containing SSVEP information. In summary, we make the following major contributions in this work:

- • The generation of synthetic dry-EEG data containing SSVEP signals using a variety of unsupervised models.
- • A demonstration that using generated data can improve the classiﬁcation of real-world EEG data, taken from multiple subjects and recorded under various conditions and sessions.
- • An exploration of both classiﬁer pre-training and dataset augmentation as use cases for the generated data.
- • Further demonstration that using synthetic EEG data can increase the convergence rate of classiﬁcation models, thus resulting in the observation that smaller quantities of real-world training data is required.

We perform extensive experiential evaluations to validate our claims and to aid reproducibility, we release our Pythonbased (PyTorch) implementation of all the generative models, along with sample input data1.

II. RELATED WORK

We consider the background information relevant to this work within two distinct areas:- recent advances made in generative models (Section II-A) and existing work on using such models to generate meaningful and coherent synthetic EEG data (Section II-B).

- A. Neural-Based Generative Models

Generative models have been proven very powerful within the context of unsupervised learning where the model learns a hidden structure of the data from its distribution to generate new data samples within the same distribution [19]. This generated dataset often contains enough variation to support the down-stream training of a secondary model [8].

1https://github.com/nikk-nikaznan/SSVEP-Neural-Generative-Models

Generative Adversarial Networks (GAN) [11] are capable of producing semantically sound artiﬁcial samples by inducing a competition between a generator (G), which attempts to capture the distribution, and a discriminator (D), which assesses the generator output and penalizes unrealistic samples. Both networks are trained simultaneously to achieve an equilibrium.

Training a GAN is known to be challenging with pervasive instability issues [20]. One such issue stems from the discriminator rapidly reaching optimality and effortlessly distinguishing between the fake samples output by the generator and samples from the real distribution. This will lead to a lack of meaningful gradients for training, effectively ceasing any progress towards the equilibrium.

The Wasserstein GAN (WGAN) is consequently proposed in [21] to rectify some of the issues associated with training a GAN. The Wasserstein-1 metric is used to measure the distance between the real and model distributions. Also known as the Earth Mover’s distance, (EM(p,q)), this metric is the minimum cost of moving distribution elements (earth mass) to transform a distribution q to distribution p (cost = mass × transport distance).

The Wasserstein GAN [21] has an aptly named critic (C) instead of a discriminator since this network is no longer a classiﬁer. Using the EM distance, the critic will not only determine whether a sample is fake or real as a discrete binary decision, but how real or how fake the generated sample is as a continuous regressive output. Under the right training circumstances, the critic will eventually converge to a linear function with ever-present meaningful gradients and cannot saturate. The loss function in the Wasserstein GAN is created via the Kantorovich-Rubinstein duality [21]:

[C(˜x)], (1)

[C(x)] − E

E

min

max

x∼Pr

x˜∼Pg

C∈F

G

where F is the set of 1-Lipschitz functions, Pr the real distribution, Pg the model distribution deﬁned by x˜ = G(z),z ∼ p(z), and z the random noise. If C is optimal, minimizing the value function with respect to G minimizes EM(Pr,Pg).

The Wasserstein GAN does not suffer from vanishing gradients or mode collapse. However, to guarantee continuity, a Lipschitz constraint must be enforced, which is achieved in [21] by clamping the weights. This results in the creation of a new hyper-parameter, which needs to be carefully tuned to the distribution.

A gradient norm penalty with respect to the critic input is consequently proposed in [22] to replace clamping. Since a differentiable function is 1-Lipschitz if and only if its gradient norm is no more than 1 everywhere, [22] limits the critic gradient norm by penalizing the function on the gradient norm for samples xˆ ∼ Pxˆ, where xˆ =  x + (1 − )˜x, 0 < < 1. This penalty term which is added to the function in Eqn. 1 is therefore as follows [22]:

[(|| x ˆC(ˆx)||2 − 1)2], (2)

### E

xˆ∼Pxˆ

where Pxˆ is implicitly deﬁned to sample uniformly along

straight lines between pairs of points sampled from the real data distribution, Pr, and Pg is the model distribution deﬁned by x˜ = G(z),z ∼ p(z) [22].

Auto-encoders have long been used as a method of creating a low-dimensional representation z of data using an encoder model, which can be used to reconstruct the original data with minimal errors via a decoder model [23]. However, traditionally they cannot be explicitly used to generate new data samples based on the learned data distribution. Variational Auto-encoders (VAE) utilise ideas from Bayesian inference to produce a more expressive data representation, whilst also having the ability to generate new data samples [24], [25]. Unlike non-probabilistic auto-encoders [23], a VAE does not learn a ﬁxed value for each element in z but instead each element is sampled from a probability distribution before being passed to the decoder model. This has been shown to produce a more semantically meaningful representation, where individual dimensions in the hidden space can correspond to tangible elements in the dataset, such as facial expression in a dataset of human faces [26].

As the decoder model of the VAE is trained to take a sample from a Gaussian distribution and produce a realistic output, it can be used to produced new data by simply sampling points in the distribution and reconstructing them.

- B. Literature Review

Within the existing body of work in the literature, there are instances of generative models used to create synthetic EEG data. For instance, [27] proposes using the improved WGAN with GP for a single channel of the EEG data for motor imagery task. The generator consists of one linear layer, six convolutional layers where each layer consists of an upsampling operation, two convolutions and one fully-connected layer. The authors evaluate the performance of four models, three different up-sampling methods (nearest-neighbour, linear interpolation and cubic interpolation with convolutional downsampling) and down-sampling via average pooling with the original WGAN-GP. All the models are then assessed using four evaluation metrics; inception score, Frechet inception distance, Euclidean distance and sliced Wasserstein distance. All four models are demonstrated to outperform WGAN-GP.

In [9], the authors propose deep EEG super-resolution using a GAN. The model is applied to a small number of EEG channel data to interpolate other channel signals using motor imagery dataset from [28]. The super-resolution data (SR) is generated via WGAN with convolutional ﬁlters using the lowresolution data (LR) from the dataset by down-sampling the EEG channels by scale factors of two and four for two different experiments. The channels removed from the down-sampling processes are used as high-resolution data (HR) to compete against SR in the discriminator. They evaluate the performance of the SR by performing classiﬁcation and comparing the accuracy with the classiﬁcation performed using HR. The authors conclude that SR is capable of producing high spatial resolution EEG signals from low resolution signals.

Instead of generating EEG signals, [29] generates previously seen images while having brain signals recorded by EEG. Six subjects are shown 2000 images with 40 classes per subject. The EEG signals are pre-processed by hardware notch ﬁlter between 49 and 51 Hz and bandpass ﬁlter between 14 and 70 Hz. Using LSTM RNN, the temporal feature representations are encoded, which are subsequently used as condition vectors employed along with random noise vectors to generate new images. They obtain a test accuracy of 83.9% when evaluating the LSTM model for feature representation.

- In [7], synthetic EEG signals are generated by inverting

the artiﬁcial time-frequency representation (TFR) obtained from conditional Deep Convolutional GAN (cDCGAN). The Wavelet Transform is used to obtain the TFR of the signals to be used by the cDCGAN to generate the artiﬁcial TFR of the EEG signals. The BCI competition II dataset III [30] is used as the EEG data. They evaluate the efﬁcacy of the synthetic data by comparing the classiﬁcation accuracy of the model trained on real data, synthetic data and a mixture of real and synthetic data with different ratios. Using additional synthetic data, the accuracy improved up to 3%.

- In [8] and [31], a GAN is used to generate synthetic

emotion recognition EEG data. The authors in [8] generate EEG in the form of differential entropy from noise distribution using a conditional WGAN with two emotion recognition datasets. They evaluate the performance of the generated data by combining the synthetic and real-world data to train a classiﬁcation model compared against a model solely trained on real-world data. The addition of the synthetic data leads to an improvement in the accuracy of up to 20% for different datasets.

The approach in [31] combines classiﬁcation and generative networks in a model using an Auxiliary Classiﬁer GAN (ACGAN). Part of the approach is encoding the data from SEED and DEAP datasets into images using a Markov Transition Field (MTF) before passing them into the AC-GAN to generate new data samples. Every sample comes with a corresponding class label. A Tiled CNN is employed to classify the MTF images to either fake or real and with the class label. They improved the classiﬁcation by less than 1% in the SEED dataset as compared with previous work.

In this paper, we generate synthetic EEG signals from SSVEP tasks using dry-EEG. While earlier work [7], [31] has been able to generate features within a secondary domain, from which EEG signals are subsequently reconstructed, we are the ﬁrst to introduce the concept of generating meaningful EEG data directly in signal space via end-to-end training instead of ﬁrst transforming the signals into different domains for SSVEP classiﬁcation. This improves overall efﬁciency, removes any need for additional signal processing, and prevents potential instability errors introduced during transformations.

III. PROPOSED APPROACH

As one of the objectives of this work is to create synthetic EEG data, which can be used to improve the training of a downstream classiﬁer [5], we explore the use of a variety of

neural-based generative models (as described in Section II). In this section, a brief description of the details of the models used in this work is provided.

- A. Deep Convolutional Generative Adversarial Network

As part of this work, we use the generative model proposed in [32]. Random noise vectors z are sampled from a Gaussian distribution and used as the generator input. At every iteration, the generator outputs fake data samples (x˜ = G(z)), which are then passed to the discriminator along with randomly selected real data samples x, classifying them as either fake or real, the gradients from which are employed to train the generator, leading to higher quality outputs at every step. An overview of our generative adversarial model is seen in Figure 2.

1) Loss Function: The loss function is based on the competition between the generator and the discriminator following the minimax objective [11]:

L = min

G

max

D

E

x∼Pr

[log(D(x))] + E

x˜∼Pg

[log(1 − D(˜x))], (3)

where Pr is the data distribution, Pg the model distribution deﬁned by x˜ = G(z),z ∼ p(z), and z the random noise vector used as the input to the generator. An overview of the training pipeline is seen in Figure 2.

Fig. 2: An overview of the generative adversarial network.

2) Implementation Details: The network architecture is based on that of [32], with the exception of the use of one dimensional convolutions since the networks process EEG signal vectors rather than images. Our generator consists of one dense layer and three 1D transpose convolutional layers.

This vector is then used as the input to our light-weight discriminator, consisting of two layers; the ﬁrst containing a convolution-BatchNorm-LeakyReLU(slope = 0.2) module followed by max pooling, and the second using a fullyconnected layer followed by a leaky ReLU (slope = 0.2).

Implementation and training is carried out in PyTorch [33], with Adam [34] used as the optimization approach (momentum β1 = 0.5, β2 = 0.999, initial learning rate α = 0.0001).

- B. Improved Wasserstein Generative Adversarial Network

Similarly to the training procedure in Section III-A, the Wasserstein GAN is made up of two completing networks, a generator and a critic. The generator receives a random noise vector z as its input, and the critic determines how real or fake the data samples created by the generator are by calculating the distance between the real data distribution and the model distribution (Earth Mover’s distance).

Since it is signiﬁcantly important to keep the critic optimal at all times, we train the critic 25 times per each generator training iteration for the ﬁrst 100 generator iterations and 5

times per each generator iteration for the rest of the training process.

1) Loss Function: Here, we take advantage of the improved Wasserstein GAN [22] with the following loss function:

E

[C(˜x)] − E

L = min

max

[C(x)]+ λ E

x˜∼Pg

x∼Pr

G

C

(4)

[(|| x ˆC(ˆx)||2 − 1)2],

xˆ∼Pxˆ

where Pg is the model distribution deﬁned by x˜ = G(z),z ∼

- p(z), z is random noise, Pr is the true data distribution, and Pxˆ is implicitly deﬁned to sample uniformly along straight lines between pairs of points sampled from Pr and Pg.

2) Implementation Details: For the sake of consistency, the architecture of the networks used here are similar to that of the networks in Section III-A. Similarly, all implementation and training is carried out in PyTorch [33], with Adam [34] used as the optimization approach (momentum β1 = 0.1, β2 = 0.999, initial learning rate α = 0.0001).

C. Variational Autoencoder

In addition to the GAN based approaches, we also explore the creation of a Convolutional Variational Auto-encoder (detailed in Section II-A) to generate synthetic EEG data. Our VAE model uses 1D convolutions to encode features from a given EEG data sample, which are used to parametrise a Gaussian distribution from which a latent and compressed representation of the input data is sampled. This latent representation is passed to the decoder section of the model which comprises transposed convolutions used to transform the latent representation back into the original EEG data.

| | |
|---|---|
| | |

Fig. 3: An overview of the Variational Auto-encoder.

Once we have trained the VAE model using the objective function detailed in the next section, we are able to use it to generate entirely new data samples, which could have plausibly come from the training data, but which is not conditional on any input to the model.

1) Loss Function: The encoder section of our VAE model is trained to learn two output vectors, µ and σ, which represent the mean and variance of the latent space from which z will be sampled, z = N(µ,σ). Using the sampled representation z, the decoder section of the VAE is trained to reconstruct the input data x. Consequently, our VAE is trained to infer the intractable distribution p(z|x), that being the likelihood of z given the data xˆ, using a stand-in tractable one q(z|x) in the following manner:

L = Eq(z|x) log(p(x|z)) − KL(q(z|x)||p(z)), (5) where KL is the Kullback-Leibler distance between p and q,

- q(z|x) is the output of the convolutional based encoder portion of our VAE and p(x|z) is the output from the decoder section.

We make use of a Gaussian prior as the distribution for p(z). Figure 8c shows the the general layout of our VAE model.

2) Implementation Details: We utilise a convolutional encoder for our VAE model and a transpose convolution based decoder. The encoder consists of a 1D convolution, with BatchNorm and leaky ReLU (slope = 0.2) as the activation function, followed by max pooling. This common learned feature representation is passed into two separate linear layers which learn the µ and σ used to parametrise the Gaussian and generate z. The decoder architecture comprises three stacked 1D transpose convolutional layers all using leaky ReLU (slope = 0.2) to perform the reconstruction from z to create xˆ.

As with the GAN models, all implementation and training is carried out in PyTorch [33], with Adam [34] used as the optimization algorithm (momentum β1 = 0.1, β2 = 0.999, initial learning rate α = 0.0001).

IV. EXPERIMENTAL SETUP

This section will detail the setup of our experimental evaluation, including introducing the empirical datasets used, detailing how we generate new data samples from our generative models and our procedure for evaluating the quality of the generated data.

A. Empirical SSVEP Dry-EEG Datasets

[Figure 2]

Fig. 4: Flowchart detailing the recording procedure for the Online and Ofﬂine SSVEP EEG Datasets. The highlighted region of the ﬁgure shows the humanoid robot used to create the Online dataset.

We make use of two empirical SSVEP dry-EEG datasets which we collected and fully detailed in our previous work [18]. The collection procedure for this dataset is detailed in Figure 4. This empirical data is used as a way of validating that the generated data is realistic enough to be used to improve the performance of a classiﬁcation model. In this dataset, objects are detected in a video sequence using a pre-trained object detection model [35]. The detected objects are then ﬂickered by rendering black/white polygon boxes on top of the objects with display frequency modulations of 10, 12 and 15 Hz to create the frequencies, common to both datasets, which we

attempt to detect via the SSVEP paradigm. Our two empirical datasets are detailed below:

- • Video-Stimuli Dataset: This dataset is collected from an ofﬂine experiment (shown in Figure 1) and is used as a basis for our generative models to learn the distribution of the SSVEP data. This dataset comprises 50 unique samples recorded for each of the three classes, taken from one subject (S01) performing the SSVEP task by looking at objects detected in a pre-recorded video sequence.
- • NAO Dataset: This dataset comprises data from an experiment containing both ofﬂine and online elements (highlighted in Figure 4). The ofﬂine portion of the data contains 50 unique samples for each of the three classes taken from three subjects (S01, S02, S03) performing the SSVEP task by looking at objects detected in a prerecorded video sequence from a humanoid robot. The online portion of the data contains 30 samples per class taken from the same three subjects when navigating the robot in real time [18].

[Figure 3]

Fig. 5: The CNN architecture used to classify the EEG signals.

- B. Synthetic Data Generation Procedure

Each of the generative models are trained upon data taken only from the Video-Stimuli dataset, detailed in Section IV-A. This will allow us to explore if data generated under one condition, can be used to improve the classiﬁcation of data recorded under another. Once training is complete, the models are used to generate entirely new and synthetic datasets, with one dataset being made for each model. A potentially unlimited amount of data could theoretically be generated from our models. For our experiments, we generate 500 unique samples, each three seconds in length, for each of the three SSVEP frequencies present in the original Video-Stimuli dataset.

- C. Classiﬁcation Procedure

In our experimental evaluation, we investigate exploiting the generated data to improve the classiﬁcation accuracy on the NAO dataset. To perform this classiﬁcation, we employ a model based on the SSVEP Convolutional Unit (SCU) Convolutional Neural Network (CNN) architecture [5] (Figure 5). Prior work has shown this model to outperform traditional approaches and even time-series speciﬁc models like Recurrent Neural Networks (RNN) when classifying SSVEP EEG data

16

The real data

The DCGAN data

14

The WGAN data

The VAE data

12

10

8

6

4

2

0

10 20 30 40 50 60 70 Frequency

(a) SSVEP Signal at 10Hz.

25

The real data

The DCGAN data

The WGAN data

20

The VAE data

15

10

5

0

10 20 30 40 50 60 70 Frequency

(b) SSVEP Signal at 12Hz.

30

The real data

The DCGAN data

The WGAN data

25

The VAE data

20

15

10

5

0

10 20 30 40 50 60 70 Frequency

(c) SSVEP Signal at 15Hz.

- Fig. 6: Comparing real and synthetic data from the generative models. Synthetic data clearly displays the characteristic SSVEP frequency peaks at the same frequencies as those observed in the real data.

[5]. The classiﬁcation model used for all experiments comprises of 1D convolutional layers, with batch normalization and max pooling. We ﬁrst pre-process the EEG channels by referencing the data, applying a bandpass ﬁlter between 9 to 60 Hz, a notch ﬁlter at 50 Hz and ﬁnally normalizing the data between 0 and 1.

training set from which the classiﬁer (see Section IV-C for details) is trained. Table I displays the results, with values given per and across all subjects, where the baseline is no synthetic data included in the training set. It is also interesting to note that no single generative models data source performs the best across all subjects.

V. RESULTS

Our experimental evaluation is designed to ﬁrstly assess if it is indeed possible to generate realistic EEG data containing SSVEP signals and secondly, if this synthetic data can be used in a variety of ways to improve the classiﬁcation accuracy on other real-world empirical datasets. All the classiﬁcation results presented are the mean results from ﬁve different random seeds in order to test robustness and each experiment uses identical train/test splits for all runs to allow for direct comparisons to be made.

- A. Data Visualization via Fast Fourier Transforms

SSVEP data has the phenomenon of frequency tagging, where the primary visual areas in human cortical oscillates to match the frequency of the ﬂuctuating sinusoidal cycle of the SSVEP stimuli presented to the subject [36]. EEG signals recorded during an SSVEP task will contain the target frequency clearly identiﬁable in the frequency domain [16].

To validate that our generative models are indeed producing viable SSVEP signals, we visualise both the real and synthetic data via the Fast Fourier Transform (FFT) to decompose the EEG signals into the frequency domain. Figure 6 displays the frequency plot of the new synthetic data generated from our DCGAN, WGAN and VAE compared against the empirical data. As can be seen, all models accurately capture the characteristic SSVEP peaks at the target frequency and associated harmonics [1], with the VAE producing signals with a comparatively lower amplitude. This result is very encouraging as it strongly suggests generative models can produce realistic SSVEP dry-EEG data.

- B. Mixed Real and Synthetic Data Classiﬁcation

To evaluate the applicability of synthetic EEG data being used to improve classiﬁcation results, we combine the synthetic (using 30 samples per class) and real data into a single

Method S01 S02 S03 Across Subjects

Baseline 0.91 ± 0.04 0.87 ± 0.10 0.84 ± 0.03 0.69 ± 0.03 DCGAN 0.86 ± 0.01 0.80 ± 0.04 0.89 ± 0.03 0.72 ± 0.03

WGAN 0.93 ± 0.04 0.90 ± 0.04 0.87 ± 0.02 0.71 ± 0.04 VAE 0.92 ± 0.03 0.90 ± 0.03 0.79 ± 0.03 0.67 ± 0.02

TABLE I: Classiﬁcation test accuracy using generated and real-world data used to train the classiﬁer. The baseline result is the classiﬁcation of only real data.

Having a single classiﬁcation model perform well across subjects is known to be highly challenging [17], yet possible [5]. Table I illustrates how the inclusion of synthetic data within the training set can positively inﬂuence generalisation capabilities across subjects, which is an important result and of signiﬁcant value in real-world applications. It is also interesting to note that although the synthetic data was generated from a different stimuli and sessions, its inclusion is still capable of improving the classiﬁcation accuracy.

C. Classiﬁcation with Pre-Training

To further explore the usefulness of the synthetic data, we pre-train our classiﬁer using only synthetic data (with 500 samples generated per class) and then further ﬁne-tune the model using the real data as in Figure 7a. The performance on the testing set is presented in Table II, where the baseline is no pre-training using synthetic data. Figure 9 highlights how the loss values for this task vary over training epochs. It can be seen that models pre-trained using the synthetic data converge faster and to a lower overall loss value.

Both Table II and Figure 9 demonstrate the ability to use the synthetic data to pre-train the network and improve the test accuracy on real data - another key result. This demonstrates the possibility of achieving higher classiﬁcation accuracy using a smaller training set of real-world data, which resolves one of the most important challenges associated with SSVEP signal classiﬁcation, unavailability of large datasets.

Method S01 S02 S03 Across Subjects

Baseline 0.91 ± 0.04 0.87 ± 0.10 0.84 ± 0.03 0.69 ± 0.03 DCGAN 0.97 ± 0.03 0.93 ± 0.03 0.87 ± 0.01 0.70 ± 0.02

WGAN 0.93 ± 0.03 0.90 ± 0.04 0.87 ± 0.03 0.72 ± 0.03 VAE 0.93 ± 0.03 0.92 ± 0.06 0.87 ± 0.05 0.73 ± 0.03

TABLE II: Accuracy for test classiﬁcation using synthetic data for pre-training stage. The baseline contains no pre-training.

Additional experiments were also conducted using varying quantities of synthetic data during pre-training. As seen in Figure 8, the models perform better on average when 500 synthetic data samples are used in the pre-training stage. This is primarily due to the subject and session variant nature of dry-EEG data, since the models can easily over-ﬁt to the distribution of the synthetic data in the presence of excessive pretraining. Furthermore, Figure 8d demonstrates how the training time can rapidly increase when the size of the synthetic pretraining dataset grows too large. Accordingly, the use of 500 synthetic data points empirically offers an optimal trade-off between improved performance and tractable training time in this instance.

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

(a) Pre-training classiﬁcation experiment.

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

(b) Training on data from different subjects.

- Fig. 7: Flowchart for experiment in section V-C (a) and experiment in section V-D (b).

D. Cross-Subject Generalisation

As mentioned in I, SSVEP classiﬁcation models often exhibit poor generalisation performance across different subjects or experiential data collecting sessions [3], [6]. In previous work [5], we successfully classiﬁed an unseen subject with no additional training required on that subject. In this section, we also attempt to demonstrate how pre-training on synthetic data can enhance the cross-subject generalisation capabilities of the model, i.e., the ability to classify data captured from one subject using a model trained on data captured from another. We train the generative models on S0X NAO Ofﬂine data (from the Nao Dataset), pre-train the classiﬁer using 500 samples of synthetic data output by said generative models, train the classiﬁer on data from a different subject (S0Y) and

- S01

- S02

| |
|---|

- S03 Across Subjects

0.95

0.95

| |
|---|

0.90

0.90

0.85

0.85

- S01

| |
|---|

- S02

| |
|---|

- S03 Across Subjects

Accuracy

Accuracy

0.80

0.80

| |
|---|

0.75

0.75

0.70

0.70

0.65

0.65

102 103 Number of Unique Synthetic Data Points used for Pre-training

102 103 Number of Unique Synthetic Data Points used for Pre-training

(a) DCGAN

(b) WGAN

800

0.90

ModelPre-trainingTime(s)

0.85

600

- S01

- S02

| |
|---|

- S03 Across Subjects

Accuracy

0.80

400

| |
|---|

0.75

200

0.70

0

0.65

102 103 Number of Unique Synthetic Data Points used for Pre-training

102 103 Number of Unique Synthetic Data Points used for Pre-training

(c) VAE

(d) Pre-training time

- Fig. 8: Test accuracy when varying the volume of synthetic data used for pre-training. Doted line indicates 500 samples.

0 20 40 60 80 100 Epochs

0.4

0.6

0.8

1.0

1.2

1.4

1.6

CrossEntropyLossValue

No pre-training

DCGAN data pre-training

WGAN data pre-training

VAE data pre-training

- Fig. 9: Convergence of the Cross-Entropy value plotted over training epochs for models with and without pre-training on synthetic data.

ﬁnally test on online data from S0X from the Nao Dataset (Figure 7b). As commonly seen within the literature [2], [17], one of the most important challenges in EEG-based research is the properties of EEG signals that vary from one subject to another as signal features can be speciﬁc to individual subjects.

Method S01 S02 S03 Mean

Baseline 0.35 0.54 0.42 0.45 ± 0.08 DCGAN 0.42 0.71 0.57 0.57 ± 0.12

WGAN 0.40 0.60 0.50 0.56 ± 0.13 VAE 0.70 0.90 0.85 0.82 ± 0.08

TABLE III: Classiﬁcation test accuracy for cross-subject Generalisation (see Figure 7b) via pre-training using synthetic data. The baseline does not include a pre-training stage.

Table III demonstrates how the baseline model performs poorly when trained using data collected from S0Y but tested on data from S0X, pointing to the lack of model Generalisability when EEG data is used. However, by pre-training the classiﬁer on the generated data using NAO ofﬂine data from S0X, we see a large improvement in classiﬁcation accuracy -

especially when data generated by the VAE is used. This is a signiﬁcant observation in the BCI research domain leading to a conjecture that, with further improvement in the results, we can eliminate the requirement for per-subject, per-session calibration for online applications.

VI. CONCLUSION

In this work, we exploit recent advances made in neuralbased generative models to explore potential beneﬁts they can offer within the context of SSVEP classiﬁcation models trained on EEG data. Since data acquisition within real-world scenarios suffers from a variety of challenges, using synthetically generated EEG signals can prove highly beneﬁcial in improving the accuracy, convergence rate and generalization capabilities of any model trained to classify EEG data. We generate synthetic EEG signals using three state-of-the-art generative models - a Generative Adversarial Network, a Wasserstein Generative Adversarial Network and a Variational Auto-Encoder. Extensive evaluations demonstrate the efﬁcacy of the synthetic data generated by said models across multiple experimental setups, with the inclusion of the generated data always improving the results.

Future work will investigate the the inﬂuence of the quantity of the synthetic data generated using different approaches used during pre-training on the classiﬁcation results can reveal valuable insight into the inner-workings of the classiﬁcation process and nature of the synthetic data. Furthermore, we also plan to assess if mixing generated data taken from several models for pre-training can also improve our results.

REFERENCES

- [1] R. P. Rao, Brain-Computer Interfacing: an Introduction. Cambridge University Press, 2013.
- [2] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A review of classiﬁcation algorithms for EEG-based brain–computer interfaces: a 10 year update,” J. Neural Engineering, vol. 15, no. 3, p. 031005, 2018.
- [3] F. Lotte, “Generating artiﬁcial EEG signals to reduce BCI calibration time,” in Int. Brain-Computer Interface Workshop, 2011, pp. 176–179.
- [4] N.-S. Kwak, K.-R. M¨uller, and S.-W. Lee, “A convolutional neural network for steady state visual evoked potential classiﬁcation under ambulatory environment,” PloS one, vol. 12, no. 2, p. e0172578, 2017.
- [5] N. K. N. Aznan, S. Bonner, J. D. Connolly, N. A. Moubayed, and T. P. Breckon, “On the classiﬁcation of SSVEP-based dry-EEG signals via convolutional neural networks,” in Int. Conf. Systems, Man, and Cybernetics. IEEE, 2018, pp. 3716–3721.
- [6] J. Thomas, T. Maszczyk, N. Sinha, T. Kluge, and J. Dauwels, “Deep learning-based classiﬁcation for brain-computer interfaces,” in Int. Conf. Systems, Man, and Cybernetics. IEEE, 2017, pp. 234–239.
- [7] Q. Zhang and Y. Liu, “Improving brain computer interface performance by data augmentation with conditional deep convolutional generative adversarial networks,” arXiv preprint arXiv:1806.07108, 2018.
- [8] Y. Luo, “EEG data augmentation for emotion recognition using a conditional wasserstein GAN,” in Int. Conf. Engineering in Medicine and Biology Society, 2018, pp. 2535–2538.
- [9] I. A. Corley and Y. Huang, “Deep eeg super-resolution: Upsampling EEG spatial resolution with generative adversarial networks,” in Int. Conf. Biomedical & Health Informatics. IEEE, 2018, pp. 100–103.
- [10] R. Salakhutdinov, “Learning deep generative models,” Annual Review of Statistics and Its Application, vol. 2, pp. 361–385, 2015.
- [11] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,” in Advances in Neural Information Processing Systems, 2014, pp. 2672– 2680.

- [12] M. Frid-Adar, I. Diamant, E. Klang, M. Amitai, J. Goldberger, and H. Greenspan, “GAN-based synthetic medical image augmentation for increased CNN performance in liver lesion classiﬁcation,” Neurocomputing, vol. 321, pp. 321–331, 2018.
- [13] G. Edlinger and C. Guger, “Can Dry EEG Sensors Improve the Usability of SMR, P300 and SSVEP Based BCIs?” in Towards Practical BrainComputer Interfaces, 2012, pp. 281–300.
- [14] M. A. Lopez-Gordo, D. Sanchez-Morillo, and F. Pelayo Valle, “Dry EEG electrodes,” Sensors, vol. 14, no. 7, pp. 12847–12870, 2014.
- [15] J. Minguillon, M. A. Lopez-Gordo, and F. Pelayo, “Trends in EEG-BCI for Daily-life: Requirements for Artifact Removal,” Biomedical Signal Processing and Control, vol. 31, pp. 407–418, 2017.
- [16] Q. Liu, K. Chen, Q. Ai, and S. Q. Xie, “Recent development of signal processing algorithms for SSVEP-based brain computer interfaces,” J. Medical and Biological Engineering, vol. 34, no. 4, pp. 299–309, 2014.
- [17] O. Dehzangi and M. Farooq, “Portable brain-computer interface for the intensive care unit patient communication using subject-dependent ssvep identiﬁcation,” BioMed research international, vol. 2018, 2018.
- [18] N. K. N. Aznan, J. D. Connolly, N. A. Moubayed, and T. P. Breckon, “Using variable natural environment brain-computer interface stimuli for real-time humanoid robot navigation,” in IEEE International Conference on Robotics and Automation. IEEE, 2019.
- [19] T. Jaakkola and D. Haussler, “Exploiting generative models in discriminative vlassiﬁers,” in Advances in Neural Information Processing Systems, 1999, pp. 487–493.
- [20] M. Arjovsky and L. Bottou, “Towards principles for training generative adversarial networks,” in Int. Conf. Learning Representations, 2017, pp. 1–17.
- [21] M. Arjovsky, S. Chintala, and L. Bottou, “Wasserstein generative adversarial networks,” in Int. Conf. Machine Learning, 2017, pp. 214–223.
- [22] I. Gulrajani, F. Ahmed, M. Arjovsky, V. Dumoulin, and A. C. Courville, “Improved training of wasserstein GANs,” in Advances in Neural Information Processing Systems, 2017, pp. 5769–5779.
- [23] G. E. Hinton and R. R. Salakhutdinov, “Reducing the dimensionality of data with neural networks,” Science, vol. 313, no. 5786, pp. 504–507, 2006.
- [24] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” arXiv preprint arXiv:1312.6114, 2013.
- [25] D. J. Rezende, S. Mohamed, and D. Wierstra, “Stochastic backpropagation and approximate inference in deep generative models,” in Int. Conf. Machine Learning, 2014, pp. 1278–1286.
- [26] A. B. L. Larsen, S. K. Sønderby, H. Larochelle, and O. Winther, “Autoencoding beyond pixels using a learned similarity metric,” in Int. Conf. Machine Learning, 2016, pp. 1558–1566.
- [27] K. G. Hartmann, R. T. Schirrmeister, and T. Ball, “EEG-GAN: Generative adversarial networks for electroencephalograhic (EEG) brain signals,” arXiv preprint arXiv:1806.01875, 2018.
- [28] J. R. Millan, “On the need for on-line learning in brain-computer interfaces,” in Int. Joint Conf. Neural Networks, 2004, pp. 2877–2882.
- [29] S. Palazzo, C. Spampinato, I. Kavasidis, D. Giordano, and M. Shah, “Generative adversarial networks conditioned by brain signals,” in Int. Conf. Computer Vision, 2017, pp. 3410–3418.
- [30] A. Schl¨ogl, “Outcome of the BCI-competition 2003 on the graz data set,” Berlin, Germany: Graz University of Technology, 2003.
- [31] J.-L. Qiu and W.-Y. Zhao, “Data encoding visualization based cognitive emotion recognition with AC-GAN applied for denoising,” in Int. Conf. Cognitive Informatics & Cognitive Computing, 2018, pp. 222–227.
- [32] A. Radford, L. Metz, and S. Chintala, “Unsupervised representation learning with deep convolutional generative adversarial networks,” arXiv preprint arXiv:1511.06434, 2015.
- [33] A. Paszke, S. Gross, S. Chintala, G. Chanan, Z. DeVito, Z. Lin, A. Desmaison, and A. Lerer, “Automatic differentiation in PyTorch,” in Advances in Neural Information Processing Systems, 2017, pp. 1–4.
- [34] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in Int. Conf. Learning Representations, 2014, pp. 1–15.
- [35] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu, and A. C. Berg, “SSD: Single shot multibox detector,” in Euro. Conf. Computer Vision, 2016, pp. 21–37.
- [36] S. K. Andersen and M. M. M¨uller, “Driving steady-state visual evoked potentials at arbitrary frequencies using temporal interpolation of stimulus presentation,” BMC Neuroscience, vol. 16, no. 1, p. 95, 2015.

