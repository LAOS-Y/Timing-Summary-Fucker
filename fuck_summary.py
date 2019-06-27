import re
import random
import argparse

def getFucker(min_scale=0.75, max_scale=1.25, mean_scale=1, std_scale=0.15):
    pat = re.compile('[0-9]+\.[0-9][0-9][0-9]')
    
    def fuckLine(line):
        found = re.findall(pat, line)
        
        for num in found:
            new_num = float(num) * (max(min_scale, min(max_scale, random.gauss(mean_scale, std_scale))))
            new_num = '%.3f' % new_num
            line = line.replace(num, new_num)
        
        return line
    
    return fuckLine

parser = argparse.ArgumentParser(description="Fuck up your Vivado timing summary")
parser.add_argument("path", help="original timing summary path")
parser.add_argument("-o", "--output", default=None, help="output path")

parser.add_argument("-m", "--min-scale", type=float, default=0.75, help="min zoom scale")
parser.add_argument("-M", "--max-scale", type=float, default=1.25, help="max zoom scale")
parser.add_argument("--mean", type=float, default=1.25, help="mean of zoom scale")
parser.add_argument("--std", type=float, default=1.25, help="standard deviation of zoom scale")

args = parser.parse_args()

assert args.min_scale < args.max_scale, "min_scale should be smaller than max_scale. Got min_scale: {}, max_scale: {}".format(args.min_scale, args.max_scale)

fuck = getFucker(args.min_scale, args.max_scale, args.mean, args.std)

in_file = open(args.path)

if args.output is not None:
    out_file = open(args.output, mode='w')

for line in in_file:
    line = fuck(line.rstrip())
    if args.output is not None:
        print(line, file=out_file)
        out_file.flush()
    else:
        print(line)

in_file.close()

if args.output is not None:
    out_file.close()