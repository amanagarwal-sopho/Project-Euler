import time
chain_len = [0] * (10 ** 6)

start = time.time()
for i in range(2,1000000):
    num = i
    count = 1
    while num != 1:
        if num%2 == 0 :
            num //= 2
        else :
            num = num * 3 + 1
        if num < i and num > 2 :
            count = chain_len[num-2] + count
            break
        else :
            count += 1
    
    chain_len[i-2] = count

elapsed = time.time() - start        
print(elapsed)
print(chain_len.index(max(chain_len))+2,max(chain_len))