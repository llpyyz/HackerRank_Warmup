"""
David Schonberger
Hackerrank.com
Warmpup - Maximizing XOR
1/4/2015
"""

def maxXOR(l,r):
    return max([a^b for a in range(l,r + 1) for b in range(l,r + 1)])
    
L = input()
R = input()
print maxXOR(L,R)
