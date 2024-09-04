from math import ceil

def PartitonPossible(nums,sumlim,max_splits):

    noOfSubarray,count = 0,0
    for i in range(0,len(nums)):
        noOfSubarray+=nums[i]
        if noOfSubarray>sumlim:
            count+=1
            noOfSubarray=nums[i]
    count+=1
    if count>max_splits:
        return 0
    else:
        return 1

def split_array(arr,max_splits):

    if max_splits>len(arr):
        return -1
    l,r = max(arr),sum(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = PartitonPossible(arr,m,max_splits)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter an array : ").split(" ")))
    max_splits = int(input("Enter max no of splits : "))
    print("Maxmimum partition among all partitons such that all partitons have minimum value is:", split_array(arr,max_splits))