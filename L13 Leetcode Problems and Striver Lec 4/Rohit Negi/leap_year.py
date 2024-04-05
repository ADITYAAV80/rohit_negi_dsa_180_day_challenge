def isLeap (N):
    if(N%4==0):
        if(N%100!=0 or N%400==0):
            return "Leap Year"
    return "Not a Leap Year"


if __name__ == '__main__': 
    t = int (input ("Enter the year : "))
    sol=isLeap((t))
    print(sol)
