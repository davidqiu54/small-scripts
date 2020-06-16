#CTtoFasta.py

#This script takes in a ct file and outputs a fasta file.

#March 4 2015

import sys

inCT = open(sys.argv[1],'r')
inLines = inCT.readlines()
inCT.close()

outF = open(sys.argv[1][:-3]+'.fa','w')

#print header
outF.write(">"+inLines[0])
#run through CT and print sequence to file
for i in range(1,len(inLines)):
	cols = inLines[i].strip().split()
	outF.write(cols[1])
outF.write("\n")