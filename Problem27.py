# Euler discovered the remarkable quadratic formula:
#                   n^2+n+41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# .However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
# is clearly divisible by 41.
# The incredible formula n^2−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
#
#     n^2+a*n+b
#
# , where |a|<1000 and |b|≤1000
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a
# and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
limit = 1000
def is_prime(n):
    if n == 1 or n<=0:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def prime_list(limit):
    primes = [i for i in range(1,limit+1)]
    for i in range(1,int(limit**0.5)):
        if primes[i]:
            for j in range(2*i+1,limit,primes[i]):
                primes[j] = 0
    return [prime for prime in primes if prime!=0 and prime!=1]

def primes_possible(a,b):
    n = 0
    num = n**2+a*n+b
    while is_prime(num):
        n += 1
        num = n**2+a*n+b
    return n

def main():
    max_possible = 1
    max_product,a_max,b_max = 1,1,1
    for a in range(-999,0):
        for b in prime_list(1000):
            if ((a+b)%2 == 0 and b!=2) and (a+b) >0:
                temp = primes_possible(a,b)
                if temp > max_possible:
                    max_possible = temp
                    max_product = a*b
                    a_max=a
                    b_max=b
    print('Max possible product:{} with a:{} and b:{} and Prime Sequence:{}'.format(max_product,a_max,b_max,max_possible))

if __name__=='__main__':
    main()




