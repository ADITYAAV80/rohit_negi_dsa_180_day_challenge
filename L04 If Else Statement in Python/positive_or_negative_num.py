def pos_or_neg(a):
    if a>=0:
        print(f"{a} is +ve")
    else:
        print(f"{a} is -ve")


if __name__=="__main__":
    a=int(input("Enter a number : "))
    pos_or_neg(a)