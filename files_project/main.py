my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()
print(file_content)

user_name = input("Enter your name: ")
my_file_writing = open("data.txt", "w")  # open a file in "w" erases all the content
my_file_writing.write(user_name)
my_file_writing.close()

# ask the user for aa list of friends
# For each friend, we will tell the user whether they are nearby
# for each nearby friend , we will add them to  nearby_friends.tx
friends = input("Enter a comma separated list of your friend(no spaces, please): ")
friends_list = friends.split(",")
print(friends_list)

people = open("people.txt", "r")
people_content = [line.strip() for line in people.readlines()]
people.close()
print(people_content)

near_by_friends = set(friends_list).intersection(set(people_content))

nearby_friends_file = open("nearby_friends.txt", "w")

for friend in near_by_friends:
    print(f"{friend} is nearby")
    nearby_friends_file.write(f"{friend}\n")

nearby_friends_file.close()
