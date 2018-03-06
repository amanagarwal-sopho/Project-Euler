import time


def prime_list(limit):
    list_prime = [True] * limit
    list_prime[0], list_prime[1] = False, False
    for i in range(2, int(limit**0.5)+1):
        if list_prime[i]:
            for k in range(i*2, limit, i):
                list_prime[k] = False

    set_of_primes = set()
    for index, item in enumerate(list_prime):
        if item:
            set_of_primes.add(index)
    return set_of_primes


def rotate(a):
    list_a = list(str(a))
    rotations = []
    s = len(list_a)
    for i in range(s):
        new_list = list_a[i:s]
        new_list += list_a[0:i]
        rotations.append(int(''.join(new_list)))
        new_list.clear()

    return rotations


def main(limit):
    set_of_primes = prime_list(limit)
    circular_primes = set()
    for prime in set_of_primes:
        if prime not in circular_primes:
            is_circular = True
            rotations = rotate(prime)
            for item in rotations:
                if item not in set_of_primes:
                    is_circular = False
                    break
            if is_circular:
                circular_primes.add(prime)

    print(len(circular_primes))


if __name__ == '__main__':
    start = time.time()
    main(1000000)
    print(time.time() - start)



