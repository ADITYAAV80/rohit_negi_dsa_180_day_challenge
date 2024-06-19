
def factorial(n:int):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)
    


if __name__=="__main__":
    n=(int(input("Enter a number : ")))
    x=factorial(n)
    print(f"Factorial of number is {x}")