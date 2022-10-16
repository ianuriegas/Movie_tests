import csv

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

watchlist = []
with open('watchlist.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        # print(row)
        watchlist.append(row)

print(watchlist)
movie = Movie()

while True:
    new_movie = input("Enter a movie to add: ")
    search_one = movie.search(new_movie)
    first_result = search_one[0]
    # print([first_result.title])
    if [first_result.title] in watchlist:
        print("That movies already in the watchlist")
    else:
        watchlist.append([first_result.title])
        if len(watchlist) == 0:
            with open('watchlist.csv', 'w') as fd:
                fd.write(str(first_result.title)+"\n")
        else:
            with open('watchlist.csv', 'a') as fd:
                fd.write(str(first_result.title)+"\n")
