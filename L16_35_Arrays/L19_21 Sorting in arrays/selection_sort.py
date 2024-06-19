def selection_sort(arr: list,n: int):
    for i in range(len(arr)):
            mini=i
            for j in range(i,len(arr)):
                if arr[j]<arr[mini]:
                    mini=j
            arr[i],arr[mini]=arr[mini],arr[i]
    return arr

if __name__=="__main__":
    inp=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    print("Sorted array is :",selection_sort(inp,len(inp)))
