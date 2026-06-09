# Type Conversion in Python

marks = "88"
age = "19"
percentage = 87.4

# String to Integer
marks_int = int(marks)
age_int = int(age)

# Float to Integer
percentage_int = int(percentage)

# Integer to Float
marks_float = float(marks_int)

# Integer to String
age_str = str(age_int)

print("Marks:", marks_int, type(marks_int))
print("Age:", age_int, type(age_int))
print("Percentage:", percentage_int, type(percentage_int))
print("Marks Float:", marks_float, type(marks_float))
print("Age String:", age_str, type(age_str))
