from math import ceil

def canWeFormBouquets(nums,k,m,day):
    
    noOfBouquets = 0
    count = 0
    for i in range(len(nums)):
        if day>=arr[i]:
            count+=1
        else:
            noOfBouquets+=count//k
            count=0
    noOfBouquets+=count//k
    if noOfBouquets>=m:
        return 1
    else:
        return 0

def minDays(arr,k,m):

    if m*k>len(arr):
        return -1
        
    l,r=min(arr),max(arr)
    ans = -1
    while l<=r:
        mid = (l+r)//2
        ret = canWeFormBouquets(arr,k,m,mid)
        if ret==1:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array containing blooming days : ").split(" ")))
    k = int(input("Enter no of adjacent flowers required for boquet : "))
    m = int(input("Enter the no of bouquets : "))
    print("Minimum number of days required to achieve result:", minDays(arr,k,m))