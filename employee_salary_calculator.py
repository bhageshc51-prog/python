# Employee Salary Calculator

# Taking employee details
employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")

# Taking salary details
basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus amount: "))
deduction = float(input("Enter deduction amount: "))

# Calculating net salary
net_salary = basic_salary + bonus - deduction

# Salary grade
if net_salary >= 70000:
    salary_grade = "High Salary"
elif net_salary >= 40000:
    salary_grade = "Medium Salary"
else:
    salary_grade = "Low Salary"

# Displaying salary report
print("\n===== Employee Salary Report =====")
print("Employee Name :", employee_name)
print("Employee ID   :", employee_id)
print("Basic Salary  :", basic_salary)
print("Bonus         :", bonus)
print("Deduction     :", deduction)
print("Net Salary    :", net_salary)
print("Salary Grade  :", salary_grade)
