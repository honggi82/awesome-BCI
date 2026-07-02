Video Article

# Using an EEG-Based Brain-Computer Interface for Virtual Cursor Movement with BCI2000

J. Adam Wilson1, Gerwin Schalk2, Léo M. Walton1, Justin C. Williams1 1Department of Biomedical Engineering, University of Wisconsin-Madison 2Wadsworth Center, New York State Dept. of Health

Correspondence to: J. Adam Wilson at jawilson@cae.wisc.edu URL: http://www.jove.com/details.php?id=1319 DOI: 10.3791/1319

Citation: Wilson J.A., Schalk G., Walton L.M., Williams J.C. (2009). Using an EEG-Based Brain-Computer Interface for Virtual Cursor Movement with BCI2000. JoVE. 29. http://www.jove.com/details.php?id=1319, doi: 10.3791/1319

Abstract

A brain-computer interface (BCI) functions by translating a neural signal, such as the electroencephalogram (EEG), into a signal that can be used to control a computer or other device. The amplitude of the EEG signals in selected frequency bins are measured and translated into a device command, in this case the horizontal and vertical velocity of a computer cursor. First, the EEG electrodes are applied to the user s scalp using a cap to record brain activity. Next, a calibration procedure is used to find the EEG electrodes and features that the user will learn to voluntarily modulate to use the BCI. In humans, the power in the mu (8-12 Hz) and beta (18-28 Hz) frequency bands decrease in amplitude during a real or imagined movement. These changes can be detected in the EEG in real-time, and used to control a BCI ([1],[2]). Therefore, during a screening test, the user is asked to make several different imagined movements with their hands and feet to determine the unique EEG features that change with the imagined movements. The results from this calibration will show the best channels to use, which are configured so that amplitude changes in the mu and beta frequency bands move the cursor either horizontally or vertically. In this experiment, the general purpose BCI system BCI2000 is used to control signal acquisition, signal processing, and feedback to the user [3].

Protocol

## Experimental Procedure

- 1. Connecting the EEG Electrodes

- 1. Electrodes will be attached to the scalp using an EEG cap; this simplifies the process of ensuring that the electrodes are in the proper location on the scalp, as specified by the 10-20 international system.
- 2. To place the cap, mark the vertex on the subject's scalp using a felt-tip pen or some other similar method. To do so, begin by locating the nasion and inion on the subject. Using a tape measure, find the distance between these two locations. The point midway between the two points, or 50% of the distance, is the vertex. Make a mark at that point for later reference. Other 10-20 points can be located in a similar manner.
- 3. Find the Cz electrode on the cap, and position it on the vertex. Keeping Cz fixed, slip the cap onto the head. Ensure that the Fz, Cz, and Pz electrodes are on the midline of the scalp, and that the O1-O2 electrodes are horizontal and level with Oz, and that Fp1-Fp2 are level with Fpz.
- 4. Now attach the reference electrode, which typically clips onto an earlobe.
- 5. Next, the electrodes are filled with a conductive gel so that the electrodes make a low-impedance contact with the scalp. To do so, a small syringe with a blunt-tipped needle is filled with the gel. Also, it may be helpful to see the EEG traces on the computer screen while the gel is being applied to determine if the connection is good.
- 6. Insert the needle into an electrode, and gently abrade the scalp with the needle to remove any dead skin. Fill the electrode with a small amount of gel, being careful not to overfill it. Start with the ear reference electrode, and repeat for all of the electrodes, including the ground.
- 7. Check the impedances for all channels, which should all be less than 5 kΩ. This method will vary depending on the particular amplifier system being used, but it should be possible to check the impedance either through hardware or through BCI2000.
- 8. If an electrode is over 5 kΩ, insert the needle again, and abrade the scalp some more. It should not be necessary to inject more gel, unless there are no decreases in the impedance.

- 2. Obtaining EEG Calibration Features

- 1. At the start of a session, particularly the first time a subject is being tested, it is useful to determine the EEG features that can be used for controlling a BCI. This is because although the basic properties of the Mu and Beta EEG rhythms are the same for all people, these features will vary from person to person, and therefore need to be calibrated prior to any other experiments.
- 2. In the calibration session, the subject is instructed to imagine different movements involving their hands or feet in response to visual cues presented on the monitor. To get started, the computer system should be configured for dual-monitor mode, so that the researcher’s display contains the control software, and the second monitor displays the experimental output.
- 3. Start BCI2000 from the BCI2000Launcher by selecting your amplifier source module, the ARSignalProcessing module, and StimulusPresentation module. In this example, we are using the gUSBampSource module, which controls the g.USBamp amplifier.
- 4. Add the parameter files for your subject, the amplifier, and the motor screening tasks. These should be configured ahead of time, so that they can simply be loaded, and the experiment can start.
- 5. Once the parameter files have been added to the file list in BCI2000Launcher, press the Launch button. If everything worked correctly, BCI2000 should start, a trace of the EEG data should appear, and the subject’s monitor should be blank prior to the start of the experiment.
- 6. During the session, the screen will either be blank, or display an instruction, such as “Right Hand,” “Left Hand,” “Both Hands,” or “Both Feet.” The instruction will appear on the screen for 3s; during this time, the subject should continuously imagine the movement. The

hand movements should be opening and closing the hands (e.g., like squeezing a tennis ball), and the foot movement should be moving the feet back and forth (e.g., like pressing on a gas pedal with both feet). When the screen is blank, the body should be completely relaxed.

7. During a run, each body part is repeated 20 times. Ideally, there should be 100 data points, meaning that there should be a total of 5 runs. With multiple sessions, fewer runs are necessary, since the subject is able to perform the imagined task better.

- 3. Analyzing the EEG Features

- 1. In order to determine which EEG features the subject is able to voluntarily modulate in order to control the BCI, the calibration data is analyzed offline using the BCI2000 Offline Analysis tool, included with BCI2000. This tool converts the collected data into frequency domain features, which shows the frequencies and locations that changed during the different movements, and are maximally correlated with the tasks. These features can then be used in a BCI experiment.
- 2. To determine which features should be used, start the BCI2000 Offline Analysis tool. BCI2000 includes an extensive tutorial for using the analysis tool, which should be consulted for more information.
- 3. Determine which EEG features are strongly correlated with each movement by finding the large r-squared values in the plots produced from the analysis tool. The channels and frequency bins with the largest r-squared values (e.g., greater than 0.2) can then be selected as a control signal component for a particular direction. For example, features that change for the Right Hand condition should be set up to move the cursor to the right side of the screen.
- 4. It is also important to remember that the Mu/Beta rhythms decrease in amplitude with an associated movement. So, in order to move the cursor to the right, the positive x-direction, this feature should have a negative weight associated with it.
- 5. The channels and frequencies chosen should be consistent with known properties of cortical sensorimotor rhythms. That is, significant changes corresponding with imagined right hand movement should be seen over the contralateral (left) motor cortex, near C3 and CP3 and centered near 8-12 Hz and/or 18-28 Hz. Similarly, left hand movements should result in changes over right motor cortex on the C4 and CP4 electrodes, and foot movements should appear over Cz and CPz. If these locations and values are different, then it is likely that some other noise or random effect was measured, and should not be configured as a control feature.
- 6. For each condition, the four largest r-squared values should be chosen in terms of the channel number and bin number. The frequencies are arranged in 2 Hz bins, so a feature with a high r-squared from 10-12 Hz would appear in bin 6. With these values in hand, the system can be configured for the cursor control task.

- 4. Online Feedback Session Configuration

- 1. Configure the cursor movement session in the BCI2000 Launcher.
- 2. Before starting the experiment, several parameters need to be configured. First, the spatial filter should be configured with a common-average reference. To do so, press Config in the BCI2000 operator to bring up the settings list, and press the Filtering tab.
- 3. Go to SpatialFiltering, and change the SpatialFilterType drop-down box so that it says “Common-Average Reference (CAR).”
- 4. Under SpatialFilter CAR Output, list the channel names or numbers selected in the calibration session. For example, you can type “C3 CP3 C4 CP4 Cz CPz” (without the quotes), and BCI2000 will know which channels to use (provided that the channel labels are listed under the “Channel Names” field in the Source tab).
- 5. Next, the classification matrix must be configured to use the features selected. Under the Filtering tab, go to the Classifier parameter and press Edit Matrix.
- 6. The number of columns should be set to 4, and the number of rows should be equal to the total number of features selected. Each matrix row corresponds to an individual feature.
- 7. The first column should contain all of the channel names being used, e.g., C3, C4, etc. The second column contains the bins selected for control. It is possible enter either a bin number or specific frequency; entering “6” or “11Hz” will select the same bin, provided that the BinWidth parameter is “2 Hz” under the Source tab. The third column is the output channel; a value of “1” corresponds to horizontal movement, and “2” corresponds to vertical movement. The channels C3, CP3, C4, and CP4 should be set to 1 for a horizontal cursor control task; C3, CP3, C4, CP4, Cz and CPz should be set to 2 for a vertical cursor control task. Finally, the fourth column holds the feature weight, and should correspond to the opposite intended direction, e.g., C3 and CP3 should be weighted -1 to move the cursor right, and C4 and CP4 should be weighted 1 to move it left. To move the cursor down, Cz and CPz should be weighted 1, and to move the cursor up, C3 and C4 should be weighted -1.

- 5. Cursor Movement Task

- 1. Now that the system is configured with the correct settings, it is time to start the experimental task.
- 2. The system is configured so that one of four targets will appear during a trial. The subject’s goal is to move the cursor to the correct target using imagined movements corresponding to the desired direction of movement (e.g., right-hand to move right, feet to move down, etc).
- 3. For the first trials, the cursor is constrained to the axis of the target. That is, if the target is at the top or bottom, it is only possible to move the cursor up or down, and if it is at the left or right of the screen, the cursor can only be moved left or right.
- 4. When the run starts, the letter “T” appears on the screen for 2 seconds. Next, one of the targets appears for 1 second.
- 5. After this 1-second period, the cursor appears in the middle of the screen. The subject uses the appropriate imagined movements to direct the cursor to the target. If the subject hits the target, it changes color. Otherwise, the subject has 5 seconds to hit the target before the session times-out and is counted as a miss.
- 6. After the trial, there is a 2 second inter-trial interval during which the subject can relax, blink, swallow, or otherwise re-adjust positions. During the trials, movement should be kept to an absolute minimum to reduce movement artifacts or muscle artifacts. It is also beneficial to sit in a dimly lit room in a comfortable chair.
- 7. After 20 trials, BCI2000 enters a suspended state. During this time, it may be necessary to re-adjust some of the settings if the subject is unable to move the cursor.
- 8. If after 4 runs the subject is still unable to volitionally move the cursor, it may be necessary to re-analyze the collected data in the BCI2000 Offline Analysis tool. Select the new channels and frequencies based on the new feature plots. It may take several runs or possibly several sessions before a subject can become proficient at the task.

Part 6: Representative Results:

- 1. Figures 1 and 2 show the r-squared values and scalp topography for the calibration procedure, indicating which channels and frequency bins should be selected for cursor control.
- 2. A trained subject should be able to quickly move the cursor to the shown target within 1 or 2 seconds.

[Figure 4]

### Figure 1 A) and B) Topography of spectral changes in the 10-12 Hz band during real and imagined movements with the right hand. C) The power spectrum on C3 during rest (dashed) and movement (solid). D) The r-squared of the power during movement compared to rest.

[Figure 5]

- Figure 2 The r-squared across all channels for imagined right-hand movement. The x-axis is the frequency in 2 Hz bins from 0 to 70 Hz. The y-axis is the channel number. The highest r-squared values are found on channels 9, 10, 17, 18, and 19, which cover the contralateral hand area of motor cortex.

Discussion

- 1. It is vital that the electrode impedances are low, but that too much gel was not used to lower the impedance. A single bad channel can affect all the others through the common-average reference. If the impedance cannot be reduced after several tries, it is recommended that a quick-insert electrode be used, which can simply be inserted into the bad electrode through the hole that the needle is placed through for injecting the gel, and taped in place.
- 2. During the first session, the subject may have difficulty imagining the required movements. In this case, it may be helpful to have them make the real movements first, and perform the offline analysis the real movement data. Configure the cursor movement session as before with the real movement data, and have the subject use the actual movements to attempt to move the cursor. After a few runs, have them gradually stop making the real movement, until they have stopped completely. After several sessions, most users stop using motor imagery altogether, and instead just “move” the cursor.

Acknowledgements

NIH NIBIB RO1: 1R01EB009103-01 Clinical Neuroengineering Training Program (1 T90 DK070079-01) Wallace H Coulter Foundation NIH Institutional Clinical and Translational Science Award NIH/NCRR 1KL2RR025012-01 Wisconsin Alumni Research Foundation

References

- 1. G. E. Fabiani, D. J. McFarland, J. R. Wolpaw, and G. Pfurtscheller. Conversion of eeg activity into cursor movement by a brain-computer interface (bci). IEEE transactions on neural systems and rehabilitation engineering : a publication of the IEEE Engineering in Medicine and Biology Society, 12(3):331–8, Sep 2004.
- 2. J. R. Wolpaw and D. J. McFarland. Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. Proc Natl Acad Sci USA, 101(51):17849–54, Dec 2004.
- 3. G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw. Bci2000: a general-purpose brain-computer interface (BCI) system. IEEE transactions on bio-medical engineering, 51(6):1034–43, Jun 2004.

