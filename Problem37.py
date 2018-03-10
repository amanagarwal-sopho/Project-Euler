import time


def truncate_ltr(num):
    return [num % (10 ** i) for i in range(1, len(str(num))+1)]


def truncate_rtl(num):
    return [num // (10 ** i) for i in range(len(str(num)))]


def prime_list(limit):
    list_prime = [True] * limit
    list_prime[0], list_prime[1] = False, False
    for i in range(2, int(limit**0.5)+1):
        if list_prime[i]:
            for k in range(i*2, limit, i):
                list_prime[k] = False

    list_of_primes = []
    for index, item in enumerate(list_prime):
        if item:
            list_of_primes.append(index)
    return set(list_of_primes)


def main():
    sum = 0
    start = time.time()
    primes = prime_list(1000000)
    range_list = {prime for prime in primes if prime not in [2, 3, 5, 7]}
    for prime in range_list:
        flag = True
        for item in truncate_ltr(prime):
            if item not in primes:
                flag = False
                break
        if flag:
            for item in truncate_rtl(prime):
                if item not in primes:
                    flag = False
                    break
        if flag:
            sum += prime

    print(sum)
    print(time.time() - start)


if __name__ == '__main__':
    main()


