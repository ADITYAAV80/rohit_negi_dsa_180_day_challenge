def findMedianSortedArrays(nums1, nums2):

    n,m = len(nums1),len(nums2)

    if m<n:
        return findMedianSortedArrays(nums2,nums1)
    
    partition = (n+m+1)//2

    l,r=0,n
    while(l<=r):
        m1 = (l+r)//2
        m2 = partition - m1
        
        l1,l2 = -float('inf'),-float('inf')
        r1,r2 = float('inf'),float('inf')

        if m1>0:
            l1 = nums1[m1-1]
        if m2>0:
            l2 = nums2[m2-1]
        if m1<n:
            r1 = nums1[m1]
        if m2<m:
            r2 = nums2[m2]
        
        if l1>r2:
            r=m1-1
        if l2>r1:
            l=m1+1
        else:
            if (n+m)%2==0:
                return float(max(l1,l2) +  min(r1,r2))/2
            else:
                return max(l1,l2)


if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    arr2 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    print("Median of two sorted arrays is :", findMedianSortedArrays(arr1,arr2))