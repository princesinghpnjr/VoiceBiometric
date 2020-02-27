import numpy as np

import matplotlib.pyplot as plot

 

# Create sine wave1

time        = np.arange(0, 100, 0.1)

sinewave1   = np.sin(time)

 

# Create sine wave2 as replica of sine wave1

time1        = np.arange(0, 100, 0.1)

sinewave2    = np.sin(time1)

 

# Plot the sine waves - subplot 1

plot.title('Two sine waves with coherence as 1')

plot.subplot(211)

plot.grid(True, which='both')

plot.xlabel('time')

plot.ylabel('amplitude')

plot.plot(time, sinewave1, time1, sinewave2)

 

# Plot the coherence - subplot 2

plot.subplot(212)

coh, f = plot.cohere(sinewave1, sinewave2, 256, 1./.01)

print("Coherence between two signals:")

print(coh)

print("Frequncies of the coherence vector:")

print(f)

plot.ylabel('coherence')

plot.show()
