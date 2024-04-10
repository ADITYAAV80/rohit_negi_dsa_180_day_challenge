from typing import *

def factorial(n:int):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)


def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    ans=[]
    for i in range(1,n+1):
        x=factorial(i)
        if x<=n:
            ans.append(x)
        else:
            break
    return ans

if __name__ == '__main__': 
    t = int (input ("Enter the number to check numbers whose factorial is less than the number : "))
    sol=factorialNumbers(t)
    for i in sol:
        print(f"{i}",end=" ")