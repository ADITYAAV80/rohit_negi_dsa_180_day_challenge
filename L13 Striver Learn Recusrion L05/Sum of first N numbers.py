def sumFirstN(n: int) -> int:
    # Write your code here.
    if (n==0):
        return 0
    else:
        return n + sumFirstN(n-1)


if __name__ == '__main__': 
    t = int (input ("Enter the number to print N times : "))
    sol=sumFirstN(t)
    print(f"Solution  : {sol}")