def merge_two_sorted_array_without_es(arr1,arr2,n,m):
    i,j=n-1,0
    while i>=0 and j<=m and arr1[i]>arr2[j]:
        arr1[i],arr2[j]=arr2[j],arr1[i]
        i-=1
        j+=1
    arr1[0:n]=sorted(arr1[0:n])
    arr2=sorted(arr2)
    arr1[n:]=arr2

if __name__=="__main__":
    arr1 = list(map(int,input("Enter an integer array 1 seperated by spaces : ").split(" ")))
    arr2 = list(map(int,input("Enter an integer array 2 seperated by spaces : ").split(" ")))
    n = len(arr1)
    m = len(arr2)
    arr1.extend([0]*m)
    merge_two_sorted_array_without_es(arr1,arr2,n,m)
    print(arr1)
    