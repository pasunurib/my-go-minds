import pandas as pd

Item=str(input("Enter the string ="))


Var= {
    'ITEMS': ["Tea","Coffee","Lemon.Tea","Boast","Milk"],
    'PRICE':[10,15,15,20,12]

}
data=pd.DataFrame(Var)
print(data)

