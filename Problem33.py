def curious_fraction(num,den):
    num_list = set(list(str(num)))^set(list(str(den)))
    a,b = 0,1
    for i in num_list:
        if i in list(str(num)):
            a = int(i)
        if i in list(str(den)):
            b = int(i)
    try :
        if a/b == num/den:
            return True
    except ZeroDivisionError:
        print(num,den)
for i in range(10,100):
    for j in range(10,100):
        if curious_fraction(i,j) and i!=j:
            print(i,j)

