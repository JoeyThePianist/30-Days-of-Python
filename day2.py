#1. Ask the user for their name and age, assign theses values to two variables, 
# and then print them.
name = None
age = None
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"You are {name} and you are {age} years old.")

#2. Investigate what happens when you try to assign a value to a variable that
# you’ve already defined. Try printing the variable before and after you reuse
# the name.
print(name)
name = "Vincent"
print(name)

#3. Below you’ll find some code with a number of errors. Try to go through the
# program line by line and fix the issues in the code. I’d encourage you to try
# running the program while you’re working on it, as reading the error messages
# is great practice for debugging your own programs.

#ERROR CODE: hourly_wage = input("Please enter your hourly wage: ')
#ERROR CODE: 
#ERROR CODE: prnt("Hourly wage: ")
#ERROR CODE: print(hourlywage)
#ERROR CODE: print("Hours worked: ")
#ERROR CODE: print(hours_worked)
#ERROR CODE: 
#ERROR CODE: hours_worked = input("How many hours did you work this week? ")

# Corrected code;
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("Please enter the amount of hours worked this week: ")
weekly_pay = int(hourly_wage) * int(hours_worked) # Extra code
#print("Hourly wage: ")
#print(hourly_wage)
#print("Hours worked: ")
#print(hours_worked)
# Using printf for results;
print(f"You make ${hourly_wage} per hour and you worked {hours_worked}hours this week. Before taxes, you may expect ${weekly_pay} on your next weekly paycheck. Thank you for your time {name}!")