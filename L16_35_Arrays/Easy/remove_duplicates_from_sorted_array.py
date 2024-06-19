def remove_duplicates(arr):
    j=0
    for i in range(1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]
    return arr[0:j+1]


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=remove_duplicates(arr)
    print("The array with duplicates removed :",sol)