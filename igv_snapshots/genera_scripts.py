from sample_code_file_maps import *

from jinja2 import Environment, FileSystemLoader

regiones = [
    ','.join(['chr15', str(48791193-3000), str(48791193+3000)]),
    ','.join(['chr2', str(21231387-3000), str(21231387+3000)]),
    ','.join(['chr2', str(21233999-3000), str(21233999+3000)]),
]


env = Environment(loader=FileSystemLoader('.'))
template =env.get_template('snap.tt')

for region in regiones:
    (chrom,start,end) = region.split(',')
    for sample in ethnicity_code:
        script = open( "evidence_%s_%s.sh" % (sample, region.replace(',','_')), 'w' )
        script.write( template.render( region   = region, 
                                       evidence = evidence[ethnicity_code[sample]] % chrom,
                                       output   = "/export/home/rgarcia/non-coding-NGS/igv_snapshots/sam/%s_%s.sam" % (sample, region.replace(',','_')) ) )
