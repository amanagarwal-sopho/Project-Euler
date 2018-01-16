import time

sum_digits = 0
num = 2 ** 1000
start = time.time()

for n in str(num) :
    sum_digits += int(n)

elapsed = time.time() - start
print(sum_digits,elapsed)
