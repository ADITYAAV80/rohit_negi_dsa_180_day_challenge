
def main():
    n=(int(input("Enter a number : ")))
    sum=0
    for i in range(0,n+1,1):
        sum+=i
    print(f"Sum of n natural numbers are: {sum}")

if __name__=="__main__":
    main()