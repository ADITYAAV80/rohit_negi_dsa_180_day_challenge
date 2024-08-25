def upperBound(arr,k):
    n = len(arr)
    l,r = 0,n-1
    ans = n
    while(l<=r):
        m = (l+r)//2
        if arr[m]>=k:
            ans = m
            r=m-1
        else:
            l=m+1
    return ans

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The index of the key is :", upperBound(arr,k))