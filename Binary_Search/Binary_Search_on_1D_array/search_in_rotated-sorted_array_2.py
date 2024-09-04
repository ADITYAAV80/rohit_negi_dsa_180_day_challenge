def search_in_rotated_sorted_array_2(arr,k):
    
    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]==k:
            ans = m
        if arr[l]==arr[m] and arr[m]==arr[r]:
            l+=1
            m-=1
        if arr[l]<=arr[m]:
            if arr[l]<=k and k<=arr[m]:
                r=m-1
            else:
                l=m+1
        else:
            if arr[m]<=k and k<=arr[r]:
                l=m+1
            else:
                r=m-1
    return arr[ans]==k
        

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The key is found :", search_in_rotated_sorted_array_2(arr,k))