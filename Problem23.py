from Problem21 import d_of
import time

abundant = []
def is_abundant(n):
    return d_of(n) > n


abundant_list = {i for i in range(12,28124) if is_abundant(i)}
sum_list = [i for i in range(1,28124)]
def sum_exists(n):
    for i in abundant_list:
        if i>n:
            return False
        if n-i in abundant_list:
            return True
    

start = time.time()
sum = 0
for i in range(1,28124):
    if not sum_exists(i):
        sum += i
        
print(sum)
print(time.time()-start)
    
    
