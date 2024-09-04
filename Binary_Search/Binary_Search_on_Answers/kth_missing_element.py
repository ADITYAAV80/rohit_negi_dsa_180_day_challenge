def kth_missing_element(arr,k):

    l,r = 0,len(arr)-1
    ans = -1
    while l<=r:
        m = (l+r)//2
        diff = arr[m]-m-1
        if diff>=k:
            r=m-1
        else:
            l=m+1
    return k+l

if __name__ == "__main__":
    arr = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    k = int(input("Enter the k value to find kth missing number : "))
    print("kth missing element is :", kth_missing_element(arr,k))