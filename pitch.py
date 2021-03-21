import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#import probability vector
df = read_excel("master.xls", sheet_name="pitch", header=None)
pr0 = df.to_numpy()
pr = pr0.flatten()

#define possible pitches
pitches = ['Bb', 'C', 'D', 'F', 'G']

#function
out = np.random.choice(pitches, 75, p=pr)
print(out)
