def bigger(items):
    max = -1
    number_max = None
    print("items = ", items)
    for item in items:
        if items[item] > max:
            max = items[item]
            number_max = item
    return number_max


def most_frequent(numbers):
    check = {}

    for item in numbers:
        if item in check:
            check[item] += 1
        else:
            check[item] = 1

    return(bigger(check))


numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print("The most frequent is:", most_frequent(numbers))
