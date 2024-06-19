def max_element(arr):
    ans=0
    for i in arr:
        if i>ans:
            ans=i
    return ans



if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=max_element(arr)
    print("The maximum element in array is :",sol)