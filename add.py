import re

def add(string):
    total = 0
    numbers = re.split("[,\n]",string)
    for number in numbers:
        if number != "":
            total += int(number)
    return total
