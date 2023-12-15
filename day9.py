#1. Below is some simple data about characters from BoJack Horseman:
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
# The data contains the character name, the voice actor/actress who
# plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple
# in the following format:
# 'BoJack Horseman is a horse voiced by Will Arnet.'
# Note that you're going to have to change the species information to lowercase
# when you print it. If you need a reminder on how to do this, we covered it in
# day 3 of the first week.
for character, voice_actor, species in main_characters:
    print(f"{character} is a {species.lower()} voiced by {voice_actor}.")

#2. Unpack the following tuple into 4 variables:
student_info = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# The data represents a student's name, their student id number, and their major
# and minor disciplines in that order.
name, student_id, (major, minor) = student_info

print(f"{name} has a student ID of {student_id}. Their major is {major} and their minor is {minor}.")

#3. Investigate what happens when you try to zip two iterables of different
# lengths. For example, try to zip a list containing three items, and a tuples
# containing four items.
test_list = ["item 1", "item 2", "item 3"]
test_tuple = ("item 4", "item 5", "item 6", "item 7")
test_zip = zip(test_list, test_tuple)

print(list(test_zip))