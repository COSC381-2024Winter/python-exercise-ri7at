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

#print statement and function
if choice == 'q':
            print("Exiting the program.")
            break
 elif choice == 'list':#list the movies
   #placeholder for funtions
 #search the movies   
 elif choice == 'search':
      term = input("Enter the name of the movie to search for: ")
      #placeholder for funtions
.....








if __name__ == "__main__":
    main()
  
movies = Movies('./movies.txt')
