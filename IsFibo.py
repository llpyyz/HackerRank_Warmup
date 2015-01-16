"""
Hackerrank.com
Warmpup - IsFibo
"""
bef = datetime.datetime.now()
#gen all fibonacci numbers <= n (default n = 10^6)
def fibo(n = 1000000):
    if(n == 0):
        fib = [0]
    elif(n == 1):
        fib = [0,1,1]
    else:
        fib = [0,1]
        i = 1
        next_fib = 1
        while(next_fib <= n):

            fib.append(next_fib)
            i += 1
            next_fib = fib[i] + fib[i-1]
            
    return fib

n = 10**10
l = fibo(n)
num = input()
for i in range(num):
    if(input() in l):
        print "IsFibo"
    else:
        print "IsNotFibo"
