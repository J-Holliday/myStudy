import numpy as np
import matplotlib.pyplot as mlp

A = 32767.0     # level
fs = 44100      # sampling rate
f0 = 262        # do of do-re-mi
wave = []

for n in range(fs):
  f = A * np.sin(2 * np.pi * f0 * n / fs)
  wave.append(f)

mlp.plot(wave)
mlp.show()
