def firstOccurence(arr,k):
    
    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]==k:
            ans =m
            r=m-1
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1    
    return ans

def lastOccurence(arr,k):
    
    n = len(arr)
    l,r = 0,n-1
    ans = -1
    while(l<=r):
        m = (l+r)//2
        if arr[m]==k:
            ans =m
            l=m+1
        elif arr[m]<k:
            l=m+1
        else:
            r=m-1    
    return ans

    


def main(arr,k):
        return [firstOccurence(arr,k),lastOccurence(arr,k)]

if __name__ == "__main__":
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the key : "))
    print("The indexes for first and last occurence is :", main(arr,k))