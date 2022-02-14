#!/usr/bin/env Rscript
library(ggplot2)
snp <- read.table("03_Rtable.txt", header = TRUE)


pdf("clones_QD.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=QD)) + geom_density() + geom_vline(xintercept = 13)
dev.off()

pdf("clones_FS.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=FS)) + geom_density() + scale_x_continuous(trans='log10')
dev.off()


pdf("clones_SOR.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=SOR)) + geom_density() + xlim(0,10)
dev.off()

pdf("clones_MQ.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=MQ)) + geom_density() + xlim(0,70)
dev.off()

pdf("clones_MQRankSum.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=MQRankSum)) + geom_density() + xlim(-11,6)
dev.off()

pdf("clones_ReadPosRankSum.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=ReadPosRankSum)) + geom_density() + xlim(-5,5)
dev.off()

pdf("clones_DP.pdf",width=6,height=4,paper='special')
ggplot(snp, aes(x=DP)) + geom_histogram(binwidth = 100) + xlim(0,5000) + geom_vline(xintercept = 1112)
dev.off()

mean(snp$DP) * 2
