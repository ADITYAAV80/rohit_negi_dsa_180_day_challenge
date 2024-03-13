def main():
    f=int(input("Enter the first number : "))
    s=int(input("Enter the second number : "))
    n=int(input("Enter the no of terms: "))
    sum=0
    print(f"{f}", end=", ")
    print(f"{s}", end=", ")
    for i in range(1,n+1,1):
        sum=f+s
        f=s
        s=sum
        print(sum, end=", ")

if __name__=="__main__":
    main()