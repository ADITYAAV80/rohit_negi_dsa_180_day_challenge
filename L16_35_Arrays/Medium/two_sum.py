def two_sum(arr,k):
    ans={}
    for i in range(0,len(arr)):
        rem=k-arr[i]
        if rem in ans.keys():
            return [ans[rem],i]
        ans[arr[i]]=i
    print(ans)



if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    k=int(input("Enter the sum : "))
    sol=two_sum(arr,k)
    print("The indices that form the given sum is :",sol)