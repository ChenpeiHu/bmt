# import relevant packages
import os  # for walking through folders
import fnmatch  # for matching filenames
import numpy as np  # for loading data files

datafold = "Important_Experiment_nr2"
outfold = "Important_Experiment_nr2_Better_Than_Before"

outfiles = []
matches = []

# walk through folders
for root, dirnames, filenames in os.walk(datafold):
    # print(root)
    # print(filenames)
    # check whether the files is a text file
    for filename in fnmatch.filter(filenames, "*.txt"):
        matches.append(os.path.join(root, filename))
        outfiles.append(os.path.join(outfold, root[len(datafold) + 1:], filename))

    # get output folder structure
    structure = os.path.join(outfold, root[len(datafold) + 1:])
    # make folder if it does not exist
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder does already exist!")

for a in range(len(matches)):
    # load file
    data = np.loadtxt(matches[a], delimiter="\t", skiprows=1)
    correct = data[:, 0] == data[:, 1]
    print(correct)
    # print(data)
    # print(correct)
    # add column to data matrix
    data = np.c_[data, correct]
    print(np.mean(data[:, 3]))
    # save file
    np.savetxt(outfiles[a], data, "%i", delimiter="\t", header="Target\tResponse\tRRT\tCorrect", comments="")
