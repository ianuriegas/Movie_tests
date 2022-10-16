import csv
import random
from tmdbv3api import Account
from tmdbv3api import Authentication
from tmdbv3api import TMDb, Movie

movie = Movie()


class Data:
    # movie = Movie()
    def __init__(self, rand_int, arr):
        self.rand_int = rand_int
        self.arr = arr

    def get_title(self):
        index = self.arr[self.rand_int][0]
        movie_one_details = movie.details(index)
        title = movie_one_details.title
        return title

    def get_popularity(self):
        index = self.arr[self.rand_int][0]
        movie_one_details = movie.details(index)
        popularity = movie_one_details.popularity
        return popularity


def read_csv():
    arr = []
    with open('movieid.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            arr.append(row)

    return arr


def main():
    arr = read_csv()

    tmdb = TMDb()
    tmdb.api_key = "1654c8831978acecdf4a44c904d790ff"

    rand_int_one = random.randint(0, len(arr))
    rand_int_two = random.randint(0, len(arr))
    rand_int_three = random.randint(0, len(arr))
    rand_int_four = random.randint(0, len(arr))

    movie_num_one = Data(rand_int_one, arr)
    one_title = movie_num_one.get_title()
    one_popularity = movie_num_one.get_popularity()
    print(one_popularity)

    movie_num_two = Data(rand_int_two, arr)
    two_title = movie_num_two.get_title()
    two_popularity = movie_num_two.get_popularity()
    print(two_popularity)

    movie_num_three = Data(rand_int_three, arr)
    three_title = movie_num_three.get_title()
    three_popularity = movie_num_three.get_popularity()
    print(three_popularity)

    movie_num_four = Data(rand_int_four, arr)
    four_title = movie_num_four.get_title()
    four_popularity = movie_num_four.get_popularity()
    print(four_popularity)

    if one_popularity >= two_popularity and one_popularity >= three_popularity and one_popularity >= four_popularity:
        answer = "A"
    elif two_popularity >= one_popularity and two_popularity >= three_popularity and two_popularity >= four_popularity:
        answer = "B"
    elif three_popularity >= one_popularity and three_popularity >= two_popularity and three_popularity >= four_popularity:
        answer = "C"
    else:
        answer = "D"

    print("Which movie is more popular?\n"
          + "A for", one_title + "\n"
          + "B for", two_title + "\n"
          + "C for", three_title + "\n"
          + "D for", four_title + "\n")

    input_ans = input("Enter Choice: ")

    if input_ans == answer:
        print("You chose correctly :)")
    else:
        print("Wrong dummy")


if __name__ == "__main__":
    main()
