def count_of_subarr_with_givensum(arr,k):
    n = len(arr)
    total, count = 0,0
    ans=dict()
    for i in range(n):
        total+=arr[i]
        if total ==k:
            count+=1
        rem = total-k
        if rem in ans:
            count+=ans[rem]
        if total not in ans:
            ans[total]=1
        else:
            ans[total]+=1
    return count


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    k=int(input("Enter the sum : "))
    sol=count_of_subarr_with_givensum(arr,k)
    print("The no of subarray with given sum is :",sol)