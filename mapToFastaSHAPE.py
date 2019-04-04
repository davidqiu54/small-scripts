#mapToFastaSHAPE.py

#Created April 3, 2019

#Created by Tom Christy

#This script takes in a map file and returns a fasta file and shape file.
#There is an option to add an upper or lower bound. This will cause only nucleotides
#within the bounds to be converted to fasta/shape and the shape numbering will start from 1
#and go to the last included nucleotide. Bounds are inclusive.

import argparse

def parse_args():
    prs = argparse.ArgumentParser()
    prs.add_argument("map",type=str,help="input map file")
    prs.add_argument("-l","--lowerBound",type=int,default=0,help="Input the lowest nucleotide number you want included in the fasta/SHAPE file.")
    prs.add_argument("-u", "--upperBound", type=int, default=0,
                     help="Input the highest nucleotide number you want included in the fasta/SHAPE file.")
    prs.add_argument("--uConvert",action="store_true",help="Use this option to convert T to U in the fasta sequence.")
    o = prs.parse_args()
    return o

if __name__ == "__main__":
    args = parse_args()
    #read in the map file into a list of lines
    inF = open(args.map,"r")
    mapLines = inF.readlines()
    inF.close()

    #set the upper and lower bounds, either from the map file or the input options
    if args.lowerBound:
        lowerLimit = args.lowerBound
    else:
        lowerLimit = 1
    if args.upperBound:
        upperLimit = args.upperBound
    else:
        upperLimit = int(mapLines[-1].strip().split()[0])

    #store only the lines within the bounds
    mapLines = mapLines[lowerLimit-1:upperLimit]

    #create a title for the outputs
    title = args.map[:-4]
    if args.lowerBound or args.upperBound:
        title+="_"+str(lowerLimit)+"_to_"+str(upperLimit)
    #open shape and fasta files
    outSHAPE = open(title+".shape",'w')
    outFasta = open(title+".fa",'w')
    outFasta.write(">"+title+"\n")
    ntNum = 1
    #run through the pertinent lines of the map file and output the fasta
    for line in mapLines:
        #split the line into a list
        cols = line.strip().split()
        #write the nt num and shape reactivity to the shape file
        outSHAPE.write(str(ntNum)+"\t"+cols[1]+"\n")
        ntNum += 1
        #write the nucleotide to the fasta sequence, convert T to U if requested in the options
        if args.uConvert and cols[3] == "T":
            outFasta.write("U")
        else:
            outFasta.write(cols[3])
    outFasta.close()
    outSHAPE.close()