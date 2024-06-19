def linear_search(arr,key):
    for i in arr:
        if i==key:
            return "Yes"
    return "No"


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    key=int(input("Enter the key : "))
    sol=linear_search(arr,key)
    print("The element has been found? :",sol)