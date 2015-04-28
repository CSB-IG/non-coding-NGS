from sh import cgatools, samtools

evidence="/amerindio2/GS000033669-DID/GS000033844-ASM/GS02379-DNA_E02/ASM/EVIDENCE/evidenceDnbs-chr%s-GS000033844-ASM.tsv.bz2"
output="/export/home/rgarcia/non-coding-NGS/psmc/sam/nahua2_chr%s.bam"
reference='/export/home/rgarcia/reference/ucsc.hg19.crr'


for ch in range(1,23)+['M','X']:
    samtools.sort( cgatools.evidence2sam( beta=True,
                                          reference=reference,
                                          evidence_dnbs=evidence % ch,
                                          _piped=True ),
                   "-", O='bam', T='/scratch/tmp',
                   o=output % ch)
