def partition(arr,low,high):
    pivot=arr[low]
    i,j=low,high
    while(i<j):
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>=pivot and j>=low+1:
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
        arr[j],arr[low]=arr[low],arr[j]
    return j

def quicksort(arr,i,j):
    if (i<j):
        pindex=partition(arr,i,j)
        quicksort(arr,i,pindex-1)
        quicksort(arr,pindex+1,j)

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    quicksort(arr,0,len(arr)-1)
    print("Sorted Array : ",arr)