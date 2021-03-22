import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#import transition matrix
df = read_excel("master.xls", sheet_name="m-tr1", header=None)
tr = df.to_numpy()

#create initial vector
v0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#create 24 options for T, TnI
transform = np.arange(24)

#function
for i in range(1, 15):
    out = np.random.choice(transform, 1, p=np.dot(matrix_power(tr, i), v0))
    print(out)
