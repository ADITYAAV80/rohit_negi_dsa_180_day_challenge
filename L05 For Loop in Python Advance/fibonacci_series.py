def main():
    f=int(input("Enter the first number : "))
    s=int(input("Enter the second number : "))
    n=int(input("Enter the no of terms: "))
    sum=0
    print(f"{f}, {s}, ", end="")
    for i in range(1,n-1):
        s,f=f+s,s
        print(s, end=", ")

if __name__=="__main__":
    main()