Age=int(input("Enter your age= "))

if Age>=18:
    print("You are  Eligible for vote")
else:
    print("You are not Eligible for vote")


''' How to find an odd or even number '''

Num=int(input("Enter the number: "))

if (Num%2)==0:
    print("{0} is a Even number".format(Num))
else:
    print("{0} is a Odd number".format(Num))


'''To find Maximum and Minimum numbers'''

X=int(input("Enter the Value of X= "))
Y=int(input("Enter the Value of Y= "))

if X>Y:
    print("X is a Greater Value".format(X))
elif Y>X:
    print("Y is a Greater Value".format(Y))
elif X==Y:
    print("Both are Same numbers")
else:
    print("Task is Pending")

#To find positive or Negative

num=int(input("Enter the Number= "))

if num>0:
    print(num," It is a Positive number")
elif num==0:
    print(num," It is a Zero")
else:
    print(num," It is a Negative number")


'''To find uppercase or lower case '''

ch=input("Enter a Character = ")

if ch.islower():
    print(ch,"is a Lower Case")
elif ch.isupper():
    print(ch,"is a Upper Case")
elif ch.isalnum():
    print(ch,"is a Alphanumeric")
elif ch.isdigit():
    print(ch,"is a Digit")
elif ch.isalpha():
    print(ch,"is a Alphabet")
else:
    print(ch, "is a Speical Character")





