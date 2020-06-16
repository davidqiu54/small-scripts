#fastqToFa.py

#April 19, 2017

#Created By: Tom Christy

#This script takes in a fastq file and, by default, outputs a fasta file with the same name 
#as the fastq. Only the read name and sequence are retained. If a second argument is given, 
#the output will be written there

import argparse

def parseArgs():
	prs = argparse.ArgumentParser()
	prs.add_argument("fastq", type=str, help="File Name of Fastq file that you want to convert")
	prs.add_argument("--fastaFile", type=str, default="", help="Use this option to specifiy the desired output file name")
	o = prs.parse_args()
	return o

#parse in the script's arguments
args = parseArgs()

#load in the fastq file
inF = open(args.fastq,'r')
fastqLines = inF.readlines()
inF.close()

#ensure proper format of fastq file
if(len(fastqLines)%4 != 0):
	print "WARNING!!! Number of lines in fastq is not divisible by 4, this could create an incorrect output!"

#create the target output file
#default output
if(args.fastaFile == ""):
	outF=open(args.fastq[:-6]+".fa",'w')
else:
	#specified output
	outF=open(args.fastaFile,'w')

#run through fastq file and output only the readName and sequence
for i in range(0,len(fastqLines),4):
	#make sure that that line i is a read name
	if(fastqLines[i][0] == '@'):
		fastqLines[i] = fastqLines[i].replace("@",">",1)
		outF.write(fastqLines[i])
		outF.write(fastqLines[i+1])
	
outF.close()