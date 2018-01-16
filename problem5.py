#TODO : USE Shorter method

def find_gcd(a,b):
    if a == 0 :
        return b
    elif b>a:
        return find_gcd(b%a,a)
    else :
        return find_gcd(a%b,b)

def find_lcm(a,b,hcf):
    return int((a*b)/hcf)
    

limit =  21
num = 2
for i in range(3,limit) :
    hcf = find_gcd(num,i)
    lcm = find_lcm(num,i,hcf)
    num = lcm
    
print(num)