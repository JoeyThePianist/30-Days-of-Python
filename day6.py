#1. Below we've provided a list of tuples, where each tuple contains
# details about an employee of a shop: their name, the number of hours
# worked last week, and their hourly rate. Print how much each employee
# is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

employee_count = len(employees)
hourly_average = 0

for employee in employees:
#   employee_count += 1
    hourly_average += employee[2]
    weekly_pay = employee[2] * employee[1]
    print(f"{employee[0]} worked {employee[1]} hours this week. Their paycheck for the week should be ${weekly_pay:.2f}.")


#2. For the employees above, print out those who are earning an hourly
# wage above average.
# Hint: you can use a for loop and two variables to keep track of the
# total wage and the number of employees. Then, use the two variables
# to calculate the average. Finally, add another loop that goes through
# the employees list again and prints out only those who have an hourly
# wage above the calculated average.
hourly_average /= employee_count
print(f"This is the hourly average: ${hourly_average:.2f}")

for employee in employees:
    if employee[2] > hourly_average:
        print(f"{employee[0]} makes above the average hourly wage! Their wage is ${employee[2]:.2f}/hour.")
    elif employee[2] == hourly_average:
        print(f"{employee[0]} makes exactly the average hourly wage.")
    else:
        print(f"{employee[0]} makes less than the average hourly wage at only ${employee[2]:.2f}/hour. We should consider giving them a raise.")

    