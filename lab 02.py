#lab 02
#fizz buzz game


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example:
n = int(input("Enter the number to play Fizz Buzz up to: "))
fizz_buzz(n)




#task 02

# Movie dataset
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Function to calculate average budget
def calculate_average_budget(movies):
    total_budget = sum(budget for _, budget in movies)
    return total_budget / len(movies)

# Function to print movies with budget higher than average
def high_budget_movies(movies):
    average_budget = calculate_average_budget(movies)
    print(f"Average budget: ${average_budget:,.2f}\n")

    count = 0
    for movie, budget in movies:
        if budget > average_budget:
            count += 1
            difference = budget - average_budget
            print(f"{movie}: ${budget:,.2f} (Higher by ${difference:,.2f})")
    
    print(f"\nNumber of movies with a higher budget than the average: {count}")

# Function to allow user to add new movies
def add_movies():
    num = int(input("How many movies would you like to add? "))
    for _ in range(num):
        name = input("Enter the movie name: ")
        budget = int(input(f"Enter the budget for {name}: "))
        movies.append((name, budget))

# Example:
add_movies()
high_budget_movies(movies)

