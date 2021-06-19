import matplotlib.pyplot as plt
from scipy import signal
from modem import modulate, demodulate, HPF
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np


class ASD:
    def __init__(self):
        pass

    def encoder(self):
        rate, data = wav.read('./audios/swthemesong.wav')  # 2CH L,R
        data = data.T[0]
        rate1, data1 = wav.read('./audios/.wav')  # 1CH

        modulated_d1 = modulate(data1, rate1)
        modulated_d1.resize(data.shape)
        final = data + modulated_d1

        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=rate, data=final)

    def decoder(self):
        rate, final = wav.read('./audios/swsteganograph.wav')  # 2CH L,R

        filtered = HPF(final, rate)
        demodulated = demodulate(filtered, rate)
        wav.write(filename="./audios/filtered.wav", rate=rate, data=demodulated)


if __name__ == "__main__":
    asd = ASD()
    asd.encoder()
    asd.decoder()
