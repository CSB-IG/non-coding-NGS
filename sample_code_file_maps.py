snps = ['GS000033832_snp.map',
        'GS000033833_snp.map',
        'GS000033834_snp.map',
        'GS000033835_snp.map',
        'GS000033836_snp.map',
        'GS000033837_snp.map',
        'GS000033838_snp.map',
        'GS000033839_snp.map',
        'GS000033840_snp.map',
        'GS000033841_snp.map',
        'GS000033842_snp.map',
        'GS000033843_snp.map',
        'GS000033844_snp.map',
        'GS000033845_snp.map',
        'GS000033846_snp.map',
        'GS000033847_snp.map',
        'GS000034176_snp.map',]

indels = ['GS000033832_indel.map',
          'GS000033833_indel.map',
          'GS000033834_indel.map',
          'GS000033835_indel.map',
          'GS000033836_indel.map',
          'GS000033837_indel.map',
          'GS000033838_indel.map',
          'GS000033839_indel.map',
          'GS000033840_indel.map',
          'GS000033841_indel.map',
          'GS000033842_indel.map',
          'GS000033843_indel.map',
          'GS000033844_indel.map',
          'GS000033845_indel.map',
          'GS000033846_indel.map',
          'GS000033847_indel.map',
          'GS000034176_indel.map',]


sample_code = { 'B01': 'GS000033833',
                'C01': 'GS000033834',
                'F01': 'GS000033837',
                'G01': 'GS000033838',
                'H01': 'GS000033839',
                'A02': 'GS000033840',
                'B02': 'GS000033841',
                'C02': 'GS000033842',
                'D02': 'GS000033843',
                'E02': 'GS000033844',
                'F02': 'GS000033845',
                'G02': 'GS000033846',
                'H02': 'GS000033847',
                'A03': 'GS000034176', 
                'A01': 'GS000033832',
                'B01': 'GS000033833',
                'C01': 'GS000033834',
                'D01': 'GS000033835',
                'E01': 'GS000033836',}

sample_ethnicity = {
    'A01': ( 'm1', 'JATE' ),
    'B01': ( 'm2', 'PTL' ),
    'C01': ( 'm3', 'JPAM' ),
    'D01': ( 'm4', 'LACA' ),
    'E01': ( 'm5', 'JIAT' ),
    'F01': ( 'Tepehuano', 'TEP09' ),
    'G01': ( 'Tepehuano', 'TEP03' ),
    'H01': ( 'Zapoteca', 'CGM077' ),
    'A02': ( 'Zapoteca', 'CGM66' ),
    'B02': ( 'Maya', 'DZ5' ),
    'C02': ( 'Maya', 'APOM10' ),
    'D02': ( 'Nahua', 'AM1554' ),
    'E02': ( 'Nahua', 'AM1299' ),
    'F02': ( 'Totonaca', 'AM1346' ),
    'G02': ( 'Totonaca', 'AM1343' ),
    'H02': ( 'Tarahumara', 'AM690' ),
    'A03': ( 'Tarahumara', 'AM642' ),}


ethnicity_code = {'Maya1'        : 'GS000033841',
                  'Maya2'        : 'GS000033842',
                  'Nahua1'       : 'GS000033843',
                  'Nahua2'       : 'GS000033844',
                  'Tarahumara1'  : 'GS000034176',
                  'Tarahumara2'  : 'GS000033847',
                  'Tepehuana1'   : 'GS000033837',
                  'Tepehuana2'   : 'GS000033838',
                  'Totonaca1'    : 'GS000033845',
                  'Totonaca2'    : 'GS000033846',
                  'Zapoteca1'    : 'GS000033840',
                  'Zapoteca2'    : 'GS000033839',
                  'm1'           : 'GS000033832',
                  'm2'           : 'GS000033833',
                  'm3'           : 'GS000033834',
                  'm4'           : 'GS000033835',
                  'm5'           : 'GS000033836'}

north     = [ 'Tarahumara1' , 'Tarahumara2', 'Tepehuana1', 'Tepehuana2' ]
centre    = [ 'Nahua1', 'Nahua2', 'Zapoteca1', 'Zapoteca2', 'Totonaca1', 'Totonaca2' ]
peninsula = [ 'Maya1', 'Maya2' ]
admixed   = [ 'm2', 'm3', ]

mayas       = ['Maya1', 'Maya2']
nahuas      = ['Nahua1', 'Nahua2']
tarahumaras = ['Tarahumara1','Tarahumara2']
tepehuanos  = ['Tepehuana1','Tepehuana2']
totonacas   = ['Totonaca1', 'Totonaca2']
zapotecas   = ['Zapoteca1','Zapoteca2']


linguistic_groups = {
    'mayas' : ['Maya1', 'Maya2'],
    'nahuas' : ['Nahua1', 'Nahua2'],
    'tarahumaras' : ['Tarahumara1','Tarahumara2'],
    'tepehuanos' : ['Tepehuana1','Tepehuana2'],
    'totonacas' : ['Totonaca1', 'Totonaca2'],
    'zapotecas' : ['Zapoteca1','Zapoteca2'],
}


evidence = {
    'GS000033834' : '/amerindio1/GS000033659-DID/GS000033834-ASM/GS02379-DNA_C01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033834-ASM.tsv.bz2',
    'GS000033835' : '/amerindio1/GS000033660-DID/GS000033835-ASM/GS02379-DNA_D01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033835-ASM.tsv.bz2',
    'GS000033836' : '/amerindio1/GS000033661-DID/GS000033836-ASM/GS02379-DNA_E01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033836-ASM.tsv.bz2',
    'GS000033837' : '/amerindio1/GS000033662-DID/GS000033837-ASM/GS02379-DNA_F01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033837-ASM.tsv.bz2',
    'GS000033838' : '/amerindio1/GS000033663-DID/GS000033838-ASM/GS02379-DNA_G01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033838-ASM.tsv.bz2',
    'GS000033839' : '/amerindio1/GS000033664-DID/GS000033839-ASM/GS02379-DNA_H01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033839-ASM.tsv.bz2',
    'GS000034176' : '/amerindio1/GS000033673-DID/GS000034176-ASM/GS02379-DNA_A03/ASM/EVIDENCE/evidenceDnbs-%s-GS000034176-ASM.tsv.bz2',
    'GS000033832' : '/amerindio2/GS000033657-DID/GS000033832-ASM/GS02379-DNA_A01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033832-ASM.tsv.bz2',
    'GS000033833' : '/amerindio2/GS000033658-DID/GS000033833-ASM/GS02379-DNA_B01/ASM/EVIDENCE/evidenceDnbs-%s-GS000033833-ASM.tsv.bz2',
    'GS000033840' : '/amerindio2/GS000033665-DID/GS000033840-ASM/GS02379-DNA_A02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033840-ASM.tsv.bz2',
    'GS000033841' : '/amerindio2/GS000033666-DID/GS000033841-ASM/GS02379-DNA_B02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033841-ASM.tsv.bz2',
    'GS000033842' : '/amerindio2/GS000033667-DID/GS000033842-ASM/GS02379-DNA_C02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033842-ASM.tsv.bz2',
    'GS000033843' : '/amerindio2/GS000033668-DID/GS000033843-ASM/GS02379-DNA_D02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033843-ASM.tsv.bz2',
    'GS000033844' : '/amerindio2/GS000033669-DID/GS000033844-ASM/GS02379-DNA_E02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033844-ASM.tsv.bz2',
    'GS000033845' : '/amerindio2/GS000033670-DID/GS000033845-ASM/GS02379-DNA_F02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033845-ASM.tsv.bz2',
    'GS000033846' : '/amerindio2/GS000033671-DID/GS000033846-ASM/GS02379-DNA_G02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033846-ASM.tsv.bz2',
    'GS000033847' : '/amerindio2/GS000033672-DID/GS000033847-ASM/GS02379-DNA_H02/ASM/EVIDENCE/evidenceDnbs-%s-GS000033847-ASM.tsv.bz2',
}
