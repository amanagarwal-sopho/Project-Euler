
limit = 4000000
sume = 0;num=0
first = 1;second = 1
while num < limit :
    num = first + second
    if num%2 == 0:
        sume += num
        print(num)
    first,second = second,num
    
print(sume)