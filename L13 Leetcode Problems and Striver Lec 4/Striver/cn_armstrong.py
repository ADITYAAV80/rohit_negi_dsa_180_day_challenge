n=int(input("Enter a number to check for armstrong : "))
sum_armstrong=0
org=n
while n!=0:
    sum_armstrong+=pow(n%10,len(str(org)))
    n=n//10
if sum_armstrong==org:
    print("The entered number is armstrong number")
else:
    print("The entered number is not an armstrong number")
