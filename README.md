random-scripts
==============
Small scripts for semi-common tasks.


For subsampling sequencing data:
--------------------------------
*bootstrap_samtofastq.py*

This script will take a .sam file as input, and return a .fastq or .fastq.gz
that approximately contains a specified number of reads. It also contains an
option for pre-filtering the input for full-length reads.

__Example__
```
python bootstrap_samtofastq.py input-file.sam --filter --out output-file.fastq.gz --reads 10000 20000
```
This command would create 3 new files:
+ input-file_fullength.sam - containing only full-length alignments
+ output-file_10000.fastq.gz - containing approximately 10,000 reads
+ output-file_20000.fastq.gz - containing approximately 20,000 reads


For combining tiled amplicon data:
----------------------------------
*combine_amplicons.py*

This script will take profile.txt files from multiple amplicons and combine them
into a single profile.txt that matches the given fasta reference file. This
will work for Nextera or amplicons, and removes data from low quality positions.

__Example__
```
python combine_amplicons.py reference.fa --profiles 1_profile.txt 2_profile.txt
```
This command would create one new file, reference_concat_profile.txt, with combined data from each of the profiles, in this case 1 and 2.


For make histograms of mutations per molecule:
----------------------------------------------
*countMutsPerMol.py*

This script will take mutation strings files from ShapeMapper_v1.2, and create a histogram plot of the number of mutations per molecule.

__Example__
```
python countMutsPerMol.py -n -o output.pdf example_mutation_strings.txt
```
This command would create one new file, output.pdf, that contains a histogram of the number of mutations per molecule.

