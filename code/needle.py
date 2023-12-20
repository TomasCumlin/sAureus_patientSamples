import sys
from Bio import Align
import numpy as np


def open_file(file):
    imported_file = open(sys.argv[file], "r")
    return imported_file

def to_list(file):
    temp_list=[]
    sequences=[]
    for line in file:
        i = line.split("\t")
        temp_list.append(i)
    for i in range(0,(len(temp_list)-1)):
        check=str(temp_list[i])
        if ">16S" == check[2:6]:
            to_append=str(temp_list[i+1])
            sequences.append(to_append.replace('[','').replace(']','').replace('\\n','').replace("'",''))
    return sequences


sequences=open_file(1)
sequence_list=to_list(sequences)


aligner = Align.PairwiseAligner(mode='global',gap_score=-5)

counter2 = len(sequence_list)
counter3=0
A = np.zeros(shape=(counter2+1, counter2+1))

for i in range(0,counter2+1):
    A[0][i]=i
    A[i][0]=i   


for i in range(0,len(sequence_list)):
    for j in range(counter3,(counter2)):
        a = sequence_list[i]
        b = sequence_list[j]
        aln= aligner.align(a,b)
        score = aligner.score(a, b)
        percent = score/(len(a))*100
        
        A[counter3+1][j+1]=percent
        A[j+1][counter3+1]=percent     
    counter3+=1

np.savetxt('{}.csv'.format((sys.argv[1]).strip('.fa')), A, delimiter=",")

print(A)