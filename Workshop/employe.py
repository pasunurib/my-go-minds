# Input employee details
employee_no = input("Enter employee number: ")
employee_name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
designation = input("Enter employee designation (manager/accountant/clerk): ")

# Calculate bonus based on designation
if designation == "manager":
    bonus = 0.20 * salary
elif designation == "accountant":
    bonus = 0.10 * salary
elif designation == "clerk":
    bonus = 0.05 * salary
else:
    bonus = 0

# Calculate total salary including bonus
total_salary = salary + bonus

# Display employee details and total salary
print("\nEmployee Details:")
print("Employee Number:", employee_no)
print("Employee Name:", employee_name)
print("Designation:", designation)
print("Salary: $",salary)
print("Bonus: $",bonus)
print("Total Salary: $",total_salary)
