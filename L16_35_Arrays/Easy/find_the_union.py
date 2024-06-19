def union(arr1,arr2):
    i,j,n,m=0,0,len(arr1)-1,len(arr2)-1
    ans=[]
    while(i<=n and j<=m):
        while(i+1<n and arr1[i]==arr1[i+1]):
            i+=1
        while(j+1<m and arr2[j]==arr2[j+1]):
            j+=1
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        elif arr1[i]==arr2[j]:
            ans.append(arr1[i])
            i+=1
            j+=1
        else:
            ans.append(arr2[j])
            j+=1
    while(i<=n):
        while(i+1<n and arr1[i]==arr1[i+1]):
            i+=1
        ans.append(arr1[i])
        i+=1
    while(j<=m):
        while(j+1<m and arr2[j]==arr2[j+1]):
            j+=1
        ans.append(arr2[j])
        j+=1
    return ans
        
if __name__=="__main__":
    arr1=list(map(int,input("Enter 1st integer array seperated by spaces : ").split(" ")))
    arr2=list(map(int,input("Enter 2nd integer array seperated by spaces : ").split(" ")))
    sol=union(arr1,arr2)
    print("The union of two arrays :",sol)