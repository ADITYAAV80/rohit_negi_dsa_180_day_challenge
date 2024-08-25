def findMissingRepeatingNumbers(arr):

    n = len(arr)
    sn = n*(n+1)//2
    sn2 = n*(n+1)*(2*n+1)//6
    arrsum=sum(arr)
    arr2sum=0
    for i in range(n):
        arr2sum+=arr[i]**2
    x_minus_y = arrsum-sn
    x_plus_y  = (arr2sum-sn2)//x_minus_y
    repeat  = (x_minus_y+x_plus_y)//2
    missing = x_plus_y-repeat
    return [repeat,missing]


if __name__ == '__main__':
    arr = list(map(int,input("Enter an integer array 1 seperated by spaces : ").split(" ")))
    ans = findMissingRepeatingNumbers(arr)
    print("The repeating and missing numbers are: {", ans[0], ", ", ans[1], "}\n")

