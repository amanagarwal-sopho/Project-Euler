list_numbers = []
with open('project_euler/input18.txt') as file:
    for line in file:
        num_list = line.split(' ')
        for item in num_list :
            item = int(item)
        list_numbers.append(num_list)

max_count = int(list_numbers[0][0])
print(max_count)
index = 0
for i in range(1,len(list_numbers)) :
    if int(list_numbers[i][index]) > int(list_numbers[i][index+1]) :
        num = int(list_numbers[i][index])
    else :
        num = int(list_numbers[i][index+1])
        index += 1
    max_count += num
    print(num)
    
print(max_count)
    