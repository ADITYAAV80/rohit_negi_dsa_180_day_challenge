def main():
    a=str(input("Enter a character : "))
    if(a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
        print(f"{a[0]} is a vowel")
    else:
        print(f"{a[0]} is a consonant")

if __name__=="__main__":
    main()