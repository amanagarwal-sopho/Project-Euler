from math import ceil

def list_prime(limit):
    count=0
    sum = 0
    prime_list = [True] * (limit-1)
    for i in range(2,ceil(limit**0.5)) :
        if prime_list[i-2] == True :
            for j in range(2*i,limit+1,i) :
                prime_list[j-2] = False
    
    for i in range(limit-1) :
        if prime_list[i] == True :
            count += 1
            sum += i+2
            #if count == 10001 :
                #break
    print(sum)
                
list_prime(2000000)