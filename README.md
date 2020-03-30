# computer-music

Let your computer compose music (random noise) for you!

## Requirements

- python 3.7
- python-pip
- python-tk
- virtualenv

## Build & Run

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Create computer music with
python create_computer_music.py

# Display help
python create_computer_music.py --help

# Display the signal wave (uses matplotlib.pyplot)
python show_signal_wave.py -f output.wav

# Play the WAV file.
python play_audio.py -f output.wav
```

## Notes

- **Sound** is the sequential disturbance of air molecules.
- **Frequency** (is the number of occurrences of a repeating event per unit of time
  and measured in the units of hertz (**Hz**).
- **Stereophonic sound** creates an illusion of multi-directional audible perspective
  (i.e. you get the impression of sound head from various directions).
- A **Sample** is a value or a set of values at a point in time and/or space.
- **Sampling** is the process to turn a continuous-time signal into a discrete-time signal.
- Sampling can be used to store, retrieve and transmit signals without any loss
  of quality.
- Audio waveforms are typically sampled at 44.1 kHz, 48 kHz, 88.2 kHz or 96 kHz.
- Human hearing: 20-20.000 Hz.
- **Bit depth** is the number of bits of information in each sample.
- Audio is typically recorded at 8, 16 and 24 bit depth.
- **WAV** or **WAVE** was developed by Microsoft and IBM for storing audio bitstream on PCs.
- WAV is typically raw and uncompressed audio in the linear pulse code modulation
  (**LPCM**) format.
- **LPCM** is the method to digitally represent sampled audio signals.
- LPCM is the standard audio code (uncompressed) format for audio CDs.
- **WAV** is just a **RIFF** file with a single "WAVE" chunk which consists of two sub-channels:
  - **fmt chunk** specifying the data format.
  - **data chunk** containing the sample data.
- The data of a WAV file is a sequence of **frames**.
- A frame consists of samples.
- **RIFF** (Resource Interchange File Format) is a generic file container format for
  storing data in tagged chunks.
- RIFF starts out with a file header followed by a sequence of data chunks.
- RIFF is primarily used to store multimedia (sound & video).
- A **chunk** is a fragment of information (used in PNG, IFF, MP3, AVI, WAV, ...)

## Also interesting

- http://soundfile.sapp.org/doc/WaveFormat/
- http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/Docs/riffmci.pdf
