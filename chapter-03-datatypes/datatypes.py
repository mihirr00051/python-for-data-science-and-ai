# Chapter 03: Datatypes in Python
# This file demonstrates core Python datatypes used in Data Science & AI


# 1. Numeric Datatypes
age = 22              # int
accuracy = 0.85       # float
complex_num = 2 + 3j  # complex

print("Numeric Datatypes:")
print(age, type(age))
print(accuracy, type(accuracy))
print(complex_num, type(complex_num))
print("-" * 40)


# 2. String Datatype
name = "shree"
domain = "Data Science & AI"

print("String Datatype:")
print(name)
print(domain)
print(type(name))
print("-" * 40)


# 3. Boolean Datatype
is_learning = True
has_experience = False

print("Boolean Datatype:")
print(is_learning, type(is_learning))
print(has_experience, type(has_experience))
print("-" * 40)


# 4. List Datatype (Mutable)
skills = ["Python", "Data Science", "AI"]

print("List Datatype:")
print(skills)
print(type(skills))
print("-" * 40)


# 5. Tuple Datatype (Immutable)
coordinates = (10, 20)

print("Tuple Datatype:")
print(coordinates)
print(type(coordinates))
print("-" * 40)


# 6. Set Datatype (Unique values)
unique_ids = {1, 2, 3, 3, 2}

print("Set Datatype:")
print(unique_ids)
print(type(unique_ids))
print("-" * 40)


# 7. Dictionary Datatype (Key-Value pairs)
student = {
    "name": "Shree",
    "field": "Data Science & AI",
    "level": "Beginner"
}

print("Dictionary Datatype:")
print(student)
print(student["name"])
print(type(student))
print("-" * 40)


# 8. None Datatype
result = None

print("None Datatype:")
print(result)
print(type(result))
print("-" * 40)
# End of Datatypes demonstration
