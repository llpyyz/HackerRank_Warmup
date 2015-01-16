"""
David Schonberger
Hackerrank.com
Warmpup - Sherlock and Squares
1/5/2015
"""
import math
num_cases = input()
for i in range(num_cases):
    next_line = raw_input()
    tmp = next_line.split(' ')
    A = int(tmp[0])
    B = int(tmp[1])
    print int(math.floor(math.sqrt(B))) - int(math.ceil(math.sqrt(A))) + 1
