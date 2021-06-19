import matplotlib.pyplot as plt
from modem import modulate, demodulate, hpf, modulate_old, demodulate_old
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np
import time


class ASD:
    def __init__(self):
        pass

    def encoder(self):
        rate, data = wav.read('./audios/swthemesong.wav')  # 2CH L,R
        data = data.T[0]
        rate1, data1 = wav.read('./audios/vader.wav')  # 1CH

        temp_time = time.time()
        modulated_d1 = modulate_old(data1, rate1)
        t0 = time.time() - temp_time

        modulated_d1.resize(data.shape)

        temp_time = time.time()
        final = data + modulated_d1
        t1 = time.time() - temp_time

        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=rate, data=final)
        print(f"elapsed time for modulation: {t0} overlaying: {t1}")


    def decoder(self):
        rate, final = wav.read('./audios/asd1-swsteganograph.wav')  # 2CH L,R

        filtered = HPF(final, rate)
        demodulated = demodulate(filtered, rate)
        wav.write(filename="./audios/asd2-demodulated.wav", rate=rate, data=demodulated)


if __name__ == "__main__":
    asd = ASD()
    asd.encoder()
    asd.decoder()
