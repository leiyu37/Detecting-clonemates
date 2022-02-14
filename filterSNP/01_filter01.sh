#!/bin/bash
#SBATCH --job-name=filter01
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100G
#SBATCH --time=48:00:00
#SBATCH --output=filter01.out
#SBATCH --error=filter01.err
#SBATCH --partition=cluster

cd /gxfs_work1/geomar/smomw353/A_projectNote/projectNote_v4/02_filter


bcftools filter --SnpGap 20 -o 01_indelDistance_snp.vcf -O v /gxfs_work1/geomar/smomw353/A_projectNote/projectNote_v4/01_combine/02_CA_raw.vcf

chmod 700 02_selectSNP.py
./02_selectSNP.py

/gxfs_home/geomar/smomw353/tools/gatk-4.1.1.0/gatk  --java-options "-Xmx96G" VariantsToTable \
-R /gxfs_work1/fs1/work-geomar/smomw353/A_newGenome/Zostera_marina.mainGenome.fasta \
-V ./02_keepDiLoci.recode.vcf \
-O ./03_Rtable.txt \
-F CHROM -F POS -F FILTER -F QD -F MQ -F FS -F SOR -F MQRankSum -F ReadPosRankSum -F DP
