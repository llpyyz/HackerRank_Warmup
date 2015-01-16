"""
David Schonberger
Hackerrank.com
Warmpup - Alternating characters
1/4/2015
"""

def count_deletions(s):
    chr_lst = ['A', 'B']
    dels = 0
    curr_idx = 1
    if('A' in s and not 'B' in s or 'B' in s and not 'A' in s):
        return len(s) - 1
    elif(s[0] == 'A'):
        next_chr_idx = 1
    else:
        next_chr_idx = 0
        
    while(curr_idx < len(s)):
        if(s[curr_idx] != chr_lst[next_chr_idx]):
            dels += 1
        else:
            next_chr_idx  = (next_chr_idx + 1) % 2
            
        curr_idx += 1

    return dels

num_cases = input()
for i in range(num_cases):
    print count_deletions(str(raw_input()))