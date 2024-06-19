def main():
    a=int(input("Enter the number : "))
    b=int(input("Enter the power : "))
    x=a
    for i in range(0,b):
        a=x*a
    print(f"ans = {a}")

if __name__=="__main__":
    main()