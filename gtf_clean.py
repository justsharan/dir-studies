import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    for line in file:
        split = line.split('\t')
        if len(split) != 9:
            print(line)
        elif split[6] != '?':
            print(line)
