import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os  # for walking through folders
import fnmatch  # for matching filenames
from sklearn import preprocessing
import statistics as stat

datafold = "accelero"

matches = []
times = []

# walk through folders
for root, dirnames, filenames in os.walk(datafold):
    for filename in fnmatch.filter(filenames, "*.txt"):
        matches.append(os.path.join(root, filename))
print(matches)
data_X = []

for a in range(len(matches)):
    data = np.loadtxt(matches[a], delimiter="\t", skiprows=1)
    data_X.append(data[:, 1])
    times.append(data[:, 0])

# print(data_X)

letterx = data_X[0]
SMV = (letterx ** 2) ** (1 / 2)  # SMV

rawdata = SMV
# print(len(rawdata))
window_size = 50
meanarray = []
for i in range(0, len(rawdata) - window_size + 1):
    currentmean = np.mean(rawdata[i:i + window_size])
    meanarray.append(currentmean)

max_stilstaan = np.max(meanarray[0:300])
print("grenswaarde stilstaan: " + str(max_stilstaan))

max_schuifelen = np.max(meanarray[0:1000])
print(str(max_schuifelen))

kleiner_dan_max_stilstaan = meanarray <= max_stilstaan
kleiner_dan_max_schuifelen = (meanarray <= max_schuifelen) & (meanarray > max_stilstaan)
groter_dan_max_schuifelen = meanarray > max_schuifelen

# plt.plot(abs(data_X[0]))
plt.subplot(3, 1, 1)
plt.title('stilstaan')
plt.plot(meanarray, color='orange')
plt.plot(kleiner_dan_max_stilstaan, color='red')
plt.subplot(3, 1, 2)
plt.title('schuifelen')
plt.plot(meanarray, color='orange')
plt.plot(kleiner_dan_max_schuifelen, color='blue')
plt.subplot(3, 1, 3)
plt.title('lopen')
plt.plot(meanarray, color='orange')
plt.plot(groter_dan_max_schuifelen, color='green')
plt.tight_layout()
plt.show()
