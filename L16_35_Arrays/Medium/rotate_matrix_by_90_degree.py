def rotate_array(arr,n):
    for i in range(0,n):
        for j in range(0,i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(0,n):
        arr[i].reverse()
    return arr

if __name__=="__main__":
    n=int(input("Enter no of rows and columns : "))
    arr=[[0 for i in range(n)] for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            print("Enter element arr[",i,"][",j,"] : ",end="")
            arr[i][j]=int(input())
    print("Your array is :-")
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    sol=rotate_array(arr,n)
    print("Solution of array by setting matrix to zero :-")
    for i in range(n):
        for j in range(n):
            print(sol[i][j],end=" ")
        print()