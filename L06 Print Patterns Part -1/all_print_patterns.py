def pattern():
    """pattern1"""
    print("pattern 1:")
    for i in range(0,5,1):
        print("*",end="")
    print("\npattern2:")
    
    """pattern2"""
    for i in range(0,5,1):
        for j in range(0,5,1):
            print("*",end="")
        print(end="\n")
    
    """pattern3"""
    print("\npattern3:")
    for i in range(1,6,1):
        for j in range(1,6,1):
            print(f"{i}",end="")
        print(end="\n")

    """pattern4"""
    print("\npattern4:")
    for i in range(1,6,1):
        for j in range(1,6,1):
            print(f"{j}",end="")
        print(end="\n")
    
    """pattern5"""
    print("\npattern5:")
    for i in range(1,6,1):
        for j in range(1,6,1):
            print(f"{6-j}",end="")
        print(end="\n")
    
    """pattern6"""
    print("\npattern6:")
    for i in range(97,102,1):
        for j in range(97,102,1):
            print(chr(i),end="")
        print(end="\n")
    
    """pattern7"""
    print("\npattern7:")
    for i in range(97,102,1):
        for j in range(97,102,1):
            print(chr(j),end="")
        print(end="\n")
    
    """pattern8"""
    print("\npattern8:")
    for i in range(0,5,1):
        for j in range(1,6,1):
            print("%2d"%((5*i)+j),end=" ")
        print(end="\n")

if __name__=="__main__":
    pattern()