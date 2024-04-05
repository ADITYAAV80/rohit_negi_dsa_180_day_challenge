"""
Problem statement
You are given a number "n".

Find the number of digits of "n" that evenly divide "n".

Note:
A digit evenly divides "n" if it leaves no remainder when dividing "n".


Example:
Input: "n" = 336

Output: 3

Explanation:
336 is divisible by both "3" and "6". Since "3" occurs twice it is counted two times.
Note:
You don"t need to print anything. Just implement the given function.
"""

def countDigits(n: int) -> int:
    a=[]
    original_val=n
    while(n!=0):
        if(n%10!=0):
            a.append(n%10)
        n=n//10
    cnt=0
    for i in a:
        if original_val % i==0:
            cnt+=1
    return cnt

if __name__=="__main__":
    n=int(input("Enter a number : "))
    sol=countDigits(n)
    print("Solution :",sol)