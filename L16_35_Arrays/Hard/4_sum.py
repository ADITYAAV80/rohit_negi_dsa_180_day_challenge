def three_sum(arr,target):
    
    n = len(arr)
    arr.sort()
    print("Sorted array is",arr)
    sol=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            k=j+1
            l=n-1
            while k<l:
                total = arr[i]+arr[j]+arr[k]+arr[l]
                print(arr[i],arr[j],arr[k],arr[l],total)
                if total>target:
                    l-=1
                elif total<target:
                    k+=1
                else:
                    sol.append([arr[i],arr[j],arr[k],arr[l]])
                    l-=1
                    k+=1
    return sol    


if __name__=="__main__":
    """
    arr = list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    k = int(input("Enter the sum : "))
    """
    sol = three_sum([1,-2,3,3,5,7,9,-6],7)
    print("The quadraplets are :",sol)