def insertionsort(arr,i,n):
    if i==n:
         return
    j=i
    while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    insertionsort(arr,i+1,n)

if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    insertionsort(arr,0,len(arr))
    print("Sorted array is :",arr)