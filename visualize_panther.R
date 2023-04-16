#!/usr/bin/env Rscript
library(stringr)
library(tidyverse)

columns = c('index', 'category', 'freq', 'percent1', 'percent2')

df_bp <- read_tsv('biologicalProcess.txt', col_names = columns)

# Format category column
df_bp <- mutate(df_bp, category = str_replace_all(category, '\\s\\(GO:\\d+\\)$', ''))
df_bp <- mutate(df_bp, category = str_to_title(category))

ggplot(df_bp, aes(x = category, y = freq)) +
  geom_bar(stat = 'identity') +
  coord_flip() +
  labs(x = '', y = 'Number of Genes') +
  theme_bw()

df_pc <- read_tsv('proteinClass.txt', col_names = columns)

# Format category column
df_pc <- mutate(df_pc, category = str_replace_all(category, '\\s\\(PC\\d+\\)$', ''))
df_pc <- mutate(df_pc, category = str_to_title(category))

ggplot(df_pc, aes(x = category, y = freq)) +
  geom_bar(stat = 'identity') +
  coord_flip() +
  labs(x = '', y = 'Number of Genes') +
  theme_bw()

df_mf <- read_tsv('molecularFunction.txt', col_names = columns)

# Format category column
df_mf <- mutate(df_mf, category = str_replace_all(category, '\\s\\(GO:\\d+\\)$', ''))
df_mf <- mutate(df_mf, category = str_to_title(category))
df_mf <- mutate(df_mf, category = str_replace_all(category, 'Atp', 'ATP'))

ggplot(df_mf, aes(x = category, y = freq)) +
  geom_bar(stat = 'identity') +
  coord_flip() +
  labs(x = '', y = 'Number of Genes') +
  theme_bw()