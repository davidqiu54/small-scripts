#removeSCfromCT.py

import argparse
import re
def parseArgs():
	prs = argparse.ArgumentParser()
	prs.add_argument("CT",type=str,help="Input CT file. Keeps the header but changes the length.")
	prs.add_argument("--outputFileName",type=str,help="Input a custom output name for the new trimmed correlation file.")
	o = prs.parse_args()
	return o


args = parseArgs()

#load in correlation file into list of lines
inputFile = open(args.CT,'r')
ctLines = inputFile.readlines()
inputFile.close()

#open up the output file
if(args.outputFileName):
	outF = open(args.outputFileName,'w')
else:
	outF = open(args.CT[:-3]+"_SCTrimmed.ct",'w')

#pop the header lines into the output
header = ctLines.pop(0)
header = header.split()
#change the length in the header, subtract out the SC
seqLength = int(header[0])
seqLength = seqLength - 14 - 43
header[0] = str(seqLength)
outF.write("\t".join(header)+"\n")


print seqLength
for line in ctLines:
	cols = line.strip().split()
	if(int(cols[0]) > 14 and int(cols[0]) <= (seqLength + 14)):	
		cols[0] = str(int(cols[0]) - 14)
		cols[2] = str(int(cols[2]) - 14)
		cols[3] = str(int(cols[3]) - 14)
		cols[5] = str(int(cols[5]) - 14)
		if(int(cols[4]) != 0):
			cols[4] = str(int(cols[4]) - 14)
		outF.write("\t".join(cols)+"\n")