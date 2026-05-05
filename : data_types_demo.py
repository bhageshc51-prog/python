# file name: data_types_demo.py

username = "Bhagesh"
score = 95
is_active = True   # bool
height = 5.8       # float

print("Username:", username)
print("Score:", score)
print("Active Status:", is_active)
print("Height:", height)

# checking data types
print("\n--- Data Types ---")
print(type(username))
print(type(score))
print(type(is_active))
print(type(height))

# string to integer conversion
num_str = "250"
num_int = int(num_str)

print("\nConverted Value:", num_int)
print("Type after conversion:", type(num_int))
