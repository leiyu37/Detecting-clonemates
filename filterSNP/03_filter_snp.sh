#!/bin/bash
#SBATCH --job-name=filterSNP
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100G
#SBATCH --time=02:00:00
#SBATCH --output=filterSNP.out
#SBATCH --error=filterSNP.err
#SBATCH --partition=cluster

cd /gxfs_work1/fs1/work-geomar/smomw353/A_projectNote/projectNote_v4/02_filter

/gxfs_home/geomar/smomw353/tools/gatk-4.1.1.0/gatk --java-options "-Xmx96G" VariantFiltration \
   -R /gxfs_work1/fs1/work-geomar/smomw353/A_newGenome/Zostera_marina.mainGenome.fasta \
   -V ./02_keepDiLoci.recode.vcf \
   -O ./05_markfilter_snp.vcf \
   --filter-expression "MQ < 40.0" \
   --filter-name "MQ_filter" \
   --filter-expression "FS > 60.0" \
   --filter-name "FS_filter" \
   --filter-expression "QD < 13.0" \
   --filter-name "QD_filter" \
   --filter-expression "MQRankSum > 2.5" \
   --filter-name "MQRankSum_L" \
   --filter-expression "MQRankSum < -2.5" \
   --filter-name "MQRankSum_S" \
   --filter-expression "ReadPosRankSum < -2.5" \
   --filter-name "ReadPosRankSum_S" \
   --filter-expression "ReadPosRankSum > 2.5" \
   --filter-name "ReadPosRankSum_L" \
   --filter-expression "SOR > 3.0" \
   --filter-name "SOR_F" \
   --filter-expression "DP > 1192.45" \
   --filter-name "DP_F"

/gxfs_home/geomar/smomw353/tools/gatk-4.1.1.0/gatk --java-options "-Xmx96G" SelectVariants \
     -R /gxfs_work1/fs1/work-geomar/smomw353/A_newGenome/Zostera_marina.mainGenome.fasta \
     -V 05_markfilter_snp.vcf \
     -O 05_rmfilter_snp.vcf \
     --exclude-filtered true


vcftools --vcf 05_rmfilter_snp.vcf \
    --minGQ 30 \
    --minDP 20 \
    --recode \
    --recode-INFO-all \
    --out 06_rmLowGQDP

chmod 700 ./filterHomo.py
./filterHomo.py

vcftools --vcf ./07_HQsnp.vcf --mac 1 --recode --recode-INFO-all --out 00_final
