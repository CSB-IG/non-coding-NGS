import matplotlib
matplotlib.rcParams.update({'font.size': 8})

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3

from venn3_utils import siete_regiones

from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
north_sets = {}
for s in north:
    north_sets[s] = set([v.strip() for v in open( "maps/%s_indel.map" % ethnicity_code[s]).readlines()])


centre_sets = {}
for s in centre:
    centre_sets[s] = set([v.strip() for v in open( "maps/%s_indel.map" % ethnicity_code[s]).readlines()])


peninsula_sets = {}
for s in peninsula:
    peninsula_sets[s] = set([v.strip() for v in open( "maps/%s_indel.map" % ethnicity_code[s]).readlines()])


admixed_sets = {}
for s in admixed:
    admixed_sets[s] = set([v.strip() for v in open( "maps/%s_indel.map" % ethnicity_code[s]).readlines()])


north_union     = set.union(*[north_sets[n] for n in north])
centre_union    = set.union(*[centre_sets[n] for n in centre])
peninsula_union = set.union(*[peninsula_sets[n] for n in peninsula])
admixed_union   = set.union(*[admixed_sets[n] for n in admixed])


figure, axes = plt.subplots(1,3)
figure.set_size_inches(10,30)
venn3(siete_regiones(admixed_union, centre_union, peninsula_union),
      set_labels=('Admixed', 'Centre', 'South'),
      ax=axes[0])
venn3(siete_regiones(north_union, admixed_union, peninsula_union),
      set_labels=('North', 'Admixed', 'South'),
      ax=axes[1])
venn3(siete_regiones(north_union, centre_union, admixed_union),
      set_labels=('North', 'Centre', 'Admixed'),
      ax=axes[2])

figure.set_size_inches(9,3)
figure.set_dpi(200)

plt.savefig('regiones_admixed_indel.png')





