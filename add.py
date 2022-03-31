def add(string):
    if string == "":
        return 0
    if "," in string:
        numbers = string.split(",")
        return int(numbers[0]) + int(numbers[1])
    return int(string)