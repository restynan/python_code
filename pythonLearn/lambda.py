# lambda functions

divide = lambda x, y: x / y

print(divide(7, 2))
# Functions are first class citizens we can assign functions to variables, and we can pass them as variables to other
# function

avg = lambda seq: sum(seq) / len(seq)
# associations
operations = {
    "average": avg,
    "total": sum,  # for python function you don't need to put sum(seq)
    "top": max
}

students = [
    {"name": "John", "grades": (78, 99, 23, 56)},
    {"name": "Peter", "grades": (46, 39, 18, 68)},
    {"name": "ken", "grades": (98, 34, 35, 36)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation_from_user = input(f"Enter average,total, or top: ")
    operation_function = operations[operation_from_user]

    print(operation_function(grades))