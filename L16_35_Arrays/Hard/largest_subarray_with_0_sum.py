def longest_subarray_with_sum_k(arr):
    summation,maxlen=0,0
    n = len(arr)
    ans={}
    for i in range(n):
        summation+=arr[i]
        if summation==0:
            maxlen=max(maxlen,i+1)
        if summation in ans.keys():
            maxlen=max(maxlen,i-ans[summation])
        if summation not in ans.keys():
            ans[summation]=i
    return maxlen


if __name__=="__main__":
    nums=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=longest_subarray_with_sum_k(nums)
    print("The length of the longest subarray with sum k is :",sol)