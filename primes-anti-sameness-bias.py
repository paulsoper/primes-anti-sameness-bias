#======================================================================
#
# primes-anti-sameness-bias.py
#
# explore the anti-samesness bias in the prime numbers - i.e.
# the fact that for a prime number (base 10) that ends in a 1
# the next prime is less likely to end in a one than in a 3, 7,
# or 9 - and the same thing for a prime that ends in a 3, or a 7
# or a 9
#
# uses a Miller-Rabin prime number generator, which, with bases
# of bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] is
# a determinative test for primes less than
# 3,317,044,064,679,887,385,961,981 - it is not the fastest for
# small primes, but lets one test the numbers in the range I am
# using while being conservative with memory - no lists necessary
#
# Paul Soper
#
# March 3, 2017
#
#=======================================================================

import math
import sys

bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def miller_rabin(n):

    if n < 2:
        return False

    # 2 is prime, and MR does not work for even numbers
    if n == 2:
        return True
    # 3 is prime - return True for 3
    if n == 3:
        return True
   
    # return False if n is even
    if not (n & 1):
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    
    while d % 2 == 0:
        d >>= 1
        s += 1
    
    for a in bases:
        if a < (n-1):
            if not check(a, s, d, n):
                return False
    return True

def miller_rabin_generate():
    n = 2
    while True:
        if miller_rabin(n):
            yield n
        n = n + 1

mrg = miller_rabin_generate()
x = 0

limit = int(sys.argv[1])

t11 = 0
t13 = 0
t17 = 0
t19 = 0
t31 = 0
t33 = 0
t37 = 0
t39 = 0
t71 = 0
t73 = 0
t77 = 0
t79 = 0
t91 = 0
t93 = 0
t97 = 0
t99 = 0

for i in range(0,limit):
    p = x
    x = next(mrg)
    if (x != 2) and (x !=5) and (p != 2) and (p != 5):
        dp = int(str(p)[-1])
        dx = int(str(x)[-1])

        if dp == 1 and dx == 1:
            t11 += 1
        if dp == 1 and dx == 3:
            t13 += 1
        if dp == 1 and dx == 7:
            t17 += 1
        if dp == 1 and dx == 9:
            t19 += 1
        if dp == 3 and dx == 1:
            t31 += 1
        if dp == 3 and dx == 3:
            t33 += 1
        if dp == 3 and dx == 7:
            t37 += 1
        if dp == 3 and dx == 9:
            t39 += 1
        if dp == 7 and dx == 1:
            t71 += 1
        if dp == 7 and dx == 3:
            t73 += 1
        if dp == 7 and dx == 7:
            t77 += 1
        if dp == 7 and dx == 9:
            t79 += 1
        if dp == 9 and dx == 1:
            t91 += 1
        if dp == 9 and dx == 3:
            t93 += 1
        if dp == 9 and dx == 7:
            t97 += 1
        if dp == 9 and dx == 9:
            t99 += 1
        
t1 = t11 + t13 + t17 + t19
t3 = t31 + t33 + t37 + t39
t7 = t71 + t73 + t77 + t79
t9 = t91 + t93 + t97 + t99

t = t1 + t3 + t7 + t9

print ("Total primes: ", t)
print ("\tEnding in 1: {:8d} {:16.4f}".format(t1, (float(t1)/float(t))*100))
print ("\tEnding in 3: {:8d} {:16.4f}".format(t3, (float(t3)/float(t))*100))
print ("\tEnding in 7: {:8d} {:16.4f}".format(t7, (float(t7)/float(t))*100))
print ("\tEnding in 9: {:8d} {:16.4f}".format(t9, (float(t9)/float(t))*100))
print ("\n\tTotal primes ending in 1: ", t1)
print ("\t\tNext ends in 1: {:8d} {:16.4f}".format(t11, (float(t11)/float(t1))*100))
print ("\t\tNext ends in 3: {:8d} {:16.4f}".format(t13, (float(t13)/float(t1))*100))
print ("\t\tNext ends in 7: {:8d} {:16.4f}".format(t17, (float(t17)/float(t1))*100))
print ("\t\tNext ends in 9: {:8d} {:16.4f}".format(t19, (float(t19)/float(t1))*100))
print ("\n\tTotal primes ending in 3: ", t3)
print ("\t\tNext ends in 1: {:8d} {:16.4f}".format(t31, (float(t31)/float(t3))*100))
print ("\t\tNext ends in 3: {:8d} {:16.4f}".format(t33, (float(t33)/float(t3))*100))
print ("\t\tNext ends in 7: {:8d} {:16.4f}".format(t37, (float(t37)/float(t3))*100))
print ("\t\tNext ends in 9: {:8d} {:16.4f}".format(t39, (float(t39)/float(t3))*100))
print ("\n\tTotal primes ending in 7: ", t7)
print ("\t\tNext ends in 1: {:8d} {:16.4f}".format(t71, (float(t71)/float(t7))*100))
print ("\t\tNext ends in 3: {:8d} {:16.4f}".format(t73, (float(t73)/float(t7))*100))
print ("\t\tNext ends in 7: {:8d} {:16.4f}".format(t77, (float(t77)/float(t7))*100))
print ("\t\tNext ends in 9: {:8d} {:16.4f}".format(t79, (float(t79)/float(t7))*100))
print ("\n\tTotal primes ending in 9: ", t9)
print ("\t\tNext ends in 1: {:8d} {:16.4f}".format(t91, (float(t91)/float(t9))*100))
print ("\t\tNext ends in 3: {:8d} {:16.4f}".format(t93, (float(t93)/float(t9))*100))
print ("\t\tNext ends in 7: {:8d} {:16.4f}".format(t97, (float(t97)/float(t9))*100))
print ("\t\tNext ends in 9: {:8d} {:16.4f}".format(t99, (float(t99)/float(t9))*100))








