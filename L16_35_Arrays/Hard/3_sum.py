def three_sum(arr,target):
    
    n = len(arr)
    arr.sort()
    print("Sorted array is",arr)
    sol=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=n-1
        while j<k:
            total = arr[i]+arr[j]+arr[k]
            if total>target:
                k-=1
            elif total<target:
                j+=1
            else:
                sol.append([arr[i],arr[j],arr[k]])
                j+=1
                k-=1
                while j<k and arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+1]:
                    k-=1
    return sol    


if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k=int(input("Enter the sum : "))
    sol=three_sum(arr,k)
    print("The triplets are :",sol)