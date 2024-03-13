def main():
    """pattern 1: lower triangular matrix"""
    print("\nPattern 1:")
    for i in range(1,6,1):
        for j in range(0,i,1):
            print("*",end="")
        print(end="\n")
    
    """pattern 2: ascending number pattern"""
    print("\nPattern 2:")
    for i in range(1,6,1):
        for j in range(1,i+1,1):
            print(f"{j}",end="")
        print(end="\n")
    
    """pattern 3"""
    print("\nPattern 3:")
    for i in range(1,6,1):
        for j in range(1,i+1,1):
            print(f"{i}",end="")
        print(end="\n")
    
    """pattern 4"""
    print("\nPattern 4:")
    for i in range(1,6,1):
        for j in range(1,i+1,1):
            print(f"{i+1-j}",end="")
        print(end="\n")

    """pattern5"""
    print("\nPattern 5:")
    for i in range(97,102,1):
        for j in range(97,i+1,1):
            print(chr(i),end="")
        print(end="\n")
    
    """pattern6"""
    print("\nPattern 6:")
    for i in range(0,5,1):
        for j in range(0,5-i,1):
            print("*",end="")
        print(end="\n")
    
    """pattern7"""
    print("\nPattern 7:")
    for i in range(0,5,1):
        for j in range(1,6-i,1):
            print(f"{j}",end="")
        print(end="\n")

    """pattern8"""
    print("\nPattern 8:")
    for i in range(0,5,1):
        for j in range(5,4-i,-1):
            print(f"{j}",end="")
        print(end="\n")


if __name__=="__main__":
    main()