import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np
from scipy import signal

def modulate(data, sample_rate):

    modulator_frequency = sample_rate
    carrier_frequency = 21000.0
    modulation_index = 1.0

    time = np.arange(sample_rate) / sample_rate
    modulator = data #np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
    carrier = np.sin(2.0 * np.pi * carrier_frequency * time)
    product = np.zeros_like(modulator)

    for i, t in enumerate(time):
        product[i] = np.sin(2. * np.pi * (carrier_frequency * t + modulator[i]))

    return product

def modulate_old(data, sample_rate=44100):

    # Duration
    #duration_s = 5.0 #******

    #from scipy.io import wavfile
    #Fs, data = wav.read('filename.wav')
    #n = data.size
    #t = n / Fs

    # ac: amplitude of the carrier. Should be kept at 1.0 in this script
    # you would modify it if you were micing it with, or modulating other,
    # waveforms.

    # carrier_hz: Frequency of the carrier
    # fm_hz: Frequency of the frequency modulator
    # k_p: deviation constant
    carrier_hz = 21000#440.0 #carrier.
    fm_hz = 220.0 #data signal freq #********** incoming rate
    k = 25.0

    # Our final waveform is going to be calculated as the cosine of carrier and
    # frequency modulated terms.

    # First, define our range of sample numbers
    each_sample_number = np.arange(data.shape[0]) #**********

    # Create the term that create the carrier
    carrier = 2 * np.pi * each_sample_number * carrier_hz / sample_rate

    # Now create the term that is the frequency modulator
    modulator = data#k * np.sin(2 * np.pi * each_sample_number * fm_hz / sample_rate)

    # Now create the modulated waveform, and attenuate it
    waveform = np.cos(carrier + modulator)
    waveform_quiet = waveform * 0.3

    # Adjust amplitude of waveform and write the .wav file.
    waveform_integers = np.int16(waveform_quiet * 32767 *0.01) #***************
    #write('fm-out.wav', sps, waveform_integers)
    return waveform_integers


def demodulate_old(data, sample_rate=44100):

    # Duration
    #duration_s = 5.0 #******

    #Fs, data = wav.read('filename.wav')
    #n = data.size
    #t = n / Fs

    # carrier_hz: Frequency of the carrier
    # fm_hz: Frequency of the frequency modulator
    # k_p: deviation constant
    carrier_hz = 21000#440.0 #carrier.
    fm_hz = 220.0 #data signal freq #********** incoming rate
    k = 25.0

    # Our final waveform is going to be calculated as the cosine of carrier and
    # frequency modulated terms.

    # First, define our range of sample numbers
    each_sample_number = np.arange(data.shape[0]) #**********

    # Create the term that create the carrier
    carrier = 2 * np.pi * each_sample_number * carrier_hz / sample_rate

    # Now create the term that is the frequency modulator
    demodulator = data#k * np.sin(2 * np.pi * each_sample_number * fm_hz / sample_rate)

    # Now create the modulated waveform, and attenuate it
    waveform = np.cos(demodulator - carrier)
    waveform_quiet = waveform * 0.3

    # Adjust amplitude of waveform and write the .wav file.
    waveform_integers = np.int16(waveform_quiet * 32767 *20) #***************
    #write('fm-out.wav', sps, waveform_integers)
    return waveform_integers


def demodulate(data, sample_rate):

    modulator_frequency = sample_rate
    carrier_frequency = 21000.0
    modulation_index = 1.0

    time = np.arange(sample_rate) / sample_rate
    modulator = data #np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
    carrier = np.sin(2.0 * np.pi * carrier_frequency * time)
    quotient = np.zeros_like(modulator)

    for i, t in enumerate(time):
        quotient[i] = np.sin(2. * np.pi * (modulator[i] - carrier_frequency * t ))

    return quotient*200

def HPF(data, rate):
    t = np.arange(data.size)
    sos = signal.butter(10, 11020, 'hp', fs=rate, output='sos')
    filtered = signal.sosfilt(sos, data)

    return filtered.astype(data.dtype)
