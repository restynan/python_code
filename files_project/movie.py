import csv

movies = [
    {"name": "The matrix", "director": "Wachasi"},
    {"name": "Green book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]
# old code
"""
with open("movies_file.csv", "w") as movies_file:
    movies_file.write("name, director\n")
    for movie in movies:
        movies_file.write(f"{movie['name']},{movie['director']}\n")
"""
# improved
with open("movies_file.csv", "w") as movies_file:
    movies_writer = csv.DictWriter(movies_file, fieldnames=["name", "director"])
    movies_writer.writeheader()
    movies_writer.writerows(movies)

"""
with open("movies_file.csv", "r") as movies_file:
    content = movies_file.readlines()
    for line in content:
        columns = line.strip().split(",")
        print(f" name: {columns[0]},  director: {columns[1]}")
"""

#improved
with open("movies_file.csv", "r") as movies_file:
    dict_reader = csv.DictReader(movies_file)  # returns a dictionary
    #
    # for line in dict_reader:
    #     print("test")
    #     print(f"Name: {line['name']}, Director: {line['director']}")
    my_test = list(dict_reader)
    print(my_test)

