def find_missing_no_in_array(arr):
    n=len(arr)
    return n*(n+1)//2-sum(arr)



if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=find_missing_no_in_array(arr)
    print("The missing element is :",sol)