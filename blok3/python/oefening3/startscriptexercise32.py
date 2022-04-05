import numpy as np  # for 'numerical' data, you must have numpy installed
import matplotlib.pyplot as plt  # only needed if you want to plot stuff

# read data from test1.txtfname   = '/test1.txt'
fname = 'test1.txt'
mydat = np.loadtxt(fname)
trialnr = np.array(mydat[:, 0], dtype=int)  # array containing trialnumbers
stim = np.array(mydat[:, 1], dtype=int)  # array containing 1 for target present trial, 0 for target absent trial
resp = np.array(mydat[:, 2], dtype=int)  # array containing 1 for target present response, 0 for target absent response
rt = np.array(mydat[:, 3], dtype=int)  # array containing reaction times per trial

correct_answers = stim == resp
print("\n" + str(correct_answers.sum()) + " correcte antwoorden")

correct_answers_geen_doel = (stim == resp) & (stim == 0)
print(str(correct_answers_geen_doel.sum()) + " correcte antwoorden zonder doel")

correct_answers_met_doel = (stim == resp) & (stim == 1)
print(str(correct_answers_met_doel.sum()) + " correcte antwoorden met doel")

valse_alarm = (stim == 0) & (resp == 1)
print(str(valse_alarm.sum()) + " valse alarmen")

missers = (stim == 1) & (resp == 0)
print(str(missers.sum()) + " missers")

totaal = correct_answers_geen_doel.sum() + correct_answers_met_doel.sum() + valse_alarm.sum() + missers.sum()
print(str(totaal) + " totaal")
# gemiddelde reactie tijd bij juiste proeven en de standaardafwijking ervan
print("gemiddelde reactietijd: " + str(np.mean(rt[correct_answers])) + " en standaard deviatie: " + str(np.std(rt[correct_answers])) + " van correcte antwoorden")

# incorrecte proeven, gemiddelden en standaardafwijkingen
incorrect_answers = stim != resp
print("gemiddelde reactietijd: " + str(np.mean(rt[incorrect_answers])) + " en standaard deviatie: " + str(np.std(rt[incorrect_answers])) + " van incorrecte antwoorden")

proeven_met_doelwit = stim == 1
print("gemiddelde reactietijd: " + str(np.mean(rt[proeven_met_doelwit])) + " en standaard deviatie: " + str(np.std(rt[proeven_met_doelwit])) + " van proeven met doelwit")

proeven_zonder_doelwit = stim == 0
print("gemiddelde reactietijd: " + str(np.mean(rt[proeven_zonder_doelwit])) + " en standaard deviatie: " + str(np.std(rt[proeven_zonder_doelwit])) + " van proeven zonder doelwit")

labels = ["correct", "incorrect", "met doelwit", "zonder doelwit"]
x_pos = np.arange(len(labels))
proeven = [np.mean(rt[correct_answers]), np.mean(rt[incorrect_answers]), np.mean(rt[proeven_met_doelwit]), np.mean(rt[proeven_zonder_doelwit])]
error = [np.std(rt[correct_answers]), np.std(rt[incorrect_answers]), np.std(rt[proeven_met_doelwit]), np.std(rt[proeven_zonder_doelwit])]

fig, ax = plt.subplots()
ax.bar(x_pos, proeven, yerr=error, align='center', alpha=0.8, ecolor='black', capsize=10)
ax.set_ylabel('reactie tijd')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)
plt.title("reactie tijden")
plt.tight_layout()
plt.show()
