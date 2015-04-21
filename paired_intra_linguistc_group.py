import matplotlib
matplotlib.use('agg')
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
          'alleles/%s_snp.alleles',
          'alleles/%s_snp_et_indel.alleles' ]


def jin_pair( set1, set2, mask):
    set_a = set([v.strip() for v in open( mask % ethnicity_code[set1]).readlines()])
    set_b = set([v.strip() for v in open( mask % ethnicity_code[set2]).readlines()])

    return jaccard_index(set_a, set_b)


def venn_pair( set1, set2, mask):
    set_a = set([v.strip() for v in open( mask % ethnicity_code[set1]).readlines()])
    set_b = set([v.strip() for v in open( mask % ethnicity_code[set2]).readlines()])
    
    plt.cla()
    venn2((set_a, set_b), set_labels=(set1, set2))
    plt.savefig("%s_%s_%s.png" % (set1, set2, 'venn'+mask.split('%s')[1] ))


pares = [ ('Maya1', 'Maya2'),
          ('Nahua1', 'Nahua2'),
          ('Tarahumara1', 'Tarahumara2'),
          ('Tepehuana1', 'Tepehuana2'),
          ('Totonaca1', 'Totonaca2'),
          ('Zapoteca1', 'Zapoteca2'),
          ('m1', 'm2'),]


for pair in pares:
    for t in types:
        print pair, t, jin_pair(pair[0], pair[1], t)
        venn_pair(pair[0], pair[1], t)
