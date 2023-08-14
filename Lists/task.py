'''To find uppercase or lower case '''

str1=input("Enter a Value = ")

if str1.islower():
    print(str1,"is a Lower Case")
elif str1.isupper():
    print(str1,"is a Upper Case")
elif str1.isdigit():
    print(str1,"is a Digit")
elif str1.isalnum():
    print(str1,"is a Alphanumeric")
elif str1.isalpha():
    print(str1,"is a Alphabet")
else :
    print(str1, "is a Speical Character")






