import pandas as pd
import numpy as np

#input the given pitch and the number of pitches for the entire rhythm
#here, F = F#
start = input("First pitch: ")
num = input("Total number of notes: ")

#obtain the transition matrx
df = pd.read_excel("master.xls", sheet_name="pr-tr", header=None)
tr = df.to_numpy()

#define the initial vector v_i
if start == "D":
    vi = ([1, 0, 0, 0, 0])
elif start == "E":
    vi = ([0, 1, 0, 0, 0])
elif start == "F":
    vi = ([0, 0, 1, 0, 0])
elif start == "A":
    vi = ([0, 0, 0, 1, 0])
elif start == "B":
    vi = ([0, 0, 0, 0, 1])

#the markov process
tr2 = np.dot(tr, tr)
tr3 = np.dot(tr2, tr)

#the possible pitches
pitches = ['D', 'E', 'F#', 'A', 'B']

#function
if num == '2':
    output = np.random.choice(pitches, 1, p=np.dot(tr, vi))
    print(output)
elif num == '3':
    output1 = np.random.choice(pitches, 1, p=np.dot(tr, vi))
    output2 = np.random.choice(pitches, 1, p=np.dot(tr2, vi))
    print(output1, output2)
elif num == '4':
    output1 = np.random.choice(pitches, 1, p=np.dot(tr, vi))
    output2 = np.random.choice(pitches, 1, p=np.dot(tr2, vi))
    output3 = np.random.choice(pitches, 1, p=np.dot(tr3, vi))
    print(output1, output2, output3)
