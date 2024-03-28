def pattern(n:int):
    
    
    """pattern 1:  right angled triangle with * """
    print("\nPattern 1:")
    for i in range(1,n+1,1):
        for j in range(0,i,1):
            print("*",end="")
        print(end="\n")
    


    """pattern 2: right angled triangle with numbers"""
    print("\nPattern 2:")
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(f"{j}",end="")
        print(end="\n")
    


    """pattern 3 : right angled triangle with numbers"""
    print("\nPattern 3:")
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(f"{i}",end="")
        print(end="\n")



    """pattern 4 : right angled triangle with numbers"""
    print("\nPattern 4:")
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(f"{i+1-j}",end="")
        print(end="\n")



    """pattern5 : right angled triangle with alphabets"""
    print("\nPattern 5:")
    for i in range(97,97+n,1):
        for j in range(97,i+1,1):
            print(chr(i),end="")
        print(end="\n")



    """pattern6 : upper triangular matrix with *"""
    print("\nPattern 6:")
    for i in range(0,n,1):
        for j in range(0,n-i,1):
            print("*",end="")
        print(end="\n")
    


    """pattern7 : upper triangular matrix with ascending numbers"""
    print("\nPattern 7:")
    for i in range(0,n,1):
        for j in range(1,n+1-i,1):
            print(f"{j}",end="")
        print(end="\n")



    """pattern8 : right angled triangle with descending numbers"""
    print("\nPattern 8:")
    for i in range(0,n,1):
        for j in range(n,n-1-i,-1):
            print(f"{j}",end="")
        print(end="\n")


if __name__=="__main__":
    n=int(input("please enter a number : "))
    pattern(n)