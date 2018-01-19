
def d_of(n):
    if n == 1:
        return 0
    divisors_list = [1]
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 :
            if n/i != i:
                divisors_list.extend([i,n//i])
            else :
                divisors_list.append(i)
                
    return sum(divisors_list)
    
def are_amicable(a,b):
    return d_of(a)==b and d_of(b)==a and b!=a

def amicable_sum(limit):    
    d_list = []
    amicable_list = []
    for i in range(1,limit+1):   
        d_list.append(d_of(i))
    
    for i,d in enumerate(d_list,1):
        try :
            if are_amicable(d,i) and d not in amicable_list:
                amicable_list.append(d)
        except IndexError:
            pass
        
    print(sum(amicable_list))

if __name__=='__main__':    
    amicable_sum(10000)
    
            
            