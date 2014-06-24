import argparse, sys

import pprint

parser = argparse.ArgumentParser(description='Extract regions in BED file from TSV file to STDOUT')
parser.add_argument('--bed',  type=argparse.FileType('r'), required=True )
parser.add_argument('--tsv',  type=argparse.FileType('r'), required=True )

args    = parser.parse_args()

bed = [v.strip().split() for v in args.bed.readlines()]
tsv = [v.strip().split() for v in args.tsv.readlines()]

for v in tsv:
    for n in bed:
        if v[0] == "chr%s" % n[0] and int(v[1]) >= int(n[1]) and int(v[2]) <= int(n[2]):
            print " ".join(v)
            break

