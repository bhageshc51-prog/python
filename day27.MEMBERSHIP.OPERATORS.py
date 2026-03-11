4. Membership Operators
Membership operators test for membership within a sequence, such as a list, string, or tuple. They return True or False based on whether the value is found in the sequence.

Membership Operators:
in: Returns True if the specified value is found in the sequence.
not in: Returns True if the specified value is not found in the sequence.
Examples:
my_list = [1, 2, 3, 4, 5]
my_string = "Python"

print(3 in my_list)  # Output: True (3 is in the list)
print(6 not in my_list)  # Output: True (6 is not in the list)
print("P" in my_string)  # Output: True ("P" is in the string)
print("z" not in my_string)  # Output: True ("z" is not in the string)