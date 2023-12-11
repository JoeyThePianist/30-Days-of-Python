#1. Create a movies list containing a single tuple. The tuple should contain a movie title,
# the director’s name, the release year of the movie, and the movie’s budget.
movies =[
    ("Unleashed", "Louis Leterrier", 2005, "$45,000,000"),
]

#2. Use the input function to gather information about another movie. You need a title,
# director’s name, release year, and budget.
movie_title = input("Hi there! We are collecting information on people's favorite movies! What's the name of your favorite movie? ")
movie_director = input("Who directed this movie? ")
movie_release = input("What year was this movie released? ")
movie_budget = input("What was the budget of this movie? ")

#3. Create a new tuple from the values you gathered using input. Make sure they’re in the same
# order as the tuple you wrote in the movies list.
movie = (movie_title, movie_director, movie_release, movie_budget),

#4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"So, your favorite movie is {movie[0][0]} and it was released in {movie[0][2]}? Neat!")

#5. Add the new movie tuple to the movies collection using append.
movies.append(movie)

#6. Print both movies in the movies collection.
print(movies[0])
print(movies[1])

#7. Remove the first movie from movies. Use any method you like.
del movies[0]
