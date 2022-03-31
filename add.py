def add(string):
    total = 0
    numbers = string.split(",")
    for number in numbers:
        if number != "":
            total += int(number)
    return total