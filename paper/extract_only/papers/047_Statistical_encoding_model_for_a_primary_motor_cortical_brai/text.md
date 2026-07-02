## Statistical Encoding Model for a Primary Motor Cortical Brain-Machine Interface

Shy Shoham*, Member, IEEE, Liam M. Paninski, Matthew R. Fellows, Nicholas G. Hatsopoulos, John P. Donoghue, Member, IEEE, and Richard A. Normann, Member, IEEE

Abstract—A number of studies of the motor system suggest that the majority of primary motor cortical neurons represent simple movement-related kinematic and dynamic quantities in their timevarying activity patterns. An example of such an encoding relationship is the cosine tuning of ﬁring rate with respect to the direction of hand motion. We present a systematic development of statistical encoding models for movement-related motor neurons using multielectrode array recordings during a two-dimensional (2-D) continuous pursuit-tracking task. Our approach avoids massive averaging of responses by utilizing 2-D normalized occupancy plots, cascaded linear-nonlinear (LN) system models and a method for describing variability in discrete random systems. We found that the expected ﬁring rate of most movement-related motor neurons is related to the kinematic values by a linear transformation, with a signiﬁcant nonlinear distortion in about of the neurons. The measured variability of the neural responses is markedly nonPoisson in many neurons and is well captured by a “normalizedGaussian” statistical model that is deﬁned and introduced here. The statistical model is seamlessly integrated into a nearly-optimal recursive method for decoding movement from neural responses based on a Sequential Monte Carlo ﬁlter.

[Figure 1]

Index Terms—Discrete distribution, LN model, neural decoding, neuroprosthetics, sequential Monte-Carlo.

I. INTRODUCTION

# T

HE study of neurons in the primary motor cortex (area MI) and their role in the motor control system has strongly re-

lied on two complementary strategies, dictated by experimental constraints as well as diverging views regarding what information is represented by individual neurons. According to the ﬁrst approach [2], [3] an emphasis is placed on a mechanistic model of the motor control system, in which the contribution of individual neurons is aggregated and transformed to create the motor control signal. Implicit in this approach is the view that

Manuscript received June 2, 2004; revised December 5, 004. The work of S. Shoham was supported in part by a Lewis-Thomas fellowship. The work of J. P. Donoghue was supported by the National Institutes of Health (NIH) under Grant R01NS25074. The work of R. A. Normann was supported in part by the State of Utah Center of Excellence under Contract 95-3365. Asterisk indicates corresponding author.

*S. Shoham is with the Faculty of Biomedical Engineering, the Technion, Israel Institute of Technology, Haifa 32000, Israel (e-mail: sshoham@bm.technion.ac.il).

L. M. Paninski is with the Gatsby Computational Neuroscience Unit, London, WC1N 3AR, U.K.

- M. R. Fellows and J. P. Donoghue are with the Neuroscience Department,

Brown University, Providence, RI 02912 USA.

- N. G. Hatsopoulos is with the Department of Organizmal Biology and

Anatomy, University of Chicago, Chicago, IL 60637 USA.

R. A. Normann is with the Bioengineering Department, University of Utah, Salt Lake City, UT 84112 USA.

Digital Object Identiﬁer 10.1109/TBME.2005.847542

the relation between the activity of individual neurons and the motor output is rather complex, as dictated by the nonlinear, state dependent transformation that leads from motor cortical ﬁring to movement. According to the second approach, the activity of individual neurons can be viewed as representing simple kinematic and dynamic features of the planned or executed motor output. A prime example of this approach is the cosine-tuning curve relating the average ﬁring rate to the direction of movement [1]. The two views are not contradictory [4], [5] and may actually lead to similar models of the motor system. Rather, their main difference is in terms of the emphasis on different functional models “movement f (activity)” versus “activity f (movement).” The evolution of models of the second type “activity f (movement)” in the context of the motor system, is partly a result of experimental constraints that limited the range and nature of movements that could be effectively experimentally controlled or measured. These models, which are closely related to models of sensory and cognitive representation processes, are called encoding models. A complete encoding model of single neurons would capture the way in which the instantaneous ﬁring rate is modulated by the kinematic movement variables, as well as the variability (or noisiness) of this ﬁring [6]–[8]. A more general model will also include interneuronal interactions. Decoding strategies (e.g., the population vector [9] or other methods [10]–[12]) as well as mechanistic models [13] complement encoding models by attempting to explain how the motor system pools together the single-cell cortical activity into a movement representation.

[Figure 2]

[Figure 3]

[Figure 4]

In this paper, we develop an encoding model for individual MI neurons using continuous simultaneous recordings of hand position (in two dimensions) and neural activity during tracking of a randomly moving target. In this experimental scenario, a number of kinematic quantities that may be related to expected ﬁring rate (e.g., position, velocity, and acceleration) are controlled so that they are well sampled within the workspace, approximately stationary over trial time, and are minimally interdependent.However,the time-varyingand random, nonrepeated nature of the task makes the encoding relationship challenging to measure, as no averaging across different trials of the same type is possible. In order to characterize the encoding using this dataset, we ﬁrst introduce nonparametric analyses that allow us to explore the effect of kinematic variables (two at a time) on the expected ﬁring rate. Having demonstrated that the two-dimensional (2-D)projectionsof the encoding relationshipare roughly linear, we use a linear-nonlinear cascade system representation (Wiener cascade) that effectively represents the combined effect of all the kinematic variables. Using the model for expected ﬁring rate we then study the associated neural variability using

0018-9294/$20.00 © 2005 IEEE

novel “neural noise” plots, comparing Poisson and an alternative, “normalized-Gaussian” distribution that we develop.

Our study of encoding in the primary motor system is motivated by an attempt to develop effective decoding algorithms for converting spike trains recorded from multiple motor neurons into the motor control signal that they represent—an essential component in an implantable brain-machine interface [14], [15]. Such algorithms may improve the applicability of these devices, possibly overcoming the hardware constraints in the current generation of implantable microelectrode arrays which limit the number of practically available units to several dozens. Optimal decoding approaches, which can be viewed as optimal estimation solutions, ultimately rely on a statistical encoding model [6], like the one developed here. To demonstrate the utility of our encoding model, we implement a recursive Bayesian ﬁlter that is optimally tailored to it using the recently developed method of Sequential Monte Carlo ﬁlters [16]–[18]. An earlier version of this work has previously appeared in S. Shoham’s Ph.D. dissertation [17].

II. EXPERIMENTAL METHODS A. Recording Setup

Two macaque monkeys (M. mulatta) were operantly conditioned to perform a visually guided manual tracking task (described below). While performing this behavior extracellular signals were recorded with a chronically implanted microelectrode array [19] (Cyberkinetics, Foxborough, MA). The array was implanted in the arm region of the monkeys’ precentral gyrus (primary motor cortex), following a training period lasting several months. The surgical implantation procedures are described elsewhere [20]. The array consists of one hundred 1.0-mm-long silicon electrodes with platinized tips (200–500 k impedances measured with a 1 kHz, 100 nA sine wave) arranged in a rectangular 10 10 grid (0.4-mm spacing). The electrode tips were approximately located in layers III and V. Additional details of the surgical and animal care procedures appear elsewhere [21]. A number of long-term studies have established the chronic recording capability of this electrode-array [22], [23], and an ongoing research effort is underway to establish its efﬁcacy in an implantable brain-machine interface [14], [24]. The procedures were approved by Brown University’s Animals Care and Use Committee.

[Figure 5]

[Figure 6]

The neural signals were bandpass ﬁltered (250–7500 Hz, 5th order Butterworth), ampliﬁed (5000x), digitized (30 kHz sampling), and acquired on a Pentium based PC using a 100-channel data acquisition system [25] (Bionic Technologies LLC., Salt Lake City, UT). Thresholds were manually set, and thresholdcrossing events were saved to disk (1.6-ms duration). Multiunit data was sorted off-line using a new automatic and noise-robust spike-sorting algorithm [26].

In addition to the neural signals, the and position of a twolinkmanipulandumwere digitizedbyadigitizingtablet(Wacom Technology Corp., Vancouver, WA) at 167 Hz with an accuracy of 0.25 mm (range: 10 10 cm) and saved to disk. These measurements were interpolated to a 1-ms resolution using a smoothing cubic spline (Spline Toolbox, Mathworks, Natick MA). The smoothing spline was also used to analytically calculate the derivatives, in order to avoid large discretization-related

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

Fig. 1. General data characteristics. Data shown from one session where 23 well-isolated units were recoded during 172 tracks that exceeded 4 s. (a) Movement traces during three successive 8-s-long tracks. Dots represent snapshots once every 50 ms. Tracks are marked by different shades of gray. (b) Raster plot of unit activity during a successful track. (c) Smoothed distribution of movement velocities during the entire recording session. (d) Smoothed velocity histogram conditioned on spikes occurring in unit #7 (with time shift of 125 ms). (a) Hand position traces, (b) spike rasters, (c) velocity distribution, (d) conditional velocity distribution.

artifacts, and the smoothing parameter was chosen manually to produce smooth derivatives with only negligible smoothing of the position time-series.

### B. Behavioral Task

The monkeys were operantly conditioned to use a low-friction manipulandum to track a target moving on a computer screen in order to receive juice rewards. The target movement was generated by low-pass ﬁltering a pseudo-random Gaussian-distributed sequence, yielding a time series with a spectral cutoff set at 0.4–0.5 Hz [10-dB drop from maximal power, see also Fig. 11(c) and (d)]. A small black cursor on the screen indicated the manipulandum location, and the monkey’s task was to keep it within the boundaries of the smoothly moving red target circle (1.5-cm radius) for a duration of 8–10 s. Only trials where the monkey acquired the target within a limited time window (1.5 s for one of the monkeys and 4 s for the second) and did not lose it for the entire track duration were considered successful and led to a reward. However, we analyzed data from all trials where the tracking duration exceeded 4 s, including unsuccessful ones.

Additional details of this experiment and additional characteristics of the results are reported in [27]. Due to the experimental design, the correlations between the time series of pairs of different kinematic variables (i.e., hand position in and , hand velocities and accelerations) were very small

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

. Fig. 1 illustrates the basic features of the experimental data.

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

Nomenclature: In the following discussion and derivations we will use to denote the “state” of the arm at time . In general, the “state” of the arm can include a large number of

[Figure 32]

[Figure 33]

[Figure 34]

kinematic or dynamic variables, however, as we only measured the manipulandum position (in two dimensions), will refer to the position and its derivatives (velocity, acceleration ). The number of spikes neuron ﬁred in the time bin that followed time is denoted . We will denote by the instantaneous ﬁring rate (also known as the stochastic intensity [28]):

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

in the limit . In calculating the nonparametric encoding plots we were interested in the conditional probabilities of single spikes, which led us to choose very short time bins ms. All the subsequent analyses are based on spike counts, and a 50-ms time bin was chosen to allow for decoding algorithms with sufﬁcient temporal resolution for smooth movement tracking but simple enough to allow for a real-time implementation. A typical average ﬁring rate for the cortical neurons we study is Hz (generally Hz), and more than 99% of the time bins contained 0–4 spikes. Braces indicate an average value.

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

III. EXPERIMENTAL METHODS

In order to understand the general encoding relationship, a model-free method for visualizing how the probability of ﬁring depends on kinematic parameters is required. Previous characterizations of motor encoding (e.g., [1], [29], and [30]) relied heavily on neural responses integrated across extended timewindows or averaged across a large number of similar trials to achieve continuous “tuning curves.” In the context of hippocampal place cells, a simple application of Bayes’ rule was used to describe encoding (or ‘normalized occupancy’) relationships in two dimensions [31]. The basic formula

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

(1)

can be directly used to explore , the probability of ﬁring a spike given that the kinematic parameters seconds later are . Given an experimental data trace, placing a point on a discrete grid of the kinematic values every time the neuron spiked provides an approximation of the density

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Fig. 1(d)]. Placing points on the same grid at every time point (irrespective of whether the cell ﬁred an action potential or not) approximates the density [Fig. 1(c)]. Dividing these histograms yields an approximate representation of the encoding relationship .

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

Plots were created for the position, velocity, and acceleration (two dimensions in each case). In making the plots we tried to focus on regions with a sufﬁcient amount of data, and chose boundaries that included the 1st to 99th percentiles of the state space in each dimension, dividing them into 50 bins. The unnormalized plots were smoothed with a Gaussian kernel ( bins, full width at bins) and regions where the value of the smoothed unnormalized occupancy histogram [Fig. 1(d)] fell below 1, were rejected. The time delay

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

[Figure 213]

[Figure 214]

was set at 125 ms. A previous study described the activity of the vast majority of MI neurons as preceding movement by

[Figure 215]

[Figure 216]

Fig. 2. Velocity-conditional ﬁring rate expressed using nonparametric plots. Contour lines appear at regular intervals. Parallel lines indicate a planar structure.

0–250 ms [29] (roughly uniform distribution), which led to the selection of this number (see also [32] for a similar result). No attempt was made to ﬁnd individual-neuron delays, however, we veriﬁed these results were fairly insensitive to small changes in

(of order 50 ms).

[Figure 217]

Nonparametric plots for the encoding of position, velocity, and acceleration in two representative units are shown in Figs. 2 and 3. For the purpose of illustration we selected the two units with the highest signal-to-noise ratio from one recording session. Apart from some high-frequency distortion near the edges, the encoding plots appear as monotonic, distorted planes (note that contour lines for a plane are parallel and equidistant). Comparing the dynamical range on the different plots in Fig. 3 demonstrates that unit 1 (left panels) encodes velocity strongly (ﬁring rate modulated between 10–35 Hz, a range twice as wide as for other variables), whereas unit 2 (right panels) encodes primarily position (ﬁring rate modulated between 7–20 Hz, a range twice as wide as for other variables). However, in neither case is the encoding exclusively for velocity or position. The plots appear planar with respect to the velocity in unit 1 and position in unit 2 (see [27] for a quantitative analysis of the linearity in the nonparametric plots).

These results point to one of the weaknesses of this technique, when the combined contribution to the ﬁring rate of all of the different kinematic variables needs to be evaluated. If the relationships were perfectly linear, we would expect the combined contribution to have this form

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

(2)

However, how to pool together the encoding functions from several nonlinear 2-D plots is not as straightforward. Moreover, relying on a single time delay may distort the plots, particularly in the acceleration plots (acceleration being the most rapidly changing signal) [33]. In order to account for nonlinearities in the encoding of multiple parameters, as well as effects occurring at multiple temporal delays, we turn from the fully nonparametric models introduced in this section to a

[Figure 259]

[Figure 260]

Fig. 3. Nonparametric encoding plots of different kinematic variables. The color scale is in spikes/s units. The left and right panels are for different units [left is the same unit as in Figs. 1(d) and 2]. (a) Position encoding. (b) Velocity encoding. (c) Acceleration encoding. Equidistant contour lines are super-posed. (d) nonparametric encoding plots calculated without any smoothing (compare left panel with b-left and right panel with a-right). Lines indicate a planar structure.

nonlinear generalization of the general linear encoding model [which generalizes (2)].

IV. LN ENCODING MODELS

Models comprised of a cascade of a linear ﬁlter followed by a general static nonlinearity , also known as LNor Wiener-cascade models, have been explored by a number of studies (e.g., [34]–[36]), and form a natural extension to linear system models. These models appear well suited for describing the properties of neurons in the early visual system. In the case of the motor system, since ﬁring tends to precede movement, encoding relationships are usually anti-causal, and can take the form

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

(3)

In order to obtain and from our data, we used a simple two-step method similar to the one described in [36]. In the ﬁrst step standard linear regression of the position (x and y) time series versus the neural response time series is used to determine (the regression coefﬁcients). Given

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

it is straightforward to obtain a linear prediction time

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

Fig. 4. Illustration of binning method used for estimating LN models from discrete neural data (simulated data). Top: The linear expectation time series

is broken into bins according to the linear prediction value (2 shaded bins illustrated). Center:The spikecounts time seriesis segmented accordingly (solid and dashed arrows point to time points corresponding to the two bins). Bottom:

[Figure 345]

[Figure 346]

is evaluated from the relationship between linear prediction and mean ﬁring rate in the corresponding time points. The dashed and solid arrows are pointing at two points that correspond to each of the two bins.

[Figure 347]

series using a convolution operation, and can now be used as a basis for evaluating the nonlinearity . This is done using a simple binning approach: the time axis is broken into subsets where falls into different bins

[Figure 348]

[Figure 349]

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

. This nonparametric aggregation of ‘related’ time bins from different parts of the time axis is illustrated in the upper two panels of Fig. 4. The relationship of and the mean number of spikes in the corresponding subset of time bins approximately corresponds to the nonlinearity , as is illustrated in the bottom panel of Fig. 4

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

. To obtain a parametric model of the data we ﬁt the empirical relationship with a polynomial. The ﬁtting procedure outlined will provide an accurate description of the encoding relationship when: 1) has an elliptically symmetric distribution [36], and 2) the neural response has a one-dimensional dependence on . Both conditions are satisﬁed to a good approximation in our data [37]. Determination of an LN system model for unit 1 is illustrated in Fig. 5. The length l of the linear kernel is not known a priori, nor is the optimal polynomial order. Both parameters affect the model complexity, and an optimal choice has to provide a good ﬁt to the data without being overly complex. Penalizing the data loglikelihood using Schwarz’s Bayesian Information Criterion (BIC) [38] provides a systematic approach to model selection

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

#

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

# (4)

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

Fig. 5. Results of LN model ﬁtting with neural data. Results are for same unit as in Figs. 1–3. (a) Penalized loglikelihood determination of kernel length. (b) Penalized loglikelihood determination of polynomial order. (c) Static nonlinearity , and 4th order polynomial ﬁt. (d) Performance of LN model in predicting the ﬁring rate (concatenation of several trials). The spike counts and prediction were smoothed with a hamming window of width 1 s.

where we calculate using the statistical models introduced later. An optimal choice is one where the penalized likelihood is maximal: in Fig. 5(a) (for each of the and dimensions). This implies that the encoding relationship for this unit is predominantly a function of position, velocity, acceleration, and jerk. The inferred nonlinearity for this unit

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

- [Fig. 5(b)] is a polynomial of order 4 (note that the penalized loglikelihood is nearly ﬂat in the range 2–4). The model is able to describe expected rate modulations in the range 12–45 Hz
- [Fig. 5(c)]. The collection of units in this study had modulations in the range 0–60 Hz (equivalent to a maximal expectation of 3 spikes/bin). Directly scrutinizing the nonlinearity reveals that it can be mostly described by a piecewise-linear combination of two parts. The power of the inferred LN model in predicting the time-varying ﬁring rate of one such cell can be qualitatively demonstrated by comparing low-pass ﬁltered versions of the prediction to a smoothed version of the binned spike counts
- [Fig. 5(d)]. The prediction is clearly able to track some of the signiﬁcant excursions of the ﬁring rate, but generally does not span its full dynamical range (since not all the factors that modulate ﬁring are captured by our measurements and model). The correlation coefﬁcient between the two time series was 0.64; 40% of the units recorded in this study had a correlation coefﬁcient larger than 0.5 (maximal cc: 0.78, mean: 0.4).

Determination of the optimal polynomial orders allows us to break the neural units into three categories: nonlinear

, linear and unresponsive . Representative units in these categories are presented in Fig. 6. The unresponsive units generally had low average ﬁring rates (0–15 Hz). In the two monkeys from which we recorded (one dataset analyzed from each monkey), unresponsive units accounted for 17% and 7%, respectively

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

[Figure 529]

[Figure 530]

[Figure 531]

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

[Figure 540]

[Figure 541]

[Figure 542]

[Figure 543]

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

[Figure 548]

[Figure 549]

[Figure 550]

Fig. 6. Calculated static nonlinearity in six representative units. The Expected rate has units of spikes/s. A 3rd order polynomial ﬁt line is also shown for each unit. (a)–(c) Nonlinear functions. (d), (e) Linear encoding functions. (f) Unresponsive unit—no signiﬁcant encoding of kinematic variables.

( and ), linear units accounted for 52% and 59%, respectively ( and ), with nonlinear units accounting for the rest % and 34%, respectively.

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

[Figure 560]

[Figure 561]

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

[Figure 566]

[Figure 567]

[Figure 568]

The optimal linear kernel length for the different units in our data fell in the range 1–6, implying that the encoding we observe is typically a mixture of various kinematic variables. Therefore, the encoding relationship must be viewed as more general than the cosine tuning curve [1], or the model proposed more recently by Moran and Schwartz [29] in which the ﬁring rate is seen to be a function exclusively of the direction of motion and its speed. Instead, it is more consistent with the complex dependence on multiple movement parameters revealed by multiple regression analysis [32], [39]. To further illustrate this point, we note that a subset of the cells we analyzed actually coded for position more strongly than for velocity (e.g., unit 2 in Fig. 3) and that for such units the predictive power of our new model was much stronger than that of the velocity tuned models (Fig. 7). Correctly accounting for these units is of particular importance when attempting to decode arm position.

V. NEURAL NOISE PLOTS

Modeling the “expected ﬁring rate” does not provide a complete description of the neural ﬁring process and describing the variability of the neuron ﬁring is also necessary in our framework for likelihood calculations. A favored approach to this problem is to assume an inhomogeneous Poisson model with rate [6], [31]. This provides a relatively simple statistical model, however, in some neural systems the Poisson model is clearly inappropriate (e.g., [40]), and a previous study has indicated a signiﬁcantly smaller-than-Poisson variability in MI unit activity [12]. While some of the units we recorded here had Poisson ﬁring statistics, a signiﬁcant proportion did not. The variance versus mean behavior of two representative units is illustrated in Fig. 8(a), and it can be seen that while unit 1 is reasonably well described as Poisson, unit 2 is clearly not.

[Figure 569]

[Figure 570]

[Figure 571]

[Figure 572]

[Figure 573]

[Figure 574]

[Figure 575]

[Figure 576]

[Figure 577]

[Figure 578]

[Figure 579]

[Figure 580]

[Figure 581]

One principled way of characterizing non-Poisson statistics in spike trains is the method of time rescaling [7], [8], where

[Figure 582]

Fig. 7. Failure of velocity based models to predict ﬁring rate in a strongly position encoding unit. The plot compares the low-pass ﬁltered ﬁring of a neural unit with the ﬁltered predictions of three models (several trials concatenated). The cosine tuning model predicts the ﬁring rate solely as a function of the direction of motion, while the Moran model uses velocity and speed as input. Parameters for both models were obtained using a maximum-likelihood procedure. The LN model kernel had a length of 2 (in both and ) and, therefore, represents a function of position and velocity. A hamming window of 1.5 s was used to ﬁlter the time traces. The correlation coefﬁcients when comparing the real and predicted traces are 0.32, 0.28, and 0.79, respectively.

the expected ﬁring rate is used to rescale the time axis, and subsequently can lead to a non-Poisson, history dependent statistical model of the ﬁring. However, as this work is focused on using spike counts in intermediate-size bins (50 ms), an alternative method was developed for describing the statistics of the discrete random spike-counts as a function of the expected ﬁring rate. The method [see Fig. 8(b)] is conceptually similar to the adaptive binning method used above to calculate the nonlinearity in the LN cascade model. Here, the expected ﬁring rate time-series (3) is calculated, and used to segment the set of time bins into subsets where falls into different bins

[Figure 583]

[Figure 584]

[Figure 585]

[Figure 586]

[Figure 587]

[Figure 588]

[Figure 589]

[Figure 590]

[Figure 591]

. For each subset we ﬁnd the probabilities for the different values of the number of spikes

[Figure 592]

[Figure 593]

[Figure 594]

[Figure 595]

[Figure 596]

[Figure 597]

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

[Figure 604]

[Figure 605]

[Figure 606]

[Figure 607]

[Figure 608]

[Figure 609]

[Figure 610]

[Figure 611]

[Figure 612]

and plot , etc. versus the expected value

[Figure 613]

[Figure 614]

[Figure 615]

[Figure 616]

[Figure 617]

[Figure 618]

[Figure 619]

[Figure 620]

[Figure 621]

[Figure 622]

[Figure 623]

[Figure 624]

[Figure 625]

[Figure 626]

[Figure 627]

[Figure 628]

[Figure 629]

[Figure 630]

[Figure 631]

. The neural noise plot in Fig. 8(c) illustrates that the Poisson model adequately describes the empirical count distributions for unit 1

[Figure 632]

[Figure 633]

[Figure 634]

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

[Figure 639]

[Figure 640]

[Figure 641]

[Figure 642]

[Figure 643]

[Figure 644]

[Figure 645]

[Figure 646]

[Figure 647]

[Figure 648]

[Figure 649]

(5)

In contrast, unit 2 does not ﬁt the Poisson model [Fig. 8(d)]. The discrepancy primarily manifests as “clustering”: higher than expected probability for 1 and 2 spikes, while the probability of 0 and 3 spikes is lower than expected. This clustering leads to the smaller-than-Poisson conditional variance in Fig. 8(a).

VI. THE NORMALIZED-GAUSSIAN DISCRETE DISTRIBUTION

The Poisson model fails to describe the empirical spiking statistics in a large proportion of the units we recorded. Several studies (e.g., [7]) replaced the Poisson model using nonexponential models for the inter-spike interval such as the gamma distribution. However, processes with such ISI distributions lead to nonanalytical forms for the distributions of discrete spike

[Figure 650]

Fig. 8. Statistical properties and noise analysis of motor unit data. (a) Spike count variance versus mean in two representative units. Each point corresponds to one percentile of the time bins, broken according to the prediction of the LN model. (b) Constructing a neural noise plot(simulation data). (top panel) The LN-expected ﬁring rate time series is binned—two bins are illustrated. (center panel) The spike counts time series is segmented accordingly. The proportion of bins having speciﬁc number of spikes is evaluated. (bottom panel) The neural noise plot illustrates the conditional probabilities of the different discrete outcomes. Each of the bins contributed one point to each of the discrete probability curves. The lines correspond to a Poisson distribution. (c) Neural noise distribution for Unit 1, compared with a Poisson model. (d) Comparison with Poisson model for Unit 2. (e) Comparison with the Normalized Gaussian model for Unit 2.

counts, and we were unable to ﬁnd a major discrete distribution [41] that was able to capture the statistics of our empirical distributions. Motivated by the observed decoupling of the variance and the mean [e.g., Fig. 8(a)] as well as the shape of the empirical distributions we observed in the neural noise plots [Fig. 8(c)], we set to adapt the normal distribution

[Figure 651]

[Figure 652]

[Figure 653]

[Figure 654]

[Figure 655]

[Figure 656]

[Figure 657]

[Figure 658]

[Figure 659]

[Figure 660]

[Figure 661]

[Figure 662]

[Figure 663]

[Figure 664]

[Figure 665]

[Figure 666]

[Figure 667]

[Figure 668]

[Figure 669]

[Figure 670]

[Figure 671]

[Figure 672]

[Figure 673]

[Figure 674]

[Figure 675]

[Figure 676]

[Figure 677]

[Figure 678]

[Figure 679]

[Figure 680]

[Figure 681]

[Figure 682]

(6)

to the case where takes only discrete positive values. One way to do this is to treat the parameter in (6) as a free parameter, chosen to normalize the probabilities. However, the resulting distribution will no longer have a mean , which will limit its usefulness. Instead, we look for a form that satisﬁes simultaneously the following two constraints:

[Figure 683]

[Figure 684]

[Figure 685]

[Figure 686]

[Figure 687]

[Figure 688]

[Figure 689]

[Figure 690]

[Figure 691]

[Figure 692]

[Figure 693]

[Figure 694]

[Figure 695]

[Figure 696]

[Figure 697]

[Figure 698]

[Figure 699]

[Figure 700]

[Figure 701]

[Figure 702]

[Figure 703]

[Figure 704]

[Figure 705]

[Figure 706]

[Figure 707]

[Figure 708]

[Figure 709]

[Figure 710]

[Figure 711]

[Figure 712]

[Figure 713]

[Figure 714]

[Figure 715]

[Figure 716]

[Figure 717]

[Figure 718]

[Figure 719]

[Figure 720]

[Figure 721]

[Figure 722]

- (7)

[Figure 723]

[Figure 724]

[Figure 725]

[Figure 726]

[Figure 727]

[Figure 728]

[Figure 729]

[Figure 730]

[Figure 731]

[Figure 732]

[Figure 733]

[Figure 734]

[Figure 735]

[Figure 736]

[Figure 737]

[Figure 738]

[Figure 739]

[Figure 740]

[Figure 741]

[Figure 742]

[Figure 743]

[Figure 744]

[Figure 745]

[Figure 746]

[Figure 747]

[Figure 748]

[Figure 749]

[Figure 750]

[Figure 751]

[Figure 752]

[Figure 753]

[Figure 754]

[Figure 755]

[Figure 756]

[Figure 757]

- (8)

[Figure 758]

Fig. 9. The Poisson and Normalized Gaussian discrete distributions. The Normalized Gaussian distribution shown here (solid lines) has a parameter

. The Normalized Gaussian distribution behaves like a Gaussian with standard deviation at large values of . For small values of it approaches the Poisson distribution (symbols) near (binomial range). The inset compares the behavior of the variance as a function of the mean for the two distributions.

Both constraints cannot in general be satisﬁed using a single free parameter. A different normalization that is able to simultaneously satisfy these constraints (using two auxiliary variables:

and ) has the following form:

[Figure 759]

[Figure 760]

[Figure 761]

[Figure 762]

[Figure 763]

[Figure 764]

[Figure 765]

[Figure 766]

[Figure 767]

[Figure 768]

[Figure 769]

[Figure 770]

[Figure 771]

[Figure 772]

[Figure 773]

[Figure 774]

[Figure 775]

[Figure 776]

[Figure 777]

[Figure 778]

[Figure 779]

[Figure 780]

[Figure 781]

[Figure 782]

[Figure 783]

[Figure 784]

[Figure 785]

[Figure 786]

[Figure 787]

[Figure 788]

[Figure 789]

[Figure 790]

[Figure 791]

[Figure 792]

[Figure 793]

[Figure 794]

[Figure 795]

[Figure 796]

[Figure 797]

[Figure 798]

[Figure 799]

[Figure 800]

[Figure 801]

[Figure 802]

[Figure 803]

[Figure 804]

[Figure 805]

[Figure 806]

[Figure 807]

[Figure 808]

[Figure 809]

[Figure 810]

[Figure 811]

[Figure 812]

[Figure 813]

[Figure 814]

[Figure 815]

[Figure 816]

[Figure 817]

[Figure 818]

[Figure 819]

(9)

[Figure 820]

[Figure 821]

[Figure 822]

[Figure 823]

[Figure 824]

[Figure 825]

[Figure 826]

[Figure 827]

[Figure 828]

[Figure 829]

[Figure 830]

[Figure 831]

[Figure 832]

[Figure 833]

[Figure 834]

[Figure 835]

[Figure 836]

[Figure 837]

[Figure 838]

[Figure 839]

[Figure 840]

[Figure 841]

[Figure 842]

[Figure 843]

[Figure 844]

[Figure 845]

[Figure 846]

[Figure 847]

[Figure 848]

[Figure 849]

[Figure 850]

.

The normalizing auxiliary variables: (zero probability) and (the rest), can be numerically evaluated from the two constraint [(7) and (8)] for a given value of and the parameters and . The simplest way to evaluate these variables is ﬁrst to evaluate from (8), and then substitute it in (7) to obtain . We call the resulting distribution the Normalized-Gaussian discrete distribution. Fig. 9 illustrates the Normalized-Gaussian probability of different values of over a range of different ’s, and compares it with the Poisson distribution in the same range. We note that the Normalized-Gaussian distribution behaves like a Gaussian distribution at large values of and (for small values of ) approaches a Poisson distribution near . The plot insert demonstrates that while in a Poisson-distributed random variable the variance is equal to the mean, a Normalized-Gaussian variable has the property of saturating variance, and for large means the variance is essentially independent of the mean. Adjusting the value of the dispersion parameter results in a different width of the individual bell curves (not shown). In our application is ﬁt numerically by minimizing the sum-squared distortion between the observed and calculated distribution in the neural noise plots.

[Figure 851]

[Figure 852]

[Figure 853]

[Figure 854]

[Figure 855]

[Figure 856]

[Figure 857]

[Figure 858]

[Figure 859]

[Figure 860]

[Figure 861]

[Figure 862]

[Figure 863]

[Figure 864]

[Figure 865]

[Figure 866]

[Figure 867]

[Figure 868]

[Figure 869]

[Figure 870]

[Figure 871]

[Figure 872]

[Figure 873]

[Figure 874]

The satisfactory ﬁt that the Normalized-Gaussian distribution provides to our data is illustrated in Fig. 8(e), which shows neural noise plots for a unit for which the Poisson model fails. In fact, we found that the new noise model works well for units with all three types of behaviors we noted in the previous section

[Figure 875]

Fig. 10. Variance versus expected ﬁring for all recorded units. Each point represents the variance versus the highest expected ﬁring rate (in spikes/bin) for each unit. The N. Gaussian lines (dashed) are for (lower line) and

. The solid line is for the Poisson distribution .

(and Fig. 6). Fig. 10 presents a composite view of the variance versus mean behavior of all the 50 units we studied here. About one half of the units lie signiﬁcantly below the identity line, and were well ﬁt by N. Gaussian models with (the N. Gaussian lines in Fig. 10 show the bounds of this parameter range). The N. Gaussian distribution converges at low and low ﬁring rate to the binomial distribution and, therefore, also captures the behavior of the large proportion of units that had low ﬁring rates. In only 8 of the 44 responsive units (all in monkey 2) the Poisson model had a higher penalized likelihood (4) relative to the N. Gaussian model.

[Figure 876]

[Figure 877]

[Figure 878]

[Figure 879]

[Figure 880]

[Figure 881]

[Figure 882]

[Figure 883]

[Figure 884]

[Figure 885]

[Figure 886]

Note: our goal in using the statistical models above is to be able to calculate the likelihood of particular experimental outcomes. A few difﬁculties arise infrequently in this application: the inherent model error in the statistical model may lead to over-weighing outcomes with a very low likelihood, the expected ﬁring rate (calculated from the LN model) may become negative and the constraints in (7) and (8) lead to small negative values of for certain values of and . To address all of these issues we truncate the likelihood from below at a small value ( was chosen here).

[Figure 887]

[Figure 888]

[Figure 889]

[Figure 890]

[Figure 891]

[Figure 892]

[Figure 893]

[Figure 894]

[Figure 895]

[Figure 896]

[Figure 897]

[Figure 898]

VII. MODEL-BASED DECODING

Taken together, (3) and (9) deﬁne the likelihood of obtaining a certain number of spikes per bin in neuron . To simplify further calculations, we assume conditional independence between the simultaneous output of n neurons (see, e.g., [12] and [42]–[44] for different perspectives on the issue of dependencies in motor cortical coding). The independence assumption leads to the following likelihood of the combined ﬁring

[Figure 899]

[Figure 900]

[Figure 901]

[Figure 902]

[Figure 903]

[Figure 904]

[Figure 905]

[Figure 906]

[Figure 907]

[Figure 908]

[Figure 909]

[Figure 910]

[Figure 911]

[Figure 912]

[Figure 913]

[Figure 914]

[Figure 915]

[Figure 916]

[Figure 917]

[Figure 918]

[Figure 919]

[Figure 920]

[Figure 921]

[Figure 922]

[Figure 923]

[Figure 924]

[Figure 925]

[Figure 926]

[Figure 927]

[Figure 928]

[Figure 929]

[Figure 930]

[Figure 931]

[Figure 932]

[Figure 933]

[Figure 934]

[Figure 935]

[Figure 936]

[Figure 937]

[Figure 938]

[Figure 939]

(10)

[Figure 940]

[Figure 941]

[Figure 942]

[Figure 943]

[Figure 944]

[Figure 945]

[Figure 946]

[Figure 947]

[Figure 948]

[Figure 949]

[Figure 950]

[Figure 951]

[Figure 952]

[Figure 953]

[Figure 954]

[Figure 955]

[Figure 956]

[Figure 957]

[Figure 958]

[Figure 959]

[Figure 960]

[Figure 961]

[Figure 962]

[Figure 963]

[Figure 964]

[Figure 965]

[Figure 966]

[Figure 967]

[Figure 968]

[Figure 969]

[Figure 970]

[Figure 971]

[Figure 972]

[Figure 973]

A full statistical characterization of our experimental system also requires a model for the dynamics of the arm. As in similar applications in the applied estimation literature [45], [46]

[Figure 974]

Fig. 11. Performance of auto regressive models of a monkey’s hand movement. (a) Experimentally obtained traces of the monkey’s hand movement ( and coordinates). (b) Time series generated by 4th order autoregressive process ﬁt to data from (a). (c) power spectra for data in (a) and (b), as well as best AR model (9th order). (d) Blow up of (c) for low frequencies. (a) Hand position trace, (b) simulated AR(4) trace, (c) power spectra, (d) power spectra (zoom).

we choose the multivariate autoregressive (AR) model, a simple model which describes a large range of realistic motion traces and leads to tractable estimation procedures

[Figure 975]

[Figure 976]

[Figure 977]

[Figure 978]

[Figure 979]

[Figure 980]

[Figure 981]

[Figure 982]

[Figure 983]

[Figure 984]

[Figure 985]

[Figure 986]

[Figure 987]

[Figure 988]

[Figure 989]

[Figure 990]

[Figure 991]

[Figure 992]

(11)

where w is a vector of independent, unit variance random disturbances (Gaussian distributed), and G are matrices (estimated using the ARFIT package for ﬁtting multivariate AR models [47]), and contains the x and y position at time t. The full time trace was obtained by pasting detrended movement traces (to minimize discontinuities). The results of ﬁtting an auto regressive model to one of our data traces are illustrated in Fig. 11 (Note the good approximation provided by an order 4 model ).

[Figure 993]

[Figure 994]

[Figure 995]

[Figure 996]

[Figure 997]

[Figure 998]

[Figure 999]

[Figure 1000]

[Figure 1001]

[Figure 1002]

[Figure 1003]

[Figure 1004]

[Figure 1005]

With the encoding and movement models characterized it is now possible to deﬁne an algorithm for decoding the arm’s movement from the neural responses in a nearly optimal fashion which is tailored to the encoding statistics. Recently, algorithms for recursive Bayesian estimation based on sequential Monte Carlo methods [16] have gained popularity for applications involving nonlinear non-Gaussian observation models (i.e., encoding models), as is our case. The implementation proceeds by recursive application of two computational procedures at every time step, leading from a conditional probability distribution at time , through an intermediate distribution, to a new conditional probability distribution at time

[Figure 1006]

[Figure 1007]

[Figure 1008]

[Figure 1009]

[Figure 1010]

[Figure 1011]

[Figure 1012]

[Figure 1013]

[Figure 1014]

[Figure 1015]

[Figure 1016]

[Figure 1017]

[Figure 1018]

[Figure 1019]

[Figure 1020]

[Figure 1021]

[Figure 1022]

[Figure 1023]

[Figure 1024]

[Figure 1025]

[Figure 1026]

[Figure 1027]

[Figure 1028]

[Figure 1029]

[Figure 1030]

[Figure 1031]

[Figure 1032]

[Figure 1033]

[Figure 1034]

[Figure 1035]

[Figure 1036]

[Figure 1037]

[Figure 1038]

[Figure 1039]

[Figure 1040]

[Figure 1041]

[Figure 1042]

[Figure 1043]

[Figure 1044]

[Figure 1045]

[Figure 1046]

[Figure 1047]

[Figure 1048]

[Figure 1049]

[Figure 1050]

[Figure 1051]

[Figure 1052]

[Figure 1053]

[Figure 1054]

[Figure 1055]

[Figure 1056]

[Figure 1057]

[Figure 1058]

[Figure 1059]

[Figure 1060]

[Figure 1061]

[Figure 1062]

[Figure 1063]

[Figure 1064]

[Figure 1065]

[Figure 1066]

[Figure 1067]

[Figure 1068]

(12)

[Figure 1069]

Fig. 12. Performance of a Sequential Monte Carlo ﬁlter using 17 simultaneously recorded motor cortical units. The units were selected from the 27 isolated in monkey 2. (a) Estimation performance during 10 successful trials in the x (upper panel) and y (lower panel) dimensions. Trials were stitched together at the locations indicated by the vertical lines. (b) Histogram of correlation coefﬁcients for all 41 trials recorded.

As in all Monte Carlo methods, the conditional probability distributions are approximately represented by a set of representative random samples (or particles), and the computations involve simple operations such as particle movement [using the movement model (11)] and resampling [using the likelihood model (10)]. A detailed account of particle ﬁlter implementations is available elsewhere [16]–[18]. Each sample in our implementation is a vector with eight elements (eight-dimensional state space), corresponding to the positions and in 4 different time delays. Thus, the ﬁlter essentially uses the ﬁring up to time

[Figure 1070]

[Figure 1071]

to predict the hand position at time . We implemented the ﬁlter using 3000 particles, and our results for position decoding using the 17 best units (selected from the 27 recorded in monkey 2) are illustrated in Fig. 12. In over of the trials the model-based trajectory estimate had a correlation coefﬁcient larger than 0.8 when compared to the actual position trajectory. The correlation coefﬁcients mean value was . In contrast, trajectories computed using a vector-based optimal linear estimator (OLE) [10] (with a single time bin set at zero delay, as in [18]) had an average correlation coefﬁcient of 0.25 with the actual trajectory (not shown).

[Figure 1072]

[Figure 1073]

[Figure 1074]

[Figure 1075]

[Figure 1076]

[Figure 1077]

[Figure 1078]

[Figure 1079]

[Figure 1080]

[Figure 1081]

[Figure 1082]

[Figure 1083]

VIII. DISCUSSION

Ourdevelopmentofstatisticalencodingmodelsfortheactivity of MI neurons has introduced a few useful new tools and pro-

vided some insight into properties of motor encoding. We began bycharacterizingtheencodingofkinematicsbyMIneuronﬁring rates.Themajorityoftheneuronswehavestudiedherehadﬁring ratesthatwerelinearlyrelatedtothekinematicvariables.Thislinearityisnotsurprising,asitisconsistentwiththeclassicalcosine shaped tuning curve(with respect to the direction of movement), and was thus anticipated by theoretical studies [5], [48]. However, a possibility that cannot be discounted based on our data is thatthelinearityresultsfromanunderlyingnonlinearrelationship thatisartiﬁciallylinearizedbybeingexperimentallysampledina narrowrangeofpositions,velocities,andaccelerations.Sincewe are probably underestimating the full-range nonlinearity, it is interestingtonotethatoveronethirdoftheresponsiveunitswehave studied exhibited signiﬁcant nonlinearity, and that most of the highly informative neurons were nonlinear. Nonlinear motor encodingmayreﬂectpervasivenonlinearitiesthroughoutthemotor control system (which models typically linearize [3]), and a speciﬁc multiplicative form of motor encoding nonlinearity has recentlybeensuggestedbasedonpsychophysicaldata[49].Experimentalmethodsthatenabletrackingthearmpositionoverawide range of motions are now available (e.g., the Shape Tape, Measurand Inc., Fredricton, NB, Canada), and this study illustrates theimportanceofperformingsuchexperimentsinordertoobtain a more complete picture of motor encoding processes.

This analysis also shows that motor cortical units encode complex functions of the arm position and its derivatives, which does not lend support to the view that motor cortex neurons encode only simpliﬁed global features of movement (like the direction of movement). To emphasize this point, we have provided a direct illustration of the extremely weak predictive power of velocity-based encoding models in a representative unit, and contrasted it with the more complete characterization provided using the LN cascade models (Fig. 7). We note that the cascade approach can also be extended to the study of neuronal interactions [44].

We found that the variability around the expected ﬁring rate is markedly sub-Poisson in many of the movement-related units we recorded, and those units may exhibit a nearly constant variance across a wide dynamic range. In contrast with other studies that have looked at variability of motor responses (e.g., [12]), we have attempted to use our encoding model to account for some of the variability that is a result of the movement-related modulations in ﬁring rate. The remaining variability, which we capture using the Normalized-Gaussian noise model, is due in part to using an imperfect model, in part to the imperfect observation of motion (only movement in 2-D was measured in our experiments), and in part to the inherent statistics of neuronal ﬁring. Our use of a predictive model in conjunction with the neural noise plot introduced here allowed us to faithfully represent signal-dependent distributions that are necessary for model-based decoding; however, we are unable to distinguish between the different sources of variance with the existing dataset. This difﬁculty notwithstanding, it is extremely likely that after ‘explaining’ additional variance the intrinsic neural statistical properties will have very little variance—markedly sub-Poisson. The nonpoisson nature of the variability has a number of implications. Square-root transforming of binned counts (e.g., [29] and [50]) is a variance stabilizing transformation suitable for Poisson processes where the noise variance

depends on the signal, and is ill-suited for the analysis of data with the properties we have described. Interestingly, the signal-dependent noise observed in the peripheral motor system, which may explain a number of phenomenological scaling laws observed in motor control [51] does not depend on signal dependent noise in MI, but rather on the organization and properties of the peripheral motor-unit pool [52].

In order to addressthe observedstatistical properties of neural ﬁring we developed the Normalized Gaussian distribution, a new discrete probability distribution. We anticipate that the new distribution will ﬁnd many additional applications in studies of neural systems, particularly cortical systems. While we have used it in conjunction with a predictive model, in other types of experiments the peri-stimulus time histogram (PSTH) of responses to highly reproducible experimental conditions could provide an approximate ﬁring rate model. This probability distribution is easy to compute, provides a signal independent varianceat highspike counts andsmoothlytransitions toa binomiallike behavior at low spike counts. It is also ﬂexible enough to ﬁt different data with a range of non-Poisson variability characteristics. The statistics of responses in extended time-windows in the visual cortex [53] are well ﬁt by a truncated Gaussian, similar to the statistics observed in the primary motor cortex [12], strengthening our belief in the general applicability of the Normalized-Gaussian distribution.

Finally, we have demonstrated that the encoding model presented can be integrated with recursive likelihood-based estimation procedures to yield practical ﬁlters for a brain-machine interface. The ﬁlter we implemented yielded a very large performance gain versus the optimal linear vector-based method (which out-performs the population vector [10]). This result was partially due to the recursive ﬁlter’s ability to use the temporal smoothness of the motion trajectory while the OLE is an instantaneous estimator. Other ﬁltering methods available for this application include ﬁnite-impulse response linear ﬁlters [27], [54]–[56], recursive Kalman ﬁltering [see [57]] and neural network based ﬁlters [56] (note that [27] and [57] tested their results using the same experimental data that we used here). Based on fundamental results in estimation theory, the optimal ﬁlter for a linear encoding model, with an additive Gaussian noise process is a linear one. This appears not very far from the situation we have described here for motor cortical units. Nevertheless, we expect that the model-based approach used here will offer future advantages in this brain-machine interface application. First, the models used are compact and the small number of parameters makes for good generalization. Second, they provide clear measures for which units are “good encoders,” providing for improved generalization performance. Third, our ﬁlter is recursive and so can deal well with short decoding epochs. Fourth, it can easily deal with recording nonstationarity (unit adaptation and loss). And ﬁnally, it is quite likely that most neurons used in actual brain-machine interfaces will exhibit rich nonlinearities in their activity patterns, which will also be well-captured by our approach.

ACKNOWLEDGMENT

The authors would like to thank Y. Gao, D. J. Warren, Prof. S. Geman, Prof. E. Bienenstock, Prof. M. Black, Prof. E. Brown,

and Prof. S. Nagarajan as well as two anonymous referees for valuable input during the preparation of this manuscript.

REFERENCES

- [1] A. P. Georgopoulos, J. F. Kalaska, R. Caminiti, and J. T. Massey, “On the relations between the direction of two-dimensional arm movements and cell discharge in primate motor cortex,” J. Neurosci., vol. 2, pp. 1527–1537, 1982.
- [2] D. R. Humphrey, “Relating motor cortex spike trains to measures of motor performance,” Brain Res., vol. 40, pp. 7–18, 1972.
- [3] E. Todorov, “Direct cortical control of muscle activation in voluntary arm movements: A model,” Nat. Neurosci., vol. 3, pp. 391–398, 2000.
- [4] F. A. Mussa-Ivaldi, “Do neurons in the motor cortex encode movement direction? An alternative hypothesis,” Neurosci. Lett., vol. 91, pp. 106–111, 1988.
- [5] T. D. Sanger, “Theoretical considerations for the analysis of population coding in motor cortex,” Neural Comput., vol. 6, pp. 29–37, 1994.
- [6] E. N. Brown, L. M. Frank, D. Tang, M. C. Quirk, and M. A. Wilson, “A statistical paradigm for neural spike train decoding applied to position prediction from ensemble ﬁring patterns of rat hippocampal place cells,” J. Neurosci., vol. 18, pp. 7411–7425, 1998.
- [7] R. Barbieri, M. C. Quirk, L. M. Frank, M. A. Wilson, and E. N. Brown, “Construction and analysis of nonpoisson stimulus-response models of neural spiking activity,” J. Neurosci. Methods, vol. 105, pp. 25–37, 2001.
- [8] E. N. Brown, R. Barbieri, V. Ventura, R. Kass, and L. M. Frank, “The time-rescaling theorem and its application to neural spike train data analysis,” Neural Comput., vol. 14, pp. 325–346, 2001.
- [9] A. P. Georgopoulos, A. B. Schwartz, and R. E. Kettner, “Neuronal population coding of movement direction,” Science, vol. 233, pp. 1416–1419, 1986.
- [10] E. Salinas and L. F. Abbott, “Vector reconstruction from ﬁring rates,” J. Comput. Neurosci., vol. 1, pp. 89–107, 1994.
- [11] T. D. Sanger, “Probability density estimation for the interpretation of neural population codes,” J. Neurophysiol., vol. 76, pp. 2790–2793, 1996.
- [12] E. M. Maynard, N. G. Hatsopoulos, C. L. Ojakangas, B. D. Acuna, J. N. Sanes, R. A. Normann, and J. P. Donoghue, “Neuronal interactions improve cortical population coding of movement direction,” J. Neurosci., vol. 19, pp. 8083–8093, 1999.
- [13] A. V. Lukashin, B. R. Amirikian, and A. P. Georgopoulos, “A simulated actuator driven by motor cortical signals,” Neuroreport, vol. 7, pp. 2597–2601, 1996.
- [14] J. P. Donoghue, “Connecting cortex to machines: Recent advances in brain interfaces,” Nat. Neurosci., vol. 5, pp. 1085–1088, 2002. Suppl..
- [15] M. A. L. Nicolelis, “Brain-machine interfaces to restore motor function and probe neural circuits,” Nat. Rev. Neurosci., vol. 4, pp. 417–422, 2003.
- [16] A. Doucet, N. D. Freitas, and N. Gordon, Sequential Monte Carlo Methods in Practice. Berlin, Germany: Springer-Verlag, 2001.
- [17] S. Shoham, “Advances toward an implantable motor cortical interface,” Ph.D. Disseertation, Dept. Bioeng, Univ. Utah, Salt Lake City, 2001.
- [18] A. E. Brockwell, A. L. Rojas, and R. E. Kass, “Recursive Bayesian decoding of motor cortical signals by particle ﬁltering,” J. Neurophysiol., vol. 91, pp. 1899–1907, 2004.
- [19] K. E. Jones, P. K. Campbell, and R. A. Normann, “A glass/silicon composite intracortical electrode array,” Ann. Biomed. Eng., vol. 20, pp. 423–437, 1992.
- [20] E. M. Maynard, E. Fernandez, and R. A. Normann, “A technique to prevent duraladhesions to chronically implanted microelectrodearrays,” J. Neurosci. Methods, vol. 97, pp. 93–101, 2000.
- [21] J. P. Donoghue, J. N. Sanes, N. G. Hatsopoulos, and G. Gaal, “Neural discharge and local ﬁeld potential oscillations in primate motor cortex during voluntary movements,” J. Neurophysiol., vol. 79, pp. 159–173, 1998.
- [22] E. M. Maynard, C. T. Nordhausen, and R. A. Normann, “The Utah intracortical electrode array: A recording structure for potential brain-computer interfaces,” Electroencephalogr. Clin. Neurophysiol., vol. 102, pp. 228–239, 1997.
- [23] P. J. Rousche and R. A. Normann, “Chronic recording capability of the Utah intracortical electrode array in cat sensory cortex,” J. Neurosci. Methods, vol. 82, pp. 1–15, 1998.
- [24] M. D. Serruya, N. G. Hatsopoulos, L. Paninski, M. R. Fellows, and J. P. Donoghue, “Brain-machine interface: Instant neural control of a movement signal,” Nature, vol. 416, pp. 141–142, 2002.

- [25] K. S. Guillory and R. A. Normann, “A 100-channel system for real time detection and storage of extracellular spike waveforms,” J. Neurosci. Methods, vol. 91, pp. 21–29, 1999.
- [26] S. Shoham, M. R. Fellows, and R. A. Normann, “Robust, automatic spike sorting using mixtures of multivariate t-distributions,” J. Neurosci. Methods, vol. 127, pp. 111–122, 2003.
- [27] L. Paninski, M. R. Fellows, N. G. Hatsopoulos, and J. P. Donoghue, “Spatiotemporal tuning of motor cortical neurons for hand position and velocity,” J. Neurophysiol., vol. 91, pp. 515–532, 2004.
- [28] D. L. Snyder and M. I. Miller, Random Point Processes in Time and Space, 2nd ed. New York: Springer, 1991.
- [29] D. W. Moran and A. B. Schwartz, “Motor cortical representation of speed and direction during reaching,” J. Neurophysiol., vol. 82, pp. 2676–2692, 1999.
- [30] B. Amirikian and A. P. Georgopulos, “Directional tuning proﬁles of motor cortical cells,” Neurosci. Res., vol. 36, pp. 73–79, 2000.
- [31] K. Zhang, I. Ginzburg, B. L. McNaughton, and T. J. Sejnowski, “Interpreting neuronal population activity by reconstruction: Uniﬁed framework with application to hippocampal place cells,” J. Neurophysiol., vol. 79, pp. 1017–1044, 1998.
- [32] J. Ashe and A. P. Georgopoulos, “Movement parameters and neural activity in motor cortex and area 5,” Cereb. Cortex, vol. 4, pp. 590–600, 1994.
- [33] D. W. Moran and A. B. Schwartz, “Motor cortical activity during drawing movements: Population representation during spiral tracing,” J. Neurophysiol., vol. 82, pp. 2693–2704, 1999.
- [34] I. W. Hunter and M. J. Korenberg, “The identiﬁcation of nonlinear biological systems: Wiener and Hammerstein cascade models,” Biol. Cybern., vol. 55, pp. 135–144, 1986.
- [35] M. J. Korenberg and I. W. Hunter, “Two methods for identifying Wiener cascades having noninvertible static nonlinearities,” Ann. Biomed. Eng., vol. 27, pp. 793–804, 1999.
- [36] E. J. Chichilnisky, “A simple white noise analysis of neuronal light responses,” Network, vol. 12, pp. 199–213, 2001.
- [37] L. Paninski, “Convergence properties of three spike-triggered analysis techniques,” Network, vol. 14, pp. 437–464, 2003.
- [38] G. Schwarz, “Estimating the dimensions of a model,” Ann. Statist., vol. 6, pp. 461–464, 1978.
- [39] Q. G. Fu, D. Flament, J. D. Coltz, and T. J. Ebner, “Temporal encoding of movement kinematics in the discharge of primate primary motor and premotor neurons,” J. Neurophysiol., vol. 73, pp. 836–854, 1995.
- [40] M. J. Berry, D. K. Warland, and M. Meister, “The structure and precision of retinal spike trains,” Proc. Nat. Acad. Sci., vol. 94, pp. 5411–5416, 1997.
- [41] N. L. Johnson and S. Kotz, Discrete Distributions. Boston, MA: Houghton Mifﬂin, 1969.
- [42] A. Riehle, S. Grun, M. Diesmann, and A. Aertsen, “Spike synchronization and rate modulation differentially involved in motor cortical function,” Science, vol. 278, pp. 1950–1953, 1997.
- [43] N. G. Hatsopoulos, L. Paninski, and J. P. Donoghue, “Sequential movement representations based on correlated neuronal activity,” Exp. Brain Res., vol. 149, pp. 478–486, 2003.
- [44] L. Paninski, S. Shoham, M. R. Fellows, N. G. Hatsopoulos, and J. P. Donoghue, “Superlinear population encoding of dynamic hand trajectory in primary motor cortex,” J. Neurosci., vol. 24, pp. 8551–8561, 2004.
- [45] A. Gelb, Applied Optimal Estimation. Cambridge, MA: MIT Press, 1974.
- [46] P. S. Maybeck, Stochastic Models, Estimation, and Control. New York: Academic, 1979, vol. 1–3.
- [47] T. Schneider and A. Neumaier, “Algorithm 808: ARﬁt—A Matlab package for the estimation of parameters and eigenmodes of multivariate autoregressive models,” in ACM Trans. Math. Softw., vol. 27, 2001, pp. 58–65.
- [48] K. Zhang and T. J. Sejnowski, “A theory of geometric constraints on neural activity for natural three-dimensional movement,” J. Neurosci., vol. 19, pp. 3122–3145, 1999.
- [49] E. J. Hwang, O. Donchin, M. A. Smith, and R. Shadmehr, “A gain-ﬁeld encoding of limb position and velocity in the internal model of arm dynamics,” PLoS Biol., vol. 1, p. E25, 2003.
- [50] A. B. Schwartz, “Motor cortical activity during drawing movements: Population representation during sinusoid tracing,” J. Neurophysiol., vol. 70, pp. 28–36, 1993.
- [51] C. M. Harris and D. M. Wolpert, “Signal-dependent noise determines motor planning,” Nature, vol. 394, pp. 780–784, 1998.

- [52] K. E. Jones, A. F. De, C. Hamilton, and D. M. Wolpert, “Sources of signal-dependent noise during isometric force production,” J. Neurophysiol., vol. 88, pp. 1533–1544, 2002.
- [53] E. D. Gershon, M. C. Wiener, P. E. Latham, and B. J. Richmond, “Coding strategies in monkey V1 and inferior temporal cortices,” J. Neurophysiol., vol. 79, pp. 1135–1144, 1998.
- [54] D. R. Humphrey, E. M. Schmidt, and W. D. Thompson, “Predicting measures of motor performance from multiple cortical spike trains,” Science, vol. 170, pp. 758–762, 1970.
- [55] A.B.Schwartz,“Directcortical representationofdrawing,”Science,vol. 265, pp. 540–542, 1994.
- [56] J. Wessberg, C. R. Stambaugh, J. D. Krallk, P. D. Beck, M. Laubach, J. K. Chapin, J. Kim, S. J. Biggs, M. A. Srinivasan, and M. A. L. Nicolelis, “Real-time prediction of hand trajectory by ensembles of cortical neurons in primates,” Nature, vol. 408, pp. 361–365, 2000.
- [57] W. Wu, M. J. Black, D. Mumford, Y. Gao, E. Bienenstock, and J. P. Donoghue, “Modeling and decoding motor cortical activity using a switching Kalman ﬁlter,” IEEE Trans. Biomed. Eng., vol. 51, no. 6, pp. 933–942, Jun. 2004.

Liam M. Paninski, photograph and biography not available at the time of publication.

Matthew R. Fellows, photograph and biography not available at the time of publication.

Nicholas G. Hatsopoulos, photograph and biography not available at the time of publication.

John P. Donoghue, photograph and biography not available at the time of publication.

Shy Shoham (S’97–M’01) , photograph and biography not available at the time of publication.

Richard A. Normann, photograph and biography not available at the time of publication.

