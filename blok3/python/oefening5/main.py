import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os  # for walking through folders
import fnmatch  # for matching filenames
from sklearn import preprocessing
import statistics as stat

datafold = "phyphox"

matches = []
SMV = []
times = []

# walk through folders
for root, dirnames, filenames in os.walk(datafold):
    for filename in fnmatch.filter(filenames, "*.csv"):
        matches.append(os.path.join(root, filename))

for a in range(len(matches)):
    # load file
    data = np.loadtxt(matches[a], delimiter=",", skiprows=1)
    data_normalizedX = np.square(preprocessing.normalize([data[:, 1]]))
    data_normalizedY = np.square(preprocessing.normalize([data[:, 2]]))
    data_normalizedZ = np.square(preprocessing.normalize([data[:, 3]]))
    SMV.append(np.sqrt(data_normalizedX + data_normalizedY + data_normalizedZ))
    # print(data)
    times.append(data[:, 0])

mean20SMVarray = []
standardeviation = []
steps = np.arange(0, len(SMV[0][0]), 20)
currentMean = 0
for i in range(0, len(SMV[0][0])):
    if i == 0:
        currentMean = np.mean(SMV[0][0][i:i + 20])
        mean20SMVarray.append(currentMean)
        standardeviation.append(np.std(SMV[0][0][i:i + 20]))
    elif i not in steps:
        mean20SMVarray.append(mean20SMVarray[-1])
        standardeviation.append(standardeviation[-1])
    else:
        currentMean = np.mean(SMV[0][0][i:i + 20])
        mean20SMVarray.append(currentMean)
        standardeviation.append(np.std(SMV[0][0][i:i + 20]))


print(SMV)

minimum = [min(mean20SMVarray)] * len(times[0])
maximum = [max(mean20SMVarray)] * len(times[0])
meanMinMax = [(min(mean20SMVarray) + max(mean20SMVarray)) / 2] * len(times[0])

seconds = 0
walking = []
shuffling = []
for x in range(0, len(mean20SMVarray)):
    if x > ((min(mean20SMVarray) + max(mean20SMVarray)) / 2):
        seconds += 1
    elif x > ((min(mean20SMVarray) + max(mean20SMVarray)) / 2) and seconds == 3:
        walking = 1

plt.figure(figsize=(20, 10))
plt.plot(times[0], mean20SMVarray)
# plt.plot(times[0], standardeviation)
plt.scatter(times[0], meanMinMax, linestyle='--')
plt.scatter(times[0], minimum, linestyle='--')
plt.scatter(times[0], maximum, linestyle='--')
plt.tight_layout()
# plt.fill_between(times[0], mean20SMVarray)

plt.show()
