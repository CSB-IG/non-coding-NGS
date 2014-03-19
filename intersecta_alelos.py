#!/usr/bin/env python

from sample_code_file_maps import ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas


def intersecta_grupo( grupo ):
    return set.intersection(*[set([v.strip() for v in open( "maps/%s_indel.map" % ethnicity_code[s]).readlines()]) for s in grupo])

def write_allele_file( s, path):
    with open(path, 'w') as f:
        for a in s:
            c = a.split()
            f.write("%s,%s,%s,%s\n" % (c[0],c[2],c[3],c[4]))


write_allele_file( intersecta_grupo( north ), "north.csv" )
write_allele_file( intersecta_grupo( centre ), "centre.csv"  )
write_allele_file( intersecta_grupo( peninsula ), "peninsula.csv"  )
write_allele_file( intersecta_grupo( admixed ), "admixed.csv"  )
write_allele_file( intersecta_grupo( mayas ), "mayas.csv"  )
write_allele_file( intersecta_grupo( nahuas ), "nahuas.csv"  )
write_allele_file( intersecta_grupo( tarahumaras ), "tarahumaras.csv"  )
write_allele_file( intersecta_grupo( tepehuanos ), "tepehuanos.csv"  )
write_allele_file( intersecta_grupo( totonacas ), "totonacas.csv"  )
write_allele_file( intersecta_grupo( zapotecas ), "zapotecas.csv"  )

