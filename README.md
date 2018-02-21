# random-scripts
Small scripts for semi-common tasks.

## For subsampling sequencing data:
### bootstrap_samtofastq.py
This script will take a .sam file as input, and return a .fastq or .fastq.gz
that approximately contains a specified number of reads. It also contains an
option for pre-filtering the input for full-length reads.

## For combining tiled amplicon data:
### combine_amplicons.py
This script will take profile.txt files from multiple amplicons and combine them
into a single profile.txt that matches the given fasta reference file. This
will work for Nextera or amplicons, and removes data from low quality positions.
