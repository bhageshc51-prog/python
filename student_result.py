student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 35:
    result = "Pass"
else:
    result = "Fail"

print("\n--- Student Report ---")
print("Name :", student_name)
print("Marks :", marks)
print("Result :", result)
