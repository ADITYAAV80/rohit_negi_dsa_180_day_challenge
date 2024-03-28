def pattern(n:int):



    """pattern1 : print * in a row"""
    print("pattern 1:")
    for i in range(0,n,1):
        print("*",end="")
    print("\npattern2:")
    


    """pattern2 : print * in square matrix"""
    for i in range(0,n,1):
        for j in range(0,n,1):
            print("*",end="")
        print(end="\n")
    


    """pattern3 : print 1 to n in a square matrix"""
    print("\npattern3:")
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            print(f"{i}",end="")
        print(end="\n")



    """pattern4 : print 1 to n in a square matrix"""
    print("\npattern4:")
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            print(f"{j}",end="")
        print(end="\n")



    """pattern5 : print n to 1 in a sqaure matrix in reverse"""
    print("\npattern5:")
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            print(f"{(n+1)-j}",end="")
        print(end="\n")



    """pattern6 : print a to ascii(n+1) characters in a square matrix"""
    print("\npattern6:")
    for i in range(97,n+97,1):
        for j in range(97,n+97,1):
            print(chr(i),end="")
        print(end="\n")



    """pattern7 : print a to ascii(n+1) characters in a square matrix"""
    print("\npattern7:")
    for i in range(97,n+97,1):
        for j in range(97,n+97,1):
            print(chr(j),end="")
        print(end="\n")



    """pattern8 : print n*n numbers in the form of square matrix"""
    print("\npattern8:")
    for i in range(0,n,1):
        for j in range(1,n+1,1):
            print("%2d"%((n*i)+j),end=" ")
        print(end="\n")



if __name__=="__main__":
    n=int(input("please enter the number : "))
    pattern(n)