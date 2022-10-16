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

movie = Movie()
movie_input = input("Input any movie that you would like recommendations for: ")
s = movie.search(movie_input)
first_result = s[0]
recommendations = movie.recommendations(first_result.id)

print("=============================================")
print("Getting recommendations for:", first_result.title)
for recommendation in recommendations:
    print("%s (%s)" % (recommendation.title, recommendation.release_date))
