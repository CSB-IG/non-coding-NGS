import matplotlib
matplotlib.use('svg')
matplotlib.rcParams.update({'font.size': 8})

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2

from sample_code_file_maps import *
from itertools import combinations

# computes jacard index for two or mor sets
def jaccard_index(first, *others):
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))


types = [ 'alleles/%s_insdel.alleles',
          'alleles/%s_snp.alleles', ]
          


def jin_pair( set1, set2, mask):
    set_a = set()
    for s in linguistic_groups[set1]:
        set_a.update([v.strip() for v in open( mask % ethnicity_code[s]).readlines()])
    set_b = set()
    for s in linguistic_groups[set2]:
        set_b.update([v.strip() for v in open( mask % ethnicity_code[s]).readlines()])
    return jaccard_index(set_a, set_b)


def venn_pair( set1, set2, mask):
    set_a = set()
    for s in linguistic_groups[set1]:
        set_a.update([v.strip() for v in open( mask % ethnicity_code[s]).readlines()])
    set_b = set()
    for s in linguistic_groups[set2]:
        set_b.update([v.strip() for v in open( mask % ethnicity_code[s]).readlines()])

    plt.cla()
    venn2((set_a, set_b), set_labels=(set1, set2))
#    figure.set_size_inches(3,15.4)
#    figure.set_dpi(400)
    plt.savefig("%s_%s_%s.svg" % (set1, set2, 'venn'+mask.split('%s')[1] ))


for pair in combinations( linguistic_groups.keys(), 2 ):
    for t in types:
        print pair, t, jin_pair(pair[0], pair[1], t)
        # venn_pair(pair[0], pair[1], t)



