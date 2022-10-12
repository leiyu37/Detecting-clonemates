#!/usr/bin/env python3
import sys

vcf_path = sys.argv[1]
sampleX1 = sys.argv[2]
sampleX2 = sys.argv[3]
out_path = sys.argv[4]

def sh_pair(vcf_path, sampleX1, sampleX2, out_path):
    """
    Calculate n_sh, sh_x1, sh_x2, sh.

    n_x1, for each locus in the vcf file, if both sampleX1 and sampleX2 have available genotype calls (not missing data), and sampleX1 is heterozygous, n_x1 + 1.
    n_x2, for each locus in the vcf file, if both sampleX1 and sampleX2 have available genotype calls (not missing data), and sampleX2 is heterozygous, n_x2 + 1.
    n_sh, for each locus in the vcf file, if sampleX1 and sampleX2 are identically heterozygous, n_sh + 1.

    sh_x1 = n_sh/n_x1
    sh_x2 = n_sh/n_x2

    sh = min(sh_x1, sh_x2)
    """

    sample_i_dict = {}
    f_in = open(vcf_path)
    for line in f_in.readlines():
        if line.startswith("#CHROM"):
            columns = line.split()
            for i in range(9, len(columns)):
                sample_i_dict[columns[i]] = i
            break
    f_in.close()

    n_x1 = 0
    n_x2 = 0
    n_sh = 0

    f_in = open(vcf_path)
    for line in f_in.readlines():
        if not line.startswith("#"):
            columns = line.split()
            genoX1 = columns[sample_i_dict[sampleX1]][0] + columns[sample_i_dict[sampleX1]][2]
            genoX2 = columns[sample_i_dict[sampleX2]][0] + columns[sample_i_dict[sampleX2]][2]
            if (genoX1 in ["00", "01", "10", "11"]) and (genoX2 in ["00", "01", "10", "11"]):
                if genoX1 == "01" or genoX1 == "10":
                    n_x1 += 1
                if genoX2 == "01" or genoX2 == "10":
                    n_x2 += 1
                if (genoX1 == "01" or genoX1 == "10") and (genoX2 == "01" or genoX2 == "10"):
                    n_sh += 1         
    f_in.close()

    sh_x1 = round(n_sh/n_x1, 4)
    sh_x2 = round(n_sh/n_x2, 4)

    sh = round(min(sh_x1, sh_x2), 4)

    f_out = open(out_path, "w")
    f_out.write("X1\tX2\tNSH\tSHX1\tSHX2\tSH\n")
    f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(sampleX1,sampleX2,n_sh,sh_x1,sh_x2,sh))
    f_out.close()

#run the calculation
sh_pair(vcf_path, sampleX1, sampleX2, out_path)
