"""
David Schonberger
Hackerrank.com
Warmpup - Finding a 'decent' number
1/6/2015
"""
num_cases = input()
for i in range(num_cases):
    N = input()
    if(N % 3 == 0):
        ans = ''.join(['5' for i in range(N)])
    elif(N == 5 or N == 10):
        ans = ''.join(['3' for i in range(N)])
    elif(N < 8):
        ans = '-1'
    else:
        fives_removed = 0
        while(N % 3 != 0):
            N -= 5
            fives_removed += 1
        ans = ''.join(['5' for i in range(N)]) + ''.join(['3' for i in range(5 * fives_removed)])
    print ans
    print len([x for x in ans if x == '5']), len([x for x in ans if x == '5']) % 3
    print len([x for x in ans if x == '3']), len([x for x in ans if x == '3']) % 5



