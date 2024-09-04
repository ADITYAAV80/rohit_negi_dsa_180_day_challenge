def min_in_rotated_sorted_array(arr):
    
    n = len(arr)
    l,r = 0,n-1
    minval = float('inf')
    while(l<=r):
        m = (l+r)//2
        print(l,r,m)
        if arr[l]<=arr[m]:
            minval=min(minval,arr[l])
            l = m+1
        else:
            minval=min(minval,arr[m])
            r = m-1
        print(minval)
    return minval        

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    print("The minimum element is found :", min_in_rotated_sorted_array(arr))