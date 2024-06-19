def left_rotate_by_one_space(arr):
    temp=arr[0]
    for i in range(0,len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=temp
    return arr


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=left_rotate_by_one_space(arr)
    print("The array rotated by one place to left :",sol)