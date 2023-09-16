number=int(input("enter a positive Number : "))

if number>0:
    if number % 2 ==0:
        print(number,"is EVEN")
    else:
        print(number,"is ODD")
else:
    print("Please Enter a Positive Number:")
