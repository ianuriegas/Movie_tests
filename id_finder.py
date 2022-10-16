import random

from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

# This file is only used to find id numbers because we can just generate
# random ones normally, it'll error, but just keep running it

USERNAME = "ianuriegas"
PASSWORD = "ianuriegas"

tmdb = TMDb()
tmdb.api_key = "1654c8831978acecdf4a44c904d790ff"

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()


with open('movieid.csv', 'a') as f:
    while True:
        rand_int_one = random.randint(0, 800000)
        movie = Movie()
        movie_one_details = movie.details(rand_int_one)
        # print(rand_int_one)
        movie_one_name = movie_one_details.title
        search_one = movie.search(movie_one_name)
        first_result = search_one[0]
        # first_result = search_one[0]
        print("\n")
        print("POPULARITY: ", movie_one_details.popularity)
        print("ID: ", first_result.id)
        print("TITLE: ", first_result.title)
        print("OVERVIEW: ", first_result.overview)
        print("POSTER PATH: ", first_result.poster_path)
        print("VOTE AVERAGE: ", first_result.vote_average)
        print("\n")
        print("ID: ", first_result.id)
        f.write(str(first_result.id)+"\n")