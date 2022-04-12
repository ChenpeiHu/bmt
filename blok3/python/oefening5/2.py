import numpy as np
import matplotlib.pyplot as plt
import os  # for walking through folders
import fnmatch  # for matching filenames

datafold = "accelero"
outfold = "Processed"
matches = []
times = []
outfiles = []

# lopen door mappen
for root, dirnames, filenames in os.walk(datafold):
    for filename in fnmatch.filter(filenames, "*.txt"):
        matches.append(os.path.join(root, filename))
        outfiles.append(os.path.join(outfold, root[len(datafold) + 1:], filename))
        # verkrijg output folder structuur
        structure = os.path.join(outfold, root[len(datafold) + 1:])
        # maak mapje als die nog niet bestaat
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            print("Folder does already exist!")

data_X = []

#data inladen
for a in range(len(matches)):
    data = np.loadtxt(matches[a], delimiter="\t", skiprows=1)
    data_X.append(data[:, 1])
    times.append(data[:, 0])

#SMV berekenen
data_Xaxis = data_X[0]
SMV = np.sqrt(np.square(data_Xaxis))  # SMV

rawdata = SMV
window_size = 50
meanarray = []

#sliding average berekenen
for i in range(0, len(rawdata)):
    currentmean = np.mean(rawdata[i:i + window_size])
    meanarray.append(currentmean)

max_stilstaan = np.max(meanarray[0:300]) #grenswaarde bepalen maximaal stilstaan
print("maximale grenswaarde stilstaan: " + str(max_stilstaan))

max_schuifelen = np.max(meanarray[0:1000]) #grenswaarde bepalen maximaal schuifelen
print("maximale grenswaarde schuifelen: " + str(max_schuifelen))

# beweging bepalen doormiddel van boolean logica
kleiner_dan_max_stilstaan = meanarray <= max_stilstaan
kleiner_dan_max_schuifelen = (meanarray <= max_schuifelen) & (meanarray > max_stilstaan)
groter_dan_max_schuifelen = meanarray > max_schuifelen

# nieuw bestand maken met extra kolom met beweging
moveData = []
actie = []

for i in range(0, len(rawdata)):
    #bewegingsdata verkrijgen
    if i < 1:
        moveData = np.loadtxt(matches[i], delimiter="\t", skiprows=1)

    #array vullen met bewegingen
    if kleiner_dan_max_stilstaan[i]:
        actie.append("stilstaan")
    elif kleiner_dan_max_schuifelen[i]:
        actie.append("schuifelen")
    else:
        actie.append("lopen")

#Nieuw bestand maken met extra kolom welke beweging word uitgevoerd
moveData = np.c_[moveData, actie]
np.savetxt(outfiles[0], moveData, "%s", delimiter=",", header="Time (s),X (m/s^2),Y (m/s^2),Z (m/s^2),Beweging",
           comments="")

#sliding average plotten
plt.plot(times[0], meanarray)
plt.ylabel("Signaal")
plt.xlabel("Tijd in seconden")
plt.title("Sliding Average")
plt.show()

# resultaten plotten
f, (ax1, ax2, ax3) = plt.subplots(3, 1)

#stilstaan
ax1.plot(times[0], meanarray, color='orange')
ax1.plot(times[0], kleiner_dan_max_stilstaan, color='red')
ax1.set_title('stilstaan')
ax1.set_xlabel('Tijd in seconden')
ax1.set_ylabel('Signaal')

#schuifelen
ax2.plot(times[0], meanarray, color='orange')
ax2.plot(times[0], kleiner_dan_max_schuifelen, color='blue')
ax2.set_title('schuifelen')
ax2.set_xlabel('Tijd in seconden')
ax2.set_ylabel('Signaal')

#lopen
ax3.plot(times[0], meanarray, color='orange')
ax3.plot(times[0], groter_dan_max_schuifelen, color='green')
ax3.set_title('lopen')
ax3.set_xlabel('Tijd in seconden')
ax3.set_ylabel('Signaal')
#grafiek opslaan als png in de outfold directory
plt.savefig(outfold + '/' + filename + '.png')

#grafiek mooier maken
plt.tight_layout()

#grafiek laten zien
plt.show()
