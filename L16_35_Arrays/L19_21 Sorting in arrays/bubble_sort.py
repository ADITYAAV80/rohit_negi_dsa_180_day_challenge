def bubbleSort(arr, n):
    # code here
    for i in range(n,0,-1):
        for j in range(0,n-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

if __name__=="__main__":
    inp=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    print("Sorted array is :",bubbleSort(inp,len(inp)))