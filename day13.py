#1. Define a exponentiate function that takes in two numbers. The first is the base,
# and the second is the power to raise the base to. The function should return the result
# of this operation. Remember we can perform exponentiation using the ** operator.
def exponentiate(num, power):
    return num ** power

#2. Define a process_string function which takes in a string and returns a new string which
# has been converted to lowercase, and has had any excess whitespace removed.
def process_string(string):
    return string.strip().lower()

#3. Write a function that takes in a tuple containing information about an actor and returns
# this data as a dictionary. The data should be in the following format:
# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.
actor_data = ("Johnny Dogs", "Irish", 37)
def actor_parser(actor_data):
    name, nationality, age = actor_data
    return {
        "Name" : name,
        "Nationality" : nationality,
        "Age" : age
    }

#4. Write a function that takes in a single number and returns True or False depending on
# whether or not the number is prime. If you need a refresher on how to calculate if a number
# is prime, we show one method in day 8 of the series.
def prime_number(dividend):
    if dividend < 2:
        return False
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            return False
    else:
        return True