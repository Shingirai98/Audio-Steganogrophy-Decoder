import matplotlib.pyplot as plt
from numpy import linspace

from modem import modulate, demodulate, hpf, modulate_old, demodulate_old, am_modulator, am_demodulator, lpf
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
        self.carrier = None
        self.times = {"mod":[], "over":[], "filt":[], "demod":[] }
        pass

    def encoder(self):
        self.rate, self.data = wav.read('./audios/swthemesong.wav')  # 2CH L,R
        self.data = self.data.T[0]
        self.rate1, self.data1 = wav.read('./audios/vader.wav')  # 1CH

        temp_time = time.time()
        self.data = lpf(self.data, self.rate)
        self.data1 = lpf(self.data1, self.rate1)
        self.modulated_d1, self.carrier = am_modulator(self.data1)
        t0 = time.time() - temp_time

        self.modulated_d1.resize(self.data.shape)

        temp_time = time.time()
        self.final = self.data + self.modulated_d1
        t1 = time.time() - temp_time
        #print(f"elapsed time for modulation: {t0} overlaying: {t1}")
        self.times["mod"].append(t0)
        self.times["over"].append(t1)


    def encoder_writer(self):
        wav.write(filename="./audios/asd0-modulated_secret.wav", rate=self.rate1, data=self.modulated_d1)
        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=self.rate, data=self.final)

    def decoder(self):
        rate, final = wav.read('./audios/asd1-swsteganograph.wav')  # 2CH L,R

        temp_time = time.time()
        self.filtered = hpf(final, rate)
        t0 = time.time() - temp_time

        temp_time = time.time()
        self.demodulated = am_demodulator(self.filtered)
        t1 = time.time() - temp_time
        #print(f"Filtering time: {t0} demodulation: {t1}")
        self.times["filt"].append(t0)
        self.times["demod"].append(t1)


    def decoder_writer(self):
        wav.write(filename="./audios/asd2-filtered.wav", rate=self.rate, data=self.filtered)
        wav.write(filename="./audios/asd3-demodulated.wav", rate=self.rate, data=self.demodulated)

    def visualizer(self):
        # ENCODING
        plot1 = plt.figure(1)
        plt.title("Carrier audio")
        plt.plot(np.arange(self.data.size), self.data)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        plot2 = plt.figure(2)
        plt.title("Secret Message Signal")
        plt.plot(np.arange(self.data1.size), self.data1)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        plot3 = plt.figure(3)
        plt.title("AM Secret Message signal")
        plt.plot(np.arange(self.modulated_d1[:60000].size), self.modulated_d1[:60000])  # plot only first 60K compare
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        plot4 = plt.figure(4)
        plt.title("Steganography Audio (Secret+Carrier)")
        plt.plot(np.arange(self.final[:60000].size), self.final[:60000])  # plot only first 60K compare
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        # DECODING
        plot5 = plt.figure(5)
        plt.title("HPF Filtered Steganography Audio")
        plt.plot(np.arange(self.filtered.size), self.filtered)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        plot6 = plt.figure(6)
        plt.title("Demodulated Secret Audio")
        plt.plot(np.arange(self.demodulated.size), self.demodulated)
        plt.ylabel('Amplitude')
        plt.xlabel('Time')

        plot7 = plt.figure(7)
        plt.title("FFT Analysis")
        plt.plot(linspace(-self.rate / 2, self.rate / 2, 46102), np.abs(fft(self.carrier)) * 10, color="purple")
        plt.plot(linspace(-self.rate / 2, self.rate / 2, 5801472), np.abs(fft(self.modulated_d1)) * 10, color="red")
        plt.plot(fftfreq(self.data1.shape[0]), np.abs(fft(self.data1)))
        plt.ylabel('Magnitude')
        plt.xlabel('Frequency')
        plots = [plot1, plot2, plot3, plot4, plot5, plot6, plot7]

        for i in range(7):
            plots[i].set_size_inches(16, 9)
            #plots[i].show()
            plt.rc('font', size=35)
            plots[i].savefig(f'./images/ASD-{i + 1}.png', dpi=100)


if __name__ == "__main__":
    asd = ASD()
    for i in range(10):
        asd.encoder()
    asd.encoder_writer()
    for i in range(10):
        asd.decoder()
    asd.decoder_writer()
    asd.visualizer()
    print(asd.times)

