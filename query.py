from movies import Movies

# Task 1: creating a menu
def display_menu():
    print("\nMenu:")
    print("* enter 'q' for exit.")
    print("* enter 'list' for listing all the movie names.")
    print("* enter 'search' for searching movies.")
    print("* enter 'cast' for searching cast.")

# Complete function for listing the movies
def list_movies(movies_instance):
    movies_list = movies_instance.list_all()
    for index, movie in enumerate(movies_list, 1):
        print(f"{index}. {movie}")

# Complete function for searching the movies
def search_movies(movies_instance, search_term):
    results = movies_instance.search_by_title(search_term)
    if results:
        for movie in results:
            print(movie)
    else:
        print("No results found.")

# Complete function for searching movie by the cast
def search_cast(movies_instance, search_term):
    results = movies_instance.search_by_actor(search_term)
    if results:
        for movie, actors in results:
            matching_actors = [actor for actor in actors if search_term.lower() in actor.lower()]
            print(movie)
            print(matching_actors)
    else:
        print("No results found.")

def main():
    movies_instance = Movies('./movies.txt')
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice == 'list':  # List the movies
            list_movies(movies_instance)
        elif choice == 'search':  # Search the movies
            term = input("Enter the name of the movie to search for: ")
            search_movies(movies_instance, term)
        elif choice == 'cast':  # Search by cast
            term = input("Enter the name of the actor to search for: ")
            search_cast(movies_instance, term)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
