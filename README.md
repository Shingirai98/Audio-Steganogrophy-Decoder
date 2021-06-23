# Audio-Steganogrophy-Decoder

## How to run

prerequisites: <br>
1. python >=3.8.5 <br>
2. sudo apt-get install python3-venv <br>

```commandline

$ git clone [url]
$ cd Audio-Steganogrophy-Decoder
$ make
$ make run
```

Check for output in audios folder.

# Files

##[ASD.py](ASD.py)

- Contains the main Audio Steganography Encoder / Decoder class.

###Methods:

1. Constructor - initializes the ASD object.
2. encoder - encodes the secret audio into the carrier audio.
3. encode_writer - writes out the encoded wav files
4. decoder - decodes the encoded stego audio
5. decoder_writer - writes out the decoded wav file
6. visualizer - plots graphs of interest.

##[modem.py](modem.py)

1. modulate - newer reference frequency modulator
2. modulate_old - old erroneous frequency modulator
3. demodulate - newer reference frequency demodulator
4. demodulate_old - old erroneous frequency demodulator
5. am_modulator - amplitude modulator (used in project)
6. am_demodulator - amplitude demodulator (used in project)
7. hpf - high pass filter (used in project)
8. lpf - low pass  (used in project)

## Images Folder
Images are well labelled and are self-explanatory. Exported from the program output.

##Audios Folder
Source audios and program output audios prefixed by "asd-x" in the order of generation.
