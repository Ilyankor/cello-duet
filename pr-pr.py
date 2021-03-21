import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#import probability vectors
df = read_excel("master.xls", sheet_name="pr-p", header=None)
prp0 = df.to_numpy()
prp = prp0.flatten()

df = read_excel("master.xls", sheet_name="pr-r", header=None)
prr0 = df.to_numpy()
prr = prr0.flatten()

#define possible pitches/rhythms
pitches = ['D', 'E', 'F#', 'A', 'B']
rhythms = np.arange(1, 25)

#functions
outp = np.random.choice(pitches, 75, p=prp)
print(outp)

#function
outr = np.random.choice(rhythms, 75, p=prr)
print(outr)
