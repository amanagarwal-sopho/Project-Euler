largest = 2

num = 600851475143

while num%2 == 0 :
    num /= 2
    
for i in range(3,int(num**0.5),2):
    
    while num%i == 0 :
        num /= i
        largest = i
        
print(largest)