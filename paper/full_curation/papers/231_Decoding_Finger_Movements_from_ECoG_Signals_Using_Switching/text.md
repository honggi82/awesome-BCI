arXiv:1106.3395v1[cs.LG]17Jun2011

Decoding ﬁnger movements from ECoG signals using switching linear models

R´emi Flamary and Alain Rakotomamonjy

Universite´ de Rouen, LITIS EA 4108, Avenue de l’Universit´e, 76801 Saint-Etienne-du-Rouvray,´ France, {remi.flamary,alain.rakoto}@insa-rouen.fr

Abstract. One of the major challenges of ECoG-based Brain-Machine Interfaces is the movement prediction of a human subject. Several methods exist to predict an arm 2-D trajectory. The fourth BCI Competition gives a dataset in which the aim is to predict individual ﬁnger movements (5-D trajectory). The diﬃculty lies in the fact that there is no simple relation between ECoG signals and ﬁnger movement. We propose in this paper to decode ﬁnger ﬂexions using switching models. This method permits to simplify the system as it is now described as an ensemble of linear models depending on an internal state. We show that an interesting accuracy prediction can be obtained by such a model.

- 1 Introduction

Some people who suﬀer some neurological diseases can be highly paralyzed because they do not have anymore control on their muscles. Therefore, their only way to communicate is by using their electroencephalogram signals. BrainComputer interfaces (BCI) research aim at developing systems that help those disabled people communicating with machines. Non-invasive BCIs have recently received a lot of interest because of their easy protocol for sensors implantation on the scalp surface [1,2]. Furthermore, although the electroencephalogram signals have been recorded through the skull, those BCI have shown great performance capabilities, and can be used by real Amyotrophic Lateral Sclerosis (ALS) patients [3,4].

However, non-invasive recordings still show some drawbacks including poor signal to noise ratio and poor spatial resolution. Hence, in order to overcome these diﬃculties, invasive BCI may be used. For instance, Electrocorticographic recordings (ECoG) have recently received a great amount of interest owing to their semi-invasive nature as they are recorded from the cortical surface. Indeed, they oﬀer higher spatial resolution and they are far less sensitive to artifact noise. Feasibility of invasive-based BCI have been proven by several recent papers [5,6,7,8]. In many of these papers, the BCI paradigm considered is motor imagery yielding thus to a binary decision BCI.

A recent breakthrough has been made by Schalk et al. [9] which has proven that ECoG recordings can lead to multiple-degree BCI control. Followed by

Pistohl et al. [10], these two works have considered the problem of predicting arm movements from ECoG signals. Both approaches are based on estimating a linear relation between features extracted from ECoG signals and the actual arm movement.

In this work, we investigate a ﬁner degree of resolution in BCI control by addressing the problem of estimating ﬁnger ﬂexions through ECoG signals. Indeed, we propose in this paper a method for decoding ﬁnger movements from ECoG data based on switching models. The underlying idea of switching models is the hypothesis that movements of each of the ﬁve ﬁngers are triggered by an internal discrete state that can be estimated and that all ﬁnger movements depend on that internal state. While such an idea of switching models have already been successfully used for arm movement prediction on monkeys from micro-electrode array measures [11], here, we develop a speciﬁc approach adapted to ﬁnger movements. The global method has been tested on the 4th Dataset of the BCI Competition IV[12].

The paper is organized as follows : First, we present the dataset from the BCI Competition IV used in this paper, then we explain our decoding method used to obtain ﬁnger ﬂexion from ECoG signals. Finally we present the results obtained with our method and we discuss several ways of improving them.

- 2 Dataset

For this work, the fourth dataset from the BCI Competition IV [12] was used. The subjects were 3 epileptic patients who had platinium electrode grids placed on the surface of their brain. The number of electrodes vary between 48 to 64 depending on the subject and their position on the cortex was unknown.

Electrocorticographic (ECoG) signals of the subject were recorded at a 1KHz sampling using BCI2000 [13]. A band-pass ﬁlter from 0.15 to 200Hz was applied to the ECoG signals. The ﬁnger ﬂexion of the subject was recorded at 25Hz and up-sampled to 1KHz. Due to the acquisition process, a delay appears between the ﬁnger movement and the measured ECoG signal. To correct this time-lag we apply the 37 ms delay proposed in the dataset description [12] to the ECoG signals.

The BCI Competition dataset consists in a 10 minutes recording per subject. 6 minutes 40 seconds (400,000 samples) were given for the learning models and the remaining 3 minutes 20 seconds (200,000 samples) were used for testing. However, since the ﬁnger ﬂexion signals have been up-sampled and thus are partly composed of artiﬁcial samples, we have down-sampled the number of points by a factor of 4 leading to a training set of size 100,000 and a testing set of size 50,000. The 100,000 samples provided for learning have been splitted in a training (75,000) and validation set (25,000). Then, all parameters of the approach have been optimized in order to maximize the performance on the validation set. Note that all results presented in the paper have been obtained using the testing set provided by the competition (after up-sampling then back by a factor of 4).

In this competition, method performance was measured through the crosscorrelation between the measured and the estimated ﬁnger ﬂexion. The correlation were averaged across ﬁngers and across subject to obtain the overall method performance. Note that the fourth ﬁnger was not used for evaluation in the competition since its movements were proven to be correlated with the other one movements [12].

- 3 Finger ﬂexion decoding using switching linear models

This section presents the full methodology we have used for addressing the problem of estimating ﬁnger ﬂexions from ECoG signals. In the ﬁrst part, we propose an overview of the switching models. Then, we describe how we learn the function that estimates which ﬁnger is about to move. Afterwards, we detail the linear models associated to each moving ﬁnger. Finally, we brieﬂy detail how the complete method works in the decoding stage.

- 3.1 Overview

In order to obtain an eﬃcient prediction of ﬁnger ﬂexions, we have made the hypothesis that for such movements the brain can be understood as a switching model. This translates into the assumption that the measured ECoG signals and the ﬁnger movements are intrinsically related by an internal state k. In our case, this state corresponds to each ﬁnger moving, k = 1 for the thumb to k = 5 for the baby ﬁnger or k = 6 for no ﬁnger movement. Here, we used mutually-exclusive states because the experimental set-up considered speciﬁes that only one or no ﬁnger is moving. Figure 1 gives the picture of our ﬁnger movement decoding scheme. Basically, the idea is that based on some features extracted from the ECoG signals, the internal hidden state triggering the switching ﬁnger models can be estimated. Then, this state allows the system to select an appropriate model Hk(x˜) for estimating all ﬁnger ﬂexions, with x˜ being a feature vector.

For the complete model, we need to estimate the function f(·) that maps the ECoG features to an internal state k ∈ {1,··· ,6} and the functions Hk(·) that relates the brain signals to all ﬁnger ﬂexion amplitudes. The next paragraphs present how we have modeled these functions and how we have estimated them from the data.

- 3.2 Moving ﬁnger estimation

The methodology used for learning the f(·) function which estimates the moving ﬁnger is given in the sequel.

Feature extraction For this problem of estimating the moving ﬁnger, the features we used are based on smoothed Auto-Regressive (AR) coeﬃcient of the signal. The global overview of the feature extraction procedure is given in

| | | | |
|---|---|---|---|
| | | | |

| | |
|---|---|
| | |

- Fig.1: Diagram of our switching models decoder. We see that from the ECoG signals, we estimate two models. (bottom ﬂow) one which outputs a state k predicting which ﬁnger is moving and (top ﬂow) another one that, given the predicted moving ﬁnger, estimates the ﬂexion of all ﬁngers.

- Fig.2: Diagram of the feature extraction procedure for the moving ﬁnger decoding. Here, we have outlined the processing of a single channel signal.

Figure 2. For a single channel, the procedure is the following. The signal from that channel is divided in non-overlapping window of 300 samples. For each window, an auto-regressive model has been estimated. Thus, AR coeﬃcients are obtained at every 300 samples (denoted by the vertical dashed line and the cross in Figure 2). In order to have a continuous AR coeﬃcients value, a smoothing spline-based interpolation between two consecutive AR coeﬃcients has been used. Note that instead of interpolating, we could have computed the AR coeﬃcients at each time instant, however, the approach we propose here has the double advantage of being less-computationally demanding and of providing some smoothed (and thus more robust to noise) AR coeﬃcients. Finally, only the two ﬁrst AR coeﬃcients are used as features. Signal dynamics have been taken into account by applying a similar procedure to shifted version of the signal at (+ts and −ts). Hence, for measurements involving 48 channels, the feature vector at a time instant t is obtained by concatenating features extracted from all channels, leading to a resulting vector of size 48 × 3 × 2 = 240.

Channel Selection Actually, we do not consider in the model all the channels. Indeed, a channel selection algorithm has been run in order to reduce the number

of channels. For this channel selection procedure, the feature vector xt at time t has been computed as described above, except that we have not considered the shifted signal versions and used only the ﬁrst AR coeﬃcient.

Then, for each ﬁnger, based on the training set, we estimated a linear regression y = xtck where x ∈ Rchan is a feature vector of number of channels dimension, y = {1,−1} stating if the considered ﬁnger is moving or not. Once, we have estimated the coeﬃcient vector ck for each ﬁnger, we selected the K channels that present the largest values of :

6

|ck|

k=1

where the absolute value is considered as element-wise. This channel selection allows us to reduce substantially the number of channels so as to minimize the computational eﬀort needed for estimating and evaluating the function f(·) and it yields better performance. K has been chosen so that the cross-correlation on the validation set is maximal.

Model estimation The model for estimating which ﬁnger is moving is a more sophisticated version of the one used above for channel selection. At ﬁrst, since the ﬁnger movements are mutually-exclusive, we have considered a winner-takesall strategy :

f(x) = argmax

fk(x) (1)

k=1,··· ,6

Here again, fk(x) is a linear model that is trained by presenting couples of feature vector and a state y = {1,−1}. The main diﬀerences between the channel selection procedure and the one used for learning fk(·) are that : the features here take into account some dynamics of the ECoG signals and a ﬁner feature selection has been performed by means of a simultaneous sparse approximation method.

Let us consider the training examples {xt,yt}ℓt=1 where xt ∈ Rd, yt,k = {1,−1}, being the k-th entry of vector yt, t denoting the time instant and k denoting all possible states (including no ﬁnger moving). yt,k tells us whether the ﬁnger k is moving at time t. Now, let us deﬁne the matrix Y, X and C as :

[Y]t,k = yt,k [X]t,j = xt,j [C]j,k = cj,k

where xt,j and cj,k are the j-th components of respectively xt and ck. The aim of simultaneous sparse approximation is to learn the coeﬃcient matrix C while yielding the same sparsity proﬁle in the diﬀerent ﬁnger models. The task boils down to the following optimization problem:x

Cˆ = argmin

C

Y − XC 2F + λs

i

Ci,· 2 (2)

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

- Fig.3: Workﬂow of the learning sets extraction (Xk and Yk) and estimation of the linear models Hk.

where λs is a trade-oﬀ parameter that has to be appropriately tuned and Ci,· being the i-th row of C. Note that our penalty term is a mixed ℓ1 − ℓ2 norm similar to those used for group-lasso. Owing to the ℓ1 penalty on the ℓ2 row-norm, such a penalty tends to induce row-sparse matrix C. Problem (2) has been solved using the block-coordinate descent algorithm proposed by Rakotomamonjy [14].

- 3.3 Learning ﬁnger ﬂexion models

Here, we discuss the model relating the ECoG data and ﬁnger movements for every possible values of k. In other words, supposing that a given ﬁnger, say the index, is going to move (as predicted by our ﬁnger moving estimation), we built an estimation of all ﬁnger movements. Hence, for each k, we are going to learn

a linear model gk,j(x˜) = x˜Th(jk) with j = 1,··· ,5, x˜ a feature vector and h(jk) a weighting vector indexed by the moving ﬁnger k and the ﬁnger j which ﬂexions are to estimate. We have chosen a linear model since they have been shown to provide good performances for decoding movements from ECoG [10,9].

At a time t, the feature vector xt has been obtained by following the same line as Pistohl et al. [10]. Indeed, we use ﬁltered time-samples as features. xt has been built in the following way. All channels have been ﬁltered with a SavitskyGolay (third order, 0.4 s width) low-pass ﬁlter. Then, xt is composed of the concatenation of the time samples at t, t − τ and t + τ for all smoothed signals

at all channels. Samples at t−τ and t+τ have been used in order to to take into account some temporal delays between the brain activity and ﬁnger movements.

Now, let us detail how, for a given moving ﬁnger k, the weight matrix Hk = [h(1k) ···h(5k)] has been learned. For a given ﬁnger k, we have used as a training set all samples xt where that ﬁnger is known to be moving. For this purpose, we have manually segmented the signals and extracted the appropriate signal segments, needed for building the target matrix Y˜k, which contains all ﬁnger positions, and for extracting the feature matrix X˜ k. This training samples extraction stage is illustrated on Figure 3. Then for learning the global linear model, we have solved the following multi-dimensional ridge regression problem.

min

Hk

Y ˜ k − X˜ kHk 2F + λk Hk 2F (3)

with λk being a regularization parameter that has to be tuned.

For this problem of ﬁnger movements estimation, we also noted that feature selection helps in improving performance. Again, we have used the estimated weighting matrix Hˆ coeﬃcients for pruning the model. Indeed, we have kept in the model the M features which correspond to the M largest entries of vector

5 i=1 |hˆ(ik)|. For possible k and subjects, M is chosen as to minimize a validation

error. Note that such an approach for pruning model can be interpreted as a shrinkage of a least-square parameters.

- 3.4 Decoding ﬁnger movement

When all models have been learned, the decoding scheme is the one given in Figure 1. Given the two feature vectors xt and x˜t at a time t, the ﬁnger position estimation is obtained as:

yˆ = x˜Tt Hˆ kˆ with kˆ = argmax

xttck (4)

k

with yˆ being a row vector containing the estimated ﬁnger movement, kˆ the ﬁnger that is supposed to move, x˜t the extracted feature at time t and Hˆ kˆ the estimated linear model for state k.

- 4 Results

In this section we present the performance of our switching model decoder. At ﬁrst, we explain how all parameters of the models have been set. Then, we present some results which help us understanding the contribution of the diﬀerent parts of our models, Finally, we evaluate our approach and compare ourselves to the BCI competition results.

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

Finger Learning Validation

[Figure 6]

[Figure 7]

- 1 8355 3848

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

- 2 9750 2965

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

- 3 13794 3287

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

- 4 6179 2915

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

- 5 10729 5362

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

- 6 26074 6623

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

- Table 1: Number of samples used in the validation step for subject 1

[Figure 32]

[Figure 33]

Finger Sub. 1 Sub. 2 Sub. 3 Average

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

- 1 0.4191 0.5554 0.7128 0.5625

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

- 2 0.4321 0.4644 0.6541 0.5169

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

- 3 0.6162 0.3723 0.2492 0.4126

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

- 4 0.4091 0.5668 0.0781 0.3513

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

- 5 0.4215 0.5165 0.5116 0.4832 Avg. 0.4596 0.4951 0.4411 0.4653

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

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

- Table 2: Correlation coeﬃcient obtained by the linear models h(kk).

- 4.1 Parameter selection

The parameters used in the moving ﬁnger estimation are selected by a validation method on the last part of the training set (75,000 for the training, 25,000 for validation). We suppose that the size of the set is important enough to avoid over-ﬁtting. Using this method, we select the number of selected channels, the time-lag ts used in feature extraction and the regularization term λs of Eq. (2).

Similarly, all parameters(τ, the number of selected channels and λk) needed for estimating Hk have been set so that they optimize the model performance of on the validation sets. For this model selection part, the size of training and validation sets vary according to k and they are summarized in Table 1 for subject 1.

- 4.2 Evaluating of the linear models Hk

Models Hk correspond to the linear regressions between the ECoG features and the ﬁnger ﬂexions when the k-th ﬁnger is moving. The signals used for evaluating these models are extracted in the same manner as the learning sets yk and X˜ k (see Figure 4) but by assuming that the true segmentation of ﬁnger movements are known. To evaluate these models, we measure the cross-correlation between the true yk and estimated ﬁnger ﬂexion X˜ khˆkk only when the ﬁnger k is moving. The correlations can be seen on Table 2.

We observe that by using a linear regression between the ECoG signals and the ﬁnger ﬂexions, we achieve a correlation of 0.46 (averaged across ﬁngers and subjects). This results correspond to those obtained for the arm trajectory prediction (Schalk [9] obtained 0.5 and Pistohl [10] obtained 0.43).

- Fig.4: Signal extraction for linear model estimation: (upper plot) full signal with segmented signal, corresponding to moving ﬁnger, bracketed by the vertical lines and (lower plot) the extracted signal corresponding to the concatenation of the samples when ﬁnger 1 is moving.

- 4.3 Evaluating the switching decoder method

In order to evaluate the eﬃciency of the switching model decoder and each block of the decoder contribution. We report three diﬀerent results: ﬁrst, for a given ﬁnger, we compute the estimated ﬁnger ﬂexion using a linear model learned on all samples (including those where the considered ﬁnger is not moving), then we decode ﬁnger ﬂexions with our switching decoder while assuming that the exact sequence of hidden states is known1 and ﬁnally we use our switching decoder with the estimated hidden states.

For a sake of baseline comparison with our switching models decoder, we have estimated the ﬁnger ﬂexions by means of a single linear model which has been trained using all the time samples. The obtained correlation are given in Table 3a and the regression result can be seen on the upper plots of Figure 5. We can see that the correlation obtained are rather low due the fact that without switching models the amplitude of the ﬂexion signals remains small.

The switching model decoder is a two-part process as it requires to have the linear models Hk and the sequence of hidden states. First we apply the decoder using the true sequence obtained thanks to the actual ﬁnger ﬂexion. Suppose that we have the exact sequence k and we apply the switching decoder with this sequence. We know that these results may never be attained as it supposes the sequence labeling method to be perfect but it gives a interesting idea of the maximal performance that our method can provide for given linear models Hk. Results can be seen in the middle plots of Figure 5 and correlations are in Table

- 3b. We obtain a high accuracy accross all subjects with an average correlation of 0.61 when using an exact sequence. This proves that the switching model can be eﬃciently used for decoding ECoG signals. Note that by using switching linear models, we include a switching mean that induce a high accuracy of correlation.

[Figure 92]

1 This is possible since the ﬁnger movements on the test set are now available

Result with a unique regression corr=0.18 (subject 1, finger 1)

Result with a unique regression corr=0.18 (subject 1, finger 2)

6

6

|Measured Estimated<br><br>|
|---|

|Measured Estimated<br><br>|
|---|

4

4

2

2

0

0

| | |
|---|---|
| | |

Result with switching models and exact sequence corr=0.80 (subject 1, finger 1)

Result with switching models and exact sequence corr=0.74 (subject 1, finger 2)

6

6

| |
|---|

4

4

2

2

0

0

| | |
|---|---|
| | |

Result with switching models and estimated sequence corr=0.70 (subject 1, finger 1)

Result with switching models and estimated sequence corr=0.61 (subject 1, finger 2)

6

6

4

4

2

2

0

0

| | |
|---|---|
| | |

| | |
|---|---|
| | |

(a) Subject 1, Finger 1

(b) Subject 1, Finger 2

- Fig.5: True and estimated ﬁnger ﬂexion for (upper plots) a global linear regression, (middle plots) switching decoder with true moving ﬁnger segmentation and (lower plots) with the switching decoder with an estimated moving ﬁnger segmentation.

Finally, we use our global method for obtaining the ﬁnger movement estimation. In other words, we used the switching models Hk to decode the signals with Equation (4) and the estimated sequence kˆ. The ﬁnger movement estimation can be seen on the lower plot of Figure 5b and the correlation measures are in Table 3c. As expected, the accuracy is lower than the one obtained with the true segmentation. However, we obtained an average correlation of 0.42 which is far better than when using a global regression approach. These predictions of the ﬁnger ﬂexions were presented in the BCI Competition and achieved the second place. Note that the last 3 ﬁngers have the lowest correlation. Those one are highly physically correlated and they are much more diﬃcult to discriminate than the two ﬁrst ones. The ﬁrst ﬁnger is by far the best estimated one as we obtained a correlation averaged accross subject of 0.56 .

- 4.4 Discussion and future works

The results presented in the previous section corresponds to the method used for the BCI Competition.

We ﬁrst note that the best performance obtained by Liang et al. [15] gives a correlation of about 0.46. Their method considers an amplitude modulation along time to cope with the abrupt change in the ﬁnger ﬂexions amplitude along time. Such an approach is somewhat similar to ours since they try to distinguish situations where ﬁngers are moving or not.

Then, we believe that our approach can be improved in several ways. Indeed, we choose to use linear models depending on the internal states,

but [10] proposed to use a kalman ﬁlter for the decoding of movement. This

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

Finger Sub. 1 Sub. 2 Sub. 3 Average

[Figure 102]

[Figure 103]

- 1 0.1821 0.2604 0.3994 0.2807

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

- 2 0.1844 0.2562 0.4247 0.2884

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

- 3 0.1828 0.2190 0.4607 0.2875

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

- 4 0.2710 0.4225 0.5479 0.4138

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

- 5 0.1505 0.2364 0.3765 0.2545 Avg. 0.1942 0.2789 0.4419 0.3050

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

(a) Linear regression

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

Finger Sub. 1 Sub. 2 Sub. 3 Average

[Figure 162]

[Figure 163]

- 1 0.8049 0.5021 0.8030 0.7033

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

- 2 0.7387 0.4638 0.7655 0.6560

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

- 3 0.7281 0.4811 0.7039 0.6377

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

- 4 0.7312 0.5366 0.6241 0.6307

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

- 5 0.2296 0.4631 0.6126 0.4351 Avg. 0.6465 0.4893 0.7018 0.6126 (b) Switching models (exact sequence)

[Figure 196]

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

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

Finger Sub. 1 Sub. 2 Sub. 3 Average

[Figure 222]

[Figure 223]

- 1 0.7016 0.3533 0.6457 0.5669

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

- 2 0.6129 0.3045 0.5097 0.4757

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

- 3 0.2774 0.0043 0.4025 0.2280

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

- 4 0.4576 0.2782 0.5920 0.4426

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

- 5 0.3597 0.2507 0.6553 0.4219 Avg. 0.4818 0.2382 0.5611 0.4270

[Figure 256]

[Figure 257]

[Figure 258]

[Figure 259]

[Figure 260]

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

(c) Switching models (est. sequence)

Table 3: Correlation between measured and estimated movement for a global linear regression (a), switching decoder with exact sequence (b) and switching decoder with an estimated sequence (c)

approach may be extended to using switching kalman ﬁlters in the switching model decoder.

Furthermore, our approach for estimating the sequence of hidden states can be highly improved. Liang [15] proposed to use Power Spectral Densities of the ECoG channel as features and we believe that these features may be added and used in the sequence labeling. In our method the features are low-pass ﬁltered in order to increase recognition performance, but other sequence labeling methods like HMM [11] have been used in BCI. Other sequence labeling methods like Conditional Random Fields [16] known to outperform HMM in some case or Sequence SVM [17] may be used to get a better sequence of hidden states.

Another interesting approach that may be investigated is the mixture of sources approach. Indeed, one may considered that each moving ﬁnger is associated to a source of ECoG signals. Then, the problem of identifying which ﬁnger is moving may boil down to a source separation problem.

- 5 Conclusions

In this paper, we present a method for the decoding ﬁnger ﬂexions from ECoG signals. The decoder is based on switching linear models. Our approach has been tested on a the BCI Competition IV Dataset 4 and achieved the second place in the competition. Results show that the switching model approach produce

better result than using a unique model. Furthermore an accurate ﬁnger ﬂexion estimation may be achieved when using an exact sequence of hidden states showing the interest of the switching models.

In future works, we plan to improve the result of the switching models decoder by two diﬀerent approaches. On the one hand, we can use more general models than linear ones for the movement prediction (switching kalman ﬁlters, nonlinear regression). On the other hand we can improve the sequence labeling along time with new approach and by using new features extracted from the ECoG signals.

References

- 1. Wolpaw, J.R., McFarland, D.J.: Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. Proceedings of the National Academy of Sciences of the United States of America 101(51) (December 2004) 17849–17854
- 2. Blankertz, B., Muller, K.R., Curio, G., Vaughan, T., Schalk, G., Wolpaw, J., Schlogl, A., Neuper, C., Pfurtscheller, G., Hinterberger, T., Schroder, M., Birbaumer, N.: The BCI competition 2003: progress and perspectives in detection and discrimination of EEG single trials. IEEE Transactions on Biomedical Engineering 51(6) (2004) 1044–1051
- 3. Sellers, E., Donchin, E.: A p300-based brain-computer interface: Initial tests by als patients. Clinical Neurophysiology 117(3) (2006) 538–548
- 4. Nijboer, F., Sellers, E., Mellinger, J., Jordan, M., Matuz, T., Furdea, A., Mochty, U., Krusienski, D., Vaughan, T., Wolpaw, J., Birbaumer, N., Kubler, A.: A braincomputer interface for people with amyotrophic lateral sclerosis. Clinical Neurophysiology 119(8) (2008) 1909–1916
- 5. E. Leuthardt, G.S., Wolpaw, J., Ojemann, J., Moran, D.: A brain-computer interface using electrocorticographic signals in humans. Journal of Neural Engineering 1 (2004) 63–71
- 6. Hill, N., Lal, T., Schroeder, M., Hinterberger, T., Wilhem, B., Nijboer, F., Mochty, U., Widman, G., Elger, C., Scholkoepf, B., Kuebler, A., Birbaumer, N.: Classifying eeg and ecog signals without subject training for fast bci implementation: Comparison of non-paralysed and completely paralysed subjects. IEEE Transactions on Neural Systems and Rehabilitation Engineering 14(2) (2006) 183–186
- 7. Hill, N., Lal, T., Tangermann, M., Hinterberger, T., Widman, G., Elger, Scholkoepf, B., Birbaumer, N.: Classifying Event-Related Desynchronization in EEG, ECoG and MEG signals. In: Toward Brain-Computer Interfacing. MIT Press (2007) 235–260
- 8. Shenoy, P., Miller, K., Ojemann, J., Rao, R.: Generalized features for electrocorticographic bci. IEEE Trans. On Biomedical Engineering 55 (2008) 273–280
- 9. Schalk, G., Kubanek, J., Miller, K.J., Anderson, N.R., Leuthardt, E.C., Ojemann, J.G., Limbrick, D., Moran, D., Gerhardt, L.A., Wolpaw, J.R.: Decoding twodimensional movement trajectories using electrocorticographic signals in humans. Journal of Neural Engineering 4(3) (2007) 264–275
- 10. Pistohl, T., Ball, T., Schulze-Bonhage, A., Aertsen, A., Mehring, C.: Prediction of arm movement trajectories from ecog-recordings in humans. Journal of Neuroscience Methods 167(1) (January 2008) 105–114

- 11. Darmanjian, S., Kim, S.P., Nechyba, M.C., Principe, J., Wessberg, J., Nicolelis, M.A.L.: Independently coupled hmm switching classiﬁer for a bimodel brainmachine interface. In: Machine Learning for Signal Processing, 2006. Proceedings of the 2006 16th IEEE Signal Processing Society Workshop on. (2006) 379–384
- 12. Miller, K.J., G.Shalk: Prediction of ﬁnger ﬂexion: 4th brain-computer interface data competition. BCI Competition IV (2008)
- 13. Schalk, G., McFarland, D., Hinterberger, T., Birbaumer, N., Wolpaw, J.: Bci2000: a general-purpose brain-computer interface (bci) system. Biomedical Engineering, IEEE Transactions on 51(6) (June 2004) 1034–1043
- 14. Rakotomamonjy, A.: Algorithms for multiple basis pursuit denoising. In: Workshop on Sparse Approximation. (2009)
- 15. Liang, N., Bougrain, L.: Decoding ﬁnger ﬂexion using amplitude modulation from band-speciﬁc ecog. In: European Symposium on Artiﬁcial Neural Networks ESANN. (2009)
- 16. Laﬀerty, J., A.McCallum, Pereira, F.: Conditional random ﬁelds: Probabilistic models for segmenting and labeling sequence data. In: Proc. 18th International Conf. on Machine Learning. (2001) 282–289
- 17. Bordes, A., Usunier, N., Bottou, L.: Sequence labelling svms trained in one pass. In Daelemans, W., Goethals, B., Morik, K., eds.: Machine Learning and Knowledge Discovery in Databases: ECML PKDD 2008. Lecture Notes in Computer Science, LNCS 5211, Springer (2008) 146–161

