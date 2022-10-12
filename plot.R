#!/usr/bin/env Rscript

library(ggplot2)

obj <- read.table("./output/SH_indices.txt", header = TRUE)
obj01 = subset(obj, Type == "TR")

png("NSH_SH.png", width = 600, height = 600, res = 300)
ggplot(obj, aes(NSH, SH, color=Type)) +
  geom_point(shape = 4) +
  geom_hline(yintercept = 0.9, color = "orange") +
  theme_classic() +
  ylab("SH") +
  xlab("NSH") +
  scale_x_continuous(limits = c(0, max(obj$NSH) +1), labels=function(x) format(x, big.mark = ",", scientific = FALSE)) +
  scale_y_continuous(limits = c(0,1), breaks = c(0, 0.25, 0.50, 0.75, 0.90, 1)) +
  scale_color_manual(values = c("TR" = "blue", "Non-TR" = "grey")) +
  geom_point(data=obj01, mapping=aes(NSH, SH), shape = 4) +
  theme(legend.position = "none")

dev.off()


png("SH_histogram.png", width = 600, height = 600, res = 300)
ggplot(obj, aes(SH)) +
  geom_histogram(binwidth = 0.01) +
  geom_vline(xintercept = 0.90, color = "orange") +
  theme_classic() +
  xlab("SH") +
  scale_y_continuous(labels=function(x) format(x, big.mark = ",", scientific = FALSE)) +
  scale_x_continuous(limits = c(0,1), breaks = c(0, 0.25, 0.50, 0.75, 0.90, 1))
dev.off()
