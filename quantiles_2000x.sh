#!/bin/bash

mincoverage=2000
minreads=0
quantiles="0.25 0.5 0.75 0.9 0.95"

outputdir=quantiles-mincov_${mincoverage}_minreads_${minreads}

mkdir $outputdir

for i in *.tsv
do
  quantile $i ${outputdir}/${i}.quant.txt $mincoverage $minreads $quantiles
done
