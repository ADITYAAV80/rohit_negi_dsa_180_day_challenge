def findFloor(arr,k):
    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]<=k:
            ans = m
            l=m+1
        else:
            r=m-1
    return ans

def findCeil(arr,k):

    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]>=k:
            ans = m
            r=m-1
        else:
            l=m+1
    return ans


def floorAndCeil(arr,k):
    floor = findFloor(arr,k)
    ceil = findCeil(arr,k)
    return [floor,ceil]

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The indexes for floor and ceil for given key is :", floorAndCeil(arr,k))