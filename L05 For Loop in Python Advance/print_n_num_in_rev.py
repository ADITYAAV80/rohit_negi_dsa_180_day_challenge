def main():
    n=int(input("Enter a Number : "))
    for i in range(n,-1,-1):
        print(f"{i}",end=", ")

if __name__=="__main__":
    main()