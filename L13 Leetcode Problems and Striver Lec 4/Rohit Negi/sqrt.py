def mySqrt(x: int) -> int:
    for i in range(0,x//2+2):
        if i*i<=x and (i+1)*(i+1)>x:
            return i
        
if __name__ == '__main__': 
    t = int (input ("Enter the number to find square root : "))
    sol=mySqrt((t))
    print(sol)
    