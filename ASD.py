import matplotlib.pyplot as plt
from modem import modulate, demodulate, hpf, modulate_old, demodulate_old
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np
import time


class ASD:
    def __init__(self):
        self.rate = self.rate1 = None
        self.data = self.data1 = None
        self.modulated_d1 = self.final = None
        self.filtered = self.demodulated = None
        pass

    def encoder(self):
        self.rate, self.data = wav.read('./audios/swthemesong.wav')  # 2CH L,R
        self.data = self.data.T[0]
        self.rate1, self.data1 = wav.read('./audios/vader.wav')  # 1CH

        temp_time = time.time()
        self.modulated_d1 = modulate_old(self.data1, self.rate1)
        t0 = time.time() - temp_time

        self.modulated_d1.resize(self.data.shape)

        temp_time = time.time()
        self.final = self.data + self.modulated_d1
        t1 = time.time() - temp_time

        wav.write(filename="./audios/asd0-modulated_secret.wav", rate=self.rate1, data=self.modulated_d1)
        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=self.rate, data=self.final)
        print(f"elapsed time for modulation: {t0} overlaying: {t1}")

    def decoder(self):
        rate, final = wav.read('./audios/asd1-swsteganograph.wav')  # 2CH L,R

        temp_time = time.time()
        self.filtered = hpf(final, rate)
        t0 = time.time() - temp_time

        temp_time = time.time()
        self.demodulated = demodulate_old(self.filtered, rate)
        t1 = time.time() - temp_time

        print(f"Filtering time: {t0} demodulation: {t1}")
        wav.write(filename="./audios/asd2-filtered.wav", rate=rate, data=filtered)
        wav.write(filename="./audios/asd3-demodulated.wav", rate=rate, data=demodulated)


if __name__ == "__main__":
    asd = ASD()
    asd.encoder()
    asd.decoder()
