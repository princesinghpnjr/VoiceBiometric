from scipy.io.wavfile import read
import matplotlib.pyplot as plt

input_data = read("1313.wav")
audio = input_data[1]

plt.plot(audio[0:1024])

plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

plt.title("smaple 1")

plt.show()
