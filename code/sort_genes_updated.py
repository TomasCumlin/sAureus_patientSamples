import sys
import csv
import numpy as np


with open(sys.argv[1], newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter='\t'))

A = np.empty((1, 23), dtype=object)

A[0,:]=data[0]


for num in range(23, -1, -1):
    for line in data[1:]:
        number = line.count("*")
        if number==num:
            A = np.vstack([A, line])

print(A)

np.savetxt('genes_sorted.csv', A, delimiter='\t', comments='', fmt='%s')