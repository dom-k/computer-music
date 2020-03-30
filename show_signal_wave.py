import sys
import wave
import argparse
import numpy as np
import matplotlib.pyplot as plt

def get_args():
    argparser = argparse.ArgumentParser(description='Display a mono audio signal wave')
    argparser.add_argument('-f', '--file', dest='file', required=True,
                           help='the wav file to display')
    return argparser.parse_args()

def show_wave_from_signal(signal, framerate):
    time_range = np.linspace(0, len(signal) / framerate, num=len(signal))
    plt.plot(time_range, signal)
    plt.show()

def main():
    args = get_args()
    wav_file = wave.open(args.file, 'rb')

    if wav_file.getnchannels == 2:
        print('Sorry, just mono files.')
        sys.exit(0)

    signal = wav_file.readframes(-1)
    signal = np.frombuffer(signal, dtype=np.int16)
    framerate = wav_file.getframerate()
    show_wave_from_signal(signal, framerate)

if __name__ == '__main__':
    main()
