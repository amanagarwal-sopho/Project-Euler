def main():
    count = 0
    num = 1
    prod = 1
    while count <= 1000000:
        for item in list(str(num)):
            count += 1
            if count in [1, 10, 100, 1000, 10000, 100000, 1000000]:
                prod *= int(item)
        num += 1
    return prod


print(main())