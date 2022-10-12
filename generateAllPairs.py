#!/usr/bin/env python3
import sys

args = sys.argv
script_path = args[1]
vcf_path = args[2]
out_path = "allPairs.sh"

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

f_out.write("#!/bin/bash\n\n")

for i in range(0, len(sample_list) - 1):
    for j in range(i+1, len(sample_list)):
        sample01 = sample_list[i]
        sample02 = sample_list[j]
        f_out.write("{} {} {} {} {}_{}_SH.txt\n".format(script_path, vcf_path, sample01, sample02, sample01, sample02))

f_out.close()
