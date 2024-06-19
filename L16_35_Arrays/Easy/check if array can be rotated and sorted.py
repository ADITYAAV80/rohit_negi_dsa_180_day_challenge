def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


def sorted_and_rotated(arr):
    for i in range(0,len(arr)):
        temp=arr[i:len(arr)]+arr[0:i]
        if sorted(temp) == True:
            return "Yes"
    return "No"


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=sorted_and_rotated(arr)
    print("The array can be sorted? :",sol)