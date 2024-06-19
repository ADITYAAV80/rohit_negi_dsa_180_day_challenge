def right_rotate_by_n_places(arr,k):
    n=len(arr)
    k=k%n
    right,left=k,n-k
    for i in range(0,right//2):
        arr[i],arr[right-1-i]=arr[right-1-i],arr[i]
    for i in range(0,left//2):
        arr[right+i],arr[n-1-i]=arr[n-1-i],arr[right+i]
    for i in range(0,n//2):
        arr[i],arr[n-1-i]=arr[n-1-i],arr[i]
    return arr

if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    k=int(input("Enter the number of rotations to right : "))
    sol=right_rotate_by_n_places(arr,k)
    print("The array rotated with",k,"places to right :",sol)
