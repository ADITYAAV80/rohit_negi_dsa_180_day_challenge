from math import ceil

def painterPartitionPossible(nums,boardlim,k):

    noofBoards,count = 0,0
    for i in range(0,len(nums)):
        noofBoards+=nums[i]
        if noofBoards>boardlim:
            count+=1
            noofBoards=nums[i]
    count+=1
    if count>k:
        return 0
    else:
        return 1

def painter_partition(arr,k):

    if k>len(arr):
        return -1
    l,r = max(arr),sum(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = painterPartitionPossible(arr,m,k)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter an array of boards with length of each board: ").split(" ")))
    k = int(input("Enter no of painters : "))
    print("Maximum number among those boards such that minimum number of boards is assigned to each painter is to be :", painter_partition(arr,k))