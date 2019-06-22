import re
import random

def getFucker(min_scale=0.75, max_scale=1.25, gauss_mean=1, gauss_std=0.15):
    pat = re.compile('[0-9]+\.[0-9][0-9][0-9]')
    
    def fuckLine(line):
        found = re.findall(pat, line)
        
        for num in found:
            new_num = float(num) * (max(min_scale, min(max_scale, random.gauss(gauss_mean, gauss_std))))
            new_num = '%.3f' % new_num
            line = line.replace(num, new_num)
        
        return line
    
    return fuckLine

path = 'timing_report.txt'
output_path = 'new_report.txt'

fuck = getFucker()

in_file = open(path)
out_file = open(output_path, mode='w')

for line in in_file:
    line = fuck(line.strip())
    print(line, file=out_file)
    out_file.flush()

in_file.close()
out_file.close()