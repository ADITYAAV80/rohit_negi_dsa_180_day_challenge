def sqrt(n):

    l,r=0,n
    ans = -1
    while(l<=r):
        m=(l+r)//2
        if m*m<=n:
            ans = m
            l=m+1
        else:
            r=m-1
    return ans
            

if __name__ == "__main__":
    n = int(input("Enter the number you want square root of : "))
    print("The integer sqrt of number is :", sqrt(n))