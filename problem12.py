def find_factors(num):
    
    limit = int (num ** 0.5) + 1
    list_factors = []
    for i in range(1,limit):
        if num % i == 0 :
            if num/i == i :
                list_factors.append(i)
            else :
                list_factors.extend((i,int(num/i)))
                
    return len(list_factors)

def main():
    num = 1
    i=2
    while True :
        if find_factors(num) > 500:
            print(num)
            break
        
        num += i
        
        i += 1
        
        
if __name__ == '__main__' :
    main()