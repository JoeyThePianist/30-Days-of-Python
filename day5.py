#1. Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding
# the memory address for a given value, and we can compare memory addresses to check for identity.
name = "Joey"
name_again = "Joey"
print(f"For testing purposes, the value entered for name and name_again is 'Joey'.")
print(f"This is the value for name: {name}.")
print(f"This is the value for name_again: {name_again}.")
print(f"This is the ID for name: {id(name)}.")
print(f"This is the ID for name_again: {id(name_again)}.")
print(f"This is the result of testing name == 'Joey': {name == "Joey"}.")
print(f"This is the result of testing name == name_again: {name == name_again}.")
print(f"This is the result of testing name is 'Joey': {name is "Joey"}.")
print(f"This is the result of testing name is name_again: {name is name_again}.")
name_again = name
print(f"Now we will rerun some of the tests after setting name_again = name. For name; Value: {name}. ID: {id(name)}. Is name == name_again? {name == name_again}. What is the result of 'name is name_again'? {name is name_again}.")

#2. Try to use the is operator or the id function to investigate the difference between this:
# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# And this:
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(f"Testing before append. The ID for numbers is {id(numbers)}. The ID for new_numbers is {id(new_numbers)}. The result of 'numbers is new_numbers' is {numbers is new_numbers}.")
numbers.append(5)
print(f"Testing after append. The ID for numbers is {id(numbers)}. The ID for new_numbers is {id(new_numbers)}. The result of 'numbers is new_numbers' is {numbers is new_numbers}.")

#3. Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
user_number = int(input("Please enter a number: "))
if user_number > 0:
    print("Looks like a positive number.")
elif user_number == 0:
    print("Nothing but a zero, is it?")
else:
    print("Well if it isn't positive, and it isn't nothing, then it has to be less than nothing. Why so negative?")

#4. Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours
# the employee worked this week, as well as the hourly wage for this employee. If the employee worked more than
# 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount
# due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
# In effect, the employees get paid 110% of their hourly wage for any overtime.
hours_worked = int(input("How many hours did the contractor work this week? Hours: "))
hourly_wage = int(input("What is the hourly rate for this contractor? Rate: "))
if hours_worked > 40:
    print(f"It looks like the contractor is owed overtime. They worked {hours_worked} hours this week. That is {hours_worked - 40} hours overtime at 110% pay. The total amount owed after overtime is ${int((hours_worked - 40) * hourly_wage * 1.10) + int(40 * hourly_wage)}.")
else:
    print(f"The contractor worked a total of {hours_worked} hours this week. They are to be paid at their normal rate. The total owed is ${hours_worked * hourly_wage}.")