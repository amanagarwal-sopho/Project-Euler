def is_pandigital(num):
    return ''.join(sorted(list(str(num)))) == '123456789'


def main():
    max_num = 0
    for num in range(1, 100000):
        i = 1
        l = ''
        while len(l) < 9:
            l += str(num * i)
            i += 1
        print(l)
        l = int(l)
        if is_pandigital(l) and l > max_num:
            max_num = l

    print(max_num)

main()
