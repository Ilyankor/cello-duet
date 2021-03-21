import numpy as np

#generate a random nxn matrix
M = np.random.rand(5,5)

#normalize the matrix rows, sum = 1
S = M/M.sum(axis=1)[:,None]

#save the matrix as a csv file
np.savetxt("matrix.csv", S, delimiter=",")
