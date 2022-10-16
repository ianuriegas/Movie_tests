import csv

from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = "1654c8831978acecdf4a44c904d790ff"

movie = Movie()


class Data:
    def __init__(self, watchlist):
        self.watchlist = watchlist

    def add_movie(self, new_movie):
        search_one = movie.search(new_movie)
        first_result = search_one[0]
        # print([first_result.title])
        if [first_result.title] in self.watchlist:
            print("That movies already in the watchlist")
        else:
            self.watchlist.append([first_result.title])
            if len(self.watchlist) == 0:
                with open('watchlist.csv', 'w') as fd:
                    fd.write(str(first_result.title) + "\n")
            else:
                with open('watchlist.csv', 'a') as fd:
                    fd.write(str(first_result.title) + "\n")

    def remove_movie(self, movie_to_remove):
        search_one = movie.search(movie_to_remove)
        first_result = search_one[0]
        print([first_result.title])
        if [first_result.title] in self.watchlist:
            self.watchlist.remove([first_result.title])
            with open('watchlist.csv', 'w') as fd:
                for i in range(0, len(self.watchlist)):
                    fd.write(str(self.watchlist[i][0]) + "\n")
        else:
            print("Movie is not in there")


def main():
    watchlist = []
    with open('watchlist.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            watchlist.append(row)

    while True:
        d = Data(watchlist)
        user_in = input("Options:\n"
                        "A - Add\n"
                        "R - Remove\n"
                        "L - List\n"
                        "Q - Quit\n")
        if user_in == "A":
            movie_to_add = input("Enter movie to add: ")
            d.add_movie(movie_to_add)
        elif user_in == "R":
            movie_to_remove = input("Enter movie to remove: ")
            d.remove_movie(movie_to_remove)
        elif user_in == "L":
            for i in range(0, len(watchlist)):
                print(watchlist[i][0])
        elif user_in == "Q":
            break
        else:
            print("Read Dummy")


if __name__ == "__main__":
    main()
