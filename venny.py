#coding: utf-8

from decimal import Decimal

def fifteen_sections(a, b, c, d):
    return { 'A_BuCuD': a - set.union(b,c,d),
             'B_AuCuD': b - set.union(a,c,d),
             'C_AuBuD': c - set.union(a,b,d),
             'D_AuBuC': d - set.union(a,b,c),

             'AiB_CuD': set.intersection(a,b) - set.union(c,d),
             'AiC_BuD': set.intersection(a,c) - set.union(b,d),
             'AiD_BuC': set.intersection(a,d) - set.union(b,c),
             'BiC_AuD': set.intersection(b,c) - set.union(a,d),
             'BiD_AuC': set.intersection(b,d) - set.union(a,c),
             'CiD_AuB': set.intersection(c,d) - set.union(a,b),

             'AiBiC_D': set.intersection(a,b,c) - d,
             'BiCiD_A': set.intersection(b,c,d) - a,
             'AiCiD_B': set.intersection(a,c,d) - b,
             'AiBiD_C': set.intersection(a,b,d) - c,

             'AiBiCiD': set.intersection(a,b,c,d), }



def fifteen_normalized_sections(a, b, c, d):
    union = Decimal(len(set.union(a,b,c,d)))

    return { 'A_BuCuD': len(a - set.union(b,c,d))/union,
             'B_AuCuD': len(b - set.union(a,c,d))/union,
             'C_AuBuD': len(c - set.union(a,b,d))/union,
             'D_AuBuC': len(d - set.union(a,b,c))/union,

             'AiB_CuD': len(set.intersection(a,b) - set.union(c,d))/union,
             'AiC_BuD': len(set.intersection(a,c) - set.union(b,d))/union,
             'AiD_BuC': len(set.intersection(a,d) - set.union(b,c))/union,
             'BiC_AuD': len(set.intersection(b,c) - set.union(a,d))/union,
             'BiD_AuC': len(set.intersection(b,d) - set.union(a,c))/union,
             'CiD_AuB': len(set.intersection(c,d) - set.union(a,b))/union,

             'AiBiC_D': len(set.intersection(a,b,c) - d)/union,
             'BiCiD_A': len(set.intersection(b,c,d) - a)/union,
             'AiCiD_B': len(set.intersection(a,c,d) - b)/union,
             'AiBiD_C': len(set.intersection(a,b,d) - c)/union,

             'AiBiCiD': len(set.intersection(a,b,c,d))/union }



regiones_admixed_indel = {'A_BuCuD': "%0.2f" % Decimal('0.2009763449790980279980426635'),
                          'AiB_CuD': "%0.2f" % Decimal('0.04127424345606374992558346196'),
                          'AiBiC_D': "%0.2f" % Decimal('0.03119541274679065066916803036'),
                          'AiBiCiD': "%0.2f" % Decimal('0.1118484196831380110964133407'),
                          'AiBiD_C': "%0.2f" % Decimal('0.02820132686502364630872190866'),
                          'AiC_BuD': "%0.2f" % Decimal('0.009013621493529028257956035435'),
                          'AiCiD_B': "%0.2f" % Decimal('0.003791540763564501351113924823'),
                          'AiD_BuC': "%0.2f" % Decimal('0.01065238256344282123622931039'),
                          'B_AuCuD': "%0.2f" % Decimal('0.3008074738888703351720873367'),
                          'BiC_AuD': "%0.2f" % Decimal('0.01807457916540219053247392517'),
                          'BiCiD_A': "%0.2f" % Decimal('0.009450392120704350717520629716'),
                          'BiD_AuC': "%0.2f" % Decimal('0.01855665312890686824715293216'),
                          'C_AuBuD': "%0.2f" % Decimal('0.1002478615228019532707702003'),
                          'CiD_AuB': "%0.2f" % Decimal('0.004575636969264880766555683173'),
                          'D_AuBuC': "%0.2f" % Decimal('0.1113341106533989844502106170'),
                          'A': 'north',
                          'B': 'centre',
                          'C': 'penninsula',
                          'D': 'admixed',}



regiones_admixed_snp = {'A_BuCuD': "%0.2f" % Decimal('0.1089225491271139596867859756'),
                        'AiB_CuD': "%0.2f" % Decimal('0.04745295411669661699313641460'),
                        'AiBiC_D': "%0.2f" % Decimal('0.06028452437165856180248002130'),
                        'AiBiCiD': "%0.2f" % Decimal('0.3361779429832315469809847130'),
                        'AiBiD_C': "%0.2f" % Decimal('0.05403769936735063813217381185'),
                        'AiC_BuD': "%0.2f" % Decimal('0.008754819839275284155121058250'),
                        'AiCiD_B': "%0.2f" % Decimal('0.006444989493142009305115127861'),
                        'AiD_BuC': "%0.2f" % Decimal('0.01364895681110705805738378117'),
                        'B_AuCuD': "%0.2f" % Decimal('0.1540504552971795967783444593'),
                        'BiC_AuD': "%0.2f" % Decimal('0.01868631825821135009208886184'),
                        'BiCiD_A': "%0.2f" % Decimal('0.01654052469391363116564581930'),
                        'BiD_AuC': "%0.2f" % Decimal('0.02118580913995940481278994564'),
                        'C_AuBuD': "%0.2f" % Decimal('0.04927291199974935716827309327'),
                        'CiD_AuB': "%0.2f" % Decimal('0.004894696442438307176217575881'),
                        'D_AuBuC': "%0.2f" % Decimal('0.09964484805897267769345934103'),
                        'A': 'north',
                        'B': 'centre',
                        'C': 'penninsula',
                        'D': 'admixed',}

def render_four_set_venn( section_texts ):
    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader('templates/'))
    template = env.get_template('four_set_venn.svg')
    
    return template.render( section_texts )

