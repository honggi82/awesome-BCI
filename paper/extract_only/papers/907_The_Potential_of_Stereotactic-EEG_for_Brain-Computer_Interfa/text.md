MINI REVIEW published: 27 February 2020 doi: 10.3389/fnins.2020.00123

[Figure 1]

# The Potential of Stereotactic-EEG for Brain-Computer Interfaces: Current Progress and Future Directions

Christian Herff1*, Dean J. Krusienski2 and Pieter Kubben3

- 1 Department of Neurosurgery, School of Mental Health and Neurosciences, Maastricht University, Maastricht, Netherlands,
- 2 ASPEN Lab, Biomedical Engineering Department, Virginia Commonwealth University, Richmond, VA, United States,
- 3 Department of Neurosurgery, Maastricht University Medical Center, Maastricht, Netherlands

Stereotactic electroencephalogaphy (sEEG) utilizes localized, penetrating depth electrodes to measure electrophysiological brain activity. It is most commonly used in the identiﬁcation of epileptogenic zones in cases of refractory epilepsy. The implanted electrodes generally provide a sparse sampling of a unique set of brain regions including deeper brain structures such as hippocampus, amygdala and insula that cannot be captured by superﬁcial measurement modalities such as electrocorticography (ECoG). Despite the overlapping clinical application and recent progress in decoding of ECoG for Brain-Computer Interfaces (BCIs), sEEG has thus far received comparatively little attention for BCI decoding. Additionally, the success of the related deep-brain stimulation (DBS) implants bodes well for the potential for chronic sEEG applications. This article provides an overview of sEEG technology, BCI-related research, and prospective future directions of sEEG for long-term BCI applications.

Edited by: Alessandro Vato,

Italian Institute of Technology (IIT), Italy Reviewed by: Disha Gupta, Langone Medical Center, New York University, United States Juan Álvaro Gallego, Northwestern University, United States *Correspondence:

Keywords: electrocorticography, ECoG, brain-computer interface, BCI, stereotactic EEG, depth electrodes, intracranial, iEEG

## 1. INTRODUCTION

Christian Herff c.herff@maastrichtuniversity.nl

Brain-Computer Interfaces (BCIs, Wolpaw et al., 2002) have rapidly advanced in recent years, employing a wide variety of communication and control paradigms (Huggins et al., 2017). Notably, BCIs based on electrocorticography (ECoG, Schalk and Leuthardt, 2011) have demonstrated reliable decoding of a number of cortical processes. Compared to surface electroencephalography (EEG), the superior decoding results of ECoG can be attributed to its millimeter-spatial and millisecond-temporal resolution (Parvizi and Kastner, 2018). Furthermore, ECoG is unaﬀected by movement artifacts and allows for the measurement of higher-frequency activity, such as the high gamma-band (>70 Hz), as it is unﬁltered by dura, skull and scalp tissues. The high-gamma band might correlate with ensemble spiking (Ray et al., 2008) and contain very localized information for a variety of motor (Miller et al., 2007) (including smiling Kern et al., 2019) and speech tasks (Crone et al., 2001; Leuthardt et al., 2012).

Specialty section: This article was submitted to

Neuroprosthetics, a section of the journal

Frontiers in Neuroscience Received: 05 July 2019 Accepted: 30 January 2020 Published: 27 February 2020

Citation: Herff C, Krusienski DJ and Kubben P

ECoG is routinely utilized for monitoring of medication-resistant epilepsy in which the electrodes are implanted for the localization of the seizure origin. The procedure involves a craniotomy to place strips or grids of electrodes directly on the cortex. The electrodes generally remain implanted for a period of one to two weeks during which the brain signals are recorded and monitored to localize the seizure origin. The ECoG electrodes are also used for functional mapping of the eloquent cortex via electrical cortical stimulation (Arya et al., 2018). In addition

(2020) The Potential of Stereotactic-EEG for Brain-Computer

Interfaces: Current Progress and Future Directions. Front. Neurosci. 14:123. doi: 10.3389/fnins.2020.00123

to epilepsy procedures, ECoG can also be collected intraoperatively during awake craniotomies for brain tumor resection surgeries.

Patients undergoing these procedures are recruited to voluntarily participate in neuroscientiﬁc research and, more recently, BCI research. These investigations have allowed for tremendous advances both in the understanding of cortical processes as well as BCI technology. However, as ECoG electrodes are typically placed over speciﬁc, localized regions of the cortex based on the clinical needs of the patients, broad coverage is generally not achieved. Furthermore, ECoG only provides access to the cortical surface and not key deeper structures such as the hippocampus, insula, Herschl’s gyrus and basal ganglia.

Another method for intracranial seizure localization employs penetrating depth electrodes that are implanted through small burr holes in the skull. These electrodes are positioned using stereotactic guidance, thus the modality is referred to as stereotactic EEG (sEEG). sEEG allows for the measurement of neural activity in deeper structures of the brain. The cortical sampling of sEEG is generally much sparser than ECoG, leading to regular combined implantation of sEEG and ECoG in the same patient. However, it is believed that sEEG alone leads to fewer surgical complications than the craniotomies required for ECoG (Iida and Otsubo, 2017). As in ECoG, the usage in epilepsy monitoring opens a window to conduct neuroscientiﬁc or BCI research with these intracranial recordings without putting any additional burden on the patient. In fact, many patients welcome participation in the experiments as a diversion from the tedium of waiting in the hospital room for the occurrence of a spontaneous seizure. While sEEG is being increasingly utilized for neuroscientiﬁc research, it has received relatively little attention for BCI research. This article provides an overview of sEEG technology, BCI-related research, and prospective future directions of sEEG for long-term BCI applications.

## 2. STEREOTACTIC EEG

The implantation of depth electrodes guided by a stereotactic frame is called stereotactic/stereo electroencephalography (sEEG) and was ﬁrst developed by Talairach and Bancaud in Paris in the late 1950s (Bancaud, 1959; Talairach and Bancaud, 1966). The procedure has become a common practice to identify epileptogenic zones in refactory elipepsy (Chassoux et al., 2018). After the patient has been identiﬁed as a candidate for invasive recordings, the epileptologist and neurosurgeon plan the trajectory of typically 5–15 cylindrical sEEG electrode shafts containing 8–18 contacts, each. Typical contacts are made from platinum/iridium, have a length of roughly 2 mm, a diameter of 1 mm and a resulting total surface area of 10 mm2 (suppliers include e.g., Dixi Medical, Beçanson, France and Ad-tech Medical, Oak Creek, U.S.A.). The typical inter-electrode distance is roughly 1.5–3.5 mm (van der Loo et al., 2017), which generally provides localized sampling of sparse brain regions. This can result in a total of hundreds of distinct recording sites across the brain, allowing for simultaneous recording within

and across various brain structures. Less sEEG electrodes are usually implanted when sEEG is used in combination with ECoG. Figure 1 shows an example of the implantation of 8 sEEG electrode shafts.

sEEG electrodes are generally preferred over ECoG grids when the lateralization of the seizures is unknown or is expected to be in deeper brain structures, such as insula or hippocampus (Parvizi and Kastner, 2018). This preference results in regular targeting of limbic structures including the medial temporal, orbitofrontal, cingulate, and insular regions. As the electrode positioning along the trajectory spans from the skull to these deeper areas, cortical regions can also be captured. This sampling of very diﬀerent areas along one electrode shaft results in special requirements for electrode referencing (Li et al., 2018). Figure 1 shows an example of a typical sEEG implantation. Red electrodes are planned (Figure 1A) to target the hippocampus and a heterotopia in the right hemisphere. Other trajectories are mainly targeting a heterotopia. Electrodes positioned along the trajectory of the planned surgical target (Figure 1B) can also capture other brain regions which can be eﬀective for BCI applications. For example, the blue electrode trajectory is proximal to the primary motor cortex. Such coverage highlights one of the major diﬀerences between sEEG and ECoG. While ECoG provides higher density coverage over a limited cortical region (typically unilateral), sEEG provides sparser coverage spanning more, bilateral brain regions including deeper structures. As with ECoG, because the targeted areas for the electrode implants are solely determined based on clinical needs, BCI investigations in sEEG must be designed to accommodate the patient-speciﬁc montages.

Because the clinical intent is to capture epileptic activity, sampling rates between 1 and 3 kHz are commonly used, giving a temporal resolution in the sub-millisecond range. In addition to the standard frequency ranges investigated in surface EEG, namely delta (1–3 Hz), theta (4–7 Hz), alpha (8–12 Hz), beta (13– 20 Hz), and gamma (21–50 Hz), sEEG allows the measurement of the high gamma band (> 70 Hz), which is highly attenuated by skull and scalp in surface EEG recordings. The high-gamma band activity has been shown to be highly correlated with taskrelated signals (Miller et al., 2007) and ensemble spiking of cells in the close proximity of the electrode contact (Ray et al., 2008). The high-gamma band is also known to be strongly correlated to the BOLD signal (Logothetis et al., 2001; Mukamel et al., 2005). In addition to the access to the high-gamma band, sEEG also provides higher signal amplitude (about ten times higher) and a resulting increase in Signal-Noise-Ratio up to 100 times higher (Ball et al., 2009) compared to scalp EEG. Additionally, sEEG provides very localized information, with superior spatial resolution compared to surface EEG (Parvizi and Kastner, 2018). Estimates place the number of cells measurable by an individual contact at ~500,000 (Miller et al., 2009). Artifacts such as electrocardiogram, movement artifacts and skin potentials are also signiﬁcantly attenuated or even absent in sEEG recordings. While surface EEG recordings can degrade over time and show large inter-session variability due to impedance issues, intracranial recordings appear to be much more stable over extended periods of time (Chao et al., 2010).

|[Figure 2]<br><br>FIGURE 1 | (A) Trajectory planning for 8 sEEG electrode shafts. (B) Computer Tomography showing implanted electrode shaft locations. (C) Implanted electrode shafts. sEEG requires only small, localized burr holes compared to the comparatively large craniotomies required for ECoG implants.|
|---|

These advantages of sEEG combined with the relative low risk proﬁle (Cardinale et al., 2012; Hader et al., 2013; Mullin et al., 2016) associated with the small burr holes (diameter of 1.2 mm) as opposed to the full craniotomy necessary for ECoG, make sEEG a desirable modality for electrophysiological investigations. The leads employed in sEEG and the associated surgery are akin to those used for Deep Brain Stimulation (DBS) procedures, which is widely-used as a treatment for tremors, dystonia and Parkinson’s Disease, with more recent application to obsessive-compulsive disorder (Greenberg et al., 2006), Tourette’s syndrome (Martinez-Ramirez et al., 2018), and epilepsy (Pycroft et al., 2018). While DBS electrodes are primarily

used for electric stimulation of the brain, the demonstrated longterm eﬃcacy of chronic DBS electrodes suggests the possibility of chronic sEEG for BCI applications.

## 3. DECODING SEEG SIGNALS FOR BCI

Signiﬁcant BCI advances have been achieved with other intracranial (Schalk and Leuthardt, 2011) and intracortical (Bensmaia and Miller, 2014) recording modalities. Penetrating microarrays implanted on the cortex have achieved robust control of commercial tablets (Nuyujukian et al., 2018), robotic

arms (Hochberg et al., 2006, 2012) and even allowed paralyzed patients to regain control of their own arms using functional electric stimulation (Ajiboye et al., 2017). ECoG arrays implanted over the cortex have achieved remarkable results in a wide variety of BCI tasks. See Schalk and Leuthardt (2011) for a review. While it is unlikely that the standard sparse sEEG implants will exhibit superior decoding performance to microarrays and ECoG for the aforementioned applications, sEEG recordings can be used in isolation or to uniquely complement these cortical recording modalities to access information from multiple subcortical regions. Speciﬁc regions of interest for BCI that cannot be accessed with other modalities are the limbic system and insula for memory, emotion, place cells, etc. and deeper brain regions such as the basal ganglia and subthalamic nucleus that might help to further deﬁne motor decoding. sEEG also has the unique potential to simultaneously target multiple brain networks, bilaterally. Initial investigations in the decoding of mental processes highlight the potential for targeting unique, bilateral combinations of cortical and deeper brain structures. In the following sections, we will highlight decoding results achieved with sEEG.

- 3.1. Motor BCI A number of studies have demonstrated decoding of motor signals for BCI using sEEG. Vadera et al. (2013) demonstrate two-dimensional cursor control from depth electrodes implanted in hand and foot cortical areas. While imagined movements were not investigated, this study highlights one of the advantages of sEEG - the opportunity to record foot cortical areas that reside in the longitudinal ﬁssure that cannot be attained with surface measurements.

Another study (Li et al., 2017b) investigates the control of a prosthetic hand using sEEG electrodes in the central sulcus. The investigators were able to decode three diﬀerent hand gestures and a resting state with good accuracies. Another robotic upper limb prosthetic employed a hybrid BCI using ECoG and sEEG, eye tracking and computer vision in two patients (McMullen et al., 2014). Two recent studies investigated the decoding of grip strength for potential use in hand prosthesis. In Murphy et al.

- (2016), the investigators decoded the grip strength of imagined and executed grip movements from subsurface sEEG electrodes in the central sulcus and the insular cortex and conclude that “depth electrodes could be useful tools for investigating the functions of deeper brain structures as well as showing that central sulcus and insular cortex may contain neural signals that could be used for control of a grasp force BMI.” Fischer et al.
- (2017) also showed that beta and gamma activity in the STN is modulated depending on the level of imagined grip force. Their study is based on electrodes implanted for DBS in the treatment of Parkinson’s disease.

- 3.2. Visual Speller BCI Studies have successfully decoded diﬀerent visual-evoked potentials from sEEG recordings. In Krusienski and Shih (2011) depth electrodes in and adjacent to the hippocampus were used to successfully operate a visual speller using the P300 response. With decoding accuracies at or near 100% using less

than 15 visual stimulations, achieved results were similar to those achieved with ECoG (Krusienski and Shih, 2011). This performance can be attributed to the existence of the P300 in the hippocampus (McCarthy et al., 1989) and that several of the posterior electrodes were bordering the occipital lobe. Additionally, the same group showed that similar performance could also be achieved using electrodes that were located in the lateral ventricle (Shih and Krusienski, 2012). By employing a motion-onset VEP (Kuba et al., 2007) and sEEG electrodes in middle temporal regions, Li et al. (2017a) showed that up to 14 characters per minute could be typed.

- 3.3. Speech BCI Another type of BCI that has rapidly developed are interfaces that aim to restore the ability to speak (Herﬀ and Schultz, 2016; Schultz et al., 2017). Studies have shown that it is possible to decode ECoG activity into text (Herﬀ et al., 2015; Moses et al., 2016, 2019) and speech output (Herﬀ et al., 2016; Angrick et al., 2019; Anumanchipalli et al., 2019). Using depth electrodes, Chrabaszcz et al. (2019) showed that STN is also active during speech production. Two recent advances showed that decoding of speech perception from depth electrodes is also possible. In Akbari et al. (2019) perceived speech was decoded from sEEG electrodes in auditory cortex into an audible waveform. In this approach, sEEG electrodes even yielded slightly better results than ECoG recordings. In Han et al. (2019), the authors decoded the attended speaker for intelligent hearing aids. In this study, one participant was implanted with bilateral temporal depth electrodes covering left and right auditory cortex. The goal of this line of research it to be able to increase intelligibility of attended speaker for smart hearing aids.
- 3.4. Navigational BCI The discovery of place and grid cells in the hippocampus (Maguire et al., 1998; Moser et al., 2008) has greatly advanced our understanding of human spatial navigation. As sEEG electrodes can sample from the hippocampus and epilepsy monitoring often requires electrodes in the hippocampus, an unparalleled opportunity to decode navigational parameters from sEEG activity arises. Several diﬀerent aspects of navigation have been decoded from sEEG electrodes in the hippocampus. Aghajan et al. (2017) used neural networks to decode movement speed. Another study (Vass et al., 2016) showed successful decoding of teleportation distance from hippocampus, highlighting that location is well-represented in these recordings. Watrous et al.

(2018) extended these ﬁndings by showing that even the navigational goal can be decoded from single united activity recorded from microelectrodes at the tip of sEEG electrodes.

- 3.5. Passive BCI Instead of directly controlling computers, the idea of passive BCIs (Zander and Kothe, 2011) is to adapt interfaces to a user’s mental state such as stress, workload, drowsiness, or emotion, which the user may or may not be consciously aware of. As sEEG targets deeper brain structures including limbic regions such as the amygdala, it is well-suited to detect and decode brain activity associated with such user states. Alasfour et al. (2019)

demonstrated the classiﬁcation of abstract naturalistic behavioral contexts from ECoG and sEEG recordings, which could be used to adapt interfaces to the coarse behavioral context of users in the future. Sani et al. (2018) showed that mood variations during natural behavior can be decoded from intracranial recordings (including sEEG). Their classiﬁers relied mostly on electrodes in limbic regions. These ﬁndings could one day help in the development of closed-loop systems to treat neuropsychiatric disorders. Yamin et al. (2017) investigate online neurofeedback in depth electrodes with a virtual reality interface. Their preliminary results show that users were able to reliably downregulate their amygdala activity.

Another aspect of cognition that could be useful for passive BCI is the encoding and retrieval of memory that could for example inform an interface which information needs to be presented again. Initial investigations highlight the feasibility of decoding aspects of memory from sEEG recordings (Song et al., 2016, 2017). Hampson et al. (2018) extended these ﬁndings and demonstrated that the typical activity pattern during successful memory encoding could also be used in stimulation to increase memory performance.

## 4. FUTURE DIRECTIONS

Despite the impressive results achieved in decoding of mental processes from sEEG recordings, there are still numerous practical issues that must be addressed before sEEG BCIs can be considered for long-term, clinical applications. Figure 2 shows the standard processing pipeline of an sEEG-based BCI. At each

individual stage of this pipeline there are unique challenges and opportunities for achieving a practical BCI.

For data acquisition, current clinical sEEG implants can be modiﬁed in a multitude of ways to improve the spatial resolution and target sampling. By maintaining the same shaft size, the contact size and density can be reduced to be able to record local ﬁeld potentials along the entire length of the shaft (Pothof et al., 2016). Additionally, microwires can be placed at the tip of the shaft for recording single-units (Pothof et al., 2016). Such modiﬁcations are expected to yield signiﬁcant improvements in BCI decoding performance as observed when using micro-ECoG in comparison to standard clinical ECoG (Slutzky et al., 2010; Wang et al., 2013; Kellis et al., 2016; Muller et al., 2016). Furthermore, the sEEG shafts can be designed to have custom electrode placement or directional electrodes (Tinkhauser et al., 2018) to strategically target multiple brain locations or networks using a single shaft and trajectory planning. Such sampling of multiple brain networks, including cortical and subcortical targets, would signiﬁcantly increase the decoding potential for many complex functions such as language and memory. Since sEEG is well-suited for bilateral implantation, there is signiﬁcant potential for investigating network coordination across hemispheres. Leveraging the clinical success of DBS based on electrical stimulation, there is also the possibility of developing bidirectional BCIs using sEEG (Wander and Rao, 2014). Additionally, the long term stability of sEEG recordings needs to be investigated. While studies show that ECoG grids provide reliable long-term measurements (Vansteensel et al., 2016; Pels et al., 2019), similar evidence for sEEG is currently lacking.

|[Figure 3]<br><br>FIGURE 2 | Envisioned pipeline for sEEG BCI. Each of the involved stages poses open challenges before successful dissemination to patients. Example applications include (from left to right) robotic arm control, memory prosthesis, wheelchair control, and speller interfaces.|
|---|

While DBS devices present fully implanted solutions, sEEG measurements still rely on externalized leads connected to bulky ampliﬁers. For realistic BCI applications, a fully implanted solution should be targeted placing new requirements on (wireless) ampliﬁers. Advances from other types of neural implants might be harnessed for these data acquisition challenges (Eftekhar et al., 2010; Liu et al., 2017).

The sparse sampling of sEEG across diﬀerent brain regions requires speciﬁc signal processing, as well as feature extraction. For example, while high-gamma has been the focus of many intracranial BCI studies and are also found in e.g., hippocampus (Colgin and Moser, 2010), other frequency ranges such as theta might be better suited for decoding activity (Stavisky et al., 2015) from deeper structures (Buzsáki, 2002). Furthermore, sEEG provides an excellent opportunity to explore more global phenomena such as traveling waves (Nunez and Srinivasan, 2006; Muller et al., 2018), connectivity (Van Mierlo et al., 2013), and frequency-coupling (Maris et al., 2011).

In addition to the common applications mentioned in Figure 2, sEEG provides a unique opportunity to enhance existing or develop new applications by harnessing brain activity from limbic and memory-related brain activity. For instance, this information could conceivably be used to convey emotion or aﬀect in a speech neuroprosthetic. As with other measurement modalities, diﬀerent requirements for the decoding procedures will arise depending on the envisioned application (Borton et al., 2013; Bensmaia and Miller, 2014).

Overall, sEEG exhibits several unique advantages of other intracranial monitoring methods. In addition to the capability of sampling subcortical regions, sEEG implantation is a less traumatic procedure that exhibits a lower risk of infection. Since the hardware and procedures for sEEG and DBS implantation are eﬀectively identical, the success and precedent established by DBS suggests that sEEG could also be chronically implanted for BCIs. Ultimately, the BCI ﬁeld needs to further develop and

test new sEEG electrode/shaft designs and develop paradigms that exploit sEEG’s unique capability of recording from multiple cortical and subcortical targets. It is also prudent to explore sEEG in conjunction with microarrays and ECoG to evaluate whether the addition of subcortical targets and networks can further reﬁne the decoding performance and capabilities of these alreadysuccessful approaches. It is feasible that future BCIs will require a hybrid of cortical (Microarrays and ECoG) and subcortical (sEEG) sampling on the path to achieving fully-transparent and natural operation.

## 5. CONCLUSION

In this review article, we brieﬂy introduced sEEG and compared its characteristics with ECoG, another intracranial measurement modality. We reviewed initial decoding work using sEEG and highlighted further potential and future directions of BCI research using sEEG.

We believe that sEEG holds great potential for BCI as it oﬀers the measurement of brain structures that are not reachable with ECoG and supplying a very broad sampling of neural activity. In particular, sEEG provides an unparalleled opportunity for the decoding of memory-related processes and limbic activity, which can also be incorporated to supplement or further enhance decoding of other cognitive processes.

## AUTHOR CONTRIBUTIONS

All authors contributed to the ﬁnal version of the manuscript.

## FUNDING

This work was part of the research project Decoding Speech In SEEG (DESIS) with project number VI.Veni.194.021, which was ﬁnanced by the Dutch Research Council (NWO).

## REFERENCES

Aghajan, Z. M., Schuette, P., Fields, T. A., Tran, M. E., Siddiqui, S. M., Hasulak, N. R., et al. (2017). Theta oscillations in the human medial temporal lobe during real-world ambulatory movement. Curr. Biol. 27, 3743–3751. doi: 10.1016/j.cub.2017.10.062

Ajiboye, A. B., Willett, F. R., Young, D. R., Memberg, W. D., Murphy, B. A., Miller, J. P., et al. (2017). Restoration of reaching and grasping movements through brain-controlled muscle stimulation in a person with tetraplegia: a proof-of-concept demonstration. Lancet 389, 1821–1830. doi: 10.1016/S0140-6736(17)30 601-3

Akbari, H., Khalighinejad, B., Herrero, J. L., Mehta, A. D., and Mesgarani, N. (2019). Towards reconstructing intelligible speech from the human auditory cortex. Sci. Rep. 9:874. doi: 10.1038/s41598-01837359-z

Alasfour, A., Gabriel, P., Jiang, X., Shamie, I., Melloni, L., Thesen, T., et al.

(2019). Coarse behavioral context decoding. J. Neural Eng. 16:016021. doi: 10.1088/1741-2552/aaee9c

Angrick, M., Herﬀ, C., Mugler, E., Tate, M. C., Slutzky, M. W., Krusienski, D. J., et al. (2019). Speech synthesis from ecog using densely connected 3d convolutional neural networks. J. Neural Eng. 16:036019. doi: 10.1088/1741-2552/ab0c59

Anumanchipalli, G. K., Chartier, J., and Chang, E. F. (2019). Speech synthesis from neural decoding of spoken sentences. Nature 568:493. doi: 10.1038/s41586-019-1119-1

Arya, R., Horn, P. S., and Crone, N. E. (2018). Ecog high-gamma modulation versus electrical stimulation for presurgical language mapping. Epilepsy Behav. 79, 26–33. doi: 10.1016/j.yebeh.2017.10.044

Ball, T., Kern, M., Mutschler, I., Aertsen, A., and Schulze-Bonhage, A. (2009). Signal quality of simultaneously recorded invasive and non-invasive eeg. Neuroimage 46, 708–716. doi: 10.1016/j.neuroimage.2009.02.028

Bancaud, J. (1959). Apport de l’exploration fonctionnelle par voie stéréotaxique à la chirurgie de l’épilepsie. Neurochirurgie 5, 55–112.

Bensmaia, S. J., and Miller, L. E. (2014). Restoring sensorimotor function through intracortical interfaces: progress and looming challenges. Nat. Rev. Neurosci. 15:313. doi: 10.1038/nrn3724

Borton, D., Micera, S., Millán, J. d. R., and Courtine, G. (2013). Personalized neuroprosthetics. Sci. Transl. Med. 5:210rv2. doi: 10.1126/scitranslmed.3005968

Buzsáki, G. (2002). Theta oscillations in the hippocampus. Neuron 33, 325–340. doi: 10.1016/S0896-6273(02)00586-X

Cardinale, F., Cossu, M., Castana, L., Casaceli, G., Schiariti, M. P., Miserocchi, A., et al. (2012). Stereoelectroencephalography: surgical methodology, safety, and stereotactic application accuracy in 500 procedures. Neurosurgery 72, 353–366. doi: 10.1227/NEU.0b013e31827d1161

Chao, Z. C., Nagasaka, Y., and Fujii, N. (2010). Long-term asynchronous decoding of arm motion using electrocorticographic signals in monkey. Front. Neuroeng. 3:3. doi: 10.3389/fneng.2010.00003

Chassoux, F., Navarro, V., Catenoix, H., Valton, L., and Vignal, J.-P.

(2018). Planning and management of seeg. Neurophysiol. Clin. 48, 25–37. doi: 10.1016/j.neucli.2017.11.007

Chrabaszcz, A., Neumann, W. J., Stretcu, O., Lipski, W. J., Bush, A., Dastolfo-Hromack, C., et al. (2019). Subthalamic nucleus and sensorimotor cortex activity during speech production. J. Neurosci. 39, 2698–2708. doi: 10.1523/JNEUROSCI.2842-18.2019

Colgin, L. L., and Moser, E. I. (2010). Gamma oscillations in the hippocampus. Physiology 25, 319–329. doi: 10.1152/physiol.00021.2010

Crone, N., Hao, L., Hart, J., Boatman, D., Lesser, R., Irizarry, R., et al. (2001). Electrocorticographic gamma activity during word production in spoken and sign language. Neurology 57, 2045–2053. doi: 10.1212/WNL.57.11.2045

Eftekhar, A., Sivylla, E. P., and Timothy, G. C. (2010). “Towards a next generation neural interface: Optimizing power, bandwidth and data quality,” in 2010 Biomedical Circuits and Systems Conference (BioCAS) (Paphos: IEEE), 122–125.

Fischer, P., Pogosyan, A., Cheeran, B., Green, A. L., Aziz, T. Z., Hyam, J., et al. (2017). Subthalamic nucleus beta and gamma activity is modulated depending on the level of imagined grip force. Exp. Neurol. 293, 53–61. doi: 10.1016/j.expneurol.2017.03.015

Greenberg, B. D., Malone, D. A., Friehs, G. M., Rezai, A. R., Kubu, C. S., Malloy, P. F., et al. (2006). Three-year outcomes in deep brain stimulation for highly resistant obsessive–compulsive disorder. Neuropsychopharmacology 31:2384. doi: 10.1038/sj.npp.1301165

Hader, W. J., Tellez-Zenteno, J., Metcalfe, A., Hernandez-Ronquillo, L., Wiebe, S., Kwon, C.-S., et al. (2013). Complications of epilepsy surgery–a systematic review of focal surgical resections and invasive eeg monitoring. Epilepsia 54, 840–847. doi: 10.1111/epi.12161

Hampson, R. E., Song, D., Robinson, B. S., Fetterhoﬀ, D., Dakos, A. S., Roeder, B. M., et al. (2018). Developing a hippocampal neural prosthetic to facilitate human memory encoding and recall. J. Neural Eng. 15:036014. doi: 10.1088/1741-2552/aaaed7

Han, C., O’Sullivan, J., Luo, Y., Herrero, J., Mehta, A. D., and Mesgarani, N.

(2019). Speaker-independent auditory attention decoding without access to clean speech sources. Sci. Adv. 5:eaav6134. doi: 10.1126/sciadv.aav6134

Herﬀ, C., Heger, D., De Pesters, A., Telaar, D., Brunner, P., Schalk, G., and Schultz, T. (2015). Brain-to-text: decoding spoken phrases from phone representations in the brain. Front. Neurosci. 9:217. doi: 10.3389/fnins.2015.00217

Herﬀ, C., Johnson, G., Diener, L., Shih, J., Krusienski, D., and Schultz, T. (2016). “Towards direct speech synthesis from ecog: a pilot study,” in 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Orlando, FL: IEEE), 1540–1543.

Herﬀ, C., and Schultz, T. (2016). Automatic speech recognition from neural signals: a focused review. Front. Neurosci. 10:429. doi: 10.3389/fnins.2016.00429

Hochberg, L. R., Bacher, D., Jarosiewicz, B., Masse, N. Y., Simeral, J. D., Vogel, J., et al. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485:372. doi: 10.1038/nature11076

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., et al. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442:164. doi: 10.1038/nature04970

Huggins, J. E., Guger, C., Ziat, M., Zander, T. O., Taylor, D., Tangermann, M., et al. (2017). Workshops of the sixth international brain–computer interface meeting: brain–computer interfaces past, present, and future. Brain Computer Interfaces 4, 3–36. doi: 10.1080/2326263X.2016.1275488

Iida, K., and Otsubo, H. (2017). Stereoelectroencephalography: indication and eﬃcacy. Neurol. Medico-chirurgica 57, 375–385. doi: 10.2176/nmc.ra.2017-0008

Kellis, S., Sorensen, L., Darvas, F., Sayres, C., O’Neill, K., Brown, R. B., et al. (2016). Multi-scale analysis of neural activity in humans: implications for micro-scale electrocorticography. Clin. Neurophysiol. 127, 591–601. doi: 10.1016/j.clinph.2015.06.002

Kern, M., Bert, S., Glanz, O., Schulze-Bonhage, A., and Ball, T. (2019). Human motor cortex relies on sparse and action-speciﬁc activation during laughing, smiling and speech production. Commun. Biol. 2:118. doi: 10.1038/s42003-019-0360-3

Krusienski, D. J., and Shih, J. J. (2011). Control of a visual keyboard using an electrocorticographic brain–computer interface. Neurorehabil. Neural Rep. 25, 323–331. doi: 10.1177/1545968310382425

Kuba, M., Kubová, Z., Kremláˇcek, J., and Langrová, J. (2007). Motion-onset veps: characteristics, methods, and diagnostic use. Vis. Res. 47, 189–202. doi: 10.1016/j.visres.2006.09.020

Leuthardt, E., Pei, X.-M., Breshears, J., Gaona, C., Sharma, M., Freudenburg, Z., et al. (2012). Temporal evolution of gamma activity in human cortex during an overt and covert word repetition task. Front. Hum. Neurosci. 6:99. doi: 10.3389/fnhum.2012.00099

Li, D., Han, H., Xu, X., Ling, Z., and Hong, B. (2017a). “Minimally invasive brain computer interface for fast typing,” in 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER) (Shanghai: IEEE), 477–480.

Li, G., Jiang, S., Paraskevopoulou, S. E., Wang, M., Xu, Y., Wu, Z., Chen, L., et al. (2018). Optimal referencing for stereo-electroencephalographic (seeg) recordings. NeuroImage 183, 327–335. doi: 10.1016/j.neuroimage.2018.08.020

Li, G., Jiang, S., Xu, Y., Wu, Z., Chen, L., and Zhang, D. (2017b). “A preliminary study towards prosthetic hand control using human stereoelectroencephalography (seeg) signals,” in 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER) (IEEE), 375–378.

Liu, Y., Luan, S., Williams, I., Rapeaux, A., and Constandinou, T. G. (2017). A 64-channel versatile neural recording soc with activity-dependent data throughput. IEEE Trans. Biomed. Circ. Syst. 11, 1344–1355. doi: 10.1109/TBCAS.2017.2759339

Logothetis, N. K., Pauls, J., Augath, M., Trinath, T., and Oeltermann, A. (2001). Neurophysiological investigation of the basis of the fmri signal. Nature 412:150. doi: 10.1038/35084005

Maguire, E. A., Burgess, N., Donnett, J. G., Frackowiak, R. S., Frith, C. D., and O’keefe, J. (1998). Knowing where and getting there: a human navigation network. Science 280, 921–924. doi: 10.1126/science.280.5365.921

Maris, E., van Vugt, M., and Kahana, M. (2011). Spatially distributed patterns of oscillatory coupling between high-frequency amplitudes and low-frequency phases in human ieeg. Neuroimage 54, 836–850. doi: 10.1016/j.neuroimage.2010.09.029

Martinez-Ramirez, D., Jimenez-Shahed, J., Leckman, J. F., Porta, M., Servello, D., Meng, F.-G., et al. (2018). Eﬃcacy and safety of deep brain stimulation in tourette syndrome: the international tourette syndrome deep brain stimulation public database and registry. JAMA Neurol. 75, 353–359. doi: 10.1001/jamaneurol.2017.4317

McCarthy, G., Wood, C. C., Williamson, P. D., and Spencer, D. D. (1989). Taskdependent ﬁeld potentials in human hippocampal formation. J. Neurosci. 9, 4253–4268. doi: 10.1523/JNEUROSCI.09-12-04253.1989

McMullen, D. P., Hotson, G., Katyal, K. D., Wester, B. A., Fifer, M. S., McGee, T. G., et al. (2014). Demonstration of a semi-autonomous hybrid brain–machine interface using human intracranial eeg, eye tracking, and computer vision to control a robotic upper limb prosthetic. IEEE Trans. Neural Syst. Rehabil. Eng. 22, 784–796. doi: 10.1109/TNSRE.2013.2294685

Miller, K. J., Leuthardt, E. C., Schalk, G., Rao, R. P., Anderson, N. R., Moran, D. W., et al. (2007). Spectral changes in cortical surface potentials during motor movement. J. Neurosci. 27, 2424–2432. doi: 10.1523/JNEUROSCI.3886-06.2007

Miller, K. J., Sorensen, L. B., Ojemann, J. G., and Den Nijs, M. (2009). Power-law scaling in the brain surface electric potential. PLoS Comput. Biol. 5:e1000609. doi: 10.1371/journal.pcbi.1000609

- Moser, E. I., Kropﬀ, E., and Moser, M.-B. (2008). Place cells, grid cells, and the brain’s spatial representation system. Annu. Rev. Neurosci. 31, 69–89. doi: 10.1146/annurev.neuro.31.061307.090723
- Moses, D. A., Leonard, M. K., Makin, J. G., and Chang, E. F. (2019). Realtime decoding of question-and-answer speech dialogue using human cortical activity. Nat. Commun. 10, 1–14. doi: 10.1038/s41467-019-10994-4

Moses, D. A., Mesgarani, N., Leonard, M. K., and Chang, E. F. (2016). Neural speech recognition: continuous phoneme decoding using spatiotemporal representations of human cortical activity. J. Neural Eng. 13:056004. doi: 10.1088/1741-2560/13/5/056004

Mukamel, R., Gelbard, H., Arieli, A., Hasson, U., Fried, I., and Malach, R. (2005). Coupling between neuronal ﬁring, ﬁeld potentials, and fmri in human auditory cortex. Science 309, 951–954. doi: 10.1126/science.1110913

Muller, L., Chavane, F., Reynolds, J., and Sejnowski, T. J. (2018). Cortical travelling waves: mechanisms and computational principles. Nat. Rev. Neurosci. 19:255. doi: 10.1038/nrn.2018.20

Muller, L., Hamilton, L. S., Edwards, E., Bouchard, K. E., and Chang, E. F. (2016). Spatial resolution dependence on spectral frequency in human speech cortex electrocorticography. J. Neural Eng. 13:056013. doi: 10.1088/1741-2560/13/5/056013

Mullin, J. P., Shriver, M., Alomar, S., Najm, I., Bulacio, J., Chauvel, P., et al. (2016). Is seeg safe? a systematic review and meta-analysis of stereo-electroencephalography–related complications. Epilepsia 57, 386–401. doi: 10.1111/epi.13298

Murphy, B. A., Miller, J. P., Gunalan, K., and Ajiboye, A. B. (2016). Contributions of subsurface cortical modulations to discrimination of executed and imagined grasp forces through stereoelectroencephalography. PLoS ONE 11:e0150359. doi: 10.1371/journal.pone.0150359

Nunez, P. L., and Srinivasan, R. (2006). A theoretical basis for standing and traveling brain waves measured with human eeg with implications for an integrated consciousness. Clin. Neurophysiol. 117, 2424–2435. doi: 10.1016/j.clinph.2006.06.754

Nuyujukian, P., Sanabria, J. A., Saab, J., Pandarinath, C., Jarosiewicz, B., Blabe, C. H., et al. (2018). Cortical control of a tablet computer by people with paralysis. PLoS ONE 13:e0204566. doi: 10.1371/journal.pone.0204566

Parvizi, J., and Kastner, S. (2018). Promises and limitations of human intracranial electroencephalography. Nat. Neurosci. 21, 474–483. doi: 10.1038/s41593-018-0108-2

Pels, E. G., Aarnoutse, E. J., Leinders, S., Freudenburg, Z. V., Branco, M. P., van der Vijgh, B. H., et al. (2019). Stability of a chronic implanted brain-computer interface in late-stage amyotrophic lateral sclerosis. Clin. Neurophysiol. 130, 1798–1803. doi: 10.1016/j.clinph.2019.07.020

Pothof, F., Bonini, L., Lanzilotto, M., Livi, A., Fogassi, L., Orban, G. A., et al. (2016). Chronic neural probe for simultaneous recording of single-unit, multiunit, and local ﬁeld potential activity from multiple brain sites. J. Neural Eng. 13:046006. doi: 10.1088/1741-2560/13/4/046006

Pycroft, L., Stein, J., and Aziz, T. (2018). Deep brain stimulation: An overview of history, methods, and future developments. Brain Neurosci. Adv. 2:2398212818816017. doi: 10.1177/2398212818816017

Ray, S., Crone, N. E., Niebur, E., Franaszczuk, P. J., and Hsiao, S. S. (2008). Neural correlates of high-gamma oscillations (60–200 hz) in macaque local ﬁeld potentials and their potential implications in electrocorticography. J. Neurosci. 28:11526–11536. doi: 10.1523/JNEUROSCI.2848-08.2008

Sani, O. G., Yang, Y., Lee, M. B., Dawes, H. E., Chang, E. F., and Shanechi, M. M.

(2018). Mood variations decoded from multi-site intracranial human brain activity. Nat. Biotechnol. 36:954. doi: 10.1038/nbt.4200

Schalk, G., and Leuthardt, E. C. (2011). Brain-computer interfaces using electrocorticographic signals. IEEE Rev. Biomed. Eng. 4, 140–154. doi: 10.1109/RBME.2011.2172408

Schultz, T., Wand, M., Hueber, T., Krusienski, D. J., Herﬀ, C., and Brumberg, J. S.

(2017). Biosignal-based spoken communication: A survey. IEEE/ACM Trans. Audio Speech Lang. Process. 25, 2257–2271. doi: 10.1109/TASLP.2017.2752365

Shih, J. J., and Krusienski, D. J. (2012). Signals from intraventricular depth electrodes can control a brain–computer interface. J. Neurosci. Methods 203, 311–314. doi: 10.1016/j.jneumeth.2011.10.012

Slutzky, M. W., Jordan, L. R., Krieg, T., Chen, M., Mogul, D. J., and Miller, L. E.

(2010). Optimal spacing of surface electrode arrays for brain-machine interface applications. J. Neural Eng. 7:26004. doi: 10.1088/1741-2560/7/2/026004

Song, D., Hampson, R. E., Robinson, B. S., Marmarelis, V. Z., Deadwyler, S. A., and Berger, T. W. (2016). “Decoding memory features from hippocampal spiking activities using sparse classiﬁcation models,” in 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Orlando, FL), 1620–1623.

Song, D., She, X., Hampson, R. E., Deadwyler, S. A., and Berger, T. W. (2017). “Multi-resolution multi-trial sparse classiﬁcation model for decoding visual memories from hippocampal spikes in human,” in 2017 39th Annual

International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Jeju Island), 1046–1049.

Stavisky, S. D., Kao, J. C., Nuyujukian, P., Ryu, S. I., and Shenoy, K. V. (2015). A high performing brain–machine interface driven by low-frequency local ﬁeld potentials alone and together with spikes. J. Neural Eng. 12:036009. doi: 10.1088/1741-2560/12/3/036009

Talairach, J., and Bancaud, J. (1966). Lesion," irritative" zone and epileptogenic focus. Stereot. Funct. Neurosurg. 27, 91–94. doi: 10.1159/000103937

Tinkhauser, G., Pogosyan, A., Debove, I., Nowacki, A., Shah, S. A., Seidel, K., et al. (2018). Directional local ﬁeld potentials: a tool to optimize deep brain stimulation. Mov. Disord. 33, 159–164. doi: 10.1002/mds.27215

Vadera, S., Marathe, A. R., Gonzalez-Martinez, J., and Taylor, D. M. (2013). Stereoelectroencephalography for continuous two-dimensional cursor control in a brain-machine interface. Neurosurg. Focus 34:E3. doi: 10.3171/2013.3.FOCUS1373

van der Loo, L. E., Schijns, O. E., Hoogland, G., Colon, A. J., Wagner, G. L., Dings, J. T., et al. (2017). Methodology, outcome, safety and in vivo accuracy in traditional frame-based stereoelectroencephalography. Acta Neurochirurg. 159, 1733–1746. doi: 10.1007/s00701-017-3242-9

Van Mierlo, P., Carrette, E., Hallez, H., Raedt, R., Meurs, A., Vandenberghe, S., et al. (2013). Ictal-onset localization through connectivity analysis of intracranial eeg signals in patients with refractory epilepsy. Epilepsia 54, 1409–1418. doi: 10.1111/epi.12206

Vansteensel, M. J., Pels, E. G., Bleichner, M. G., Branco, M. P., Denison, T., Freudenburg, Z. V., et al. (2016). Fully implanted brain–computer interface in a locked-in patient with als. N. Engl. J. Med. 375, 2060–2066. doi: 10.1056/NEJMoa1608085

Vass, L. K., Copara, M. S., Seyal, M., Shahlaie, K., Farias, S. T., Shen, P. Y., et al. (2016). Oscillations go the distance: low-frequency human hippocampal oscillations code spatial distance in the absence of sensory cues during teleportation. Neuron 89, 1180–1186. doi: 10.1016/j.neuron.2016. 01.045

Wander, J. D., and Rao, R. P. (2014). Brain–computer interfaces: a powerful tool for scientiﬁc inquiry. Curr. Opin. Neurobiol. 25, 70–75. doi: 10.1016/j.conb.2013.11.013

Wang, W., Collinger, J. L., Degenhart, A. D., Tyler-Kabara, E. C., Schwartz, A. B., Moran, D. W., et al. (2013). An electrocorticographic brain interface in an individual with tetraplegia. PLoS ONE. 8:e55344. doi: 10.1371/journal.pone.0055344

Watrous, A. J., Miller, J., Qasim, S. E., Fried, I., and Jacobs, J. (2018). Phase-tuned neuronal ﬁring encodes human contextual representations for navigational goals. eLife 7:e32554. doi: 10.7554/eLife.32554

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain–computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Yamin, H. G., Gazit, T., Tchemodanov, N., Raz, G., Jackont, G., Charles, F., et al. (2017). Depth electrode neurofeedback with a virtual reality interface. Brain-Computer Interfaces 4, 201–213. doi: 10.1080/2326263X.2017.1338008 Zander, T. O., and Kothe, C. (2011). Towards passive brain–computer interfaces: applying brain–computer interface technology to human–machine systems in general. J. Neural Eng. 8:025005. doi: 10.1088/1741-2560/8/2/025005

Conﬂict of Interest: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2020 Herﬀ, Krusienski and Kubben. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

