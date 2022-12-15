import random
from imdb import Cinemagoer


ia = Cinemagoer()


def start_game():
    movies = ia.get_top250_movies()
    random_indexes = random.sample(range(0, len(movies)), 20)
    print(random_indexes)
    for index in random_indexes:
        movie = movies[index]
        print(movie.data)
        #movie_info = ia.get_movie(movie.movieID)
        #print(movie_info['genres'])


def main():
    """
    Runs the program flow.
    """
    start_game()
    

main()