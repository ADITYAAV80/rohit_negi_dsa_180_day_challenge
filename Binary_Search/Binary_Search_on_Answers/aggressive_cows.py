from math import ceil

def canWeArrange(nums,m,k):
    
    lastpos =0
    count = 0 
    for i in range(1,len(nums)):
        if nums[i]-nums[lastpos]>=m:
            count+=1
            lastpos = i
    count+=1
    if count>=k:
        return 1
    else:
        return 0

def aggressive_cows(arr,k):

    l,r = 1,max(arr)
    arr = sorted(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = canWeArrange(arr,m,k)
        print(l,r,m,ret)
        if ret==1:
            ans=m
            l=m+1
        else:
            r=m-1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array containing position of stalls: ").split(" ")))
    k = int(input("Enter no of aggresive cows : "))
    print("Maximum distance between each aggressive cow we can achieve is :", aggressive_cows(arr,k))