from argparse import ArgumentParser
import pandas as pd
import sys

parser = ArgumentParser()
parser.add_argument('-c', '--code', help='Class code')
parser.add_argument('-l', '--len', help='Maximum transcript length (inclusive)')
parser.add_argument('-o', '--output', help='Output file')

args = parser.parse_args()

gffcmp_file = pd.read_csv(sys.argv[1])
filtered = gffcmp_file[(gffcmp_file['class_code'] == args.code) & (gffcmp_file['len'] <= args.len)]

filtered.to_csv(args.output)
