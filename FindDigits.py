"""
David Schonberger
Hackerrank.com
Warmpup - Find Digits
"""

def count_digit_divisors(n):
    print len([x for x in n if x != '0' and int(n) % int(x) == 0])

num = input()
for i in range(num):
    count_digit_divisors(str(input()))
