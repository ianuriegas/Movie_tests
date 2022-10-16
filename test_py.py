import random

from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

USERNAME = "ianuriegas"
PASSWORD = "ianuriegas"

tmdb = TMDb()
tmdb.api_key = "1654c8831978acecdf4a44c904d790ff"

auth = Authentication(username=USERNAME, password=PASSWORD)

account = Account()
details = account.details()

print("You are logged in as %s. Your account ID is %s." % (details.username, details.id))
print("This session expires at: %s" % auth.expires_at)


rand_int_one = random.randint(0, 100000)
rand_int_two = random.randint(0, 100000)

# general movie constructor
movie = Movie()

# gets movie details of ranodm int
success = False
finish = 0
while not success:
    try:
        movie_one_details = movie.details(rand_int_one)
        print(rand_int_one)
        movie_one_name = movie_one_details.title
        search_one = movie.search(movie_one_name)
        # print("TITLE: ", movie_one_details.title)
        first_result = search_one[0]
        print("\n")
        print("POPULARITY: ", movie_one_details.popularity)
        print("ID: ", first_result.id)
        print("TITLE: ", first_result.title)
        print("OVERVIEW: ", first_result.overview)
        print("POSTER PATH: ", first_result.poster_path)
        print("VOTE AVERAGE: ", first_result.vote_average)
        finish = finish + 1
        success = True
    except:
        pass

# gets movie details of ranodm int
success = False
while not success:
    try:
        movie_two_details = movie.details(rand_int_two)
        print(rand_int_two)

        # movie_two_details = movie.details(rand_int_two)

        movie_two_name = movie_two_details.title
        search_two = movie.search(movie_two_name)
        second_result = search_two[0]
        print("\n")
        print("POPULARITY: ", movie_two_details.popularity)
        print("ID: ", second_result.id)
        print("TITLE: ", second_result.title)
        print("OVERVIEW: ", second_result.overview)
        print("POSTER PATH: ", second_result.poster_path)
        print("VOTE AVERAGE: ", second_result.vote_average)
        finish = finish + 1
        success = True
    except:
        pass

print("\n")
if movie_one_details.popularity <= movie_two_details.popularity:
    print(second_result.title)

else:
    print(first_result.title)
