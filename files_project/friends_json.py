# json is imported as a string
#  strings should have double quotes
import json

file = open("friends_json.txt", "r")
file_contents = json.load(file)  # reads  file and turns into dict
file.close()
print(file_contents["friends"])

cars = [
    {"make": "Ford", "model": "Focus"},
    {"make": "Toyota", "model": "Rav4"}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"make": "Ford", "model": "Focus"}]'
car_from_str = json.loads(my_json_string)  # reads  string and turns into dict
print(car_from_str)



