
def main():
    n=int(input("enter value n : "))
    for i in range(0,n+1,1):
        if(i%2==0):
            print(f"{i}")

if __name__=="__main__":
    main()