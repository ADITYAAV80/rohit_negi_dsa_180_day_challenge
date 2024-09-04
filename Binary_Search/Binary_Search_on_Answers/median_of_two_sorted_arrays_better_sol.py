def findMedianSortedArrays(nums1, nums2):
        
        i,j=0,0
        n,m = len(nums1),len(nums2)
        
        ind1 = (n+m-1)//2
        ind2 = (n+m)//2
        
        ele1,ele2 = 0,0
        cnt = 0

        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                if cnt == ind1:
                    ele1 = nums1[i]
                if cnt == ind2:
                    ele2 = nums1[i]
                i+=1
                cnt+=1
            else:
                if cnt == ind1:
                    ele1 = nums2[j]
                if cnt == ind2:
                    ele2 = nums2[j]
                j+=1
                cnt+=1
        while i<n:
            if cnt == ind1:
                ele1 = nums1[i]
            if cnt == ind2:
                ele2 = nums1[i]
            i+=1
            cnt+=1
        while j<m:
            if cnt == ind1:
                ele1 = nums2[j]
            if cnt == ind2:
                ele2 = nums2[j]
            j+=1
            cnt+=1

        if (n+m)%2==0:
            return float(ele1+ele2)/2
        else:
            return float(ele1)

if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    arr2 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    print("Median of two sorted arrays is :", findMedianSortedArrays(arr1,arr2))