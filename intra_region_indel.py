from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn3


from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
tarahumaras_sets = {}
for s in tarahumaras:
    tarahumaras_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


tepehuanos_sets = {}
for s in tepehuanos:
    tepehuanos_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


nahuas_sets = {}
for s in nahuas:
    nahuas_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


totonacas_sets = {}
for s in totonacas:
    totonacas_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


zapotecas_sets = {}
for s in zapotecas:
    zapotecas_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])


tarahumaras_u   = set.union(*[tarahumaras_sets[n] for n in tarahumaras])
tepehuanos_u    = set.union(*[tepehuanos_sets[n] for n in tepehuanos])

nahuas_u    = set.union(*[nahuas_sets[n] for n in nahuas])
totonacas_u    = set.union(*[totonacas_sets[n] for n in totonacas])
zapotecas_u    = set.union(*[zapotecas_sets[n] for n in zapotecas])


figure, axes = plt.subplots(1,2)
venn2([tarahumaras_u, tepehuanos_u], set_labels=('Tarahumara', 'Tepehuano'),ax=axes[0])
venn3([nahuas_u, totonacas_u, zapotecas_u], set_labels=('Nahua', 'Totonaca', 'Zapoteca'),ax=axes[1])
plt.savefig('centro_norte_intraregion_indel.svg')
