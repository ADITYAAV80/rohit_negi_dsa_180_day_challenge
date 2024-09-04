from math import ceil

def canWeTransport(nums,weight_lim,dayLim):
    addweight,count = 0,0
    for i in range(0,len(nums)):
        addweight+=nums[i]
        if addweight>weight_lim:
            count+=1
            addweight=nums[i]
            if addweight>weight_lim:
                return 0
    count+=1
    if count>dayLim:
        return 0
    else:
        return 1

def capacity_to_ship(arr,days):

    if days==1:
        return sum(arr)
    l,r = max(arr),sum(arr)
    ans = -1
    while l<=r:
        m = (l+r)//2
        ret = canWeTransport(arr,m,days)
        if ret==1:
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter an array of weights on belts: ").split(" ")))
    days = int(input("Enter no of days : "))
    print("Least weight capacity of the ship :", capacity_to_ship(arr,days))