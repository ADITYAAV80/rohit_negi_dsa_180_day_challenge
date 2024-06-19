def pattern(n:int):
    


    """pattern 1:
        *
       ***
      ***** 
    *********
    """
    print("\nPattern 1:")
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*(i-1)+1):
            print("*",end="")
        for j in range(0,n-i):
            print(" ",end="")
        print(end="\n")



    """pattern 2:
    *********
      *****
       ***
        *
    """
    print("\nPattern 2:")
    for i in range(1,n+1):
        for j in range(0,i-1):
            print(" ",end="")
        for j in range(0,2*(n-i)+1):
            print("*",end="")
        for j in range(0,i-1):
            print(" ",end="")
        print(end="\n")



    """pattern 3:
        *
       ***
      ***** 
    *********    
    *********
      *****
       ***
        *
    """
    print("\nPattern 3:")
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*(i-1)+1):
            print("*",end="")
        for j in range(0,n-i):
            print(" ",end="")
        print(end="\n")
    for i in range(1,n+1):
        for j in range(0,i-1):
            print(" ",end="")
        for j in range(0,2*(n-i)+1):
            print("*",end="")
        for j in range(0,i-1):
            print(" ",end="")
        print(end="\n")



    """pattern 4:
    *
    **
    ***
    **
    *
    """
    print("\nPattern 4:")
    for i in range(1,2*n+1):
        for j in range(0,n-abs(n-i)):
            print("*",end="")
        print(end="\n")



    """pattern 5:
    1
    01
    101
    0101
    10101
    """
    print("\nPattern 5:")
    for i in range(1,n+1):
        for j in range(0,i):
            print((i+j)%2,end="")
        print(end="\n")
    
    """pattern 6:
            1
           121
          12321
         1234321 
    """
    print("\nPattern 6:")
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        for j in range(0,n-i):
            print(" ",end="")
        print(end="\n")
    
    """pattern 7:
            A
           ABA
          ABCBA
         ABCDCBA 
    """
    print("\nPattern 7:")
    for i in range(1,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(65,i+65):
            print(chr(j),end="")
        for j in range(65+i-2,64,-1):
            print(chr(j),end="")
        for j in range(0,n-i):
            print(" ",end="")
        print(end="\n")
    
    
    
    """pattern 8:
        1    1
        12  21      
        123321
    """
    print("\nPattern 8:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(0,2*(n-i)):
            print(" ",end="")
        for j in range(i,0,-1): 
            print(j,end="")
        print(end="\n")
    

    """pattern 9:
    ********
    ***  ***
    **    **
    *      *
    *      *
    **    **
    ***  ***
    ********
    """
    print("\nPattern 9:")
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        for j in range(0,i*2):
            print(" ",end="")
        for j in range(0,n-i):
            print("*",end="")
        print(end="\n")
    for i in range(n,0,-1):
        for j in range(0,n-i+1):
            print("*",end="")
        for j in range(0,(i-1)*2):
            print(" ",end="")
        for j in range(0,n-i+1):
            print("*",end="")
        print(end="\n")    



    """pattern 10:
    *             *
    * *         * *
    * * *     * * *
    * * * * * * * *
    * * *     * * *
    * *         * *
    *             *
    """
    print("\nPattern 10:")
    for i in range(1,n+1):
        for j in range(0,i):
            print("*",end=" ")
        for j in range(0,(n-i)*2):
            print(" ",end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print(end="\n") 
    for i in range(n-1,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        for j in range(0,(n-i)*2):
            print(" ",end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print(end="\n")



    """pattern 11:
    ****
    *  *
    *  *
    ****
    """
    print("\nPattern 11:")
    for i in range(0,n):
        for j in range(0,n):
            if(i==0 or j==0 or i==n-1 or j==n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print(end="\n")
    
    """pattern 12:
    33333
    32223
    32123
    32223
    33333
    ****
    """
    print("\nPattern 12:")
    for i in range(0,2*n-1):
        for j in range(0,2*n-1):
            left=i
            top=j
            right= 2*n-1-i-1
            bottom=2*n-1-j-1
            a=min(left,top,right,bottom)
            print((n-a),end="")
        print(end="\n")



if __name__=="__main__":
    n=int(input("please enter a number : "))
    pattern(n)