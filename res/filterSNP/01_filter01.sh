#!/bin/bash

bcftools filter --SnpGap 20 -o 01_indelDistance_snp.vcf -O v 02_CA_raw.vcf

chmod 700 02_selectSNP.py
./02_selectSNP.py

./gatk-4.1.1.0/gatk  --java-options "-Xmx96G" VariantsToTable \
-R Zostera_marina.mainGenome.fasta \
-V ./02_keepDiLoci.recode.vcf \
-O ./03_Rtable.txt \
-F CHROM -F POS -F FILTER -F QD -F MQ -F FS -F SOR -F MQRankSum -F ReadPosRankSum -F DP
