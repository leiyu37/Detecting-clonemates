#!/usr/bin/env python3
import sys

def jaccard_similarity(A, B):
    #Find intersection of two sets
    nominator = A.intersection(B)

    #Find union of two sets
    denominator = A.union(B)

    #Take the ratio of sizes
    if len(denominator) > 0:
        similarity = round(len(nominator)/len(denominator), 4)
    else:
        similarity = 0.0
    
    return similarity

def jaccard_pair_het(vcf_path, sampleX1, sampleX2, out_path):
    sample_i_dict = {}
    f_in = open(vcf_path)
    for line in f_in.readlines():
        if line.startswith("#CHROM"):
            columns = line.split()
            for i in range(9, len(columns)):
                sample_i_dict[columns[i]] = i
            break
    f_in.close()

    set_x1 = set()
    set_x2 = set()

    f_in = open(vcf_path)
    for line in f_in.readlines():
        if not line.startswith("#"):
            columns = line.split()
            genoX1 = columns[sample_i_dict[sampleX1]][0] + columns[sample_i_dict[sampleX1]][2]
            genoX2 = columns[sample_i_dict[sampleX2]][0] + columns[sample_i_dict[sampleX2]][2]
            if (genoX1 in ["00", "01", "10", "11"]) and (genoX2 in ["00", "01", "10", "11"]):
                if genoX1 == "01" or genoX1 == "10" :
                    set_x1.add("{}_{}".format(columns[0], columns[1]))
                if genoX2 == "01" or genoX2 == "10" :
                    set_x2.add("{}_{}".format(columns[0], columns[1]))

    f_in.close()


    jaccard = jaccard_similarity(set_x1, set_x2)

    f_out = open(out_path, "w")
    f_out.write("X1\tX2\tJaccard_het\n")
    f_out.write("{}\t{}\t{}\n".format(sampleX1, sampleX2, jaccard))
    f_out.close()

vcf_path = sys.argv[1]
sampleX1 = sys.argv[2]
sampleX2 = sys.argv[3]
out_path = sys.argv[4]

#run the calculation
jaccard_pair_het(vcf_path, sampleX1, sampleX2, out_path)
