def max_product_subarray(arr):

    n = len(arr)
    tempProduct=1
    maxProduct=1
    for i in range(n):
        tempProduct*=arr[i]
        if tempProduct>maxProduct:
            maxProduct=tempProduct
        if tempProduct==0:
            tempProduct=1
    return maxProduct

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by spaces : ").split(" ")))
    sol=max_product_subarray(arr)
    print("The Majority elements are :",sol)