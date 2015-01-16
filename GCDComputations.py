"""
David Schonberger
Hackerrank.com
Warmpup - GCD Computation
1/6/2015
"""
def gcd_lst(l):
    if(len(l) == 2):
        return gcd(l[0], l[1])
    else:
        return gcd(l.pop(0), gcd_lst(l))

def gcd(a,b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a

num_cases = input()
for i in range(num_cases):
    N = input()
    s = raw_input()
    num_lst = s.split(' ')
    num_lst = [int(x) for x in num_lst]
    if(1 in num_lst):
        ans = "YES"
    elif(len(num_lst) == 1):
        ans = "NO"
    else:
        if(gcd_lst(num_lst) == 1):
            ans = "YES"
        else:
            ans = "NO"
    print ans
 