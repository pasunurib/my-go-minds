import pandas as pd


df=pd.DataFrame(columns=["Account Number","Name",
                         "Current Balance","Transaction Amount",
                         "Transaction Code","Net Balance"])
while True:
    acno=input("Enter the Account Number( or'exit' to finish): ")
    if acno.lower() == 'exit':
        break

    name=input("Enter Name: ")
    current_balance = float(input("Enter the current Balance: "))
    transaxction_amount = float(input("Enter the Transaction Amount: "))
    transaction_code = input("Enter Transaction Code (d/w for deposit/withdraw): ")

    if transaction_code.lower() == "d":
        net_balance = current_balance + transaxction_amount
    elif transaction_code.lower() == "w":
        net_balance=current_balance - transaxction_amount
    else:
        print("Invalid transaction code. Please enter 'd' or 'w' .")
        continue
    new_data= pd.DataFrame({"AccountNumber":[acno], "Name": [name], "Current Balance":[current_balance],
                  "Transaction Amount": [transaxction_amount],"Transaction Code":[transaction_code],
                  "Net Balance": [net_balance]})
    df = pd.concat([df,new_data],ignore_index=True)


print(df)