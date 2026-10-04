employee_name=input("Enter your full name: ")
basic_salary=float(input("Enter your basic salary: "))
transport_allowance=float(input("Enter your transport allowance: "))
food_allowance=float(input("Enter your food allowance: "))

gross_salary=basic_salary+transport_allowance+food_allowance

print("=====================================")
print("           EMPLOYEE PAYSLIP          ")
print("=====================================")
print("Employee: ", employee_name)
print("Basic Salary: ", basic_salary)
print("Transport Allowance: ", transport_allowance)
print("Food Allowance: ", food_allowance)
print("-------------------------------------")

print("Gross Salary: ", gross_salary)