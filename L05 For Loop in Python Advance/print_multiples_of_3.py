def main():
    n=int(input("Enter a Number"))
    for i in range(0,n+1):
        if(i%3==0):
            print(f"{i}",end=", ")

if __name__=="__main__":
    main()