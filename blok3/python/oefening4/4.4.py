# import relevant packages
import os  # for walking through folders
import fnmatch  # for matching filenames
import numpy as np  # for loading data files
import matplotlib.pyplot as plt

datafold = "Important_Experiment_nr2_Better_Than_Before"

matches = []

# walk through folders
for root, dirnames, filenames in os.walk(datafold):
    # print(root)
    # print(filenames)
    # check whether the files is a text file
    for filename in fnmatch.filter(filenames, "*.txt"):
        matches.append(os.path.join(root, filename))

correctResponses = []
average_rt = []

for a in range(len(matches)):
    # load file
    data = np.loadtxt(matches[a], delimiter="\t", skiprows=1)
    correct = data[:, 0] == data[:, 1]
    print(data)
    correctResponses.append(np.sum(correct))
    average_rt.append(np.mean(data[:, 2]))

print(average_rt)

plt.scatter(correctResponses, average_rt)
plt.show()
