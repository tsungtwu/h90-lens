# H90 Lens — Full Algorithm Reference

> Eventide H90 Harmonizer — All algorithms with complete parameter details.
> Data sourced from H90 Manual v1.12.5.

## Delay

### Band Delay

Delays are followed by user selectable modulated filters.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value from No Delay to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as A.
- **Resonance** `0-10`: Sets the resonance or sharpness of the filter. Varies from 0 (subtle effects) to 10 (dramatic resonance effects).
- **Modulation Depth** `0-10`: Sets the amount that the filter cut-off or center frequencies are modulated/shifted.
- **Modulation Speed** `0-5Hz`: Sets the modulation rate for the filter center frequencies (0 to 5 Hz).
- **Filter**: Select filter type – Low Pass, Band Pass or Hi Pass.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Bouquet Delay

Emulation of analog delay pedals with two different flavors and modern tricks.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 0 to 50 mixes in the delayed signal, 50 to 100 mixes out the dry signal.
- **Delay** `75-1000ms`: Delay length control for the Delay mode in milliseconds. Shorter delay lengths brighten the signal delay line output. Both LoFi and Modern modes can make use of the full delay time range, but the hardware that served as the inspiration for LoFi mode was only intended to be used up to 300 ms. Anything above that and you’re seriously under-clocking the chip.
- **Feedback** `0-10`: Controls the level of feedback in the delay path for both the Short and Long delay modes. Capable of driving the delay into self oscillation close to 10 (not precise due to other settings in the BBD affecting feedback) in Modern mode, and at varying amounts (depending on delay time settings) in LoFi. (75 ms to 1000 ms)
- **Mod Depth** `0-10`: Controls the amount of modulation applied to the BBD delay line. Note that modulation amounts will vary depending on the Delay time.
- **LFO Rate** `0.01-20Hz`: Controls the speed/rate of the modulation LFO. (0.01 Hz to 20 Hz)
- **LFO Shape**: LFO Shape of the modulation oscillator. The choices are: SINE FATSINE TRIANGLE SQUARE SAW RAMP NOISE
- **Delay Mode**: (Lofi/Modern) Two different options for delay sounds. LoFi emulates an early bucket brigade pedal that was limited to a delay time of 300 ms. Modern will be a little brighter/cleaner sounding and the self-oscillation will be a little more uniform.
- **Jump Interval**: Controls the ratio used to jump the delay time when using the PitchJump performance parameter. (m3, M3, P4, P5, Oct.)
- **Stereo Tap Division**: When stereo outputs are connected, a second tap out of the BBD emulation is connected to the second channel. This controls the point at which this second delay is tapped out of the BBD.

#### Performance Parameters

- **Self Osc**: A momentary or latching performance parameter that causes the BBD emulation to self-oscillate.
- **Pitch Jump**: A momentary or latching performance parameter that instantaneously scales the delay time (clock frequency) of the BBD emulation by the ratio determined by the Jump Interval parameter. This causes a momentary pitch shift of any sound being fed back through the BBD emulation.
- **Retrigger**: Retriggers the modulation LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Digital Delay

Twin 3 second delays with independent delay time and feedback controls.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value from No Delay to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as A.
- **X-Fade** `2-200ms`: When delays change, performs a crossfade function to prevent abrupt changes that could result in glitching or clicking. X-Fade sets the speed of the crossfade. Small values result in rapid crossfades, larger values more gradual crossfades. Crossfade rates vary from 2 ms to 200 ms.
- **Modulation Depth** `0-10`: Selects the amount of delay modulation (0 = Off, 10 = Max).
- **Modulation Speed** `0-5Hz`: Sets the delay modulation rate (0 - 5 Hz).
- **Filter** `-100 to 100`: A low pass/high pass filter variable from -100 (max high pass) to 0 (no filtering) to 100 (max low pass) to change the tone of your delay repeats.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Ducked Delay

Delay levels dynamically lower during playing and restore when silent.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time for Delay A output from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value - changing this from 0 to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as A.
- **Ducking Ratio** `0-10`: Sets the ducking ratio or the degree to which the delay is attenuated.
- **Threshold** `-36 to -66dB`: Sets the ducking threshold - the audio amplitude - at which ducking kicks in (-36 dB to -66 dB).
- **Release Time** `10-500ms`: Sets the release time from 500 to 10 ms. With the release time set to short values, the delay will kick in quickly when you stop playing. With the release time set to longer values, the delay will stay ducked for a while. Longer release times are useful when you’re playing a riff and don’t want the delay to kick in between notes.
- **Filter** `-100 to 100`: A low pass/high pass filter variable from -100 (max high pass) to 0 (no filtering) to 100 (max low pass) to change the tone of your delay repeats.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Filter Pong

Dual delays ping pong between outputs with filter effects.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time for Delay A output from 0 to 3000 ms. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value - changing this from 0 to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats. The FilterPong Effect is created by cross connecting the feedback paths of the twin delays. As a result, only a single feedback control is needed.
- **Slur** `0-10`: Controls the diffusion of the repeats. With low diffusion the repeats are discrete. Increasing diffusion slurs the repeats.
- **Modulation Wave Shape**: Selects the shape of the filter modulation. The options are: Sine Triangle Square
- **Modulation Depth** `0-10`: Sets the filters’ amount of frequency modulation.
- **Modulation Speed** `0-10`: Speed multiplier for filter modulation.
- **Filter** `-100 to 100`: Controls the mix of dry/filtered signal input to ping-pong delay.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Head Space

Authentic tape delay emulation with adjustable playback heads, wow/flutter, drive, and hiss controls.

#### Parameters

- **Mix** `0-10`: Controls the levels of the dry and wet (tape delayed) signals to the output of the effect. 0 to 5 mixes in the delayed signals. 5 to 10 mixes out the dry signal.
- **Delay Time** `200-3000ms`: Controls the longest delay length possible of any one Head by changing the tape speed. Use a Head Div of 1 to reach full delay time of any one tap. 200-3000 ms.
- **Speed**: Runs the tape emulation at either Half or Full speed while keeping the overall delay amounts the same. At Full speed the machine ranges from 30 ips to 1.875 ips. At Half the machine ranges from 15 ips to a glacially slow speed of 0.9375 ips.
- **Rec Drive** `0-10`: Higher levels saturate the tape creating an overdriven sound
- **Feedback** `0-10`: Master Feedback control for all Heads. Capable of driving the tape delay into self oscillation from around 7 to 10 (not precise due to other settings affecting feedback structure and levels in the feedback loop).
- **Fdbk Path**: Controls which Heads contribute their output to the feedback loop. The options are: 1, 2, 3, or 4 1 & 2 1 & 3 1 & 4 2 & 3 2 & 4 3 & 4 1 & 2 & 3 1 & 2 & 4 1 & 3 & 4 2 & 3 & 4 All
- **Wow & Flutter** `0-10`: Controls the amount of mechanical anomalies of a real tape machine. These anomalies manifest as pitch warbles and delay variations. Use 0 for a perfectly constructed and maintained high end tape machine. Use 10 for a lower end, old tape machine in need of some serious repair.
- **Tape Hiss** `0-10`: Controls the amount of tape hiss. 0 is no hiss. 10 is the most amount of hiss. Control is global over all playback heads.
- **Filter** `-10 to 10`: Equalization control for all Head outputs. The outputs of the EQs are in the feedback loop. -10 to 0 Low cut shelf. 0 to 10 Hi cut filter (low pass). The following parameters apply to all 4 tape heads:
- **Boil Time** `200-10000ms`: Controls the time it takes for the Boil performance parameter to ramp up to its apex. 200 to 10000 ms.
- **Break Time** `200-10000ms`: Controls the time it takes for the machine to ramp down to its slowest speed when the Breakdown performance parameter is engaged. 200 to 10000 ms.

#### Performance Parameters

- **Boil**: These reels sure do seem like they’re spinning fast. Does anyone smell smoke?
- **Breakdown**: Someone pulled the plug, the servos have decided they’re tired of spinning. Either way things really seem to be s l o w i n g d o w …

---

### Mod Delay

Modulated delays for creating chorus effects and chorused delays.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value from No Delay to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as A.
- **Modulation Wave Shape**: Selects the modulation wave shape. There are two choices for each wave shape. The single waveforms modulate the two delays in phase and the double waveforms modulate the two delays out of phase.
- **Modulation Depth** `0-20`: Selects the amount of delay modulation (0 = Off, 20 = Max).
- **Modulation Speed** `0-5Hz`: Sets the delay modulation rate (0 - 5 Hz).
- **Filter** `-100 to 100`: A low pass/high cut filter variable from -100 (max low cut) to 0 (no filtering) to 100 (max high cut).

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### MultiTap

10 delay taps with controls for delay time, diffusion, tap levels, and spacing.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value from No Delay to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as A.
- **Slur** `0-10`: Controls the diffusion of the repeats from discrete to slurred.
- **Taper** `-10 to 10`: Sets the relative level (taper) of the taps. With Taper at -10, the 1st tap is the quietest and the last tap loudest. With Taper at 0, all taps are equally loud. With Taper at 10, the 1st tap is loudest and the last tap quietest.
- **Spread** `0-10`: Sets the spacing between taps from 0 (spacing increases) to 5 (taps are equally spaced) to 10 (spacing between taps decreases).
- **Filter** `0-10`: Tone control that reduces high frequencies to darken the ambient sounds that you create.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Reverse

Audio segments are reversed, spliced, and crossfaded to prevent artifacts.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A**: Sets delay time for Delay A output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value - changing this from 0 to a whole note in common note increments.
- **Delay B**: Same as Delay A
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as Feedback A.
- **X-Fade** `2-200ms`: In Reverse, the audio segments are read backwards and must be spliced. Crossfades occur at the splice point to prevent abrupt changes that could result in glitching or clicking. X-Fade sets the rate of the crossfade. Small values result in fast crossfades and a more audible rhythm for the reverse effect, larger values more gradual crossfades and a smoother reverse sound. Crossfade rate is variable from 2 ms to 200 ms.
- **Modulation Depth** `0-10`: Selects the amount of modulation (0 = Off, 10 = Max).
- **Modulation Speed** `0-5Hz`: Sets the delay modulation rate (0 - 5 Hz).
- **Filter** `-100 to 100`: A low pass/high pass filter variable from -100 (max high pass) to 0 (no filtering) to 100 (max low pass) to change the tone of your delay repeats.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### Tape Echo

Simulates analog tape delay with hiss, wow, flutter, and saturation controls.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time for Delay A output B from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value - changing this from 0 to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as Delay A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as Feedback A.
- **Saturation** `0-10`: Simulates analog tape saturation. Ranges from ‘0’ (none) to ‘10’ (max) for the warm compression and distortion associated with overdriven tape.
- **Tape Wow** `0-10`: Simulates analog tape Wow. Wow is a term used to describe relatively slowly changing pitch and amplitude modulations caused by problems with the motor or tape transport that causes the tape’s motion across the head to vary. A well maintained tape recorder should have no audible Wow. Ranges from ‘0’ (none) to ‘10’ (max).
- **Tape Flutter** `0-10`: Simulates tape machine Flutter. Like Wow, Flutter is caused when the tape motion across the magnetic heads isn’t constant. Flutter is a more rapidly changing variation than Wow. Flutter ranges from 0 (none) to 10 (max).
- **Filter** `0-10`: Controls the filter characteristics to simulate tape recorder frequency response. As you increase the filter value, you’ll hear a more pronounced tape tone.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

### UltraTap

Versatile multi-tap delay capable of rhythmic, glitchy, pad-like swells, reverbs, and tremolo effects.

#### Parameters

- **Mix** `0-100%`: Wet/Dry mix, where 100 is an all wet signal. It has a special nonlinear taper which puts most of the knob travel in the most usable range.
- **Length** `0-10s`: Total time over which the Taps are spaced in, up to 10 seconds.
- **Taps** `1-64`: The number of delay taps, from 1 to 64.
- **Predelay** `0-1s`: The amount of time before the first Tap starts, up to 1 second.
- **Spread** `-10 to 10`: The rhythmic spacing of the taps. Positive values will group more taps towards the end for a “speeding-up” delay sound. Negative values will group taps towards the beginning, for a “slowing-down” feeling. Zero results in constant spacing.
- **Taper** `-10 to 10`: Controls the fade of the taps. Positive values for a fade-down over the taps. Negative values for fade-up over the taps. Zero will result in equal gain across all taps.
- **Feedback** `0-10`: Repeats of a length-valued delay that is fed back around the entire multi-tap machine.
- **Tone** `-10 to 10`: A tone control. Positive values for brighter sounding taps. Negative values for darker sounding taps.
- **Slurm** `0-10`: Juicy tap slurring/smearing and modulation.
- **Chop**: A pre-tap-machine “chopping’ tremolo OR auto-volume processor. The tremolo has several LFO waveform choices: Off Triangle Sawtooth Ramp Square
- **Width** `-10 to 10`: Adjust how the taps are evenly distributed in the stereo field. 0 will result in the no distribution, while positive values will increasingly distribute the taps more, and negative values will reverse this image.

#### Performance Parameters

- **Retrigger**: Retriggers the modulation LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Vintage Delay

Simulates analog and digital delays from past eras with bit-resolution and filter controls.

#### Parameters

- **Mix** `0-100%`: wet/dry mixer, 100% is all wet signal.
- **Delay Mix** `0-100%`: Controls the relative level of Delay A and Delay B. Delay Mix’s mixing behavior depends on whether you’re using mono or stereo outputs. For mono output: Delay Mix = 0%, output 1 will have only delay A’s contribution. Delay Mix = 50%, output 1 has an equal amount of delay A and delay B. Delay Mix = 100%, output 1 will have only delay B’s contribution. For stereo output: Delay Mix = 0%, both outputs will have only delay A’s contribution. Delay Mix = 50%, delay A goes to output 1 only and delay B goes to output 2 only. Delay Mix = 100%, both outputs will have only Delay B’s contribution.
- **Delay A** `0-3000ms`: Sets delay time for Delay A from 0 to 3000 ms (milliseconds). With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value - changing this from 0 to a whole note in common note increments.
- **Delay B** `0-3000ms`: Same as Delay A.
- **Feedback A** `0-10`: Controls level of Feedback A, the number of repeats.
- **Feedback B** `0-10`: Same as Feedback A.
- **Bits**: Selects the number of bits of resolution. Early digital delays used analog to digital converters with limited resolution. Theory predicts that each bit equals 6 dB of resolution; so that an 8 bit converter would deliver, at best, a mere 48 dB of dynamic range. Vintage Delay simulates the effects of limited resolution - the sound of nasty digital noise from years gone by.
- **Modulation Depth** `0-10`: Selects the amount of delay modulation (0 = Off, 10 = Max).
- **Modulation Speed** `0-5Hz`: Sets the delay modulation rate (0 - 5 Hz).
- **Filter** `0-10`: Controls the filter to simulate the tone of band-limited old school delays.

#### Performance Parameters

- **Repeat**: A momentary or latching parameter that sets the feedback to the highest value.

---

## Distortion

### Aggravate

An Octave fuzz inspired by famous classic analog octave fuzzes from the 70's with versatile controls and chewy tone.

#### Parameters

- **Mix**: The clean/dirty mix, full left is clean, full right is dirty.
- **Fuzz**: The amount of fuzz.
- **Octave**: Enables or disables the analog-style octave effect
- **Thick**: Makes the fuzz thick (or thicker).
- **Mids** `-100 to 100`: Midrange control for the stage. -100 to 0 removes midrange for a more scooped sound. 0 to 100 adds midrange.
- **Tone** `-100 to 100`: -100 to 0 rolls off the treble creating a bassier tone. 0 to 100 brightens the effect.
- **Bias**: Increasing this control will add a “spitty” characteristic to your tone.
- **Filter Env**: Controls the sensitivity of the filter envelope follower. Negative values will start at a high cutoff frequency and move lower as you play; positive values will start at a low cutoff frequency and move higher as you play. At 0 there will be no filtering.
- **Env Shape**: Shape of the enveloper filter. Exponential is suggested for guitar, while Linear is suggested for bass.
- **Resonance**: Controls the resonance of the filter.
- **Pump Depth**: Controls the ratio of the pumping compressor. Increasing this will make the pumping effect more pronounced.
- **Pump Control**: Sets what the pump is controlled by. Pump Rate uses the included LFO, manual lets you control the Pump as a performance control.
- **Pump Rate** `0.50-5 Hz`: Adjusts the speed of the pump rate from .50 - 5 Hz. Higher pump rates work better with shorter release times.
- **Release**: Release time of the pump effect.

#### Performance Parameters

- **Pump**: Manually triggers the Pump effect. Only works when Pump Control is set to Manual.
- **Retrig**: Retriggers the LFO of Pump Rate.

---

### CrushStation

An overdrive/distortion command center enabling creamy saturation to brutal sonic assault with stereo capability.

#### Parameters

- **Mix**: The clean/dirty mix, full left is clean, full right is dirty.
- **Drive**: The overdrive amount. Ranges from subtle boost/overdrive to full on distortion with Grit and Sustain controls pushing it into fuzz territory.
- **Compressor/Sustainer**: Compression/Sustain which is Pre distortion (counterclockwise), or Post distortion (clockwise). The sustainer is specially designed to vary the numerous parameters of a typical compressor such as the ratio, attack, release, and the makeup gain to keep the overall loudness consistent.
- **Sag**: Turn it up to get increasingly sputtery, crushed, and broken sounds. Inspired by power rail sag of poorly designed tube amps and the dead and dying gear of times past.
- **Octaves**: Mixes in/out lower and higher pitch-shifted octaves before the distortion and compression.
- **Grit**: Adds more low end before the distortion for a gritty chugging sound.
- **Bass**: Cut and boost lower frequencies to hollow out the sound or add some thud.
- **Mids**: Cut and boost mid range frequencies (frequency selectable with Mids Frequency control) to scoop some muddiness or punch through a mix.
- **Mids Frequency**: Tunable center frequency of the Mids cut/boost. Similar to a parked wah when boosted up high. Smoothly changes when connected to an expression pedal.
- **Treble**: Cut and Boost higher frequencies to mellow out the sound or emphasize higher harmonics.

---

### PitchFuzz

Multi-effect combining Fuzz, three Pitch Shifters, and two Delays with flexible routing for arpeggiated effects.

#### Parameters

- **Fuzz** `0-100`: Controls the amount of Fuzz/Distortion generated after the input signal. A setting of 0 completely bypasses the Fuzz effect. Use 1 to 50 for a distortion type effect and 51 to 100 for more of a Fuzz type effect.
- **Fuzz Tone**: Tone shaper for the fuzz effect.
- **Pitch Amount**: Controls the level of the three Pitch Shifters. From 0 to 3 Voices. Pitch A: 0 to 1.0, Pitch A + B: 1.0 to 2.0, Pitch A + B + C: 2.0 to 3.0.
- **Pitch A** `±2 octaves`: Adjust the pitch shift amount of the A voice. Range is +/- 2 octaves with micro pitch shift ability at unison (+/- 25c).
- **Pitch B** `±2 octaves`: Same as Pitch A.
- **Pitch C** `±2 octaves`: Same as Pitch A.
- **Delay Level**: Controls the amount of both Delays in the signal path as well as two types of Delay routings (Group Delay and Arp Delay). Starting fully counter-clockwise, Group Delay sends the whole signal including all of the Pitched Voices to both delays. Turning past center activates Arpeggiated Delay Mode. In this mode, only voices B and C are fed to the delays (separately and respectively) allowing the creation of arpeggiated effects. Try this with Pitch Amount set to 3.0.
- **Delay A** `0-2500ms`: Sets the Delay time for Delay A from 0 to 2500 ms when Tempo Sync is OFF. With Tempo Sync ON, Delay is adjusted in note division increments from No Delay to a Whole Note in the most common note divisions.
- **Delay B** `0-2500ms`: Same as Delay A.
- **Feedback**: Adjusts the amount of feedback for both delays and contains two feedback types (F1 and F2). F1 links both delay times to create a rhythmic, repeating pattern where the longer delay sets the pattern length. The shorter delay will not repeat again until the longer delay has passed. F2 is a traditional feedback control, where delay times are independent.

---

### Sculpt

Multi-band Distortion with Envelope Follower Control Filters for carving out your own sound.

#### Parameters

- **Mix**: The clean/dirty mix, all the way left is clean, all the way right is dirty.
- **Band Mix**: The mix between the low and high band.
- **Crossover Frequency**: The crossover frequency where the low band and high band are split.
- **Low Drive**: Overdrive of the low band.
- **High Drive**: Overdrive of the high band.
- **Compressor**: Pre distortion (counter-clockwise), or Post distortion (clockwise). Turn counter-clockwise to juice up the harmonics in the distortion, or turn clockwise for some sparkly compressor spank. The Sculpt compressor is specially designed to vary the numerous parameters of a typical compressor such as the ratio, attack, release and the makeup gain to keep the overall loudness consistent.
- **Low Boost**: Boosts the low end either Pre distortion (counter-clockwise) for chuggier low end, or Post distortion (clockwise) for smoother low end.
- **Filter-Pre**: Peaking filter Pre distortion. Turning left sweeps a cutting filter up in frequency. Turning right sweeps a boosting filter up in frequency, similar to having a parked wah before the distortion. Smoothly changes when connected to an expression pedal.
- **Filter-Post**: Peaking filter Post distortion. Turning left sweeps a cutting filter up in frequency. Turning right sweeps a boosting filter up in frequency, similar to having a parked wah after the distortion. Smoothly changes when connected to an expression pedal.
- **Envelope Follower**: Envelope follower that modulates both Filter-Pre and Filter-Post according to this input sensitivity setting. The values of Filter-Pre and Filter-Post become the depths that the envelope glides up to. Interesting dynamic changes are achieved when pre and post are set to opposite sweeps, e.g. Pre boost, and Post cut, etc.
- **Stereo Mode**: Split features unique spectral panning effects that spread the hi and lo bands out into the separate channels. Dual Mono outputs the same signal to both outputs channels.

---

### WeedWacker

Two stage, serial overdrive effect reminiscent of a famous green overdrive.

#### Parameters

- **Mix**: Global mix level of the entire WeedWacker effect.
- **Gate Threshold**: Adjusts the noise gate threshold for the entire effect. -90 dB is off.
- **Stage 2**: Activates or bypasses the 2nd overdrive stage. The following parameters are available for both Stage 1 and 2:
- **Drive 1** `0-100`: Sets the distortion level of the overdrive stage. 0 is cleanest. 100 is dirtiest.
- **Tone 1** `-100 to 100`: Tone control for the stage. -100 to 0 rolls off the treble creating a bassier tone. 0 to 100 brightens the effect.
- **Mids 1** `-100 to 100`: Midrange control for the stage. -100 to 0 removes midrange for a more scooped sound. 0 to 100 adds midrange.
- **Level 1**: Final output level control for the stage.
- **Drive 2** `0-100`: Sets the distortion level of the overdrive stage. 0 is cleanest. 100 is dirtiest.
- **Tone 2** `-100 to 100`: Tone control for the stage. -100 to 0 rolls off the treble creating a bassier tone. 0 to 100 brightens the effect.
- **Mids 2** `-100 to 100`: Midrange control for the stage. -100 to 0 removes midrange for a more scooped sound. 0 to 100 adds midrange.
- **Level 2**: Final output level control for the stage.

---

## EQ

### EQ Compressor

A multi-featured parametric equalizer coupled with a dynamic, intuitive compressor for premium tone shaping.

#### Parameters

- **Gain 1** `±12dB boost / -18dB cut`: The gain of the first parametric filter. Provides 12 dB of boost or 18 dB of attenuation.
- **Frequency 1** `30-1500 Hz`: The center frequency of the first parametric filter. The frequency ranges from 30 Hz to 1500 Hz.
- **Width 1** `1-10`: Controls the bandwidth of the 1st parametric filter. A value of 10 represents a larger bandwidth while a value of 1 represents a narrower bandwidth.
- **Gain 2** `±12dB boost / -18dB cut`: The gain for the 2nd parametric filter. Provides 12 dB of boost or 18 dB of attenuation.
- **Frequency 2** `1000-9999 Hz`: The center frequency of the first parametric band. The frequency ranges from 1000 Hz to 9999 Hz.
- **Width 2** `1-10`: Controls the bandwidth of the 2nd parametric filter. A value of 10 represents a larger bandwidth while a value of 1 represents a narrower bandwidth.
- **Bass** `±12dB boost / -18dB cut`: Controls the gain on the Low Frequency Shelving Filter which is centered around 400 Hz with a slope of 8 dB/Octave. You can boost the lows by 12 dB or cut by 18 dB.
- **Treble** `±12dB boost / -18dB cut`: The gain on the High Frequency Shelving Filter which is centered around 1800 Hz with a slope of 8 dB/Octave. You can boost the highs by 12 dB or cut by 18 dB.
- **Compressor**: The amount of compression applied to the signal. The values to the left half of the knob will affect the Pre-EQ compression, increasing the amount of compression as you move it counterclockwise. The values to the right half of the knob will affect the Post-EQ compression, increasing the amount of compression as you move it clockwise. The compressor is specially designed to vary the numerous parameters of a typical compressor such as the ratio, attack, release and the makeup gain to keep the overall loudness consistent.
- **Trim** `±12dB`: Controls the level at the output of the signal path. Provides 12 dB of boost or 12 dB of attenuation. The Algorithm is designed to “gracefully” clip if there is too much gain inside the EQ.

---

## Granular

### Cosmic Web

High-end rack processing with a modern, macro granular package blending reverse pitched grains with classic Eventide reverb.

#### Parameters

- **Mix**: Dry / Wet Mixer.
- **Reverb**: Post Mix reverb on the whole signal.
- **AutoRetrig**: Level for dynamic retriggering of Reverse grain start AND gating effect.
- **Level**: Level for Voice A/B.
- **Length**: Length of Voice A/B grain in msecs or note values (tempo sync).
- **Pitch**: Pitch of voice A/B. Note: it’s really a speed control too, a higher pitch will repeat the grain within the Length.
- **Detune**: Fine pitch detuning of Voice A/B with a multi voice stereo spreading effect.
- **Feedback**: Amount grain delay feedback for Voice A/B.
- **Crystals**: Crystals style feedback around voice structures. Choices are: Off, A, B, A+B.
- **Ping Pong**: Puts Voices in ping pong mode using the stereo voices in series. Reverse Direction will have initial reverse grain on the left, and forward on the right. Choices are: Off, A, B, A+B.
- **Reverse**: Reverse grain playback. Choices are: Off, A, B, A+B.

#### Performance Parameters

- **Retrigger**: Manual reverse grain and gating retrigger for creative rhythmic effects.
- **Repeat A**: Sets infinite delay feedback for voice A, sustaining the current grain pattern indefinitely.
- **Repeat B**: Sets infinite delay feedback for voice B, sustaining the current grain pattern indefinitely.
- **Freeze**: Freezes the reverb tail, sustaining it indefinitely without new input.
- **Dump**: Clears the memory of both voices, silencing any sustained grains.

---

### Glitch

Slice, distort, and reconstruct audio with three distinct glitch types that work independently or stack together.

#### Parameters

- **Mix**: Wet/Dry Mixer.
- **Interrupt** `On/Off`: If set to On, Glitches will pause (interrupt) the dry audio.
- **Glitch Type**: Sets which glitch flavors are active. If a combination is selected, all active glitch flavors will be heard whenever a glitch occurs. Burst: This is the familiar behavior of many short grains grouped together and pitch shifted. Alias: This will apply aliasing to the input signal if no other glitch is happening, or else it will apply aliasing to the output of another glitch (Burst or Clock). Clock: If a Burst glitch is occurring, then the clock changes will be applied to the burst. Otherwise, a grain equal to the LENGTH will be triggered and the Clock jump will occur during this grain.
- **Trigger Mode**: Chance: glitches occur pseudorandomly according to the value of Chance. Envelope: a glitch occurs when the input reaches the Env Thresh value. Manual: glitches only occur when the Glitch Perform Parameter is pressed.
- **Chance**: Determines the probability (chance) that a glitch occurs when Trigger Mode is set to Chance.
- **Env Thresh**: Determines the threshold for input audio to trigger a glitch when Trigger Mode is set to Env.
- **Glitch Time** `60-8000ms`: Determines the length of a glitch. 60 ms - 8000 ms, or tempo synced
- **Glitch Fade** `0-100%`: A symmetric fade in/out for the Glitches when they occur as a percentage of the Glitch Time. 0 to 100% of Glitch Time
- **Flux**: Determines the number of times per Length that Alias Amount, Burst Rate, and the Clock will be randomly modulated. For Alias Amount and Burst Rate, the random values will be less than or equal to what the user has set for these values (e.g. if Alias Amount is 50, all random Alias Amount values will be less than or equal to 50). The clock may jump to any frequency. In tempo mode, the random modulations will be evenly distributed over the length; otherwise, they are randomly distributed over the length.
- **Alias Amount** `0-100`: Determines the amount of aliasing applied by decreasing the sample rate of the aliaser as the control is turned up. At a value of 100, the aliaser downsamples the input to 1.5 KHz.
- **Burst Rate**: Determines the rate at which grains are triggered during a Burst Glitch. Higher values correspond to more grains triggered during a burst, resulting in a denser sound.
- **Burst Pitch**: If set to a single interval, then when a Burst Glitch occurs, the audio will be pitch shifted by this interval whenever a pitch jump occurs. If Random Down, then -Oct, -P5, and -P4 will be chosen randomly. If Random Up, then +P4, +P5, and +Oct will be chosen randomly. If Random All, then any interval will be chosen randomly, including unison. Note that pitches closer to the most recent pitch will be favored for the next randomly selected pitch.
- **Clock Target** `8-36 kHz`: When FLUX is OFF, this sets the frequency that a clock glitch will resample the buffer to. The clock values are 8, 9, 12, 16, 18, 24, 32, or 36 KHz (Note that these values from right to left represent shifting by -P4, -P5, -Oct, -P11, -P12, -2Oct, -P18, -P19)
- **Reverb Mix**: A wet/dry control for the Reverb. Note that reverb is added to the dry signal as well.
- **Reverb Decay**: Controls the decay time of the reverb.
- **Width**: Determines the width of the stereo image.
- **Filter**: A resonant filter post-grains, pre-reverb. From 0 to 100: Decreases the cutoff frequency of a resonant low pass filter. From 0 to -100: Increases the cutoff frequency of a resonant high pass filter.

#### Performance Parameters

- **Glitch**: Triggers continuous glitch looping that persists until disengaged.
- **Glitch M**: Momentary glitch that is active only while the footswitch is held.

---

### GrainMod

Morph your sound with modulated grain parameters. Three independent LFOs target Trigger Rate, Grain Duration, and Filter.

#### Parameters

- **Mix**: Wet/Dry mixer.
- **Width** `0-100`: Increases the width of the stereo image. 0 is mono (though the reverb at the end of the signal chain is still stereo).
- **Delay** `0-1000ms`: Sets the amount of delay used by the granular processor. 0 to 1000 milliseconds, or tempo synced
- **Retrig Source**: Determines what control will retrigger the LFOs. If Manual, the perform mode footswitch RETRIGGER control will be used. If Env, the LFOs are retriggered every time the input is above a fixed, low threshold. This is to create a more predictable modulation sound whenever a new note/chord is played.
- **Reverb Mix**: A one knob reverb (from Cosmic Web) that increases mix and decay as the knob is increased. Note that reverb is added to the dry signal as well.
- **Direction Mod** `0-100`: Controls the amount of square wave modulation to the grain direction. At 0 all grains will be played forward, and at 100 all grains will be played backward. For intermediate values, grains will be played in both directions, with more grains being played in reverse as the knob is increased.
- **Direction Mod Rate** `0.01-20 Hz`: Sets the rate of the Direction LFO. 0.01 to 20 Hz, or tempo synced.
- **Trigger Rate** `0.2-32 Hz`: Sets the rate at which new grains are triggered. 0.2 to 32 Hz, or tempo synced.
- **Grain Duration** `20-2000ms`: Sets the duration of each grain. 20 to 2000 ms, or tempo synced.
- **Filter**: A resonant filter post-grains, pre-reverb. From 0 to 100: Decreases the cutoff frequency of a resonant low pass filter. From 0 to -100: Increases the cutoff frequency of a resonant high pass filter. Trigger, Grain Duration, and Filter each have a dedicated LFO with the following parameters:

#### Performance Parameters

- **Retrigger**: Resets all LFO waveform cycles to their starting position.

---

### Stutter

The classic granular effect. Create burst patterns with precise control over timing and subdivision.

#### Parameters

- **Mix**: Wet/Dry mixer.
- **Interrupt** `On/Off`: If set to On, stutter burst will pause (interrupt) the dry audio.
- **Filter**: A resonant filter post-grains, pre-reverb. From 0 to 100: Decreases the cutoff frequency of a resonant low pass filter. From 0 to -100: Increases the cutoff frequency of a resonant high pass filter.
- **Trigger Mode**: Chance: Stutter bursts occur pseudorandomly according to the value of Chance. Envelope: A stutter burst occurs when the input reaches the Env Thresh value. Manual: Stutter bursts only occur when the Stutter Perform Parameter is pressed.
- **Chance**: Determines the probability (chance) of a stutter burst when Trigger Mode is set to Chance.
- **Env Thresh**: Determines the threshold for input audio to trigger a stutter burst when Trigger Mode is set to Env.
- **Length**: Determines the length of a stutter burst.
- **Rate**: Determines the spacing of each individual stutter in a stutter burst. Also determines the rate at which audio is panned if using the Width control.
- **Smear** `25-300%`: Sets the duration of the individual stutters within a burst as a percentage of Rate. 25% to 300% of Rate.
- **Pitch Chance**: Determines the probability of a pitch jump by the interval or combination set by the Pitch control.
- **Pitch**: If set to a single interval, then the audio will be pitch shifted by this interval whenever a pitch jump occurs. If Random Down, then -Oct, -P5, and -P4 will be chosen randomly. If Random Up, then +P4, +P5, and +Oct will be chosen randomly. If Random All, then any interval will be chosen randomly, including unison. Note that pitches closer to the most recent pitch will be favored for the next randomly selected pitch.
- **Detune**: Applies detuning to the stuttered output. Detuning will still be applied to unison shifted audio.
- **Spread Type**: Speed: As Spread Amt is increased, stutters will be grouped increasingly closer together over a stutter burst. Slow: As Spread Amt is increased, stutters will be spaced increasingly farther apart over a stutter burst. Double+Half: As Spread Amt is increased, the probability of Stutter Rate either being halved or doubled is increased. At 100, you will only hear stutter bursts that are randomly half or double speed compared to the Stutter Time setting.
- **Spread Amount**: Increases the audible effect for each setting in the Spread Type parameter.
- **Width**: Increases the stereo image of the stutter bursts. 0 is mono (though the reverb at the end of the signal chain is still stereo).
- **Reverb Mix**: A wet/dry control for the Reverb. Note that reverb is added to the dry signal as well.
- **Decay**: Controls the decay time of the reverb.

#### Performance Parameters

- **Stutter**: Triggers continuous stutter looping that persists until disengaged.
- **Stutter M**: Momentary stutter that is active only while the footswitch is held.
- **Retrigger**: Resets the LFO waveform to its starting position.

---

## Harmonizer

### Crystals

Combines twin reverse pitch shifters, delays, feedback, and reverb to generate cascading pitched delays and granular textures.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch A/B Mix**: Controls the ratio of the level of Pitch A to Pitch B.
- **Pitch Shift A**: Controls the amount of pitch shift for A in cents (1 cent = 1/100th of a semitone).
- **Pitch Shift B**: Controls the amount of pitch shift for B in cents (1 cent = 1/100th of a semitone).
- **Reverse Delay Buffer A**: Controls the length of the reverse time buffer for A. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Reverse Delay Buffer B**: Controls the length of the reverse time buffer for B. With Tempo OFF, delay is displayed in ms. With Tempo ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Reverb Mix Level** `0-100%`: Sets the Wet/dry mix of the reverb level, where 100 is an all wet signal. Note that this mix level is part of the wet signal path, so the global Mix control will still affect the amount of wet signal being heard overall.
- **Reverb Decay Rate**: Selects the Reverb Decay rate.
- **Feedback A**: Controls level of Feedback A.
- **Feedback B**: Controls level of Feedback B.

#### Performance Parameters

- **Flex**: Shifts both voices up one octave.

---

### Diatonic

Pitch shifters track notes and shift by harmonic interval based on Key and Scale. Twin independent pitch changers with delays and feedback.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch A/B Mix**: Controls the ratio of the level of Pitch A to Pitch B. Note: The A/B mix is set before the feedback delays so that feedback can continue on A or B and not be affected by new audio when the Pitch Mix control is turned completely to the opposite channel. This allows you to create a mini 'looper' effect.
- **Pitch Shift A**: Selects the harmonic interval (pitch shift) for Pitch A.
- **Pitch Shift B**: Selects the harmonic interval (pitch shift) for Pitch B.
- **Delay A**: Controls the amount of time delay of the A pitch shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Delay B**: Controls the amount of time delay of the B pitch shifted output. With Tempo OFF, delay is displayed in ms. With Tempo ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Key**: Selects the key.
- **Scale**: Selects the scale. The supported scales are: Major Minor Dorian Phrygian Lydian Mixolydian Locrian Harmonic Minor Melodic Minor Whole Tone Enigmatic Neapolitan Hungarian
- **Feedback A**: Controls level of voice A Feedback. The feedback delay length is the length of either Delay A or Delay B, whichever is longer, to make sure both voices fade out simultaneously.
- **Feedback B**: Controls level of voice B Feedback. The feedback delay length is the length of either Delay A or Delay B, whichever is longer, to make sure both voices fade out simultaneously.
- **Quantization**: Quantizes the notes that are not in the selected key scale to fit within the selected key and scale.

#### Performance Parameters

- **Learn**: Press-and-hold the Learn switch while playing a note and the H90 will set the key to that note.

---

### H910 H949

Emulates legendary Eventide H910 Harmonizer, the world's first real-time pro-audio pitch changer.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch A/B Mix**: Controls the ratio of the level of Pitch A to Pitch B.
- **Pitch Shift Up A**: Controls the amount of pitch shift for voice A expressed as a ratio.
- **Pitch Shift Down B**: Controls the amount of pitch shift for voice B expressed as a ratio.
- **Delay A**: Controls the amount of time delay of the A pitch-shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Delay B**: Controls the amount of time delay of the B pitch-shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Splice Type**: Selects the type of Harmonizer emulated: H910 (just a tiny bit unstable, flickering display, free-running oscillators add randomness), H949-1 (may cause glitches with increasing frequency as pitch ratio deviates from 1:1, more appropriate for smaller pitch ratios), H949-2 (intelligent splicing reduces glitching but adds coloration, suitable for extreme pitch ratios), Modern (takes advantage of powerful DSP to further reduce glitching).
- **Pitch Coarse/Fine Control**: Selects the type of pitch ratio control for Pitch A and Pitch B parameters: Normal allows continuous control as a pitch ratio. Micro allows for fine adjustments around Unison. Chromatic allows you to select intervals equal to the 12 note per octave scale.
- **Pitch A Feedback**: Controls the amount of feedback for Delay A.
- **Pitch B Feedback**: Controls the amount of feedback for Delay B.

#### Performance Parameters

- **Repeat**: Press-and-hold for infinite repeat.

---

### HarModulator

Combines twin chromatic pitch shifters with modulation delivering effects from subtle to extreme.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch A/B Mix**: Controls the ratio of the level of Pitch A to Pitch B.
- **Pitch Shift A** `-3 to +3 octaves`: Selects the pitch shift interval in semitone increments from down three octaves to up three octaves.
- **Pitch Shift B** `-3 to +3 octaves`: Selects the pitch shift interval in semitone increments from down three octaves to up three octaves.
- **Delay A**: Controls the amount of time delay of the A pitch shifted output. With Tempo OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Delay B**: Controls the amount of time delay of the B pitch shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Modulation Depth**: Controls the amount (or depth) of pitch modulation displayed in cents over a four octave range (two octaves down, two octaves up). Fine control for micro-pitch modulation is available and displayed in cents, ranging from -30 to +30 cents. When the modulation is a positive value the two voices will modulate in sync with each other; when the value is negative they will modulate out of sync.
- **Modulation Rate** `0.1-10 Hz`: Controls the modulation rate. Note: If Enveloep is selected as the Mod Shape, then modulation is driven by the amplitude of the audio input and Modulation Rate becomes a Sensitivity control.
- **Modulation Shape**: Selects the modulation shape. Select Envelop and your playing will drive the pitch modulation.
- **Feedback**: Controls the amount of feedback for Delays A and B.

#### Performance Parameters

- **Flex**: Shifts both voices up one octave.

---

### HarPeggiator

Creates dual 16-step arpeggios combining pitch sequencer, rhythm sequencer, and effect sequencer.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Arpeggiator A/B Mix**: Controls the ratio of arpeggiator A to arpeggiator B.
- **Pitch Sequence A**: See description and table above
- **Pitch Sequence B**: See description and table above
- **Rhythm A**: These controls select the rhythm/groove sequence for A/B. The rhythm sequences are a set of 21 selectable presets. The pitch sequences are numbered from 01 to 20, plus and additional random rhythm. Set the control to Off to turn off the rhythm sequence. With the rhythm sequence turned Off, all sixteen steps of the sequence are played at full amplitude.
- **Rhythm B**: See the description for Rhythm A.
- **Dynamics** `-10 to +10`: Sets attack and release time for the dynamics of the Rhythm and Effects. When set to minimum (-10), the audio takes the entire step length to fade in; at mid-range (0), the audio is present for the entire step duration; and at maximum (10), the audio is present for only 1/10th of the step’s duration. Note: This control has no effect when both Rhythm and Effect knobs are set to Off.
- **Step Length**: With Tempo Sync OFF, sets the length of each of the 16 steps in ms. With Tempo Sync ON, sets the length of each step relative to the tap tempo (length of note e.g. whole, quarter, etc.).
- **Effect A**: HarPeggiator lets you apply a sequence of filter, fuzz and/or glitch effects to each note of the 16-step sequence. The effect sequences are a set of 25 selectable presets. The effects are indicated by effect type: Filter 1-5 Fuzz 1-5 Glitch 1-5 All There are five filter effects, five fuzz effects and five glitch effects to choose from. Or, you can select one of four different types of random effect sequences: Random Filters Random Fuzz Random Glitches
- **Effect B**: See the description for Effect A.

#### Performance Parameters

- **Restart**: Restarts the sequence from the beginning.

---

### MicroPitch

Fine-resolution pitch shifter ideal for vocal doubling, tone fattening, and unique delays.

#### Parameters

- **Mix**: Relative level of the wet and dry signals.
- **Pitch Mix**: Controls the ratio of the level of Pitch A to Pitch B.
- **Pitch A** `+0 to +50 cents`: Controls the amount of pitch shift up for voice A, from Unison to +50 cents.
- **Pitch B** `-50 to 0 cents`: Controls the amount of pitch shift down for voice B, from Unison to -50 cents.
- **Delay A**: Controls the amount of time delay of the A pitch-shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Delay B**: Controls the amount of time delay of the B pitch-shifted output. With Tempo Sync OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Modulation Depth** `0-100`: Controls the amount (or depth) of pitch modulation around the current pitch for each voice. A value of 100 represents a bipolar full swing of the modulation from 0 cents to 2x Pitch. Lesser values scale proportionally.
- **Mod Source**: Selects the modulation source. -Env: Increased volume decreases the Pitch modulation. LFO: Pitch modulation is controlled by the LFO rate set by the Mod Rate parameter. +Env: Increased volume increases the Pitch modulation.
- **Mod Rate** `0.1-10 Hz`: Controls the LFO rate when LFO is selected as the Mod Source. 0.1 to 10 Hz
- **Mod Sens**: Controls the sensitivity of the envelope follower when -Env or +Env is selected as the Mod Source.
- **Feedback**: Controls the amount of feedback for Delays A and B.
- **Tone**: Applies filtering to voice A and voice B.

#### Performance Parameters

- **Flex**: Doubles the pitch shift amount of both voices.

---

### Octaver

Synthesizes paired sub-harmonics one and two octaves below with octave fuzz generator and modulated filters.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Sub-Harmonic Mix**: Controls mix of 1st and 2nd sub-harmonics (A and B). Note that Inputs 1 and Inputs 2 are not mixed.
- **Filter Center Frequency A**: Controls the center frequency of the resonant filter for A.
- **Filter Center Frequency B**: Controls the center frequency of the resonant filter for B.
- **Filter Resonance A**: Controls filter resonance for A. Note: After adjusting the filter’s center frequency and resonance, you may want to try modulating the filter.
- **Filter Resonance B**: Controls filter resonance for B.
- **Envelope Filter Shift**: Octaver allows your playing to vary the center frequency of the filters. This control adjusts the degree to which the input signal’s envelop shifts the filter’s center frequency.
- **Envelope Sensitivity**: Controls the sensitivity of the frequency sweeps to the input signal level.
- **Distortion**: Controls the amount of distortion (fuzz).
- **Octave-Fuzz Mix**: Controls the mix of octaves and fuzz.

---

### PitchFlex

Designed for live use with expression pedal or footswitch, set pitch shift at each end of pedal travel.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch Mix**: Controls the ratio of the level of Pitch A to Pitch B.
- **Manual Shift**: Sweeps the pitch from the ‘heel’ to ‘toe’ value. Map an expression pedal to this parameter and adjust it to perform the sweep.
- **Heel A**: Sets pitch shift of the voice in the heel position. When ‘OFF’ is selected, the voice is muted at the heel position and the pitch is set to unison.
- **Heel B**: Sets pitch shift of the voice in the heel position. When ‘OFF’ is selected, the voice is muted at the heel position and the pitch is set to unison.
- **Toe A**: Sets pitch shift of the voice in the toe position. When ‘OFF’ is selected, the A pitch shifter is disabled at the toe position and toe is treated as unison.
- **Toe B**: Sets pitch shift of the voice in the toe position. When ‘OFF’ is selected, the A pitch shifter is disabled at the toe position and toe is treated as unison.
- **Heel-to-toe glissando**: This parameter is for use when using the Flex performance parameter, or an Auxiliary Switch to control the pitch change effect for voices A and B. Sets the time to move from ‘heel’ to ‘toe’. With Tempo Sync ON the maximum is ½ note.
- **Toe-to-heel glissando**: Same as above, but set the time to move from ‘toe’ to ‘heel’.
- **Glissando Shape**: Controls the ‘shape’ that the pitch modulation follows when using the Flex Switch. If set to Negative values, the pitch goes slowly towards ‘toe’ and quickly transitions to ‘heel’, Positive is the other way around, and 0 means the pitch shifts up and down linearly.
- **Low Pass Filter**: A low pass filter to ‘darken’ the effect.

#### Performance Parameters

- **Flex**: Sweep the pitch shift from ‘toe’ to ‘heel’ position.

---

### PolyFlex

Fully polyphonic version of PitchFlex allowing chord bending, dive bombs, and pedal-steel tones.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Detune** `-50 to +50 cents`: A detune amount applied to both the base shift amount and the Flex amount, from -50 cents to 50 cents.
- **Flex Time** `0-2s`: How long it takes to get from the Shift interval to the Flex interval from 0 to 2 seconds.
- **Return Time** `0-2s`: How long it takes to return to the Shift interval from the Flex interval from 0 to 2 seconds.
- **Auto Engage**: When on, the algorithm is bypassed until the Flex is engaged, or Manual Flex is above 0. This will be triggered by any of the available ways to Flex.
- **Auto Engage Hold Time** `0-1s`: If Auto Engage is on, this parameter allows the pitch shifted effect to remain on for a period of time from 0 to 1 second. This can help the auto engage parameter from disengaging abruptly. The following parameters are available for both pitch A and B:
- **Level A**: Adjusts the level of the pitch shifted voice.
- **Level B**: Adjusts the level of the pitch shifted voice.
- **Shift A**: The base pitch shift amount specified in musical intervals for each voice of shifting. -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Shift B**: The base pitch shift amount specified in musical intervals for each voice of shifting. -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Flex A**: The pitch shift amount to dive/bend to. -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Flex B**: The pitch shift amount to dive/bend to. -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Pan A**: Moves the pitch shifted voice left or right in the stereo field.
- **Pan B**: Moves the pitch shifted voice left or right in the stereo field.

#### Performance Parameters

- **Flex A**: Activates pitch bend for voice A, gliding from Shift A to Flex A interval.
- **Flex B**: Activates pitch bend for voice B, gliding from Shift B to Flex B interval.
- **Flex Dual**: Bends both voices simultaneously.
- **Freeze**: Freezes the pitch-shifiting sound for pad like textures. The dry signal is still passed through. Note that if Auto Engage is On, you won’t hear the frozen signal when you are not flexing.

---

### Polyphony

Low-latency, high quality polyphonic pitch shifter leveraging SIFT technology with zero tracking errors.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Inst Type**: Tunes the underlying pitch shifting Algorithm for either pitched or percussive instruments. Tip The Percussive instrument mode is designed to prioritize preserving the transients and tone of the original signal while also having less latency. For applications where you would like to re-tune a guitar or bass (Mix is 100% wet) Percussive mode may work better for small shift intervals. For larger intervals the quality of the shifted sound will be be better in the Pitched mode.
- **Feedback Sw**: Places the pitch shifter inside or outside of the feedback path. Because the pitch shifting is a mono in, multi out effect, the feedback paths of the shifted voices are summed together first before being fed back to the pitch shifter. This causes the feedback to slowly fade towards the center even if the voices are panned hard left/right when the pitch shifter is inside the feedback path. There is also a gentle lowpass filter in this mode to help remove some of the very very high annoying stuff that can happen when shifting up over and over again. Note: Feedback amounts may have different effects in one mode vs the other.
- **Auto EQ** `0-10+`: Determines the amount of automatic EQ that is applied to the shifted voices to help them sound more natural. When shifting down the auto eq brightens things up to try and preserve the transients of the original signal. When shifting up, the auto eq smooths out harsh squeaky sounds. The EQ is automatically adjusted based on the amount of shift applied in either direction. A default setting of 10 is recommended. The following parameters are available for both pitch A and B:
- **Level A**: Adjusts the volume of the pitch.
- **Level B**: Adjusts the volume of the pitch.
- **Shift A**: -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Shift B**: -2 Oct, -P12, -P11, -Oct, -M7, -m7, -M6, -m6, -P5, -Tri, -P4, -M3, -m3, -M2, -m2, Uni, m2, M2, m3, M3, P4, Tri, P5, m6, M6, m7, M7, Oct, P11, P12, 2 Oct
- **Detune A** `-50 to +50 cents`: The amount of detuning, from -50 cents to 50 cents.
- **Detune B** `-50 to +50 cents`: The amount of detuning, from -50 cents to 50 cents.
- **Delay A** `0-2s`: The amount of delay, from 0 ms to 2 s.
- **Delay B** `0-2s`: The amount of delay, from 0 ms to 2 s.
- **Feedback A**: The amount of feedback for each voice. Behaves differently depending on how Feedback Sw is set.
- **Feedback B**: The amount of feedback for each voice. Behaves differently depending on how Feedback Sw is set.
- **Pan A**: Moves the pitch left or right in the stereo field.
- **Pan B**: Moves the pitch left or right in the stereo field.

#### Performance Parameters

- **Freeze**: Freezes the pitch-shifiting sound for pad like textures. The dry signal is still passed through.

---

### Prism Shift

Polyphonic effects generating 3 arpeggiated voices from a single chord with sophisticated tracking.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Arp Type**: Sets which type of Arpeggio to use. The choices are: Rising Falling Falling/Rising Rising/Falling
- **Step Length**: Time between successive notes in the arpeggio
- **Shift**: Shift ratio for the low/high voices. E.g., if -1oct +1oct is used the high voice will be shifted up and octave and the low voice will be shifted down an octave. The choices are: -1oct +1oct -P4 +P5 -P5 +P4 +1oct +2oct +P5 +P12 +P4 +P11
- **Arp Order**: Order of the voices in the arpeggio. E.g., if the Arp Type is rising and the Arp Order is L-M-H, then the arpeggio will rise from low-to-high frequencies. However, if the Arp Order is H-M-L, then the high voice will rise, following by a rising mid voice, and then a rising low voice. This creates a simultaneous ascending while descending sort of effect. The choices are: L-M-H L-H-M M-L-H M-H-L H-L-M H-M-L
- **Auto EQ** `0-10+`: An Eq for the pitch shifted voices. A default setting of 10 is recommended. The following controls are available for all three voices:
- **Gain Low**: A gain control for the specific voice.
- **Gain Mid**: A gain control for the specific voice.
- **Gain High**: A gain control for the specific voice.
- **Feedback**: A feedback control for the specific voice.
- **Spread**: Controls the stereo spread of the voices. When set to -1 the Low voice is panned hard left, the mid voice is panned center, and the high voice is panned hard right. When set to +1 this is reversed. Intermediate values morph between these two extremes.
- **Slew Time**: A slew on the Shift control. A large value will cause changes to the Shift parameter to glissando.

#### Performance Parameters

- **Freeze**: Freezes the “High” and “Low” pitch shifted voices, the “Mid” voice (which is not pitch shifted) is not frozen.
- **Shift M**: Moves the current value of the shift knob 1 position clockwise, wrapping if necessary.

---

### Quadravox

Up to four pitch shifted voices with independent interval selection based on key and scale.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Pitch A+C/B+D Mix**: Controls the ratio of level Pitch A+C to Pitch B+D. With the knob set full counter-clockwise, PitchA + PitchC are set to equal level. Full clock-wise, sets Pitch B + Pitch D to equal levels. The ratio of level of Pitch A to Pitch C and of Pitch B to Pitch D are fixed at equal levels and cannot be changed.
- **Pitch Shift A**: Selects the harmonic interval (pitch shift) for Pitch A. Set to minimum to turn OFF voice A.
- **Pitch Shift B**: Selects the harmonic interval (pitch shift) for Pitch B. Set to minimum to turn OFF voice B.
- **Pitch Shift C**: Selects the harmonic interval (pitch shift) for Pitch C. Set to minimum to turn OFF voice C.
- **Pitch Shift D**: Selects the harmonic interval (pitch shift) for Pitch D. Set to minimum to turn OFF voice D.
- **Delay D**: Quadravox’s delay controls work differently from those in the other effects. Quadravox’s four delays are not independently variable. Instead, they are staggered with A having the shortest delay, B longer than A, C longer than B and D the longest. The Delay D control is used to set the last delay. With Tempo OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Delay Grouping**: Select the grouping of the four delays (A, B, C, D). The delays can be evenly spaced or spread out.
- **Key**: Selects the key.
- **Scale**: Selects the scale. The supported scales are: Major Minor Dorian Phrygian Lydian Mixolydian Locrian Harmonic Minor Melodic Minor Whole Tone Enigmatic Neapolitan Hungarian
- **Quantization**: Quantizes the notes that are not in the selected key scale to fit within the selected key and scale.

#### Performance Parameters

- **Learn Mode**: Press and hold the Learn switch while playing a note and the H90 will set the key to that note.

---

### Resonator

Staggers 4 resonant comb filters for ambient, arpeggiated, or reverberant sounds.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Length**: Total length of the delay line. This length is split into 8 subdivisions on which the comb filters can be staggered.
- **Rhythm**: Represents the rhythm pattern of the comb filters. Each digit indicates the subdivision on which a comb filter is positioned. “1.3.5.7” will sound like even quarter notes since the four comb filters are evenly spaced on the 1st, 3rd, 5th, and 7th subdivisions.
- **Feedback**: The feedback level of each of the comb filters. Feedback type 1 [FB1] maintains the pattern set by the rhythm knob, whereas feedback type 2 [FB2] degrades the pattern as it repeats.
- **Resonance**: Affects how intensely the comb filters resonate. The comb filters will ring out more intensely as the resonance increases in either the positive or negative direction. Resonance set to 0 will acts as multi-tap delay without any additional resonant tones.
- **Reverb**: Controls the amount of reverb in the comb filter path.
- **Note 1**: Tunes the note values that trigger each respective comb filter. When resonance is positive, all integer multiples of this frequency will resonate. When the resonance is negative, only odd multiples of this frequency will resonate. These note values also affect the high and low pass filters surrounding each comb filter. When resonance is set to 0, these knobs can still be used to filter the delays.
- **Note 2**: Same as Note 1.
- **Note 3**: Same as Note 1.
- **Note 4**: Same as Note 1.

---

## Harmonizer+

### Quadravox+

4-voice vocal harmonizer with creative delay and arpeggio effects, unison voice replacing dry signal for quantization and formant manipulation.

#### Parameters

- **Unison Mix** `0-100%`: Mixes in the a unison copy of the dry signal, 100% is entirely the unison signal. Note that there is no true dry signal, but your unison voice will sound more natural with quantization off and higher tuning speeds.
- **Unison Formant** `-600 to +600 cents`: Shift the formants of the unison voice from -600 to 600 c without adjusting the pitch.
- **Key**: Selects the key.
- **Scale**: Selects the scale.
- **Quantization**: Quantizes the notes that are not in the selected key scale to fit within the selected key and scale.
- **Formant Link**: Automatically stretches or compresses the vocal formants in proportion to the pitch shift interval. Positive values will make the voice sound more throaty when pitching down and more chipmunky when shifting up. Negative values invert this relationship. Larger positive or negative values produce a more pronounced effect. A value of 0 preserves the natural formants of the voice (they are unaltered)
- **Pitch Mix**: Controls the ratio of level Pitch A+C to Pitch B+D. With the knob set full counter-clockwise, PitchA + PitchC are set to equal level. Full clock-wise, sets Pitch B + Pitch D to equal levels. The ratio of level of Pitch A to Pitch C and of Pitch B to Pitch D are fixed at equal levels and cannot be changed.
- **Shift A**: Selects the harmonic interval (pitch shift) for the Pitch. Set to minimum to turn any voice OFF.
- **Shift B**: Selects the harmonic interval (pitch shift) for the Pitch. Set to minimum to turn any voice OFF.
- **Shift C**: Selects the harmonic interval (pitch shift) for the Pitch. Set to minimum to turn any voice OFF.
- **Shift D**: Selects the harmonic interval (pitch shift) for the Pitch. Set to minimum to turn any voice OFF.
- **Delay**: The four delays are not independently variable. Instead, they are staggered with A having the shortest delay, B longer than A, C longer than B and D the longest. The Delay control is used to set the last delay. With Tempo OFF, delay is displayed in ms. With Tempo Sync ON, delay can be sync’d to the tempo and is displayed as a rhythmic sub-division of the tempo beat value.
- **Division**: Adjusts how the Delay parameter is divided between the four delays (A, B, C, D). The delays can be evenly spaced or spread out.
- **Feedback**: Amount of Feedback for the delay line.
- **Spread**: Pans the voices left/right.
- **Tuning Speed** `0-200ms`: Adjust the speed of pitch shifting from snappy, hard tuned quantization to more subtle pitch correction. 0 to 200ms
- **Detune** `±50 cents`: Equally detunes all voices +/- 50 c.
- **Auto EQ** `On/Off`: Boosts both low and high frequencies which often sound quieter after pitch shifting. This can help the pitch shifted voices sit better in the mix.

#### Performance Parameters

- **Root Learn**: Analyzes the current vocal pitch via footswitch and automatically updates the Root/Key parameter.
- **Glide**: Shifts pitch to the designated glide interval, smoothly transitioning from current to target pitch.
- **Glide Mom**: Momentary pitch shift to glide interval; returns when released.

---

### VocalShift

High quality vocal harmonizer with 3 voices, independent pitch and formant shifting, key/scale quantization.

#### Parameters

- **Mix**: Wet/Dry mixer.
- **Root**: Sets the root for the Scale parameter.
- **Scale**: Set the Scale that determines the pitch shifted intervals.
- **Shift A**: Pitch shift interval.
- **Shift B**: Pitch shift interval.
- **Shift C**: Pitch shift interval.
- **Formant A**: Formant shift amount. Positive values will make the voice sound more chipmunky, negative values will make the voice sound more throaty. Leaving this control at 0 will preserve the formants and give a more natural sound when changing the Shift parameter.
- **Formant B**: Formant shift amount. Positive values will make the voice sound more chipmunky, negative values will make the voice sound more throaty. Leaving this control at 0 will preserve the formants and give a more natural sound when changing the Shift parameter.
- **Formant C**: Formant shift amount. Positive values will make the voice sound more chipmunky, negative values will make the voice sound more throaty. Leaving this control at 0 will preserve the formants and give a more natural sound when changing the Shift parameter.
- **Formant Link**: Automatically stretches or compresses the vocal formants in proportion to the pitch shift interval. Positive values will make the voice sound more throaty when pitching down and more chipmunky when shifting up. Negative values invert this relationship. Larger positive or negative values produce a more pronounced effect. A value of 0 preserves the natural formants of the voice (they are unaltered).
- **Gain A**: Voice level.
- **Gain B**: Voice level.
- **Gain C**: Voice level.
- **Delay A**: Delay time in ms or Tempo Synced.
- **Delay B**: Delay time in ms or Tempo Synced.
- **Delay C**: Delay time in ms or Tempo Synced.
- **Feedback A**: Feedback amount.
- **Pan A** `-50 to +50`: Stereo position (-50: left, 0: center, 50: right).
- **Pan B** `-50 to +50`: Stereo position (-50: left, 0: center, 50: right).
- **Pan C** `-50 to +50`: Stereo position (-50: left, 0: center, 50: right).
- **Detune** `0-50 cents`: Applies equal detuning up and down to Voice B & C from 0 to 50c. 0 to -50c applies opposite detuning.
- **Tuning Speed** `0-500ms`: Adjust the speed of pitch shifting from snappy, hard tuned quantization to more subtle pitch correction. Note that tuning speed is applied whether quantization is on/off, and is an important parameter to tuning how the algorithms processed the vocal signal. 0 to 500ms.

#### Performance Parameters

- **Root Learn**: Analyzes the currently sung note via footswitch and updates the Root parameter automatically.
- **Glide**: Shifts pitch to the designated glide interval.
- **Glide M**: Momentary pitch shift to glide interval; returns when released.
- **Hold M**: Momentarily maintains the current voice pitches while preserving articulation nuances of the dry signal.
- **Hold**: Latching version of Hold M; sustains voice pitches until disengaged.

---

### VocalShiftMIDI

Four voice version of VocalShift with MIDI control of pitch shift values for harmonies, chord stacks, and pitch correction.

#### Parameters

- **Unison Mix** `0-100%`: Mixes in the a unison copy of the dry signal, 100% is entirely the unison signal. Note that there is no true dry signal, but your unison voice will sound more natural with quantization off and higher tuning speeds.
- **Unison Formant** `-600 to +600 cents`: Shift the formants of the unison voice from -600 to 600 c without adjusting the pitch.
- **Tuning Speed** `0-500ms`: Adjust the speed of pitch shifting from snappy, hard tuned quantization to more subtle pitch correction. 0 to 500ms.
- **Gate**: Controls the threshold of the noise gate.
- **Gate Attack**: Sets the attack time for the noise gate.
- **Gate Release**: Sets the release time for the noise gate.
- **Vibe Rate** `0-8 Hz`: The rate of the vibrato applied to the MIDI pitch shifted voices. 0 to 8 Hz.
- **Vibe Depth** `0-50 cents`: The depth of the vibrato applied to the MIDI pitch shifted voices. 0 to 50 c.
- **Vibe Slew** `0-2000ms`: The time it takes before vibrato is applied. 0 to 2000 ms.
- **Glide** `0-5000 oct/ms`: Sets the slew time between note changes for each voice. 0 to 5000 octaves per millisecond.
- **Delay**: Global Delay time for all voices in ms or Tempo Synced.
- **Feedback**: Feedback amount for the delay line.
- **Formant Link**: Automatically stretches or compresses the vocal formants in proportion to the pitch shift interval. Positive values will make the voice sound more throaty when pitching down and more chipmunky when shifting up. Negative values invert this relationship. Larger positive or negative values produce a more pronounced effect. A value of 0 preserves the natural formants of the voice (they are unaltered).
- **Spread**: Narrow / Medium / Wide. Pans every other voice left or right.
- **Attack** `0-3000ms`: Envelope attack time of the pitch shifted voice. 0 to 3000 ms.
- **Release** `0-3000ms`: Envelope release time of the pitch shifted voice. 0 to 3000 ms.
- **Hold** `On/Off`: Off will only output pitch shifted audio while an incoming MIDI note is ON. On will ignore MIDI note OFF and hold the value of the incoming MIDI note until it receives another MIDI note. Attack/Release times do not apply when Sustain is latching.
- **Velocity Sens** `0-100`: Adjusts the sensitivity of incoming MIDI velocity data. At 100, MIDI velocity messages are passed thru unchanged. At 0, MIDI velocity will be ignored and the pitch shifted voices will always play at full volume. At 50, the minimum velocity value would be 64. Use this control if you are unable to adjust the velocity curve on your MIDI controller.
- **Auto EQ** `On/Off`: Boosts both low and high frequencies which often sound quieter after pitch shifting. This can help the pitch shifted voices sit better in the mix.
- **Latency Mode**: Low/High - Higher latency may result in improved performance with a tradeoff of more noticeable latency. The high latency setting is recommended when using extreme formant settings. Low introduces ~25 ms of latency, while High introduces ~50 ms of latency.

#### Performance Parameters

- **Root Learn**: Analyzes the currently sung note and updates the Root parameter automatically.
- **Freeze**: Preserves the input signal for pad creation and MIDI-controlled pitch shifting over the frozen audio.
- **Freeze M**: Momentary freeze of input signal; releases when footswitch is released.

---

### VocalTune

Stripped down version of VocalShift for vocal correction and hard tune effects with integrated EQ and compressor.

#### Parameters

- **Root**: Sets the root for the Scale parameter.
- **Scale**: Set the Scale that determines the intervals that the vocals will be quantized to.
- **Tuning Reference**: Set the reference point for the key/scale quantization.
- **Quant Error** `0-50 cents`: Allows small pitch variations to not be quantized. Useful for vocals with vibrato when quantization is on. 0 to 50 c.
- **Formant** `-600 to +600 cents`: Shift the formants from -600 to 600 c without adjusting the pitch.
- **Tuning Speed** `0-500ms`: Adjust the speed of quantization from snappy, robotic sounding quantization to more subtle pitch correction. 0 to 500 ms.
- **Bass** `-18 to +12 dB`: Boost/Cut the bass frequencies from -18 to +12 dB.
- **Treble** `-18 to +12 dB`: Boost/Cute the treble frequencies -18 to +12 dB.
- **Threshold**: Set the threshold of the compressor.
- **Ratio** `1:1 to 20:1`: Ratio of the compressor, ranging from 1:1 to 20:1.
- **Attack** `0.1-100ms`: Compressor attack time, 0.1 to 100 ms.
- **Release** `1-1000ms`: Compressor release time, 1-1000 ms.
- **Gain** `-16 to +12 dB`: Compressor makeup gain, -16 to +12 dB.
- **Gate**: Threshold of noise gate.

---

## Looper

### Looper

60 seconds of stereo recording at full quality and up to 480 seconds at reduced quality with variable-speed playback, overdubbing, and MIDI sync.

#### Parameters

- **Mix**: Mix control between the Dry audio input and Looper playback.
- **Loop Max-Length** `60s/120s/240s/480s`: When the Loop is Empty, sets the Maximum allowed Loop Length. Note that audio recording quality is degraded at slower recording speeds (1/2x and 1/4x). The maximum loop length is determined by the setting of the Rec Speed parameter as follows: 60 sec at 2x 120 sec at 1x 240 sec at 1/2x 480 sec at 1/4x When the Loop contains audio, the Max-Length parameter cannot be adjusted. Note With Tempo Mode On, the range of the Max-Length parameter depends on the H90’s Tempo BPM value. Lower BPM values will not fill up the entire parameter range.
- **Loop Play-Start Point**: When using Tempo Sync, the minimum length of audio that can be played out is 1 beat so, the Play-Start Point will display in beats allowing you start playback from 0 beats up to Loop Length minus 1 beat. For example, if you recorded an 8 beat loop, this will range from 0 to 7 beats. Changing the Play-Start Point during Playback will apply the next time the Loop comes around and will maintain perfect beat sync with the Tempo Source.
- **Loop Play-Length**: When using Tempo Sync, the minimum length of audio that can be played out is 1 beat so, the Play-Length will display in beats allowing playback lengths of 1 beat up to the Loop Length. For example, if you recorded an 8 beat loop, the Play-Length will range from 1 to 8 beats. Changing the Play-Length during Playback will apply the next time the Loop comes around and will maintain perfect beat sync with your Tempo Source. Of course, new Play-Lengths that don’t evenly divide the total Loop Length will cause the loop to “walk” the downbeat, thus creating interesting poly-rhythms against an existing pattern.
- **Loop Decay Rate** `0-100%`: When dubbing you may want the original saved audio to persist as you add new sounds. Of course, indefinitely adding new signals will eventually result in ‘mud’ (the “Crayola” effect). The Decay Rate control allows the saved audio to fade as you dub new material. The Decay Rate is adjustable from 0% [DCY: 0] to 100% [DCY:100]. When set to 0%, the loop never decays. When set to 100% the previously saved audio decays completely each time through the loop when dubbing. In other words, the looped audio is only played once. The Loop Decay Rate control has no effect on normal Playback, only dubbing.
- **Dubbing Mode**: The Dubbing Mode choices are: Latch - Press the footswitch once to start dubbing and again to stop. Punch - Dub only while the footswitch is held down. Repl-Latch - Press the footswitch once to start replacing the loop audio and again to stop. Repl-Punch - Replace the loop audio only while the footswitch is held down.
- **Playmode**: Playmode affects three actions of the Looper: the action when Recording reaches Max-Length, the action when Playing reaches the Play-Length, and the action of the PLAY switch.
- **Resolution**: When set to Smooth, resolution is 1%. The other Depth control settings allow you to select the Play Speed in musical intervals as follows (a negative value corresponds to Reverse Play, and all resolutions have 0% in the middle for a full Pause):
- **Record Speed** `2x/1x/1/2x/1/4x`: Determines the speed at which the initial loop is recorded. Slower speeds allow for longer loop lengths but at a lower fidelity. 2x – Double 1x – Normal 1/2x – Half 1/4x – Quarter
- **Play Speed** `-200% to +200%`: Determines the playback speed of the loop. Play Speed resolution is dependent on the setting of the Resolution control. A negative speed with Empty causes playback to automatically start in the Reverse direction after the loop is closed, either through a PLAY button press or the Loop and Autoplay settings on the Playmode knob. After a loop is recorded, Play Speed controls the speed of Loop playback AND dubbing over the full range of speeds allowing for continuous real-time scrubbing from one octave up in Reverse Play (-200%), to one octave up in Forward Play (200%), with a pause (0%) directly in the middle (knob set to 12 o’clock).
- **Filter**: Controls the tone of the looped audio. Tone control filters are placed at both the input and output of the Looper. This allows you to control the tone of the audio that you’re recording and then independently control the tone on playback. Turn to the left to cut low frequencies and to the right to cut high frequencies. For flat response, set the knob to 12 o’clock.

#### Performance Parameters

- **Record**: Press the Footswitch to start recording a loop.
- **Play**: Press the Footswitch to play a loop that has been recorded. The Playmode parameter will determine how this works.
- **Stop**: Press the Footswitch to stop playback of the loop.
- **Empty**: Press the Footswitch to empty the loop.
- **Undo/Redo**: Press the Footswitch to undo the last overdub. Press it again to redo.
- **Direction**: Toggles the direction of the loop playback between forwards/backwards.
- **Speed**: Toggles the speed of the loop between full speed and half speed. At half speed the range of the Play Speed parameter will be limited to +/- 100.

---

## Modulation

### Chorus

Creates the sound of multiple instruments by randomly modulating delay lines and panning voices in stereo.

#### Parameters

- **Intensity**: Dry / wet mix.
- **Type**: Selects the chorus type. The choices are: Liquid, Organic, Shimmer, Classic. Each type has a different chorus character and affects how the Feedback parameter behaves.
- **Depth**: Sets the modulation sweep range from narrow to wide.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Feedback**: Controls feedback for Liquid and Shimmer. For Organic, used to scale a manual delay offset. For Classic, used to control a filter.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Even-Vibe

Stereo emulation of the classic Shin-ei Uni-Vibe with independent LFO control and envelope follower.

#### Parameters

- **Mix** `0-100%`: Controls the mix between the unprocessed input and the modulated output. Set to 50% for a Uni-Vibe in chorus mode. Set to 100% for Uni-Vibe in vibrato mode.
- **Speed** `0.1-20 Hz`: Determines the rate of the modulation. Tempo Sync off, Hertz. On, subdivisions. Like a classic Uni-Vibe, Speed will also subtly effect the intensity of the modulation. Don’t overthink it.
- **Intensity**: Adjusts the depth of the modulation.
- **Width**: Adjusts the stereo width of the output.
- **Env Speed**: Adjusts how much the envelope controls the rate of the modulation. Negative values will result in slower modulation while the envelope is open, positive values will result in faster modulation.
- **Env Inten**: Adjusts how much the envelope controls the depth of the modulation. Negative values will result in less intensity of the modulation while the envelope is open, positive values will result in more intensity.
- **Softclip**: Adjusts the amount of gentle transistor soft clipping.

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Flanger

Creates deeper, more numerous frequency notches than phasing through modulated delay line mixing.

#### Parameters

- **Intensity**: Effect level.
- **Type**: Selects flanger topology: Positive (non-inverted), Negative (inverted for deeper nulls), Jet (extreme metallic effect), Thru-0 (dual delay lines flanging through zero for dramatic sweeps).
- **Depth**: Sets the modulation sweep range from narrow to wide.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Delay Offset**: Set Delay offset.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Harmadillo

Flexible harmonic tremolo splitting signals into low/high frequency bands with inverted LFO and envelope control.

#### Parameters

- **Depth** `0-100`: This is the depth of the low and high bands of the tremolo. At 0, the tremolo will have no effect on the volume of the bands. At 100, the bands will be completely faded in and out.
- **Rate**: This is the base rate of the tremolo. When Tempo Sync is ON, this becomes a multiplier on the tapped BPM value. The Env Rate control can change the apparent rate, so if the rate that you are hearing is different from the value of the Rate control, try setting the value of Env Rate to 0.
- **Shape**: The shape of the tremolo waveform. The same shape is used for both high and low bands. The shapes describe what happens to the low band, since it’s usually the main part of your sound; the high band will change in the opposite direction. Options are: Sine, Fat Sine, Phat Sine, Triangle, Ramp Dn, Ramp Up, Pulse 25, Pulse 50, Pulse 75, Lump, Rump, Slope.
- **X-Over**: This control determines where in the frequency spectrum the low band ends and the high frequency band begins. In practice, each band rolls off around the crossover frequency, so they overlap a bit. The X-Over control allows you to adjust the amount of overlap; see below. To mimic an ordinary tremolo, set X-Over to its maximum value of 12,000 Hz. Most of an electric guitar’s sound spectrum is below 6,000 Hz. Any audio above 12,000 Hz (i.e., hardly any sound) will be heard in the high band, and everything else will be heard in the “low” band. Change X-Over gradually to morph into and out of an ordinary tremolo sound. X-Over is especially interesting when Shape is set to an asymmetric shape such as Ramp Up. This means that for each cycle of the tremolo the portion of the signal below the X-Over value will be faded in and the portion of the signal above the X-Over value will be faded out. If you start playing a scale below the X-Over frequency and continue playing above it, the shape of the tremolo will appear to change as you cross over the X-Over frequency!
- **X-Overlap**: This control adjusts the amount of overlap between the high and low bands. Negative values will produce a cut at the crossover frequency, and positive values will produce a boost at the crossover frequency. To explore the effect of this control set: X-Over to 100 Depth to 0 Env Depth to 0 Drive to 0 Env X-Over to 0 This removes the tremolo effect so you can hear the filtering. Slowly sweep the X-Over value from 100 Hz to 3,000 Hz as you play a repeated note, and listen for a boost at the crossover frequency. Harmonic tremolo effects often have a scoop in the midrange near their crossover. You can emulate this by using negative values for X-Over. To dial in classic sounds, set Env X-Over to 0, set the X-Over frequency between 400 Hz and 900 Hz, and adjust X-Over as needed.
- **Drive**: This control adds warmth to the signal by mimicking the behavior of a tube amplifier’s harmonic tremolo.
- **Env Depth** `-100 to +100`: This control uses the amplitude envelope of the input to increase or decrease the tremolo’s depth. Positive values increase the depth of the tremolo when you attack a note. The depth will return to the level set by the Depth control as the note decays. Additionally, louder notes will have greater depth than softer notes. Negative values reduce the tremolo when you attack a note, increasing the clarity of your attacks and making sustained notes more expressive over time. Playing louder will reduce the depth of the tremolo, and you can use large negative values to create tremolos that only appear when the input is soft. The Env Depth control covers a large range, so we recommend starting with values closer to 0, and then adjusting the control as needed.
- **Env Rate** `-100 to +100`: This control uses the amplitude envelope of the input signal to affect the rate of the tremolo. With positive values, the tremolo jumps up in frequency when you attack a note and gradually returns to the original rate set by the Rate or Tap Tempo controls. The harder you play, the longer it will take to return. Negative values will temporarily reduce the rate of the tremolo when you attack a note, and the rate will return to the value set by the RATE knob or Tap Tempo as the note decays. With larger negative values and high Rate values, you can use this control to create bouncing-ball tremolo type effects. This is especially effective with the Shape control set to Pulse, Ramp Dn, Ramp Up, or Slope 0. The Env Rate control covers a large range. At 100%, it can push the internal LFO rate up to 80 Hz, so we recommend starting with values closer to 0, and then adjusting the control as needed.
- **Env X-Over**: This control uses the amplitude envelope to affect the crossover frequency. To create a swept filter effect similar to an autowah, set X-Overlap to 100, set the X-Over frequency to 200 Hz, and then increase the amount of the Env X-Over control as necessary. The frequency of the crossover filter will now track the loudness of the input signal. You can create a single-notch phaser by turning Depth to 0, X-Overlap to -100, X-Over to 3500, and then set Env X-Over to a medium negative value, adjusting to taste. Once you have a sound you like, try slowly turning up the Depth control. Try playing long chords with these settings. In addition to the phasing effect, you will now notice that the tremolo also seems to change as a chord dies out. This is because the crossover frequency returns to the high X-Over value (3500 Hz) as the chord decays. Try setting Shape to an asymmetric waveform (e.g., Ramp Dn) to produce waveform morphing effects as the crossover frequency changes.
- **Tone**: A tone control for shaping the high or low end of the output signal. Negative values roll off high frequencies (High Cut), and positive values roll off low frequencies (Low Cut).

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Instant Flanger

Authentic emulation of the original 1975 studio rackmount with vintage tape flanging character.

#### Parameters

- **Depth** `-100 to +100`: Controls the mix of wet and dry signals. At 0% the output is solely the wet signal. At 100% the output is the sum of the wet and dry signals. At −100% the output is the sum of the wet signal and the inverted dry signal. Note Many modulation-type effects provide mix controls. The Instant Flanger has a mix knob too, but rather than being labeled Mix, it is called Depth. Why is it called Depth, you ask? As you add more of the dry signal to the wet signal, nulls appear in the output spectrum. These nulls get deeper as the two signals approach equal amplitude. Hence you are controlling the depth of the nulls!
- **Source**: Sets the source of the modulation. This can be any combination of the following: Oscillator, Manual, Envelope.
- **Mode**: Adjusts the stereo width of the flanging: Shallow, Deep, and Wide. Note The original Instant Flanger had two unique outputs called Main and Aux. The Main output used two bucket brigade devices in series, while the Aux output only used a single Bucket Brigade. This means the delay times of the Main output are roughly double that of the Aux output. The Mode control gives you access to which of these outputs is used by the Algorithm, and it can drastically change the sound. In Shallow mode, all outputs will correspond to the Aux output of the hardware unit. In Deep mode, all outputs will correspond to the Main output of the hardware unit. In Wide mode, the Main output is routed to the left channel and the Aux output is routed to the right channel. Because of the different delay lengths and the fact that Main and Aux are out of phase with each other, Wide mode will sound like it is panning the signal to the left or right, depending on how the Depth knob is set. Note that if you are using a mono output, Wide mode will be the same as Deep mode.
- **Rate** `0.01-20 Hz`: Controls the rate of the LFO between 0.01 Hz and 20 Hz.
- **LFO Width** `0-100`: Adjusts the range of the sweep of the Flanger’s LFO. 100 is the widest possible sweep and equivalent to the range of the original hardware.
- **Env Thresh** `-60 to 0 dB`: Controls the threshold of the envelope follower, between −60 dB and 0 dB. An input signal will cause the biggest phase shift when it reaches the threshold level.
- **Env Release** `10ms-10s`: Sets the release time of the envelope follower. Release times can vary from 10 milliseconds to 10 seconds.
- **Feedback** `0-100%`: Controls the feedback of the flanger output. 0% sends none of the output back to the input to the bucket brigades, and 100% sends the maximum amount of output back to the input of the bucket brigades.
- **Low Cut**: Applies a high-pass filter to the input signal before it is delayed. The original signal is still mixed with the output of the delays, but the flanging effect only acts on high frequencies.
- **Manual** `0-100%`: Provides manual control of the flanging. 0% corresponds to setting the bucket brigades to their longest delay times, while 100% sets them to their shortest.

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Instant Phaser

Modeled on the original 1972 hardware unit with Age knob for tonal character ranging from factory-fresh to aged.

#### Parameters

- **Depth** `0-100%`: Controls the mix of wet and dry signals. At 0% the output is solely the phase shifted signal. At 100% the output is the addition of the phase shifted signal and the input. This will cause a gain of 6dB at certain frequencies depending on the phase shift.
- **Feedback** `0-100%`: Controls the feedback of the phase shift sections. 0% sends none of the output back to the input to the phase shift sections and 100% sends the maximum amount of output back to the input of the phase shift sections.
- **Mode**: Adjusts the stereo width of the phasing: Shallow, Deep, and Wide Note The original Instant Phaser had two unique outputs called Main and Aux. The main output had two extra stages of phase shifting compared to the aux out, which means the two outputs are 180 degrees out of phase with each other. The Mode control gives you access to which of these outputs is used by the Algorithm, and it can drastically change the sound. In Shallow mode, all outputs will correspond to the Aux output of the hardware unit. In Deep mode, all outputs will correspond to the Main output of the hardware unit. In Wide mode, the Main output is routed to the left channel and the Aux output is routed to the right channel. Note that if you are using a mono output, Wide mode will be the same as Deep mode.
- **Age** `0-100%`: Controls the age of the electrical components that make up the Instant Phaser. 0% is a factory fresh unit from 1971, 25% is the box we modeled as it is now, 100% is a very ungracefully aged Instant Phaser.
- **Source**: Sets the source of the modulation. This can be any combination of the following: Oscillator, Manual, Envelope.
- **LFO Rate** `0.01-20 Hz`: Controls the rate of the LFO from 0.01Hz to 20Hz
- **LFO Width** `0-100`: Adjusts the range of the sweep of the Phaser’s LFO. 100 is the widest possible sweep and equivalent to the range of the original hardware.
- **Env Thresh** `-60 to 0 dB`: Controls the threshold of the envelope follower. This is variable from -60dB to -0dB.
- **Env Release** `10ms-10s`: Sets the release time of the envelope follower. Release times can vary from 10 milliseconds to 10 seconds.
- **Manual** `0-100%`: Provides manual control of phasing. 0% moves the nulls in the frequency response to their highest position in frequency, 100% moves them to their lowest position in frequency.

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### ModFilter

Modulated filters with selectable types and dual LFO modulation for swept, stereo-panned filter effects.

#### Parameters

- **Intensity**: Effect level. Controls a combination of base filter frequency and resonance.
- **Type**: Selects the filter type. The choices are: Lowpass, Bandpass, Highpass.
- **Depth**: Sets the modulation sweep range from narrow to wide. Controls the frequency offset of the left and right channels to create a stereo image.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Stereo Width**: In mono, this control is not used. In stereo, this control shifts the phase of the right channel’s LFO creating a tremolo that will move from left to right in the stereo field. When set to Max, the right channel will be 180 degrees out of phase with the left, creating an autopanner.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Phaser

All-pass filters creating moving frequency notches with characteristic sweeping sound.

#### Parameters

- **Intensity**: Effect level.
- **Type**: Selects phaser topology: Positive (non-inverted), Negative (inverted), Feedback (feedback only for deeper effect), Bi-phase (Mu-Tron-style topology), PhaseX0 (Phase 90 clone).
- **Depth**: Sets the modulation sweep range from narrow to wide.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Stages**: This control allows you to select the number of digital filters. For Bi-phase, selects the sweep direction.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Q-Wah

Versatile wah combining manual control, auto-wah, and vocal formant modes with dual LFO modulation.

#### Parameters

- **Q-Intensity**: Increases the resonance of the wah effect.
- **Type**: Wah Wah Vocal Wah Bass Wah Bass Vocal Note The Bass types retain the low end as the wah filter climbs to higher frequencies.
- **Depth**: When Effect Type is Wah Wah or Bass Wah, Depth sets the modulation sweep range from narrow to wide. When Effect Type is Vocal Wah or Bass Vocal, and “Bottom / Start Vowel” is set to Bottom, Vowel will determine the vowel sound of the vocal wah. When Effect Type is Vocal Wah or Bass Vocal, and “Bottom / Start Vowel” is set to Start Vowel, End Vowel sets the ending vowel for a talk-box style effect. List of available vowels: B..EA..T M..I..X S..E..T S..A..X H..O..T R..A..W W..OO..D T..U..NE F..U..N B..IR..D
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Bottom**: When Effect Type is Wah Wah or Bass Wah, Bottom sets the base frequency. When Effect Type is Vocal Wah or Bass Vocal, the first half of this parameter sets Bottom and the second half sets Start Vowel for a talk-box style effect.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### RingMod

Multiplies input by audio-frequency waveform creating complex bell-like non-harmonic overtones.

#### Parameters

- **Intensity**: Effect level.
- **Type**: Selects the ring modulator type. The choices are: Ring, String, Pitch. When set to Pitch, RingMod will pitch track the incoming audio.
- **Pitch** `±1200 cents`: If Type is set to Pitch, RingMod will pitch track the incoming audio and modulate it by a waveform that is shifted up to +/- 1200 c from your input, giving you a consistent synth-like tone across all notes. This parameter is unused when Type is set to Ring or String.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Tone**: Rolls off the high frequencies as it is turned clockwise.
- **Depth Mod**: Slightly detunes the right and left voices, which creates a stereo field.
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Rotary

Leslie speaker simulation with independent rotor and horn speed controls with Standard or Giant cabinet.

#### Parameters

- **Mix** `0-100%`: Wet/Dry mix, where 100 is an all wet signal. It has a special nonlinear taper which puts most of the knob travel in the most usable range.
- **Type**: Select the size of the cabinets. Standard Giant
- **Rotor Spd** `0.10-20 Hz`: Sets the rotation speed of the Rotor (low frequency) speaker, from 0.10 Hz to 20 Hz.
- **Horn Spd** `0.10-20 Hz`: Sets the rotation speed of the Horn (high frequency) speaker, from 0.10 Hz to 20 Hz.
- **Rtr/Hrn Mix**: Sets the balance between the Rotor level and Horn level.
- **Tone**: Rolls off the high frequencies as it is turned clockwise.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation from the secondary LFO that is applied to the Rotor Spd and Horn Spd parameters. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Rotor Spd value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Sticky Tape

Classic tape echo with compression, wow/flutter, and flange capability.

#### Parameters

- **Mix**: Controls the amount of dry and tapified signal.
- **Compression**: How much compression is applied. This is based off of the compression section of the DBX compander found in many professional tape machines. NOTE: Gain is automatically applied after the compression to try and maintain constant signal level. The Compression knob has been tuned for both Guitar and Bass. It is especially important to have the Instrument Type set correctly for Bass input and high Compression amounts.
- **Rec Drive**: How much gain is applied before going in to the tape emulation.
- **Tape Speed**: Controls the nominal speed at which the two tape machines are running. This affects the tone of the signal.
- **W&F Amount**: Adjusts the amount of wow and flutter applied. NOTE: With no offset, or no flanging engaged this will sound like detuning. With offset, or a flange engaged this sounds like modulation.
- **W&F Rate**: Controls the speed of the wow and flutter. 10 is a faster, more fluttery sound and 0 is more wowy.
- **Filter**: A simple tone control applied after the tape processing.
- **Width**: When stereo outputs are connected this pans the two tape machines to opposite sides. Note: When Offset is 0.0, or only a single output is connected, this control will do nothing.
- **Machine 2 Offset**: Controls how delayed Machine 2 is from Machine 1 by adjusting its speed. At 0, the machines are running perfectly in sync. 10 adds enough delay to get into slapback territory. NOTE: When no offset is applied, a default range is used when using the Flange performance switches. If an offset is applied, then the offset is treated as the range.
- **Flange Length**: Controls the rate of the flange performance parameters. This represents the time it takes for the flange to travel 1/2 of its period.

#### Performance Parameters

- **Flange M**: A momentary performance switch to engage the flange. This changes Machine 2’s speed by an amount determined by either the offset, or a default setting, and a rate determined by the flange length knob. Hold it down and it’s like your thumb is on the reel, lift up and the speed of Machine 2 will return to its original setting.
- **Flange**: A latching performance switch which simply turns on or off an automatic flange.

---

### TremoloPan

Modulated level effect creating tremolo that pans left-right, at maximum width becomes autopanner.

#### Parameters

- **Drive/Edge**: When Effect Type is set to Bias, this controls the amount of Drive. For high input levels, setting this to high levels can cause overload distortion. When Effect Type is set to Opto, this controls the input’s slew rate (Edge) and, depending on the input signal, may only have a subtle effect.
- **Type**: Selects tremolo type: Bias or Opto. Bias is a standard tremolo with drive control. Opto emulates an optical tremolo with slew rate control.
- **Depth**: Sets the modulation sweep range from narrow to wide.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Spread/Width**: In mono: spreads the tremolo waveform making the sound smoother. In stereo: shifts the right channel LFO phase for left-right panning; maximum (180°) creates an out-of-phase autopanner.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO modulation source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Tricerachorus

Bucket-brigade tri-chorus with three 120°-offset voices plus MicroPitch detuning.

#### Parameters

- **Chorus Mix** `0-99`: Global mix control for chorusing and has two modes, Chorus and Chorale. Chorus and Chorale Mix levels are independent of Detune Mix (see below). Chorus Mode (0 - 99 range on left half of the knob), all three chorus channel mixes, Left, Center, and Right are affected together. At 100 (Vibrato), no dry signal is present. In Chorus mode, LFO shapes are triangular from a range of 0 to 75. After 75, the LFO morphs from triangular to sinusoidal at 100. Chorale Mode (99 - 0 range on right half of the knob) adds two fixed rate LFOs, one slow and one fast, to the primary LFOs creating an effect similar to combining the Preset and Manual modes on the DYTRONICS TriChorus . This increases the complexity of the modulation, producing a richer sound. In Chorale mode, all LFO shapes are sinusoidal throughout the range of the control.
- **Rate** `0.1-20 Hz`: This is the base rate of the chorus modulation, from 0.1 Hz to 20 Hz. When Tempo Sync is On, this becomes a multiplier on the tapped BPM value. The Env Rate control can change the apparent rate, so if the rate that you are hearing is different from the value of the Rate control, try setting the value of Env Rate to 0.
- **Depth L** `Off-100`: Chorus modulation depth of the Left voice. From Off, to 100. When Off, the voice is removed from the mix, and the levels of the other voices are automatically adjusted to preserve the wet-dry blend. In mono to stereo routing, if Depth R is Off but Depth L is active, the chorused signal will be routed to the left and the dry signal will be routed to the right. This is a classic technique for producing a wider stereo image.
- **Depth C** `Off-100`: Chorus modulation depth of the Center voice. From Off, to 100. When Off, the voice is removed from the mix, and the levels of the other voices are automatically adjusted to preserve the wet-dry blend.
- **Depth R** `Off-100`: Chorus modulation depth of the Right voice. From Off, to 100. When Off, the voice is removed from the mix, and the levels of the other voices are automatically adjusted to preserve the wet-dry blend. In mono to stereo routing, if Depth L is OFF but Depth R is active, the chorused signal will be routed to the right and the dry signal will be routed to the left. This is a classic technique for producing a wider stereo image.
- **Delay** `0.39-200ms`: When Chorus Mix is in Chorus Mode, DELAY sets the minimum delay time for all voices, ranging from 0.39 mS to 200 mS. Short delays can be used to create light flanging. Typical chorus delays range from 1.5-10 mS. You can create a chorused slapback sound by using values between 50 and 100 mS. When “Chorus Mix / Vibrato / Chorale Mix” is in Chorale Mode, the delay amount for each voice becomes a function of the Delay setting and the Depth level of each voice. In this case, the Delay becomes a range of possible delay amount for each voice. As you increase the Depth of a voice, its delay amount decreases.
- **Detune Mix**: Mix control for the Detune section of the Algorithm. The Detuners are fed from the stereo output of the Chorus voices. Detune Mix controls the stereo left and right channels at the same time and is independent of “Chorus Mix / Vibrato / Chorale Mix”.
- **Detune** `±40 cents`: Controls both detune amounts for the left and right channels. Range is +/- 40 cents. Left and right channels get opposing amounts of detune (for example -30L/+30R). For enhanced versatility, the channels can be set with different opposing amounts. Left channel is the base detune amount and right channel can be adjusted around an 8 cent opposing window (for example -16L/+12R to -16L/+19R).
- **Env Mix** `-100 to +100`: Envelope to Mix. Playing dynamics modulate the global “Chorus Mix / Vibrato / Chorale Mix” and Detune Mix amounts. Range is -100 to 100. Negative values decrease the mix levels when you attack a note, and can be used to increase the clarity of your attacks or make sustained notes more expressive over time. Playing louder will reduce the chorusing effect, and you can use large negative values to only allow chorusing when the input is soft. At zero, the envelope will not affect the chorus or detune mixes. Positive values increase the internal mix levels for chorus and detune from 0 up to the levels set by the mix knobs when you attack a note. For example, with Detune Mix set to 50, Chorus Mix set to 0, and Env Mix set to 50, when a note is attacked, the internal detune level will increase to 50, then decay towards 0 with the note. The chorus level, however, will not increase because it is at 0.
- **Tone**: Shapes the high or low end of the output signal. Positive values roll off high frequencies Hi Cut, 0 is flat, and negative values roll off low frequencies Lo Cut. Use the Lo Cut range to reduce muddiness. Use the Hi Cut range to roll off high frequencies for a softer sound. The tone control only affects the wet signal path. Changes to the Chorus Mix knob (or usage of Env Mix) may change the apparent effect of the Tone control. For example, a setting of Hi Cut 50 will sound brighter when the Chorus Mix knob is set at 50 versus when Chorus Mix is at 100 (Vibrato).

#### Performance Parameters

- **Swirl**: Adds another dimension to TriceraChorus’ sound via stereo phase shifters after the Detune section to create throbbing and swooshing effects. The amount of Swirl depends on the greater level of either Chorus Mix or Detune Mix and follows the Env Mix control. Swirl speed is adjusted by Rate and follows the ENV Rate control. Use faster rates to achieve deeper Swirl effects.
- **Retrigger**: Retriggers the LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.

---

### Undulator

Classic modulated tremolo from the iconic H3000 combining swell, detuned delay chains, and AM/FM modulated tremolo.

#### Parameters

- **Intensity**: Increase the dry/effect ratio.
- **Feedback**: Controls the amount of feedback in the delay structure.
- **Depth**: Sets the tremolo sweep range, which increases in depth and intensity as the knob is turned clockwise.
- **Speed**: Sets the rate of the tremolo. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Spread**: Controls the amount of detuning in the delay structure.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

### Vibrato

Pitch modulation simulating string vibrato or whammy bar with Modern, Vintage, and Retro types.

#### Parameters

- **Intensity**: Effect level.
- **Type**: Selects vibrato type: Modern, Vintage, Retro.
- **Modulation Depth**: Sets the modulation sweep range from narrow to wide.
- **Speed**: Sets the modulation sweep rate. Speed becomes Sensitivity when Shape is set to Envelope or ADSR.
- **Modulation Waveform Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Stereo Width**: For Modern and Vintage controls the width of stereo panning (stereo mode only). For Retro selects the number of filter stages.
- **Depth Mod**: Controls the amount of modulation of the Depth parameter. Analogous to AM (Amplitude Modulation).
- **Speed Mod**: Controls the amount of modulation of the Speed parameter. Analogous to FM (Frequency Modulation).
- **Mod Rate**: Sets the secondary LFO rate – determines how fast the Depth Mod and Speed Mod “wiggle” their targets. Ranges from 1/8th to 8x the Speed value. Mod Rate becomes Mod Sens when Mod Source is set to Envelope or ADSR.
- **Mod Source**: Selects the secondary LFO waveform, or source. The choices are: Sine Triangle Peak Random Square Ramp SampHold

#### Performance Parameters

- **Retrigger**: Retriggers the primary and secondary modulation LFOs to the beginning of their cycles. Useful for re-syncing during playback, or creative effects.
- **Speed/Brake**: The Brake engages while this switch is pressed. Short-press to toggle between Fast and Slow. Long-press to engage Brake.
- **Fast/Slow**: Press to toggle between Fast and Slow, which slows the primary and secondary LFOs by a predetermined factor. The Brake does not engage while this switch is pressed.
- **Brake M**: Slows the LFOs at a constant rate and pauses the LFOs until the switch is released.

---

## Multi

### SpaceTime

Multi-effects combining Modulation, two Delays, and Reverb into one easy-to-use effect.

#### Parameters

- **Mix** `0-100%`: Controls overall Algorithm wet/dry balance. 100% is all wet signal.
- **Mod Amt** `0-100`: Adds Modulation to entire signal path. Modulation depth also increases as you go from 0 to 100.
- **Mod Rate** `0.05-12.50 Hz`: Adjusts the speed of the LFO controlling the Modulation section of SpaceTime. Continuously adjustable from 0.05Hz to 12.50Hz.
- **Verb Lvl** `0-100`: Adjust the output level of the Reverb and routes the Reverb in Series after the Delays or Parallel with the Delays. The first half of the knob adjusts Series Reverb level from 0 to 100 while the second half of the knob switches to Parallel routing and adjusts Reverb level from 0 to 100. Percussive playing coupled with long Delay times and short Reverb Decay times will showcase parallel routing.
- **Decay**: Sets the decay length of the Reverb in seconds or Note Divisions when with Tempo Sync ON.
- **Color** `0-100`: Changes the Reverb character from small and dense (set to 0) to large and spacious (set to 100).
- **Delay Lvl** `0-100`: Controls the amount of both Delays in the signal path. Can also be used to set the dry to wet blend of delayed signal sent to the Reverb in the series path. With DLY LVL set less than 50, dry signal and Delayed signal are both sent to the Reverb section. After 50, DLY LVL reduces the dry signal sent to the Reverb allowing only the delay repeats to have Reverb when the control reaches 100.
- **Delay A** `0-2500ms`: Sets the Delay time for Delay A from 0 to 2500 ms when TEMPO Sync is OFF. With TEMPO Sync ON, Delay is sync’ed to the Tempo BPM and is adjusted in note division increments from No Delay to a Whole Note in the most common note divisions.
- **Delay B** `0-2500ms`: See description for Delay A
- **Feedback**: Adjusts the amount of feedback for both delays and contains two feedback types (F1 and F2). F1 links both delay times to create a rhythmic, repeating pattern where the longer delay sets the pattern length. The shorter delay will not repeat again until the longer delay has passed. F2 is a traditional feedback control, where delay times are independent.

---

## Reverb

### Blackhole

A galactic-scale reverb from the DSP4000 with lush sounds ideal for guitars, strings, and pads.

#### Parameters

- **Mix**: Determines the relative level of the wet and dry signals.
- **Gravity**: The Blackhole’s equivalent of decay time. On the right-hand side, the Gravity control sweeps through its forward reverb range from a very dense decay to a very long and smooth decay. On the left hand side, the Gravity control is in its inverse mode and sweeps through a range of reverse reverb-like settings.
- **Size**: Determines the size of the reverb. This can range from cartoonishly small to cosmically epic.
- **Pre Delay** `0-2000ms`: Sets the amount of delay before the reverb section. When Tempo Sync is off, this ranges from 0 ms to 2000 ms. When Tempo Sync is on, this is set in subdivisions of the tempo.
- **Low Level**: Controls the level of low frequencies in the reverb tail using a shelving filter with a corner frequency of 350 Hz.
- **High Level**: Controls the level of high frequencies in the reverb tail using a shelving filter with a corner frequency of 2000 Hz.
- **Mod Depth**: Sets the modulation depth in the reverb tail. This can be a subtle control, which nevertheless can reduce ringing in the reverb tail and add some motion to the sound. This parameter is frozen while Feedback is set to Infinite or Freeze.
- **Mod Rate**: Sets the relative speed of the modulation in the reverb tail. Subtle but useful.
- **Feedback**: Controls the feedback around the entire reverberation structure, for even larger sounds. Turning clockwise to Infinite will allow for infinite reverberation time, while still letting incoming signal into the reverberation structure. Turning further clockwise to Freeze sets the reverberation time to infinite, and does not allow incoming signal into the reverberation structure.
- **Resonance**: Controls the resonance of the Low-level and High-level filters. When the filters are set to 0, this does nothing, but when they are active, it can create a much more filtered sound. But be careful, extreme settings will increase the chances of overloads.

---

### DualVerb

Two parallel high-quality studio reverbs with independent controls for rich stereo reverberation.

#### Parameters

- **Mix**: Determines the relative level of the wet and dry signals.
- **A/B Mix**: Determines the input level of the A and B reverbs. When Decay is Frozen, A/B Mix is post-reverb (normally it is pre-reverb). With stereo outputs, you may turn this parameter fully clockwise for dual mono reverbs (A on left, B on right). A mono input will be sent to each reverb, while a stereo input will send input 1 to reverb A, and input 2 to reverb B.
- **Resonance**: Adjusts the resonance of reverb A and B’s Tone controls. This does not affect the sound if Tone is set to 0.
- **Size**: Determines the size of both reverbs A and B. Many different size combinations are possible with this one knob. The following parameters are available for both Reverb A and B:
- **Decay A** `0-50s`: Sets the decay time for the reverb. When Tempo Sync is off, this ranges from 0 s to 50 s. When Tempo Sync is on, this is set in subdivisions of the tempo. Turning clockwise to Infinite will allow for infinite reverberation time, while still letting incoming signal into the reverberation structure. Turning further clockwise to Freeze sets the reverberation time to infinite, and does not allow incoming signal into the reverberation structure.
- **Decay B** `0-50s`: Sets the decay time for the reverb. When Tempo Sync is off, this ranges from 0 s to 50 s. When Tempo Sync is on, this is set in subdivisions of the tempo. Turning clockwise to Infinite will allow for infinite reverberation time, while still letting incoming signal into the reverberation structure. Turning further clockwise to Freeze sets the reverberation time to infinite, and does not allow incoming signal into the reverberation structure.
- **Pre Delay A** `0-900ms`: Sets the amount of delay before the reverb. When Tempo Sync is off, this ranges from 0 to 900 ms. When Tempo Sync is on, this is set in subdivisions of the tempo.
- **Pre Delay B** `0-900ms`: Sets the amount of delay before the reverb. When Tempo Sync is off, this ranges from 0 to 900 ms. When Tempo Sync is on, this is set in subdivisions of the tempo.
- **Tone A**: Tone control for the reverb. Negative values bring out the lows, while positive values bring out the highs.
- **Tone B**: Tone control for the reverb. Negative values bring out the lows, while positive values bring out the highs.

---

### DynaVerb

Eclipse reverb coupled with Omnipressor model for dynamics-based reverb control.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal
- **Decay**: Decay in seconds or note-based with Tempo Sync ON. When decay is 0, this effect can be used as a standalone Omnipressor or gate.
- **Size**: Room size of reverb.
- **Attack Time**: Attack time of Omnipressor/gate in seconds.
- **Low Band Shelving Level**: Post reverb shelving boost/cut of low frequencies with cut-off at 350 Hz.
- **High Band Shelving Level**: Post reverb shelving boost/cut of high frequencies with cutoff at 2000 Hz.
- **Compression/Expansion Ratio**: Ratio control for the Omnipressor from traditional Gated sound, to expansion, then compression, then limiting and infinite ducking, then to negative ratios which result in dynamic reversal.
- **Release Time**: Release time for the Omnipressor/gate in seconds.
- **Threshold**: Threshold for the Omnipressor/gate.
- **Sidechain**: The mixer to the sidechain input (gain control signal). When set to minimum, the gain curve is derived from the input only. At maximum, it is a feedback dynamics unit with gain derived from the reverb output. In Omnipressor Mode, this simply lets you fade between a feedforward (FF) and feedback (FB) compressor/expander/gate/etc.

---

### Hall

Simulates large enclosed spaces with flexible 3-band crossover reverb network.

#### Parameters

- **Mix**: Determines the relative level of the wet and dry signals.
- **Decay**: Master decay in seconds or note-based with Tempo Sync ON.
- **Size**: Hall size.
- **Pre Delay**: pre-delay in milliseconds or note-based with Tempo Sync ON.
- **Low Band Reverb Level**: boost/cut of LOW reverb with cut-off at 300 Hz, -100 effectively cuts all of the low band reverb.
- **High Band Reverb Level**: boost/cut of HIGH reverb with cut-off at 1500 Hz, -100 effectively cuts all of the high band reverb.
- **Low Band Decay**: Decay of low band reverb, scales the Decay time.
- **High Band Decay**: Decay of high band reverb, scales the Decay time.
- **Modulation Level**: Increases random modulation of reverb tails.
- **Mid Band Reverb Level**: Boost/cut of mid reverb (between 300 and 1500 Hz), -100 effectively cuts all of the mid band reverb.

---

### MangledVerb

Non-standard stereo reverb feeding into distortion, from subtle bow-scraping to chaotic mayhem.

#### Parameters

- **Mix** `0-100`: Wet/dry mix, where 100 is an all wet signal. It has a special nonlinear taper which puts most of the knob travel in the most usable range. Note: the Mix control is not accounted for in the signal flow diagram.
- **Decay** `1-100`: Length of reverb decay scaled from 1-100. Less decay will take away reverb attack. Specifically, higher values (greater than 70) will impart traditional reverb tails, while lower values (less than 70) can result in reverse reverb sounds with more build up.
- **Size**: Determines the size of the reverb. To use MangledVerb as a distortion type effect, try setting this below 15.
- **Pre Delay** `0-1500ms`: Sets the amount of delay before the reverb section. When tempo mode is off, this range is from 0 to 1500 milliseconds. When Tempo Sync is set to ON, Pre-Delay is set in beat divisions of the tempo. The Pre-Delay control affects the Pre-Delay Block in the signal flow diagram.
- **Low Band Level**: Boost/Cut of the low frequencies before the distortion section of the signal path.
- **Mid Band Level**: Boost/Cut of the middle frequencies before the distortion section of the signal path.
- **High Band Level**: Boost/Cut of the high frequencies before the distortion section of the signal path.
- **Softclip/Overdrive Type**: Use this control to choose from two types of distortions (soft-clipping and overdrive) and set their gain/drive amount. The first half of the knob controls the Softclip gain level from 1 to 100. Passing 100 in Softclip switches the distortion type to Overdrive with a gain/drive range of 1 to 100. The gain/drive amounts in the distortion section were designed so that the transition from Softclip to Overdrive would be as smooth as possible.
- **Distortion Output Level** `-18dB to +6dB`: Controls the output level of the distortion section from -18 dB to +6 dB. Adding gain/drive in the distortion section via the Softclip/Overdrive control will naturally add level, so use this control accordingly. Note: The Level control knob is different than the Out Gain. The Out Gain sets the output level of the entire Algorithm (including the dry signal path).
- **Wobble**: A modulation rate that does some spooky detuning.

---

### ModEchoVerb

H8000-based infinite reverb into infinite-feedback delay with modulation options.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Decay**: Decay in seconds or note based with Tempo Sync on. All the way right Infinite gives an infinite reverb/sustain.
- **Size**: From normal Hall type room sizes to huge canyon sounds with echoes.
- **Echo**: Post reverb delay time in milliseconds or note-based with Tempo Sync ON.
- **Low Band Shelving Level**: Post reverb shelving boost/cut of low frequencies with cutoff at 350 Hz.
- **High Band Shelving Level**: Post reverb shelving boost/cut of high frequencies with cutoff at 2000 Hz.
- **Echo Feedback**: Feedback amount around the post reverb echo.
- **Modulation Rate** `0-100`: The modulation rate from 0 to 100.
- **Modulation Type & Depth**: Select modulation type and depth: Swept Verb Flanger Mix Chorus Mix
- **Echo Tone**: Tone control in the feedback loop of the echoes.

---

### Plate

Emulates early analog-mechanical reverbs with extended reverb times and extensive tone controls.

#### Parameters

- **Mix**: Determines the relative level of the wet and dry signals.
- **Decay**: Decay in seconds or note-based with Tempo Sync ON.
- **Size**: Plate size.
- **Pre Delay**: Pre delay in milliseconds or note-based with Tempo Sync ON.
- **Low Damp**: Sets the damping frequency for the low end.
- **High Damp**: Sets the damping frequency for the high end.
- **Distance**: Sets room/transducer distance from source/plate driver.
- **Diffusion**: Adjusts diffusion amount which affects reverb build up and tail density.
- **Mod Level**: Mixes in random modulation in reverb tail.
- **Tone** `-100 to +100`: A pre-reverberator tone control, -100 to 0 is darker, 0 to 100 is brighter.

---

### Reverse Reverb

True reverse reverb followed by forward reverb with delay/feedback.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Decay**: Reverse decay in milliseconds or note-based with Tempo Sync ON (also the delay amount for Late Dry Signal Level).
- **Size**: Mixes in a standard reverb that is post reverse section for bigger sounds.
- **Feedback**: Amount of delay feedback around reverse reverb (delay amount is Decay amount).
- **Low Level**: Shelving boost/cut of low frequencies.
- **High Level**: Shelving boost/cut of high frequencies.
- **Late Dry Signal Level**: Adjusts amount of dry signal that occurs directly after the reverse build up.
- **Diffusion**: Diffusion in the reverse build-up: set to zero for a mechanical stutter.
- **Modulation Level**: MicroPitch detuning modulation at the input.
- **Contour**: Increase the span between low and high crossover frequencies for the Low Level and High Level. Affects the sound unless Low Level and High Level are both set to 0.

---

### Room

Precision room simulator from vocal booths to small halls with early/late reflection control.

#### Parameters

- **Mix**: Determines the relative level of the wet and dry signals.
- **Decay**: Decay in seconds or note-based with Tempo Sync ON.
- **Size**: Room size.
- **Pre Delay**: Pre-delay in milliseconds or note-based with Tempo Sync ON.
- **Low Band Shelving**: Post reverb shelving boost/cut of low frequencies with cutoff at 350 Hz.
- **High Band Shelving**: Post reverb shelving boost/cut of high frequencies with cutoff determined by High Band Cutoff Frequency parameter.
- **Early Reflection Level**: Control the levels of the early and late reflections.
- **Late Reflection Level**: Control the levels of the early and late reflections.
- **Diffusion**: Adjusts diffusion amount which affects reverb build up and tail density.
- **Modulation Level**: Adds random modulation of both diffusors and late reverb tail.
- **High Band Cutoff Frequency**: Control the corner frequency of High Band Shelving. No affect if High Band Shelving parameter is is set to 0.

---

### SP2016 Reverb

Emulation of classic Eventide SP2016 Signal Processor reverb in Vintage and Modern versions.

#### Parameters

- **Mix**: Controls the mix between the unprocessed input and the reverberated output. This is especially useful when some pre-delay is added.
- **Reverb Type**: Selects the reverb Algorithm. SP2016 Reverb features three reverb Algorithms, Stereo Room, Room, and Plate. Each Algorithm is available in two versions: Vintage and Modern. The Vintage Algorithms are modeled on the original SP2016’s Algorithms and hardware, and feature a lower bit-depth than the modern versions. The Modern Algorithms are brighter, more diffuse, and use a higher bit-depth. Note The Position, Diffusion, and EQ controls are disabled for the Vintage Plate Algorithm because they were not present in the original SP2016 Algorithm.
- **Decay**: Sets the reverb time.
- **Position**: This is used to move your “listening position” from the front of the “room” to the rear. You’ll find that Position is one of the most useful controls in adjusting the reverb to fit your mix. A simplified explanation: it changes the mix between the early and late reflections; what actually happens in the Algorithm is more complex than this, however.
- **Diffusion**: This alters the character of your space – from the sharp reflections of flat, hard surfaces (low) to the diffused reflections from rough, irregular ones (high). The Diffusion control doesn’t change the decay time, but it does have an effect on the evident nature of the decay by thickening or thinning its density. Note that this can often be a subtle difference and may be difficult to hear with some types of program material and/or with long decay times. The effects of the control will be most apparent with short decays and program material with percussive attacks.
- **Pre Delay** `0-999ms`: Introduces a delay before the reverb effect. SP2016 Reverb is capable of long pre-delays, up to 999 milliseconds, and these can be used to create echo effects as well. Note The equalization section provides controls for high and low shelving filters. These controls affect parameters deep within the feedback structure of the reverberator and the effect may be subtle or dramatic depending on the program material and other reverb settings such as Decay, Position, or Diffusion. In general, the controls will have more pronounced effects at longer decay times and more distant position settings. Additionally, it’s usually easier to hear the effect of changes to the high frequency controls than it is to hear changes to the low frequency controls.
- **Low Freq** `50-500 Hz`: Sets the corner frequency for the low shelving filter; the range is from 50 to 500 Hz in increments of 50 Hz.
- **Low Gain** `-8 to +4 dB`: Adjustable gain for the low shelving filter, from -8 to +4 dB.
- **High Freq** `1000-8000 Hz`: Sets the corner frequency for the high shelf filter; the range is from 1000 to 8000 Hz in increments of 500 Hz.
- **High Gain** `-8 to 0 dB`: Adjustable gain for the high shelf filter, from -8 to 0 dB.

---

### Shimmer

Pitch-shifted reverb creating heavenly textures with two pitch shifters in feedback path.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Decay** `0-100`: Arbitrary 0-100 decay (less decay will also take away reverb attack).
- **Size**: Size of the reverb.
- **Delay**: Post reverb and pre pitch-shift delay time in milliseconds or note-based with Tempo Sync on.
- **Low Band Decay**: Amount of post reverb and pitch-shifter low band signal (this is in the feedback path).
- **High Band Decay**: Amount of post reverb and pitch-shifter high band signal (this is in the feedback path).
- **Pitch Shift A**: Pitch-shifter A’s pitch in cents 500c = P4th 700c = P5th 1200c = 1 Octave 1900c = 1 Octave+P5 2400 = 2 Octaves
- **Pitch Shift B**: See description for Pitch Shift A
- **Pitch Decay** `0-100`: The Pitch Decay knob controls the amount of pitch shifting in the reverb tail. It increases from 0 to 100. Beyond 100 are two Freeze modes. Pitch Freeze locks out the pitch shifters, but feeds the reverb, allowing you to freeze the Shimmer pitch climb at opportune times. Pitch+verb Freeze freezes everything (pitch and reverb) for dry soloing on top of the frozen reverb.
- **Mid Band Decay**: Amount of post reverb and pitch-shifter mid band signal (this is in the feedback path).

---

### Spring

Models guitar amplifier spring reverb with physical parameter access and tube-amp tremolo.

#### Parameters

- **Mix**: Wet/dry between reverb and tremolo dry signal. If Tremolo Pre/Post is set to Pre, then this controls the wet/dry mix between the spring reverb and the tremolo’d dry signal. If Tremolo Pre/Post is set to Post, then this controls the wet/dry mix between the tremolo’d spring reverb and the unaltered dry signal.
- **Decay**: Decay in seconds or note-based with Tempo Sync on.
- **Tension**: Controls spring tension.
- **Number of Springs** `1-3`: Number of springs in the ‘tank,’ mixes in 1 to 3 springs.
- **Low Band Damping**: Sets the damping frequency for the low end.
- **High Band Damping**: Sets the damping frequency for the high end.
- **Tremolo Intensity**: The depth of the tremolo.
- **Tremolo Rate**: The speed of the tremolo in Hz or note-based with Tempo Sync ON.
- **Tremolo Pre/Post**: Places the tremolo before or after the spring reverb. Note that when in Pre mode, the Mix control only affects the reverb signal. Tremolo will still be applied to the dry signal.
- **Modulation Level**: Mixes in modulation for a nice chorusing effect.
- **Resonance**: Metallic resonance at the High Band Damping frequency.
- **Spring Type**: Select from 2 different reverb tank size. Large and small.

---

### TremoloVerb

Large reverb controlled by aggressive tremolo with waveform, envelope, and expression pedal control.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 100% is all wet signal.
- **Decay**: Decay in seconds or note-based with Tempo Sync ON.
- **Size**: Room size of reverb.
- **Pre Delay**: Pre-delay time in milliseconds or note-based with Tempo Sync ON.
- **Low Band Shelving Level**: Post reverb shelving boost/cut of low frequencies with cutoff at 350 Hz.
- **High Band Shelving Level**: Post reverb shelving boost/cut of high frequencies with cutoff at High Freq.
- **Tremolo Shape**: Selects the waveform, or source, of the modulation. The choices are: Sine Triangle Peak Random Square Ramp SampHold
- **Tremolo Speed**: Tremolo speed in Hz, sensitivity, or note-based with Tempo Sync on.
- **Tremolo Depth**: Tremolo depth, in stereo mode you have the option to have mono depth (same on both channels) or stereo depth (tremolo is 90 degrees out of phase).
- **High Band Cutoff Frequency**: The high corner frequency of High-level. Affects the sound unless High-level is set to 0.

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### Wormhole

Massive, tilting reverb with sci-fi themed controls and warping for dynamic pitch/delay modulation.

#### Parameters

- **Mix** `0-100%`: Wet/dry mixer, 0 is fully dry, 100 is fully wet.
- **Length** `0-100 light years`: Wormhole distance in light years. Controls the decay time of the reverb. Internally tapered from 0 l.y. (shortest decay, 3s) to 100 l.y. (longest decay, 1000s). (0 to 100 l.y. or 30.67 parsecs).
- **Diameter** `0-100`: Width of the interstellar Wormhole. Controls the size of the reverb. A Diameter of 0 is tight enough to pull the ears off a gundark. A Diameter of 100 will fit Executor-class Super Star Destroyers eight abreast.
- **Lo Decay** `0-100`: Decay rate of the low frequency content of the reverb. 0 is quickest decay. 100 is slowest decay.
- **Hi Decay** `0-100`: Decay rate out of the high frequency content of the reverb. 0 is quickest decay. 100 is slowest decay.
- **Entry Field** `0-100`: Entrance characteristics to the Wormhole. Controls early reflections and diffusion in the reverb. 0 is a rougher entrance to the WormHole (less diffuse, noticeable early reflections). 100 is a smoother entrance to the Wormhole (more diffuse, less noticeable early reflections).
- **Pre Delay** `0-2000ms`: Delay added before Wormhole entrance. (0 t0 2000ms)
- **Stability** `0-100`: Wormhole stability across time. Controls modulation depth of the reverb. 0% is the least stable Wormhole with large pitch variations happening to the reverb through time (max modulation/most unstable). 100% is a stable Wormhole with no reverb pitch variations through time (no modulation).
- **Stability Rate** `0-100`: Movement speed of an unstable Wormhole. Controls modulation rate of the reverb. Range is from 0 (slowest rate) to 100 (fastest modulation rate). Use in conjunction with the Stability control.
- **Warp Acceleration** `1.0-10s`: How long it takes to traverse the wormhole and reach the top warp speed set by the Warp Factor control. Units are in total time to traverse the worm hole and lower values accelerate faster. Controls the rate of change of the reverb delay lines. (1.0 to 10s)
- **Warp Factor** `5-10`: Top warp speed desired through the worm hole. Higher Factors manifest as a higher final pitch changes. Warp Factor 10.00 theoretically highest possible speed. Controls the amount of change of the delay lines. (5 to 10s)
- **Warp Mix**: Sets the mix level of the effect during warping, overrides the Mix control.
- **Warp Bass**: Bass EQ control for Warp effect.
- **Warp Treble**: Treble EQ control for Warp effect.

#### Performance Parameters

- **Warp L**: Latching footswitch. Press once to go thru the entire warping cycle. Footswitch unlatches after cycle completion.
- **Warp M**: Momentary footswitch. Hold to keep warp cycle engaged. Releasing before cycle completion generates a “deceleration” (decreasing pitch) sound to the warp effect.

---

## Synth

### HotSawz

Subtractive synthesis using six oscillators following a mono pitch tracker with low-pass filter and three modulation sources.

#### Parameters

- **Mix** `0-100`: Knob has four ranges, each 0 to 100. Each range mixes the dry signal with various oscillator combinations.
- **Osc Depth**: Mixes in 2nd oscillators for each register and adds detuning. Also spreads the oscillators across the stereo field. Modulation sources assigned to Osc Depth are additive.
- **Cutoff**: Controls the cutoff frequency of the low pass filter. Filter is in series with wet signal.
- **Resonance**: Controls the low pass filter’s resonance.
- **Speed** `0.1-20 Hz`: Controls LFO’s wave shape and speed. This parameter has four ranges, each 0.1 Hz to 20 Hz or Whole note to 1/16 note divisions. Each range switches the LFO wave shape.
- **LFO Amount**: Assigns LFO destination and controls amount of modulation. Knob has four ranges. Each range assigns the LFO to a different destination for modulation.
- **Attack** `0-3000ms`: Gate Attack speed from 0 to 3000ms. When the Gate Sustain/Range knob is set to OFF, Attack knob has no effect.
- **Decay** `0-3000ms`: Gate Decay speed from 0 to 3000ms. When the Gate Sustain/Range knob is set to OFF, Decay knob has no effect.
- **Gate**: Assigns gate destination and controls amount of either Sustain or Range of the Gate. Knob has four ranges. Gate Sustain level occurs after both Attack and Decay of the Gate (There is no release in the Gate). Gate Range (for Pitch as destination) is how far from 0 pitch modulation is allowed to go at the end of Gate attack.
- **Envelope** `0-100`: This Envelope is triggered and drawn by dynamics of input level. This parameter assigns Envelope destination and controls amount of modulation. It has four ranges, each 0 to 100. Each range assigns the Envelope to a different destination for modulation.

#### Performance Parameters

- **Retrigger**: Retriggers the LFO to the beginning of the cycle. Useful for re-syncing during playback, or creative effects.

---

### PolySynth

Polyphonic guitar-to-synth transformer using SIFT technology with multiple voices and modulation options.

#### Parameters

- **Mix** `0-100`: Controls the amount of dry and pitch shifted signal. 0 to 100.
- **Attack** `5-1000ms`: Controls the Attack time of the generated synth sounds. 5 to 1000 ms or Tempo Based.
- **Resonance** `0-100`: Controls the resonance of the filters after each synth voice. 0 is no resonance, 100 is very resonant. 0 to 100.
- **Cutoff** `0-100`: Controls the cutoff frequency of the filter. 0 to 100.
- **Env Amount** `-100 to 100`: Sets the maximum amount the filter cutoff will open or close to (start is always what is set by the Cutoff knob). -100 to 100.
- **Env Sense** `0-100`: Adjusts the sensitivity of the envelope or how hard do you need to play to get it to hit the value set by Env Amount. 0 to 100.
- **LFO Destination**: Sets what parameter the LFO is modulating: Cutoff Volume Pitch PWM Detune
- **LFO Amount** `-100 to 100`: Controls the amount of modulation the LFO applies. -100 to 100.
- **LFO Rate** `0.01-20.0 Hz`: Sets the speed of the LFO. 0.01 to 20.0 Hz or Tempo Based.
- **LFO Shape**: Sets the shape of the LFO: Sine Triangle Square Peak Ramp Up Ramp Down Random Sample & Hold
- **Detune** `-100 to 100`: Controls the detuning of all three voices. Adds a variable amount to each such that modulation is still heard even with two voices. -100 to 100.
- **Spread** `-100 to 100`: Pans Voice 1 and Voice 3 to opposite sides while keeping Voice 2 in the middle. -100 to 100.

#### Performance Parameters

- **Freeze**: Freezes the current synth sound, sustaining it indefinitely.
- **LFO Retrig**: Retriggers the LFO momentarily to its starting position.

---

### Synthonizer

Pitch-tracking synthesizer with Voice A (additive, organ/theremin) and Voice B (subtractive, classic analog).

#### Parameters

- **Mix** `0-100`: Wet/dry mixer, 100% is all wet signal.
- **Vox Mix**: Controls the ratio of the two synthesized voices A and B.
- **Wave Mix A**: Controls the mix of the various added waveforms to control the tone and perceived pitch of voice A.
- **Octave B**: Controls the blend between unison, 1 octave down, and 1 octave up synth voices to control the tone and perceived pitch of voice B.
- **Attack A**: Controls the attack time for synthesized voice A.
- **Attack B**: Controls the attack time for the filter on synthesized voice B.
- **Verb Level**: Sets the reverb level.
- **Verb Decay**: Sets the reverb decay time.
- **Shape A**: Selects voice A waveshape: Sine Triangle Sawtooth Organ 1 Organ 2
- **Sweep B** `0-100`: Controls the sweepable filter on voice B. Values from 0 to 50 sweep a low-pass filter, values from 50 to 100 sweep a high-pass filter.

#### Performance Parameters

- **Flex**: Shifts both voices up one octave when activated.

---

## Utility

### Mute

Mutes incoming audio completely.

---

### Thru

Passes audio through unaffected.

---
