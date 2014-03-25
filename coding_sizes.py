
gmap = open('maps/all_genes_sorted.map', 'r').readlines()

coding_length = {}
for g in gmap:
    (chrom, start, end) = g.strip().split()
    if chrom in coding_length:
        coding_length[chrom] += (int(end) - int(start))
    else:
        coding_length[chrom] = (int(end) - int(start))


coding_length['Y'] = 0

# genes per chromosome, in order
gene_count = {
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


print "chr length coding_length gene_count"
for nn in range(1,23) + ['X', 'Y']:
    n = str(nn)
    print "%s %s %s %s" % (n,
                           chromosome_length[n],
                           coding_length[n],
                           gene_count[n],)


                           
