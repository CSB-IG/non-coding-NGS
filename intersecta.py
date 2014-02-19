from sample_code_file_maps import snps, indels, ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas



# load indels into a dictionary of sets
# maya_sets = {}
# for maya in mayas:
#     maya_sets[maya] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[maya]).readlines()])



# load indels into a dictionary of sets
north_sets = {}
for s in north:
    north_sets[s] = set([v.strip() for v in open( "%s_indel.map" % ethnicity_code[s]).readlines()])

north_union = set.union(*[north_sets[n] for n in north])
