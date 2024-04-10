from typing import List
ans=[]
def printNos(x: int) -> List[int]: 
    # Write your code here
    if(x==0):
        return []
    else:
        ans=printNos(x-1)
        ans.append(x)
    return ans

if __name__ == '__main__': 
    t = int (input ("Enter the number to print 1 to N : "))
    sol=printNos(t)
    for i in sol:
        print(f"{i}",end=" ")