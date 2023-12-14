#1. Write a short guessing game program using a while loop. The user should be prompted
# to guess a number between 1 and 100, and you should tell them whether their guess was
# too high or too low after each guess. The loop should keeping running until the user
# guesses the number correctly.
number = 27
guess = int(input("Guess a number between 1 and 100. Enter your guess here: "))

while guess != number:
    if guess < number:
        print(f"Your guess of {guess} was too low! Try again.")
        guess = int(input("What's your new guess? "))
    elif guess > number:
        print(f"Your guess of {guess} was too high! Try again.")
        guess = int(input("What's your new guess? "))

if guess == number:
    print(f"You guessed {guess} and my number was {number}! Nice job! Thanks for playing!")

#2. Use a loop and the continue keyword to print out every character in the string "Python",
# except the "o". Remember that strings are collections, and they are iterable, so you can
# iterate over the string, which will yield one character at a time.
test_word = "Python"

for letter in test_word:
    if letter == "o":
        continue
    else:
        print(letter)

#3. Using one of the examples from earlier or a solution entirely of your own, create a program
# that prints out every prime number between 1 and 100.
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(dividend)

print(primes)