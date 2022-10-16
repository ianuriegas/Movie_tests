import csv
import random
from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie


class data:
    def __init__(self, rand_int, arr):
        self.rand_int = rand_int
        self.arr = arr

    def get_popularity(self, rand_int, arr):
        movie = Movie()

        index = arr[rand_int][0]
        movie_one_details = movie.details(index)
        movie_one_name = movie_one_details.title
        search_one = movie.search(movie_one_name)
        first_result = search_one[0]
        movie_one_details.popularity
        return


def read_csv():
    arr = []
    with open('movieid.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            arr.append(row)

    return arr


def main():
    arr = read_csv()

    USERNAME = "ianuriegas"
    PASSWORD = "ianuriegas"

    tmdb = TMDb()
    tmdb.api_key = "1654c8831978acecdf4a44c904d790ff"

    # auth = Authentication(username=USERNAME, password=PASSWORD)

    # account = Account()
    # details = account.details()

    # print("You are logged in as %s. Your account ID is %s." % (details.username, details.id))
    # print("This session expires at: %s" % auth.expires_at)

    movie = Movie()

    d = data()



    rand_int_one = random.randint(0, len(arr))
    rand_int_two = random.randint(0, len(arr))
    rand_int_three = random.randint(0, len(arr))
    rand_int_four = random.randint(0, len(arr))

    i = arr[rand_int_one][0]
    movie_one_details = movie.details(i)
    movie_one_name = movie_one_details.title
    search_one = movie.search(movie_one_name)
    first_result = search_one[0]
    print("\n")
    print("POPULARITY: ", movie_one_details.popularity)

    j = arr[rand_int_two][0]
    movie_two_details = movie.details(j)
    movie_two_name = movie_two_details.title
    search_two = movie.search(movie_two_name)
    second_result = search_two[0]
    print("\n")
    print("POPULARITY: ", movie_two_details.popularity)

    h = arr[rand_int_three][0]
    movie_three_details = movie.details(h)
    movie_three_name = movie_three_details.title
    search_three = movie.search(movie_three_name)
    third_result = search_three[0]
    print("\n")
    print("POPULARITY: ", movie_three_details.popularity)

    k = arr[rand_int_four][0]
    movie_four_details = movie.details(k)
    movie_four_name = movie_four_details.title
    search_four = movie.search(movie_four_name)
    fourth_result = search_four[0]
    print("\n")
    print("POPULARITY: ", movie_four_details.popularity)

    print("\n")

    if movie_one_details.popularity >= movie_two_details.popularity and movie_one_details.popularity >= movie_three_details.popularity and movie_one_details.popularity >= movie_four_details.popularity:
        # print(first_result.title)
        answer = "A"
    elif movie_two_details.popularity >= movie_one_details.popularity and movie_two_details.popularity >= movie_three_details.popularity and movie_two_details.popularity >= movie_four_details.popularity:
        # print(second_result.title)
        answer = "B"
    elif movie_three_details.popularity >= movie_one_details.popularity and movie_three_details.popularity >= movie_two_details.popularity and movie_three_details.popularity >= movie_four_details.popularity:
        answer = "C"
    else:
        answer = "D"

    print("Which movie is more popular?\n"
          + "A for", first_result.title + "\n"
          + "B for", second_result.title + "\n"
          + "C for", third_result.title + "\n"
          + "D for", fourth_result.title + "\n")

    input_ans = input("Enter Choice: ")

    if input_ans == answer:
        print("You chose correctly :)")
    else:
        print("Wrong dummy")


if __name__ == "__main__":
    main()
