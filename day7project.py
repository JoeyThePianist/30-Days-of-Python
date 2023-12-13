# Below you'll find a list which contains the relevant data about a selection of movies.
# Each item in the list is a tuple containing a movie name and movie budget in that order:
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
#4. SOLUTION
add_movie_count = int(input("You want to add some new movies to the list? Cool. How many? "))

for x in range(add_movie_count):
    name = input(f"Please enter the name for movie {x + 1}: ").title().strip()
    budget = int(input(f"What was the budget for this movie? Only numbers are necessary here! "))
    new_movie = (name, budget)
    movies.append(new_movie)

# For this project, your program should do the following:
#1. Calculate the average budget of all movies in the data set.
average_budget = 0

for movie in movies:
    average_budget += movie[1]

average_budget /= len(movies)

#2. Print out every movie that has a budget higher than the average you calculated. You should
# also print out how much higher than the average the movie's budget was.
above_average_budget = 0

for movie in movies:
    if movie[1] > average_budget:
        print(f"The movie {movie[0]} had a higher budget than average. It was ${movie[1] - average_budget:,.2f} higher!")
        above_average_budget += 1
        
#3. Print out how many movies spent more than the average you calculated.
print(f"Out of {len(movies)} movies, there were a total of {above_average_budget} movies that had a budget above the average.")

#4. If you want a little extra challenge, allow users to add more movies to the data set before
# running the calculations.
# You can do this by asking the user how many movies they want to add, which will allow you to
# use a for loop and range to repeat some code a given number of times. Inside the for loop, you
# can write some code that takes in some user input and appends a movie tuple containing the
# collected data to the movie list.