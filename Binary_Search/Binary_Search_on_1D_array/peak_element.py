def peak_element_in_array(arr):
    
    n = len(arr)
    if n==1:
        return 0
    l,r=0,n-1
    while(l<=r):
        m=(l+r)//2
        if (m==0 or arr[m-1]<arr[m]) and (m==n-1 or arr[m]>arr[m+1]):
            return m
        elif arr[m]<arr[m+1]:
            l=m+1
        else:
            r=m-1
    return -1
            

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    print("The index of peak element in array is :", peak_element_in_array(arr))