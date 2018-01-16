limit = 500

for i in range(2,limit) :
    for j in range(1,i+1):
        a = i ** 2 - j ** 2
        b = 2 * i * j
        c = i ** 2 + j ** 2
        if c>limit :
            break
        if a**2 + b**2 == c**2 and a !=0 and b!=0 and a+b+c == 1000:
            print(a*b*c)
    
