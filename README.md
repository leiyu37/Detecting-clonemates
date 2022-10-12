# Detecting clonemate pairs based on "Shared Heterozygosity(SH)" and technical replicates
## Example dataset
        data/all.vcf
This file includes 18021 bi-allelic SNPs for 133 individuals, including four technical replicates (coded a & b at the end of sample names). 
(Edgeloe, Jane M., et al. "Extensive polyploid clonality was a successful strategy for seagrass to expand into a newly submerged environment." Proceedings of the Royal Society B 289.1976 (2022): 20220538.)

## Generate a bash script
        ./generateAllPairs.py /path/to/SH_pair.py path/to/vcf
### For example:
        ./generateAllPairs.py ./SH_pair.py ./data/all.vcf
### The output is: [allPairs.sh](output/allPairs.sh)
