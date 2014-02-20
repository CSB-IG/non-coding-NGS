from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3


from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
north_sets = {}
for s in north:
    north_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])


centre_sets = {}
for s in centre:
    centre_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])


peninsula_sets = {}
for s in peninsula:
    peninsula_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])


admixed_sets = {}
for s in admixed:
    admixed_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])


north_union     = set.union(*[north_sets[n] for n in north])
centre_union    = set.union(*[centre_sets[n] for n in centre])
peninsula_union = set.union(*[peninsula_sets[n] for n in peninsula])
admixed_union   = set.union(*[admixed_sets[n] for n in admixed])

#plt.figure(figsize=(4,4))
import pprint

figure, axes = plt.subplots(1,3)
pprint.pprint(axes)
venn3([admixed_union, centre_union, peninsula_union], set_labels=('Admixed', 'Centre', 'South'),ax=axes[0])
venn3([north_union, admixed_union, peninsula_union], set_labels=('North', 'Admixed', 'South'),ax=axes[1])
venn3([north_union, centre_union, admixed_union], set_labels=('North', 'Centre', 'Admixed'),ax=axes[2])

figure.set_size_inches(9,3)
figure.set_dpi(200)

plt.savefig('regiones_admixed_snp.svg')

