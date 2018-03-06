import time

limit = 1000000
start = time.time()
sum = 0
for i in range(limit):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]:
        sum += i
print(sum)
print(time.time() - start)
