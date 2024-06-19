def maximum_consecutive_ones(arr):
    i,n=0,len(arr)
    maximum=0
    while(i<n):
        counter=0
        while(i<n and arr[i]==1):
            counter+=1
            i+=1
        i+=1
        print(counter)
        if(counter>maximum):
            maximum=counter
    return maximum

if __name__=="__main__":
    arr=list(map(int,input("Enter an integer array seperated by spaces : ").split(" ")))
    sol=maximum_consecutive_ones(arr)
    print("The number of maximum consecutive ones is :",sol)