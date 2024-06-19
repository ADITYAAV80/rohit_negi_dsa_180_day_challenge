def second_max_element(arr):
    l,sl=0,-1
    for i in arr:
        if i > l:
            sl=l
            l=i
        elif i > sl and i < l:
            sl=i
    return sl


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=second_max_element(arr)
    print("The second largest element in array is :",sol)