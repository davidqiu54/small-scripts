
import matplotlib.pyplot as plt
import numpy as np

from sys import argv
import os.path

# accept an arbitraty number of mutation strings to plot together...


# read filters:
minReadLength = 100
maxSCount = 10


def readMutationStrings(filename):

  muts = [0]*100
  with open(filename) as f:
    
    for line in f:
      spl = line.rstrip().split()
    
      if len(spl[3])< minReadLength  or spl[3].count('s') > maxSCount:
        continue

      num=0
      for event in ('A', 'G', 'C', 'T','-'):
        num += spl[3].count(event)
      muts[num]+=1

  # trim the array
  while muts[-1]==0:
    muts.pop()

  return np.array(muts, dtype='float64')



def printhelp():
   
  out = """usage:: python countMutsPerMol.py [-n] [-p] [-o filename] inputfile1 [inputfile1] [inputfile2] ...
  	-n = normalize read counts to sum to 1
	-p = print histogram values to stdout as well as creating figure
	-o = output figure name; defaults to 'hitrate.pdf'
	Accepts an abitrary number of mutation string files, provided as a list: file1 file2... 
   """

  print out



norm = False
printout = False
figname = 'hitrate.pdf'
filenames = []



if len(argv) < 2:
  printhelp()
  exit()

# parse arguments
for f in argv[1:]:

  if f[:2] == '-n':
    norm = True
    
  elif f[:2] == '-p':
    printout = True
 
  elif f[:2] == '-o':
    figname = f.split('=')[1]

  elif os.path.isfile(f):
    filenames.append(f)

  else:
    print "skipping undefined file or argument %s" % f


# read the files
mutations = []
minv = 1e10
for f in filenames:
  
  m = readMutationStrings(f)
  if norm:
    m/=sum(m)
  
  curmin = min(m[m>0])
  if curmin < minv:
     minv = curmin

  mutations.append(m)



##################
# make the plot
##################
dim = len(mutations)
w = 0.75
dimw = w/dim
colors = ['k','r','b','g','c','m','y','0.6']

maxmut = max([len(x) for x in mutations])
xcoor = np.arange(0, maxmut)

for i,d in enumerate(mutations):
  
  plt.bar(np.arange(len(d)) + i*dimw, d, width=dimw, bottom=minv/10.,label = filenames[i], color=colors[i])
  if printout:
    print list(d), sum(d)

plt.xticks(xcoor+w/2, xcoor)

if norm:
  plt.ylabel("Relative fraction of Reads")
else:
  plt.ylabel("Number of Reads")

  
plt.xlabel("Mutations per read")
plt.legend()
plt.tight_layout()
#plt.yscale('log')
plt.savefig(figname)

