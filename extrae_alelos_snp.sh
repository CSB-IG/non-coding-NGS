bzcat /amerindio1/GS000033659-DID/GS000033834-ASM/GS02379-DNA_C01/ASM/masterVarBeta-GS000033834-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033834_snp.alleles &
bzcat /amerindio1/GS000033660-DID/GS000033835-ASM/GS02379-DNA_D01/ASM/masterVarBeta-GS000033835-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033835_snp.alleles &
bzcat /amerindio1/GS000033661-DID/GS000033836-ASM/GS02379-DNA_E01/ASM/masterVarBeta-GS000033836-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033836_snp.alleles &
bzcat /amerindio1/GS000033662-DID/GS000033837-ASM/GS02379-DNA_F01/ASM/masterVarBeta-GS000033837-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033837_snp.alleles &
bzcat /amerindio1/GS000033663-DID/GS000033838-ASM/GS02379-DNA_G01/ASM/masterVarBeta-GS000033838-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033838_snp.alleles &
bzcat /amerindio1/GS000033664-DID/GS000033839-ASM/GS02379-DNA_H01/ASM/masterVarBeta-GS000033839-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033839_snp.alleles &
bzcat /amerindio1/GS000033673-DID/GS000034176-ASM/GS02379-DNA_A03/ASM/masterVarBeta-GS000034176-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000034176_snp.alleles &
bzcat /amerindio2/GS000033657-DID/GS000033832-ASM/GS02379-DNA_A01/ASM/masterVarBeta-GS000033832-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033832_snp.alleles &
bzcat /amerindio2/GS000033658-DID/GS000033833-ASM/GS02379-DNA_B01/ASM/masterVarBeta-GS000033833-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033833_snp.alleles &
bzcat /amerindio2/GS000033665-DID/GS000033840-ASM/GS02379-DNA_A02/ASM/masterVarBeta-GS000033840-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033840_snp.alleles &
bzcat /amerindio2/GS000033666-DID/GS000033841-ASM/GS02379-DNA_B02/ASM/masterVarBeta-GS000033841-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033841_snp.alleles &
bzcat /amerindio2/GS000033667-DID/GS000033842-ASM/GS02379-DNA_C02/ASM/masterVarBeta-GS000033842-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033842_snp.alleles &
bzcat /amerindio2/GS000033668-DID/GS000033843-ASM/GS02379-DNA_D02/ASM/masterVarBeta-GS000033843-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033843_snp.alleles &
bzcat /amerindio2/GS000033669-DID/GS000033844-ASM/GS02379-DNA_E02/ASM/masterVarBeta-GS000033844-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033844_snp.alleles &
bzcat /amerindio2/GS000033670-DID/GS000033845-ASM/GS02379-DNA_F02/ASM/masterVarBeta-GS000033845-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033845_snp.alleles &
bzcat /amerindio2/GS000033671-DID/GS000033846-ASM/GS02379-DNA_G02/ASM/masterVarBeta-GS000033846-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033846_snp.alleles &
bzcat /amerindio2/GS000033672-DID/GS000033847-ASM/GS02379-DNA_H02/ASM/masterVarBeta-GS000033847-ASM.tsv.bz2  | grep -P "\tsnp\t" | awk '{if ($6=="hom") {print $3,$4,$5,$9,$10;} else {print $3,$4,$5,$8,$9;}}' > GS000033847_snp.alleles &
