def calcGDC(m: int, n: int) -> int:
    if n==0:
        return m
    return calcGDC(n,m%n)

if __name__=="__main__":
    m=int(input("Enter the number 1 : "))
    n=int(input("Enter the number 1 : "))
    sol=calcGDC(m,n)
    print("Solution :",sol)