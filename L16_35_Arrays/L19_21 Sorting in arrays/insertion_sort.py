def insertionsort(arr: list,n :int):
    for i in range(0,n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr


if __name__=="__main__":
    inp=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    print("Sorted array is :",insertionsort(inp,len(inp)))