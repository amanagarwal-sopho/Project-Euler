def factorial(num):
    if num == 0 :
        return 1
    else :
        return num * factorial(num-1)
        
if __name__=='__main__':
    fact = str(factorial(100))
    digits = [int(s) for s in fact]
    print(sum(digits))
    