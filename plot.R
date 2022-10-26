#!/usr/bin/env Rscript

library(ggplot2)

obj <- read.table("./output/SH_indices.txt", header = TRUE)
obj01 = subset(obj, Type == "TR")

pdf("NSH_SH_01.pdf", width = 4, height = 4)
ggplot(obj, aes(NSH, SH, color=Type)) +
  geom_point(shape = 4) +
  theme_classic() +
  ylab("SH") +
  xlab("NSH") +
  scale_x_continuous(limits = c(0, max(obj$NSH) +1), labels=function(x) format(x, big.mark = ",", scientific = FALSE)) +
  scale_y_continuous(limits = c(0,1), breaks = c(0, 0.25, 0.50, 0.75, 1)) +
  scale_color_manual(values = c("TR" = "blue", "Non-TR" = "grey")) +
  geom_point(data=obj01, mapping=aes(NSH, SH), shape = 4) +
  theme(legend.position = "none")

dev.off()


pdf("NSH_SH_02.pdf", width = 4, height = 4)
ggplot(obj, aes(NSH, SH, color=Type)) +
  geom_point(shape = 4) +
  geom_hline(yintercept = 0.9, color = "orange") +
  theme_classic() +
  ylab("SH") +
  xlab("NSH") +
  scale_x_continuous(limits = c(0, max(obj$NSH) +1), labels=function(x) format(x, big.mark = ",", scientific = FALSE)) +
  scale_y_continuous(limits = c(0,1), breaks = c(0, 0.25, 0.50, 0.75, 0.90, 1)) +
  scale_color_manual(values = c("TR" = "grey", "Non-TR" = "grey")) +
  geom_point(data=obj01, mapping=aes(NSH, SH), shape = 4) +
  theme(legend.position = "none")

dev.off()
