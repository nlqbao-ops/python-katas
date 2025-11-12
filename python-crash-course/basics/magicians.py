magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# range
numbers = list(range(1,6))
print(numbers)

# list comprehension 

squares = [value**2 for value in range(1,11)]
print(squares)

# slicing list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# copy list

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

# tuples: immutable lists

dimensions = (200, 50)
print(dimensions[0])
