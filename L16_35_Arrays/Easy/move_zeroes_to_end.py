def move_zeroes_to_end(arr):
    n=len(arr)
    j=0
    for i in range(0,n):
       if arr[i]!=0:
           arr[j],arr[i]=arr[i],arr[j]
           j+=1
    return arr
            


if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=move_zeroes_to_end(arr)
    print("The array with zeroes moved to end :",sol)