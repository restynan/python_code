def hundred_numbers_1():
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums


print(hundred_numbers_1())
print([x * 2 for x in hundred_numbers_1()])


# using generators
def hundred_numbers_g():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers_g()  # need when we do asy
print(next(g))
print(next(g))
print(list(g))


# All objects that have __next are called iterators
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))

for n in my_gen:
    print(n)


def starts_with_r(friend):
    return friend.startswith('R')


friends = ["Roth", "Mike", "Rita", "Moses", "Ruth"]

friends_start_r = filter(starts_with_r, friends)  # returns a generator
friends_start_r_ = filter(lambda friend: friend.startswith('R'), friends)  # same as above
friends_start_r__ = (f for f in friends if f.startswith('R'))  # same as above  called generator compression, its faster
print(next(friends_start_r))
print(list(friends_start_r))

friends_lower = map(lambda f: f.lower(), friends)
friends_lower_ = [f for f in friends if f.lower()]  # returns a list
friends_lower__ = (f for f in friends if f.lower())  # generator

# Any return to true if  any elements evaluates to true
# all return true if all values evaluate to true


friend_starts_with_m = [f for f in friends if f.startswith('M')]
if any(friend_starts_with_m):  # bool({dict}) true  if not empty
    print("you have friends starting with M")

print(all([1, 5, 6]))  # true
print(all([0, 1, 5, 6]))  # False because bool(0)-> false
