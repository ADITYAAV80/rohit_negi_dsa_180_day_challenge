def bitwiseComplement(n: int):
        binary=[]
        complement=[]
        if(n==0): return 1
        while(n!=0):
            binary.append(n%2)
            n=n//2
        for i in binary:
            if(i==0):
                complement.append(1)
            else:
                complement.append(0)
        sol=0
        for i in range(0,len(complement)):
            sol+=pow(2,i)*complement[i]
        return sol

if __name__ == '__main__': 
    t = int (input ("Enter the number to perform complement : "))
    sol=bitwiseComplement(t)
    print("1's complement of number:",sol)