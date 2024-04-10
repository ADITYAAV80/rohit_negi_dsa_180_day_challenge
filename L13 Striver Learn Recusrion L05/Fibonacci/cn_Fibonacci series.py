from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    ans=[]
    ans.append(0)
    n1,n2=1,1
    if(n==1):
        return ans
    else:
        for i in range(1,n):
            ans.append(n1)
            n1,n2=n2,n1+n2
        return ans

if __name__ == '__main__': 
    t = int (input ("Enter the number to generate fibonacci series : "))
    sol=generateFibonacciNumbers(t)
    for i in sol:
        print(f"{i}",end=" ")