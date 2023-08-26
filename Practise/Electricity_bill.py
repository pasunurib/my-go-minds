print("============================")
print("Program for Electricity Bill")
print("============================")

def Bill_001(units):
    if units<=100:
        bill=0
    elif units<=200:
        bill=5 * (units-100)
    elif units <=400:
        bill= 5 * 100+10* (units-200)
    else:
        bill=5*100 +10 *200+15 *(units-400)

    return bill

units_consumed=int(input("Enter the units consumed : "))
total_bill=Bill_001(units_consumed)
print(f"Electicity bill for {units_consumed} units: ${total_bill:2f}")



