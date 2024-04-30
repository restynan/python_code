# for loop
friends = ["John", "Ritah", "Peter"]
for friend in friends:
    print(friend)

elements = [3, 4, 2, 7, 7]

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# if loop succesufully run  do something or if there is a faulty car  break

cars = ["ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("stopping the production line")
        break
    print(f"This car is {status}")
    print(f"shipping new car to Customer")
else:
    print("All cars built successfully. No faulty cars")


# prime number

for n in range(2, 10):
    for i in range(2, n):
            if n % i== 0:
                print(f"{n} not prime number")
                break
    else:
        print(f"{n} is a prime number")