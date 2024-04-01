def pattern(n:int):


    
    """pattern 1:
            *
           **
          ***
         ****  
    """
    print("\nPattern 1:")
    for x in range(0,n):
        for i in range(0,n-x):
            print(" ",end="")
        for j in range(0,x+1):
            print("*",end="")
        print(end="\n")



    """pattern 2:
            1
           22
          333
         4444 
    """
    print("\nPattern 2:")
    for i in range(1,n+1):
        for j in range(0,(n-i)):
            print(" ",end="")
        for j in range(0,i):
            print(f"{i}",end="")
        print(end="\n")



    """pattern 3:
            1
           12
          123
         1234   
    """
    print("\nPattern 3:")
    for i in range(1,n+1):
        for j in range(0,(n-i)):
            print(" ",end="")
        for j in range(1,i+1):
            print(f"{j}",end="")
        print(end="\n")



    """pattern 4:
            a
           ab
          abc
         abcd   
    """
    print("\nPattern 4:")
    for i in range(1,n+1):
        for j in range(0,(n-i)):
            print(" ",end="")
        for j in range(97,97+i):
            print(f"{chr(j)}",end="")
        print(end="\n")



if __name__=="__main__":
    n=int(input("please enter a number : "))
    pattern(n)