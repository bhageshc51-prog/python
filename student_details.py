# File Name: student_details.py

# Student Information Program

student_name = "Rahul"
student_age = 21
student_branch = "Computer Science"
student_usn = "1BM23CS101"
student_cgpa = 8.7
is_hosteller = True

# Printing student details
print("----- STUDENT DETAILS -----")
print("Name :", student_name)
print("Age :", student_age)
print("Branch :", student_branch)
print("USN :", student_usn)
print("CGPA :", student_cgpa)
print("Hosteller :", is_hosteller)

# Checking data types
print("\n----- DATA TYPES -----")
print("Type of student_name :", type(student_name))
print("Type of student_age :", type(student_age))
print("Type of student_branch :", type(student_branch))
print("Type of student_usn :", type(student_usn))
print("Type of student_cgpa :", type(student_cgpa))
print("Type of is_hosteller :", type(is_hosteller))

# Subject marks
python_marks = 89
maths_marks = 95
electronics_marks = 78
english_marks = 85

# Total and average calculation
total_marks = python_marks + maths_marks + electronics_marks + english_marks
average_marks = total_marks / 4

print("\n----- MARKS DETAILS -----")
print("Python Marks :", python_marks)
print("Maths Marks :", maths_marks)
print("Electronics Marks :", electronics_marks)
print("English Marks :", english_marks)

print("\nTotal Marks :", total_marks)
print("Average Marks :", average_marks)

# Grade calculation
if average_marks >= 90:
    print("Grade : A+")
elif average_marks >= 75:
    print("Grade : A")
elif average_marks >= 60:
    print("Grade : B")
else:
    print("Grade : C")

# List example
subjects = ["Python", "Maths", "Electronics", "English"]

print("\n----- SUBJECT LIST -----")
for subject in subjects:
    print(subject)

# Dictionary example
student = {
    "Name": student_name,
    "Age": student_age,
    "Branch": student_branch,
    "CGPA": student_cgpa
}

print("\n----- DICTIONARY DATA -----")
for key, value in student.items():
    print(key, ":", value)

print("\nProgram Executed Successfully")
