"""
David Schonberger
Hackerrank.com
Warmpup - The Love Letter Mystery
1/4/2015
"""

def is_palindrome(s):
    palin = False
    if(len(s) <= 1):    
        palin = True
    else:
        first = s[0]
        last = s[len(s)-1]
        palin = first == last and is_palindrome(s[1:len(s) - 2])

    return palin

num_cases = input()
for i in range(num_cases):
    s = str(raw_input())
    if(is_palindrome(s)):
        print 0
    else:
        print sum([abs(ord(s[len(s)-1-i]) - ord(s[i])) for i in range(len(s)/2)])
