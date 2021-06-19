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

        plot1 = plt.figure(1)
        plt.title("Carrier audio")
        plt.plot(np.arange(data.size), data)
        plot2 = plt.figure(2)
        plt.title("Secret")
        plt.plot(np.arange(data1.size), data1)
        plot3 = plt.figure(3)
        plt.title("Modulated Secret")
        plt.plot(np.arange(modulated_d1[:60000].size), modulated_d1[:60000]) #plot only first 60K compare
        plot4 = plt.figure(4)
        plt.title("Stegonagraph")
        plt.plot(np.arange(final[:60000].size), final[:60000]) #plot only first 60K compare
        plt.show()

        wav.write(filename="./audios/asd0-modulated_secret.wav", rate=rate1, data=modulated_d1)
        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=rate, data=final)
        print(f"elapsed time for modulation: {t0} overlaying: {t1}")


    def decoder(self):
        rate, final = wav.read('./audios/asd1-swsteganograph.wav')  # 2CH L,R

        temp_time = time.time()
        filtered = hpf(final, rate)
        t0 = time.time() - temp_time

        temp_time = time.time()
        demodulated = demodulate_old(filtered, rate)
        t1 = time.time() - temp_time

        plot1 = plt.figure(1)
        plt.title("Filtered")
        plt.plot(np.arange(filtered.size), filtered)
        plot2 = plt.figure(2)
        plt.title("Demodulated")
        plt.plot(np.arange(demodulated.size), demodulated)
        plt.show()

        print(f"Filtering time: {t0} demodulation: {t1}")
        wav.write(filename="./audios/asd2-filtered.wav", rate=rate, data=filtered)
        wav.write(filename="./audios/asd3-demodulated.wav", rate=rate, data=demodulated)


if __name__ == "__main__":
    asd = ASD()
    asd.encoder()
    asd.decoder()
