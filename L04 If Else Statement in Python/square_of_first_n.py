def main():
    a=int(input("Enter a number : "))
    for i in range(1,a+1,1):
        print(f"{i}^2 = ",i*i)

if __name__=="__main__":
    main()