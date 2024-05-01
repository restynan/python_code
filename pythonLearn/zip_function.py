#Zip function combining two lists , where the final is a tuple of two elements
# dict converts  a list of tuples to a dictionary
# dict([(test, 1)(test,2)])
friends ={"John", "Mark", "Tony"}
time_seen = [3,5,6]
long_timers = dict (zip(friends,time_seen))
print(long_timers)
