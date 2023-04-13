from argparse import ArgumentParser
import pandas as pd

parser = ArgumentParser()
parser.add_argument('-c', '--code', help='Class code')
parser.add_argument('-l', '--len', help='Maximum transcript length (inclusive)', type=int)
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('filename')

args = parser.parse_args()

pd.options.display.max_columns = None
pd.options.display.max_rows = None

cols = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']

gffcmp = pd.read_csv(args.filename, sep='\t', names=cols, header=None)

class_code_filter = gffcmp['attribute'].str.contains(f'class_code "{args.code}"')
length_filter = gffcmp['end'] - gffcmp['start'] <= args.len

filtered = gffcmp[class_code_filter & length_filter]
filtered.to_csv(args.output, sep='\t', header=None, index=None)
