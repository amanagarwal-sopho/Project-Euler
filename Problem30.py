def sum_fifth(num):
    strnum = str(num)
    sum = 0
    for i in strnum:
        sum += int(i)**5
    return sum==num

sum = 0
for i in range(2,200000):
    if sum_fifth(i):
        sum += i

print(sum)
