# On the Quantification of SSVEP Frequency Responses in Human EEG in Realistic BCI Conditions

Rafał Kus´1*, Anna Duszyk2, Piotr Milanowski1, Maciej Łabe˛cki1, Maria Bierzyn´ska3, Zofia Radzikowska2, Magdalena Michalska1, Jarosław Z_ygierewicz1, Piotr Suffczyn´ski1, Piotr Jerzy Durka1

1 Faculty of Physics, University of Warsaw, Warsaw, Poland, 2 Department of Psychology, University of Social Sciences and Humanities, Warsaw, Poland, 3Department of Molecular and Cellular Neurobiology, Nencki Institute of Experimental Biology, Warsaw, Poland

|Abstract<br><br>This article concerns one of the most important problems of brain-computer interfaces (BCI) based on Steady State Visual Evoked Potentials (SSVEP), that is the selection of the a-priori most suitable frequencies for stimulation. Previous works related to this problem were done either with measuring systems that have little in common with actual BCI systems (e.g., single flashing LED) or were presented on a small number of subjects, or the tested frequency range did not cover a broad spectrum. Their results indicate a strong SSVEP response around 10 Hz, in the range 13–25 Hz, and at high frequencies in the band of 40–60 Hz. In the case of BCI interfaces, stimulation with frequencies from various ranges are used. The frequencies are often adapted for each user separately. The selection of these frequencies, however, was not yet justified in quantitative group-level study with proper statistical account for inter-subject variability. The aim of this study is to determine the SSVEP response curve, that is, the magnitude of the evoked signal as a function of frequency. The SSVEP response was induced in conditions as close as possible to the actual BCI system, using a wide range of frequencies (5– 30 Hz, in step of 1 Hz). The data were obtained for 10 subjects. SSVEP curves for individual subjects and the population curve was determined. Statistical analysis were conducted both on the level of individual subjects and for the group. The main result of the study is the identification of the optimal range of frequencies, which is 12–18 Hz, for the registration of SSVEP phenomena. The applied criterion of optimality was: to find the largest contiguous range of frequencies yielding the strong and constant-level SSVEP response.<br><br>Citation: Kus´ R, Duszyk A, Milanowski P, Łabe˛cki M, Bierzyn´ska M, et al. (2013) On the Quantification of SSVEP Frequency Responses in Human EEG in Realistic BCI Conditions. PLoS ONE 8(10): e77536. doi:10.1371/journal.pone.0077536<br><br>Editor: Gareth Robert Barnes, University College of London – Institute of Neurology, United Kingdom Received April 17, 2013; Accepted September 3, 2013; Published October 18, 2013 Copyright: 2013 Kus´ et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.<br><br>Funding: The work was partially supported by the Ventures Programme of Foundation for Polish Science operated within the Innovative Economy Operational Programme (IE OP) 2007–2013 within European Regional Development Fund. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. The additional part of the funding was from Polish funds for science.<br><br>Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: rkus@fuw.edu.pl|
|---|

Introduction

Brain responses to repetitive sensory stimulus have been studied for decades. For instance Regan [1] has observed that a rapidly repeating stimulus, such as a flickering light of certain frequency, may induce response in corresponding frequencies (that of stimulation and higher harmonics) in the EEG recorded over visual areas of the scalp. These brain responses have been named steady-state visual evoked potentials (SSVEP). This phenomenon is commonly used in Brain-Computer Interface (BCI) systems [2]. A graphical interface of the SSVEP-based BCI system usually consists of different commands, e.g. letters or symbols, that flicker at specific frequencies. User pays attention to a particular flickering command, while ignoring others, which induces SSVEP with the corresponding frequency. BCI system identifies the user intention by quantifying and classifying SSVEP. Proper choice of flicker frequencies and accurate estimation of the response magnitude are critical for BCI. Although it is generally acknowledged that the SSVEP response depends on the frequency of the stimulation, there are relatively few studies investigating this relation in detail. Regan [3] has shown that the dependence of the amplitude of SSVEP on the flicker frequency generally exhibits three distinct maxima. The ‘low-frequency’ response with a

maximum around 10 Hz, the ‘medium-frequency’ response in 13– 25 Hz range and ‘high-frequency’ response in 40–60 Hz range. Similar results have been subsequently obtained in other studies.

In [4], a representative dependence of SSVEP amplitude on frequency response of one subject exhibits three maxima centered on 15, 31 and 41 Hz. Pastor [5] investigated the EEG oscillatory responses to flicker stimulation for selected frequencies in the 5– 60 Hz range. The response amplitude was largest at 15 Hz in the occipital area and at 25 Hz in the frontal areas. Herrmann [6] investigated the EEG responses to flicker stimulation in the frequency range 1–100 Hz with 1 Hz resolution. His main finding was that the brain exhibits resonant frequencies around 10, 20, 40 and 80 Hz. The relative magnitudes of response frequencies were not the main objective of the study, hence the results do not pertain directly to BCI systems, e.g., the curve representing average response magnitude across 10 subjects was not smooth and exhibited several maxima and minima. The standard error of the mean was not provided hence it is not possible to assess statistical significance of the peaks.

Although the dependence of response magnitude on stimulation frequency has been investigated in several studies, and is commonly used to guide the selection of stimulation frequencies,

there is no consensus regarding the optimal frequencies for the SSVEP-based BCIs. This is reflected in very diversified frequencies adopted in various studies. Some authors used narrow ‘lowfrequency’ band, e.g. 6.666–8.571 Hz [7], 5–9.9 Hz [8], while others used medium frequency range, e.g. 14–18 Hz [9] or even higher frequencies e.g., 27–43 Hz [10]. The application of frequencies from the alpha band (8–13 Hz) is also not consistent across studies. While in some BCI applications, frequencies from the alpha band are excluded (e.g., 6, 7, 8 and 13 Hz [11]), they are included in some other studies (e.g. 6.67, 7.50, 8.57, 10.00, 12.00 Hz [12]). The widespread diversity of the stimulation frequencies across studies indicates that there is still a need to find out which frequencies may provide an optimal performance of the SSVEP-based BCI.

The goal of this study is to provide a link between fundamental research and its applications in designing knowledge-based BCI systems with maximum performance. For this purpose we investigate the SSVEP responses in the wide range of responsive stimulation frequencies, using a 4-class SSVEP-based BCI. To the best of our knowledge, this topic has not been investigated in detail previously, in the settings corresponding to real BCI application.

Materials and Methods Subjects and Data Collection

Ten subjects participated in this study. All right–handed, 5 males and 5 females, mean age: 28.7 years, range: 24–41. EEG was recorded by means of 19 Ag/Ag-Cl electrodes placed on the surface of the scalp according to the international 10–20 system. All the electrodes from this system, except Fp1 and Fp2, were used to further analysis. The ground electrode was placed over the clavicle of the subject and the reference electrodes were placed over the left and right mastoid (M1 and M2). The impedance of

[Figure 1]

Figure 2. Scheme of a single experimental trial. Resting period lasted 6 seconds, the stimulation epoch lasted 4 seconds. Two seconds before stimulation onset (at 0 s.), the subject was instructed by a voice command to which of the fields he or she should attend. The signals from 26 to 22 s. of the resting epoch and signal from 0 to 4 s. of the stimulation epoch were selected for further analysis as No Visual Stimulation Epochs and Visual Stimulation Epochs, respectively. doi:10.1371/journal.pone.0077536.g002

the electrodes was below 5 kV. The signal was acquired by Porti7 (TMSI) amplifier with sampling frequency 1024 Hz.

Visual stimulation

Subjects were seated on a comfortable chair, in a dim room. Visual stimulation was delivered using a custom made BCI stimulator [13], placed at 100 cm in front of the subject. It consisted of liquid crystal display (LCD) backlit by an array of LEDs. The LCD (19.5 by 35 cm) was divided into four square fields, 4.5 cm by 4.5 cm each in 2|2 arrangement, separated by 4 cm of blank space. The size of the single square field, observed from the distance of 100 cm, was &2.6 degrees of visual angle and the distance between the centers of two adjacent fields was &4.9 degrees. This geometry implies that that if the subject

[Figure 2]

Figure 1. Scheme of the experimental paradigm. In resting epochs the screen remains blank, whereas during stimulation each field flashes with the indicated frequency. The task of the subject is to focus attention on the field indicated by a voice command issued two seconds before the stimulation onset. Indicated field is marked red. doi:10.1371/journal.pone.0077536.g001

[Figure 3]

- Figure 3. Visualisation of the spatial filters and spatial patterns corresponding to the highest eigenvalue (eq. 2 and 3) .Four left columns – spatial filters, four right columns – spatial patterns at stimulation frequencies: 5 Hz, 11 Hz, 16 Hz, 21 Hz and 26 Hz. Each row presents results for one subject. Color code: red positive, blue negative values.

( )

- doi:10.1371/journal.pone.0077536.g003

focused on the center of the target field the target stimulus would be situated in foveal vision and the neighbouring ones would be localized in peripheral vision. Such localization of flickering fields should reduce the interference of neighbouring stimuli in the EEG signal [14–16] and the distraction of attention of the subject, yet it requires only relatively small eye movement to change the attended field. The luminance of stimuli emitted by single square field was 30 lx. Each LED highlighted a single field of the display. The LEDs were controlled by a micro-controller (MCU). The MCU drove the LEDs with square wave of stable frequency and duty cycle equal to 0.5. Each LED could flicker with a different frequency.

Experimental Paradigm

The schematic sequence of events is presented in Fig. 1. The experiment consisted of 4 s long stimulation periods interleaved by 6 s long resting periods. During the resting period the LCD panel was turned off. During the stimulation intervals, in order to create experimental conditions corresponding to SSVEP paradigm used in BCI systems, all four fields were simultaneously active, each flickering with different frequency. Two seconds before stimulation onset the subject was instructed by a voice command to which of the four fields he or she should attend. Thus we consider two experimental conditions: Visual Stimulation (VS) with given

frequency f and No Visual Stimulation (NVS) (Fig. 2). Further data analysis will consider mainly the VS condition. Both the position of the attended segment and its flickering frequency were randomly selected to avoid habituation. The subject was stimulated 50 times with each integer frequency between 5 and 30 Hz, i.e. 5, 6, 7,. 29, 30 Hz. Due to the length of the test, the experiment was divided into five sessions of 40 minutes. In each session the subject was stimulated with 10 repetitions of each frequency. For each subject, the full test was split into two meetings (two and three sessions, or vice versa). The length of the break between sessions during one day usually lasted about 15 minutes.

Ethics statement

The study was approved by the Research Ethics Committee at University of Social Sciences and Humanities in Warsaw, Poland. All subjects declared the absence of neurological or mental illnesses, and were screened against the photosensitive epilepsy by the standard clinical EEG test. Informed, written consent was obtained from all of the subjects.

Data analysis

There are two important issues concerning the assessment of the magnitude of the SSVEP response. The first comes from the fact

[Figure 4]

- Figure 4. SSVEP frequency response curves. Columns correspond to the method of SSVEP evaluation: Left – spectral power, right – Signal to Noise Ratio. Rows 1–10 correspond to individual subjects, last row shows the response averaged across 10 subjects. Horizontal axis – stimulation frequency. Vertical axes have two scales. In the left column: left scale – normalized power nPc(f ), right scale – absolute mean power Pcf . In the right column: left scale – values of nSNRcf , right scale – values of SNRcf . Error bars indicate the RMS error. Each plot presents two curves: the blue line shows values obtained for NVS, and the red one for VS condition. The gray regions in rows 1–10 mark the frequencies, where the given measure (column) gives significantly higher result for VS than NVS epochs for the a given subject (row) – results of within-subject level tests. The gray color on the plots in the last row means significant reactive frequencies for the population. Dotted vertical lines at 8 Hz and 13 Hz mark the range of the aband. Note: For S6 in left column the blue line exceeds the shown range to reach the value of nPNVSf ~2:6.

- doi:10.1371/journal.pone.0077536.g004

[Figure 5]

Figure 5. Test of magnitude of nSNR response for pairs of frequencies. White pixel indicate a pair of stimulation frequencies (one from horizontal, and one from vertical axis) which do not show significant differences in mean nSNR response, black pixel indicates that the difference is significant. Color squares indicate contiguous frequency ranges which pairwise have equal mean responses.

- doi:10.1371/journal.pone.0077536.g005

that the EEG signal contains both the activity related to visual stimuli and activity related to other processes. Second issue relates to the definition of the measure, which would quantify the SSVEP in an efficient way, relevant to the prospective application. Because of these issues, application of appropriate signal preprocessing and processing algorithms to extract the relevant activity is the central point of any SSVEP-based BCI. In the following sections we focus on techniques which are feasible in potential BCI application, that is those, that after a calibration session can be applied on-line.

Extraction of resting and stimulation epochs. From the EEG signal we extract segments of interest: 4 s long epochs of signal preceding the stimulation onset by 2 s, denoted as

xNVSf [Rk|N, and 4 s long epochs of signal during the stimulation with frequency f , denoted as xVSf [Rk|N, where Rk|N denotes a k|N real number matrix, k is the number of channels and N is the number of samples (Fig. 2).

Spatial Filtering. The recorded signal contains response to light stimulation and background EEG activity. To increase the ratio of the SSVEP magnitude to the magnitude of the background activity, we applied Common Spatial Pattern filter (CSP) [17–20]. This filter, in case of two multichannel time-series, yields a linear combination of the original channels such that the

variance of one of the resulting signals is maximized for one of the time-series and simultaneously it is minimized for the other timeseries. It is expected, that the most prominent changes in EEG signal, during the flickering stimulation, will be observed in the

frequency of stimulation. All data segments xVSf were band-pass filtered by means of 1-st order Chebyshev Type II filter with passband centered at frequencies of interest f . The width of the passband was 2 Hz (from f {1 Hz to f z1 Hz). The time series filtered around frequency f are denoted as yf .

The CSP transformation matrix Wf was estimated separately for each stimulation frequency f , since their spatial filters might not be identical. The matrix Wf can be obtained as a solution of the generalized eigenvalue problem [21]:

½Wf ,Lf ~eig(Rzf ,(Rzf zR{f )) ð1Þ

where: Rzf is the mean covariance matrix estimated by ensemble averaging of the single trial covariances matrices of yf – it describes the covariance structure of the signal of interest, and R{f is the mean covariance matrix estimated by ensemble averaging of the single trial covariances matrices of yf{1 and yfz1 – it describes the covariance structure of the background activity in adjacent

[Figure 6]

- Figure 6. Distribution of nSNR responses in selected frequency ranges. Each box-plot shows median (middle red line) together with its 95% confidence interval (notches). The lower and upper edge indicate 25th and 75th quantile, the whiskers show the span the data.

- doi:10.1371/journal.pone.0077536.g006

frequencies; Lf is a diagonal matrix of eigenvalues and Wf is a full matrix whose columns are corresponding eigenvectors so that

Rzf Wf ~(Rzf zR{f )Wf Lf . Next, the original signals xf were transformed by the estimated CSP filter:

sf ~Wf xf ð2Þ

The CSP filter, like other Blind Source Separation techniques, does not guarantee that the transformed signals sf contain the brain electrical activity separated into physiologically meaningful components. But, by the construction of the CSP filter, the channel corresponding to the highest eigenvalue in Lf , has the maximal variance for the z condition and lowest variance for the { condition. Further, the covariance matrices were estimated by ensemble averaging, thus the considerable contribution to Rzf and R{f will be derived from the EEG activity which has persistent covariance structure over the trials. That’s why we assume that channel corresponding to the highest eigenvalue in Lf , denoted as ~sf , will contain the activity related to SSVEP. The validation of this assumption will be presented in the Results section.

Spatial Patterns. It is very important to understand the relationship between the spatial filters, represented by each row of the matrix Wf and the corresponding spatial patterns. The CSP filter, in given output channel, produces a signal containing the activity uncorrelated to activity in other output channels. Assuming that this activity is generated by some sources, one can compute the projection of their activity on the scalp. From (2) one gets:

xf ~W{f 1sf ð3Þ

Each column of matrix W{f 1 gives the contribution of the corresponding source to the EEG signal and it is called spatial pattern of signal sf . It can be visualized as a plot showing its spatial distribution. The comparison of the obtained spatial filter and spatial patterns will be shown in the Results section.

Spectral power. The signals xcf , (c[fNVS,VSg) corresponding to given stimulation frequency f (both NVS and VS epochs) were first transformed by relevant CSP filter, then the spectral power estimates, Pc(f ), were computed for the channel ~scf , which corresponds to the highest eigenvalue in Lf . Pc(f ) is obtained by evaluating the spectral power at frequency f by means of periodogram with Tukey window with parameter equal to 0.1. For the convenience of between subject comparison the average spectra were normalized to the maximal value obtained for the VS condition for a given subject:

Pcf maxf[½5,30Hz PVSf ð4Þ

nPcf ~

where: Pcf is the Pc(f ) averaged over experiment realizations with given stimulation frequency f for a given subject.

Signal to Noise Ratio. Spectral power of EEG decreases with frequency. This property implies that response to highfrequency stimulation has less absolute power than response to low-frequency one. Therefore SSVEP can be better quantified as a relative increase of power at the stimulation frequency, with respect to its baseline value. The quantity, often used to measures the relative increase or decrease of the EEG power, is Event Related Spectral Perturbation [22]. However in context of on-line computations, relying on baseline values is not convenient. A more practical approach, especially applicable for SSVEP, was proposed in [23]. It measures the activity level at a given stimulation frequency (regarded as signal level) with respect to the level of activity in adjacent frequencies (regarded as noise level). Expressed as a ratio of corresponding powers this measure is an estimator of Signal-to-Noise-Ratio (SNR) for a given realization of experiment:

n:Pc(f ) Pi~n=2

SNRcf ~

i~1 ðPc(f zi:Df )zPc(f {i:Df )Þ

ð5Þ

we used: n=6, Df =0.25 Hz. This estimator of SNR was used as a feature for classification in BCI e.g. in [28]. In order to compare the average SNR between subjects we propose to normalize it for each subject by its maximal value:

SNRcf maxf[½5,30Hz SNRVSf

nSNRcf ~

ð6Þ

where: SNRcf is the SNRcf averaged over experiment realizations with given stimulation frequency f for a given subject.

Results Spatial Filters and Spatial Patterns

Examples of spatial filters and spatial patterns corresponding to the highest eigenvalue for each subject and for subset of stimulation frequencies is presented on the Fig. 3. One can observe, that the spatial patterns in most cases have clear dipolar form with extremum at the parietal and occipital electrodes, compatible with a hypothetical SSVEP source located in visual cortex. In most cases the pattern is symmetric, with extremum around electrodes O1 and O2 (e.g. subject S8), but in some cases it is asymmetric, with extremum either around the electrode O2 (e.g. subject S1 at frequency 21 Hz) or electrode O1 (e.g. subject S1 at frequency 11 Hz). Only five subjects (S8, S2, S7, S3, S9) have

almost constant spatial pattern across frequencies. For the rest of the subjects the spatial pattern varies with frequency.

The spatial patterns, although not constant, are generally consistent (up to sign) within and between subjects. But the spatial filters show much larger variability. This diversity results from different activity not related to SSVEP in different frequency bands (e.g. background EEG, muscle activity). The aim of the spatial filters is minimization of this additional activity in favor of SSVEP, thus the obtained spatial filters differ for the different stimulation frequencies.

SSVEP Frequency Response

Course of the response curve. SSVEP frequency responses obtained by means of normalized spectral power nPc(f ) are shown in the left column of Fig. 4 for all individual subjects (rows 1–10); the last row shows the responses averaged across subjects. The maxima of the response curve correspond to the presence of three frequency ranges of EEG rhythms: H (5–7.5 Hz), a (8–13 Hz) and b (above 14 Hz) [24]. For half of the subjects (S1, S2, S3, S4, S5 and S10) there is a pronounced peak in PVS(f ) centered in the a band. Only for some of them it corresponds exactly to the peak in PNVS(f ) (S2, S4 and S5). Two of the subjects have a broad peak in PVS(f ) extending from a to b band (S7, S8), and two of them have the peak shifted towards b range (S6, S9). In the average response curve, one can see that the highest values of PVS(f ) are obtained for the a range, but they have considerably higher root-meansquare (RMS) error than these in the b range.

The nSNR measure gives ratios of power at the stimulation frequency to the mean power at adjacent frequencies. This makes it less sensitive to the fact that with the increase of frequency the measured bioelectrical brain activity is more attenuated. As a result for most of the subjects we observe slower decrease of the SSVEP response with frequency, and in general the response curve is much more leveled (cf. Fig. 4 right vs left panel in each row). The response curve averaged over subjects (Fig. 4 bottom panel) reveals that there is a broad peak ranging from a to b band, with its peak located around 16 Hz. With respect to the average response measured by normalized spectral power the peak is shifted from a to b band.

Reactive frequencies. We performed two levels of statistical tests. The first level, within subjects, seeks an answer: at which of the stimulation frequencies the response evaluated by given measure (either Pc(f ) or SNRcf ) is higher for the VS than for the NVS epochs. For this test we applied one sided Wilcoxon test with False Discovery Rate (FDR) [25] correction for multiple comparison; the maximum FDR level (q-value) was set to 5%. From this level of analysis for each subject we obtain list of frequencies for which the null hypothesis was rejected. This are subject’s reactive frequencies.

The second level, between subjects, seeks an answer whether a given stimulation frequency is reactive in the population, i.e. can we reject the hypothesis that for the considered frequency the given measure yields higher result for the VS than for the NVS epochs in not more than half of the population. We treat the first level test results for given frequency across subjects as a Bernoulli process (with sequence of length equal to the number of subjects and number of successes equal to the number of subjects for whom the considered frequency is the reactive one). We compute the probability of obtaining such or more extreme sequence from Bernoulli distribution with parameter equal to 0.5 and correct it for multiple comparison with FDR (q-level~5%).

In Fig. 4 in rows 1–10, the significant – according to the withinsubject level tests – SSVEP responses are marked in gray. The

results show that normalized spectral power measure does not detect the significant SSVEP response only for subject S6 for stimulation frequencies within a band, and for subject S1 in the b band. The last row shows the mean responses averaged across subjects. In this panel, the gray bars indicate significant results of the second level statistical test. We see that for all tested frequencies the hypothesis that SSVEP reaction will be significant in not more than half of the population can be rejected. In this sense, we can state that all frequencies are reactive according to both spectral power and SNR measure.

Optimal frequencies

The next, more detailed question is which frequency range, on the population level, is optimal for SSVEP detection. The optimality criteria applied is that the response is the largest and similar for different frequencies within a contiguous range. To tackle this problem we performed a series of paired t-tests. Each

test compares nSNRVSf responses obtained for two different frequencies of stimulation for the group of subjects. The results shown in Fig. 5 were corrected for multiple comparisons by means of FDR (q~5%). In this plot white pixel indicates a pair of stimulation frequencies (one from horizontal, and one from vertical axis) which do not yield significant differences in mean nSNR response, black pixel indicates that the difference is significant. One can notice, that there are contiguous, partially overlapping, frequency ranges which pairwise have equal mean responses. We selected four ranges of stimulation frequencies which are large and contiguous, marked by color squares. The next step was to find out which of these contiguous frequency

range has the highest nSNRVSf to fulfill our optimality criterion. One way ANOVA reveals that the mean nSNRVSf in these ranges are not equal (F3,256 =33.6, p=2e–18). According to post-hoc test (Tukey HSD) we can state that at the significance level 5%(corrected) the mean nSNRVSf are different between each pair of the ranges (Fig. 6) except 8–14 Hz and 18–23 Hz. Thus the frequency bands can be ordered according to mean nSNR value in the following way: nSNRVS12{18wnSNRVS8{14~nSNRVS18{23w nSNRVS25{30:

Discussion Realistic design of the experiment

Paradigm. The experimental paradigms found in the SSVEP literature (e.g. [5,6]) were limited to the long term stimulation with randomly selected frequencies, separated by short breaks. Such conditions are not realistic in a BCI system. The typical mode of operation of a BCI system consists of periods, when the subject focuses attention on the flickering light, and periods when he or she observes the BCI feedback or results of the selected action. This is true for both synchronous and asynchronous BCI systems. In this respect, proposed paradigm composed of stimulation epochs (VS) interleaved with the resting periods (NVS) seems more appropriate.

Number of flickering fields. In spite of claiming to investigate the properties of the SSVEP with the aim of improving SSVEP-based BCI, most of the reported studies were based upon unrealistic paradigm where the measures of the SSVEP response concerned the EEG activity recorded during stimulation with only one flickering light source [3,5,6,26,27]. The main objective of the presented study is determination of the SSVEP frequency response in the experimental condition involving the possible interference of neighboring, relatively large, flickering fields. In contrast to the previous studies, results presented here were obtained with a real

BCI appliance [13]. In the presented paradigm each filed flickered with different, randomly selected frequency. Some of the attended frequencies have greater chance to occur together with the unattended frequencies having one of the harmonics equal to the attended one. For example one may consider attended stimulus 24 Hz which can be presented with the unattended stimuli 6, 8, 12 Hz which have a harmonic equal to 24 Hz in contrast to attended stimulus 23 Hz which has no unattended frequency with harmonics equal 23 Hz. A priori, it could be assumed that the frequencies which have many possibilities to be stimulated simultaneously with harmonically related neighbors would evoke different SSVEP response than those which have no such possibilities. But for the tested BCI appliance and methods of SSVEP evaluation, there is no visible interference from the not attended harmonically related frequencies. Careful inspection of Fig. 4 and 5 shows that frequencies which have higher chance to occur together with harmonically related frequencies don’t exhibit visibly stronger responses.

Measuring the SSVEP response

Derivation selection. The issue of an electrode montage optimal for SSVEP measurement was not unequivocally solved so far. In order to identify the electrode with the best SSVEP response, different techniques were used by different authors, e.g. averaging the signals from occipital leads (O1, Oz, O2) [5] or searching for the best bipolar combination of the occipital lead and some other electrode [4]. Following Molina [28] we propose to measure the SSVEP response in the channel of CSP filtered signals sf which corresponds to the greatest eigenvalue of Lf . This channel is characterized by maximal variance for the time-series of interest and minimal variance for the time-series regarded as noise. The spatial patterns obtained for such selected channel are in most cases compatible with a presumed dipole in the visual cortex.

We showed that the selected spatial patten vary with stimulation frequencies (only four subject out of ten had the stable spatial pattern, independent of the stimulation frequencies). But even for the cases when the spatial patterns are independent of the stimulation frequencies, the spatial filters may vary with frequency due to different spatial distribution of background EEG activity in different frequency bands. These results suggest that the separate spatial filters should be estimated at least for the stimulation frequency ranges corresponding to different EEG rhythms.

Quantification of SSVEP. The response due to a flickering stimulation is mixed with the ongoing EEG activity. Thus the prerequisite to quantify the response is to separate it from the background activity. Measures of SSVEP proposed in [3,5,6] use time-locked averaging technique to suppress the background EEG activity. This method, although widely used in evoked potential research, is not very useful in a BCI setup, since it requires a sizable number of realizations to be effective.

The general signal processing techniques involving the frequency and spatial filtering to improve the signal-to-noise ratio can be used in the pre-processing stage, but at the next stage it is essential to construct a measure which is sensitive and specific to the activity resulting from the stimulation. There are two general approaches to quantification of the SSVEP. The first one is to use the amplitude of the spectral peak at the stimulation frequency. This can be obtained by autoregressive modeling [6] or Fourier analysis [4,5]. The spectral amplitudes are then corrected for a typical EEG spectrum profile: e.g. by multiplying the results by the frequency [5]. The other one relies on constructing derived measures, e.g. the ratio of spectral power at the stimulation frequency to the average power in adjacent frequencies [4]. We

showed that the range of frequencies which evoke most pronounced response depends to some extent on the applied response measure. For the population, average normalized

spectral power measure nPVSf has maximum in the a band while the nSNRVSf has the maximum in the low-b band. This discrepancy comes from the fact that the nPVSf measure is affected by three factors: one is the activity induced by stimulation, the second is the attenuation of EEG amplitude with frequency, and the third one is the modulation of the background activity due to stimulation. The consequences of the second and third factors are reduced to great extent in case of the nSNRVSf measure.

Comparison of responses in different stimulating frequency

In this paper we investigated the responses to stimulation by light flickering with frequency in the 5–30 Hz range. The sensitivity of the brain to particular frequency as reflected by SSVEP frequency response curve was not uniform across frequencies and its exact shape depended on the method used to quantify the response, and on the subjects.

Our results are in agreement with other results reported in the literature, concerning SSVEP responses. Regan [3] has shown that the amplitudes of SSVEP exhibit resonant-like peaks in three frequency regions, with peak frequencies around 10 Hz, 20 Hz and 50 Hz. In our study only two first peaks are present as the range of frequencies investigated was limited to 5–30 Hz. It should be noted that these peaks are rather seen in individual subjects than in the group average. Pastor et al [5] has analyzed SSVEP responses to flicker stimulation in the 5–60 Hz range. They found that response reached a maximum at 15 Hz in occipital regions and at 25 Hz in frontal regions. The occipital maximum is in agreement with the one reported in our study, for nSNRf method. Analogous result was also presented for one subject in [4].

Herrmann [6] reported that the SSVEP responses exhibit resonance phenomena around 10, 20, 40 and 80 Hz. It has been shown in single subjects, by means of comparing responses to a given resonant frequency and two adjacent frequencies. Dominant responses at resonant frequencies were apparent in the power spectra and in their larger amplitude as compared to response amplitudes at both adjacent frequencies. In our study, the power spectra of the individual subjects don’t point to the resonance properties of the brain, described above.

Of the two quantification methods studied in this paper the SNR measure is more selective to the SSVEP phenomenon as explained above. Thus further statistical analysis were performed only for responses measured with SNR. All the studied stimulation frequencies evoked response, yielding SNRcf for VS epochs significantly higher than for NVS epochs. Using pair-wise tests we found contiguous, partially overlapping, frequency ranges with equal mean nSNR responses. The nSNR response, grouped in these ranges, have different group means. From the presented results it follows that the most effective frequencies evoking the largest SSVEP response belong to the frequency band of 12– 18 Hz.

Author Contributions

Conceived and designed the experiments: RK AD MŁ MM. Performed the experiments: AD MŁ MB ZR MM. Analyzed the data: RK PM MŁ JZ. Contributed reagents/materials/analysis tools: RK JZ PM. Wrote the paper: RK AD PM MŁ MB ZR MM JZ_ PS PD.

References

- 1. Regan D (1968) A high frequency mechanism which underlies visual evoked potentials. Electroencephalography and Clinical Neurophysiology 25(3): 231– 257.
- 2. Brunner C, Allison B, Altsta¨tter C, Neuper C (2012) A comparison of three brain-computer interfaces based on event-related desynchronization, steady state visual evoked potentials, or a hybrid approach using both signals. Journal of Neural Engineering 8(2): doi: 10.1088/1741-2560/8/2/025010.
- 3. Regan D (1975) Recent advances in electrical recording from the human brain. Nature 6(253): 401–407.
- 4. Wang Y, Wang R, Gao X, Gao S (2005) Brain-computer Interface based on the High-frequency Steady-state Visual Evoked Potential. In: First International Conference on Neural Interface and Control Proceedings.
- 5. Pastor M, Artieda J, Arbizu J, Valencia M, Masdeu J (2003) Human cerebral activation during steady-state visual-evoked responses. Journal of Neuroscience 23(37): 621–627.
- 6. Herrmann CS (2001) Human EEG responses to 1-100 Hz flicker: resonance phenomena in visual cortex and their potential correlation to cognitive phenomena. Experimental Brain Research 137(3–4): 346–353.
- 7. Cecotti H (2010) A Self-Paced and Calibration-Less SSVEP-Based BrainComputer Interface Speller. IEEE Transactions on Neural Systems and Rehabilitation Engineering 18(2): 127–133.
- 8. Hwang H, Jung Y, Choik H, Lee S, Im C (2012) Development of an SSVEPbased BCI spelling system adopting a QWERTY-style LED keyboard. Journal of Neuroscience Methods 208(1): 59–65.
- 9. Lopez-Gordo M, Prieto A, Pelayo F, C M (2011) Customized stimulation enhances performance of independent binary SSVEP-BCI. Clinical Neurophysiology 122(1): 128–133.
- 10. Lin Z, Zhang CMI, Wu W, Gao X (2007) Frequency Recognition Based on Canonical Correlation analysis for SSVEP-Based BCIs. IEEE Transactions on Biomedical Engineering 54: 1172–1176.
- 11. Muller-Putz G, Scherer R, Brauneis C, Pfurtscheller G (2005) Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components. Journal of Neural Engineering 2: 123–130.
- 12. Volosyak I (2011) SSVEP based Bremen BCI interface-boosting information transfer rates. Journal of Neural Engineering 8(3): 10.1088/1741-2560/8/3/ 036020.
- 13. Durka P, Kus R, Zygierewicz J, Michalska M, Milanowski P, et al. (2012) Usercentered design of brain-computer interfaces: OpenBCI.pl and BCI Appliance. Bulletin of the Polish Academy of Sciences, Technical Sciences 60(3): 427–431.
- 14. Fuchs S, Andersen S, Gruber T, Mu¨ller M (2008) Attentional bias of competitive interactions in neuronal networks of early visual processing in the human brain. Neuroimage 41(3): 1086–101.

- 15. Ng K, Bradley A, Cunnington R (2011) Effect of competing stimuli on SSVEPbased BCI. In: Engineering in Medicine and Biology Society, EMBC, 2011 Annual International Conference of the IEEE.
- 16. Ng K, Bradley A, Cunnington R (2012) Stimulus specificity of a steady-state visual-evoked potential-based brain-computer interface. Journal of Neural engineering 9(3): doi 036008.
- 17. Koles Z, Lazar S MSand Zhou (1990) Spatial patterns underlying population differences in the background EEG. Brain Topography 2(4): 275–284.
- 18. Koles Z (1991) The quantitative extraction and topographic mapping of the abnormal components in the clinical eeg. Electroencephalography and Clinical Neurophysiology 79: 440–447.
- 19. Koles Z, Lind J, Flor-Henry P (1994) Spatial patterns in the background EEG underlying mental disease in man. Electroencephalography and Clinical Neurophysiology 91: 319–328.
- 20. Koles Z, Lind J, Soong A (1995) Spatio-temporal decomposition of the EEG: a general approach to the isolation and localization of sources. Electroencephalography and Clinical Neurophysiology 95: 219–230.
- 21. Fukunaga K (1990) Introduction to Statistical Pattern Recognition. Academic Press; 2 edition.
- 22. Makeig S (1993) Auditory Event-Related Dynamics of the EEG Spectrum and Effects of Exposure to Tones. Electroencephalography and Clinical Neurophysiology 86: 283–293.
- 23. Wang Y, Wang R, Gao X, Hong B, Gao S (2006) A practical VEP-based braincomputer interface. IEEE Transactions on Neural Systems and Rehabilitation Engineering 2: 234–240.
- 24. Niedermeyer E, da Silva FL (2005) Electroencephalography: Basic Principles, Clinical Applications and Related Fields. Philadelphia: Lippincott Williams and Wilkins.
- 25. Benjamini Y, Yekutieli D (2001) The control of the False Discovery Rate Under Dependancy. Annals of Statistics 29: 1165–1188.
- 26. Bakardjian H, Tanaka T, Cichocki A (2009) Optimization of SSVEP brain responses with application to eight-command Brain-Computer Interface. Neuroscience Letters 469: 34–38.
- 27. Kaashoek I (2008) Automatic determination of the optimum stimulation frequencies in an SSVEP based BCI. Technical report, Koninklijke Philips Electronics N.V.
- 28. Molina GM, Zhu D, Abtahi S (2010) Phase detection in a visual-evokedpotential based brain computer interface. In: 18th European Signal Processing Conference (EUSIPCO-2010), Aalborg, Denmark, August 23–27.

