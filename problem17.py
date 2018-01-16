name_array = [['one','two','three','four','five','six','seven','eight','nine'],
                ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'],['twenty'],
                ['thirty'],['forty'],['fifty'],['sixty'],['seventy'],['eighty'],['ninety'],['hundred'],['thousand']]

limit = 2531
count = 0

for i in range(1,limit):
    word = ''
    if i >= 1000 :
        word += name_array[0][i//1000 - 1] + ' '
        word += name_array[11][0]
        if i%1000 > 0 :
            word += ' and '
        i %= 1000
    if i >= 100 :
        word += name_array[0][i//100 - 1] + ' '
        word += name_array[10][0]
        if i%100 > 0 :
            word += ' and '
        i %= 100
    if i >= 20 :       
        word += name_array[i//10][0] + ' '
        i %= 10
    if i <20 and i>=10 :
        word += name_array[1][i%10]
        i = 0
    if i<10 and i > 0 :
        word += name_array[0][i%10 - 1]
    
    count += len(word.replace(' ',''))
    print(word)
print(count)