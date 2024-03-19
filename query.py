from movies import Movies
#task 1: creating a menu

def display_menu():
  movies_instance = Movies('./movies.txt')
   while True:
        display_menu()
    print("\nMenu:")
    print("* enter 'q' for exit.")
    print("* enter 'list' for listing all the movie names.")
    print("* enter 'search' for searching movies.")
    print("* enter 'cast' for searching cast.")

#complete function for listing the movide
def list_movies(movies_instance):
    movies_list = movies_instance.list_all()
    for index, movie in enumerate(movies_list, 1):
        print(f"{index}. {movie}")

#complete function for searching the movies
def search_movies(movies_instance, search_term):
    results = movies_instance.search_by_title(search_term)
    if results:
        for movie in results:
            print(movie)
    else:
        print("No results found.")
#print statement and function

if choice == 'q':
            print("Exiting the program.")
            break
 elif choice == 'list':#list the movies
    list_movies(movies_instance)
 elif choice == 'search':
            term = input("Enter the name of the movie to search for: ")
            search_movies(movies_instance, term)
 #search the movies   
 #search by cast
.....








if __name__ == "__main__":
    main()
  
movies = Movies('./movies.txt')
