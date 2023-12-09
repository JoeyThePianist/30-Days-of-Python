age = 34
jan_days = 31
feb_days = 28
mar_days = 31
apr_days = 30
may_days = 31
jun_days = 30
jul_days = 31
aug_days = 31
sep_days = 30
oct_days = 31
nov_days = 30
dec_days = 31
days_per_year = jan_days + feb_days + mar_days + apr_days + may_days + jun_days + jul_days + aug_days + sep_days + oct_days + nov_days + dec_days
weeks_per_year = 52
months_per_year = 12
r = 5
area = 3.141 * (r*r)
# This is included to show the functionality of pow(the first number is what is being multiplied, the 2nd is the exponent so 5 to the power of 2)
area = 3.141 * pow(5, 2)

#1. Print your age to the console.
print(f"I am {age} years old.")

#2. Calculate and print the number of days, weeks, and months in 27 years. 
# Don’t worry about leap years!
print(f"There are {days_per_year * 27} days, {weeks_per_year * 27} weeks, or {months_per_year * 27} months in 27 years.")

#3. Calculate and print the area of a circle with a radius of 5 units. 
# You can be as accurate as you like with the value of pi.
print(f"The area of a circle with a radius of 5 units is {area}.")