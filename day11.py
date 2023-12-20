#1. Create an empty set and assign it to a variable.
empty_set = set()

#2. Add three items to your empty set using either several add calls,
# or a single call to update.
empty_set.add("item 1")
print(empty_set)
empty_set.update(["item 2", "item 3"])
print(empty_set)

#3. Create a second set which includes at least one common element with
# the first set.
empty_set_two = {"item 3"}

#4. Find the union, symmetric difference, and intersection of the two
# sets. Print the results of each operation.
print(empty_set.union(empty_set_two))
print(empty_set.symmetric_difference(empty_set_two))
print(empty_set.intersection(empty_set_two))

#5. Create a sequence of numbers using range, then ask the user to enter
# a number. Inform the user whether or not their number was within the
# range you specified.
# If you want an extra challenge, also tell the user if their number was
# too high or too low.
num_set = set()
num_set.update(range(27, 72))

guess = int(input("Let's play a game. It is really easy. Guess a number and if it's in the range of numbers I have set aside here, you win! What's your guess? "))

if guess in num_set:
    print("You guessed within my range. Good job!")
elif guess < 27:
    print("Your guess was too low.")
elif guess > 72:
    print("Your guess was too high.")
else:
    print("What are you doing?")