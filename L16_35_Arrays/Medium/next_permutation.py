def next_permutation(arr,n):
    pindex=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pindex=i
            break
    if pindex==-1:
        arr.reverse()
    else:
        for i in range(n-1,pindex-1,-1):
            if arr[i]>arr[pindex]:
                arr[i],arr[pindex]=arr[pindex],arr[i]
                break
        arr[pindex+1:] = reversed(arr[pindex+1:])


if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    next_permutation(arr,len(arr))
    print("The next permutation of array is : ",arr)