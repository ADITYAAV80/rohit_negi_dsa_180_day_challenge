from math import ceil

def canHeEat(nums,m,h):
    
    total = 0
    for i in range(len(nums)):
        total+=ceil(nums[i]/float(m))
        if total>h:
            return 0
    return 1

def koko_eating_bananas(arr,h):

    l,r=1,max(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = canHeEat(arr,m,h)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array containing piles of bananas : ").split(" ")))
    h = int(input("Enter hours left before guards come back : "))
    print("The no of bananas to eat per hour is :", koko_eating_bananas(arr,h))