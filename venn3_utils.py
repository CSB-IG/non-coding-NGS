from decimal import Decimal

def siete_regiones(a, b, c):
    just_a = Decimal(len(a - b.union(c)))
    just_b = Decimal(len(b - a.union(c)))
    just_c = Decimal(len(c - a.union(b)))

    aIbIc = set.intersection(a, b, c)

    cIb = Decimal(len(c.intersection( b ) - aIbIc))
    cIa = Decimal(len(c.intersection( a ) - aIbIc))
    bIa = Decimal(len(b.intersection( a ) - aIbIc))

    aIbIc = Decimal(len(aIbIc))

    total = Decimal(just_a + just_b + bIa + just_c + cIa + cIb + aIbIc)

    return [float("%.2f" % (just_a/total)),
            float("%.2f" % (just_b/total)),
            float("%.2f" % (bIa/total)),
            float("%.2f" % (just_c/total)),
            float("%.2f" % (cIa/total)),
            float("%.2f" % (cIb/total)),
            float("%.2f" % (aIbIc/total))]
