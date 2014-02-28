import matplotlib
matplotlib.rcParams.update({'font.size': 8})

from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
north_sets = {}
for s in north:
    north_sets[s] = set([v.strip() for v in open( "maps/%s_snp.map" % ethnicity_code[s]).readlines()])


centre_sets = {}
for s in centre:
    centre_sets[s] = set([v.strip() for v in open( "maps/%s_snp.map" % ethnicity_code[s]).readlines()])


peninsula_sets = {}
for s in peninsula:
    peninsula_sets[s] = set([v.strip() for v in open( "maps/%s_snp.map" % ethnicity_code[s]).readlines()])

north_union = set.union(*[north_sets[n] for n in north])
centre_union = set.union(*[centre_sets[n] for n in centre])
peninsula_union = set.union(*[peninsula_sets[n] for n in peninsula])

from decimal import Decimal

just_north = Decimal(len(north_union - centre_union.union(peninsula_union)))
just_centre = Decimal(len(centre_union - north_union.union(peninsula_union)))
just_peninsula = Decimal(len(peninsula_union - north_union.union(centre_union)))

nIcIp = set.intersection(centre_union, north_union, peninsula_union)

pIc = Decimal(len(peninsula_union.intersection( centre_union) - nIcIp))
pIn = Decimal(len(peninsula_union.intersection( north_union) - nIcIp))
cIn = Decimal(len(centre_union.intersection( north_union) - nIcIp))

nIcIp = Decimal(len(nIcIp))


total = Decimal(just_north + just_centre + cIn + just_peninsula + pIn + pIc + nIcIp)


from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3
plt.figure(figsize=(4,4))
v = venn3([float("%.2f" % (just_north/total)),
           float("%.2f" % (just_centre/total)),
           float("%.2f" % (cIn/total)),
           float("%.2f" % (just_peninsula/total)),
           float("%.2f" % (pIn/total)),
           float("%.2f" % (pIc/total)),
           float("%.2f" % (nIcIp/total))], set_labels=('North', 'Centre', 'South'))
plt.savefig('regiones_snp.png')
