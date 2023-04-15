#!/usr/bin/env python
from argparse import ArgumentParser
from Bio import SeqIO

parser = ArgumentParser()
parser.add_argument('-l', '--len', help='Maximum length to filter by (inclusive)', type=int)
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('filename')

args = parser.parse_args()

filtered_records = [
    fasta_record
    for fasta_record in SeqIO.parse(args.filename, 'fasta')
    if len(fasta_record.seq) <= args.len
]

output_file = open(args.output, 'w')
SeqIO.write(filtered_records, output_file, 'fasta')
