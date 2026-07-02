[Figure 1]

### J. Biomedical Science and Engineering, 2008, 1, 64-67 ScientificResearch

Publishing

# Pattern recognition of motor imagery EEG using wavelet transform Pattern recognition of motor imagery EEG using wavelet transform

### Bao-Guo Xu & Ai-Guo Song

School of Instrument Science and Engineering Southeast University, Nanjing 210096, China.

#### SciResCopyright2008©

ABSTRACT This paper presents a novel effective method for

feature extraction of motor imaginary. We combine Brain-computer interface (BCI) provides new the discrete wavelet transform (DWT) with communication and control channels that do autoregressive model (AR) to extract more useful not depend on the brain's normal output of information for non-stationary EEG signals. Applyperipheral nerves and muscles. In this paper, ing this method to analyze the Graz dataset for BCI we report on results of developing a single competition 2003, we achieved the classification trial online motor imagery feature extraction accuracy of 90.0%. method for BCI. The wavelet coefficients and autoregressive parameter model was used to 2. METHODOLOGY extract the features from the motor imagery 2.1. Experimental paradigm EEG and the linear discriminant analysis The data set was provided by department of medical based on mahalanobis distance was utilized informatics, institute for biomedical engineering, unito classify the pattern of left and right hand versity of technology Graz [5]. It was recorded from movement imagery. The performance was a normal subject (female, 25y) during a feedback sestested by the Graz dataset for BCI competition sion. The subject sat in a relaxing chair with armrests. 2003 and the satisfactory results are obtained The task was to control a feedback bar by means of with an error rate as low as 10.0%. imagery left or right hand movements. The order of

left and right cues was random.

shows the timing of the experiment. The first 2s was quite; at t=2s an acoustic stimulus indicated the beginning of the trial; the trigger channel (#4) went from low to high, and a cross “+” was dis-

Figure 1

Keywords Brain-computer interface (BCI); Motor imagery; Wavelet coefficients; Autoregressive model

1. INTRODUCTION played for 1s; then at t=3s, an arrow (left or right) Left and right hand movement imagery can modify was displayed as cue. At the same time the subject the neuronal activity in the primary sensorimotor was asked to move a bar into the direction of the cue. areas, leading to the changes of the mu rhythm and The feedback was based on AAR parameters of chanbeta rhythm. BCI requires effective online process- nel #1 (C3) and #3 (C4), the AAR parameters were ing method to classify these EEG signals in order to combined with a discriminant analysis into one outconstruct a system enabling severely physically dis- put parameter. abled patients to communication with their surround- The recording was made using a G.tec amplifier ings [1-4]. and a Ag/AgCl electrodes. Three bipolar EEG chan-

[Figure 2]

[Figure 3]

1 2 3

1 2 3

Time/s

FeeDback period With Cue

Trigger Beep

Figure1. Timing scheme. Figure 2. Electrode positions.

Published Online May 2008 in SciRes.http://www.srpublishing.org/journal/jbise JBiSE

nance. This led us to use wavelet decomposition to extract the differences between the two motor imagery tasks.

[Figure 4]

Channel C3 Channel C4

18 16 14 12

25

Left Imagery Right Imagery

Left Imagery Right Imagery

20

### 2.3. Procedure

The flow chart of processing single-trial motor imagery EEG is shown as in . First, the time window was used to filter the data in temporal domain in order to get the segment that contained the most obvious difference between the two motor imagery tasks. Then EEG signals were decomposed into the frequency sub-bands using DWT and a set for statistical features was extracted from the sub-bands to represent the distribution of wavelet coefficients according to the characteristics of motor imagery EEG signals. Also the sixth-order AR coefficients of segmentation EEG signals were estimated using Burg's algorithm. Next, the combination features of wavelet coef-

Spectram(db)

Spectram(db)

15

Figure 4

10

8 6 4 2

10

5

0

0

0 10 20 30

0 10 20 30

Frequency(HZ)

Frequency(HZ)

Figure 3. Average power spectrums on channel C3 and C4.

nels (anterior '+', posterior '-') were measured over ficients and the AR coefficients were used as an input C3, Cz and C4 [ ]. The EEG was sampled vector. Finally linear discriminant analysis (LDA) with 128Hz, it was filtered between 0.5 and 30Hz. based on mahalanobis distance was utilized to clasSimilar experiments are described in [6]. sify computed features into different categories that The experiment consists of 7 runs with 40 trials represent the left or right hand movement imagery. each. All runs were conducted on the same day with several minutes break durrng experiment. One half of the datasets are provided for training; others are for 2.4. Feature extraction using discrete wavelet evaluating the performance of the system. transforms

- Figure 2
- Figure 3
- Figure 4. Flow chart of the data processing.

Classic Fourier transform has succeeded in station2.2. Feature consideration ary signals processing. However, EEG signal con-

tains non-stationary or transitory characteristics. Central brain oscillations in the mu rhythm in the

Thus it is not suitable to directly apply Fourier transrange of 7-12Hz and beta above 13Hz bands are

form to such signals. The wavelet transform decomstrongly related to sensorimotor tasks. Sensory stim-

poses a signal into a set of functions obtained by ulation, motor behavior, mental imagery can change

shifting and dilating one single function called the functional connectivity cortex which results in an

mother wavelet [10 11]. Continuous wavelet transamplitude suppression or in an amplitude enhance-

form is given by

ment .This phenomenon was also called eventrelated desynchronization (ERD) and event-related synchronization (ERS) [7 8]. Left and right hand movement imagery is typically accompanied with ERD in the mu and beta rhythms and has the charac-

[Figure 5]

(1)

teristic of contralateral dominance. Where (t) is the mother wavelet, is the scale

[Figure 6]

[Figure 7]

The power spectrums on C3 and C4 of the training parameter and is the shift parameter. In principle set are shown in . It indicates that the power the CWT produced an infinite number of coefficients, spectrums mainly distribute in the range of 8-13Hz thus it provides a redundant representation of the sigand 19-24Hz.In addition, the power of mu and beta nal. rhythms evoked by right hand movement imagery is The DWT provides a highly efficient wavelet replower than that of left hand movement imagery for resentation that can be implemented with a simple channel C3, and it is contrary for channel C4 which is recursive filter scheme and the original signal reconconsistent with the principle of contralateral domi- struction can be obtained by an inverse filter. The pro-

[Figure 8]

[Figure 9]

Statistical features wavelet Coefficients

linear discriminant analysis

EEG temporal filter

Coefficients of autoregressive model

66 B.G. Xu et al./J. Biomedical Science and Engineering 1 (2008) 64-67

[Figure 10]

- Figure 5. Decomposition of DWT; h[n] is the high-pass filter; g[n] is the low-pass filter.

cedure of multi-resolution decomposition of a signal trum and too high tends to introduce spurious peaks. x[n] is schematically shown in . Here order six was used based on the suggestions [9].

Figure 5

The number of levels of decomposition is chosen Then the Burg's method was used to estimate the on the basis of the dominant frequency components AR coefficients. This method is more accurate and of the signal. According to the motor imagery EEG yields better resolution without the problem of specsignals itself, we chose the level of 4 and the wavelet tral 'leakage' as compared to other methods such as of Daubechies order 10.As a result, the EEG signal is Levison-Durbin as it uses the data points directly. In decomposed into the details D1-D3 and approxima- addition, the Burg's method can minimize both fortion A3. The ranges of different frequency band are ward and backward error. shown in . Next the AR coefficients were computed and we

Table 1

The extracted wavelet coefficients show the distri- got six coefficients for each channel, giving a total of bution of the motor imagery signal in time and fre- 12 AR coefficients features for each EEG segment for quency. It can be seen from the table that the compo- a motor imagery task. nent D3 decomposition is within the mu rhythm, D2 is within the beta rhythm. Statistics over the set of 2.6. Linear discriminant analysis (LDA) wavelet coefficients were computed so as to reduce LDA is one of the most effective linear classification the total dimension of the feature vectors. The statis- methods for brain-computer interface, and it requires tical features of each sub-band are as follows: fewer examples for obtaining a reliable classifier out-

- (1) Mean of the absolute values of the coefficients. put [12].
- (2) Standard deviation of the coefficients. As to the LDA method, assume that each data ele-
- (3) Average power of the wavelet coefficients. ment si has m features. Then, an element si is one These features represent the frequency distribu- point in a dimensional feature space. The number of

tion and the amount of changes in frequency distribu- examples is n , each example is assigned to one of two tion. Thus 12 statistical features of wavelet coeffi- classes C={0,1}; Then, S is a matrix of size n×m, and cients are obtained for two channels. C is a vector of size n.N0. And N1 are the number of

elements for class 0 and 1, respectively.

### 2.5. Feature extraction using autoregressive The mean c of each classc is the mean over all si model

[Figure 11]

with i being all elements with in class c . The total EEG signal can be considered as the output of a linear

mean of the data is

filter driven by a white noise. This filter, referred to as AR, is a linear combination of the previous output itself. A zero-mean, stationary autoregressive process of orderp is given by

[Figure 12]

(3)

[Figure 13]

Table 1. Frequencies correspond to different levels of deposition for daubechies order 10 wavelet with a sample rate 128HZ.

(2)

Where p is the model order, x(n) is the signal at the

Level

Frequency range (Hz) 32-64 16-32 8-16 0-8

Decomposed signal D1 D2 D3 A3

sampled point n, ap(i) is the AR coefficients and (n) is a zero-mean white noise. In application, the values

- 1
- 2
- 3 3

of the ap(i) have to be estimated from the finite samples of datax(1),x(2),x(3),…,x(N).

The first important things involved in using AR model is determining the optimal AR model order since too low a model order tends to smooth the spec-

Table 2 . Dirrerent wavelet used for extracting features.

tion and channel to outside world.

Recognition rate 90% 90% 89.29% 87.86%

Wavelet Daubechies order 10 Discrete Meyer Coiflets order 5 Rbio1.3

## ACKNOWLEDGEMENTS

The work was founded by the National Basic Research Program of China (973 Program) (No.2002CB321/02), Natural Science Foundation of China (No.60475034,No.60643007) and 863 High-Tech project (No.2006AA04Z246).

## REFERENCE

[1]J. Virts. The Third International Meeting on Brain-Computer The covariance matrix C of the data is the expecta- ral.InterfaceSyst. Rehabil. Eng.Technology: Making2006, 14:126-127.a Difference. IEEE Trans .Neu-

tion value for [2]T. M. Vaughan. Brain-computer Interface Technology: A Review of the Second International Meeting. IEEE Trans .Neural. Syst. Rehabil. Eng. 2003, 11:94-109.

[Figure 14]

[3]J. R. Wolpaw, N. Birbaumer, and W. Heetderks, et al. Brain-

computer Interface Technology: A Review of the First InternaThen, the weight vector w and the offset w0 are tional Meeting.IEEE Trans. Rehabil. Eng.2000, 8:164-173 .

- [4]J. R. Wolpaw, N. Birbaumer & D. J. McFarland, et al. Braincomputer interface for communication and control . Clinical Neurophysiology 2002 , 113:767-791.
- [5]B. Blankertz, K. R. Muller & G. Curio, et al. BCI Competition 2003-Progress and Perspectives in Detection and Discrimina-

[Figure 15]

- (5)
- (6)

(4)

- (7)

[Figure 16]

The weight vector w determines a separating 51:1044-1051.tion of EEG Single Trials. IEEE Trans. Rehabil. Eng. 2004, hyperplane in the m -dimensional feature space. The [6]A. Schlögl, C. Neuper & G. Pfurtscheller. Estimating the normal distance D(x) of any element x is mutual information of an EEG-based Brain-Computer-

Interface. Biomedizinische. Technik. 2002, 47:3-8.

[Figure 17]

[7]E. Houdayer, E. Labyt & J. Cassim, et al. Relationship between event-related beta synchronization and afferent inputs: analysis of finger movement and peripheral nerve stimulations. Clinical

If D(x) is larger than 0, x is assigned to class 1, Neurophysiology2006, 117:628-636.

while if D(x) is smaller than 0, x is assigned to class 0. [8]G. Pfurstcheller & F. H. Lopes da Silva. Event-related However, D(x)=0 indicates that all elements x are EEG/MEGciples. ClinicalsynchronizationNeurophysiologyand desynchronizaiton:1999, 110:1842-1857.basic prinpart of the separating hyperplane. [9]G. Pfurstcheller & C. Neuper. Motor imagery and Direct Brain-

Computer Communication. Proc. IEEE2001, 89:1123-1134.

- 3. EXPERIMENT RESULTS [10]A.extractionSubasi.andEEGa mixturesignal classificationof expert model.usingExpertwaveletSystemfeaturewith Here, we have had 6 statistical wavelet coefficients Application, in press. and 6 AR coefficients for each channel, giving a total [11]A. Subasi. Automatic recognition of alertness level from EEG of 24 features for a motor imagery task. These by using neural network and wavelet coefficients. Expert Sys-

parameters were selected as inputs of LDA classifier. [12]A.temSchlogl.with ApplicationA new linear2005,classification28:701-711. method for an EEGcompared the classification performances based brain-computer interface. unpublished.

among four different wavelets. The results show the Daubechies order 10 gave the best performance and the recognition rate is as high as 90.0%. Also the results indicate that method of combining DWT with AR model are capable of extracting more useful information from the simultaneously acquired motor imagery EEG. Furthermore, when the window of 384 samples with a shift of 1 sample was used, maximum classification accuracy of 92.1% is achieved.

- 4. CONCLUSION AND FUTURE WORK In this paper, a novel single-trial motor imagery EEG classification method is proposed. The pattern classification techniques as described in this work make possible the development of a fully automated motor imagery EEG signals analysis system which is accurate, simple and reliable enough to use in braincomputer interface. Future work will utilize the algorithms developed in this study to directly control the embedded rehabilitation robot so as to help the patient with severed paralysis to solve the problem of environment control and provide a new communica-

Table 2

