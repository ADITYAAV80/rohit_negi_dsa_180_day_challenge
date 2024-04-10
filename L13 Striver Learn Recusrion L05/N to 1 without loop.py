from typing import List

def print_reverse(x:int, ans:list):
    if(x==0):
        return ans
    else:
        ans.append(x)
        print_reverse(x-1,ans)
    return ans

def printNos(x: int) -> List[int]:
    ans=[]
    sol=print_reverse(x,ans)
    return sol

if __name__ == '__main__': 
    t = int (input ("Enter the number to print N times : "))
    sol=printNos(t)
    for i in sol:
        print(f"{i}",end=" ")