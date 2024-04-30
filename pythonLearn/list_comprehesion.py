# comprehension with conditionals
numbers = [1, 2, 3, 4, 6]
doubled_values = [num * 2 for num in numbers]
print(doubled_values)

ages = [45, 89, 22, 97, 100]
odd_ages = [age for age in ages if age%2 == 1]
print(odd_ages)