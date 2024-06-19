def sort_an_array_of_0s_1s_2s(arr):
    low,mid,high=0,0,len(arr)-1
    i=0
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high],arr[mid]=arr[mid],arr[high]
            high-=1
    return arr

if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=sort_an_array_of_0s_1s_2s(arr)