from typing import *
i=0
def reverseArray(n: int, nums: List[int],i=0) -> List[int]:
    if i >=n//2:
        return nums
    else:
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
        return reverseArray(n,nums,i+1)

if __name__ == '__main__': 
    t = list(map(int,input("Enter the list numbers seperated by space : ").split()))
    sol=reverseArray(len(t),t)
    print("Reversed List : ",end="")
    for i in sol:
        print(f"{i}",end=" ")