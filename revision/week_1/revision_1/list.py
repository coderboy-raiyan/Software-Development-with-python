cinema_halls = []

rows, cols = (3, 4)

hall = {}

# again in this new array lets change
# the first element of the first row
# to 1 and print the array


def create_cinema(name, movie_name, hall_number):
    hall_cinema = {"name": name,
                   "movie_name": movie_name, "hall_num": hall_number}
    cinema_halls.append(hall_cinema)


def book_seat(row, col, number):
    if (hall[str(number)]):
        hall[str(number)][row-1][col-1] = 1
    else:
        hall["333"] = [[0 for i in range(cols)] for j in range(rows)]

        hall[str(number)][row-1][col-1] = 1


create_cinema("Star cineplex", "Jawan", "333")
create_cinema("Star", "Spider", "555")
print(cinema_halls)

book_seat(2, 2, "333")

for slots in hall["333"]:
    print(slots)
