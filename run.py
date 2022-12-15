from imdb import Cinemagoer


ia = Cinemagoer()


def start_game():
    movies = ia.get_top250_movies()
    for movie in movies:
        print(movie.data)
        movie_info = ia.get_movie(movie.movieID)
        print(movie_info['genres'])


def main():
    """
    Runs the program flow.
    """
    start_game()
    

main()