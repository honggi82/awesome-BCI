[Figure 1]

I!1ternationa~ J9urna1ofInn9V!1tive co.mputing

Jnfc!rmαtionαndControl

ICICInternational@2008ISSN1349-4198

VoluIne4，-Number10，October2008

L

pp. 2617-2680

PATTERNRECOGNITIONOFEEGSIGNALDURINGMOTOR IMAGERYBYUSINGSOM

TOMONARIYAMAGUCHI，KOICHINAGATA，PHAMQUANGTRUONG MITSUHIKOFUJIOANDKATSUHIROINOUE

DepartmentofSystemsD白 ignandInformati岱

KyushuInstituteofTechnology 68ι4Kawazu，Iizuka，Fukuoka，820-8502，Japan

Lyamagu@k恒ir凶i.印ces.k守yut旬ech.a配c.j伊p;{inoue町;lf白何u吋ljiぬo}@ces.kyu叫凶1te配ch.ac.j

GERτT、PFURTSCHELLER LaboratoryofBrain-ComputerInterface GrazUniversityofTechnology Graz，Austria pfurtscheller@tugraz.at ReceivedJanuary2008;revisedMay2008

ABSTRACT. Electroencephalogmph (EEG)reco吋ingsd包吋ngrightαndlejthαndmotor 'imageryαcnbeusedt omoveαcursortoαtαrgetonαcomputerscreen. SuchanEEGbasedbrain-computerinterfiαce (BCI) canprovide anewcommunication chαnnelto何' placeanimpai陀 dmotorfunction. I tαcnbeusedbye.g・，handicapuserswithamyotrophic αlteralsclerosis (ALS). Theconventionalmethodpurposestherecognitionofrighthαnd αndlejthαndmotorimαgery・Inthisωork，featu陀 extractionmethodbasedon8elfOrga・

nizingMα，.p s(80M)usingauto・regressive(AR)spectrumωαsintroducedtodiscriminate theEEGsignals陀 cordeddU1ing吋ghthαnd，l.eβhandandfootmotorimαgery・Mapstructureお investigαted加 ordertodevelopaBCIsystemwhichextractsphysicallymeaningful information d-irectly陀 levanttomotorimagery. Theαnalysismethods ofEEGsignαl s α陀 discussedthrough仇eexperimentalstudies.

Keywords:EEG，AR-model，Braincomputerinterface，Motorimagery，SOM

- 1 .Introduction. InhumanEEG，iti sknownthat responsewaveformssuch鎚󠄀 visual andaudialevokedresponsesrespectivelycausedbyphoticandauditorystimuliappearand thatbeingrequiredselectivereactionsforseveralsortsofstimuli，eventrelatedpotentials are observed [6] . I ti salso knownthat whenaperson i sgoing to movealimb，event relatedsynchronizationjdesynchronization (ERDjERS)andotherrelevanteventrelated potentials are observed in EEG.In particular，event related potentials are knownto beobserved even he only intends to movehis limb without actual movement. These factsmeanthatinformationaboutchangesofhumanbrainactivityincognitiveprocess ormovementdecisionprocess arecontainedintheobservedEEGandsuggest thatthe extractionofthisinformationenableustoguessfromEEGofapersonwhathei sgoing todo. Accordingtothisprincipal，BrainComputerInterface(BCI) actualizescomputer interfaceforhandicappedpersonsandhasbeenrapidlyprogressingrecently[9][11].

TherearetwotypesofactualizationsofBCI，i.e.，invasiveandnon-invasiveones.InvasiveBCIsmakeuseofelectrocorticogram(ECoG)measuredfromelectrodesimplanted directlyintothebrainandhave制 1advantagetoobtaintheelectricactivityofthecortex without noiseor power decreasing but haveasurgical infection risk [8] . Ontheother

2617

[Figure 2]

2618 T.YAMAGUCHI，ETAL.

hand，asnon-invasiveBCIs，magnetoencephalography (MEG)，functionalmagneticresか nanceimaging(flvIRI)，opticaltopographyandBCIusingEEGareknown. Amongthem， theBCIusing EEGmeasured仕omelectrodesattachedto thescalpi sinexpensiveand widelyresearched. Forexample，theresearchgroupofJ .R.WolpawatWordsworthCenter (USA)hasdevelopedBCIsystemswhichcontrol2-dimensionalmovement(up-down andleft-right) ofacomputercursor byidentifyingchanges in the brain signalsduring leftandrighthandmotorimagery，orselectcharactersdisplayedbydetectingP300event related potential relevant to reco伊比ion[10].Onthe other hand，the research group ofG. Pfurtscheller at GrazUniversityofTechnology (Austria) have beeninvestigating thelineardiscriminantmethodbasedonAdaptiv←，ARmodelfordetect4classes(motor imageriesforleftandrighthands，foot andtongue) ofchangesofEEGtoapplytothe man-machineinte巾.ce[7] .TheauthorsalsohavebeenstudyingaboutastatisticalpatternrecognitionbasedonARmodeltorecognizetheEEGpatternsduringle氏andright handmotorimageryandtoapplytoBCIsystems [1][2].Asaresult，weconfirmedthat subjectsbecametoabletohandlearobotwithabouta10daystraining.BCIsystems basedonP300seldomneedsubjecttrai凶ngbuti ti shardtouseforlongbecausethey cause the fatigueofsubjects. Onthe contrary，in case ofBCIsusing changes ofEEG during motor imagery，although they tire subjects less，subject training to control the brainwavesi sneededfornow.

I fproper informationrelevant to motorimagery can beextractedfrombrainwaves，

subject tr出ningseemto beunnecessary.Inthissense，researches aroundBCIarenow developingandwethinkmoreprecisedevelopmentofsignalanalysistechniquesi sindispensible.

Assignal analysis，various techniques such as conventional frequency analysis，wave shapeidentification，independentconlponentanalysis(ICA) andfractalanalysisetc. are developed. Onthe other hand，manypattern recognition methods are investigated to identifytheleftandrighthandmotorimageryfrominformationextractedbythesesignal analysistechniques. Identificationmethodsbased011theresult ofposition-identificatio11 ofsourcesignalrelevanttomotorimageryarefocused011asphysiologicallymea且ingful informationextractiontechniques. Forexample，sourcesignalest

[Figure 3]

PATTERNRECOGNITIONOFEEGSIGNAL

2619

[Figure 4]

>12.5sec FIGURE1.Timingchart

[+l[件 [1ャ JLt_ l~]

Fixation Left Right downward FeedBack

Cross 凶ftH制 (Ri仰 H制 (RightF倒}

FIGURE2.DisplayImage FB(horizontal)= lefthandlikelihood-righthandlikelihood

FB(vertical)=rightfootlikelihood-(lefthandlikelihood+righthandlikelihood) / 2

aboutchangesofEEGcausedbymotorimageryoraboutindividualdifferencesi sfound andthee宜ectivenessourmethodi scertified.

- 2 .Materials andMethods. Three subjects (A，B，C: 22-24 years old) participated in this work . All were right-handed and right-footed and not takingmedication. We experimentedhandandfootmovementimageryonthesesubjects.

2.1 .Experimentalparadigm. Duringtheexperiment，thesubjectfi.xatedacomputer monitor 100cmin合ontofhim.Eachtrialw，槌󠄀 8000mslong (Figure 1).At3000 ms， thefi.xationcrossw凶 overlaidwithanarrowat thecenterofthemonitorfor 1250ms， pointing either to the left(←)1 to the right(→)and downwards(↓).Depending on thedirectionofthearrow，thesubjectwasinstructedtoimagineamovementoftheleft hand，therighthandorrightfoot. Priortotheexperiment，eachsubjectwasgiventhe opportunitytopracticeandperformactualmovementsofthelefthand，righthandand rightfootaccordingtothearrowdirectiondisplayedonthemonitor(Figure2).Feedback (FB)consistingofabar-graphi spresentedatthecenterofもhemonitorfrom5000msto 8000ms.

There were two types ofsessions:in the initial sessions，datawascollected for the creationofasubject-specificclassifierand，therefore，nofeedbackwasprovided.Inthe followingfeedbacksessions:theclassifierwasthenusedtocl凶 siちrthesubject'sEEGonlinewhileheimaginedthe requestedkindofmovement，andfeedbackwωgiventothe subjectasdescribedabove.

Subjectsparticipatedin 10sessionsallondifferentdays.Howeversubject Aparticipatedoncemoretocheck theresultsofexperiment.Eachsessionconsistedof4experimental runs of60 trials (20 'le町， 20 'right and 20 'foot' trials) andlasted about 60 minutes. Thesequenceofeachtrials，aswellasthedurationofthebreaksbetweenconsecutive trials (rangingbetween2500 and4500 ms)，wererandomizedthroughout each experimentalrun.Andafter the secondsession，thefeedbackswereexecutedbased on theparameterestimatedfromtheprevioussession'sdata.

[Figure 5]

2620 T.YAMAGUCHI，ETAL.

FIGURE3.Positionoftheelectrodes

- 2.2.EEGrecording anddata acquisition. EEGrecording electrode positions are showninFigure3 .Forexmnple，channelC3i sderivedbyfollowingequation.

Y=Yo一(YA+YP+YL+YR)!4 (1)

whe民 thesignalsde巾 edbythismethodarecalledsmallLaplacianfilteredsignals (SL signals).Yo，YA，YP，YLandYRdenoteasfollows.

Yo:αη electrodeplαcedC3 YA:αnelectrodeplαced2.5αηαnteriortoC3 YP:αnelectrodeplaced2.5cmposteriortoC3 YL:αη electrodeplαced2.5crnlefttoC3 YR:αnelectrodeplαced2.5crnrighttoC3

Channel C4andCzare derived in the sameway. TheEEGsignals are amplified and band-passfilteredbetween1.5and60HzbyNihonKhoden創 npl泊erandthensampled at128Hz. Electrooculogram(EOG)arederivedfromtwoelectrodes，oneplacedmedially justabovetherighteyeandtheotherlaterallyjustbelowthelefteye，inordertodetect vertical部 wellas horizontaleye moveme附 . Electromyogram (EMG)i sderived from bipolarelectrode. Thetargetmusclei stheleftandrightforearmflexormuscle， 組dthe bicepsmuscleofthigh. ThesesignalsareusedtoscreentheEEGrecordingsforeyeand musclemovementartifacts.

- 3 .FeatureExtractionMethodBasedonARmodel.EEGsignalsareassumedto begenerated仕omanautoregressive(AR)model. Namely，letYtbetheobservedEEG signalattimetand1/tbeanindependentrandomvariablewiththenormaldistribution

E[Vt1/sJ=pdt，s，Vt."VN[O，p]. ThenthebehaviorofEEGi sexpressedas

Yt=乞伽t-j+νt.'=φTZt-l十円 (m+1~ t三N) (2)

withtheparametervectors争=[ゆ1ゆ，2，・・・，ゆrnJTandZt-l= [Yt-bYt-2，・・・，Yt_rn]T.The firstm observationsYl，Y2 ，... ，YmserveastheinitialconditionsfortheEq.(2). Wealso combinetheparametersasasinglevector)(=[<tT，p]T組 dr伽 it邸 thefeaturep紅 細 eter.

[Figure 6]

PATTERNRECOGNITIONOFEEGSIGNAL 2621

Forthefeatureparameterfhcorrespondingtotheclassωk，wemakeassumptionsof independencyanddetenninacy. Namely，weassumei tsatisfiestheindependencycondition

P(YbY2，・..，Ym，fh)=P(YbY2，・・・ ，Ym)P(fh) (3) andthedeterminacycondition

p(YNIωk)=p(YNI仇) (4) aresatisfied. HereYN=[Yl'Y2，・・・ ，YN]T.

Theseassumptionsyieldthefollowingexplicitexpressionfortheconditionalprobability densityfunctions.

、立与.!!!: r N 1

(YNI州 )=P(Yl，Y2，...，Ym) ¥2πト~~、 Pk))‘ exp---~- I1-..，~2Pk.~，>=(Yt¥<7.一可-， .-.-Zt_l)21"， I (5)

L '~ t=m+l J

Theaimofthisworki stoidentifytwoclassesofhuman'swill. Weadoptthefollowing Bayesiandecisionrule.

k*=ArgAヤxPr(ωkIYN)

### ( N 、

=ArgA{αパl-L-ln(2m)--Y2 2Pk (Ut-《Zトlr+lnPr(叫)>

N-m_ ，_ 1 七-. ，? .I

~l ¥"". -，..-.-" ， •----，--，../J (6)

t会

whereYN=[YllY2，・・・ 1YN]Ti satimeseque即 eofEEGsignalandωkrepresentsthek-th class. Toestimatetheseparameters，thelikelihoodfunction

L=P(YNωIk) (7)

i sadoptedasthecriterion. TolnaximizeL，put allofthe 1-storderpartialdifferentials ofLtobezero. Thenthederivedsimultaneousequationsaresolvedtogiverisetothe followingrelations.

]L孟[.1YtzL]

も=孟[1Zt-lz

P k=正石乞(仇-67zt-1)2

- (8)
- (9)

ARspectrumS(f )i scaIculatedbyfollowing叩 ation.fdenotesthefrequency.

8(f)=~m p : l n

11-2二Okexp(-j・2πfk)1

k=l

Thechangesoftheparameterscaused thefrequencytochange.1 tmeansthat some informationcanbeextracted仕omtheparameters.

- 4 .PatternRecognitionMethodbyUsingSOM.

[Figure 7]

2622 T.YAMAGUCHI，ETAL.

- 4.1.Selforganizing maps. The80M i sdefined部 amappingfromtheinputvector x =[Xl， X21・・・ ，Xk]TontoatWIか dimensionalarrayofnodes. Thelatticetypeofthearray

i sdefinedhexagonalofnlinesm rows. ¥Vitheverynodei，aparametricreferencevector

r~i ~i ~i

ffii=斗[仰叫:m ，m町2'い 川ηm川叫弘叫Zlk1Sa翻S回so閃ci刷a抗te吋d(σFi郁伊r閃e4叫).

Thelearning process of801v1 i sshownbelow. Tobegin with，every input vector x i scompared with allthemi' Thesmallest value ofthe Euclidean distance Ilx-mill determinethebestmatchingnodec :

c =arg凶nllx-mill. 、，.、 a

F

唱E An u

， ，

••、 、

ThereferencevectorslocatedaroundthebestInatchingnodecareupdatedasfollows:

ffii(t+1)=mi(t)+ん(t)[x(t)-mi(t)]，

hci=α(t)-exp￨-q(¥ IIr c2σ-rdl2¥1

2(t) J

whereα(t )i sthelearningratefactor，andσ(t)i sthewidthofthekernel，and九 組dr i arelocationvectorsofnodescandirespectively.α(t )andσ(t )aremonotonedecreasing functionoftheperiodoflearning.

(11)

~nput: X=[x)，.l"2""，Xk]T

m

nodei:mi=[mJ，mL--vm;]T

( i=1，2，.，.. nxm) FIGURE4.8tructureof80Ivl

- 4.2.Pattern recognition method. In this work，the 80Marray w鎚󠄀 madebythe estimatedARspectrum.Eachunitofthearraywaslabeledbytheclass (quantization) according to itsupdate frequency. Toavoid the influence oftransient states，weused theupdatefrequencyofthelastpartofthelearningstage.Aschematicoverviewofour algorithmi sshownin Figure 5 . Eachunit i saccompaniedwith informationaboutAR spectrumasitsreferencevector(Figure6(c)). Inpattemidentificationprocess，eachtest datai sclassifiedbyitsARspectrum. Namely，ARspectrumofthetestdatai spassedto 8011，thenthedatai sdiscriminatedtobelongtotheclassofwhichthelabeli sattached totheunitofthereferencevectornearesttotheinputARspectrumwithrespecttothe distance(Eq.(10)).

Inthiswork，weuse310calEEGsignalscomposedfrom15channelEEGsignals(Figure 3)bythe8mallLaplacian(Eq.(l)). Thusthederived3localEEGsignalsC3，C4andCz canbeassumedmutuallyindependent. Inotherwords，eachlocalEEGsignali sconsidered to possessitsowncharacteristic featuresandhence wemayconstruct 3discrimination modulesasdescribedaboveforeverylocalEEGsignalsandthencombiningthembythe majority decision rule，weobtain the total discrinlInation system. A block diagrami s showninFigure7 .

[Figure 8]

PATTERNRECOGNITIONOFEEGSIGNAL

2623

[Figure 9]

￨Qua山 ationI

Discrimination

Map

FIGURE5.Paradigmofthe80恥1array

回 u:.-[!~a-...~ .，jJ~--.l....J.，.J_ー

ヨ，~IL 二'_ :.---. l~.~I~ ~ー L_1 、

LUI'-. -i~I...JL， -'_..JIL~~I 一日一i

⑮。1・~三壬唱CMlWlHil' 00000~・・..。0000・・・・出同0・ーで‘一一.';-:-よ.J・~...，ULLiI.J.ーIL~~I-L，-~~'="I=-"'-::--'F Iι_.~Iーコ」仁i_!_1_1

[己乙 2 コ￨口にでで亡て]

## ha態252記 aお潟場拡箆伊心LUL，:"::' "，J.J..J巳u--i;J口

協1.....-0:跡it...諮ZL ~.9鎗!D.-.議潟脇寝e.-e_e.2:!i!:女:;;."s[CJLUILLt- ::)~)~ムj[.~:μ~L日」レ，-:-L，--:-:'二=-:-，:._.L~J ' J

I~罰跨議誇詰寄ら事誤認窃"ヨtfi.;;，; r :D~lLr工 戸 己I~.J1ゴ口 lコ

W M W (5・301Hz])

FIGURE6. 80Ivlarray(subjectB)

(a) ContinuousColorlVlapofthenumberofupdate. Eachnodei spaintedbyRGB(X， Y，Z).X，YandZarenumberofupdateoneachcl蹴(1eft1悶 ld，righthandandfoot motorimagery)respectively. (b)DiscreteColorMapofthenumberofupdate(binarizationbythreshold). (c)ElementMapofthenumberofupdate(5""30[Hz]).

，SOMClass伽 1

C3Signalsr

[Figure 10]

[Figure 11]

SOMCl回 sifier2

[Figure 12]

SOMClassifier3

FIGURE7.Discrimination8ystem

- 4.3.Evaluation methods 1: Features most updated units in each class. To extractinformationaboutthedifferencesbetweentheclasses(lefthand，righthandand footmotorimageη)，weintroducethefollowingdistancefunctionasthecriterion.

dー= (m~-'m!!J 2.+(m~-m:)2+(m~ -m:)2

##### (12)

12 I+_2σ R σ_2.i+Iσ_2 F σR+σF

[Figure 13]

2624 T.YAMAGUCHI，ETAL.

wheremL，mR，mF34FσAandσ予arerespectivelythemeansandthevariancesofthe input ARspectrumusedforupdatingthereferencevectoroftherepresentativeunit of theclassinthelastpartofthelearningstage. Heretherepresentativeuniti sdefinedas themostfrequentlyupdatedUlli tintheclass.

- 4.4.Evaluation methods 2:Features units labeled sameclass in each class. WhileEq.(12) makesuseoftheinterrepr回 印 刷iveunitinfo口nation，hereweintroduce thefollowingweighteddistancefunctionstoutilizetheinformationaboutalloftheunit labelledasthesamecl鉛 sonthediscriminatemap.

.r mi-mh r mi-m〉 r mh-mb 'JL11.=σ_1:i+σ1 _1R，JLF=σ，_:i+σ1 ，_F 1 JRF=σら+σb

(13)

wherem~， m，n'mトσ'L，0"Rand0"Farerespectivelythemeansandth恥1鴎es抗ta飢n吋da紅.rdvaぽ.r弘ian恥ce部S ぱOft巾hereti伽f a鎚󠄀ssigneddistancesto∞conlparethe，島fea抗tu町re白soぱftheclasses.

FhuExper-enm4 r u

T&p何回nふ氾

m α

C1j

陀Quougu

se

& L

恥

oa

O8d

p

‘

oaofnldu

n u

mvDUns81dm)o

×

hmnFd36ds

沼

16.n

d

同一

(=u

ne1ω

，6

nn'huv

バ 川 ×

ddJ

什

q u

y

・ ・ 加

qak

内把

m

開咋仏国

MaeM=d

出川功

3

sb0yU(

ム い

α

⑪

AhdS

し

Lf

印

日山

=um

∞

tJ

則的一

Ml

・3e2os80mu(tBa

土

ea

usl

到

hd

dma--wtt

F T i

m

川・叫凶オオオ

o

抑

れ

mm

卯即日出)刷仏山由戸川

直

UHJd

一14K04JMo

te-3i6

日

336E

mw

地肌

UqpH

川吋い

n w

わ附

閉

bon

ゆ ( 八

813

・1n

・ 引

R1.U

四

24

一 ( ( ( ・

1

川

IAISE21240E

凹

陪

JLAE

旧

18137

・

u t - -

』

E

EMee

判

h

抗一一位一一一一一

hh

ET&DTT

••••

JUに 噌󠄀i

- 5.2.Experimentalresult.

- 5.2.1 .Pαtternrecognitionresult.Thethreeclassclωsificationresultsusingthismethod areshowninFigure8 .Eachsubjects (A，B:C)participatedin10"，11sessionsindicated inx-axis.Theaccuracyofthepatternidentificationofthethreeclassesi sindicatedin y-axis. Input spectrum bandw加 3"，64Hz. Theexperimental result shows that the accuracyrateswerein45"，-，60%.

Moreover，the majority decision rule was applied to the classification result ofeach channe.l ¥Vhenresults for twoor threeclasses arenot consistent，"Reject" classi sassigned. Correctratesanderror ratesdecreasedsimultaneouslybythismethod(Tables. 1， 2and3).Fromviewpointofreliability(decreaseoferrorrate)，thismethodi spractical.

Comparisonwiththeclassificationresultsusingstatisticalpatternrecognitionmethod based onARmodel [4 ]depicted in Tables 1，2and3 . Accuracy rates based onSOM werehigherthanthat based onstatisticalone.Comparedwith thestatistical method， theaccuracyratesbyusingthemajoritymethodshowedhighratesontheaverage(subj.

A: 49.1→49.6，% subj.B: 43.4→ 46.0，% subj.C: 38.2→45.9%).Especially，the improvementwasseeninthedataforwhichwehadobtainedlowaccuracyratebyusing thestatisticalmethod.

[Figure 14]

PATTERNRECOGNITIONOFEEGSIGNAL 2625

- 5.2.2. Result 01evaluαtion method1 .Thecriterion value takes alarge difference in a specificband(Figures9，10，11). Theseresultsshowthatthereexistdifferencesnotonly inthefrequencybandsofα 組 dswavesbutalsointhebandsof)(andiwaves. Therefore， weinvestigated80Mwhichusedelementsofthesub-band ((} :4"，7Hz，α: 8"，13Hz，β: 14"，30Hz，γ: 30"，64Hz) astheinputvector. Tables4，5and6showthefollowingfact. In someresults，the highest accuracy rateswere achieved when8011used element of thesub-bandinwhichpeaksofcriterionappeared.Thisfactsuggeststhat ane百'ective sub-bandforpatternrecognitioni sextractedbyourmethod. Thismethodhasthebetter performancethanthestatisticalpatternrecognitionmethod.
- 5.2.3. Result01evaluαtionmethod2 .Theresultofinvestigationofthefeaturesofthemap byusingtheweightedsigneddistancefunctions (Eq.(13))i sshowninFigures. 12，13and

14. Thedi旺'erenceofthe weighted signed distances represents the difference between classes. Ingeneral，i ti sconsidered.thatevent-relatedsynchronizationjdesynchronization (ERDjER8)areobservedincontralateralregionduringh組 dmotorimagery(e.g. right handrnotorimagerytochannel C3).Inthisexperiment，thedifferencewasseeninthe αbandinchannel C3andchannel C4duringlefthandmotorimagery andright hand rnotorimageryforsubjectAandsubject C.ForsubjectB，thedifferencewasseenina frequencybandthatwasalittlehigherthantheαband. Thesecontralateralshowsthe featureofERDjERSobservedinEEGduringrnotorimagery. Wenotethatafeaturein theneighborhoodofαbandi sobservedfortherighthandandlefthandmotorimagery (Figures12，13 and14).Thuswegazedonthecomponentlirnitedto8"，13Hzfeatures toinvestigate throughout allsessions.Figure 15 showstransitionoftheaveragepower oftheαbandthrough 11 sessionsofsubjectA.Frornthisfigure，the contralateralcan beseenwithchannel C3andchannelC4inleftjrighthandmotorirnagery. Thesefacts suggestthatSOMcanbe凶 edasatoolthatextractsmoredetailedfeatures.

70

a O

E d

向UEunu

OEUE1va

内

[ 訴

] h n o g

』

300

医dnUZ1vnu

Yaqad

且

帽

のd

2 3 4 5 6 7 8 9 10 11

ロ&凶ectA固Subj回 tB固Sut羽田tC Session

FIGURE8.ThreeclassesclassificationresultbyusingSOM Eachsubjectsparticipatedin10"，11sessions

[Figure 15]

2626 T.YAMAGUCHI，ETAL.

- TABLE1.Patternrecognitionresult (SubjectA)
- TABLE2.Patternrecognitionresult (SubjectB)

d

- TABLE3. Patternrecog凶 ionresult (SubjectC)

|Sessio|accuracyr別| | |
|---|---|---|---|
| |SOM n C3 C4 Cz|majorilydecision CorreCl Error R吋配t|statislicaJmelh吋 C3&C4&Cz|
|ヲ<br><br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10 1I<br>|45.6% 49.49も 41.7努<br>46.1% 51.1% 50.6%<br>47.8% 59.4も1' 47.2%<br>48.3% 48.3% 43.99も 46.1% 50.0% 46.7%<br><br><br>51.7% 57.2% 47.8% 48.9% 53.3% 53.9%<br>52.2% 50.6% 52.2勿: 引 .1% 46.1% 45.6% 52.89も 60.0% 43.9% 52.2% 56.79も 46.1%<br>|45.6% 40.0% 14.4%<br><br>49.4% 33.9% 16.7も1'<br>50.0% 34.4% 15.6%<br><br>46.1% 31.7% 22.2%<br><br>45.6% 40.6% 13.9%<br><br>51.1% 36.7% 12.2% 51.7% 31.1% 17.2% 56.1'7もみt49も 9.4%<br><br>46.7% 41.1% 12.2% 53.3% 36.1% 10.6% 50.6% 41.7% 7.8%<br><br><br><br><br>|40.6% 49.8% 47.6% 49.39も 47.2もi.' 61.3% 54.49も 54.7% 39.1% 38.8% 57.3%|
|mean|49.3% 52.9% 47.2%|49.6% 36.5% 13.8%|49.1%|

|SessioJ|a∞uraclt'l'il| | |
|---|---|---|---|
| |SOM l C3 C4 Cz|majoritydecision Co町民t Error R吋ecl|statisticnlmethod C3&C4&Cz|
|2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>|45.6% 47.2% 46.7% 55.6% 47.8% 50，()%<br><br>47.8% 48.9% 46.1% 42.29も 44.4'1も 45.6%<br>48.3% 46.7% 43.9% 47.2% 51.1% 49.49も 45.6% 50.0% 47.2呪:<br>49.4% 44.4% 48.3% 45.6% 43.9% 46.7% 47.2% 48.9% 50.0%<br>|43.3% 35.6% 21.I% 52.8% 24.4% 22.8%<br><br>46.1% 32.2% 21.7%<br><br>41.1% 40.6% 18.3%<br>42.2% 35.6% 22.2%<br><br><br>47.2% 29.4% 23.3%<br><br><br>46.7も}， 31.7% 21.7%<br>47.2% 38.9% 13.9% 42.8% 39.4% 17.8% 50.6% 34.4% 15.0%<br>|45.99ら 59.5%<br><br>40.9% 43.8% 43.2%<br>41.6% 41.9%<br><br><br>39.29も 37.8%<br>40.1%<br>|
|mean|47.4% 47.3% 47.4%|46.0% 34.2% 19.8%|43.4%|

|Sessio|accuracy偶]| | |
|---|---|---|---|
| |SOM n C3 C4 Cz|majoritydecision Co汀ect Error Rejecl|statisticalmethod C3&C4&Cz|
|2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>|47.8% 48.3% 49.4% 45.6'}も 50.6% 47.8%<br><br>47.2% 45.6% 45.6% 45.6'.1も 46.19も 47.8%<br>47.2% 46.7% 48.9%<br>47.2% 47.8% 46.7% 51.1% 45.0% 48.3% 49.4% 45.6% 44.4% 47.2% 43.9% 46.7% 44.4% 42.2% 45.6%<br>|46.7% 29.4% 23.9% 49.4% 39.4% 11.1%<br>47.8% 31.1% 21.1% 42.8% 41.1% 16.1% 47.8% 31.7% 20.6% 42.2% 34.4% 23.3% 47.8% 35.0% 17.2% 45.6% 36.1% 18.3% 44.4% 41.1% 14.4% 44.49も 37.2% 18.3%<br>|37.7%<br><br>40.9%<br><br>37.8% 43.0%<br><br>41.9% 39.7%<br><br><br><br><br>35.3も与 32.39る<br>36.7lJる 36.8%<br>|
|mean|47.3% 46.2% 47.1%|45.9% 35.7% 18.4%|38.2%|

d

6 .Conclusion. Inthiswork，featureextractionbasedonSOMusingARspectrumwas introduced to analysis theEEGsignals recorded duringright hand，lefthandandfoot motorimagery.Atypicalfeature ofdifference ofthec1槌󠄀sescan bediscussed byusing SOMto extract representative features.In somesubjects，there were differences inB and' Ybands in additionto general αandsbandsregion.Theidentification accuracy ratehasimprovedbylimitingthebandforlearningstageofSOM.Therefore，thisresult suggeststhataparticulareffectivesub-bandforpatternrecognitionthati ssubjectspecific couldbeobtainedbyusingSOM(i.e.subject'sindividualvariationhasbeenextracted bythis algorithm). fvloreover，the effectiveEEGfeatures for pattern reco伊 itionthat

[Figure 16]

PATTERNRECOGNITIONOFEEGSIGNAL cntenon

2627

[ChannelC3]1

￨ Jへ八 八 ^.~ .I

官 10 20 30 40 SO 日

一一

プ 八 %

IS司1~/------.-------.-----~-------r------~----~.-~

￨ [ C h a n n c lCZ]I

￨ 八 人 ￨

も 10 20 30 40 S O ω

FIGURE9.Thecriterionvalueofthemostupdatedunitineachclass(Subj.A)

TABLE4. Threeclassesclassificationresultineachband byusingSO~ll (Subj.A)

accuracy[%] 4-7Hz 8-13Hz 14-30Hz 30・64Hz 3-64Hz ChannelC3 47.2% 55.6% 45.0% 47.2% 52.2%

IChannelC4 44.4% 58.3% 50.0% 49.4% 56.7% ChannelCz 51.1% 47.8% 56.1% 48.3% 46.19も

cntenon 十 [ChannelC3.H

#### 20:r~.^ . ~. _. . • 1

~I10 日 30 日 5日 B

ト [ChannelC4.H

22 i B E 2 5 3 . 0 4日 5 0 4 白

ト [ChannelCz]~

l A A A~~~____~

2E 10 z o m 4 8 5 0 ω

frequency[Hz]

FIGURE 10. Thecriterion value ofthe most updated unit in each class (Subj. B)

i scontralateralwereobtainedbyinvestigatingtotheweighteddistancebetweenclasses. Thismention，the changingelement that correspondsto ERD/ERScouldbeextracted duringmotorimageryinEEG.Basedonth田 efindings，onetechniqueto EEGanalysis during motor imagery was made. Byimproving this method，i tcomes to beable to distinguish foot motorimagery fromhandmotorimagery. This leads to improvement

[Figure 17]

2628 T.YAMAGUCHI，ETAL.

- TABLE5. ThreeclassesclassificationresultineachbandbyusingSOM(Subj.B) accuracy[%1

牛耳-Iz 8-13Hz 14-30Hz 30・64Hz 3・64Hz

Channe]c31145.6% 47.8% 47.2% 41.7% i45.6% ChannelC41150.0% 46.1% 52.8% 47.8% 47.8% ChannelCz~ 49.4% 45.0% 49.4% 48.9% 51.1%

cntenon

l …亡3j

[ChannelC411

~I-b F-25 却 「 へλ h a j

; I J J J ¥ ! ? n e l : z I

~

FIGURE11 .Thecriterion value ofthe mostupdated unit in each class (Subj.C)

- TABLE6. Threeclぉ sesclassificationresultineachbandbyusingSOM(Subj.C) accuracy[%]

4-7Hz 品13Hz 14-30Hz 30-64Hzi3-64Hz

ChannelC3 44.4% 45.0% 49.4% 45.6% 44.4% ChannelC4 50.0% 46.1% 46.79も 45.0% ! 42.2% Channe)Cz 44.4% 45.6% 47.8% 43.3% 45.6%

ofourfeed-backsystemandhence toshorten subject training.Thesestudies areunder construction.

REFERENCES

- [1 ]K. Inoue，D.Mori，G.PfurtschellerandK.Kumamar比 PatternrecognitionofEEGsignalsduring rightandleftmotorimagerylearningeffectsofthe subjects，inComplexMedicalEngineering，J .L. ¥Vu，K.Ito，S .Tobimatsu，T.NishidaandH.Fukayama(eds.)，Springer，pp.251・261，2007.
- [2 ]K.Inoue，K.KumamaruandG.Pfu巾 chell民 Robotoperation凶 edonpatternrecognitionofEEG signals，Proc. ofthe 3rdInternαtional Brain-ComputerInterJαce Workshop andTrain飢，gCourse， Graz，Austria，pp.116-117，2006.
- [3 ]T.Ishibashi，M.Sugahara，S .Tamatsuka，K.Inoue，H.GotandaandK.Kumamaru，Estimationof thenumberofunknownsourcesignalsandit sapplicationtoEEGanalysis，Proc. ofthe38thISCIE InternationalSymposiumonStochαsticSystem TheoryandItsApplications，2006.
- [4 ]R.L.Kash)句， Optimal featureselection and decision rules inc1assification problemswith time series，IEEETrans. Information Theory，vol.IT-24，pp.281-288，1978.
- [5 ]T.Kohonen，Self-OrgαnizingMaps，Springer-VerlagandEnvironment，1996.
- [6 ]E.NiedermeyerandF.L.DaSilva，Electroencephαlography: BαsicPrinciples，ClinicalAppliωtions， αndRelatedFields，¥Villiams&Wilkins‘1999.

[Figure 18]

PATTERNRECOGNITIONOFEEGSIGNAL

2629

Lefthand Lefthand Righthand

ωωd伽叩a加伽山吋伽附nn州ne耐elCイ…〕つ￨V

Ri招箆討帥ht日th加la叩nd(σfu同Rサ司 FOOl ぴ(fLF吋 Foot び(fRミう?けf) lハ¥ハf I . L ___J J

伽cl蜘hmlan吋a訂如nn川“ell印C4Jv¥〉〕

，

叫 iL ￨ 岨E 、u

damelCV¥ノ ljiI1:

510 15 20 25 30 5]01520 25 30 5101520 25 30 lHz]

- FIGURE12.Weighteddistancebetweeneachcl総弓 (subjectA)

Left hand Leflhand Righthand

Righthand(fLR) FoOl (fLF) Foot (fRF)

h ω::L八 (11JlJ11八八^-

;凶\~/'-"1-0:[‘ JJアνvコ

:I_ 1~~_u _____1:~[7\二二J

channel汁亡ゴ::￨¥:'-~-_.ili二 i

5]01520 25 30 5101520 25 30 5101520 25 30

2￨fヘ 1:~I! ご!八，-... ..-.ノ

damiezik二つι-=J:1v-- 1

101520 25 30 510 1520 25 30 5IO1 520 25 30

- FIGURE13.vVeighteddistancebetweeneachclass (subjectB)

- [7 ]G.Pfurtscheller，C.Brunner，A. SchloglandF.H.LopesdaSilva，Murhythm(de)synchronization andEEGsingle-trialclassificationofdi百'erentmotorimagerytasks，Neurolmage，vo1.31，no.l，pp.153・ 159，2006.
- [8 ]J .C.Sanchez，A.Gundl.肌 P.R.CarneyandJ .C.PrinCIpe，Extractionandlocalizationofmesoscopic motorcontrolsignalsforhumanECoGneuroprosthetics，JournalofNeuroscienceMethods，no.167， pp.63・81，2008.
- [9 ]J .J .Vidal，Towarddirectbraincomputercommunication，AnnualRev.，BiophysicsBio-engineering， pp.157・180，1973.

[Figure 19]

2630 T. YAMAGUCHI，ETAL.

Left hand Leflhand Righlhand versus ver日us versus

国l l ・21 i.~.-'".~--.1 トベ

channelC3叫レ/叶 「 lo~1 ￨

ムJ¥ |円:「~..-，--プ三了寸7ぺ一ベ寸 γプ

し../'¥¥L、、」‘】Vd

hannelCz~I ハ lll l:いの~

# neJLZ:l/¥../"ノヘイ :Lー;二]:し I

URE14.Weighteddistancebetweeneachclass (subject C)

[dBI ChannelC3 (dB) .ChannelC4

[Figure 20]

.0.]

###### .o.H

.0.4 .0.45 .0.'

.0."

.0.6 .0.65

ベ :- 1012.o .9~

[Scssion] (Session[

FIGURE15.Transitionoftheaveragepoweroftheαband(SubjectA) SubjectAparticipatedin 11 sessions. 1nchannelC3，thepoweroftherighthandrnotor imageryclassi soveralllowerthananother. 1ncontrast，inchannelC4thepoweroftheleft classi soveralllowerth組 another.Thesefeaturesarecalledcontralateral.

- [10]J .R.¥Volpaw，N.Birbaumer，D. J .McFarla吋 andG.Pfurtscheller，TheresaM.Vaughan，Braincomputerinterfacesforcommunicationandcontrol，ClinicalNeurophysiology，vol.1l3，no.6，pp.767・， 791，2002.

[1μ1日1]μJ.恥W;01如pa側wandD.除McFar巾lan叫匙Mu山l川“tichan

ceph凶αalo句IgmphνandClinicalNeuro骨-phy似i旬010句gy，no.90，pp.444-449，1997.

- [12]L.YunandK.Uch加 ura，Usingself-organizingmapforroadnetworkextractionfromIkonos回 agery， lnternationalJournal oflnnovαtive Computing，lnformαtionαndControl，vo13，no.3，pp.641-656， 2007.
- [13]Z.Zha昭， Kazuaki1，T.Miyake，T.IrnamuraandS.Horihata，Estimationofsoundsourcedirection usingabinauralmodel，lnternationalJournal ollnnovative Computing，lnformation andControl vo13，no.3，pp.551・564，2007.

