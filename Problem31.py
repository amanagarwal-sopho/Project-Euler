def count(arr,m,n):

    if n==0:
        return 1
    if n<0:
        return 0
    if m<=0 and n>=1:
        return 0

    return count(arr,m-1,n) + count(arr,m,n-arr[m-1])

def main():
    arr = [1,2,5,10,20,50,100,200]
    print(count(arr,len(arr),200))


if __name__=='__main__':
    main()