bzcat ./Genomas/GS000033657-DID/GS000033832-ASM/GS02379-DNA_A01/ASM/masterVarBeta-GS000033832-ASM.tsv.bz2 | grep -P "\t(ins|del)\t" | awk '{print $3,$4,$5}' > 33832_indel.map
bzcat ./Genomas/GS000033658-DID/GS000033833-ASM/GS02379-DNA_B01/ASM/masterVarBeta-GS000033833-ASM.tsv.bz2 | grep -P "\t(ins|del)\t" | awk '{print $3,$4,$5}' > 33833_indel.map
bzcat ./Genomas/GS000033659-DID/GS000033834-ASM/GS02379-DNA_C01/ASM/masterVarBeta-GS000033834-ASM.tsv.bz2 | grep -P "\t(ins|del)\t" | awk '{print $3,$4,$5}' > 33834_indel.map
bzcat ./Genomas/GS000033660-DID/GS000033835-ASM/GS02379-DNA_D01/ASM/masterVarBeta-GS000033835-ASM.tsv.bz2 | grep -P "\t(ins|del)\t" | awk '{print $3,$4,$5}' > 33835_indel.map
bzcat ./Genomas/GS000033661-DID/GS000033836-ASM/GS02379-DNA_E01/ASM/masterVarBeta-GS000033836-ASM.tsv.bz2 | grep -P "\t(ins|del)\t" | awk '{print $3,$4,$5}' > 33836_indel.map



