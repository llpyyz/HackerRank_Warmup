"""
David Schonberger
Hackerrank.com
Warmpup - Game of Thrones - I
1/4/2015
"""
#count occurence of c in s
def chr_count(c,s):
    return len([ch for ch in s if ch == c])

string = raw_input()
found = False
l =  [ch for ch in string]
l.sort()
chr_set = set(l)

if(len(l) % 2 == 0):
    if(sum([chr_count(c,l) % 2 == 1 for c in chr_set]) == 0):
        found = True
else:
    if(sum([chr_count(c,l) % 2 == 1 for c in chr_set]) == 1):
        found = True

if not found:
    print("NO")
else:
    print("YES")
