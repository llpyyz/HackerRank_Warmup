"""
David Schonberger
Hackerrank.com
Warmpup - Filling jars
1/5/2015
"""    
s = raw_input()
s = s.split(' ')
N = int(s[0])
M = int(s[1])

total_candies = 0
for i in range(M):
    next_line = raw_input()
    tmp = next_line.split(' ')
    total_candies += int(tmp[2]) * (int(tmp[1]) - int(tmp[0]) + 1)
    
print total_candies / N
