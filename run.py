import random
from imdb import Cinemagoer


ia = Cinemagoer()


def get_random_movies(list, count=20):
    random_indexes = random.sample(range(0, len(list)), count)
    return [list[index] for index in random_indexes]


def get_does_user_like_movie(movie):
    title = movie.data["title"]
    year = movie.data["year"]
    answer = input(f"[{year}] {title} \n")
    while answer != "y" and answer != "n":
        answer = input(f"Please answer with y or n. Do you like: [{year}] {title} \n")
    return answer == "y"


def get_genres_of_movie(movie):
    movie_info = ia.get_movie(movie.movieID)
    genres = movie_info["genres"]
    return genres


def suggest_movies(liked_genres, liked_movies_count):
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
        print(genre_movie.data["title"])


def start_game():
    """
    Game logic
    """
    movies = ia.get_top250_movies()
    random_movies = get_random_movies(movies)
    input(
        "You will be asked with [year] movie. Answer with y if you know and like the movie, answer with n otherwise. Press return to continue\n"
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
