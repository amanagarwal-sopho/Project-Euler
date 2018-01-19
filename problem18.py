arr = []
with open('input18.txt') as file:
    for count,line in enumerate(file,1):
        pass
    arr = [[0 for j in range(count)] for i in range(count)]
    file.seek(0,0)
    for i,line in enumerate(file):
        num_list = line.split(' ')
        for j,item in enumerate(num_list) :
            arr[i][j] = int(item)
            
for i in range(count):
    print(*arr[i],sep=' ',end='\n')


for i in range(count-1,0,-1):
    for j in range(i,0,-1):
        arr[i-1][j-1] = max(arr[i][j]+arr[i-1][j-1],arr[i][j-1]+arr[i-1][j-1])
        
        
print(arr[0][0])
    

    