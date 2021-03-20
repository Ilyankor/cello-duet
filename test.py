import numpy as np
from pandas import DataFrame, read_excel
from numpy.linalg import matrix_power

#input the given pitch and the number of pitches for the entire rhythm
#here, F = F#
start = input("First pitch: ")
num = input("Total number of notes: ")

#obtain the transition matrx
df = read_excel("master.xls", sheet_name="pr-tr", header=None)
tr = df.to_numpy()

#define the initial vector v_i
if start == "D":
    v0 = ([1, 0, 0, 0, 0])
elif start == "E":
    v0 = ([0, 1, 0, 0, 0])
elif start == "F":
    v0 = ([0, 0, 1, 0, 0])
elif start == "A":
    v0 = ([0, 0, 0, 1, 0])
elif start == "B":
    v0 = ([0, 0, 0, 0, 1])

#the markov process
tr2 = matrix_power(tr, 2)
tr3 = matrix_power(tr, 3)

#the possible pitches
pitches = ['D', 'E', 'F#', 'A', 'B']

#function
if num == '2':
    output = np.random.choice(pitches, 1, p=np.dot(tr, v0))
    print(output)
elif num == '3':
    output1 = np.random.choice(pitches, 1, p=np.dot(tr, v0))
    output2 = np.random.choice(pitches, 1, p=np.dot(tr2, v0))
    print(output1, output2)
elif num == '4':
    output1 = np.random.choice(pitches, 1, p=np.dot(tr, v0))
    output2 = np.random.choice(pitches, 1, p=np.dot(tr2, v0))
    output3 = np.random.choice(pitches, 1, p=np.dot(tr3, v0))
    print(output1, output2, output3)
