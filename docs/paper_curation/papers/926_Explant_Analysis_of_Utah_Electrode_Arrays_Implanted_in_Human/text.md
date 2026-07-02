ORIGINAL RESEARCH

published: 07 December 2021 doi: 10.3389/fbioe.2021.759711

# Explant Analysis of Utah Electrode Arrays Implanted in Human Cortex for Brain-Computer-Interfaces

Kevin Woeppel1,2, Christopher Hughes1,2,3, Angelica J. Herrera1,2,3, James R. Eles1, Elizabeth C. Tyler-Kabara2,4, Robert A. Gaunt1,2,3,5, Jennifer L. Collinger1,2,3,5 and Xinyan Tracy Cui1,2*

1Department of Bioengineering, University of Pittsburgh, Pittsburgh, PA, United States, 2Center for the Neural Basis of Cognition, Pittsburgh, PA, United States, 3Rehab Neural Engineering Labs, Pittsburgh, PA, United States, 4Department of Neurosurgery, The University of Texas at Austin, Austin, TX, United States, 5Department of Physical Medicine and Rehabilitation, University of Pittsburgh, Pittsburgh, PA, United States

Edited by:

Valentina Castagnola, Italian Institute of Technology (IIT), Italy

Reviewed by:

Gaelle Piret, Institut National de la Santé et de la

Recherche Médicale (INSERM), France

Dan Wu, Zhejiang University of Technology,

China Stefano Carli,

University of Ferrara, Italy

*Correspondence: Xinyan Tracy Cui xic11@pitt.edu

Specialty section: This article was submitted to

Biomaterials, a section of the journal Frontiers in Bioengineering and

Biotechnology Received: 16 August 2021

Accepted: 29 October 2021 Published: 07 December 2021

Citation: Woeppel K, Hughes C, Herrera AJ,

Eles JR, Tyler-Kabara EC, Gaunt RA, Collinger JL and Cui XT (2021) Explant

Analysis of Utah Electrode Arrays Implanted in Human Cortex for Brain-

Computer-Interfaces. Front. Bioeng. Biotechnol. 9:759711. doi: 10.3389/fbioe.2021.759711

Brain-computer interfaces are being developed to restore movement for people living with paralysis due to injury or disease. Although the therapeutic potential is great, long-term stability of the interface is critical for widespread clinical implementation. While many factors can affect recording and stimulation performance including electrode material stability and host tissue reaction, these factors have not been investigated in human implants. In this clinical study, we sought to characterize the material integrity and biological tissue encapsulation via explant analysis in an effort to identify factors that inﬂuence electrophysiological performance. We examined a total of six Utah arrays explanted from two human participants involved in intracortical BCI studies. Two platinum (Pt) arrays were implanted for 980 days in one participant (P1) and two Pt and two iridium oxide (IrOx) arrays were implanted for 182 days in the second participant (P2). We observed that the recording quality followed a similar trend in all six arrays with an initial increase in peak-to-peak voltage during the ﬁrst 30–40 days and gradual decline thereafter in P1. Using optical and two-photon microscopy we observed a higher degree of tissue encapsulation on both arrays implanted for longer durations in participant P1. We then used scanning electron microscopy and energy dispersive X-ray spectroscopy to assess material degradation. All measures of material degradation for the Pt arrays were found to be more prominent in the participant with a longer implantation time. Two IrOx arrays were subjected to brief survey stimulations, and one of these arrays showed loss of iridium from most of the stimulated sites. Recording performance appeared to be unaffected by this loss of iridium, suggesting that the adhesion of IrOx coating may have been compromised by the stimulation, but the metal layer did not detach until or after array removal. In summary, both tissue encapsulation and material degradation were more pronounced in the arrays that were implanted for a longer duration. Additionally, these arrays also had lower signal amplitude and impedance. New biomaterial strategies that minimize ﬁbrotic encapsulation and enhance material stability should be developed to achieve high quality recording and stimulation for longer implantation periods.

Keywords: brain-computer interface, human participant, Utah array, neural electrical stimulation, neural electrode array, explant analysis

## 1 INTRODUCTION

Intracortical brain-computer interfaces (BCIs) can restore function for people affected by signiﬁcant paralysis by allowing the user to control an effector or assistive device with signals recorded in the brain. In recent years intracortical implants in motor cortex have been used for BCI control in primates and human participants with up to 10 degrees of freedom (Hochberg et al., 2006; Santhanam et al., 2006; Velliste et al., 2008; Collinger et al., 2013; Wodlinger et al., 2014; Bouton et al., 2016; Ajiboye et al., 2017). More recently, somatosensory feedback has also been added to these systems by stimulating through electrodes in the somatosensory cortex (Flesher et al., 2016; Armenta Salas et al., 2018; Fifer et al., 2020; Hughes et al., 2020; Flesher et al., 2021; Hughes et al., 2021). Given that intracortical BCIs require surgical implantation, they must be stable over many years to be clinically viable. This issue has been studied in both humans and primates, demonstrating that signals can be reliably recorded from electrodes in the motor cortex for over 6 years when devices do not fail, although there is considerable inter-subject variability and signals typically deteriorate over time (Suner et al., 2005; Chestek et al., 2011; Simeral et al., 2011; James et al., 2013; Downey et al., 2018; Bullard et al., 2020; Hughes et al., 2021).

Changes in recorded activity can be caused by many factors including movements of the electrodes relative to the brain, encapsulation of the electrode sites, as well as material degradation and failure (Prasad et al., 2014; Kozai et al., 2015; Woeppel et al., 2017). These factors can be broadly grouped into multiple failure categories, including material and biological failure (James et al., 2013).

Biological failures can occur as a result of the host tissue reactions to the implant. The traumatic nature of the implant leads to glial activation and encapsulation of the implant in a glial sheath (Polikov et al., 2005; Salatino et al., 2017). The glial sheath creates a physical barrier between the electrode and the neurons, while the extensive inﬂammation damages healthy neurons and may cause a neuron dead zone around the implant (Buzsáki, 2004; Schwartz et al., 2006). One recent study examining brain tissue from a human patient implanted with a Utah microelectrode array for 7 months found a substantial degree of tissue damage which correlated with decreased recording performance (Szymanski et al., 2021). In addition to central nervous system (CNS) reactions, the meninges can grow under the electrode. Meningeal encapsulation is highly collagenous and originates from non-CNS tissues. Substantial undergrowth of meningeal tissues can result in displacement of the electrode sites or complete ejection of the device from the CNS (Woolley et al., 2013). Subsequent device ejection is the most prevalent cause of chronic device failure in non-human primates, accounting for nearly 30% of chronic failure (Barrese et al., 2016; Dunlap et al., 2020). Longer experimental times increase the chance of meningeal undergrowth and eventual ejection of the recording device from the host tissues (Rousche and Normann, 1998; Barrese et al., 2016; Degenhart et al., 2016).

Material failures include metal corrosion, insulation cracking, and insulation delamination. These material failure modes often

increase in likelihood as time progresses. The parylene-C insulation commonly used for Utah style intracortical arrays can crack and delaminate, shunting current to the biological tissues (Schmidt et al., 1988; Prasad et al., 2014; Xie et al., 2014; Caldwell et al., 2020). The metal tips of Utah arrays, most commonly platinum or iridium oxide, are generally stable in vitro, but may be eroded away by aggressive stimulation (Negi et al., 2010) or the comparatively harsh in vivo environment (Negi et al., 2010). Furthermore, use of the electrodes for stimulation can impact the rate of tip degradation (Cogan, 2008; Gilgunn et al., 2013).

To establish stimulation limits for these clinical studies, experiments were performed in non-human primates and showed that frequent microstimulation over 6 months did not cause more loss of neurons around the electrode tips than insertion of the devices themselves and that stimulation had no behavioral effect for tasks that required tactile feedback (Chen et al., 2014; Kim et al., 2015). Using these established parameters, we would not expect stimulation to cause further damage to the brain tissue after implantation or have deleterious effects on behavior. In fact, stimulation over 5 years in a participant with these established parameters has not resulted in signiﬁcant differences in signal between stimulated and nonstimulated arrays and detection thresholds have improved over time (Hughes et al., 2021). However, to our knowledge there have been no post-implant examinations of the material properties of intracortical arrays implanted in humans. Here we examine the extent to which any material degradation occurred on explanted human intracortical electrodes, which will aid in the design and development of robust BCIs for long-term clinical use.

In this work, electrodes explanted from two human participants were examined to determine the extent of tissue encapsulation and material failure and to assess how these factors affected chronic recording performance. These electrodes were implanted for different lengths of time and were surgically explanted: 987 days for the two arrays in participant 1 (P1) and 182 days for the four arrays in participant 2 (P2). Both

- arrays in P1 and two of the arrays in the P2 had platinum (Pt) tips and were used for recording only, while the other two of the
- arrays in P2 had sputtered iridium oxide (IrOx) tips and were used for both stimulating and recording (Negi et al., 2010). First, the extent and nature of the tissue encapsulation of the arrays was investigated using optical microscopy and two-photon microscopy (TPM). Following this, the electrode arrays were examined with scanning electron microscopy (SEM) and energy-dispersive x-ray spectroscopy (EDS) to evaluate the extent of material damage. Finally, we compared the results of these analyses to endpoint recording performance of the devices and characterized the relationship between electrical stimulation and material degradation.

2 METHODS 2.1 Participants

These studies (NCT01894802 and NCT01364480) were conducted under Investigational Device Exemptions from the

|[Figure 1]<br><br>FIGURE 1 | Six electrode arrays were implanted in two participants: two recording arrays in P1 motor cortex, two recording arrays in P2 somatosensory cortex, and two stimulating arrays in P2 parietal cortex. Intraoperative images of implanted arrays in P1 (A) and P2 (B). The image taken in (A) is before implantation of the electrodes, and (B) is after implantation. Reference wires can also be seen in (A) near the arrays.|
|---|

U.S. Food and Drug administration and were approved by the Institutional Review Boards at the University of Pittsburgh (Pittsburgh, PA) and the Space and Naval Warfare Systems Center Paciﬁc (San Diego, CA). Informed consent was obtained before any study procedures were conducted. Two participants were implanted with microelectrode arrays in the brain. The ﬁrst subject (P1) was implanted with two intracortical

Pt microelectrode arrays (4 mm × 4 mm, Blackrock Microsystems, Salt Lake City, UT, United States) each with 96 wired electrode shanks (length 1.5 mm) in a 10 × 10 grid in the participant’s left motor cortex (Figure 1). The second subject (P2) was implanted with two Pt microelectrode arrays (Blackrock Microsystems, Salt Lake City, UT) in the left somatosensory cortex and two IrOx microelectrode arrays in the left parietal cortex. Each Pt array in the somatosensory cortex consisted of 88 wired electrodes in a 10 × 10 grid while each IrOx array in the parietal cortex consisted of 32 wired electrodes distributed throughout a 6 × 10 grid (Figure 1). Following implantation of the arrays into P2, it was discovered that the implant locations were posterior to the intended sites. Following which, the pedestals were removed, and a second implantation was performed 2 months later. This second set of implants are not within the scope of this study and are still implanted in the participant as of October 2021. A timeline for the arrays from implant to ﬁnal analysis can be found in Table 1.

2.2 Neural Recording and Signal Quality Metrics

Neural data were collected for both P1 and P2 using Neuroport Neural Signal Processors (Blackrock Microsystems, Salt Lake City, UT). At the beginning of each test session, a threshold for all channels was set at −5.25 (P1 before day 565) and −4.5 (all other test sessions) times the root-mean-square voltage. Data were collected across 287 sessions spanning 33 months for P1 and 40 sessions across 4 months for P2. No recordings were done for the ﬁnal 2 months of P2’s implant as the percutaneous pedestal connectors had been removed to prepare for the reimplant.

One of the main goals of the clinical study was to provide the participants with high degree-of-freedom control of a robotic arm. To accomplish this, participants performed a braincomputer interface calibration paradigm at the beginning of a test session. We used 3 min of data collected during this calibration procedure to run spike sorting analyses ofﬂine. The sorting method, described in detail in Downey et al. (2018) used principal component analysis (PCA) to separate units, deﬁned as threshold crossings from an individual electrode, based on the similarity of their waveform shape. Characteristics for each unit were then calculated. Peak-to-peak voltage (Vpp) was deﬁned as the voltage difference between the peak and the trough of the average waveform for each unit. Since there could be more than one unit identiﬁed per electrode, the unit with the maximum Vpp was chosen to represent the signal quality for the given electrode. Electrodes were considered to be viable if they contained waveforms with a minimum Vpp of 20 µV in P1 and 30 µV in P2 and a minimum ﬁring rate of 0.25 Hz. We chose these lower amplitude thresholds rather than being more conservative because lower amplitude multiunit recordings can still be used for decoding, although very low amplitude recordings may be more indicative of noise.

2.2.1 Impedances

Electrode impedances were measured for both participants using the NeuroPort patient cable data acquisition system (Blackrock

- TABLE 1 | Timeline of implantation, procedures, and explant analysis.

Electrode Length

Used for stimulation

Reason for explanation

Post explaint optical imaging

Fixation Staining Two photon microscopy

Enzymatic cleaning

SEM EDS

of implant

- P1 Medial and Lateral Recording arrays

987 days No Retraction of skin around pedestal

Immediately after explant (Figure 3)

Formalin, immediately after explant

Hoechst (cell nuclei), 20-min at 1: 1,000 22C

Yes following staining

Yes following TPM

Yes, environmental SEM then standards SEM (Figure 6)

Yes, last procedure performed

- P2 Medial and Lateral Recording Arrays

182 days No Undesired implant location

Immediately after explant (Supplementary Figure S1)

Formalin, 2 months after explant

None Yes, following staining

No Yes, standard SEM only (Figure 6)

Yes, last procedure performed

P2 Medial and Lateral Stimulating Arrays

182 days Yes, 7 times over ﬁrst 30 days

Undesired implant location

Immediately after explant (Supplementary Figure S1)

Formalin, 2 months after explant

None No No Yes, standard SEM only (Figure 6)

Yes, last procedure performed (Figure 7)

Microsystems, Salt Lake City, UT). For P1, impedances were measured at the beginning of a test session once a month. Impedances values for P2 were measured at the beginning of each test session. The system delivered a 1 kHz, 10 nA peak-topeak sinusoidal current to each implanted electrode for 1 s.

2.2.2 Intracortical Stimulation and Calculated Metrics

Seven test sessions across approximately 1 month involved microstimulation on the IrOx arrays. Stimulation was delivered using a CereStim R96 multichannel microstimulation system (Blackrock Microsystems, Salt Lake City, UT). Pulse trains consisted of cathodal phase ﬁrst, current-controlled, chargebalanced pulses delivered at frequencies from 20 to 300 Hz and at amplitudes from 1 to 100 μA. The cathodal phase was 200 μs long, the anodal phase was 400 μs long, and the anodal phase was set to half the amplitude of the cathodal phase. The phases were separated by a 100 μs interphase period. Stimulus pulse trains were varied in terms of amplitude, frequency, and train duration.

The voltage transients associated with each stimulus pulse were recorded using National Instruments data acquisition modules. Voltage traces were displayed in real time using LabView and saved to disk for analysis. Interphase voltage was measured as the voltage at the end of the interphase period immediately prior to the anodal phase for a given stimulation pulse. The total charge delivered to each electrode was calculated across all stimulation experiments using the charge delivered during the cathodal phase.

2.3 Explanted Array Handling Before Imaging

The two Pt arrays in P1 were explanted on day 987 post-implant and the four arrays in P2 were explanted on day 182. Following explantation, all arrays were removed from their wire bundles by clipping the wires proximal to the probe and were washed with saline. The P1 arrays were immediately ﬁxed in formalin and then

transferred to PBS bath for storage. Immunohistochemical staining procedure was performed on these two arrays with the goal of identifying neuron (NeuN) and microglia/ macrophage (Iba-1). The staining process involves incubation of the arrays with primary antibodies solutions overnight, with secondary antibodies for 4 h followed by Hoescht solution for 20 min for nuclei staining. The antibody staining was unsuccessful, and only nuclei stain was used for the tissue analysis. The P2 arrays were ﬁxed 2 months post-implant, and one of the Pt arrays had visible tissue encapsulation and was imaged using TPM. Because these arrays were not immediately ﬁxed, we did not perform immunostaining, and only characterized the collagen structure, which can be stable without the ﬁxation.

After optical and TPM imaging, two arrays explanted from P1 were sent to the FDA for initial analysis. The arrays were initially imaged with an environmental SEM, then enzymatically cleaned with Asepti-Zyme neutral pH enzymatic instrument presoak/ cleaner (4 ml in 250 ml saline) at 37°C for 90 min, followed by Getinge Clean Enzymatic detergent (1 ml in 250 ml saline) at 37°C for 90 min, and then by MetriZyme detergent (1 ml in 250 ml saline) 37°C for 90 min. Samples were then thoroughly washed with water and air dried, ready for SEM imaging. This process was effective at removing some of the tissue and revealing the electrode tip/shank for material analysis. Arrays from P2 did not undergo the enzymatic cleaning procedure. All arrays were stored adhered to copper tape, tips up.

2.4 Electrode Imaging

Explanted electrodes were ﬁrst characterized by optical and twophoton microscopy to assess the degree of tissue encapsulation. For TPM, we used a two-photon laser scanning microscope with a Bruker scan head (Prairie Technologies, Madison, WI), TI: sapphire laser tuned to 920 nm (Mai Tai DS; Spectra-Physics, Menlo Park, CA), light collection through non-descanned photomultiplier tubes (Hamamatsu Photonics KK, Hamamatsu, Shizuoka, Japan), and a 10x or 16x, 0.8

numerical aperture water immersion objective (Nikon Inc., Milville, NY). Laser power was maintained between 20 and 40 mW. For each electrode tip, Z-stacks were collected with ﬁlters to resolve second harmonic generation (SHG) at half the laser wavelength (∼460 nm), which enabled intrinsic imaging of collagen-I representing the meningeal encapsulation. Images along the length of the electrode shanks were collected as Z-stacks. Z-stack images were either collected at speciﬁc regions of interest, or in a grid at all locations across the face of the electrode array. Grid images were automated by the Prairie software with a 10% overlap between images. All image stitching and subsequent image processing was conducted with ImageJ software (NIH). Electrode integrity was characterized by scanning electron microscopy (SEM) and energy-dispersive x-ray spectroscopy (EDS). Samples were washed, dried under alcohol, and sputter-coated with 4 nm Au/Pd. Images were taken by JSM 6335F electron microscope. EDS was taken by Zeiss Sigma 500VP, excluding Au and Pd from quantiﬁcation.

Using the SEM and optical images, a qualitative category of “non-degraded/unencapsulated” or “degraded/encapsulated” was assigned to each electrode based on the degree of damage to the tip or shank, or the level of encapsulation around the electrode. Arrays explanted from P1 were more extensively cleaned prior to imaging, and the encapsulation score was based on optical images of the explanted arrays. Encapsulation on arrays from P2 was determined by examining the SEM images. Degraded electrode tips were deﬁned as having obvious and substantial surface defects in the metal coating, including pitting of the metal, ﬂaking of the metal, and exposure of the underlying silicon. Degraded shanks were deﬁned relative to the parylene insulation, with defects including insulation cracking along the shank, peeling of the insulation away from the shank near the tip, and other obvious defects in or below the insulation. These categories were compared to EDS images, conﬁrming the presence/absence of metalation at the tip (Pt/IrOx). Electrodes which could not be quantiﬁed, due to breakage during removal or gross encapsulation, were assigned a null score and excluded from analysis.

- 2.5 Statistics Changes in signal and impedances over time were assessed using linear regression. For impedances, data were log-transformed because data did not follow a linear trend. For P2 impedances and Vpp, we excluded data prior to day 30 for regression because the impedances measured in this range were highly variable.

Total charge delivered, minimum interphase voltages, and charge delivered after exceeding an interphase voltage of −0.6 V were compared between the two electrode arrays that had received stimulation using Mann-Whitney tests. We used a non-parametric test because the data was determined to not be normally distributed using an Anderson-Darling test. We used a Fisher exact test to determine if there was a signiﬁcant relationship between an electrode’s material properties (undamaged or damaged) and the length of implantation (Pt arrays in P1 vs. P2) or if it received stimulation (P2 IrOx arrays, yes or no). We further quantiﬁed if there was a relationship between both total charge injected and charge injected with

interphase voltages below −0.6 V on stimulated electrodes and their material properties (undamaged or damaged) using logistic regression. Electrode categories were compared to impedances and Vpp using Mann-Whitney tests. We used a non-parametric test because the variances between groups were not the same.

3 RESULTS

- 3.1 Signal Amplitude and Impedances

Decreased Over Time

Changes in the impedances and peak-to-peak voltages over time were observed on implanted electrodes in both participants (Figure 2). Impedances decreased over time on electrodes implanted in P1 (p < 0.001, log-transformed linear regression, Figure 2A). For P2, the starting impedances of IrOx electrodes were lower than the platinum electrodes, which is consistent with the manufacturer’s speciﬁcation (Negi et al., 2010). From day 1–20 we observed an increase in impedances. The initial increase in impedance reversed after 1 month (30 days), and a signiﬁcant downward trend in impedances was observed until the end of recording for both the IrOx (p < 0.001, linear regression) and platinum arrays (p < 0.001, linear regression). Impedances gathered from P1 eventually stabilized after approximately 2 years. The difference between the ﬁnal impedance values recorded in P1 and P2 can be explained by the difference in length of implantation. Previous studies have determined that impedance values of stimulated and non-stimulated intracortical electrodes decrease dramatically over the ﬁrst couple of years after implantation in humans (Hughes et al., 2021) and monkeys (Suner et al., 2005; Chestek et al., 2011). Since P2 was implanted for a signiﬁcantly shorter period, we would expect the electrode impedance values to be larger and more variable, which the data supports.

In the same manner as the impedance measurements, an initial increase in Vpp was observed for both P1 and P2. However, after an increase in the ﬁrst 30 days, the measured Vpp from P1 and P2 exhibited a downward trend (p < 0.001, linear regression, Figures 2C,D). The rates of decrease in the Vpp between day 30 and 120 for P1 and P2 were −4.0 μV/month and −4.86 μV/month, respectively. Median Vpp decreased by 52% across 550 days in P1 and by 14% across 90 days in P2. The median Vpp for P1 leveled off at approximately 25–30 µV.

Comparing across patients, the platinum arrays performed similarly over the ﬁrst months of implantation. Impedances of the Pt arrays in both P1 and P2 were both initially higher than the IrOx arrays (Figure 2E). Recorded unit amplitudes were similar across all arrays regardless of material or patient (Figure 2F).

- 3.2 Encapsulating Tissues Were Apparent

on Multiple Arrays

Based on the gross optical micrographs, both P1 arrays had a signiﬁcant degree of adherent tissue on the electrode base and shanks. The nature of the encapsulating tissue was examined with TPM, measuring the second harmonic signal characteristic of collagen. For the more heavily encapsulated P1 arrays, the

|[Figure 2]<br><br>FIGURE 2 | Impedances and peak-to-peak voltages decreased over time. Data points represent the median across electrodes for a given test date. The shaded regions show the interquartile ranges smoothed with a nine-point moving average ﬁlter with a triangular kernel. Median impedances recorded on (A) P1 electrodes and (B) P2 electrodes across the length of implant. Impedance measurements on P1 were not conducted with the same temporal resolution as P2. Different colors represent platinum or IrOx for P2 as indicated in the legend. Vpp recorded on (C) P1 electrodes and (D) P2 electrodes across the length of implant. For P1, there was a discontinuity in the Vpp at day post-implant 550 due to a change in the RMS threshold from −5.25 to −4.5. Overlayed impedances and Vpp for P1 and P2 are shown in (E) and (F), respectively.|
|---|

encapsulation sheet was found both along the shanks of the array (Figures 3A–D) and at the base (Figures 3E–H). The lateral array (Figure 3A) exhibited strong second-harmonic signal within the tissue sheet conﬁrmed that it was primarily composed of collagen-I ﬁbers (Figures 3C,D). After further examining the indicated electrodes and staining for cell nuclei, we observed that the encapsulation was highly cellularized (Figures 3C,D). In addition, the encapsulation continued down the shank of the electrode, with cellular and collagenous material detected along the shanks and tips of the array. Upon examining the medial array (Figure 3E), we observed that the encapsulation was not homogenous, instead exhibiting greater second harmonic signals nearer to the edges (Figure 3G) while having greater cell density nearer the center (Figure 3H). SHG imaging is also a good tool for detecting blood vessels because of the strong presence of collagen in the vessel wall, however we did not observe clear blood vessel structure in the P1 explants.

We examined relationship between the preimplant location of the medial Pt array of P2 (Figure 4A) and the tissue present on

the explanted array. For the medial Pt array in P2, the encapsulation tissue covers the whole array (Figure 4B; Supplementary Figure S1) and the TPM imaging from the side revealed signiﬁcant tissue covering the majority of the electrode tips (Figure 4C). Here, we identiﬁed clear vascular architecture in the encapsulation tissue with SHG imaging (Figure 4D, highlighted in blue). The blood vessel in the encapsulation tissue was traced and super-imposed to the image of pial vasculature observed pre-implantation (Figure 4E). As can be seen in Figure 4F, the blood vessel traces match the pia vasculature. This indicates that the blood vessels observed to be at the tip of this array were pial blood vessels. Two mechanisms may lead to this: 1) the array did not fully penetrate the pia at the time of implantation; 2) the array was successfully implanted in the brain parenchyma and the pia membrane was pulled out with the array. Since we were able to obtain high Vpp recordings from this array in the region coinciding with the vasculature (Figure 2D), the ﬁrst potential mechanism was ruled out. Therefore, we conclude that not all the

|[Figure 3]<br><br>FIGURE 3 | Characterization of the encapsulation of the electrodes. Arrays were imaged with an optical microscope in air. Both arrays are from P1. The encapsulation of the lateral array (A) was further examined with TPM. (B) The location of 2P imaging along the Z axis and select electrode shanks. The array was stained for cell nuclei and zoomed-in images were taken of the green (C) and red (D) regions. In both regions there is prominent second harmonic signal, indicating the presence of collagen. The medial array in (E) was chosen to display the lack of homogeneity of the encapsulating tissues. (F) Location along the z-axis (blue box) and two selected areas further imaged. 3D rotation images were generated displaying the tissue encapsulation and nuclei staining from the regions highlighted in green (G) or red (H). The outer image (G) displays high second harmonic signal while the inner image (H) has elevated cell counts, demonstrating the heterogeneity of the encapsulation.|
|---|

tissue present on the device is ﬁbrotic scar in nature, and that at least some of the tissue on this explant is pia membrane that was pulled out with the device.

- 3.3 Length of Implantation Impacts the Degree of Material Degradation and Fibrous

Encapsulation

Based on the optical and SEM images, electrodes were assigned a binary score for the tip, shank, and degree of ﬁbrous encapsulation (Figure 5) The electrode scores and images are shown in Figure 6, and summary data for each group are displayed in Table 2, excluding electrodes which were not wired or used for recording or stimulation. Electrodes that appeared to be broken or damaged by implantation/ explantation were excluded from analysis. Tips and shanks were evaluated separately to examine the effects of both tip metallization and electrode insulation on device performance. Differences in the total number of electrodes receiving a tip category, shank category, and encapsulation are due to damage to the electrodes or excess encapsulation preventing the assignment of a proper.

Categories assigned to P1 and P2 platinum arrays were compared to identify any potential changes in material deterioration or encapsulation which may be attributed to the length of implantation (Table 3). We found that both measures of material degradation (tip and shank damage) were more prominent for longer implantation times (27.8% tip damage

for P1 and 11.1% for P2, 15.2% shank damage for P1 and 1.8% for P2, p < 0.001 for both). We also found that the degree of encapsulation is more signiﬁcant for longer implants with 72.4% for the P1 arrays and 50% for the P2 arrays (p < 0.001).

3.4 Stimulation Resulted in Electrode Damage on One Stimulating Array but Not the Other

Two IrOx arrays implanted in P2 received a low amount of total charge (<160 µC per electrode site). Each of the two stimulated IrOx arrays had 60 electrodes, half of which were electrically connected and used for stimulation. Preimplant optical images of the arrays did not show any variation between arrays. The stimulated electrode sites are arranged primarily in a checkerboard fashion. SEM shows that the lateral array had a high degree of tip and shank degradation (Figure 7A). Interestingly, tips and shanks showing visible damage appeared to coincide with the electrodes that were used for stimulation. Furthermore, EDS revealed that stimulated tips had lower iridium counts than non-stimulated tips as illustrated by the lower intensity of the magenta coloring (Figure 7B). The loss of metallization for the lateral stimulating array occurred predominantly on the electrodes used for stimulation. The medial array did not show this pattern (Figure 7C). The damage scores for each electrode tip and shank are summarized in Figures 7D,E. The checkerboard

|[Figure 4]<br><br>FIGURE 4 | Brain vascularization can be visualized on the medial Pt array from P2. The pre-implant location is indicated with a yellow box (A). (B) Optical image of the array showing tissue coverage. (C) TPM of the shanks of the electrode, with green denoting second harmonic signal from collagen and red denoting the autoﬂuorescence of the device. Each electrode was imaged and separated by row (side view). Most of the electrode tips are covered by collagenous tissue. (D) TPM image of the array looking from the tips downward, with a portion of vasculature marked in blue as determined by SHG imaging. (E) zoomed in image from (A) where electrode shanks are superimposed on the underlying vasculature. (F) The vasculature visualized in (D) is superimposed on (E), showing similar trajectory, demonstrating that the vasculature structure identiﬁed in the tissue on the explanted array is likely of pial origin.|
|---|

pattern of damages of the lateral array is clearly seen, which correspond very well with arrangement of the stimulation electrodes. The medial stimulating array has overall much less observable material damage but more tissue encapsulation. Of the 62 electrodes used for stimulation on both arrays, 56 were analyzed, of which 23 had notable tip degradation, 21 of which were located on the lateral electrode array. Metal loss, and the corresponding decrease in iridium signal, was not observed on any non-stimulated electrodes. These results are summarized in Table 4.

Delivered charge and measured interphase voltages were compared to the material degradation. The amount of stimulation provided was quantiﬁed by both the total charge delivered and number of pulses delivered. Although the mean amount of charge injected on the lateral array was greater, it was not signiﬁcantly different than the mean charge injected on the medial array (Mann-Whitney test, p 0.22). The medial array contained the three electrodes with the most charge delivered, none of which displayed observable material degradation. However, we examined the minimum voltage during the interphase period (Figure 7F) and found that the lateral array electrodes experienced higher voltage excursions on average than the medial array electrodes (mean minimum voltage was −1.7 V for the lateral, and −1.1 V for the medial array). Furthermore,

there was a signiﬁcant relationship between the total charge injected at voltages more negative than −0.6 V (Figure 7G) and the tip score (p 0.025, crit-p 0.034, logistic regression) and shank category (p 0.023, crit-p 0.034, logistic regression) on the lateral stimulating array. There was no relationship between total charge injected at voltages less than −0.6 V and tip category (p 0.60, logistic regression) or shank category (p 1, logistic regression) on the medial array (Figure 7H). We found no signiﬁcant differences in recording quality (Vpp) (Figure 7I) between the damaged and non-damaged electrodes on the two stimulation arrays, after excluding the encapsulated electrodes.

## 4 DISCUSSION

In order for BCIs to become a viable therapy, the longevity of the devices and mechanisms of failure must be well understood. Effective electrode design requires knowledge of the stability of the materials in the harsh in vivo environment and the effects of gradually accumulating damage to the device. However, the relationships between chronic material degradation and device performance are poorly understood. The effects of material degradation on performance in human subjects is further complicated by the limited number of human subjects and the

|[Figure 5]<br><br>FIGURE 5 | Tip and shank damage occurred on some implanted electrodes and encapsulation occurred on four implanted arrays. Representative high magniﬁcation images of undamaged/unencapsulated and damaged/encapsulated electrodes. Tip images were taken from P1 array 1, with the degraded tip showing demetallation and biologic fouling (scale bar is 10 µm). Shank images were taken from P2 lateral stimulating array (scale bar is 100 µm). The degraded shank shows multiple surface and subsurface irregularities including pitting and delamination from the tip. Encapsulation images were from P2 medial stimulating array (scale bar is 100 µm). Pre implant optical images are provided to display pristine electrodes.|
|---|

even smaller amount of explanted human BCI arrays. In this work, the in vivo performance of human neural electrode arrays was compared to the material integrity after explantation. We have found signs of material degradation on all electrode arrays, with longer implantation times correlating with an increased number of degraded electrodes (Table 3). Additionally, biological tissue encapsulation on the explanted device was also documented as another potential factor to inﬂuence recording quality. The biological encapsulation tissues were highly collagenous and also highly cellularized, and appear to form in a time dependent manner, increasing with the length of implantation. A similar form of tissue response has been observed in a post mortem analysis of tissue surrounding a

MEA implanted for 7 months (Szymanski et al., 2021). Further, the nature of the encapsulation at the periphery of the array and the center is different. Together, these results suggest that the encapsulation originated from the meninges, as opposed to the CNS.

4.1 Encapsulation and Material Degradation Were Both Related to the Length of Implantation

Material and biological failure modes are most common on longer time scales (James et al., 2013), and it was expected that material degradation and collagenous encapsulation would increase with longer implant times. Indeed, we observed that the arrays implanted in P1 exhibited greater degrees of material degradation and encapsulation than those in P2 which were implanted for a much shorter length. We also observed a characteristic decline in recording performance and impedances with longer implantation times.

Impedance measurements are often used to determine the integrity of electrodes, while also serving as a method of investigating the interface between the electrode and the host tissues (Thakore et al., 2012; Lago et al., 2016). Previously, we have reported that in rats, complete ﬁbrous encapsulation of the electrode resulted in lower 1 kHz impedance compared to partial encapsulation (Cody et al., 2018). Complex impedance spectra analysis performed in the aforementioned study revealed unique features in the Nyquist plot that corresponds to an extracellular resistance component, which is smaller in the fully encapsulated device than the partially encapsulated device. This may be counterintuitive initially, but can be explained by a few mechanisms. First, the composition of the encapsulation tissue is high in collagen and less resistive than highly cellular and myelin rich brain tissue. Secondly, if the ﬁbrotic growth at the base pushes the array up, a liquid ﬁlled gap will be formed between cone shaped shanks and the tract, creating a less resistive current path. Due to the limitation in our instrumentation in this study, impedance data were only obtained at 1 kHz preventing us from measuring complex impedances, but it is plausible that a similar effect may have occurred here. Full spectrum impedance recording in future studies could dissect the contributions from tissue encapsulation and material changes and determine whether the same factors are relevant here. However, such measurement needs to meet the regulatory requirements associated with clinical studies.

The decreases in impedance over time could also be a result of degradation of the electrode tips and shank insulation which leads to increased electrochemical surface area. Interestingly, we found no relationships between the impedance of the electrode at 1 kHz and the Vpp during recording for Pt arrays (Supplementary Figure S2). This is not surprising as impedance is only a measure of the electrochemical properties of the electrode and the electrode/tissue interface and does not account for biological variables such as distance from the electrode to the neuron or health of the host tissues, which are more relevant to Vpp. Impedance has previously been shown to be an unreliable

|[Figure 6]<br><br>FIGURE 6 | Categories assigned to each electrode site. (A) Each site was assigned a category with respect to their material integrity or degree of encapsulation. Black sites were not able to be categorized and were excluded from the analysis. Encapsulation was determined by examining the optical images of the arrays for P1 and SEM images for P2. This is due to the enzymatic digestion of the encapsulating tissues that was performed prior to SEM imaging for P1. (B,C) Recording arrays implanted into P1 after enzymatic treatment. (D) Medial stimulating array implanted into P2. (E,F) Medial and lateral recording arrays implanted into P2. (G) Lateral stimulating array implanted into P2. (H,I) Higher magniﬁcation images of recording array in (F) and stimulating arrays in (G), respectively. White arrows indicate electrodes which were used for stimulation. Red arrows indicate representative electrodes which were excluded from analysis.|
|---|

- TABLE 2 | Number of electrically connected electrodes that were classiﬁed as undamaged/unencapsulated or damaged/encapsulated based on tip degradation, shank degradation, and tissue encapsulation.

Tip degradation Shank degradation Encapsulation Low (%) High (%) Low (%) High (%) Low (%) High (%)

- P1 Medial 77 (83.7) 15 (16.3) 84 (91.3) 8 (8.7) 41 (43.6) 53 (56.4)

- P1 Lateral 45 (58.4) 32 (41.6) 67 (79.8) 17 (20.2) 10 (11.0) 81 (89.0)
- P2 Pt Medial 59 (81.9) 13 (18.1) 82 (96.5) 3 (3.5) 0 (0) 88 (100)

- P2 Pt Lateral 85 (96.6) 3 (3.4) 88 (100) 0 (0) 88 (100) 0 (0) P2 IrOx Medial 26 (92.9) 2 (7.1) 32 (100) 0 (0) 6 (18.8) 26 (81.2) P2 IrOx Lateral 7 (25) 21 (75) 9 (32.1) 19 (67.9) 30 (100) 0 (0) Excluded 45 21 7

- TABLE 3 | Differences observed between patients with different length of implant (980 days for P1 and 182 days for P2) on material degradation and encapsulation for electrically connected platinum recording electrode arrays.

caused material damage on the lateral array but not the medial array is unclear. While the speciﬁc reason for this cannot be determined, impedances were lower on the medial array (Supplementary Figure S3). The decrease in impedance then could have resulted in lower amplitude voltage excursions during stimulation, decreasing the likelihood of material damage. Indeed, we found that the lateral array had more negative interphase voltages (mean −1.7 V) when compared to the medial array (mean −1.1 V).

P1 (%) P2 Pt (%) Fisher exact p value

Degraded Tips 27.8 11.1 <0.001 Degraded Shank 15.2 1.8 <0.001 Encapsulated 72.4 50 <0.001

More material damage was found on the lateral stimulating array in P2 which experienced higher cathodic interphase voltage amplitude. The interphase voltage is analogous to the maximum cathodic electrode potential (Emc) measured during charge injection limit (CIL) experiments performed in vitro. Emc with values more negative than −0.6 V (vs. Ag/AgCl) are often considered to be unsafe due to irreversible water hydrolysis occurring at the electrode which could cause hydrogen gas production and pH increases (Cogan et al., 2005). Such reactions could lead to delamination of the IrOx coating even with a small number of pulses. We do not expect the median interphase voltage to be directly comparable to in vitro CIL measurements due to the two-electrode setup and increased variables introduced from the biological environment, but we expect the general relationship between voltage and interfacial reactions to hold. Besides the fact that lateral array experienced higher voltage excursion on average, we found a signiﬁcant correlation between the charge injected below −0.6 V and damage on the lateral stimulating array (Figure 7H). These results indicate that stimulation, beyond a certain voltage threshold, may damage electrodes in a dose (charge) dependent manner.

predictor of recording performance in rodents and non-human primates (Jiang et al., 2014; Cody et al., 2018). Another important material factor that likely contribute to the uniform reduction of impedance on all arrays is the silicone hermetic sealing failure above the arrays from the wire bundle to the pedestal, which should be characterized in future studies.

The observed collagenous encapsulation of the arrays has been observed in rodent and non-human primate studies (James et al., 2013; Degenhart et al., 2016; Cody et al., 2018). Encapsulation of the electrode tip region can isolate the electrode from nearby neurons, resulting in a lowered Vpp. In addition, the collagenous material grown at the base of the array platform can lift the electrode up and away from the original target neurons, also resulting in Vpp decrease (Degenhart et al., 2016; Cody et al., 2018). Both tissue growth at the tips and the base have been observed from the explanted devices which may contribute to the degradation of Vpp over time in human subjects.

- 4.2 Stimulation at More Negative Voltages May Drive Material Damage Under Certain

Partial and complete loss of SIROF from Utah arrays upon continuous stimulation has been reported in previous in vitro studies (Negi et al., 2010), but the stimulation doses in these previous studies applied were much higher (7 h of continuous stimulation above 60 nC). One potential explanation is that the stimulation on the lateral array only weakened the adhesion of the IrOx coating and the coating was stripped from the electrode during or after explantation. Alternatively, variations could also be a result of batch-to-batch difference in fabrication where the lateral array received poorly adhered IrOx coating. Notably, the electrodes damaged by stimulation performed just as well in recording as the undamaged electrodes. This interesting result

Circumstances

The stimulation parameters used in this study were based on studies from non-human primates showing that these parameters had no additional effects on cortical tissue apart from implanting the devices themselves, had no behavioral effect on the animal, and had limited effects on the electrode tissue interface (Chen et al., 2014; Kim et al., 2015). Here, we found that electrical stimulation induced damage on one of the two devices. On the lateral array, de-metallization was visible under SEM and detected by EDS on the stimulated electrodes, indicating that stimulation was the cause of the metal loss. The reason that stimulation

|[Figure 7]<br><br>FIGURE 7 | Stimulation-induced material damage on one of the two arrays. (A) SEM image of four shanks of the lateral array, tip damages are found on the stimulated electrodes marked with white arrows. (B) EDS of the stimulating electrodes for the lateral array showing reduced presence of iridium (magenta) on most of the stimulated sites (white arrows). (C) SEM image of the medial stimulating array tips. No differences were observed between the non-stimulated and stimulated tips on this array. Scale bars are 100 µm. (D,E) Arrays showing the measured material properties on the stimulation arrays including tip categories (D) and shank categories (E). Green spaces show electrodes categorized as undamaged/unencapsulated, blue spaces show electrodes categorized as damaged, and black spaces show electrodes that were excluded from analysis. (F,G). Medial (top) and lateral (bottom) stimulating arrays showing (F) minimum interphase voltage (G) and total charge injected below −0.6 V. The color bar for the minimum interphase voltages is log-transformed to emphasize differences between electrodes. Grey spaces indicate unwired electrodes. White spaces indicate wired electrodes that were never stimulated. (H) Logistic regression for charge injected over −0.6 V and damage to tips (left) or shanks (right). (I) Measured peak-to-peak voltages on stimulated electrodes after removing electrodes which were encapsulated with ﬁbrous tissues. There were no signiﬁcant differences observed in the measured unit amplitudes (MannWhitney non-parametric test).|
|---|

indicates that despite the IrOx delamination and insulation cracking, the electrode is capable of recording neural signal. While electrodes receiving stimulation have previously been shown to be able to record signal for up to 1,500 days (Hughes et al., 2021), whether this recording capability is

maintained over periods of time greater than this remains to be investigated.

The biocompatibility of IrOx coatings has been widely studied and validated for stimulation and recording applications (Lee et al., 2002; Cogan et al., 2005; Cogan 2008; Negi et al., 2010; Negi

- TABLE 4 | Effect of stimulation on material degradation and encapsulation for IrOx arrays. Non-stimulated tips were not electrically connected. Stimulated (%) Non-stimulated (%) χ2 statistic p value

Damaged tips 41.1 5.6 14.7 <0.001 Damaged shank 33.3 0.0 19.3 <0.001 High encapsulation 43.3 39.7 0.1 >0.05

et al., 2010; Hughes et al., 2021). In another of our studies, stimulating electrodes for over 5 years in a human participant did not result in worse signal recordings when compared to recording electrodes (Hughes et al., 2021). Furthermore, the ability to evoke sensation on stimulated electrodes only improved over time. Based on our observations here, this could be because 1) the material damage caused by stimulation is idiosyncratic, and stimulation didn’t result in damage on the arrays of this 5years study or 2) material damage caused by stimulation had no effect on the electrode’s ability to record or stimulate. Discerning between the two is difﬁcult, as studying the in vivo properties of the electrodes in parallel with the material properties is not possible in humans. Analysis will need to be conducted on these arrays that received much higher levels of stimulation after explant. Additionally, further animal studies using the stimulus parameters used in our study and assessing damage and changes in recording over time could provide insight here.

4.3 Implications for Future Intracortical Electrode Arrays

Overall, our results show that both material integrity and recording performance of human intracortical electrodes decrease over time. Degradation was observed on both the electrode tips and the shank insulation. We have also observed different degrees of tissue encapsulation both at the array base, middle of the shank, and the tips of the arrays. Since we do not have real time data of these material and tissue changes, and explant analysis only provides a partial picture at the end point, we cannot accurately correlate material and biological factors to recording outcome. Multiple human studies have demonstrated that intracortical electrode recordings can enable brain-computer interface control of computer cursor and robotic arms for years after implant, (Bullard et al., 2020) yet the observations in the current study support the need for strategies for increasing material durability and decreasing ﬁbrous encapsulation in order to further improve human BCI recording quality and longevity. Additionally, on one implanted array, we observed clear iridium loss as a result of stimulation, which correlated to more charge injected at more negative voltages. Further research on improving metal adhesion and developing real time electrode potential monitoring methods during stimulation may eliminate such incidences.

## DATA AVAILABILITY STATEMENT

The raw data supporting the conclusion of this article will be made available by the authors, without undue reservation.

## ETHICS STATEMENT

The studies involving human participants were reviewed and conducted under Investigational Device Exemptions from the Food and Drug Administration and were and approved by Institutional Review Boards at the University of Pittsburgh Space and the Naval Warfare Systems Center Paciﬁc. The participants provided their written informed consent to participate in this study.

## AUTHOR CONTRIBUTIONS

All authors provided signiﬁcant intellectual contribution to the manuscript. KW performed the SEM imaging, elemental analysis, writing, and data analysis for Sections 3.2–3.4. CH and AH were involved in the ephys data acquisition, writing, and data analysis for Sections 3.1, 3.4, JE performed the two photon imaging and analysis, ET performed the surgical procedures on the human participants. RG led the stimulation experiments, JC led the recording study and XC led the explant analysis. All authors have edited, revised and proofread the manuscript.

## FUNDING

The recording and stimulation study was partly funded by the Defense Advanced Research Projects Agency’s (Arlington, VA, United States) Revolutionizing Prosthetics program (contract number N66001-10-C-4056). The views expressed herein are those of the authors and do not represent the ofﬁcial policy or position of the Department of Defense or US Government. The explant materials and tissue analysis were supported by the National Institutes of Health grant R01NS110564, R01NS062109 and R01NS089688

## ACKNOWLEDGMENTS

We thank the participants for their dedication to this study. We thank Pavel Takmakov of the Food and Drug Adminstration for the initial discussion and cleaning protocols for SEM.

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fbioe.2021.759711/ full#supplementary-material

## REFERENCES

Ajiboye, A. B., Willett, F. R., Young, D. R., Memberg, W. D., Murphy, B. A., Miller, J. P., et al. (2017). Restoration of Reaching and Grasping Movements through Brain-Controlled Muscle Stimulation in a Person with Tetraplegia: a Proof-OfConcept Demonstration. The Lancet 389, 1821–1830. doi:10.1016/S01406736(17)30601-3

Armenta Salas, M., Bashford, L., Kellis, S., Jafari, M., Jo, H., Kramer, D., et al.

(2018). Proprioceptive and Cutaneous Sensations in Humans Elicited by Intracortical Microstimulation. eLife 7, e32904. doi:10.7554/eLife.32904

Barrese, J. C., Aceros, J., and Donoghue, J. P. (2016). Scanning Electron Microscopy of Chronically Implanted Intracortical Microelectrode Arrays in Non-human Primates. J. Neural Eng. 13, 026003. doi:10.1088/17412560/13/2/026003

Bouton, C. E., Shaikhouni, A., Annetta, N. V., Bockbrader, M. A., Friedenberg, D. A., Nielson, D. M., et al. (2016). Restoring Cortical Control of Functional Movement in a Human with Quadriplegia. Nature 533, 247–250. doi:10.1038/ nature17435

Bullard, A. J., Hutchison, B. C., Lee, J., Chestek, C. A., and Patil, P. G. (2020). Estimating Risk for Future Intracranial, Fully Implanted, Modular Neuroprosthetic Systems: A Systematic Review of Hardware Complications in Clinical Deep Brain Stimulation and Experimental Human Intracortical Arrays. Neuromodulation: Techn. Neural Interf. 23, 411–426. doi:10.1111/ner.13069

Buzsáki, G. (2004). Large-scale Recording of Neuronal Ensembles. Nat. Neurosci. 7, 446–451. doi:10.1038/nn1233

Caldwell, R., Street, M. G., Sharma, R., Takmakov, P., Baker, B., and Rieth, L. (2020). Characterization of Parylene-C Degradation Mechanisms: In Vitro Reactive Accelerated Aging Model Compared to Multiyear In Vivo Implantation. Biomaterials 232, 119731. doi:10.1016/j.biomaterials.2019.119731

Chen, K. H., Dammann, J. F., Boback, J. L., Tenore, F. V., Otto, K. J., Gaunt, R. A., et al. (2014). The Effect of Chronic Intracortical Microstimulation on the Electrode-Tissue Interface. J. Neural Eng. 11, 026004. doi:10.1088/1741-2560/ 11/2/026004

Chestek, C. A., Gilja, V., Nuyujukian, P., Foster, J. D., Fan, J. M., Kaufman, M. T., et al. (2011). Long-term Stability of Neural Prosthetic Control Signals from Silicon Cortical Arrays in Rhesus Macaque Motor Cortex. J. Neural Eng. 8, 045005. doi:10.1088/1741-2560/8/4/045005

Cody, P. A., Eles, J. R., Lagenaur, C. F., Kozai, T. D. Y., and Cui, X. T. (2018). Unique Electrophysiological and Impedance Signatures between Encapsulation Types: An Analysis of Biological Utah Array Failure and Beneﬁt of a Biomimetic Coating in a Rat Model. Biomaterials 161, 117–128. doi:10.1016/j.biomaterials.2018.01.025

Cogan, S. F. (2008). Neural Stimulation and Recording Electrodes. Annu. Rev. Biomed. Eng. 10, 275–309. doi:10.1146/annurev.bioeng.10.061807.160518

Cogan, S. F., Troyk, P. R., Ehrlich, J., and Plante, T. D. (2005). In Vitro comparison of the Charge-Injection Limits of Activated Iridium Oxide (AIROF) and Platinum-Iridium Microelectrodes. IEEE Trans. Biomed. Eng. 52, 1612–1614. doi:10.1109/TBME.2005.851503

Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber, D. J., et al. (2013). High-performance Neuroprosthetic Control by an Individual with Tetraplegia. The Lancet 381, 557–564. doi:10.1016/S01406736(12)61816-9

Degenhart, A. D., Eles, J., Dum, R., Mischel, J. L., Smalianchuk, I., Endler, B., et al. (2016). Histological Evaluation of a Chronically-Implanted Electrocorticographic Electrode Grid in a Non-human Primate. J. Neural Eng. 13, 046019. doi:10.1088/1741-2560/13/4/046019

Downey, J. E., Schwed, N., Chase, S. M., Schwartz, A. B., and Collinger, J. L. (2018). Intracortical Recording Stability in Human Brain-Computer Interface Users. J. Neural Eng. 15, 046016. doi:10.1088/1741-2552/aab7a0

Dunlap, C. F., Colachis, S. C., Meyers, E. C., Bockbrader, M. A., and Friedenberg, D. A. (2020). Classifying Intracortical Brain-Machine Interface Signal Disruptions Based on System Performance and Applicable Compensatory Strategies: A Review. Front. Neurorobot. 14, 558987. doi:10.3389/fnbot.2020.558987

Fifer, M. S., McMullen, D. P., Thomas, T. M., Osborn, L. E., Nickl, R. W., Candrea, D. N., et al. (2020). Intracortical Microstimulation Elicits Human Fingertip Sensations. medRxiv 05, 20117374. doi:10.1101/2020.05.29.20117374

Flesher, S. N., Collinger, J. L., Foldes, S. T., Weiss, J. M., Downey, J. E., TylerKabara, E. C., et al. (2016). Intracortical Microstimulation of Human Somatosensory Cortex. Sci. Transl Med. 8, 361ra141. doi:10.1126/ scitranslmed.aaf8083

Flesher, S. N., Downey, J. E., Weiss, J. M., Hughes, C. L., Herrera, A. J., TylerKabara, E. C., et al. (2021). A Brain-Computer Interface that Evokes Tactile Sensations Improves Robotic Arm Control. Science 372, 831–836. doi:10.1126/ science.abd0380

Gilgunn, P. J., Ong, X. C., Flesher, S. N., Schwartz, A. B., and Gaunt, R. A. (2013). “Structural Analysis of Explanted Microelectrode Arrays,” in 2013 6th International IEEE/EMBS Conference on Neural Engineering (NER), November 6–8, 2014. doi:10.1109/NER.2013.6696035

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., et al. (2006). Neuronal Ensemble Control of Prosthetic Devices by a Human with Tetraplegia. Nature 442, 164–171. doi:10.1038/nature04970

Hughes, C., Herrera, A., Gaunt, R., and Collinger, J. (2020). “Bidirectional BrainComputer Interfaces,” in Handbook of Clinical Neurology (Oxford, UK: Elsevier), 168, 163–181. doi:10.1016/b978-0-444-63934-9.00013-5

Hughes, C. L., Flesher, S. N., Weiss, J. M., Downey, J. E., Boninger, M., Collinger, J. L., et al. (2021). Neural Stimulation and Recording Performance in Human Sensorimotor Cortex over 1500 Days. J. Neural Eng. 18 (4), 045012. doi:10.1088/1741-2552/ac18ad

James, C. B., Naveen, R., Kaivon, P., Corey, T., Carlos, V.-I., Lachlan, F., et al. (2013). Failure Mode Analysis of Silicon-Based Intracortical Microelectrode Arrays in Non-human Primates. J. Neural Eng. 10, 066014. doi:10.1088/17412560/13/2/026003

Jiang, J., Willett, F. R., and Taylor, D. M. (2014). “Relationship Between Microelectrode Array Impedance and Chronic Recording Quality of Single Units and Local Field Potentials,” in 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, August 26–30, 2014. doi:10.1109/EMBC.2014.6944265

Kim, S., Callier, T., Tabot, G. A., Gaunt, R. A., Tenore, F. V., and Bensmaia, S. J. (2015). Behavioral Assessment of Sensitivity to Intracortical Microstimulation of Primate Somatosensory Cortex. Proc. Natl. Acad. Sci. USA 112, 15202–15207. doi:10.1073/pnas.1509265112

Kozai, T. D. Y., Catt, K., Li, X., Gugel, Z. V., Olafsson, V. T., Vazquez, A. L., et al. (2015). Mechanical Failure Modes of Chronically Implanted Planar SiliconBased Neural Probes for Laminar Recording. Biomaterials 37, 25–39. doi:10.1016/j.biomaterials.2014.10.040

Lago, N., Cester, A., Wrachien, N., Natali, M., Quiroga, S. D., Bonetti, S., et al.

(2016). A Physical-Based Equivalent Circuit Model for an Organic/electrolyte Interface. Org. Electro. 35, 176–185. doi:10.1016/j.orgel.2016.05.018

Lee, I., Whang, C.-N., Choi, K., Choo, M.-S., and Lee, Y.-H. (2002). Characterization of Iridium Film as a Stimulating Neural Electrode. Biomaterials 23, 2375–2380. doi:10.1016/S0142-9612(01)00373-8

Negi, S., Bhandari, R., Rieth, L., and Solzbacher, F. (2010). In Vitro comparison of Sputtered Iridium Oxide and Platinum-Coated Neural Implantable Microelectrode Arrays. Biomed. Mater. 5, 015007. doi:10.1088/1748-6041/5/ 1/015007

Negi, S., Bhandari, R., Rieth, L., Van Wagenen, R., and Solzbacher, F. (2010). Neural Electrode Degradation from Continuous Electrical Stimulation: Comparison of Sputtered and Activated Iridium Oxide. J. Neurosci. Methods 186, 8–17. doi:10.1016/j.jneumeth.2009.10.016

Polikov, V. S., Tresco, P. A., and Reichert, W. M. (2005). Response of Brain Tissue to Chronically Implanted Neural Electrodes. J. Neurosci. Methods 148, 1–18. doi:10.1016/j.jneumeth.2005.08.015

Prasad, A., Xue, Q.-S., Dieme, R., Sankar, V., Mayrand, R. C., Nishida, T., et al.

(2014). Abiotic-biotic Characterization of Pt/Ir Microelectrode Arrays in Chronic Implants. Front. Neuroeng. 7, 2. doi:10.3389/fneng.2014.00002

Rousche, P. J., and Normann, R. A. (1998). Chronic Recording Capability of the Utah Intracortical Electrode Array in Cat Sensory Cortex. J. Neurosci. Methods 82, 1–15. doi:10.1016/S0165-0270(98)00031-4

Salatino, J. W., Ludwig, K. A., Kozai, T. D. Y., and Purcell, E. K. (2017). Glial Responses to Implanted Electrodes in the Brain. Nat. Biomed. Eng. 1, 862–877. doi:10.1038/s41551-017-0154-1

Santhanam, G., Ryu, S. I., Yu, B. M., Afshar, A., and Shenoy, K. V. (2006). A HighPerformance Brain-Computer Interface. Nature 442, 195–198. doi:10.1038/ nature04968

Schmidt, E. M., McIntosh, J. S., and Bak, M. J. (1988). Long-term Implants of Parylene-C Coated Microelectrodes. Med. Biol. Eng. Comput. 26, 96–101. doi:10.1007/BF02441836

Schwartz, A. B., Cui, X. T., Weber, D. J., and Moran, D. W. (2006). BrainControlled Interfaces: Movement Restoration with Neural Prosthetics. Neuron 52, 205–220. doi:10.1016/j.neuron.2006.09.019

Simeral, J. D., Kim, S.-P., Black, M. J., Donoghue, J. P., and Hochberg, L. R. (2011). Neural Control of Cursor Trajectory and Click by a Human with Tetraplegia 1000 Days after Implant of an Intracortical Microelectrode Array. J. Neural Eng. 8, 025027. doi:10.1088/1741-2560/8/2/025027

Suner, S., Fellows, M. R., Vargas-Irwin, C., Nakata, G. K., and Donoghue, J. P. (2005). Reliability of Signals from a Chronically Implanted, Silicon-Based Electrode Array in Non-human Primate Primary Motor Cortex. IEEE Trans. Neural Syst. Rehabil. Eng. 13, 524–541. doi:10.1109/TNSRE.2005.857687

Szymanski, L. J., Kellis, S., Liu, C. Y., Jones, K. T., Andersen, R. A., Commins, D., et al. (2021). Neuropathological Effects of Chronically Implanted, Intracortical Microelectrodes in a Tetraplegic Patient. J. Neural Eng. 18, 0460b9. doi:10.1088/ 1741-2552/ac127e

Thakore, V., Molnar, P., and Hickman, J. J. (2012). An Optimization-Based Study of Equivalent Circuit Models for Representing Recordings at the NeuronElectrode Interface. IEEE Trans. Biomed. Eng. 59, 2338–2347. doi:10.1109/ TBME.2012.2203820

Velliste, M., Perel, S., Spalding, M. C., Whitford, A. S., and Schwartz, A. B. (2008). Cortical Control of a Prosthetic Arm for Self-Feeding. Nature 453, 1098–1101. doi:10.1038/nature06996

Wodlinger, B., Downey, J. E., Tyler-Kabara, E. C., Schwartz, A. B., Boninger, M. L., and Collinger, J. L. (2014). Ten-dimensional Anthropomorphic Arm Control in a Human Brain−machine Interface: Difﬁculties, Solutions, and Limitations. J. Neural Eng. 12, 016011. doi:10.1088/1741-2560/12/1/016011

Woeppel, K., Yang, Q., and Cui, X. T. (2017). Recent Advances in Neural Electrode-Tissue Interfaces. Curr. Opin. Biomed. Eng. 4, 21–31. doi:10.1016/ j.cobme.2017.09.003

Woolley, A. J., Desai, H. A., and Otto, K. J. (2013). Chronic Intracortical Microelectrode Arrays Induce Non-uniform, Depth-Related Tissue Responses. J. Neural Eng. 10, 026007. doi:10.1088/1741-2560/10/2/026007 Xie, X., Rieth, L., Williams, L., Negi, S., Bhandari, R., Caldwell, R., et al. (2014). Long-term Reliability of Al2O3 and Parylene C Bilayer Encapsulated Utah Electrode Array Based Neural Interfaces for Chronic Implantation. J. Neural Eng. 11, 026016. doi:10.1088/17412560/11/2/026016

Conﬂict of Interest: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their afﬁliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2021 Woeppel, Hughes, Herrera, Eles, Tyler-Kabara, Gaunt, Collinger and Cui. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

