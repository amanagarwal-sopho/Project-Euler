from numpy import array
def find_product(array1):
    max_product = 1
    print(array1)
    for i in range(len(array1)):
        product = 1
        for j in range(len(array1)):
            product *= array1[i][j]
        if product > max_product :
            max_product = product
        
    for j in range(len(array1)):
        product = 1
        for i in range(len(array1)):
            product *= array1[i][j]
        if product > max_product :
            max_product = product
    
    pr = 1
    pl = 1
    for i in range(len(array1)):
        for j in range(len(array1)):
            if i == j :
                pr *= array1[i][j]
            if i+j == len(array1)-1 :
                pl *= array1[i][j]
    max_product = max(max_product,pr,pl)
    return max_product
    
arr = []


with open('input11.txt','r') as input_file :
    for line in input_file:
        row = []
        num = ''
        for char in line :
            if char == ' ' :
                row.append(int(num))
                num = ''
            else :
                num += char
        
        row.append(int(num))
        arr.append(row)

max_product = 0

arr = array(arr)
print(len(arr))
for row in range(len(arr)-3):
    for col in range(len(arr)-3):
        test_array = arr[row:row+4,col:col+4]
        row_max_product = find_product(test_array)
        print(row_max_product)
        if row_max_product > max_product :
            max_product = row_max_product
            
        
  
print(max_product)     



                