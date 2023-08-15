import re
str1 = input("Enter the Value = ")

if str1.isupper():
    print("Checking if the string '", str1, "' is uppercased or not")
    print(bool(re.match('[A-Z]', format(str1))))
elif str1.islower():
    print("Checking if the string '", str1, "' is lowercased or not")
    print(bool(re.match('[a-z]', format(str1))))
elif str1.isdigit():
    print("Checking if the Digit '", str1, "' is Digit or not")
    print(bool(re.match('[0-9]', format(str1))))
else:
    print("It is a Special Character")






