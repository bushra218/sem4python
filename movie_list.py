FILENAME="movies.txt"
def write_movies(movies):
    with open(FILENAME,"w") as file:
        for movie in movies:
            file.write(movie+"\n")

def read_movies():
    movies=[]
    with open(FILENAME) as file:
        for line in file:
            line=line.replace("\n","")
            movies.append(line)
    return movies

def list_movies(movies):
    for i in range(len(movies)):
        movie=movies[i]
        print(str(i+1)+" . " + movie)
    print()

def add_movie(movies):
    movie=input("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(movie + " was added. \n")

def delete_movie(movies):
    index=int(input("Number: "))
    movie=movies.pop(index-1)
    write_movies(movies)
    print(movie + " was deleted. \n")

def display_menu():
    print("The movie List Program")
    print()
    print("COMMAND MENU")
    print("List-- List all movies")
    print("add-- Add a movie")
    print("del -- Delete a movie")
    print("exit-- exit a program")
    print()

def main():
    display_menu()
    movies=read_movies()
    while True:
        command = input("command  : ")
        if command=="list":
            list_movies(movies)
        elif command=="add":
            add_movie(movies)
        elif command=="del":
            delete_movie(movies)
        elif command=="exit":
            print("Bye!")
            print("\nThank You \nName: Ansari Bushra \nUIN:231P046 \nRoll no:03 \n")

            break
        else:
            print(" Not a valid command please try again..")
if __name__=="__main__":
    main()

