import re

def add(string):
    if string == "":
        return 0
    total = 0
    negativeList = []
    delimiter = ","
    if string[0] == "/":
        delimiter = string[2]
        string = string[4:]
    numbers = re.split(f"[{delimiter}\n]",string)
    for number in numbers:
        if int(number) <= 1000:
            total += int(number)
            if int(number) < 0:
                negativeList.append(number)
    if negativeList != []:
        raise ValueError(f'Negatives not allowed: {",".join(negativeList)}')
    return total