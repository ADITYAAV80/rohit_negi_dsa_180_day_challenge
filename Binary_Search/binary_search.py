def binSearch(arr,k):
    n =len(arr)
    l,r=0,n-1
    while(l<=r):
        m = (l+r)//2
        if arr[m]==k:
            return m
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1
    return -1

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The index of the key is :", binSearch(arr,k))