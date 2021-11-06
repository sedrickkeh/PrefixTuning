import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('-file', type=str)
parser.add_argument('-num', type=int)
parser.add_argument('-train', type=str)
parser.add_argument('-output', type=str)
args = parser.parse_args()

with open(args.file, encoding="utf-8") as f:
    lines = [line for line in f.read().splitlines() if (len(line) > 0 and not line.isspace() and len(line.split('||')) ==2 )]
random.shuffle(lines)
third = len(lines) // 3
assert args.train == 'train' or args.train == 'test' or args.train == 'valid'
if args.train == 'train':
    lines = lines[:third]
elif args.train == 'test':
    lines = lines[third:2 * third] 
elif args.train == 'valid':
    lines = lines[2 * third:]
lines = lines[:args.num]

with open(args.output, 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')