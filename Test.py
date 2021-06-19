# -----Read in .wav file
# Per the documentation, scipy.io.wavfile.read(somefile) returns a tuple of two items: the first is the sampling rate in samples per second, the second is a numpy array with all the data read from the file:

import matplotlib
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import glob
import sys
import os
from pydub import AudioSegment

import numpy as np

samplerate, data = wavfile.read('./vader.wav')
samplerate1, playeddata = wavfile.read('./forceisstrong.wav')
# audio segments

vader = AudioSegment.from_wav("./vader.wav")
swsong = AudioSegment.from_wav("./forceisstrong.wav")

samples = vader.get_array_of_samples()
samples1 = swsong.get_array_of_samples()

FFTsmaples = np.fft.fft(samples)
shifted = np.fft.fftshift(transformed)
fft_out = fft(vader)
fft_out2 = fft(shifted)
plt.plot(data, np.abs(vader))
plt.show()

#use samples n samples1 in 1st trial
'''
ly = AudioSegment.from_wav("vader.wav")

samples = ly.get_array_of_samples()
print(samples[1000:5000])

# Advanced usage, if you have raw audio data:
sound = AudioSegment(
    # raw audio data (bytes)
    data=b'…',

    # 2 byte (16 bit) samples
    sample_width=2,

    # 44.1 kHz frame rate
    frame_rate=44100,

    # stereo
    channels=2
)

# superposed audio
combined = swsong.overlay(vader)




class Frame():
    def __init__(self, buff_size):
        frame = [buff_size]


# -----Add to buffer
bufferSize = 1000
# frame buffer = frames.get(bufferSize)
# for each binary bit
# if binary bit == 1
# then addHighPowerHFT into frame buffer
# if binary bit == 0r
# then noHFTInjection into frame buffer

# frames = Read WaveFile(fileName)
# characters = Read Character Data()
# binary bits = Convert(Characters)
# foreach bit in binary bits
# add HFT(bit)
# output file = Write WaveFile


# ---------For each HF bit[1], add it to frame buffer
# frames = Read WaveFile(stegoFileName)
# fftData = FFT(frames)
# data = HighPass(fftData
# foreach buffer in data
# bits += get Bit(buffer)
# characters = Convert(bits)


# ----------Decode the encoded file
# Reversing the shift:
#print(np.all((np.fft.ifftshift(shifted) - transformed) < 10 ** -9))'''
