def main():
    n=int(input("enter value n : "))
    for i in range(0,n+1,2):
        print(f"{i}",end=", ")

if __name__=="__main__":
    main()