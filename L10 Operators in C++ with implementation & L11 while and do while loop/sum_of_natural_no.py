def sum_n_terms(n:int):
    i=0
    sum_no=0
    while(i!=n):
        i+=1
        sum_no+=i
    return sum_no



if __name__=="__main__":
    n=int(input("Enter a number to find sum of natural numbers : "))
    x=sum_n_terms(n)
    print("Sum of",n,"natural numbers :",x)