import re

def add(string):
    total = 0
    numbers = re.split("[,\n]",string)
    for number in numbers:
        if number != "" and int(number) <= 1000:
            total += int(number)
    return total
