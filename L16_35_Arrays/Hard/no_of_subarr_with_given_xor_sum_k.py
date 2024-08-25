def no_of_subarr_with_given_xor_sum_k(arr,k):
    total, count = 0,0
    ans={}
    n = len(arr)
    for i in range(n):
        total^=arr[i]
        if total == k:
            count+=1
        rem=total^k
        if rem in ans:
            count+=ans[rem]
        if total not in ans:
            ans[total]=1
        else:
            ans[total]+=1
    return count

if __name__=="__main__":
    nums=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    k=int(input("Enter the xor value : "))
    sol=no_of_subarr_with_given_xor_sum_k(nums,k)
    print("The number of subarray with xor sum k is :",sol)