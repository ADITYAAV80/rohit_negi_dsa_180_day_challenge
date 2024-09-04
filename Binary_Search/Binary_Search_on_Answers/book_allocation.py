from math import ceil

def canWeDistribute(nums,pagelim,k):

    addpage,count = 0,0
    for i in range(0,len(nums)):
        addpage+=nums[i]
        if addpage>pagelim:
            count+=1
            addpage=nums[i]
    count+=1
    if count>k:
        return 0
    else:
        return 1

def book_allocation(arr,k):

    if k>len(arr):
        return -1
    l,r = max(arr),sum(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = canWeDistribute(arr,m,k)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter an array of books with pages: ").split(" ")))
    k = int(input("Enter no of students : "))
    print("Maximum number of pages that can be assigned to a student to be minimum :", book_allocation(arr,k))