import argparse, sys

import pprint

parser = argparse.ArgumentParser(description='Create map of variants NOT in specified map.')
parser.add_argument('--variant_map',  type=argparse.FileType('r'), required=True )
parser.add_argument('--coding_map',  type=argparse.FileType('r'), required=True )

args    = parser.parse_args()
variant_map = args.variant_map
coding_map  = args.coding_map

if __name__ == '__main__':

    coding    = [v.strip().split() for v in coding_map.readlines()]
    vars      = [v.strip().split() for v in variant_map.readlines()]


    for v in vars:
        in_coding_region = False
        for n in coding:
            if v[0] == "chr%s" % n[0] and int(v[1]) >= int(n[1]) and int(v[2]) <= int(n[2]):
                in_coding_region = True

        if not in_coding_region:
            print " ".join(v)

