import random
from imdb import Cinemagoer


ia = Cinemagoer()


def get_random_movies(list, count=20):
    random_indexes = random.sample(range(0, len(list)), count)
    return [list[index] for index in random_indexes]


def get_does_user_like_movie(movie):
    title = movie.data['title']
    year = movie.data['year']
    answer = input(f"[{year}] {title} \n")
    while answer != "y" and answer != "n":
        answer = input(f"Please answer with y or n. Do you like: [{year}] {title} \n")
    return answer == "y"


def get_genres_of_movie(movie):
    movie_info = ia.get_movie(movie.movieID)
    genres = movie_info['genres']
    return genres


def start_game():
    """
    Game logic
    """
    movies = ia.get_top250_movies()
    random_movies = get_random_movies(movies)
    input("You will be asked with [year] movie. Answer with y if you know and like the movie, answer with n otherwise. Press return to continue\n")
    liked_movies_count = 0
    liked_genres = dict()
    for movie in random_movies:
        if get_does_user_like_movie(movie):
            liked_movies_count += 1
            print("Adding genres to your list, please wait...\n")
            genres = get_genres_of_movie(movie)
            for genre in genres:
                liked_genres[genre] = liked_genres.get(genre, 0) + 1
    print(f"\nYou liked {liked_movies_count} movies.")
    print("Your favorite genres:")
    print(liked_genres)


def main():
    """
    Runs the program flow.
    """
    start_game()
    

main()