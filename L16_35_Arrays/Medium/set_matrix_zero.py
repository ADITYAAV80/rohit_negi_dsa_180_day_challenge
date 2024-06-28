def set_matrix_zero(arr,m,n):
    col1=1
    for i in range(0,m):
        for j in range(0,n):
            if arr[i][j]==0:
                arr[i][0]=0
                if j!=0:
                    arr[0][j]=0
                else:
                    col1=0

    for i in range(m-1,0,-1):
        for j in range(n-1,0,-1):
            if arr[i][0]==0 or arr[0][j]==0:
                arr[i][j]=0

    if arr[0][0]==0:
        for j in range(n-1,-1,-1):
            arr[0][j]=0
    
    if col1==0:
        for i in range(m-1,0,-1):
            arr[i][0]=0
    
    return arr

    

if __name__=="__main__":
    m=int(input("Enter no of rows : "))
    n=int(input("Enter no of columns : "))
    arr=[[0 for i in range(n)] for i in range(m)]
    for i in range(0,m):
        for j in range(0,n):
            print("Enter element arr[",i,"][",j,"] : ",end="")
            arr[i][j]=int(input())
    print("Your array is :-")
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()
    sol=set_matrix_zero(arr,m,n)
    print("Solution of array by setting matrix to zero :-")
    for i in range(m):
        for j in range(n):
            print(sol[i][j],end=" ")
        print()