# Electricity Bill Calculator

# Taking customer details
customer_name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")

# Taking electricity units
units = int(input("Enter electricity units consumed: "))

# Calculating bill amount
if units <= 100:
    bill = units * 2
elif units <= 300:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (200 * 3) + ((units - 300) * 5)

# Displaying bill report
print("\n===== Electricity Bill =====")
print("Customer Name :", customer_name)
print("Customer ID   :", customer_id)
print("Units Used    :", units)
print("Total Bill    : ₹", bill)
