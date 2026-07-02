Review

# Neurolinguistics Research Advancing Development of a Direct-Speech Brain-Computer Interface

Ciaran Cooney,1,* Raffaella Folli,2 and Damien Coyle1

A direct-speech brain-computer interface (DS-BCI) acquires neural signals corresponding to imagined speech, then processes and decodes these signals to produce a linguistic output in the form of phonemes, words, or sentences. Recent research has shown the potential of neurolinguistics to enhance decoding approaches to imagined speech with the inclusion of semantics and phonology in experimental procedures. As neurolinguistics research ﬁndings are beginning to be incorporated within the scope of DS-BCI research, it is our view that a thorough understanding of imagined speech, and its relationship with overt speech, must be considered an integral feature of research in this ﬁeld. With a focus on imagined speech, we provide a review of the most important neurolinguistics research informing the ﬁeld of DS-BCI and suggest how this research may be utilized to improve current experimental protocols and decoding techniques. Our review of the literature supports a crossdisciplinary approach to DS-BCI research, in which neurolinguistics concepts and methods are utilized to aid development of a naturalistic mode of communication.

SEEKING A NATURALISTIC FORM OF COMMUNICATION THROUGH DIRECT-SPEECH BRAIN-COMPUTER INTERFACE

A direct-speech brain-computer interface (DS-BCI) is one that captures and decodes neural signals corresponding directly to speech production, enabling a naturalistic mode of communication (Iljina et al., 2017). Such a system has the potential to transform the lives of patients with severe motor dysfunction, including pathologies such as amyotrophic lateral sclerosis resulting in locked-in syndrome. Loss of verbal communication has a profound effect on those inﬂicted, with loss of social interaction and the potential for isolation. In parallel with this personal degeneration, a caregiver faces a more difﬁcult challenge in ascertaining the needs of the patient. These factors have played a crucial role in driving the development of DS-BCIs (Brumberg et al., 2011; Oken et al., 2014).

It is our view that development of a functional DS-BCI must be predicated on imagined speech (see section ‘‘Imagined Speech: A Special Case of Speech’’ for a detailed description) as the communicative modality. However, several other types of speech have been utilized in experiments referenced throughout this text, making it important to deﬁne their meanings. Table 1 is a categorization of the different types of speech typically used in DS-BCI experimentation. Three types of speech are presented, namely, overt (Blakely et al., 2008), intended (Guenther et al., 2009), and imagined (D’Zmura et al., 2009), and these are subcategorized according to whether the speech is being produced or perceived by a subject. Overt speech production results in an audible output that can be heard by the person speaking and by others within range of the sounds produced. Intended speech is the name given to describe when a person tries to speak but does not have the capacity to produce an audible output. Imagined speech is the internal pronunciation of words without any audible output or associated movement. These are types of speech production and possible methods of communication with DS-BCI. However, several studies have used decoding approaches applied to the neural correlates of speech perception as evidence for the potential of decoding speech processes for communication (Di Liberto et al., 2015; Wang et al., 2018). We consider it to be extremely important to distinguish speech perception studies from speech production studies and to be aware that the ‘‘speech’’ in these studies refers to different phenomena. In perception studies, the speech being considered is the stimulus provided by the experimenter. The corresponding response of the subject, typically in the auditory cortex, is the neural activity being decoded. This differs greatly from the study of speech production in which the subject is actively producing phones, words, or sentences, whether prompted or unprompted, with neural correlates typically corresponding to brain

- 1Intelligent Systems Research Centre, Ulster University, Derry, UK
- 2Institute for Research in Social Sciences, Ulster University, Jordanstown, UK

*Correspondence: cooney-c@ulster.ac.uk

https://doi.org/10.1016/j.isci. 2018.09.016

[Figure 1]

iScience 8, 103–125, October 26, 2018 ª 2018 The Author(s). This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

103

| |Production|Perception|
|---|---|---|
|Overt|Fully articulated speech with audible output|Active or passive hearing of audible speech (one’s own speech or from another source)|
|Intended|Intention to produce overt speech but without the capacity to produce audible output|Perception of one’s own intended speech production|
|Imagined|Internal pronunciation of words, independent of movement and without any audible output|Perception of one’s own imagined speech production|

- Table 1. Categorization of Types of Speech Typically Used in DS-BCI Experiments

regions associated with speech production. Although speech perception studies are important for DSBCI research, this review is primarily concerned with speech production and, in particular, imagined speech production.

A DS-BCI consists of several important stages (see Figure 1). The stages depicted in Figures 1B–1G have each been extensively covered in the literature (Blakely et al., 2008; Guenther et al., 2009; reviewed in Bocquelet et al., 2017). However, there is relatively little consideration of the difﬁculty in modeling the ﬁrst of these stages (Figure 1A), namely, imagined speech production, during which a participant articulates words internally without any motor movement. Neurolinguistics research is providing insight into the cognitive function, phenomenology, and neurobiology of speech production in general (Hickok, 2014) and imagined speech in particular (Alderson-Day and Fernyhough, 2015; Perrone-Bertolotti et al., 2014), and it is our view that these insights should be utilized within DS-BCI research. We concur with the arguments expressed by Iljina et al. (2017) that, given the complexity of speech production processes, combining research from the ﬁelds of BCI and neurolinguistics must be seen as an important approach for those seeking to capture and decode the phenomena.

Imagined speech is the internal pronunciation of words without any motor movement or acoustic output (Torres-Garcı´a et al., 2016) (see section ‘‘Imagined Speech: A Special Case of Speech’’). Related, and overlapping, terminology for imagined speech includes self-talk, sub-vocal/covert speech, internal dialogue/ monologue, sub-vocalization, utterance, self-verbalization, and self-statement (Morin and Michaud,

- 2007). However, for the purposes of performing controlled experiments in the ﬁeld of DS-BCI, it is necessary to maintain a consistent terminology and description of the phenomena (see section ‘‘Imagined Speech: A Special Case of Speech’’). Although imagined and overt speech are not identical, there is overlap between imagined and overt speech production, and imagined speech has become an alternative neuro-paradigm for communicative BCI (D’Zmura et al., 2009; DaSalla et al., 2009; Deng et al., 2010). Such a system differs from other types of communicative BCIs (Chaudhary et al., 2017; Pandarinath et al., 2017) in that it relies on tapping directly into a person’s speech production processes, rather than using some unrelated neural activity as the method of communication.

Several DS-BCI studies have used neurolinguistics approaches within their experimental procedures (Gonza´lezCastan˜eda et al., 2017; Kim et al., 2013; Wang et al., 2011; Zhao and Rudzicz, 2015). In general, the approaches used have been to design a constrained dictionary of words categorized according to their relative semantic or phonological relationships. The basic principle underpinning this approach is that the categorical features of a word may aid decoding accuracy in imagined speech. There is some evidence that this is a valid approach to take, particularly in relation to semantic categorization, which has received greater attention in the literature. Studiesexaminingthefeasibilityofdecodingsemanticinformationfromneuralsignalshaveshownthatsemantic category can be predicted from brain activity (Kim et al., 2013; Wang et al., 2011). However, further research is requiredtodeterminethetrue potentialofneurolinguistics researchinrelation tothe neurobiologyofimagined speech and the structured processes underlying speech production, to inform DS-BCI research.

Here,wereviewtrends inDS-BCI research,and the currentunderstandingofspeechproduction processes, with anemphasisonimaginedspeech.Weconsiderthepotentialimplicationsofattemptingtoharnessneurolinguistics concepts and the limitationsofworkingdirectlywithimagined speech.Anargumentispresented that effective research in the ﬁeld of DS-BCI should incorporate neurolinguistics research and a thorough understanding of imagined speech where possible to aid the development of a naturalistic mode of communication.

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

- Figure 1. Seeking a Naturalistic Form of Communication through Direct-Speech BCI

- (A) DS-BCI is a system that decodes neural signals (e.g., electroencephalography [EEG] or electrocorticography [ECoG])
- (B) corresponding to imagined speech (A). Recorded signals are processed to facilitate maximal information extraction and improvement of signal-to-noise ratio (C). The feature extraction (D) and classiﬁcation (E) stages compute the most discriminative information in the recorded signals and classify them as a part of speech. The output of a DS-BCI system is a textual representation of the imagined speech (F) and auditory representation, which can be used for both communication and feedback (G). In this example, the user actively produces the words ‘‘I am thirsty!’’ with imagined speech. The signals acquired are temporally aligned with each word to facilitate feature extraction and classiﬁcation. The system produces two outputs: a text printout of the imagined speech words being produced and a synthesized audio output, i.e., ‘‘I am thirsty!’’

TRENDS IN DS-BCI

The development of a ‘‘silent’’ interface has long been an active area of research to enable users to communicate without audible articulation of their speech. Several modalities have been developed to facilitate such communication through movement-independent BCI, including BCI-spellers (e.g., D’albis et al.,

- 2012), BCIs based on steady-state visually evoked potential (e.g., Bin et al., 2009), and BCIs based on motor imagery (e.g., Tabar and Halici, 2017a) (see AlSaleh et al., 2016; Tabar and Halici, 2017b for reviews). There are numerous forms that these silent interfaces have taken to provide a more naturalistic, language-based mode of communication, including ultrasound imaging of lip proﬁles (Denby et al., 2006) and word recognition using magnetic implants and sensors (Gilbert et al., 2010). However, approaches such as these require active motor skills that can be readily utilized as the communicative modality and are therefore not movement-independent BCIs.The utilityof BCI as amode forlanguage-basedcommunicationhas been notedby researchers for many years (Denby et al., 2006; Donchin et al., 2000), with the concept for a DS-BCI being a movement-independent BCI based on neural activity corresponding directly to imagined speech production processes. However, the possibility of developing a BCI predicated purely on imagined speech has only recently begun to gather momentum (Ikeda et al., 2014; Yoshimura et al., 2016; Nguyen et al., 2017) as researchers have revealed promising results in attempts to classify units of imagined speech (Gonza´lez-Castan˜ eda et al.,2017;Martin etal.,2014;Peiet al.,2011a;Yoshimuraetal., 2016;ZhaoandRudzicz,2015).There have been several incarnations of DS-BCIs, including a wireless BCI for real-time speech synthesis (Guenther et al., 2009) and a concept for continuous speech recognition (Herff et al., 2017). The current stream of DS-BCI research indicates a trend toward improved classiﬁcation of imagined speech units for decoded brain activity (Gonza´lez-Castan˜eda et al., 2017; Martin et al., 2014) and the development of methodologies for continuous decoding of imagined speech (Brumberg et al., 2016). There have also been recent

B

[Figure 7]

A

[Figure 8]

[Figure 9]

- Figure 2. Direct-Speech BCI Studies Categorized According to Recording Techniques and Types of Speech (A) is a cross-categorization of DS-BCI studies according to the recording techniques applied and the types of speech being investigated.Thetime periodforthisanalysis beginswiththestudyofBlakelyetal. (2008), because this istheﬁrststudybasedon the BCI paradigm depicted and runs to 2018. Criteria for inclusion in this analysis are those studies using said recording techniques to decode speech production (overt, imagined, and intended) directly from neural activity. EEG and ECoG are the mostoftenusedrecordingapproaches.Hightemporalresolutionisanimportantfeatureofboth.Althoughmicro-electrodesdo offerhighspatialandtemporalresolution,theiruseisnotalwayspossibleorappropriate.Overtspeechhasbeenusedasaproxy forimaginedspeech,orincomparativestudies.Thebehavioraldifﬁcultyofstudyingimaginedspeechis,atleastinpart,areason for this trend. The two bar graphs (B) show the distribution of measurement techniques and of types of speech used across all studies. ECoG is utilized in a total of twenty studies and EEG in a total of sixteen. See Table 2.

developments in the classiﬁcation of the neural correlates of speech perception (Di Liberto et al., 2015; Wang et al., 2018), one of which demonstrates real-time classiﬁcation of auditory sentences from neural activity (Moses et al., 2018). Although this research is vital for the implementation of a closed-loop DS-BCI, it is important that results from speech perception studies are assessed independently of speech production studies, as the neural activity corresponding to each cannot be assumed to have similar properties.

There have been notable successes in attempts to improve the decoding of language content directly from neural activity. The neural correlates of vowels and consonants (Idrees and Farooq, 2016; Pei et al., 2011b; Yoshimuraetal.,2016), phonemes (Brumbergetal., 2011;Leuthardt etal.,2011), syllables (Denget al.,2010), whole words (Gonza´lez-Castan˜ eda et al., 2017; Martin et al., 2016), and even sentences (Herff et al., 2015) have all been evaluated using advanced decoding algorithms. Decoding of discrete units of speech, single vowels, for example, has been a popular experimental paradigm in DS-BCI to date (Ikeda et al., 2014, Sereshkeh et al, Rezazadeh Sereshkeh et al., 2017a) presented evidence suggesting that it is possible to classify units of imagined speech from electroencephalogram (EEG), presenting 63.2% G 6.4 accuracy for pairwise classiﬁcation tasks. Other studies have shown that decoding accuracies of vowels and consonants were similar for both overt and imagined speech (Pei et al., 2011a). Elsewhere, linguistic content has been harnessed to aid discrimination of both overt and imagined speech, with phonology (Zhao and Rudzicz, 2015), semantics (Kim et al., 2013), and syntax (Herff et al., 2015) each showing some potential to aid classiﬁcation in DS-BCI. Figure 2, and the corresponding data in Table 2, categorizes DS-BCI studies according to recording technique and the type of speech being investigated. The time period for this analysis begins with the study of Blakely et al. (2008), because this is the ﬁrst study based on the BCI paradigm depicted, and runs through to 2018. Criteria for inclusion in this analysis are those studies using typical recording techniques (EEG, electrocorticogram [ECoG], micro-arrays, functional magnetic resonance imagining [fMRI], and functional near-infrared spectroscopy [fNIRS]) to decode speech production (overt, imagined, intended), but not speech perception, directly from neural activity. Studies utilizing speech imagery or imagined hearing

|Reference|Recording Technique|Type of Speech|Experimental Paradigm|
|---|---|---|---|
|Blakely et al., 2008|Micro-electrode|Overt|Phoneme pronunciation|
|D’Zmura et al., 2009|EEG|Imagined|Imagined speech of two syllables spoken in one of three rhythms|
|Guenther et al., 2009|Micro-electrode|Intended|Vowel production involving movement from a central vowel location to one of three peripheral vowel locations|
|Porbadnigk et al., 2009|EEG|Imagined|Five words, presented in block, sequential, or random order|
|Brigham and Kumar, 2010|EEG|Imagined|Imagined speech of two syllables, /ba/ and /ku/ at two rhythms|
|Deng et al., 2010|EEG|Imagined|Imagined speech of two syllables spoken in one of three rhythms|
|Kellis et al., 2010|Micro-electrode|Overt|Repetition of one of ten words|
|Brumberg et al., 2011|Micro-electrode|Intended|Intended production of 38 American English phonemes|
|Chi et al., 2011|EEG|Imagined|Generation of ﬁve types of phonemes that differ in their manner vocal articulation|
|Leuthardt et al., 2011|ECoG|Overt/Imagined|Overt and imagined phoneme articulation|
|Pei et al., 2011a|ECoG|Overt/Imagined|Overt and imagined repetition of 36 monosyllabic words|
|Wang et al., 2011|ECoG|Overt|Three language tasks based on picture naming|
|Pei et al., 2011b|ECoG|Overt/Imagined|Word repetition using overt or covert speech in response to visual or auditory stimuli|
|Derix et al., 2012|ECoG|Overt|Spontaneous speech in non-experimental setup|
|Herff et al., 2012|fNIRS|Overt/Imagined|Utterances produced in auditory, silent, and imagined speech|
|Zhang et al., 2012|ECoG|Overt|Articulation of Chinese sentences|
|Kim et al., 2013|EEG|Overt/Imagined|Speech of monosyllabic Korean words representing two categories of meaning (number and face)|
|Bouchard and Chang, 2014|ECoG|Overt|Reading of consonant-vowel syllables|
|Derix et al., 2014|ECoG|Overt|Spontaneous speech in non-experimental setup|
|Ikeda et al., 2014|ECoG|Imagined|Imagined speech production of three Japanese vowels|
|Kanas et al., 2014|ECoG|Overt|Two-syllable repetition tasks|
|Martin et al., 2014|ECoG|Overt/Imagined|Overt and covert reading of short stories|
|Mugler et al., 2014a|ECoG|Overt|Overt speech used to identify different phonemes by where they place in different words|
|Mugler et al., 2014b|ECoG|Overt|Overt speech used to identify different phonemes by where they place in different words|
|Song and Sepulveda, 2014|EEG|Overt/Imagined|High tone production in overt, inhibited, and imagined speech|
|Herff et al., 2015|ECoG|Overt|Reading from well-known texts|
|Iqbal et al., 2015a|EEG|Imagined|Imagined speech of vowels /a/ and /u/, and no action|
|Iqbal et al., 2015b|EEG|Imagined|Imagined speech of vowels /a/ and /u/, and no action|
|Lotte et al., 2015|ECoG|Overt|Reading from well-known texts|
|Zhao and Rudzicz, 2015|EEG|Overt/Imagined|Imagined speech production of seven phonemes and two pairs of phonologically similar words|

#### Table 2. Overview of DS-BCI Studies Attempting to Decode Speech from Neural Activity (Continued on next page)

|Reference|Recording Technique|Type of Speech|Experimental Paradigm|
|---|---|---|---|
|Herff et al., 2016|ECoG|Overt|Recitation of a presented sentence|
|Martin et al., 2016|ECoG|Overt/Imagined|Overt and imagined speech production of words selected to maximize variability of number of syllables and semantic category|
|Yoshimura et al., 2016|EEG/fMRI|Imagined|Imagined speech production of Japanese vowels /a/ and /i/|
|Gonza´lez-Castan˜eda et al., 2017|EEG|Imagined|Imagined speech production of ﬁve Spanish words|
|Nguyen et al., 2017|EEG|Imagined|Imagined speech of short words, long words, and vowels|
|Ramsey et al., 2017|ECoG|Overt|Overt speech production of four phonemes|
|Rezazadeh Sereshkeh et al., 2017a|EEG|Imagined|Imagined speech repetition of the words "yes" or "no"|
|Rezazadeh Sereshkeh et al., 2017b|EEG|Imagined|Imagined speech repetition of the words "yes" or "no"|
|Fargier et al., 2018|EEG|Overt|Overt word production corresponding to presented pictures|
|Hashim et al., 2018|EEG|Imagined|Imagined speech word production|
|Ibayashi et al., 2018|ECoG|Overt|Overt speech of 15 Japanese syllables|
|Livezey et al., 2018|ECoG|Overt|Overt speech of 57 different consonant-vowel syllables|

Table 2. Continued

have been excluded, as we do not consider these modalities to be representative of the speech production required of a DS-BCI. The cross-sectional data (Figure 2A) indicate that studies have favored two recording techniques and two types of speech. Clearly, EEG and ECoG are the most dominant recording techniques, having been cited in 16 and 20 studies, respectively (Figure 2B), the likely reason being the high temporal resolution (milliseconds) they both possess, particularly in comparison with imaging techniques such as fMRI (with temporal resolution in the order of seconds). This high temporal resolution is required to capture the dynamic processes associated with speech production (Herff et al., 2016). As a non-invasive recording technique, EEG makes recruitment of experimental participants easier, but the greater spatial resolution of ECoG renders it a better candidate for decoding imagined speech signals when participants are made available as a result of treatment of pre-existing medical conditions (e.g., epilepsy) (Martin et al., 2016). Although microelectrode arrays have shown good performance in ﬁelds such as neuromotor prostheses (e.g., Hochberg et al., 2012), relatively few studies have utilized them for recording the spiking activity of single or multiple units (SU or MU), i.e., neurons, during imagined speech. However, the SU or MU offer the required signal speciﬁcity to improve imagined speech decoding processes given the success in movement and movement intention decoding (Bouton et al., 2016).

It is clear from the data presented in Figure 2 that overt speech production is heavily utilized in experimental trials. Overt speech is included in a total of 26 studies (17 solely overt and 9alongside imagined speech) (Figure 2B). There are several reasons for this trend, including the lack of behavioral veriﬁcation associated with imagined speech, whereby it is difﬁcult to conﬁrm whether experimental tasks have been performed correctly, and the lower amplitude of EEG/ECoG signals it produces (Palmer et al., 2001; Shuster and Lemieux, 2005). Despite lower amplitude signals, there is evidence to suggest that EEG can provide considerable information on imagined speech that can be utilized for a DS-BCI (D’Zmura et al., 2009). Attempts to decode continuous overt speech have been made (Herff et al., 2015), and it is anticipated that further developments mayenable adaptation of this approach for imagined speech. As stated, theuseof overt speech is prevalentinDS-BCI research.However,if atrulynaturalisticform of communicationis tobeachievedusing imagined speech, then a thorough understanding of the phenomena is required.

## IMAGINED SPEECH: A SPECIAL CASE OF SPEECH

The Phenomena of Imagined Speech

As mentioned earlier, many deﬁnitions for imagined speech are present in the literature (Alderson-Day and Fernyhough, 2015; Hirshorn and Thompson-Schill, 2006), one of which refers to it as the internal

pronunciation of words without emitting sounds or making facial movements (Torres-Garcı´a et al., 2016). Research has demonstrated that imagined speech involves many cognitive functions, including learning (Alderson-Day and Fernyhough, 2015), task production (Dolcos and Albarracin, 2014), and memory (Perrone-Bertolotti et al., 2014).

Despite its central position in everyday life, imagined speech has been the subject of relatively little research. Behavioral evidence has indicated that imagined speech is provided by the motor system’s prediction of sensory actions (corollary discharge) (Scott et al., 2013) and it has been suggested that imagined speech is produced in much the same way as overt speech, without the motor-based articulation that generates auditory output (Oppenheim and Dell, 2010). Martı´nez-Manrique and Vicente (Martı´nez-Manrique and Vicente, 2015) support an ‘‘activity’’ view of imagined speech, in which the phenomena does not have a ‘‘proper function’’ in cognition but has simply inherited its suite of functions from overt speech.

Other studies have characterized imagined speech as the basis for rehearsal in short-term memory (Baddeley et al., 1975) and as having a phonological inﬂuence in reading and writing (Oppenheim and Dell,

- 2008). Further studies concur with these ﬁndings, suggesting that inner rehearsal is a central tenet of imagined speech within the phonological loop, i.e., the temporary storage of information in short-term memory (Perrone-Bertolotti et al., 2014), and that imagined speech may interact with working memory to enhance the encoding of new material (Marvel and Desmond, 2012). It has been suggested that imagined speech serves a regulatory role in social speech communication, meaning that it is utilized in overt speech communications (speaking and listening), as well as being implicated as part of a covert articulatory planning process within the speech-motor processing paradigm (see Price [2012] for review).

It has been proposed that imagined speech may be used to generally represent, maintain, and organize taskrelevant information and conscious thoughts (Dolcos and Albarracin, 2014). Although imagined speech is not normally associated with executive control processes, the role of imagined speech in task switching, for example, switching attention across multiple arithmetic problems, has been studied (Emerson and Miyake,

- 2003). The difﬁculties associated with studying imagined speech in experimental research has led to the use of overt speech as a proxy for the phenomena in DS-BCI research (e.g., Martin et al., 2014; Pei et al., 2011b). Therefore, it is useful to have a clear picture of the relationship between the two types of speech.

The Relationship between Overt and Imagined Speech Production

The relationship between overt speech and imagined speech has been extensively debated (Brocklehurst and Corley, 2011; Corley et al., 2011; Oppenheim and Dell, 2010, 2008), although at present there is no deﬁnitive position on the precise nature of this relationship. Here, we present the evidence for a close relationship between overt and imagined speech, before considering the ways in which the two differ. Finally, we discuss the implications of this relationship for DS-BCI research.

Ithasbeenpositedthatimaginedspeechisatruncatedformofovertspeech,inthatthestagesofproductionare thesameforboth,beforethearticulatoryeffectsassociatedwithovertspeech(OppenheimandDell,2010).Subjective accounts of imagined speech indicate that it resembles overt speech in tempo, pitch, and rhythm (MacKay, 1992) and studies have found that imagined speech retains deep-lying features such as lexical and semantic information (Oppenheim and Dell, 2008). The motor simulation hypothesis places overt and imagined speech on a continuum, on which linguistic mechanisms and physiological correlates are shared (Perrone-Bertolotti et al., 2014), albeit with features attenuated in imagined speech (Alderson-Day and Fernyhough, 2015). Importantly, the motor simulation hypothesis assumes that imagined speech necessarily includes fully speciﬁed articulatory detail (e.g., Levelt, 1989), merely lacking observable sound and movement.

Phonemic similarity (in which mistaken phonemes are replaced with similar phonemes) has been observed with similar magnitudes for both overt and imagined speech production (Brocklehurst and Corley, 2011), and further ﬁndings suggest that imagined speech is speciﬁed at the sub-phonemic level and that its process of production must be similar to that of overt speech (Corley et al., 2011). The implication here is that imagined speech does contain much of the featural richness associated with overt speech, a view fully compatible with evidence that phonological representations are fully encoded in imagined speech. Imagined speech has been considered part of an overall speech production system, in which it is used for predictive simulation or ‘‘forward models’’ of linguistic representations, suggesting that it is produced in much the same way as overt speech, minus overt articulation (Levelt et al., 1999).

There is considerable overlap between the neurobiology of overt and imagined speech (Marvel and Desmond, 2012), with neural activations in typical left-hemispheric language regions, in general, being associated with both (Basho et al., 2007; Huang et al., 2002; McGuire et al., 1996a; Palmer et al., 2001) (see section ‘‘The Neuroanatomy of Imagined Speech’’). Activation of Broca area during imagined speech indicates that this typical language region is associated with its production and is consistent with results from functional imaging studies examining silent articulation (Paulesu et al., 1993). fMRI results have shown activation of the supplementary motor area (SMA), inferior frontal gyrus (IFG), and insula during phonological processing of imagined and overt speech (Aleman et al., 2005). Furthering current understanding of the neuroanatomy and neural correlates of imagined speech production is an important aspect of research in this ﬁeld.

Although they suggest that there is signiﬁcant overlap between overt and imagined speech, Oppenheim and Dell (2008) also advise that imagined speech is impoverished at the featural level and thus abstract and underspeciﬁed. It has been suggested that imagined speech is often attenuated at the surface level, lacking phonological (Oppenheim and Dell, 2008) or phonetic (Wheeldon and Levelt, 1995) detail. Countering the view that imagined speech is intrinsically similar to overt speech, the abstraction hypothesis contends that imagined speech is produced as a consequence of activation of abstract linguistic representations (e.g., Indefrey and Levelt, 2004). The theory states that imagined speech is activated before the speaker retrieves any articulatory information and therefore should not require any motor activations. There are several arguments in favor of the abstraction view (summarized in Oppenheim and Dell, 2010), the ﬁrst of which is that imagined speech is produced faster than overt speech, suggesting that imagined speech is abbreviated in some respect (e.g., MacKay, 1992) and thus lacks the articulatory properties associated with overt speech. Another argument is that attenuated activity in language-related brain regions during imagined speech indicates that the processes of production are not as complete as in overt speech. The third argument presented is that imagined speech does not require articulatory abilities and so articulation is not required for complete use of imagined speech. The authors also observe that articulatory suppression does not necessarily eliminate imagined speech. Moreover, imagined speech does not (necessarily) translatetoovert speechperformance. Theoretically, were overt andimaginedspeechto involvesimilar planning processes, then it would be reasonable to expect practice of an utterance in one form of speech to improve performance in the other. However, evidence has indicated that this is not the case (Corley et al., 2011).

Alternatively, the ﬂexible abstraction hypothesis states that there is a single form of imagined speech, which is represented at the phonemic-selection level (Oppenheim and Dell, 2010). The hypothesis states that representations can be modulated by articulation to include more explicit features, and the authors suggest that cases in which imagined speech appears to have phonological features may be caused by participants deploying a form of imagined speech involving a greater degree of articulation. The ﬂexible abstraction hypothesis suggests that imagined speech may fail to involve articulatory representations but it can incorporate lower-level articulatory planning when speakers silently articulate. The surface-impoverished hypothesis states that imagined speech is impoverished at the surface level, having weaker lower-level representation (e.g., featural level), and the deep-impoverished hypothesis states that imagined speech represents sounds and gestures but not higher level information (Oppenheim and Dell, 2008). Imagined speech may be formed as a featurally abstract forward model (Pickering and Garrod,

- 2013), and phonological features may be experienced as a result of the sensory prediction created (Scott

- et al., 2013). Imagined speech may also vary depending on cognitive and emotional conditions, causing changes between abstract and concrete forms (Fernyhough, 2004).

As stated earlier, neuroanatomical overlap between regions associated with overt and imagined speech has been observed. Nevertheless, there are signiﬁcant differences in brain activity between the two processes (e.g., Basho et al., 2007). For example, fMRI has discovered that imagined speech elicits greater activation in several areas of the brain (e.g., Basho et al., 2007) and a lesion symptom mapping (LSM) study of patients with aphasia showed that participants with poor overt speech retained relatively strong imagined speech in comparison (Stark et al., 2017), suggesting a dissociation of the cognitive mechanisms generating overt and imagined speech. Previous work with aphasics, indicating that imagined speech abilities were more effected by lesions to the left pars opercularis than overt speech production, led Geva, Jones et al. (Geva et al., 2011b) to state that imagined speech cannot be assumed to be overt speech without a motor component. For further information on the neurobiology of imagined speech, see section ‘‘The Neuroanatomy of Imagined Speech.’’

Perrone-Bertolotti et al. (2014) astutely observe that the variance in results between overt and imagined speech experiments may, at least partially, be explained by the different speech tasks involved in the studies. Word repetition, object naming, verb generation, etc., all require different speech production processes and thus engage different areas of the brain. It is also conceivable that differences between the two types of speech could be put down to participants being better able to perceive certain types of error in overt speech. Perrone-Bertolotti et al. (2014) also suggest that differing results may indicate that imagined speech consists of ﬂexible subtypes or levels and that the experimental paradigm may be partially responsible for the differences observed between the two types of speech.

Clearly, there is no deﬁnitive description of the precise relationship between overt and imagined speech, and this is a subject that requires further elucidation from neurolinguistics research. We agree with Martı´nez-Manrique and Vicente (2015) that a comprehensive view of imagined speech will require precise models of linguistic production and comprehension and a cognitive account will require more data than is currently available. Therefore, we must also agree with Geva, Jones et al. (Geva et al., 2011b) that overt speech cannot simply be assumed to be a reliable substitute for imagined speech. It is our contention, in relation to DS-BCIs, that it is not possible to reliably infer performance in an imagined speech paradigm from results obtained during overt speech experiments. This is not to say that there is no value in overt speech paradigms, and given that there is much overlap in the linguistic theory and neurobiology associated with both, there is certainly a lot to be gained from such experiments. However, as the communicative paradigm for an eventual operational DS-BCI is imagined speech, we must emphasize the importance of utilizing this modality, when possible, in experimental protocols.

The Neuroanatomy of Imagined Speech

Alderson-Day and Fernyhough (2015) suggest that a prima facie assumption about the neural correlates of imagined speech might be that they closely resemble an attenuated version of the neural activity associated with overt speech. There is evidence supporting activation in Broca area, SMA, and parts of the prefrontal cortex, having been observed during both overt and imagined speech (see Price, 2012 for review). Studies have shown that overt and imagined speech do produce similar neural activations, with the exception of certain motor-related activity associated with overt speech (Palmer et al., 2001), and that the bloodoxygen-level-dependent response measured from fMRI recordings was greater during overt than during imagined speech (Shuster and Lemieux, 2005). However, the neuroanatomy of imagined speech has been shown to differ from that of overt speech (e.g., Basho et al., 2007). It is important to identify the regions speciﬁcally correlated with imagined speech in the context of development of a DS-BCI that are independent of movement and therefore not overt speech production and are independent of stimuli and therefore not speech perception.

Reports on the anatomical underpinnings of imagined speech have consistently implicated the left inferior frontal gyrus (LIFG) as the anatomical basis for the phenomena (Aleman et al., 2005; McGuire et al., 1996a, 1996b; Shergill et al., 2002) (see Figure 3 [Berwick et al., 2013]). Positron emission tomography (PET) has attributed LIFG activation to imagined speech during sentence and single-word production (McGuire et al., 1996b), and fMRI was used to observe LIFG activation during imagined sentence production (Shergill and Bullmore, 2001; Shergill et al., 2002). In the second of these fMRI studies (Shergill et al., 2002), the LIFG, along with other regions, was associated with increased activation corresponding to increased rates of imagined speech production. The region has also been associated with increased activation during dialogic, in comparison with monologic, imagined speech (Alderson-Day et al., 2015). Morin and Michaud (2007) note that the LIFG exhibits functional heterogeneity, observing that its most anterior parts (Brodmann area [BA]45) are involved in word retrieval and their associated meanings, whereas the posterior part (BA46/47) specializes in accessing words through an articulatory code (Paulesu et al., 1997). It has been observed that task-elicited imagined speech results in increased activation in the LIFG, in comparison with spontaneous imagined speech (Hurlburt et al., 2016). The authors suggest that activation of LIFG during task-elicited imagined speech may be a reﬂection of elicitation tasks rather than the speech itself, as the LIFG is thought to be integral to planning and execution of hierarchical sequences.

Among regions most often observed as corresponding to imagined speech production are SMA (Shergill and Bullmore, 2001; Shergill et al., 2002), insula (Aleman et al., 2005), premotor cortex (McGuire et al., 1996a), STG, and middle temporal gyrus (MTG) (Shuster and Lemieux, 2005). The SMA, left precentral gyrus, and right inferior parietal lobe are all associated with increased activation at slower rates of imagined

[Figure 10]

- Figure 3. Neuroanatomical Regions Associated with Imagined Speech Production The diagram depicts brain regions typically associated with language function in the left hemisphere (Berwick et al., 2013), with each of the numbered sections indicating one of Brodmann areas (BA). The IFG, which includes BA44 and BA45, is the most common region associated with imagined speech production. Single word and sentence production both activate the IFG, and the region is thought to be associated with word retrieval and associated meanings (BA45). Both the STG and MTG have been implicated in imagined speech studies as relating to the phonological loop and to production of dialogic imagined speech. The dorsal pathways between BA44 and the posterior superior temporal cortex (pSTC) supports core syntactic processes. The ventral pathways, including between BA45 and the temporal cortex (TC), support processing of semantic and conceptual information. Reprinted with permission from Berwick et al. 2013, copyright 2013, Elsevier.

speech production (Shergill et al., 2002). The SMA has also been associated with sentence-repetition tasks (Shergill and Bullmore, 2001) and phonological processing during imagined speech (Aleman et al., 2005). The insula has been implicated in multiple studies reporting on imagined word production (Aleman et al., 2005; Hubbard, 2010; McGuire et al., 1996a; Shergill and Bullmore, 2001) but may not be representative of imagined speech given that it is often associated with imagined hearing (see later discussion) and overt speech. However, Shuster and Lemieux (2005) observed that many studies that have failed to report involvement of the insula in speech production have typically used only imagined or silently articulated speech (Wildgruber et al., 2001).

Increased activation has been observed in the left MTG and STG during the production of multisyllabic words in imagined speech trials (Shuster and Lemieux, 2005), and the posterior STG has been implicated in metric stress evaluation in the phonological loop (Aleman et al., 2005) (see Figure 3). Interestingly, the left MTG and STG are often associated with increased activity during trials involving imagined hearing or dialogic imagined speech (see Alderson-Day and Fernyhough, 2015 for review). This type of task, in which a participant is asked to imagine hearing speech in another person’s voice, is thought to rely on memory for phonological information (Alderson-Day and Fernyhough, 2015) and to activate the primary auditory cortex (Heschl gyrus) (Hurlburt et al., 2016). Other ﬁndings indicate that dialogic imagined speech draws from a range of regions beyond a typical left-sided perisylvian language network, including the right IFG, right MTG, and the right STG/STS (Alderson-Day et al., 2015). The precuneus, posterior cingulate, left insula, and cerebellum are also implicated. The dorsal pathways between BA44 and the posterior superior temporal cortex subserve higher-order hierarchical sequences and thus support core syntactic processes (Friederici, 2018), whereas the ventral pathways, including between BA45 and the temporal cortex, support processing of semantic and conceptual information (Berwick et al., 2013).

Hurlburt, Heavey, and Kelsey (Hurlburt et al., 2013) state that both production and perception of imagined speech exhibit activations in regions such as the IFG, SMA, insula, and posterior STG (Hubbard, 2010; Price, 2012). Although there certainly appears to be overlap between imagined speech and imagined hearing, they are, in general, anatomically separable. Imagined speech is typically associated with left-hemispheric regions, including the LIFG, insula, and STG (McGuire et al., 1996a), whereas imagined hearing corresponds to a bilateral network with the activation of SMA, posterior parietal cortex, STG, and MTG (Zatorre and Halpern, 2005). It has been suggested that differences between the two conditions may be the result of additional motor elements of imagined speech, which involve the deployment of a somatosensory forward model (Tian and Poeppel, 2013).

Concerns have been raised surrounding the ecological validity of ﬁndings on the neural components of imagined speech (Alderson-Day and Fernyhough, 2015). Paradigms are often simple word or sentencerepetition tasks, ignoring the complexity of imagined speech (Jones and Fernyhough, 2007). Although

experiments such as these are a common approach in language studies, it is our view that further studies examining spontaneously produced speech (Derix et al., 2014, 2012; Ruescher et al., 2013) and imagined speech (Hurlburt et al., 2016) are required to provide greater elucidation of the neural underpinnings of the phenomena. It is also important to note that, as well as general activations associated with imagined speech production, processing of complex lexical, phonological, semantic (Basho et al., 2007), or word retrieval (Hirshorn and Thompson-Schill, 2006) tasks correspond to additional activity in the inferior frontal cortex (IFC) of the left hemisphere. We concur with Bocquelet et al. (2017) that neuroanatomical ﬁndings indicate that high-level processing of imagined speech requires left-lateralization.

Information on the neuroanatomical regions associated with imagined speech production is enhanced by consideration of the characteristics of the corresponding neural activations and, in particular, the frequency bands that may provide the most discriminable content. Activations in the beta band above Broca area and the frontal cortex have been associated with imagined speech production (Rezazadeh Sereshkeh et al., 2017b). In one study, increased activity was observed in EEG channels located close to Broca area in the frequency range of 20–30 Hz, whereas activity in Wernicke area appeared primarily below 15 Hz (Nguyen et al., 2017). This may indicate that separate frequency bands contain information relating to different speech production processes. In the same study, the authors use evidence from the classiﬁcation of short versus long words to suggest that differences in the complexity of words could create discriminative features across frequency bands. In an imagined speech yes/no classiﬁcation task, no discriminative difference was detected in the delta, theta, alpha, and mu rhythms. However, in the higher frequency ranges (beta and gamma), a discriminative pattern was associated with typical left-sided speech regions (Rezazadeh Sereshkeh et al., 2017b).

MEG measurements obtained during a silent reading task showed event-related desynchronization in the alpha and beta bands over Broca area (Goto et al., 2011). The results of an ECoG study into imagined speech vowel articulation suggested that signals in the alpha (8–13 Hz) and beta (14–30 Hz) bands over Broca area may contain information about the articulatory code of single vowels but not about segmentation of a phoneme sequence (Ikeda et al., 2014). Clearly, the recording technique employed impacts the frequency ranges that can be analyzed. For example, ﬁltering imagined speech EEG data between 3 and 20 Hz (Deng et al., 2010) found considerable energy in the alpha band (8–14 Hz), whereas using ECoG has allowed researchers to obtain features from the high gamma (70–150 Hz) band (Martin et al., 2016), which is useful for its association with spike rate and local ﬁeld potential and its reliable tracking of rapid neural ﬂuctuations during speech perception and production (e.g., Pei et al., 2011a). It is our view that this information on the important frequency bands associated with imagined speech can aid decoding approaches in future research. However, it is also important that further research in this area is undertaken so that a detailed and accurate picture of the spatial-temporal-spectral correlates of imagined speech is developed.

In the next section, we extend our analysis on the neuroanatomical underpinning of imagined speech to include the current understanding of speech production processes and the anatomical regions of interest they correspond to.

## HOW IS (IMAGINED) SPEECH PRODUCED?

Models of Speech Production

It is a matter of consensus in psycholinguistic research that speech production is planned across multiple hierarchically organized levels of analysis (Hickok, 2012) and that word production involves at least two stages of processing: a lexical and a phonological stage (Levelt et al., 1999) (Figure 4B). Models of speech production can differ in terms of the number of distinct stages involved (Hickok, 2014, 2012; Levelt, 1999; Levelt et al., 1999), but there is general agreement that it involves a staged, hierarchical process with a temporal structure, as indicated by the models in Figure 4.

According to Levelt (1999), spoken word production includes lexical selection, lemma retrieval, and morphological and phonological code retrieval and is completed with articulation (Figure 4A). Models of speech production typically begin with an input from the conceptual system, i.e., the message to be expressed (Levelt, 1999). This is then mapped to a corresponding lexical representation, encoding properties such as grammatical features but not a phonological form. Following selection of a lemma, the morphological stage bridges the gap between the conceptual domain and the phonological or articulatory domain.

### A B C

- Figure 4. Speech Production Models with Estimated Time Courses Although models can differ in the number of components, there is general agreement that speech production is a staged, hierarchical process with a temporal structure, as indicated in the diagram. In (A), estimated time courses associated with the stages of production are provided in milliseconds (ms) (Indefrey, 2011) along with a production model containing two major components. These are the word (lemma) level and the phonological level (Hickok, 2012). In (B), a more detailed model depicts several different phases in the production process (Levelt et al., 1999). The initial stage is conceptual preparation, where a message to be expressed is formulated and a lexical concept produced. Next is lexical selection, in which a word or lemma is retrieved for use. Following selection of a lemma, the morphological stage bridges between the conceptual domain and the phonological, or articulatory, domain. A word is then encoded in syllabic form before being encoded in phonetic form, from which the audible output is produced. In (C), a truncated version of the model in (B) is presented to highlight the stages of production corresponding to imagined speech. The estimated time courses end with the phonological encoding/syllabiﬁcation stage. (A) is adapted with permission from Hickok 2012, copyright 2012, Springer Nature. (B) is adapted with permission from Levelt et al. 1999, copyright 1999, Cambridge University Press.

*upper boundary.

Phonetic encoding and articulation, seen in Figure 4A, are stages of the speech production process concerned with acoustic output. The speech production models, as stated here, are based primarily on work in the ﬁelds of motor control and psycholinguistics, and it has been noted that linguistic models are currently constrained by the need for further developments in neuroscience (Hickok, 2012). EEG studies have been used to study the time courses associated with the processing stages in word production (see Indefrey, 2011 for review). Following analysis of several event-related potential studies, Indefrey (2011) presented the following estimated onset times and durations for overt speech production: conceptual preparation (0–200 ms), lemma retrieval (200–275 ms), phonological code retrieval (275 ms onset), syllabiﬁcation (355 ms onset; 20 ms per phonemes, 50–55 ms per syllable), phonetic encoding (455 ms onset), and articulation (600 ms) (Figure 4A). Although this research is based on overt speech, and the articulation stage is not relevant, the estimated timings can be informative for DS-BCI researchers seeking to target a speciﬁc stage of the production process during signal decoding.

Language production involves multiple levels of representation, and this modular system incorporates various sub-systems, i.e., semantics, syntax, and phonology. Different brain regions in the left and right hemispheres have been identiﬁed as supporting these language functions, with syntactic processing supported by networks involving the temporal cortex and inferior frontal cortex, and less lateralized temporo-frontal networks subserving semantic processing (see Friederici, 2011). In discussing Hebbian theory, Pulvermu¨ller (1999) considers whether lexical or semantic distinctions reﬂect differences that are biologically real, using it to explain the observation that word meanings can be mapped to different cortical regions, for example. This results in words that are distinguished on the basis of linguistic criteria being represented differently in the brain. Investigations into the neural correlates of language function and competence commonly employ functional imaging approaches (see Indefrey and Levelt, 2004), as well as LSM, to determine the links between linguistic pathologies and corresponding lesion sites in aphasics (Bates et al., 2003). Linguistic research can be considered within the context of several modular

domains, four of which (semantics, lexical access, syntax, and phonology) are discussed in the following sections.

Semantics and the Meaning of Words

Semantic knowledge has been referred to as the ability to assign and use the meaning of words, relying on both stored semantic knowledge and executive control to enable semantic activation in line with goals and constraints (Whitney et al., 2012). The term semantics refers to the meaning of a word or collection of words. In the models of speech production in Figure 4, semantic information forms part of the conceptual stage in which a message to be expressed is conceived. This conceptual stage precedes lexical selection, syntactic encoding, and phonological encoding, with the process leading up to selection of a lexical concept referred to as ‘‘conceptual preparation.’’ Mapping between the semantic concept to be expressed and a lexical formulation of this message is not a simple one-to-one process, as there are often multiple ways to refer to a single concept (e.g., a car may be referred to as a vehicle, saloon, or motorcar) (Levelt et al., 1999).

Semantic comprehension studies indicate that semantic operations are normally slower to develop and longer lasting than syntactic operations (Pin˜ ango et al., 2006) and thus accommodate slower lexical activation than syntactic dependencies (Love et al., 2008). However, it cannot simply be assumed that the relationship between semantic and syntactic comprehension is mirrored in speech production processes. One study has posited the possibility of an intermediate layer between semantics and phonology owing to the arbitrary nature of the mapping from meaning to sounds, i.e., words with similar meanings do not tend to have similar sounds associated (Lambon Ralph et al., 2002), and the Hebbian associationist model predicts that semantic differences between word categories generate patterns of neural activity reﬂective of those differences (Pulvermu¨ ller, 1999). For example, naming of living versus inanimate objects was more strongly correlated with integrity of the middle temporal cortex, whereas both categories showed signiﬁcant overlap in the frontal cortex (Henseler et al., 2014). In addition, large parts of the IFG appear to be involved in semantic differentiation of verbs versus nouns. Activation in the LIFG is typically exhibited when difﬁcult semantic relationships, such as the meaning of ambiguous words (e.g., words such as break, light, and head have multiple meanings) within a sentence, need to be parsed. These difﬁcult relationships may be weak or unusual associations, an increased number of response options, or competition among potential targets in a semantic network (Badre et al., 2005). Although many neuroimaging studies have concentrated on the LIFG as the basis for semantic processing and control, other studies show that damage to a wide distribution of brain regions results in impairment of semantic control (Whitney et al., 2012). The orbital IFG exhibited higher correlation with the semantic differentiation of nouns, whereas a more posterior, triangular/opercular part of the IFG was associated with the impaired differentiation of verbs. Results from action word studies have indicated that semantic processing can engage many different cortical areas, with Pulvermu¨ ller (2005) stating that this contradicts the view that processing of meaning is concentrated in a single cortical location. Moreover, it has been demonstrated that word class distinctions can be made in relation to different types of action words (Hauk et al., 2004), with different cortical activations associated with the muscles used to perform a given action, the complexity of the movement, and the number of muscles involved (Pulvermu¨ ller, 1999).

Lexical Access Maps Meaning to Words

Lexical access is the process that facilitates access to the words retained in memory that are required for language production. Dell, Martin, and Schwartz (Dell et al., 2007) present a two-step model of lexical access in which a network consists of a semantic layer connected to words and words connected to a phoneme layer. Word retrieval begins when the semantic features of an intended word are activated. This activation proceeds through the network, resulting in the selection of the most active word from a grammatical category. A phonological retrieval stage begins with the activation of this selected word.

Lexical access effects the ﬂuency and speed at which speech is produced. For example, it has been shown that function words (i.e., contributing to syntax/grammar) are accessed faster than content words (i.e., contributing to information/meaning), independent of perceptual characteristics (Segalowitz and Lane,

- 2004). Another factor inﬂuencing lexical ﬂuency is the frequency with which a word is used (Mohr et al., 1996). In a picture-naming paradigm, participants displayed quicker response times in object-naming tasks than they did in action-naming tasks, leading the authors to posit that the process of mapping between the picture and the name itself appears to differ between lexical categories, namely, nouns versus verbs

(Szekely et al., 2005). Other evidence taken from studies involving patients with aphasia has shown that the mental lexicon distinguishes grammatical classes (Benetello et al., 2016).

There are several brain regions associated with word production during lexical selection. Indefrey and Levelt (2004) reviewed 82 functional imaging studies of single word production, identifying 11 regions in the left hemisphere (posterior IFG, ventral precentral gyrus, SMA, mid- and posterior STG and MTG, posterior temporal fusiform gyrus, anterior insula, thalamus, and medial cerebellum) and four in the right (mid-STG, medial and lateral cerebellum and SMA) involved in core processes of word production. Other functional imaging studies have demonstrated that lexical-semantic knowledge is stored in the temporal lobe (Vigneau et al., 2006) and that the region can operate as a lexical interface linking phonological and semantic information in a sound-to-meaning interface (Hickok and Poeppel, 2007). Elsewhere, the left MTG has been found to associate with lexical selection (Indefrey and Levelt, 2004). The spatiotemporal dynamics of word retrieval, including lexical selection, are not well understood, but Rie` s et al. (2017) have shown that activation of word representations and their selection temporally co-occur and that a widespread network of overlapping brain regions is associated. The variety of brain regions implicated in word production suggests that there is potential for exploiting semantics, syntax, and phonology to activate different regions during imagined speech production to maximize the separability of brain activations for DS-BCI.

The Hierarchical Structure of Syntax

Contemporary linguistic theories contend that syntactic and sentential representations are complex sets of hierarchically organized syntactic categories and that the relationships between categories in this hierarchy determine the different aspects of propositional meaning (see Zaccarella and Friederici [2016] for a neurobiological review of syntactic hierarchies). During syntactic encoding, a conceptual message is linguistically encoded by retrieval of corresponding words from the lexicon and grammatical ordering of these words (Indefrey et al., 2001). Stored syntactic information, such as word class, is used to compute a structure that speciﬁes the relationships between words in a sentence, e.g., order and inﬂection.

It has been proposed (Frazier, 1987), and countered (Friederici, 2002), that there is an isolated syntactic processing mechanism that has no relation to semantics or other non-syntactic information. It has been stated that syntactic encoding in speech production exhibits close temporal overlap with other processes (Indefrey et al., 2001) and that brain activations in the frontotemporal language network have indicated that syntactic processing occurs before semantic processing but that these processes are not isolated mechanisms (Friederici, 2002).

Syntactic processing is speciﬁcally associated with BA44, located in the posterior portion of Broca area in the LIFG and its white matter connection to the posterior temporal cortex (Friederici, 2018). A functional imaging study has provided evidence that hierarchical syntactic conditions localized in the ventral portion of BA44 (Zaccarella and Friederici, 2015). In contrast, activations corresponding to processing of two-word sentences without syntactic hierarchy were associated with the frontal operculum/anterior insula. Love et al. (2008) provide evidence that the left IFC supports syntactic processing because it sustains the requisite lexical activation speed needed for the real-time formation of a syntactic dependency. Elsewhere, PET has been used to identify both sentence-level and local syntactic encoding of speech in the Rolandic operculum, adjacent to Broca area (Indefrey et al., 2001).

The Internal Phonological Speech Code

Within psycholinguistic theory the assumption exists that speech articulation is preceded by an internal abstract speech code (Wheeldon and Levelt, 1995). In speech production, a word can have different intonation, duration, and amplitude, leading to the proposal that each linguistic unit has a phonological representation encoding features unique to that unit. Phonological representations are categorical and consist of discrete timeless segments (Wheeldon and Levelt, 1995). Models differ as to the timing and order at which phonemes are assigned to a phonological structure. Following the syntactic computation phase, stored information on the sounds of words is retrieved as ‘‘phonological codes.’’ These are then transformed to produce an executable code, i.e., speech (Indefrey et al., 2001).

It has been proposed that phonological word representation is accessed from Broca area and compiled into segments of syllables (Indefrey and Levelt, 2004). Other studies indicate that the posterior middle and inferior portions of the temporal lobes are linked to phonological and semantic processing (see Hickok

and Poeppel, 2007). Another suggestion (Edwards et al., 2010) is that speech production is enabled through verbal/phonological working memory using the dorsal stream areas implicated in speech perception and phonological working memory (e.g., Hickok and Poeppel, 2007). It has been suggested that phonological encoding exhibits correlation with the superior temporal sulcus (STS) (Llorens et al., 2011), whereas the authors of one study linked the IFG and STS gamma band responses (>40 Hz) to the phonological retrieval processes and imagined speech production, using intracranial EEG recordings (Mainy et al., 2008). Although it is well known that lemma selection begins earlier than phonological encoding, it seems that there is some temporal overlap between the two activations (Sedivy, 2014) and it is possible that phonologically similar words are represented by overlapping cell assemblies sharing a single perisylvian region (Pulvermu¨ller, 1999). It is possible for a phonological word form to have two meanings (e.g., the noun/verb dichotomy of the/to beat), and it has been suggested that there must be an underlying mechanism for realizing the exclusive-or relationship between the two.

The review of the literature presented in the earlier sections provides the basis for our discussion on the role of linguistics within the framework of DS-BCI research. This discussion is presented in the next section.

AN ENHANCED ROLE FOR LINGUISTICS IN BCI RESEARCH

Overt speech is a rich tapestry of sound, pitch, rhythm, structure, and meaning, and studies have shown that imagined speech retains many of these articulatory characteristics (Alderson-Day and Fernyhough, 2015; Scott et al., 2013). It is one of the great challenges of DS-BCI research to represent this communicative richness through the modality of a BCI. With this goal in mind, improvements to experimental protocol have been suggested, including the use of a vocabulary of words with semantic meaning to improve discrimination between words and a normalization of word length to mitigate the high variance of this feature (Porbadnigk et al., 2009). We advocate the use of novel experimental design to enhance effective elicitation of imagined speech and improve discriminability between phonemes, words, and sentences. Further investigation into the neurological and neuroanatomical underpinnings of imagined speech production and the development of a more concrete understanding of the information contained within different frequency bands at different brain foci are also required. The importance of consistency in the way imagined speech is produced by experimental participants and the effect of providing them with a thorough understanding of what is meant by imagined speech production are additional areas for investigation that may improve the robustness of experimentation. In the following subsections, we extend the work of Iljina et al. (2017) by highlighting three key areas where BCI research can beneﬁt from ﬁndings in the ﬁeld of neurolinguistics.

Incorporating the Structure of Speech Production Processing

The sheer complexity of the neural mechanisms underpinning speech is one of the primary factors causing resistance to the development of a DS-BCI. In comparison with many of the previous incarnations of communicative BCI (Chaudhary et al., 2017; Pandarinath et al., 2017), the character of the modality of interaction, i.e., imagined speech, is still a relatively poorly understood phenomenon. In relation to DS-BCIs, the following question has been put forward: when does semantic, phonological, or syntactic processing occur (Iljina et al., 2017)? The analysis of Indefrey (2011) provides some insight into the relative timings associated with the stages of speech production (see Figure 4) and indicates that it may be possible to target decoding of semantic information at an earlier stage than the phonological representation. The temporal sequence of these processes is an important consideration for BCI researchers seeking to extract meaning from imagined speech, but there are opposing views to navigate. One of these is a sequential model in which word production involves a series of separate stages from semantic concept through word retrieval and phonological articulation (Levelt et al., 1999). Alternative models hypothesize a parallel architecture in which neurolinguistic processes occur simultaneously (Jackendoff, 2007). Whichever of these models is correct, they must be incorporated into the DS-BCI paradigm.

The speech production process as depicted in section ‘‘How is (Imagined) Speech Produced?’’ offers a staged process with the potential to be mined for more targeted decoding approaches. Models of speech processing, for example, have proposed that accessing the phonological representation of a word releases two kinds of information: a frame that speciﬁes the structure of a word and phonemes to ﬁll slots in this structure (Dell, 1988; Levelt, 1992). An interesting operation referred to as gap ﬁlling (Love et al., 2008) has been observed in studies of lexical priming whereby the meaning of a displaced constituent is activated when it is ﬁrst encountered in a sentence and then reactivated at a site indexed by a trace. Consider the following sentence as an example: ‘‘(The boy)i that the horse chased (t)i is tall.’’ In a case like this, activation

is present for ‘‘boy’’ and again at the gap indexed by ‘‘t,’’ where there is no phonologically realized word. Crucially, there is no activation before the word ‘‘chased,’’ indicating that the activation for ‘‘boy’’ at the gap is not residual activation but the result of reactivation (Love et al., 2008). This may have important implications for the development of a DS-BCI that decodes continuous imagined speech from brain activity, as the neurological basis of syntax requires a complex series of operations not simply based on surface word order. Understanding of the widely distributed brain regions associated with semantic and syntactic processing and speech production (as discussed in sections ‘‘Semantics and the Meaning of Words’’ and ‘‘The Hierarchical Structure of Syntax’’) should be harnessed along with enhanced methods for eliciting imagined speech, to improve the decoding accuracy of DS-BCIs.

Herff et al. (2017) have shown that continuous speech is represented as a sequence of phones within the brain and is thus a legitimate target for DS-BCI research. Following this, it seems reasonable to suggest that concatenation of imagined speech units can be used to produce words and sentences. Perrone-Bertolotti et al. (2014) discuss concerns over the way imagined speech manifests itself and how personal agency or lack thereof leads to different forms of imagined speech. The more active form, described as ‘‘deliberate covert production of speech,’’ is consciously generated speech and the target of DS-BCI research. However, a less deliberate manifestation known as ‘‘verbal mind wandering’’ can occur spontaneously. Despite not being the direct target of DS-BCIs, this second state of imagined speech may inﬂuence the performance of such a device or even activate communication when none was intended.

Leveraging Neurolinguistics Concepts to Improve Discriminability

The ability to effectively discriminate between neural recordings is an essential component of any BCI, and it is a particularly complicated challenge in relation to DS-BCIs, given the complex and dynamic processes of speech production. Decoding brain activity corresponding to imagined speech, given the dense vocabulary and the volume of potential semantic combinations that humans possess is an exceptional challenge. In section ‘‘Semantics and the Meaning of Words,’’ evidence is presented linking different semantic categories to different lesion foci, and semantic categorization of words appears to be a promising method for improving classiﬁcation from a constrained lexicon. Content words, i.e., words with rich semantic meaning (e.g., words referring to tastes, sensations, sounds, or motor activities) have been associated with distinct regions of the brain and may enable classiﬁcation of words based on semantic criteria (Pulvermu¨ ller, 1999). Although this may appear to be a somewhat contrived method for improving accuracy, this approach can help elucidate the degree to which semantic categorization contributes to differentiation between words (Wang et al., 2011). Categorical differences between words can induce signiﬁcantly different brain activity, and this variance may be an aid to classiﬁcation. For example, action words (e.g., kick, throw, blink) can have the effect of activating brain regions actually involved in carrying out the activity (Hauk et al., 2004). Similarly, words corresponding to touch may include signiﬁcant activation in the somatosensory cortices and sound words may cause increased activation in bilateral auditory cortices (Pulvermu¨ ller, 1999).

Imagined speech’s close association with working memory (Marvel and Desmond, 2012), the range of articulatory forms it can take (Alderson-Day et al., 2015; Deng et al., 2010), and the different neural activations it exhibits in relation to overt speech (Basho et al., 2007) contribute to making imagined speech extremely difﬁcult to decode effectively. Methods employed in neurolinguistics can help DS-BCI researchers improve cuing and elicitation techniques, making it easier to determine precisely what is being decoded from brain activity. This may take the form of semantic or phonological priming, as suggested earlier, or improvement of experimental protocols to ensure participants are clear on what is expected from them. It may also be possible to protect against unwanted noise in the data, for example, via articulatory suppression.

The previously stated proposal that each linguistic unit has a unique phonological representation (section ‘‘The Internal Phonological Speech Code’’) is a potential avenue for improving imagined speech discriminability (Zhao and Rudzicz, 2015). Clearly, if the assertion of a unique phonological code is correct, this would be a primary target of DS-BCI decoding approaches, as a single representation corresponding to a single word or phoneme would make those approaches easier to implement, given that the prior stages in the speech production process may not be required. It is the recommendation of this review that further investigation into the potential phonological discriminability of units of imagined speech is pursued.

Although much of the research to date into a possible DS-BCI has focused on discrete linguistic units, i.e., vowels, consonants, it has been suggested that the neural substrates responsible for the representation of phonemes may differ depending on whether they are processed as part of a sequence or processed alone (Ikeda et al., 2014). Di Liberto, O’Sullivan, and Lalor (Di Liberto et al., 2015) lament the lack of research present in the literature regarding the parsing and processing of continuous speech. However, the difﬁculty of experimentation with imagined speech and the impracticality of attempting to decode continuous speech, at a time when decoding discrete units of speech is still enormously challenging, has meant that to date the majority of studies have focused on discrete units of speech in the development of decoding strategies.

If progress is to be made using these approaches, the anatomical information summarized in sections ‘‘Imagined Speech: A Special Case of Speech’’ and ‘‘How is (Imagined) Speech Produced?’’ will be important for informing decoding strategies. Targeting regions of interest speciﬁc to speech production may be a promising approach to the development of a DS-BCI (Guenther et al., 2009), particularly considering that speech processing is a highly distributed operation with semantics, lexical access, syntax, and phonology, all correlated to different regions. Although we agree with Bocquelet et al. (2017) that the LIFG is clearly implicated in imagined speech production, and a promising candidate for DS-BCI research, we think it is important to consider a wider, and probably bilateral, network where the distributed connectivity predicted by Hebbian theory is accounted for. The evidence presented here indicates a wide cortical network associated with different linguistic categories and stages of the speech production process. It is our assertion that a complete picture of the neuroanatomical correlates of imagined speech will provide greater opportunities for effective discriminability.

Mitigating the Limitations of Experimental Methodology

Progress toward a DS-BCI is dependent on the effectiveness of future research methodologies and on novel approaches to system development. It has been noted that researchers seeking to distinguish word classes from neural activation should consider the effect of word length, word frequency, emotional properties of the stimuli, word repetition, priming, and syntactic and semantic context when designing experiments (Pulvermu¨ ller, 1999). The same author also warns of the possible unintended effects of presenting words in sentences or word strings, because the neurophysiological response is a complex blend of the semantic and syntactic interactions of the given words. One of the difﬁculties associated with the development of a DS-BCI is inferring from experimental participants that the required tasks have been performed (Geva et al., 2011b). The lack of behavioral output from participants has meant that researchers have been faced with a choice of whether to accept assertions that a given task has been correctly undertaken, to design their experimental procedure in a manner that will elicit the required imagined speech activity (Geva et al., 2011a), or to merge their imagined speech protocols with an overt action in an attempt at cross-veriﬁcation (Oppenheim and Dell, 2008). Limitations to the scope of empirical study in the case of imagined speech has induced the development of methods for indirect study of the phenomenon (Filik and Barber, 2011; Oppenheim and Dell, 2008). Alderson-Day and Fernyhough (2015) present recent methodological advances in the ﬁeld, including imagined speech inducement and inhibition, as a means of studying its effects.

Neuroimaging studies into the nature of imagined speech have often asked participants to simply articulate some words or sentences in imagined speech or to imagine speech with different characteristics. A danger associated with these studies is the lack of ecological validity in eliciting imagined speech (Alderson-Day and Fernyhough, 2015) and the failure of researchers to acknowledge the possibility that imagined speech is present during baseline assessments (Jones and Fernyhough, 2007). A technique known as articulatory suppression might provide some assistance in ameliorating this issue (Miyake et al., 2004). The evidence presented in section ‘‘The Phenomena of Imagined Speech’’ indicated variation in the phenomena of imagined speech, both in terms of how it is activated and how it is perceived. Studies have shown that imagined speech is not generally understood in the same way by participants and can vary widely in its phenomenology (Alderson-Day and Fernyhough, 2015). It is the job of the DS-BCI researcher to ensure that each participant is well informed before engaging in experimentation. The methodology employed by Geva, Jones, et al. (Geva et al., 2011b) may be an interesting avenue for exploration in DS-BCI research. Their use of rhyming words and/or homophones is commonly applied in linguistics (Badre et al., 2005; Filik and Barber, 2011) to allow researchers to know whether participants are using imagined speech or resorting to other linguistic/cognitive strategies. For example, ‘‘might’’ and ‘‘mite’’ are homophones,

whereas ‘‘ear’’ and ‘‘oar’’ are not. These are tasks that could not be solved by orthography alone and thus require the use of imagined speech.

Research methodology using overt speech to represent imagined speech within experimental paradigms is ﬂawed, at least to some degree. Overt speech–trained models, for example, are an active research area, but it must be understood that neural representations of overt and imagined speech are not identical (Chakrabarti et al., 2015). Hubbard (2010) reﬂects that differences in experimental results between overt and imagined speech may simply be a function of a participant’s ability to self-monitor and report accurately. There is general agreement that overt speech engages greater activation across a broader network of the brain than imagined speech, with areas including the mesial temporal lobe and subcortical structures (Kielar et al., 2011). Owing to some notable differences observed from neural responses in overt and imagined conditions, inferences drawn from language processing studies should be considered with caution (Llorens et al., 2011). However, Iljina et al. (2017) believe that the body of research presented on both overt and imagined speech supports the premise of being able to decode expressive language from neuronal processes as well as translation of ﬁndings from overt to imagined speech.

Experimental results can be negatively affected by experimental conditions, and an alternative approach to improving the robustness of results in relation to speech production and communicative interaction is the use of non-experimental, ‘‘real-world’’ speech (Derix et al., 2014, 2012; Ruescher et al., 2013). Spontaneous language can reﬂect mental states and thus constitutes a fundamental link between externally observable behavior and internal cognitive processes (Derix et al., 2014). Using their methodology, in which simultaneous ECoG and digital video recordings are used to identify periods of spontaneous communication between interlocutors, the group cited earlier has conducted studies based on concepts developed in psycholinguistic research into spontaneously spoken language. The authors highlight the importance of study paradigms in which real-world situations can be investigated in a way not possible under strict experimental procedures. They present the use of stimuli such as naturalistic texts, recordings of interacting individuals, and virtual reality simulations as associated methods being employed elsewhere (Derix

- et al., 2014).

In a series of studies, the research team used their methodology to study the neuronal processes related to real-life communication in a non-experimental scenario (Derix et al., 2014, 2012; Ruescher et al., 2013). This involved a technique for identifying time periods in which patients were involved in conversation with either partners or physicians (Derix et al., 2012). Extracted epochs consisted of periods of natural, uninstructed conversation, with the results indicating that the choice of linguistic and non-linguistic behaviors depends on whom a person is speaking with. The authors suggest that such meta-information may have utility in BCI applications aimed at restoration of expressive speech. Although non-experimental conditions do facilitate the study of spontaneous speech, it is important to acknowledge, as the research team has, that participants’ behavior may be moderated by the knowledge that they are under surveillance, and therefore not completely natural (Derix et al., 2014). However, we agree with Iljina et al. (2017) that a thorough understanding of brain activity during real-world speech is required for the development of truly naturalistic DS-BCI.

As indicated throughout this review, there are several ways in which DS-BCI research can beneﬁt from neurolinguistics research advances. Understanding the phenomena of imagined speech and individual speech processes is crucial, but looking toward neurolinguistics to enhance experimental methodology and interpretation of results is also advocated here. Other avenues exist for exploration of improvements to the performance of DS-BCIs, including signal acquisition and advanced classiﬁcation algorithms, but it would be wrong to ignore the potential utility of cross-disciplinary research in neurolinguistics and DS-BCI.

CONCLUDING REMARKS

Development of a DS-BCI is an extremely challenging undertaking. It is the assertion of this review that a cross-disciplinary approach must be taken to advance the ﬁeld toward a naturalistic form of communication. Here, we advocate the integration of neurolinguistics within the DS-BCI paradigm for the improvement of experimental methodology and to aid approaches to the decoding of neural signals. Insights into the nature of imagined speech and speech production processes can inform research practices,

whereas methodological approaches common in linguistics can help improve procedural robustness in studies involving imagined speech.

Clearly, there is no deﬁnitive description of the phenomena of imagined speech. Independently depicted as a truncated form of overt speech, as showing greater activation in several brain regions than overt speech and as having attenuated features in comparison with overt speech, imagined speech is still relatively poorly understood. Continuing research into imagined speech from a neurolinguistics perspective will be vital for DS-BCI. Imagined speech manifests itself in different forms, whether that be through active or passive generation of imagined speech; through accent, rhythm, or pitch; or through conversational or single-speaker scenarios. That being the case, future research in this ﬁeld must make it abundantly clear to experimental participants precisely what is being asked of them. The ﬁeld of neurolinguistics can help inform DS-BCI research on methods for targeting the imagined speech content required. Not unrelated to this is the potential for additional information to be encoded in the neural recordings extracted during periods of imagined speech production. Working memory and imagined speech appear to be intrinsically linked, and imagined speech trials are susceptible to inﬂuence from the auditory or visual cues presented. It is therefore important that experimental methodologies and decoding approaches mitigate against this unwanted content where possible.

This review has shown that DS-BCI is concerned not only with the phenomena of imagined speech and how it differs from overt speech but also with the neuroanatomy and speciﬁc processes involved in the production of speech. Speech production is a temporal process with a hierarchical structure, and it is clear that it cannot be considered a single function localized in a single brain region. Evidence has been presented from neurolinguistics research to indicate that different systems of speech production, such as semantics and syntax, operate at distinct time periods (sometimes overlapping) across a distributed network of brain regions and that these systems activate patterns of brain activity that may be useful for approaches to decoding imagined speech.

A fully functioning DS-BCI may, at present, seem a long way off, and it may appear that there are more pressing concerns, such as improving signal acquisition, for the ﬁeld to be focused on at present. However, it is our contention that it would be remiss to ignore the ﬁeld of neurolinguistics in DS-BCI research, given the potential beneﬁts it can offer in the short term and the high probability that it will be required in the longer-term development of a naturalistic mode of communication.

## ACKNOWLEDGMENTS

This work is supported by a Department for the Economy studentship, provided by the Northern Ireland Executive.

## AUTHOR CONTRIBUTIONS

Conceptualization, C.C., R.F., and D.C.; writing: original draft, C.C.; writing: review and editing R.F. and D.C.

REFERENCES

Alderson-Day, B., and Fernyhough, C. (2015). Inner speech: development, cognitive functions, phenomenology, and neurobiology. Psychol. Bull. 141, 931–965.

Alderson-Day, B., Weis, S., McCarthy-Jones, S., Moseley, P., Smailes, D., and Fernyhough, C.

(2015). The brain’s conversation with itself: neural substrates of dialogic inner speech. Soc. Cogn. Affect. Neurosci. 11, 110–120.

Aleman, A., Formisano, E., Koppenhagen, H., Hagoort, P., De Haan, E.H.F., and Kahn, R.S.

(2005). The functional neuroanatomy of metrical stress evaluation of perceived and imagined spoken words. Cereb. Cortex 15, 221–228.

AlSaleh, M.M., Arvaneh, M., Christensen, H., Moore, R.K., 2016. Brain-computer interface

technology for speech recognition: a review. Asia-Paciﬁc Signal Inf. Process. Assoc. Annu. Summit Conf. (APSIPA ASC 2016).

Baddeley, A.D., Thomson, N., and Buchanan, M.

(1975). Word length and the structure of shortterm memory. J. Verbal Learn. Verbal Behav. 14, 575–589.

Badre, D., Poldrack, R.A., Pare´-Blagoev, E.J., Insler, R.Z., and Wagner, A.D. (2005). Dissociable controlled retrieval and generalized selection mechanisms in ventrolateral prefrontal cortex. Neuron 47, 907–918.

Basho, S., Palmer, E.D., Rubio, M.A., Wulfeck, B., and Mu¨ller, R.A. (2007). Effects of generation mode in fMRI adaptations of semantic ﬂuency:

paced production and overt speech. Neuropsychologia 45, 1697–1706.

Bates, E., Wilson, S.M., Saygin, A.P., Dick, F., Sereno, M.I., Knight, R.T., and Dronkers, N.F. (2003). Voxel-based lesion–symptom mapping. Nat. Neurosci. 6, 448–450.

Benetello, A., Finocchiaro, C., Capasso, R., Capitani, E., Laiacona, M., Magon, S., and Miceli, G. (2016). The dissociability of lexical retrieval and morphosyntactic processes for nouns and verbs: a functional and anatomoclinical study. Brain Lang. 159, 11–22.

Berwick, R.C., Friederici, A.D., Chomsky, N., and Bolhuis, J.J. (2013). Evolution, brain, and the nature of language. Trends Cogn. Sci. 17, 89–98.

Bin, G., Gao, X., Yan, Z., Hong, B., and Gao, S.

(2009). An online multi-channel SSVEP-based brain-computer interface using a canonical correlation analysis method. J. Neural Eng. 6, 046002.

Blakely, T., Miller, K.J., Rao, R.P.N., Holmes, M.D., and Ojemann, J.G. (2008). Localization and classiﬁcation of phonemes using high spatial resolution electrocorticography (ECoG) grids. Conf. IEEE Eng. Med. Biol. Soc. 2008, 4964–4967. Bocquelet, F., Hueber, T., Girin, L., Chabarde`s, S., and Yvert, B. (2017). Key considerations in designing a speech brain-computer interface. J. Physiol. 110, 392–401. Bouchard, K.E., and Chang, E.F. (2014). Neural decoding of spoken vowels from human sensorymotor cortex with high-density electrocorticography. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 6782–6785. Bouton, C.E., Shaikhouni, A., Annetta, N.V., Bockbrader, M.A., Friedenberg, D.A., Nielson, D.M., Sharma, G., Sederberg, P.B., Glenn, B.C., Mysiw, W.J., et al. (2016). Restoring cortical control of functional movement in a human with quadriplegia. Nature 533, 247–250.

Brigham, K., Kumar, B.V.K.V., 2010. Imagined speech classiﬁcation with EEG signals for silent communication: a preliminary investigation into synthetic telepathy. 2010 4th Int. Conf. Bioinforma. Biomed. Eng. iCBBE 2010. 1–4.

Brocklehurst, P.H., and Corley, M. (2011). Investigating the inner speech of people who stutter: evidence for (and against) the covert repair hypothesis. J. Commun. Disord. 44, 246–260.

Brumberg, J.S., Krusienski, D.J., Chakrabarti, S., Gunduz, A., Brunner, P., Ritaccio, A.L., and Schalk, G. (2016). Spatio-temporal progression of cortical activity related to continuous overt and covert speech production in a reading task. PLoS One 11, 1–21.

Brumberg, J.S., Wright, E.J., Andreasen, D.S., Guenther, F.H., and Kennedy, P.R. (2011). Classiﬁcation of intended phoneme production from chronic intracortical microelectrode recordings in speech-motor cortex. Front. Neurosci. 5, 1–12.

Chakrabarti, S., Sandberg, H.M., Brumberg, J.S., and Krusienski, D.J. (2015). Progress in speech decoding from the electrocorticogram. Biomed. Eng. Lett. 5, 10–21.

Chaudhary, U., Xia, B., Silvoni, S., Cohen, L.G., and Birbaumer, N. (2017). Brain–computer interface–based communication in the completely locked-in state. PLoS Biol. 15, 1–25.

Chi, X., Hagedorn, J.B., Schoonover, D., and Zmura, M.D. (2011). EEG-based discrimination of imagined speech phonemes. Int. J. Bioelectromagn. 13, 201–206.

Corley, M., Brocklehurst, P.H., and Moat, H.S. (2011). Error biases in inner and overt speech: evidence from tongue twisters. J. Exp. Psychol. Learn. Mem. Cogn. 37, 162–175.

D’albis, T., Blatt, R., Tedesco, R., Sbattella, L., and Matteucci, M. (2012). A predictive speller controlled by a brain-computer interface based

on motor imagery. ACM Trans. Comput. Interact. 19, 1–25.

D’Zmura, M., Deng, S., Lappas, T., Thorpe, S., and Srinivasan, R. (2009). Toward {EEG} sensing of imagined speech. Hum. Comput. Interact. Part I 5610, 40–48.

DaSalla, C.S., Kambara, H., Sato, M., and Koike, Y.

- (2009). Single-trial classiﬁcation of vowel speech imagery using common spatial patterns. Neural Netw. 22, 1334–1339.

Dell, G.S. (1988). The retrieval of phonological forms in production: tests of predictions from a connectionist model. J. Mem. Lang. 27, 124–142. Dell, G.S., Martin, N., and Schwartz, M.F. (2007). A case-series test of the interactive two-step model of lexical access: predicting word repetition from picture naming. J. Mem. Lang. 56, 490–520. Denby, B., Oussar, Y., Dreyfus, G., Stone, M.,

2006. Prospects for a silent speech interface using ultrasound imaging. Proc. 2006 IEEE Int. Conf. Acoust. Speed Signal Process. Proc. 1, I-365-I368.

Deng, S., Srinivasan, R., Lappas, T., and D’Zmura, M. (2010). EEG classiﬁcation of imagined syllable rhythm using Hilbert spectrum methods. J. Neural Eng. 7, 046006.

Derix, J., Iljina, O., Schulze-Bonhage, A., Aertsen, A., and Ball, T. (2012). ‘‘Doctor’’ or ‘‘darling’’? decoding the communication partner from ECoG of the anterior temporal lobe during nonexperimental, real-life social interaction. Front. Hum. Neurosci. 6, 1–14.

Derix, J., Iljina, O., Weiske, J., Schulze-Bonhage, A., Aertsen, A., and Ball, T. (2014). From speech to thought: the neuronal basis of cognitive units in non-experimental, real-life communication investigated using ECoG. Front. Hum. Neurosci. 8, 1–17.

Di Liberto, G.M., O’Sullivan, J.A., and Lalor, E.C.

(2015). Low-frequency cortical entrainment to speech reﬂects phoneme-level processing. Curr. Biol. 25, 2457–2465.

Dolcos, S., and Albarracin, D. (2014). The inner speech of behavioral regulation: intentions and task performance strengthen when you talk to yourself as a You. Eur. J. Soc. Psychol. 44, 636–642.

Donchin, E., Spencer, K.M., and Wijesinghe, R.

(2000). The mental prosthesis: assessing the speed of a P300-based brain- computer interface. IEEE Trans. Rehabil. Eng. 8, 174–179.

Edwards, E., Nagarajan, S.S., Dalal, S.S., Canolty, R.T., Kirsch, H.E., Barbaro, N.M., and Knight, R.T.

- (2010). Spatiotemporal imaging of cortical activation during verb generation and picture naming. Neuroimage 50, 291–301.

Emerson, M.J., and Miyake, A. (2003). The role of inner speech in task switching: a dual-task investigation. J. Mem. Lang. 48, 148–168.

Fargier, R., Bu¨rki, A., Pinet, S., Alario, F.X., and Laganaro, M. (2018). Word onset phonetic properties and motor artifacts in speech production EEG recordings. Psychophysiology 55, 1–10.

Fernyhough, C. (2004). Alien voices and inner dialogue: towards a developmental account of auditory verbal hallucinations. New Ideas Psychol. 22, 49–68.

Filik, R., and Barber, E. (2011). Inner speech during silent reading reﬂects the reader’s regional accent. PLoS One 6, e2782.

Frazier, L. (1987). Sentence processing: a tutorial review. In Attention and Performance 12: The Psychology of Reading, M. Coltheart, ed. (Lawrence Erlbaum Associates, Inc), pp. 559–586.

Friederici, A.D. (2018). The neural basis for human syntax: Broca’s area and beyond. Curr. Opin. Behav. Sci. 21, 88–92.

Friederici, A.D. (2011). The brain basis of language processing: from structure to function. Physiol. Rev. 91, 1357–1392.

Friederici, A.D. (2002). Towards a neural basis of auditory sentence processing. Trends Cogn. Sci. 6, 78–84.

Geva, S., Bennett, S., Warburton, E.A., and Patterson, K. (2011a). Discrepancy between inner and overt speech: implications for post-stroke aphasia and normal language processing. Aphasiology 25, 323–343.

Geva, S., Jones, P.S., Crinion, J.T., Price, C.J., Baron, J.C., and Warburton, E.A. (2011b). The neural correlates of inner speech deﬁned by voxel-based lesion-symptom mapping. Brain 134, 3071–3082.

Gilbert, J.M., Rybchenko, S.I., Hofe, R., Ell, S.R., Fagan, M.J., Moore, R.K., and Green, P. (2010). Isolated word recognition of silent speech using magnetic implants and sensors. Med. Eng. Phys. 32, 1189–1197.

Gonza´lez-Castan˜eda, E.F., Torres-Garcı´a, A.A., Reyes-Garcı´a, C.A., and Villasen˜or-Pineda, L.

(2017). Soniﬁcation and textiﬁcation: proposing methods for classifying unspoken words from EEG signals. Biomed. Signal Process. Control 37, 82–91.

Goto, T., Hirata, M., Umekawa, Y., Yanagisawa, T., Shayne, M., Saitoh, Y., Kishima, H., Yorifuji, S., and Yoshimine, T. (2011). Frequency-dependent spatiotemporal distribution of cerebral oscillatory changes during silent reading: a magnetoencephalograhic group analysis. Neuroimage 54, 560–567.

Guenther, F.H., Brumberg, J.S., Joseph Wright, E., Nieto-Castanon, A., Tourville, J.A., Panko, M., Law, R., Siebert, S.A., Bartels, J.L., Andreasen, D.S., et al. (2009). A wireless brain-machine interface for real-time speech synthesis. PLoS One 4, e8218.

Hashim, N., Ali, A., and Mohd-Isa, W.-N. (2018). Word-based classiﬁcation of imagined speech using EEG. In Computational Science and Technology, R. Alfred, H. Iida, A.A. Ag Ibrahim, and Y. Lim, eds. (Springer Singapore), pp. 195–204.

Hauk, O., Johnsrude, I., and Pulvermu¨ller, F.

(2004). Somatotopic representation of action words in human motor and premotor cortex. Neuron 41, 301–307.

Henseler, I., Regenbrecht, F., and Obrig, H.

(2014). Lesion correlates of patholinguistic proﬁles in chronic aphasia: comparisons of syndrome-, modality-and symptom-level assessment. Brain 137, 918–930.

Herff, C., de Pesters, A., Heger, D., Brunner, P., Schalk, G., and Schultz, T. (2017). Towards continuous speech recognition for {BCI}. In BrainComputer Interface Research. A State-of-the-Art Summary 5, C. Guger, B. Allison, and J. Ushiba, eds. (Springer International Publishing), pp. 21–29.

Herff, C., Heger, D., de Pesters, A., Telaar, D., Brunner, P., Schalk, G., and Schultz, T. (2015). Brain-to-text: decoding spoken phrases from phone representations in the brain. Front. Neurosci. 9, 1–11.

Herff, C., Johnson, G., Diener, L., Shih, J., Krusienski, D., and Schultz, T. (2016). Towards direct speech synthesis from ECoG: a pilot study. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2016, 1540– 1543.

Herff, C., Putze, F., Heger, D., Guan, C., and Schultz, T. (2012). Speaking mode recognition from functional near infrared spectroscopy. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 1715–1718.

Hickok, G. (2014). The architecture of speech production and the role of the phoneme in speech processing. Lang. Cogn. Neurosci. 29, 2–20.

Hickok, G. (2012). Computational neuroanatomy of speech production. Nat. Rev. Neurosci. 13, 135–145.

Hickok, G., and Poeppel, D. (2007). The cortical organization of speech processing. Nat. Rev. Neurosci. 8, 393–402.

Hirshorn, E.A., and Thompson-Schill, S.L. (2006). Role of the left inferior frontal gyrus in covert word retrieval: neural correlates of switching during verbal ﬂuency. Neuropsychologia 44, 2547–2557.

Hochberg, L.R., Bacher, D., Jarosiewicz, B., Masse, N.Y., Simeral, J.D., Vogel, J., Haddadin, S., Liu, J., Cash, S.S., Van Der Smagt, P., and Donoghue, J.P. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485, 372–375.

Huang, J., Carr, T.H., and Cao, Y. (2002). Comparing cortical activations for silent and overt speech using event-related fMRI. Hum. Brain Mapp. 15, 26–38.

Hubbard, T.L. (2010). Auditory imagery: empirical ﬁndings. Psychol. Bull. 136, 302–329.

Hurlburt, R.T., Alderson-Day, B., Kuhn, S., and Fernyhough, C. (2016). Exploring the ecological validity of thinking on demand: neural correlates of elicited vs. spontaneously occurring inner speech. PLoS One 11, 1–16.

Hurlburt, R.T., Heavey, C.L., and Kelsey, J.M.

- (2013). Toward a phenomenology of inner speaking. Conscious. Cogn. 22, 1477–1494.

Ibayashi, K., Kunii, N., Matsuo, T., Ishishita, Y., Shimada, S., Kawai, K., and Saito, N. (2018). Decoding speech with integrated hybrid signals recorded from the human ventral motor cortex. Front. Neurosci. 12, 221.

Idrees, B.M., Farooq, O., 2016. EEG based vowel classiﬁcation during speech imagery. 2016 3rd Int. Conf. Comput. Sustain. Glob. Dev. 1130–1134.

Ikeda, S., Shibata, T., Nakano, N., Okada, R., Tsuyuguchi, N., Ikeda, K., and Kato, A. (2014). Neural decoding of single vowels during covert articulation using electrocorticography. Front. Hum. Neurosci. 8, 1–8.

Iljina, O., Derix, J., Schirrmeister, R.T., SchulzeBonhage, A., Auer, P., Aertsen, A., and Ball, T. (2017). Neurolinguistic and machine-learning perspectives on direct speech BCIs for restoration of naturalistic communication. Brain Computer Interfaces 4, 186–199.

Indefrey, P. (2011). The spatial and temporal signatures of word production: a critical update. Front. Psychol. 2, 255.

Indefrey, P., Brown, C.M., Hellwig, F., Amunts, K., Herzog, H., Seitz, R.J., and Hagoort, P. (2001). A neural correlate of syntactic encoding during speech production. Proc. Natl. Acad. Sci. U S A 98, 5933–5936.

Indefrey, P., and Levelt, W.J.M. (2004). The spatial and temporal signatures of word production components. Cognition 92, 101–144.

Iqbal, S., Khan, Y.U., Farooq, O., 2015a. EEG based classiﬁcation of imagined vowel sounds. 2015 2nd Int. Conf. Comput. Sustain. Glob. Dev. 1591–1594.

Iqbal, S., Shanir, P.P.M., Khan, Y.U.K., Farooq, O., 2015b. Time domain analysis of EEG to classify imagined speech. Proc. Second Int. Conf. Comput. Commun. Technol. Adv. Intell. Syst. Comput. 380, 793–800.

Jackendoff, R. (2007). A parallel architecture perspective on language processing. Brain Res. 1146, 2–22.

Jones, S.R., and Fernyhough, C. (2007). Neural correlates of inner speech and auditory verbal hallucinations: a critical review and theoretical integration. Clin. Psychol. Rev. 27, 140–154.

Kanas, V.G., Mporas, I., Benz, H.L., Sgarbas, K.N., Bezerianos, A., and Crone, N.E. (2014). Joint spatial-spectral feature space clustering for speech activity detection from ECoG signals. IEEE Trans. Biomed. Eng. 61, 1241–1250.

Kellis, S., Miller, K., Thomson, K., Brown, R., House, P., and Greger, B. (2010). Decoding spoken words using local ﬁeld potentials recorded from the cortical surface. J. Neural Eng. 7, 056007.

Kielar, A., Milman, L., Bonakdarpour, B., and Thompson, C.K. (2011). Neural correlates of covert and overt production of tense and agreement morphology: evidence from fMRI. J. Neurolinguist. 24, 183–201.

Kim, T., Lee, J., Choi, H., Lee, H., Kim, I.Y., Jang, D.P., 2013. Meaning based covert speech classiﬁcation for brain-computer interface based on electroencephalography. Int. IEEE/EMBS Conf. Neural Eng. NER. 53–56.

Lambon Ralph, M.A., Moriarty, L., Sage, K., Ackerman, T., Arul, K., Bird, H., Crisp, J., Davies, S., Ellis, A., and Harold, R. (2002). Anomia is simply a reﬂection of semantic and phonological

impairments: evidence from a case-series study. Aphasiology 16, 56–82.

Leuthardt, E.C., Gaona, C., Sharma, M., Szrama, N., Roland, J., Freudenberg, Z., Solis, J., Breshears, J., and Schalk, G. (2011). Using the electrocorticographic speech network to control a brain–computer interface in humans. J. Neural Eng. 8, 036004.

Levelt, W.J.M. (1989). Speaking: From Intention to Articulation (The MIT Press).

Levelt, W.J.M. (1999). Models of word production. Trends Cogn. Sci. 3, 223–232.

Levelt, W.J.M. (1992). Accessing words in speech production: stages, processes and representations. Cognition 42, 1–22.

Levelt, W.J.M., Roelofs, A., and Meyer, A.S.

(1999). A theory of lexical access in speech production. Behav. Brain Sci. 22, 1–75.

Livezey, J.A., Bouchard, K.E., and Chang, E.F. (2018). Deep learning as a tool for neural data analysis: speech classiﬁcation and crossfrequency coupling in human sensorimotor cortex, pp. 1–23, https://arxiv.org/abs/1803. 09807.

Llorens, A., Tre´buchon, A., Lie´geois-Chauvel, C., and Alario, F.X. (2011). Intra-cranial recordings of brain activity during language production. Front. Psychol. 2, 1–12.

Lotte, F., Brumberg, J.S., Brunner, P., Gunduz, A., Ritaccio, A.L., Guan, C., and Schalk, G. (2015). Electrocorticographic representations of segmental features in continuous speech. Front. Hum. Neurosci. 09, 1–13.

Love, T., Swinney, D., Walenski, M., and Zurif, E.

(2008). How left inferior frontal cortex participates in syntactic processing: evidence from aphasia. Brain Lang. 107, 203–219.

MacKay, D.G. (1992). Constraints on theories of inner speech. In Auditory Imagery, D. Reisberg, ed. (Lawrence Erlbaum Associates, Inc), pp. 121–149.

Mainy, N., Jung, J., Baciu, M., Kahane, P., Schoendorff, B., Minotti, L., Hoffmann, D., Bertrand, O., and Lachaux, J.P. (2008). Cortical dynamics of word recognition. Hum. Brain Mapp. 29, 1215–1230.

Martin, S., Brunner, P., Holdgraf, C., Heinze, H.-J., Crone, N.E., Rieger, J., Schalk, G., Knight, R.T., and Pasley, B.N. (2014). Decoding spectrotemporal features of overt and covert speech from the human cortex. Front. Neuroeng. 7, 14.

Martin, S., Brunner, P., Iturrate, I., Milla´n, J.d R., Schalk, G., Knight, R.T., and Pasley, B.N. (2016). Word pair classiﬁcation during imagined speech using direct brain recordings. Sci. Rep. 6, 25803.

Martı´nez-Manrique, F., and Vicente, A. (2015). The activity view of inner speech. Front. Psychol. 6, 1–13.

Marvel, C.L., and Desmond, J.E. (2012). From storage to manipulation: how the neural correlates of verbal working memory reﬂect varying demands on inner speech. Brain Lang. 120, 42–51.

McGuire, P.K., Silbersweig, D.A., Murray, R.M., David, A.S., Frackowiak, R.S.J., and Frith, C.D.

- (1996a). Functional anatomy of inner speech and auditory verbal imagery. Psychol. Med. 26, 29–38.

McGuire, P.K., Silbersweig, D.A., Wright, I., Murray, R.M., Frackowiak, R.S., and Frith, C.D.

- (1996b). The neural correlates of inner speech and auditory verbal imagery in schizophrenia: relationship to auditory verbal hallucinations. Br. J. Psychiatry 169, 148–159.

Miyake, A., Emerson, M.J., Padilla, F., and Ahn, J.C. (2004). Inner speech as a retrieval aid for task goals: the effects of cue type and articulatory suppression in the random task cuing paradigm. Acta Psychol. (Amst) 115, 123–142.

Mohr, B., Pulvermu¨ller, F., Mittelsta¨dt, K., and Rayman, J. (1996). Multiple simultaneous stimulus presentation facilitates lexical processing. Neuropsychologia 34, 1003–1013.

Morin, A., and Michaud, J. (2007). Self-awareness and the left inferior frontal gyrus: inner speech use during self-related processing. Brain Res. Bull. 74, 387–396.

Moses, D.A., Leonard, M.K., and Chang, E.F.

(2018). Real-time classiﬁcation of auditory sentences using evoked cortical activity in humans. J. Neural Eng. 15, 036005.

Mugler, E.M., Goldrick, M., and Slutzky, M.W.

- (2014a). Cortical encoding of phonemic context during word production. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2014, 6790–6793.

Mugler, E.M., Patton, J.L., Flint, R.D., Wright, Z.A., Schuele, S.U., Rosenow, J., Shih, J.J., Krusienski, D.J., and Slutzky, M.W. (2014b). Direct classiﬁcation of all American English phonemes using signals from functional speech motor cortex. J. Neural Eng. 11, 035015.

Nguyen, C.H., Karavas, G., and Artemiadis, P.

(2017). Inferring imagined speech using EEG signals: a new approach using Riemannian Manifold features. J. Neural Eng. 15, 016002.

Oken, B.S., Orhan, U., Roark, B., Erdogmus, D., Fowler, A., Mooney, A., Peters, B., Miller, M., and Fried-Oken, M.B. (2014). Brain–computer interface with language model– electroencephalography fusion for locked-in syndrome. Neurorehabil. Neural Repair 28, 387–394.

Oppenheim, G.M., and Dell, G.S. (2010). Motor movement matters: the ﬂexible abstractness of inner speech. Mem. Cognit. 38, 1147–1160.

Oppenheim, G.M., and Dell, G.S. (2008). Inner speech slips exhibit lexical bias, but not the phonemic similarity effect. Cognition 106, 528–537.

Palmer, E.D., Rosen, H.J., Ojemann, J.G., Buckner, R.L., Kelley, W.M., and Petersen, S.E.

(2001). An event-related fMRI study of overt and covert word stem completion. Neuroimage 14, 182–193.

Pandarinath, C., Nuyujukian, P., Blabe, C.H., Sorice, B.L., Saab, J., Willett, F.R., Hochberg, L.R., Shenoy, K.V., and Henderson, J.M. (2017). High performance communication by people with paralysis using an intracortical brain-computer interface. Elife 6, 1–27.

Paulesu, E., Frith, C.D., and Frackowiak, R.S.J.

(1993). The neural correlates of the verbal component of working memory. Nature 361, 342–345.

Paulesu, E., Goldacre, B., Scifo, P., Cappa, S.F., Gilardi, M.C., Castiglioni, I., Perani, D., and Fazio,

- F. (1997). Functional heterogeneity of left inferior frontal cortex as revealed by fMRI. Neuroreport 8, 2011–2017. Pei, X., Barbour, D.L., Leuthardt, E.C., and Schalk,
- G. (2011a). Decoding vowels and consonants in spoken and imagined words using electrocorticographic signals in humans. J. Neural Eng. 8, 046028.

Pei, X., Leuthardt, E.C., Gaona, C.M., Brunner, P., Wolpaw, J.R., and Schalk, G. (2011b). Spatiotemporal dynamics of electrocorticographic high gamma activity during overt and covert word repetition. Neuroimage 54, 2960–2972.

Perrone-Bertolotti, M., Rapin, L., Lachaux, J.-P., and Lœvenbruck, H. (2014). What is that little voice inside my head? Inner speech phenomenology, its role in cognitive performance, and its relation to self-monitoring. Behav. Brain Res. 261, 220–239.

Pickering, M.J., and Garrod, S. (2013). An integrated theory of language production and comprehension. Behav. Brain Sci. 36, 329–347.

Pin˜ango, M.M., Winnick, A., Ullah, R., and Zurif, E. (2006). Time-course of semantic composition: the case of aspectual coercion. J. Psycholinguist. Res. 35, 233–244.

Porbadnigk, A., Wester, M., Calliess, J., Schultz, T., 2009. EEG-based speech recognition impact of temporal effects. Int. Conf. Bio-inspired Syst. Signal Process.

Price, C.J. (2012). A review and synthesis of the ﬁrst 20years of PET and fMRI studies of heard speech, spoken language and reading. Neuroimage 62, 816–847.

Pulvermu¨ller, F. (2005). Brain mechanisms linking language and action. Nat. Rev. Neurosci. 6, 576–582.

Pulvermu¨ller, F. (1999). Words in the brain’s language. Behav. Brain Sci. 22, 253–336.

Ramsey, N.F., Salari, E., Aarnoutse, E.J., Vansteensel, M.J., Bleichner, M.B., and Freudenburg, Z.V. (2017). Decoding spoken phonemes from sensorimotor cortex with high-density ECoG grids. Neuroimage 180, 301–311.

Rezazadeh Sereshkeh, A., Trott, R., Bricout, A., Chau, T., 2017a. EEG classiﬁcation of covert speech using regularized neural networks. IEEE/ ACM Trans. Audio Speech Lang. Process. 25, 2292–2300.

Rezazadeh Sereshkeh, A., Trott, R., Bricout, A., and Chau, T. (2017b). Online EEG classiﬁcation of covert speech for brain–computer interfacing. Int. J. Neural Syst. 27, 1750033.

Rie`s, S.K., Dhillon, R.K., Clarke, A., KingStephens, D., Laxer, K.D., Weber, P.B., Kuperman, R.A., Auguste, K.I., Brunner, P., Schalk, G., et al. (2017). Spatiotemporal dynamics

of word retrieval in speech production revealed by cortical high-frequency band activity. Proc. Natl. Acad. Sci. U S A 114, E4530–E4538. Ruescher, J., Iljina, O., Altenmu¨ller, D.M., Aertsen, A., Schulze-Bonhage, A., and Ball, T.

(2013). Somatotopic mapping of natural upperand lower-extremity movements and speech production with high gamma electrocorticography. Neuroimage 81, 164–177.

Scott, M., Yeung, H.H., Gick, B., and Werker, J.F.

(2013). Inner speech captures the perception of external speech. J. Acoust. Soc. Am. 133, EL286– EL292.

Sedivy, J. (2014). Language in Mind: An Introduction to Psycholinguistics (Sinauer Associates).

Segalowitz, S.J., and Lane, K. (2004). Perceptual ﬂuency and lexical access for function versus content words. Behav. Brain Sci. 27, 2018.

Shergill, S., and Bullmore, E. (2001). A functional study of auditory verbal imagery. Psychol. Med. 31, 241–253.

Shergill, S.S., Brammer, M.J., Fukuda, R., Bullmore, E., Amaro, E., Murray, R.M., and McGuire, P.K. (2002). Modulation of activity in temporal cortex during generation of inner speech. Hum. Brain Mapp. 16, 219–227.

Shuster, L.I., and Lemieux, S.K. (2005). An fMRI investigation of covertly and overtly produced mono- and multisyllabic words. Brain Lang. 93, 20–31.

Song, Y., Sepulveda, F., 2014. Classifying speech related vs. idle state towards onset detection in brain-computer interfaces overt, inhibited overt, and covert speech sound production vs. idle state. IEEE 2014 Biomed. Circuits Syst. Conf. BioCAS 2014-Proc. 568–571.

Stark, B.C., Geva, S., and Warburton, E.A. (2017). Inner speech’s relationship with overt speech in poststroke aphasia. J. Speech Lang. Hear. Res. 26, 1–10.

Szekely, A., D’Amico, S., Devescovi, A., Federmeier, K., Herron, D., Iyer, G., Jacobsen, T., Are´valo, A.L., Vargha, A., and Bates, E.

(2005). Timed action and object naming. Cortex 41, 7–25.

- Tabar, Y.R., and Halici, U. (2017a). A novel deep learning approach for classiﬁcation of EEG motor imagery signals. J. Neural Eng. 14, 016003.
- Tabar, Y.R., and Halici, U. (2017b). Brain computer interfaces for silent speech. Eur. Rev. 25, 208–230.

Tian, X., and Poeppel, D. (2013). The effect of imagination on stimulation: the functional speciﬁcity of efference copies in speech processing. J. Cogn. Neurosci. 25, 1020–1036.

Torres-Garcı´a, A.A., Reyes-Garcı´a, C.A., Villasen˜or-Pineda, L., and Garcı´a-Aguilar, G.

(2016). Implementing a fuzzy inference system in a multi-objective EEG channel selection model for imagined speech classiﬁcation. Expert Syst. Appl. 59, 1–12.

Vigneau, M., Beaucousin, V., Herve´, P.Y., Duffau, H., Crivello, F., Houde´, O., Mazoyer, B., and

Tzourio-Mazoyer, N. (2006). Meta-analyzing left hemisphere language areas: phonology, semantics, and sentence processing. Neuroimage 30, 1414–1432.

Wang, W., Degenhart, A.D., Sudre, G.P., Pomerleau, D.A., and Tyler-Kabara, E.C. (2011). Decoding semantic information from human electrocorticographic (ECoG) signals. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2011, 6294– 6298.

Wang, Y.Y., Wang, P., and Yu, Y. (2018). Decoding English alphabet letters using EEG phase information. Front. Neurosci. 12, 1–10.

Wheeldon, L.R., and Levelt, W.J.M. (1995). Monitoring the time course of phonological encoding. J. Mem. Lang. 34, 311–334.

Whitney, C., Kirk, M., O’Sullivan, J., Lambon Ralph, M.A., and Jefferies, E. (2012). Executive

semantic processing is underpinned by a largescale neural network: revealing the contribution of left prefrontal, posterior temporal, and parietal cortex to controlled retrieval and selection using TMS. J. Cogn. Neurosci. 24, 133–147.

Wildgruber, D., Ackermann, H., and Grodd, W.

(2001). Differential contributions of motor cortex, basal ganglia, and cerebellum to speech motor control: effects of syllable repetition rate evaluated by fMRI. Neuroimage 13, 101–109.

Yoshimura, N., Nishimoto, A., Belkacem, A.N., Shin, D., Kambara, H., Hanakawa, T., and Koike, Y.

(2016). Decoding of covert vowel articulation using electroencephalography cortical currents. Front. Neurosci. 10, 1–15.

Zaccarella, E., and Friederici, A.D. (2016). The neurobiological nature of syntactic hierarchies. Neurosci. Biobehav. Rev. 81, 205–212.

Zaccarella, E., and Friederici, A.D. (2015). Merge in the human brain: a sub-region based functional investigation in the left pars opercularis. Front. Psychol. 6, 1–9.

Zatorre, R.J., and Halpern, A.R. (2005). Mental concerts: musical imagery and auditory cortex. Neuron 47, 9–12.

Zhang, D., Gong, E., Wu, W., Lin, J., Zhou, W., and Hong, B. (2012). Spoken sentences decoding based on intracranial high gamma response using dynamic time warping. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 3292– 3295.

Zhao, S., Rudzicz, F., 2015. Classifying phonological categories in imagined and articulated speech. ICASSP, IEEE Int. Conf. Acoust. Speech Signal Process. - Proc. 2015, 992–996.

