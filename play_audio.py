import wave
import sys
import pyaudio
import argparse

CHUNK = 1024

def get_args():
    argparser = argparse.ArgumentParser('Play a wav file')
    argparser.add_argument('-f', '--file', dest='file', default='Input wav file')
    return argparser.parse_args()

def main():
    args = get_args()

    wav_file = wave.open(args.file, 'rb')
    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio.get_format_from_width(wav_file.getsampwidth()),
                        channels=wav_file.getnchannels(),
                        rate=wav_file.getframerate(),
                        output=True)

    signal = wav_file.readframes(CHUNK)

    while signal != '':
        stream.write(signal)
        signal = wav_file.readframes(CHUNK)

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == '__main__':
    main()
