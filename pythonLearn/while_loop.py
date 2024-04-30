# while_loop
# when you want to do something undefined number of times
user_input = input("Are you still learning? (yes/no): ")
while user_input == "yes":
    print("You're learning")
    user_input = input("Are you still learning? (yes/no): ")

user_input_ = input("Do you want to continue? (Enter y/q)")

while user_input_ != "q":
    if user_input_ == "y":
        print("hello")
    user_input_ = input("Do you want to continue? (Enter y/q)")
