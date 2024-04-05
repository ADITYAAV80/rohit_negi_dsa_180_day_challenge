"""
    Sample Input 1 :
    0
    Sample Output 1 :
    0

    Sample Input 2 :
    12
    Sample Output 2 :
    805306368

    Explanation For Sample Input 1 :
    For the first test case :
    Since the given number N = 0 is represented as 
    00000000000000000000000000000000 in its binary 
    representation. So after reversing the bits, 
    it will become 00000000000000000000000000000000 
    which is equal to 0 only. So the output is 0.     



    For the second test case :
    Since the given number N = 12 is represented as 
    00000000000000000000000000001100 in its binary 
    representation. So after reversing the bits, it will 
    become 00110000000000000000000000000000, which is 
    equal to 805306368 only. So the output is 805306368.
"""

def binary(n:int):
    a=[]
    while n!=0:
        x=n%2
        a.append(x)
        n=n//2
    while len(a)!=32:
        a.append(0)
    return a

def decimal(n: list):
    x=0
    sum_list=0
    while x!=32:
         sum_list+=pow(2,31-x)*n[x]
         x+=1
    return(sum_list)

def reverseBits(n:int):
    x=binary(n)
    return(decimal(x))

if __name__=="__main__":
    n=int(input("Enter a number : "))
    sol=reverseBits(n)
    print("Solution :",sol)