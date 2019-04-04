#compareSHAPE.py

#November 4, 2015

#This script takes in two .shape files and plots their reactivities on the same scale
#-999 values are completely ignored. The nucleotide numbering is assumed to be the same
#in both SHAPE files.

#import statements

import argparse
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
#this function takes in a shape file name and outputs an array of the shape values.
#-999 values are removed
def loadSHAPE(fileName):
	inF = open(fileName,'r')
	inLines = inF.readlines()
	inF.close()
	#create empty array to hold SHAPE values
	shapeData = list()
	#loop through shape lines and pull out good stuff
	for line in inLines:
		cols = line.strip().split()
		if(float(cols[1])>-100):
			shapeData.append([int(cols[0]),float(cols[1])])
	#return filtered SHAPE data
	return shapeData


def parseArgs():
    prs = argparse.ArgumentParser()
    prs.add_argument("input1", type=str, help="1st SHAPE File")
    prs.add_argument("input2", type=str, help="2cnd SHAPE File")
    prs.add_argument('--delta',action='store_true',default=False,help='Make a SHAPE1-SHAPE2 plot')
    prs.add_argument("--circle5",action='store_true',default=False,help="Highlignt known regions of the 5\' end of DENVII that change SHAPE reactivity when circularized")
    o = prs.parse_args()
    return o
	
args = parseArgs()
matplotlib.rcParams.update({'font.size': 18})
#Do -6 just to remove .shape suffix
name1 = args.input1[:-6]
name2 = args.input2[:-6]
if(args.delta):
	#read in file 1
	inF1 = open(args.input1,'r')
	inLines1 = inF1.readlines()
	inF1.close()
	#read in file 2
	inF2 = open(args.input2,'r')
	inLines2 = inF2.readlines()
	inF2.close()
	#create empty array to hold SHAPE values
	shapeData = list()
	#loop through shape lines and pull out good stuff
	for i in range(len(inLines1)):
		cols1 = inLines1[i].strip().split()
		cols2 = inLines2[i].strip().split()
		if(float(cols1[1])>-100 and float(cols2[1])>-100):
			shapeData.append([int(cols1[0]),float(cols1[1])-float(cols2[1])])
	delta = np.array(shapeData)
	fig = plt.figure("SHAPE Differential", figsize=(20,10))
	plt.plot(delta[:,0],delta[:,1],'r', drawstyle='steps-mid', label = name1+" - "+name2)
	plt.axhline(color = 'k')
	if(args.circle5):
		plt.axvspan(85,89,alpha=0.3,color='lightgrey')
		plt.axvspan(105,110,alpha=0.3,color='lightgrey')
		plt.axvspan(134,144,alpha=0.3,color='lightgrey')
	plt.xlabel('Nucleotide')
	plt.ylabel('SHAPE Reactivity Difference')
	plt.title(name1+" - "+name2+" SHAPE Reactivity Difference")
	plt.legend(loc = 1)
	plt.tight_layout()
	#plt.show()
	plt.savefig(name1+"_To_"+name2+"_SHAPEReactivitySubtraction.pdf")
else:
	shape1 = np.array(loadSHAPE(args.input1))
	shape2 = np.array(loadSHAPE(args.input2))
	fig = plt.figure("SHAPE Reactivity Comparison", figsize=(20,10))

	plt.plot(shape1[:,0],shape1[:,1],'r', drawstyle='steps-mid', label = name1)
	plt.plot(shape2[:,0],shape2[:,1],'b', drawstyle='steps-mid', label = name2)
	plt.axhline(color = 'k')
	if(args.circle5):
		plt.axvspan(85,89,alpha=0.3,color='lightgrey')
		plt.axvspan(105,110,alpha=0.3,color='lightgrey')
		plt.axvspan(134,144,alpha=0.3,color='lightgrey')
	plt.title("SHAPE Reactivity Comparison")
	plt.xlabel('Nucleotide')
	plt.ylabel('SHAPE Reactivity')
	plt.legend(loc = 1)
	plt.tight_layout()
	#plt.show()
	plt.savefig(name1+"_To_"+name2+"_SHAPEReactivityComparison.pdf")
	