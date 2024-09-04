def findKthelementSortedArrays(nums1, nums2, k):
        
        i,j=0,0
        n,m = len(nums1),len(nums2)
        k-=1
        ele = 0
        cnt = 0

        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                if cnt == k:
                    ele = nums1[i]
                i+=1
                cnt+=1
            else:
                if cnt == k:
                    ele = nums2[j]
                j+=1
                cnt+=1
        while i<n:
            if cnt == k:
                ele = nums1[i]
            i+=1
            cnt+=1
        while j<m:
            if cnt == k:
                ele = nums2[j]
            j+=1
            cnt+=1

        return ele

if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    arr2 = list(map(int,input("Enter the array elements seperated by spaces: ").split(" ")))
    k = int(input("Enter the value of k : "))
    print("Kth element of two sorted arrays is :", findKthelementSortedArrays(arr1,arr2,k))