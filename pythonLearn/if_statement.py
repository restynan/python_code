friends = ["Rolf", "Ruth"]
family = ["Peter", "John"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("yes he is my friend")
elif user_name in family:
    print("Hello family")
else:
    print("hello stranger")