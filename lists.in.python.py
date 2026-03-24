# 🐍 LISTS IN PYTHON

---

# 📚 1. What is a List?

A **List** in Python is a collection of items that are **ordered, mutable (changeable), and allow duplicate elements**.

Lists can store **multiple values in a single variable** and can contain **different types of data**, such as integers, strings, or even other lists.

Python lists are widely used because they are **flexible and easy to modify**.

---

# ✨ Features of Python Lists

✔ Ordered collection of elements  
✔ Mutable (elements can be changed)  
✔ Allows duplicate values  
✔ Can store different data types  
✔ Supports indexing and slicing  

---

# 🧾 Syntax

```python
my_list = [element1, element2, element3, ...]

💡 Example
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]

Explanation:

fruits → List of strings
numbers → List of integers
mixed → List containing different data types

🔎 Accessing Elements in a List

Elements in a list are accessed using index numbers.

Index starts from 0.

fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])

Output:

apple
banana
🔄 Modifying List Elements

Lists are mutable, which means their values can be changed.

fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"

print(fruits)

Output:

['apple', 'orange', 'cherry']
➕ Adding Elements to a List

You can add elements using append().

fruits = ["apple", "banana"]

fruits.append("cherry")

print(fruits)

Output:

['apple', 'banana', 'cherry']
➖ Removing Elements from a List

You can remove elements using remove().

fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")

print(fruits)

Output:

['apple', 'cherry']
📏 Length of a List

The len() function returns the number of elements in a list.

fruits = ["apple", "banana", "cherry"]

print(len(fruits))

Output:

3

