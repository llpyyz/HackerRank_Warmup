"""
David Schonberger
Hackerrank.com
Warmpup - Angry Children
1/4/2015
"""
n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
print min([candies[i] - candies[i - k + 1] for i in range(k - 1,len(candies))])
