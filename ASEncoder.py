'''Attempt 3 workin - resize after fft'''

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np

def modulate(data, sample_rate=44100):

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


def main():

    #rate, data = wav.read('./forceisstrong.wav')
    rate, data = wav.read('./swthemesong.wav') #2CH L,R
    data = data.T[0]
    rate1, data1 = wav.read('./vader.wav') #1CH
    #cant process whole file - buffer issues
    '''
    #rfft losing out some energy with complex elements.
    fft_out = rfft(data) #[:20000] parallelize?
    fft_out1 = rfft(data1)    
    
    ifft_out = irfft(fft_out).flatten().astype(data.dtype)
    ifft_out1 = irfft(fft_out1).flatten().astype(data1.dtype)
    
    #b is higher dimension, then:
    #a.resize(b.shape)
    #c = a+b
    #chack which size is larger. - carrier gotta b larger.
    
    ifft_out1.resize(ifft_out.shape)  
    
    
    
    final = ifft_out + ifft_out1 #np.add(fft_out, fft_out1) # or just +
    sub = final - ifft_out
    sub = np.trim_zeros(sub, trim='b')
    

    #output = irfft(final).astype(int)
    #testout = irfft(fft_out1)        
    
    final = ifft_out + ifft_out1 #np.add(fft_out, fft_out1) # or just +
    '''
    #data1.resize(data.shape)
    modulated_d1 = modulate(data1, rate1)
    modulated_d1.resize(data.shape)
    final = data + modulated_d1
    wav.write(filename="./mod1.wav", rate=rate, data=final)#data[:,1])


main()