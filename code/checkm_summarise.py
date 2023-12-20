# Take the stats output from checkM (bin_stats_ext.tsv) and save relevant columns to new csv


import sys
import csv

def open_file(file):
    imported_file = open(sys.argv[file], "r")
    return imported_file

def to_list(file):
    temp_list=[]
    for line in file:
        i = line.split(",")
        temp_list.append(i)
            
    return temp_list

def obtain(row,index,marker):
    i = row[index]
    i = i.split(marker)
    return i

table = open_file(1)
table_list = to_list(table)

with open('large.csv','w') as f1:
    writer=csv.writer(f1, delimiter='\t',lineterminator='\n',)
    for line in table_list:
        sample = obtain(line,0,"\t")
        species = obtain(line,0,":")
        genomes = obtain(line,1,":")
        completeness = obtain(line,10,":")
        contamination = obtain(line,11,":")
        gc = obtain(line,12,":")
        genome_size = obtain(line,14,":")
        contigs = obtain(line,17,":")
        longest = obtain(line,19,":")
        n50 = obtain(line,21,":")

        row = [sample[0] + "\t" + species[1] + "\t" + genomes[1] + "\t" + completeness[1] +
        "\t" + contamination[1] + "\t" + gc[1] + "\t" + genome_size[1] + "\t" + contigs[1] +
        "\t" + longest[1] + "\t" + n50[1]]
        writer.writerow(row)


for line in table_list:
    species = obtain(line,0,":")
    genomes = obtain(line,1,":")
    completeness = obtain(line,10,":")
    contamination = obtain(line,11,":")
    gc = obtain(line,12,":")
    genome_size = obtain(line,14,":")
    contigs = obtain(line,17,":")
    longest = obtain(line,19,":")
    n50 = obtain(line,21,":")

    print("Sample" + "\t" + species[0] + "\t" + genomes[0] + "\t" + completeness[0] +
    "\t" + contamination[0] + "\t" + gc[0] + "\t" + genome_size[0] + "\t" + contigs[0] +
    "\t" + longest[0] + "\t" + n50[0] + "\n")
    break


