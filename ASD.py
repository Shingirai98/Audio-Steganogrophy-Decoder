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

        wav.write(filename="./audios/asd0-modulated_secret.wav", rate=self.rate1, data=self.modulated_d1)
        wav.write(filename="./audios/asd1-swsteganograph.wav", rate=self.rate, data=self.final)
        print(f"elapsed time for modulation: {t0} overlaying: {t1}")

    def decoder(self):
        rate, final = wav.read('./audios/asd1-swsteganograph.wav')  # 2CH L,R

        temp_time = time.time()
        self.filtered = hpf(final, rate)
        t0 = time.time() - temp_time

        temp_time = time.time()
        self.demodulated = am_demodulator(self.filtered)
        t1 = time.time() - temp_time

        print(f"Filtering time: {t0} demodulation: {t1}")
        wav.write(filename="./audios/asd2-filtered.wav", rate=self.rate, data=self.filtered)
        wav.write(filename="./audios/asd3-demodulated.wav", rate=self.rate, data=self.demodulated)

    def visualizer(self):
        #ENCODING
        plot1 = plt.figure(1)
        plt.title("Carrier audio")
        plt.plot(np.arange(self.data[:60000].size), self.data[:60000])
        plot2 = plt.figure(2)
        plt.title("Secret")
        plt.plot(np.arange(self.data1.size), self.data1)
        plot3 = plt.figure(3)
        plt.title("Modulated Secret")
        plt.plot(np.arange(self.modulated_d1[:60000].size), self.modulated_d1[:60000])  # plot only first 60K compare
        plot4 = plt.figure(4)
        plt.title("Stegonagraph")
        plt.plot(np.arange(self.final[:60000].size), self.final[:60000])  # plot only first 60K compare

        #DECODING
        plot5 = plt.figure(5)
        plt.title("Filtered")
        plt.plot(np.arange(self.filtered.size), self.filtered)
        plot6 = plt.figure(6)
        plt.title("Demodulated")
        plt.plot(np.arange(self.demodulated.size), self.demodulated)

        plot7 = plt.figure(7)
        plt.title("FFT")
        plt.plot( linspace(-self.rate/2, self.rate/2, 46102), np.abs(fft(self.carrier))*10)
        plt.plot( linspace(-self.rate/2, self.rate/2, 5801472), np.abs(fft(self.modulated_d1))*10)
        plt.plot( fftfreq(self.data1.shape[0]), np.abs(fft(self.data1)))
        # plt.legend = True
        # r0 = fft(data) #[:20000] parallelize?
        # r1 = fft(data1)
        # r1.resize(r0.shape)
        # r2 = np.abs(r0+r1)
        #plt.show()
        plots = [plot1,plot2,plot3,plot4,plot5,plot6,plot7]

        for i in range(7):
            #plot = plt.gcf()
            plots[i].set_size_inches(16, 9)
            plots[i].show()
            plots[i].savefig(f'ASD-{i}.png', dpi=100)


        # plt.subplot(3,1,1)
        # plt.title('Audio Steganography Process') #Amplitude Modulation
        # plt.plot( self.data ,'g')
        # plt.ylabel('Amplitude')
        # plt.xlabel('Carrier Audio')
        #
        # plt.subplot(3,1,2)
        # plt.plot(self.data1, 'r')
        # plt.ylabel('Amplitude')
        # plt.xlabel('Secret Message Signal')
        #
        # plt.subplot(3,1,3)
        # plt.plot(self.modulated_d1[:60000], color="purple")
        # plt.ylabel('Amplitude')
        # plt.xlabel('AM Secret Message signal')

        # plt.subplot(7,1,4)
        # plt.plot(self.final[:60000], color="purple")
        # plt.ylabel('Amplitude')
        # plt.xlabel('Steganography Audio (AM Secret+Carrier)')
        #
        # plt.subplot(7,1,5)
        # plt.plot(self.filtered, color="blue")
        # plt.ylabel('Amplitude')
        # plt.xlabel('HPF Filtered Steganography Audio')
        #
        # plt.subplot(7,1,6)
        # plt.plot(self.demodulated, color="yellow")
        # plt.ylabel('Amplitude')
        # plt.xlabel('Demodulated Secret Audio')

        # plt.subplots_adjust(hspace=1)
        # plt.rc('font', size=15)
        #
        # fig = plt.gcf()
        # fig.set_size_inches(16, 9)
        # #plt.show()
        # fig.savefig('Stego.png', dpi=100)


if __name__ == "__main__":
    asd = ASD()
    asd.encoder()
    asd.decoder()
    asd.visualizer()

