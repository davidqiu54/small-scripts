#removeSCFromProfile.py

import argparse
import re
def parseArgs():
	prs = argparse.ArgumentParser()
	prs.add_argument("profile",type=str,help="Input profile file. Keeps the header but changes the length.")
	prs.add_argument("--outputFileName",type=str,help="Input a custom output name for the new trimmed correlation file.")
	o = prs.parse_args()
	return o


args = parseArgs()

#load in correlation file into list of lines
inputFile = open(args.profile,'r')
profileLines = inputFile.readlines()
inputFile.close()

#open up the output file
if(args.outputFileName):
	outF = open(args.outputFileName,'w')
else:
	outF = open(args.profile[:-4]+"_SCTrimmed.txt",'w')

#write out header
outF.write(profileLines.pop(0))
#determine the sequence length by subtraction from the last nt in the profile
seqLength = int(profileLines[-1].split()[0])
seqLength = seqLength - 14 - 43

for line in profileLines:
	cols = line.strip().split()
	if(int(cols[0]) > 14 and int(cols[0]) <= (seqLength + 14)):
		cols[0] = str(int(cols[0]) - 14)
		outF.write("\t".join(cols)+"\n")
	