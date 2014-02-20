import matplotlib
matplotlib.rcParams.update({'font.size': 8})

from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn3


from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
tarahumaras_sets = {}
for s in tarahumaras:
    tarahumaras_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])

tepehuanos_sets = {}
for s in tepehuanos:
    tepehuanos_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])

totonacas_sets = {}
for s in totonacas:
    totonacas_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])

nahuas_sets = {}
for s in nahuas:
    nahuas_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])


zapotecas_sets = {}
for s in zapotecas:
    zapotecas_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])

mayas_sets = {}
for s in mayas:
    mayas_sets[s] = set([v.strip() for v in open( "%s_snp.map" % ethnicity_code[s]).readlines()])



figure, axes = plt.subplots(6,1)

venn2([tarahumaras_sets['Tarahumara1'], tarahumaras_sets['Tarahumara2']], set_labels=('Tarahumara 1', 'Tarahumara 2'),ax=axes[0])
venn2([tepehuanos_sets['Tepehuana1'], tepehuanos_sets['Tepehuana2']], set_labels=('Tepehuana 1', 'Tepehuana 2'),ax=axes[1])
venn2([totonacas_sets['Totonaca1'], totonacas_sets['Totonaca2']], set_labels=('Totonaca 1', 'Totonaca 2'),ax=axes[2])

venn2([nahuas_sets['Nahua1'], nahuas_sets['Nahua2']], set_labels=('Nahua 1', 'Nahua 2'),ax=axes[3])
venn2([zapotecas_sets['Zapoteca1'], zapotecas_sets['Zapoteca2']], set_labels=('Zapoteca 1', 'Zapoteca 2'),ax=axes[4])
venn2([mayas_sets['Maya1'], mayas_sets['Maya2']], set_labels=('Maya 1', 'Maya 2'),ax=axes[5])

figure.set_size_inches(3,15.4)
figure.set_dpi(400)

plt.savefig('pares_snp.svg')
