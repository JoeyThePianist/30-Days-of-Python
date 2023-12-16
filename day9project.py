#1. The program you write for this project should do the following: It should be able to accept
# a card number from the user. For this project, you can assume that the number will be entered
# as a single string of characters (i.e. there won't be any spaces between the numbers). However,
# you should be able to accept a card number with spaces at the start or end of the string.
# If you want to challenge yourself, you should try to be more versatile with regards to the format
# that you accept card numbers in.
# You may want to turn the user's input into a list of numbers, as that will make it easier to work with.
#2. The program should validate that card number using the Luhn algorithm described above. You should
# implement this algorithm yourself.
# After removing the checking digit and reversing the card number, you'll need a for loop to go over the
# credit card numbers. As you go through each digit, you must find a way to determine whether a digit is
# in an odd or an even position. Remember you can check the model solution if you get stuck!
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LUHN ALGORITHM 
# A. Remove the rightmost digit from the card number. This number is called the checking digit, and it
# will be excluded from most of our calculations.
# B. Reverse the order of the remaining digits.
# C. 1..For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.)
# and double them. 2..If any of the results are greater than 9, subtract 9 from those numbers.
# D. Add together all of the results and add the checking digit.
# E. If the result is divisible by 10, the number is a valid card number. If it's not, the card number is
# not valid.
# TEST NUMBER;
# BASE> 5893804115457289 A> 589380411545728X B> 827545114083985X C1> 16214585218016318810X C2> 725585218073981X
# D> 7 + 2 + 5 + 5 + 8 + 5 + 2 + 1 + 8 + 0 + 7 + 3 + 9 + 8 + 1 + 9 = 80 E> 80 is divisible by 10.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#3. Once the validation is complete, the program should inform the user whether or not the card number is
# valid by printing a string to the console.
card_number = int(input("Please enter your card number: ").replace(' ', ''))

# Turning the card number into a string
strify_card_num = str(card_number)

# Grabbing the length of the card stringified card number
x = len(strify_card_num)

# Removing the last digit of the card number per first part of algorithm
new_card_num = list(strify_card_num)
checking_digit = new_card_num.pop(-1)

# Reversing the card number per second part of algorithm
new_card_num.reverse()

# Doubling numbers at even indeces per third part of algorithm
index = 0

while index < 15:
    new_card_num[index] = int(new_card_num[index]) + int(new_card_num[index])
    index += 2

# After doubling even indeces, we must also subtract numbers above 9 by 9 per additional section of third part
index = 0

while index < len(new_card_num):
    if int(new_card_num[index]) > 9:
        new_card_num[index] -= 9
        index += 1
    else:
        index += 1

# Adding together all of the results along with the checking digit per the fourth part of the algorithm
num_sum = 0

for num in new_card_num:
    num_sum += int(num)

num_sum += int(checking_digit)

# Verifying if the sum is divisible by 10 per the final part of the algorithm
if num_sum % 10 == 0:
    print("This card is valid.")
else:
    print("This card is not valid.")
    