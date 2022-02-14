#!/usr/bin/env python3
import sys

vcf_path = sys.argv[1]
sampleA = sys.argv[2]
sampleB = sys.argv[3]
out_path = sys.argv[4]

def similarity(vcf_path, sampleA, sampleB, out_path):
    """
    Calculate n_ibh, ibh_a, ibh_b, ibh_s.

    n_a, for each locus in the vcf file, if both sampleA and sampleB have available genotype calls (not missing data), and sampleA is heterozygous, n_a + 1.
    n_b, for each locus in the vcf file, if both sampleA and sampleB have available genotype calls (not missing data), and sampleB is heterozygous, n_b + 1.
    n_ibh, for each locus in the vcf file, if sampleA and sampleB are identically heterozygous, n_ibh + 1.

    ibh_a = n_ibh/n_a
    ibh_b = n_ibh/n_b

    ibh_s = min(ibh_a, ibh_b)
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

    n_a = 0
    n_b = 0
    n_ibh = 0

    f_in = open(vcf_path)
    for line in f_in.readlines():
        if not line.startswith("#"):
            columns = line.split()
            genoA = columns[sample_i_dict[sampleA]][0] + columns[sample_i_dict[sampleA]][2]
            genoB = columns[sample_i_dict[sampleB]][0] + columns[sample_i_dict[sampleB]][2]
            if (genoA in ["00", "01", "10", "11"]) and (genoB in ["00", "01", "10", "11"]):
                if genoA == "01" or genoA == "10":
                    n_a += 1
                if genoB == "01" or genoB == "10":
                    n_b += 1
                if (genoA == "01" or genoA == "10") and (genoB == "01" or genoB == "10"):
                    n_ibh += 1         
    f_in.close()

    ibh_a = round(n_ibh/n_a, 4)
    ibh_b = round(n_ibh/n_b, 4)

    ibh_s = round(min(ibh_a, ibh_b), 4)

    f_out = open(out_path, "w")
    f_out.write("SampleA\tSampleB\tN_IBH\tIBH_A\tIBH_B\tIBHs\n")
    f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(sampleA,sampleB,n_ibh,ibh_a,ibh_b,ibh_s))
    f_out.close()

#run the calculation
similarity(vcf_path, sampleA, sampleB, out_path)
