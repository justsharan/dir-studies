from argparse import ArgumentParser
import pandas as pd

parser = ArgumentParser()
parser.add_argument('-c', '--code', help='Class code')
parser.add_argument('-l', '--len', help='Maximum transcript length (inclusive)', type=int)
parser.add_argument('-o', '--output', help='Output file')
parser.add_argument('filename')

args = parser.parse_args()

gffcmp_file = pd.read_csv(args.filename, sep='\t')
filtered = gffcmp_file[(gffcmp_file['class_code'] == args.code) & (gffcmp_file['len'] <= args.len)]

filtered.to_csv(args.output)
