#!/usr/bin/env python3

def filterHomo(vcf_path, out_path):
    f_in = open(vcf_path)
    f_out = open(out_path, "w")

    for line in f_in.readlines():
        if line.startswith("#"):
            f_out.write(line)
        else:
            columns = line.split()
            for i in range(9, len(columns)):
                element = columns[i]
                genotype = element[0] + element[2]
                n_ref = int(element.split(":")[1].split(",")[0])
                n_var = int(element.split(":")[1].split(",")[1])

                if (genotype == "00" and n_var > 0) or (genotype == "11" and n_ref > 0):
                    columns[i] = "./." + element[3:]
            f_out.write("\t".join(columns) + "\n")
    f_in.close()
    f_out.close()

filterHomo("./06_rmLowGQDP.recode.vcf", "./07_HQsnp.vcf")
