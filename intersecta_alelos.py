#!/usr/bin/env python

from sample_code_file_maps import ethnicity_code
from sample_code_file_maps import north, centre, peninsula, admixed
from sample_code_file_maps import mayas, nahuas, tarahumaras, tepehuanos, totonacas, zapotecas


def intersecta_grupo( grupo ):
    return set.intersection(*[set([v.strip() for v in open( "alleles/%s_snp_non_coding_ensembl.alleles" % ethnicity_code[s]).readlines()]) for s in grupo])

def write_allele_file( s, path):
    with open(path, 'w') as f:
        for a in s:
            c = a.split()
            if c[0] != 'chrM' and len(c[3])==1 and len(c[4])==1:
                f.write("%s,%s,%s,%s\n" % (c[0],c[2],c[3],c[4]))


write_allele_file( intersecta_grupo( north ), "north_nc_ensembl_alleles.csv" )
write_allele_file( intersecta_grupo( centre ), "centre_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( peninsula ), "peninsula_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( admixed ), "admixed_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( mayas ), "mayas_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( nahuas ), "nahuas_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( tarahumaras ), "tarahumaras_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( tepehuanos ), "tepehuanos_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( totonacas ), "totonacas_nc_ensembl_alleles.csv"  )
write_allele_file( intersecta_grupo( zapotecas ), "zapotecas_nc_ensembl_alleles.csv"  )

