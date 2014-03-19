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



from venny import fifteen_normalized_sections

import pprint
pprint.pprint(fifteen_normalized_sections(north_union,
                                          centre_union,
                                          peninsula_union,
                                          admixed_union))
