def bubble_sort(arr,n):
    if n==1:
        return
    for j in range(0,n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    bubble_sort(arr,n-1)

if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    bubble_sort(arr,len(arr))
    print("Sorted array is :",arr)