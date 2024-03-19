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

#print statement and function
if choice == 'q':
            print("Exiting the program.")
            break
 elif choice == 'list':#list the movies
    list_movies(movies_instance)
 #search the movies   
 #search by cast
.....








if __name__ == "__main__":
    main()
  
movies = Movies('./movies.txt')
