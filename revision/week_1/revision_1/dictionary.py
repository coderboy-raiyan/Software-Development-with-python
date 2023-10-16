cinema_halls = [{"name": "Star cineplex", "movie": "Jawan", "hall_num": 333}]

for item in cinema_halls:
    for jk, ik in item.items():
        print(jk, ": ", ik)

for i, k in enumerate(cinema_halls):
    print(i, k)
