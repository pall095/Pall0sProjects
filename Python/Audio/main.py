import pyaudio
import struct
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data_int = struct.unpack( str(2 * CHUNK) + 'B', data )
    print( data_int )
    data_np = np.array( data_int , dtype = "i" )[ ::2 ]
    fft_data = np.fft.fft( data_np )
    freqs = np.fft.fftfreq( len( data_np ) , d = 1./RATE )





print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
