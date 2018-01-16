def is_pallindrome(num):
    string_num = str(num)
    new_num = ''
    for i in range(len(string_num)-1,-1,-1):
        new_num += string_num[i]
    
    new_num = int(new_num)
    
    if new_num == num :
        return True
    else :
        return False

largest = 10001       
for i in range(999,100,-1):
    for j in range(i,100,-1):
        if is_pallindrome(i*j):
            if i*j > largest :
                largest = i*j

print(largest)