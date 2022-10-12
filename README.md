# Detecting clonemate pairs based on "Shared Heterozygosity(SH)" and technical replicates
## 1. Requirements
* A vcf file containing bi-allelic SNPs
* [SH_pair.py](SH_pair.py)
## 1. Example dataset
        data/all.vcf
This file includes 18,021 bi-allelic SNPs for 133 individuals, including four technical replicates (coded a & b at the end of sample names).  
(Edgeloe, Jane M., et al. "Extensive polyploid clonality was a successful strategy for seagrass to expand into a newly submerged environment." Proceedings of the Royal Society B 289.1976 (2022): 20220538.)
## 2. Generating a bash script
        ./generateAllPairs.py /path/to/SH_pair.py path/to/vcf
For example:

        ./generateAllPairs.py ./SH_pair.py ./data/all.vcf

The output is: [allPairs.sh](output/allPairs.sh)

## 3. Calculating pairwise SH indices
        ./SH_pair.py /path/to/vcf sampleX1 sampleX2 /path/to/output
#### For example:
        ./SH_pair.py ./data/all.vcf DH12 DH15 DH12_DH15_SH.txt
#### The output is: [DH12_DH15_SH.txt](output/DH12_DH15_SH.txt)
#### X1: name of the first sample
#### X2: name of the second sample
#### NSH: the number of the SNPs 
#### SHX1	
#### SHX2	
#### SH
