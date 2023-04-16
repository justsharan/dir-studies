Repository to store miscellaneous scripts

GTF schema: [Source](https://www.ensembl.org/info/website/upload/gff.html)


## `gtf_clean.py`
I was having an issue with the transcriptome assembly step where some of the entries in the GTF file provided by the reference genome had a `?` value for the strand attribute. This script was made to just filter those out.

Usage: `./gtf_clean.py path/to/annotation.gtf > annotation.cleaned.gtf`

## `gffcmp_filter.py`
This script filters the output from gffcompare by class code and length. I used this to only get the matches that were novel (class code of `u`) and less than 300 nucleotides.

Usage: `./gffcmp_filter.py -c u -l 300 gffcmp.sample.tmap -o gffcmp.filtered.tmap`

## `filter_fasta_by_length.py`
The name is pretty descriptive. Filters the provided FASTA sequence by a maximum length.

Usage: `./filter_fasta_by_length.py -l 300 transcripts.fasta -o transcripts.filtered.fasta`

## `visualize_panther.R`

I originally tried to write this in python with seaborn, but I ran into a ton of issues with its formatting that I decided to make this instead.

Usage: `./visualize_panther.R pantherChart.txt` (or run in an interactive R session)
