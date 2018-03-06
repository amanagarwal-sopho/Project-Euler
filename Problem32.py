def is_pandigital(num1,num2):
    num_list = {1,2,3,4,5,6,7,8,9}
    num = str(num1)+str(num2)+str(num1*num2)
    for i in num:
        try:
            num_list.remove(int(i))
        except KeyError:
            return False

    if len(num_list) > 0:
        return False
    else :
        return True


def main():
    pandigital_list = set()
    for i in range(1,2000):
        for j in range(1,2000):
            if is_pandigital(i,j) and i*j not in pandigital_list:
                pandigital_list.add(i*j)
                print(i,j,i*j)

    print(sum(pandigital_list))

main()