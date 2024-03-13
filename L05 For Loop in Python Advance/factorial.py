
def main():
    n=(int(input("Enter a number : ")))
    x=0
    for i in range(1,n,1):
        n=n*i
    print(f"Factorial of number is {n}")


if __name__=="__main__":
    main()