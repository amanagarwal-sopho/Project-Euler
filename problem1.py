

limit = 1000000

def SimpleApproach():
    
    print(sum([i for i in range(limit) if i%5==0 or i%3==0]))

def EfficientApproach():
    print(SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15))


def SumDivisibleBy(n):
    p = (limit-1) // n
    sum = n*(p*(p+1))/2
    return sum
    
if __name__ == '__main__':
    EfficientApproach()
    SimpleApproach()
    

    