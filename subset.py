#!/usr/bin/env python3
#*/py vcf_path out_path f n
#f: f/1; n: repeat n times.
import random
import sys
import subprocess

def randomselect(vcf_path, f):
    target_list = []
    for i in range(1, f):
        target_list.append(0)
    target_list.append(1)


    f_in = open(vcf_path)
    f_out = open("temp.vcf", "w")

    for line in f_in.readlines():
        if line.startswith("#"):
            f_out.write(line)
        else:
            clock = random.choice(target_list)
            if clock == 1:
                f_out.write(line)

    f_in.close()
    f_out.close()

def similarity(vcf_path, sampleA, sampleB):
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

    return n_ibh, ibh_s


args = sys.argv
vcf_path = args[1]
out_path = args[2]
f = int(args[3])
n = int(args[4])

sample_list = []
f_in = open(vcf_path)
for line in f_in.readlines():
    if line.startswith("#CHROM"):
        columns = line.split()
        for i in range(9, len(columns)):
            sample = columns[i]
            sample_list.append(sample)
        break
f_in.close()

f_out = open(out_path, "w")
f_out.write("SampleA\tSampleB\tN_IBH\tIBHs\n")

for repeat in range(0, n):
    randomselect(vcf_path, f)
    for i in range(0, len(sample_list) - 1):
        for j in range(i+1, len(sample_list)):
            sampleA = sample_list[i]
            sampleB = sample_list[j]
            n_ibh, ibh_s = similarity("temp.vcf", sampleA, sampleB)
            f_out.write("{}\t{}\t{}\t{}\n".format(sampleA,sampleB,n_ibh,ibh_s))
f_out.close()

cmd = "rm ./temp.vcf"
subprocess.call(cmd, shell=True)
