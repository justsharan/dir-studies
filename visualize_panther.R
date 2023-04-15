#!/usr/bin/env Rscript

library(stringr)
library(tidyverse)

columns = c('index', 'category', 'freq', 'percent1', 'percent2')

args <- commandArgs(TRUE)

df <- read_tsv(args[1], col_names=columns)

# Format category column
df <- mutate(df, category = str_replace_all(category, '\\s\\(GO:\\d+\\)$', ''))
df <- mutate(df, category = str_to_title(category))

print(head(df))

ggplot(df, aes(x = category, y = freq)) +
  geom_bar(stat = 'identity') +
  coord_flip() +
  labs(x = 'Biological Process', y = 'Number of Genes')
  theme_bw()

