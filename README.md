# random-scripts
Small scripts for semi-common tasks.

## bootstrap_samtofastq.py
For subsampling sequencing data:
This script will take a .sam file as input, and return a .fastq or 
.fastq.gz that approximately contains a specified number of reads. It also
contains an option for pre-filtering the input for full-length reads.
