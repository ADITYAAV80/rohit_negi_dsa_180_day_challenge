def firstOccurence(arr,k):
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

def lastOccurence(arr,k):

    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]>k:
            ans = m
            r=m-1
        else:
            l=m+1
    return ans-1


def floorAndCeil(arr,k):
    n = len(arr)
    fo = firstOccurence(arr,k)
    
    if fo ==-1 or fo==n or arr[fo]!=k:
        return [-1,-1]
    else:
        return [fo,lastOccurence(arr,k)]

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The indexes for floor and ceil for given key is :", floorAndCeil(arr,k))