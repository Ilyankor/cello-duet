import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#import transition matrix
df = read_excel("master.xls", sheet_name="m-tr4", header=None)
tr = df.to_numpy()

#define initial vectors
V = np.random.rand(16)
v0 = V/np.sum(V)

#choices for rhythms
rhythms = [1, 2, 3, 5, 6, 9, 12, 13, 15, 16, 18, 19, 20, 21, 23, 24]

#function
for i in range(0, 75):
    out = np.random.choice(rhythms, 1, p=np.dot(matrix_power(tr, i), v0))
    print(out)
