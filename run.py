from imdb import Cinemagoer


ia = Cinemagoer()

results = ia.search_movie("harry potter")
for result in results:
    print(result.data["title"])
