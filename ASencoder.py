def main():
    import matplotlib.pyplot as plt
    from scipy.io import wavfile as wav
    from scipy.fftpack import fft
    import numpy as np
    #rate, data = wav.read('./forceisstrong.wav')
    rate, data = wav.read('./swthemesong.wav')
    fft_out = fft(data)
    plt.plot(data, np.abs(fft_out))
    plt.show()
main()
