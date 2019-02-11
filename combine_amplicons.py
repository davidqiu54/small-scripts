# ProfileSmoosher
#
# This is a script to combine shape data from multiple amplicons from a single
# target into one shape profile
#
# It takes a single reference fasta and multiple SHAPE profile.txt files
# After sequence identities are confirmed, new profile.txt file will be writen:
#     For modified and untreated samples, counts and depths will be summed.
#     New profiles will be calculated from these counts.
#
import sys
from argparse import ArgumentParser
import re
import numpy as np


def parseFasta(fasta=None):
    """
    Given a fasta file:
    1) Create a dict with names and sequences
    2) Parse header lines for name (dict key)
    3) proceeding lines are concatenated onto name's dict value (sequence)
    """
    seqs = {}
    with open(fasta) as seqfile:
        all_nucs = re.compile("^[ACGTN]*$", re.IGNORECASE)
        is_head = re.compile("^>(.*)$")
        for line in seqfile:
            if is_head.match(line):
                seq_name = is_head.search(line).group(1)
                seqs[seq_name] = ""
            elif all_nucs.match(line.strip()):
                seqs[seq_name] += line.strip()
            else:
                sys.exit("fasta sequence is formatted incorrectly")
    return seqs


def makeNewProfile(seq_dict=None,
                   profiles=None,
                   **kwargs):
    """

    """
    # make sure only 1 sequence in dict
    # grab name, sequence, and length
    if len(seq_dict) == 1:
        seq_name = seq_dict.keys()[0]
        seq = seq_dict.values()[0]
        seq_len = len(seq)
    else:
        sys.exit("seq_dict does not contain just 1 sequence")
    # initiate a new_profile and populate the sequence and nucleotide fields
    profile_types = np.dtype([('nuc', 'i4'), ('seq', 'S1'),
                              ('mod_muts', 'i4'), ('mod_depth', 'i4'),
                              ('mod_effdepth', 'i4'), ('mod_rate', 'f8'),
                              ('unt_muts', 'i4'), ('unt_depth', 'i4'),
                              ('unt_effdepth', 'i4'), ('unt_rate', 'f8'),
                              ('den_muts', 'i4'), ('den_depth', 'i4'),
                              ('den_effdepth', 'i4'), ('den_rate', 'f8'),
                              ('prof', 'f8'), ('stderr', 'f8'),
                              ('HQprof', 'f8'), ('HQstderr', 'f8'),
                              ('norm_prof', 'f8'), ('norm_stderr', 'f8')])
    new = np.zeros(seq_len, dtype=profile_types)
    new['seq'] = [nt for nt in seq]
    new['nuc'] = np.arange(1, len(seq) + 1)
    # for each profile, find the unique start site
    # add counts to new where appropriate
    for prof in profiles:
        profile = np.genfromtxt(prof, skip_header=1, dtype=profile_types)
        sub = ''.join(profile['seq']).upper()
        sub_len = len(sub)
        start = seq.index(sub)
        # add current profile to new
        not_nans = np.logical_not(np.isnan(profile['HQprof']))
        ref_index = np.zeros(seq_len, dtype=bool)
        ref_index[start:start + sub_len] += not_nans
        fields = ['mod_muts', 'mod_depth', 'mod_effdepth',
                  'unt_muts', 'unt_depth', 'unt_effdepth']
        for field in fields:
            new[field][ref_index] += profile[field][not_nans]
    # compute the mutation rates
    new['mod_rate'] = new['mod_muts'].astype('f8') / new['mod_effdepth']
    new['unt_rate'] = new['unt_muts'].astype('f8') / new['unt_effdepth']
    new['den_rate'] = new['den_muts'].astype('f8') / new['den_effdepth']
    # compute prof and standard error
    new['prof'] = new['mod_rate'] - new['unt_rate']
    Modified_err = (new['mod_rate'] / new['mod_effdepth'])**0.5
    Untreated_err = (new['unt_rate'] / new['unt_effdepth'])**0.5
    new['stderr'] = (Modified_err**2 + Untreated_err**2)**0.5
    # compute HQprof and HQstderr, for now equal to prof and stderr
    new['HQprof'] = new['prof']
    new['HQstderr'] = new['stderr']
    # compute normalized profile and stderr
    ignore_nans = np.logical_not(np.isnan(new['prof']))
    norm_factor = 0.5 / (np.median(new['prof'][ignore_nans]))
    new['norm_prof'][ignore_nans] = new['HQprof'][ignore_nans] * norm_factor
    new['norm_stderr'][ignore_nans] = new['HQstderr'][ignore_nans] * norm_factor
    # write new profile out to profile.txt
    filename = '{0}_concat_profile.txt'.format(seq_name)
    field_names = '\t'.join(new.dtype.names)
    np.savetxt(filename, new, delimiter='\t', header=field_names,
               fmt=['%.1i', '%.1s', '%.1i', '%.1i', '%.1i', '%.6f',
                    '%.1i', '%.1i', '%.1i', '%.6f', '%.1i', '%.1i', '%.1i',
                    '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f', '%.6f'])


if __name__ == "__main__":
    ap = ArgumentParser(description="Combine amplicons into one profile.txt")
    ap.add_argument("fasta", metavar="reference fasta", type=str,
                    help="filename of input reference fasta file")
    ap.add_argument("--profiles", default=None, type=str, nargs="+",
                    help="_profile.txt files to be combined")
    pa = vars(ap.parse_args(sys.argv[1:]))
    seq = parseFasta(pa["fasta"])
    profileFile = makeNewProfile(seq, pa["profiles"])
