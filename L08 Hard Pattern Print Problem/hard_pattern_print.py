def main():
    for i in range(1,6,1):
        for j in range(1,2,1):
            print(" "*(6-i),"*"*i,end="")
        print(end="\n")

if __name__=="__main__":
    main()