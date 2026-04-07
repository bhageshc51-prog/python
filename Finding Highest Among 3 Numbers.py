a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("a is highest")
elif b > a and b > c:
    print("b is highest")
else:
    print("c is highest")