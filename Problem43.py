import itertools
import time


def property(num):
    numbers = [2, 3, 5, 7, 11, 13, 17]
    i = 1
    for number in numbers:
        if int(str(num)[i:i+3]) % number != 0:
            return False
        i += 1
    return True


def main():
    sum = 0
    for item in itertools.permutations('0123456789'):
        if item[0] != '0':
            if property(int(''.join(item))):
                sum += int(''.join(item))

    print(sum)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)