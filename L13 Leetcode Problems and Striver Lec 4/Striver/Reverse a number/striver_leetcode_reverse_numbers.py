def reverse(x: int):
    rev=0
    original_no=x

    """dealing with negative_no"""
    if x<0:
        x=x*-1
        
    """reverse a number"""
    while x>0:
        n=x%10
        rev=rev*10+n
        x=x//10  
        
    """correction for negative numbers"""
    if original_no<0:
        rev=rev*-1

    """returning value"""   
    if rev>(-1*pow(2,31)) and rev<pow(2,31)-1:
        return rev
    else:
        return 0

if __name__=="__main__":
    n=int(input("Enter a number : "))
    sol=reverse(n)
    print("Reverse of",n,"is :",sol)