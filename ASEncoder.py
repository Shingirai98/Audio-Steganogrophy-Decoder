'''Attempt 3 workin - resize after fft'''

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import rfft, irfft, fft, ifft, fftfreq
import numpy as np

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
