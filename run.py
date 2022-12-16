import random
from imdb import Cinemagoer


ia = Cinemagoer()



def start_game():
    """
    Game logic
    """
    movies = ia.get_top250_movies()
    random_indexes = random.sample(range(0, len(movies)), 3)
    input("You will be asked with [year] movie. Answer with y if you know and like the movie, answer with n otherwise. Press return to continue\n")
    liked_movies_count = 0
    liked_genres = dict()
    for index in random_indexes:
        movie = movies[index]
        title = movie.data['title']
        year = movie.data['year']
        answer = input(f"[{year}] {title} \n")
        while answer != "y" and answer != "n":
            answer = input(f"Please answer with y or n. Do you like: [{year}] {title} \n")
        if answer == "y":
            print("Adding genres to your list, please wait...\n")
            liked_movies_count += 1
            movie_info = ia.get_movie(movie.movieID)
            genres = movie_info['genres']
            for genre in genres:
                liked_genres[genre] = liked_genres.get(genre, 0) + 1
    print(f"\You liked {liked_movies_count} movies.")
    print("Your favorite genres:")
    print(liked_genres)
        

def main():
    """
    Runs the program flow.
    """
    start_game()
    

main()