def leaders(arr):
    n=len(arr)
    leader=[arr[n-1]]
    for i in range(n-2,-1,-1):
        if arr[i]>=leader[-1]:
            leader.append(arr[i])
    return leader

if __name__=="__main__":
    arr=list(map(int,input("Enter array elements seperated by space: ").split(" ")))
    sol=leaders(arr)
    print("Leaders of array are : ",sol)