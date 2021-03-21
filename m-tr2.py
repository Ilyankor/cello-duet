import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power
from random import randint

#import transition matrix
df = read_excel("master.xls", sheet_name="m-tr2", header=None)
tr = df.to_numpy()

#choices for initial pc set
v0n = randint(1, 4)

if v0n == 1:
    v0 = [1, 0, 0, 0, 0, 0, 0, 0]
elif v0n == 2:
    v0 = [0, 1, 0, 0, 0, 0, 0, 0]
elif v0n == 3:
    v0 = [0, 0, 1, 0, 0, 0, 0, 0]
elif v0n == 4:
    v0 = [0, 0, 0, 1, 0, 0, 0, 0]

print(v0n)

#choices for pitch-class set
pcset = np.arange(1, 9)

for i in range(1, 15):
    out = np.random.choice(pcset, 1, p=np.dot(matrix_power(tr, i), v0))
    print(out)
