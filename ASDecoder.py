import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile as wav
import numpy as np

def HPF(data, rate):
    t = np.arange(data.size)
    sig=data
    plot1 = plt.figure(1)
    plt.plot([i for i in range(data[2000:2100].size)], data[2000:2100])

    #Design a digital high-pass filter at 15 Hz to remove the 10 Hz tone, and apply it to the signal. (It’s recommended to use second-order sections format when filtering, to avoid numerical error with transfer function (ba) format):

    sos = signal.butter(10, 11020, 'hp', fs=rate, output='sos')
    filtered = signal.sosfilt(sos, sig)

    plt.show()
    return filtered.astype(data.dtype)

#filtered = HPF(final,sample)
#wav.write(filename="./filtered.wav", rate=sample, data=filtered)
