print("============================")
print("Program for Electricity Bill")
print("============================")

uni=int(input("Enter the Units :  "))
print("----------------------------")

if (uni>0 and uni<=100):
    print("Units :",uni,"Price:""Free")
elif(uni>100 and uni<=200):
    print("Units :",uni,"Price :",uni*5)
elif(uni>200 and uni<=400):
    print("Units :",uni,"Price :",uni*10)
else:
    print("Units :",uni,"Price : 5000")
print("============================")
