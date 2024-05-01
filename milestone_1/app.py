MENU_PROMPT = "\nEnter 'a' to adda movie, 'I' to see your movies, 'f' to find a movie by title, or 'q' t quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def print_movie(movie):
    print(f"Title : {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f"Release year : {movie['year']}")


def show_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    title = input("Enter movie title: ")
    for movie in movies:
        if movie["title"] == title:
            print_movie(movie)


user_options ={
    "a": add_movie,
    "I": show_movies,
    "f": find_movie,
}


def operation():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            user_operation = user_options[selection]
            user_operation()
            selection = input(MENU_PROMPT)
        else:
            print("unknown command, please try again")


operation()

if __name__ == '__main__':
    print("hi")


"""while selection != "q":
    if selection == "a":
        add_movie()
    elif selection == "I":
        show_movies()
    elif selection == "f":
        find_movie()"""