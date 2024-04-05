from typing import List
from math import *
def printDivisors(n: int) -> List[int]:
    # Write your code here
    a=set()
    i=1
    while(i*i<=n):
        if(n%i==0):
            a.add(i)
            a.add(n//i)
        i+=1
    return list(sorted(a)) 

if __name__=="__main__":
    m=int(input("Enter the number to print divisors: "))
    sol=printDivisors(m)
    print("Solution : ",end="")
    for i in sol:
        print(f"{i},",end="")