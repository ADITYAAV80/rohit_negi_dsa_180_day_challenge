def max_subarray_sum_indices(arr):
    tempsum,total=0,0
    for i in range(0,len(arr)):
        if tempsum==0:
            temp_minindex=i
        tempsum+=arr[i]
        if tempsum>total:
            minindex=temp_minindex
            maxindex=i+1
            total=tempsum
        if tempsum<0:
            tempsum=0
    return arr[minindex:maxindex]

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=max_subarray_sum_indices(arr)
    print("Maximum subarray : ",sol,"with sum",sum(sol))