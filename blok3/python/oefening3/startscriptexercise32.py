from IPython import get_ipython
# get_ipython().magic('reset -sf')

import numpy as np 							# for 'numerical' data, you must have numpy installed				   
import matplotlib.pyplot as plt 			# only needed if you want to plot stuff

# read data from test1.txtfname   = '/test1.txt'
fname   = 'test1.txt'
mydat   = np.loadtxt(fname)
trialnr = np.array(mydat[:,0], dtype=int)      # array containing trialnumbers
stim    = np.array(mydat[:,1], dtype=int)      # array containing 1 for target present trial, 0 for target absent trial
resp    = np.array(mydat[:,2], dtype=int)      # array containing 1 for target present response, 0 for target absent response
rt      = np.array(mydat[:,3], dtype=int)      # array containing reaction times per trial