from  typing import *
ans=[]
def printNtimes(n: int) -> List[str]:
    if(n==0):
        return []
    else:
        ans=printNtimes(n-1)
        ans.append("Coding Ninjas")
    return ans

if __name__ == '__main__': 
    t = int (input ("Enter the number to print N times : "))
    sol=printNtimes(t)
    for i in sol:
        print(f"-->{i}",end="\n")