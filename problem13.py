
i = -2
carry = 0
num = []
with open('project_euler/input13.txt','r') as file:
    for i in range(-2,-52,-1) :
        sum = carry
        for line in file:
            sum += int(line[i])
        file.seek(0,0)
        carry = sum//10
        if i == -51 :
            digit = sum
        else :
            digit = sum % 10
        print(i,sum,carry)
        num.append(digit)
        
num.reverse()
for item in num :
    print(item,end='')