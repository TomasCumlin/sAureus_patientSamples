# Code is run on gff-files obtained by BARRNAP
# Slices the 16S-sequences and save them to new fasta-files
# random line in test branch

import sys

fi = open(sys.argv[1])
nucleotide = []

# obtain nucleotide start/end positions for all 16S sequences 
for line in fi:
    if "Name=16S" in line:
        temp = line.split('\t')
        nucleotide.append(temp[3])
        nucleotide.append(temp[4])

# open file as string
fi = open(sys.argv[1])
fi_string = fi.read()

# obtain the index where nucleotide reads begins
index = (fi_string.index("Flye"))+4

counter=0

for i in range(0,(len(nucleotide)),2):
    start = index+int(nucleotide[i])
    end = (index+int(nucleotide[i+1]))+1
    with open(f'{sys.argv[2]}_{counter}.fasta', 'w') as f:
        print(f'>16S_{sys.argv[2]}_{counter}\n',fi_string[start:end], file=f)
    counter+=1 

