# In case you're not familiar with the game, it goes like this:
# One player starts by saying the number 1.
# Each player then takes it in turns to say the next number, counting
# one at a time.
# If the number is divisible by 3, instead of saying the number, the
# player should say, "Fizz".
# If the number is divisible by 5, instead of saying the number, the
# player should say, "Buzz".
# If the number is divisible by 3and5, instead of saying the number, the
# player should say, "Fizz Buzz".
# If you make a mistake, you're usually eliminated from the game, and the
# game continues until there's only a single player remaining.
# If there are no mistakes, the first 15 rounds of Fizz Buzz should look
# like this:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz Buzz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For our version, we're only going to have a single player, the
# computer, and it's going to play the first 100 rounds of Fizz Buzz all
# by itself. In other words, we need to print out the first 100 items in
# the sequence, starting from 1.
for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)