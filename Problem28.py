#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#                   21 22 23 24 25
#                   20  7  8  9 10
#                   19  6  1  2 11
#                   18  5  4  3 12
#                   17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def sum_of_diagonals(limit):
    arr = [ [0 for j in range(limit)] for i in range(limit)]
    count = limit ** 2
    i = -1
    j = limit
    k = 0
    while i != limit//2 and j != limit//2 :
        i+=1
        j-=1
        while j>=k:
            arr[i][j] = count
            count -= 1
            j-=1

        i += 1
        j += 1
        while i<limit-k:
            arr[i][j] = count
            count -=1
            i += 1

        j += 1
        i -= 1
        while j<limit-k:
            arr[i][j] = count
            count -= 1
            j += 1

        j -= 1
        i -= 1
        while i>k:
            arr[i][j] = count
            count -= 1
            i -= 1
        k+=1

    sum_diagonal = 0
    for i in range(limit):
        for j in range(limit):
            if i==j or i+j==limit-1:
                sum_diagonal += arr[i][j]
    return sum_diagonal

def sum_diagonals_formula(limit):
    return (4*limit**3 + 3*limit**2 + 8*limit-9)//6

print(sum_of_diagonals(1001))
print(sum_diagonals_formula(1001))


