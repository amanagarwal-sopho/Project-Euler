def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
    
def main():
    grid = 20
    print(factorial(grid*2)//(factorial(grid) * factorial(grid)))
    
if __name__ == '__main__' :
    main()