import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#import probability vector
df = read_excel("master.xls", sheet_name="rhythm", header=None)
pr0 = df.to_numpy()
pr = pr0.flatten()

#define possible rhythms
rhythms = np.arange(1, 25)

#function
out = np.random.choice(rhythms, 75, p=pr)
print(out)
