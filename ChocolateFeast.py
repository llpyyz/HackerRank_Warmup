"""
David Schonberger
Hackerrank.com
Warmpup - Chocolate feast
1/5/2015
"""    
num_cases = input()
for i in range(num_cases):
    next_line = raw_input()
    tmp = next_line.split(' ')
    N = int(tmp[0])
    C = int(tmp[1])
    M = int(tmp[2])
    chocolates = N / C
    curr_wrappers = chocolates
    maxit = 100
    currit = 0
    while(curr_wrappers > 0 and currit < maxit):
        chocolates += curr_wrappers / M
        curr_wrappers = curr_wrappers / M + curr_wrappers % M
        currit += 1
        
    print chocolates
