def single_element_in_sorted_array(arr):
    
    n = len(arr)
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    l,r=1,n-2
    while(l<=r):
        m=(l+r)//2
        if arr[m-1]!=arr[m] and arr[m]!=arr[m+1]:
            return arr[m]
        elif (m%2==1 and arr[m]==arr[m-1]) or (m%2==0 and arr[m]==arr[m+1]):
            l=m+1
        else:
            r=m-1
    return -1
            

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    print("The single element in sorted array is :", single_element_in_sorted_array(arr))