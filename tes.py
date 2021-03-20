import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

df = read_excel("master.xls", sheet_name="m-tr1", header=None)
tr = df.to_numpy()

v = np.random.rand(24)
v0 = v/np.sum(v)

transform = np.arange(24)

for i in range(1, 15):
    out = np.random.choice(transform, 1, p=np.dot(matrix_power(tr, i), v0))
    print(out)
