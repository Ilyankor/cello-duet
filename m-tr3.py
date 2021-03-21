import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#input information
car = int(input("Cardinality of pitch-class set: "))
num = int(input("Total number of notes: "))

#import transition matrix
df1 = read_excel("master.xls", sheet_name="m-tr3-1", header=None)
df2 = read_excel("master.xls", sheet_name="m-tr3-2", header=None)
df3 = read_excel("master.xls", sheet_name="m-tr3-3", header=None)

#define initial vectors
if car == 3:
    v0 = [1, 0, 0]
    tr = df1.to_numpy()
elif car == 4:
    v0 = [1, 0, 0, 0]
    tr = df2.to_numpy()
elif car == 5:
    v0 = [1, 0, 0, 0, 0]
    tr = df3.to_numpy()

#choices for pitches
pitches = np.arange(1, car + 1)

#function
for i in range(1, num):
    out = np.random.choice(pitches, 1, p=np.dot(matrix_power(tr, i), v0))
    print(out)
