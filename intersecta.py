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



# pIc = len(peninsula_union.intersection( centre_union))

# pIn = len(peninsula_union.intersection( north_union))

# cIn = len(centre_union.intersection( north_union))

# nIcIp = len(set.intersection(centre_union, north_union, peninsula_union))

# just_north = len(north_union - centre_union.union(peninsula_union))

# just_centre = len(centre_union - north_union.union(peninsula_union))

# just_peninsula = len(peninsula_union - north_union.union(centre_union))


from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3
plt.figure(figsize=(4,4))
v = venn3([north_union, centre_union, peninsula_union], set_labels=('Norte', 'Centro', 'Sur'))
plt.show()
