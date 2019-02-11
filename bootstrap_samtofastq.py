import sys
from argparse import ArgumentParser
from itertools import izip as zip
from numpy.random import poisson


def filter_fulllength(sam=None,
                      out=None,
                      reads=None,
                      **kwargs):

    fl_sam = sam[:-4] + "_fulllength.sam"
    count = 0
    # create sam file containing only full-length reads
    with open(sam, "rU") as fin, open(fl_sam, "w") as fout:
        seqs = dict()
        for line in fin:
            fields = [x.strip() for x in line.split()]
            if count % 10000 == 0:
                print("{} reads . . .".format(count))
            if fields[0] in ["@HD", "@RG", "@PG", "@CO"]:
                fout.write(line)
            elif fields[0] in ["@SQ"]:
                fout.write(line)
                seqs[fields[1][3:]] = int(fields[2][3:])
            else:
                total = 0
                current = ''
                for c in fields[5]:
                    if c.isdigit():
                        current += c
                    if c in 'MNDX=':
                        total += int(current)
                        current = ''
                    if c in 'SHIP':
                        current = ''
                if total == seqs[fields[2]]:
                    fout.write(line)
                    count += 1

        return fl_sam, count


def subsample_samtofastq(count=None,
                         sam=None,
                         out=None,
                         reads=None,
                         **kwargs):

    counts = [0 for x in reads]

    with open(sam, "rU") as fin:
        fastqs = [out.replace(".fastq", "_" + str(x) + ".fastq")
                  for x in reads]
        if out.endswith(".gz"):
            fouts = [gzip.open(fastq, "wt") for fastq in fastqs]
        else:
            fouts = [open(fastq, "w") for fastq in fastqs]
        for line in fin:
            fields = [field.strip() for field in line.split()]
            if fields[0] in ["@HD", "@SQ", "@RG", "@PG", "@CO"]:
                continue
            for i, read in enumerate(reads):
                p = poisson(read / (count * 1.0))
                for x in range(p):
                    counts[i] += 1
                    fouts[i].write("@" + fields[0] + "\n"
                                   + fields[9] + "\n+\n" + fields[10] + "\n")
    print("number of reads selected for each --reads input")
    for read, count in zip(reads, counts):
        print("--reads {}: {}".format(read, count))


if __name__ == "__main__":
    ap = ArgumentParser(description="subsample full length reads from the " +
                                    "sam file of shapemapper's output when " +
                                    "--output-aligned is called")
    ap.add_argument("sam", metavar=".sam file", type=str,
                    help="filename of input sam file")
    ap.add_argument("--filter", action="store_true",
                    help="before subsampling, filter for full-length reads")
    ap.add_argument("--out", type=str, default=None,
                    help="filename of output fastq file (add .gz to " +
                    "compress), period before 'fastq' will be replaced with" +
                    " '_[read-count].'")
    ap.add_argument("--reads", type=int, default=None, nargs="+",
                    help="an integer or list of integers, the number(s) of" +
                    " reads to be in the final fastq file(s)")

    pa = vars(ap.parse_args(sys.argv[1:]))
    # locals().update(pa.__dict__)

    if pa["filter"]:
        pa["sam"], count = filter_fulllength(pa["sam"])
    else:
        count = sum([1 for line in open(pa["sam"])])

    subsample_samtofastq(count, **pa)
