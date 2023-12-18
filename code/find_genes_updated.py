# To detect genes in a tbl file

import sys
import numpy as np

def open_file(file):
    imported_file = open(sys.argv[file], "r")
    return imported_file

def to_list(file, gene):
    temp_list=[]
    for line in file:
        if gene==True:
            if "gene" in line:
                i = line.split("\t")
                temp_list.append((i[4]))
        else:
            i = line.split(",")
            temp_list.append((i))
    return temp_list

def check_gene(gene_array, length, index, sample_list):
    for i in range(1,length):
        for j in sample_list:
            j=j.strip()
            reference_gene=gene_array[i,0]
            gene_length = len(reference_gene)
            if j[:gene_length].upper() == reference_gene.upper():
                gene_array[i, index]="*"
        if gene_array[i,index]==None:
            gene_array[i,index]="n/a"

genes = open_file(1)

sample_1 = open_file(2)
sample_2 = open_file(3)
sample_3 = open_file(4)
sample_4 = open_file(5)
sample_5 = open_file(6)
sample_6 = open_file(7)
sample_7 = open_file(8)


gene_list = []
gene_list=to_list(genes,False)

sample_genes_1 = []
sample_genes_1 = to_list(sample_1,True)
sample_genes_2 = []
sample_genes_2 = to_list(sample_2,True)
sample_genes_3 = []
sample_genes_3 = to_list(sample_3,True)
sample_genes_4 = []
sample_genes_4 = to_list(sample_4,True)
sample_genes_5 = []
sample_genes_5 = to_list(sample_5,True)
sample_genes_6 = []
sample_genes_6 = to_list(sample_6,True)
sample_genes_7 = []
sample_genes_7 = to_list(sample_7,True)


columns=len(gene_list)
rows=len(sys.argv)
A = np.empty((columns, rows), dtype=object)


A[0][0]="Gene"
A[0][1]="Product"
for i in range(1,columns):
    A[i][0]=gene_list[i][0]
    A[i][1]=gene_list[i][1].strip('\n')


for i in range(2,rows):
    header=f'{str(sys.argv[i])}'
    A[0][i]=header.replace('.tbl','')


check_gene(A,columns,2, sample_genes_1)
check_gene(A,columns,3, sample_genes_2)
check_gene(A,columns,4, sample_genes_3)
check_gene(A,columns,5, sample_genes_4)
check_gene(A,columns,6, sample_genes_5)
check_gene(A,columns,7, sample_genes_6)
check_gene(A,columns,8, sample_genes_7)

np.savetxt('genes_sample15-21.csv', A, delimiter='\t', comments='', fmt='%s')

print(A)