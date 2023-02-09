
def next_cube():
    acc = 1

    while True:
        yield acc ** 3
        acc += 1



count = 1
for num in next_cube():
    if count > 15:
        break
    print(num)
    count += 1