
gmap = open('maps/all_genes_sorted.map', 'r').readlines()

coding_length = {}
for g in gmap:
    (chrom, start, end) = g.strip().split()
    if chrom in coding_length:
        coding_length[chrom] += (int(end) - int(start))
    else:
        coding_length[chrom] = (int(end) - int(start))


coding_length['Y'] = 0


ensembl_gmap = open('maps/ensembl_all_genes.tsv', 'r').readlines()
ensembl_all = {}
for g in ensembl_gmap:
    (chrom, start, end) = g.strip().split()
    if chrom in ensembl_all:
        ensembl_all[chrom] += (int(end) - int(start))
    else:
        ensembl_all[chrom] = (int(end) - int(start))



ensembl_coding_gmap = open('maps/ensembl_coding_genes.tsv', 'r').readlines()
coding_ensembl = {}
for g in ensembl_coding_gmap:
    (chrom, start, end) = g.strip().split()
    if chrom in coding_ensembl:
        coding_ensembl[chrom] += (int(end) - int(start))
    else:
        coding_ensembl[chrom] = (int(end) - int(start))



# golden helix genes per chromosome, in order
gh_gene_count = {
    '1': 2319,
    '2': 1463,
    '3': 1228,
    '4': 869,
    '5': 1003,
    '6': 1189,
    '7': 1110,
    '8': 807,
    '9': 944,
    '10': 898,
    '11': 1435,
    '12': 1163,
    '13': 396,
    '14': 766,
    '15': 802,
    '16': 939,
    '17': 1344,
    '18': 327,
    '19': 1612,
    '20': 645,
    '21': 291,
    '22': 539,
    'X': 1002,
    'Y': 0,
}


chromosome_length = {
    '1': 248956422,
    '2': 242193529,
    '3': 198295559,
    '4': 190214555,
    '5': 181538259,
    '6': 170805979,
    '7': 159345973,
    '8': 145138636,
    '9': 138394717,
    '10': 133797422,
    '11': 135086622,
    '12': 133275309,
    '13': 114364328,
    '14': 107043718,
    '15': 101991189,
    '16': 90338345,
    '17': 83257441,
    '18': 80373285,
    '19': 58617616,
    '20': 64444167,
    '21': 46709983,
    '22': 50818468,
    'X': 156040895,
    'Y': 57227415,
}    


ensembl_all_gene_count = {
    '1': 5363,
    '2': 4047,
    '3': 3101,
    '4': 2563,
    '5': 2859,
    '6': 2905,
    '7': 2876,
    '8': 2386,
    '9': 2323,
    '10': 2260,
    '11': 3208,
    '12': 2818,
    '13': 1217,
    '14': 2244,
    '15': 2080,
    '16': 2343,
    '17': 2903,
    '18': 1127,
    '19': 2910,
    '20': 1317,
    '21': 736,
    '22': 1263,
    'X': 2392,
    'Y': 495,
}

ensembl_coding_gene_count = {
    '1': 2076,
    '2': 1281,
    '3': 1078,
    '4': 767,
    '5': 893,
    '6': 1052,
    '7': 917,
    '8': 701,
    '9': 805,
    '10': 771,
    '11': 1317,
    '12': 1070,
    '13': 329,
    '14': 652,
    '15': 617,
    '16': 875,
    '17': 1208,
    '18': 288,
    '19': 1481,
    '20': 560,
    '21': 242,
    '22': 450,
    'X': 830,
    'Y': 54,
}

print "chr,length,golden_helix,ge_gene_count,ensembl_all,ensembl_all_gene_count,ensembl_coding,ensembl_coding_gene_count"
for nn in range(1,23) + ['X', 'Y']:
    n = str(nn)
    print ",".join([str(j) for j in [n,
                                    chromosome_length[n],
                                    coding_length[n],
                                    gh_gene_count[n],
                                    ensembl_all[n],
                                    ensembl_all_gene_count[n],
                                    coding_ensembl[n],
                                    ensembl_coding_gene_count[n]]] )

