"""
Application for receiving the liked movies from user
and suggest what to watch next.
"""
import random
from imdb import Cinemagoer


ia = Cinemagoer()


class MovieBasicInfo:
    """Class definition for movie"""
    def __init__(self, movie):
        self.title = movie.data["title"]
        self.year = movie.data["year"]


def get_random_movies(count=20):
    """
    Returns a random list of movies from top 250 IMDB movies.
    Parameters
    count: Number of random movies to return, default 20.
    """
    movies = ia.get_top250_movies()
    random_indexes = random.sample(range(0, len(movies)), count)
    return [movies[index] for index in random_indexes]


def does_user_like_movie(movie):
    """
    Helper function to ask if user likes the movie,
    parse the answer and return bool value.
    """
    movie_basic_info = MovieBasicInfo(movie)
    answer = input(f"> [{movie_basic_info.year}] {movie_basic_info.title} \n")
    while answer not in ["y", "n"]:
        answer = input(
            "Please answer with y or n. Do you like: "
            f"[{movie_basic_info.year}] {movie_basic_info.title} \n"
        )
    return answer == "y"


def get_genres_of_movie(movie):
    """
    Helper function to get genres of movie,
    by using Cinemagoer's get_movie function
    Returns a list of genre string
    """
    movie_info = ia.get_movie(movie.movieID)
    genres = movie_info["genres"]
    return genres


def suggest_movies(liked_genres):
    """
    Gets the top movies with liked_genres using Cinemagoer library,
    and prints them to the console as suggestions.
    """
    top_genres_dict = {
        k: v
        for k, v in sorted(
            liked_genres.items(), key=lambda item: item[1],
            reverse=True
        )
    }
    top_genres_list = [
        genre_item[0] for genre_item in list(top_genres_dict.items())[:3]
    ]
    print(
        f"""
----------------------------------------------------------------------
Your favorite genres are: {', '.join(top_genres_list)}
Here are some suggestions for you:
----------------------------------------------------------------------
"""
    )
    top_genre_movies = ia.get_top50_movies_by_genres(top_genres_list)
    for genre_movie in top_genre_movies[:10]:
        movie_basic_info = MovieBasicInfo(genre_movie)
        print(f"[{movie_basic_info.year}] {movie_basic_info.title}")


def get_liked_genres_with_movies(movies):
    """
    For each movie, ask users if they like the move,
    if yes, add genres to genres dictionary
    """
    liked_genres = {}
    for movie in movies:
        if does_user_like_movie(movie):
            print("* adding genres to your list, please wait...")
            genres = get_genres_of_movie(movie)
            for genre in genres:
                liked_genres[genre] = liked_genres.get(genre, 0) + 1
        print("")
    return liked_genres


def start_game():
    """
    Game logic
    """
    input(
        """
----------------------------------------------------------------------
Welcome! You will be asked with 20 random top 250 IMDB movies.
Answer with y if like the movie, answer with n otherwise.
Press ENTER/RETURN to continue.
----------------------------------------------------------------------\n"""
    )
    random_movies = get_random_movies()
    liked_genres = get_liked_genres_with_movies(random_movies)
    suggest_movies(liked_genres)


def main():
    """Starts the game."""
    start_game()
    answer = input("\nDo you want to try again? (y/n): ")
    if answer == "y":
        main()


main()
