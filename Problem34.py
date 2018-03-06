from math import factorial


def is_curious(num):
    sum = 0
    for k in list(str(num)):
        sum += factorial(int(k))
    return sum == num


def main():
    sum = 0
    for i in range(1000000):
        if is_curious(i):
            sum += i
    print(sum)


if __name__ == '__main__':
    main()
