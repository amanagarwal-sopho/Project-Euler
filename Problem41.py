def is_pandigital(num, n):
    return sorted(list(str(num))) == [str(i) for i in range(1, n+1)]

def is_prime(num):
    if num % 2 == 0 and num % 3 == 0:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

    return True

def main():
    for num in range(9999999):
        if is_pandigital(num, len(str(num))) and is_prime(num):
            final = num
    print(final)

main()