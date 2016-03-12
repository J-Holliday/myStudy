import numpy as np
import struct

# define header
RIFF_HEADER = b"\x52\x49\x46\x46"   # "RIFF"
FILE_SIZE = b"\xAC\x88\15\00"       # tekitou
WAVE_HEADER = b"\x57\x41\x56\x45"   # "WAVE"
WAVE_FORMAT = b"\x66\x6D\x74\x20"   # "fmt "
FORMAT_SIZE = b"\x10\x00\x00\x00"   # 16
FORMAT_ID = b"\x01\x00"             # linearPCM
CHUNNELS = b"\x01\x00"              # mono
SAMPLING_RATE = b"\x44\xAC\x00\x00" # 44100
BYTES_PER_SEC = b"\x88\x58\x01\x00" # 44100 * 2(16bit) * 1(mono)
BLOCK_SIZE = b"\x02\x00"            # 2(16bit) * 1(mono)
SIGNIFICANT = b"\x10\x00"           # 16bit
DATA_HEADER = b"\x64\x61\x74\x61"   # "data"
DATA_SIZE = b"\xAC\x88\x15\x00"     # tekitou

HEADER = RIFF_HEADER + FILE_SIZE + WAVE_HEADER + WAVE_FORMAT + FORMAT_SIZE + FORMAT_ID + CHUNNELS + SAMPLING_RATE + BYTES_PER_SEC + BLOCK_SIZE + SIGNIFICANT + DATA_HEADER + DATA_SIZE

# make wave
A = 32767.0
fs = 44100
f0 = np.array([262, 294, 330, 349, 392, 440, 494, 523])
f1 = f0/2
f2 = f0/4
wave = []
sop = [0, 0, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 0, 0]
bas = [0, 0, 2, 0, 3, 0, 2, 0, 1, 1, 0, 0, 4, 4, 0, 0]

for i in range(len(sop)):
  for n in range(fs):
    fa = A/2*np.sin(2*np.pi*2*f0[sop[i]]*n/fs)
    fb = A/2*np.sin(2*np.pi*2*f1[bas[i]]*n/fs)
    wave.append(int(fa+fb))

# convert wave to binary data
binary =  struct.pack("h" * len(wave), *wave)

# output file
res = HEADER + binary
f = open("output_twincleStar.wav", "wb")
f.write(res)
f.close()
