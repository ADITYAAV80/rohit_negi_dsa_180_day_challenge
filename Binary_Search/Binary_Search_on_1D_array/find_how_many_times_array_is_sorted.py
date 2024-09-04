def min_in_rotated_sorted_array(arr):
    
    n = len(arr)
    l,r = 0,n-1
    minval = float('inf')
    minindex = float('inf')
    while(l<=r):
        m = (l+r)//2
        if arr[l]<=arr[m]:
            if arr[l]<minval:
                minval = arr[l]
                minindex = l
            l = m+1
        else:
            if arr[r]<minval:
                minval = arr[m]
                minindex = m
            r = m-1
    return minindex

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    print("The no of times array is rotated :", min_in_rotated_sorted_array(arr))