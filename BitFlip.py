"""
David Schonberger
Hackerrank.com
Warmpup - Bit flip
1/5/2015
"""
def extend(num):
    return ''.join(['0' for i in range(32 - len(num))]) + num
        
def flip_bits(num):
    res =  ''.join([str(1 ^ int(c)) for c in num])
    return res
    
num_cases = input()
for i in range(num_cases):
    n = bin(input())[2:]
    if(len(n) < 32):
        n = extend(n)
    print int(flip_bits(n),2)
