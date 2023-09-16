num1=float(input("Enter the num1: "))
num2=float(input("Enter the num2: "))
num3=float(input("Enter the num3: "))

if num1 >= num2 and num2 >= num3:
    print(f"The biggest number is : {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The biggest number is : {num2}")
else:
    print(f"The biggest number is : {num3}")
