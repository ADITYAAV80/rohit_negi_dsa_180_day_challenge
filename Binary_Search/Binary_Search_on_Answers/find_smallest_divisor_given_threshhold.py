from math import ceil

def canWeDivide(nums,m,limit):
    
    total = 0
    for i in range(len(nums)):
        total+=ceil(nums[i]/float(m))
        if total>limit:
            return 0
    return 1

def find_smallest_divisor_given_threshhold(arr,limit):

    l,r=1,max(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = canWeDivide(arr,m,limit)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array : ").split(" ")))
    limit = int(input("Enter the threshhold: "))
    print("The smallest divisor to achieve sum below threshhold is:", find_smallest_divisor_given_threshhold(arr,limit))