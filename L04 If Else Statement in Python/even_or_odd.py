def even_or_odd():
    a=int(input("enter your number:\n"))
    if(a%2==0):
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

if __name__=="__main__":
    even_or_odd()