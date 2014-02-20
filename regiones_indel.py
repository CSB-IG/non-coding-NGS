import matplotlib
matplotlib.rcParams.update({'font.size': 8})

from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
north_sets = {}
for s in north:
    north_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


centre_sets = {}
for s in centre:
    centre_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


peninsula_sets = {}
for s in peninsula:
    peninsula_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


north_union = set.union(*[north_sets[n] for n in north])
centre_union = set.union(*[centre_sets[n] for n in centre])
peninsula_union = set.union(*[peninsula_sets[n] for n in peninsula])


from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3
plt.figure(figsize=(4,4))
v = venn3([north_union, centre_union, peninsula_union], set_labels=('North', 'Centre', 'South'))
plt.savefig('regiones_indel.svg')

