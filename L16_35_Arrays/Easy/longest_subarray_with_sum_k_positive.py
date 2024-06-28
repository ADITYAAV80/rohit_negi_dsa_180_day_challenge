def longest_subarray_with_sum_k(arr,key):
    arr=sorted(arr)
    left,right,maxlen=0,0,0
    sum=arr[0]
    while(right<len(arr)):
        while left<=right and sum>key:
            sum-=arr[left]
            left+=1
        if sum==key:
            maxlen=max(maxlen,right-left+1)
        right+=1
        if right<len(arr):
            sum+=arr[right]
    return maxlen
         
if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    key=int(input("Enter the key value: "))
    sol=longest_subarray_with_sum_k(arr,key)
    print("Length of the longest subarray is : ",sol)