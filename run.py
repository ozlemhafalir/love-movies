import random
from imdb import Cinemagoer


ia = Cinemagoer()


class MovieBasicInfo:
    """Class definition for movie"""

    def __init__(self, movie):
        self.title = movie.data["title"]
        self.year = movie.data["year"]


def get_random_movies(list, count=20):
    """
    From a given list of movies, returns a random list.
    Parameters
    list: Source list
    count: Number of random movies to return, default 20.
    """
    random_indexes = random.sample(range(0, len(list)), count)
    return [list[index] for index in random_indexes]


def get_does_user_like_movie(movie):
    """Helper function to ask if user likes the movie, parse and return boolean value."""
    movie_basic_info = MovieBasicInfo(movie)
    answer = input(f"[{movie_basic_info.year}] {movie_basic_info.title} \n")
    while answer != "y" and answer != "n":
        answer = input(
            f"Please answer with y or n. Do you like: [{movie_basic_info.year}] {movie_basic_info.title} \n"
        )
    return answer == "y"


def get_genres_of_movie(movie):
    """Helper function to get genres of movie, by using Cinemagoer's get_movie function"""
    movie_info = ia.get_movie(movie.movieID)
    genres = movie_info["genres"]
    return genres


def suggest_movies(liked_genres, liked_movies_count):
    """
    Gets the top movies with liked_genres using Cinemagoer library. And prints them to the console as suggestions.
    """
    top_genres_dict = {
        k: v
        for k, v in sorted(liked_genres.items(), key=lambda item: item[1], reverse=True)
    }
    top_genres_list = [
        genre_item[0] for genre_item in list(top_genres_dict.items())[:3]
    ]
    print(
        f"\nYou liked {liked_movies_count} movies. Your favorite genres are: {', '.join(top_genres_list)}"
    )
    top_genre_movies = ia.get_top50_movies_by_genres(top_genres_list)
    print("\nHere are some suggestions for you")
    for genre_movie in top_genre_movies[:10]:
        movie_basic_info = MovieBasicInfo(genre_movie)
        print(f"[{movie_basic_info.year}] {movie_basic_info.title}")


def start_game():
    """
    Game logic
    """
    movies = ia.get_top250_movies()
    random_movies = get_random_movies(movies)
    input(
        """
        ----------------------------------------------------------------------
        Welcome! You will be asked with [year] movie.
        Answer with y if you know and like the movie, answer with n otherwise.
        Press return to continue.
        ----------------------------------------------------------------------
        \n\n
        """
    )
    liked_movies_count = 0
    liked_genres = dict()
    for movie in random_movies:
        if get_does_user_like_movie(movie):
            liked_movies_count += 1
            print("Adding genres to your list, please wait...\n")
            genres = get_genres_of_movie(movie)
            for genre in genres:
                liked_genres[genre] = liked_genres.get(genre, 0) + 1
    suggest_movies(liked_genres, liked_movies_count)


def main():
    """
    Runs the program flow.
    """
    start_game()


main()
