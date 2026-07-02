# Low-Power Circuits for Brain-Machine Interfaces

Rahul Sarpeshkar, Woradorn Wattanapanitch, Benjamin I. Rapoport, Scott K. Arfin, Michael W. Baker, Soumyajit Mandal, and Michale S. Fee

Massachusetts Institute of Technology Cambridge, Massachusetts, United States of America rahuls@mit.edu

Abstract—This paper presents work on ultra-low-power circuits for brain-machine interfaces with applications for paralysis prosthetics, prosthetics for the blind, and experimental neuroscience systems. The circuits include a micropower neural amplifier with adaptive power biasing for use in multi-electrode arrays; an analog linear decoding and learning architecture for data compression; radio-frequency (RF) impedance modulation for low-power data telemetry; a wireless link for efficient power transfer; mixed-signal system integration for efficiency, robustness, and programmability; and circuits for wireless stimulation of neurons. Experimental results from chips that have recorded from and stimulated neurons in the zebra-finch brain and from RF power-link systems are presented. Circuit simulations that have successfully processed prerecorded data from a monkey brain and from an RF data telemetry system are also presented.

I. INTRODUCTION

Large-scale chronic multi-electrode neural recording systems have emerged as an important experimental paradigm for investigating brain function. Experiments using such Brain-Machine Interfaces (BMIs) have shown that it is possible to predict intended limb movements by analyzing simultaneous recordings from many neurons. These findings have suggested a potential approach for treating paralysis [1]. Chronic use of BMIs with large numbers of electrodes requires ultra-low-power operation so that the system is miniature and implantable, heat dissipated in the brain is minimized, and frequent battery replacement and resurgery in implanted systems is unnecessary. Low-power neural amplifiers are extremely important in such interfaces since one such amplifier is needed for each electrode. In this work, we present data from a novel micropower neural amplifier that appears to be the most power-efficient neural amplifier reported to date. We also describe a scheme for adapting the noise floor of this amplifier to the noise-floor requirements at each recording site, potentially enabling multi-electrode systems to reduce recording power by an order of magnitude.

RF data telemetry is necessary to communicate information wirelessly from neurons in the brain through the skull and skin. Due to the relatively high power costs of transcutaneous data communication (100 electrodes with 12-bit 20kHz-sampled neural information yield a data rate of 24Mbs-1), some form of data compression is needed to reduce the bandwidth of information transmitted from the brain. An adaptive, learnable, multi-input-multioutput linear filter that projects firing-rate neuronal data onto a few motor output parameters has successfully been used to decode movement intentions from neural signals [1]. Such filters have proven useful for interpreting population codes of neurons in various brain

Sam Musallam and Richard A. Andersen

Division of Biology California Institute of Technology Pasadena, California, United States of America

regions and perform comparably to adaptive Kalman filters and other probabilistic decoding techniques. In this work, we discuss how we may use an analog decoding and learning architecture to compute such a filter in a power-efficient analog fashion, thereby allowing high data compression (an output rate of 3 × 100Hz × 8bits = 2.4kbs-1 is more than sufficient for anticipated applications). We present circuit simulations of the architecture that successfully learn and decode a monkey’s intention to move from its prerecorded neural spiking data.

We also propose a novel low-power impedance-modulation technique for BMIs that can be used to transmit RF data from the brain flexibly and efficiently so that the power costs of communication are almost solely borne by external RF circuitry outside the skin and skull rather than by the implanted RF circuitry within, as in prior designs [2]. Thus, heat and power dissipation in implanted hardware within the brain can be minimized.

Efficient wireless links that transmit RF power through the skin are necessary to power implanted chips in the interface directly via rectification and possibly also to recharge implanted batteries with a finite number of recharges. In this work we present data from an RF link that achieves efficiencies near theoretical limits and summarize the tradeoffs needed to make such links efficient.

In addition to being small and extremely power efficient, practical brain-machine interfaces also need to be programmable and capable of reporting high-bandwidth analog or lower-bandwidth spiking information from a few neurons if needed, sorting spikes from multiple neurons, and operating robustly in RF and mixedsignal environments. In this work we propose a novel low-power mixed-signal architecture for such interfaces that enables one to combine the power efficiency of an implanted programmable analog system with the flexibility of an external digital processor such that efficiency and flexibility are simultaneously achieved by combining the best of the analog and digital worlds.

Certain BMIs, such as visual prostheses for the blind or neurophysiological experimental systems, may require neural stimulation rather than (or in addition to) recording. We present experimental results from a chip used for wireless stimulation of neurons in a zebra finch brain and discuss how simple wakeup circuitry can be used to lower power in such systems.

This paper is organized as follows: In Section II we discuss the adaptive micropower neural amplifier and its use in multi-electrode systems. In Section III we discuss the analog linear decoding and learning architecture. In Section IV we discuss RF data and power telemetry links. In Section V we discuss a mixed-signal architecture for BMIs that can enable efficiency and flexibility. In Section VI we conclude by discussing wireless neural stimulation.

1-4244-0921-7/07 $25.00 © 2007 IEEE.

## 2068

II. AN ADAPTIVE MICROPOWER NEURAL AMPLIFIER

Fig. 1(a) shows the architecture of our adaptive micropower amplifier. The first gain stage is similar to that reported in [3] except that it is implemented with the use of an all-subthreshold and foldedcascode architecture shown in Fig. 1(b), allowing low-voltage operation. We add a bandwidth-limiting stage to keep the overall bandwidth constant as we vary the bias current of the gain stage to adapt its noise per unit bandwidth. The additional power of the bandwidth-limiting stage is negligible because the 100x gain provided by the gain stage alleviates its noise floor requirements. Fig. 1(c) shows data recorded from the RA region of a zebra-finch bird brain with a Carbostat 800kohm impedance electrode and our amplifier. There was no discernible difference compared with a recording from a commercial neural amplifier. We measured an input-referred noise of 5.5µV rms over a 5kHz bandwidth (integrated from 0.5 Hz–5 kHz) with a power consumption of 7µW for 40dB of gain. Although our amplifier’s current consumption normalized for bandwidth and noise is about 1.3x larger than that of the best prior design reported in [3], our power consumption is 0.52x lower because our topology permits 2V rather than 5V operation. In prior designs, the 5V power supply was necessary for maintaining large overdrive voltages in some above-threshold transistors to minimize their noise contributions. Our amplifier occupies a chip area of 0.09mm2 and was fabricated in a commercial 0.5µm CMOS process.

The power required to build an amplifier with constant bandwidth, constant power-supply voltage, and an input-referred noise vn scales as 1/vn2 if the amplifier is thermal noise limited. This relation clearly shows the steep power cost of achieving low-noise performance in an amplifier. Neural amplifiers have been designed to handle the worst-case range of signal strengths that may be expected

- (a)
- (b)
- (c)

C f

Cf

IBW

IBW

C in

Cin

#### V in

Vin

-

### -

G m

Gm

V out

Vout

+

+

gm

Cin

Cin

V ref

Vref

m

+

+

-

-

C

CL

IGm

G m

Cf

Cf

V bias

Vbias

Bandwidth-limiting stage

Gain Stage

M9 M10

Mb2 Mb1

Vcasc

M7 M8

Ibias

##### V+ V-

I out

M1 M2

- Mb3
- Mb4

M5 M6

M3 M4

Long Time trace

300

Amplitude(uV)

200

100

0

0 10 20 30 40 50 60 70

Time (ms)

Short time trace

300

Amplitude(uV)

200

100

0

12 14 16 18 20 22

Time (ms)

Figure 1. (a, b) The adaptive micropower neural amplifer circuit. (c) Recording obtained from the RA region of a zebra finch brain using the amplifier circuit shown.

| | | | |
|---|---|---|---|
|DAC Adjust| | | |
| |Ibias|2Ibias|2|

φi

- (a)
- (b)

n-1Ibias

[Figure 1]

φi

Vin,i Vout,i MUX

2m A2

A1

φi

2n-1C

| |C|2C<br><br>| |
|---|---|---|---|
|DAC Adjust| | | |
| | | | |

φi

0.07

0.06

0.05

Probability

0.04

0.03

0.02

0.01

0

0 20 40 60 80 100 120 140

Noise Strength (µV)

Figure 2. (a) An adaptive scheme for neural amplifier biasing. (b) The noise distribution computed by sampling statistics from a chronically-implanted array of 64 electrodes in a monkey brain.

in any recording situation. In practice, there is considerable variance in the noise and action potential strengths of typical recordings. The steep cost of achieving low-noise performance in an amplifier suggests that rather than designing amplifiers with the lowest noise at all locations, significant power savings can be achieved if an amplifier can adapt its input-referred noise to the local noise floor. This adaptability enables the overall power in a multi-electrode system to be determined by the average electrode rather than by the worst-case electrode. The control loop for setting each amplifier’s bias current in a multi-electrode array may easily be implemented with little power overhead per recording site: One very-low-noise neural amplifier is used infrequently to evaluate the noise floor at each recording site in a sequential and multiplexed fashion so that its power overhead is shared amongst all recording sites and it is only active during calibration as shown in Fig. 2(a). Fig. 2(b) shows a typical probability distribution that we obtained from neural data recorded using a chronically-implanted 64-electrode array in a monkey. For this probability distribution, using our adaptive amplifiers, a 12x reduction in neural recording power for an entire system of 100 electrodes can be achieved.

III. AN ANALOG ARCHITECTURE FOR LINEAR DECODING AND LEARNING

In some of our prior work on a bionic-ear (cochlear implant) processor, we experimentally demonstrated that analog preprocessing and delayed digitization enable order-of-magnitude power reductions over traditional A-D-then-DSP implementations [4]. Such implementations can also preserve programmability and robustness to offset, power-supply-noise, and temperature variations. In this work, we investigated whether it may be possible to achieve similar power reductions in implementing digital linear decoding and learning algorithms with analog architectures operating on analog neuronal firing rates. We were able to do so: Fig. 3(a) shows a novel analog architecture that uses a continuous-time analog gradient descent algorithm to learn a decoding filter via supervised learning. The derivation of this architecture is beyond the scope of this paper but yields a modified version of the delta learning rule well known in machine learning. Using simple transconductor-capacitor filters and multiplier, adder and subtracter circuits in subthreshold technology, we were able to show via SPICE simulations in a 0.18µm process that our architecture is capable of learning and then decoding a monkey’s intention to move its arm from data recorded from ten neurons in its

posterior parietal cortex. The recorded spike-time data from a monkey were converted into analog firing rates using fourth-order waveletlike analog matched filters on 1ms-wide spiking inputs, followed by thresholding, followed by third-order analog interpolation filters. The figure shows that the performance is similar to that achieved via digital decoding and learning algorithms. The power consumption of a single channel is near 54nW and a complete 100 channel system with 3 motor outputs is implementable with 17µW using a 1V power supply on a modest-sized chip. Thus, our analog architecture is extremely power efficient and can enable a dramatic reduction in communication power due to its data-compression properties. An actual chip implementation would need overhead for offset and mismatch compensation via DAC calibration, and temperature- and power-supply–immune biasing as our prior work has shown [4].

IV. RF DATA AND POWER TELEMETRY

Fig. 4 shows a low-power RF data telemetry design using our impedance modulation scheme. The primary external unit broadcasts a 27MHz continuous-wave carrier using a class-E amplifier topology. The secondary implanted unit switches its impedance from minimum (a series resonant coil) to maximum (an open-circuited coil) by using a switch in series with C2, thus amplitude-modulating the load at the primary. The load modulation is detected by mixing the primary voltage with the unmodulated carrier and low-pass filtering the output. The large carrier component, which gets mixed down to DC, is rejected by AC coupling the output of the filter into a chain of amplifiers. The output of the amplifier chain is thresholded to recover the Manchester-encoded transmitted data. SPICE-based circuit simulations from a 0.18µm process in Fig. 4(b) show successful data transmission at rates exceeding 1Mbps even when a very pessimistic value of k=0.05 is assumed for the coupling factor between coils, the quality factor of the primary is given by Q1=10, and the quality factor of the secondary is given by Q2=4. Thus, our link design is robust to changes in the coupling factor and inductor quality factors. The

Mi,target (t )

∑

-

Mi(t )

- (a)

- (b)

∑

| |∗<br><br>,1<br><br>( )<br><br>n<br><br>n<br><br>p W t ∂<br><br>∂|
|---|---|
| | |

|∗<br><br>W1(t )|
|---|

| |1,1<br><br>1( )<br><br>p W t ∂<br><br>∂<br><br>∗|
|---|---|
| | |

∗

...

...

...

...

...

...

. . .

Wn(t )

| |∗<br><br>n k<br><br>n<br><br>p<br><br>W t<br><br>,<br><br>( ) ∂<br><br>∂|
|---|---|
| | |

| |∗<br><br>p k<br><br>W t<br><br>1,<br><br>1( ) ∂<br><br>∂|
|---|---|
| | |

N1(t ) Nn(t )

Intended−Reach−Direction Decoding

0.64

Target

Decoding

Learning Input off

0.62

- D1−trial 1

- D1−trial 2

0.6

D2−trial1 D2−trial2

0.58

Voltage

Learning

0.56

0.54

Input Off

0.52

0.5

0 0.05 0.1 0.15 0.2 0.25

Time (sec)

Figure 3. (a) An analog architecture for linear decoding and learning. (b) Circuit simulations indicating that the architecture successfully learns and decodes from spiking data in a monkey.

EXTERNAL UNIT IMPLANTED UNIT

SKIN

BFL

(a)

DATA

C1

C2

C3

L L2

IN

|L1| |
|---|---|
| | |

LO

k

A

SC

OUT

VREF

[Figure 2]

(b)

Figure 4. (a) A block diagram of our impedance-modulation telemetry system. (b) Data from a simulation of the entire system shows the faithful recovery of transmitted data (blue) by the system with a slight delay (red).

primary power consumption was found to be 1.1mW and the secondary power consumption was found to be near zero (<1µW). This design is not thermal-noise limited, which means that the transmitted power can be reduced further.

An RF power link test setup is shown in Fig. 5(a). The system uses a custom Class-E driver, built on a chip, a primary resonator circuit, a secondary resonator circuit and a Schottky diode rectifier as shown in Fig. 5(b). The rectifier loads the secondary resonator with an effective AC resistance of RL/2 if there is little ripple on the load RL, a necessary condition for a good power supply. Ignoring rectifier and driver losses, a theoretical analysis shows that the maximum possible power efficiency in the link occurs when the load RL is chosen so that QL = ωRLC2/2 = (1/k)√(Q2/Q1) and is given by ηmax = k2Q1Q2/((kQ1+1)(kQ2+1)), where k is a geometry-dependent coupling factor and Q1 and Q2 are the quality factors of the primary and secondary resonators, respectively. Fig. 5(c) shows that theoretical and experimental measurements are in good accord and were taken for Q1 ≈ 40 and Q2 ≈ 70. RF power links can thus be quite power efficient if operated near their optima.

V. HYBRID ANALOG-DIGITAL SYSTEM DESIGN

Fig. 6 shows an overall architecture that consists of low power implanted DAC-programmable analog circuits that are configured by an external DSP or FPGA. Depending on the user’s choice, the system can be configured to report raw neural data from a selected set of electrodes, single and multiunit spikes extracted via spike sorting, local field potential (LFP) data, or decoded motor parameters via a data telemetry ‘uplink’ as we have previously described. Such flexibility is possible because the parameter values for the analog wavelet-like spike-sorting filters or other analog parameters are determined by detailed digital analysis of raw uplinked analog neural data and then downloaded into the implant via a low-bandwidth telemetry ‘downlink.’ Since the relatively power-hungry digital analysis need only be done occasionally to keep the system up-to-date as spikes or neurons appear or disappear, the overall power consumption of the system remains low but the flexibility of a digital system can be leveraged.

VI. WIRELESS NEURAL STIMULATION

Thus far, we have focused on circuits and systems capable only of recording from neurons in the brain. Fig. 7 (a) shows a system that we have used for wirelessly stimulating neurons in the zebra finch brain, as shown in Fig. 7(c). The system consists of an external transmitter (not shown) controllable through a computer interface, and a miniature, implantable wireless receiver-and-stimulator. The miniature printed circuit board contains a receiver coil and electrodes (reverse side), battery (not shown), and a custom integrated circuit for data demodulation and neural stimulation. The chip, fabricated in a standard 0.5µm CMOS process, occupies 2.25mm2 and is capable of delivering biphasic current pulses to 4 addressable electrode sites at 32 selectable current levels ranging from 10µA to 1mA, as shown in Fig. 7(b). The entire implant weighs 0.6g (including battery) and occupies a footprint smaller than 1.5cm2. During periods of birdsong inactivity, the chip can automatically enter a sleep mode in which it uses only 7µA of quiescent current. When an external microphone detects song, the computer activates the wireless transmitter, which generates an RF signal. A detector on board the chip receives this signal and wakes up the data demodulation and output driver circuitry. This system demonstrates the practicability of a power efficient scheme for programmable neural stimulation.

REFERENCES [1] J. Wessberg, C. R. Stambaugh, J. D. Kralik, P. D. Beck, M.

Laubach, J. K. Chapin, J. Kim, S. J. Biggs, M. A. Srinivasan,

[Figure 3]

Coils

- (a)
- (b)
- (c)

Rectifier TestBoard

PowerDriver &Controller Testboard

CoilRotation

CoilSeparationDistance

M=k

k

Cs

Efficiency vs. Coil Separation (PLOAD = 1mW)

- 0.8

- 1

0.6

η

Theory

0.4

Measured

0.2

0

2 3 4 5 6 7 8 9 10 11

coil separation distance (mm)

Figure 5. (a) Photograph of our RF test setup. (b) The RF power link circuits and rectifier. (c) Plot of the theoretical and measured efficiency of the link as a function of distance between primary and secondary coils.

and M. A. L. Nicolelis, “Real-Time Prediction of Hand Trajectory by Ensembles of Cortical Neurons in Primates,” Nature, vol. 408, pp. 361–365, November 2000.

- [2] R. Harrison, P. Watkins, R. Kier, R. Lovejoy, D. Black, R. Normann, and F. Solzbacher, “A low-power integrated circuit for a wireless 100-electrode neural recording system”, Proceedings of the International Solid State Circuits Conference (ISSCC), pp. 554–555, 2006.
- [3] R. R. Harrison and C. Charles, “A Low-Power Low-Noise CMOS Amplifier for Neural Recording Applications,” IEEE J. Solid State Circuits, vol. 38, no. 6, pp. 958–965, June 2003.
- [4] R. Sarpeshkar, C. Salthouse, J. J. Sit, M. Baker, S. Zhak, T. Lu, L. Turicchia, and S. Balster, “An Ultra-Low-Power Programmable Analog Bionic Ear Processor,” IEEE Transactions on Biomedical Engineering, vol. 52, no. 4, pp. 711–727, April 2005.

Motor parameters

Decoder

Data selector

MFR

|LFP| |
|---|---|
|LFP spectrum analyzer| |

Spike time extractor

Lowpass filters

|ADC| |
|---|---|
| | |

Spikes

|Load modulator|
|---|

Matched filter processing

Low power FPGA

Load modulation

receiver

DSP/

Analog data

Neural amplifiers

| | |
|---|---|
|Link to arm / computer| |

ASK

ASK

PROGRAMMING transmitter

receiver

| | |
|---|---|
|Electrode array| |

POWER

Battery charger

DC / DC converter

External unit

Implanted system

Figure 6. A block diagram of our overall system.

[Figure 4]

- (a)
- (b)
- (c)

- 0.5

- 1

Current(mA)

0

−0.5

−1

−100 −50 0 50 100

Time (µs)

- 0.5

- 1

Response

AmplifiedNeuralSignal(V)

0

−0.5

Stimulation artifact

−1

0 5 10 15 20 25 30

Tims (ms)

Figure 7. (a) Photograph of the chip-on-board wireless neural stimulation system. (b) Measured biphasic current pulses demonstrating 32 stimulation levels. (c) HVC (High Vocal Center) response to neural stimulation in area X.

