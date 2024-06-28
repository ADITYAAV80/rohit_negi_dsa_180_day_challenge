def max_subarray_sum(arr):
    tempsum,total=0,0
    for i in range(0,len(arr)):
        tempsum+=arr[i]
        if tempsum>total:
            total=tempsum
        if tempsum<0:
            tempsum=0
    return total

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=max_subarray_sum(arr)
    print("Maximum subarray sum : ",sol)