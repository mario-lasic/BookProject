from data import root, genres, sub_genres

def startup():
    print("Hello and welcome to the book recomendation program! \n")

def choices():
    genre = ""
    choice = ""
    print("What genre would you like to see? \n")
    while True:

        genre = input(f"Here is list of possible genre: {genres} \n")
        if genre not in genres:
            print("Not on the list!")
        else: 
            break
    
    sub_genre = input(f"Would you like see and choose from sub geners\n Y'\'N: ")
    if sub_genre.lower() == 'y':
        while True:
            choice = input(f"Please choose from the following list {sub_genres[genre]} \n")
            if choice not in sub_genres[genre]:
                print("Not on the list!")
            else:
                break

    return genre, choice


def recomedations():
    pass

startup()
choices()
