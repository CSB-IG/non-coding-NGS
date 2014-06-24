#!/bin/bash

SINBAD=$1
CIRCOS=`basename $SINBAD .csv`.tsv
OUTDIR=`dirname $SINBAD`

cat $SINBAD | awk -F "," '{print $1,$2,$2+1,$5}' | sed -e 's/chr/hs/g' > $OUTDIR/$CIRCOS
