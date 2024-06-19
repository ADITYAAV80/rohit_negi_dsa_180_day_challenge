def longest_subarray_with_sum_k(arr,k):
    summation,maxlen=0,0
    ans={}
    for i in range(0,len(arr)):
        summation+=arr[i]
        if summation==k:
            maxlen=max(maxlen,i+1)
        rem=k-summation
        if rem in ans.keys():
            maxlen=max(maxlen,i-ans[rem])
        if summation not in ans.keys():
            ans[summation]=i
    return maxlen


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    k=int(input("Enter the sum : "))
    sol=longest_subarray_with_sum_k(arr,k)
    print("The length of the longest subarray with sum k is :",sol)