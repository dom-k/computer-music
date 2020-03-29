import wave
import random
import argparse
import numpy as np

def get_args():
    argparser = argparse.ArgumentParser('Let your computer compose music (random noise) for you!')
    argparser.add_argument('-o', '--output', dest='output_file', default='output.wav',
                           help='specify the the output file')
    argparser.add_argument('-f', '--framerate', dest='framerate', default=44100,
                           help='samples per second')
    argparser.add_argument('-n', '--nframes', dest='nframes', default=300000,
                           help='number of frames')
    argparser.add_argument('-c', '--channels', dest='nchannels', default=1,
                           help='number of channels')
    argparser.add_argument('-s', '--sampwidth', dest='sampwidth', default=2,
                           help='sample width')
    argparser.add_argument('--min', dest='min_frame', default=-20000,
                           help='min frame range')
    argparser.add_argument('--max', dest='max_frame', default=20000,
                           help='max frame range')

    return argparser.parse_args()

def create_random_bytes(nframes, min_frame, max_frame):
    random_bytes = []

    for _ in range(nframes):
        r = random.randrange(min_frame, max_frame)
        random_bytes.append(r)

    random_bytes = np.asarray(random_bytes, dtype=np.int16)
    return random_bytes


def main():
    args = get_args()
    wav_file = wave.open(args.output_file, 'wb')
    wav_file.setnchannels(args.nchannels)
    wav_file.setframerate(args.framerate)
    wav_file.setnframes(args.nframes)
    wav_file.setsampwidth(args.sampwidth)

    random_bytes = create_random_bytes(args.nframes, args.min_frame, args.max_frame)
    wav_file.writeframes(random_bytes)
    wav_file.close()

if __name__ == '__main__':
    main()
