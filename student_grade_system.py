# Student Grade Management System

# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks input
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculating total and average
total = subject1 + subject2 + subject3
average = total / 3

# Grade calculation
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

# Displaying result
print("\n===== Student Report =====")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total)
print("Average Marks:", round(average, 2))
print("Grade        :", grade)
